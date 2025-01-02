label nerd_dialogue:
    with fade
    if sister_interaction == 2 and (current_location == "club" and time_of_day == "evening") and sister_coin_started:
        show nerd at right2
        show mainCharacter at left2
        $ nerd_interaction += 1
        p "Hi! You're not busy?"
        n "Hey. Tell me what you want."
        p "How did you know I wanted something from you?"
        n "I, the nerd, only exist to help everyone. After all, no one comes to me just to talk."
        "You got a little embarrassed."
        p "(silent) ......"
        n "Well, tell me what you want."
        p "Do you happen to know where I can find old valuable coins?"
        n "Ooh, you're interested in coins too?"
        p "No, I just messed up and I want to apologize to my sister..."
        n "Ah, that's how it is..."
        n "I can help you with that, but you'll have to play a game with me."
        n "Since we're high schoolers, why don't we play a quiz...? I'll ask a question, say the answer choices, and you pick the correct answer."
        n "How about that?"
        p "Okay, I agree."
        n "Great! Let's start."
        call start_quiz
    elif "Ask for notes from a nerd" in current_tasks:
        show nerd at right2
        show mainCharacter at left2
        $ remove_task("Ask for notes from a nerd")
        n "Hi! Can I help you?"
        p "Hi! Yes, I'd like to ask for your help."
        n "Let me guess, you need help studying?"
        p "Yeah, you're right."
        n "I'm not surprised..."
        p "(silent) ....."
        n "So, what do you need?"
        p "You know we've got big tests coming up in a lot of subjects."
        p "Specifically, in music, drawing, and math"
        p "I'd like to ask you for help with my studies."
        n "Do you need the material explained? Or do you need notes?"
        p "I need your math notes"
        p "I'd like to study for a math test, but I don't have notes"
        p "I mean, I have records, but they're not complete."
        p "Can you help me?"
        "You look at the nerd with hope."
        n "Of course I'll help you. But not for nothing, of course"
        if sister_coin_started:
            if nerdQuizWin:
                n "You did a good job with my questions last time."
                n "Well you remember that little test you took to get a coin for your sister?"
                n "Well, you managed to pass it and I gave you a coin."
                n "I think you've had enough tests."
                n "You did well last time, so you should be able to answer my questions correctly this time too"
                n "And I don't really want to bog you down with questions, because we've got midterms coming up."
                n "Probably the least you want to do right now is take tests."
                n "And I don't want you to think I'm just a nerd who's only interested in learning."
                n "Studying is great, but in addition to studying you should also rest, do sports, socialize with friends"
                n "In short, live life to the fullest"
                "You're a little tired of his speech"
                p "So what's your point?"
            else:
                n "You didn't do a very good job with my questions last time"
                n "Even though they weren't very difficult, I'm a little surprised you didn't do well....."
                n "I'm not surprised you want my tapes."
                n "Apparently you're clearly not ready for a math test."
        p "What am I supposed to do?"
        n "As you know, every week someone from the class cleans the school"
        n "And so this week I'm cleaning up the school"
        n "I guess you'll agree with me, but cleaning is no fun."
        n "Especially alone, cleaning a school is boring, tedious and very time consuming."
        n "So let's do this-- you help me clean up the school, and I'll give you my notes."
        n "How's that sound?"
        "You agree with what the nerd said about cleaning - it's boring, tedious and very time consuming"
        "But you need his notes to study for the test."
        "It's unlikely anyone will have a better record than him"
        "So you realize you have no choice but to help him clean up."
        p "All right, I'll do it."
        n "That's great! Let's get started"
        call rubbish_collector
    else:
        show nerd
        n "I'm a little busy right now."
    
    hide nerd
    hide mainCharacter
    with fade
    $ show_screens()
    return
