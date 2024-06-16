import tensorflow as tf
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import yaml

# Load config
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

# Load processed data
X_test = pd.read_csv(config['data']['processed_path'] + 'X_test.csv')
y_test = pd.read_csv(config['data']['processed_path'] + 'y_test.csv')

# Load the model
model = tf.keras.models.load_model(config['model']['saved_path'] + 'model.h5')

# Make predictions
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Print evaluation metrics
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
