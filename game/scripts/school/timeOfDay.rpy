# Define item and character display conditions, as well as utility functions for screen visibility
init python:
    # Function to hide all interactive screens
    def hide_screens(): # TXT06
        renpy.hide_screen("time_buttons")
        renpy.hide_screen("navigation_arrows")
        renpy.hide_screen("inventory_icon")
        renpy.hide_screen("room_characters")
        renpy.hide_screen("tasks_button")
        renpy.hide_screen("relationships_button")

    # Function to show all interactive screens
    def show_screens(): # TXT05
        renpy.show_screen("time_buttons")
        renpy.show_screen("navigation_arrows")
        renpy.show_screen("inventory_icon")
        renpy.show_screen("room_characters")
        renpy.show_screen("tasks_button")
        renpy.show_screen("relationships_button")

    # Function to start dialogue when interacting with a character
    def start_dialogue(label):  # TXT07
        renpy.call(label)

# Main school location loop
label mainSchoolLoop:
    window hide
    $ update_background()
    $ show_screens()
    while True:
        if check_inventory_for_items(required_ingredients) == True:
            $ hide_screens()
            jump endSchoolMemories
        pause
