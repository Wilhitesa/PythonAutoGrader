"""
Name: file_retrieval.py
Author: Samuel Wilhite
Date: 04/29/2025
Description: This file is for GUI file selection.
"""
from tkinter import filedialog, Tk

def get_all_paths() -> tuple[str, str, str]:
    """
    Use Tkinter to open a file dialog and select the student folder, JSON file, and result location.
    :return: The selected folder path, file path, and where to place the results.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Student Folder")
    file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])
    result_location = filedialog.askdirectory(title="Select Folder to Place Results")
    root.destroy()

    return folder_path, file_path, result_location

if __name__ == "__main__":
    folder, file, result = get_all_paths()
    print(f"Selected folder: {folder}")
    print(f"Selected file: {file}")
    print(f"Selected result folder: {result}")