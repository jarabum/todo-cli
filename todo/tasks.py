import json
from operator import index
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

def add_task(name, priority):
    tasks = load_tasks()
    tasks.append({"name": name, "done": False, "priority": priority})
    save_tasks(tasks)
    console.print(f"Added task: [bright_green]{name}[/bright_green]")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        console.print("[bright_red]No tasks yet![/bright_red]")
        return
    console.print("[bright_cyan]List of tasks:[/bright_cyan]")
    for i, task in enumerate(tasks):
        color = "white"
        if task["priority"] == "medium":
            color = "bright_yellow"
        elif task["priority"] == "high":
            color = "bright_red"
        
        if task["done"]:
            status = "\\[x]"
            console.print(f"[bright_black]{i+1}[/bright_black]. [dark_green]{status}[/dark_green] [bright_green]{task['name']}[/bright_green]")
        else:
            status = "[ ]"
            console.print(f"[bright_black]{i+1}[/bright_black]. [bright_black]{status}[/bright_black] [{color}]{task['name']}[/{color}]")
        

def complete_task(task_id):
    tasks = load_tasks()
    if task_id < 1 or task_id > len(tasks):
        console.print(f"[bright_red]No task number {task_id}![/bright_red]")
        return

    if tasks[task_id - 1]["done"] == True:
        tasks[task_id - 1]["done"] = False
        save_tasks(tasks)
        console.print(f"[white]{tasks[task_id - 1]['name']}[/white] marked as not done")
    elif tasks[task_id - 1]["done"] == False:
        tasks[task_id - 1]["done"] = True
        save_tasks(tasks)
        console.print(f"[bright_green]{tasks[task_id - 1]['name']}[/bright_green] marked as done")

def remove_task(task_id):
    tasks = load_tasks()
    if task_id < 1 or task_id > len(tasks):
        console.print(f"[bright_red]No task number {task_id}[/bright_red]")
        return

    removed_task = tasks[task_id - 1]["name"]
    tasks.pop(task_id - 1)
    save_tasks(tasks)
    console.print(f"Removed [bright_red]{removed_task}[bright_red]")

def clear_tasks():
    tasks = load_tasks()
    removedtasks = []

    for task in tasks:
        if task["done"]:
            removedtasks.append(task["name"])

    save_tasks([task for task in tasks if not task["done"]])

    console.print("[bright_cyan]Removed:[/bright_cyan]")
    for task in removedtasks:
        console.print(f"[bright_red]{task}[/bright_red]")
