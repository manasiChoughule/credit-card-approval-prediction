import os
import sys
from src.exception import CustomeException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # where to save train, test, and raw path
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")
    

class DataIngestion:
    def __init__(self):
        # stores path variable of our 3 data files
        self.ingestion_config = DataIngestionConfig()
        

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv('notebook/data/application_record_combined.csv')
            logging.info('Read the dataset as dataframe')
            
            # create artificats folders and dont change anything if it already exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            
            # save raw data 
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            
            # split the data
            logging.info("Train Test split initiated")            
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)
            
            # store the data to the articats according to the path
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            logging.info("Data Ingestion completed")        
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomeException(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()