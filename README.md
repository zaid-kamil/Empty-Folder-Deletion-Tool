# Empty Folder Deletion Tool

## Overview

The Empty Folder Deletion Tool is a simple utility program designed to help you identify and remove empty folders within a selected directory. Empty folders can accumulate over time, cluttering your file system, and this tool provides an easy way to maintain a clean and organized directory structure.

![Empty Folder Deletion Tool](images/empty_folder_deletion_tool.png)

## Features

- Browse for a directory: Use the "Browse Folder" button to select a directory where you want to identify and remove empty folders.
- Verify selected path: The tool checks if the selected path exists and if it's a valid directory before proceeding.
- List empty folders: It identifies and lists all the empty folders within the selected directory.
- Confirm and delete: After listing the empty folders, you have the option to confirm the deletion. A confirmation dialog will show the list of empty folders for your review before deletion.
- Deleted folders: The tool will delete the empty folders upon confirmation and provide a notification with information about the folders removed.

## Requirements

- Python: The Empty Folder Deletion Tool is written in Python and requires Python to be installed on your system.
- Tkinter: Tkinter is a standard Python interface for creating graphical user interfaces (GUIs). It is included with most Python installations.

## How to Use

1. Launch the program by running `empty_folder_deletion.py`.
2. Click the "Browse Folder" button to select the directory where you want to search for and delete empty folders.
3. The tool will list the empty folders within the selected directory.
4. Review the list and confirm if you want to delete the empty folders.
5. The tool will remove the empty folders and provide a confirmation message.

## Benefits

- **Organization:** Maintain a clean and organized file system by removing unnecessary empty folders.
- **Efficiency:** Save time by automating the process of identifying and deleting empty folders.
- **Ease of Use:** The user-friendly graphical interface makes it easy for users of all levels of experience.

![Empty Folder Deletion List](images/empty_folder_deletion_confirmation.png)

## To-Do List

Here's a list of features and improvements that we plan to add to the Empty Folder Deletion Tool:

- [ ] Implement a progress bar to track the deletion process.
- [ ] Add the ability to specify file extensions for deletion (e.g., delete empty folders only if they contain specific file types).
- [ ] Improve error handling and provide more informative error messages.
- [ ] Allow users to set a maximum folder depth for scanning (avoid deep nested folders).
- [ ] Create a log file to keep a record of deleted folders and any errors.
- [ ] Implement an option to move deleted folders to a backup directory instead of permanent deletion.

If you're interested in contributing to the project or have suggestions for additional features, feel free to open an issue or submit a pull request.

## Contributions

Contributions to this tool are welcome. If you have suggestions or want to enhance its functionality, feel free to submit a pull request.

## License

This tool is distributed under the [GPL License](https://www.gnu.org/licenses/gpl-3.0.txt).
