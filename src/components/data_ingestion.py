import pandas as pd
import numpy as np
from src.constants import *
from src.config.configuration import *
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    raw_data_path=RAW_FILE_PATH
    train_data_path=TRAIN_FILE_PATH
    test_data_path=TEST_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("starting initiate data_ingestion")
            df=pd.read_csv(DATASET_PATH)
            #creating RAW_DATA folder and saving raw_data to csv
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)
            logging.info("raw data saved in raw_data_path")

            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            logging.info("train, test split of data done")

            ##creating TRAIN_DATA folder and saving train_data to csv
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path,header=True)
            logging.info("train data saved in train_data_path")

            #creating TEST_DATA folder and saving train_data to csv
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,header=True)
            logging.info("test file saved in test_data_path")

            logging.info(" returning train and test data path")

            return (self.data_ingestion_config.train_data_path,
                    self.data_ingestion_config.test_data_path)
        

        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()