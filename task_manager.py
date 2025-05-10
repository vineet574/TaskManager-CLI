import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("✅ Task added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. [{status}] {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print("🎉 Task marked as complete.")
    except IndexError:
        print("❗ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['description']}")
    except IndexError:
        print("❗ Invalid task number.")

def main():
    while True:
        print("\n📋 Task Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter task number to mark complete: "))
                complete_task(index)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == '5':
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
