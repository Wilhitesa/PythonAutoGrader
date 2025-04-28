# Python Auto-Grader
![readme-header-image.jpg](assets/readme-header-image.jpg)\
*Image provided by [David Mulder](https://www.flickr.com/photos/113026679@N03/26647523637)*

## Description
This program was created to automate the grading of student assignments.

## Running the Code
```shell
python main.py
```

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

#### JSON File Structure:
- `"comment"` - Comments are allowed in the JSON file. They are ignored. However, ensure there is no more than one comment per JSON object to obey JSON syntax.
- `"criteria_section_X"` - JSON object that is a grading section. These sections can be named anything other than `"comment"`, but must be unique. These sections **must** contain:
  - `"grading_criteria"` - JSON object that contains the grading criteria for the section. This object must be named `"grading_criteria"` and contain at least one grading criteria. Criteria will be JSON objects with an integer value within named `"required_count"`.
  - `"element_X"` - JSON object that is a grading element. These elements can be named anything other than `"comment"`, `"grading_criteria"`, or an already existing element name in the section. These elements will contain:
    - `"spreadsheet_cell"` - The cell reference in the student submission Excel file to be graded. This cell reference must be a valid Excel cell reference.
    - `"simple_value"` - A simple value that will be compared to the value in the spreadsheet cell.
    - `"computed_value"` - *(optional)* A computed value that will be calculated using the value in the spreadsheet cell. This value must be a valid Python expression and can use the value of the spreadsheet cell as a variable.
    - `"value_min"` and `"value_max"` - *(optional)* A range of values that will be compared to the value in the spreadsheet cell.
    - `"value_tolerance"` - *(optional)* An optional tolerance for the value comparison.


### Important things to note:
- Each criteria section must have a `"grading_criteria"` element.
- Elements can either have `"simple_value"`, `"computed_value"`, or both `"value_min"` and `"value_max"`, but cannot have more than one of these at the same time.
- When using `"computed_value"` or `"simple_value"`, the `"value_tolerance"` element is able to be used and optional. 
- The `"spreadsheet_cell"` element must be a valid Excel cell reference. Sheetname is optional.

### final_grades.xlsx
This will be the general structure of the final grades Excel file:

| Student Filename   | criteria_section_1   | score        | comment | criteria_section_2  | score      | comment                                                             | criteria_section_3 | score        | comment                                                                  |
|--------------------|----------------------|--------------|---------|---------------------|------------|---------------------------------------------------------------------|--------------------|--------------|--------------------------------------------------------------------------|
| student_file1.xlsx | criteria_section_1   | proficient   |         | criteria_section_2  | proficient |                                                                     | criteria_section_3 | proficient   |                                                                          |
| student_file2.xlsx | criteria_section_1   | proficient   |         | criteria_section_2  | novice     | Your value for element 1 was out of tolerance, expected 2 but got 0 | criteria_section_3 | insufficient | Your value for element 1 was out of tolerance, expected 0 to 1 but got 3 |

- `Student Filename` will be the name of the student file.
- `criteria_section_X` will be the name of the grading section.
- comments can be empty if there are no issues with the grading.
- `score` will be the name of the grading criteria bracket met by the student score

## Packages Used
This project uses the following packages:
- `pandas` - Data manipulation
- `openpyxl` - Excel file manipulation'

## Authors/Collaborators
- Samuel Wilhite - Full project code
- Doug Sandy - Project Commissioner/Spreadsheet Design

## Future Improvements
- None at this moment