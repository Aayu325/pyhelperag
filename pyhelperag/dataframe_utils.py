import pandas as pd

def summarize_dataframe(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "nulls": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.to_dict()
    }

def df_memory_usage(df):
    return df.memory_usage(deep=True).sum() / 1024**2  # in MB
