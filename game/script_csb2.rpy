# NOTE: ONLY NEW DEFINITIONS ARE REQUIRED HERE
# IF THEY'RE IN CSB1, WE DON'T NEED TO REDECLARE
# TODO: [ARC] Should we have all definitions in one file?

#CSB2 Character Definitions
define copguy = Character("CopGuy")
define arceus = Character("Arceus")
define anno = Character("Anno")
define border_guard = Character("Border Guard")
define linus = Character("Linus")

#CSB2 Character Images
image ed_phone = "characters/ed_phone.png"
image arceus = "characters/arceus.png"
image arceus flipped = Transform("characters/arceus.png", xzoom = -1)
image anno = "characters/anno.png"
image border_guard = "characters/border_guard.png"
image linus = "characters/linus.png"

#CSB2 Background Images
image helipad = "bg/helipad.png"
image cs_street = "bg/cs_street.png"
image jail_inside = "bg/jail_inside.png"
image jail_cell = "bg/jail_cell.png"
image border = "bg/canadian_border.png"
image outside_tim_hortons = "bg/outside_tim_hortons.png"
image inside_tim_hortons = "bg/inside_tim_hortons.png"
image tunnel = "bg/tunnel.png"
image canada = "bg/canada.png"
image outside_ltt = "bg/linus_office_outside.png"
image inside_ltt = "bg/linus_hallway.png"

# Transitions
define determination = Dissolve(0.0)

# Animated sprites
image blue_light:
    "blue_light.png"
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat

image red_light:
    "red_light.png"
    alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat

# The game starts here.

label csbii_start:

    scene helipad
    show cs_angry at left
    show wesley at right
    cs "You'll pay for what you did!"
    n "Wesley sweats nervously."
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
    n "CS punches Wesley and knocks him out."
    show cs_angry at center with move
    play audio "audio/punch.ogg"
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show wesley at right with vpunch
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show wesley at right with vpunch
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show wesley at right with vpunch
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "victorypunch.ogg" volume 0.5
    hide wesley with easeoutright
    show cs_angry at left with move
    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at right
    show cs_angry at left with move
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump caught

# Caught
label caught:
    cs "Dammit! Ed's calling the police! I gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    show blue_light at left onlayer overlay
    show red_light at right onlayer overlay
    n "The police arrive and CS runs away."
    hide cs_angry with moveoutleft
    show ed_phone at left with move
    show copguy at right with moveinright
    copguy "Get back here!"
    cs "You can't catch me, I'm the speedy Michael Rosen!"
    stop music fadeout 3.0
    n "As CS is not actually the speedy Michael Rosen, he gets caught by the police."
    scene black with fade
    jump jail

label jail:
    scene jail_inside
    show cs_neutral at offscreenleft
    show copguy at offscreenright
    with determination
    show cs_neutral at left
    show copguy at right
    with move
    copguy "Alright, welcome to the slammer. How tough are ya?"
    cs "How tough am I?! How, tough, am, I?! I beat Cuphead!"
    copguy "So?"
    cs "In under 90 minutes!"
    copguy "Hmm... okay, you're a tough enough guy to handle this cellmate, then."

    hide copguy with moveoutright
    show arceus at right with moveinright

    play music "<loop 0>stal.mp3" volume 0.4
    cs "Oh, hi Arceus."
    arceus "Heya, CS."
    cs "So what are you in for?"
    arceus "Putting spyware on a politician's phone."
    cs "Yeah, no, that checks out."
    arceus "And from my recent debug of CSBounciness, I know that you're in for beating up workers at HoHSiS."
    cs "Your what?"
    arceus "Never mind. Why'd you do it, anyhow?"
    hide cs_neutral
    show cs_disappointed at left
    cs "I was 100 percent unsatisfied."
    arceus "As was I. As was I..."
    n "A brief moment of silence..."
    hide cs_disappointed
    show cs_neutral at left
    arceus "Welp. I'm tired of this place. Wanna break out?"
    cs "Eh.. Sure, why not, I've played plenty of the Escapists, I should be able to figure it out."
    cs "We should break out at least one other person though."
    arceus "If you say so.. Who were you thinking of breaking out?"
    cs "Let's just break out that guy next to us, I think his name was Anno..."
    arceus "Anno? Sure, I've seen what he's capable of, he may be of use to us."
    cs "Alright then, let's get going!"

    show arceus at offscreenright
    show cs_neutral at offscreenleft
    with ease
    hide arceus
    hide cs_neutral
    jump breakout

