# Imports
import json
import os
from pandas import DataFrame
from src.cell_eval import evaluate_element, read_file
from src.excel_output import ExcelOutput
from src.file_retrieval import get_all_paths


def main():
    """
    Main function to evaluate student scores based on criteria defined in a JSON file.
    """
    student_files, json_filename, result_loc = get_all_paths()
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
                output.add_row(results)
        output.write(result_loc, json_filename.split("/")[-1].split(".")[0] + "_")  # Adds a prefix to the filename


def evaluate_criteria(criteria: json, score: int) -> str:
    """
    Retrieves the grading criteria tier from the JSON file based on the score.
    :param criteria: A JSON object containing grading criteria. See "grading_criteria" in the JSON file example in the README.md.
    :param score: The score to evaluate against the criteria.
    :return: The string representation of the grading criteria tier.
    """
    for criteria_key, criteria_value in criteria.items():
        if score >= criteria_value["required_count"]:
            return str(criteria_key)
    return "Error: No criteria met"


if __name__ == "__main__":
    main()