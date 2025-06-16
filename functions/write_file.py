"""
File writing module.

This module provides functionality to safely write content to files
within a permitted working directory, with safeguards against
writing to files outside the allowed scope.
"""

import os
from typing import Any

from google.genai import types

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


# Schema definition for the function to be used with Google's Generative AI API
schema_write_file: types.FunctionDeclaration = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file within the permitted working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base directory that contains or will contain the file."
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory or absolute.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            )
        },
    ),
)
