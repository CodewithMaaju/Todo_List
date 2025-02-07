class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✔ Done" if task.completed else "❌ Not Done"
            print(f"{index}. {task.title} - {status}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print(f"Task '{self.tasks[task_number - 1].title}' marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.title}' has been deleted.")
        else:
            print("Invalid task number.")

# Function to run the interactive menu
def main():
    my_list = ToDoList()

    while True:
        print("\n📌 TO-DO LIST MENU 📌")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            my_list.add_task(title)
        elif choice == "2":
            my_list.show_tasks()
        elif choice == "3":
            my_list.show_tasks()
            task_num = int(input("Enter task number to mark as completed: "))
            my_list.mark_completed(task_num)
        elif choice == "4":
            my_list.show_tasks()
            task_num = int(input("Enter task number to delete: "))
            my_list.delete_task(task_num)
        elif choice == "5":
            print("Goodbye! ✅")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
