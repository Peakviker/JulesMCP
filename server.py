from fastmcp import FastMCP
import os
import sys
import json
import platform
import datetime

# Initialize FastMCP server
mcp = FastMCP("Jules-Hermes")

# Global/File-based storage configuration
TASK_FILE = "tasks.json"
THOUGHT_FILE = "thoughts.log"
OBJECTIVE_FILE = "objective.json"
EVENT_FILE = "events.json"

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
def record_thought(thought: str):
    """Records an internal reasoning step or observation."""
    timestamp = datetime.datetime.now().isoformat()
    with open(THOUGHT_FILE, "a") as f:
        f.write(f"[{timestamp}] {thought}\n")
    return "Thought recorded."

@mcp.resource("thought-log://current")
def get_thought_log() -> str:
    """Returns the current log of reasoning steps."""
    if not os.path.exists(THOUGHT_FILE):
        return "No thoughts recorded yet."
    with open(THOUGHT_FILE, "r") as f:
        return f.read()

@mcp.tool()
def set_objective(objective: str):
    """Sets the current high-level objective for the session."""
    data = {
        "objective": objective,
        "set_at": datetime.datetime.now().isoformat()
    }
    with open(OBJECTIVE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return f"Objective set: {objective}"

@mcp.resource("objective://current")
def get_current_objective() -> str:
    """Returns the current session objective."""
    if not os.path.exists(OBJECTIVE_FILE):
        return "No objective set."
    with open(OBJECTIVE_FILE, "r") as f:
        return f.read()

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
def manage_tasks(action: str, task: str = None, task_id: int = None, status: str = None, assigned_to: str = None):
    """Manages a task list. Actions: 'add', 'list', 'update', 'clear'."""
    if action == "add":
        if not task:
            return "Task description is required for 'add' action."
        tasks = []
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as f:
                tasks = json.load(f)
        new_task = {
            "id": len(tasks) + 1,
            "task": task,
            "status": "pending",
            "assigned_to": assigned_to or "Unassigned",
            "created_at": datetime.datetime.now().isoformat()
        }
        tasks.append(new_task)
        with open(TASK_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
        return f"Task added with ID {new_task['id']}: {task} (Assigned to: {new_task['assigned_to']})"

    elif action == "list":
        if not os.path.exists(TASK_FILE):
            return "No tasks found."
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)
        return json.dumps(tasks, indent=2)

    elif action == "update":
        if task_id is None:
            return "task_id is required for 'update' action."
        if not os.path.exists(TASK_FILE):
            return "No tasks found."
        with open(TASK_FILE, "r") as f:
            tasks = json.load(f)

        for t in tasks:
            if t["id"] == task_id:
                if status:
                    t["status"] = status
                if assigned_to:
                    t["assigned_to"] = assigned_to
                t["updated_at"] = datetime.datetime.now().isoformat()
                with open(TASK_FILE, "w") as f:
                    json.dump(tasks, f, indent=2)
                return f"Task {task_id} updated."
        return f"Task with ID {task_id} not found."

    elif action == "clear":
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)
        return "Task list cleared."

    else:
        return "Invalid action."

@mcp.tool()
def get_task_details(task_id: int):
    """Retrieves full information about a specific task by its ID."""
    if not os.path.exists(TASK_FILE):
        return "No tasks found."
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
    for t in tasks:
        if t["id"] == task_id:
            return json.dumps(t, indent=2)
    return f"Task with ID {task_id} not found."

@mcp.tool()
def emit_event(event_type: str, description: str):
    """Emits a structured event to the session event stream."""
    events = []
    if os.path.exists(EVENT_FILE):
        with open(EVENT_FILE, "r") as f:
            events = json.load(f)

    event = {
        "timestamp": datetime.datetime.now().isoformat(),
        "type": event_type,
        "description": description
    }
    events.append(event)
    # Keep only last 50 events
    events = events[-50:]

    with open(EVENT_FILE, "w") as f:
        json.dump(events, f, indent=2)
    return f"Event emitted: [{event_type}] {description}"

@mcp.resource("events://recent")
def get_recent_events() -> str:
    """Returns the structured list of recent events."""
    if not os.path.exists(EVENT_FILE):
        return "No events recorded."
    with open(EVENT_FILE, "r") as f:
        return f.read()

if __name__ == "__main__":
    mcp.run()
