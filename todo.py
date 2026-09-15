"""Simple CLI todo list that stores tasks in JSON."""
import json
import sys
from pathlib import Path

TASKS_FILE = Path("todo.json")

def load_tasks():
    """Load tasks from todo.json, return empty list if file doesn't exist."""
    if TASKS_FILE.exists():
        return json.loads(TASKS_FILE.read_text())
    return []

def save_tasks(tasks):
    """Write tasks list to todo.json."""
    TASKS_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(text):
    """Add a new task with given text."""
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Added: {text}")

def list_tasks():
    """Print all tasks with index and done status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else " "
        print(f"{i}: [{status}] {task['text']}")

def mark_done(index):
    """Mark task at given index as complete."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Done: {tasks[index]['text']}")
    else:
        print(f"Invalid task index: {index}")

def demo():
    """Run self-check: add, list, and mark tasks complete."""
    if TASKS_FILE.exists():
        TASKS_FILE.unlink()
    add_task("test task 1")
    add_task("test task 2")
    list_tasks()
    mark_done(0)
    list_tasks()
    assert load_tasks()[0]["done"] == True
    assert load_tasks()[1]["done"] == False
    TASKS_FILE.unlink()
    print("Self-check passed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|done|test]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(sys.argv) > 2:
        mark_done(int(sys.argv[2]))
    elif cmd == "test":
        demo()
    else:
        print("Unknown command or missing arguments.")
