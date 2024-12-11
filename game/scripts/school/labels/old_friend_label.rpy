   
label old_friend_dialogue:

    $ hide_screens()
    with fade

    if "Ask for notes from an old friend" in current_tasks:
        of "Hi! How long has it been? How are you doing?"
        p "Hi! Yeah, long time no see. I'm good, how are you?"
        of "I'm doing okay, too. I heard you wanted to ask for my help. How can I help you?"
        p "Yes, I'd like to ask you for help. I would like to ask you for help with my studies."
        p "You probably already know that we have a big music quiz coming up."
        p "And I'd like you to lend me your music notes so I can study for the test."
        p "Because I'm not ready for it yet and I don't know what to do. I didn't take much notes in class."
        p "Can you help me, please?"
        of "Of course I'll help you. But not for nothing, of course"
        p "What do you mean? You won't even give me, your old friend, your notes for nothing?"
        of "Of course I will, but I'd like to go out and hang out together."
        of "We've been socializing very little lately, so I'd like to go out."
        of "A reminiscence of an old day, so to speak"
        menu:
            "Accept":
                "You remember that you really haven't talked in a while and you'd love to spend time with him"
                "You realize that if you agree, he will help you and you will improve your relationship with him"
                p "Yeah, why not?"
                p "We really haven't been anywhere in a long time."
                p "Let's go out and the tapes can wait for a while."
                p "I think we're gonna have a good time together."
                of "(smiling) I'm glad you said yes!"
                "You realize you don't have much time left to study for a test"
                "But, besides the music test, you'll have two other tests in other subjects."
                "At the same time, you realize that you made the right choice because you improved your relationship with your friend"
                "And sometimes relationships are more important than studying"
                jump walkWithOldFriend
            "Refuse":
                $ old_friend_relationship -= 1
                "You remember that you really haven't talked in a while and you'd love to spend time with him"
                "But you realize you don't have much time left to study for a test"
                "But, besides the music test, you'll have two other tests in other subjects."
                "You decide to turn down your friend's offer after all, since you're running out of time"
                p "I'd love to go out with you, but I have a test coming up."
                p "We can take a rain check after the tests."
                p "There will still be plenty of time to walk around"
                of "(sadly) I'm sorry you said no. But I realize you need the notes and you have a test to study for."
                of "I hope we can meet another time"
                of "And hopefully we'll still be able to go out another time"
                p "Yes, absolutely!"
                "An old friend reluctantly hands you the notes"
                "You can see by the look on his face that he's not very happy that you refused to take a walk"
                "You realize that you made things worse with him by doing this, but you can fix it another time after all the scrutiny."
                $ remove_task("Ask for notes from an old friend")
                if "BookBrown" not in [item[0] for item in inventory_items if item]:
                    $ add_to_inventory(*notes_items["BookBrown"])
                if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
                    $ add_task("Come to the classroom teacher")
                
    else:
        n "I'm a little busy right now."

    hide old_friend
    hide mainCharacter
    with fade
    jump mainSchoolLoop


