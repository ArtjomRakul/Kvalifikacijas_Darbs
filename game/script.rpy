# Define the characters of the game. 
define p = Character('[player_name]', color="#3131d7") 
define fs = Character('Forest Spirit', color="#c8c8c8") 
define wiseMan = Character('Sage', color="#c5bc3a") 
define shadow = Character('Shadow', color="#352c2c") 
define sister = Character('Sister', color='#f18a8a') 
define stranger = Character('Stranger', color="#2bd12e") 
define w = Character('Witch', color="#9b0a98")
define of = Character('Old friend', color="#8ae3f1")
define b = Character('Bully', color="#e3830f")
define n = Character('Nerd', color="#0f8ae3")
define ateacher = Character('Art teacher', color="#f1f18a")
define mteacher = Character('Music teacher', color="#ef8af1")
define cteacher = Character('Class teacher', color="#408a75")

# Define character images 
image mainCharacter = im.Scale("characters/mainCharacter.png", 750, 750) 
image forestSpirit = im.Scale("characters/forestSpirit.png", 750, 750) 
image stranger_img = im.Scale("characters/stranger.png", 750, 750) 
image wiseMan = im.Scale("characters/wiseMan.png", 750, 750) 
image sister_img = im.Scale("characters/sister.png", 750, 750) 
image witch = im.Scale("characters/witch.png", 750, 750) 

# Defining shadow images 
image shadow_man = im.Scale("characters/shadows/shadow_man.png", 750, 750) 
image shadow_woman = im.Scale("characters/shadows/shadow_woman.png", 750, 750) 
image shadow_bandit = im.Scale("characters/shadows/shadow_bandit.png", 900, 900) 

# Define background images 
image field_bg = im.Scale("backgrounds/forest/Fields 2.png", 1920, 1080) 
image path1_bg = im.Scale("backgrounds/forest/Path 1.png", 1920, 1080) 
image path2_bg = im.Scale("backgrounds/forest/Path 2.png", 1920, 1080) 
image bigTree_bg = im.Scale("backgrounds/forest/BigTree.png", 1920, 1080) 
image crossroad_bg = im.Scale("backgrounds/forest/Crossroad.png", 1920, 1080) 
image unknownHouse_bg = im.Scale("backgrounds/forest/unknownHouse.png", 1920, 1080)
image houseEntry_bg = im.Scale("backgrounds/cottage_MiniGame/cottage_backgrounds/CottageHearth.png", 1920, 1080)
image darkForest_bg = im.Scale("backgrounds/forest/Dark 1.png", 1920, 1080) 
image deadTree_bg = im.Scale("backgrounds/forest/Dark 6.png", 1920, 1080) 
image birch_bg = im.Scale("backgrounds/forest/Birch 1.png", 1920, 1080) 
image tavern_bg = im.Scale("backgrounds/forest/VillageTavern.png", 1920, 1080) 
image witchSwamp_bg = im.Scale("backgrounds/forest/Cabin 1.png", 1920, 1080) 
image witchHouse_bg = im.Scale("backgrounds/forest/Cabin 6.png", 1920, 1080) 
image village_bg = im.Scale("backgrounds/forest/Village.png", 1920, 1080) 
image strangerSwamp_bg = im.Scale("backgrounds/forest/Cabin 4.png", 1920, 1080) 
image dungeon_entry_bg = im.Scale("backgrounds/forest/dungeon_entry.png", 1920, 1080) 
image dungeon_bg = im.Scale("backgrounds/forest/dungeon.png", 1920, 1080) 
image magicSchool_bg = im.Scale("backgrounds/magic_school/magicSchool.png", 1920, 1080) 
image cauldron = im.Scale("images/backgrounds/magic_school/Cauldron.png", 1920, 1080)

#Initialization of variables 
default player_name = "" 
default overcoming_fears = 0 
default liar = False 
default realLetter = True 
default helpSister = False
 
# Start of the game 
label start: 
    # A background image of the field with a blackout effect is shown 
    scene field_bg 
    with fade 
    # Input the name of the main character 
    $ player_name = renpy.input("Enter the main character's name:") 
    # The .strip() function removes extra spaces that the player may have typed in accidentally. 
    $ player_name = player_name.strip()  
    # If the player has not entered a name, the default name will be Thomas. 
    if player_name == "": 
        $ player_name = "Thomas" 
     
    "The field, the sun is shining bright." 
    # Shows the main character on the screen with an appearance effect 
    show mainCharacter at center 
    with dissolve 
    p "Hmm..." 
    "You wake up in the middle of a field." 
    "You don't remember how you got here or where you are." 
    p "Where... Where am I?" 
    "You look around. You see a large yet beautiful field around you." 
    "It's surrounded by grass and lots of different beautiful and different colored flowers." 
    p "These flowers... they look so vivid, almost unnaturally so."
    "You reach out to touch a nearby sunflower, its petals almost glowing in the sunlight."
    p "But something feels off. The air is too still, too quiet."
    p "And it's beautiful here, but..." 
    "You rub your eyes." 
    p "Why is everything so fuzzy... and blurry? It's like he's not real." 
    p "(to myself) Maybe there's something wrong with my eyes?" 
    "After a few seconds, you realize that your eyes are not deceiving you and the world around you really doesn't look real." 
    p "(panicking a little) Where am I?!" 
    "You calm down quickly." 
    p "(to myself) Maybe it's just a dream?" 
    p "I've certainly had conscious dreams, but now some other sensations..." 
    p "I'm not just conscious, but I can still feel everything - the smell of the flowers, the warmth of the sun, the light flow of the wind..." 
    "A shiver runs down your spine, despite the warmth of the sun."
    p "(to myself) This feels different. More intense. More...real than a dream."
    "You pinch yourself, hoping to wake up, but nothing changes."
    "You, trying to figure out where you are, are also trying to remember the last moments before you were in this place." 
    p "So... The car... My sister... We were going somewhere." 
    p "(thinking) No, there's no way I could have fallen asleep, I was driving." 
    p "And the next thing I can't remember anything..." 
    "At that moment, all sorts of scary thoughts come into the your head." 
    p "(a little nervous) No way! We had an accident?" 
    p "Am I dead?!" 
    "Your heart pounds in your chest, a cold dread washing over you."
    p "(to myself) If I'm dead... what is this place? Heaven? Hell?"
    "You look around again, the vibrant field suddenly seeming eerie and unfamiliar."
    "With each passing second, you become more and more panicked and nervous, thinking that you are already dead" 
    "After a while, you calm down, but there's still a small sense of dread because of the uncertainty and not understanding what's happening to you." 
    "You realize that standing still and trying to remember the past won't get you out of here." 
    p "Okay, enough standing still here. I can't remember anything else." 
    p "We should take a look around." 
    "You look around and notices a nearby forest and a small path." 
    "Also from far away you discerned some strange figure, but you were standing far away, so he didn't make out the figure" 
    p "(to myself) A forest? That's... unsettling."
    p "There's someone standing there..." 
    p "And apparently it's waiting for me." 
    "You squint, trying to get a better look at the figure, but the distance is too great."
    p "(to myself) Who are they? Do they know what's going on?"
    "A sense of apprehension washes over you, but it's mixed with a desperate hope for answers."
    p "Okay, I have no other choice, I have to go there." 
    "You take a deep breath, steeling yourself for whatever lies ahead."
    p "(to myself) I need to find out where I am and how to get back... back to where I belong."
    "You take a step forward, then another, slowly moving towards the path that leads to the forest and the waiting figure."
    "As you walk, you notice details you hadn't seen before. The grass beneath you feet feels unusually soft, almost like walking on a cloud."
    p "(to myself) This is all too strange. None of this makes sense."
    "The flowers seem to sway in a rhythm that doesn't match the gentle breeze, their colors shifting subtly as he passes."
    "You glance back at the spot where you woke up, wondering if it's still visible from where you are now."
    p "(to myself) Will I even be able to find my way back if I need to?"
    "The thought sends a shiver down your spine, but you push it aside, focusing on the figure in the distance."
    "With each step, the figure becomes clearer, but still too far away to make out any distinct features."
    p "(to myself) Are they watching me? Do they know I'm coming?"
    "You try to project an air of confidence, though your heart is pounding in your chest."
    "The path leading to the forest is narrow and winding, disappearing into the shadows of the trees."
    p "(to myself) That forest looks dark... and ominous."
    "A primal fear tugs at you, warning you to turn back, but you know you can't."
    "You stop for a moment, taking in the scene before you."
    "The bright, vibrant field behind you, the shadowy forest ahead, and the enigmatic figure waiting in the distance."
    p "(to myself) This is it. No turning back now."
    "You take a final deep breath and continues walking, your steps more determined now, your fear replaced by a sense of resolve."
    "You're made yout decision. You're going to find answers, no matter what."
    hide mainCharacter with moveoutright 
 
    # Skip to the next scene 
    jump forestSpiritMeeting
 
# The scene of the meeting with the Forest Spirit
label forestSpiritMeeting:
    scene path1_bg with fade
    show forestSpirit at right2
    show mainCharacter at left2 with moveinleft

    fs "(politely) Greetings, traveler. We've been waiting for you for a long time."
    p "(suspiciously) We? Who's 'we'? Do you know me? Who are you? Where am I?"
    fs "(smiling) So many questions all at once. But I expected that."
    fs "I am the Forest Spirit, the guardian of this realm. As for where you are..."
    fs "You stand in a world that reflects your very being."
    p "(confused) My... being? What does that even mean?"
    "You glance around at the towering trees, the dappled sunlight filtering through the leaves, the strange stillness of the air."
    p "(to myself) This place feels... alive. But not in a natural way."
    fs "(gently) This forest is yours. It exists because of you. Every tree, every shadow, every path—they all come from within you."
    p "(denying) That’s ridiculous! How can an entire forest come from me?"
    "You gesture wildly at the surroundings, your voice laced with disbelief."
    p "I'm just a... a regular guy! I don't have forests inside me!"
    fs "(calmly) You might not remember, but you’ve carried this place with you your whole life."
    fs "When you were a child, it was brighter, simpler. But as you grew, so did its complexity—and its darkness."
    p "(interrupting) No. This doesn’t make any sense. Forests don’t just *exist* inside people!"
    fs "(nodding) True. Not in the way you think. But this isn’t a physical place—it’s a mirror."
    fs "A mirror of your thoughts, emotions, memories, and fears."
    p "(disbelieving) Fears? What fears? I don’t feel afraid."
    "You crosses your arms, trying to project an air of confidence, but a flicker of doubt crosses your eyes."
    p "(to myself) Is he trying to mess with my head?"
    fs "(gently) Don’t you?"
    "You hesitate, sensing a deeper weight behind the Spirit’s words. You look down, avoiding the Spirit's gaze."
    p "(shaking his head) I don’t have time for riddles. Just tell me how to get out of here!"
    fs "(seriously) To leave, you must first understand this place—and yourself."
    fs "You need to face what lies hidden here. Only then will the way forward reveal itself."
    p "(mocking) Oh, great. Let me guess—you’re some kind of mystical guide?"
    fs "(smiling faintly) If it comforts you to think of me that way, so be it. But I am more than that."
    fs "I am a part of you, after all."
    p "(snapping) You’re a part of me? You don’t even make sense!"
    "YOu take a step back, as if distancing himself from the Spirit's unsettling words."
    show mainCharacter at left3
    with moveoutleft
    p "(to myself) This is crazy. He's just messing with me."
    fs "(patiently) This world, this forest, was born the moment you were."
    fs "It has grown with you, changed with you, and now, it waits for you to confront it."
    p "(angrily) Confront it? Why should I? This place means nothing to me!"
    fs "(softly) If that were true, you wouldn’t be here."
    "You fall silent, a flicker of doubt crossing your face."
    "You look around again, your eyes scanning the forest with a new, uneasy awareness."
    fs "(continuing) You’ve ignored this place for so long. But now, you can no longer avoid it."
    fs "Your choices, your regrets, your pain—they’ve all led you here."
    fs "And until you face them, you cannot leave."
    p "(defiantly) What if I don’t want to face them? What if I just stay here?"
    fs "(seriously) Then you will remain here forever."
    p "(challenging) You’re lying."
    fs "(sharply) Am I? Think of the accident you’ve trapped yourself in."
    p "(confused) Accident? What are you talking about?"
    "You furrow your brow, the word 'accident' sounding foreign and yet strangely familiar."
    p "(to myself) What does that even mean? Is it some kind of code?"
    fs "(sadly) The accident. The moment everything changed."
    p "(growing tense) Accident...? No. Stop. You don’t know anything about me."
    "Your heart starts to race, a cold dread creeping into your chest. You clenches your fists, trying to suppress the rising panic."
    p "(to myself) How does he know about that? It's impossible."
    fs "(quietly) You were driving home with your sister that night. It was late, and you were tired. You only had one drink, but..."
    fs "One was all it took."
    "You stiffen, memories flashing unbidden in your mind."
    "The headlights of an oncoming car, the screech of tires, the shattering of glass."
    p "(angrily) Shut up! You don’t know what you’re talking about!"
    p "You’re not real! You’re just some... some hallucination!"
    "You cover your ears, trying to block out the Spirit's words, but they echo in your mind, relentless and piercing."
    p "(to myself) This isn't happening. This can't be happening."
    fs "(gently) Deny it all you want, but the truth remains."
    fs "You were rushing. You didn’t see the oncoming car until it was too late."
    "The protagonist stumbles back, shaking his head violently. He can almost feel the impact, the sickening crunch of metal, the world spinning out of control."
    p "(desperately) No. That’s not true. It’s not true!"
    fs "(firmly) And yet, here you are."
    "Silence falls between them, heavy and suffocating. The only sound is the rustling of leaves in the wind, a sound that now seems ominous and foreboding."
    p "(weakly) My sister... What happened to her? Is she alive?"
    "He looks up at the Spirit, his eyes filled with a desperate plea, a raw vulnerability he can no longer hide."
    p "(to myself) Please... let her be okay. Let this all be some terrible nightmare."
    fs "(quietly) I don’t know. My knowledge is limited to this world—your world."
    fs "But if you wish to find out, you must leave this place first."
    p "(whispering) I have to leave... I have to find out..."
    "He takes a deep, shaky breath, trying to regain his composure. The thought of his sister, alone and possibly hurt, fuels a surge of determination within him."
    p "(to myself) I have to do this. For her."
    fs "(gently) Then begin your journey. The path ahead is not easy, but it is necessary."
    "The Spirit takes a step closer, his presence both comforting and unsettling."
    "He seems to radiate an ancient wisdom, a deep understanding that both attracts and frightens the protagonist."
    fs "(sternly) A word of warning: this forest is not empty."
    fs "You will meet others here. Some will help you. Others... may not."
    fs "Be respectful. Even though you created this place, you are not in control of it."
    p "(hesitant) Who are they? These... others?"
    "He looks around nervously, the shadows between the trees suddenly seeming deeper, more menacing."
    p "(to myself) What else is lurking in this place?"
    fs "(cryptically) Fragments of yourself. Shadows of your past. And perhaps, echoes of your future."
    fs "You’ll understand more as you travel. For now, follow the path."
    p "(uneasy) And you? Are you coming with me?"
    fs "(shaking his head) No. My role is to guide you, not to walk your path for you."
    fs "But we will meet again. When the time is right."
    "The Forest Spirit begins to dissolve, his form shimmering like sunlight on water. He fades slowly, his presence lingering like a fading echo."
    p "(calling out) Wait! What if I fail? What if I can’t find the way out?"
    fs "(his voice fading) Then you will remain lost... until you find the courage to face yourself."
    "And with that, he is gone. The protagonist stands alone, the forest around him silent and still."
    "The sunlight seems dimmer now, the shadows longer, and a chill wind rustles through the leaves, carrying a sense of eerie isolation."
    p "(to myself) This is insane. None of this makes sense."
    "He runs a hand through his hair, his mind reeling from the encounter."
    "The Spirit's words echo in his head, a confusing mix of cryptic pronouncements and painful truths."
    p "(to myself) A forest inside me? My fears? The accident?"
    "He closes his eyes, trying to make sense of it all, but the images that flash through his mind are fragmented and disturbing."
    "He sees flashes of his sister's face, the twisted wreckage of a car, and a darkness that seems to swallow everything."
    p "(to myself) He knew about the accident. He knew about my sister. How?"
    "He opens his eyes and looks around again, the forest now seeming less like a beautiful landscape and more like a labyrinth of his own making."
    "The trees stand like silent sentinels, their branches reaching out like skeletal fingers, and the path ahead disappears into a shadowy unknown."
    p "(to myself) He said this place reflects me. My thoughts, my emotions, my memories... my fears."
    "He shivers, despite the warmth of the sun."
    "The thought of confronting his deepest fears is terrifying, but the alternative—remaining trapped in this strange world forever—is even worse."
    p "(to myself) I have to find the way out. I have to know what happened to my sister."
    "He takes a deep breath, trying to steady his nerves."
    "The air is thick with the scent of pine and damp earth, and a strange, ethereal melody seems to drift through the trees, almost too faint to hear."
    p "(to myself) What was that word he used? Accident? What does it mean?"
    "He repeats the word in his mind, trying to unlock its meaning, but it remains a mystery."
    "He wonders if it's a clue, a key to understanding this place and his own predicament."
    p "(to myself) Maybe I'll find out along the way. If there's a way to get out of here, I'll find it."
    "He looks down at the path before him, a narrow dirt track that winds its way into the heart of the forest."
    "It's a daunting prospect, facing the unknown with only the cryptic words of a disappearing spirit as guidance."
    p "(to myself) He said I'd meet others. Fragments of myself. What does that even mean?"
    "He imagines shadowy figures lurking among the trees, watching his every move, judging his every decision."
    "The thought sends a chill down his spine, but he forces himself to stay calm."
    p "(to myself) I can't let fear control me. I have to be strong. For my sister."
    "He takes one last look at the spot where the Forest Spirit had stood, the air still shimmering with a faint, residual energy."
    "Then, with a deep breath, he steels himself and takes his first step forward into the unknown."
    p "(after a pause) But if there’s even a chance... I have to try. For her."
    "He sets off down the path, his footsteps echoing softly in the quiet forest."
    "The trees loom overhead, their leaves rustling in the breeze, and the dappled sunlight paints intricate patterns on the ground."
    "He doesn't know what lies ahead, but he knows he can't turn back."
    p "(to myself) This is just the beginning. I have to keep moving forward."
    "He walks on, his eyes scanning the forest around him, his mind racing with questions and uncertainties."
    "But beneath the fear and confusion, a spark of determination begins to grow. He will face whatever this forest throws at him, and he will find his way home."

    jump wiseManMeeting

