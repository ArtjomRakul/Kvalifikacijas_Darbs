# Define variables for character relationships
# These variables will increment based on player actions during the game
default relationship_wiseMan = 0 
default relationship_sister = 0 
default sister_relationship = 0 
default music_teacher_relationship = 0
default old_friend_relationship = 0
default overall_relationships = 0 

init python:
    # Function to get the relationship status as a text based on the score
    def get_relationship_status(score): # RLTS01
        if score > 0:
            return f"Positive (+{score})"
        elif score < 0:
            return f"Negative ({score})"
        else:
            return "Neutral (0)"


# Button to open the Relationships screen
screen relationships_button():
    textbutton "Relationships" action Show("relationships_screen") xalign 0.95 yalign 0.1

# Screen to display relationship statuses
screen relationships_screen():
    tag menu    # Identifies this screen as a menu-type screen
    modal True  # Prevent interaction with other game elements while this screen is open

    frame:
        style_prefix "relationship" # Use a style prefix for consistent styling
        xalign 0.5  # Center the frame horizontally
        yalign 0.5  # Center the frame vertically
        padding (20, 20, 20, 20)    # Add padding inside the frame
        background "#222222"

        vbox:
            spacing 15  # Add space between each element in the vertical box layout
            text "Relationships" style "relationship_title"

            # Display each character's relationship status
            text "Sister: [get_relationship_status(sister_relationship)]" style "relationship_item"
            text "Music Teacher: [get_relationship_status(music_teacher_relationship)]" style "relationship_item"
            text "Old Friend: [get_relationship_status(old_friend_relationship)]" style "relationship_item"

            # Close button to exit the relationships screen
            textbutton "Close" action Hide("relationships_screen")
