
# Item and character definitions with their display conditions
init python:
    def hide_screens():
        renpy.hide_screen("time_buttons")
        renpy.hide_screen("navigation_arrows")
        renpy.hide_screen("inventory_icon")
        renpy.hide_screen("room_characters")
        renpy.hide_screen("tasks_button")
        renpy.hide_screen("relationships_button")

    def show_screens():
        renpy.show_screen("time_buttons")
        renpy.show_screen("navigation_arrows")
        renpy.show_screen("inventory_icon")
        renpy.show_screen("room_characters")
        renpy.show_screen("tasks_button")
        renpy.show_screen("relationships_button")

    # Function to change rooms with a transition effect
    def change_room(new_location):
        global current_location
        current_location = new_location
        update_background(transition=dissolve)

    # Function to update background based on room and time of day
    def update_background(transition=None):
        # Hide all backgrounds before showing the current one
        for location in navigation_positions:
            for time in ["morning", "afternoon", "evening"]:
                renpy.hide(f"{location}_{time}")
        
        # Show the new background with a transition
        if transition:
            renpy.transition(transition)  # Queue the transition correctly
        renpy.show(f"{current_location}_{time_of_day}")

    # Function to advance time of day
    def advance_time():
        global time_of_day
        time_of_day = {"morning": "afternoon", "afternoon": "evening", "evening": "morning"}[time_of_day]
        update_background()

    # Function to start dialogue when interacting with a character
    def start_dialogue(label):
        renpy.call(label)

# Screens for time-of-day management
screen time_buttons():
    hbox:
        xalign 0.85
        yalign 0.03
        if time_of_day == "morning":
            textbutton "Morning" action Function(advance_time) background "#ffff88"
        elif time_of_day == "afternoon":
            textbutton "Afternoon" action Function(advance_time) background "#ffff88"
        elif time_of_day == "evening":
            textbutton "Evening" action Function(advance_time) background "#ffff88"

screen navigation_arrows():
    if current_location in navigation_positions:
        for direction, (target_room, xpos, ypos) in navigation_positions[current_location].items():
            # Check if the target room is visible based on its condition
            if location_conditions.get(target_room, lambda: True)():
                imagebutton:
                    idle im.Scale({
                        "left": "images/navigation_arrows/arrow_left.png",
                        "right": "images/navigation_arrows/arrow_right.png",
                        "up": "images/navigation_arrows/arrow_up.png",
                        "down": "images/navigation_arrows/arrow_down.png",
                    }.get(direction, "images/navigation_arrows/arrow_right.png"), 75, 75)
                    xpos xpos
                    ypos ypos
                    action Function(change_room, target_room)

# Screen for displaying clickable characters in rooms
screen room_characters():
    if (current_location, time_of_day) in characters_in_rooms:
        for char_name, char_image, xpos, ypos, dialogue_label in characters_in_rooms[(current_location, time_of_day)]:
            imagebutton:
                idle im.Scale(char_image, 500, 500)  # Adjust character size as needed
                xpos xpos
                ypos ypos
                action Function(start_dialogue, dialogue_label)