# The scene of the meeting with the Wise Man 
label wiseManMeeting: 
    scene bigTree_bg  
    with fade 
    "The protagonist is walking down a path and sees an unusual and huge tree ahead of him." 
    show mainCharacter at center 
    with moveinleft 
    p "Wow... What a huge tree..." 
    p "It also looks so strange.... Unusual... But beautiful..." 
    "The protagonist approaches a tree and sees a passage inside the tree." 
    p "There's a passage in the tree...? I wonder what's inside?" 

    "He circles the tree cautiously, peering into the darkness within."
    "The air around the tree feels thick with an ancient energy, almost palpable."
    p "(to myself) This feels... different. Like something important is here."

    "The protagonist was about to go inside the tree when suddenly a wise old man comes out." 
    show mainCharacter at left2 
    with moveinleft 
    show wiseMan at right2  
    with dissolve 
    wiseMan "(smiling) Greetings, traveler!" 
    p "(surprised) Hi! Who are you?" 
    wiseMan "Everyone calls me Wise Man. What will you be?" 
    # Display the protagonist's name on the screen 
    p "My name is [player_name]. I... I created this world." 

    "He hesitates, the words feeling strange and unfamiliar on his tongue."
    "He still can't quite grasp the concept of this forest being his own creation."

    wiseMan "(surprised) Oh, I'm sorry I didn't recognize you right away."
    wiseMan "I don't have very good eyesight, so I didn't realize who you were right away." 
    p "It's no big deal." 
    p "You'd better tell me what this tree is and why it's so unusual?" 
    p "And why the passage in the tree? Do you live there?" 
    wiseMan "This tree is the Great Tree. It holds all your wisdom, knowledge, and experience that you have gained throughout your life." 
    wiseMan "You could say it's your library, where all your knowledge is stored." 
    wiseMan "You might ask, since this Tree holds all knowledge, what is this old man doing here and why does he live in a tree?" 
    wiseMan "And I'll answer you. I am your wisdom. I am your experience. I am your knowledge." 
    wiseMan "How shall I put it. I am this tree, only in spirit form. Or human, whatever you want to call it." 
    p "(to himself) This old man is obviously nuts if he thinks he's a tree." 

    "He eyes the old man skeptically, wondering if he's encountered another enigmatic being like the Forest Spirit."

    "The main character wanted to ask something, but suddenly he saw the old man start eating bugs." 
    "The protagonist became wary when he saw such a thing." 
    "Seeing with what appetite the old man eats bugs, the protagonist immediately forgot what he wanted to ask." 
    p "(to myself) What the...?! I mean, he eats bugs! What a weird old man!" 

    "He suppresses a shudder, his stomach churning at the sight."
    "He takes a step back, unconsciously distancing himself from the bug-eating sage."

    "The sage, having finished his lunch, looked at the protagonist and smiled." 
    wiseMan "You obviously came for a reason and you want me to help you." 
    wiseMan "I can help you, but the price for my help is your decisions." 
    # Function called to display the in-game menu with two options. 
    menu: 
        # Menu item for selecting Forest Spirit Trust (Option One) 
        "Trust the Wise Man and accept his help.": 
            # Show notification of changes in relationship 
            show screen custom_notify("Your relationship with the Sage has improved") 
            $ relationship_wiseMan += 1 
            "The protagonist recalls the Wise Man's behavior and his dinner."  
            "After everything he's seen, the main character doesn't really want to trust the Sage, but he decides to trust since he has no other choice." 
            "The Sage is the only one who can help us get out of this place so far." 

            p "Okay, I'm willing to accept your help. Though, I have to admit, you're a bit... unconventional."
            p "And please, no more bug-eating while I'm around."

            wiseMan "A wise man takes sustenance where he finds it. But very well, I'll refrain."
            wiseMan "Now, as for your path..."
            wiseMan "Follow this path further down, and then at the intersection, turn left. There you'll find what you're looking for."
            p "Thank you! I'll be off." 

            "He nods gratefully, still slightly unnerved by the encounter, but relieved to have some direction."
            p "(to myself) Left at the intersection. Got it."

            "The Sage smiled and disappeared into the tree. The passage seems to ripple and close behind him, as if it were never there."
            hide wiseMan  
            with dissolve 
            "The protagonist was left alone on the path." 
            p "(to myself) Well, I'll move on." 
        # Menu item to refuse the help of a forest spirit(Second option) 
        "Be wary and refuse help.": 
            show screen custom_notify("Your relationship with the Sage has deteriorated") 
            $ relationship_wiseMan -= 1 
            "The protagonist recalls the Sage's behavior and his dinner. After all he has seen, the protagonist decides not to trust the Wise Man." 

            p "(with disbelief) I'm sorry, but I can't trust you. Especially not after that... snack."
            wiseMan "A pity. Perhaps you'll reconsider when you've encountered more of this world's... peculiarities."
            p "I think I can handle myself. I created this world, after all, so I'll find a way out." 

            "He turns to leave, his gut telling him to get away from this strange old man."
            "He feels a flicker of uncertainty, a nagging doubt about his decision, but he pushes it aside."
            p "(to myself) I don't need his help. I can figure this out on my own."

            "The Sage silently turned around and disappeared into the tree."
            "The passage ripples and closes, leaving no trace of its existence."
            hide wiseMan 
            with dissolve 
            "The protagonist was left alone on the path." 

            "The protagonist felt something change inside him, but he didn't know what."
            "A certain weight, a sense of lost opportunity, settles upon him."
            "It got a little lonely and cold on his soul." 
            "But that feeling passed almost immediately and the protagonist continued on his way, trying to ignore the lingering unease."
            p "(to myself) Well, let's start looking for a way out on our own. Though, which way is even 'out' in this place?"
            "He looks down both directions of the path, trying to decide which way to go."
            "The forest seems to press in on him, the silence amplifying his sense of isolation."
            p "(to myself) I guess it doesn't really matter. One way or another, I have to keep moving."

    hide mainCharacter  
    with moveoutright 
 
    jump forestCrossroad
 
# Crossroads scene in the woods 
label forestCrossroad: 
    scene crossroad_bg  
    with fade 
    "The protagonist is walking down a path and sees a crossroads in front of him." 
    show mainCharacter at center  
    with dissolve 
    p "So... There's an intersection here... Which way should I go, right or left?" 
    "He stops at the crossroads, taking in his surroundings."
    "The path ahead splits into two distinct directions: one leading deeper into the shadowy woods, the other towards a clearing bathed in a soft, ethereal light."
    p "(to myself) This place feels... heavy. Like there's a weight hanging in the air."
    "He looks down the right-hand path, a narrow track that winds through dense trees, barely visible in the gloom."
    "An unsettling silence emanates from the darkness, broken only by the occasional rustle of unseen leaves."
    p "(to myself) That way looks ominous. Like something dangerous is lurking in the shadows."
    "He then turns his gaze towards the left-hand path, a wider, more inviting route that leads towards a glade filled with glowing flowers and shimmering mist."
    "A gentle warmth radiates from the clearing, a stark contrast to the chill that permeates the right-hand path."
    p "(to myself) That way seems more peaceful. But is it the right way?"
    # Automatically selects the correct option if the relationship with the Sage is 1 (positive relationship) 
    if relationship_wiseMan == 1: 
        "The protagonist was about to turn right, but abruptly remembers the Wise Man's words and decides to turn left." 
        p "(to myself) Right! The Wise Man said I should take a left turn. I hope he knows what he's talking about."
        p "(to myself) That bug-eating habit doesn't exactly inspire confidence, but..."
        "He hesitates for a moment, glancing back at the right-hand path, a flicker of doubt crossing his face."
        "But then he steels himself, remembering his purpose."
        p "(to myself) I have to trust someone. And I promised myself I'd find out what happened to my sister."
        "The main character turns left and walks down the path towards the light-filled glade."
        "As he walks, the air grows warmer, the scent of flowers stronger, and the oppressive weight he felt at the crossroads begins to lift."
        p "(to myself) This feels better. Like I'm heading in the right direction."
        $ rightChoice = True 
    else: 
        # Display the directional selection menu at the intersection if the relationship with the Sage is not 1 
        menu: 
            "Turn right deep into the woods.": 
                "The main character turns right and walks down the path." 
                p "(to myself) Well, I'll go right. Against the Wise Man's advice, but something tells me this is the way I need to go."
                "The path narrows, the trees closing in around him, their branches intertwined like skeletal arms reaching out to grasp him."
                "The air grows colder, the shadows deeper, and the silence becomes more profound, more unnerving."
                p "(to myself) I hope I'm not making a mistake. This place feels... wrong."
                hide mainCharacter with moveoutright 
                $ rightChoice = False 
            "Turn left to the light glade.": 
                "The main character turns left and walks down the path." 
                p "(to myself) Well, I'll go left. It seems safer than the other way, at least."
                "The path widens, leading him into a glade bathed in a warm, inviting light."
                "Colorful flowers bloom all around, their petals shimmering with an iridescent sheen, and a gentle mist hangs in the air, creating an ethereal atmosphere."
                p "(to myself) This is... beautiful. I wonder what I'll find here."
                hide mainCharacter with moveoutleft 
                $ rightChoice = True 
 
    # Depending on the player's choice, move to the next scene 
    if rightChoice: 
        jump unknown_house
    else: 
        jump pathIntoDarkForest
 
