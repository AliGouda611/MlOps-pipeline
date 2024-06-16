import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import os
import yaml

# Load config
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

# Load processed data
X_train = pd.read_csv(config['data']['processed_path'] + 'X_train.csv')
y_train = pd.read_csv(config['data']['processed_path'] + 'y_train.csv')

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=config['training']['epochs'], batch_size=config['training']['batch_size'])

# Save the model
os.makedirs(config['model']['saved_path'], exist_ok=True)
model.save(os.path.join(config['model']['saved_path'], 'model.h5'))
