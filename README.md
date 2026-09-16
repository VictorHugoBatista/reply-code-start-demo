# Simple Todo List

A minimal CLI todo list that stores tasks in JSON.

## Project Structure

```
├── src/
│   └── todo.py          # Main CLI implementation
├── tests/
│   └── test_todo.py     # Test suite
└── README.md
```

## Usage

Add a task:
```bash
python src/todo.py add "buy milk"
```

List all tasks:
```bash
python src/todo.py list
```

Mark a task as done (by index):
```bash
python src/todo.py done 0
```

Edit a task (by index):
```bash
python src/todo.py edit 0 "buy organic milk"
```

Duplicate a task (by index):
```bash
python src/todo.py duplicate 0
```

Remove a task (by index):
```bash
python src/todo.py remove 0
```

Export all tasks as JSON:
```bash
python src/todo.py export
```

Run tests:
```bash
python -m pytest tests/test_todo.py
```

## How it works

- Tasks are stored in `todo.json` in the current directory
- Each task has `text` and `done` status
- Commands are processed via `sys.argv` with no external dependencies

## AI Agent Execution & Synchronization

This repository is configured to synchronize automatically with a "finish" demo repository via GitHub Actions. When code is pushed to the main branch, a workflow runs that:

1. **Syncs code**: Copies Python files and source code to the target repository (excluding `.github` workflows and `README.md`)
2. **Removes documentation**: Cleans up documentation folders and markdown files (preserving the target's README)
3. **Removes comments**: Strips all code comments from synchronized files (to focus on raw implementation)
4. **Pushes changes**: Commits and pushes the cleaned code to the target repository

### How to use

Push changes to the main branch — the workflow triggers automatically via `git push origin main`. The target repository will be updated with your latest code, cleaned and ready for AI agent execution.

### Workflow file

The synchronization is defined in `.github/workflows/sync-to-finish.yml`. No manual intervention needed — comments are automatically removed from all `.py`, `.rb`, `.js`, `.ts`, and C-like files before sync.
