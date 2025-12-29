def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()

while True:
    print("\n📝 To-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        number = int(input("Enter task number to delete: "))
        tasks.pop(number - 1)
        save_tasks(tasks)
        print("🗑️ Task deleted!")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice!")
