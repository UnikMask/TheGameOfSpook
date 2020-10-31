# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom morning

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

    return
