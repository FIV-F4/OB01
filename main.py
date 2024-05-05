class Task:
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def show_all_tasks(self):
        pass
    def add_tasks(self):
        pass

    def mark_completed(self):
        self.completed = True