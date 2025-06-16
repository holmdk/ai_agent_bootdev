import sys
import os
from google.genai import types

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from call_function import call_function

def extract_result(content: types.Content | str) -> str:
    """
    Extract the result from a Content object or return the error string.

    Args:
        content: A Content object or error string.

    Returns:
        The extracted result as a string.
    """
    if isinstance(content, str):
        return content

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

def test_extract_result():
    """Test the extract_result function with different inputs."""
    # Test with a string input
    result = extract_result("Error: Test error")
    print("\nResult of extract_result with string input:")
    print(result)
    assert result == "Error: Test error"

    # Test with None input
    result = extract_result(None)
    print("\nResult of extract_result with None input:")
    print(result)
    assert result == "No result found"

    # Test with a Content object that has a result
    content = types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name="test_function",
                response={"result": "Test result"}
            )
        ]
    )
    result = extract_result(content)
    print("\nResult of extract_result with result Content:")
    print(result)
    assert result == "Test result"

    # Test with a Content object that has an error
    content = types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name="test_function",
                response={"error": "Test error"}
            )
        ]
    )
    result = extract_result(content)
    print("\nResult of extract_result with error Content:")
    print(result)
    assert result == "Error: Test error"


if __name__ == "__main__":
    print("Testing call_function.py...")
    test_get_file_content()
    test_get_files_info()
    test_non_existent_function()
    test_extract_result()
    print("\nTests completed.")
