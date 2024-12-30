# Define the images for the characters, resizing them to 750x750 pixels for consistency
image sister_young = im.Scale("images/characters/sister_young.png", 750, 750)
image nerd = im.Scale("images/characters/nerd.png", 750, 750)
image old_friend = im.Scale("images/characters/old_friend.png", 750, 750)
image bully = im.Scale("images/characters/bully.png", 750, 750)
image ArtTeacher = im.Scale("images/characters/teacher_art.png", 750, 750)
image MusicTeacher = im.Scale("images/characters/teacher_music.png", 750, 750)
image ClassTeacher = im.Scale("images/characters/teacher_class.png", 750, 750)

# Define variables to track interactions with characters
# These variables will increment based on player actions during the game
default sister_interaction = 0 
default art_teacher_interaction = 0
default music_teacher_interaction = 0
default class_teacher_interaction = 0
default old_friend_interaction = 0
default nerd_interaction = 0
default bully_interaction = 0

# Define initial settings for time of day, location, and inventory
default time_of_day = "morning"
default current_location = "hallway11"
default inventory_items = [None] * 10  # Inventory with 10 empty slots
# Define dictionary to map item names to their properties (name and image)
define notes_items = {
    "BookGreen": ("BookGreen", im.Scale("images/items/ctg_MiniGame/BookGreen.png", 100, 100)),
    "BookBlue": ("BookBlue", im.Scale("images/items/ctg_MiniGame/BookBlue.png", 100, 100)),
    "BookBrown": ("BookBrown", im.Scale("images/items/ctg_MiniGame/BookBrown.png", 100, 100))
}
# Define dictionary for potion ingredients with their properties
define potion_ingredients = {
    "FruitGreen" : ("FruitGreen", im.Scale("images/items/ctg_MiniGame/FruitGreen.png", 100, 100)),
    "RoseWhite" : ("RoseWhite", im.Scale("images/items/potion_ingredients/RoseWhite.png", 100, 100)),
    "PotionGreenBlue" : ("PotionGreenBlue", im.Scale("images/items/potion_ingredients/PotionGreenBlue.png", 100, 100))
}

# Define the required items for mini-games
define required_books = {"BookGreen", "BookBlue", "BookBrown"}
define required_potion_ingredients = {"FruitGreen", "RoseWhite", "PotionGreenBlue"}

# Track boolean flags for specific game events
default sister_coin_started = False
default nerdQuizWin = False
default goForAWalk = False

init python:
    # Define conditions for room visibility
    # Each lambda function determines whether the room is accessible to the player
    location_conditions = {
        "hallway11": lambda: True,  # Always accessible
        "classroom11": lambda: True,
        "hallway12": lambda: True,
        "classroom12": lambda: True,
        "hallway13": lambda: True,
        "classroom13": lambda: True,
        "club_entry": lambda: True,
        "club": lambda: True,
        "roof": lambda: True,
    }

    # Determine the position of the navigation buttons for each room
    # Each entry specifies the direction of movement (left, right, up, down) and the coordinates of the buttons
    navigation_positions = {
        "classroom11": {"right": ("hallway11", 1450, 400)},
        "hallway11": {"left": ("classroom11", 300, 500), "up": ("hallway12", 950, 300)},
        "hallway12": {"left": ("classroom12", 300, 500), "up": ("hallway13", 950, 300), "down": ("hallway11", 950, 900)},
        "classroom12": {"right": ("hallway12", 1650, 400)},
        "hallway13": {"left": ("classroom13", 300, 500), "up": ("club_entry", 950, 300), "down": ("hallway12", 950, 900)},
        "classroom13": {"down": ("hallway13", 950, 900)},
        "club_entry": {"left": ("hallway13", 300, 500), "up": ("club", 950, 500), "right": ("roof", 1450, 500)},
        "club": {"right": ("club_entry", 1250, 500)},
        "roof": {"down": ("club_entry", 930, 500)},
    }

    # Determine the presence of characters in certain rooms based on the time of day
    # Each entry includes the room, time, character position and dialog label
    characters_in_rooms = {
        ("classroom11", "morning"): [
            ("Sister", "images/characters/sister_young.png", 1300, 480, "sister_dialogue"),
            ("ClassTeacher", "images/characters/teacher_class.png", 700, 180, "class_teacher_dialogue"),
            ("Nerd", "images/characters/nerd.png", 70, 580, "nerd_dialogue"),
        ],
        ("classroom11", "afternoon"): [
            ("ClassTeacher", "images/characters/teacher_class.png", 700, 180, "class_teacher_dialogue"),
        ],
        ("classroom11", "evening"): [
            ("OldFriend", "images/characters/old_friend.png", 70, 580, "old_friend_dialogue"),
            ("ClassTeacher", "images/characters/teacher_class.png", 700, 180, "class_teacher_dialogue")
        ],
        ("hallway11", "morning"): [
            ("OldFriend", "images/characters/old_friend.png", 1200, 350, "old_friend_dialogue"),
        ],
        ("hallway11", "afternoon"): [
            ("Bully", "images/characters/bully.png", 1200, 350, "bully_dialogue"),
        ],
        ("hallway12", "morning"): [
            ("Bully", "images/characters/bully.png", 1200, 350, "bully_dialogue"),
        ],
        ("hallway13", "evening"): [
            ("Bully", "images/characters/bully.png", 1200, 350, "bully_dialogue"),
        ],
        ("classroom12", "morning"): [
            ("ArtTeacher", "images/characters/teacher_art.png", 700, 580, "art_teacher_dialogue")
        ],
        ("classroom12", "afternoon"): [
            ("ArtTeacher", "images/characters/teacher_art.png", 700, 580, "art_teacher_dialogue"),
        ],
        ("classroom12", "evening"): [
            ("ArtTeacher", "images/characters/teacher_art.png", 700, 580, "art_teacher_dialogue"),
            ("Sister", "images/characters/sister_young.png", 1300, 580, "sister_dialogue")
        ],
        ("classroom13", "morning"): [
            ("MusicTeacher", "images/characters/teacher_music.png", 1100, 330, "music_teacher_dialogue")
        ],
        ("classroom13", "afternoon"): [
            ("MusicTeacher", "images/characters/teacher_music.png", 1100, 330, "music_teacher_dialogue"),
            ("Sister", "images/characters/sister_young.png", 300, 480, "sister_dialogue")
        ],
        ("classroom13", "evening"): [
            ("MusicTeacher", "images/characters/teacher_music.png", 1100, 330, "music_teacher_dialogue")
        ],
        ("club", "afternoon"): [
            ("OldFriend", "images/characters/old_friend.png", 1200, 350, "old_friend_dialogue"),
        ],
        ("club", "evening"): [
            ("Nerd", "images/characters/nerd.png", 70, 480, "nerd_dialogue")
        ],
        ("roof", "afternoon"): [
            ("Nerd", "images/characters/nerd.png", 70, 580, "nerd_dialogue")
        ]
    }