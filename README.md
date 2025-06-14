# Gemini AI Interaction Tool

A simple command-line tool to interact with the Gemini AI model. This tool allows you to send prompts to the Gemini model and receive responses directly in your terminal.

## Features

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

Basic usage:
```
python main.py "Your prompt here"
```

With verbose output:
```
python main.py "Your prompt here" --verbose
```

### Command Line Arguments

- First argument (required): The prompt to send to the Gemini model
- `--verbose` (optional): Display additional information including:
  - The user's prompt
  - Number of prompt tokens used
  - Number of response tokens generated

### Example

Basic usage:
```
python main.py "What is the meaning of life?"
```

Verbose output:
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