# Technical Documentation: Jules-Hermes MCP Server

## Architecture
The server is built using the `fastmcp` library, which implements the Model Context Protocol (MCP).

## Tools Detail

### `analyze_repository(path=".")`
- **Description**: Scans the specified directory (recursively, ignoring `.git`) and returns a JSON object with file counts mapped to their extensions.
- **Output**: JSON string.

### `get_system_info()`
- **Description**: Collects platform, Python version, current working directory, and CPU count.
- **Output**: JSON string.

### `manage_tasks(action, task=None)`
- **Description**: Manages `tasks.json` file.
- **Actions**:
  - `add`: Appends a new task to the list.
  - `list`: Returns all tasks in JSON format.
  - `clear`: Deletes the `tasks.json` file.
- **Output**: Confirmation message or JSON string.

## Dependencies
- `fastmcp`: Python library for building MCP servers.
- `json`, `os`, `platform`, `sys`: Standard Python libraries.
