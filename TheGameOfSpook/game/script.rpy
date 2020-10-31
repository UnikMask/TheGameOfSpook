# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("You")
define a = Character("Amex-kun")
define e = Character("Ewan")
define unknown = Character("???")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom morning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Today is haloween!"

    "I have been waiting for this day for ages now, and it has finally come."

    "Indeed, where I live, halloween is widely considered as the most important day of the year."

    p "Woah! It's already 7am! I need to run to school!"

    "I quickly jump in my trousers, dive in my T-shirt, and exit my bedroom to the living room."

    "Suddenly..."

    # This ends the game.

    jump scene3

label scene2:


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

    a ""

    a ""

    "An awkward pause. Amex-kun's smile suddenly disappears into a smug, looking at me. His tone shifts radically"

    p "So... Now that I know you are interested, let me ask you a most crucial question."

    a "What is it, Amex-tan?"

    p "You see, there are more than just one card..."

    p "Take the blue card, and we will be sailing the winds of American Express into the unknown."

    p "Take the red card, and you will stay here. However, do not expect nothing to change this time."

    a "I don't know, darling... Which one should I chose?"

    p "What is your choice?"

    menu:

        "Take the blue card":
            jump blue

        "Take the red card":
            jump red


label refuse:

    a "Sorry, I cannot take this..."

    p "Nah, I understand man... "

    pause 1

    "Maybe you'll get it next time we meet!"


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

    e "Welcome to Stacshack 2021 everybody!"

    e "I\'m Ewan, your school president, and this year this competition is sponsored by American Express!'"

    e "Please welcome our 2 American Express representatives Amex-kun, aaand..."

    p "Quick, love, tell them your name!"

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
 #   jump therevelation
