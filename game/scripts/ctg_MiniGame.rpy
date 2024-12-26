# Label to start the mini-game
label start_house_minigame:
    style textbutton is default
    default puzzle_active = False
    $ current_room = 0
    # List of rooms and their background images
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
    default puzzle_slots = [None, None, None]  

    # Define the items present in each room, with their locations indicated
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

# Label to display the current room
label show_room:
    $ room_name, room_image_path = rooms[current_room]

    # Displaying the current room background
    scene expression room_image_path with fade

    # Display items in the room and the backpack icon if riddle has started
    call screen display_items(room_name)

    return


init python:
    # Function to change rooms
    def change_room(direction): # CTG01
        renpy.sound.play(click)  # Play the click sound effect
        global current_room
        # Close any open screens before changing the room
        renpy.hide_screen("inventory_screen_ctg")
        renpy.hide_screen("final_puzzle")

        # Update the current room
        current_room = (current_room + direction) % len(rooms)
        # Refresh the room display
        renpy.call("show_room")

    # Function to pick up an item in a room
    def pick_item(room_name, item_name):    # CTG02
        global riddle_started
        if item_name == "Paper":
            renpy.sound.play(success) # Play the success sound effect
            riddle_started = True
            renpy.notify("Find wisdom in the EARTH, peace in the SKY, and life in the green of NATURE")
            # Remove the paper from the room's items
            room_items[room_name] = [item for item in room_items[room_name] if item[0] != "Paper"]
        elif "Book" in item_name:
            if item_name not in inventory:
                renpy.sound.play(success) # Play the success sound effect
                inventory.append(item_name)
                renpy.notify("You may find this book helpful.")
                # Remove the book from the room's items
                room_items[room_name] = [item for item in room_items[room_name] if item[0] != item_name]
        else:
            renpy.sound.play(fail) # Play the fail sound effect
            renpy.notify("This item has nothing to do with the riddle.")
        renpy.call("show_room")

    # Function to place a book in a puzzle slot
    def set_puzzle_slot(index): # CTG03
        global selected_book, puzzle_slots, inventory
        # Check if a book is selected
        if selected_book is not None:
            puzzle_slots[index] = selected_book
            inventory.remove(selected_book)
            # Clear selected book after setting the slot
            selected_book = None 
    
    # Function to check if the puzzle solution is correct
    def check_puzzle_solution():    # CTG04
        if puzzle_slots == ["BookBrown", "BookBlue", "BookGreen"]:
            renpy.sound.play(success) # Play the success sound effect
            renpy.hide_screen("final_puzzle")
            global puzzle_completed
            puzzle_completed = True
            renpy.jump("puzzle_completed")
        else:
            renpy.sound.play(fail) # Play the fail sound effect
            renpy.notify("The order is incorrect. Try again.")
            renpy.notify("Find wisdom in the EARTH, peace in the SKY, and life in the green of NATURE")
            # Return books to the inventory and reset slots
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
    centered "With potion in hand, you exit the cottage, leaving its mysteries behind."

    # End the mini-game

    jump sisterMeeting