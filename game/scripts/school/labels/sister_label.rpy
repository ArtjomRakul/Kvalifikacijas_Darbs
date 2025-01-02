label sister_dialogue:
    with fade
    if sister_interaction == 0 and art_teacher_interaction == 1:
        if time_of_day != "morning":
            show sister_young
            sister "I'm a little busy right now."
            hide sister_young
            hide mainCharacter
            $ show_screens()
            return
        show sister_young at right2
        hide mainCharacter
        show mainCharacter at left2
        p "Hi! How was music class?"
        sister "(sadly) Ehhh, the music teacher is always very demanding and strict. You know her."
        "You remember how as a child you disliked her because she was strict and demanding. You decide to cheer her up."
        p "Yes, although she is a very good teacher, she is sometimes very strict. I don't like that character trait in her either."
        sister "Uh-huh..."
        p "Don't be so upset! You'll have a drawing class later and you'll feel better right away. I know how much you like to draw."
        sister "(cheerfully) Yes, I love drawing!"
        p "By the way, did your art teacher tell you anything about potions?"
        sister "(puzzled) Potion? What potion?"
        p "We had to draw some weird potion in class and if you drink it, legends say a person can understand and realize themselves."
        sister "(thought) Hmm. It didn't happen."
        sister "Maybe you're making up stuff for yourself again."
        p "No, it really was like that!"
        sister "Well, even so, you're too young to understand and realize yourself hee-hee-hee."
        p "Can you ask her about the potion in class, please?"
        sister "If you weren't my brother, I wouldn't be doing this kind of thing. Okay, I'll figure something out."
        p "Thank you so much!"
        $ remove_task("Talk to your sister in class")
        $ add_task("Go to the music class")
        show screen custom_notify("Go to the music class")  # CN09
        $ sister_interaction += 1
    elif sister_interaction == 1 and music_teacher_interaction == 1 and time_of_day == "morning":
        show sister_young at right2
        hide mainCharacter
        show mainCharacter at left2
        sister "Hey. Did you want something?"
        p "Did you find out about the potion?"
        sister "Yes... I did..."
        p "And what did you find out?"
        sister "I found out you're a moron! There was no potion!"
        p "But the teacher..."
        sister "She didn't say anything. You just made a fool of me in front of the whole class! Go away!"
        hide sister_young 
        with dissolve
        show mainCharacter at center
        with dissolve
        menu:
            "Try to make amends":
                $ sister_coin_started = True
                "You care a lot about your sister, so you want to make it up to her somehow."
                "You remember that she's really into all sorts of historical coins."
                "You remember that the only one in the class who might know anything about it is a nerd."
                "You recall that he often sat in the club room in the evenings after all his lessons and studied"
                $ remove_task("Talk to your sister in class")
                $ add_task("Go to the club room and meet a nerd")
                show screen custom_notify("Go to the club room and meet a nerd")    # CN10
            "Leave":
                $ sister_coin_started = False
                $ sister_relationship -= 1
                "You decide to leave your sister alone for now."
                $ remove_task("Talk to your sister in class")
                if "Talk to the art teacher" not in current_tasks:
                    $ add_task("Talk to the art teacher")
                if "Talk to the music teacher" not in current_tasks:
                    $ add_task("Talk to the music teacher")

                show screen custom_notify("Talk to the teachers")   # CN11
        
        $ sister_interaction += 1
        hide sister_young
        hide mainCharacter
        with fade
        $ show_screens()
        return
        
    elif nerd_interaction == 1 and sister_coin_started and "Ask for notes from your sister" not in current_tasks and "BookGreen" not in [item[0] for item in inventory_items if item]:
        if "CoinBronze" in [item[0] for item in inventory_items if item]:
            $ remove_from_inventory("CoinBronze")
            $ sister_relationship -= 1
            sister "Oh... Is this what you got? You could have done better."
        elif "CoinSilver" in [item[0] for item in inventory_items if item]:
            $ remove_from_inventory("CoinSilver")
            $ sister_relationship += 1
            sister "Wow, you did it! I'm so proud of you!"
            sister "This really means a lot to me."
        
        hide sister_young
        $ remove_task("Bring the coin to your sister")
        if "Talk to the art teacher" not in current_tasks:
            $ add_task("Talk to the art teacher")
        if "Talk to the music teacher" not in current_tasks:
            $ add_task("Talk to the music teacher")

        show screen custom_notify("Talk to the teachers")   # CN11
        $ show_screens()
        return
    elif "Ask for notes from your sister" in current_tasks and sister_interaction == 2 and "BookGreen" not in [item[0] for item in inventory_items if item]:
        call sister_notes
    elif "Bring the notes to your sister" in current_tasks and sister_interaction == 3 and "BookGreen" in [item[0] for item in inventory_items if item]:
        show sister_young at right2
        show mainCharacter at left2
        $ sister_interaction += 1
        p "Hey! I brought you the tapes."
        p "I took them from the bully."
        "My sister was glad you helped her."
        sister "(smiling) Thank you so much!"
        "But she immediately began to worry that the bully might have done something to you."
        sister "(concerned) Bully didn't do anything to you? How did you get the tapes away from her?"
        p "(calmly) Don't worry, it's okay. I just played rock-paper-scissors with him and beat him with your notebook."
        sister "Phew, I'm glad you're doing okay."
        sister "Cause I was starting to worry."
        sister "Thank you again for returning the notebook. You can keep it, you deserve it."
        "You took your sister's notebook."
        "Now you can prepare for all the test papers"
        $ remove_task("Bring the notes to your sister")
        if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
            $ add_task("Come to the classroom teacher")
    else:
        show sister_young at center
        sister "I'm a little busy right now."
    
    hide sister_young
    hide mainCharacter
    with fade
    $ show_screens()
    return

