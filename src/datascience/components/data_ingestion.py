 
import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Download dataset from the source URL if not already present locally.
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                logger.info(f"Downloading file from {self.config.source_URL} ...")
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"File downloaded successfully: {filename}")
                logger.info(f"Download headers: {headers}")
            else:
                logger.info(f"File already exists at {self.config.local_data_file}")
        except Exception as e:
            logger.error("Error during file download")
            raise e

    def extract_zip_file(self):
        """
        Extract the downloaded zip file into the specified directory.
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extraction completed. Files are available at: {unzip_path}")
        except Exception as e:
            logger.error("Error during file extraction")
            raise e
