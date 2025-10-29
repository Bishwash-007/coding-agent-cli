import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_file_info


def main():
    load_dotenv()
    api_key = os.environ.get('GOOGLE_API_KEY')
    client = genai.Client(
        api_key = api_key
    )
    verbose_flag = False
    
    if len(sys.argv) < 2 :
        print(f"Opps, I need a prompt to perform lol")
        sys.exit(1)
        
    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        verbose_flag = True
            
    prompt = sys.argv[1]
    
        
    messages = [
        types.Content(role="user",parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        return
    
    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Token Count : {response.usage_metadata.prompt_token_count}")
    
# main()

print(get_file_info('calculator' , 'pkg')) 