# Main game loop
label schoolMemories:
    $ update_background()
    "You approach the building, a sense of anticipation mixed with trepidation swirling within you."
    "The weathered wooden doors loom before you, hinting at secrets and forgotten moments held within."
    "You walk inside that building."
    "You're excited about what might be inside, your heart pounding with a mixture of hope and fear."
    "What will you find in this place? Answers? Or more questions?"
    "But when you went inside, you saw your school."
    "The place where you spent most of your life."
    "A wave of nostalgia washes over you, followed by a chilling sense of unease."
    "This isn't right. This isn't how it should be."
    show mainCharacter at center
    with dissolve
    p "(puzzled) What? My school?"
    p "How did it even end up inside this building?"
    p "This doesn't make any sense."
    p "It's like... like a dream, but too real, too vivid."
    "You look around, your eyes scanning the familiar hallways, the worn-out lockers, the faded posters on the walls."
    "It's all exactly as you remember it, yet... different."
    "Empty... {w} Hollow..."
    p "Right... The Sage told me that this building was my memories."
    p "He said it would reflect my inner world, my past experiences."
    p "So, this is it? My subconscious laid bare?"
    p "This must be another test from my subconscious."
    p "It wants to test me."
    p "It wants to see if I've learned anything, if I've grown at all."
    p "Most likely it wants to test me - whether I'll make the same mistakes I've already made, whether I've changed or not...."
    p "I'll take that challenge. I have to. There's no other choice."
    "You take a deep breath, steeling your nerves, and walk into school."
    "The familiar scent of old textbooks and floor wax fills your nostrils, triggering a flood of memories."
    "You think back to your younger years - how you had fun with your friends, laughing and joking in the cafeteria..."
    "...how you skipped classes, seeking adventure and freedom..."
    "...how you spent your time at school, both the good and the bad."
    "You remember the thrill of acing a test, the sting of betrayal, the awkwardness of first crushes, the pressure of expectations."
    "It's all here, swirling around you like a ghostly echo."
    "But you notice something's not right."
    "There's not a soul in the school."
    "The silence is deafening, oppressive."
    "You don't see or hear the students playing at recess or the teacher telling the students the latest topic."
    "It's as if everyone vanished, leaving you alone in this deserted monument to your past."
    "A shiver runs down your spine."
    "This isn't just a memory; it's something more."
    "Something...{w} unsettling."
    p "(to myself) Where is everyone? Why is it so quiet? This feels...{w} wrong."
    p "Like a ghost town of my own making."
    "You wander through the empty corridors, your footsteps echoing in the silence."
    "The classrooms are empty, the desks neatly arranged as if waiting for students who will never arrive."
    "The gymnasium is still, the basketball hoops standing like silent sentinels."
    "Suddenly, as you round a corner near the library, you meet a Forest Spirit who was walking down the corridor."
    show mainCharacter at left2
    with moveoutleft
    show forestSpirit at right2
    with dissolve
    p "Hi! How did you get here?"
    p "I thought I was alone in this... memory?"
    "The Forest Spirit smiles, a gentle, knowing expression that puts you slightly at ease, though a sense of wariness still lingers."
    fs "Hi. I was wondering what your \"memories\" would show you and what kind of place you'd go to."
    fs "So I asked the Sage to let me in for a while to see you."
    fs "He granted me permission to observe, to witness your journey through your past."
    p "Why isn't anyone here? Why is the school empty?"
    p "It's creepy, to say the least. Shouldn't there be... people? Students? Teachers?"
    fs "Your memories will show you what you need to see."
    fs "They'll only show you those who were most connected to you and influenced you in some way."
    fs "The others are... echoes,{w} background noise."
    fs "They don't hold the key to your escape."
    p "But why school?"
    p "How will school help me get out of this place?"
    p "What lessons could this empty building possibly hold?"
    "You gesture around the deserted hallway, frustration creeping into your voice."
    "This place feels more like a maze than a memory."
    fs "School is the place where your personality is born."
    fs "It's a crucible where you were forged, shaped by experiences both joyful and painful."
    fs "School besides knowledge gives you both friends and enemies, good memories and bad ones."
    fs "So it also shapes your personality, it greatly influences the formation of your personality, it is an important stage in your life."
    fs "It's where you learned to love, to hate, to trust, to betray."
    fs "All of those lessons are etched into your soul."
    "The Forest Spirit eyes glowing with an ancient wisdom."
    fs "You just have to walk around the school and you'll find the answer to your question."
    fs "This place will tell you how to get out of this place, but it won't help you if you don't deserve it."
    fs "You have to be willing to confront your past, to accept your mistakes, and to learn from them."
    p "Okay... I hear you."
    p "It's not just about finding a way out, it's about finding myself, isn't it?"
    p "About understanding who I was and who I want to be."
    "You nod slowly, the weight of the Forest Spirit's words settling upon you."
    "This isn't just a test; it's a journey of self-discovery."
    fs "(smiling) We're not likely to meet anytime soon, so good luck to you!"
    fs "I trust that you'll get on the right path and not repeat your mistakes."
    fs "The choices you make here will determine your fate. Remember that."
    "The Forest Spirit's form begins to fade, its light dissolving into the shadows."
    hide forestSpirit with dissolve
    "The Forest Spirit disappears and you immediately hear a child's voice coming from the study."
    "It's a small, frightened voice, filled with a pain that resonates deep within your heart."
    p "(to myself) A child's voice? What's going on? Who is that?"
    "A surge of urgency courses through you, pulling you towards the sound."
    "You feel a strange connection to that voice, a sense of responsibility that you can't ignore."
    "You glance back at the empty corridor, then towards the study where the voice came from."
    "The silence of the school presses in on you, but the child's voice is a lifeline, a beacon in the darkness."
    p "(to myself) I have to go. I have to find out who that is and what they need."
    p "Maybe... maybe this is the answer I've been looking for."
    "You steel your resolve and start walking towards the study."
    
    hide mainCharacter
    jump firstMeetingAtSchool
    