label sister_notes:
    $ sister_interaction += 1
    with fade
    show sister_young at right3
    show bully at right2
    "You want to approach your sister, but you see a bully picking on her."
    "You can hear them talking from afar."
    "You can tell right away that this is not going to be a pleasant conversation. A bully is not usually a pleasant conversation."
    sister "Go away! I don't want to talk to you!"
    b "Come on, don't be like that! I just want to talk to you."
    sister "I said go away!"
    b "What if I don't want to go away?"
    b "What are you gonna do then? Call your little brother?"
    sister "....."
    b "Come on, call your brother!"
    b "Call out to him in your sheepish voice."
    b "Just watch your voice."
    "You see the sister trying to say something, but she can't make it."
    if sister_coin_started:
        if nerdQuizWin == False:
            menu:
                "Help your sister":
                    $ sister_relationship += 1
                    call helpYourSister
                "Leave":
                    $ sister_relationship -= 1
                    call leaveYourSister
        else:
            call helpYourSister
    else:
        call leaveYourSister
    
    return

label helpYourSister:
    play music darkmusic
    "You can't stand it when someone is rude to your sister."
    "You decide to intervene."
    show mainCharacter at left2
    p "Hey, you! What's going on here?"
    p "Can't you see she doesn't want to talk to you?"
    p "Leave her alone!"
    sister "Brother..."
    b "Oh, look who's here! The little brother!"
    b "What are you going to do? Hit me?"
    "I'm not afraid of you!"
    b "You're just a little kid!"
    b "Or are you going to call the teacher in that nasty little voice of yours?"
    p "(uncertainly) No, will you deal with me?"
    "You see the bully start to approach you."
    show bully at right1
    with moveoutleft
    "You feel your heart start to beat faster."
    "Your hands start to sweat and shake."
    "You can't stop that shaking as the bully is stronger than you."
    "You don't know what to do."
    "But one thing's for sure, you won't let your sister suffer."
    play music seriousmusic
    if helpSister == False:
        "You remember that you've already dumped her once and you don't want to do it again."
        "You don't want her to be alone."
        "You don't want her to suffer again."
        "You don't want her to go through that horror again."
        "You still feel guilty about what you did and you want to fix it."
    else:
        "You remember that you saved her once before and you want to do it again."
        "You think back to that Shadow in the woods and you realize that this bully is not as scary as that Shadow."
        "Your confidence returns to you and you're ready to protect your sister."
    p "I told you to leave her alone!"
    "You're scared, but you take a step toward him."
    show mainCharacter at left1
    with moveoutright
    if helpSister == False:
        "The bully paused for a moment."
        show bully at center
        with moveoutleft
        "But soon he moves on to you as he sees the fear and insecurity in your eyes."
        b "I won't let go! What are you gonna do to me?"
        "He's persistent"
        "You can see him smiling"
        "He's probably excited about his victory and what he'll do to you."
        "You see the image of that Shadow you met in the woods."
        "He's just as scary and big and strong"
        "Your heart beats faster"
        "Your breathing has quickened"
        "You're starting to tremble"
        "You're starting to panic"
        if goForAWalk == True:
            call helpFromOldFriend
        else:
            call failureToProtectSister
    else:
        "The bully stopped."
        "You can see in his face as he begins to realize you're serious."
        "You can tell by the look on his face that he clearly didn't expect this from you and he's surprised."
        "You can see him starting to pull back."
        show bully at right2
        with moveoutright
        p "(confidently) Where are you going?"
        p "You wanted to talk to me, didn't you?"
        "You abruptly realize that you said it for nothing."
        "You pissed him off with those words and he came to his senses."
        "You see him back start to approach you."
        show bully at right1
        with moveoutleft
        b "(roughly) Aren't you a little cocky for such a brat?"
        sister "Stop it! Stop it!"
        "The situation is escalating"
        if goForAWalk == True:
            call helpFromOldFriend
        else:
            call failureToProtectSister
    
    return

