task_list = []

def add_task(task):
    task_list.append(task)
    print(f'Task "{task}" added.')

def view_tasks():
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")

def  remove_task(task_number):
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number -1)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                print("Current Tasks:\n",)

                for idx, task in enumerate(task_list, start=1):
                    print(f"{idx}. {task}")
                    
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()