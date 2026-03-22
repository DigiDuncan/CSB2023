######## INTRO ########
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
    # For now we'll use this I guess
    scene bus_stop

    # it's mike in the background, working at the bus stop! lmao
    if fun_value(FUN_VALUE_LEGENDARY):
        show mike at manual_pos(0.8, 0.6, 0.5):
            zoom 0.5
            block:
                linear 0.5 xzoom -1
                linear 0.25 ypos 0.55
                linear 0.25 ypos 0.6
                linear 0.5 xzoom 1
                linear 0.25 ypos 0.55
                linear 0.25 ypos 0.6
                repeat

    show cs disappointed at left
    show arceus angry at right
    with dissolve
    pause 0.5

    n "CS notices that Arceus has barely said anything the entire time."
    cs "Hey, Arc, are you alright?"
    arceus "No, I am not."
    arceus "My feet hurt, I'm exhausted, and I'm honestly pissed that you just kept wanting to go west."
    arceus "There was literally {w=0.25}nothing {w=0.25}{i}there."
    arceus "Do you, like, lack object permanance or something?"
    arceus "Did you {i}seriously{/i} think that something new would happen if you kept doing the same thing over and over again?"
    if fun_value(FUN_VALUE_COMMON):
        show cs surprised
        cs "Well, I mean, technically, it {i}did-- {nw}"
        show cs scared
        arceus "Now,{w=0} you shut the God damn fuck up {i}right now{/i} or so help me,{w=0} God." with vpunch
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

    show arceus angry at manual_pos(0.6, 0.625, 1.0):
        linear 1.0 zoom 0.4
    with MoveTransition(1.0)

    show cs disappointed
    cs "Yeah, I think I will, too."

    show cs disappointed at manual_pos(0.4, 0.625, 1.0):
        linear 1.5 zoom 0.4
    with MoveTransition(1.5)

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
    $ collect("runaway_bus")
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
    pause 2.0

    ######## ON THE BUS ########
        
    play sound sfx_ambiance_bus_interior loop fadein 2.0
    play sound2 sfx_csnore loop fadein 2.0
    play music sleeping_room loop fadein 2.0 if_changed
    scene bus_seat
    show cs happy flipped at manual_pos(0.6, 1.0, 1.0):
        rotate 5
    show arceus asleep flipped at manual_pos(0.9, 1.0, 1.0):
        rotate -10
    with Dissolve(2.0)
    music sleeping_room

    n "The moment they sit down, CS and Arceus fall into a deep sleep."

    camera:
        matrixcolor duskmatrix
    with Dissolve(2.0)
    
    n "The bus comes and goes from Bellingham International Airport..."

    camera:
        matrixcolor darkmatrix
    with Dissolve(2.0)

    n "...{w=0} eventually passing state lines into California."

    stop music fadeout 2.0
    stop sound fadeout 2.0
    stop sound2 fadeout 2.0
    scene black with Dissolve(2.0)
    camera:
        matrixcolor IdentityMatrix() # resets shader
    pause 2.0

    ######## WAKE UP ########

    play music apple_kid fadein 2.0 if_changed
    play sound2 sfx_csnore loop fadein 2.0
    scene bus_seat
    show cs happy at manual_pos(0.7, 1.0, 1.0):
        rotate 15
    show arceus asleep flipped at manual_pos(0.8, 1.0, 1.0):
        rotate -15
    with Dissolve(2.0)
    music apple_kid

    n "A few hours later, the bus finally comes to a stop."
    show kappn at manual_pos(1.2, 0.7, 0.5) with determination
    show kappn at manual_pos(0.9, 0.7, 0.5) with MoveTransition(1.0)
    kappn "Arright, fellas. End o' the line."
    show arceus flipped with { "master": dissolve }
    arceus "Hmmgh?"
    kappn "Ye, welcome te San Franciscer!"
    kappn "If'n ye're here fer the beach, ye'd better wake yer friend up an' get outta 'ere 'fore it gets too crowded!"
    arceus "Beach...? San... {nw}"
    show arceus asleep flipped with { "master": dissolve }
    extend "mmm..."
    pause 1.0
    "..."
    pause 1.0
    kappn "... Aye, lad?"
    pause 3.0
    show arceus worried flipped
    arceus "{i}San Francisco?!" with vpunch
    arceus "CS! Wake up!"
    show cs concentrate
    cs "Hnnngh..."
    cs "{size=-12}But, Mommy, I don't {i}wanna{/i} go to school..."
    show arceus angry flipped:
        linear 1.0 xpos 0.75
    n "CS pulls Arceus closer as if he were some sort of body pillow."
    arceus "{i}CS!" with vpunch
    arceus "Get offa me!"
    play sound sfx_punch_alt
    show arceus angry:
        linear 0.1 xpos 0.725
        linear 0.1 xpos 0.75
    stop sound2
    show cs scared
    cs "{cshake}YEOWCH!!" with hpunch
    n "Arceus elbows CS in the stomach."
    cs "What was {i}that{/i} for?!"
    arceus "Dude, get {nw}"
    extend "{i}off!" with vpunch
    cs "Shit, sorry!"
    show cs happy
    cs "You're just so soft and fluffy!"
    arceus "Yeah, and my {i}future {/i}{nw}"
    extend "{i}wife{/i} would agree with you!" with vpunch
    arceus "Now, fuckin' lemme {nw}"
    show cs scared
    extend "{i}go!" with vpunch
    show cs disappointed
    cs "Right, sorry."
    show cs disappointed:
        parallel:
            linear 0.5 rotate 0
        parallel:
            linear 0.5 xpos 0.6
    show arceus angry:
        parallel:
            linear 0.5 rotate 0
        parallel:
            linear 0.5 xpos 0.9
    pause 2.0
    cs "Oh, hey, Mr. Driver. Are we at the airport?"
    show arceus worried
    arceus "Dude, {i}no!{/i} We fucked up!"
    arceus "We're in {i}California!"
    show cs scared
    cs "What?!" with vpunch
    kappn "That's right! Welcome te sunny Californ{w=0.1}-I{w=0.05}-A!"
    cs "{i}Shit!{/i} We were supposed to get off at the airport in Bellingham!"
    cs "Do you think you can take us to the nearest airport?"
    kappn "No can do, lad! Ol' gal's almost outta fuel!"
    show cs disappointed
    show arceus worried flipped
    arceus "What should we do?"
    kappn "Well, if'n ye take this here map, I reckon ye can find another bus real easy-like."
    kappn "But, if'n ye're not in any kind o' hurry, ye shoul' take a gander 'round the city!"
    kappn "When ye firs' got on me bus, the two of ye looked more stressed out 'an two sea urchins at a sushi parlor!" # foreshadowing is a literary device in whi--
    kappn "An' I thought to meself, \"I dunno what 'ey're in town fer, but I'm sure glad to be takin' 'em some'ere {i}else!\""
    arceus "I guess, yeah, we {i}were{/i} pretty stressed..."
    show cs surprised
    cs "And we're not {i}really{/i} in any hurry to get home..."
    show cs
    cs "I even feel pretty great today."
    show arceus
    arceus "Hey, me too, actually."
    show cs happy
    show arceus happy
    kappn "Well, I'd be surprised if ye {i}didn't!"
    kappn "The two of ye slept like scallops fer the las' 16 hours!"
    show cs scared
    show arceus worried flipped
    cs "16 hours?!" (multiple=2) with vpunch 
    arceus "16 hours?!" (multiple=2) with vpunch 
    scene black with dissolve
    pause 1.0
    n "CS and Arceus deboard the bus and start walking."
    pause 2.0

    scene valencia_st
    show cs disappointed at left
    show arceus worried at right
    with dissolve
    cs "Well, {i}now{/i} what?"
    arceus "Let's check out the map, I guess?"
    # TODO: map item
    show cs surprised
    arceus "All I know is that when Pakoo and Mika came here on vacation last year, they told us that the airport here is {i}insane.{/i}"
    arceus "We'll probably want to wait until, like, 2 AM to even step foot in there."
    show cs disappointed
    cs "Yikes, good idea."
    cs "At least that'll give us the whole day to look around..."
    show arceus
    arceus "Yeah. So, where to?"
    show cs happy
    cs "Let's find out together!"
    show cs at mid_mid_left
    show arceus at mid_mid_right
    with MoveTransition(0.5)
    # TODO: raise map up
    show cs surprised
    pause 1.0
    
    # TODO: get real map music

    call screen beach_overworld_map(
        current_time = "dawn",
        current_location = (1109, 531, "Valencia & 20th"),
        left_hand = "arc", 
        right_hand = "cs", 
        jump_points = [ 
            (500, 690, "Ocean Beach", "beach.beach_dawn"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_dawn"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_dawn"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_dawn")
        ]
    ) 
    with dissolve

######## ENDING ########
label beach_end:
    scene black with dissolve
    "The day is over, so you get on a plane to New York or something, idk, none of this is written yet."

    ### achievement checks
    # TODO: achievement names/descriptions/thumbnails are not final
    python:
        # unlock achievement for completing this once
        achievement_manager.unlock("californication")

        # unlock for seeing all possible choices
        if "beach_bum" not in persistent.unlocked_achievements:
            # TODO: fix this to reflect changes in location list
            locations_list = [ "beach", "boardwalk", "downtown", "park"]
            times_list = ["dawn", "day", "noon", "dusk", "night"]
            beach_labels_list = []

            # construct the list of labels because fuck you if you think i'm doing this by hand
            for l in locations_list:
                for t in times_list:
                    next_value = "beach." + l + "_" + t
                    beach_labels_list.append(next_value)

            # compare this list to the labels we've seen
            count_seen = 0
            for bl in beach_labels_list:
                if renpy.seen_label(bl):
                    count_seen = count_seen + 1

            persistent.beach_routes_seen = count_seen

            if persistent.beach_routes_seen == len(beach_labels_list):
                achievement_manager.unlock("beach_bum")

    "Maybe you unlocked an achievement or two here."
    "Returning to main menu."

    return
