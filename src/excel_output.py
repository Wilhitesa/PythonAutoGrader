import pandas as pd

# This class is used to output data to an Excel file.
class ExcelOutput:
    """
    A class to handle writing data to an Excel file.
    """

    # initialize the class with a DataFrame
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    # Add a row to the DataFrame
    def add_row(self, row_data: dict):
        self.dataframe = self.dataframe.append(row_data, ignore_index=True)

    # Write the DataFrame to an Excel file
    def write(self, file_path: str):
        self.dataframe.to_excel(file_path, index=False)