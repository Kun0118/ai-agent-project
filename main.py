import argparse
from dotenv import load_dotenv
import os
from google import genai
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    parser = argparse.ArgumentParser(prog="Gemini prompt", description="Type your prompt.")
    parser.add_argument("user_argument", type = str, help = "type your arguement")
    args = parser.parse_args()


    

    if api_key == None:
        raise RuntimeError("API key not found")
    client = genai.Client(api_key=api_key)

    response = client   .models.generate_content(
    model='gemini-2.5-flash', contents=args.user_argument)

    if response.usage_metadata == None:
        raise RuntimeError("API request failed... Please try again later.")
    else:
        usage = response.usage_metadata

    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print(response.text)
    


if __name__ == "__main__":
    main()
