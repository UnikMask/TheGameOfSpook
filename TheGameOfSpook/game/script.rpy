# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("You")
define a = Character("Amex-kun")
define e = Character("Elen")
define ew = Character("Ryan Gibb")
define unknown = Character("???")
define s = Character("Skelly-san")
define f = Character("Female student council president")
define j = Character("John Honey-San")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $elen_aff = 0
    $amex_dude_aff = 0
    $fem_stu_co_aff = 0
    $male_stu_co_aff = 0
    $male_teacher_aff = 0
    $skelly_san_aff = 0

    scene bedroom morning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "Today is haloween!"
    "I have been waiting for this day for ages now, and it has finally come."
    "Indeed, where I live, halloween is widely considered as the most important day of the year."
    p "Woah! It's already 7am! I need to run to school!"
    "I quickly jump in my trousers, dive in my T-shirt, and exit my bedroom to the living room."
    "Suddenly..."
    show elen skot
    e "Hello sleepy, you have to hurry up, we're almost late for school!"

    menu:
        "What do I say?"

        "How- how did you get into my room?!":
            e "I climbed in the window silly."
            "I sigh. She does this way too often."
            p "You need to stop doing that you know."
            e "Yeah yeah, sure. Now hurry up or we'll be late!"

        "Elen, you need to stop climbing through my window.":
            $elen_aff += 5
            e "But why would I do that?? You'd miss school every day you know."
            "I sigh. She does this way too often."
            p "Fine."


    hide elen scot
    scene school morning
    "This is the school that Elen and I have been to since I can remember, which is strange since it's only a high school..."
    "It's quite boring. I can't remember anyone enough to introduce them. It feels like every day is my first..."
    jump scene2


label scene2:
    scene classroom skelly

    #Dialogue

    "Its the first class of today and I'm so excited because its with Skelly-san!"

    show skellysan

    menu:
        "Greet Skelly-san":
            p"Good morning Skelly-san, how are you today?"
            $skelly_san_aff += 2
            s"Hello!! I'm doing very well today, how kind of you to ask. Such a wonderful student you are."
            s"Was your weekend any good?."

            menu:
                "Make an excuse to sit down":
                    p"Actually my feet hurt from the walk to school, so I'm going to go sit down before class starts"
                    s"Oh ok, that's a good idea! You better sit down to make sure you don't hurt yourself any further! It's better tibia safe than sorry"

                "Continue with the conversation":
                    $skelly_san_aff += 1
                    p"It was pretty boring, but I did enjoy the homework you set! It was really interesting to answer the riddles about all the different bones you have in your body"
                    s"Oh really? I'm glad you enjoyed it, I hoped that you'd find it humerus"
                    s"Speaking of bones, I have a great joke for you, do you want to hear it?"

                    menu:
                        "Yes":
                            $skelly_san_aff += 1
                            s"What's a skeleton's favorite type of plant?"
                            s"A bone-zai tree!"
                            p"...haha"
                            s"HAHAHAH, jokes are great, I love them. They're a great way to start your day!"
                            s"It was lovely to chat with you but class is about to start so you should get to your seat"
                            s"And can you be a dear and turn on the heater for me while you're at it. I'm practically chilled to the bone."
                            menu:
                                "Turn on heater":
                                    $skelly_san_aff += 3
                                    p"Sure thing!"
                                    "That's such a weird way to phrase being cold... I hope she's not getting sick"
                                "Go straight to your seat":
                                    "That's such a weird way to phrase being cold... I hope she's not getting sick"
                        "No":
                            s"Oh ok, lovely having a chat, you better head to your seat now, class is about to start"



        "Ignore Skelly-san":
            s "Oh, are you not in the mood to talk to me today. That's ok! Why don't you take a seat, class is about to start soon"

    hide skellysan

    "Today feels like a good day! I hope nothing bad happens."

    show femstuco

    "Oh, that's the female student council president. Together with the male student council president, they are the ultimate duo."
    p "Good morning, how was your weekend?"
    f "It was enjoyable. I had a fibula-ous time studying with the student council president"
    f "I've come to realise that his jaw line is a pleasure to look at. It just sends shivers down my spine every time"
    "Ok...those are some weird things to say but good for her I guess"
    p"Um, that's interesting to know.."
    f"Yes it is, but I better not catch you looking at him or I will have a bone to pick with you."

    scene black
    with fade
    jump scene3


