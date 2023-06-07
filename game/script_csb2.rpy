#CSB2 Character Definitions
define copguy = Character("CopGuy")
define arceus = Character("Arceus")
define anno = Character("Anno")

#CSB2 Character Images
image cs_neutral = "characters/cs.png"
image cs_happy = "characters/cs_happy.png"
image cs_angry = "characters/cs_angry.png"
image rich = "characters/richard.png"
image ed = "characters/ed.png"
image ed_phone = "characters/ed_phone.png"
image wesley = "characters/wesley.png"
image arceus = "characters/arceus.png"
image arceus flipped = Transform("characters/arceus.png", xzoom = -1)
# image anno = "characters/anno.png"

#CSB2 Background Images
image helipad = "bg/helipad.png"
image cs_street = "bg/cs_street.png"
image jail_inside = "bg/jail_inside.png"
image border = "bg/canadian_border.png"


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
    cs "Your what?"
    arceus "Never mind. Why'd you do it, anyhow?"
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
    # scene jail_cell
    # TODO: inside cell BG

    show cs at left with dissolve
    show arceus at right with dissolve

    arceus "So, what's the plan? I've been tryna break outta here for 5 years."
    cs "Well, for a start. I need to get a feel of the routine here."
    arceus "Well, I'll quickly describe that for you, cause I can't stand another minute here." 
    "{i}Arceus describes the prison routine to CS.{/i}"
    cs "I think I got all that."
    arceus "So, what's our plan, Boss?"
    cs "I gotta grab a few plastic spoons from the mess hall, a cup of molten chocolate, a guard outfit, and a change of shorts."
    arceus "Why a change of shorts?"
    cs "You kidding me? I'm gonna shit myself 'cause this is scary as hell."
    arceus "Fair enough."

    hide cs with dissolve
    hide arceus with dissolve
    scene black with fade

    "{i}The day ends, and the next day progresses. CS and Arceus gather the required essentials for their escape. Along the way, they inform Anno, who more than happily complies with the plan.{/i}" 
    "{i}The next evening...{/i}"
    cs "Key, check."

    show arceus flipped at left with moveinleft
    arceus "Uniforms, check."

    show anno at right with moveinright
    anno "Spoons, check."

    show cs_neutral at center with dissolve
    cs "Extra shorts..."
    cs "Check."
    cs "Alright men, let's get the heck out of here!"

    scene black with dissolve

    # TODO: Guys, can we actually detail the escape a *little* bit?
    "{i}The plan goes off without a hitch, the three ditch their prison outfits, and put on their guard uniforms.{/i}" 


    "{i}The three dig their way out of the cell and make a break into the dark of the evening.{/i}"
    cs "Jeez... I didn't think that would actually work."

    show arceus at right with easeinright
    arceus "You what?" 
    
    show anno
    anno "How are we supposed to cross the border with the new wall?"
    # TODO: Are we in New York?
    arceus "Not the Mexican border, the Canadian border, we're in New York, it's way closer and they're too polite to send us back."
    cs "Works for me, free healthcare."
    arceus "Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."

    hide arceus with dissolve
    hide anno with dissolve
    jump bordercrossing

label bordercrossing:
    scene border with fade
    "God, typing all this sucks."
