import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)        
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: {abs_file_path} is not in the working directory"
    
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"something went wrong while creating parent directory {e}"
        
    if not os.path.isfile(abs_file_path):
        pass
        
    try:
        with open(abs_file_path,"w") as f:
            f.write(content)
        return f"'{file_path}' Modified ... ({len(content)}) characters wrote to file"
        
    except Exception as e:
        return f"Failed to write to file: {file_path}, {e}"
    
    
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Runs a python file and accepts additional args as a list from cli",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to the file from the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to write to a file"
            )
        },
    ),
)