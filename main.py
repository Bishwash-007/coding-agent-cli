import sys
from google.genai import types

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
from llm import client


def main():
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, generate a plan using function calls. 
You can perform the following operations:

- List files and directories
- Read file contents
- Write or modify files
- Run Python or JavaScript files
- Format code with Prettier
- Show diff previews
- Track recent changes

All paths you provide should be relative to the working directory. 
Do not include absolute paths in your function calls.
"""

    verbose_flag = "--verbose" in sys.argv

    if len(sys.argv) < 2:
        print("Oops, you need to provide a prompt")
        sys.exit(1)

    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    available_tools = types.Tool(
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

    config = types.GenerateContentConfig(
        tools=[available_tools],
        system_instruction=types.Content(parts=[types.Part(text=system_prompt)]),
    )

    max_iters = 20

    for _ in range(max_iters):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=config,
        )

        if verbose_flag:
            print(f"\n=== AI Response Debug ===")
            print(f"User Prompt: {user_prompt}")
            if response.usage_metadata:
                print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
            print("========================\n")

        if not response or not response.usage_metadata:
            print("Invalid response from AI")
            return

        if response.candidates:
            for candidate in response.candidates:
                if candidate and candidate.content:
                    messages.append(candidate.content)

        if response.function_calls:
            for fn_call in response.function_calls:
                result = call_function(fn_call, verbose_flag)
                messages.append(result)

                if fn_call.name == "show_diff":
                    diff_text = result.parts[0].response.get("result", "")
                    print("=== Diff Preview ===")
                    print(diff_text)
                    apply_change = input("Apply changes? (y/n) ").strip().lower()
                    if apply_change == "y":
                        fn_call.args["preview"] = False
                        confirmed_result = call_function(fn_call, verbose_flag)
                        print(confirmed_result.parts[0].response.get("result", ""))
        else:
            print(response.text)
            return


if __name__ == "__main__":
    main()