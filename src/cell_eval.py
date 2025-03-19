import pandas as pd


# Read an Excel file and return a pandas DataFrame
def read_file(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)


# Evaluates an Excel cell in a DataFrame.
def evaluate_cell(dataframe: pd.DataFrame, value_col: int, value_row: int, simple_value=None, value_tolerance=None,
                  value_min=None, value_max=None) -> bool:
    final_max, final_min = 0, 0
    if simple_value and value_tolerance:
        final_max = simple_value + value_tolerance
        final_min = simple_value - value_tolerance
    elif value_min and value_max:
        final_max = value_max
        final_min = value_min

    return final_min <= dataframe.iat[value_row, value_col] <= final_max
