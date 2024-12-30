define coin_items = {
    "CoinSilver": ("CoinSilver", im.Scale("images/items/ctg_MiniGame/CoinSilver.png", 100, 100)),
    "CoinBronze": ("CoinBronze", im.Scale("images/items/ctg_MiniGame/CoinBronze.png", 100, 100))
}

default quiz_nerd_started = False

init python:
    # Function to shuffle questions
    def shuffle_questions(questions): # NQ01
        import random
        random.shuffle(questions)

    # Function to update the timer
    def update_timer(): # NQ02
        if store.quiz_timer_active:
            store.quiz_time_left -= 0.1
            if store.quiz_time_left <= 0:
                store.quiz_timer_active = False
                if quiz_nerd_started:
                    renpy.jump("quiz_timeout")  # Trigger timeout handling
                elif quiz_teachers_started:
                    renpy.jump("quiz_teachers_timeout") # Trigger timeout handling

    # Function to handle selected answers
    def handle_quiz_answer(selected_option, correct_option):    # NQ03
        store.quiz_timer_active = False
        if selected_option == correct_option:
            store.quiz_correct_answers += 1
        store.quiz_question_index += 1
        renpy.jump("quiz_loop")

# Quiz Mini-Game with Timer
label start_quiz:
    # Initialize variables
    default quiz_correct_answers = 0
    default quiz_total_questions = 10
    default quiz_question_index = 0
    default quiz_time_left = 15.0
    default quiz_timer_active = False
    $ quiz_nerd_started = True

    # List of quiz questions with options and answers
    define quiz_questions = [
        {"question": "What is the capital of France?", 
        "options": ["Berlin", "Paris", "Rome", "Madrid"], 
        "answer": 1, 
        "subject": "Geography"},

        {"question": "What is the powerhouse of the cell?", 
        "options": ["Nucleus", "Mitochondria", "Ribosome", "Cytoplasm"], 
        "answer": 1, 
        "subject": "Biology"},

        {"question": "What is 12 x 8?", 
        "options": ["96", "88", "108", "86"], 
        "answer": 0, 
        "subject": "Math"},

        {"question": "What is the speed of light in vacuum?", 
        "options": ["3x10^6 m/s", "3x10^8 m/s", "3x10^10 m/s", "3x10^12 m/s"], 
        "answer": 1, 
        "subject": "Physics"},

        {"question": "Who was the first president of the USA?", 
        "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "James Madison"], 
        "answer": 2, 
        "subject": "History"},

        {"question": "What is the largest planet in our solar system?", 
        "options": ["Mars", "Venus", "Jupiter", "Saturn"], 
        "answer": 2, 
        "subject": "Astronomy"},

        {"question": "What is the chemical symbol for gold?", 
        "options": ["Au", "Ag", "Fe", "Cu"], 
        "answer": 0, 
        "subject": "Chemistry"},

        {"question": "Who wrote 'Romeo and Juliet'?", 
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], 
        "answer": 0, 
        "subject": "Literature"},

        {"question": "What is the largest mammal on Earth?", 
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 
        "answer": 1, 
        "subject": "Biology"},

        {"question": "What is the square root of 144?", 
        "options": ["12", "14", "16", "18"], 
        "answer": 0, 
        "subject": "Math"}
    ]

    # Shuffle questions
    python:
        shuffle_questions(quiz_questions)

    # Start quiz loop
    call quiz_loop
    return

# Main quiz loop to display questions
label quiz_loop:
    if quiz_question_index < quiz_total_questions:
        # Get the current question details
        $ current_question = quiz_questions[quiz_question_index]
        $ quiz_question_text = current_question["question"]
        $ quiz_options = current_question["options"]
        $ quiz_correct_option = current_question["answer"]
        $ quiz_subject = current_question["subject"]
        # Reset the timer for the new question
        $ quiz_time_left = 15.0
        $ quiz_timer_active = True

        # Show question screen
        call screen quiz_question_screen_with_timer(
            quiz_question_text, 
            quiz_options, 
            quiz_subject, 
            quiz_correct_option
        )

        # Once the screen returns, go back to top of quiz_loop
        # so we either show next question or end the quiz.
        return
    else:
        # All questions have been asked -> CALL quiz_result
        jump quiz_result

# Handle timeout scenario when the player doesn't answer in time
label quiz_timeout:
    python:
        import random
        # Randomly select an answer
        random_answer = random.randint(0, len(quiz_options) - 1)
        if random_answer == quiz_correct_option:
            quiz_correct_answers += 1
    $ quiz_question_index += 1
    jump quiz_loop

# Show quiz results and determine the outcome
label quiz_result:
    if quiz_correct_answers >= (quiz_total_questions // 2 + 1):
        jump win_quiz
    else:
        jump lose_quiz

# Winning scenario
label win_quiz:
    python:
        renpy.sound.play(success) # Play the success sound effect
        # Add Silver Coin to inventory
        add_to_inventory(*coin_items["CoinSilver"])

    n "You passed the quiz! Congratulations!"
    $ nerdQuizWin = True
    $ remove_task("Go to the club room and meet a nerd")
    $ add_task("Bring the coin to your sister")
    show screen custom_notify("Bring the coin to your sister")
    hide nerd
    hide mainCharacter
    return

# Losing scenario
label lose_quiz:
    python:
        renpy.sound.play(fail) # Play the fail sound effect
        add_to_inventory(*coin_items["CoinBronze"]) # Add Bronze Coin to inventory
    n "You failed the quiz. Better luck next time!"
    $ remove_task("Go to the club room and meet a nerd")
    $ add_task("Bring the coin to your sister")
    show screen custom_notify("Bring the coin to your sister")
    hide nerd
    hide mainCharacter
    return

