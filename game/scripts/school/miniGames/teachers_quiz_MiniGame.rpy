default quiz_progress = "math"  # Tracks which quiz is next: math, music, drawing
default quiz_teachers_started = False

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
    {"question": "5 + 7 =", 
    "options": ["10", "11", "12", "13"], 
    "answer": 2},

    {"question": "9 x 6 =", 
    "options": ["54", "45", "63", "36"], 
    "answer": 0},

    {"question": "15 - 8 =", 
    "options": ["5", "6", "7", "8"], 
    "answer": 2},

    {"question": "18 ÷ 3 =", 
    "options": ["5", "6", "7", "8"], 
    "answer": 1},

    {"question": "4 x 4 =", 
    "options": ["12", "14", "16", "18"], 
    "answer": 2},
]

define music_quiz_questions = [
    {"question": "Who composed 'Fur Elise'?", 
    "options": ["Mozart", "Beethoven", "Bach", "Chopin"], 
    "answer": 1},

    {"question": "How many keys does a piano have?", 
    "options": ["76", "88", "61", "72"], 
    "answer": 1},

    {"question": "What is the term for a group of notes?", 
    "options": ["Scale", "Chord", "Arpeggio", "Interval"], 
    "answer": 1},

    {"question": "Highest vocal range?", 
    "options": ["Alto", "Tenor", "Bass", "Soprano"], 
    "answer": 3},

    {"question": "Which instrument has strings and pedals?", 
    "options": ["Violin", "Harp", "Flute", "Trombone"], 
    "answer": 1},
]

define drawing_quiz_questions = [
    {"question": "What are primary colors?", 
    "options": ["Red, Green, Blue", "Red, Yellow, Blue", "Red, Yellow, Green", "Red, Green, White"], 
    "answer": 1},
    
    {"question": "Which medium uses water?", 
    "options": ["Oil Paint", "Watercolor", "Acrylic", "Pastels"], 
    "answer": 1},

    {"question": "Quick drawing for shapes?", 
    "options": ["Sketch", "Portrait", "Caricature", "Illustration"], 
    "answer": 0},

    {"question": "What is hatching?", 
    "options": ["A shading technique", "A drawing method", "A coloring style", "A painting technique"], 
    "answer": 0},

    {"question": "Who painted Mona Lisa?", 
    "options": ["Van Gogh", "Da Vinci", "Raphael", "Michelangelo"], 
    "answer": 1},
]

# Timer and answer handling functions
init python:
    # Function to handle selected answers
    def handle_teachers_answer(selected_option, correct_option): # TCHR01
        renpy.sound.play(switch) # Play the switch sound effect
        store.quiz_timer_active = False
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
        renpy.jump("quiz_teachers_loop")    # Move to the next question

# Main label for starting the quiz
label start_teachers_quiz:
    # Determine which quiz to start based on quiz_progress
    if quiz_progress == "math":
        call math_quiz_start
    elif quiz_progress == "music":
        call music_quiz_start
    elif quiz_progress == "drawing":
        call drawing_quiz_start
    return

# Labels for starting each specific quiz
label math_quiz_start:
    $ quiz_progress = "math"
    # Shuffle questions
    python:
        shuffle_questions(math_quiz_questions)
    call quiz_teachers_loop
    return

label music_quiz_start:
    $ quiz_progress = "music"
    # Shuffle questions
    python:
        shuffle_questions(music_quiz_questions)
    call quiz_teachers_loop
    return

label drawing_quiz_start:
    $ quiz_progress = "drawing"
    # Shuffle questions
    python:
        shuffle_questions(drawing_quiz_questions)
    call quiz_teachers_loop
    return

# Main loop for presenting quiz questions
label quiz_teachers_loop:
    # Load the current question and progress for the active quiz
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
        call quiz_teachers_result   # Jump to the result screen if all questions are answered
        return

    # Prepare question data for display
    $ quiz_question_text = current_question["question"]
    $ quiz_options = current_question["options"]
    $ quiz_correct_option = current_question["answer"]
    $ quiz_time_left = 15.0
    $ quiz_timer_active = True

    call screen quiz_screen(
        quiz_question_text, 
        quiz_options, 
        quiz_correct_option
    )
    
    return

# Handle timeout when the player doesn't answer in time
label quiz_teachers_timeout:
    if quiz_progress == "math":
        $ math_quiz_question_index += 1
    elif quiz_progress == "music":
        $ music_quiz_question_index += 1
    elif quiz_progress == "drawing":
        $ drawing_quiz_question_index += 1
    jump quiz_teachers_loop     # Move to the next question

# Display results and handle the next steps
label quiz_teachers_result: # TCHR02
    if quiz_progress == "math" and math_quiz_score >= 150:
        python:
            renpy.sound.play(success)
        $ add_to_inventory(*potion_ingredients["FruitGreen"])
        show screen custom_notify("Talk to the music teacher")
        $ quiz_progress = "music"
        $ remove_task("Come to the classroom teacher")
        $ add_task("Come to the music teacher")
        return
    elif quiz_progress == "music" and music_quiz_score >= 150:
        python:
            renpy.sound.play(success)
        $ add_to_inventory(*potion_ingredients["RoseWhite"])
        show screen custom_notify("Talk to the art teacher")
        $ quiz_progress = "drawing"
        $ remove_task("Come to the music teacher")
        $ add_task("Come to the art teacher")
        return
    elif quiz_progress == "drawing" and drawing_quiz_score >= 150:
        python:
            renpy.sound.play(success)
        $ add_to_inventory(*potion_ingredients["PotionGreenBlue"])
        $ quiz_progress = "done"
        $ remove_task("Come to the art teacher")
        return
    else:
        n "You failed the quiz. Try again!"
        # Resetting test results for retry
        if quiz_progress == "math":
            python:
                renpy.sound.play(fail)
            $ math_quiz_question_index = 0
            $ math_quiz_score = 0
            jump math_quiz_start
        elif quiz_progress == "music":
            python:
                renpy.sound.play(fail)
            $ music_quiz_question_index = 0
            $ music_quiz_score = 0
            jump music_quiz_start
        elif quiz_progress == "drawing":
            python:
                renpy.sound.play(fail)
            $ drawing_quiz_question_index = 0
            $ drawing_quiz_score = 0
            jump drawing_quiz_start