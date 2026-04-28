import json
from pathlib import Path

TASKS_FILE = Path.home() / ".todo_tasks.json"

def load_tasks():
    if not TASKS_FILE.exists():
        return []
    return json.loads(TASKS_FILE.read_text())

def save_tasks(tasks):
    TASKS_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(name):
    tasks = load_tasks()
    tasks.append({"name": name, "done": False})
    save_tasks(tasks)
    print(f"Added task: {name}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    print("List of tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        print(f"{i+1}. {status} {task['name']}")

def complete_task(task_id):
    tasks = load_tasks()
    if task_id < 1 or task_id > len(tasks):
        print(f"No task number {task_id}")
        return

    if tasks[task_id - 1]["done"] == True:
        tasks[task_id - 1]["done"] = False
        save_tasks(tasks)
        print(f"Task: '{tasks[task_id - 1]['name']}' marked as not done")
    elif tasks[task_id - 1]["done"] == False:
        tasks[task_id - 1]["done"] = True
        save_tasks(tasks)
        print(f"Task: '{tasks[task_id - 1]['name']}' marked as done")

def remove_task(task_id):
    tasks = load_tasks()
    if task_id < 1 or task_id > len(tasks):
        print(f"No task number {task_id}")
        return

    removed_task = tasks[task_id - 1]["name"]
    tasks.pop(task_id - 1)
    save_tasks(tasks)
    print(f"Removed '{removed_task}'")