label walkWithOldFriend:
    $ goForAWalk = True
    $ old_friend_relationship += 1
    "You came to the park"
    "The sun is shining. A faint but warm breeze is blowing."
    "You're reminiscing about the old days"
    of "(with a smile on his face) Eh, remember those very young days when we skipped our last classes?"
    of "When we were at the park playing catch-up on the playground."
    of "We ran and jumped on the slides, climbed trees and crawled in the sandbox"
    of "Ha-ha-ha-ha, those were fun times."
    "You think back to that money and you almost have tears coming after those warm memories"
    "You're thinking to yourself that you didn't skip class for nothing."
    "Those warm memories were worth it"
    P "(smiling) Yeah. Those were the good ole days."
    p "You make it sound like you're in your 60s, ha ha ha ha."
    of "Ha ha ha. Well, when this was all happening. It was first grade"
    of "Then the teachers also complained to our parents that we were two bullies and skipping school"
    p "Yeah, I've been there. I got in a lot of trouble after that"
    of "Ha ha ha, I didn't feel good about it either after all the complaints from teachers"
    of "But we can't afford it now"
    of "After all, we're all grown up now."
    of "And now we don't have time to skip class."
    of "If you miss one lesson now, it will take a few days to learn and understand what was covered in that class"
    p "Uh-huh. That's right..."
    "You further carry on the conversation by talking about the past and recalling both good and bad moments"

    with fade
    scene field_bg
    with fade

    "You were so engrossed in talking and reminiscing about the past that you didn't notice that the environment around you had somehow changed"
    "You look around and realize you've been here before. Only you can't remember where or when you've been here."
    "Like you've been here a while."
    "You remember that field, that smell of flowers, that lush and soft grass under your feet"
    of "(gasps) You remember this place?"
    "You got goosebumps after saying that."
    "From your friend's mouth comes a different voice, not at all familiar to you"
    "You realize it wasn't your friend who said that"
    of "You still can't remember? You've been here before"
    "You abruptly remember that you woke up in this world right here, in this very field."
    p "How is that possible? We were just in the park!"
    p "And how did we end up back in the field anyway? Isn't this place outside of this building?"
    of "We're in the memories. Since you've been here before, you remember this place, so I can show you this field."
    of "I can show you all your memories"
    # Поочерёдно показывает все воспоминания
    p "(frightened) Who are you or what are you?"
    of "I am your memories"
    p "And why did you show me all this?"
    p "What do you want from me?"
    of "I don't need anything from you. I am your memories"
    of "I'm just collecting and keeping all the memories in you"
    p "Then why are you talking to me?"
    p "You're not talking to me because you just want to talk to me."
    of "That's right. And you're a smart guy, and you always have been."
    of "You're looking to get out of this world, you want to get out of this world."
    of "You still want to see your loved ones, don't you?"
    "You, without thinking, answer him."
    p "Yes! I do!"
    of "Oh, that's great. The only thing you need is a yellow-red potion."
    of "You should know what I'm talking about"
    of "You've already heard about this potion from someone."
    "You remember that your art teacher told you about this potion before."
    "She said that 'by drinking this potion, a person can understand and realize themselves'"
    p "Was it you then? Did you use her voice to talk about the potion?"
    of "You're a smart one."
    "You also remember that the teacher made you look bad afterward."
    "She made you look like a fool, just like your sister."
    p "But you shouldn't have made me and my sister look like fools, it was unnecessary"
    of "Yes, I apologize, that was unnecessary."
    p "What do I have to do to get this potion?"
    of "You need to gather all the ingredients for the potion"
    of "The most important and basic material you already have is the red potion"
    of "It's different from what you'll have to get, but it doesn't matter"
    of "(speaking to himself) It's a good thing you didn't drink that potion, or it would have been bad..."
    p "What? What did you say?"
    of "No, it's nothing"
    of "The rest of what you'll need is this: FruitGreen, RoseWhite and PotionGreenBlue"
    p "And where are these items located? How am I supposed to get them?"
    of "You just have to be yourself."
    of "If you accept your past self, your future self will be happy about it"
    p "Sounds... Weird."
    of "I do, but I've said all I'm gonna say."
    of "Good luck to you! I hope you make it through!"
    with fade
    $ update_background()
    with fade
    "You came back"
    of "Oh yeah, here's the footage you asked for. Hopefully we'll get to go out like this again."
    p "Thanks for the walk and for the notes! Yes, it will definitely work out!"
    if "BookBrown" not in [item[0] for item in inventory_items if item]:
            $ add_to_inventory(*notes_items["BookBrown"])
    if check_inventory_for_items(required_books) and "Come to the classroom teacher" not in current_tasks:
        $ add_task("Come to the classroom teacher")
    jump mainSchoolLoop
