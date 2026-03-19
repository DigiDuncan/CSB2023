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
    
    jump beach_overworld_map

######## THE MAP ########
label beach_overworld_map:
    ##### advance the clock first
    # TODO: these are currently using washington road bg/values, swap them later
    # TODO: implement actual planned soundtracks
    python:
        if beach_current_time == "start":
            beach_current_time = "morning"
            beach_current_shader = "dusk"
            beach_current_map_bgm = audio.outdoors

        elif beach_current_time == "morning":
            beach_current_time = "day"
            beach_current_shader = "day"
            beach_current_map_bgm = audio.bedroom_day

        elif beach_current_time == "day":
            beach_current_time = "afternoon"
            beach_current_shader = "day"
            beach_current_map_bgm = audio.ochre_woods_day

        elif beach_current_time == "afternoon":
            beach_current_time = "evening"
            beach_current_shader = "dusk"
            beach_current_map_bgm = audio.onbs

        elif beach_current_time == "evening":
            beach_current_time = "night"
            beach_current_shader = ""
            beach_current_map_bgm = audio.krabby_klub

        elif beach_current_time == "night":
            beach_current_time = "end"
            beach_current_shader = ""

    ##### begin the next part of the story
    if beach_current_time != "end":

        # TODO: get an actually nice world map, just using a menu to make sure it works
        scene expression "washington_road %s" % beach_current_shader
        with dissolve

        # TODO: make sure any inline variables work with awawa mode

        # this is stupid and awful and bad. it fetches the internal ID of the current track.
        # if anyone has a better way to do this dynamically, please, be my guest. - tate
        python:
            for song, data in vars(store.audio).items():
                if data is beach_current_map_bgm:
                    beach_current_map_bgm_string = song
                    break
                else:
                    beach_current_map_bgm_string = "not found"

            # have to access this directly, i know it's bad aaaa
            execute_music(song)

            renpy.music.play(beach_current_map_bgm)

        "It is now [beach_current_time]. The current BGM's ID is [beach_current_map_bgm_string]."

        # TODO: actual locations are subject to change. need to consult w/ Pakoo on the best way to organize these
        menu:
            "Select a location."
            "Beach":
                $ renpy.jump("beach_beach."+beach_current_time)
            "Boardwalk":
                $ renpy.jump("beach_boardwalk."+beach_current_time)
            "Downtown":
                $ renpy.jump("beach_downtown."+beach_current_time)
            "Uptown":
                $ renpy.jump("beach_uptown."+beach_current_time)
    else:
        jump beach_end

