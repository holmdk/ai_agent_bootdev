# AI Agent Development Toolkit

This repository contains a collection of tools and utilities for AI agent development, including:

1. A command-line calculator application
2. File operation utilities for secure file access
3. A Gemini AI interaction tool

## Components

### 1. Calculator Application

A command-line calculator that evaluates mathematical expressions and displays results in a decorative box.

#### Features
- Evaluates basic arithmetic expressions (+, -, *, /)
- Handles operator precedence correctly
- Displays results in a visually appealing format

### 2. File Operations Utilities

A set of functions for secure file operations within a permitted working directory.

#### Features
- Reading file contents with security checks
- Writing content to files with directory creation
- Listing files and directories with detailed information

### 3. Gemini AI Interaction Tool

A simple command-line tool to interact with the Gemini AI model.

#### Features
- Simple command-line interface
- Direct interaction with Gemini 2.0 Flash model
- Optional verbose mode for detailed information about token usage

## Prerequisites

- Python 3.6 or higher
- A Gemini API key

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd ai_agent_bootdev
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

   Alternatively, if you're using a modern Python setup:
   ```
   pip install python-dotenv google-generativeai
   ```

3. Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### 1. Calculator Application

Run the calculator from the `calculator` directory:

```
cd calculator
python main.py "3 + 4 * 2"
```

This will display a nicely formatted result:
```
┌──────────────┐
│  3 + 4 * 2   │
│              │
│  =           │
│              │
│  11          │
└──────────────┘
```

### 2. File Operations Utilities

These utilities can be imported and used in your Python scripts:

```python
# Reading file content
from functions.get_file_content import get_file_content
content = get_file_content("working_directory", "path/to/file.txt")

# Writing to a file
from functions.write_file import write_file
result = write_file("working_directory", "path/to/file.txt", "File content")

# Listing files in a directory
from functions.get_files_info import get_files_info
files_info = get_files_info("working_directory", "path/to/directory")
```

You can also run the test script to see these functions in action:
```
python tests.py
```

### 3. Gemini AI Interaction Tool

Basic usage:
```
python main.py "Your prompt here"
```

With verbose output:
```
python main.py "Your prompt here" --verbose
```

#### Command Line Arguments

- First argument (required): The prompt to send to the Gemini model
- `--verbose` (optional): Display additional information including:
  - The user's prompt
  - Number of prompt tokens used
  - Number of response tokens generated

#### Example

```
python main.py "What is the meaning of life?" --verbose
```

This will display:
```
User prompt: What is the meaning of life?
Prompt tokens: <number>
Response tokens: <number>
<Gemini's response>
```

## Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key (required)

## Dependencies

- `python-dotenv`: For loading environment variables
- `google-generativeai`: Google's official Python library for Gemini AI

## License

[Specify license information here]
