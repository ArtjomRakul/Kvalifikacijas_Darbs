# Define variables for character relationships
default relationship_wiseMan = 0 
default relationship_sister = 0 
default sister_relationship = 0 
default music_teacher_relationship = 0
default old_friend_relationship = 0
default overall_relationships = 0 

init python:
    def get_relationship_status(score):
        if score > 0:
            return "Positive (+[score])" 
        elif score < 0:
            return "Negative ([score])"
        else:
            return "Neutral (0)"

# Button to open the Relationships screen
screen relationships_button():
    textbutton "Relationships" action Show("relationships_screen") xalign 0.95 yalign 0.1

# Screen to display relationship statuses
screen relationships_screen():
    tag menu
    modal True

    frame:
        style_prefix "relationship"
        xalign 0.5
        yalign 0.5
        padding (20, 20, 20, 20)
        background "#222222"

        vbox:
            spacing 15
            text "Relationships" style "relationship_title"

            # Display each character's relationship status
            text "Sister: [get_relationship_status(sister_relationship)]" style "relationship_item"
            text "Music Teacher: [get_relationship_status(music_teacher_relationship)]" style "relationship_item"
            text "Old Friend: [get_relationship_status(old_friend_relationship)]" style "relationship_item"

            # Close button
            textbutton "Close" action Hide("relationships_screen")
