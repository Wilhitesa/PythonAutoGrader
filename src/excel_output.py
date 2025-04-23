import json
import pandas as pd

# This class is used to output data to an Excel file.
class ExcelOutput:
    """
    A class to handle writing data to an Excel file.
    """

    # initialize the class with a DataFrame
    def __init__(self, pd_dataframe: pd.DataFrame):
        self.dataframe = pd_dataframe

    # Add a row to the DataFrame
    def add_row(self, row_data: []):
        self.dataframe.loc[len(self.dataframe)] = row_data
    # Write the DataFrame to an Excel file
    def write(self, folder_path: str):
        self.dataframe.to_excel(folder_path + "/results.xlsx", index=False)