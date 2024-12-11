init python:
    current_tasks = []  # A list to hold the current tasks

    # Function to add a task to the list of current tasks
    def add_task(task):
        if task not in current_tasks:
            current_tasks.append(task)

    # Function to remove a task from the list of current tasks
    def remove_task(task):
        if task in current_tasks:
            current_tasks.remove(task)


screen tasks_button():
    textbutton "Tasks" action Show("tasks_screen") xalign 0.05 yalign 0.03

screen tasks_screen():
    tag menu
    modal True
    frame:
        style_prefix "task"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            text "Current Tasks" style "task_title"
            if current_tasks:
                for task in current_tasks:
                    text task style "task_item"
            else:
                text "No current tasks." style "task_item"
            textbutton "Close" action Hide("tasks_screen")

style task_title:
    size 32
    bold True
    color "#FFFFFF"
    xalign 0.5

style task_item:
    size 24
    color "#FFFFFF"
