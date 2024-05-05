class Task:
    tasks = []
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed
        Task.tasks.append(self)

    @classmethod
    def show_all_tasks(cls):
        if cls.tasks:
            for task in cls.tasks:
                if not task.completed:
                    print(f"Описание: {task.description}, Срок: {task.due_date}, Статус: Не выполнено")
        else:
            print("Задач нет.")
    @classmethod
    def add_task(cls, description, due_date):
        return cls(description, due_date)

    def mark_completed(self):
        self.completed = True

task1 = Task.add_task("Купить продукты", "2024-05-10")
task2 = Task.add_task("Посетить врача", "2024-05-15")
task3 = Task.add_task("Пройти следующий урок в zerocoder", "2024-05-12")

task1.mark_completed()

Task.show_all_tasks()