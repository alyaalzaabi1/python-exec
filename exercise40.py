tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def show_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

# Example
add_task("Finish Python exercises")
add_task("Read MCP article")
show_tasks()
mark_done(0)
remove_task(1)
print("\nUpdated Tasks:")
show_tasks()
