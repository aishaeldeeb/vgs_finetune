import os
import shutil
from pathlib import Path

# Function to copy files and ensure integrity
def organize_and_validate_files(dataset_dir, output_dir):
    # Define input folders
    folders = ['train', 'val', 'test']

    # Define output folders
    audio_dir = Path(output_dir) / 'audio'
    frames_dir = Path(output_dir) / 'frames'
    audio_dir.mkdir(parents=True, exist_ok=True)
    frames_dir.mkdir(parents=True, exist_ok=True)

    # Iterate through each folder
    for folder in folders:
        folder_path = Path(dataset_dir) / folder

        if not folder_path.exists():
            print(f"Skipping missing folder: {folder_path}")
            continue

        for file in folder_path.iterdir():
            # Determine file type and destination
            if file.suffix == '.wav':
                dest_dir = audio_dir
            elif file.suffix == '.png':
                dest_dir = frames_dir
            else:
                # Skip unrelated files
                continue

            # Copy file
            dest_file = dest_dir / file.name
            shutil.copy2(file, dest_file)

            # Validate file integrity
            if not dest_file.exists() or os.path.getsize(dest_file) == 0:
                print(f"Warning: Failed to copy {file} to {dest_file}")
            else:
                print(f"Successfully copied {file} to {dest_file}")

if __name__ == "__main__":
    dataset_dir = "./dataset"  # Update with the actual path to your dataset
    output_dir = "./organized_dataset"  # Define where to store organized files

    organize_and_validate_files(dataset_dir, output_dir)
    print("File organization completed.")
