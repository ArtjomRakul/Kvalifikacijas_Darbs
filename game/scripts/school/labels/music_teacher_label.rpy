
label music_teacher_dialogue:
    $ hide_screens()
    with fade
    if music_teacher_interaction == 0:
        show MusicTeacher at right2
        show mainCharacter at left2
        mteacher "You're not gonna be a singer. Your voice is as bad as your sister's.... You should practice more!"
        mteacher "In music, you don't have to force notes and pronunciations, you have to sing with soul!"
        p "Okay, I hear you..."
        show bully at left3
        with moveinleft
        "The bully hears the teacher reprimanding you and starts harassing you."
        b "(laughing) You sound like a sheep, ha-ha-ha. And the sister must be the same, only she's a sheep."
        b "Brother's a sheep and sister's a sheep, that's hilarious. Ha-ha-ha-ha."
        "You already wanted to shut him up, but the teacher did it faster."
        mteacher "What kind of language is that? Apologize quickly!"
        b "I will not apologize to this sheep!"
        mteacher "If you don't apologize, I'll tell the class teacher!"
        b "(reluctantly) Okay, okay... Sorry."
        mteacher "There you go!"
        hide bully
        with moveoutright
        "Bully walks out of class."
        p "Thank you!"
        mteacher "You're a big boy, you need to think about fighting back."
        mteacher "If you keep taking all his insults about you and your sister, you'll only make things worse for yourself."
        mteacher "Bullies like him need to be put in their place."
        p "Okay..."
        hide MusicTeacher
        hide mainCharacter
        $ current_location = "hallway13" # Update current location
        $ update_background() 
        with fade
        "You walk out into the hallway and you meet a bully. He comes up to you."
        show bully at center
        b "Hey, can't you stand up for yourself?"
        p "I'm sorry... But..."
        b "Huh? What are you rambling on about? You're lucky you had a teacher around."
        b "If you'd said that to me instead of that hag, you'd be in trouble."
        hide bully 
        with dissolve
        "The bully's leaving."
        $ bully_confronted = True
        $ music_teacher_interaction += 1
        $ remove_task("Go to the music class")
        $ add_task("Talk to your sister in class")
        show screen custom_notify("Talk to your sister in class")
    elif class_teacher_interaction == 0 and sister_interaction == 2 and music_teacher_interaction == 1 and "Talk to the music teacher" in current_tasks:
        show MusicTeacher at right2
        show mainCharacter at left2
        mteacher "I am very disappointed in your progress in my subject. You're doing very poorly"
        p "(puzzled) But I do all my homework! Why am I doing so badly?"
        mteacher "Yeah, you do all your homework and you're more or less good at it."
        mteacher "But you also have to realize that in music, you have to know more than just how to write notes and name instruments."
        mteacher "The ability to sing, to draw out intonation, to shout out the low and high notes of the voice all add to the music."
        p "Why do I need to sing if I'm good with instruments? For example, a drummer doesn't need to be able to sing - he just plays the drum."
        mteacher "You see, you're a bright boy, but in school we have to teach you kids everything."
        mteacher "This is done so that you further understand what you like and what you don't like."
        p "(cheekily) I don't like singing! So I won't sing!"
        mteacher "(surprised) Oh, what impertinence! Not the kind of [player_name] I knew! I'll tell your homeroom teacher!"
        p "(indignantly) Tell me! I'm not singing anyway!"
        mteacher "All right. Whatever you say!"
        $ music_teacher_interaction += 1
        $ remove_task("Talk to the music teacher")
        if "Talk to the art teacher" not in current_tasks:
            show screen custom_notify("Talk to the class teacher")
            $ add_task("Talk to the class teacher")
    elif class_teacher_interaction == 1 and "Talk to the music teacher" in current_tasks:
        show MusicTeacher at right2
        show mainCharacter at left2
        mteacher "Did you want something?"
        # Display dialogue options
        menu:
            "Apologize for my impertinence":
                $ music_teacher_relationship += 1
                "You feel bad that you're about to apologize, but you know it's the right thing to do."
                p "(unsure) I'd like to apologize for my behavior in our last conversation..."
                p "I said too much and didn't realize what I was saying."
                p "I in no way meant to insult you or insult what you do....."
                mteacher "I realize you're young and still have a lot to figure out."
                mteacher "But don't take what you said to me too seriously."
                mteacher "Sometimes you need to talk it out to make you feel better, but it's not always the right thing to do"
                mteacher "And I'm not the right person to talk to about it directly."
                mteacher "The important thing is that you realized all the things you said and you had the courage to apologize"
                mteacher "You did good. Apology accepted. You can go."
                p "There was one more thing I wanted to do..."
            "Ask about the records":
                $ music_teacher_relationship -= 1
                p "I'd like to ask you something."
        
        p "The class teacher told me we have a music test coming up."
        p "Do you know who I can ask for notes so I can study for a test?"
        mteacher "(a little upset) Actually, it would be good if you took notes in class. Then you wouldn't have to ask someone for notes."
        mteacher "I know someone who can help you with your records. He's your classmate and also your old friend."
        mteacher "I thought you already knew that he takes notes in all of his classes and is always willing to help you out"
        mteacher "It doesn't matter. The important thing is that he can obviously help you, since you're friends with him."
        mteacher "So go to him and ask for the records. But don't forget to thank him for his help"
        p "Thank you! I'll go to him now!"
        $ music_teacher_interaction += 1
        $ remove_task("Talk to the music teacher")
        $ add_task("Ask for notes from an old friend")
        $ add_task("Ask for notes from your sister")
        $ add_task("Ask for notes from a nerd")
    elif "Come to the music teacher" in current_tasks:
        $ music_teacher_interaction += 1
        mteacher "So, did you study for the test?"
        p "Yeah, I'm prepared"
        mteacher "All right! Then let's start writing the test paper!"
        jump start_teachers_quiz
    else:
        mteacher "I'm a little busy right now."

    hide MusicTeacher
    hide mainCharacter
    with fade
    jump mainSchoolLoop
