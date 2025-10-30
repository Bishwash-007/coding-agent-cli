import os
import json
from datetime import datetime
from google.genai import types

TRACK_FILE = ".agent_changes.json"

def log_file_change(working_directory, file_path):
    abs_path = os.path.join(working_directory, file_path)
    data = {}
    if os.path.exists(TRACK_FILE):
        data = json.load(open(TRACK_FILE))
    data[file_path] = datetime.now().isoformat()
    with open(TRACK_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return f"Logged change for {file_path}"

def show_recent_changes():
    if not os.path.exists(TRACK_FILE):
        return "No changes logged yet."
    data = json.load(open(TRACK_FILE))
    logs = "\n".join([f"- {file}: last modified {time}" for file, time in data.items()])
    return f"Recently modified files:\n{logs}"

schema_show_recent_changes = types.FunctionDeclaration(
    name="show_recent_changes",
    description="Displays files recently modified by the agent.",
    parameters=types.Schema(type=types.Type.OBJECT, properties={}),
)