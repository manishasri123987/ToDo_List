print("=== To-Do List ===")

tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = int(input("\nEnter choice (1-4): "))

    if choice == 1:
        print("Enter task name:")
        task = input()
        tasks.append(task)
        print("Task added successfully!")
        print(f"Total tasks: {len(tasks)}")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            print(f"Enter task number to delete (1-{len(tasks)}):")
            num = int(input())
            if num < 1 or num > len(tasks):
                print("Invalid task number!")
            else:
                removed = tasks.pop(num-1)
                print(f"Deleted: {removed}")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
