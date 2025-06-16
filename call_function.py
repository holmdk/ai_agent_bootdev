"""
Function calling module for the AI Code Assistant.

This module provides functionality to call external functions based on AI model requests.
"""

import json
import subprocess

from google.genai import types

from functions.get_file_content import get_file_content, schema_get_file_content
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.run_python import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

def call_function(function_call_part: types.FunctionCall, verbose: bool = False) -> types.Content | str:
    """
    Call a function based on the function call part from the AI model.

    Args:
        function_call_part: The function call part from the AI model.
        verbose: Whether to print verbose output.

    Returns:
        A Content object with the function response or an error string.

    Raises:
        Exception: If there's an error in function execution.
    """
    function_call_part = types.FunctionCall(
        name=function_call_part.name,
        args=function_call_part.args,
    )

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    # Dictionary mapping function names to their corresponding functions
    function_map = {
        "get_file_content": get_file_content,
        "write_file": write_file,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file
    }

    # Get the function from the dictionary
    func = function_map.get(function_call_part.name)

    if func is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    # Parse the arguments
    try:
        # Convert the args string to a dictionary
        if isinstance(function_call_part.args, str):
            args_dict = json.loads(function_call_part.args)
        else:
            args_dict = function_call_part.args

        # Add the working_directory argument
        args_dict["working_directory"] = "./calculator"

        # Call the function with the arguments
        function_result = func(**args_dict)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    except Exception as e:
        return f"Error: {str(e)}"