label unknown_house:
    scene unknownHouse_bg with fade
    show mainCharacter at center
    "Ты идешь по тропинке и вдруг видишь перед собой дом."
    "Ты не знаешь чей это дом и как он тут оказался, но ты чувствуешь, что от него не исходит что-то зловещее."
    "Тебе совсем не страшно от того, что или кто нам находится и что могут с тобой сделать."
    "Ты уверен, что ты в безопасности и тебе не стоит бояться этого места."
    p "(про себя) Довольно уютный домик."
    p "(про себя) Не думаю, что со мной случиться что-то страшное, если я зайду в этот дом."
    p "Может быть мне даже повезёт и я кого-нибудь встречу и он мне поможет в моём пути."
    "Ты, сделав сильный вздох, заходишь в дом"
    scene houseEntry_bg with fade
    "Ты входишь внутрь дома."
    "Внутри довольно ярко и уютно."
    "Дома довольно чисто, но в доме никого нету"
    "Ты решаешь осмотреться и видишь, что рядом лежит какая-то записка"
    jump start_house_minigame
    
# The scene of the meeting with the Shadows in the dark woods 
label pathIntoDarkForest: 
    scene darkForest_bg with dissolve 
    show mainCharacter at left2  
    with moveinleft 
    "You decide to venture deep into the forest."
    "Dark trees and shadows cover you, giving you an oppressive feeling, as if something sinister lurks behind every tree." 
    "The forest seems endless, and the silence oppresses your thoughts, making your heart beat faster." 
    p "Something's wrong. It's like this forest has a life of its own. But I have to keep going." 
    "He walks on, his footsteps echoing unnaturally loud in the stillness."
    "The air grows heavy, the shadows deepening around him, creating an almost suffocating atmosphere."
    p "(to myself) I shouldn't have come this way. This place feels... malevolent."
    "Suddenly, two figures appear in front of you." 
    show shadow_woman at right2 
    with dissolve 
    show shadow_man at right1 
    with dissolve 
    "There's a strange feeling coming from them." 
    "The sight of them gives you goosebumps. You get scared." 
    "Looking at them makes you more and more scared by the second." 
    "Your heart starts beating faster and faster." 
    "Your breathing is quickening." 
    "They stand silently, their forms flickering and shifting like flames in the dim light."
    "Their features are obscured by shadows, but he can sense their eyes fixed on him, cold and piercing."
    p "(to myself) What are they? They feel... familiar. But in a disturbing way."
    "He takes a step back, his hand instinctively reaching for something to defend himself with, but he finds nothing."
    "He feels a growing sense of dread, a primal fear rising within him."
    p "(through fear) Who are you?!" 
    show shadow_man at center 
    with moveinleft  
    "One of the Shadows comes closer, her voice sounding like the whisper of the wind:" 
    shadow "We are your mistakes, your fears. You can't hide from us." 
    "The voice seems to echo from all around him, as if the forest itself is speaking."
    "He feels a cold shiver run down his spine, his muscles tensing in anticipation."
    "You try to back away, but another Shadow blocks your path." 
    shadow "You can't run away from us. We'll always be with you." 
    shadow "You wanted to get rid of us, so you put us in this damn forest." 
    shadow "But you can't get rid of us. We're part of you." 
    shadow "We are your shadows." 
    "Their voices intertwine, a chilling chorus that seems to penetrate his very being."
    "He feels trapped, surrounded by the embodiment of his deepest fears and regrets."
    p "(to myself) My shadows? What does that even mean? Are they real? Or am I losing my mind?"
    "You're backing off a bit." 
    show mainCharacter at left3 
    with moveoutleft 
    "The shadows are starting to close in on you." 
    "You can feel them starting to pull you in their direction." 
    "He can feel their presence closing in, a suffocating darkness that threatens to consume him."
    "He tries to focus, to think clearly, but his mind is racing, his thoughts scattered and fragmented."
    "You try to back away, but the shadows are getting closer and closer." 
    "You're in a panic wondering what to do." 
    "He glances from one shadow to the other, desperately searching for a way out."
    "His heart pounds in his chest, his breath coming in short, ragged gasps."
    "He knows he has to do something, anything, to escape this nightmare."
    "You're faced with a choice:" 
    menu: 
        "To try and talk to the Shadows.": 
            jump talk_to_shadows 
        "Run away.":
            jump run_away
 
# The scene of trying to talk to the Shadows 
label talk_to_shadows: 
    show screen custom_notify("You have overcome your fears.") 
    $ overcoming_fears += 1 
    "You decide to try talking to the Shadows, realizing that you can't run away from your fears." 
    "He takes a deep breath, steeling himself against the fear that threatens to overwhelm him."
    "He looks directly at the Shadows, his gaze unwavering."
    p "(through fear, but with a hint of defiance) I am not afraid of you."
    "You are only a part of me, and I will accept my mistakes." 
    shadow "You think you can put up with us? We'll always be there for you."
    shadow "We are the constant reminders of your failures, your regrets."
    p "(determined) I know you'll always be there for me. And I'll always be scared." 
    p "I will hesitate, but I will not run." 
    p "You can't run away from your mistakes and fears forever. I will accept my mistakes and move on." 
    "He stands tall, his voice gaining strength with each word."
    "He can feel a shift within him, a sense of acceptance and resolve replacing the fear that had gripped him."
    shadow "Do you think it's that easy? To simply accept us?"
    shadow "We are a part of you, woven into the fabric of your being."
    p "I know. And I don't expect it to be easy. But I'm not going to let you control me anymore."
    p "I'm not going to let my past define me. I'm going to learn from it, and I'm going to move forward."
    "The shadows begin to dissolve, as if realizing that you are no longer afraid of them. You feel relief and release." 
    "As they fade, he can see glimpses of his past, painful memories that he had long suppressed."
    "He sees the car accident, the fear in his sister's eyes, the crushing weight of guilt."
    "But now, the memories don't hold the same power over him. He acknowledges them, accepts them, and lets them go."
    p "I understand now. I can't hide from the past, but I can embrace it." 
    p "(to myself) And I can use it to become stronger. To become the person I need to be."

    jump return_to_crossroad 
 
# Escape scene from the Shadows  
label run_away: 
    $ overcoming_fears -= 1 
    show screen custom_notify("You have not overcome your fears.") 
    "You decide to run away from the Shadows, realizing you can't handle them." 
    "You've never been as scared as you are right now." 
    p "(to myself) Gotta run away! Gotta run away!" 
    hide mainCharacter with moveoutleft 
    "You run, but you see that the Shadows aren't running after you, they're just standing still and laughing loudly." 
    "The shadows stare at your back as you run away and disappear into the darkness of the forest." 
     
    jump return_to_crossroad 
 
# The scene of the return to the crossroads after the meeting with the Shadows     
label return_to_crossroad: 
    scene crossroad_bg with fade 
    "You're going back to the crossroads." 
    show mainCharacter at center 
    with moveinright 
    if overcoming_fears > 0: 
        p "(to myself) It was really scary and creepy, but I kind of made it through." 
        p "I can't remember the last time I was this scared." 
        "You take a deep breath to calm yourself."
        p "(sighing) Phew... Gotta be more careful about my choices next time." 
        p "(thinking) At least I've learned my lesson..." 
        p "I realized that it's okay to be wrong and afraid, and they don't have to be considered the enemy." 
        p "Mistakes and fears are part of every journey. Without fear and mistakes, there is no success." 
        "He looks down the right-hand path, the shadows no longer seeming as menacing."
        "He considers going that way, now that he's faced his fears, but then shakes his head."
        p "(to myself) No. I made a promise. I need to keep going forward. For my sister."
        "He looks towards the left-hand path, the light from the glade beckoning him onward."
        "He takes a deep breath and starts walking, his steps more confident now, his fear replaced by a sense of purpose."
        p "(to myself) I don't know what lies ahead, but I'm ready to face it. Whatever it takes."
        "After you've thought it over, you decide to continue on your journey." 
        p "Well, I'll move on." 
    else: 
        p "(to myself) It was really scary!!! I can't do this anymore!" 
        "You're starting to panic again and can't get your act together." 
        p "Why don't they just tell me where the exit is?!" 
        p "What's the point of all these trials and adventures?" 
        p "I just want to go home!" 
        "He sinks to his knees, his body trembling, tears streaming down his face."
        "The weight of his fear and confusion overwhelms him, leaving him feeling lost and helpless."
        "You start crying and you can't hold back the tears." 
        p "I thought... I thought I was going to be killed..." 
        p "I don't want to go on like this..." 
        p "I want to go home..." 
        "He curls up, wrapping his arms around himself, trying to find some semblance of comfort in the midst of his despair."
        "The forest around him seems to mock him, its silence amplifying his isolation."
        p "(to myself) I'm trapped. I'll never get out of here. I'll never see my sister again."
        "After a while, he slowly begins to regain his composure."
        "He wipes his tears, takes a deep, shaky breath, and forces himself to stand up."
        p "(to myself) I can't give up. Not yet. I have to keep trying. For her."
        "He looks down the left-hand path, the one he had avoided before."
        "It's the only way forward now, the only chance he has of escaping this nightmare."
        "After the tantrum and after you've thought it over, you decide to continue on your path." 
        p "There's a second way, hopefully it will be better." 
     
    hide mainCharacter with moveoutleft 
    jump unknown_house
 
# The scene of the meeting with the sister 
label sisterMeeting: 
    scene path2_bg with fade 
    "You passed that little test." 
    "You go and wonder why someone would want to hide some potion in their own house." 
    "The most important question is from whom and why?" 
    "You suddenly hear voices." 
    "You see a man hitting on a woman." 
    show shadow_bandit at right3 
    with dissolve 
    show sister_img at right1 
    with dissolve 
    "You decide to get close to them so you can hear what they're talking about, but at the same time be unnoticed." 
    "As you get closer, you start to hear them talking." 
    "But you also notice that this man is unusually tall." 
    "Get oA me!" 
    "But I love you!" 
    "You shadow! You lost soul!" 
    "How did you even get in here?! You're not supposed to be here!" 
    "Come to me! You'll be with me forever!" 
    "No! Get oA!" 
    "You see the shadow trying to grab your sister." 
    show sister_img at center 
    with moveoutleft 
    show shadow_bandit at right2 
    with moveinright 
    "You want to help her, but you're scared. That shadow looks too dangerous and too big." 
    "You're thinking about what to do." 
    menu: 
        "Help a woman.":
            $ helpSister = True
            jump help_sister 
        "The man is too big, I can't handle him.":
            jump dont_help_sister 
 
# The scene of helping my sister     
label help_sister: 
    show screen custom_notify("You have overcome your fears.") 
    pause 3.0 
    show screen custom_notify("Your relationship with your sister has improved.") 
    $ overcoming_fears += 1 
    $ relationship_sister += 1 
    "You decide to help a woman." 
    "You walk up to them and start talking." 
    show mainCharacter at left2 
    with moveinleft 
    p "Hey! Leave her alone!" 
    shadow "Who are you?!" 
    shadow "Go on your way, you little man!" 
    "Shadow doesn't pay attention to you and keeps hitting on the woman." 
    "He steps between the shadow and the woman, his fear momentarily forgotten in a surge of protective anger."
    p "(menacingly) I am the one who created this world!" 
    p "I am the one who created you!" 
    p "I'm [player_name]!" 
    p "And I won't let you hurt her!" 
    "His voice rings with authority, surprising even himself."
    "He can feel a power emanating from within, a connection to this strange world that he hadn't felt before."
    "The shadow stops and looks at you." 
    "The shadow and the woman look at you in surprise." 
    "They're shocked by what you said." 
    shadow "(surprised) You..." 
    show shadow_bandit at right3 
    with moveoutright 
    "The shadow takes a step back in fright." 
    shadow "(surprised) No way..." 
    shadow "It's you! You shouldn't be here!" 
    p "(menacingly) The only one who shouldn't be here is you!" 
    p "(confidently) I created you, and I can destroy you!" 
    "He glares at the shadow, his eyes burning with intensity."
    "He can feel the shadow's fear, its power diminishing in the face of his newfound confidence."
    "You don't stop staring menacingly at the shadow." 
    "Shadow realizes you're serious and he gets scared." 
    "Shadow feels a lot of pressure coming from you." 
    shadow "I'm sorry! I'm leaving! Just don't kill me!" 
    p "(menacingly) Go away!" 
    hide shadow_bandit with moveoutright 
    "The shadow runs away, disappearing into the darkness of the forest." 
    "He watches the shadow flee, a sense of triumph washing over him."
    "He turns to the woman, his relief evident in his expression."
    show sister_img at right2 
    with moveoutright 
    show mainCharacter at left2 
    sister "Thank you, little brother! I don't know what I'd do without you!" 
    p "You're welcome! I did the best I could!" 
    "He smiles, but then freezes, her words catching him off guard."
    "For a second you froze in bewilderment." 
    p "(hesitantly) Did you say 'little brother'?" 
    sister "Yes! You're my brother!" 
    p "(surprised) What?" 
    p "How is that so? The Forest Spirit said I'm alone in this world. And it's not connected to the real world." 
    p "(scared) You died too?! And why don't I remember you!" 
    "He stammers, his mind reeling from the revelation. The fear returns, colder and sharper than before."
    sister "(trying to calm you down) No, no! I'm not your sister." 
    sister "I may look like your sister, but I'm not your sister." 
    sister "I am what you wouldn't help me without." 
    p "(unsure) Confidence?!" 
    sister "(chuckling) If I was your confidence, you wouldn't have to help me. I would have chased that shadow away myself." 
    p "(embarrassed) Then who are you?" 
    sister "I am your kindness."
    p "(surprised) Kindness? But why do you look like my sister?" 
    sister "(thoughtfully) Hmm. I don't even know... Maybe you subconsciously made me look like that?" 
    sister "Or maybe because you're a kind and caring brother?" 
    "He blushes at her words, a warmth spreading through his chest."
    "He looks at her, really looks at her, and sees a kindness and compassion in her eyes that mirrors his own."
    "You blushed imminently at such words."
    "She saw that and started giggling." 
    sister "Heehee, you're so cute!" 
    sister "But if it makes you feel more comfortable, you can call me sister." 
    p "(embarrassed) Well... Okay..." 
    "He smiles shyly, the tension easing from his shoulders."
    "He feels a connection to this woman, a sense of kinship that transcends the strangeness of this world."
    "Your sister smiled and turned the conversation to another topic." 
    sister "Since you helped me, I'll help you too." 
    sister "You're looking for a way out of this place, right?" 
    p "Yes, I'm looking for a way out. Can you help me?" 
    sister "Of course! I know someone who can help you." 
    sister "I was just about to meet this man." 
    sister "You can come with me if you want." 
    "He nods eagerly, grateful for her offer."
    "He feels a flicker of hope, a sense that he might actually escape this strange world and find his way back to reality."
    p "Yes, I'll go with you." 
    "He falls into step beside her, the two of them walking side-by-side down the path."
    "The forest seems less menacing now, the shadows less oppressive."
    "He feels a sense of companionship, a shared purpose that eases his loneliness and strengthens his resolve."
    "You follow your sister, not knowing what lies ahead, but feeling more confident now that you're not alone."
    p "(to myself) Maybe, just maybe, I'll find my way home. And maybe, along the way, I'll learn something about myself too."

    jump pathToTavern
 
