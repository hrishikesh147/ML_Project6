# from src.constants import *
# from src.logger import logging
# from src.exception import CustomException
# import os, sys
# from src.config.configuration import *

# import pandas as pd
# import numpy as np
# from src.utils import load_model
# from sklearn.pipeline import Pipeline
# import pickle

# #----------------------------------PREDICTION_FOLDER-----------------------
# #                 1)PREDICTION_CSV                     2)FEATURE_ENG_FOLDER

# PREDICTION_FOLDER="batch_prediction"
# PREDICTION_CSV="prediction_csv"
# PREDICTION_FILE="output.csv"
# FEATURE_ENG_FOLDER="feature_eng"

# ROOT_DIR=os.getcwd()
# BATCH_PREDICTION=os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV)
# FEATURE_ENG=os.path.join(ROOT_DIR,PREDICTION_FOLDER,FEATURE_ENG_FOLDER)

# class batch_prediction:
#     def __init__(self,input_file_path,model_file_path,transformer_file_path,feature_engineering_file_path):
#         self.input_file_path=input_file_path
#         self.model_file_path=model_file_path
#         self.transformer_file_path=transformer_file_path
#         self.feature_engineering_file_path=feature_engineering_file_path

#     def start_batch_prediction(self):
#         try:
#             #first load the different files----------------------------------------------------
#             #load the featutre engg pipeline
#             with open(self.feature_engineering_file_path,'rb') as f:
#                 feture_pipeline=pickle.load(f)

#             #load the data_transformation pipeline
#             with open(self.transformer_file_path,'rb') as f:
#                 processor=pickle.load(f)

#             #load the model separately
#             model=load_model(self.model_file_path)

#             #now create pipelines------------------------------------------------------------
#             #creating feature Engg pipelines
#             feature_enigneering_pipeline=Pipeline([
#                 ("feature_engg",feture_pipeline)
#             ])

#             df=pd.read_csv(self.input_file_path)

#             df.to_csv("food_delivery_time.csv")

#             # NOw apply Feature engineering Pipeline to the df
#             feature_enigneering_pipeline.transform(df)
#             df.to_csv("feature_engineering.csv")


#             FEATURE_ENINGEERING_PATH=FEATURE_ENG
#             os.makedirs(FEATURE_ENINGEERING_PATH,exist_ok=True)

#             file_path=os.path.join(FEATURE_ENINGEERING_PATH,'batch_feature_eng.csv')
#             df.to_csv(file_path,index=False)

#             #lets drop time target column
#             df.drop('Time_taken (min)',axis=1)
#             df.to_csv("time_taken_dropped.csv")

#             transformed_data=processor.transform(df)

#             file_path=os.path.join(FEATURE_ENINGEERING_PATH,'processor.csv')
#             predictions=model.predict(transformed_data)

#             df_prediction=pd.DataFrame(predictions,columns=['prediction'])

#             BATCH_PREDICTIOn_PATH=BATCH_PREDICTION
#             os.makedirs(BATCH_PREDICTIOn_PATH,exist_ok=True)
#             csv_path=os.path.join(BATCH_PREDICTIOn_PATH,'output.csv')

#             df_prediction.to_csv(csv_path,index=False)
#             logging.info(f"Batch prediction Done")


#         except Exception as e:
#             raise CustomException(e,sys)
    
