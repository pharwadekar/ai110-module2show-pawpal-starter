import pytest
from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    task = Task("Walk", "10:00")
    task.mark_complete()
    assert task.completed == True

def test_task_addition():
    pet = Pet("Rex", "Dog")
    task = Task("Walk", "10:00")
    pet.add_task(task)
    assert len(pet.tasks) == 1

def test_sorting():
    owner = Owner("Alice")
    pet = Pet("Rex", "Dog")
    owner.add_pet(pet)
    pet.add_task(Task("Walk", "12:00"))
    pet.add_task(Task("Feed", "08:00"))
    
    scheduler = Scheduler(owner)
    tasks = scheduler.sort_by_time(owner.get_all_tasks())
    assert tasks[0][1].description == "Feed"
    assert tasks[1][1].description == "Walk"

def test_conflict_detection():
    owner = Owner("Alice")
    pet1 = Pet("Rex", "Dog")
    pet2 = Pet("Mittens", "Cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    pet1.add_task(Task("Walk", "12:00"))
    pet2.add_task(Task("Feed", "12:00"))
    
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert "12:00" in conflicts
