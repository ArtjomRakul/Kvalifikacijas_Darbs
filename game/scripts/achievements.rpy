init python:
    # Define the achievements
    achievements = {
        "First Puzzle": {"description": "Complete the first puzzle.", "completed": False},
        "Master Collector": {"description": "Collect all items in the game.", "completed": False},
        "Leaving the Forest": {"description": "Leave the forest location.", "completed": False},
        "Friendship Goal": {"description": "Achieve a high relationship score with characters.", "completed": False},
    }
    
    # Function to unlock an achievement
    def unlock_achievement(name):   # ACH01
        if name in achievements and not achievements[name]["completed"]:
            achievements[name]["completed"] = True
            renpy.notify("Achievement Unlocked: {}".format(achievements[name]["description"]))  # N01

screen achievements_screen():
    tag menu  # Ensures that this screen is treated as a menu
    modal True  # Prevents interaction with other UI elements while open

    frame:
        style_group "achievement_frame"
        xalign 0.5
        yalign 0.5
        background "#333333"
        padding (40, 40, 40, 40)
        vbox:
            spacing 20
            text "Achievements" size 40 color "#FFFFFF" xalign 0.5

            # Scrollable area for achievements
            viewport:
                draggable True
                mousewheel True
                vbox:
                    spacing 15
                    for name, info in achievements.items():
                        # Determine background color based on completion status
                        $ bg_color = "#28a745" if info["completed"] else "#6c757d"
                        hbox:
                            spacing 20
                            # Achievement Container with dynamic background
                            frame:
                                background bg_color
                                padding (10, 10)
                                xminimum 500  # Adjust width as needed
                                yminimum 80   # Adjust height as needed
                                vbox:
                                    spacing 5
                                    text name size 28 color "#FFFFFF" xalign 0.0
                                    text info["description"] size 22 color "#DDDDDD" xalign 0.0
                        
            # Close button
            textbutton "Close" action Hide("achievements_screen") style "close_button"

# Define styles for the frame and buttons
style achievement_frame:
    background "#444444"

style close_button:
    size 30
    color "#FFFFFF"
    background "#007BFF"
    hover_background "#0056b3"
    padding (10, 20)
    xalign 0.5

screen main_ui():
    # Achievements Button at left middle-bottom
    frame:
        xpos 150  # Adjust X position as needed for left alignment
        ypos 250  # Adjust Y position based on your screen resolution
        anchor (0.5, 0.5)
        background "#555555"  # Gray background for the button
        padding (10, 10)
        textbutton "Achievements" action Show("achievements_screen") style "achievements_button"

    # Define style for the Achievements text button
style achievements_button:
    size 24
    color "#FFFFFF"
    background "#6c757d"  # Gray background indicating locked state (can be neutral)
    hover_background "#5a6268"  # Darker gray on hover
    padding (15, 10)
    xalign 0.5
    yalign 0.5
