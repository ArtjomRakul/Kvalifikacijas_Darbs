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