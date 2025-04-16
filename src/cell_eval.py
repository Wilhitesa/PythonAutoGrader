import pandas as pd
import openpyxl
import json

# Read an Excel file and return a pandas DataFrame
def read_file(file_path: str) -> openpyxl.Workbook:
    return openpyxl.open(file_path, read_only=True)



def evaluate_element(vals: json, sheet: openpyxl.Workbook) -> [bool, str]:
    comment = ""
    correct = True

    if "simple_value" in vals:
        minimum = vals["simple_value"]
        maximum = vals["simple_value"]
        if "value_tolerance" in vals:
            minimum = vals["simple_value"] - vals["value_tolerance"]
            maximum = vals["simple_value"] + vals["value_tolerance"]

        parts = vals["spreadsheet_cell"].split("!")
        parts[1] = parts[1].replace("$", "")

        num = sheet[parts[0]][parts[1]].value

        correct = minimum <= num <= maximum
        if not correct:
            comment += f"Expected value of {vals['simple_value']}, but got {num}. "
    elif "complex_value" in vals:
        pass
    elif "value_min" in vals and "value_max" in vals:
        pass
    else:
        raise Exception("Invalid JSON format")

    return [correct, comment]