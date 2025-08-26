# To-Do List Manager
tasks = []
while True:
    print("\n TO DO LIST MANAGER")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

if choice == "1":
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

elif choice == "2":
    if len(tasks) == 0:
        print("No tasks yet! Add one.")
    else:
        print("Here are your tasks: ")
        for idx, task in enumerate(tasks, start = 1):
            print(f"{idx}.{task}")

elif choice == "3":
    if len(tasks) == 0:
        print("You have no tasks to remove.")
    else:
        for idx, task in enumerate(tasks, start = 1):
            print(f"{idx}.{task}")
        try:
            remove_index = int(input("Enter number of task to remove: "))
            if 1 <= remove_index <= len(tasks):
                removed_task = tasks.pop(remove_index-1)
                print(f"Task '{removed_task}' removed ✅")
            else:
                print("Invalid task number ❌")
        except ValueError:
            print("Please enter a valid number ❗")

elif choice == "4":
    print("Bye! Keep slaying your goals 👋✌️")

else:
    print("Invalid Choice! Try again.")