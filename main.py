import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

from call_function import call_function


def main():
    load_dotenv()
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    client = genai.Client(
        api_key = api_key
    )
    
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

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
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    
    config = types.GenerateContentConfig(
        tools = [available_functions],
        system_instruction=types.Content(
            parts=[types.Part(text=system_prompt)]
        ),
    )

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config = config
    )
    
    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Token Count : {response.usage_metadata.prompt_token_count}")
    
    if response is None or response.usage_metadata is None:
        print("Invalid Response")
        return
    
    if response.function_calls:
        print(response.function_calls)
        for function_call_part in response.function_calls:
            result = call_function(function_call_part, verbose_flag)
            print(result)
        
            
    else:
        print(response.text)

    

    
main()
