import json
import pandas as pd

# This class is used to output data to an Excel file.
class ExcelOutput:
    """
    A class to handle writing data to an Excel file.
    """
    # initialize the class with a DataFrame
    def __init__(self, pd_dataframe: pd.DataFrame):
        """
        Initialize the ExcelOutput class with a DataFrame.
        :param pd_dataframe: A pandas DataFrame to be used for output.
        """
        self.dataframe = pd_dataframe

    # Add a row to the DataFrame
    def add_row(self, row_data: list[str]) -> None:
        """
        Add a row to the DataFrame.
        :param row_data: A list of data to be added as a new row.
        """
        self.dataframe.loc[len(self.dataframe)] = row_data

    # Write the DataFrame to an Excel file
    def write(self, folder_path: str, json_filename: str) -> None:
        """
        Write the DataFrame to an Excel file.
        :param folder_path: The path to the folder where the Excel file will be saved.
        :param json_filename: The name of the JSON file used for grading. It will be used as a part of the Excel file name.
        :return: None
        """
        self.dataframe.to_excel(f"{folder_path}/{json_filename}results.xlsx", index=False)