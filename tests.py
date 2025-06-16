"""
Test script for file operations functions.

This script tests the functionality of get_file_content, get_files_info, write_file, 
and run_python_file functions. Uncomment specific tests as needed.
"""
import os

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
import subprocess

if __name__ == '__main__':
    pass
    # Tests for get_files_info function
    # print(get_files_info("calculator", "."))
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator", "/bin"))  # Should return an error for security reasons
    # print(get_files_info("calculator", "../"))   # Should return an error for security reasons

    # Tests for get_file_content function
    # print(get_file_content("calculator", "lorem.txt"))
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))  # Should return an error for security reasons

    # Tests for write_file function
    #print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    #print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    #print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))  # Should return an error for security reasons

    # Tests for run_python_file function
    #print(run_python_file("calculator", "main.py"))  # Test running a valid Python file
    #print(run_python_file("calculator", "tests.py"))  # Test running the tests file itself
    #print(run_python_file("calculator", "../main.py"))  # Test path traversal (should return an error)
    #print(run_python_file("calculator", "nonexistent.py"))  # Test nonexistent file (should return an error)

    #print(subprocess.run(
    #    ['python', 'main.py', 'read the contents of main.py'],
    #    capture_output=True,
    #    cwd=os.path.dirname(__file__),
    #    text=True,
    #).stdout)   #-->  get_file_content({'file_path': 'main.py'})

    #print(subprocess.run(
    #    ['python', 'main.py', "write 'hello' to main.txt"],
    #    capture_output=True,
    #    cwd=os.path.dirname(__file__),
    #    text=True,
    #).stdout)   #  -> write_file({'file_path': 'main.txt', 'content': 'hello'})

    #print(subprocess.run(
    #    ['python', 'main.py', "run main.py"],
    #    capture_output=True,
    #    cwd=os.path.dirname(__file__),
    #    text=True,
    #).stdout) # run_python_file({'file_path': 'main.py'})

    #print(subprocess.run(
    #    ['python', 'main.py', "list the contents of the pkg directory"],
    #    capture_output=True,
    #    cwd=os.path.dirname(__file__),
    #    text=True,
    #).stdout)  # -> get_files_info({'directory': 'pkg'})