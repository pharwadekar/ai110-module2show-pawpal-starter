from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Task:
    description: str
    time: str
    frequency: str = "Once"
    completed: bool = False

    def mark_complete(self):
        self.completed = True

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_all_tasks(self):
        return [(pet.name, task) for pet in self.pets for task in pet.tasks]

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self, tasks):
        return sorted(tasks, key=lambda x: datetime.strptime(x[1].time, "%H:%M"))

    def detect_conflicts(self):
        tasks = self.owner.get_all_tasks()
        times = set()
        conflicts = []
        for _, task in tasks:
            if task.time in times:
                conflicts.append(task.time)
            times.add(task.time)
        return conflicts
