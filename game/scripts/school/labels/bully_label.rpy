label bully_dialogue:
    $ hide_screens()
    with fade
    if "Take your sister's notes away from the bully" in current_tasks:
        $ bully_interaction += 1
        show bully at right2
        hide mainCharacter
        show mainCharacter at left2
        b "What do you want?"
        "You're a little scared to hang out with him after that incident."
        "You were always shaking with fear last time, but now you're somehow confident that he won't hurt you"
        "But you still feel fear and you're concerned"
        "Your heart is beating hard, but your hands aren't shaking this time."
        "This time it's like you have a lump in your throat and you can't find the words to answer him."
        b "Come on, tell me what you want!"
        "The bully is pissed off by your silence."
        "After he said that, you immediately started talking"
        P "(quietly and uncertainly) Give me my sister's records!"
        b "What? Speak louder!"
        p "(uncertainly) Give me my sister's records! Please!"
        p "(uncertainly) You took my sister's notes without her permission when you left class."
        b "What records? I didn't take anything!"
        p "(confidently) Don't lie! Or I'll tell the teachers!"
        "The bully's facial expression changed"
        "He now looks at you with disgust after mentioning teachers"
        b "(grunts) You're all at it again."
        b "(grunts) All you know how to do is complain to your teachers."
        b "I'm not giving them away, I have a test to study for."
        p "My sister will need to study for a test too, so give the notes!"
        p "You can ask for notes from other students"
        b "No. You know very well I don't have any friends in my class."
        b "I don't have anyone to ask for records"
        b "Especially since, as I noticed, your sister was the only one who did so many records on music"
        p "Since you won't give up the records voluntarily, then what do you want in return for giving up the records?"
        b "Hmm... I'll have to think about it..."
        "The bully hesitated for a moment"
        "You realize you have a chance to take the tapes away from him."
        "But you can't imagine what he'd want in return."
        "Did it make you sick"
        "You start going over in your head what he'll want in return."
        "These thoughts frighten and terrify you."
        "You're getting scarier and scarier by the second"
        "With each passing second, more and more horrible and twisted thoughts pop into your head."
        "You're getting more and more nervous by the second."
        "Goosebumps run down your back and you start to sweat."
        p "(nervously and to himself) Well, what's taking him so long?"
        p "(nervously and to myself) I'm afraid to imagine what he could offer me."
        "Suddenly you see the smirk on the bully's face"
        "He's about to tell you what he wants"
        "You freeze and wait for his words"
        b "I know what you can offer me"
        p "(nervously) What?"
        b "Let's play rock-paper-scissors."
        "You're a little surprised by his offer"
        "You didn't expect an offer like that"
        p "(surprised) In rock-paper-scissors?"
        b "Yes."
        "You are at one and the same time surprised and delighted at his suggestion"
        "You expected the worst from him"
        "You didn't even think that someone like him could suggest a regular game of rock-paper-scissors-paper-scissors"
        "Are you glad that's what he suggested"
        "You've finally calmed down"
        b "If you win, I'll give you the records."
        p "And if I lose?"
        b "If you lose, I'll keep the tapes."
        p "All right, I'll do it."
        p "(to myself) Even though it's weird, I'm glad he suggested it."
        p "(to myself) But now I have to pull myself together and beat him."
        p "(to myself) I can't lose"
        p "(to myself) I have to win and take the tapes away from him!"
        hide bully
        hide mainCharacter
        jump rock_paper_scissors_game
    else:
        show bully at center
        b "What do you want, buddy?"

    hide bully
    hide mainCharacter
    with fade
    jump mainSchoolLoop
