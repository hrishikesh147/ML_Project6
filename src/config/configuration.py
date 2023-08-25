from src.constants import *
import os,sys

# ROOt_DIR_KEY =os.getcwd()
# DATA_DIR="Data"
# DATA_DIR_KEY="finalTrain.csv"

# ARTIFACT_DIR_KEY="Artifact"
# # data ingestion variables-----------------------------------------
# DATA_INGESTIOn_KEY ="data_ingestion"
# DATA_INGESTION_RAW_DATA_DIR ="raw_data_dir"
# RAW_DATA_DIR_KEY ="raw.csv"

# DATA_INGESTION_INGESTED_DATA_DIR_KEY ="ingested_dir"
# TRAIN_DATA_DIR_KEY ="train.csv"
# TEST_DATA_DIR_KEY ="test.csv"

# def get_current_time_stamp():
#     return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

# CURRENT_TIME_STAMP=get_current_time_stamp()

ROOT_DIR=ROOt_DIR_KEY

DATASET_PATH=os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY)

RAW_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTIOn_KEY,CURRENT_TIME_STAMP,
                           DATA_INGESTION_RAW_DATA_DIR,RAW_DATA_DIR_KEY)

TRAIN_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTIOn_KEY,CURRENT_TIME_STAMP,
                            DATA_INGESTION_INGESTED_DATA_DIR_KEY,TRAIN_DATA_DIR_KEY)

TEST_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTIOn_KEY,CURRENT_TIME_STAMP,
                            DATA_INGESTION_INGESTED_DATA_DIR_KEY,TEST_DATA_DIR_KEY)
