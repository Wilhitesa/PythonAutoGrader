import pandas as pd

# Read a csv file and return a pandas DataFrame
def read_file(file_path) -> pd.DataFrame:
    return pd.read_csv(file_path)