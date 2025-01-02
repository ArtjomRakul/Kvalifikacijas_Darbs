init python:
    import random

    # Function to determine the winner of a single attempt based on choices
    def determine_winner(player_choice, bully_choice):  # BM01
        if player_choice == bully_choice:
            return "draw"
        elif (
            (player_choice == "rock" and bully_choice == "scissors") or
            (player_choice == "scissors" and bully_choice == "paper") or
            (player_choice == "paper" and bully_choice == "rock")
        ):
            return "player"
        else:
            return "bully"

# Label to start the rock-paper-scissors mini-game
label rock_paper_scissors_game: # BM02
    with fade
    show mainCharacter at left2
    show bully at right2

    # Start the game loop
    while True:
        # Initialize variables for the game
        $ player_score = 0
        $ bully_score = 0
        $ rounds_played = 0
        $ max_rounds = 3
        $ choices = ["rock", "paper", "scissors"]

        # Play 3 rounds of the game
        while rounds_played < max_rounds:
            # Reset scores for the current round
            $ player_wins = 0
            $ bully_wins = 0
            $ attempts = 0
            $ max_attempts = 3

            "Round [rounds_played + 1] begins!"

            # Play attempts in the current round until someone wins 2 attempts or attempts are exhausted
            while attempts < max_attempts and player_wins < 2 and bully_wins < 2:
                menu:
                    "Rock":
                        $ player_choice = "rock"
                    "Paper":
                        $ player_choice = "paper"
                    "Scissors":
                        $ player_choice = "scissors"
                python:
                    renpy.sound.play(switch) # Play the switch sound effect

                # Computer(bully) randomly selects its choice
                $ bully_choice = random.choice(choices)

                # Determine the winner of this attempt
                $ result = determine_winner(player_choice, bully_choice)

                # Display the choices and update scores
                if result == "player":
                    $ player_wins += 1
                    "You chose [player_choice]  -   Bully chose [bully_choice]. You win this attempt!"
                elif result == "bully":
                    $ bully_wins += 1
                    "You chose [player_choice]  -   Bully chose [bully_choice]. The bully wins this attempt."
                else:
                    "You chose [player_choice]  -   Bully chose [bully_choice]. It's a draw!"

                # Increment attempts
                $ attempts += 1
                "Current Score: You - [player_wins], Bully - [bully_wins]. Attempts left: [max_attempts - attempts]."

            # Determine the winner of the round
            if player_wins > bully_wins:
                $ player_score += 1
                "You won Round [rounds_played + 1]!"
            elif bully_wins > player_wins:
                $ bully_score += 1
                "The bully won Round [rounds_played + 1]!"
            else:
                "Round [rounds_played + 1] ended in a draw!"

            # Increment the round count
            $ rounds_played += 1
            "End of Round [rounds_played]. Overall Score: You - [player_score], Bully - [bully_score]."

        # Check the result of the game after all rounds
        if player_score > bully_score:
            python:
                renpy.sound.play(success) # Play the success sound effect
            "Congratulations! You won the rock-paper-scissors game with an overall score of [player_score] to [bully_score]!"
            b "Well, you're lucky this time"
            b "Here are your notes. Take it and go"
            if "BookGreen" not in [item[0] for item in inventory_items if item]:
                $ add_to_inventory(*notes_items["BookGreen"])
            $ remove_task("Take your sister's notes away from the bully")
            $ add_task("Bring the notes to your sister")
            return
        else:
            python:
                renpy.sound.play(fail) # Play the fail sound effect
            "The bully has defeated you. You'll have to try again!"