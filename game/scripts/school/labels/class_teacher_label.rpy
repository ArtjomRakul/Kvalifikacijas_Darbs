
label class_teacher_dialogue:
    $ hide_screens()
    with fade
    if "Talk to the class teacher" in current_tasks:
        $ remove_task("Talk to the class teacher")
        show ClassTeacher at right2
        hide mainCharacter
        show mainCharacter at left2
        cteacher "Hello, [player_name]"
        p "(quietly) Good [time_of_day], teacher"
        "You realize what this conversation is about. You're getting a little tense."
        cteacher "I heard some rumors about your progress in school....."
        cteacher "And I'm not very happy after hearing that."
        "You've become uncomfortable"
        p "(quietly) I'm sorry..."
        cteacher "It's not me you need to apologize to, it's your teachers for being rude to them."
        cteacher "And also to myself for failing to meet my goals."
        p "(uncertainly) Yes. I understand..."
        cteacher "Apparently you don't understand it well enough to allow it."
        cteacher "Or, on the contrary, you understand everything, but you don't want to accept it and move on with your life"
        p "....."
        cteacher "Let me help you with that a little bit."
        cteacher "I want to remind you that you have tests coming up in subjects where you're a little behind - music, drawing, and math."
        cteacher "I want to tell you right away that these tests are not easy, so just reading the notes will not be enough."
        cteacher "And cheating's not an option, since you're sitting in the front row."
        "You smirked"
        cteacher "Did I say something funny?"
        "You came to your senses quickly and the smirk disappeared from your face"
        p "No, I'm sorry."
        cteacher "You can cheat, but what's the use? You just write off what's in your sporkel and you forget all about it when you leave the office."
        cteacher "But schools are there so that you learn new things and memorize them, not just write them off and forget about them"
        cteacher "In turn, this could all come in handy in the future, because you probably don't know where you're going to end up"
        "You got bored with his tedious yet obvious words."
        p "Yes, I get it, all right!"
        cteacher "Okay, I was talking about something else. What am I talking about?"
        cteacher "Oh yeah, you've got midterms coming up and you're going to need to study for them. As I said before, notes are of little help here"
        p "(surprised) Why aren't the notes helpful? Are we going to have assignments we haven't done yet?"
        cteacher "No. Just knowing you, I know you don't have much of a record in these subjects"
        "You remember that you didn't take much notes in your last few classes. Instead of taking notes, you just sat there and listened"
        p "But I've been listening to your lessons and the topics we've been going over"
        cteacher "I don't think you have a very good memory to remember all the subtleties of recent topics"
        cteacher "You may have listened to my stories, but I think you only memorized everything superficially, without memorizing or paying attention to the details and subtleties of the topic"
        "Even though you get tedious with his words, you're shocked at how he reads you like an open book"
        cteacher "I'm going to help you with this a little bit. Ask your friends or classmates for help. Ask them for their notes. Read them"
        p "But who do I ask them from?"
        cteacher "Hmm. Let me see..."
        cteacher "I know your sister has a good drawing grade, so you can ask her for help with drawing"
        cteacher "What about my subject, math, you can ask the nerd for help, he has all tens and writes everything down."
        cteacher "If you get your hands on his notebook, you're in luck!"
        p "What about the music?"
        cteacher "I can't help you with music. You can ask the teacher herself about it"
        "You think back to your last conversation with your music teacher and you feel uncomfortable"
        "You think she's unlikely to want to help you after your last and not so pleasant conversation"
        p "I think she's unlikely to tell me directly who can help me with that...."
        cteacher "I think she's gonna help you anyway."
        p "(surprised) Yes? But why?"
        cteacher "No matter how strict or angry she is, she always remains a kind and sweet person at heart"
        cteacher "Especially as a teacher, she is responsible for you. It's in her best interest to help you learn"
        p "Okay, thank you!"
        cteacher "Oh yeah, if you pass the tests, I have a little surprise for you."
        p "(surprised) Yeah? What's the surprise?"
        cteacher "When you do the tests, then you'll know."
        "You were intrigued by what he said. You thought he might be the one to get you out of this place."
        "You're a bit of an afterthought..."
        cteacher "Well, what's on your mind? You don't have much time left to study for the tests."
        p "Yeah, all right!"
        $ class_teacher_interaction += 1
        show screen custom_notify("Talk to the music teacher")
        $ add_task("Talk to the music teacher")
    elif "Come to the classroom teacher" in current_task and class_teacher_interaction == 1:
        $ class_teacher_interaction += 1
        cteacher "So, did you study for the test?"
        p "Yeah, I'm prepared"
        cteacher "All right! Then let's start writing the test paper!"
        jump start_teachers_quiz
    else:
        cteacher "I'm a little busy right now."
    
    hide ClassTeacher
    hide mainCharacter
    with fade
    jump mainSchoolLoop
        