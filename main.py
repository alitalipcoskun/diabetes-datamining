from preprocess import PreProcessor
import pandas as pd


if __name__ == "__main__":
    filename = "diabetes.csv"
    path = f"./data/{filename}"
    
    df = pd.read_csv(path)
    
    processor = PreProcessor(df)
    cols = processor.seperate_columns(return_cols=True)
    
    