#!/bin/bash

# Define the project structure
mkdir -p mlops-project/{data/{raw,processed},notebooks,scripts,models/saved_model,config,tests}

# Navigate into the project directory
cd mlops-project

# Create placeholder files with content where applicable
touch .gitignore README.md requirements.txt Dockerfile docker-compose.yml

# Create initial Python script files
touch scripts/{data_preprocessing.py,model_training.py,model_evaluation.py,model_deployment.py}

# Create initial Jupyter notebook
touch notebooks/exploratory_data_analysis.ipynb

# Create test files
touch tests/{test_data_preprocessing.py,test_model_training.py,test_model_evaluation.py}

# Create config file
touch config/config.yaml

# Add content to .gitignore
echo "__pycache__/
*.pyc
*.pyo
*.ipynb_checkpoints
.env" > .gitignore

# Add content to README.md
echo "# MLOps Project

This project demonstrates a full MLOps pipeline for deploying deep neural networks.

## Project Structure

\`\`\`plaintext
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
\`\`\`

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.8+
- Git

### Installation

1. Clone the repository:
   \`\`\`bash
   git clone <repository_url>
   cd mlops-project
   \`\`\`

2. Build and run Docker containers:
   \`\`\`bash
   docker-compose up --build
   \`\`\`

3. Run tests:
   \`\`\`bash
   pytest tests/
   \`\`\`
" > README.md

# Add content to requirements.txt
echo "pandas
numpy
scikit-learn
tensorflow
torch
flask
fastapi
gunicorn
docker
pytest
loguru" > requirements.txt

# Add content to Dockerfile
echo "FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [\"gunicorn\", \"--bind\", \"0.0.0.0:5000\", \"model_deployment:app\"]
" > Dockerfile

# Add content to docker-compose.yml
echo "version: '3.8'

services:
  web:
    build: .
    ports:
      - \"5000:5000\"
    volumes:
      - .:/app
    environment:
      - ENV=production
" > docker-compose.yml

# Add content to config.yaml
echo "data:
  raw_path: data/raw/
  processed_path: data/processed/

model:
  saved_path: models/saved_model/

training:
  epochs: 10
  batch_size: 32
  learning_rate: 0.001
" > config/config.yaml

# Print success message
echo "Project structure created successfully."
