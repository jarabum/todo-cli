import json
from pathlib import Path
from rich.console import Console

TASKS_FILE = Path.home() / ".todo_tasks.json"
console = Console()

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
    console.print(f"Added task: [bright_green]{name}[/bright_green]")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        console.print("[bright_red]No tasks yet![/bright_red]")
        return
    console.print("[bright_cyan]List of tasks:[/bright_cyan]")
    for i, task in enumerate(tasks):
        if task["done"]:
            status = "\\[x]"
            console.print(f"[bright_black]{i+1}[/bright_black]. [dark_green]{status}[/dark_green] [bright_green]{task['name']}[/bright_green]")
        else:
            status = "[ ]"
            console.print(f"[bright_black]{i+1}[/bright_black]. [bright_black]{status}[/bright_black] [white]{task['name']}[/white]")
        

def complete_task(task_id):
    tasks = load_tasks()
    if task_id < 1 or task_id > len(tasks):
        console.print(f"[bright_red]No task number {task_id}![/bright_red]")
        return

    if tasks[task_id - 1]["done"] == True:
        tasks[task_id - 1]["done"] = False
        save_tasks(tasks)
        print(f"{tasks[task_id - 1]['name']} marked as not done")
    elif tasks[task_id - 1]["done"] == False:
        tasks[task_id - 1]["done"] = True
        save_tasks(tasks)
        print(f"{tasks[task_id - 1]['name']} marked as done")

def remove_task(task_id):
    tasks = load_tasks()
    if task_id < 1 or task_id > len(tasks):
        print(f"No task number {task_id}")
        return

    removed_task = tasks[task_id - 1]["name"]
    tasks.pop(task_id - 1)
    save_tasks(tasks)
    print(f"Removed '{removed_task}'")
