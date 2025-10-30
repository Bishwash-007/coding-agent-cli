import os
import subprocess
from google.genai import types

def run_javascript_file(working_directory, file_path: str, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: {abs_file_path} is not inside working directory"
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} does not exist"
    
    if not (file_path.endswith(".js") or file_path.endswith(".ts") or file_path.endswith(".jsx") or file_path.endswith(".tsx")):
        return "Error: not a JavaScript/TypeScript file"
    
    try:
        cmd = ["node", file_path] if file_path.endswith(".js") else ["npx", "ts-node", file_path]
        cmd.extend(args)
        result = subprocess.run(cmd, cwd=abs_working_directory, capture_output=True, text=True, timeout=30)
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        return f"Execution error: {e}"

schema_run_javascript_file = types.FunctionDeclaration(
    name="run_javascript_file",
    description="Executes JavaScript or TypeScript files using Node.js or ts-node.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING),
            "args": types.Schema(type=types.Type.ARRAY, items=types.Schema(type=types.Type.STRING)),
        },
    ),
)