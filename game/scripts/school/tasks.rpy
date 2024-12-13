init python:
    current_tasks = []  # A list to hold the current tasks

    # Function to add a task to the list of current tasks
    def add_task(task):
        # Check if the task is not already in the list
        if task not in current_tasks:
            current_tasks.append(task)

    # Function to remove a task from the list of current tasks
    def remove_task(task):
        # Check if the task exists in the list
        if task in current_tasks:
            current_tasks.remove(task)


# Screen to display the "Tasks" button in the UI
screen tasks_button():
    textbutton "Tasks" action Show("tasks_screen") xalign 0.05 yalign 0.03

# Screen to display the list of current tasks
screen tasks_screen():
    # Marks this screen as modal, preventing interaction with other UI elements while open
    tag menu
    modal True
    frame:
        # Apply the task style to the frame
        style_prefix "task"
        xalign 0.5  # Center the frame horizontally
        yalign 0.5  # Center the frame vertically
        vbox:
            spacing 10
            text "Current Tasks" style "task_title"
            # Check if there are any tasks in the current_tasks list
            if current_tasks:
                # Loop through each task and display it
                for task in current_tasks:
                    text task style "task_item"
            else:
                text "No current tasks." style "task_item"
            textbutton "Close" action Hide("tasks_screen")

# Style for the task list title
style task_title:
    size 32
    bold True
    color "#FFFFFF"
    xalign 0.5

# Style for each task item in the list
style task_item:
    size 24
    color "#FFFFFF"
