init python:
    # Function to add a task to the list of current tasks
    def add_task(task): # TSK01
        # Check if the task is not already in the list
        if task not in current_tasks:
            renpy.sound.play(switch) 
            current_tasks.append(task)

    # Function to remove a task from the list of current tasks
    def remove_task(task):  # TSK02
        # Check if the task exists in the list
        if task in current_tasks:
            renpy.sound.play(switch)
            current_tasks.remove(task)