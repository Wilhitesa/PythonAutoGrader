import json
import sys

from src.cell_eval import evaluate_element, read_file


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <excel_folder_path> <criteria.json> <final_grade_excel_path>")
        sys.exit(1)

    json_filename = sys.argv[2]
    with (open(json_filename) as file):
        data = json.load(file)
        excel = read_file(sys.argv[1])
        student_scores = []
        for key, value in data.items():
            if "comment" in key:
                continue
            numCorrect = 0
            combined_comments = ""
            for element_key, element_value in value.items():
                if "comment" in element_key:
                    # Skip comments
                    continue
                elif "element" in element_key:
                    correct, comment = evaluate_element(element_value, excel)
                    print(f"{element_value["spreadsheet_cell"]}: {correct}, {comment}")
                    numCorrect += 1 if correct else 0
                    combined_comments += comment + "\n"
                elif "grading_criteria" in element_key:
                    eval_str = evaluate_criteria(element_value, numCorrect)
                    student_scores.append(eval_str)
                    print(eval_str)

def evaluate_criteria(criteria: json, score: int) -> str:
    for criteria_key, criteria_value in criteria.items():
        if score >= criteria_value["required_count"]:
            return criteria_key


if __name__ == "__main__":
    main()