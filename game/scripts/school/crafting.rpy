init python:
    # Function to craft the potion
    def craft_potion():
        global inventory, required_potion_ingredients
        # Remove required items from inventory
        for item in required_potion_ingredients:
            remove_from_inventory(item)
        # Add the crafted potion to inventory
        renpy.notify("You have crafted the Potion!")
        # Proceed to the ending
        renpy.hide_screen("crafting_screen")
        renpy.jump("endSchoolMemories")

# Screen for crafting the potion
screen crafting_screen():
    modal True  # Prevent interaction with other UI elements
    frame:
        align (0.5, 0.5)
        background "#222222"
        padding (30, 30, 30, 30)
        vbox:
            spacing 20
            text "Craft Potion" size 40 color "#FFFFFF" xalign 0.5

            text "Combine the following ingredients to craft the potion:" size 24 color "#FFFFFF" xalign 0.5

            # Display the required ingredients
            hbox:
                spacing 10
                add im.Scale("images/items/ctg_MiniGame/FruitGreen.png", 100, 100)
                add im.Scale("images/items/potion_ingredients/RoseWhite.png", 100, 100)
                add im.Scale("images/items/potion_ingredients/PotionGreenBlue.png", 100, 100)

            # Craft Button
            textbutton "Craft Potion" action Function(craft_potion) style "craft_button"

# Define styles for the buttons
style craft_button:
    size 30
    color "#FFFFFF"
    background "#28a745"  # Green background
    hover_background "#218838"
    padding (10, 20)
    xalign 0.5
