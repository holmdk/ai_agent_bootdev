import os

from functions.helper_functions import extract_absolute_paths


def write_file(working_directory: str, file_path: str, content: str) -> str:
    """
    Write content to a file within the permitted working directory.

    Args:
        working_directory: The base directory that contains or will contain the file.
        file_path: The path to the file, relative to the working directory or absolute.
        content: The content to write to the file.

    Returns:
        A success message with the number of characters written or an error message.
    """
    try:
        abs_file_path, abs_working_dir = extract_absolute_paths(file_path, working_directory)

        # Check if the file is within the permitted working directory
        if not abs_file_path.startswith(abs_working_dir + os.path.sep) and abs_file_path != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if the directory for the file exists and create it if not
        directory = os.path.dirname(abs_file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Overwrite the contents of the file with the content argument
        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
