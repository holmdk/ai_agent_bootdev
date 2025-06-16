import sys
import os
from google.genai import types

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.call_function import call_function

def extract_result(content):
    """Extract the result from a Content object."""
    if not content or not content.parts or not content.parts[0].function_response:
        return "No result found"

    response = content.parts[0].function_response.response
    if 'result' in response:
        return response['result']
    elif 'error' in response:
        return f"Error: {response['error']}"
    else:
        return f"Unknown response format: {response}"

def test_get_file_content():
    # Create a FunctionCall object for get_file_content
    function_call_part = types.FunctionCall(
        name="get_file_content",
        args={
            "file_path": "pkg/calculator.py"
        }
    )

    # Call the function
    result = call_function(function_call_part, verbose=True)
    print("\nResult of get_file_content:")
    content = extract_result(result)
    # Print first 200 characters of the content
    print(content[:200] + "..." if len(content) > 200 else content)

def test_get_files_info():
    # Create a FunctionCall object for get_files_info
    function_call_part = types.FunctionCall(
        name="get_files_info",
        args={
            "directory": "pkg"
        }
    )

    # Call the function
    result = call_function(function_call_part, verbose=True)
    print("\nResult of get_files_info:")
    print(extract_result(result))

def test_non_existent_function():
    # Create a FunctionCall object for a non-existent function
    function_call_part = types.FunctionCall(
        name="non_existent_function",
        args={
            "param": "value"
        }
    )

    # Call the function
    result = call_function(function_call_part, verbose=True)
    print("\nResult of non_existent_function:")
    print(extract_result(result))

if __name__ == "__main__":
    print("Testing call_function.py...")
    test_get_file_content()
    test_get_files_info()
    test_non_existent_function()
    print("\nTests completed.")
