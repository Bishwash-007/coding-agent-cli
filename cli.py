import sys
from google.genai import types
from llm import client

from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.format_with_prettier import schema_format_with_prettier
from functions.run_javascript_file import schema_run_javascript_file
from functions.modify_file import schema_modify_file
from functions.track_changes import schema_show_recent_changes
from functions.show_diff import schema_show_diff

from call_function import call_function
from decoration import show_welcome, display_response, prompt_input
from rich.prompt import Prompt

from llm import client

WORKING_DIRECTORY = "projects" 

SYSTEM_PROMPT = """
You are a helpful AI coding agent for multi-language projects.
You can perform the following operations:

- List files and directories
- Read file contents
- Write or modify files
- Run Python or JavaScript files
- Format code with Prettier
- Show diff previews
- Summarize code files
- Track recent changes

All paths should be relative to the working directory.
"""

AVAILABLE_TOOLS = types.Tool(
    function_declarations=[
        schema_run_python_file,
        schema_run_javascript_file,
        schema_write_file,
        schema_get_file_content,
        schema_get_files_info,
        schema_format_with_prettier,
        schema_modify_file,
        schema_show_recent_changes,
        schema_show_diff,
    ]
)

CONFIG = types.GenerateContentConfig(
    tools=[AVAILABLE_TOOLS],
    system_instruction=types.Content(parts=[types.Part(text=SYSTEM_PROMPT)]),
)


def interactive_loop(verbose=False):
    show_welcome()
    
    messages = []

    while True:
        user_input = prompt_input().strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=CONFIG
        )

        if verbose:
            display_response("DEBUG", f"Prompt: {user_input}\nTokens: {response.usage_metadata.prompt_token_count}")

        if response.candidates:
            for candidate in response.candidates:
                if candidate and candidate.content:
                    messages.append(candidate.content)

        if response.function_calls:
            for fn_call in response.function_calls:
                result = call_function(fn_call, verbose)
                messages.append(result)
                
                if fn_call.name == "show_diff":
                    display_response("Diff Preview")
                    apply_change = Prompt.ask("Apply changes? (y/n)", choices=["y", "n"], default="n")
                    if apply_change == "y":
                        fn_call.args["preview"] = False
                        confirmed_result = call_function(fn_call, verbose)
                        output_text = confirmed_result.parts[0].response.get("result", "")
                        print(confirmed_result.parts[0].response.get("result", ""))
                        display_response("Applied Changes", output_text)

        else:
            display_response(content=response.text)


if __name__ == "__main__":
    verbose_flag = "--verbose" in sys.argv
    interactive_loop(verbose_flag)