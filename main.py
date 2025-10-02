import os
import sys
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.function_schemas import *

def main():
    logging.getLogger().setLevel(logging.CRITICAL)

    try:
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
    except FileExistsError:
        raise FileExistsError(".env file not found. Please create one with the necessary environment variables.")   
    except KeyError:
        raise KeyError("GEMINI_API_KEY not found in environment variables.")
    except Exception as e:
        raise (f"An error occurred while retrieving GEMINI_API_KEY: {e}")

    client = genai.Client(api_key=api_key)
    
    verbose = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "--verbose" or sys.argv[1] == "-h":
            print_usage()
        user_prompt = sys.argv[1]
        if len(sys.argv) > 2:
            verbose = sys.argv[2] == "--verbose"
    else:
        print_usage()
        
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
        
    messages = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)]),]
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt,
                                           tools=[available_functions], 
                                           ),
        )
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print()
        
    
    print("Response:")
    if hasattr(response, "text") and response.text:
        print(response.text)
    else:
        print("There are non-text parts in the response")
    
    print()   
    print("Function calls:")        
    if hasattr(response, "function_calls") and response.function_calls:
            for fc in response.function_calls:
                print(f"Calling function: {fc.name}({fc.args})")
    else:
        print("No function calls in response")
    
def print_usage():
    print("Usage: uv run main.py <\"Your prompt here\"> [--verbose]")
    os._exit(1)

if __name__ == "__main__":
    main()
