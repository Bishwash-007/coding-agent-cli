# functions/format_with_prettier.py
import os
import subprocess
from google.genai import types

def format_with_prettier(working_directory, file_path: str):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: {abs_file_path} is outside working directory"
    
    try:
        result = subprocess.run(
            ["npx", "prettier", "--write", abs_file_path],
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
            timeout=20
        )
        return f"Prettier Output:\n{result.stdout}\n{result.stderr}"
    except Exception as e:
        return f"Error formatting with Prettier: {e}"

schema_format_with_prettier = types.FunctionDeclaration(
    name="format_with_prettier",
    description="Formats a given JS/TS/CSS/HTML file using Prettier.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING),
        },
    ),
)