import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Load the saved model
model = tf.keras.models.load_model('models/model.keras')

# Load new data for inference
new_data = pd.read_excel('data/train.xlsx')

# Extract features (assuming 'price' is not present in new data)
X_new = new_data.drop(columns=['price'])
print(X_new[0:5])
exit()

# Standardize the new data
scaler = StandardScaler()
# You should use the same scaler that was used during training
X_new = scaler.fit_transform(X_new)

# Make predictions with the loaded model
predictions = model.predict(X_new)

# Print predictions
print(predictions)
