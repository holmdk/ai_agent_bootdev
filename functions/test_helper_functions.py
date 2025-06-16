"""
Unit tests for the helper_functions module.

This module contains tests for the utility functions that handle file paths.
"""

import os
import unittest
from pathlib import Path

from functions.helper_functions import extract_absolute_paths


class TestHelperFunctions(unittest.TestCase):
    """Test suite for the helper_functions module."""

    def setUp(self) -> None:
        """Set up test environment with temporary paths."""
        # Use a known base directory for testing
        self.working_dir = "/tmp/test_working_dir"
        
        # Create some test paths
        self.rel_path = "subdir/test_file.txt"
        self.abs_path = "/tmp/test_working_dir/subdir/test_file.txt"
        self.outside_path = "/etc/passwd"

    def test_extract_absolute_paths_relative(self) -> None:
        """Test that relative paths are correctly converted to absolute paths."""
        abs_file_path, abs_working_dir = extract_absolute_paths(self.rel_path, self.working_dir)
        
        # Convert to Path objects to handle platform-specific path separators
        expected_file_path = Path(os.path.abspath(os.path.join(self.working_dir, self.rel_path)))
        actual_file_path = Path(abs_file_path)
        
        expected_working_dir = Path(os.path.abspath(self.working_dir))
        actual_working_dir = Path(abs_working_dir)
        
        self.assertEqual(actual_file_path, expected_file_path)
        self.assertEqual(actual_working_dir, expected_working_dir)

    def test_extract_absolute_paths_absolute(self) -> None:
        """Test that absolute paths are handled correctly."""
        abs_file_path, abs_working_dir = extract_absolute_paths(self.abs_path, self.working_dir)
        
        # Convert to Path objects to handle platform-specific path separators
        expected_file_path = Path(os.path.abspath(self.abs_path))
        actual_file_path = Path(abs_file_path)
        
        expected_working_dir = Path(os.path.abspath(self.working_dir))
        actual_working_dir = Path(abs_working_dir)
        
        self.assertEqual(actual_file_path, expected_file_path)
        self.assertEqual(actual_working_dir, expected_working_dir)

    def test_extract_absolute_paths_outside(self) -> None:
        """Test that paths outside the working directory are handled correctly."""
        abs_file_path, abs_working_dir = extract_absolute_paths(self.outside_path, self.working_dir)
        
        # The function should still return the absolute paths, even if the file is outside
        # the working directory (it's up to the calling function to check this)
        expected_file_path = Path(os.path.abspath(self.outside_path))
        actual_file_path = Path(abs_file_path)
        
        expected_working_dir = Path(os.path.abspath(self.working_dir))
        actual_working_dir = Path(abs_working_dir)
        
        self.assertEqual(actual_file_path, expected_file_path)
        self.assertEqual(actual_working_dir, expected_working_dir)


if __name__ == "__main__":
    unittest.main()