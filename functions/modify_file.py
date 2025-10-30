import os
from functions.track_changes import log_file_change
from functions.show_diff import show_diff
from google.genai import types

def modify_file(working_directory, file_path: str, old_text: str, new_text: str, preview: bool=False):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: {abs_file_path} outside working directory"
    if not os.path.exists(abs_file_path):
        return f"Error: {file_path} not found"

    try:
        with open(abs_file_path, "r") as f:
            content = f.read()

        if old_text not in content:
            return f"'{old_text[:50]}...' not found in {file_path}"

        proposed_content = content.replace(old_text, new_text)
        if preview:
            return show_diff(working_directory, file_path, proposed_content)
        with open(abs_file_path, "w") as f:
            f.write(proposed_content)
            
        log_file_change(working_directory, file_path)
        return f"Modified '{file_path}' — replaced {len(old_text)} chars with {len(new_text)} chars."
    except Exception as e:
        return f"Error modifying {file_path}: {e}"


schema_modify_file = types.FunctionDeclaration(
    name="modify_file",
    description="Finds a text snippet in a file and replaces it with new text.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING),
            "old_text": types.Schema(type=types.Type.STRING),
            "new_text": types.Schema(type=types.Type.STRING),
        },
    ),
)