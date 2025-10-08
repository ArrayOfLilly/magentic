import os
import sys
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.function_schemas import *
from call_function import *
from pprint import pprint
from prompts import *
from config import MAX_ITERS

def main():
    logging.getLogger().setLevel(logging.CRITICAL)

    api_key = load_apikey()
    client = genai.Client(api_key=api_key)
    
    verbose = False
    
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print_usage()   
        
    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    
    messages = [
        types.Content(role="user",parts=[types.Part(text=user_prompt)]),]
    
    iters = 0
    while True:
        iters += 1
        print(f"Iteration {iters}")
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
    
def print_usage():
    print()
    print("AI Code Assistant")
    print('\nUsage: python main.py "your prompt here" [--verbose]')
    print('Example: python main.py "How do I fix the calculator?"')
    os._exit(1)
    
def load_apikey():
    try:
        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
    except FileExistsError:
        raise FileExistsError(".env file not found. Please create one with the necessary environment variables.")   
    except KeyError:
        raise KeyError("GEMINI_API_KEY not found in environment variables.")
    except Exception as e:
        raise (f"An error occurred while retrieving GEMINI_API_KEY: {e}")
    return api_key

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt,
                                           tools=[available_functions], 
                                           ),
        )
    
    if verbose:        
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")
    
    print("Response:")
    if hasattr(response, "text") and response.text:
        print(response.text)
    else:
        print("There are non-text parts in the response")
    
    print("\nFunction calls:")       
    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
         raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="user", parts=function_responses))

if __name__ == "__main__":
    main()
