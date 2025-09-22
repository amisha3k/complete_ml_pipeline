#End to end data science project

###Workflow--ML pipeline

1. Data Ingestion--


1. update config.yaml----------- > in data ingestion, the first step is to update the config.yaml file. This file contains important configurations such as data source inputs, which can be databases, APIs, or ETL pipelines. The config.yaml file specifies where to fetch the data from and how to ingest it.

2. update the entity
3. update the configuration manager in srcc config

config.yaml  ---> ConfigurationManager ---> DataIngestionConfig ---> DataIngestion
                     │                                 │
                     ▼                                 ▼
               Create directories             Download + Extract ZIP
                     │                                 │
                     ▼                                 ▼
                artifacts/                  artifacts/data_ingestion/raw CSV







2. Data Validation

3. Data Transformation

4. Model Trainer

5. Model Evaluation



update schema.yaml
update params.yaml
update the entity
update the components
update the pipeline
update the main.py