# Define background and rubbish images
image room1 = "images/backgrounds/magic_school/school/classroom11_afternoon.png"
image room2 = "images/backgrounds/magic_school/school/classroom12_afternoon.png"
image room3 = "images/backgrounds/magic_school/school/classroom13_afternoon.png"
image room4 = "images/backgrounds/magic_school/school/club_afternoon.png"
image room5 = "images/backgrounds/magic_school/school/club_cleaning_afternoon.png"
image room6 = "images/backgrounds/magic_school/school/club_desk_afternoon.png"
image room7 = "images/backgrounds/magic_school/school/roof_afternoon.png"

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

# A persistent dictionary to track collected items
init python:
    if not hasattr(persistent, "garbage_collected"):
        persistent.garbage_collected = {}

# Define the collect_garbage function
init python:
    def collect_garbage(room, item):
        # Mark an item as collected in the current room.
        persistent.garbage_collected[(room, item)] = True

    def next_room():
        # Move to the next room or end the mini-game.
        global current_room, collected_garbage
        if current_room < total_rooms:
            current_room += 1
            collected_garbage = 0
            renpy.call("show_rubbish_room")
        else:
            renpy.call("mini_game_end")

# Label to start the mini-game
label rubbish_collector:
    # Reset game variables
    $ current_room = 1
    $ collected_garbage = 0
    $ persistent.garbage_collected.clear()
    call show_rubbish_room from _call_show_rubbish_room
    return

# Label to handle each room
label show_rubbish_room:
    # Display the current room background dynamically
    scene expression "room" + str(current_room)
    
    # Show the room's UI
    call screen room_screen
    return

# Screen for each room
screen room_screen():
    # Display collection progress
    vbox:
        align (0.5, 0.1)
        text "Room [current_room]: [collected_garbage]/[garbage_per_room] items collected" size 30

    # Display rubbish items at fixed positions
    for i, (x, y) in enumerate(item_positions[current_room]):
        if not persistent.garbage_collected.get((current_room, i), False):
            imagebutton:
                idle im.Scale("images/items/nerd_rubbish_MiniGame/Stick.png", 100, 100)
                action [
                    Function(collect_garbage, current_room, i),
                    SetVariable("collected_garbage", collected_garbage + 1)
                ]
                xpos x
                ypos y

    # If all garbage is collected, show navigation button
    if collected_garbage >= garbage_per_room:
        textbutton "Go to Next Room" align (0.5, 0.9) action [Function(next_room)]

# Label for mini-game end
label mini_game_end:
    $ update_background()
    show nerd at right2
    show mainCharacter at left2
    n "Молодец! Ты хорошо справился!"
    n "Ты наверно сильно устал?"
    p "Да, немного..."
    n "Не удивительно. Уборка - это тяжелый труд."
    n "Но ты молодец, что справился с ней!"
    n "Ты заслуживаешь награду!"
    n "Вот мои обещанные записи! Удачи подготовиться к контрольной!"
    p "Спасибо!"
    if "BookBlue" not in [item[0] for item in inventory_items if item]:
        $ add_to_inventory(*notes_items["BookBlue"])
    if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
        $ add_task("Come to the classroom teacher")
    hide nerd
    hide mainCharacter
    jump mainSchoolLoop
