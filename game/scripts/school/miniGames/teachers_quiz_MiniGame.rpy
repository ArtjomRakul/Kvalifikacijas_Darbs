# Declare all default variables at the top of the script
default quiz_progress = "math"  # Tracks which quiz is next: math, music, drawing
default quiz_teachers_time_left = 15.0
default quiz_teachers_timer_active = False

# Math Quiz Variables
default math_quiz_total_questions = 5
default math_quiz_question_index = 0
default math_quiz_score = 0

# Music Quiz Variables
default music_quiz_total_questions = 5
default music_quiz_question_index = 0
default music_quiz_score = 0

# Drawing Quiz Variables
default drawing_quiz_total_questions = 5
default drawing_quiz_question_index = 0
default drawing_quiz_score = 0

# Define questions for all quizzes
define math_quiz_questions = [
    {"question": "5 + 7 =", "options": ["10", "11", "12", "13"], "answer": 2},
    {"question": "9 x 6 =", "options": ["54", "45", "63", "36"], "answer": 0},
    {"question": "15 - 8 =", "options": ["5", "6", "7", "8"], "answer": 2},
    {"question": "18 ÷ 3 =", "options": ["5", "6", "7", "8"], "answer": 1},
    {"question": "4 x 4 =", "options": ["12", "14", "16", "18"], "answer": 2},
]

define music_quiz_questions = [
    {"question": "Who composed 'Fur Elise'?", "options": ["Mozart", "Beethoven", "Bach", "Chopin"], "answer": 1},
    {"question": "How many keys does a piano have?", "options": ["76", "88", "61", "72"], "answer": 1},
    {"question": "What is the term for a group of notes?", "options": ["Scale", "Chord", "Arpeggio", "Interval"], "answer": 1},
    {"question": "Highest vocal range?", "options": ["Alto", "Tenor", "Bass", "Soprano"], "answer": 3},
    {"question": "Which instrument has strings and pedals?", "options": ["Violin", "Harp", "Flute", "Trombone"], "answer": 1},
]

define drawing_quiz_questions = [
    {"question": "What are primary colors?", "options": ["Red, Green, Blue", "Red, Yellow, Blue", "Red, Yellow, Green", "Red, Green, White"], "answer": 1},
    {"question": "Which medium uses water?", "options": ["Oil Paint", "Watercolor", "Acrylic", "Pastels"], "answer": 1},
    {"question": "Quick drawing for shapes?", "options": ["Sketch", "Portrait", "Caricature", "Illustration"], "answer": 0},
    {"question": "What is hatching?", "options": ["A shading technique", "A drawing method", "A coloring style", "A painting technique"], "answer": 0},
    {"question": "Who painted Mona Lisa?", "options": ["Van Gogh", "Da Vinci", "Raphael", "Michelangelo"], "answer": 1},
]

# Main label for starting the quiz
label start_teachers_quiz:
    if quiz_progress == "math":
        jump math_quiz_start
    elif quiz_progress == "music":
        jump music_quiz_start
    elif quiz_progress == "drawing":
        jump drawing_quiz_start
    return

# Math Quiz
label math_quiz_start:
    $ quiz_progress = "math"
    python:
        import random
        random.shuffle(math_quiz_questions)
    jump quiz_teachers_loop

# Music Quiz
label music_quiz_start:
    $ quiz_progress = "music"
    python:
        import random
        random.shuffle(music_quiz_questions)
    jump quiz_teachers_loop

# Drawing Quiz
label drawing_quiz_start:
    $ quiz_progress = "drawing"
    python:
        import random
        random.shuffle(drawing_quiz_questions)
    jump quiz_teachers_loop

# Quiz Loop
label quiz_teachers_loop:
    if quiz_progress == "math" and math_quiz_question_index < math_quiz_total_questions:
        $ current_question = math_quiz_questions[math_quiz_question_index]
        $ quiz_score = math_quiz_score
    elif quiz_progress == "music" and music_quiz_question_index < music_quiz_total_questions:
        $ current_question = music_quiz_questions[music_quiz_question_index]
        $ quiz_score = music_quiz_score
    elif quiz_progress == "drawing" and drawing_quiz_question_index < drawing_quiz_total_questions:
        $ current_question = drawing_quiz_questions[drawing_quiz_question_index]
        $ quiz_score = drawing_quiz_score
    else:
        jump quiz_teachers_result

    $ quiz_question_text = current_question["question"]
    $ quiz_options = current_question["options"]
    $ quiz_correct_option = current_question["answer"]
    $ quiz_teachers_time_left = 15.0
    $ quiz_teachers_timer_active = True

    call screen quiz_screen(quiz_question_text, quiz_options, quiz_correct_option)

