# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#CSB1 Character Definitions
define cs = Character("cs188")
define craptop = Character("Craptop")
define sticky = Character("Sticky Note")
define carguy = Character("Car Guy")
define greeter = Character("Greeter")
define doug = Character("Doug")
define cashier = Character("Cashier")
define ycs = Character("Young CS")
define hoh_operator = Character("HoH SiS Operator")
define rich = Character("Rich")
define ed = Character("Ed")
define wesley = Character("Wesley")
define worker_1 = Character("Worker 1")
define worker_2 = Character("Worker 2")

#CSB1 Character Images
image cs_neutral = "characters/csocola.png"
image cs_happy = "characters/csocola_happy.png"
image carguy = "characters/carguy.png"
image doug = "characters/ceo.png"
image cashier = "characters/cashier.png"
#image ycs = "characters/young_cs"
image rich = "characters/richard.png"
image ed = "characters/ed.png"
image wesley = "characters/wesley.png"
image worker_1 = "characters/corn_worker"
image worker_2 = "characters/corn_worker"

#CSB1 Background Images

image cs_room = "bg/cs_bedroom1.png"

# The game starts here.

label start:

    scene cs_room
    show cs_neutral
    cs "Welp, time to start up the ol' Craptop."

    return