######## LOCATION: BEACH ########
label beach_beach:
    label .morning:
        stop music fadeout 2.0
        scene black with Dissolve(2.0)
        play music cobalt_coast_2
        scene ocean_beach_entrance
        with dissolve
        music cobalt_coast_2

        n "CS and Arceus arrive at Ocean Beach."
     
        scene ocean_beach_path
        show cs happy at left
        show arceus at right
        with dissolve

        cs "Woohoo! We made it!"
        arceus "But, why are we here again? You can't even swim."
        show cs
        cs "So? We can still cool off in the water."
        show arceus angry
        show cs disappointed

        if fun_value(FUN_VALUE_COMMON):
            arceus "Fuck you mean \"oui\"? You speakin' French?"
            arceus "I can't get my fur wet."
        else:
            arceus "Fuck you mean \"we\"? I can't get my fur wet."

        cs "Why not?"
        arceus "Because it'll take all day to dry and then I'll get all poofy."
        cs "Damn..."
        show cs
        cs "Well, {i}I{/i} still want to go in the water."
        cs "Be back in a sec."
        show arceus worried
        show cs flipped at offscreenleft with { "master": MoveTransition(1.0) }
        show arceus worried
        arceus "Wait, where are you going?"
        cs "I won't be long!"
        pause 1.0
        show arceus angry
        pause 1.0
        arceus "..."
        pause 1.0
        arceus "{size=-12}I guess it might feel good on my feet..."
        show arceus angry flipped at offscreenright with { "master": MoveTransition(1.0) }
        n "Arceus begins to follow the coastline."

        scene ocean_beach_coast
        show arceus angry flipped at offscreenleft
        show obama beach at offscreenright
        show mean angry flipped at manual_pos(1.3, 0.8, 1.0)
        with determination
        show arceus angry flipped at left with move
        with dissolve
        
        show obama beach at right
        show mean angry flipped at manual_pos(0.9, 0.8, 1.0)
        with MoveTransition(1.0)

        obama "Excuse me."
        show arceus worried flipped
        arceus "President Obama?!" with vpunch
        obama "Yes, it is I."
        obama "I have a question for you."
        obama "I found this strange talking ball. It is yellow, and {i}you{/i} are yellow-- does it belong to you?"
        show mean furious flipped
        mean_offscreen "For the last time, I'm not a fucking {nw}"
        extend "{i}ball!" with vpunch
        show mean angry flipped
        mean_offscreen "Now, will you put me down already?!"
        obama "I must return you to your owner. It is the ethical thing to do."
        obama "As President, I am determined to reunite all lost beach balls with their owners."
        mean_offscreen "Fine, the yellow fucker is my owner. Now, let me go!"
        obama "Fair enough. Have a great day!"
        arceus "Wait, but I'm not-- {nw}"
        obama "If you will excuse me-- I hear the hotdog stand here has a \"Presidential Special\", and I must ascertain whether it is worthy of that title."
        obama "Farewell for now!"
        show obama beach behind arceus at offscreenleft with move
        pause 2.0
        show mean flipped unamused
        mean_offscreen "Yo."
        mean_offscreen "Name's Mean."
        arceus "Uh, hey. I'm Arceus. I usually go by Arc, though."
        mean "Nice to, uh, be owned by you, I guess?"
        arceus "Nice to, um, be your owner, too...?"
        mean "Well, okay, I guess the closest thing to my \"owner\" would be my friend, but even {i}that's{/i} a stretch."
        mean "Have you seen someone in pink shorts?"
        arceus "'Fraid not. My friend and I actually just got here."
        show arceus angry flipped
        arceus "Where {i}is{/i} he, anyway?"
        mean "What's he look like?"
        arceus "Oh, uh, he's wearing a purple cat maid outfit."
        show mean ayo flipped
        mean "{i}That{/i} guy?! Yeah, I saw him just before the fuckin' President interrupted my swimming!"
        show tate beach flipped at mid_mid_right
        show cs beach happy flipped at right
        show mean ayo at manual_pos(0.5, 0.8, 1.0)
        show arceus worried flipped
        with moveinright
        cs "Hey guys!"
        cs "You won't {i}believe{/i} who I just ran into!"
        arceus "CS, what are you-- {nw}"
        mean "Tate! There you are!"
        mean "Wait-- you {i}know{/i} this guy?!"
        show tate sheepish beach flipped
        tate "Yeah? This is CS."
        mean "{i}That's{/i} CS?!"
        show cs disappointed beach flipped
        cs "Wait, what do you mean?"
        show arceus angry flipped
        arceus "Isn't it obvious?"
        tate "{size=-12}Listen, it's better not to question it."
        cs "What'd you say?"
        show tate beach
        tate "Eh? I didn't say anything."
        tate "Now, are we gonna go get that hot dog, or what?"
        show tate beach flipped
        show mean wat behind arceus
        show arceus worried flipped
        arceus "Shit, I want one... we haven't eaten in, uh, a while."
        show mean behind arceus
        mean "Eh, fuck it, I could eat."
        show mean happy behind arceus
        mean "Let's go! My treat."

        show cs happy beach flipped
        show arceus happy flipped
        cs "Wow, thanks!" (multiple=3)
        arceus "Thank you so much!" (multiple=3)
        tate "Hell yeah, thank you!" (multiple=3)

        show arceus flipped at offscreenright
        show mean happy at manual_pos(1.3, 0.8, 1.0)
        show tate beach at offscreenright
        show cs beach at offscreenright
        with move

        "..."


        jump beach_overworld_map
    label .day:
        "Pretend an event happened at the beach during the day."
        "Returning to the map."
        jump beach_overworld_map
    label .afternoon:
        "Pretend an event happened at the beach in the afternoon."
        "Returning to the map."
        jump beach_overworld_map
    label .evening:
        "Pretend an event happened at the beach in the evening."
        "Returning to the map."
        jump beach_overworld_map
    label .night:
        "Pretend an event happened at the beach at night."
        "Returning to the map."
        jump beach_overworld_map

######## LOCATION: BOARDWALK ########
label beach_boardwalk:
    label .morning:
        "Pretend an event happened at the boardwalk in the morning."
        "Returning to the map."
        jump beach_overworld_map
    label .day:
        "Pretend an event happened at the boardwalk during the day."
        "Returning to the map."
        jump beach_overworld_map
    label .afternoon:
        "Pretend an event happened at the boardwalk in the afternoon."
        "Returning to the map."
        jump beach_overworld_map
    label .evening:
        "Pretend an event happened at the boardwalk in the evening."
        "Returning to the map."
        jump beach_overworld_map
    label .night:
        "Pretend an event happened at the boardwalk at night."
        "Returning to the map."
        jump beach_overworld_map

######## LOCATION: DOWNTOWN ########
label beach_downtown:
    label .morning:
        "Pretend an event happened downtown in the morning."
        "Returning to the map."
        jump beach_overworld_map
    label .day:
        "Pretend an event happened downtown during the day."
        "Returning to the map."
        jump beach_overworld_map
    label .afternoon:
        "Pretend an event happened downtown in the afternoon."
        "Returning to the map."
        jump beach_overworld_map
    label .evening:
        "Pretend an event happened downtown in the evening."
        "Returning to the map."
        jump beach_overworld_map
    label .night:
        "Pretend an event happened downtown at night."
        "Returning to the map."
        jump beach_overworld_map

######## LOCATION: UPTOWN ########
label beach_uptown:
    label .morning:
        "Pretend an event happened uptown in the morning."
        "Returning to the map."
        jump beach_overworld_map
    label .day:
        "Pretend an event happened uptown during the day."
        "Returning to the map."
        jump beach_overworld_map
    label .afternoon:
        "Pretend an event happened uptown in the afternoon."
        "Returning to the map."
        jump beach_overworld_map
    label .evening:
        "Pretend an event happened uptown in the evening."
        "Returning to the map."
        jump beach_overworld_map
    label .night:
        "Pretend an event happened uptown at night."
        "Returning to the map."
        jump beach_overworld_map

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
            locations_list = [ "beach", "boardwalk", "downtown", "uptown"]
            times_list = ["morning", "day", "afternoon", "evening", "night"]
            beach_labels_list = []

            # construct the list of labels because fuck you if you think i'm doing this by hand
            for l in locations_list:
                for t in times_list:
                    next_value = "beach_" + l + "." + t
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
