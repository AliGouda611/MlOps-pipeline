from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import yaml

# Load config
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

# Load the model
model = tf.keras.models.load_model(config['model']['saved_path'] + 'model.h5')

# Initialize FastAPI
app = FastAPI()

class PredictRequest(BaseModel):
    data: list

@app.post('/predict')
def predict(request: PredictRequest):
    data = np.array(request.data)
    predictions = model.predict(data)
    return {'predictions': predictions.tolist()}

# Run the server using uvicorn
# In Dockerfile CMD: ["uvicorn", "scripts.model_deployment:app", "--host", "0.0.0.0", "--port", "5000"]
