# Initialize an empty list to store tasks
tasks = []


# Function to add a new task to the list
def add_task():
    task_description = input("Enter the task description: ")
    tasks.append(task_description)
    print("Task added successfully!")


# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


# Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


# Main program loop
while True:
    print("\nMenu:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
