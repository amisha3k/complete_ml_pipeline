from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH

print("CONFIG:", CONFIG_FILE_PATH, CONFIG_FILE_PATH.exists())
print("PARAMS:", PARAMS_FILE_PATH, PARAMS_FILE_PATH.exists())
print("SCHEMA:", SCHEMA_FILE_PATH, SCHEMA_FILE_PATH.exists())

STAGE_NAME="data ingestion stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion=DataIngestionTrainingPipeline() 
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>> stage {STAGE_NAME} empleted<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e    

STAGE_NAME="data validation stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_validation=DataValidationTrainingPipeline() 
        data_validation.initiate_data_validation()
        logger.info(f">>>>>>> stage {STAGE_NAME} empleted<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e         

STAGE_NAME="data transformation stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataTransformationTrainingPipeline() 
        obj.initiate_data_transformation()
        logger.info(f">>>>>>> stage {STAGE_NAME} empleted<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e  