label firstMeetingAtSchool:
    $ current_location = "classroom11"
    $ update_background()
    with fade
    show sister_young
    "You see a little girl sitting at a desk in the otherwise empty classroom."
    "Her bright eyes shine with youthful innocence, her hair neatly braided."
    "You recognize her instantly."
    "It's your sister, but... smaller. Younger."
    p "S... Sister? Is that… you?"
    "Your voice catches in your throat, thick with emotion."
    "A wave of warmth washes over you, followed by a sharp pang of guilt."
    "You shake your head, pushing away the painful memories."
    "This isn't the time. You need to focus on the present, on this strange, surreal reunion."
    sister "Hi! What else could I be? Ha ha ha ha."
    "Her laughter rings out, clear and bright, echoing in the otherwise silent classroom."
    "It's a sound that tugs at your heartstrings."
    "A melody of carefree joy that you haven't heard in what feels like a lifetime."
    sister "Why are you so late to class? You're almost late for class!"
    sister "Class teacher is going to be so mad!"
    sister "He said he was going to give a pop quiz today!"
    "She looks up at you, her brow furrowed in mock concern."
    "Her eyes sparkle with mischief, and you can't help but smile."
    "It's so like her to worry about the small things, even in this strange, empty version of reality."

    # So if we've left her before, it'll be this
    if relationship_sister == -1:
        p "I'm sorry I left you in the forest...."
        p "I didn't have the courage to help you and save you..."
        p "I was so scared, so selfish..."
        "Your voice cracks, the words heavy with regret."
        "The image of your sister, lost and alone in the dark woods, flashes through your mind."
        "The guilt gnaws at you, a constant reminder of your failure."
        sister "(puzzled) Forest? Abandoned? What are you talking about?"
        sister "Are you feeling okay? You're acting kind of weird."
        "She tilts her head, her eyes filled with genuine concern."
        "She doesn't understand."
        "This version of her is just a memory, a fragment of your past, untouched by the events that have shaped you."
        p "But you're… I saw you… in the forest…" 
        p "you were scared...{w} and I...{w} I left you there..."
        sister "(interrupting) You're reading your comic books again and making up stuff."
        sister "You always get so carried away with those stories!"
        sister "Pull yourself together! There's a lesson coming up."
        sister "And you know how much I hate it when you miss class."
        "She gives you a playful nudge, her smile returning."
        "She dismisses your words as fantasy, as the ramblings of a daydreamer."
        "It stings, but you understand."
        "This isn't the real her, not the one who suffered because of your choices."
        "You think to yourself that this sister has nothing to do with the one you met in the forest."
        "This is the sister you remember, the one before everything went wrong."
        "The one you failed to protect."
        "You remember that it was just the guise of Kindness, but it's still hard to see your sister around after what you've done."
        "The guilt is a heavy weight, pressing down on you, suffocating you with its intensity."
        p "(to myself) She doesn't remember. She doesn't know the pain I caused her."
        p "Maybe... maybe that's for the best. I don't want her to carry that burden."
    else:
        "You think to yourself that this sister has nothing to do with the one you met in the forest."
        "This is a pure, unadulterated memory, a glimpse into a happier time."
        "You remember that the figure in the forest was just the appearance of Kindness, but you're still happy to see her"
        "Even if it's just a phantom of your past."
        "It fills you with a bittersweet longing, a yearning for a time when things were simpler, when your heart wasn't so heavy with regret."
        p "(to myself) In the woods there were only guises of my emotions, but here they are real - this one is not a guise at all, but a memory."
        p "A precious fragment of a life I almost lost."
        "You take a step closer to her, wanting to reach out, to touch her, to reassure yourself that she's okay, but you hesitate."
        "This isn't the real her."
        "This is just a memory, a phantom of the past."
        "Touching her would be like trying to grasp smoke."

    hide sister_young
    with dissolve
    p "(to myself) I need to find a way out of here."
    p "(to myself) I need to find a way back to… reality."
    p "(to myself) But what if this is my reality now? What if I'm trapped here forever, in this empty shell of my past?"
    "The thought sends a shiver down your spine."
    "You have to escape."
    "You have to find a way to move forward, to leave this place behind. But how?"
    jump hallway11Sister

