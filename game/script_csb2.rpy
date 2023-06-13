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
    play sound "audio/punch.ogg"
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

# Chop
label chop:
    show cs_angry at left
    show wesley at right
    cs "Hiya!"
    n "CS chops Wesley in the chest and he flies off the roof."
    show cs_angry at center with move
    play sound "audio/chop.ogg"
    hide wesley with easeoutright
    show cs_angry at left with move
    cs "I sawed this foundation repairman in half!"
    show ed_phone at right
    show cs_angry at left with move
    ed "Hello, 911? My coworker just got karate chopped by a disgruntled customer off the roof! Send help!"
    jump caught

# Kick
label kick:
    show cs_angry at left
    show wesley at right
    $ renpy.movie_cutscene("movies/kick.ogv")
    hide wesley with easeoutright
    show cs_angry at left with move
    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at right
    show cs_angry at left with move
    ed "Hello, 911? My coworker just got kicked by a disgruntled customer off the roof! Send help!"
    jump caught

# Special
label special:
    show cs_angry at left
    show wesley at right
    n "CS uses his YTP magic to make the foundation repairman fight eachother."
    hide wesley at right
    play sound "audio/punch.ogg"
    rich "Hey! Cut it out!"
    play sound "audio/punch.ogg"
    wesley "I'm not trying to fight! I don't know what is happening help!!"
    play sound "audio/punch.ogg"
    rich "Ed! Do something!"
    play sound "audio/punch.ogg"
    show ed at right
    ed "Hello, 911? My coworkers are-"
    n "CS sentence-mixes Ed's words to his own will."
    ed "Everything is fine here officer. No need to come here."

# Caught
label caught:
    cs "Dammit! Ed's calling the police! I gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    play sound "siren.ogg" loop
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
    stop sound fadeout 1.0
    scene black with fade
    jump jail

label jail:
    scene jail_inside with fade
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
    music stal - C418
    cs "Oh, hi Arceus."
    arceus "Heya, CS. .w."
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
    play music "<loop 0>moongazer.mp3" volume 0.5
    music Moongazer - Dr. Awesome
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
    # If anyone asks, Arceus is part god and can dig really easily, I guess.
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
    n "The three continue to dig for hours, until their hands begin to blister and their spoons break."
    arceus "Based on my instinct and my tiredness. This should be far enough."
    n "The now escaped fugitives dig up for their ascent to the surface."
    stop music fadeout 3.0

    hide arceus with dissolve
    hide anno with dissolve
    jump bordercrossing

label bordercrossing:
    scene border with fade
    play music "<loop 0>onett.mp3" volume 0.6
    music Onett Theme - Earthbound
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
    scene flag
    play music "star_spangled_banner.mp3"
    n "The crew look behind them and still see a faint American flag waving."
    scene canada
    stop music
    play music "<loop 0>onett.mp3" volume 0.6
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
    stop music fadeout 3.0

    scene inside_tim_hortons
    play music "<loop 0>buy_something.mp3" volume 0.6
    music Buy Something Will Ya! - Earthbound
    show cs_neutral at left with moveinleft
    show arceus flipped at center with moveinleft
    show anno at right with moveinleft

    anno "Finally."
    hide anno
    hide cs_neutral
    with dissolve

    show arceus flipped at left with move
    show cashier at right with moveinright

    # TODO: [DIGI] Room flower shop music here

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
    stop music fadeout 3.0
    # TODO: Music stops.

    show cs_disappointed
    cs "..."
    cs "I think I'm {i}really{/i} sleep deprived."

    scene black with fade
    pause 1.0
    scene inside_tim_hortons
    play music "<loop 0>buy_something.mp3" volume 0.6
    show cs_neutral
    show anno at left
    show arceus at right
    with fade

    n "CS, Arceus, and Anno enjoy some well-deserved donuts."
    arceus "Sorry to interrupt you two, but we may have a problem: Those donuts cost me the last of my money. We are going to need to find a way to make some cash."
    scene outside_ltt
    n "CS looks across the street to see Linus Media Group."
    hide cs_neutral
    hide arceus
    hide Anno

    scene inside_tim_hortons
    show cs_neutral
    cs "Linus Media Group, huh? I have a lot of video editing experience, maybe I can get a job there."
    stop music fadeout 3.0

    scene black with fade
    n "CS walks into the studio to ask for a job."

    scene inside_ltt
    show linus
    with fade
    play music "<loop 0>passport.mp3" volume 0.5
    music PASSPORT.MID - George Stone
    linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
    cs "Colour is spelled with a u, eh."
    linus "I need actual papers, the last time I hired someone who used that as proof of citizenship I got fined and had to sell one of my thousands of RTX Titans."
    cs "Ummmm, I'll be right back."

    scene outside_ltt
    show arceus at right
    with dissolve
    show cs_neutral at left with moveinleft

    cs "Arc, what am I gonna do? They need proof I'm legal to work."
    arceus "Hmmm..."
    n "A lightbulb goes off in Arceus' head."
    arceus "Leave it to me."
    hide arceus with moveoutright

    scene alley
    show arceus flipped with moveinleft

    n "Arceus rummages around in the dumpsters behind LMG."
    arceus "Hnng...{w} hmmpmh... {w}aha!"
    n "Arceus finds an old laptop."
    arceus "Perfect."
    n "Within minutes, Arceus has edited the governement records to set CS' file as having a valid work visa."
    arceus "Nice."
    n "Arceus rummages around the dumpster more and finds a magnet from a old CRT."
    n "He places it against the laptop, destroying the hard drive instantly."
    arceus "Without a trace."
    n "He discards both items and rushes out of the alley."

    hide arceus flipped
    show arceus
    hide arceus with moveoutleft

    scene outside_ltt
    show cs_neutral at left
    show arceus at right with moveinright

    arceus "All taken care of."
    cs "What did you do?"
    arceus "Don't worry about it. Just have them look you up."

    scene black with fade
    scene inside_ltt
    show linus
    with fade

    linus "I didn't think you could have a number as a last name..."
    linus "Yep, there you are, cs188, full working visa."
    linus "Looks like you're hired!"
    cs "Ohhh yes! {w}{i}ahem{/i} I mean, thank you, Linus!"

    scene inside_tim_hortons
    show anno at right
    show arceus flipped at left
    show cs with moveinleft

    cs "I did it, I got the job!"
    anno "Woohoo!"
    arceus "Hell yeah!"

    anno "Let's celebrate!"
    n "CS, Anno, and Arceus cheers their donuts together."
    stop music fadeout 3.0
    scene black with fade
    jump csbiii_start
