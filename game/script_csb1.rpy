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
define rich = Character("Richard")
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
image worker_1 = "characters/corn_worker.png"
image worker_2 = "characters/corn_worker.png"

#CSB1 Background Images

image black = "bg/black.png"
image cs_room = "bg/cs_bedroom1.png"
image cs_room_2 = "bg/cs_bedroom2.png"
image craptop_desktop = "bg/Craptop_Desktop.png"
image craptop_update = "bg/Craptop_Updating.png"
image craptop_car = "bg/craptop_car.png"
image craptop_edit = "bg/craptop_edit.png"
image craptop_error = "bg/Craptop_error.png"
image craptop_yt = "bg/craptop_ytp"
image cs_house = "bg/Cs_house.png"
image cs_car = "bg/car_driveway.png"
image cs_car_inside = "bg/car_inside.png"
image walmart_outside = "bg/Walmart_Outside.png"
image walmart_inside = "bg/walmart_inside.png"
image walmart_aisle = "bg/walmart_shelf.png"
image walmart_register = "bg/walmart_checkout.png"
image cs_door_closed = "bg/door_closed.png"
image cs_door_open = "bg/door_open.png"
image hoh_hq = "bg/office1.png"

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
    carguy "You should try Crotch Doctor!"
    cs "OH GOD AN ADVERTISER!!!"
    cs "QUICK START THE CAR START THE CAR!!!"
    hide carguy
    # TODO: Transition, door slam
    show cs_car_inside behind cs_neutral
    cs "Whew.. That was close!"
    cs "Should I go get groceries?"
    menu:
        "Get groceries?"
        "Yes":
            cs "Yeah... It's a good idea to get some stuff."
        "No":
            cs "Screw you, I'm going anyway!"
    scene walmart_outside
    show cs_happy
    cs "Oh yes! Walmart is open!"
    scene walmart_inside with fade
    "{i}CS walks inside{/i}"
    show doug at right with moveinright
    greeter "Hello and welcome to Walmart! Can I help you with anything?"
    show cs_neutral at left with moveinleft
    cs "Wow! It's Walmart CEO Doug McMillon! You actually work here?"
    doug "Of course! They were short a greeter today, so I filled in the slot!"
    cs "Wow! He seems like a good man!"
    hide doug with moveoutright
    show cs_neutral at center with move
    cs "Now. Lets find some food!"
    show walmart_aisle behind cs_neutral with dissolve
    cs "*pop* Noice! Genergy is 2 for $5! I'll take them all!"
    cs "Oooh! Pringles are on sale too! Yoink!"
    "{i}CS walks to checkout.{/i}"
    show walmart_register behind cs_neutral with dissolve
    show cs_neutral at left with move
    show cashier at right with dissolve
    cs "Here's my stuff!"
    cashier "That'll be $11.88."
    cs "Here you go!"
    cashier "Have a good day."
    cs "You too, bye!"
    hide cashier
    show walmart_outside behind cs_neutral with dissolve
    cs "Let's get to the car."
    show carguy at right with moveinright
    carguy "Nooooot so nice scratch."
    cs "Not you again!"
    cs "I gotta get outta here!"
    hide carguy
    # TODO: Transition, door slam
    show car_inside behind cs_neutral
    cs "Let's get home before that guy doctor's my crotch!"
    show black with fade
    "{i}CS drives home and manages to avoid reenacting one of his favorite car crash videos.{/i}"
    scene cs_room
    "{i}CS arrives home and walks to his room.{/i}"
    show cs_happy with dissolve
    cs "Ahhh. It's good to be home!"
    show cs_neutral
    hide cs_happy
    cs "You know, I haven't put out a YTP in a while. I should work on one of my in-progress ones."
    show craptop_edit with fade
    "{i}CS walks to his craptop and opens up Premiere.{/i}"
    cs "Ooooh! Here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    "{i}CS watches the in-progress video.{/i}"
    cs "This is pretty good, but I am feeling uninspired... I don't know where to go from here..."
    cs "..."
    cs "I know! Should watch some other YTPs for inspiration"
    show craptop_yt
    hide craptop_edit
    "{i}CS opens up YouTube and begins watching YTPs. After a while, CS runs into some old YTPs.{/i}"
    cs "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now..."
    cs "..."
    cs "Oh look a flashback. What a coincidence..."
    scene cs_room with pixellate
    show young_cs with moveinbottom
    ycs "Hey guys! Young CS here! Today I'm gonna be editing a craaaaAaAAaAAAAAaaAazy video!!"
    "{i}keyboard tapping{/i}"
    ycs "Ohhhhhh YeeEeeEeEeeEEeEEs! This is lookin' good!"
    hide young_cs
    scene cs_room with pixellate
    show cs_neutral
    cs "Oh, flashback over."
    "{i}A loud crash can be heard as though an atom has split in CS' foundation.{/i}"
    cs "Woah! I was dreaming so long that the foundation fell apart. My house just fell to the side!"
    cs "I really need to get some foundation repair."
    cs "Better call HoH SiS!"
    cs "They are really good at giving me the JoJ!"
    cs "{i}Dials 1-800-HoH-SiiS{/i}"
    cs "Hello? Can you give me the JoJ?"
    hoh_operator "Is this a prank caller on the line?"
    cs "No! My house really needs foundation repair! I need your help ASAP!!"
    hoh_operator "Alright. That will be 200,000 bits. You can pay us afterwards."
    hoh_operator "{i}hangs up{/i}"
    cs "Well that is one thing taken care of."
    cs "I guess I'll work on my new YTP while I wait."
    scene black with fade
    "{i}Time passes and the doorbell rings{/i}"
    scene door_closed with fade
    show cs_happy with moveinbottom
    cs "Oh they're here!"
    cs "Let me go get the door.."
    show door_open behind cs_happy
    cs "Hello! I am cs188 and I-"
    show cs_neutral
    hide cs_happy
    show cs_neutral at left with move
    show ed at right with moveinright
    ed "Alright that will be 200,000 Bits."
    cs "Okay, I guess they already told you what I need done.. Lemme get my wallet..."
    cs "Hang on a sec. Didn't they say I could pay afterwards?"
    ed "Yeah well, corporate policies just changed 5 seconds ago. Pay up."
    hide cs_neutral with moveoutleft
    "{i}A few moments later...{/i}"
    show cs_neutral at left with moveinleft
    cs "Here you go! I'll get out of you guys' hair while you work."
    hide cs_neutral with moveoutright
    "{i}CS leaves after paying 200,000 Bits.{/i}"
    ed "Come on in, guys, CS left."
    show ed at left with move
    show wesley at center with moveinright
    show rich at right with moveinright
    ed "So now that we're here, what should we do to him?"
    "Ed, Wesley, and Richard" "Hmmm..."
    wesley "Let's go check his room. We might get some ideas."
    show cs_room behind ed with dissolve
    "{i}The three HoH SiS workers go upstairs.{/i}"
    wesley "Wow I didn't know CS had a Union Jack!"
    ed "CS sure loves those Brits~!"
    wesley "Alright, but now what should we do?"
    ed "How about we burn down his house!"
    wesley "Eh..."
    rich "How about we mess with his laptop?"
    ed "Alright! Let's get sabotagin'!"
    show craptop_desktop with dissolve
    "{i}Ed launches the craptop{/i}"
    ed "Heheh... he won't know what hit him..."
    wesley "Quickly! Let's get out of here before he comes back!"
    show craptop_update
    wesley "Hurry up!"
    "..."
    show craptop_error
    scene cs_house
    show ed at left with moveinbottom
    show wesley at center with moveinbottom
    show rich at right with moveinbottom
    rich "Lemme call our JoJ UFO."
    # TODO: Beaming up animation
    "Ed, Wesley, and Richard" "I'm beaming up!"
    hide ed with moveouttop
    hide wesley with moveouttop
    hide rich with moveouttop
    scene cs_street
    show cs_neutral with moveinleft
    cs "Things sure are boooooring around here..."
    cs "I should check on the HoH SiS folks. They should be making some progress by now."
    scene cs_room
    show cs_neutral with moveinbottom
    "{i}CS walks into his room.{/i}"
    cs "What?! They're gone?!"
    cs "The house is still on the side, and my computer is messed up!"
    cs "I need to get those guys!"
    cs "I'm gonna go to HoH SiS HQ and kick some butt!"
    show black with dissolve
    "{i}...{/i}"
    scene hoh_hq
    show cs_neutral with dissolve
    cs "Alright! Where are the head JoJites?!"
    show worker_1 at right with moveinright
    worker_1 "I don't know!!"
    cs "BullShisH!"
    cs "{i}CS punches the worker.{/i}"
    hide worker_1 with moveoutright
    show worker_2 at right with moveinright
    worker_2 "They--... They're on the roof!!"
    cs "Good!!"
    "{i}...{/i}"
    show black with dissolve
    "Arceus proceeds to have a stroke as his wrists scream out in agony from typing the entirety of CSB1"
    jump csbii
