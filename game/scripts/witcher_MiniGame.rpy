# Declare variables for tracking correct answers, question index, and mini-game completion status
default correct_answers = 0
default question_index = 0
default witch_minigame_completed = False  # Tracks if mini-game is completed

# List of statements and their truth values
init python:
    witch_statements = [
    {"statement": "Shadows - fears and mistakes - only get in the way and keep you from moving forward. If you get rid of them, you will have no obstacles in front of you.", "truth": False},
    {"statement": "Making mistakes is a bad thing. Mistakes show how bad you are, and you don't get better.", "truth": False},
    {"statement": "It was your own fault for the accident that brought you here.", "truth": True},
    {"statement": "You have forgiven yourself for past mistakes.", "truth": False},
    {"statement": "Fear is just a feeling that can be overcome.", "truth": True}
]

    # Function to update the player's score and increments the question index.
    def update_score_and_index(player_answer, correct_answer):  # WTCH01
        renpy.sound.play(click) # Play a sound effect
        global correct_answers, question_index
        if player_answer == correct_answer:
            correct_answers += 1
        question_index += 1

    # Function to check if there are more questions to display.
    def check_next_question_or_end():  # WTCH02
        if question_index < len(witch_statements):
            statement = witch_statements[question_index]["statement"]
            correct_answer = witch_statements[question_index]["truth"]
            renpy.show_screen("witch_minigame_screen", statement=statement, correct_answer=correct_answer)
        else:
            renpy.jump("witch_minigame_end")  # Jump to end of mini-game

# Start of the mini-game label
label witch_minigame:
    # Check if mini-game has already been completed
    if witch_minigame_completed:
        return  # Exit immediately if completed

    # Reset variables at the start
    $ correct_answers = 0
    $ question_index = 0
    $ witch_minigame_completed = True  # Mark mini-game as completed
    if relationship_sister == -1:
        $ witch_statements.append({"statement": "You let your sister down, didn't you? You should regret it.", "truth": True})
    if relationship_wiseMan == -1:
        $ witch_statements.append({"statement": "You've failed the wise man, haven't you? You should regret it.", "truth": True})

    scene witchHouse_bg with fade
    show mainCharacter at left2
    show witch at right2

    $ statement = witch_statements[question_index]["statement"]
    $ correct_answer = witch_statements[question_index]["truth"]
    show screen witch_minigame_screen(statement, correct_answer)

    $ renpy.pause()

# End of the mini-game label
label witch_minigame_end:
    hide screen witch_minigame_screen
    if correct_answers >= 3:
        centered "You have proven your worth."
        $ realLetter = True
    else:
        centered "You failed to prove your worth."
        $ realLetter = False

    jump returnToStranger