# Python Auto-Grader
![readme-header-image.jpg](assets/readme-header-image.jpg)\
*Image provided by [David Mulder](https://www.flickr.com/photos/113026679@N03/26647523637)*

## Description
This program was created to automate the grading of student assignments.

## Running the Code
```shell
python main.py <excel_folder_path> <criteria.json> <final_grade_excel_path>
```
- `excel_folder_path` - Path to the folder containing the student submissions in Excel format.
- `criteria.json` - Path to the JSON file containing the grading criteria.
- `final_grade_excel_path` - Path and name of the output Excel file where the final grades will be saved.

## Important File Structures

### 'criteria.json'
```json
{
  "comment": "Comments are allowed in the criteria.json file. They are ignored.",
  "criteria_section_1": {
    "comment": "this is an element. Multiple elements can be in a section.",
    "element_1": {
      "comment": "elements are able to be named anything that does not already exist, comment or grading_criteria",
      "spreadsheet_cell": "Sheetname!$A$1",
      "simple_value": 0
    },
    "element_2": {
      "spreadsheet_cell": "Sheetname!$A$1",
      "simple_value": 1,
      "value_tolerance": 0.1
    },
    "grading_criteria": {
      "proficient": {
        "required_count": 2
      },
      "novice": {
        "required_count": 1
      },
      "insufficient": {
        "required_count": 0
      }
    }
  },
  "criteria_section_2": {
    "element_1": {
      "spreadsheet_cell": "Sheetname!$A$1",
      "comment": "Complex values are calculated values in python format. They are evaluated in the context of the spreadsheet cell value.",
      "computed_value": "2 * [Sheetname!$B$2]"
    },
    "element_2": {
      "spreadsheet_cell": "Sheetname!$A$1",
      "computed_value": "2 * [Sheetname!$B$2]",
      "value_tolerance": 0.1
    },
    "grading_criteria": {
      "proficient": {
        "required_count": 2
      },
      "novice": {
        "required_count": 1
      },
      "insufficient": {
        "required_count": 0
      }
    }
  },
  "criteria_section_3": {
    "element_1": {
      "spreadsheet_cell": "Sheetname!$A$1",
      "value_min": 0,
      "value_max": 1
    },
    "grading_criteria": {
      "proficient": {
        "required_count": 1
      },
      "insufficient": {
        "required_count": 0
      }
    }
  }
}
```
**Important things to note:**
- Each criteria section must have a `"grading_criteria"` element.
- Elements can either have `"simple_value"`, `"computed_value"`, or both `"value_min"` and `"value_max"`, but cannot have more than one of these at the same time.
- When using `"computed_value"` or `"simple_value"`, the `"value_tolerance"` element is able to be used and optional. 
- The `"spreadsheet_cell"` element must be a valid Excel cell reference. Sheetname is optional.

### final_grades.xlsx

| Student Filename   | criteria_section_1   | score        | comment | criteria_section_2  | score      | comment                                                             | criteria_section_3 | score        | comment                                                                  |
|--------------------|----------------------|--------------|---------|---------------------|------------|---------------------------------------------------------------------|--------------------|--------------|--------------------------------------------------------------------------|
| student_file1.xlsx | criteria_section_1   | proficient   |         | criteria_section_2  | proficient |                                                                     | criteria_section_3 | proficient   |                                                                          |
| student_file2.xlsx | criteria_section_1   | proficient   |         | criteria_section_2  | novice     | Your value for element 1 was out of tolerance, expected 2 but got 0 | criteria_section_3 | insufficient | Your value for element 1 was out of tolerance, expected 0 to 1 but got 3 |

- `Student Filename` will be the name of the student file.
- comments can be empty if there are no issues with the grading.
- `score` will be the name of the grading criteria bracket met by the student's score.

## Packages Used
This project uses the following packages:
- `pandas` - Data manipulation
- `openpyxl` - Excel file manipulation'

## Authors/Collaborators
- Samuel Wilhite - Full project code
- Doug Sandy - Project Commissioner/Spreadsheet Design

## Sprint Goals
- Integrated into one piece of code