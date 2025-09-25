# End-to-End MLOps Pipeline with MLflow & DagsHub

This project demonstrates the development of a **complete machine learning pipeline**, covering all stages from data ingestion to model prediction with experiment tracking and artifact management.

## Key Components

- **Data Ingestion & Validation**:  
  Automates loading of datasets, schema validation, and quality checks to ensure reliable inputs for training.

- **Data Transformation & Feature Engineering**:  
  Applies preprocessing steps and feature transformations to prepare data for modeling.

- **Model Training & Evaluation**:  
  Trains machine learning models, evaluates performance using metrics like RMSE, MAE, and R², and saves evaluation results.

- **Model Logging & Experiment Tracking**:  
  Uses **MLflow** to log models, metrics, and artifacts, enabling reproducible experiments and centralized tracking.

- **Integration with DagsHub**:  
  Demonstrates remote tracking of MLflow experiments, artifact storage, and model management, ensuring seamless collaboration and version control.

- **Prediction Ready**:  
  Provides a framework for serving models and performing predictions.

 **Dataset Context:**  
 
 This project uses a **wine quality dataset** containing physicochemical properties of wines, such as acidity, sugar, pH, sulphates, and alcohol          content. The goal is to predict wine quality based on these features, serving as a practical example for building an end-to-end MLOps pipeline.



# Workflow--ML pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation---data engineering, data preprocessing
4. Model Trainer
5. Model Evaluation

# updation part

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5.  update the configuration manager in srcc config
6. update the components
7. update the pipeline
8. update the main.py
