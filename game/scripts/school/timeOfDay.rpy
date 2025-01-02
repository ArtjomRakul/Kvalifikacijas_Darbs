# Define item and character display conditions, as well as utility functions for screen visibility
init python:
    # Function to hide all interactive screens
    def hide_screens(): # TXT02
        renpy.hide_screen("time_buttons")
        renpy.hide_screen("navigation_arrows")
        renpy.hide_screen("inventory_icon")
        renpy.hide_screen("room_characters")
        renpy.hide_screen("tasks_button")
        renpy.hide_screen("relationships_button")

    # Function to show all interactive screens
    def show_screens(): # TXT01
        renpy.show_screen("time_buttons")
        renpy.show_screen("navigation_arrows")
        renpy.show_screen("inventory_icon")
        renpy.show_screen("room_characters")
        renpy.show_screen("tasks_button")
        renpy.show_screen("relationships_button")

    # Function to start dialogue when interacting with a character
    def start_dialogue(label):  # TXT03
        hide_screens()
        renpy.call(label)


# Main entry point into the school exploration part of the game
label school_exploration:
    # Always show the interactive screens so the player can navigate:
    window hide
    $ update_background()
    $ show_screens()
    
    # As long as the player doesn’t have all items, 
    # we keep returning here after dialogues or mini-games.
    label exploration_loop:
        # Check if all required items have been collected. If yes, jump to end.
        if check_inventory_for_items(required_potion_ingredients):
            $ hide_screens()
            call unlock_achievement("Master Collector")
            show screen crafting_screen
        
        # We use Ren’Py’s "pause" to wait for user interaction. While paused, 
        # the player can navigate rooms, interact with characters, etc.
        pause

        jump exploration_loop

    return