import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

import joblib
import urllib.request as request
from src.datascience import logger
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.constants import *
from src.datascience.constants import CONFIG_FILE_PATH
from src.datascience.utils.common import read_yaml,create_directories,save_json

import os
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/amisha3k/ds_wine_prediction.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="amisha3k"
os.environ["MLFLOW_TRACKING_PASSWORD"]="e454077689b7938f4a4a5f3fc65e4a051bd61360"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)
        return rmse,mae,r2

    def log_into_mlflow(self):

        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)

        test_x=test_data.drop([self.config.target_column],axis=1)
        test_y=test_data[[self.config.target_column]]
 

        # mlflow.set_tracking_uri(str(Path(self.config.mlflow_uri).absolute()))
        # #mlflow.set_registry_uri(self.config.mlflow_uri)
        # tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        mlflow_uri = self.config.mlflow_uri
        if mlflow_uri.startswith("http"):
             mlflow.set_tracking_uri(mlflow_uri)   # Remote server (e.g. DagsHub, localhost:5000)
        else:
             mlflow.set_tracking_uri(str(Path(mlflow_uri).absolute()))  # Local folder

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

  
        with mlflow.start_run():

            predicted_qualities=model.predict(test_x)

            (rmse,mae,r2)=self.eval_metrics(test_y,predicted_qualities)

            #saving metrics as local
            scores={"rmse":rmse,"mae":mae,"r2":r2}
            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_metric("rmse",rmse)   
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)
           
            if tracking_url_type_store == "file":
            # local file-based MLflow store (works with log_model)
               mlflow.sklearn.log_model(model, "model")
            else:
            # Remote (e.g., DagsHub) → save + log as artifact (no registry)
               mlflow.sklearn.save_model(model, "model")
               mlflow.log_artifacts("model", artifact_path="model")