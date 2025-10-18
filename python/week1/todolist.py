tasks = []

while True:
    print('''
    -------- TO-DO LIST --------
    1) Add task
    2) View tasks
    3) Delete task
    4) Exit
    ----------------------------''')

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            delete_choice = input("Enter the task number to delete: ") 

            if delete_choice.isdigit():
                index = int(delete_choice)
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number only.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