# Scene of refusing to help his sister 
label dont_help_sister: 
    show screen custom_notify("You have not overcome your fears.") 
    pause 3.0 
    show screen custom_notify("Your relationship with your sister has deteriorated.") 
    $ overcoming_fears -= 1 
    $ relationship_sister -= 1 
    "You choose not to interfere with their conversation."
    "You realize you can't handle the shadows. He's too huge and dangerous." 
    "You decide to leave and stay out of their business." 
    "He hesitates, his heart pounding in his chest."
    "He wants to help, he knows he should help, but the fear is too strong."
    "The shadow's menacing presence overwhelms him, paralyzing him with indecision."
    p "(to myself) I can't do this. He's too powerful. I'd just get hurt... or worse."
    "He takes a step back, then another, his gaze fixed on the terrifying scene unfolding before him."
    "He can hear his sister's cries, her pleas for help, but he forces himself to turn away."
    p "(to myself) I'm sorry. I'm so sorry. But I can't. I just can't."
    "He turns and runs, his footsteps echoing in the silent forest."
    "He doesn't look back, his shame and guilt weighing heavily on his shoulders."
    "He tries to block out the sounds of his sister's struggle, but they haunt him, echoing in his mind."
    p "(to myself) I'm a coward. I abandoned her. I left her to face that monster alone."
    "Women look around in fear and notice you moving away from them." 
    sister "(desperately) Wait! Don't leave me! Please, help me!"
    "Her cry pierces his heart, but he keeps running, his fear driving him forward."
    "He knows he's made a terrible mistake, a choice he'll likely regret for the rest of his life."
    p "(to myself) I'll never forgive myself for this. Never."
    "He runs until he can no longer hear his sister's cries, until the only sound is the pounding of his own heart and the ragged gasps of his breath."
    "He collapses against a tree, his body shaking, his mind consumed by fear and self-loathing."
    p "(to myself) What have I done?"
    "He sits there for a long time, lost in his despair, the image of his sister's terrified face seared into his memory."
    "He knows he has to keep moving, to find a way out of this cursed forest, but the weight of his cowardice makes every step a struggle."
    p "(to myself) I have to keep going. But how can I face anyone after this? How can I face myself?"

    jump pathToTavern 
    return
 
# The scene on the way to the tavern 
label pathToTavern: 
    # Counting the total number of character relationships to date 
    $ overall_relationships += relationship_sister + relationship_wiseMan 
    if overall_relationships > 0 and overcoming_fears > 0: 
        scene birch_bg with fade 
        show mainCharacter at center  
        with dissolve 
        "After a while you come to a grove of birch trees." 
        "You feel relief and joy." 
        "It makes you want to smile and glow with joy." 
        "You feel like you're on the right track." 
        "You wanted to tell your sister something, but she wasn't around." 
        "She disappeared somewhere." 
        "You were starting to get worried, but then you see a familiar figure approach you." 
        show forestSpirit at right2  
        with moveinright 
        "It's a Forest Spirit." 
        "Greetings! It's been a long time." 
        "After seeing the Forest Spirit, you immediately stopped thinking about your sister and where she disappeared to."
        "You could say with absolute certainty that she was fine." 
        p "Hi! Yeah, long time no see." 
        fs "Maybe, but I've been watching you the whole time." 
        fs "Your Kindness... {w} I'm sorry, your sister is fine. I'd like to talk to you in private." 
        "You're a little puzzled by what he said about his sister." 
        p "(puzzled) How did you...? How did you know about my sister?" 
        "I am, after all, a Forest Spirit. I know a lot about you and this world." 
        p "Ah yes... Right..." 
        p "And where did you follow me from? I didn't see you." 
        fs "I've lived here your whole life, so I know these places better than anyone. I'm good at hiding." 
        "I also have to keep an eye on this world so that it doesn't die and trouble doesn't happen in it." 
        "Keeping things in order, so to speak." 
        p "I see..." 
        fs "I wanted to tell you that you're on the right track." 
        fs "Move in the same direction and you're sure to find what you're looking for." 
        p "Thank you, Forest Spirit." 
        p "And how do I know I'm moving in the right direction?" 
        fs "I don't remember if I said this before or not, but your actions reflect on this world." 
        fs "If you see bright spots around you, you're on the right track." 
        fs "If you see dark and gloomy places, you're going to the wrong place." 
        p "(thoughtfully) I see... Good..." 
        "Okay, I won't keep you. You've got a lot to do." 
        fs "You're good to go. Good luck to you!" 
        p "Thank you! See you later!" 
        hide forestSpirit with dissolve 
        "The Forest Spirit smiled and disappeared into the forest." 
        "After he disappears, your sister appears beside you." 
        show sister_img at left2 
        with dissolve 
        "What are you standing up for? Let's move on!" 
        p "Yes, yes, of course!" 
        "You continued your journey together." 
        jump tavern 
    else: 
        scene deadTree_bg with fade 
        show mainCharacter at center  
        with dissolve 
        "After a while you come to a dead tree." 
        "You feel stiA and afraid." 
        "You're wary, you've got goosebumps." 
        "You feel like you're not on the right track." 
        "You were starting to get worried, but then you see a familiar figure approach you." 
        show forestSpirit at right2  
        with moveinright 
        "It's a Forest Spirit." 
        "Greetings! It's been a long time." 
        "After seeing the Forest Spirit, then you calmed down a bit."
        "You realized that as long as he was around, you were fine." 
        p "Hi! Yeah, long time no see." 
        fs "Maybe, but I've been watching you the whole time." 
        fs "And you disappointed me..." 
        "You're a little puzzled by his words." 
        p "(puzzled) Disappointed? What did I do wrong!" 
        if relationship_wiseMan == -1 and relationship_sister == 1: 
            fs "You have rejected the Wise Man and have not understood his lessons." 
            p "He ate bugs!" 
            fs "Yeah, he's a little weird, but he's a good person." 
            fs "Just because he's diAerent doesn't mean he's bad and shouldn't be dealt with." 
            fs "But at least you didn't chicken out and helped Kindness when you could have run away. That was commendable." 
            p "And where did you follow me from? I didn't see you." 
            fs "I've lived here your whole life, so I know these places better than anyone. I'm good at hiding." 
            "I also have to keep an eye on this world so that it doesn't die and trouble doesn't happen in it." 
            "Keeping things in order, so to speak." 
            p "I see..." 
            fs "I wanted to tell you that you're a little oA the right track." 
            p "(puzzled) \"Have you strayed from the right path?\"" 
            p "How do I know I'm moving in the right direction?" 
            fs "I don't remember if I said this before or not, but your actions reflect on this world." 
            fs "If you see bright spots around you, you're on the right track." 
            fs "If you see dark and gloomy places, you're going to the wrong place." 
            p "(thoughtfully) I see... Good..." 
            "Okay, I won't keep you. You've got a lot to do." 
            "You can go." 
            p "Thank you! See you later!" 
            hide forestSpirit with dissolve 
            "The Forest Spirit smiled and disappeared into the forest." 
            "After he disappears, your sister appears beside you." 
            show sister_img at left2 
            with dissolve 
            "What are you standing up for? Let's move on!" 
            p "Yes, yes, of course!" 
            "You are a little distressed by his words about the Sage, but you continued your journey together." 
            jump tavern 
        elif relationship_wiseMan == 1 and relationship_sister == -1: 
            fs "You rejected Kindness and did not understand his lessons." 
            p "But there was a huge shadow!" 
            fs "Yes, there was a huge shadow." 
            "You didn't have to fight the shadow. You could have spooked it." 
            fs "But at least you didn't reject the Sage, despite his oddities. That was commendable." 
            p "And where did you follow me from? I didn't see you." 
            fs "I've lived here your whole life, so I know these places better than anyone. I'm good at hiding." 
            "I also have to keep an eye on this world so that it doesn't die and trouble doesn't happen in it." 
            "Keeping things in order, so to speak." 
            p "I see..." 
            fs "I wanted to tell you that you're a little oA the right track." 
            p "(puzzled) \"Have you strayed from the right path?\"" 
            p "How do I know I'm moving in the right direction?" 
            fs "I don't remember if I said this before or not, but your actions reflect on this world." 
            fs "If you see bright spots around you, you're on the right track." 
            fs "If you see dark and gloomy places, you're going to the wrong place." 
            p "(thoughtfully) I see... Good..." 
            "Okay, I won't keep you. You've got a lot to do." 
            "You can go." 
            p "Thank you! See you later!" 
            hide forestSpirit with dissolve 
            "The Forest Spirit smiled and disappeared into the forest." 
            "You're a little saddened by what he said about Kindness, but you continued on your way." 
            jump tavern 
        elif relationship_wiseMan == -1 and relationship_sister == -1: 
            fs "You have rejected the Wise Man and have not understood his lessons." 
            fs "You also rejected Kindness, even though you needed her and she looked like your sister." 
            p "But there was a huge shadow! И... and there was a huge shadow!" 
            fs "(menacingly) Don't interrupt! I'm talking now!" 
            "You got scared and shut up." 
            fs "Yes, there was a huge shadow." 
            "You didn't have to fight the shadow. You could have spooked it." 
            "But you still chickened out!" 
            fs "You chickened out without even trying anything. Even when she looked like your sister!!!" 
            "The Forest Spirit keeps reprimanding you for your actions." 
            fs "You have also rejected the Sage!" 
            fs "You only wanted to take the easiest path and you didn't want to be surrounded by people like him." 
            "You're not like that, and you don't need friends like that." 
            p "(silent) ..." 
            "There was an awkward silence." 
            "Soon the Forest Spirit continues." 
            fs "I wanted to tell you that you deviated from the right path." 
            p "(puzzled) \"Have you strayed from the right path?\"" 
            p "How do I know I'm moving in the right direction?" 
            fs "I don't remember if I said this before or not, but your actions reflect on this world." 
            fs "If you see bright spots around you, you're on the right track." 
            fs "If you see dark and gloomy places, you're going to the wrong place." 
            p "(thoughtfully) I see... Good..." 
            "You've really disappointed me a lot." 
            "Go!" 
            hide forestSpirit with dissolve 
            "The Forest Spirit smiled and disappeared into the forest." 
            p "Fine! I'll move on!" 
            p "I'll manage without you!" 
            "You are distressed by his words about the Sage and the Kindness, but you have continued on your way." 
            jump swamp

