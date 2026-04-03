from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner("Alice")
    pet1 = Pet("Rex", "Dog")
    pet2 = Pet("Mittens", "Cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    pet1.add_task(Task("Morning Walk", "08:00"))
    pet1.add_task(Task("Evening Walk", "18:00"))
    pet2.add_task(Task("Feed", "08:00"))

    scheduler = Scheduler(owner)
    
    print("Today's Schedule:")
    tasks = scheduler.sort_by_time(owner.get_all_tasks())
    for pet_name, task in tasks:
        print(f"[{task.time}] {pet_name}: {task.description} {'(Done)' if task.completed else ''}")
        
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        print(f"\nWarning! Conflicts detected at times: {', '.join(conflicts)}")

if __name__ == "__main__":
    main()
