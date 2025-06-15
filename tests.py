"""
Test script for file operations functions.

This script tests the functionality of get_file_content, get_files_info, and write_file functions.
Uncomment specific tests as needed.
"""

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file


if __name__ == '__main__':
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
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))  # Should return an error for security reasons
