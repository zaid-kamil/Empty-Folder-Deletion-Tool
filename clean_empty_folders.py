import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def verify_path(path):
    if not os.path.exists(path):
        messagebox.showerror("Error", f"Path '{path}' does not exist.")
        return False
    if not os.path.isdir(path):
        messagebox.showerror("Error", f"'{path}' is not a directory.")
        return False
    return True

def list_empty_folders(path):
    empty_folders = []
    for folder, _, _ in os.walk(path, topdown=False):
        if not os.listdir(folder):
            empty_folders.append(folder)
    return empty_folders

def delete_empty_folders(path, empty_folders):
    for folder in empty_folders:
        os.rmdir(folder)
        print(f"Deleted empty folder: {folder}")

def browse_folder():
    selected_path = filedialog.askdirectory()
    if selected_path and verify_path(selected_path):
        empty_folders = list_empty_folders(selected_path)
        if not empty_folders:
            messagebox.showinfo("Info", "No empty folders found.")
        else:
            response = messagebox.askquestion("Confirmation", "The following folders are empty:\n\n"
                                             + "\n".join(empty_folders) + "\n\nDo you want to delete them?")
            if response == "yes":
                delete_empty_folders(selected_path, empty_folders)
                messagebox.showinfo("Info", "Empty folders deleted.")
    
# Create a Tkinter GUI window
root = tk.Tk()
root.title("Empty Folder Deletion")
# Set the window size
root.geometry("300x100")
# Set the window background color
root.config(background='white')
# add a header in the center of the window
header = tk.Label(root, text="Select a folder to delete empty folders")
header.pack()
# Create a button to browse for the folder
browse_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack()

# Start the Tkinter main loop
root.mainloop()
