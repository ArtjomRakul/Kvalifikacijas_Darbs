init python:
    # Function to update the background based on the player's current room and time of day
    def update_background(): # RSCH01
        # Hide all backgrounds first
        for location in navigation_positions:
            for time in ["morning", "afternoon", "evening"]:
                renpy.hide(f"{location}_{time}")

        renpy.transition(dissolve)  # Apply the transition effect
        renpy.show(f"{current_location}_{time_of_day}")

    # Function to advance the in-game time of day
    def advance_time(): # RSCH02
        global time_of_day
        time_of_day = {"morning": "afternoon", "afternoon": "evening", "evening": "morning"}[time_of_day]
        update_background()