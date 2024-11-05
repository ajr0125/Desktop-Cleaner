# Import necessary libraries - os for reading file directories, shutil for copying/moving files,
# tkinter for GUI creation, messagebox for messages boxes in gui
import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Dictionary to categorize file types
file_categories = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Compressed": [".zip", ".tar", ".rar"],
    "Code": [".py", ".js", ".java", ".cpp", ".html", ".css"],
    "Others": []
}

class DesktopCleaner:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.title("Desktop Cleaner")

        # Label to prompt the user
        self.label = tk.Label(master, text="Choose how to organize your files:")
        self.label.pack(pady=10)

        # Button to organize files by type
        self.type_button = tk.Button(master, text="Organize by File Type", command=self.organize_by_type)
        self.type_button.pack(pady=5)

        # Button to organize files by size
        self.size_button = tk.Button(master, text="Organize by Size", command=self.organize_by_size)
        self.size_button.pack(pady=5)

        # Button to organize files by last modified date
        self.date_button = tk.Button(master, text="Organize by Date", command=self.organize_by_date)
        self.date_button.pack(pady=5)

        # Button to quit the application
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_application)
        self.quit_button.pack(pady=20)

    def quit_application(self):
        # Closes the GUI window
        self.master.destroy()

    def organize_by_type(self):
        # Trigger organization by file type
        self.organize_files(key='type')
    
    def organize_by_size(self):
        # Trigger organization by file size
        self.organize_files(key='size')
    
    def organize_by_date(self):
        # Trigger organization by last modified date
        self.organize_files(key='date')

    def organize_files(self, key):
        # Get the path to the user's desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        # List all files in the desktop directory
        files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

        if key == 'type':
            # Organize files into categories based on file extensions
            folders = {category: [] for category in file_categories.keys()}
            for file in files:
                # Get the file extension
                _, file_extension = os.path.splitext(file)
                # Determine the appropriate category based on the file extension
                categorized = False
                for category, extensions in file_categories.items():
                    if file_extension.lower() in extensions:
                        folders[category].append(file)
                        categorized = True
                        break
                if not categorized:
                    folders["Others"].append(file)  # Add to Others if not categorized

            # Create folders and move files into corresponding category folders
            for folder, files in folders.items():
                folder_path = os.path.join(desktop_path, folder)
                # Create folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)  
                for file in files:
                    # Move file
                    shutil.move(os.path.join(desktop_path, file), os.path.join(folder_path, file))

            messagebox.showinfo("Success", "Files organized by type.")

        elif key == 'size':
            # Organize files by size categories: Small, Medium, Large
            folders = {'Small': [], 'Medium': [], 'Large': []}
            for file in files:
                file_size = os.path.getsize(os.path.join(desktop_path, file))
                # Less than 1 MB
                if file_size < 1024 * 1024:  
                    folders['Small'].append(file)
                # Less than 10 MB
                elif file_size < 10 * 1024 * 1024:  
                    folders['Medium'].append(file)
                # Larger than 10 MB
                else:
                    folders['Large'].append(file)

            # Create folders and move files into corresponding size folders
            for folder, files in folders.items():
                folder_path = os.path.join(desktop_path, folder)
                # Create folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)  
                for file in files:
                    # Move file
                    shutil.move(os.path.join(desktop_path, file), os.path.join(folder_path, file))  

            messagebox.showinfo("Success", "Files organized by size.")

        elif key == 'date':
            # Organize files by their last modified date
            folders = {}
            for file in files:
                modified_time = os.path.getmtime(os.path.join(desktop_path, file))
                folder_name = 'Recent' if modified_time > (os.path.getmtime(desktop_path) - 30 * 86400) else 'Old'
                if folder_name not in folders:
                    folders[folder_name] = []
                folders[folder_name].append(file)

            # Create folders and move files based on their modified date
            for folder, files in folders.items():
                folder_path = os.path.join(desktop_path, folder)
                # Create folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)  
                for file in files:
                    # Move file
                    shutil.move(os.path.join(desktop_path, file), os.path.join(folder_path, file))  

            messagebox.showinfo("Success", "Files organized by date.")

if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    # Initialize DesktopCleaner application
    app = DesktopCleaner(root)
    # Run Tkinter event loop
    root.mainloop()  
