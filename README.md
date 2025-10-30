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

Usage
---
![Image]('./image.png')

Setup Environment Variables
---

get your api key from google ai studio
https://aistudio.google.com

```
GOOGLE_API_KEY=
```
