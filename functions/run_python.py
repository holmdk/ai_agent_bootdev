"""
Python file execution module.

This module provides functionality to safely execute Python files
within a permitted working directory, with safeguards against
executing files outside the allowed scope.
"""

import os
import subprocess
from typing import Any

from google.genai import types

from functions.helper_functions import extract_absolute_paths


def run_python_file(working_directory: str, file_path: str) -> str:
    """
    Execute a Python file and capture its output.

    This function runs a Python file specified by file_path within the context of 
    the working_directory. It captures and returns the standard output, standard error,
    and exit code of the executed Python process.

    Args:
        working_directory (str): The directory to use as the working directory for execution.
        file_path (str): The path to the Python file to execute, relative to working_directory.

    Returns:
        str: A formatted string containing the output of the executed Python file.
             This includes stdout, stderr, and exit code information if applicable.
             Returns an error message if execution fails or if the file is outside
             the permitted working directory.

    Raises:
        No exceptions are raised as they are caught and returned as error messages.
    """
    TIMEOUT = 30
    try:
        abs_file_path, abs_working_dir = extract_absolute_paths(file_path, working_directory)

        # Check if the file is within the permitted working directory
        if not abs_file_path.startswith(abs_working_dir + os.path.sep) and abs_file_path != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if the file_path exists and is a file
        if not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        # If the file doesn't end with ".py", return an error string:
        if not str(file_path).endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

        try:
            result = subprocess.run(["python", abs_file_path], cwd=abs_working_dir, capture_output=True, timeout=TIMEOUT, text=True)

            # Format the output
            output_parts = []

            # Add stdout if it exists
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")

            # Add stderr if it exists
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")

            # Add exit code message if non-zero
            if result.returncode != 0:
                output_parts.append(f"Process exited with code {result.returncode}")

            # If no output was produced
            if not output_parts:
                return "No output produced."

            # Join all parts with newlines
            return "\n".join(output_parts)
        except Exception as e:
            return f"Error: executing Python file: {e}"

    except Exception as e:
        return f"Error: {e}"


# Schema definition for the function to be used with Google's Generative AI API
schema_run_python_file: types.FunctionDeclaration = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file and capture its output within the permitted working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to use as the working directory for execution."
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to working_directory.",
            )
        },
    ),
)
