tasks = []

# load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except:
    pass

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose a number: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")

        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(i + 1, task)

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if num <= len(tasks):
            tasks.pop(num - 1)

            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(t + "\n")

            print("Task deleted!")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")