# The scene of the tavern
label tavern: 
    if relationship_sister == 1: 
        scene tavern_bg with fade 
        show stranger_img at right3 
        with dissolve 
        "After a long time, you approach the tavern and go inside." 
        show sister_img at left2 
        with moveinleft 
        show mainCharacter at left3 
        with moveinleft 
        "It's quite cozy and warm inside the tavern, as well as very crowded." 
        "There are candles burning everywhere and you can hear pleasant music." 
        "It's like the whole tavern is protected from the outside world." 
        "You feel safe inside the tavern." 
        sister "Here we are!" 
        p "Yes, we're here!" 
        sister "See that man over there by the table? He's the one who can help us." 
        "You look at this man and you notice he's very hairy. And he looks unkempt." 
        p "(to myself) Some strange type again.... One eats bugs and the other..." 
        p "(to myself) Okay, I'm gonna have to talk to him. I'm not gonna judge him by his looks." 
        "You're approaching a stranger." 
        show sister_img at center 
        with moveinleft 
        show mainCharacter at left1 
        with moveinleft 
        stranger "Ooh, what people! Long time no see!" 
        sister "(cheerfully) Hi there! How are you?" 
        "As always! I live and enjoy life! I decided to eat and drink as usual." 
        sister "I can see you haven't changed! That's why I found you!" 
        sister "Yeah, right, I spend a lot of time at the tavern." 
        "A wanderer notices you." 
        stranger "Who's that with you? Is he with you?" 
        p "Yes, my name is..." 
        sister "(interrupts) That's my brother. He's looking for a way out of this place." 
        "Your sister starts whispering to you." 
        sister "(whispering) It's best not to say who you are. It's safer for all of us." 
        stranger "You guys are weird. There's a way out, and you're looking for it." 
        stranger "(starting to laugh) How much have you had to drink?" 
        sister "(laughing) You're such a joker! No, no, he doesn't drink." 
        sister "We're looking for a way out of this place. \out of here." 
        stranger "(also getting serious) \"From here\" you say..." 
        stranger "Let's get out of the tavern, there's too many ears." 
        "The stranger stands up and you all leave the tavern together." 
        scene village_bg with fade 
        show stranger_img at right2 
        with dissolve 
        show sister_img at left2 
        with moveinleft 
        show mainCharacter at left3 
        with moveinleft 
        "You're standing outside a tavern. There's not a soul around you." 
        "Just the three of you and silence." 
        "The sister is starting to talk." 
        sister "So, can you help us?" 
        stranger "You must trust him a lot to ask for this." 
        sister "Yes! He saved me from a giant shadow!" 
        stranger "(surprised) Shadows?! Here?!" 
        sister "I didn't know how Shadow got here, but he saved me!" 
        stranger "(thoughtfully) Hmm... Interesting... Even I sometimes fear the giant Shadow, and he also chased it away..." 
        "After a while, the wanderer begins to speak." 
        stranger "Yes, I can help you. But the price will be great." 
        p "(confidently) I'm ready!" 
        stranger "I like your determination." 
        stranger "All right, then listen up." 
        stranger "You'll have to go to the local witch and get a letter." 
        stranger "Now, you will have to get a letter from the witch. This letter is very important to me."
        stranger "Do not open it under any circumstances!" 
        sister "(surprised) That letter?" 
        stranger "(sadly) Yes, that letter." 
        stranger "When you get the letter, bring it to me." 
        stranger "She lives in a swamp north of here. That's where you should go." 
        p "Okay, we'll head over there." 
        stranger "No, you're the only one who's going there." 
        "The nurse nods her head silently." 
        p "(surprised) Why just me?" 
        stranger "Because you're diAerent from everyone else in this world and you know it." 
        stranger "Especially in case of trouble, there's nothing Kindness can do." 
        p "What about you? You can kind of chase Shadow away - then you'll chase her away too." 
        stranger "I couldn't. Couldn't... Many times..." 
        stranger "That's what I paid for..." 
        "There was an awkward silence..." 
        stranger "I was about to go to her again, but I felt like it would be my last time... Good thing you showed up here..." 
        p "Okay, I'll do it!" 
        stranger "Just be careful. She's sneaky and can trick you like she did me." 
        sister "Be very careful! Good luck to you!" 
        p "Okay, thank you!" 
        hide mainCharacter with moveoutright 
        "You walk oA toward the swamp, leaving Kindness and the Wanderer to worry about you." 
    else: 
        scene tavern_bg with fade 
        show stranger_img at right3 
        with dissolve 
        "After a long time, you walk up to the tavern and go inside." 
        show mainCharacter at left3 
        with moveinleft 
        "It's pretty deserted inside the tavern." 
        "There are candles burning everywhere, but the tavern still feels dark and damp." 
        "The whole tavern is rotten from the outside world. It's like the whole tavern is soaked in all the horrors of this world." 
        "But you see one man sitting in the tavern." 
        "You look at this man and you notice he's very hairy. And he looks unkempt." 
        p "(to myself) Some strange type again.... One eats bugs and the other..." 
        p "(to myself) Okay, I'm gonna have to talk to him. I'm not gonna judge him by his looks." 
        "You're approaching a stranger." 
        show mainCharacter at left2 
        with moveinleft 
        p "Hey, hello!" 
        stranger "Hey, who are you?" 
        p "My name is..." 
        p "I'm looking for a way out of this place." 
        stranger "Hey, kid, are you drunk? Here's the way out, and you're looking for it..." 
        p "(embarrassed) No, no, I'm not drunk. I'm really looking for a way out of this place.... out of here." 
        stranger "(also getting serious) \"From here\" you say..." 
        stranger "Let's get out of the tavern, there's too many ears." 
        "The stranger stands up and you all leave the tavern together." 
        scene village_bg with fade 
        show stranger_img at right2 
        with dissolve 
        show mainCharacter at left2 
        with moveinleft 
        "You're standing outside a tavern. There's not a soul around you." 
        "Just the two of you and silence." 
        "You're starting to talk." 
        p "So, can you help us?" 
        stranger "You must not be an ordinary citizen of this world to ask such a thing." 
        stranger "You never told me who you were?" 
        p "(whisper) My name is [player_name] and I am the creator of this world." 
        stranger "(surprised) Wow... How did you even get here?" 
        p "Roughly speaking I got into trouble and now I'm stuck in this world that I want to get out of." 
        stranger "I see. Well, I can help you." 
        p "(confidently) I'm ready!" 
        stranger "All right, then listen carefully." 
        stranger "You'll have to go to the local witch and get a letter."
        stranger "This letter is very important to me. Do not open it under any circumstances!" 
        
        stranger "When you get the letter, bring it to me." 
        stranger "She lives in a swamp north of here. That's where you should go." 
        p "Okay, I'll head over there." 
        p "Wait. What about you?" 
        stranger "I couldn't. Couldn't... Tried many times to get that damn letter..." 
        stranger "That's what I paid for..." 
        "There was an awkward silence..." 
        stranger "I was about to go to her again, but I felt like it would be my last time..."
        stranger "Good thing you showed up here..." 
        stranger "She's sneaky and she can trick you like she did me." 
        p "Okay, I'll do it!" 
        stranger "Oh, yeah, while you're still at it. Have you seen Kindness by any chance? We were supposed to meet here..."
        stranger "For something..." 
        menu: 
            "Telling the truth.":
                "You remember leaving her alone with that Shadow... That monster..." 
                p "(with regret) Yes... Saw..." 
                stranger "Where is she?" 
                "It's hard for you to talk about it, but you still have the strength to tell the truth." 
                p "She's in the woods... She's in trouble..." 
                stranger "(worried) What?! Into trouble?" 
                p "(with regret) On the way here, I heard her screaming, and I went over there..."
                p "And I saw her being molested by a giant Shadow... But I did nothing and left..." 
                p "(sadly) I left her alone.... I chickened out!" 
                "The Wanderer's face showed that he was now overwhelmed with emotion."
                "He was in rage and in sadness, in joy and in sorrow, in resentment and in compassion..." 
                stranger "(menacingly) Oh, you!!! How dare you leave her!? You were supposed to help her!!!" 
                stranger "Get out of here! And I'll run into the woods and find her, if it's not too late..." 
                hide stranger_img with moveoutleft 
                "The traveler runs oA towards the forest, leaving you alone outside the tavern." 
                "You feel a lot of guilt for not helping her, but you're a little glad you had the courage to tell the truth." 
                "It was with these mixed feelings that you went to the witch." 
            "Lie.":
                $ liar = True 
                p "No, I haven't seen her. This forest is very huge, maybe she's somewhere in the woods." 
                "The traveler has been squinting at you. He senses you're hiding something." 
                stranger "(calmly) Okay... Well then go to the witch, I'll wait for you here." 
                p "(nervously) Okay, I'll head over there." 
                hide mainCharacter with moveoutright 
                "You walk oA toward the witch, leaving the Wanderer alone outside the tavern." 
                "The traveler is beginning to suspect you... He's beginning to guess that something's not right..." 
                stranger "Hmm. You're saying, 'This forest is really big, so maybe she's somewhere in the forest. Something's not right." 
     
    jump swamp 
 
