import os,sys
from datetime import datetime

ROOt_DIR_KEY =os.getcwd()
DATA_DIR="Data"
DATA_DIR_KEY="finalTrain.csv"

ARTIFACT_DIR_KEY="Artifact"
# data ingestion variables-----------------------------------------
DATA_INGESTIOn_KEY ="data_ingestion"
DATA_INGESTION_RAW_DATA_DIR ="raw_data_dir"
RAW_DATA_DIR_KEY ="raw.csv"

DATA_INGESTION_INGESTED_DATA_DIR_KEY ="ingested_dir"
TRAIN_DATA_DIR_KEY ="train.csv"
TEST_DATA_DIR_KEY ="test.csv"

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP=get_current_time_stamp()

# data transformation variables------------(folder structure shown below)-----------------------
#data_transformation->processor (folder)            ,    transformation (folder)
#                    1) processor.pkl               ,  1) train.csv      2)  test.csv 
DATA_TRANSFORMATION_ARTIFACT ="data_transformation"

DATA_PREPROCCED_DIR ="procceor"
DATA_TRANSFORMTION_PROCESSING_OBJ="processor.pkl"

DATA_TRANSFORM_DIR ="transformation"
TRANSFORM_TRAIN_DIR_KEY ="train.csv"
TRANSFORM_TEST_DIR_KEY ="test.csv"

#model training variable-----------
MODEL_TRAINER_KEY="model_trainer"
MODEL_OBJECT="model.pkl"