label leaveYourSister:
    play music sadmusic
    "You decide not to get involved in the situation."
    "You look from the side at them and you remember that you've seen this picture somewhere before."
    "You remember that situation in the woods on the way to the tavern."
    "When you went to the tavern, a huge Shadow was harassing your sister."
    "More specifically, the image of your sister"
    "You look at the bully and see the image of that Shadow you met in the woods"
    "He's just as scary and big and strong"
    p "(to myself) What am I doing? I can't just stand by and watch him hit on my sister."
    p "(to myself) I have to do something!"
    p "(to himself) But what?"
    p "(to myself) What can I do?"
    p "My body won't listen to me"
    "The more you watch a bully pick on your sister, the more you start to panic"
    "You're starting to tremble"
    "You're starting to panic"
    "You decide to reassure yourself"
    p "(to myself) Easy, [player_name], easy."
    p "(to myself) Don't panic."
    p "(to myself) It's gonna be okay."
    p "(to myself) In the woods it was just the shape of a sister, but now it's a real sister."
    p "(to herself) My sister is a very strong and smart girl."
    p "(to myself) I'm sure she'll be fine."
    "You feel like you're lying to yourself."
    "You feel like you don't believe yourself."
    "You're really scared"
    "You're scared not only because of what the bully might do to your sister, but also because of what he might do to you"
    "Deep down you know it, but you don't want to accept it."
    "You see the very notes you wanted to ask your sister for on the edge of the table."
    "You'd like to ask your sister for those tapes, but you can't do that."
    "If you ask your sister for those notes, the bully will pay attention to you"
    "And you really don't want that"
    "So you quietly and quickly pick up the records"
    "You're ashamed of the act, but you do it nonetheless"
    p "(to myself) I'm sorry, sister."
    "You pull out the notes, flip to a random page, and ostensibly start reading"
    "You pretend it's none of your business and you don't see what's going on."
    "Out of the corner of your eye, you notice your sister looking at you with desperation"
    "You walk by, but the bully notices."
    b "Oh, look who's here! The little brother"
    b "Only apparently he won't want to help you."
    b "Because he's weak! Ha ha ha!"
    b "Can't even protect his sister, hahaha!"
    b "All right, I don't care about [player_name]."
    b "So, \"sister\", where were we?"
    "You've gone far enough away that you can't hear what they're talking about."
    "But by the look of her sister, she's clearly not thrilled about this conversation with the bully"
    "She obviously doesn't like it"
    "You're the reason you're not at peace"
    "You realize that you abandoned her"
    if helpSister == False:
        "You realize you left her again....."
        "Threw her alone with those monsters...."
        "Then there was The Shadow, and now there's a bully"
        "You're feeling very uneasy about this"
    "But there's nothing you can do, because the choice has already been made."
    "You realize that you're unlikely to help her anymore, so you decide to just walk away, leaving your sister alone with the bully."
    if current_location == "classroom11":
        $ current_location = "hallway11"
    elif current_location == "classroom12":
        $ current_location = "hallway12"
    elif current_location == "classroom13":
        $ current_location = "hallway13"
    
    $ update_background()

    $ remove_task("Ask for notes from your sister")
    if "BookGreen" not in [item[0] for item in inventory_items if item]:
        $ add_to_inventory(*notes_items["BookGreen"])
    if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
        $ add_task("Come to the classroom teacher")
    hide mainCharacter
    hide sister_young
    hide bully
    return
                
