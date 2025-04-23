from tkinter import filedialog, Tk

def get_all_paths() -> [str, str, str]:
    """
    Use Tkinter to open a file dialog and select the student folder, JSON file, and result location.
    :return: [str, str, str] - The selected folder path, file path, and where to place the results.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Student Folder")
    file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])
    result_location = filedialog.askdirectory(title="Select Folder to Place Results")
    root.destroy()

    return folder_path, file_path, result_location




if __name__ == "__main__":
    # student_folder_path = get_student_folder_path()
    # print(f"Selected folder: {student_folder_path}")
    folder, file, result = get_all_paths()
    print(f"Selected folder: {folder}")
    print(f"Selected file: {file}")
    print(f"Selected result folder: {result}")