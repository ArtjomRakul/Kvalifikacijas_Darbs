# Define item and character display conditions, as well as utility functions for screen visibility
init python:
    # Function to hide all interactive screens
    def hide_screens():
        renpy.hide_screen("time_buttons")
        renpy.hide_screen("navigation_arrows")
        renpy.hide_screen("inventory_icon")
        renpy.hide_screen("room_characters")
        renpy.hide_screen("tasks_button")
        renpy.hide_screen("relationships_button")

    # Function to show all interactive screens
    def show_screens():
        renpy.show_screen("time_buttons")
        renpy.show_screen("navigation_arrows")
        renpy.show_screen("inventory_icon")
        renpy.show_screen("room_characters")
        renpy.show_screen("tasks_button")
        renpy.show_screen("relationships_button")

    # Function to start dialogue when interacting with a character
    def start_dialogue(label):
        renpy.call(label)

# Screen for managing time of day with interactive buttons
screen time_buttons():
    hbox:
        xalign 0.85
        yalign 0.03
        # Display a button for the current time of day, allowing the player to advance time
        if time_of_day == "morning":
            textbutton "Morning" action Function(advance_time) background "#ffff88"
        elif time_of_day == "afternoon":
            textbutton "Afternoon" action Function(advance_time) background "#ffff88"
        elif time_of_day == "evening":
            textbutton "Evening" action Function(advance_time) background "#ffff88"

# Screen for room navigation using directional arrows
screen navigation_arrows():
    # Check if the current location has navigation options
    if current_location in navigation_positions:
        for direction, (target_room, xpos, ypos) in navigation_positions[current_location].items():
            # Ensure the target room is visible based on its condition
            if location_conditions.get(target_room, lambda: True)():
                imagebutton:
                    # Display navigation arrows based on direction
                    idle im.Scale({
                        "left": "images/navigation_arrows/arrow_left.png",
                        "right": "images/navigation_arrows/arrow_right.png",
                        "up": "images/navigation_arrows/arrow_up.png",
                        "down": "images/navigation_arrows/arrow_down.png",
                    }.get(direction, "images/navigation_arrows/arrow_right.png"), 75, 75)
                    xpos xpos
                    ypos ypos
                    action Function(change_school_room, target_room)

# Screen for displaying interactive characters in rooms
screen room_characters():
    # Check if there are characters in the current location at the current time of day
    if (current_location, time_of_day) in characters_in_rooms:
        for char_name, char_image, xpos, ypos, dialogue_label in characters_in_rooms[(current_location, time_of_day)]:
            imagebutton:
            # Display the character's image at the specified position
                idle im.Scale(char_image, 500, 500) 
                xpos xpos
                ypos ypos
                # Start dialogue when the character is clicked
                action Function(start_dialogue, dialogue_label)

# Main game loop
label mainSchoolLoop:
    window hide
    $ update_background()
    $ show_screens()
    while True:
        if check_inventory_for_items(required_ingredients) == True:
            $ hide_screens()
            jump endSchoolMemories
        pause
