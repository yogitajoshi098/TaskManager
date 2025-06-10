from day_5_taskClasses import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Filter Tasks by Status")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            try:
                number = int(input("Enter task number to mark as done: "))
                manager.Marks_Status_Done(number)
            except:
                print("Please enter a valid number.")

        elif choice == "4":
            status = input("Enter status to filter by (pending/done✅): ").strip()
            filtered = [task for task in manager.tasks if task["status"] == status]
            if not filtered:
                print("No tasks with that status.")
            else:
                for task in filtered:
                    print(task)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")

if __name__ == "__main__":
    main()
