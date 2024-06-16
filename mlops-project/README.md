# MLOps Project

This project demonstrates a full MLOps pipeline for deploying deep neural networks.

## Project Structure

```plaintext
mlops-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   └── exploratory_data_analysis.ipynb
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── model_deployment.py
│
├── models/
│   ├── saved_model/
│
├── config/
│   └── config.yaml
│
├── tests/
│   ├── test_data_preprocessing.py
│   ├── test_model_training.py
│   └── test_model_evaluation.py
│
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.8+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AliGouda611/MlOps-pipeline.git
   cd mlops-project
   ```

2. Build and run Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Run tests:
   ```bash
   pytest tests/
   ```



## MLOps Pipeline

### 1. Data Preprocessing

The data preprocessing step involves loading raw data, cleaning, transforming, and normalizing it, then splitting it into training and testing sets.

- **Script:** `scripts/data_preprocessing.py`
- **Input:** Raw data (`data/raw/dataset.csv`)
- **Output:** Processed data (`data/processed/`)

To run data preprocessing:
```bash
python scripts/data_preprocessing.py


Model Training
The model training step involves defining a deep neural network, training it on the preprocessed data, and saving the trained model.

Script: scripts/model_training.py
Input: Processed training data (data/processed/X_train.csv, data/processed/y_train.csv)
Output: Trained model (models/saved_model/model.h5)
To train the model:

bash
Copy code
python scripts/model_training.py
3. Model Evaluation
The model evaluation step involves loading the trained model and evaluating its performance on the test data using various metrics.

Script: scripts/model_evaluation.py
Input: Processed test data (data/processed/X_test.csv, data/processed/y_test.csv), Trained model (models/saved_model/model.h5)
Output: Evaluation metrics (printed to console)
To evaluate the model:

bash
Copy code
python scripts/model_evaluation.py
4. Model Deployment
The model deployment step involves deploying the trained model as a REST API using FastAPI.

Script: scripts/model_deployment.py
Input: Trained model (models/saved_model/model.h5)
Output: Running REST API service
To deploy the model:

bash
Copy code
docker-compose up --build
Getting Started
Prerequisites
Docker
Docker Compose
Python 3.8+
Git
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd mlops-project
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure raw data is available in the data/raw/ directory.

Usage
Run data preprocessing:

bash
Copy code
python scripts/data_preprocessing.py
Train the model:

bash
Copy code
python scripts/model_training.py
Evaluate the model:

bash
Copy code
python scripts/model_evaluation.py
Deploy the model as a REST API:

bash
Copy code
docker-compose up --build
Testing
Automated tests are located in the tests/ directory. Use PyTest to run the tests.

bash
Copy code
pytest tests/
Configuration
Configuration settings are stored in config/config.yaml.

yaml
Copy code
data:
  raw_path: data/raw/
  processed_path: data/processed/

model:
  saved_path: models/saved_model/

training:
  epochs: 10
  batch_size: 32
  learning_rate: 0.001
Authors
[Ali Gouda]