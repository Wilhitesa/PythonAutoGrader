import json
import sys

def main():
    if sys.argv != 3:
        print("Usage: python main.py <excel_folder_path> <criteria.json> <final_grade_excel_path>")
        sys.exit(1)

    json_filename = sys.argv[1]
    with open(json_filename) as file:
        data = json.load(file)
        student_scores = {}
        for key, value in data.items():
            if "comment" in key:
                pass
            numCorrect = 0
            for element_key, element_value in value.items():
                if "comment" in element_key:
                    pass
                elif "element" in element_key:
                    pass
                elif "grading_criteria" in element_key:
                    eval_str = evaluate_criteria(element_value, numCorrect)
                    student_scores[key] = eval_str

def evaluate_criteria(criteria: json, score: int) -> str:
    for criteria_key, criteria_value in criteria.items():
        if criteria_value["required_count"] >= score:
            return criteria_key


if __name__ == "__main__":
    main()