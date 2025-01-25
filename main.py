from src.preprocess import PreProcessor
import pandas as pd


if __name__ == "__main__":
    filename = "diabetes.csv"
    path = f"./data/{filename}"
    
    df = pd.read_csv(path)
    preprocessor = PreProcessor(df=df)
     
    
    

    
    