label swamp:
    if relationship_wiseMan == -1 and relationship_sister == -1:
        scene strangerSwamp_bg with fade
        show mainCharacter at center
        "After what feels like an eternity of wandering, the trees begin to thin, replaced by a dense, oppressive humidity."
        "The air hangs heavy, thick with the smell of decay and stagnant water."
        "After a while you come to a swamp."
        "There's a bunch of stinky, dirty swamp water here."
        "You don't want to be here, but you have nowhere else to go."
        p "(to myself) Great, just great. As if things weren't bad enough already."
        "You realize you're going to have to walk through this swamp."
        "The mud sucks at your boots with every step, making a sickening squelching sound."
        "Insects buzz incessantly around your head, and the air is thick with the croaking of unseen frogs."
        p "(to myself) This is disgusting. I can practically feel the swamp clinging to me."
        "But suddenly you notice a small house in the distance."
        "It's barely visible through the mist and tangled vines, a dilapidated structure that seems to be sinking into the mire."
        "It's covered in moss and fungus. The boards are rotting and covered in mold."
        "It's like this house is about to fall apart, but something is keeping this house from falling apart."
        p "(to myself)  Is that... a house?  What's a house doing out here?"
        "A flicker of hope ignites within you, quickly followed by a surge of apprehension."
        "The house looks abandoned, possibly dangerous."
        p "(to myself) Should I go there?  It could be a trap... but what other choice do I have?"
        "You look back, the way you came is shrouded in dense fog, no way to go back, only forward."
        p "(to myself) I can't just stay here. The swamp... it feels like it's closing in on me."
        "You hesitate, weighing your options. The swamp is treacherous, and the house offers the only semblance of shelter. "
        "You realize you have no choice but to go to that house."
        hide mainCharacter with dissolve
        scene black with fade
        "You're going inside the house."
        "The air inside is even heavier, thick with a musty odor that makes you gag."
        "Every step you take echoes eerily in the silence."
        "The house is dark and you can't see anything. You try to feel for something, but nothing works."
        p "(to myself)  Can't see a thing.  Where's the door? A window? Anything?"
        "You stumble forward, your hands outstretched, feeling along the damp, crumbling walls."
        "But you feel a cool breeze blowing on you from outside, like someone opened a door."
        p "(to myself)  A draft?  Maybe there's another way out..."
        "You're starting to walk into that wind."
        scene dungeon_entry_bg with fade
        show mainCharacter at center
        with dissolve
        "You find yourself in a dungeon. More accurately, you would say a dungeon."
        "The air is cold and damp, and the only light comes from a flickering torch further down a narrow corridor."
        "You don't want to be here, you're scared, but you have nowhere else to go."
        p "(to myself)  A dungeon?  How did I get here? This is insane!"
        "You look around frantically, your heart pounding in your chest."
        "The walls are made of rough-hewn stone, and the floor is slick with moisture."
        "If you turn around, you're unlikely to find your way out in this darkness."
        "You also see that the door to the dungeon is open and there's a light on."
        p "(to myself) There's obviously someone in there. Or something..."
        "A wave of fear washes over you, but you force yourself to take a deep breath."
        p "(to myself) I have to stay calm. Panicking won't help. I need to figure out what's going on."
        "You have no choice but to go deeper into the dungeon."
        hide mainCharacter with dissolve
        scene dungeon_bg with fade
        show stranger_img at right2
        with dissolve
        "You see a stranger standing in the dungeon."
        "He's silhouetted against the torchlight, a tall, imposing figure with a wild mane of hair and a long, unkempt beard."
        "You see a stranger standing in the dungeon."
        "He's silhouetted against the torchlight, a tall, imposing figure with a wild mane of hair and a long, unkempt beard."
        "You look at this man and you notice he's very hairy. And he looks unkempt."
        p "(to myself) Some strange type again.... One eats bugs and the other..."
        "You eye him warily, trying to gauge his intentions. He doesn't seem hostile, but there's something unsettling about his presence."
        p "(to himself) You can hardly expect anything good from him."
        "You're approaching a stranger."
        show mainCharacter at left2
        with moveinleft
        p "(with fear) P... Hi..."
        "Your voice trembles slightly as you speak, the dungeon's oppressive atmosphere adding to your unease."
        "A stranger notices you and starts talking."
        stranger "Well, hello, [player_name]. I thought you weren't coming."
        p "(surprised) How do you know my name? Who are you?"
        "His words send a shiver down your spine. How could he possibly know your name?"
        "This whole situation is becoming more and more bizarre."
        stranger "It's not hard to guess who you are. We were living in peace, but at one point, the world started to rot."
        stranger "Everything in the neighborhood is dark, my house is in the swamp, and my house doesn't even look like a house anymore."
        stranger "There's a lot more of these Shadows. They've been popping up more and more lately."
        stranger "It was predictable that you'd show up here."
        "He speaks in a low, gravelly voice, his eyes fixed on you with an intensity that makes you uncomfortable."
        p "(unsure) Who are you?"
        "You press him for answers, desperate to understand what's happening."
        stranger "It doesn't matter who I am. It matters what I do."
        stranger "I've been chasing the Shadows out of the county, but now there are too many and I've started catching them and putting them in my dungeon."
        stranger "Before you came here, I had a cellar under my house, and now I have a dungeon."
        "You're getting uneasy."
        "You think of the Shadows you met on your path-they were very scary, and he, the Wanderer, is fishing them out."
        "The shadows he mentioned, you remember. Black, terrifying figures you encountered earlier."
        "The thought of this man dealing with them on a regular basis is both frightening and strangely reassuring."
        "Just the thought of him being stronger than Shadows makes you scared."
        "You steal another glance at the stranger, trying to reconcile his appearance with his words." 
        "He claims to be fighting these \"Shadows\", but he looks more like a wild hermit than a hero."
        stranger "I have an assignment for you."
        stranger "Since you are the creator of this world, you can banish these shadows. One shadow is right outside this door."
        "His words hang in the air, heavy with expectation. Creator of this world? Banish shadows? It all sounds like madness."
        p "(uncertainly) But how can I drive her away? I mean, they're scary and strong!"
        "You voice your doubts, your fear evident in your tone. You're just an ordinary person, not some kind of supernatural warrior."
        stranger "Don't be afraid, I'll be right beside you. I'll help you."
        "He offers reassurance, but his presence doesn't exactly inspire confidence."
        "Still, you're desperate, and you have no other options."
        p "(unsure) Okay, I'll give it a try."
        "You agree reluctantly, your heart pounding in your chest. "
        "You have no idea what you're getting into, but you can't just stand idly by while Shadows threaten this world… or whatever this place is."
        "You take a deep breath, trying to steel your nerves. This is it. There's no turning back now."
        jump firstCrucialChoice
 
    scene witchSwamp_bg with fade
    show mainCharacter at center
    "The air grows thick and heavy, the scent of pine replaced by a stagnant, earthy odor."
    "The ground beneath your feet becomes increasingly soggy, and the trees twist into grotesque shapes, draped with Spanish moss."
    "After a while you come to a swamp."
    "There's a bunch of stinky, dirty swamp water here."
    "You don't want to be here, but you have nowhere else to go."
    p "(to myself) Oh, fantastic. A swamp. Just what I needed."
    "You pick your way carefully through the muck, the water squelching with every step."
    "The buzzing of insects is incessant, and the air is heavy with the croaking of unseen frogs."
    p "(to myself) This is disgusting. I can feel the mud seeping into my boots."
    "You realize you're going to have to walk through this swamp."
    "The deeper you venture, the more oppressive the atmosphere becomes."
    "The trees close in around you, their branches forming a tangled canopy that blocks out most of the sunlight."
    p "(to myself) I hope I'm going the right way. This place is starting to creep me out."
    "But suddenly you notice a small house in the distance."
    "It's barely visible through the mist and tangled vines, a dilapidated structure that seems to be sinking into the mire."
    "It's covered in moss and fungus. The boards are rotting and covered in mold."
    "It's like this house is about to fall apart, but something is keeping this house from falling apart."
    p "(to myself) A house? Out here? That's...unexpected."
    "A flicker of hope ignites within you, quickly followed by a surge of apprehension."
    "The house looks abandoned, possibly dangerous."
    p "(to myself)  Should I go there? It could be a trap... but what other choice do I have?"
    p "I can't stay out here in the swamp all night."
    "You look around, hoping to see another option, but the swamp stretches endlessly in every direction, a maze of murky water and twisted trees."
    p "(to myself) No, it's no use. That house is the only chance I've got."
    "You realize you have no choice but to go to that house."
    scene witchHouse_bg with fade
    show mainCharacter at left2
    with moveinleft
    "You approach the house cautiously, your footsteps muffled by the soft ground. The closer you get, the more dilapidated it appears. The roof sags, and the windows are dark and empty."
    p "(to myself) This place looks like it's about to collapse. I hope it's safe..."
    "You're going inside the house."
    "The door creaks open with a groan, revealing a dimly lit interior."
    "The air inside is even heavier, thick with a musty odor that makes you gag."
    "You immediately smell mold and rotten boards."
    "It's as if no one has lived in the house for a long time, but you see a woman standing by the table."
    "The single room is sparsely furnished, with a rickety table, a few chairs, and shelves filled with strange jars and dried herbs."
    "A fire crackles in the hearth, casting flickering shadows on the walls."
    show witch at right2
    with dissolve
    "You immediately thought of the possibility that it might be a witch."
    "It's just like in fairy tales - a muddy swamp, an old cottage and a witch...."
    "Only she doesn't look old, she looks quite young, almost unnervingly so."
    "Her eyes sparkle with an unnatural light, and a faint smile plays on her lips."
    "She looks at you and smiles."
    w "Hello. It's been a long time since anyone has visited me..."
    "Her voice is smooth and melodic, but there's an undercurrent of something else, something that makes you uneasy."
    "You get uncomfortable with her smile."
    "You feel like she knows something about you. You can't shake the feeling that she's been expecting you."
    p "Hello... You wouldn't happen to..."
    w "(interrupting) Yes, I am a witch. You thought right."
    "She chuckles softly, her eyes fixed on yours. It's as if she can read your thoughts, anticipate your every move."
    w "And thank you for the compliment, it's been a long time since anyone called me a young woman."
    "You're a little puzzled by her words."
    "You were beginning to think you'd said every thought out loud, but you were sure you'd been silent."
    p "(to myself) How does she know what I was thinking?!"
    w "(with a smile) Silly, I read your mind. I just told you I'm a witch. I'm capable of many things."
    "You're a little shocked after she said she read your mind. A wave of fear washes over you."
    "This witch is more powerful than you initially thought."
    p "(to myself) This is bad. Really bad. I need to be careful what I think around her."
    w "So what are you doing here? There's a reason you came to this place."
    "She leans forward, her eyes boring into yours. You can feel her probing your mind, searching for answers."
    p "I came to get a letter.... A man sent me..."
    w "(grudgingly) Did that man send you?! Ahhh, I'm so sick of him!"
    w "I'm living in this swamp, putting spoils on people, and he's trying to kick me out!"
    w "He just doesn't understand the delicate balance of this ecosystem. My magic is essential to maintaining it."
    w "So I put a spell on him so he wouldn't touch me, but he still comes. He's persistent, I'll give him that."
    w "And now he's sent you here too!"
    "The witch paces back and forth, muttering to herself. She seems genuinely frustrated."
    "The witch calmed down a bit and continued talking."
    w "So... I'm giving you a chance to get out of here."
    w "You can leave and I won't do anything to you. Just go back the way you came and forget you ever saw this place."
    p "(confidently) No! He asked me for help and I can't let him down! I've come too far to turn back now."
    w "(despairingly) Well... You've made your choice. Don't say I didn't warn you."
    "The witch starts whispering something, and the air around you crackles with energy."
    "You start to feel really bad, a dizzying nausea washing over you, but suddenly you feel better."
    "The witch was very much surprised that nothing happened to you. Her eyes widen in disbelief."
    w "(surprised) How come?! What happened? Who the hell are you?!"
    p "You said you were capable of many things, but apparently you can't match me..."
    p "After all, I am the creator of this world and I can drive you away!  Or so I've been told..."
    "You try to project an air of confidence, although you're not entirely sure what you're saying."
    "You're bluffing, hoping to intimidate her."
    "The witch was surprised to have the creator of this world in her home."
    "She studies you intently, a flicker of recognition in her eyes."
    "But the second she did, she immediately calmed down and smiled."
    "A knowing smile that sends shivers down your spine."
    w "No, no, no. You can't get rid of me. Not yet, anyway."
    p "(surprised) Well, why is that?"
    w "I am part of your soul. A part you haven't yet confronted."
    w "If you destroy me, you destroy a part of yourself. And you're not ready for that, are you?"
    "There was an awkward pause.  The witch's words hang in the air, heavy with meaning."
    w "Okay. Since you're [player_name], I'll give you a letter. But not for nothing.  Everything comes at a price."
    p "You do realize you're in no position to demand anything right now."
    p "I could just leave, and you wouldn't be able to stop me."
    "You try to sound more confident than you feel."
    w "On the contrary. You are the one who is in no position to refuse my offer."
    w "After all, if you refuse, that Wanderer will be very much disappointed. He's placed his hopes on you, you know."
    w "He won't be able to live on, realizing that even [player_name] himself, the owner of this world, is helpless before me. He'll be crushed."
    "You got angry at her words and clenched your fists hard, but you knew she was right."
    "If you can't help the Wanderer, who will?"
    "By this act, you prove to yourself that you are not ready to accept yourself and leave this world."
    if liar:
        menu:
            "Agree.":
                "You realize that you've already failed the Wanderer once and you can't afford to fail him again. He's counting on you."
                "You swallow your pride and decide to take her up on her offer."
                p "Fine. What do I have to do?"
            "Refuse.":
                "You realize you've already failed the Wanderer once, but the witch's power is unsettling. If you lose, she could do terrible things to you."
                "You don't want to risk it for someone you barely know."
                p "I'm sorry, but I can't accept your offer. It's too risky."
                w "(smiling) You misunderstand. You don't have a choice. You can't just walk out of here."
                w "You can't just walk away from me like that!"
                "You wanted to leave already, but suddenly you feel your legs wouldn't obey you."
                "The witch has done something to you. A strange tingling sensation spreads through your body, and you realize you're rooted to the spot."
                p "(struggling) What have you done to me?! Let me go!"
                w "I merely persuaded you to stay. Now, we'll play my little game, and then you'll get your letter.  Whether you like it or not."
                "You realize you have to play her game and you stop resisting. "
                "You glare at her, your frustration and fear bubbling beneath the surface."

    p "Okay, I agree. What do I need to do?"
    w "(smiling) Let's play a game. A game of truth... and lies."
    "The witch holds out her hands and starts whispering something."
    "The air around her shimmers, and the room grows colder."
    "You start to feel your mind opening up, exposed. It's a deeply unsettling sensation, like being stripped bare."
    "It's like anyone can look into your eyes and read everything you think happened to you..."
    "Your deepest fears, your hidden desires, all laid bare before this enigmatic witch."
    "She stopped whispering and smiled.  Her smile is no longer playful, but something colder, more calculating."
    p "(concerned) What have you done to me?"
    w "I just learned a little something about you... It's necessary for the game. Don't worry, it's just a temporary… adjustment."
    p "And what game are we going to play?"
    w "Let's play Truth or Lies. I'll tell you some facts, some truths about yourself, and some… fabrications. You tell me if I'm lying or telling the truth."
    w "If you guess all my facts correctly, I'll give you the letter. Fail, and… well, let's just say the consequences won't be pleasant."
    p "Okay, I agree. Let's play."  
    "You try to sound confident, but your voice wavers slightly."
    jump witch_minigame
     
label returnToStranger: 
    scene village_bg with fade 
    show stranger_img at right2 
    with dissolve 

    if liar: 
        "You return to the village to see the Wanderer."
        "You spot him standing in the middle of the clearing, his arms crossed tightly over his chest."
        "His expression is dark, his jaw clenched, and his foot taps impatiently against the ground."
        "The air feels heavy as you approach, the weight of guilt pressing down on your shoulders."
        "The Wanderer’s glare cuts through you like a knife, and you realize immediately—he knows."
        show mainCharacter at left2 
        with moveinleft 
        p "Hey, I’m back…" 
        stranger "(sharply) I wish you hadn’t come back at all." 
        "His voice is low and venomous, each word laced with barely contained fury." 
        "You freeze in place, your stomach twisting into knots."
        "His anger is palpable, and it feels like it’s seeping into the air around him." 
        p "(hesitant) I… what’s wrong? Did something happen…? Did you… find my sister?" 
        stranger "(bitterly) Find her? No. The forest took her. The Shadows… they don’t give back what they take." 
        "His voice wavers slightly, the pain evident even through his anger. He turns his back to you, staring off into the distance as though searching for something—anything—that isn’t there." 
        stranger "(quietly, almost to himself) She’s gone… just like the others."
        stranger "The people this forest takes never come back." 
        "You feel the guilt hit you like a tidal wave, crashing over you and threatening to drown you."
        "You open your mouth to speak, but no words come out." 
        p "(whispering) I’m… I’m so sorry. I didn’t mean for this to happen. I was just—" 
        stranger "(suddenly screaming) I don’t want to hear your excuses!" 
        "His voice echoes through the clearing, raw and full of pain."
        "His fists are clenched so tightly that his knuckles are white, and his whole body trembles with emotion." 
        stranger "You lied to me! You lied, and because of that, she’s gone! Do you even understand what that means?!" 
        "Tears glisten in his eyes, but he refuses to let them fall."
        "He takes a deep, shaky breath before continuing, his voice quieter now, but no less filled with anguish." 
        stranger "(softly) She was the only one who cared about me."
        stranger "The only one who didn’t treat me like a freak. She… she saw me for who I was, not what I’d done. And now… now she’s gone." 
        "He turns back toward you, his eyes blazing with fury and grief."
        "He points a trembling finger at you, his voice cracking as he speaks." 
        stranger "This is your fault. You could’ve helped her, but you didn’t."
        "You chose yourself over her, and now she’s gone because of you." 
        p "(desperately) I… I didn’t mean—" 
        stranger "(cutting you off) Get out. Just… get out. I don’t want to see your face ever again." 
        "His words hit you like a physical blow, and you stagger back, your heart pounding in your chest."
        "You know there’s nothing you can say to make this right." 
        "The guilt feels like a weight pressing down on your chest, suffocating you."
        "Without another word, you turn and walk away, the Wanderer’s accusations echoing in your mind." 
        hide mainCharacter with moveoutleft 

    elif liar == False and relationship_sister == -1: 
        "You return to the village, your steps heavy with shame and regret."
        "The Wanderer is waiting for you, leaning against a wooden post, his arms crossed."
        "Kindness stands behind him, her face unreadable." 
        "The sight of her makes your heart ache with guilt."
        "Her usual warmth and light are gone, replaced by a cold, distant stare that cuts through you like ice." 
        show mainCharacter at left2 
        with moveinleft 
        p "I… I’m back." 
        p "Kindness… I’m so sorry. I didn’t mean to leave you…" 
        p "I was scared, I—" 
        stranger "(interrupting, sharply) No. You *chose* to leave her." 
        "His voice is firm and unyielding, filled with disappointment."
        "He walks forward, his eyes locked onto yours with a piercing glare."  
        stranger "You abandoned her when she needed you the most. You were too afraid to face the Shadow, so you ran."
        stranger "Don’t try to excuse it."  
        "The weight of his words strikes you like a hammer."
        "You open your mouth to respond, but the lump in your throat keeps you silent."  
        p "(with regret) I… I know I did. And I regret it more than anything."
        p "I’ve been thinking about it every step of the way… and I—"  
        "You trail off, unable to find the words to express the depth of your guilt."
        "The silence between you stretches, heavy and suffocating."  

        "Kindness steps forward, her expression as cold and distant as before. Her voice is soft, but there’s no warmth in it."  
        sister "You left me. I trusted you, and you left me. Do you know how that felt?"  
        "Her words cut deeper than you expected. You feel your breath hitch as her gaze pierces through you."  
        p "(quietly) I’m sorry… I really am. I know saying it isn’t enough, but I truly am sorry."  

        stranger "(grudgingly) At least you’re honest about it. I’ll give you that much."  
        "The Wanderer’s voice softens slightly, though the underlying anger remains. He exhales sharply, shaking his head."  
        stranger "If you hadn’t told me the truth, I wouldn’t have been able to find her in time."
        strnager "The Shadow would’ve taken her, just like all the others."  
        "His words catch you off guard."
        "Relief flickers through you, but it’s fleeting, weighed down by the guilt still lingering in your chest."  
        p "(hesitant) You… you saved her?"  
        stranger "Yes. Barely. But only because you admitted what you’d done. If you’d lied, she’d be gone by now."  
        "He looks over his shoulder at Kindness, who nods slightly in agreement, though her expression remains distant."  
        stranger "Kindness and I are angry at you."
        "You abandoned her, and that’s not something we can just forgive."
        "But… you did the right thing in the end. And for that, I’m grateful."  
        "A faint glimmer of hope flickers in your chest, but it’s quickly overshadowed by the heavy weight of your actions."  
        p "(quietly) Thank you… for saving her. I don’t deserve your kindness."  
        "Kindness doesn’t respond. Instead, she turns and walks away, heading toward the tavern without a word."
        "Her silence is louder than anything she could’ve said."  
        hide sister_img with dissolve  
        "The Wanderer watches her leave, then turns back to you with a sigh."  

        stranger "As for the letter… take it to the Wise Man. He’ll know what to do with it."  
        p "What about your curse? Don’t you need the letter for that?"  
        stranger "(gruffly) My curse is my problem."
        stranger "I got myself into this mess, and I’ll get myself out of it. It’s my responsibility, not yours."  
        stranger "(pausing) Besides, that letter… it’s connected to something much bigger than my curse."
        stranger "Something that involves this entire forest. Maybe even beyond it."  
        "His expression becomes distant, his eyes unfocused as though he’s seeing something far away."
        "His voice softens, almost to a whisper."  
        stranger "This world is changing, [player_name]. The Shadows are growing stronger, and the cracks in this place are spreading."
        stranger "That letter might hold the answers we need, but I’m not the one to find them."  
        stranger "You are."  

        p "(confused) Me? Why me?"  
        stranger "(with a small smile) Because this world is tied to you."
        stranger "Whether you realize it or not, you’re at the center of all of this. The Wise Man will help you understand."  
        "His words leave you with more questions than answers, but you nod, knowing you can’t waste any more time."  
        p "Alright… I’ll take the letter to the Wise Man. Thank you for trusting me with it."  
        stranger "(nodding) Good luck, [player_name]. You’ll need it."  
        "With those parting words, you turn and begin to walk away, the letter clutched tightly in your hand."
        "The Wanderer’s words echo in your mind, filling you with a mix of determination and unease."  
        hide mainCharacter with moveoutleft  

    else: 
        "You return to the village, and the sight of the Wanderer waiting for you fills you with a sense of relief."  
        "Standing next to him is Kindness, her warm smile lighting up the heavy atmosphere of the village."
        "The tension you carried from the swamp seems to ease slightly at the sight of their familiar faces."  
        show mainCharacter at left2 
        with moveinleft 
        p "Hi! I’m back. I got the letter."  
        stranger "(cheerfully) Here comes our hero!"  
        "The Wanderer steps forward, his hands on his hips, a wide grin spread across his face."
        "Kindness stands a little further back, her hands clasped in front of her, her expression one of quiet relief."  
        stranger "Let me see it. Did you have any trouble?"  
        p "(nodding) I had to deal with a witch in the swamp, but… yeah, I got it."  
        "You pull the letter from your bag and hold it out to him."
        "But instead of taking it, the Wanderer pauses, studying you with a thoughtful expression."  
        stranger "(serious) You know, on second thought… maybe you should keep it."  
        p "(confused) Wait, what? I thought you needed it to deal with your curse."  
        stranger "(shaking his head) No. My curse isn’t what matters anymore. I’ll deal with it myself."
        "This letter… it’s bigger than me. Bigger than my problems."  
        "He glances over at Kindness, who nods slightly in agreement."  
        stranger "I have a feeling you’re going to need this more than I ever will. Something tells me your journey is far from over."  
        p "(uncertain) What do you mean? What’s in this letter?"  
        stranger "(smiling faintly) I don’t know. But I do know that it’s connected to the Shadows, to the cracks spreading through this world. And to you."  
        p "(hesitant) To me? But why me?"  
        stranger "Because this world is tied to you, [player_name]. You’re at the center of it."
        stranger "Whether you believe it or not, you’re the one who has the power to fix it—or let it fall apart."  
        "His words send a shiver down your spine."
        "You clutch the letter tighter, feeling its weight in your hands, even though it’s just a piece of paper."  
        p "(softly) What should I do with it?"  
        sister "(gently) Take it to the Wise Man."  
        "Kindness steps forward, her voice calm and reassuring."
        "She places a hand on your shoulder, her touch warm and grounding."  
        sister "He’s strange, but he knows this forest better than anyone. He’ll be able to guide you."  
        stranger "(nodding) She’s right. The Wise Man is… well, let’s just say he’s wiser than he looks."
        stranger "He’ll know what to do with the letter."  
        stranger "(with a grin) And don’t worry about me. I’ll deal with my curse on my own. It’s my responsibility, after all."  
        p "(determined) Alright. I’ll take the letter to the Wise Man."  
        stranger "(smiling) Good. You’ve got a long road ahead of you, [player_name]. But I have a feeling you’ll do just fine."  
        sister "(softly) Be careful out there. The Shadows won’t make it easy for you."  
        "You nod, feeling a mix of determination and unease."
        "With the letter clutched tightly in your hand, you turn and begin to walk away, the Wanderer and Kindness watching you as you go."  
        "Their presence lingers in your mind as you leave the village behind, the weight of your journey pressing heavily on your shoulders."  
        hide mainCharacter with moveoutleft  

    jump returnToWiseMan