label scene3:
    scene canteen
    "It's now lunch time. I could try sitting down with Elen, but she's sitting with her skelly friends. I don't want to invade her space..."
    "Instead, I decide to sit down on a corner of the canteen, alone."
    "As I eat my ribs, however, a shady figure comes up to me, hand in his suit pockets"
    show amexkun
    unknown "Ahoy there young lad! Having a hard time eating? Ain't got the stomach?"
    p "Who are you?"
    unknown "First time someone had the guts to ask me that! But again who has any around these regions."
    unknown "Call me Amex!"
    p "Alright, Amex-kun... So... Do you want anything?"
    a "Now, lad, I'm not here to ask for anything, I \'m only here to ask you..."
    a "If you are interested into an American Express account opened!!"
    a "Enjoy many benefits on supermarkets, booked flights, and restaurants worldwide, on up to $25,000.00 per year in purchases!"
    "His voice and his looks... They are... Charming. I can't manage to take my eyes off of him."
    "And this card he's talking about... It's benefits are so life-changing! Yet something seems so.. Immoral in accepting his offer..."
    a "You've been pretty silent there... I do have to say, and I have the guts to say it..."
    "He blushes"
    a "I would like to perhaps know you a bit more?"
    "This feeling that we both are meant for each other... I cannot shake it off! Like the whole world is going to crumble if I refuse!"
    a "So... Do you want this American express card?"
    show amexcard
    with dissolve
    "If I chose to take this card, I will enjoy so many benefits... But would that really give me happiness?"
    menu:
        "Accept the American Express card":
            jump accept
        "Refuse the American Express card":
            jump refuse


label accept:
    show amexkun
    with dissolve
    p "Your eyes, your looks, your suit, your elegance, your card... They make me shiver down my spine!"
    a "And what is that supposed to mean?"
    p "I love you Amex-kun!! I know we haven't met for long, but with you, I feel something I never felt before!"
    a "So..."
    p "I accept your card, Amex-kun!!!"
    "Amex-kun suddenly stutters, surprised. He might not have expected this answer. Suddenly a big smile appears up his face."
    a "I have been feeling the same... This makes me so overjoyed!"

    pause 5

    "An awkward pause. Amex-kun's smile suddenly disappears into a smug, looking at me. His tone shifts radically"
    a "So... Now that I know you are interested, let me ask you a most crucial question."
    p "What is it, Amex-tan?"
    a "You see, there are more than just one card..."
    a "Take the blue card, and we will be sailing the winds of American Express into the unknown."
    a "Take the red card, and you will stay here. However, do not expect nothing to change this time."
    p "I don't know, darling... Which one should I chose?"
    a "What is your choice?"

    menu:
        "Take the blue card":
            jump blue
        "Take the red card":
            jump red


label refuse:
    p "Sorry, I cannot take this..."
    a "Nah, I understand man... "
    pause 1
    "Maybe you'll get it next time we meet!"
    jump scene4


label blue:
    p "I choose the blue card!"
    "Amex-kun's face suddenly comes back to this irresistible smile"
    a "I knew you would make the right decision! Come here my love!"
    "Amex-kun embraces me."
    scene black
    with fade
    pause 1
    "And as I leave the school with him, one hand with my amex card, and the other with Amex-kun's hand, we say goodbye,"
    "one last time,"
    "to this amazingly spooky school."
    pause 3
    "4 months later"
    ew "Welcome to Stacshack 2021 everybody!"
    ew "I\'m Ewan, your school president, and this year this competition is sponsored by American Express!'"
    ew "Please welcome our 2 American Express representatives Amex-kun, aaand..."
    a "Quick, love, tell them your name!"
    python:
        povname = renpy.input("My name is ")
        povname = povname.strip()
        if not povname:
            povname = "John Smith"
    p "My name is [povname] !!"
    pause 1
    return



