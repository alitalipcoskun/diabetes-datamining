from preprocess import Preprocessor
import pandas as pd


if __name__ == "__main__":
    filename = "diabetes.csv"
    path = f"./data/{filename}"
    
    df = pd.read_csv(path)
    
    processor = Preprocessor(df)
    cols = processor.seperate_columns(return_cols=True)
    
    print(cols)    
    
    print(df["Pregnancies"].value_counts())
    