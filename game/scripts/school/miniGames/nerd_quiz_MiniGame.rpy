define coin_items = {
    "CoinSilver": ("CoinSilver", im.Scale("images/items/ctg_MiniGame/CoinSilver.png", 100, 100)),  # Silver Coin image path
    "CoinBronze": ("CoinBronze", im.Scale("images/items/ctg_MiniGame/CoinBronze.png", 100, 100))   # Bronze Coin image path
}

# Quiz Mini-Game with Timer and Error Fix
label start_quiz:
    # Initialize variables
    default quiz_correct_answers = 0
    default quiz_total_questions = 10
    default quiz_question_index = 0
    default quiz_time_left = 10.0
    default quiz_timer_active = False

    # Questions and answers
    define quiz_questions = [
        {"question": "What is the capital of France?", "options": ["Berlin", "Paris", "Rome", "Madrid"], "answer": 1, "subject": "Geography"},
        {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Mitochondria", "Ribosome", "Cytoplasm"], "answer": 1, "subject": "Biology"},
        {"question": "What is 12 x 8?", "options": ["96", "88", "108", "86"], "answer": 0, "subject": "Math"},
        {"question": "What is the speed of light in vacuum?", "options": ["3x10^6 m/s", "3x10^8 m/s", "3x10^10 m/s", "3x10^12 m/s"], "answer": 1, "subject": "Physics"},
        {"question": "Who was the first president of the USA?", "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "James Madison"], "answer": 2, "subject": "History"},
        {"question": "What is the largest planet in our solar system?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": 2, "subject": "Astronomy"},
        {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Fe", "Cu"], "answer": 0, "subject": "Chemistry"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "answer": 0, "subject": "Literature"},
        {"question": "What is the largest mammal on Earth?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": 1, "subject": "Biology"},
        {"question": "What is the square root of 144?", "options": ["12", "14", "16", "18"], "answer": 0, "subject": "Math"}
    ]

    # Shuffle questions
    python:
        import random
        random.shuffle(quiz_questions)

    # Start quiz loop
    jump quiz_loop

label quiz_loop:
    if quiz_question_index < quiz_total_questions:
        $ current_question = quiz_questions[quiz_question_index]
        $ quiz_question_text = current_question["question"]
        $ quiz_options = current_question["options"]
        $ quiz_correct_option = current_question["answer"]
        $ quiz_subject = current_question["subject"]
        $ quiz_time_left = 10.0
        $ quiz_timer_active = True

        # Show question screen
        call screen quiz_question_screen_with_timer(quiz_question_text, quiz_options, quiz_subject, quiz_correct_option)
        return
    else:
        jump quiz_result

label quiz_timeout:
    python:
        import random
        # Randomly select an answer
        random_answer = random.randint(0, len(quiz_options) - 1)
        if random_answer == quiz_correct_option:
            quiz_correct_answers += 1
    $ quiz_question_index += 1
    jump quiz_loop


label quiz_result:
    if quiz_correct_answers >= (quiz_total_questions // 2 + 1):
        jump win_quiz
    else:
        jump lose_quiz

# Screen for questions with timer
screen quiz_question_screen_with_timer(quiz_question_text, quiz_options, quiz_subject, quiz_correct_option):
    modal True
    frame:
        align (0.5, 0.5)
        vbox:
            spacing 10
            text f"Subject: {quiz_subject}" size 30
            text quiz_question_text size 25
            for i, option in enumerate(quiz_options):
                textbutton option:
                    action Function(handle_quiz_answer, i, quiz_correct_option)
            bar value AnimatedValue(quiz_time_left / 10.0) range 1.0:
                xsize 300 ysize 20
                left_bar "#00FF00"
                right_bar "#FF0000"
            text f"Time left: {quiz_time_left:.1f} seconds" size 20 color "#FF0000" align (0.5, 0.5)
    # Timer countdown
    timer 0.1 repeat True action Function(update_timer)

# Timer and answer handling functions
init python:
    def update_timer():
        store.quiz_time_left -= 0.1
        if store.quiz_time_left <= 0:
            store.quiz_timer_active = False
            renpy.jump("quiz_timeout")

    def handle_quiz_answer(selected_option, correct_option):
        store.quiz_timer_active = False
        if selected_option == correct_option:
            store.quiz_correct_answers += 1
        store.quiz_question_index += 1
        renpy.jump("quiz_loop")

# Endings
label win_quiz:
    n "You passed the quiz! Congratulations!"
    $ nerdQuizWin = True
    python:
        # Add Silver Coin to inventory
        add_to_inventory(*coin_items["CoinSilver"])
    $ remove_task("Go to the club room and meet a nerd")
    $ add_task("Bring the coin to your sister")
    show screen custom_notify("Bring the coin to your sister")
    jump mainSchoolLoop

label lose_quiz:
    n "You failed the quiz. Better luck next time!"
    python:
        # Add Bronze Coin to inventory
        add_to_inventory(*coin_items["CoinBronze"])
    $ remove_task("Go to the club room and meet a nerd")
    $ add_task("Bring the coin to your sister")
    show screen custom_notify("Bring the coin to your sister")
    jump mainSchoolLoop

