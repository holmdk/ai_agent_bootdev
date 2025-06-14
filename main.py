#!/usr/bin/env python3
"""
A simple script to interact with the Gemini AI model.
Takes a prompt as a command line argument and returns the model's response.
Optional --verbose flag provides additional information about the interaction.
"""
# Standard library imports
import os
import sys

# Third-party imports
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables and initialize client
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if __name__ == '__main__':
    # Get user prompt from command line arguments
    try:
        input_prompt = sys.argv[1]
    except IndexError:
        sys.exit("Error: Please provide a prompt as the first argument")

    # Prepare message for the model
    messages = [
        types.Content(role="user", parts=[types.Part(text=input_prompt)]),
    ]

    # Generate response from the model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # Check if verbose flag has been set
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {input_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        print(response.text)