label quiz_teachers_timeout:
    if quiz_progress == "math":
        $ math_quiz_question_index += 1
    elif quiz_progress == "music":
        $ music_quiz_question_index += 1
    elif quiz_progress == "drawing":
        $ drawing_quiz_question_index += 1
    jump quiz_teachers_loop

label quiz_teachers_result:
    if quiz_progress == "math" and math_quiz_score >= 150:
        $ add_to_inventory(*potion_ingredients["FruitGreen"])
        show screen custom_notify("Come to the music teacher")
        $ quiz_progress = "music"
        $ remove_task("Come to the classroom teacher")
        $ add_task("Come to the music teacher")
        jump mainSchoolLoop
    elif quiz_progress == "music" and music_quiz_score >= 150:
        $ add_to_inventory(*potion_ingredients["RoseWhite"])
        show screen custom_notify("Come to the art teacher")
        $ quiz_progress = "drawing"
        $ remove_task("Come to the music teacher")
        $ add_task("Come to the art teacher")
        jump mainSchoolLoop
    elif quiz_progress == "drawing" and drawing_quiz_score >= 150:
        $ add_to_inventory(*potion_ingredients["PotionGreenBlue"])
        show screen custom_notify("Brew a potion")
        $ quiz_progress = "done"
        $ remove_task("Come to the art teacher")
        $ add_task("Brew a potion")
        jump mainSchoolLoop
    else:
        n "You failed the quiz. Try again!"
        # Reset quiz progress for the current quiz
        if quiz_progress == "math":
            $ math_quiz_question_index = 0
            $ math_quiz_score = 0
            jump math_quiz_start
        elif quiz_progress == "music":
            $ music_quiz_question_index = 0
            $ music_quiz_score = 0
            jump music_quiz_start
        elif quiz_progress == "drawing":
            $ drawing_quiz_question_index = 0
            $ drawing_quiz_score = 0
            jump drawing_quiz_start


# Screens
screen quiz_score_display(quiz_score):
    frame:
        align (0.5, 0.05)
        background "#0008"
        padding (10, 5)
        text "Score: [quiz_score]" size 20

screen quiz_screen(quiz_question_text, quiz_options, quiz_correct_option):
    modal True
    frame:
        align (0.5, 0.5)
        vbox:
            spacing 10
            text quiz_question_text size 30
            for i, option in enumerate(quiz_options):
                textbutton option:
                    action Function(handle_teachers_answer, i, quiz_correct_option)
            bar value AnimatedValue(quiz_teachers_time_left / 15.0) range 1.0:
                xsize 300 ysize 20
                left_bar "#00FF00"
                right_bar "#FF0000"
            text f"Time left: {quiz_teachers_time_left:.1f}" size 20 color "#FF0000" align (0.5, 0.5)
    timer 0.1 repeat True action Function(update_timer)

# Functions
init python:
    def update_timer():
        if store.quiz_teachers_timer_active:
            store.quiz_teachers_time_left -= 0.1
            if store.quiz_teachers_time_left <= 0:
                store.quiz_teachers_timer_active = False
                renpy.jump("quiz_teachers_timeout")

    def handle_teachers_answer(selected_option, correct_option):
        store.quiz_teachers_timer_active = False
        if selected_option == correct_option:
            if store.quiz_progress == "math":
                store.math_quiz_score += 50
            elif store.quiz_progress == "music":
                store.music_quiz_score += 50
            elif store.quiz_progress == "drawing":
                store.drawing_quiz_score += 50
        if store.quiz_progress == "math":
            store.math_quiz_question_index += 1
        elif store.quiz_progress == "music":
            store.music_quiz_question_index += 1
        elif store.quiz_progress == "drawing":
            store.drawing_quiz_question_index += 1
        renpy.jump("quiz_teachers_loop")
