import os
import shutil
import re

# Define source and destination directories
source_dir = "/media/appsmartz/storage/annotation/Kartik_Codes/Todays_18/"  # Change this to your source directory
destination_dir = "/media/appsmartz/storage/annotation/Kartik_Codes/guitar/"  # Change this to your destination directory
error_log = "/media/appsmartz/storage/annotation/erroe.txt"  # File to store directories that caused errors

# Function to check if a file matches the pattern
def matches_pattern(filename):
    return re.match(r"^Guitar\d.wav", filename) is not None

# Open the error log file
with open(error_log, "w") as log_file:
    log_file.write("Folders where errors occurred:\n")

    # Loop through each subdirectory in the source directory
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)

        if os.path.isdir(subdir_path):  # Check if it is a directory
            try:
                found_match = False  # Flag to check if any matching file is found
                
                # Loop through all files in the subdirectory
                for file in os.listdir(subdir_path):
                    if matches_pattern(file):  # Check if the file matches the pattern
                        found_match = True
                        break  # Stop searching if at least one match is found
                
                # Copy the whole directory if at least one matching file was found
                if found_match:
                    dest_path = os.path.join(destination_dir, subdir)
                    
                    if not os.path.exists(dest_path):  # Ensure it doesn’t overwrite
                        shutil.copytree(subdir_path, dest_path)
                        print(f"Copied directory: {subdir_path} to {dest_path}")

            except Exception as e:
                # Log the directory where an error occurred
                log_file.write(f"{subdir} - Error: {str(e)}\n")
                print(f"Error in directory: {subdir}. Logged in {error_log}.")
