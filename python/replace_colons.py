import os
import argparse


def replace_colons(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            original_path = os.path.join(foldername, filename)
            new_filename = filename.replace(":", "_")  # Replace ':' with '_'

            if new_filename != filename:
                new_path = os.path.join(foldername, new_filename)
                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} -> {new_path}")


if __name__ == "__main__":
    target_directory = None
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "target_directory", type=str, help="Target directory for replace"
    )
    args = parser.parse_args()
    if target_directory:
        replace_colons(target_directory)