label hallway11Sister:
    $ current_location = "hallway11"
    $ time_of_day = "afternoon"
    $ update_background()
    with fade
    show sister_young at center
    with dissolve
    "Class is over. In the hallway."
    sister "Now we will have lessons in different rooms, we are in different groups."
    sister "I will have a music lesson and you will have a drawing lesson."
    sister "I hope you haven't forgotten that the art lesson is in room 1-2."
    p "Thanks for reminding me, or I forgot."
    sister "Okay, then I'll meet you sometime later. You can always find me in our class!"
    hide sister_young 
    with dissolve
    $ add_task("Go to an art class")
    show screen custom_notify("Go to an art class") 
    "Your sister leaves for music class, leaving you alone in the hallway."
    jump mainSchoolLoop

label mainSchoolLoop:
    window hide
    $ update_background()
    $ show_screens()
    while True:
        if check_inventory_for_items(required_ingredients) == True:
            $ hide_screens()
            jump endSchoolMemories
        pause

label endSchoolMemories:
    scene cauldron
    with fade
    "You've collected all the necessary ingredients for the potion."
    "Now you need to brew it and decide whether to drink it or not."
    "You mixed all the necessary ingredients and got the very potion that will get you out of here"
    "In your hands you hold the potion you've come all this way for."
    "You pondered over the words of this place and the sage about this potion 'getting rid of all problems'."
    $ overall_relationships += sister_relationship + music_teacher_relationship + old_friend_relationship
    if overall_relationships <= 0:
        "You decided to drink the potion and get rid of all the problems."
        "You drank the potion and felt a surge of energy and lightness."
        "But that rush of strength and lightness was abruptly replaced by emptiness."
        "You felt like you were losing yourself - your memories, your emotions."
        scene black
        with dissolve
        "You wake up in the hospital."
        "You don't remember how you got here or what happened."
        "The doctors say you've been in a coma for a long time."
        "You see your loved ones who are excited about your awakening."
        "But you feel nothing... You don't feel joy or admiration. Nothing."
        "Soon, doctors give you a prognosis that you won't be able to express and feel emotions."
        "You will feel empty inside for the rest of your life."
        show screen custom_notify("You have reached a good ending.")
    else:
        "You decided not to drink the potion."
        "You realize that all the difficulties, worries and failures are part of the journey and you can't move on without it all."
        "You break the potion."
        scene black
        with dissolve
        "You wake up in the hospital."
        "You don't remember how you got here or what happened."
        "The doctors say you've been in a coma for a long time."
        "You see your loved ones who are excited about your awakening."
        "You're very happy to see them too."
        "You remember everything that happened while you were in the coma."
        "You are glad that you got out of this place, but at the same time you are a little sad.... You sometimes think about what happened to you."
        "Soon you recovered and were discharged from the hospital. You live your life to the fullest, despite all the obstacles and worries."
        show screen custom_notify("You have reached the best ending.")
    "The end."
    return