
from fastapi import FastAPI, HTTPException
from typing import Optional

import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler

import json

time_taken_bins = {
    0: 'min: 50, max: 340',
    1: 'min: 345, max: 635',
    2: 'min: 640, max: 930',
    3: 'min: 935, max: 1225',
    4: 'min: 1230, max: 1515',
    5: 'min: 1520, max: 1810',
    6: 'min: 1815, max: 2105',
    7: 'min: 2110, max: 2400',
    8: 'min: 2425, max: 2670',
    9: 'min: 2750, max: 2990'
}

air_bins = {0: 'Air India', 1: 'AirAsia', 2: 'GO FIRST', 3: 'Indigo', 4: 'SpiceJet', 5: 'StarAir', 6: 'Trujet', 7: 'Vistara'}
city_bins = {0: 'Bangalore', 1: 'Chennai', 2: 'Delhi', 3: 'Hyderabad', 4: 'Kolkata', 5: 'Mumbai'}
stop_bins = {0: '1-stop', 1: '2+-stop', 2: 'non-stop'}


model = tf.keras.models.load_model('models/model.keras')
precalculated = pd.read_excel('data/mean.xlsx')

# 'airline', 'num_code', 'stop_type', 'time_taken', #brute force
pregenerated = []
for air in range(8):
    for code in range(5):
        for stop in range(3):
            for time in range(10):
                pregenerated.append([air, code, stop, time])

df = pd.DataFrame(pregenerated, columns=['airline', 'num_code', 'stop_type', 'time_taken'])

app = FastAPI()

# 'f', 't', 'd', 'e'
@app.get("/calculate")
def calculate(f: int, t: int, d: int, e: int):
    vec = [f, t, d, e]
    print(f"{vec=}")
    vec = pd.DataFrame([vec], columns=['f', 't', 'd', 'e'])
    vec = pd.concat([vec]*8*5*3*10, ignore_index=True)

    vec = pd.concat([df, vec], axis=1)

    scaler = StandardScaler()
    vec = scaler.fit_transform(vec)

    preds = model.predict(vec)
    best = preds.argmin(axis=0)
    # print(f"{best[0]=}")
    # print(f"{vec.shape=} {preds.shape=} {best.shape=}")

    # print(df.loc[best])
    # print(preds[best])

    # print()
    # print(df.loc[best].to_numpy())
    # print(df.loc[best].to_numpy().shape)
    # print(preds[best])
    # print(preds[best].shape)
    # print()

    result = np.concatenate((df.loc[best].to_numpy(), preds[best]), axis=1).flatten()

    # best = best[0]
    # preds = pd.DataFrame(preds[best])
    # result = pd.concat([df.loc[best], preds], axis=1)

    # result.columns = ['airline', 'num_code', 'stop_type', 'time_taken', 'price']
    # print(result.tolist())
    result = result.tolist()


    mean = precalculated[(precalculated[0] == t) & (precalculated[1] == f) & (precalculated[3] == e)]
    print(mean.to_numpy().shape)
    print(mean[4].to_numpy().astype('int').flatten().tolist())
    # mean = mean['B']

    # result = { 'price':42 }

    result =  {
        'airline': air_bins[int(result[0])],
        'stop_type': stop_bins[int(result[2])],
        'time_taken': time_taken_bins[int(result[3])],
        'price': int(result[4]),
        'mean': mean[4].to_numpy().astype('int').flatten().tolist()
    }

    print(json.dumps(result))
    return json.dumps(result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)

# http://127.0.0.1:8000/calculate?a=10&b=5