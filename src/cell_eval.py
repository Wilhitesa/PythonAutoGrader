import pandas as pd
import openpyxl
import json

from numpy.ma.core import maximum


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
        equation = vals["complex_value"].split(" ")
        for piece in equation:
            if "$" in piece:
                parts = piece.split("!")
                parts[1] = parts[1].replace("$", "")
                eq_num = sheet[parts[0]][parts[1]].value
                equation[equation.index(piece)] = str(eq_num)
        equation = " ".join(equation)

        minimum = eval(equation)
        maximum = eval(equation)

        if "value_tolerance" in vals:
            minimum = eval(equation) - vals["value_tolerance"]
            maximum = eval(equation) + vals["value_tolerance"]

        parts = vals["spreadsheet_cell"].split("!")
        parts[1] = parts[1].replace("$", "")

        num = sheet[parts[0]][parts[1]].value

        correct = minimum <= num <= maximum
        if not correct:
            comment += f"Expected value of {vals['complex_value']}, but got {num}. "

    elif "value_min" in vals and "value_max" in vals:
        minimum = vals["value_min"]
        maximum = vals["value_max"]

        parts = vals["spreadsheet_cell"].split("!")
        parts[1] = parts[1].replace("$", "")

        num = sheet[parts[0]][parts[1]].value

        correct = minimum <= num <= maximum
        if not correct:
            comment += f"Expected value between {minimum} and {maximum}, but got {num}. "
    else:
        raise Exception("Invalid JSON format")

    return [correct, comment]