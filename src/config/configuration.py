from src.constants import *
import os,sys

#DATA INGESTION PATHS..................................................................

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



#DATA TRANSFORMATION PATHS.........................................................................

# # data transformation variables------------(folder structure shown below)-----------------------
# #data_transformation->   processor (folder)            ,         transformation (folder)
# #            1) processor.pkl  2)feature_engg.pkl   ,     1) train.csv      2)  test.csv 
# DATA_TRANSFORMATION_ARTIFACT ="data_transformation"

# DATA_PREPROCCED_DIR ="procceor"
# DATA_TRANSFORMTION_PROCESSING_OBJ="processor.pkl"

# DATA_TRANSFORM_DIR ="transformation"
# TRANSFORM_TRAIN_DIR_KEY ="train.csv"
# TRANSFORM_TEST_DIR_KEY ="test.csv"

PREPROCESING_OBJ_FILE =os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                           DATA_PREPROCCED_DIR,DATA_TRANSFORMTION_PROCESSING_OBJ)

FEATURE_ENGG_OBJ_FILE_PATH =os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                           DATA_PREPROCCED_DIR,' feature_engg.pkl')

TRANSFORM_TRAIn_FILE_PATH =os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                        DATA_TRANSFORM_DIR,TRANSFORM_TRAIN_DIR_KEY)

TRANSFORM_TEST_FILE_PATH =os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_TRANSFORMATION_ARTIFACT,
                        DATA_TRANSFORM_DIR,TRANSFORM_TEST_DIR_KEY)


#model training..........................................................
MODEL_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,MODEL_TRAINER_KEY,MODEL_OBJECT)

