import json
import os
import sys

from pandas import DataFrame

from file_retrieval import get_all_paths

from src.cell_eval import evaluate_element, read_file
from src.excel_output import ExcelOutput
from src.file_retrieval import get_all_paths


def main():
    """
    Main function to evaluate student scores based on criteria defined in a JSON file.
    """
    student_files, json_filename, result_loc = get_all_paths()
    #TODO: retrieve all files in student folder path, then iterate through them with following code
    with open(json_filename) as file:
        file_list = os.listdir(student_files)

        data = json.load(file)
        cols = ["student_file"]
        for key, value in data.items():
            if not "comment" in key:
                cols.append(key)
                cols.append("score")
                cols.append("comments")


        output = ExcelOutput(DataFrame(columns=cols))

        for student_file in file_list:
            if student_file.endswith(".xlsx"):
                excel = read_file(student_files + '/' + student_file)
                results = [student_file]
                # excel = read_file(get_student_folder_path())
                student_scores = []
                for key, value in data.items():
                    if "comment" in key:
                        # Skip comments
                        continue
                    num_correct = 0
                    results.append(key)
                    combined_comments = ""
                    for element_key, element_value in value.items():
                        if "element" in element_key:
                            correct, comment = evaluate_element(element_value, excel)
                            # print(f"{element_value["spreadsheet_cell"]}: {correct}, {comment}")
                            num_correct += 1 if correct else 0
                            combined_comments += comment + "\n" if comment else ""
                        elif "grading_criteria" in element_key:
                            eval_str = evaluate_criteria(element_value, num_correct)
                            results.append(eval_str)
                            results.append(combined_comments)
                            # student_scores.append(eval_str)
                            #print(f"Score for {key}: {eval_str}")
                            #print(f"Comments for {key}: {combined_comments}")
                output.add_row(results)
        output.write(result_loc)


def evaluate_criteria(criteria: json, score: int) -> str:
    for criteria_key, criteria_value in criteria.items():
        if score >= criteria_value["required_count"]:
            return criteria_key


if __name__ == "__main__":
    main()