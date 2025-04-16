from tkinter import filedialog, Tk

def get_student_folder_path() -> str:
    """
    Opens a file dialog to select a folder and returns the selected folder path.
    :return: str - The path of the selected folder.
    """
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Student Folder")
    root.destroy()
    return folder_path

if __name__ == "__main__":
    student_folder_path = get_student_folder_path()
    print(f"Selected folder: {student_folder_path}")