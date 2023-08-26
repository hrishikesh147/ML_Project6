# from src.constants import *
# from src.logger import logging
# from src.exception import CustomException
# import os, sys
# from src.config.configuration import *
# from dataclasses import dataclass
# from sklearn.base import BaseEstimator, TransformerMixin
# import numpy as np
# import pandas as pd

# from sklearn.svm import SVR
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.tree import DecisionTreeRegressor
# from src.utils import evaluate_model,save_obj

# @dataclass
# class ModelTrainerConfig:
#     trained_model_file_path=MODEL_FILE_PATH


# class ModelTrainer:
#     def __init__(self):
#         self.model_trainer_config=ModelTrainerConfig()

#     def initiate_model_training(self,train_array,test_array):
#         try:
#             X_train,y_train,X_test,y_test=(train_array[:,:-1],train_array[:,-1] ,
#                                            test_array[:,:-1],test_array[:,-1])
            
#             models={
#                 'decisiontree':DecisionTreeRegressor(),
#                 'gradientboosting':GradientBoostingRegressor(),
#                 'random_forest':RandomForestRegressor(),
#                 'Svr':SVR()
#             }

#             model_report=evaluate_model(X_train,y_train,X_test,y_test,models)
#             print(model_report)
            
#             best_model_score=max(sorted(model_report.values()))
#             best_model_name=list(model_report.keys())[
#                 list(model_report.values().index(best_model_score))
#             ]

#             best_model=models[best_model_name]
#             print(f"best model found:{best_model_name}, r2_score: {best_model_score}")
#             logging.info(f"best model found:{best_model_name}, r2_score: {best_model_score}")

#             save_obj(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)


#         except Exception as e:
#             raise CustomException(e,sys)