label failureToProtectSister:
    with fade
    hide bully
    hide mainCharacter
    hide sister_young
    scene black
    "It darkened abruptly"
    "You don't understand what happened"
    p "(to myself) Did the lights go out in the classroom?"
    p "(to myself) What's going on?"
    "You feel everything - the smell of the classroom, the cold wind from behind the open window, the noise of the children."
    "But for some reason you can't move."
    p "(to myself) What the hell is going on here?"
    $ update_background()
    show sister_young at center
    play music sadmusic
    sister "Brother! Brother!"
    "You're getting a headache"
    p "Don't shout like that! My head hurts!"
    "Now you can see it all again, but the bully's gone."
    "And you notice that you're lying down"
    show sister_young at right2
    with moveoutright
    show mainCharacter at left2
    with moveinbottom
    p "What happened? Where did the bully go?"
    sister "Poor brother..."
    sister "You don't remember anything?"
    "You try to remember recent events, but the last thing you remember is being approached by a bully"
    p "No, I don't remember"
    sister "Poor brother. He hit you so hard."
    p "Did he hit me?"
    sister "Yeah, he hit you!"
    sister "How insensitive he is!"
    sister "You shouldn't have stood up for me!"
    p "How could I? You're my sister."
    p "I couldn't just walk by"
    "Your sister was a little embarrassed"
    sister "(quietly) Dummy..."
    p "I just remembered that Shadow in the woods that was harassing you."
    p "I didn't want you to go through that again."
    p "I didn't want to make you suffer and agonize again."
    "Your sister looks at you with misunderstanding."
    sister "A shadow? In the woods?"
    sister "What are you talking about?"
    sister "He must have hit you pretty hard if you're talking nonsense."
    "You realize it was inappropriate and you chose to keep quiet."
    sister "You need to get as much rest as you can right now! I'll tell the teacher all about what he did to you!"
    p "Yeah, well..."
    p "(uncertainly) But I don't think we should tell the teacher everything."
    sister "Why?"
    p "I think if you tell the teacher, he'll bully you harder"
    p "And over me."
    p "That I couldn't protect my sister..."
    sister "What are you doing?!"
    sister "You think if I tell the teacher, he'll keep hitting on me?"
    sister "(confidently) Ha ha ha, no!"
    sister "I think even he realizes that if he hits on me or you again, he's going to be in trouble"
    sister "From the teacher, I mean."
    sister "Now go get some rest!"
    p "Yeah, well..."
    sister "Oh, yeah, I almost forgot"
    sister "You were looking for me to find the records, right?"
    p "Yeah, that's right."
    sister "Here, take this"
    "The sister wants to hand over the tapes, but she sees that they're missing"
    sister "You didn't happen to pick up my records yet, did you?"
    p "No, I didn't"
    sister "Weird..."
    "You see the sister start looking for the records"
    sister "Weird... Where are they?"
    "You see the way she's thinking"
    "That's when you see the look of surprise and anger on her face"
    sister "Did he steal my tapes?!"
    p "Who?"
    sister "Bully!"
    sister "Apparently when I ran to you, he saw my notes and stole them!"
    sister "He's so disgusting!"
    sister "I'll show him!"
    "The sister was about to go looking for the bully, but you stopped her."
    p "Hold on. I'll talk to him."
    sister "No! Do you want him to hit you again?"
    p "No, he's not gonna hit me."
    p "You're about to tell the teacher what happened"
    p "The teacher will immediately go to deal with him"
    p "After talking to the teacher, the bully will no longer harass you, much less touch me"
    sister "Are you sure about this?"
    p "Yeah, I'm sure"
    sister "Okay..."
    sister "But be careful"
    p "Yes, thank you."
    $ remove_task("Ask for notes from your sister")
    $ add_task("Take your sister's notes away from the bully")
    hide mainCharacter
    hide sister_young
    return
                        
