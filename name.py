import os

def rename_txt_to_md(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                txt_file_path = os.path.join(root, file)
                md_file_path = os.path.splitext(txt_file_path)[0] + ".md"
                os.rename(txt_file_path, md_file_path)
                print(f"Renamed: {txt_file_path} -> {md_file_path}")

# Specify the root directory to start renaming files
root_directory = "D:\GitHub\ILP-Python"  # Replace with your directory path
rename_txt_to_md(root_directory)
