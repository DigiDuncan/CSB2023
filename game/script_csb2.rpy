#CSB2 Character Definitions
define copguy = Character("CopGuy")

#CSB2 Character Images
image cs_neutral = "characters/cs.png"
image cs_happy = "characters/cs_happy.png"
image cs_angry = "characters/cs_angry.png"
image rich = "characters/richard.png"
image ed = "characters/ed.png"
image ed_phone = "characters/ed_phone.png"
image wesley = "characters/wesley.png"

#CSB2 Background Images
image helipad = "bg/helipad.png"
image cs_street = "bg/cs_street.png"


# The game starts here.

label csbii:

    scene helipad
    show cs_angry at left
    show wesley at right
    cs "You'll pay for what you did?"
    "{i}Wesley sweats nervously."
    wesley "Do you want a refund?"
    cs "I'll refund your face to the floor!"
    hide cs_angry
    hide wesley

    menu:
        "What attack would you like to use?"
        "Punch":
            jump punch
        "Chop":
            jump chop
        "Kick":
            jump kick
        "Special":
            jump special

# Punch
label punch:
    show cs_angry at left
    show wesley at right
    cs "Take this!"
    # TODO: Punch animation
    "{i}CS punches Wesley and knocks him out.{/i}"
    hide wesley with easeoutright
    cs "That'll teach you not to miss with a nerd's computer!"
    hide cs_angry
    show ed_phone at right
    show cs at left with move
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump caught

# Caught
label caught:
    cs "Dammit! Ed's calling the police! I gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    # TODO: Blue and red flashes
    "{i}The police arrive and CS runs away.{/i}"
    hide cs with moveoutleft
    show copguy at right with moveinright
    copguy "Get back here!"
    cs "You can't catch me, I'm the speedy Michael Rosen!"
    "{i}As CS is not actually the speedy Michael Rosen, he gets caught by the police.{/i}"
