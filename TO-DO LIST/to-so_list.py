tasks = []

def add_task():
    title = input("Enter a new task: ")

    # Create a task dictionary to store task details in the list
    task = {
        "title": title,
        "status": "pending"
    }
    tasks.append(task)
    print(f'Task "{title}" added successfully.')

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - {task['status']}")

def edit_task():
    view_tasks()
    a = int(input("Enter the number of the task to edit: ")) - 1

    if 0 <= a < len(tasks):
        new_title = input("Enter the new title for the task: ")
        tasks[a]['title'] = new_title
        print(f'Task "{new_title}" updated successfully.')
    else:
        print("Invalid task number.")

def mark_task_completed():
    view_tasks()
    a = int(input("Enter the number of the task to mark as completed: ")) - 1

    if 0 <= a < len(tasks):
        tasks[a]['status'] = 'completed'
        print(f'Task "{tasks[a]["title"]}" marked as completed.')
    else:
        print("Invalid task number.")

def remove_task():
    view_tasks()
    a = int(input("Enter the number of the task to remove: ")) - 1

    if 0 <= a < len(tasks):
        removed_task = tasks.pop(a)
        print(f'Task "{removed_task["title"]}" removed successfully.')
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\nTask Manager Menu:\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Remove Task")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            remove_task()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
