label art_teacher_dialogue:
    with fade

    # First interaction
    if art_teacher_interaction == 0 and "Go to an art class" in current_tasks:
        show ArtTeacher at right2
        hide mainCharacter
        show mainCharacter at left2
        ateacher "So [player_name], did you bring everything you need for the lesson this time?"
        p "Yes, teacher!"
        ateacher "Well, get out your paintbrush. Today we're going to paint..."
        p "Isn't that..."
        ateacher "It's a potion. Legend has it that by drinking this potion, a person can understand and realize themselves."
        ateacher "It's also very beautiful and mysterious."
        p "She said, 'a person can understand and realize themselves'? That could be what I need!"
        p "And can you tell me more about this potion, please?"
        ateacher "Okay, this isn't a history class! Sit down and draw this potion! If you draw it well, maybe I'll tell you more about it sometime."
        "After saying that, you are motivated to draw this potion well, as this potion may prove to be the key to getting out of this place."
        ateacher "Class is over, it's still daytime."
        $ remove_task("Go to an art class")
        $ add_task("Talk to your sister in class")
        show screen custom_notify("Talk to your sister in class")
        $ art_teacher_interaction += 1

    # Interaction after talking to the sister
    elif sister_interaction >= 2 and art_teacher_interaction == 1:
        show ArtTeacher at right2
        hide mainCharacter
        show mainCharacter at left2
        ateacher "Did you want something?"
        p "Why did you lie to my sister about the potion?"
        ateacher "(surprised) Potion? What potion?"
        p "We were drawing a potion last lesson and you said you were going to tell me about it."
        ateacher "(misunderstanding) I think you're confused about something. There was no such thing."
        ateacher "If this is some kind of another hoax, it's not to my liking."
        if "Talk to the art teacher" in current_tasks:
            ateacher "Oh, by the way. I wanted to tell you that I've been very unhappy with you lately. You've been in the clouds." 
            ateacher "Your grades are down, you're doing the wrong thing in class."
            ateacher "Last class you were supposed to draw an apple, and you drew some kind of potion."
            ateacher "And now you're asking stupid questions about that potion."
            ateacher "I already went to your homeroom teacher and told him all about you. When you have time, go see him."
            $ remove_task("Talk to the art teacher")
            if "Talk to the music teacher" not in current_tasks:
                show screen custom_notify("Talk to the class teacher")
                $ add_task("Talk to the class teacher")
    elif "Come to the art teacher" in current_tasks:
        $ art_teacher_interaction += 1
        ateacher "So, did you study for the test?"
        p "Yeah, I'm prepared"
        ateacher "All right! Then let's start writing the test paper!"
        jump start_teachers_quiz
    else:
        show ArtTeacher at center
        ateacher "I'm a little busy right now."
    
    hide ArtTeacher
    hide mainCharacter
    with fade
    jump mainSchoolLoop
