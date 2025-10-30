## Braniac AI

Interactive coding agent build with google genai

Currently this supports just the basic stuff like
- Project creation.
- Simple bug fix.
- read/write file.
- modify file.

and possibly other stuffs if it doesn't break


Run Locally
---

Make sure you have uv installed
if not.Refer to the installation guide https://docs.astral.sh/uv/getting-started/installation/#standalone-installer

```
git clone https://github.com/Bishwash-007/coding-agent-cli.git

cd coding-agent-cli

uv venv
uv sync

uv run cli.py
```

Example Usage
---

![Image](https://github.com/Bishwash-007/coding-agent-cli/blob/337e65e21663d64b1798cc3cbeb5b2e4cce9f58a/images/image.png?raw=True)

When prompted input your prompt<br>
e.g : initialize me a express js application

![Image](https://github.com/Bishwash-007/coding-agent-cli/blob/337e65e21663d64b1798cc3cbeb5b2e4cce9f58a/images/image2.png?raw=True)

you can ask the agent to build your project. keep it simple lol

Setup Environment Variables
---

get your api key from google ai studio
https://aistudio.google.com

```
GOOGLE_API_KEY=
```
