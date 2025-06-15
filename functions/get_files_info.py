import os
from typing import List, Optional

from functions.helper_functions import extract_absolute_paths


def formatter(file_name: str, file_size: int, is_dir: bool) -> str:
    """
    Format file information into a readable string.

    Args:
        file_name: The name of the file or directory.
        file_size: The size of the file in bytes.
        is_dir: Whether the item is a directory.

    Returns:
        A formatted string with file information.
    """
    return f"- {file_name}: file_size={file_size}, is_dir={is_dir}\n"


def get_files_info(working_directory: str, directory: Optional[str] = None) -> str:
    """
    Get information about files in a directory within the permitted working directory.

    Args:
        working_directory: The base directory that contains the target directory.
        directory: The path to the directory to list, relative to the working directory or absolute.
                  If None, defaults to the working directory itself.

    Returns:
        A string containing information about each file in the directory,
        or an error message if the directory cannot be accessed.
    """
    try:
        # If directory is None, use "." to represent the current directory
        if directory is None:
            directory = "."

        abs_directory, abs_working_dir = extract_absolute_paths(directory, working_directory)

        # Check if the directory is outside the working directory
        if not abs_directory.startswith(abs_working_dir + os.path.sep) and abs_directory != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if the directory exists and is a directory
        if not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'

        # Use the absolute directory path for listing files
        files = os.listdir(abs_directory)
        contents: List[str] = []

        for file_name in files:
            # Create the full path for the file
            file_path = os.path.join(abs_directory, file_name)

            # Check if it's a directory
            is_dir = os.path.isdir(file_path)

            # Get the file size
            file_size = os.path.getsize(file_path)

            # Add the formatted information to contents
            contents.append(formatter(file_name, file_size, is_dir))

        # Join all the formatted strings and return
        return ''.join(contents)

    except Exception as e:
        return f"Error: {e}"
