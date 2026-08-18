# Technical Documentation: Jules-Hermes MCP Server

## Interaction Infrastructure

### Resources
- **`objective://current`**: Current session goal.
- **`events://recent`**: Last 50 session events (JSON).
- **`thought-log://current`**: Raw text log of reasoning steps.

### Tools

#### `set_objective(objective)`
Sets the session's north star.

#### `emit_event(event_type, description)`
Logs a milestone or operational event. Types: `milestone`, `error`, `correction`, `info`.

#### `manage_tasks(action, ...)`
- **Actions**: `add`, `list`, `update`, `clear`.
- **Fields**: `task`, `task_id`, `status`, `assigned_to`.

#### `record_thought(thought)`
Appends reasoning to the persistent log.

#### `get_task_details(task_id)`
Full metadata for a specific task.

#### `analyze_repository(path)`
File extension statistics.

#### `get_system_info()`
Host environment metadata.
