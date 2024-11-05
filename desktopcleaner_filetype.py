# Import necessary libraries - os for reading file directories, shutil for copying/moving files
import os
import shutil

# Define the path to your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# File type categories and their folders
file_categories = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Compressed": [".zip", ".tar", ".rar"],
    "Code": [".py", ".js", ".java", ".cpp", ".html", ".css"],
    "Others": []
}

# Create folders if they don't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move a file to the appropriate folder
def move_file(file, desktop_path, category_folder):
    # Constructs full file path on desktop and destination (where filed is moved to)
    source_path = os.path.join(desktop_path, file)
    destination_path = os.path.join(desktop_path, category_folder, file)

    # If directory doesn't already exist, make it
    if not os.path.exists(os.path.dirname(destination_path)):
        os.makedirs(os.path.dirname(destination_path))

    # Move file to the destination folder
    shutil.move(source_path, destination_path)

# Organize files based on their extension
def organize_files():
    # Iterate over all files and directories in desktop_path
    for file in os.listdir(desktop_path):
        # Skip system files and folders
        if file.startswith('.'):
            continue
        if os.path.isdir(os.path.join(desktop_path, file)):
            continue

        # Extract file extension
        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        # Check if file matches any category and move it accordingly
        for category, extensions in file_categories.items():
            if file_ext in extensions:
                move_file(file, desktop_path, category)
                moved = True
                break

        # If file does not match any category, move it to "Others"
        if not moved:
            move_file(file, desktop_path, "Others")

# Run the organizer
organize_files()
