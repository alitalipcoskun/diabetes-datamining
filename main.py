from src.preprocess import PreProcessor
import pandas as pd


if __name__ == "__main__":
    filename = "diabetes.csv"
    path = f"./data/{filename}"
    
    df = pd.read_csv(path)
    preprocessor = PreProcessor(df=df)
    preprocessor.seperate_columns(cardinal_th=0.5)
     
    
    

    
    