label breakout:
    scene jail_cell
    show cs_neutral at left
    show arceus at right
    with dissolve

    arceus "So, what's the plan? I've been trying to break outta here for five years."
    cs "Well, for a start. I need to get a feel of the routine here."
    arceus "I really can't stand being here another minute. I'll give you the rundown. Hasn't changed then, won't change now." 
    n "Arceus describes the prison routine to CS."
    cs "I think I got all that."
    arceus "So, what's our plan, boss?"
    cs "I gotta grab a few plastic spoons from the mess hall, a cup of molten chocolate, a guard outfit, and a change of shorts."
    arceus "Why a change of shorts?"
    hide cs_neutral
    show cs_disappointed at left
    cs "You kidding me? I'm gonna shit myself 'cause this is scary as hell."
    arceus "Fair enough."

    hide cs_disappointed
    hide arceus
    with dissolve
    scene black with fade

    stop music fadeout 3.0
    n "The current day ends, and the next one progresses. CS and Arceus gather the required essentials for their escape. Along the way, they inform Anno, who more than happily complies with the plan." 
    n "The next evening..."
    play music "<loop 0>jailescape.mp3" volume 0.5
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

    n "In the dark of the night, the three begin chipping away at their cell floor."
    n "Upon breaking through, they set up makeshift bed dummies in their beds with their prison outfits, and dawn their acquired guard outfits."

    scene tunnel
    n "They begin digging quickly, making distance away from their cells."
    cs "Jeez... I didn't think that would actually work."

    show arceus at right with easeinright
    arceus "You what?" 
    
    show anno
    anno "How are we supposed to cross the border with the new wall?"
    arceus "Not the Mexican border, the Canadian border, we're in Washington, it's way closer and they're too polite to send us back."
    cs "Works for me, free healthcare."
    arceus "Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."
    hide anno
    hide arceus
    with dissolve
    n "The three continue to dig for hours. Until their hands begin to blister and their spoons break"
    arceus "Based on my instinct and my tiredness. This should be far enough."
    n "The now escaped fugitives dig up for their ascend to the surface."
    stop music fadeout 3.0

    hide arceus with dissolve
    hide anno with dissolve
    jump bordercrossing

label bordercrossing:
    scene border with fade
    n "CS, Anno, and Arceus emerge and begin heading north towards the border crossing."
    n "A wild border guard appears."

    show border_guard at center with dissolve
    border_guard "I'm going to need proof of citizenship, eh."
    show border_guard at right with move
    show arceus flipped at left with moveinleft
    arceus "Colour is spelled with a u, eh."
    border_guard "Works for me, eh."

    hide border_guard with dissolve
    scene canada with fade 
    n "Some time passes as the party continues forth into the land of Canada."
    cs "Arceus, can we stop somewhere? I'm getting hungry."
    anno "Yeah, we've been walking for miles now."
    arceus "Guys. We've only just left the border. You can still see it behind us."
    n "The crew look behind them and still see a faint american flag waving."
    cs "Prison food just isn't all that filling."
    arceus "I suppose we could find a Tim Horton's, it's as common in Canada as a McDonald's is in America."
    n "Anno and CS nod aggresively."
    n "Arceus sniffs the air."
    arceus "There's one just over here, come on."

    scene outside_tim_hortons
    show cs_neutral at left
    cs "I'm starving after all that walking, I need a donut."
    show cs_neutral at offscreenright with move
    show arceus flipped at offscreenright with moveinleft
    show anno at offscreenright with moveinleft

    scene inside_tim_hortons
    play music "<loop 0>timmies.mp3"
    show cs_neutral at left with moveinleft
    show arceus flipped at center with moveinleft
    show anno at right with moveinleft

    anno "Finally."
    hide anno
    hide cs_neutral
    with dissolve

    show arceus flipped at left with move
    show cashier at right with moveinright

    # TODO: Room flower shop music here

    arceus "Hi."
    cashier "Can I help you?"
    arceus "Yeah, can I have a dozen glazed donuts please?"
    cashier "Oh hi, Arceus, I didn't know it was you."

    hide cashier
    hide arceus flipped
    show anno
    anno "Wait, huh?"

    hide anno
    show arceus flipped at left
    show cashier at right

    cashier "Here you go."
    arceus "That's me!"
    arceus "How much is it?"
    cashier "It'll be $18.{nw}"
    arceus "Here you go! Keep the change."
    arceus "Hi doggy!"
    cashier "You're my favorite customer."
    arceus "Thanks a lot! Bye~"
    hide arceus flipped with moveoutleft
    cashier "Buh-bye!"
    hide cashier with dissolve

    # TODO: Music stops.

    show cs_disappointed
    cs "..."
    cs "I think I'm {i}really{/i} sleep deprived."

    scene inside_tim_hortons with fade

    show cs_neutral
    show anno at left
    show arceus at right

    n "CS, Arceus, and Anno enjoy some well-deserved donuts."
    arceus "Sorry to interrupt you two, but we may have a problem: Those donuts cost me the last of my money. We are going to need to find a way to make some cash."
    scene outside_ltt
    n "CS looks across the street to see Linus Media Group."
    hide cs_neutral
    hide arceus
    hide Anno

    scene inside_tim_hortons
    show cs_neutral
    cs "A media group, huh? I have a lot of video editing experience, maybe I can get a job there."

    scene black with fade
    stop music fadeout 3.0
    n "CS walks into the studio to ask for a job."

    scene inside_ltt
    show linus
    with fade
    play music "<loop 0>linusmeetup.mp3" volume 0.5
    linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
    cs "Colour is spelled with a u, eh."
    linus "I need actual papers, the last time I hired someone who used that as proof of citizenship I got fined and had to sell one of my thousands of RTX Titans."
    cs "Ummmm, I'll be right back."
