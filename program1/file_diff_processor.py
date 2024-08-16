import os
import shutil


# Function to extract file names and statuses
def process_file_diff(file_diff_path):
    modified_added = []
    renamed_deleted = []

    with open(file_diff_path, 'r') as file_diff:
        for line in file_diff:
            parts = line.split()  # Split using whitespace
            if len(parts) == 2:
                status, filepath = parts
                filepath = filepath.strip()
                filename = os.path.basename(filepath)

                if status in ("M", "A"):
                    modified_added.append((filename, filepath))
                elif status in ("R", "D"):
                    renamed_deleted.append((filename, filepath))
    return modified_added, renamed_deleted


# Function to copy/move files to the appropriate folders
def copy_files_to_destination(file_list, destination_folder):
    deploy_base = "deployPackage"
    if not os.path.exists(deploy_base):
        os.makedirs(deploy_base)

    for file, source_path in file_list:
        destination_dir = os.path.join(deploy_base, destination_folder)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        destination_path = os.path.join(destination_dir, file)
        print({source_path})
        if os.path.exists(source_path):
            print(f"Copying {file} from {source_path} to {destination_path}")
            shutil.copy2(source_path, destination_path)
        else:
            print(f"Source file {file} not found at {source_path}")

# Process the file_diff.txt
file_diff_path = "C:/Users/Faiz/file_diff.txt"
modified_added, renamed_deleted = process_file_diff(file_diff_path)

# Copy files to the appropriate destination folders
copy_files_to_destination(modified_added, "added")
copy_files_to_destination(renamed_deleted, "removed")