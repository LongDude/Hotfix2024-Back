import pandas as pd

# excel_data = pd.ExcelFile(path)
df = pd.read_excel('data/mean.xlsx')

# df.info()

df = df[(df[4] > 0)]

# df.info()

X = df.drop(columns=[4])
y = df[4]

print(f"{X.shape=} {X=}")
X.info()
print(f"{y.shape=} {y=}")
y.info()


# exit()

import tensorflow as tf
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1)
])

model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.MeanSquaredError(), metrics=['mae'])
model.fit(X_train, y_train, epochs=30, validation_split=0.1, batch_size=1024, )

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
