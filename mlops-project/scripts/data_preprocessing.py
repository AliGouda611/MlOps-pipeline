import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# Define file paths
raw_data_path = 'data/raw/dataset.csv'
processed_data_path = 'data/processed/'

# Load raw data
df = pd.read_csv(raw_data_path)

# Data preprocessing (e.g., filling missing values, encoding categorical features)
df.fillna(0, inplace=True)  # Example of filling missing values

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('target', axis=1))

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['target'], test_size=0.2, random_state=42)

# Save processed data
os.makedirs(processed_data_path, exist_ok=True)
pd.DataFrame(X_train).to_csv(os.path.join(processed_data_path, 'X_train.csv'), index=False)
pd.DataFrame(X_test).to_csv(os.path.join(processed_data_path, 'X_test.csv'), index=False)
pd.DataFrame(y_train).to_csv(os.path.join(processed_data_path, 'y_train.csv'), index=False)
pd.DataFrame(y_test).to_csv(os.path.join(processed_data_path, 'y_test.csv'), index=False)