label firstCrucialChoice:
    scene black with fade
    "You go to the door and you open it."
    "You see The Shadow sitting in the corner of the room."
    "She looks at you and starts to approach you."
    "You feel fear begin to overwhelm you. You start to choke and you start to feel heavy."
    stranger "(menacingly) Get a grip, you little brat! You can do it! Chase her away!"
    "The Wanderer's voice is sharp, almost cruel, but it slices through the fog of your terror like a knife."
    p "(thoughts) What is this place... Who is she? Why does it feel like I've met her before?)"
    "The Shadow's form twists and flickers, its shape unsettlingly human yet utterly alien."
    stranger "(more insistent) Are you deaf? Move! Do something before it’s too late!"
    p "(panicked) Too late for what?! Who is she? What does she want from me?!"
    "The Wanderer doesn’t answer, his gaze locked on the Shadow with a mixture of urgency and disdain."
    "The room seems to shrink around you, the oppressive atmosphere pressing against your chest like a vice."
    "You're trying to collect your thoughts and chase the Shadow away."

    if overcoming_fears == -2:
        "You're gripped by fear and panic. You don't control your body, fear does."
        "You begin to kill The Shadow mercilessly."
        p "(screams) DIE! DIE! DIE!"
        stranger "(screams) NO! WHAT ARE YOU DOING? DON'T DO THAT!"
        "Each strike feels like a release, yet the voice in the back of your mind screams at you to stop."
        "The Shadow's eyes meet yours for a brief, agonizing moment. They aren’t filled with hatred or rage, but... sorrow."
        p "(thoughts, frantic) No, no, stop looking at me like that! You're the enemy! You have to be the enemy!"
        "The Wanderer rushes forward, grabbing your arm, but you shove him away."
        stranger "(desperately) Listen to me! You don’t understand what you’re doing!"
        p "(screaming) Leave me alone! This thing... it has to die!"
        "The Shadow collapses, her form dissolving into a black mist that swirls around your feet before vanishing."
        "The room falls deathly silent, the weight of your actions crashing down on you."
        stranger "(quietly, with anger) You killed her... You killed a part of yourself."
        p "(stammering) A... part of myself? No... that’s not true. She was... she was evil!"
        stranger "(coldly) Keep telling yourself that. You’ll find out soon enough what you’ve lost."
        "He turns his back to you, his figure fading into the shadows of the room."
        p "(whispers) What have I done...?"
        "You fall to your knees, your body trembling as guilt claws at your chest."
        jump worstEnding

    menu:
        "Destroy the shadow.":
            "You're gripped by fear and panic. You don't control your body, fear does."
            "You begin to kill The Shadow mercilessly."
            p "(screams) DIE! DIE! DIE!"
            stranger "(screams) NO! WHAT ARE YOU DOING? DON'T DO THAT!"
            "The Shadow's face twists in agony, yet something in her eyes stops you for a brief second. She looks... familiar."
            p "(thoughts) No, it’s not real. This isn’t real. She’s lying!"
            "You continue your assault, the room echoing with your screams and the Wanderer’s protests."
            stranger "(pleading) Stop this! Don’t let your fear win!"
            "But you can’t stop. The Shadow crumbles, her form disintegrating into nothingness."
            "The room falls silent, but the weight of what you’ve done lingers in the air like a suffocating fog."
            stranger "(quietly) You’ve chosen the path of destruction. I hope you’re ready for the consequences."
            p "(whispering to self) Consequences? What consequences...?"
            "The Wanderer fades away, leaving you alone with your thoughts."
            jump worstEnding

        "Chase away the shadows.":
            $ overcoming_fears += 1
            p "(muttering to self) No, I can't do that... As much as I'm scared, I can't do that..."
            "You take a deep breath, your hands trembling but steadying as you exhale."
            p "(firmly) Leave me alone! You don’t belong here!"
            "The Shadow pauses, her form flickering as though caught between this world and another."
            stranger "(surprised) You did it! You managed to drive her away!"
            "The Shadow begins to dissolve into the air, leaving behind only a faint wisp of darkness."
            "Relief washes over you, but a strange sadness lingers, as if you’ve lost something important."
            p "(to self) I did it... but... why does it still hurt?"
            stranger "(approaching) Well done. You faced your fear, and you didn’t give in. That takes strength."
            p "(hesitant) Was she... connected to me somehow?"
            stranger "(serious) Everything here is connected to you. Every fear, every regret... every mistake."
            "His words strike a chord deep within you, and for a moment, memories flicker at the edge of your mind, just out of reach."
            p "(thoughtful) Maybe... maybe I can fix this. Fix myself."
            stranger "You passed the test. I think you can definitely correct your mistakes, so I'm going to give you a letter."
            "The Wanderer pulls out a letter, its edges glowing faintly, and holds it out to you."
            p "(reaching out) Thank you... What is this letter?"
            stranger "(mysteriously) That’s for the Sage to explain. Take it to him, and you’ll understand."
            stranger "(firmly) Go back to the Sage and give him this letter. He will explain everything to you."
            p "(nodding) All right, I'll head over there."
            "You glance back at the place where the Shadow disappeared, a strange mix of pride and sorrow in your chest."
            "The Wanderer watches you quietly, his expression unreadable."
            stranger "(softly) Don’t let fear define you. You’re stronger than you think."
            hide mainCharacter
            with moveoutleft
            "You leave this strange place, leaving the Wanderer alone in the dungeon."
            jump returnToWiseMan

label worstEnding: 
    scene black with fade 
    show mainCharacter at center  
    "There is complete silence."
    "You feel nothing, hear nothing, see nothing."
    "It's like you're in a void."
    "An endless, empty expanse of nothingness."
    p "(to myself) What happened? Where am I?"
    p "One minute I was fighting the Shadow…"
    p "the..."
    p "nothing."
    p "Just this… emptiness..."
    "A cold dread creeps into your heart, a chilling sense of isolation that seeps into your very being."
    "The silence presses against you, heavy and suffocating, amplifying the chaos in your mind."
    p "(to myself) Is this death? Is this what it feels like? No… I was supposed to find my way home…"
    "Suddenly, a faint light pierces the darkness."
    "Out of the void, the Forest Spirit appears beside you, his presence a stark contrast to the surrounding emptiness."
    show forestSpirit at right2 
    show mainCharacter at left2 
    with moveoutleft 
    p "(desperate) Oh, you're finally here! Did I make it out? Am I free? Am I coming home?"
    "Hope flickers within you, a fragile flame in the vast darkness, but the Spirit's expression extinguishes it instantly."
    fs "No, you didn't get out."
    fs "I can't let you go."
    fs "You broke the fundamental law of this world."
    "His voice is cold, devoid of the usual warmth and gentleness."
    "His eyes hold a deep sorrow, but also an unwavering resolve."
    p "(at a loss for words) Why? What did I do?"
    p "I mean, I got rid of the Shadow! I saved Kindness, I…"
    fs "(interrupting) You killed her."
    fs "You extinguished the very essence of fear, a vital part of the balance of this world."
    fs "Getting rid of the Shadow is forbidden."
    fs "It represents a part of you, a part of everyone."
    fs "It cannot be destroyed."
    "His words hit you like a physical blow, shattering the fragile hope you had clung to."
    p "(pleading) I didn’t know! I thought I was doing the right thing!"
    p "She was terrifying! I had to protect myself!"
    fs "Ignorance is no excuse."
    fs "Fear is not an enemy to be destroyed but a force to be understood and tamed."
    fs "Without it, you lose part of your humanity, part of your soul."
    fs "You tipped the balance."
    fs "You destroyed the delicate thread that holds this world—and yourself—together."
    p "(frantic) I didn’t mean! I was scared! I didn’t know what else to do!"
    fs "(coldly) Fear drove you, and now fear will consume you."
    fs "You will exist here, in this black void, where there is nothing."
    fs "No light, no sound, no sensation."
    fs "Just the endless emptiness of your own making."
    "His words echo in your mind, each syllable a dagger plunging deeper into your heart."
    fs "You'll be here forever, thinking about your sins, the consequences of your actions."
    p "(hopelessly) No... No!!! This can't be happening! I don't deserve this!"
    p "I tried to do good, I…"
    fs "You tried, but your actions speak louder than your intentions."
    fs "Destruction, not creation. Fear, not courage."
    "His gaze hardens, and for the first time, you see not just sorrow, but a glimmer of anger."
    fs "You cling to the illusion of control, the belief that you could destroy a part of yourself without consequences."
    fs "You were wrong."
    "Tears stream down your face, hot against the cold emptiness that surrounds you."
    p "(desperation turning to anger) No! Don’t leave me here! I’m the creator of this world!"
    p "If you leave me here, what will happen to this world? It will cease to exist!"
    fs "What will happen to this world? THIS IS YOUR WORLD! YOU ARE IN YOUR WORLD RIGHT NOW!"
    fs "It is a reflection of your inner self, and you have made it into this desolate void."
    p "(shouting) But there’s nothing here! It’s empty!"
    fs "Exactly… By destroying the Shadow, by destroying your fear, you destroyed a vital part of yourself…"
    fs "You destroyed the very foundation of your being."
    "The Forest Spirit's form begins to flicker, fading into the darkness."
    fs "Goodbye, [player_name]… May you find peace in the nothingness you have created."
    p "(screaming) Nooooooooooooo!!!"
    "Your scream echoes through the void, swallowed by the endless emptiness."
    hide forestSpirit with dissolve
    show mainCharacter at center 
    with dissolve
    "The Forest Spirit disappears, leaving you alone in the void, alone with the chilling realization of your eternal fate."
    "You collapse to your knees, the weight of your actions pressing down on you."
    "Memories of happier times flash before your eyes—moments with loved ones, laughter, and love now distant and fading."
    p "(voice trembling) What have I done?"
    p "Why couldn't I see...?"
    "A deep sorrow wells up inside you, overwhelming and all-consuming."
    "Regret twists through your heart like icy fingers."
    "Visions of your sister's face appear in your mind, her smile now a haunting reminder of what you've lost."
    p "(whispers) I'm so sorry..."
    p "I never meant for any of this to happen."
    "Tears continue to fall, each drop a symbol of your broken spirit and the irreversible path you've taken."
    "Time loses all meaning in the void."
    "Seconds stretch into eternity as you grapple with the enormity of your choices."
    p "(desperate) There has to be a way back... I can't stay like this forever."
    "But the darkness remains unyielding, accepting your pleas without response."
    "The absence of any sign indicates that escape is impossible."
    "Your pleas fade into the nothingness, unheard and unanswered."
    "The reality of your isolation settles in, a permanent fixture in this eternal emptiness."
    "In the real world, after a car accident, you went into a coma from which you will not wake."
    "The doctors can do nothing, and the days turn into weeks, weeks into years."
    "Your sister, devastated by your loss, struggles to hold on."
    "At first, she visits you every day, talking to you, hoping for a miracle."
    "But hope fades, and grief takes its toll."
    "Unable to bear the pain, she succumbs to her sorrow, leaving this world shortly after."
    "Your family mourns, their lives forever altered by the tragedy."
    "The world continues, oblivious to your fate, the story of your life reduced to a fleeting memory."
    show screen custom_notify("You have reached the worst ending.")
    "Game over."
    "The end."
    
    return

