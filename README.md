
# ScopePilot

**AI-powered, cloud-agnostic infrastructure management.**

ScopePilot is an open-source project designed to simplify cloud infrastructure discovery, understanding, and management through a unified interface.

The project aims to help developers interact with cloud resources without requiring extensive knowledge of each cloud provider's native tools and APIs.

> Status: Early development. Core functionality is not implemented yet.

## Project Goals

- Provide a unified abstraction for multiple cloud providers.
- Discover and inspect cloud infrastructure resources.
- Offer CLI and API interfaces.
- Enable AI-assisted infrastructure interactions.
- Prioritize security, transparency, and user control.
- Follow Clean Architecture principles.

## Planned Cloud Providers

| Provider | Status |
|----------|--------|
| Mock | Planned for v0.1.0 |
| AWS | Planned for v0.1.0 |
| Azure | Future |
| Google Cloud | Future |

## Technology Stack

- Python 3.12+
- Pytest
- Ruff
- Setuptools

Additional technologies will be introduced as required.

## Architecture

ScopePilot follows Clean Architecture principles.

The project is organized into four main layers:

- **Domain:** Core business entities and rules.
- **Application:** Use cases and application interfaces.
- **Infrastructure:** External systems and provider adapters.
- **Presentation:** APIs and future CLI interfaces.

Dependencies should point toward the inner layers.

## Getting Started

### Requirements

- Python 3.12 or later
- Git

### Clone the repository

```bash
git clone https://github.com/caleones/ScopePilot.git
cd ScopePilot
```

### Create a virtual environment

On Windows:

```powershell
py -m venv .venv
```

### Install development dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

### Verify installation

```powershell
.\.venv\Scripts\python.exe -c "import scopepilot; print('ScopePilot installed successfully')"
```

## Development

### Run linting

```powershell
.\.venv\Scripts\python.exe -m ruff check .
```

### Check formatting

```powershell
.\.venv\Scripts\python.exe -m ruff format --check .
```

### Run tests

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Tests will be introduced as development progresses.

## Roadmap

### v0.1.0 - Cloud Discovery MVP

- Python project setup
- Cloud resource domain model
- Cloud provider abstraction
- Mock cloud provider
- Resource discovery use case
- Read-only AWS EC2 discovery
- CLI integration
- Automated tests and CI

### v0.2.0 - AI Assistant

- LLM integration
- Tool calling
- Cloud resource queries
- Authorization and safety controls
- AI response evaluation

## Security

ScopePilot is being designed with security as a core requirement.

The initial real cloud integrations will be read-only.

## Contributing

Development is managed through GitHub Issues, Projects, and Pull Requests.

Each feature should have clear acceptance criteria, appropriate tests, and documented changes.
