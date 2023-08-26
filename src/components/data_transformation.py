from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder
from sklearn.pipeline import Pipeline
from src.utils import save_obj
from src.config.configuration import PREPROCESING_OBJ_FILE,TRANSFORM_TRAIn_FILE_PATH,TRANSFORM_TEST_FILE_PATH,FEATURE_ENGG_OBJ_FILE_PATH

class Feature_Engineering(BaseEstimator,TransformerMixin):
    def __init__(self):
         logging.info("... STARTING feature Engineering ...")

    def distance_numpy(self, df, lat1, lon1,lat2, lon2 ):
        p = np.pi/180
        a = 0.5 - np.cos((df[lat2]-df[lat1])*p)/2 + np.cos(df[lat1]*p) * np.cos(df[lat2]*p) * (1-np.cos((df[lon2]-df[lon1])*p))/2
        df['distance'] = 12734 * np.arccos(np.sort(a))

    def transform_data(self,df):
        try:
            df.drop(['ID'], axis = 1, inplace = True)
            logging.info("droppin ID column")

            self.distance_numpy(df,'Restaurant_latitude',
                                'Restaurant_longitude',
                                'Delivery_location_latitude',
                                'Delivery_location_longitude')
            
            logging.info("distance calculated")
            
            df.drop(['Delivery_person_ID','Restaurant_latitude','Restaurant_longitude',
                     'Delivery_location_latitude','Delivery_location_longitude',
                     'Order_Date','Time_Orderd','Time_Order_picked'],axis=1,inplace=True)
            
            logging.info("Non important columns dropped")

            return df 

        except Exception as e:
            raise CustomException (e,sys)
        
    def transform(self,X,y):
        try:
            logging.info("transform_data function to be applied....")
            transformed_df=self.transform_data(X)
            logging.info("transform_data function applied on X variable")
            return transformed_df
        except Exception as e:
            raise CustomException(e,sys)
        
@dataclass
class DataTransformationConfig():
    proccessed_obj_file_path =PREPROCESING_OBJ_FILE,
    feature_engg_obj_path =FEATURE_ENGG_OBJ_FILE_PATH,
    transform_train_path =TRANSFORM_TRAIn_FILE_PATH,
    transform_test_path=TRANSFORM_TEST_FILE_PATH

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        logging.info("starting data transformation")

    def get_data_transformation_obj(self,df):
        try:
            Road_traffic_density = ['Low', 'Medium', 'High', 'Jam']
            Weather_conditions = ['Sunny', 'Cloudy', 'Fog', 'Sandstorms', 'Windy', 'Stormy']

            categorical_columns = ['Type_of_order','Type_of_vehicle','Festival','City']
            ordinal_encoder = ['Road_traffic_density', 'Weather_conditions']
            numerical_column=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition',
                              'multiple_deliveries','distance']
            
            logging.info("numerical_pipeline step began.....")
            numerical_pipeline=Pipeline(steps=[
            ('impute',SimpleImputer(strategy='constant',fill_value=0)),
            ('scaler',StandardScaler(with_mean=False))
            ])
            logging.info("numerical_pipeline step completed SUCCESFULLY")

            logging.info("categorical_pipeline step began.....")
            categorical_pipeline=Pipeline(steps=[
            ('impute',SimpleImputer(strategy='most_frequent')),
            ('onehotencoding',OneHotEncoder(handle_unknown='ignore')),
            ('scaler',StandardScaler(with_mean=False))
        ])
            logging.info("categorical_pipeline step completed SUCCESFULLY")

            logging.info("ordinal_pipeline step began.....")
            ordinal_pipeline=Pipeline(steps=[
            ('impute',SimpleImputer(strategy='most_frequent')),
            ('ordinalencoding',OrdinalEncoder(categories=[Road_traffic_density,Weather_conditions])),
            ('scaler',StandardScaler(with_mean=False)) 
        ])
            logging.info("ordinal_pipeline step completed SUCCESFULLY")

            logging.info("ColumnTransformer step began.....")
            preprocssor=ColumnTransformer(
                ('numerical_pipeline',numerical_pipeline,numerical_column),
                ('categorical_pipeline',categorical_pipeline,categorical_columns),
                ('ordinal_column',ordinal_pipeline,ordinal_encoder)
            )

            logging.info("Column transformer step completed")
            return preprocssor

        except Exception as e:
            raise CustomException(e,sys)
        
    def get_feature_engineering_object(self):
        try:
            feature_engineering=Pipeline(steps=['fe',Feature_Engineering()])
            return feature_engineering
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_transformation(self,train_path,test_path):
        logging.info("initiating data transformation")
        train_df=pd.read_csv(train_path)
        test_df=pd.read_csv(test_path)
        logging.info("train_df/test_df splitting Done")

        fe_obj=self.get_feature_engineering_object()
        logging.info("get_feature_engineering_object called")
        

        train_df=fe_obj.fit_transform(train_df)
        test_df=fe_obj.transform(test_df)
        logging.info("fit_transform/transform of train_df/test_df Done")

        train_df.to_csv("train_data.csv")
        test_df.to_csv("test_data.csv")
        logging.info(" train_data.csv/test_data.csv saved Done")

        processinf_obj = self.get_data_transformation_obj()
        logging.info("get_data_transformation_obj called")

        traget_columns_name = "Time_taken (min)"

        X_train=train_df.drop(columns=traget_columns_name,axis=1)
        y_train=train_df[traget_columns_name]
        logging.info("target column dropped from X _train and target assigned to y_train")

        X_test=test_df.drop(columns=traget_columns_name,axis=1)
        y_test=test_df[traget_columns_name]
        logging.info("target column dropped from X _test and target assigned to y_test")

        X_train=processinf_obj.fit_transform(X_train)
        X_test=processinf_obj.transform(X_test)
        logging.info("fit_transform/transform of X_train/y_train Done")

        train_arr=np.c_(X_train,np.array(y_train))
        test_arr=np.c_(X_test,np.array(y_test))
        logging.info("concatenation of train_arr,test_arr Done")

        df_train=pd.DataFrame(train_arr)
        df_test=pd.DataFrame(test_arr)
        logging.info("pd.DataFrame of train_arr,test_arr Done")
        
        os.makedirs(os.path.dirname(self.data_transformation_config.transform_train_path),exist_ok=True)
        df_train.to_csv(self.data_transformation_config.transform_train_path,index=False,header=True)

        os.makedirs(os.path.dirname(self.data_transformation_config.transform_test_path),exist_ok=True)
        df_test.to_csv(self.data_transformation_config.transform_test_path,index=False,header=True)

        save_obj(file_path=self.data_transformation_config.feature_engg_obj_path,obj=fe_obj)
        save_obj(file_path=self.data_transformation_config.proccessed_obj_file_path,obj=fe_obj)

        logging.info("returning train_arr,test_arr,self.data_transformation_config.proccessed_obj_file_path")
        return train_arr,test_arr,self.data_transformation_config.proccessed_obj_file_path