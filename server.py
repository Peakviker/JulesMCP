from fastmcp import FastMCP
import os
import sys
import json
import platform

# Initialize FastMCP server
mcp = FastMCP("Jules-Hermes")

@mcp.tool()
def analyze_repository(path: str = "."):
    """Analyzes the repository structure and returns file counts by extension."""
    if not os.path.exists(path):
        return f"Path {path} does not exist."

    analysis = {}
    for root, dirs, files in os.walk(path):
        if ".git" in root:
            continue
        for file in files:
            ext = os.path.splitext(file)[1] or "no_extension"
            analysis[ext] = analysis.get(ext, 0) + 1

    return json.dumps(analysis, indent=2)

@mcp.tool()
def get_system_info():
    """Returns basic system information."""
    info = {
        "platform": platform.platform(),
        "python_version": sys.version,
        "current_directory": os.getcwd(),
        "cpu_count": os.cpu_count()
    }
    return json.dumps(info, indent=2)

@mcp.tool()
def manage_tasks(action: str, task: str = None):
    """Manages a simple task list. Actions: 'add', 'list', 'clear'."""
    task_file = "tasks.json"

    if action == "add":
        if not task:
            return "Task description is required for 'add' action."
        tasks = []
        if os.path.exists(task_file):
            with open(task_file, "r") as f:
                tasks = json.load(f)
        tasks.append({"task": task, "status": "pending"})
        with open(task_file, "w") as f:
            json.dump(tasks, f, indent=2)
        return f"Task added: {task}"

    elif action == "list":
        if not os.path.exists(task_file):
            return "No tasks found."
        with open(task_file, "r") as f:
            tasks = json.load(f)
        return json.dumps(tasks, indent=2)

    elif action == "clear":
        if os.path.exists(task_file):
            os.remove(task_file)
        return "Task list cleared."

    else:
        return "Invalid action. Use 'add', 'list', or 'clear'."

if __name__ == "__main__":
    mcp.run()
