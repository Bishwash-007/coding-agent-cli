import os
from google.genai import types

from config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)        
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: {abs_file_path} is not in the working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: {abs_file_path} is not a file'
    
    file_content_string = ""
    try:
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARACTERS)
            if len(file_content_string) > MAX_CHARACTERS:
                file_content_string += f'[...File "{file_path}" truncated at 1000 characters]'
                
        return file_content_string
         
    except Exception as e:
        return f"Something went wrong while reading file. Exception: {e}"

        
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gives the content of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to the file from the working directory",
            ),
        },
    ),
)