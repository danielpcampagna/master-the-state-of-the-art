import os
import shutil
from glob import glob
import re

def copy_markdown_files_with_category_ok(markdown_files, target_folder):
    """
    Copies Markdown files containing 'category: ok' to the target folder.

    Parameters:
    - markdown_files: List of paths to Markdown files.
    - target_folder: Path to the directory where matching files will be copied.
    """
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    for file_path in markdown_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                match = re.search(r'category: (\w+)', content, re.IGNORECASE)
                if match:
                    category = match.group(1)
                    target_folder_category = os.path.join(target_folder, category)
                    os.makedirs(target_folder_category, exist_ok=True)
                    shutil.copy(file_path, target_folder_category)
                    print(f"Copied: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    # List of Markdown file paths to check
    markdown_files = glob('../obsidian/works/*.md')

    # Target directory to copy matching files into
    target_folder = './extract_category_ok_works/works'
    os.makedirs(target_folder, exist_ok=True)

    copy_markdown_files_with_category_ok(markdown_files, target_folder)
