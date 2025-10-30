import os
import difflib

from google.genai import types

def show_diff(working_directory, file_path: str, new_text: str):
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.exists(abs_path):
        return f"Error: {file_path} not found"

    with open(abs_path, "r") as f:
        old_text = f.read()

    old_lines = old_text.splitlines(keepends=True)
    new_lines = new_text.splitlines(keepends=True)

    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=f"a/{file_path}",
        tofile=f"b/{file_path}",
        lineterm="",
        n=3 
    )

    diff_text = "".join(diff)
    return diff_text if diff_text else f"No changes detected in {file_path}."


schema_show_diff = types.FunctionDeclaration(
    name="show_diff",
    description="Shows a unified diff between the current file and a proposed new version.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING),
            "new_text": types.Schema(type=types.Type.STRING),
        },
    ),
)