label returnToWiseMan:
    scene bigTree_bg
    with fade
    show wiseMan at right2
    with dissolve
    "After a long journey, you have finally come to the Sage who has been waiting for your return."
    show mainCharacter at left2
    with moveinleft
    p "Hello, Sage. I'm back."
    wiseMan "Hey, [player_name]. You're back!"
    wiseMan "I can see by the look on your face that your journey has not been easy and you have realized a lot of things for yourself."
    "You remember all the events that happened to you along the way."
    p "Yes, the road was not easy..."
    p "I met many people... and faced some hard truths about myself."
    wiseMan "Tell me, what was the most difficult challenge you encountered?"
    p "That's hard to say... Perhaps it was..."
    "You pause, reflecting on your experiences."
    p "I think it was learning to forgive myself."
    p "For the mistakes I made, the people I hurt..."
    p "There were moments I wanted to give up, to turn back, but something kept pushing me forward."
    p "The weight of my past choices...{w} it felt like a heavy burden I was carrying."
    p "And then there were the people I met... some kind, some cruel."
    p "Each encounter left a mark on me."
    wiseMan "Forgiveness is indeed a powerful force, [player_name]. It seems you have learned much."
    "He smiles warmly."
    wiseMan "But you haven't answered my question yet. Did you bring me a letter?"
    p "Yes, right here."
    "You are holding out a letter to the Sage."
    wiseMan "Thank you, [player_name]. I knew you could bring me that letter."
    p "You're welcome. It wasn't easy finding it, though."
    p "I had to face some... unpleasant memories to get it."
    p "There were times I doubted myself, doubted if I could even make it this far."
    p "But I kept remembering why I started this journey in the first place."
    p "The need to understand, to find my way back... it kept me going."
    wiseMan "Indeed. The past can be a difficult place to revisit, but it holds valuable lessons for us all."
    wiseMan "And it seems you have faced those lessons head-on."
    wiseMan "The path to self-discovery is often fraught with challenges, but it is through those challenges that we grow and evolve."
    p "(uncertainly) Sage, what's in the letter? What should I do next?"
    p "I mean, all this time I've been walking, trying to find it, but I still don't understand why."
    p "Is this going to help me get home?"
    p "Is it going to tell me what happened to my sister?"
    p "I still have so many questions, so much uncertainty."
    p "I hope this letter holds some answers."
    p "Or at least points me in the right direction."
    "I feel like I'm so close, yet still so far from understanding everything."
    # If the letter's fake, he won't let us go any further # He can't let us through. He says the letter says this potion will put us out of our misery. We drink it
    if realLetter == False:
        wiseMan "Ah, yes. It says that this potion you found in an unknown house will get rid of all your troubles."
        wiseMan "You can drink it, and you'll be free of all your troubles."
        wiseMan "It promises peace, an end to the confusion and pain."
        p "(cheerfully) Wow! I didn't think it would be that easy! Goodbye, Sage!"
        p "I mean, if it's that simple… why not?"
        p "All this struggle, all this pain… maybe it's time to just let go."
        p "I hope this is the right choice."
        p "I hope this brings me the peace it promises."
        wiseMan "(sadly) Goodbye, [player_name]..."
        "You drink the potion."
        "You feel yourself starting to fall asleep and you feel yourself drifting off into the unknown."
        "A strange calmness washes over you, but it's quickly replaced by a growing numbness."
        p "(fading voice) Wait… something doesn’t feel right…"
        "Your vision blurs, and the world around you fades to black."
        jump badEnding

    "Hmm. Come follow me. I'll explain everything to you."
    "A wise man enters a giant tree, you follow him."
    p "This tree... it feels ancient. Powerful."
    p "Like it has witnessed centuries of history unfold."
    p "I can almost feel the weight of time pressing down on me as I step inside."
    wiseMan "Indeed. It is a gateway to a place of learning and growth."
    wiseMan "A place where the boundaries of reality and perception blur."
    "The air inside the tree shimmers with an otherworldly light."
    p "I feel... different. Like something is changing within me."
    p "A sense of anticipation, mixed with a healthy dose of trepidation, fills me."
    p "It’s like… my senses are heightened, yet at the same time, I feel strangely detached from my physical body."
    wiseMan "That is the magic of this place, [player_name]."
    wiseMan "Be open to its wisdom."
    wiseMan "Allow yourself to be guided by the energy that flows through this sacred space."
    p "I'll try. But...what kind of learning? What am I supposed to learn here?"
    p "I thought bringing you the letter was the end of my journey, not the beginning of something else."
    p "I'm still so confused about everything that's happened."
    p "I hope this place can help me make sense of it all."
    wiseMan "Patience, [player_name]. All will be revealed in due time."
    wiseMan "The path to knowledge is not always a straight one, and sometimes the greatest discoveries are made when we least expect them."
    wiseMan "For now, just trust in the process, and allow yourself to be open to the possibilities that lie before you."
    p "Okay, I trust you, Sage. Lead the way."
    p "I'm ready to learn whatever it is I need to learn."
    "You follow the Sage deeper into the tree, the shimmering light growing brighter with each step."
    p "It’s…beautiful. And a little intimidating, to be honest."
    p "But I have a feeling that whatever happens next, it's going to change everything."
    "You feel a sense of destiny pulling you forward."
    "A sense that you are on the verge of uncovering a truth that has eluded you for far too long."
    jump magicSchool
 
label badEnding:
    scene black with fade
    show mainCharacter at center
    "You wake up in total darkness."
    "You don't realize where you are."
    "A chilling emptiness surrounds you, pressing in from all sides."
    p "Awww... Where am I? Is anyone here?"
    "Your voice echoes in the void, unanswered."
    "A wave of nausea washes over you, and your head throbs with a dull, persistent ache."
    p "(to myself) What... what happened?"
    p "I remember...{w} the potion...{w} the witch's house..."
    "A flicker of movement in the darkness catches your eye."
    "A spectral figure, shimmering and indistinct, materializes beside you."
    show forestSpirit at right2
    with dissolve
    "The Forest Spirit gazes at you with an expression of profound sadness."
    p "Ooh, you're finally here!"
    p "Did I make it out?{w} Am I free?{w} Am I coming home?"
    "Hope flares in your chest, a desperate ember in the encroaching darkness."
    fs "No, you didn't get out..."
    fs "I don't want to make you sad, but you're dying..."
    "The words hit you like a physical blow, stealing your breath and leaving you reeling in disbelief."
    p "(at a loss for words) Wh... What? How so?"
    p "That... that can't be right."
    "Your mind races, searching for a way to deny the terrible truth, but a cold certainty settles in your stomach, heavy and inescapable."
    fs "You drank the potion you found in the house. It was a potion that would get rid of all your problems."
    fs "You failed the witch's test and she repaid you with this."
    fs "She tricked you."
    "A bitter laugh escapes your lips, choked with despair and self-loathing."
    p "(to myself) Problems... she said it would get rid of all my problems."
    p "I was so desperate, so foolish..."
    fs "She gave you a fake letter that said this potion would cure you, but it was poison."
    p "(panicked) What do I do?! What am I going to do!!"
    p "Why didn't the Sage tell me about this?"
    p "He should have known! He should have warned me!"
    "Your voice rises in a desperate plea, but the darkness offers no comfort, no answers."
    fs "Even the Sage is not omniscient. He couldn't know that the letter was fake."
    fs "He couldn't know there was poison in the potion."
    fs "Some things are hidden even from the wisest of beings."
    p "But why did the witch do this to me? If I die, she dies too."
    p "It doesn't make sense!"
    p "Why would she sacrifice herself just to hurt me?"
    "A wave of dizziness washes over you, blurring the edges of your vision."
    "You feel your strength fading, your grip on consciousness loosening."
    fs "No matter how good deeds you've done, turning away from the truth is bad."
    fs "You ran from your memories, from your responsibilities."
    fs "You couldn't accept the truth, you rejected it, and it repaid you for it."
    fs "The forest reflects your inner state, and you chose to let the darkness consume you."
    p "No... No... I just wanted to forget."
    p "I just wanted the pain to go away. Was that too much to ask?"
    "Tears stream down your face, hot and bitter."
    "Regret, sharp and piercing, claws at your heart."
    p "(to myself) My sister...{w} my friends...{w} I'll never see them again."
    p "All because I was too weak to face my past!"
    "Your chest tightens, each breath a painful struggle."
    "The darkness closes in, suffocating you with its cold embrace."
    fs "Goodbye, [player_name]... I wish it could have been different."
    "The Forest Spirit's voice fades, becoming a whisper in the void."
    "You try to speak, to apologize, to beg for another chance, but your voice is trapped in your throat."
    hide forestSpirit with dissolve
    hide mainCharacter with dissolve
    "In the real world, after an accident, you went into a coma."
    "Doctors fought tirelessly to save you, but the damage was too severe."
    "Your loved ones held vigil by your bedside, praying for a miracle that never came."
    "A week later, you died without regaining consciousness, your spirit lost to the shadows of the forest."
    show screen custom_notify("You have reached a bad ending.")
    "Game over."
    "The End."

    return
 
label magicSchool:
    scene magicSchool_bg with fade
    show wiseMan at right2
    with dissolve
    show mainCharacter at left2
    with dissolve
    wiseMan "Welcome!  I've been expecting you."
    "You step inside the tree, expecting a hollow interior, but instead, you find yourself in a vast, open space."
    "The air is warm and alive with the hum of unseen energy."
    "You go inside the tree and you see that there is a whole world inside the tree."
    "Towering trees rise towards a sky filled with swirling nebulae, and strange, glowing plants illuminate the ground with an ethereal light."
    "You don't understand how a whole world can be inside a tree."
    "It defies logic, reason, everything you thought you knew about reality."
    "You're shocked."
    "It's exciting and scary at the same time."
    "The beauty is breathtaking, but there's an underlying sense of unease, a feeling that something is not quite right."
    "You look in the distance and you see a very large building, it looks like a school."
    "A magic school."
    p "(at a loss for words) Wow... This is… incredible."
    wiseMan "Fascinating, isn't it? This is a reflection of your inner world, a manifestation of your memories, your potential, your fears."
    p "What is this place?  How is this even possible?"
    wiseMan "We've delved deeper into your inner world - your memories."
    wiseMan "This is a place where the boundaries of reality are..."
    wiseMan "fluid"
    wiseMan "A place where anything is possible."
    wiseMan "This building, this school… it's like a fortress guarding your most precious memories, the ones that shape who you are."
    "He gestures towards the school, his eyes twinkling with an ancient wisdom."
    "All you have to do is go in there. Face your memories, confront your fears. That’s the key."
    p "Stop. I just have to go in there? That's it?  It seems too… simple."
    wiseMan "Ha ha ha... It's certainly not the only thing you need to do, but it's the first step."
    wiseMan "And trust me, it won’t be as simple as you think."
    wiseMan "Once you get inside - you'll have a hard time getting out of there."
    wiseMan "The memories within those walls… they have a way of holding onto you."
    wiseMan "You’ll be tested, challenged."
    wiseMan "But through it all, you must remember who you are, and why you’re here."
    wiseMan "Are you ready for this, [player_name]?  Are you ready to face yourself?"
    p "I think so..."
    p "By the way, what about the potion? The one the witch gave me?"
    "You pull the small vial from your pocket, the liquid inside swirling with an iridescent sheen."
    p "She said it would… \"get rid of all your problems\"?"
    wiseMan "Yes. A tempting offer, isn't it? A quick fix, an easy escape."
    wiseMan "But be warned, such shortcuts often come at a steep price."
    wiseMan "When you go inside, you'll have to learn the true meaning of this potion."
    wiseMan "Its purpose, its power… and its potential consequences."
    wiseMan "So don't be in a hurry to drink it - save it."
    wiseMan "There may come a time when you truly need it, but that time is not now."
    p "Okay... I understand. I'll keep it safe. I'm ready."
    "You take a deep breath, steeling yourself for the challenges ahead."
    "The Wise Man’s words resonate within you, a mixture of warning and encouragement."
    wiseMan "Then go. I'll be waiting for you here, when you return."
    "May your memories guide you, and your courage protect you."
    hide wiseMan with dissolve
    "You are left alone at the foot of the immense school building."
    "The air hums with anticipation, and a strange energy seems to emanate from the walls, beckoning you forward."
    "You realize that the journey won't be easy, but you're ready."
    "You've come too far to turn back now."
    "You're willing to do anything to get out of this place and finally see your sister."
    "The thought of her, waiting for you, gives you strength."
    "You gaze up at the towering structure, a sense of awe and trepidation washing over you. This is it."
    "The next step on your journey, into the heart of your own memories."
    p "Well... Let's go!"
    "With a renewed sense of determination, you start walking towards the school, each step echoing in the strange, silent world."
    "The glowing plants illuminate your path, leading you towards the unknown, towards the memories that await within."
    jump schoolMemories
