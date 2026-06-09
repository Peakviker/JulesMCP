# Jules-Hermes MCP Server

This is an MCP (Model Context Protocol) server designed to interface with Hermes-Agent. It provides tools for repository analysis, task tracking, and retrieving system information.

## Features

- **Analyze Repository**: Get a breakdown of file types in the repository.
- **System Information**: Retrieve details about the operating environment.
- **Task Management**: Simple persistent task list for tracking progress.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Peakviker/JulesMCP.git
   cd JulesMCP
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server
To start the MCP server manually:
```bash
python3 server.py
```

### Integration with Hermes-Agent
Use the provided `skill.yaml` to register the server as a skill in Hermes-Agent.

## Documentation
Detailed technical information can be found in the [docs/TECHNICAL.md](docs/TECHNICAL.md) file.
