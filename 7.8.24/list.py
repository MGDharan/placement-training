class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")
    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f"Completed task: {self.tasks[task_number]['task']}")
        else:
            print("Invalid task number")
    def display_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} [{status}]")
todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Read a book")
todo_list.display_tasks()
todo_list.complete_task(0)
todo_list.display_tasks()
