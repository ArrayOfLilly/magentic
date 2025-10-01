import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
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
        
    messages = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)]),]
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
        )
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print("Response:")
    print(response.text)
    
def print_usage():
    print("Usage: uv run main.py \"Your prompt here\") [--verbose]")
    os._exit(1)

if __name__ == "__main__":
    main()
