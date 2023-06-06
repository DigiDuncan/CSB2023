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

image black = "bg/black.png"
image cs_room = "bg/cs_bedroom1.png"
image cs_room_2 = "bg/cs_bedroom2.png"
image craptop_desktop = "bg/Craptop_Desktop.png"
image craptop_update = "bg/Craptop_Updating.png"
image craptop_car = "bg/craptop_car.png"
image cs_house = "bg/Cs_house.png"
image cs_car = "bg/car_driveway.png"
image cs_car_inside = "bg/car_inside.png"

# The game starts here.

label start:

    scene cs_room
    show cs_neutral
    cs "Welp, time to start up the ol' Craptop."
    hide cs_neutral
    scene craptop_desktop
    craptop "Your PC sux. lol."
    sticky "Delete the CSCord."
    cs "Eh, maybe tomorrow."
    scene craptop_update
    craptop "Downloading update 200/13..."
    craptop "Update complete."
    cs "OoOoOoOoO yes!"
    scene craptop_car
    cs "Time to watch car crash videos for the next couple of hours!"
    show black with fade
    "{i}Two hours later...{/i}"
    scene cs_room
    show cs_neutral
    cs "Okay... What to do now?"
    cs "I could go outside, look at some flowers.."
    show cs_room_2 behind cs_neutral
    hide cs_room
    cs "Oh! Look out the window! There's a Michael Rosen!"
    hide cs_neutral
    show cs_happy
    cs "Yeah! Let's go outside!"
    scene cs_house
    show cs_happy
    cs "Nice day!"
    hide cs_happy
    show cs_neutral
    cs "Well, I guess it's car time."
    show cs_car behind cs_neutral
    hide cs_house
    show cs_neutral at left with move
    show carguy at right with moveinright
    carguy "Nice car!"
    cs "It's pretty nice, but it's got some scratches..."
    carguy "Nooot so nice scratch.."
    carguy "You should try crotch doctor!"
    cs "OH GOD AN ADVERTISER!!!"
    cs "QUICK START THE CAR START THE CAR!!!"
    hide carguy
    show cs_car_inside behind cs_neutral
    cs "Whew.. That was close!"
    cs "Should I go get groceries?"
    return
