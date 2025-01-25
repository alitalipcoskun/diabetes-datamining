from src.logger import CustomLogger
import numpy as np
import pandas as pd




class PreProcessor:
    def __init__(self,
                 df: pd.DataFrame,
                 log_filename: str = "preprocess.log"):
        self.__df = df
        self.__categoric_cols = []
        self.__numeric_cols = []
        self.__cardinal_cols = []
        self.__log = CustomLogger(log_filename)
        
        self.__numeric_types = [np.int64, 
                                np.float64, 
                                np.int32,
                                np.float32,
                                int,
                                float]
              
    @property
    def categoric_columns(self):
        return self.__categoric_cols

    @property
    def cardinal_columns(self):
        return self.__cardinal_cols
    
    @property
    def numeric_columns(self):
        return self.__numeric_cols
    
    @property
    def df(self):
        return self.__df
    
    
    
    @df.setter
    def df(self, df):
        self.__df = df
    
    
    def seperate_columns(self,
                        categoric_th: int = 8,
                        cardinal_th: int = 20,
                        return_cols:bool = False) -> None:
        """
            The function helps you seperate columns as follows: categoric, numeric, ordinal

            Parameters:
                categoric_th -> int: It is the treshold for categoric variables. It is defined 8 as default.
                cardinal_th -> int: It is the treshold for cardinal variables. It is defined 20 as default.

        """
        
        try:
            self.__verify_treshold(categoric_th)
            self.__verify_treshold(cardinal_th)
            
            
            df = self.df

            self.__log.logger.info("Seperation process of the columns are started")
            
            # Categoric columns
            categoric_columns = [column for column in df.columns if df[column].dtypes == 'O']
            num_but_cats = [column for column in df.columns if df[column].nunique() < categoric_th and df[column].dtypes != 'O']
            cat_but_cardinals = [column for column in df.columns if df[column].nunique() > cardinal_th and df[column].dtypes == "O"]
            
            categoric_columns = categoric_columns + num_but_cats
            categoric_columns = [column for column in categoric_columns if column not in cat_but_cardinals]
            
            # Numeric columns
            numeric_columns = [column for column in df.columns if (df[column].dtypes != "O")]
            numeric_columns = [column for column in numeric_columns if column not in num_but_cats]
        
            self.__numeric_cols = numeric_columns
            self.__categoric_cols = categoric_columns
            self.__cardinal_cols = cat_but_cardinals
            
            self.__log.logger.debug(categoric_columns)
            self.__log.logger.debug(numeric_columns)            
            self.__log.logger.debug(cat_but_cardinals)
        
            self.__log.logger.info("Preprocessor successfully seperated the columns")
        
            if return_cols:
                return [categoric_columns, numeric_columns, cat_but_cardinals]
        except Exception:
            self.__log.logger.critical("An error occured")
        finally:
            self.__log.logger.info("End of execution of seperate_columns")
            
    def log_missing_values(self):
        """
        The function does logs the null values for each column. It provides insights if the dataframe contains NaN in column.
        """
        
        try:
            self.__log.logger.info("Checking process of NaN values started.")
            
            # Retrieving dataframe
            df = self.df
        
            # Iterating over dataframe
            for column in df.columns:
                nan_amount = df[column].isnull().sum()
                self.__log.logger.info(f"For column {column}, nan value amount is: {nan_amount}")
        
        except Exception:
            self.__log.logger.error("An error occured while checking nan values")
        
        finally:
            self.__log.logger.info("Checking process of NaN values successfully ended.")
        
            
    def __verify_treshold(self, treshold: int):
        if treshold < 0:
            raise Exception("Invalid value for treshold value.")