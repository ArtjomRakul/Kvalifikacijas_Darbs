# Define background images for each room
image room1 = "images/backgrounds/magic_school/school/classroom11_afternoon.png"
image room2 = "images/backgrounds/magic_school/school/classroom12_afternoon.png"
image room3 = "images/backgrounds/magic_school/school/classroom13_afternoon.png"
image room4 = "images/backgrounds/magic_school/school/club_afternoon.png"
image room5 = "images/backgrounds/magic_school/school/club_cleaning_afternoon.png"
image room6 = "images/backgrounds/magic_school/school/club_desk_afternoon.png"
image room7 = "images/backgrounds/magic_school/school/roof_afternoon.png"

# Define the rubbish item image
image rubbish = "images/items/nerd_rubbish_MiniGame/Stick.png"

# Initialize variables
default current_room = 1
default collected_garbage = 0
default total_rooms = 7
define garbage_per_room = 5

# Fixed positions for rubbish items in each room
init python:
    item_positions = {
        1: [(500, 875), (900, 875), (1500, 575), (700, 750), (1250, 650)],
        2: [(100, 950), (1100, 725), (850, 850), (750, 350), (1700, 850)],
        3: [(120, 720), (450, 580), (720, 600), (1550, 900), (1650, 550)],
        4: [(300, 850), (450, 800), (700, 800), (1000, 750), (1000, 850)],
        5: [(500, 340), (700, 700), (900, 900), (1350, 900), (1460, 600)],
        6: [(100, 210), (300, 350), (500, 220), (700, 260), (900, 310)],
        7: [(350, 750), (350, 900), (550, 900), (850, 850), (1500, 900)]
    }

# A persistent dictionary to keep track of collected items across sessions
init python:
    if not hasattr(persistent, "garbage_collected"):
        persistent.garbage_collected = {}

# Functions for the mini-game logic
init python:
    # Function to mark an item as collected
    def collect_garbage(room, item):
        # Add the collected item to the persistent dictionary
        persistent.garbage_collected[(room, item)] = True

    # Function to move to the next room
    def next_room():
        global current_room, collected_garbage
        if current_room < total_rooms:
            current_room += 1
            collected_garbage = 0
            # Load the next room
            renpy.call("show_rubbish_room")
        else:
            renpy.call("mini_game_end")

# Label to start the mini-game
label rubbish_collector:
    # Reset game variables for a fresh start
    $ current_room = 1
    $ collected_garbage = 0
    # Clear all collected garbage data
    $ persistent.garbage_collected.clear()
    call show_rubbish_room from _call_show_rubbish_room
    return

# Label to display the current room
label show_rubbish_room:
    # Dynamically set the room background based on the current room
    scene expression "room" + str(current_room)
    
    # Show the room's UI
    call screen room_screen
    return

# Screen to display room UI and rubbish items
screen room_screen():
    # Display collection progress at the top of the screen
    vbox:
        align (0.5, 0.1)
        text "Room [current_room]: [collected_garbage]/[garbage_per_room] items collected" size 30

    # Display rubbish items at their predefined positions
    for i, (x, y) in enumerate(item_positions[current_room]):
        # Only show items that have not yet been collected
        if not persistent.garbage_collected.get((current_room, i), False):
            imagebutton:
                idle im.Scale("images/items/nerd_rubbish_MiniGame/Stick.png", 100, 100)
                action [
                    # Mark item as collected
                    Function(collect_garbage, current_room, i),
                    SetVariable("collected_garbage", collected_garbage + 1)
                ]
                xpos x
                ypos y

    # If all garbage is collected, show a button to move to the next room
    if collected_garbage >= garbage_per_room:
        textbutton "Go to Next Room" align (0.5, 0.9) action [Function(next_room)]

# Label to handle the end of the mini-game
label mini_game_end:
    # Update background to default or post-game state
    $ update_background()
    show nerd at right2
    show mainCharacter at left2
    n "Well done! You did good!"
    n "You must be pretty tired, huh?"
    p "Yeah, a little bit..."
    n "No wonder. Cleaning is hard work."
    n "But good for you for handling it!"
    n "You deserve an award!"
    n "Here are my promised notes! Good luck studying for the test!"
    p "Thank you!"
    # Add a reward to the inventory if not already present
    if "BookBlue" not in [item[0] for item in inventory_items if item]:
        $ add_to_inventory(*notes_items["BookBlue"])
    if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
        $ add_task("Come to the classroom teacher")
    # Hide characters and return to the main loop
    hide nerd
    hide mainCharacter
    jump mainSchoolLoop
