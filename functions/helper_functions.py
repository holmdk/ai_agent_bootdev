import os
from typing import Tuple


def extract_absolute_paths(file_path: str, working_directory: str) -> Tuple[str, str]:
    """
    Convert file path and working directory to absolute paths.

    Args:
        file_path: The path to the file, can be relative or absolute.
        working_directory: The base directory for relative paths.

    Returns:
        A tuple containing (absolute_file_path, absolute_working_directory).
    """
    # Handle the case where file_path is a relative path
    if not os.path.isabs(file_path):
        full_file_path = os.path.join(working_directory, file_path)
    else:
        full_file_path = file_path

    # Convert both paths to absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(full_file_path)

    return abs_file_path, abs_working_dir
