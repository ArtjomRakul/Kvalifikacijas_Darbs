init python:
    # Function to change the current school room
    def change_school_room(new_location):
        global current_location
        # Update the global variable to the new location
        current_location = new_location
        # Update the background to reflect the change in location
        update_background(transition=dissolve)

    # Function to update background based on room and time of day
    def update_background(transition=None):
        # Hide all backgrounds before showing the current one
        for location in navigation_positions:
            for time in ["morning", "afternoon", "evening"]:
                renpy.hide(f"{location}_{time}")
        
        # Show the new background with a transition
        if transition:
            renpy.transition(transition)  # Queue the transition correctly
        renpy.show(f"{current_location}_{time_of_day}")

    # Function to advance the in-game time of day
    def advance_time(): # RSCH02
        global time_of_day
        time_of_day = {"morning": "afternoon", "afternoon": "evening", "evening": "morning"}[time_of_day]
        update_background()