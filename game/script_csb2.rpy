#CSB2 Character Definitions
define copguy = Character("CopGuy")
define arceus = Character("Arceus")

#CSB2 Character Images
image cs_neutral = "characters/cs.png"
image cs_happy = "characters/cs_happy.png"
image cs_angry = "characters/cs_angry.png"
image rich = "characters/richard.png"
image ed = "characters/ed.png"
image ed_phone = "characters/ed_phone.png"
image wesley = "characters/wesley.png"
image arceus = "characters/arceus.png"

#CSB2 Background Images
image helipad = "bg/helipad.png"
image cs_street = "bg/cs_street.png"
image jail_inside = "bg/jail_inside.png"


# The game starts here.

label csbii_start:

    scene helipad
    show cs_angry at left
    show wesley at right
    cs "You'll pay for what you did!"
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
    show ed_phone at right
    show cs_angry at left with move
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump caught

# Caught
label caught:
    cs "Dammit! Ed's calling the police! I gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    # TODO: Blue and red flashes
    "{i}The police arrive and CS runs away.{/i}"
    hide cs_angry with moveoutleft
    show ed_phone at left with move
    show copguy at right with moveinright
    copguy "Get back here!"
    cs "You can't catch me, I'm the speedy Michael Rosen!"
    "{i}As CS is not actually the speedy Michael Rosen, he gets caught by the police.{/i}"
    scene black with fade
    jump jail

label jail:
    scene jail_inside with fade
    show cs at left with moveinleft
    show copguy at right with moveinright
    copguy "Alright, welcome to the slammer. How tough are ya?"
    cs "How tough am I?! How, tough, am, I?! I beat Cuphead!"
    copguy "So?"
    cs "In under 90 minutes!"
    copguy "Hmm... okay, you're a tough enough guy to handle this cellmate, then."

    hide copguy with moveoutright
    show arceus at right with moveinright

    cs "Oh, hi Arceus."
    arceus "Aye, Boss. .w."
    cs "So what are you in for?"
    arceus "I put spyware a politician's phone."
    cs "Yeah, no, that checks out."
    arceus "And from my recent playthrough of CSBounciness, I assume you're in for beating up workers at HoHSiS."
    cs "I was 100 percent unsatisfied."
    arceus "As was I. As was I..."
    "{i}A brief moment of silence...{/i}"
    arceus "Welp, I'm bored of this place... Wanna break out? :3"
    cs "Eh.. Sure, why not, I've played plenty of the Escapists, I should be able to figure it out."
    cs "We should break out at least one other person though."
    arceus "Alright, who do ya wanna break out...?"
    cs "Let's just break out that guy next to us, I think his name was Anno..."
    arceus "Anno? Sure, he may be of use to us."
    cs "Alright then, let's get going!"

    # TODO: How to make these happen at the same time?
    hide arceus with moveoutright
    hide cs with moveoutleft
    jump breakout

label breakout:
    "Digi was tired of writing and stopped."
