import os
from dotenv import load_dotenv
from google import genai

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

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)    

if __name__ == "__main__":
    main()