label red:
    "Amex-kun pauses..."
    pause 10
    p "Wrong answer lad..."
    p "But maybe the color red really fits you in the end..."
    return


image bg classroom = "images/classroom.jpg"
image john Honey-San = "images/JohnHoneyCrop.png" #credit
label scene4:


    "That guy was weird, I've never seen him here before he must be new"

    "I better get to my next class now I don't want to be late!"

    scene bg classroom
    show john Honey-San
    "*Enters Classroom*"

    j "Good afternoon class, please be seated, I expect this to just be a normal lesson, we will not be celebrating Halloween in my classroom"

    "What?? how could someone not like Halloween? It's the best day of the year!"

    j"Today we will be taking another break from your course to talk about why you should invest in the new crypto currency I have developed - AmCoin"
    p "But sir why don't you like halloween?"
    j"halloween is just a stupid holiday for stupid children to harass respectable members of society and beg for candy"
    j"Besides what is the point of celebrating the paranormal when it doesn't exist"

    j"Now as I was saying before I was so rudely interupted"
    j"Many notable people have already invested in Amcoin, such as myself, they are clever enough to see -"
    "Spooky noises from outside the classroom*"
    hide john Honey-San
    "*John Honey-San leaves to check what happened*"
    "Classmate: \"Quick whilst he's gone everyone run!\""
    menu:
        "leave with everyone":
            "I better get out of here whilst I still can"
        "stay behind":
            p"I better stay behind I don't want to get into trouble"
            show john Honey-San
            "*John Honey-San returns, confused about where everyone went*"
            j"Oh you're still here, well you might aswell leave like everyone else now"
            menu:
                "leave":
                    p"okay, see you next class"
                "stay behind":
                    p"No it's okay I have something I wanted to talk to you about"
                    j"oh? what is it?"
                    p"I thought I'd tell you a Halloween joke to help show you that Halloween can be alot of fun"
                    menu:
                        "Whats a ghost's favourite dessert?":
                            p"I-Scream!"
                            j"Do you think that it's funny to laugh at someone who is lactose intolerant?"
                            j"get out of my class."
                        "What does a skeleton order at a restaurant?":
                            p"Spare Ribs!"
                            j"ahaha thats funny maybe we should go to a restaurant tonight then if you'd like"
    jump scene6



label scene6:

    scene restaurant
    show elen skot
    with fade
    p "{i}Wow, I can't believe I'm really on a date with Elen...{/i}"
    menu:
        "What should I say?"

        "How was school?":
            e "It was boring."
            p "{i}That didn't tickle her funny bone...{/i}"

        "What are you doing for Halloween?":
            e "I'm going as a skeleton! It's so cool, there's this haunted house and everything..."
            p "{i}That seemed to really tickle her funny bone...{/i}"
            $elen_aff += 5

    p "{i}Maybe I should tell a joke.{/i}"
    menu:
        "Which joke do you want to tell?"

        "Why don't they play music in skeleton church?":
            e "I don't know, why don't they?"
            p "Cause they don't have any organs!"
            e "OMG that's amazing LMAO."
            $elen_aff += 5

        "What do you call two witches that live together?":
            e "I don't like witches..."
            p "Broom-mates! Get it, room-mates but witches use brooms!"
            e "..."

    p "{i}Well, this night has gone well so far, but it's getting late.{/i}"
    menu:
        "What do you say?"

        "Have a spooky Halloween! If you want to get candy you'd better start trick-or-treating now.":
            e "Good idea! I need to show off my costume!"
            $elen_aff +=5

        "We should go now, it's getting late.":
            e "Why, you don't want to hang out with me anymore??"
            p "No, that's not what I meant! I'm sorry!"

    p "Well, that was a nice evening, I'm really happy I got to spend time with you."
    e "Yeah, me too... UwU"

    scene black
    with fade
    pause 2
    jump start
