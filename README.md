# AI Agent Development Toolkit

This repository contains an AI agent development toolkit powered by Google's Gemini API.

## AI Agent Setup

The main component of this repository is an AI coding agent that can help with various programming tasks through a command-line interface.

### Features

- **Interactive AI Assistant**: Communicate with Google's Gemini 2.0 Flash model
- **Function Calling Capability**: The AI can perform operations on your filesystem:
  - List files and directories
  - Read file contents
  - Execute Python files
  - Write or modify files
- **Conversation Context**: Maintains conversation history for contextual responses
- **Verbose Mode**: Optional detailed output showing token usage

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

### AI Coding Assistant

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
python main.py "How do I fix the calculator?" --verbose
```

This will display:
```
User prompt: How do I fix the calculator?
Prompt tokens: <number>
Response tokens: <number>
 - Calling function: get_files_info
 - Calling function: get_file_content
<Gemini's response with suggestions to fix the calculator>
```

### How It Works

1. The AI agent receives your prompt
2. It analyzes your request and creates a plan using function calls
3. It can access files in the working directory (./calculator by default)
4. It can read, write, and execute code to help solve your problem
5. The conversation continues until a final response is generated

## Configuration

The AI agent behavior can be configured through the `config.py` file:

- `MAX_CHARS`: Maximum characters for text processing (default: 10000)
- `WORKING_DIR`: Working directory for file operations (default: "./calculator")
- `MAX_ITERS`: Maximum number of conversation iterations (default: 20)

## Available Functions

The AI agent can use the following functions:

- `get_files_info`: Lists files and directories
- `get_file_content`: Reads content from a file
- `write_file`: Writes content to a file
- `run_python_file`: Executes a Python file

## Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key (required)

## Dependencies

- `python-dotenv`: For loading environment variables
- `google-generativeai`: Google's official Python library for Gemini AI

## License

[Specify license information here]

## Next Steps

Here are some potential enhancements for this AI Agent Development Toolkit:

### Memory and State Management
- **Long-term Memory**: Implement persistent storage for conversation history across sessions
- **Knowledge Base Integration**: Connect to external knowledge bases or documentation
- **State Management**: Add capability to save and restore agent state

### Enhanced Reasoning Capabilities
- **Chain-of-Thought Reasoning**: Implement explicit reasoning steps for complex problems
- **Planning and Decomposition**: Add structured planning for multi-step tasks
- **Self-reflection**: Enable the agent to evaluate and improve its own responses

### Tool Integration
- **Web Search**: Add capability to search the web for up-to-date information
- **API Integration**: Connect to external APIs (GitHub, Stack Overflow, etc.)
- **Database Interaction**: Add functions to query and modify databases
- **Version Control Integration**: Direct interaction with Git repositories

### User Experience
- **Interactive Mode**: Add a REPL-like interface for continuous interaction
- **Multi-modal Input/Output**: Support for images, diagrams, and other media types
- **Customizable Personas**: Allow users to define different agent personalities
- **Progress Tracking**: Visual indication of multi-step task progress

### Security and Safety
- **Sandboxed Execution**: Improve security for code execution
- **Permission System**: Granular permissions for file and system operations
- **Content Filtering**: Add guardrails for generating safe and appropriate content

### Performance Optimization
- **Caching**: Implement response caching for common queries
- **Parallel Function Execution**: Run multiple functions concurrently
- **Model Switching**: Dynamically select different models based on the task
