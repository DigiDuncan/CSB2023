label beach_start:
    play music happy_roaming volume 0.5 if_changed
    scene washington_road day
    show cs at left
    show arceus angry at right
    with dissolve
    music happy_roaming

    pause 0.5
    show cs surprised
    cs "You know, Arc..."
    cs "I saw a bus stop a little ways back."
    cs "Think it goes to anywhere cool?"
    arceus "If it'll keep you from going west again, I guess it's worth a look..."
    show cs happy
    cs "Great! Let's check it out!"
    window hide
    show cs happy flipped
    hide cs with moveoutleft
    pause 0.5
    show arceus angry at offscreenleft with MoveTransition(1.0)
    pause 0.5

    scene black with dissolve
    pause 0.5

    n "About an hour later, the two arrive in Bellingham."
    pause 0.5

    # TODO: need bg of a bus stop in Bellingham. I wonder if greyfade can get me one...
    scene

    # it's mike in the background, working at the bus stop! lmao
    if fun_value(FUN_VALUE_LEGENDARY):
        show mike at manual_pos(0.8, 0.5, 0.5):
            zoom 0.5
            block:
                linear 0.5 xzoom -1
                linear 0.25 ypos 0.45
                linear 0.25 ypos 0.5
                linear 0.5 xzoom 1
                linear 0.25 ypos 0.45
                linear 0.25 ypos 0.5
                repeat

    show cs disappointed at left
    show arceus angry at right
    with dissolve
    pause 0.5

    n "CS notices that Arceus has barely said anything the entire time."
    cs "Hey, Arc, are you alright?"
    arceus "No, I am not."
    arceus "My feet hurt, I'm exhausted, and I'm honestly pissed that you just kept going west."
    arceus "There was literally {w=0.25}nothing {w=0.25}{i}there."
    arceus "Do you, like, lack object permanance, or something?"
    arceus "Did you {i}seriously{/i} think that something new would happen if you kept doing the same thing over and over again?"
    if fun_value(FUN_VALUE_COMMON):
        show cs surprised
        cs "Well, I mean, technically, it {i}did-- {nw}"
        show cs scared
        arceus "Now you shut the goddamn fuck up right now or so help me God-- {nw}" with vpunch
        show cs disappointed
    arceus "How long ago, exactly, did you even {i}notice{/i} this bus stop?"
    show cs worried
    cs "Uh... {w=0.5}{nw}"
    show cs scared
    extend "maybe... {w=0.5}{nw}"
    show cs happy
    extend "don't worry about it!"
    cs "The important part is that we're here {i}now!"
    cs "We don't have to walk anymore!"
    show cs
    cs "That's better now, right?"
    arceus "No?"
    show cs disappointed
    arceus "What the {nw}"
    extend "{i}fuck?!" with vpunch
    arceus "We've been out here for {i}days,{/i} and it all could have been {i}avoided!"
    arceus "From now on, {nw}"
    show cs worried
    extend "{i}I'm{/i} calling the shots!" with vpunch
    arceus "{i}You{/i} {nw}" with vpunch
    extend "will be following {nw}"
    extend "{i}me!" with vpunch
    show cs disappointed
    cs "Fine, okay. We'll try it your way."
    cs "What {i}is{/i} your way, then, anyway?"
    arceus "This bus should take us to an airport."
    arceus "We are taking the {i}first{/i} flight back to New York."
    arceus "As soon as {i}your{/i} ass is home safe and sound, {i}I'm{/i} getting an Uber to the nearest hotel and taking a fucking {nw}"
    extend "{i}nap!" with vpunch
    cs "I thought you hated flying."
    arceus "Oh, {i}believe{/i} me, I {i}do."
    show cs worried
    arceus "You wanna know what {i}else{/i} I hate?"
    show cs scared
    arceus "Walking along an empty road in the middle of buttfuck {nw}"
    extend "{i}nowhere!" with vpunch
    cs "Okay, okay! I get it!"
    show cs disappointed
    cs "I'm sorry!"
    cs "Your plan sounds solid. How long until the bus gets here?"
    show arceus angry flipped at mid_offscreen_right with move
    n "Arceus checks the timetable."
    pause 1.0
    arceus "Looks like it should be right around the corner."
    show cs
    cs "Oh, nice. We got here just in time, then!"
    show arceus angry
    arceus "I'm gonna sit down. My feet are killing me..." # but are they feet or paws?

    show arceus angry at manual_pos(0.8, 0.8, 1.0):
        linear 0.75 zoom 0.75
    with MoveTransition(0.75)

    show cs disappointed
    cs "Yeah, I think I will, too."

    show cs disappointed at manual_pos(0.4, 0.8, 1.0):
        linear 1.0 zoom 0.75
    with MoveTransition(1.0)

    pause 2.0
    "..."
    pause 1.0
    show arceus worried
    pause 2.0
    arceus "Hey, uh..."
    arceus "I'm sorry for snapping at you."
    cs "Eh, don't worry about it."
    cs "You weren't wrong. I should have listened way earlier."
    show cs
    cs "At least that crab was pretty cool."
    show arceus
    arceus "Yeah, I guess it was."
    arceus "Wonder what a crab needs a pen for, though."

    show runaway_bus at manual_pos(2.2, 1.3, 1.0):
        block:
            linear 0.1 ypos 1.25
            linear 0.1 ypos 1.3
            repeat

    n "Before the two can ponder the crustacean's intentions further, the bus arrives, right on schedule."

    play sound sfx_car_approach_stop volume 5.0 fadein 2.0
    pause 2.0
    show runaway_bus at manual_pos(1.0, 1.3, 1.0):
        linear 0.1 ypos 1.25
        linear 0.1 ypos 1.3
        repeat
        time 2.0
    with MoveTransition(2.0)
    stop sound
    pause 3.0

    hide arceus
    hide cs
    with dissolve

    play sound sfx_driving
    show runaway_bus at manual_pos(-1.0, 1.3, 1.0):
        linear 0.1 ypos 1.25
        linear 0.1 ypos 1.3
        repeat
    with MoveTransition(3.0)
    pause 1.0
    scene black with Dissolve(2.0)
    stop sound fadeout 2.0
    stop music fadeout 2.0
    music end


    "Placeholder line. Returning to main menu."
