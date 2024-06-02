
from fastapi import FastAPI, HTTPException
from typing import Optional

import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

model = tf.keras.models.load_model('models/model.keras')

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
    vec = pd.DataFrame([vec], columns=['f', 't', 'd', 'e'])
    vec = pd.concat([vec]*8*5*3*10, ignore_index=True)

    vec = pd.concat([df, vec], axis=1)

    scaler = StandardScaler()
    vec = scaler.fit_transform(vec)

    preds = model.predict(vec)
    best = preds.argmin(axis=1)

    result = pd.concat([df[best], preds[best]], axis=1)
    # result.columns = ['airline', 'num_code', 'stop_type', 'time_taken', 'price']

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)

# http://127.0.0.1:8000/calculate?a=10&b=5