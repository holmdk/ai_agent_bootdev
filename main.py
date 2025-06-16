#!/usr/bin/env python3
"""
A simple script to interact with the Gemini AI model.
Takes a prompt as a command line argument and returns the model's response.
Optional --verbose flag provides additional information about the interaction.
"""
# Standard library imports
import os
import sys
from typing import Optional

# Third-party imports
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt

from call_function import available_functions


if __name__ == '__main__':
    # Load environment variables and initialize client
    load_dotenv()

    # Get user prompt from command line arguments
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key: Optional[str] = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # Prepare message for the model
    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    config = types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    # Generate response from the model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=config,
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        print(response.text)

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

