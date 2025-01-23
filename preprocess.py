from logger import CustomLogger





class PreProcessor:
    def __init__(self, df):
        self.__df = df
        self.__categoric_cols = []
        self.__numeric_cols = []
        self.__cardinal_cols = []
        self.__log = CustomLogger("preprocess.log")
              
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


            categoric_cols = [column for column in df.columns if df[column].dtypes == 'O']
            numeric_columns = [column for column in df.columns if df[column].dtypes != 'O']
            num_but_cats = [column for column in df.columns if df[column].nunique() < categoric_th and df[column].dtypes != 'O']

            cat_but_cardinals = [column for column in categoric_cols if df[column].nunique() > cardinal_th]

            categoric_cols = categoric_cols + num_but_cats
            categoric_cols = [column for column in categoric_cols if column not in cat_but_cardinals]

            numeric_columns = [column for column in numeric_columns if column not in num_but_cats]
        
            self.__numeric_cols = numeric_columns
            self.__categoric_cols = categoric_cols
            self.__cardinal_cols = cat_but_cardinals
        
            self.__log.logger.info("Preprocessor successfully seperated the columns")
        
            if return_cols:
                return [categoric_cols, numeric_columns, categoric_cols]
        except Exception:
            self.__log.logger.critical(Exception)
            
    def __verify_treshold(self, treshold: int):
        if treshold < 0:
            raise Exception("Unexpected datatype for treshold value")