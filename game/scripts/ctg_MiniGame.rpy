# Label to start the mini-game
label start_house_minigame:
    style textbutton is default
    default puzzle_active = False
    $ current_room = 0
    $ rooms = [
        ("hearth", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageHearth.png", 1920, 1080)),
        ("kitchen", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageKitchen.png", 1920, 1080)),
        ("bedroom", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageBedroom.png", 1920, 1080)),
        ("windows", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageWindows.png", 1920, 1080)),
        ("interior", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageInterior.png", 1920, 1080)),
        ("table", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageTable.png", 1920, 1080)),
        ("library", im.Scale("images/backgrounds/cottage_MiniGame/cottage_backgrounds/CottageLibrary.png", 1920, 1080))
    ]

    # Initialize the inventory and flags
    default inventory = []
    default riddle_started = False
    default puzzle_completed = False
    default puzzle_slots = [None, None, None]  # To hold book order for the puzzle

    # Define items in each roomgame/
    $ room_items = {
        "hearth": [("Paper", im.Scale("images/items/ctg_MiniGame/Paper.png", 100, 100), 1150, 725)],
        "kitchen": [("FruitGreen", im.Scale("images/items/ctg_MiniGame/FruitGreen.png", 100, 100), 1150, 725)],
        "bedroom": [("BookBlue", im.Scale("images/items/ctg_MiniGame/BookBlue.png", 100, 100), 1150, 725)],
        "windows": [("BookGreen", im.Scale("images/items/ctg_MiniGame/BookGreen.png", 100, 100), 1150, 725)],
        "interior": [("CoinSilver", im.Scale("images/items/ctg_MiniGame/CoinSilver.png", 100, 100), 1150, 725)],
        "table": [("BookBrown", im.Scale("images/items/ctg_MiniGame/BookBrown.png", 100, 100), 1150, 725)],
        "library": []
    }

    # Show the initial room
    call show_room from _call_show_room

    return

# Function to display the current room
label show_room:
    $ room_name, room_image_path = rooms[current_room]

    # Display the current room's background
    scene expression room_image_path with fade

    # Display items in the room and backpack icon if riddle has started
    call screen display_items(room_name)

    return

# Python function to change rooms and pick items
init python:
    def change_room(direction):
        global current_room
        # Close any open screens before changing the room
        renpy.hide_screen("inventory_screen_ctg")
        renpy.hide_screen("final_puzzle")

        # Update the current room
        current_room = (current_room + direction) % len(rooms)
        renpy.call("show_room")

    def pick_item(room_name, item_name):
        global riddle_started
        if item_name == "Paper":
            riddle_started = True
            renpy.notify("Find wisdom in the {color=#8b4e25}earth{/color}, peace in the {color=#0000ff}sky{/color}, and life in the green of {color=#00ff00}nature{/color}")
            room_items[room_name] = [item for item in room_items[room_name] if item[0] != "Paper"]
        elif "Book" in item_name:
            if item_name not in inventory:
                inventory.append(item_name)
                renpy.notify("You may find this book helpful.")
                room_items[room_name] = [item for item in room_items[room_name] if item[0] != item_name]
        else:
            renpy.notify("This item has nothing to do with the riddle.")
        renpy.call("show_room")

    def set_puzzle_slot(index):
        global selected_book, puzzle_slots, inventory
        if selected_book is not None:
            puzzle_slots[index] = selected_book
            inventory.remove(selected_book)  # Remove the selected book from the inventory
            selected_book = None  # Clear selected book after setting the slot

    def check_puzzle_solution():
        if puzzle_slots == ["BookBrown", "BookBlue", "BookGreen"]:
            renpy.hide_screen("final_puzzle")
            global puzzle_completed
            puzzle_completed = True
            renpy.jump("puzzle_completed")
        else:
            renpy.notify("The order is incorrect. Try again.")
            renpy.notify("Find wisdom in the {color=#8b4e25}earth{/color}, peace in the {color=#0000ff}sky{/color}, and life in the green of {color=#00ff00}nature{/color}")
            for i in range(3):
                if puzzle_slots[i] is not None:
                    inventory.append(puzzle_slots[i])  # Return the books to inventory
                puzzle_slots[i] = None
        renpy.call("show_room")
        
# Label for the puzzle completion and ending scene
label puzzle_completed:
    # Show message for finding the potion
    scene black with fade
    centered "You have found a mysterious potion hidden in the depths of the library..."

    # Give the player a final message before leaving
    centered "With potion in hand, you exit the cottage, leaving its mysteries behind."

    # End the mini-game
    jump sisterMeeting