label helpFromOldFriend:
    play music emotionalmusic
    "Suddenly your old friend comes to your rescue."
    show old_friend at center
    with moveinright
    p "You..."
    of "Stop hitting on everyone!"
    "Bully realizes he's not in an advantageous position and decides to back off"
    b "Shit. What a bunch of you against one"
    b "Maybe I should back off"
    b "You're lucky this time"
    b "You better hope that the next time we meet, there's no one around to see you."
    b "That goes for everyone"
    b "Especially to you, [player_name]..."
    hide bully
    with moveoutright
    "As soon as the bully left, you sighed really hard"
    p "(to myself) Thank God he's gone."
    p "(to myself) I don't know what I would have done if he'd gone on."
    "You've calmed down a bit, but your heart is still beating fast"
    "Hands are still shaking"
    "An old friend turns to you and smiles"
    of "Are you all right?"
    p "Yes, thank you so much! I owe you one!"
    p "I dread to imagine what would have happened if you hadn't shown up"
    of "You're welcome! I'm always happy to help!"
    sister "Thank you so much!"
    "The sister looks at you worriedly"
    sister "How are you? Are you okay?"
    p "Yeah, I'm fine!"
    p "How are you doing? Did he do something to you?"
    sister "No, he was just hitting on me"
    if sister_coin_started:
        if nerdQuizWin == True:
            sister "He wanted to take that coin you gave me."
            "After hearing those words, you got angry"
            "You have strength and self-confidence"
            "The strength and confidence to talk to a bully"
            p "He's an asshole!"
            sister "Easy, easy! It's okay!"
            sister "He didn't take it, so it's okay."
            "You calmed down right after that"
            p "(relieved) Whew, that's good."
            p "Cause I've been meaning to deal with him"
            sister "Handle it? With him?"
            sister "After all this?"
            sister "Are you out of your mind? You don't want to do that"
            p "Yeah, you're right."
        else:
            sister "He wanted to take something from me."
            p "Which is what?"
            sister "Well... It doesn't matter"
            p "No, it's very important!"
            p "What if he comes back to take that thing away from you again!"
            sister "Well... I don't think he's coming back"
            sister "Besides, it doesn't really matter what he wanted to take from me."
            p "I see..."
    sister "So you need to get some rest after all this"
    sister "Because you've been so nervous since the incident."
    sister "Go get some rest."
    p "Yeah, well..."
    sister "Oh, yeah, I almost forgot"
    sister "You were looking for me to find the records, right?"
    p "Yeah, that's right."
    sister "Here, take this"
    "My sister sends you her notes"
    p "Thank you so much!"

    $ remove_task("Ask for notes from your sister")
    if "BookGreen" not in [item[0] for item in inventory_items if item]:
        $ add_to_inventory(*notes_items["BookGreen"])
    if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
        $ add_task("Come to the classroom teacher")
    hide old_friend
    hide sister_young
    hide mainCharacter
    return