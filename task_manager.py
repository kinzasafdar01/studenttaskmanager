class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        title = title.strip()

        if not title:
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def complete_task(self, task_id):
        raise ValueError("Complete feature is not implemented yet.")

    def delete_task(self, task_id):
        raise ValueError("Delete feature is not implemented yet.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f'{task["id"]}. {task["title"]} [{status}]')


def main():
    manager = TaskManager()

    while True:
        print("\nSTUDENT TASK MANAGER")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                task = manager.add_task(input("Enter task title: "))
                print(f'Task added with ID {task["id"]}.')
            elif choice == "2":
                manager.display_tasks()
            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                manager.complete_task(task_id)
                print("Task marked as completed.")
            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                print("Task deleted.")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Choose 1 to 5.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()