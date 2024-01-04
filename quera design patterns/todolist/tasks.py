from interfaces import ITask


class Task(ITask):
    def get_detail(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}, Status: {status}"


class CompositeTask(ITask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subtasks: list[ITask] = []

    def mark_complete(self):
        super().mark_complete()
        for task in self.subtasks:
            task.mark_complete()

    def add_subtask(self, task: ITask):
        self.subtasks.append(task)

    def get_detail(self):
        status = "Completed" if self.completed else "Pending"
        result = f"Composite Task: {self.name}, Status: {status}\n\tSubtasks:"
        for task in self.subtasks:
            result += f"\n\t- {task.get_detail()}"
        return result
