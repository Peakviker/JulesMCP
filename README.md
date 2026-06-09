# Jules-Hermes MCP Server

This is an MCP (Model Context Protocol) server designed to enable a robust, multi-agent interaction loop between Jules and Hermes-Agent. It focuses on task execution, live monitoring, and contextual awareness.

## Features

- **Contextual Awareness**: Define and retrieve the session's high-level goal using `set_objective` and the `objective://current` resource.
- **Event Stream**: Track significant milestones and corrections in real-time via `emit_event` and the `events://recent` resource.
- **Thought Recording**: Persistent log of reasoning steps accessible via `thought-log://current`.
- **Advanced Task Management**: Full task lifecycle tracking with unique IDs, statuses, and agent assignments (`assigned_to`).
- **Repository Analysis**: Deep scan of codebase file structure.

## Installation

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.

## Usage

### Integration with Hermes-Agent
Register this server as a skill using the provided `skill.yaml`. This allows Hermes to:
1. Understand the **Objective**.
2. **Assign tasks** to Jules or itself.
3. **Monitor progress** through events and thoughts.
4. **Correct course** by updating task statuses.

## Documentation
See [docs/TECHNICAL.md](docs/TECHNICAL.md) for full API details.
