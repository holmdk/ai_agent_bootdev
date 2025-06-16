import os

from google.genai import types

from functions.helper_functions import extract_absolute_paths


def get_file_content(working_directory: str, file_path: str) -> str:
    """
    Read and return the content of a file within the permitted working directory.

    Args:
        working_directory: The base directory that contains the file.
        file_path: The path to the file, relative to the working directory or absolute.

    Returns:
        The content of the file as a string, or an error message if the file cannot be read.
        Files larger than 10000 characters will be truncated.
    """
    try:
        abs_file_path, abs_working_dir = extract_absolute_paths(file_path, working_directory)

        # Check if the file is within the permitted working directory
        if not abs_file_path.startswith(abs_working_dir + os.path.sep) and abs_file_path != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if the file_path exists and is a file
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file and return its contents as a string
        # If the file is longer than MAX_CHARS, truncate it and append a message
        MAX_CHARS = 10000

        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            is_truncated = len(file_content_string) == MAX_CHARS

            if is_truncated:
                # Check if there's more content by trying to read one more character
                if f.read(1):
                    return file_content_string + f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read and return the content of a file within the permitted working directory, files larger than 10000 characters will be truncated.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The base directory that contains the file."
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory or absolute.",
            )
        },
    ),
)

