"""Core logic of the Student Task & Study Management System."""
from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class Task:
    task_id: int
    title: str
    subject: str
    due_date: date
    done: bool = False


class TaskManager:
    """Keeps track of a student's tasks and deadlines."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, subject: str, due_date: date) -> Task:
        if not title or not title.strip():
            raise ValueError("Task title must not be empty")
        task = Task(self._next_id, title.strip(), subject, due_date)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> Task:
        task = self.get_task(task_id)
        if task is None:
            raise KeyError(f"Task {task_id} not found")
        task.done = True
        return task

    def pending_tasks(self) -> List[Task]:
        return [t for t in self._tasks if not t.done]

    def overdue_tasks(self, today: date) -> List[Task]:
        return [t for t in self._tasks if not t.done and t.due_date < today]

    def progress_percent(self) -> float:
        if not self._tasks:
            return 0.0
        done = sum(1 for t in self._tasks if t.done)
        return round(done * 100 / len(self._tasks), 2)
