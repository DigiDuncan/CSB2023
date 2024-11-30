# THIS IS REFERENCE FOR DIGI
# PEOPLE AT THE PARTY:
# CS
# Arc, Kitty
# Anno
# Digi
# Mean, Tate
# Billy
# Obama
# Copguy, Sheriff
# Ed, Rich, Wesley
# K-17, K-22
# Aria
# Michael
# Linus, Luke
# Blank
# Nova
# Elizabeth, Anne, Grace
# DB05

label ce_start:
    play music lets_hear_winter volume 0.7 if_changed
    music lets_hear_winter
    scene cs_bedroom2 
    show cs at mid_left
    with Dissolve(1.0)

    pause 0.5
    n "CS wakes up to a snowy winter morning."
    cs "Oh, {i}yes!{/i} It snowed today!"
    show cs at mid_mid_right with move
    pause 0.5

    n "CS takes a look at the calendar."
    show cs happy
    cs "Woohoo!"
    cs "Christmas is almost here!"
    show cs
    cs "... And, you know what that means!"
    if fun_value(FUN_VALUE_COMMON):
        cs "Fish!"  # TODO: SFX: [[FISH]]
        cs "But, more importantly..."
    cs "I finally get to throw a huge Christmas party at my house!"
    show cs happy flipped
    cs "I'm so pumped! I should call everyone one more time to make sure they're still coming."
    play sound sfx_ring_once
    show cs happy phone flipped with dissolve
    $ collect("cs_phone") # i am putting the item collection for non-CE items here anyway in case we do include item collection in CE standalone - tate
    pause 0.5
    scene black with dissolve
    pause 1.0
    n "CS makes a phone call to each of the friends he had invited."
    pause 0.5

    scene cs_bedroom1_ce
    show cs phone at center
    with dissolve
    pause 1.0
    play sound sfx_end_call
    pause 1.0
    show cs with dissolve

    show cs happy
    # remember, CS does not remember Mean in this timeline, so let's imply a few guests are bringing a plus-one, including, uh, me. - tate
    cs "Yep, looks like that's everyone, and {i}then{/i} some! It's gonna be a full house!"
    cs "I've got two days to prepare!"
    pause 2.0
    "..."
    show cs disappointed
    cs "...{fast} I have not prepared at all."
    cs "Fuck."
    # if y'all know CS, then y'all know damn well why this line exists. - tate
    cs "I literally had two {i}weeks{/i} to get everything ready, but I guess I just left it until the last minute again..." 
    pause 0.5

    show cs
    cs "Well, I guess the first thing to do is decide where to actually hold the party."
    show cs flipped
    cs "I have this huge-ass mansion, but I only usually use, like, three rooms!"
    show cs happy flipped
    cs "I think I know just the place!"
    hide cs with moveoutleft
    n "CS walks into his spare living room."

    scene cs_living2
    show cs at center
    with dissolve

    cs "This should be plenty of space!"
    cs "Now, I've just gotta make the place look {i}festive!"
    show cs happy
    cs "I {i}knew{/i} all that décor I bought at Michael's would come in handy! I should go grab it."
    show cs
    n "CS heads towards the garage."
    hide cs with moveoutright
    pause 0.5
    play sound sfx_house_door_open
    pause 0.5

    # OKAY, EDITING THIS IS GETTING RIDICULOUS. I'M REDOING ALL THESE SPAGHETTI-ASS MENUS. 
    # I AM *NOT* ANIMATING THESE THINGS 2-3 TIMES EACH, AND YOU CAN'T MAKE ME. - TATE

    scene cs_garage
    show cs at mid_left
    show garage_shelf behind cs at manual_pos(0.9, 0.5, 0.5)
    with dissolve
    pause 1.0
    cs "Alright! What should I bring in first?"
    menu:
        cs "Alright! What should I bring in first?{fast}"
        "Christmas tree":
            $ tree_first = True
            jump ce_tree
        "Lights and garland":
            $ lights_first = True
            $ got_lights = True
            jump ce_lights
        "Ornaments and decorations":
            $ decor_first = True
            $ got_decor = True
            jump ce_decor

label ce_tree:
    # GET TREE FIRST
    if tree_first:
            
        cs "I should get the Christmas tree first."
    
        # these unusual transitions will force the dialogue window to remain open while CS is moving the box.
        
        show cs at mid_offscreen_right with { "master" : MoveTransition(0.5) }
        cs "Who {i}doesn't{/i} wanna get {i}this{/i} thing out? This is the {i}best{/i} part of decorating!" # there are so many italics in this line

        play sound sfx_box_drag volume 5.0
        show cs
        show tree_box at manual_pos(1.2, 0.8)
        cs "I just..."

        play sound sfx_box_drag volume 5.0
        show cs angry at right
        show tree_box at manual_pos(0.9, 0.8)
        with { "master" : MoveTransition(0.5) }
        cs "I just...{fast} need to be..."
        $ collect("tree_box")

        play sound sfx_box_drag volume 5.0
        show cs pissed at mid_right
        show tree_box at manual_pos(0.8, 0.8)
        with { "master" : MoveTransition(0.5) }
        cs "I just... need to be...{fast} careful..."

        show cs concentrate
        cs "{sc=1.0}Hnng..."

        play sound sfx_box_drag volume 5.0
        show cs worried at mid_mid_right 
        show tree_box at manual_pos(0.6, 0.8)
        with MoveTransition(0.15)
        with hpunch
        show cs scared
        show garage_shelf:
            linear 0.25 rotate -30
        pause 0.25
        play sound2 sfx_metalpipe noloop
        $ collect("cheap_shelf")

        scene black with vpunch
        n "All of a sudden, the shelf tips and falls onto CS!"

        play sound2 sfx_lego_break noloop
        play sound [ "<silence 1.0>", sfx_cat_crash ]
        cs "Shit!{w=1.0}{nw}"
        
        pause 2.0
        scene cs_garage_mess
        with dissolve

        pause 1.0
        cs "Ow..."
        pause 1.0
        show cs disappointed at manual_pos(0.3, 1.2, 0.5):
            rotate 75
        show cs disappointed at manual_pos(0.5, 1.115, 1.0) with MoveTransition(1.0):
            linear 1.0 rotate -0
        n "CS digs himself out from the mess of lights, garland, and Legos."
        show cs disappointed at manual_pos(0.75, 1.115, 1.0) with move

        # CS steps on a Lego.
        play sound sfx_spikes
        show cs scared with hpunch
        n "He steps directly onto a stray Lego."
        cs "Fuck!"
        show cs disappointed flipped
        cs "Man, what a mess!"
        cs "This is gonna take forever to clean up!"
        hide cs with moveoutleft
        jump ce_anno

    # IF TREE IS NOT FIRST
    if lights_first or decor_first:
        cs "Nice! Time to get the Christmas tree!"
        show cs at mid_offscreen_right with move
        show tree_box at manual_pos(1.2, 0.8)
        pause 1.0
        # i want him to be struggling a bit to move it due to the awkward size - tate

        play sound sfx_box_drag volume 5.0
        show cs concentrate at right
        show tree_box at manual_pos(0.9, 0.8)
        with move
        pause 0.5
        $ collect("tree_box")

        play sound sfx_box_drag volume 5.0
        show cs concentrate at mid_mid_right
        show tree_box at manual_pos(0.7, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 5.0
        show cs concentrate at center
        show tree_box at manual_pos(0.6, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 5.0
        show cs concentrate at mid_mid_left
        show tree_box at manual_pos(0.4, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 5.0
        show cs concentrate at left
        show tree_box at manual_pos(0.2, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 5.0
        show cs concentrate at mid_offscreen_left
        show tree_box at manual_pos(0.0, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 5.0
        show cs concentrate at offscreenleft
        show tree_box at manual_pos(-0.2, 0.8)
        with move
        pause 0.5

        # fading it out
        play sound sfx_box_drag volume 4.0
        show tree_box at manual_pos(-0.4, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 3.0
        show tree_box at manual_pos(-0.6, 0.8)
        with move
        pause 0.5

        play sound sfx_box_drag volume 2.0
        pause 1.5
    
        n "CS drags the box out of the garage and into the living room."

        jump ce_check_status

label ce_lights:
    if lights_first:
        cs "I should probably get the lights and garland first. That box is easiest to reach, anyway."
    if got_tree or got_decor:
        cs "Alright, I should probably get the lights and garland next."

    # Animation
    show cs at mid_offscreen_right with move
    show lights_box at manual_pos(1.2, 0.5)
    pause 1.0
    show lights_box at manual_pos(0.9, 0.4) with moveinright
    $ collect("lights_box")
    pause 0.5
    show cs flipped at offscreenleft
    show lights_box at offscreenleft
    with move
    pause 1.0
    play sound sfx_box_place volume 4.0

    n "CS leaves the box by the couch so he can untangle the lights comfortably later."

    jump ce_check_status

label ce_decor:
    if decor_first:
        cs "I'm gonna get the decorations first! I have a {i}huge{/i} assortment of Legos in there, too!"
    if got_tree or got_lights:
        cs "Alright, I should probably get the decorations next."
    
    # Animation
    show cs at mid_offscreen_right with move
    show decor_boxes at manual_pos(1.2, 0.5)
    pause 1.0
    show decor_boxes at manual_pos(0.9, 0.4) with moveinright
    $ collect("decor_boxes")
    pause 0.5
    show cs flipped at offscreenleft
    show decor_boxes at offscreenleft
    with move
    pause 1.0
    play sound sfx_box_place volume 4.0

    n "CS places the boxes onto the floor."

    jump ce_check_status

# CHECK STATUS HERE
label ce_check_status:

    # If you have everything, just get outta here!
    if got_lights and got_decor and got_tree:
        jump ce_before_anno

    # Otherwise...
    else:

        # Decor was first, and that's all you have
        if decor_first and not (got_tree or got_lights):
            show cs at left with moveinleft
            n "CS returns to the garage to grab the next box."
            menu:
                "Christmas tree":
                    $ got_tree = True
                    jump ce_tree
                "Lights and garland":
                    $ got_lights = True
                    jump ce_lights
     
        # Lights were first, and that's all you have
        if lights_first and not (got_tree or got_decor):
            show cs at left with moveinleft
            n "CS returns to the garage to grab the next box."
            menu:
                "Christmas tree":
                    $ got_tree = True
                    jump ce_tree
                "Ornaments and decorations":
                    $ got_decor = True
                    jump ce_decor

        # Have lights and tree
        if got_lights and got_tree:
            show cs at left with moveinleft
            n "CS returns to the garage to retrieve the last box." 
            menu:
                "Ornaments and decorations":
                    $ got_decor = True
                    jump ce_decor

        # Have decor and tree
        if got_decor and got_tree:
            show cs at left with moveinleft
            n "CS returns to the garage to retrieve the last box."
            menu:
                "Lights and garland":
                    $ got_lights = True
                    jump ce_lights

        # Have lights and decor
        if got_lights and got_decor:
            show cs at left with moveinleft
            n "CS returns to the garage to retrieve the last box."
            menu:
                "Christmas tree":
                    $ got_tree = True
                    jump ce_tree

label ce_before_anno:
    scene cs_foyer
    show cs happy at center
    with dissolve
    cs "Woohoo! That's finally done!"

    if fun_value(FUN_VALUE_COMMON):
        cs "Everything I need to decorate the house is all right here at my fingertits!"
    else:
        cs "Everything I need to decorate the house is all right here at my fingertips!"

    cs "This is where the fun part begins!"
    jump ce_anno

label ce_anno:
    scene cs_foyer
    show cs disappointed at center
    with dissolve
    if tree_first:
        n "CS takes one last glance at the disaster in the garage."
        n "He lets out a groan."
        cs "This is {i}not{/i} how this was supposed to go..."
    else:
        n "CS looks upon his stash of lights and baubles and feels a little overwhelmed."
        cs "Wow, this is more than I thought..."
    cs "Maybe I should call someone over to help."
    cs "I wonder if Anno is around."
    show cs disappointed phone with dissolve
    play sound sfx_ring_once
    show cs disappointed phone at mid_left with move
    show anno_house at mid_offscreen_right
    show anno phone at mid_right
    with moveinright
    anno "Hello?"
    show cs happy phone
    cs "Hey Anno, CS here!"
    anno "Yes, I know the party is in two days, you just called me. I'm still coming."
    show cs phone
    cs "Yeah, I know. I was just wondering...{w=1.0}{nw}"
    show cs happy phone
    cs "Yeah, I know. I was just wondering...{fast} if you wanted to help me decorate my house!"
    anno "Ah, man, I still have to get something for the gift exchange..."
    show cs disappointed phone
    "..."
    anno "... But, I can do that tomorrow."
    anno "Yeah, sure, I'll come over. Be there soon."
    show cs happy phone
    cs "Cool! See ya then!"
    hide anno_house
    hide anno
    with moveoutright
    show cs happy phone at center with move
    play sound sfx_end_call
    pause 1.0
    show cs with dissolve
    pause 0.5

    cs "Awesome! Anno's gonna come over to help out!"
    show cs surprised flipped
    cs "I guess I should start planning where everything is gonna--"
    show cs worried
    cs "Actually, shit, it snowed last night!"
    stop music fadeout 3.0
    music end
    cs "I need to shovel before Anno gets here!"
    hide cs with moveoutright
    scene black with dissolve

    n "CS puts on his coat before heading back to the garage for a shovel."

    if tree_first:
        scene cs_garage_mess with dissolve
        show cs disappointed coat hat at offscreenleft
        show cs disappointed coat hat at mid_mid_left with moveinleft
        show cs scared coat hat
        play sound sfx_spikes
        cs "Shit!" with hpunch
        show cs worried coat hat
        # I just want to put for posterity here that the original line was:
        # "I hate Legos, but only when they're in my feet!"
        # Which I think is very funny. -- Digi
        cs "I love Legos, but not when they're embedded in my {i}feet!" 
        cs "Now, where did I last put..."
    else:
        scene cs_garage with dissolve
        show cs disappointed coat hat at mid_mid_left with moveinleft
    pause 0.5
    show cs disappointed coat hat at right with move
    pause 0.5
    cs "Here we go."
    if fun_value(FUN_VALUE_COMMON):
        cs "Yahoo."

    show cs disappointed coat hat at mid_offscreen_right with move
    show shovel at manual_pos(1.2, 0.8, 0.5) with determination
    $ collect("shovel")

    show cs disappointed coat hat at right 
    show shovel at manual_pos(0.9, 0.7, 0.5):
        rotate 15
    with move

    pause 0.5
    cs "I sure hope it didn't snow {i}too{/i} much..."
    pause 0.5
    show cs disappointed coat hat flipped at left 
    show shovel at manual_pos(0.25, 0.7, 0.5):
        rotate 15
    with move
    pause 0.25
    play sound sfx_snd_lightswitch

    n "CS presses the button to open the garage door, but nothing happens."

    play sound sfx_snd_lightswitch
    pause 0.5
    play sound sfx_snd_lightswitch
    pause 0.25
    play sound sfx_snd_lightswitch
    pause 1.0

    cs "Damn it, I think it's iced shut."
    cs "I'll just have to go around through the front."

    hide cs 
    hide shovel
    with moveoutleft
    scene black with dissolve
    pause 1.0
    play sound sfx_house_door_close
    pause 3.0

    scene cs_house_snowed_in
    show cs disappointed coat hat flipped at right
    show shovel at manual_pos(0.9, 0.7, 0.5):
        rotate 15
    with dissolve
    play music snowy
    music snowy
    n "As CS closes the door behind him, he is greeted by a massive pile of snow blocking the garage."
    cs "Well, that's just {i}great."
    cs "This is gonna take at least an hour to shovel aside..."
    pause 0.25

    # had to do it. -tate
    show cold_breath:
        alpha 0
        xpos 0.75
        ypos 0.3
        parallel:
            linear 0.5 alpha 1.0
            linear 1.5 alpha 0
        parallel:
            linear 1.5 xpos 0.7
        parallel:
            linear 1.5 ypos 0.2

    pause 2.0
    n "CS lets out a sigh into the cold."
    "..."
    cs "Guess I'd better get to it."
    cs "Let's get to it.{w=0.25}{nw}"
    cs "I'm gonna get to it.{w=0.05}{nw}"
    cs "I'm gonna get to it.{fast}\nI'm gonna get to it.{w=0.05}{nw}"
    cs "I'm gonna get to it.\nI'm gonna get to it.{fast}\nI'm gonna get to it.{w=1.0}{nw}"
    pause 2.0
    cs "Faaf."
    pause 0.5
    
    # SHOVEL ANIMATION TIME

    # FIRST
    # walk to it
    # TODO: this is only playing one footstep. it should be two. the next instance is two. I DON'T UNDERSTAND - tate
    play sound "<from 0.74 to 1.723>sfx/sfx_snow_walk.ogg" volume 2.0
    show cs disappointed coat hat flipped at center
    show shovel at manual_pos(0.6, 0.7, 0.5)
    with MoveTransition(1.0)
    # shovel go down
    show snow_pile at manual_pos(0.3, 1.1, 0.5) with determination:
        zoom 0.4
    $ collect("snow_pile")
    # TODO: shovel sounds
    show shovel at manual_pos(0.4, 0.9, 0.5) with move:
        rotate 15
    pause 0.5
    # shovel go up
    show shovel at manual_pos(0.5, 0.7, 0.5):
        linear 0.5 rotate 110
    show snow_pile at manual_pos(0.35, 0.5, 0.5):
        linear 0.5 rotate 10
    with move
    pause 0.5
    # turn around
    show cs disappointed coat hat at center
    show shovel at manual_pos(0.5, 0.7, 0.5):
        xzoom -1.0
        rotate -110
    show snow_pile at manual_pos(0.65, 0.5, 0.5):
        xzoom -1.0
        rotate -10
    pause 0.5
    # walk back
    play sound "<from 0.074 to 1.723>sfx/sfx_snow_walk.ogg" volume 2.0
    show cs disappointed coat hat at right
    show shovel at manual_pos(0.9, 0.7, 0.5)
    show snow_pile at manual_pos(1.05, 0.5, 0.5)
    with MoveTransition(1.0)
    pause 0.5
    # put it down
    show shovel at manual_pos(0.9, 0.8, 0.5):
        linear 0.5 rotate -15
    show snow_pile at manual_pos(1.15, 1.0, 0.5):
        linear 0.5 rotate -15
    with move
    pause 1.0

    # SECOND
    # turn around
    show cs disappointed coat hat flipped at right
    show shovel at manual_pos(0.9, 0.7, 0.5):
        xzoom 1.0
        rotate 15
    pause 0.5
    # walk to it
    play sound "<from 0.074 to 0.869>sfx/sfx_snow_walk.ogg" volume 2.0
    show cs disappointed coat hat flipped at mid_right
    show shovel at manual_pos(0.7, 0.7, 0.5)
    with MoveTransition(1.0)
    # shovel go down
    show snow_pile at manual_pos(0.4, 1.1, 0.5) with determination:
        zoom 0.4
    # TODO: shovel sounds
    show shovel at manual_pos(0.6, 0.9, 0.5) with move:
        rotate 15
    pause 0.5
    # shovel go up
    show shovel at manual_pos(0.6, 0.7, 0.5):
        linear 0.5 rotate 110
    show snow_pile at manual_pos(0.5, 0.5, 0.5):
        linear 0.5 rotate 10
    with move
    pause 0.5
    # turn around
    show cs disappointed coat hat at mid_right
    show shovel at manual_pos(0.8, 0.7, 0.5):
        xzoom -1.0
        rotate -110
    show snow_pile at manual_pos(0.95, 0.5, 0.5):
        xzoom -1.0
        rotate -10
    pause 0.5
    # walk back
    play sound "<from 0.074 to 0.869>sfx/sfx_snow_walk.ogg" volume 2.0
    show cs disappointed coat hat at right
    show shovel at manual_pos(0.9, 0.7, 0.5)
    show snow_pile at manual_pos(1.05, 0.5, 0.5)
    with MoveTransition(1.0)
    pause 0.5
    # put it down
    show shovel at manual_pos(0.9, 0.9, 0.5):
        linear 0.5 rotate -15
    show snow_pile at manual_pos(1.15, 1.0, 0.5):
        linear 0.5 rotate -15
    with move
    pause 1.0

    # THIRD
    # turn around and walk
    play sound "<from 0.074 to 2.563>sfx/sfx_snow_walk.ogg" volume 2.0
    show cs disappointed coat hat flipped at mid_left
    show shovel at manual_pos(0.3, 0.7, 0.5):
        xzoom 1.0
        rotate 15
    with MoveTransition(2.5)
    # shovel go down
    show snow_pile at manual_pos(0.0, 1.1, 0.5) with determination:
        zoom 0.4
    pause 0.5
    # TODO: shovel sounds
    show shovel at manual_pos(0.1, 0.9, 0.5) with move:
        rotate 15
    pause 0.5
    # shovel go up
    show shovel at manual_pos(0.2, 0.7, 0.5):
        linear 0.5 rotate 110
    show snow_pile at manual_pos(0.1, 0.5, 0.5):
        linear 0.5 rotate 10
    with move
    pause 0.5
    # flip
    show cs disappointed coat hat at mid_left
    show shovel at manual_pos(0.5, 0.7, 0.5):
        xzoom -1.0
        rotate -110
    show snow_pile at manual_pos(0.6, 0.5, 0.5):
        xzoom -1.0
        rotate -10
    pause 0.5
    # walk back
    play sound "<from 0.074 to 2.563>sfx/sfx_snow_walk.ogg" volume 2.0
    show cs disappointed coat hat at right
    show shovel at manual_pos(0.9, 0.7, 0.5)
    show snow_pile at manual_pos(1.05, 0.5, 0.5)
    with MoveTransition(2.5)
    pause 0.5
    # put it down
    show shovel at manual_pos(0.9, 0.9, 0.5):
        linear 0.5 rotate -15
    show snow_pile at manual_pos(1.15, 1.0, 0.5):
        linear 0.5 rotate -15
    with move
    pause 1.0

    # enter carguy
    show carguy flipped at offscreenleft with determination
    play sound sfx_snow_walk loop volume 2.0 fadein 2.0
    n "About ten minutes into shoveling, CS hears someone walking up his driveway."
    pause 2.0
    show carguy flipped at left with MoveTransition(1.0)
    stop sound
    pause 0.5
    play sound sfx_nice_snow
    carguy_nobeep "Nice snow!"
    play sound sfx_not_so_nice_driveway
    carguy_nobeep "Nooot so nice driveway."
    show cs disappointed coat hat flipped
    show shovel at manual_pos(0.9, 0.7, 0.5):
        xzoom 1.0
        rotate 15
    cs "Look, man, I'm trying."
    cs "It's cold as balls out here."
    carguy "Speaking of balls, you need some help?"
    carguy "I've got something that'll do the trick!"
    carguy "Crotch Doctor, with advanced \"Scratch My Balls\" technology, not only removes taint scrapes, stuffs, grapes, and other blemishes from your car, it {i}also{/i} instantly melts snow!"
    carguy "Watch!"
    show crotch_doctor with dissolve:
        zoom 0.2
        yzoom 1
        pos (0.3,0.45)

    $ collect("crotch_doctor")

    n "Carguy produces a bottle of Crotch Doctor from his breast pocket and unscrews the cap."
    n "He tips it upside down and gives it a squeeze."
    show crotch_doctor:
        zoom 0.2
        yzoom 1
        pos (0.25,0.45)
        linear 0.5 rotate 180
    pause 0.7
    play sound sfx_bottle_squirt
    show crotch_doctor:
        zoom 0.2
        yzoom 1
        pos (0.25,0.45)
        linear 0.5 xzoom 0.2
        linear 0.5 xzoom 1   
    pause 2.0
    play sound2 sfx_droplet noloop volume 10.0
    pause 1.0
    play sound sfx_snow_evaporate volume 2.0
    pause 0.5

    n "A single drop falls onto the snow, revealing only a hint of the asphalt below."
    pause 0.5
    
    cs "Umm..."
    carguy "Hold on, it's just..."
    play sound sfx_bottle_hit volume 4.0
    show crotch_doctor:
        zoom 0.2
        yzoom 1
        pos (0.25,0.45)
        linear 0.1 ypos 350
        linear 0.1 ypos 550

    n "Carguy vigorously shakes and smacks the empty bottle."
    play sound2 sfx_bottle_hit volume 4.0
    play sound sfx_bottle_squeeze
    show crotch_doctor:
        zoom 0.2
        yzoom 1
        pos (0.25,0.45)
        linear 0.1 ypos 350
        linear 0.1 ypos 550
        repeat 7
    pause 1.5
    stop sound2
    pause 1.0
    carguy "{size=-15}I thought I'd brought more of this..." 
    hide crotch_doctor with dissolve
    carguy "Welp, sorry! Looks like I've run out!"
    carguy "Gotta run! Happy holidays to you!"
    play sound2 sfx_whoosh noloop
    play sound sfx_snow_run loop volume 3.0
    show carguy at offscreenleft with MoveTransition(0.25)
    pause 0.5
    stop sound fadeout 5.0
    n "Carguy turns on his heel and scampers away through the snow."
    pause 2.0
    show cs angry coat hat flipped
    cs "Well, {i}that{/i} was a huge waste of my time!"
    show cs worried coat hat flipped
    cs "I need to finish shoveling, already! My face is starting to freeze!"
    pause 0.5

    play sound sfx_snow_walk loop volume 2.0
    show cs disappointed coat hat flipped at center
    show shovel at manual_pos(0.6, 0.7, 0.5):
        rotate 15
    with MoveTransition(2.0)
    # TODO: SFX more shoveling, ain't no way in hell i'm animating this a second time though.
    scene white with dissolve
    pause 2.0

    stop sound fadeout 1.0
    scene cs_house_snow
    show cs disappointed coat hat flipped at center
    show shovel at manual_pos(0.6, 0.7, 0.5):
        rotate 15
    with Dissolve(1.0)

    play sound sfx_car_approach_stop volume 5.0 fadein 5.0
    n "As CS finishes clearing the driveway, he spots Anno's car turning onto his street."
    cs "Just in time!"

    # TODO: sfx - anno's car

    show cs happy coat hat flipped
    n "CS waves to Anno as the car pulls into CS' driveway."
    show cs coat hat flipped
    play sound sfx_car_door_open
    play sound2 sfx_car_door_ajar
    pause 3.0
    stop sound2
    play sound sfx_doorslam
    pause 3.0
    show anno coat at left with moveinleft
    anno "Hey, how's it going?"
    show cs disappointed coat hat flipped
    cs "Cold. Very cold."
    cs "You would not {i}believe{/i} how much snow there was!"
    cs "You showed up just as I got done shoveling here."
    show cs worried coat hat
    show shovel at manual_pos(0.4, 0.7, 0.5):
        rotate -15
    cs "Let's get inside, please! My hands are gonna fall off!"
    anno "Right behind you."
    show cs worried coat hat at offscreenright
    show anno coat at offscreenright
    show shovel at offscreenright
    with moveoutright
    play sound sfx_house_door_open

    scene black with dissolve
    pause 2.0
    play sound sfx_house_door_close
    pause 2.0
    n "After taking their jackets and snowy shoes off, the two head to CS' living room."
    pause 1.0

    scene cs_living2
    show cs at left
    show anno at right
    with dissolve

    n "They take a few minutes to catch up and recover from the bitter cold."
    pause 1.0

    anno "Well, CS, how's it been?"
    show cs happy
    cs "Good! Still rockin' that Kurt Cobain look, I see."
    anno "Pfft, you thought I would get rid of it?"
    show cs
    cs "Nah, it totally suits you."
    cs "I've mostly just been enjoying {i}not{/i} being chased by the cops again and living a relatively normal life."
    anno "Yeah, how was the trip back after all that? We haven't really kept in touch since we all split up in Canada."
    show cs disappointed
    cs "Well, I had a blast working for LTT for a few days, but the cops found me as soon as I was featured in a video, so Arc and I had to hit the road again."
    show cs
    cs "We eventually proved to the cops that I wasn't guilty, and then Billy Mays took us all the way home."
    anno "How the {i}hell{/i} did you manage to come across Billy Mays?!"
    show cs happy
    cs "Crazy coincidence, I guess! It was a lot of fun though!"
    cs "We went to PencilCon, I won a golden pencil sharpener, visited some old friends, and did a lot of sightseeing!"
    show cs
    anno "Sounds like one hell of a time."
    anno "I guess the cops were so focused on finding {i}you{/i} that they mostly left me alone."
    anno "I tried to start up a band, but that didn't really work out."
    anno "Spoofy streams don't pay for shit." # no, no, they do not. - tate
    show cs disappointed
    cs "Damn. Sorry to hear."

    # Christmas tree first
    if tree_first:
        anno "By the way, where are all of the decorations?"
        cs "Ah, yes. They're all in the garage. Come on, I'll show you."
        hide cs with moveoutright
        hide anno with moveoutright
        n "Anno follows CS into the garage."

        scene cs_garage_mess with dissolve
        show cs disappointed at center
        show anno at left
        with moveinleft
        n "Anno gawks at the mess on the floor, carefully avoiding the strewn-about Legos."
        anno "Damn, bitch, you {i}live{/i} like this?"
        cs "... I may have had a... {i}small{/i} mishap when I was trying to get the tree out."
        anno "{i}\"Small\"?!" with vpunch
        show cs worried flipped
        cs "Okay, maybe {i}not-{/i}so-small, but, do you think you can help me?"
        show cs disappointed
        cs "I figured it'd be faster if I had a helping hand."
        n "Anno groans."
        anno "I was hoping to be {i}setting up{/i} decorations, not {i}cleaning them{/i} up."
        anno "But, I guess we don't really have any other option, do we?"
        cs "Guess not..."
        show cs disappointed at mid_right with move
        cs "Here, I'll grab these boxes, and we'll start throwing stuff in them."
        scene black with dissolve
        n "After about an hour, they manage to clean up the mess without stepping on too many more Legos."
        n "CS and Anno drag the remaining boxes inside."
    else:
        anno "So, you needed my help with decorating, right?"
        show cs
        cs "Yeah. I've already brought everything in, so let's start unpacking it."
        anno "Alright!"
        scene black with dissolve
        centered "20 minutes later..."
        
# Setting up decorations
label ce_setup:
    stop music fadeout 3.0
    music end
    scene cs_living2
    show cs at left
    show anno at right
    with dissolve
    # TODO: need pile of decorations in boxes
    cs "Well, Anno, we did it! Are ya ready?"
    anno "Yeah! Where should we start?"

    scene black with dissolve
    n "Insert decorating scene here."
    # TODO: Decorating scene
    #Living room
    #Kitchen
    #Hallway
    #Entrance
    #Outside
    #After

    scene cs_living2_festive
    show cs happy at left
    show anno at right
    with dissolve
    cs "Wow, thanks, Anno!"
    cs "You really rizzed up my crib, for real! On {i}God!"
    "..."
    anno "Maybe {i}don't{/i} say that."
    show cs disappointed
    cs "Sorry."
    show cs
    anno "Well, I think we did a pretty darn good job."
    show cs happy
    cs "Hell yeah, we did!"
    cs "Everyone is gonna have a blast at this party!"
    show cs
    anno "Before I get going, was there anything else you needed help with?"
    show cs disappointed
    cs "No, I don't think so..."
    show cs worried
    n "CS remembers that he didn't buy any food for the party."
    cs "Shit, I do need to go shopping for food. I haven't bought anything for the party!"
    anno "Well, you got today and tomorrow at least."
    show cs
    cs "Yeah, I think I'm gonna head out here in a moment, I just need to make a list."
    anno "Alrighty, well, good luck with that!"
    anno "I'll see you in two days!"
    cs "Goodbye, Anno!"
    hide anno with moveoutright
    show cs flipped with determination
    hide cs with moveoutleft
    scene cs_bedroom1_ce with dissolve
    show cs disappointed at center with moveinleft
    n "Once Anno leaves, CS starts to worry a little."
    show cs angry
    cs "Damn it, I can't believe I forgot to get my own food for the party!"
    show cs disappointed
    cs "It's gonna be extremely busy tomorrow, so I should probably go now."
    cs "What to buy..."
    cs "Probably some pies, I think Michael was gonna make some mashed potatoes, so I should get some of those..."
    show cs
    cs "You know what? I got some time, I should destress and watch some car crash compilations to calm down."
    n "CS puts on a new compilation video and relaxes on his couch."
    scene black with dissolve
    pause 3.0
    scene cs_bedroom1_ce_car
    show cs
    with dissolve
    cs "...So out of 500 crashes..."
    show cs happy
    cs "That's about 257 red cars at fault!"
    show cs worried
    cs "Yikes! Thank God I don't have a red car."
    # What I love about that line is it implies that CS would be suddenly worse at driving if he owned a red car. -- Digi
    show cs
    cs "Alright, I should go get my groceries now."
    n "CS looks at the time."
    show cs worried
    cs "Oh no! It's 3AM!"
    show cs disappointed
    cs "Darn, the time really flew! Now I have to go tomorrow!"
    cs "I guess I can finish my shopping list and get to sleep."
    cs "Hmm... what else do I need?"
    n "After about another hour of trying to make his list and not watch more motor mayhem, CS finally gets to bed."
    scene black with dissolve
    centered "One long winter's nap later..."

# Day 2
label ce_before_shopping:
    # NOTE: something went wrong with this scene. i have to use manual_pos for everything or CS is floating? how annoying.
    play sound sfx_csnore loop
    play sound2 sfx_clock_ticking volume 0.5
    scene cs_bedroom2
    show cs happy flipped at manual_pos(700, 1400, 1.0):
        rotate 60
    with dissolve
    pause 1.0
    n "CS awakens from a restful sleep."
    if fun_value(FUN_VALUE_RARE):
        pause 2.0
        "..."
        n "I said, \"CS awakens from a restful sleep.\""
        pause 1.0
        "..."
        pause 2.0
        n "{cshake}{size=+24}CS, WAKE UP!!!" with hpunch
        stop sound
        show cs scared flipped
        cs "Wha--?!" with hpunch

        play sound sfx_blanket volume 10.0
        show cs disappointed at manual_pos(0.4, 1.115, 1.0):
            linear 0.5 rotate 0
        with move
        n "He finally rolls out of bed."
    else:
        stop sound fadeout 1.0
        pause 2.0
        show cs flipped
        pause 0.5
        play sound sfx_blanket volume 10.0
        show cs at manual_pos(0.4, 1.115, 1.0):
            linear 1.0 rotate 0
        with move
        n "He slowly rolls out of bed."

    n "Through bleary eyes, he takes a few steps to look at the clock."
    show cs at manual_pos(0.9, 1.115, 1.0) with MoveTransition(1.0)
    "..."
    show cs scared
    cs "{i}Huh?!" with hpunch
    cs "Oh, shit! It's 2PM already?!"
    cs "I've gotta get my shopping done!"
    show cs worried coat hat flipped with dissolve
    n "CS tosses his coat on and sprints out the door!"
    hide cs with easeoutleft
    play sound sfx_house_door_open
    pause 0.5
    scene black with dissolve
    stop sound2 fadeout 2.0
    pause 0.5
    play sound sfx_house_door_close
    pause 2.0

    scene cs_house_snow
    show cs coat hat flipped at mid_right
    with dissolve
    cs "Thank goodness it didn't snow overnight. Shoveling yesterday fuckin' sucked."
    # I just want this to be known.
    # I love this line.
    # It's so CS-coded but it's just not a line you'd expect to be in a visual novel.
    # Made me laugh when I first read it, and it's still getting a chuckle out of me.
    # He's right -- shoveling does fuckin' suck.
    # -- Digi
    cs "I don't want to do it all over again!"
    cs "I'm sure the shopping rush has already started. I need to get going!"
    hide cs with moveoutleft
    play sound sfx_car_door_open
    pause 1.0
    play sound sfx_doorslam
    n "CS gets in the car and starts thinking about where to go."

    scene cs_car_inside_snow
    show cs coat hat at left
    with dissolve
    cs "I only went to Walmart last time since they had that deal on Genergy, but I don't shop there regularly..."
    cs "I think I'll try somewhere else this time."
    n "CS starts up his car and heads to Target."
    play sound sfx_driving
    pause 2.0
    scene black with Dissolve(2.0)
    stop sound fadeout 5.0
    pause 5.0
    play music winter_unclearance_sale loop volume 0.85 fadein 1.0
    play sound sfx_hubbub loop volume 0.2 fadein 1.0
    scene tgt_inside
    with dissolve
    pause 3.0
    show cs coat hat at center with moveinleft
    n "CS arrives at Target."
    n "The faint scent of holiday-themed candles wafts through the air."

    show cs happy coat with dissolve
    cs "Now, {i}this{/i} is a {i}real{/i} store!"
    show cs coat
    cs "Everything is mostly clean and neat, no depressing lighting or messy aisles..."
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        cs "I should probably stop glazing up Target and actually buy what I came here for."
    else:
        cs "I should probably stop admiring the view and actually buy what I came here for."
    show cs coat flipped with determination
    hide cs with moveoutleft
    n "CS grabs a cart before venturing further into the store."
    show cs coat at offscreenleft
    show shopping_cart at manual_pos(-0.2, 1.1, 0.75)
    
    show shopping_cart at Move((-0.2, 0.6), (1.1, 0.6), 0.5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    hide cs with moveoutright

    # Shopping
    scene tgt_tater with dissolve
    show cs coat at center
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with moveinleft

    $ collect("shopping_cart")

    n "He starts at the produce section."
    show cs coat surprised
    cs "I think Michael said something about making mashed potatoes..."
    show cs coat disappointed
    cs "Jeez, with the number of people coming, that's going to take a {i}lot{/i} of taters."
    show cs coat
    cs "Heh. {i}Tate's{/i} coming, too."
    show cs coat happy
    cs "Let's hope Michael stays away from {i}them{/i} with the masher!"
    # pfffffft. i hadn't read this part until now and lmao wow - tate

    show cs coat flipped
    cs "I think three bags of these should be enough."

    # first two are normal...

    show cs coat flipped at mid_left with move
    pause 1.0
    show potato_bag at manual_pos(50, 300) with Dissolve(0.25)
    pause 0.5
    show cs coat at center
    show potato_bag at manual_pos(0.6, 0.5, 0.5)
    with move
    pause 0.5
    show potato_bag at manual_pos(0.8, 0.8, 0.5) with MoveTransition(0.25)
    hide potato_bag with dissolve
    $ collect("potato_bag")

    show cs coat flipped at mid_left with move
    pause 1.0
    show potato_bag at manual_pos(50, 300) with Dissolve(0.25)
    pause 0.5
    show cs coat at center
    show potato_bag at manual_pos(0.6, 0.5, 0.5)
    with move
    pause 0.5
    show potato_bag at manual_pos(0.8, 0.8, 0.5) with MoveTransition(0.25)
    hide potato_bag with dissolve

    show cs coat flipped at mid_left with move
    pause 1.0

    if fun_value(FUN_VALUE_LEGENDARY):
        $ got_tato_bag = True
        # this here is some EXTREMELY DEEP tate lore.

        # let's try the audio filtering feature! let's make this next thing muffled.
        $ renpy.music.set_audio_filter("sound2", renpy.audio.filter.Lowpass(1200))

        play sound2 [ "<silence 0.5>", sfx_tato_screm ] noloop 
        show tato_bag at manual_pos(50, 300) with Dissolve(0.25)
        pause 0.5
        show cs coat at center
        show tato_bag at manual_pos(0.6, 0.5, 0.5)
        with move
        pause 0.5
        show tato_bag at manual_pos(0.8, 0.8, 0.5) with MoveTransition(0.25)
        hide tato_bag with dissolve
        $ collect("tato_bag")
        pause 1.0
        show cs coat surprised
        cs "Huh..."
        "..."
        cs "Could've sworn I heard something..."
        pause 1.5
        show cs coat
        cs "Must have come from somewhere else in the store."

        # turn filter off again
        $ renpy.music.set_audio_filter("sound2", None)

    else:
        show potato_bag at manual_pos(50, 300) with Dissolve(0.25)
        pause 0.5
        show cs coat at center
        show potato_bag at manual_pos(0.6, 0.5, 0.5)
        with move
        pause 0.5
        show potato_bag at manual_pos(0.8, 0.8, 0.5) with MoveTransition(0.25)
        hide potato_bag with dissolve

    show cs coat
    n "After grabbing some \"tates\" of his own, CS heads over to the grocery aisles."
    # i hope this line ain't too weird. just felt too abrupt without SOMETHING here. - tate
    hide cs 
    hide shopping_cart
    with moveoutright
    pause 1.0

    scene tgt_bread with dissolve
    show cs coat at center 
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with moveinleft
    pause 1.0
    # NOTE: Good bread (intentional)
    cs "Oh, good, bread. Can't have a holiday dinner without some good bread!"
    cs "I guess I'll get Italian bread. You can make real good garlic bread with that."
    cs "Since Digi's coming, and I think they're ace, I'd better have the good stuff."
    # This is deep-cut ace jokes, CS will not understand this one. -- Digi
    show cs coat at mid_right with move
    pause 1.0

    show bread at manual_pos(0.9, 0.3) with Dissolve(0.25)
    show bread at manual_pos(0.8, 0.8) with MoveTransition(0.25)
    hide bread with dissolve
    $ collect("bread")

    show cs coat flipped at center with move
    show cs coat with determination

    show cs coat at right 
    show shopping_cart at manual_pos(1.1, 1.1, 0.5)
    with move

    n "As he makes his way to the next aisle, CS is already distracted from his shopping list."
    cs "Ooh, an endcap! This is where the good deals are."
    show cs coat surprised
    cs "Or, you know, the stuff that's about to expire..."
    show cs coat happy
    cs "Let's check it out!"
    
    hide cs
    hide shopping_cart
    with moveoutright
    pause 0.5

    scene tgt_endcap with dissolve
    pause 0.5
    
    show cs coat at left
    show shopping_cart at manual_pos(0.5, 1.1, 0.5)
    with moveinleft

    n "CS spots some EZ-Cheese."
    show cs coat happy
    cs "Oh, {i}sweet!{/i} This stuff {i}never{/i} expires!"
    show cs coat disappointed
    cs "Mostly because it's not real cheese..."
    show cs coat worried
    pause 1.0
    show cs coat happy
    cs "Not that {i}I'm{/i} complaining!"

    show spray_cheese at manual_pos(0.4, 0.4) with Dissolve(0.25)
    show spray_cheese at manual_pos(0.5, 0.8) with MoveTransition(0.25)
    hide spray_cheese with dissolve
    $ collect("spray_cheese")

    pause 1.0
    n "CS yoinks some spray cheese."
    pause 1.0
    "..."
    show cs coat disappointed
    cs "Alright, CS, stay focused."
    hide cs
    hide shopping_cart
    with moveoutright
    pause 1.0

    scene tgt_chips with dissolve
    pause 1.0
    show cs coat at center
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with moveinleft

    n "The next few aisles don't hold much for CS beyond some content for observational comedy."
    show cs coat surprised
    cs "\"3D\" Doritos? I'm pretty sure {i}all{/i} Doritos are 3D. Would be pretty hard to eat them, otherwise."
    show cs coat disappointed
    cs "You know, I think they're making these bags of chips smaller and smaller, too."
    show cs coat worried
    cs "\"Family Size\"? {i}\"Party{/i} Size\"? Are you serious?"
    cs "I can eat one of these all by myself, and I don't {i}feel{/i} like I'm eating enough for a whole family or party..."
    cs "It would take a whole lot more than one bag to feed {i}this{/i} party, too!"
    show cs coat scared
    cs "How small do they expect these families or parties to even {i}be?"
    show cs coat disappointed
    cs "Who knows. Gotta love capitalism."
    show cs coat flipped at left with move
    pause 1.0
    show cs coat happy flipped
    cs "Gotta love Pringles, too."

    show pringles at manual_pos(0.075, 0.4) with Dissolve(0.25)
    pause 0.5
    show cs coat at center
    show pringles at manual_pos(0.6, 0.4)
    with move
    pause 0.5
    show pringles at manual_pos(0.7, 0.8) with MoveTransition(0.25)
    hide pringles with dissolve
    $ collect("pringles")

    n "CS grabs a can of his favorite flavor before moving on to the next aisle."
    show cs coat with determination
    pause 0.5
    hide cs 
    hide shopping_cart
    with moveoutright
    
    scene tgt_shelf with dissolve
    show cs coat at mid_left
    show shopping_cart at manual_pos(0.5, 1.1, 0.5)
    with moveinleft  
    n "Finally, CS stumbles upon something that was actually on his shopping list."
    cs "Genergy, of course. Always need that."
    show cs coat disappointed
    cs "Walmart usually has a better deal on these, but, {i}gosh,{/i} I hate going there."
    show cs coat happy
    cs "And, I'm gonna need a {i}lot{/i} of Genergy to get through all this party prep!"

    # TODO: BUG: THIS IS NOT PLAYING FOR SOME 
    
    show genergy at manual_pos(0.4, 0.3) with Dissolve(0.25)
    show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.25)
    $ collect("genergy")

    show genergy at manual_pos(0.4, 0.3) with Dissolve(0.25)
    show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.25)

    show genergy at manual_pos(0.4, 0.3) with Dissolve(0.25)
    show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.25)

    show genergy at manual_pos(0.4, 0.3) with Dissolve(0.25)
    show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.25)

    show genergy at manual_pos(0.4, 0.3) with Dissolve(0.25)
    show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.25)

    # just want him to get A LOT of genergy lmfao - tate

    if fun_value(FUN_VALUE_COMMON):
        # Roger that, Tate -- Digi
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)
        show genergy at manual_pos(0.4, 0.3) with Dissolve(0.05)
        show genergy at manual_pos(0.55, 0.8) with MoveTransition(0.05)

    scene tgt_tree with dissolve
    show cs coat flipped at mid_right_right
    show shopping_cart flipped at manual_pos(0.7, 1.1, 0.5)
    with moveinright
    pause 2.0

    n "After clearing out the stock of Genergy, CS continues on to another area of the store."

    show cs coat disappointed
    cs "Jeez, there sure are a lot of people out today..."
    show cs coat worried
    cs "I guess that's what I get for leaving shopping until the last minute."
    cs "But, I guess I {i}am{/i} the same man known for uploading videos at 11:59 PM on the 31st, so I should be used to this sort of thing."
    show cs coat disappointed
    cs "At least everyone here seems polite. They probably just want to get what they need and get out, too."

    show pomni at offscreenleft
    show shopping_cart as second at manual_pos(-0.5, 1.1, 0.5)
    with determination

    show cs coat disappointed at mid_right
    show shopping_cart flipped at manual_pos(0.5, 1.1, 0.5)
    show pomni flipped at mid_offscreen_left
    show shopping_cart as second at manual_pos(0.2, 1.1, 0.5)
    with move
    show cs coat scared
    show pomni eyes flipped
    with hpunch

    n "CS nearly runs his cart right into another."
    show cs coat worried
    cs "Oh, I'm so sorry!"
    show pomni concern
    pomni "Oh, uh... i-{w=0.1}it's o-okay! Y-{w=0.1}You probably just didn't see me--"
    show pomni think
    pomni "Wait, aren't you that guy from IKEA?"
    show cs coat scared
    cs "Huh?!"
    show cs coat worried
    cs "I haven't been to IKEA in a long time..."
    show pomni eyes flipped
    "..."
    n "The clown girl looks visibly distressed."

    show pomni concern
    pomni "But... how?!"
    pomni "You {i}really{/i} don't remember me?"
    show pomni think flipped
    pomni "Is this what that {color=#FFDBFC}time traveler{/color} was talking about?"
    show cs coat scared
    cs "What are {i}you{/i} talking about?!"
    show pomni concern
    pomni "I'm... just going to head out now! Lots of {i}very{/i} important..."
    show pomni concern flipped
    pause 0.5
    show pomni concern
    n "Pomni glances at her surroundings."
    show pomni flipped
    pomni "... Shopping to do! Yeah! I just love, uh... capitalism?"
    show cs coat worried
    cs "Wait, what do you mean by--{w=0.5}{nw}"
    show pomni concern
    pomni "Gotta run! Bye!"
    play sound sfx_whoosh
    show pomni concern flipped at offscreenright behind cs with MoveTransition(0.25)
    n "Pomni dashes away, leaving her empty cart behind."
    pause 0.5
    show cs coat disappointed
    cs "That was... odd."
    cs "You don't see a lot of weirdos like that at Target."
    cs "I guess this place is more like Walmart than I thought."
    show cs coat surprised flipped
    cs "Guess I have a lookalike who shops at IKEA, too?"
    show cs coat flipped
    cs "Oh, well. I should probably also get back to shopping."
    
    hide cs
    hide shopping_cart
    with moveoutleft

    scene tgt_tech with dissolve
    show cs coat flipped at right 
    show shopping_cart flipped at manual_pos(0.6, 1.1, 0.5)
    with moveinright 
    n "CS passes by the electronics section."
    cs "Okay, I don't need anything there."
    show cs coat surprised flipped
    cs "Buuuuuut..."
    cs "I mean, I can't {i}not{/i} see what they have on display."

    n "CS spots the Nintendo Switch demo display, featuring {i}Tetris 99,{/i} all ready to play."
    cs "Okay, that's the universe just {i}asking{/i} me to play a round."

    # TODO: lmao, are we gonna put a tetris minigame here?
    # EDIT: Maybe. -- Digi

    show cs coat happy flipped at left with move
    n "CS steps over to the display."

    # hey check out this neat trick - tate
    show black with dissolve
    centered "Way more than one round later..."
    hide black with dissolve

    n "CS finally realizes how much time has passed."
    # i changed this because CS has not actually picked up anything cold yet, so nothing would be condensating - tate

    show cs coat scared flipped
    cs "Oh, shoot!" with hpunch
    cs "Right! I need to actually accomplish things today!"
    show cs worried coat at right with move
    show cs worried coat flipped with determination
    pause 0.25

    hide cs
    hide shopping_cart
    with moveoutleft

    scene tgt_dairy with dissolve
    pause 0.5
    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    with moveinleft

    n "Still thinking about that last {i}Tetris{/i} match, CS approaches the cold items."

    pause 1.0
    show cs coat disappointed
    cs "This meal is going to take {i}so{/i} much butter..."
    show cs coat happy
    cs "Well, if there's one thing I learned about cooking from Paula Deen, it's that {i}everything's{/i} better with butter!"
    show cs coat worried
    cs "... And, that Paula Deen is scary. I learned {i}that,{/i} too."
    show cs coat happy
    cs "Good thing she's not attending {i}this{/i} party!"
    show cs coat

    show butter at manual_pos(0.4, 0.3) with Dissolve(0.25):
        zoom 0.5
    show butter at manual_pos(0.3, 0.8) with MoveTransition(0.25)
    $ collect("butter")

    show butter at manual_pos(0.4, 0.3) with Dissolve(0.25):
        zoom 0.5
    show butter at manual_pos(0.3, 0.8) with MoveTransition(0.25)

    show butter at manual_pos(0.4, 0.3) with Dissolve(0.25):
        zoom 0.5
    show butter at manual_pos(0.3, 0.8) with MoveTransition(0.25)
    hide butter with dissolve
    pause 0.25

    hide cs
    hide shopping_cart
    with moveoutright

    scene tgt_frozen with dissolve

    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    with moveinleft

    n "CS finds the pies."
    show cs coat surprised
    cs "I probably don't need to buy too many of these..."
    show cs coat worried
    cs "There's already going to be so much food that I don't think everyone will even have {i}room{/i} for dessert!"
    show cs coat
    cs "I'll just grab two."

    show pie at manual_pos(0.5, 0.3) with Dissolve(0.25):
        zoom 0.5
    show pie at manual_pos(0.4, 0.8) with MoveTransition(0.25)
    $ collect("pie")

    show pie at manual_pos(0.5, 0.3) with Dissolve(0.25):
        zoom 0.5
    show pie at manual_pos(0.4, 0.8) with MoveTransition(0.25)
    hide pie with dissolve
    pause 0.25

    hide cs
    hide shopping_cart
    with moveoutright

    scene tgt_alcy with dissolve

    show cs coat at center
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with moveinleft

    n "Finally, CS lands in the alcohol section."
    cs "I know at least a few people I invited don't drink, but damn it, it's Christmas. I'm grabbing some 'nog!"

    show nog at manual_pos(0.8, 0.3) with Dissolve(0.25)
    show nog at manual_pos(0.7, 0.8) with MoveTransition(0.25)
    hide nog with dissolve
    $ collect("nog")
    pause 0.25

    hide cs
    hide shopping_cart
    with moveoutright

# Checkout
label ce_checkout:
    n "CS heads over to the checkout lanes."
    scene tgt_line
    show streetguy flipped at mid_right_right
    show amtrak_stewardess at mid_right
    show snufkin flipped at mid_mid_right
    show customer at center
    with dissolve
    play music winter_unclearance_sale if_changed loop volume 0.3 fadein 1.0

    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    with moveinleft

    pause 1.0
    show cs coat disappointed
    cs "Wait, what?"
    show cs coat angry
    cs "There are no lanes open! How the hell am I supposed to check out?"
    show cs coat disappointed
    cs "Oh, wait... I guess self-checkout is open..."

    show cs coat disappointed at mid_left
    show shopping_cart at manual_pos(0.5, 1.1, 0.5)
    with moveinleft

    n "CS joins the queue wrapped around the self-check area."
    cs "Man, this place is really short staffed, especially for the holidays!"
    show customer flipped
    customer "They're always like this. I come here every day, and it seems like there are fewer and fewer people working."
    show cs coat worried
    cs "Yikes, I wonder why..."

    play sound sfx_target_beep volume 0.5
    hide streetguy with moveoutright
    show amtrak_stewardess at mid_right_right
    show snufkin flipped at mid_right
    show customer at mid_mid_right
    with move
    show cs coat at center 
    show shopping_cart at manual_pos(0.7, 1.1, 0.5)
    with move

    pause 2.0

    play sound sfx_target_beep volume 0.6
    hide amtrak_stewardess with moveoutright
    show snufkin flipped at mid_right_right
    show customer at mid_right
    with move
    show cs coat at mid_mid_right
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with move

    pause 2.0

    play sound sfx_target_beep volume 0.7
    hide snufkin flipped with moveoutright
    show customer at mid_right_right with move
    show cs coat at mid_right
    show shopping_cart at manual_pos(1.0, 1.1, 0.5)
    with move

    pause 3.0

    play sound sfx_target_beep volume 0.8
    hide customer with moveoutright
    show cs coat at mid_right_right
    show shopping_cart at manual_pos(1.2, 1.1, 0.5)
    with move
    pause 2.0

    cs "Finally, my turn..."

    stop music fadeout 10.0
    play sound2 sfx_tgt_bg fadein 3.0
    scene tgt_checkerror with dissolve
    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    with moveinleft

    n "CS sees an error on the display."
    show cs coat disappointed
    cs "Welp, can't use that one!"
    hide cs 
    hide shopping_cart
    with moveoutright
    n "He moves on to try the next machine."

    scene tgt_checkout with dissolve
    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    with moveinleft
    pause 1.0

    show butter at manual_pos(0.4, 0.8) with Dissolve(0.25):
        zoom 0.5
    show butter at manual_pos(0.4, 0.6) with MoveTransition(0.25)
    play sound sfx_target_beep
    pause 0.5
    scene tgt_checkout_scanning
    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show butter at manual_pos(0.4, 0.6):
        zoom 0.5
    pause 0.5
    scene tgt_checkout_scan_twice
    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show butter at manual_pos(0.4, 0.6):
        zoom 0.5
    play sound sfx_scan_twice
    n "As CS starts scanning his items, the machine responds with a disapproving beep."
    show cs coat worried
    cs "What? It says I scanned this twice? No, I didn't!"
    show cs coat disappointed
    show pakoo tgt at mid_right with moveinright
    tgt_worker "Oh, yeah, it always does that. Just keep going, it's fine."
    show cs coat
    cs "Okay."
    scene tgt_checkout_scanning
    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show butter at manual_pos(0.4, 0.6):
        zoom 0.5
    show pakoo tgt at mid_right
    show pakoo tgt flipped with determination
    hide pakoo tgt with moveoutright

    show butter at manual_pos(0.7, 0.6) with move
    hide butter with dissolve

    show butter at manual_pos(0.4, 0.8) with Dissolve(0.25):
        zoom 0.5
    show butter at manual_pos(0.4, 0.6) with MoveTransition(0.25)
    # don't scan this one, he already scanned one twice.
    show butter at manual_pos(0.7, 0.6) with move
    hide butter with dissolve

    show butter at manual_pos(0.4, 0.8) with Dissolve(0.25):
        zoom 0.5
    show butter at manual_pos(0.4, 0.6) with MoveTransition(0.25)
    play sound sfx_target_beep
    show butter at manual_pos(0.7, 0.6) with move
    hide butter with dissolve

    show pie at manual_pos(0.4, 0.8) with Dissolve(0.25):
        zoom 0.5
    show pie at manual_pos(0.4, 0.6) with MoveTransition(0.25)
    play sound sfx_target_beep
    show pie at manual_pos(0.7, 0.6) with move
    hide pie with dissolve

    show pie at manual_pos(0.4, 0.8) with Dissolve(0.25):
        zoom 0.5
    show pie at manual_pos(0.4, 0.6) with MoveTransition(0.25)
    play sound sfx_target_beep
    pause 0.25
    show cs coat disappointed
    play sound sfx_target_beep
    pause 0.5

    cs "Ah, crap. I {i}definitely{/i} scanned this one too many times."
    n "The worker comes back."
    show pakoo tgt at mid_right with moveinright
    show pakoo tgt happy with determination
    tgt_worker "Hello, what's wrong?"
    cs "Sorry, I scanned this pie twice."
    show pakoo tgt think
    tgt_worker "... How many do you have?"
    cs "Just the two."
    show pakoo tgt confused
    tgt_worker "Wh-- okay, hold on."
    show pakoo tgt at center with move
    show pakoo tgt tap
    pause 0.5
    scene tgt_checkout_tm
    show cs coat disappointed at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show pie at manual_pos(0.4, 0.6):
        zoom 0.5
    show pakoo tgt scan
    play sound sfx_zebra_scan
    pause 0.5
    show pakoo tgt tap
    pause 2.5
    scene tgt_checkout_scanning
    show cs coat disappointed at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show pie at manual_pos(0.4, 0.6):
        zoom 0.5
    show pakoo tgt tap
    show pakoo tgt at mid_right with move
    tgt_worker "There you go."
    show cs coat
    cs "Thanks!"
    show pakoo tgt flipped with determination
    hide pakoo tgt with moveoutright
    show cs coat angry
    cs "Hey, wait a minute!"
    show pakoo tgt at mid_right with moveinright
    tgt_worker "Yeah?"
    cs "These are ringing up as $11.99 per pie!" # TODO: y'all, these pies are only $5.69 each normally, should we fix this? - tate
    show pakoo tgt upset
    cs "The sign said they were, like, 20%% off!"
    show pakoo tgt think2
    tgt_worker "Hmm..."
    show pakoo tgt scan
    play sound sfx_zebra_scan
    n "The employee scans the pie."
    show cs coat disappointed
    show pakoo tgt
    tgt_worker "Do you perchance have Target Circle?" # who just says perchance?? are you sure about this line??? - tate
    # Listen, Pakoo wrote it, and it's his dialouge, so. -- Digi
    cs "No?"
    show pakoo tgt think2
    tgt_worker "You need Target Circle to get this deal, sorry."
    menu:
        "Sign up for Target Circle?"
        "Yes":
            # NOTE: I don't think we need to do anything special for this check in CE. We can have it change the story more in DX. - pak
            $ got_target_circle = True
            cs "Alright, fine. How do I sign up? Is it through the Target app?"
            show pakoo tgt happy
            tgt_worker "Yeah, just install the app, set up an account, and you can get a bunch of deals in the store."
            cs "Okay, I can do that real quick."

            # stolen from train dialogue shhhh - tate
            show cs_phone flipped with MoveTransition(0.25):
                xpos 0.25
                ypos 0.65
                alpha 0.0
                parallel:
                    linear 0.25 alpha 1.0
                parallel:
                    linear 0.25 ypos 0.45
    
            pause 2.0
            show cs coat worried
            cs "Damn, the internet is {i}terrible{/i} in here!"
            tgt_worker "Yeah, I don't ever use the wi-fi here. It's so bad."
            tgt_worker "Anyway, once you're done, you just go to your wallet, and you scan that barcode!"
            show cs coat
            cs "Thanks."
            
            show cs_phone at manual_pos(0.35, 0.5) with move
            play sound sfx_target_beep
            pause 0.5
            hide cs_phone with dissolve
            pause 0.5
            tgt_worker "Have a good day."
        "No":
            show cs coat angry
            show pakoo tgt upset
            cs "Really?"
            tgt_worker "I'm sorry, but, that's just how the deal works."
            show cs coat disappointed
            cs "Fine, whatever. I'll just pay full price."

    show pakoo tgt flipped with determination
    hide pakoo tgt with moveoutright

    show pie at manual_pos(0.7, 0.6) with move
    hide pie with dissolve

    show pringles at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show pringles at manual_pos(0.4, 0.5) with MoveTransition(0.25)
    play sound sfx_target_beep
    show pringles at manual_pos(0.7, 0.5) with move
    hide pringles with dissolve

    show spray_cheese at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show spray_cheese at manual_pos(0.4, 0.5) with MoveTransition(0.25)
    play sound sfx_target_beep
    show spray_cheese at manual_pos(0.7, 0.5) with move
    hide spray_cheese with dissolve

    show bread at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show bread at manual_pos(0.4, 0.5) with MoveTransition(0.25)
    play sound sfx_target_beep
    show bread at manual_pos(0.7, 0.5) with move
    hide bread with dissolve
    
    show potato_bag at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show potato_bag at manual_pos(0.4, 0.5) with MoveTransition(0.25)
    play sound sfx_target_beep
    show potato_bag at manual_pos(0.7, 0.5) with move
    hide potato_bag with dissolve

    show potato_bag at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show potato_bag at manual_pos(0.4, 0.5) with MoveTransition(0.25)
    play sound sfx_target_beep
    show potato_bag at manual_pos(0.7, 0.5) with move
    hide potato_bag with dissolve

    if got_tato_bag == True:
        show tato_bag at manual_pos(0.4, 0.8) with Dissolve(0.25)
        show tato_bag at manual_pos(0.4, 0.5) with MoveTransition(0.25)
        play sound sfx_target_beep
        show tato_bag at manual_pos(0.7, 0.5) with move
        hide tato_bag with dissolve
    else:
        show potato_bag at manual_pos(0.4, 0.8) with Dissolve(0.25)
        show potato_bag at manual_pos(0.4, 0.5) with MoveTransition(0.25)
        play sound sfx_target_beep
        show potato_bag at manual_pos(0.7, 0.5) with move
        hide potato_bag with dissolve

    show nog at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show nog at manual_pos(0.4, 0.5) with MoveTransition(0.25)
    play sound sfx_target_beep
    scene tgt_checkout_id
    play sound sfx_idcheck
    show cs coat worried at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show nog at manual_pos(0.4, 0.5)
    n "As CS scans his alcohol, the machine buzzes at him. An on-screen message is requesting an ID."
    show cs coat pissed
    cs "Seriously?!" with vpunch
    show cs coat angry
    n "The employee runs over again."
    show pakoo tgt upset at mid_right with moveinright
    tgt_worker "Oh, yeah. I should probably do that for you."
    show pakoo tgt upset at center with move
    show pakoo tgt tap
    scene tgt_checkout_tm
    show cs coat angry at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show nog at manual_pos(0.4, 0.5)
    show pakoo tgt scan
    play sound sfx_zebra_scan
    pause 0.5
    show pakoo tgt tap
    pause 2.5
    show pakoo tgt
    n "The employee signs into the machine and opens the prompt to enter a number."
    n "They then wait patiently for CS."
    cs "What? Do you need something from me?"
    show pakoo tgt think2
    tgt_worker "Yeah, I need to check your ID."
    show cs coat pissed
    show pakoo tgt upset
    cs "Are you kidding me?"
    tgt_worker "Sorry, you legally can't buy this if you don't show ID."
    show cs coat disappointed
    n "CS sighs."

    show cs_wallet with MoveTransition(0.25):
        zoom 0.2
        xpos 0.15
        ypos 0.65
        alpha 0.0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.6
    $ collect("cs_wallet")

    pause 1.0

    show cs_id at manual_pos(0.2, 0.6) with dissolve:
        zoom 0.25
    $ collect("cs_id")
    
    show cs_id at manual_pos(0.3, 0.5) with move
    cs "Here you go."
    show pakoo tgt tap
    n "The worker punches in CS' birthdate before handing the card back."
    show cs_id at manual_pos(0.2, 0.6) with move

    show pakoo tgt flipped with determination
    hide pakoo tgt with moveoutright
    hide cs_id
    hide cs_wallet
    with dissolve
    scene tgt_checkout_scanning
    show cs coat disappointed at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show nog at manual_pos(0.4, 0.5)
    show nog at manual_pos(0.7, 0.5) with move
    hide nog with dissolve

    show genergy at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show genergy at manual_pos(0.4, 0.5) with { "master" : MoveTransition(0.25) }
    play sound sfx_target_beep
    show cs coat angry
    cs "Kids these days, asking me for my ID..."
    show genergy at manual_pos(0.7, 0.5) with move
    hide genergy with dissolve

    show genergy at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show genergy at manual_pos(0.4, 0.5) with { "master" : MoveTransition(0.25) }
    play sound sfx_target_beep
    show cs coat pissed
    cs "I'm {i}clearly{/i} an adult!"
    show genergy at manual_pos(0.7, 0.5) with move
    hide genergy with dissolve

    show genergy at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show genergy at manual_pos(0.4, 0.5) with { "master" : MoveTransition(0.25) }
    play sound sfx_target_beep
    cs "They should hire some new people!"
    show genergy at manual_pos(0.7, 0.5) with move
    hide genergy with dissolve

    show genergy at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show genergy at manual_pos(0.4, 0.5) with { "master" : MoveTransition(0.25) }
    play sound sfx_target_beep
    show cs coat worried
    cs "At least they don't card for {i}energy drinks!" # some places do! hell, i even got carded for SHARPIES once! - tate
    show genergy at manual_pos(0.7, 0.5) with move # In England they do I think - pak
    hide genergy with dissolve  # tate, don't snorf sharpies - digi

    show genergy at manual_pos(0.4, 0.8) with Dissolve(0.25)
    show genergy at manual_pos(0.4, 0.5) with { "master" : MoveTransition(0.25) }
    play sound sfx_target_beep
    show cs coat
    cs "Cool, that's everything."
    show genergy at manual_pos(0.7, 0.5) with move
    hide genergy with dissolve

    show cs coat at mid_mid_right with move
    show cs coat flipped
    scene tgt_checkout_circle
    show cs coat flipped
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    pause 1.5
    scene tgt_checkout_pay
    show cs coat flipped
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show cs_wallet with MoveTransition(0.25):
        zoom 0.2
        xpos 0.4
        ypos 0.65
        alpha 0.0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.6
    pause 2.0

    # List of items: 5lb bags of potatoes (3x), bread (x1), spray cheese (x1), pringles (x1), genergy (x5), butter (x3), pie (x2), eggnog (x1)

    play sound sfx_moneyfalls
    show spent_target at t_fake_rpg_text(0.5, 0.1, 0.5)
    # TODO: find the sfx that's like "ding-ding-DING~!" when you pay on these machines
    # TODO: the total should be actually closer to $75.37. if CS gets target circle here, should we display a different total? - tate
    # The $81.88 is the closet price we can make and keep up the "every price in the game has had 188 in it" joke. -- Digi

    n "CS pays with his card before heading out to the car."
    hide cs_wallet with dissolve
    show cs coat flipped at left with move
    scene tgt_checkout_finish
    show cs coat flipped at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show cs coat with determination
    pause 0.25
    hide cs
    hide shopping_cart
    with moveoutright
    
    stop sound fadeout 3.0
    stop sound2 fadeout 3.0
    scene black with dissolve
    scene tgt_outside
    with dissolve
    pause 0.5

    show cs coat hat
    show shopping_cart at manual_pos(0.7, 1.1, 0.5)
    with moveinleft
    pause 1.0

    cs "I'd better go straight home and put everything away."
    show cs coat hat happy
    cs "Tomorrow's the big day! This is gonna be the best party {i}ever!"
    hide cs
    hide shopping_cart
    with moveoutright
    pause 2.0
    play sound sfx_driving
    scene black with Dissolve(5.0)
    stop sound fadeout 4.0

label ce_aftershop:
    pause 2.0
    scene cs_kitchen
    show cs_kitchen_fg
    show d20:
        zoom 0.1
        xpos 1200
        ypos 820
    with dissolve
    pause 0.5
    play sound sfx_house_door_open
    pause 3.0
    play sound sfx_house_door_close
    pause 2.0
    show cs flipped at mid_right behind cs_kitchen_fg 
    show target_bags at right
    $ collect("target_bags")
    with moveinright
    n "When CS gets home, he walks to the kitchen to start putting groceries away."
    # TODO: am i REALLY gonna have to animate him putting every individual item away??? do i really have to????? - tate
    # We could just do a fade cut if you want? -- Digi
    "..."
    "..."
    "..."
    pause 0.5
    hide target_bags with dissolve
    pause 1.0
    show cs flipped at center behind cs_kitchen_fg with move
    # TODO: sfx knock it onto the floor
    show d20:
        zoom 0.1
        linear 0.1 rotate 165 xpos 1000 ypos 600
        linear 0.2 rotate 165 xpos 800 ypos 500
        linear 0.1 rotate 165 xpos 700 ypos 700
        linear 0.1 rotate 165 xpos 600 ypos 900
        linear 0.1 rotate 165 xpos 500 ypos 1100
    n "As he finishes up, a D20 sitting on the counter is knocked onto the floor."
    $ collect("d20")
    show cs disappointed flipped behind cs_kitchen_fg
    cs "What the hell?"
    show cs disappointed flipped with { "master": move }:
        parallel:
            linear 0.5 rotate -45
        parallel:
            linear 0.5 xpos 0.4
        parallel:
            linear 0.5 ypos 1.5
    cs "Since when did I ever own one of these?"
    pause 1.0

    n "CS picks up the die."

    show cs disappointed flipped with { "master": move }:
        parallel:
            linear 0.5 rotate 0
        parallel:
            linear 0.5 xpos 0.5
        parallel:
            linear 0.5 ypos 1.1
    show d20:
        zoom 0.1
        xpos 0.3 ypos 1100
        linear 0.5 xpos 0.4 ypos 600
    pause 2.5
    show cs flipped behind cs_kitchen_fg

    $ reroll()
    cs "Hey, look, I rolled a [d20]!"
    hide d20 with dissolve
    pause 1.0

    show cs flipped behind cs_kitchen_fg
    # repetitive on purpose - tate
    cs "Welp, the groceries are all put away..."
    cs "The decorations look all nice..."
    show cs happy flipped
    cs "I think I'm all ready for this party!"
    n "CS lets out a satisfied yawn."
    show cs
    cs "It's getting late. I should probably call it an early night."
    if fun_value(FUN_VALUE_COMMON):
        show cs disappointed
        cs "My sleep schedule's abysmal, but I {i}can't{/i} sleep {i}any{/i}time!"
    hide cs with moveoutright
    pause 0.5

    scene cs_bedroom2
    with dissolve
    pause 0.5

    show cs at mid_left with moveinleft
    show cs flipped with determination
    pause 0.5

    # totally stolen from archival shhh
    show cs happy flipped at manual_pos(160, 200)
    play sound sfx_blanket volume 10.0
    show cs happy flipped at manual_pos(160, 200):
        rotate 0
        parallel:
            linear 1.0 rotate 60
        parallel:
            linear 1.0 ypos 300
        parallel:
            linear 1.0 xpos -350
    
    pause 2.0
    show cs happy flipped
    n "CS settles in under the covers..."
    pause 2.0
    show cs concentrate flipped
    n "However, his mind won't let him rest."
    show cs disappointed flipped
    cs "I just can't stop thinking about tomorrow."
    show cs surprised flipped
    cs "I wonder who's gonna get here first, and if everyone will show up as promised..."
    pause 2.0
    show cs scared flipped
    cs "What if {i}no one{/i} shows up?"
    show cs disappointed flipped
    cs "That would suck a lot."
    show cs flipped
    cs "But, I don't think that'll happen."
    cs "Everyone confirmed they got my invitations, and they all said on the phone that they'll come!"
    show cs happy flipped
    cs "If nothing else, at least Anno is coming for sure!"
    pause 1.0
    show cs disappointed flipped
    cs "Okay, CS, stop thinking about all these what-ifs..."
    cs "You need to sleep!"
    show cs concentrate flipped
    scene black with Dissolve(2.0)
    n "After some time, CS finally dozes off..."
    $ in_d20_viewer = False
    jump ce_party_before


# TODO: basically all of these need sfx added for whatever vehicle they arrive in. - tate

label ce_party_before:
    scene cs_bedroom2
    show cs happy christmas
    with dissolve
    cs "Today is the day!"
    cs "Now I just have to wait for people to arrive!"
    show cs christmas flipped
    cs "I wonder who will arrive first?"
    if d20 == 1:
        n "CS waits paiently."
        n "He keeps on waiting."
        show cs disappointed christmas flipped
        cs "Alright, any minute now..."
        cs "The party starts in about 15 minutes, so people should start showing up soon..."
        n "CS keeps on waiting, but it looks like no one shows up early."
        jump after_d20      
    if d20 == 2:
        n "As CS asks himself this, a small car pulls up in the driveway."
        cs "Hmm, let's go see who that is!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show arceus dark flipped at mid_left
        show kitty festive dark at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        arceus "Hey, CS!"
        cs "Hey, Arc! Hey, Kitty!"
        kitty "What's up?"
        cs "Well, Merry Christmas, guys! I'm glad you could travel back here for this!"
        arceus "No problem! I mean, after everything we went through, how could I not?"
        cs "Yeah, well, should we get inside? It's pretty cold out."
        kitty "Well, we are rather warm, but yeah."  # british + furry = well equipped for cold
        kitty "Let's go inside."
        jump after_d20      
    if d20 == 3:
        n "CS peers out the window to see Anno's car pull into the driveway."
        cs "Hey, look at that! Anno's here first!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show anno festive dark at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        anno "Hey, CS!"
        anno "I showed up kinda early, but I wanted to see everyone's initial reactions of our decor work!"
        cs "Well, I'm glad you showed up. Come inside! It's cold out."
        jump after_d20      
    if d20 == 4:
        n "All of a sudden, CS hears a futuristic-sounding vehicle land outside."
        show cs disappointed christmas flipped
        cs "What the hell is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show digi dark flipped at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        show digi happy dark flipped
        digi "Hey, CS! How've you been?"
        show digi dark flipped
        cs "Hey, Digi! I didn't know you had a... spaceship?"
        digi "Oh yeah, this old thing. It's a bit of a nugget but it gets the job done."
        cs "Why have I never seen this before?"
        digi "Was never coming from space before."
        pause 0.5
        show digi shock dark flipped with hpunch
        n "Digi shudders from the temperature."
        digi "It's cold out. Can we go inside?"
        cs "Yeah, let's go."
        jump after_d20
    if d20 == 5 or d20 == 6:
        n "As soon as he says that, he feels the house start to shake."
        show cs disappointed christmas flipped
        cs "Wh--{w=0.5} what's going on?"
        show cs worried christmas flipped
        n "As the house shakes even faster, a loud train whistle bellows out."
        # TODO: SFX train whistle
        cs "Holy shit, is that a {i}train?!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show tate festive dark flipped at mid_left
        show mean human dark flipped at left
        with dissolve
        show cs worried christmas dark flipped at right with moveinright
        cs "That {i}is{/i} a fucking train!"
        tate "Hey, CS! How've you been?"
        cs "Tate? Hey! I've been great!"
        mean "Hey, CS, Merry Christmas!"
        cs "Merry Christmas to you too... Mean, right?"
        mean "Yup!"
        cs "Sorry, I've never seen you in person. Shall we get inside?"  # Does that help? -- Digi
        tate "Yeah!" (multiple = 2)
        mean "Yeah!" (multiple = 2)
        jump after_d20   
    if d20 == 7:
        n "CS notices a familiar blue car roll up onto the driveway."
        cs "Look at that! Looks like Billy is here first!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show billy festive dark at mid_left
        with dissolve
        show cs dark christmas flipped at right with moveinright
        billy "Hi! It's Billy!"
        billy "Merry Christmas!"
        cs "Merry Christmas to you too, Billy!"
        billy "Times like these make me wish I could still run commercials."
        billy "It's been hard to sell products by word of mouth, especially since I died that one time."
        cs "That sucks man, I hope this party cheers you up."
        billy "Let's get inside. It's freezing out here!"
        jump after_d20      
    if d20 == 8:
        n "All of a sudden, CS hears helicopter blades above his house."
        show cs worried christmas flipped
        cs "Woah, what the hell?!"
        n "A Blackhawk helicopter is seen landing out in the middle of the street."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show obama festive dark at mid_left
        with dissolve
        show cs dark christmas flipped at right with moveinright
        # wait, uh, can someone pls explain to me when they ACTUALLY met obama in CSB??? - tate
        n "The President of the United States steps out."
        obama "Hello, CS! Nice to meet you."
        cs "Obama?! I didn't think you would actually come!"
        obama "Well, I {i}have{/i} enjoyed your content, and when you sent an invitation to your Christmas party, I figured I could come visit for a while."
        obama "Besides, running the political circus has become tiring enough, I need a break."
        cs "Fair enough, I guess! Well, Mr. President, let's get inside and wait for the other guests."
        obama "Sure thing. It is very cold outside."
        jump after_d20
    if d20 == 9:
        play sound sfx_siren
        show blue_light at left
        show red_light at right
        n "Sirens start blaring outside."
        show cs worried christmas flipped
        cs "Uh oh! Why are the cops here?"
        n "CS rushes outside."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show copguy festive dark flipped at mid_left
        with dissolve
        show cs worried christmas dark flipped at right with moveinright
        copguy "Heya, CS. Did I scare you?"
        cs "Fuck, yeah, you did! I didn't think you were gonna be on duty!"
        copguy "Well, someone's gotta be security, right?"
        cs "I... guess?"
        cs "Whatever, let's get inside. I'm freezing!"
        jump after_d20      
    if d20 == 10:
        n "CS looks outside to see a bus pull up."
        cs "Hmm, I wonder who took the bus."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show sheriff festive dark flipped at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        sheriff "God damn it! Stupid damn wheels! Stuck in the snow!"
        cs "Woah, hey! Who are you, again?"
        sheriff "Who am I? I'm Copguy's boss, that's who!"
        sheriff "I asked him to pick me up, but apparently he had to go shopping or some shit!"
        sheriff "And I had to take the bus!"
        cs "Oh, wow, okay. Uhm, do you need help?"
        sheriff "{i}Yes!{/i} I keep getting stuck in the snow! Take me inside!"
        jump after_d20      
    if d20 == 11:
        n "A familiar sound like a laser beam is heard from outside."
        play sound sfx_beam
        hide cs with moveoutleft
        scene cs_house_snow_night
        show ed festive dark flipped at center
        show rich festive dark flipped at mid_left
        show wesley festive dark flipped at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "Hey guys! How have you been doing?"
        ed "We've been doing well! Our business has been profitable recently!"
        ed "Even Wesley has made a speedy recovery! He wasn't too happy about needing a metal rod installed into his back, though."
        show cs festive worried dark flipped
        cs "Yeah, I'm... uh..."
        cs "I'm really sorry about that. I still feel bad about taking things too far."
        n "Wesley stares at the ground and mutters."
        wesley "Yeah."
        rich "Well, why don't we get inside? It's freezing!"
        cs "Yeah, let's go!"
        jump after_d20      
    if d20 == 12:
        n "An old Dodge Charger pulls up on the driveway."
        cs "Nice car! I wonder if that's Carguy..."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show k22 dark flipped at left
        show k17 dark flipped at mid_left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Hey, it's... two Pakoos?"
        show k17 happy dark flipped
        k17 "CS!!!"
        show k17 dark flipped
        k22 "Hey, CS. Merry Christmas!"
        cs "Hi, so, umm..."
        cs "Are you guys {i}both{/i} Pakoo?"
        k22 "It's... kind of complicated."
        k22 "Let's go inside, then we can explain."
        jump after_d20      
    if d20 == 13:
        n "A teleport-like sound is heard outside."
        # TODO: sfx for that
        show cs disappointed christmas flipped
        cs "What in the world?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show aria festive dark flipped at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "Oh, hey! Aria, right?"
        aria "Yep, that's me!"
        aria "Goodness, am I too early?"
        cs "A little, but that's okay!"
        cs "I was hoping someone would arrive early."
        aria "Well then. Should we head inside? You're probably getting cold, I assume."
        cs "Yeah, it's kinda freezing out."
        jump after_d20      
    if d20 == 14:
        n "Someone's car pulls into the driveway."
        cs "I wonder who that could be?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show michael festive dark at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "Oh, hey, it's Michael!"
        cs "You're still visiting the United States? I thought you were only here for the summer!"
        michael "I decided to spend a whole year over here."
        michael "It's pretty cold out, innit?"
        cs "Yeah, let's get inside now."
        jump after_d20      
    if d20 == 15:
        n "CS sees Linus' car pulling up outside."
        cs "It looks like Linus got here first!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show linus festive dark at mid_left
        show luke festive dark flipped at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        linus "Hey, CS! Long time no see!"
        cs "You too, and Luke as well?"
        luke "Hey, man! I know we didn't talk much during your short employment, but it was fun having you around!"
        luke "Linus talks a lot about you."
        cs "Oh, really?"
        linus "I just think you're a funny guy!"
        linus "What wasn't funny was the cops showing up at LTT, but we can let bygones be bygones."
        cs "Yeah, sorry about all that. It's a long story."
        cs "Why don't we go inside, and I'll explain the whole thing while we wait."
        jump after_d20      
    if d20 == 16:
        n "Another Honda Civic shows up in CS' driveway."
        cs "Oh, look at that! It's Blank!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show blank dark flipped at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        blank "Hey, CS, how have you been?"
        cs "I've been doing well! Did you drive safe here?"
        blank "I did, but lots of people on the interstate sure didn't!"
        blank "I got quite a bit of dashcam footage if you want to watch some with me."
        cs "Sure thing! Let's get inside and watch while we wait for the others."
        jump after_d20      
    if d20 == 17:
        n "An unknown car shows up in the driveway."
        cs "I wonder who that is?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show nova dark flipped at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        nova "Hey, CS! Thanks for inviting me to your Christmas party!"
        cs "Yeah, sure thing!"
        cs "It's been a while. How've you been?"
        nova "Oh, y'know, I've been moving a lot, had my friend move in with me..."
        cs "Well, if you wanna chat about it, let's go inside first. It's cold out here."
        jump after_d20      
    if d20 == 18:
        n "CS sees a Cherokee pull up to his house."
        show cs disappointed christmas flipped
        cs "What the fuck? Who is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show elizabeth dark at center
        show anne dark at mid_left
        show grace dark at left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Hey, uhh..."
        eliza "Is this the right place?"
        cs "I think so!"
        cs "Are you..."
        eliza "I'm Elizabeth. Behind me is Anne and Grace."
        cs "You might have the wrong place. Sorry."
        eliza "Do you know a Mika? A Mikapara?"
        cs "Is that you?"
        eliza "Close enough."
        cs "Well, should we go inside."
        eliza "Yeah, I guess so."
        jump after_d20      
    if d20 == 19:
        n "An orange Mini Coooper shows up infront of CS' house."
        cs "Holy crap, is that who I think it is?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show db dark at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "DB! You're the first one here!"
        db "I am?!"
        cs "Yes! You managed to be the earliest this time!"
        db "Wow, I can't believe it!"
        cs "Yeah! Let's get inside and we can talk!"
        jump after_d20      
    if d20 == 20:
        n "A man in a white shirt walks up to CS' house."
        show cs disappointed christmas flipped
        cs "Who the hell is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show avgn dark flipped at mid_left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Hey, are you--"
        avgn "I'm the fuckin' Nerd!" with vpunch
        cs "The Angry Video Game Nerd?! I didn't invite you! At least, I don't {i}think{/i} I did..."
        avgn "It doesn't fucking matter! Merry fucking Christmas!"
        cs "Okay... Do you, uh, wanna go inside?"
        avgn "Hell yeah!"
        cs "Alright, then..."
        jump after_d20      
    else:
        n "CS waits paiently."
        n "He keeps on waiting."
        show cs disappointed christmas flipped
        cs "Okay, what's going on? I figured {i}someone{/i} would be early."
        n "CS looks out into the distance."
        cs "Wait, who is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show iris flipped at mid_left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Who the heck are you?"
        iris "Oh, hello."
        iris "It seems you rolled a..."
        n "Iris looks confused."
        iris "Um... a [d20]."
        cs "Rolled... like on a die?"
        iris "You rolled a D20 earlier, no?"
        cs "I did, but how did I roll on [d20] on a D20? That's not even a thing you {i}can{/i} roll!"
        cs "And, how did you know I did that?"
        iris "Ah, that's a lot to discuss. Shall we go inside? I'm sure you're rather cold."
        cs "I..."
        n "CS gives up trying to understand, for now."
        show cs christmas dark flipped
        cs "Sure."
        jump after_d20

    # TODO: TATE STOPPED EDITING HERE!

label after_d20:
    if in_d20_viewer:
        jump d20_viewer
    else:
        jump ce_introductions

# Introductions
label ce_introductions:
    scene black with dissolve
    n "By the time of the party, everyone shows up at CS' house in droves."
    scene cs_foyer_festive
    show cs christmas at left
    show anno festive at mid_left behind cs
    show aria festive at mid_mid_left behind anno
    show digi at center
    show tate festive flipped at mid_right
    with dissolve
    play music teeth_dust if_changed
    music teeth_dust
    cs "Well, it looks like everyone is here, right?"
    if d20 != 19:
        anno "DB isn't here yet, but other than that, yeah."
    else:
        anno "Looks like it, yeah."
    show tate sheepish festive flipped
    tate "There are... a lot of people here..."
    show digi thinking flipped
    digi "Yeah, I wonder where Arc and Kitty are..."
    show k17 happy at center
    show k22 at mid_mid_right behind k17
    with moveinright
    show tate shock festive flipped
    show digi happy flipped
    k17 "OMG! Hey, guys!"
    show k17 shock
    k17 "You guys all look so... different!"
    show k22 confident
    k22 "Hi, I'm his--"  # "handler." -- Digi
    show cs disappointed christmas
    k17 "CS, look how much you've grown!"
    show k22
    cs "Okay, why are there two Pakoos?"
    cs "...and you don't have green hair anymore again?"
    show k22 disappointed
    k22 "Oh boy, alright K-17, calm down for one second. I think everyone here needs an explanation."
    show k17
    show digi happy
    show tate festive flipped
    cs "Yes, please. I didn't want to say it, but it seems like everytime I meet you guys, your appearance always changes!"
    aria "Sorry."
    show digi sad
    digi "Did I change too much?"
    cs "No, no, just-- let Pakoo #2 speak."
    if fun_value(FUN_VALUE_RARE):
        show k17 disappointed
        k17 "Hey, where's Fyreee at?"
        show k22 angry
        k22 "Damn it, can you let me talk?"
        show k17
    else:
        show k22
        k22 "I'm gonna assume that's me."
    show digi
    show k22 confident
    k22 "Alright, so, I'm K-22, the physical manifestation of Pakoo's memories from the year 2022."
    show k22
    k22 "This is K-17, I'm sure you can figure out what year he is."
    show k17 happy
    k17 "Remember me? I'm the Sunny D guy!"
    n "CS groans."
    cs "Okay, so what about the green haired one?"
    show k17
    show k22 confident
    k22 "That's Addy, our boss. They run this archiving facility far away from here, and I guess they would be the closest version of Pakoo you know, but they aren't here right now."
    show k22 disappointed
    k22 "They are running their own Christmas party, which I wanted to be a part of, but this creature right here just {i}had{/i} to go this party,"
    k22 "And I have to make sure he doesn't get too crazy."
    cs "Great."
    cs "Is that it?"
    show k22
    k22 "I mean, I could go on, but I'd be here all night."
    show mean human at mid_offscreen_right with moveinright
    mean "Hey, what's going on here?"
    show mean human shocked
    show k17 flipped
    show k22 flipped
    mean "Wait, there's two Pakoos now?"
    show mean human annoyed
    show k22 confident flipped
    k22 "Okay, so--"
    show k22 flipped
    show tate sheepish festive flipped
    tate "I'll just tell him later."
    show tate festive flipped
    cs "Alright, well, I'll let you guys talk, I'm gonna check on the others."
    hide cs with moveoutright
    show k17 shock flipped
    k17 "So, who are you? Are you DigBick?"
    show mean human angry
    mean "What did you just call me?"
    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at right behind cs_kitchen_fg
    show ed festive at mid_right behind cs_kitchen_fg
    show michael festive at mid_mid_right behind cs_kitchen_fg
    show billy festive at mid_mid_left behind cs_kitchen_fg
    with dissolve
    show cs christmas at left with moveinleft
    cs "Hey guys, how are you all doing?"
    obama "Hello, CS, we are all preparing our meals for dinner tonight."
    obama "I'm going to make a carrot cake."
    if fun_value(FUN_VALUE_COMMON):
        show wm1:
            xpos -250
            ypos 980
            zoom 1.25
            linear 0.35 xpos 0 ypos 680 zoom 1.0
        with dissolve
        window hide
        pause 1.5
        show wm1:
            xpos 0
            ypos 680
            zoom 1.0
            linear 0.35 xpos -250 ypos 980 zoom 1.25
        pause 0.5
        billy "I'm gonna make some Big City Sliders!"
        show wm2:
            xpos -250
            ypos 980
            zoom 1.25
            linear 0.35 xpos 0 ypos 680 zoom 1.0
        with dissolve
        window hide
        pause 2.5
        show wm2:
            xpos 0
            ypos 680
            zoom 1.0
            linear 0.35 xpos -250 ypos 980 zoom 1.25
        pause 0.5
        michael "I've been thinking of preparing some mashed potatoes."
        show wm3:
            xpos -250
            ypos 980
            zoom 1.25
            linear 0.35 xpos 0 ypos 680 zoom 1.0
        with dissolve
        window hide
        pause 1.0
        show wm3:
            xpos 0
            ypos 680
            zoom 1.0
            linear 0.35 xpos -250 ypos 980 zoom 1.25
        pause 0.5
        cs "That all sounds great!"
        cs "What about you, Ed?"
        ed "Well, I think when it comes to cooking, it's just as good as my foundation repair skills."
        ed "I'm preparing a Christmas turkey for our feast."
        show wm4:
            xpos -250
            ypos 980
            zoom 1.25
            linear 0.35 xpos 0 ypos 680 zoom 1.0
        with dissolve
        window hide
        pause 0.5
        show wm4:
            xpos 0
            ypos 680
            zoom 1.0
            linear 0.35 xpos -250 ypos 980 zoom 1.25
        pause 0.5
    else:
        billy "I'm gonna make some Big City Sliders!"
        michael "I've been thinking of preparing some mashed potatoes."
        cs "That all sounds great!"
        cs "What about you, Ed?"
        ed "Well, I think when it comes to cooking, it's just as good as my foundation repair skills."
        ed "I'm preparing a Christmas turkey for our feast."
    cs "Damn! That sounds delicious!"
    if fun_value(FUN_VALUE_COMMON):
        cs "Hey Ed, can you make me a sandwich?"
        ed "{i}Noe!"
    cs "Well, I hope you are all doing great!"
    cs "I'm gonna go check everyone else!"
    show cs flipped with determination
    hide cs with moveoutleft
    scene cs_living
    show digi thinking flipped at left
    show linus festive at mid_left behind digi
    show luke festive at mid_left_left behind linus
    show blank at mid_right
    show nova at right
    with dissolve
    digi "So, this should go {i}here..."
    linus "No, you got the wrong cable!"
    luke "You idiots are both wrong! You're putting it in the wrong port!"
    digi "Ohhhhh..." (multiple = 2)
    linus "Ohhhhh..." (multiple = 2)
    show cs christmas flipped at center with moveinright
    cs "Hey guys! What are you guys doing?"
    show digi flipped
    digi "Oh, we are just trying to set up a projector to play movies on!"
    linus "Don't ask how this became a three-man job."
    show cs christmas
    cs "Well, what about you two?"
    blank "We are working on setting up the music."
    nova "The problem is, I don't really want to have Blank play his shitty music during the party."
    blank "Why? Not all of it's crazy shit, like yours is."
    show cs disappointed christmas
    show digi shock flipped
    nova "Shut the hell up!"
    show cs worried christmas
    cs "Woah, okay, calm down."
    show digi sad flipped
    show cs disappointed christmas
    cs "This is a Christmas party, after all. Let's try to have fun."
    show cs christmas flipped
    show digi flipped
    cs "I'm gonna go check on anyone else who is here."
    hide cs with moveoutleft
    scene cs_hallway
    show arceus flipped at mid_left
    show kitty festive at left
    with dissolve
    show cs christmas flipped at center with moveinright
    cs "Hey, how are you guys? I was looking all over and couldn't find you."
    arceus "Sorry, CS, we kind of got overwhelmed."
    kitty "We aren't the best with huge social gatherings."
    cs "Ah, it's okay. I'm just happy to get to talk to you guys."
    arceus "We'll be around when something important happens."
    show elizabeth at right
    show anne at mid_right
    show grace at mid_mid_right
    with moveinright
    eliza "Hey, what's up."
    show cs worried christmas
    grace "CS! You're that YTP guy!"
    show cs disappointed christmas
    cs "Uhm... who are you three?"
    eliza "Well, do you know Mika at all?"
    show cs angry christmas
    cs "I swear to God, are you guys like, memories or some shit as well?"
    eliza "Relax, no, we are just..."
    eliza "Just think of us as them I guess, yeah."
    # TODO: This should be explained better
    cs "You guys are so complicated."
    arceus "I mean, it wasn't too hard for me to figure out, funny enough."
    show cs disappointed christmas
    n "CS sighs."
    cs "I guess not, I'm just stressed out a bit."
    cs "I just really want this party to go well, and I feel like at this point I don't know half the people here."
    cs "I mean, you split into three people, Pakoo split into two..."
    eliza "I mean, if you want us to, we can step outside for a bit."
    cs "No, no, it's okay."
    cs "I hope you guys have fun, I'm gonna go back to the party."
    hide cs with moveoutright
    if d20 == 20:
        pause 1.0
        show avgn at center
        avgn "You guys ever heard of {i}Dr. Jekyll and Mr. Hyde{/i} for the NES?"
        eliza "Uhh, no?"
        avgn "Good, because it's fucking {i}ass!"
# Banter
label ce_banter:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "While the party starts up, Copguy and the sheriff get into a predicament."
    scene cs_living2_festive
    show wesley festive at right
    show rich festive at mid_right
    show db at center
    show copguy festive at mid_right
    show sheriff festive flipped at mid_left
    with dissolve
    play music dont_preheat_your_oven if_changed
    music dont_preheat_your_oven
    sheriff "Hey, Copguy!"
    copguy "I know, this party is great, right?"
    sheriff "No, I need to take a shit!"
    copguy "Okay, do you want me to tell everyone?"
    sheriff "Very funny, smartass! I need you to go with me."
    sheriff "My legs don't work, remember?"
    copguy "Damn it, this sucks."
    copguy "Alright, let's go."
    show copguy festive at left with move
    show copguy festive flipped with determination
    pause 0.5
    hide copguy
    hide sheriff
    with moveoutright
    scene cs_bathroom with dissolve
    show copguy festive flipped at left
    show sheriff festive flipped at mid_left
    with moveinleft
    pause 1.0
    show copguy festive flipped at center with move
    play sound sfx_door_jiggle volume 0.8
    n "Copguy jiggles the bathroom door."
    tate "Occupied!"
    show copguy festive
    copguy "Sorry, sir, we gotta wait."
    sheriff "This is the police! Open up!"
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show sheriff festive flipped at mid_left
    show copguy festive
    show tate cry festive
    hide tate with easeoutright
    tate "{i}Awawawawa!!!"
    copguy "Really?"
    sheriff "What? I really have to go!"
    copguy "Whatever, just go. I'll wait here."
    sheriff "What do you mean? You have to wait here with me!"
    sheriff "I can't get off and on the toilet myself! This bathroom isn't handicap-accessible!"
    copguy "I think this is the worst crime I've dealt with."
    show copguy festive at left behind sheriff with move
    show copguy festive flipped with determination
    pause 1.0
    show copguy festive flipped at mid_mid_left
    show sheriff festive flipped at center
    with move
    hide copguy
    hide sheriff
    with dissolve
    play sound sfx_house_door_close
    scene cs_bathroom
    copguy "Alright, but you better hurry! I don't wanna be in here all day!"
    scene cs_kitchen
    show cs_kitchen_fg
    show k17 flipped at left
    show obama festive at center behind cs_kitchen_fg
    show ed festive at mid_right behind cs_kitchen_fg
    show michael festive at mid_mid_right behind cs_kitchen_fg
    show billy festive at right behind cs_kitchen_fg
    with dissolve
    k17 "So Obama, how have you stayed President?"
    k17 "Aren't you on your what, like, fourth term?"
    if fun_value(FUN_VALUE_COMMON):
        obama "Ever heard of squatter's rights?"
        show k17 shock flipped
        k17 "You... can do that?"
        obama "I'm friggin' Obama, bitch! I can do what I want!"
    else:
        obama "Well, you see, we managed to somehow exhaust the list of succession back in 2018, and the house voted me back in."
        k17 "Huh, I see. That's pretty crazy."
        # What the actual fuck happened in 2018 by the way, I'm so curious
        # How the fuck did 50 hyper-important government officials get either killed or incapacitated?!
        # We need to get into this some time. -- Digi
    scene cs_living_signal
    show digi thinking flipped at left
    show linus festive at mid_left behind digi
    show luke festive at mid_left_left behind linus
    show cs disappointed christmas flipped at right
    with dissolve
    cs "Is this projector still not set up?"
    show digi angry flipped
    digi "No! The projector keeps giving me this really weird error!"
    linus "Not even I've seen this!"
    digi "Watch, I'll turn it on, and..."
    scene cs_living_error
    show digi angry flipped at left
    show linus festive at mid_left behind digi
    show luke festive at mid_left_left behind linus
    show cs disappointed christmas flipped at right
    play sound sfx_bluescreen
    show digi disappointed flipped
    rich "Hey, nice movie!"
    wesley "Looks like you'll have to set that up all over again."
    db "I got here early for this?"
    if d20 == 20:
        avgn "You know what's {i}bullll{/i}shit?"
        avgn "This movie, that's what!"
    ed "Hey guys, what movie are we watching?"
    wesley "Nothing until these bozos fix the projector!"
    luke "Okay hold on, I got an idea."
    show digi thinking flipped
    luke "Everyone step away from the projector."
    show digi thinking flipped at center
    show linus festive at mid_right
    with move
    show digi with determination
    n "After a little bit of tech magic, the projector comes to life."
    scene cs_living_elf
    show digi at center
    show linus festive at mid_right behind digi
    show luke festive at mid_left_left behind linus
    show cs disappointed christmas flipped at right
    play sound sfx_tada
    show digi shock
    luke "Ta-da!"
    rich "Finally, we can watch something."
    wesley "Are you 100-percent satisfied, Richard?"
    rich "Only about 80-percent."
    scene cs_foyer_festive
    show aria festive at mid_mid_left
    show tate festive sheepish flipped at mid_right
    show mean human at mid_offscreen_right
    show k22 flipped at left behind k17
    show k17 flipped at center
    with dissolve
    k17 "So, there's a new World Trade Center now?"
    show k22 disappointed flipped
    k22 "What do you mean? They finished that in like 2014!"
    k17 "Oh. Sorry, I forgot about that."
    show k22 flipped
    k17 "Okay, so, if big guy over there is DigBick..."
    show mean human angry
    show tate sheepish festive flipped
    mean "I'm not DigBick!"
    k17 "Are you DigBick's... girlfriend?"
    show tate sheepish blush festive flipped
    tate "What?"
    mean "No, first of all, I'm not fucking DigBick."
    show k17 disappointed flipped
    mean "I'm Mean, and this is Tate. We are friends."
    k17 "Yeah, you sound mean."
    show tate furious blush festive flipped
    tate "And I'm not a girl--!{w=0.25}{nw}" with vpunch
    show tate furious festive flipped
    show mean human annoyed
    show tate srs festive flipped
    show k17
    hide aria
    show aria festive at mid_mid_left
    k17 "What about you?"
    aria "Me? I'm Aria."
    show k17 shock
    k17 "Who?"
    show k22 confident flipped
    k22 "Uhh, well..."
    aria "I'm an old friend, the other one that wasn't Arceus? I got different."
    show k22 disappointed flipped
    k17 "Whaa?"
    k22 "Excuse us for a moment."
    show k22 disappointed flipped at Move((0.0, 0.14), (1.0, 0.14), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.4
    show k17 shock at Move((0.3125, 0.14), (1.0, 0.14), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 2.5
    scene cs_bathroom with dissolve
    copguy "{i}Please{/i} tell me that's it, I can't bear this anymore."
    sheriff "Yep, I'm done!"
    sheriff "Now, are you gonna help me wipe?"
    play sound sfx_walkie_on
    n "All of a sudden, Copguy's walkie goes off."
    walkie "Officer Copguy, we have a break-in at a house in the neighborhood you are currently at."
    walkie "Can you report on that?"
    copguy "Gladly! Give me a second and I'll be in my car."
    play sound sfx_walkie_off
    copguy "Sorry boss, as much as I would love to keep helping you, this is important."
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show sheriff festive
    show copguy festive flipped
    hide copguy with easeoutright
    sheriff "Wait! You can't just leave me here!"
    copguy "I'll just be a moment! Don't move."
    play sound sfx_house_door_close
    scene cs_bathroom
    sheriff "God damn it! {i}Get back here!"
    pause 3.0
    sheriff "\"Don't move.\" Thanks, Copguy, you're a real fucking comedian."
    scene cs_door_outside 
    show k17 disappointed flipped at mid_left
    show k22 disappointed at mid_right
    show snow1white
    show snow2white
    with dissolve
    k17 "This is so unfair!"
    k17 "CS said that it's annoying that we changed or whatever, but look at everyone else!"
    k17 "All of my friends have changed so much!"
    k22 "Yeah, well when you are constrained to one year of your life, that can happen."
    k17 "It's just, how do I like, change that?"
    k17 "I can't just change who I am!"
    show k22 confident
    k22 "Look, you don't need to. I probably should've told you about how people change and whatnot."
    k22 "Honestly, Addy should've told you, but they were probably too busy setting up their party."
    show k22 happy
    k22 "Speaking of which, do you want to go back home? Celebrate Christmas with Addy?"
    k17 "Hmm..."
    show k17 happy flipped
    show k22 disappointed
    k17 "No, I wanna stay here till the end!"
    show k17 flipped
    k17 "I'll just keep being myself, and try to keep more of an open mind. Thank you, K-22!"
    show k17 flipped at center with ease
    play sound sfx_house_door_open
    hide k17 with dissolve
    play sound sfx_house_door_close
    k22 "Damn it. It was worth a try."
    show k22 at mid_left with move
    show k22 flipped with determination
    k22 "I wonder how Addy is doing, anyway."
    play sound sfx_ring_once
    show k22 phone at mid_left with move
    n "K-22 hits up Addy."
    $ renpy.music.set_pause(True, "music")
    play music2 frollo_rave if_changed
    music frollo_rave
    show archival_5 at mid_offscreen_right
    show pakoo disappointed at mid_right
    with moveinright
    addy "HELLO??"
    k22 "Hey, uhh, how is it going over there?"
    addy "WHAT? I CAN'T HEAR YOU, THE MUSIC IS REALLY LOUD!"
    show k22 phone angry # TODO: hey pakoo this one still uses the old eyes - tate
    k22 "I WAS ASKING IF--{w=1.0}{nw}"
    addy "YEAH, I'LL CALL YOU LATER! HAVE FUN AT CS' PARTY!"
    play sound sfx_end_call
    hide archival_5
    hide pakoo
    with moveoutright
    stop music2
    $ renpy.music.set_pause(False, "music")
    show k22 angry flipped
    k22 "Motherfucker!"
    show snow3
    show snow4
    n "All of a sudden, the wind starts to pick up and snow begins to fall."
    show k22 disappointed flipped
    k22 "Brr... I should probably just get back inside and enjoy the party..."
    scene cs_bathroom with dissolve
    show k17 at mid_right with moveinright
    sheriff "Hey! Is someone there?"
    k17 "Huh?"
    sheriff "Hey, you! Can you help me out of here?"
    show k17 shock
    k17 "Uhh... uhh..."
    k17 "I'll go get someone!"
    hide k17 with easeoutleft

    # audio ducking
    # TODO: also why is elf_1 a movie file if it's not even on-screen...? - tate
    # It might be at some point on the screen -- Digi
    $ renpy.music.set_volume(0.25)
  
    scene cs_living2_festive
    show elf_1
    show wesley festive at right
    show rich festive at mid_right
    show db at center
    show cs christmas at left
    with dissolve
    rich "Oh, man, I love this part."
    show k17 shock at mid_mid_right with moveinright
    k17 "Hey, guys, uh-- how do I put this...?"
    k17 "The sheriff is stuck in the bathroom?"
    show cs disappointed christmas
    show k17 disappointed
    cs "Damn it, one second--"
    obama "CS! Are you there?"
    show cs christmas
    cs "Okay, let me do this first. The {i}president{/i} is calling!"
    hide cs with moveoutright
    
# Cooking
label ce_cooking:
    play music dont_preheat_your_oven if_changed
    scene cs_kitchen
    show cs_kitchen_fg

    # un-duck the audio
    $ renpy.music.set_volume(1.0)

    show obama festive at mid_right behind cs_kitchen_fg
    show michael festive at mid_offscreen_left behind cs_kitchen_fg
    show billy festive at left behind cs_kitchen_fg
    with dissolve
    show cs christmas at center behind cs_kitchen_fg with moveinleft
    cs "Hey, Mr. President, what do you need?"
    stop music fadeout 3.0
    music end
    obama "You can just call me Obama."
    obama "Second of all, I accidently cut myself while chopping these carrots."
    obama "What a fool I am."  # One of my favorite lines -- Digi
    show cs disappointed christmas
    cs "Oh my God, are you okay?"
    obama "Yes, I'm fine, but I need someone to keep cutting for me."
    obama "Can you do it for me?"
    show cs christmas
    cs "I guess I can, yeah."
    obama "Great, I just need a few more carrots cut up."
    obama "Give me a moment. I need a Band-Aid."
    hide obama with moveoutleft
    show cs christmas at mid_right with move
    cs "Alright, just a few carrots."
    cs "Let's do this."
    # TODO: Carrot Karate Chop Minigame
    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at center behind cs_kitchen_fg
    show michael festive at mid_offscreen_left behind cs_kitchen_fg
    show billy festive at left behind cs_kitchen_fg
    show cs christmas flipped at mid_right behind cs_kitchen_fg  
    with dissolve
    show smoke
    obama "Well, would you look at that?"
    obama "That was some mighty fine chopping, CS!"
    show cs happy christmas flipped
    cs "Woohoo!"
    cs "Thank you! Maybe I should cook more."
    show cs christmas flipped
    cs "Speaking of cooking, I can smell something... burning..."
    obama "It is perhaps the smoke bellowing from the oven?"
    show cs worried christmas flipped
    play sound sfx_smoke_alarm loop
    n "All of a sudden, the smoke detectors start beeping!"
    digi "Ahh! Turn it off!"
    nova "Damn it, Blank! I {i}said{/i} we weren't playing your music!"
    aria "Honestly, this is kind of a bop. Keep it going."
    if d20 == 20:
        avgn "Ahh! My ears!"
        avgn "What is this? The soundtrack from a LJN game?"
    show ed festive flipped at center behind cs_kitchen_fg with easeinleft
    ed "Nooooo!"
    ed "My turkey!"
    show bigsmoke with dissolve
    n "Ed opens up the oven, only to have even more smoke pour out."
    n "Everyone hacks and coughs as smoke fills the room."
    hide bigsmoke with dissolve
    stop sound
    n "When the smoke finally clears, Ed pulls out a blackened turkey."
    hide smoke with dissolve
    show cs christmas flipped
    play music snowdin_town
    music snowdin_town
    ed "Damn it! My roast is ruined!"
    billy "Not to fear, Ed! I made my famous restaurant mini-burgers!"
    show ed festive
    ed "You mean, steamed hams?"
    billy "Who the actual fuck calls burgers \"steamed hams?\""
    ed "It's a... regional dialect?"
    billy "..."
    billy "Steamed hams... for God's sake..."
    billy "You Texans are crazy."
    michael "I also have my mashed potatoes!"
    cs "Well, at least we still have somewhat of a Christmas dinner."
    hide ed with moveoutleft
    n "Ed sheepishly walks back into the living room after throwing away the turkey."
    cs "Obama, finish baking your cake, and we can start eating."
    cs "I'm gonna go check up on everyone while you do that."
    hide cs with moveoutleft
    scene cs_bathroom
    show grace at mid_left
    with dissolve
    sheriff "...and I had to take that job that left me the way I am."
    sheriff "I could've went to college, studied the paranormal..."
    sheriff "...started up a shower curtain business, run a newspaper business..."
    sheriff "...but no. I had to be a {i}cop."
    grace "Hey, are you almost done in there?"
    sheriff "Just leave me alone..."
    grace "But I really need to go!"
    sheriff "Find another bathroom."
    grace "But this is the only one in the house!"
    sheriff "In this mansion? There is only {i}one{/i} damn bathroom?!"
    show copguy festive flipped at center with moveinleft
    copguy "Hey, sorry, excuse me."
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show grace at mid_left
    show copguy festive flipped at center
    show sheriff festive at center behind copguy
    pause 1.0
    play sound sfx_house_door_close
    scene cs_bathroom
    show grace at mid_left
    copguy "Hey, boss! You won't {i}believe{/i} what I just experienced."
    copguy "This kid caught two burglars trying to rob his house with homemade traps!"
    copguy "It was so impressive, I probably would've fallen for some of them!"
    sheriff "That's great, can you get me off this toilet now?"
    sheriff "I've been thinking of signing my will here because of how long it's been!"
    copguy "Alright, let's get you out of here, old man."
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show grace at mid_left
    with determination
    show copguy festive at mid_right
    show sheriff festive at center behind copguy
    pause 1.0
    hide copguy
    hide sheriff
    with moveoutleft
    grace "Finally!"
    grace "Guys, the sheriff is out!"
    show grace at center with move
    hide grace with dissolve
    scene cs_bathroom
    show anne at mid_mid_left with moveinleft
    show rich festive at mid_left with moveinleft
    show kitty festive at mid_left_left with moveinleft
    show luke festive at left with moveinleft
    n "A line starts to form next to the bathroom."

    scene cs_hallway
    show arceus at mid_left
    show kitty at mid_right
    with dissolve
    kitty "Arcie, you're a fucking walnut."
    show arceus worried
    arceus "Huh? Where did that come from?"
    kitty "Dunno, just felt like calling you a walnut."
    show arceus happy
    arceus "Y'know, that's fair..."
    show arceus
    n "..."
    n "..."
    n "... Why hasn't the scene transitioned yet?"
    show arceus angry
    arceus "Because I'm not done yet, dipshit."
    n "... k."
    arceus "Isn't it weird how the first night of Hanukkah fell on Christmas day this year?"
    kitty "Yeah, that's pretty weird, innit?"
    arceus "Even weirder, when you think about it, next year will have two Hanukkahs."
    kitty "... How so?"
    arceus "Well, you figure, eight nights of Hanukkah."
    kitty "... Uh huh."
    arceus "And today's the 25th of December."
    kitty "... I see.."
    arceus "So the last night of Hanukkah would be the 2nd of January."
    kitty "... ... Shit, you right."

    # OK, is this scene too meta? I like it a lot but I'm worried I'm pushing the boundaries a bit here.
    scene cs_foyer_festive
    show aria festive at left
    show digi at center
    show arceus at right
    with dissolve
    arceus "Yeah, so to get the code done, I just got drunk off a bottle of wine and Digi and I chewed through it in a night."
    aria "Damn, that's the best way to do it."
    show digi thinking
    digi "I mean, {i}I{/i} was sober the whole time. I had to put up with this fluffy bastard."
    aria "Of course you were, I think a sip of wine would knock you flat."
    show digi goober
    digi "Hey, I'm not {i}that{/i} small."
    aria "Usually."
    show digi happy
    arceus "And you love putting up with this fluffy bastard."
    digi "While that's true, I think half of that night was spent coding, and the other half was spent confusing the names of four different bald dudes."
    arceus "To be fair, that was hilarious."
    digi "You got me there."
    show cs christmas at mid_left with moveinleft
    n "CS walks in on the conversation."
    cs "Hey guys! What are you all talking about?"
    digi "Oh, we were just discussing what developing the first game was li--"
    show digi shock
    n "Aria shoots a look at Digi, as much as she can do that in her current form."
    digi "Er, uh, just talking about a coding project we all worked on."
    cs "Oh, OK. Probably a bunch of stuff I wouldn't understand."
    show digi
    aria "Certainly not."
    show cs happy christmas
    cs "You guys do good work, though, I can't wait to see what the next DPN Games game will be!"
    show arceus worried
    arceus "Yeah, me too."
    hide cs with moveoutright
    n "CS walks off."
    show digi sad
    aria "You're going to have to get better at the whole \"not breaking the illusion\" thing, Digi."
    digi "What? He wouldn't have thought anything of it if you didn't stop me mid-sentence."
    show arceus
    arceus "We just need to be a little more careful than that."
    digi "Fair enough. Wouldn't want this place falling apart."
    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at mid_left behind cs_kitchen_fg
    show billy festive at mid_right behind cs_kitchen_fg
    with dissolve
    billy "So then I said: \"That's a resturaunt mini burger {w=1.0}{i}no one{/i} loves!"
    n "Obama laughs."
    obama "Billy, you crack me up. You're one of America's greatest."
    billy "That means a lot coming from you, Mr. President!"
    obama "Please, call me Barack."
    billy "The man in the suit always lurking behind you said if I do that, he'll kill me!"
    obama "He's just teasing. Isn't that right, Luther?"
    n "Luther says nothing and nods once."
    billy "Well then, thanks for the compliment, Barack!"
    obama "You gotta tell me the one about the cabinet full of cleaners again."
    show cs christmas at center with moveinleft
    n "CS walks in to greet the unlikely friends."
    cs "Obama, Billy! You two getting along?"
    obama "This guy's a hoot."
    billy "Barack here is a real nice guy!"
    cs "Well, that's great. Glad to see two people from different walks of life enjoying each other's company."
    obama "That's what Christmas is all about, isn't it?"
    billy "That's the power, of the holiday season!"
    show cs happy christmas
    cs "Well, I gotta go check on the others, you two have fun!"
    hide cs with moveoutright
    n "CS departs for the next room."
    billy "Right, so I said: \"you shittin' me?\""

label ce_mike:
    stop music fadeout 3.0
    music end
    scene cs_living2_festive
    show cs christmas at left
    show rich festive at center
    show ed festive at mid_right
    show grace at right
    with dissolve
    cs "Gee, that pizza I ordered sure is taking its time!"
    play sound sfx_doorbell
    n "Just at that moment, the doorbell rings."
    cs "Well, tickle my ballsack! What great timing!"
    grace "CS... you can't just say stuff like that."
    n "CS moves to open the door."
    scene cs_foyer_festive with dissolve
    show cs christmas at left with moveinleft
    cs "Hey guys, the pizza is here!"
    n "CS opens the door to let the pizza person in."
    show mike at right with moveinright
    play music rice_and_wine
    music rice_and_wine
    mike "I'm Chinese."
    cs "Oh, my God! It's Mike, everyone, quick, come look at Mike!"
    show k17 flipped at mid_mid_right behind grace
    show grace at mid_right
    show obama festive at center behind grace
    show tate festive at mid_left
    show billy festive at mid_mid_left
    with moveinleft
    show k17 happy flipped
    k17 "Hey, it's Mike! How's it going, long time no see!"
    grace "Oh my God! I love you, Mike!"
    tate "What's up, Mike?"
    obama "Mike, remember when I pardoned you?"
    billy "This guy can sell pizza better than I can!"
    show tate festive flipped with determination
    hide tate
    hide billy
    with moveoutleft
    show obama festive at mid_left behind cs
    show k17 at mid_mid_left
    show grace at center
    with move
    show k17 flipped with determination
    arceus "What's going on in here?"
    show arceus angry flipped at mid_mid_right with moveinleft
    show cs happy christmas
    cs "It's Mike, Arceus! Mike the Pizzapotamus!"
    show cs christmas
    show arceus angry
    arceus "Who?"
    grace "How do you not know who Mike the Pizzapotamus is?"
    obama "I mentioned him in my re-election speech!"
    cs "The children love him! He's the best in the world!"
    show arceus worried
    arceus "Yeah, I guess he's not... ringing a bell?"
    show k17 disappointed flipped
    k17 "He works at the bus stop, dude!"
    arceus "You mean the bus station?"
    grace "No, the bus stop!"
    arceus "Oh, so he drives the bus?"
    show cs angry christmas
    "Everyone" "No! The bus stop!"  # TODO: Make this a character, so it has a beep
    mike "You really don't know me, do you?"
    show arceus worried flipped
    arceus "Huh?"
    show pipe_gun flipped at manual_pos(0.6, 0.35) with dissolve
    n "Pizzapotamus shoots Arceus in the chest."
    play sound sfx_hks1
    show arceus worried flipped at manual_pos(0.4, 0.55):
        linear 0.5 rotate -45
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    n "As Arceus is dying on the floor, he faintly hears people talking."
    grace "I expected more from you."
    obama "Should've listened to my campaign speeches, bitch."
    mike "Alright, who wants to try pizza from my thermos?"
    show cs happy christmas
    cs "Oh, yes! Me first! Woohoo!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    pause 2.0
    play sound sfx_csnore
    cs "Zzz..."
    rich "Hey, CS, are you sleeping?"
    scene cs_living2_festive 
    show wesley festive at right
    show rich festive at mid_right
    show db at center
    show ed festive at mid_left behind cs
    show cs concentrate christmas at left
    with dissolve
    play sound sfx_csnore
    rich "CS!"
    stop sound
    show cs worried christmas
    cs "Huh?"
    show cs disappointed christmas
    cs "Oh, sorry, I did doze off."
    cs "I had this insane dream, and there was this pizza guy..."
    wesley "Speaking of pizza, should we have dinner now? I'm starving."
    cs "Yeah, that's a good point. Give me a moment to get ready."  

# Dinner/More Banter
label ce_dinner:
    play music christmas_spirit
    music christmas_spirit
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive flipped at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    with dissolve
    cs "Well, I'd love to start off this wonderful meal by saying--"
    blank "Hey, stop it! We are not playing your music!"
    if fun_value(FUN_VALUE_COMMON):  # I made this joke a fun value, it just seems too mean to be the main route
        nova "Blank, Blank..."
        nova "This song is so..."
        show cs christmas disappointed
        show tate festive sheepish flipped
        nova "FUCKING ASS!"
        nova "STOP MAKING MUSIC!"
        nova "STOP MAKING MUSIC!"
        show cs christmas angry flipped
        nova "Turn that shit off!"
    else:
        nova "Well I don't want to hear catgirl moans at the dinner table!"
        blank "They're mixed into the instrumentation, you can barely--"
    cs "Hey! Can you two stop fighting and get over here and eat with us!"

    show left_room at mid_left
    show left_chair_back at mid_left
    show left_table at mid_left
    show cs christmas at mid_left
    show anno festive at mid_offscreen_left
    show tate festive at center
    show db at manual_pos(0.85, 0.6, 0.5)
    show k22 at manual_pos(-0.25, 0.575, 0.5)
    with move
    db "So, CS, how's your streams been going recently?"
    cs "Well, it's mainly been car crash streams on Sundays as usual."
    cs "It's been hard to really do crazy stuff as much as I did back then on Mixer ever since it died."
    db "Ah, yeah, I get that."
    tate "But hey, we still have fun!"
    show left_room at left
    show left_chair_back at left
    show left_table at left
    show cs christmas at mid_offscreen_right
    show anno festive at mid_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 at center
    show k17 disappointed flipped at mid_left_left
    with move
    k22 "Hey K-17, are you gonna eat your food?"
    k17 "I... uhh..."
    k17 "I need to go to the bathroom..."
    show k17 disappointed with determination
    hide k17 with moveoutleft
    pause 0.5
    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    with dissolve
    obama "So, Billy, any good new pitches on the table for you?"
    billy "Well, I got in contact with Phil Swift recently, you may have heard of him from Flex Tape!"
    michael "Actually, Phil's a friend of mine! He's stayed over my place plenty of times."
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "I was going to invite him to the party this evening, but he's been so busy pitching Flex products. I think he's in Europe right now."
    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    billy "Well, you might see him and I team up for a commercial soon, if this deal goes through!"
    obama "How much does it cost to get you in a commerical, anywho?"
    billy "If I told you, I'd have to kill you!"
    n "Obama and Billy chuckle, but Luther does not."

    show arceus flipped
    arceus "How's the foundation repair business, HoH SiS?"
    ed "It's been pretty good, since we got all those contracts after our run-in."
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Heh, I'm still sorry about all that..."
    scene night_bg
    show right_room at center
    show right_chair_back at center
    show obama festive at mid_offscreen_left
    show michael festive at mid_left
    show ed festive at center
    show wesley festive at mid_right
    show rich festive at mid_offscreen_right
    show right_table at center
    wesley "My back is sorry about it, too."
    rich "Oh, can it, ding-dong, you got surgery, didn't cha?"
    wesley "Having a metal pole in your back isn't ideal, numbnuts."
    mean "I mean, metal is {i}stronger{/i} than bones, so it's kinda like an upgrade!"
    wesley "Tell that to the TSA."
    arceus "I don't tell anything to the TSA."
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Well, again, I hope I've been able to make it up to you guys, mostly."
    scene night_bg
    show right_room at center
    show right_chair_back at center
    show obama festive at mid_offscreen_left
    show michael festive at mid_left
    show ed festive at center
    show wesley festive at mid_right
    show rich festive at mid_offscreen_right
    show right_table at center
    show linus festive at manual_pos(1.3, 0.6, 0.5)
    show luke festive at manual_pos(1.45, 0.6, 0.5)
    ed "You've more than made it up to us, CS."
    rich "Yeah, you helped propel our business to new heights! Or, I guess, new foundations."
    wesley "Mmm."

    scene night_bg
    show right_room at right
    show right_chair_back at right
    show obama festive at manual_pos(-0.5, 0.5, 0.5)
    show michael festive at manual_pos(-0.25, 0.6, 0.5)
    show ed festive at manual_pos(0, 0.55, 0.5)
    show wesley festive at manual_pos(0.25, 0.575, 0.5)
    show rich festive at manual_pos(0.5, 0.6, 0.5)
    show linus festive at manual_pos(0.80, 0.6, 0.5)
    show luke festive at manual_pos(0.95, 0.6, 0.5)
    show right_table at right
    with move
    linus "So, CS, when are we getting you back for another video?"
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Oh, jeez, life has been so busy."
    scene night_bg
    show right_room at right
    show right_chair_back at right
    show obama festive at manual_pos(-0.5, 0.5, 0.5)
    show michael festive at manual_pos(-0.25, 0.6, 0.5)
    show ed festive at manual_pos(0, 0.55, 0.5)
    show wesley festive at manual_pos(0.25, 0.575, 0.5)
    show rich festive at manual_pos(0.5, 0.6, 0.5)
    show linus festive at manual_pos(0.80, 0.6, 0.5)
    show luke festive at manual_pos(0.95, 0.6, 0.5)
    show right_table at right
    luke "You were a fan favourite."  # Intentional Canadian spelling
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Well, if I can make it to Canada at some point soon..."
    scene night_bg
    show right_room at right
    show right_chair_back at right
    show obama festive at manual_pos(-0.5, 0.5, 0.5)
    show michael festive at manual_pos(-0.25, 0.6, 0.5)
    show ed festive at manual_pos(0, 0.55, 0.5)
    show wesley festive at manual_pos(0.25, 0.575, 0.5)
    show rich festive at manual_pos(0.5, 0.6, 0.5)
    show linus festive at manual_pos(0.80, 0.6, 0.5)
    show luke festive at manual_pos(0.95, 0.6, 0.5)
    show right_table at right
    linus "We'll pay for your flight out~"
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Tempting. Very tempting. I'll see what I can do."
    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus flipped at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    arceus "Hey, at least you can go to LTT and not have to walk all the way there this time!"
    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "True... honestly, would you want to go too?"
    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus flipped at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    show wesley festive at manual_pos(1.3, 0.6, 0.5)
    show rich festive at manual_pos(1.5, 0.6, 0.5)
    show linus festive at manual_pos(1.65, 0.6, 0.5)
    show luke festive at manual_pos(1.80, 0.6, 0.5)
    arceus "Me? I'm in the UK now, I don't know if I can make it all the way to West Canada."
    scene night_bg
    show right_room at right
    show right_chair_back at right
    show arceus flipped at manual_pos(-0.95, 0.65, 0.5)
    show billy festive at manual_pos(-0.75, 0.6, 0.5)
    show obama festive at manual_pos(-0.5, 0.5, 0.5)
    show michael festive at manual_pos(-0.25, 0.6, 0.5)
    show ed festive at manual_pos(0, 0.55, 0.5)
    show wesley festive at manual_pos(0.25, 0.575, 0.5)
    show rich festive at manual_pos(0.5, 0.6, 0.5)
    show linus festive at manual_pos(0.80, 0.6, 0.5)
    show luke festive at manual_pos(0.95, 0.6, 0.5)
    show right_table at right
    with move
    linus "We'd pay for your flight out, as well."
    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus flipped at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    arceus "What about my bethrothed, though?"
    scene night_bg
    show left_room at right
    show left_chair_back at right
    show kitty festive flipped at manual_pos(0.80, 0.7, 0.5)
    show db at manual_pos(0.55, 0.55, 0.5)
    show tate festive at mid_left
    show cs christmas at mid_offscreen_left
    show left_table at right
    kitty "Don't ever call me that again."
    scene night_bg
    show right_room at right
    show right_chair_back at right
    show obama festive at manual_pos(-0.5, 0.5, 0.5)
    show michael festive at manual_pos(-0.25, 0.6, 0.5)
    show ed festive at manual_pos(0, 0.55, 0.5)
    show wesley festive at manual_pos(0.25, 0.575, 0.5)
    show rich festive at manual_pos(0.5, 0.6, 0.5)
    show linus festive at manual_pos(0.80, 0.6, 0.5)
    show luke festive at manual_pos(0.95, 0.6, 0.5)
    show right_table at right
    linus "Sure, why not?"
    luke "You just add two international flights to the cost of this, Linus."
    linus "Since when have I been responsible with money, Luke?"
    n "Luke takes a sip of his drink to stop himself from laughing too hard."
    luke "You said it, not me."

    scene night_bg
    show left_room
    show left_chair_back
    show cs christmas at center
    show anno festive at mid_left
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show digi at manual_pos(-0.3, 0.65, 0.5)
    show left_table
    with dissolve
    cs "Y'know, I kinda wish that I learned to start driving sooner."
    cs "I can't stop driving everywhere!"
    show left_room at left
    show left_chair_back at left
    show left_table at left
    show cs christmas at mid_offscreen_right
    show anno festive at mid_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 at center
    show digi at manual_pos(0.175, 0.65, 0.5)
    with move
    k22 "Speaking of driving, this reminds me of something."
    k22 "Why does anyone buy regular unleaded gas?"
    show digi thinking flipped
    digi "Because it's cheaper?"
    k22 "Okay, but it's not though. Super unleaded is way cheaper, and it's better for your car."
    show digi disappointed flipped
    digi "That doesn't make any sense."
    show k22 confident
    k22 "It doesn't, but it's true!"
    show k22 disappointed
    show digi sad flipped
    digi "It's not though, Super unleaded is more expensive."
    k22 "It's... not though."
    show digi angry flipped
    digi "What are you talking about? Of course it's more because it's better for your car!"
    show cs christmas flipped
    cs "Don't you guys mean, unleaded plus?"
    digi "Yeah! See? CS knows!"
    k22 "No, it's called super unleaded, and it's cheaper than regular unleaded!"
    digi "But it's not! Why would it be?"
    scene night_bg
    show right_room at center
    show right_chair_back at center
    show obama festive at mid_offscreen_left
    show michael festive at mid_left
    show ed festive at center
    show wesley festive at mid_right
    show rich festive at mid_offscreen_right
    show right_table at center
    ed "Are you thinking of premium unleaded?"
    scene night_bg
    show left_room at left
    show left_chair_back at left
    show cs christmas flipped at mid_offscreen_right
    show anno festive at mid_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 disappointed at center
    show digi angry flipped at manual_pos(0.175, 0.65, 0.5)
    show left_table at left
    k22 "No, it's not premium, or unleaded 88..."
    scene night_bg
    show right_room at center
    show right_chair_back at center
    show obama festive at mid_offscreen_left
    show michael festive at mid_left
    show ed festive at center
    show wesley festive at mid_right
    show rich festive at mid_offscreen_right
    show right_table at center
    ed "Unleaded 88?"
    scene night_bg
    show left_room at left
    show left_chair_back at left
    show cs christmas flipped at mid_offscreen_right
    show anno festive at mid_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 angry at center
    show digi disappointed flipped at manual_pos(0.175, 0.65, 0.5)
    show left_table at left
    k22 "It's called super unleaded, it has ethanol in it, and it's {i}better. for. your. car!{/i}"
    k22 "Every gas station we've been to, it's always regular, super, the third option, and diesel!"
    digi "I still think you may be thinking of premium."
    k22 "No, I'm-- Give me a second, I have a picture of this on my phone."
    show digi thinking flipped
    digi "CS, have you ever seen super unleaded?"
    cs "Uhh... no?"
    show k22 confident
    k22 "Ah-a! See?"
    show gas_prices at mid_right with easeinbottom
    show digi shock flipped
    digi "What? How?"
    cs "What backwards town do you live in where the better gas is cheaper?"
    k22 "See, the super unleaded is the cheapest, then regular, then premium!"
    hide gas_prices with easeoutbottom
    show digi thinking flipped
    digi "So, the question now is, what's the difference between plus and super?"
    show k22
    k22 "They might be the same thing."
    k22 "Our super unleaded gas has ethanol in it."
    show k22 confident
    k22 "Guess who makes ethanol? We do!"
    show digi happy flipped
    digi "I see now!"
    show k22
    digi "So, because you guys make this additive, it's cheaper for you, but more expensive for us."
    k22 "Probably."
    cs "Shit, maybe we need to start making ethanol."
    scene night_bg
    show right_room at center
    show right_chair_back at center
    show obama festive at mid_offscreen_left
    show michael festive at mid_left
    show ed festive at center
    show wesley festive at mid_right
    show rich festive at mid_offscreen_right
    show right_table at center
    ed "That's great and all, but what in the world is unleaded 88?"
    scene night_bg
    show left_room at left
    show left_chair_back at left
    show cs christmas flipped at mid_offscreen_right
    show anno festive at mid_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 at center
    show digi flipped at manual_pos(0.175, 0.65, 0.5)
    show left_table at left
    k22 "It's for cars newer than 2001, that's all I know."

    show digi sad flipped
    digi "Hey CS, did K-17 ever come back from the bathroom?"
    cs "Huh?"
    cs "Oh, yeah, is that where they ran off to?"
    digi "We should probably go check on them, see if they are okay..."
    scene cs_bathroom
    with dissolve
    show digi sad flipped at mid_mid_left
    show cs christmas at left
    with moveinleft
    digi "Hey! K-17? Are you in there?"
    k17 "Nuh uh!"
    cs "Do you need, any help at all? We are gonna start the gift exchange here in a few minutes!"
    n "K-17 starts sobbing."
    k17 "No one... told me..."
    k17 "Mixer... died..."
    show cs christmas worried
    show digi shock flipped
    cs "Uh oh."
    digi "Shiiit."
    show cs christmas disappointed
    cs "Yeah, Mixer shut down some time ago now... sorry about that."
    show digi sad flipped
    k17 "But why? Why! It was like, the perfect streaming platform!"
    digi "It was, but it was owned by Microsoft. It was bound to happen."
    cs "Hey."
    digi "Listen, just because the Zune was cool doesn't mean--"
    k17 "What do we even do now? Without Mixer, where do you stream?"
    show cs christmas
    show digi flipped
    cs "Well, I stream on {a=https://twitch.tv/cs188/}Twitch.{/a}"
    digi "{a=https://twitch.tv/DigiDuncan}Me too{/a}, when I get the chance."
    n "K-17 sniffles."
    k17 "At least Crazy Saturday lives on..."
    show cs christmas disappointed
    cs "{i}Well..."
    digi "Let him believe, CS. Let him believe."

# Gift Exchange
label ce_exchange:
    scene cs_living
    show cs christmas at center
    with dissolve
    play music superstar_road volume 0.5
    music superstar_road
    cs "Alright, everyone! It's time for the gift exchange!"
    cs "Everyone brought a gift, right?"
    n "Everyone nods."
    cs "Alright, well I marked numbers for everyone who showed up, so I'll go around while you guys draw from the bag!"
    hide cs with moveoutright
    n "CS goes around, and everyone draws out of the bag."
    cs "Let's see, who is going first?"
    #roll 1
    cs "Would you look at that! I guess I'm going first!"
    show cs christmas at mid_left with moveinleft
    cs "I'm gonna pick, this one!"
    cs "I got..."
    show cs disappointed christmas
    show thigh_highs at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    cs "Thigh highs?"
    show cs full christmas at manual_pos(0.034, 0.187)
    arceus "Look at that, you got my gift, CS!"
    hide thigh_highs with dissolve
    cs "Well, I guess I have more now!"
    k17 "You wear thigh highs?"
    cs "Yeah, I'm wearing them right now! See?"
    show cs full christmas at Move((0.034, 0.187), (0.034, -0.4), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    window hide
    pause 2.5
    show cs full christmas at Move((0.034, -0.4), (0.034, 0.187), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")  
    digi "Oh, shit. I guess I never looked down to check."
    aria "I just assumed because of the outfit."
    hide cs with moveoutright
    arceus "Welp, it looks like I'm next."
    show arceus flipped at mid_left with moveinleft
    arceus "I got..."
    show tea_and_crumpets at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    arceus "Tea and crumpets?"
    kitty "Arcie! You got my gift!"
    hide tea_and_crumpets with dissolve
    show arceus worried flipped
    arceus "Sorry! I honestly forgot which one was yours."
    kitty "You saw me carry it in, dumbass!"
    hide arceus with moveoutright   
    kitty "Whatever, it's my turn now."
    show kitty festive at mid_left with moveinleft
    kitty "Looks like I got..."
    show riffmaster at Move((0.3125, 1.0), (0.3125, 0.35), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    kitty "A... Guitar Hero controller?"
    cs "Holy shit, that's a Riffmaster!"
    kitty "Is that good?"
    cs "It's just a really good guitar controller."
    hide riffmaster with dissolve
    anno "That was my gift!"
    hide kitty with moveoutright   
    anno "It looks like I'm up next."
    show anno festive at mid_left with moveinleft
    anno "I got..."
    show raspberry_pi at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    anno "What the hell is this?"
    arceus "Ooh! That's a Raspberry Pi!"
    obama "What are you on about? That doesn't look edible at all!"
    digi "No-- okay, it's my gift, so let me explain."
    digi "It's a small computer you can use to run basic servers or build little projects!"
    hide raspberry_pi with dissolve
    anno "Oh. Cool, I guess."
    hide anno with moveoutright
    show digi flipped at mid_left with moveinleft
    digi "Well it's my turn now, and I'm gonna steal that Riffmaster!"
    show kitty festive flipped at mid_right with moveinright
    show riffmaster at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide riffmaster with dissolve
    hide digi with moveoutright
    kitty "Damn."
    kitty "Well, what do I do now?"
    cs "You can steal another gift, or pick out another one."
    hide kitty with moveoutleft
    arceus "Psst! Kitty! Come here!"
    n "Arceus whispers something into her ear."
    show kitty festive at mid_left with moveinleft
    kitty "Alright, Anno, hand over your computer thing."
    show anno festive at mid_right with moveinright
    show raspberry_pi at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide raspberry_pi with dissolve
    hide kitty with moveoutright   
    anno "Welp, next gift I guess."
    show anno festive at mid_left with move
    anno "I guess I'll pick this one."
    anno "I wonder what it'll be?"
    show lego_train at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    anno "A Lego set!"
    mean "A {i}train{/i} Lego set!"
    hide lego_train with dissolve
    mean "That's my gift, by the way."
    if fun_value(FUN_VALUE_COMMON):
        tate "We know!"
    hide anno with moveoutright
    mean "Alright, well I guess it's my turn."
    show mean human flipped at mid_left with moveinleft
    mean "I'm picking this big one!"
    show instant_pot at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    mean "An instant pot?"
    tate "Mean, you got my gift!"
    show mean human happy flipped
    hide instant_pot with dissolve
    mean "Well it's mine now, bitch!"
    mean "Who's next?"
    hide mean with moveoutright
    tate "It's me!"
    show tate festive at mid_left with moveinleft    
    tate "Let's see..."
    show handy_switch at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.5
    show tate smug festive 
    tate "Billy? Is this yours?"
    billy "It's the Handy Switch!"
    billy "It let's you control any power source, from anywhere!"
    hide handy_switch with dissolve
    show tate festive
    tate "I'm sure I can find a use for this."
    hide tate with moveoutright
    billy "Alright, it's my turn!" 
    show billy festive at mid_left with moveinleft
    show doi at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top") 
    billy "Wow! Is this the Declaration of Independence?"
    obama "Yep! It's the real deal!"
    obama "Figured I didn't need it anymore, so it's yours now!"
    hide doi with dissolve
    billy "Great! I can probably pitch this!"
    hide billy with moveoutright
    obama "Welp, I guess it's my turn now."
    show obama festive at mid_left with moveinleft 
    show mgs1 at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top") 
    obama "Metal Gear Solid?"
    copguy "Yeah, that's mine, I didn't know what anyone really wants, so I just found this at the station."
    hide mgs1 with dissolve
    obama "Dude, this is like my favorite game. I appreciate it."
    copguy "I'm glad."
    hide obama with moveoutright
    copguy "It's my turn now."
    show copguy festive flipped at mid_left with moveinleft 
    show gravity_falls at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    copguy "Okay, so I got \"Gravity Falls Season 2 Director's Cut\"..."
    show colt at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    copguy "...and boss? Is this your gun?"
    sheriff "Yeah, you got my gift. Don't ask how that DVD got in there."
    hide gravity_falls
    hide colt
    with dissolve
    hide copguy with moveoutright
    sheriff "Because I don't know either."
    show sheriff festive flipped at mid_left with moveinleft 
    sheriff "Whatever, it's my turn to pick a gift."
    sheriff "Damn, this is heavy! What the hell is this?"
    show cement at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    sheriff "A bag of cement?"
    ed "We had some leftover from the last house we worked on."
    hide cement with dissolve
    sheriff "Great, I can drop this on Copguy's head for leaving me in the bathroom!"
    hide sheriff with moveoutright
    ed "I guess it's my go."
    show ed festive flipped at mid_left with moveinleft 
    show melted_ice_cream at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    ed "What the hell? Who brought ice cream? It's all melted!"
    #Audio clip of Richard laughing
    play sound sfx_richlaugh
    pause 3.0
    hide melted_ice_cream with dissolve
    ed "Damn it, Richard! I don't want this!"
    hide ed with moveoutright
    rich "Well, let's see what I get."
    show rich festive flipped at mid_left with moveinleft 
    show pills at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    rich "Pain pills?"
    wesley "Wait a minute! Those are mine!"
    show wesley festive at mid_right with moveinright
    wesley "I didn't mean to gift that..."
    wesley "I'm gonna steal those since it's my turn now!"
    show pills at Move((0.3125, 0.5), (0.7125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    hide pills with dissolve
    hide wesley with moveoutright
    rich "Hey!"
    rich "What do I even get now?"
    rich "There's nothing else I really want here..."
    rich "I guess it's time to open another present."
    show sunny_d at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    rich "I got Sunny D!"
    hide sunny_d with dissolve
    n "K-17 starts giggling."
    hide rich with moveoutright
    k17 "Alright! My go!"
    show k17 flipped at mid_left with moveinleft
    show fumo at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.5
    show k17 disappointed flipped
    k17 "Addy?"
    show k22 disappointed flipped at offscreenleft
    k22 "Huh?"
    hide k22 
    hide fumo
    with easeoutright
    n "K-22 springs up and steals the gift from K-17, sprinting out of the room."
    k22 "I'm sorry, I'll be right back!"
    k17 "What the hay! Now I gotta get another gift!"
    show k17 flipped
    k17 "I'm gonna take the Gravity Falls Commentary!"
    show sheriff festive at mid_right with moveinright
    show gravity_falls at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide gravity_falls with dissolve
    show colt at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide colt with dissolve
    k17 "...and the gun."
    hide k17 with moveoutright
    show copguy festive flipped at left with moveinleft
    copguy "Alright, then I'm taking the Declaration of Independence!"
    show billy festive at center with moveinright
    billy "What the actual fuck?"
    show doi at Move((0.4, 0.5), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 2.0
    hide doi with dissolve
    billy "Stop stealing gifts!"
    hide copguy with moveoutright
    hide sheriff with moveoutleft
    show billy festive at mid_left with move
    billy "Alright, I'll just take the next gift."
    show adderall at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    billy "Adderall?"
    billy "Nope! I'm done with any kind of drug! Not after last time!"
    aria "Aw, that was my gift!"
    aria "You want me to take it?"
    billy "Yes, please!"
    show aria festive at mid_right with moveinright
    show adderall at Move((0.3125, 0.5), (0.7125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    hide adderall with dissolve
    n "Aria steals Billy's gift."
    hide aria with moveoutleft
    billy "Awesome! I get to pick another gift!"
    show peach_syrup at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    billy "Peach syrup!"
    michael "Noice, you got my gift!"
    michael "It goes well with about everything!"
    hide peach_syrup with dissolve
    billy "I'll keep this one!"
    hide billy with moveoutright
    michael "Alright, what gift to choose..."
    show michael festive at mid_left with moveinleft
    show ltt_bottle at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    michael "I got a new water bottle!"
    linus "You got my LTT water bottle!"
    hide ltt_bottle with dissolve
    linus "{a=https://www.lttstore.com}lttstore.com.{/a}"
    hide michael with moveoutright
    linus "Alright, it's my turn."
    show linus festive at mid_left with moveinleft
    show ltt_screwdriver at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    linus "Hey, Luke! I got your gift!"
    luke "Couldn't you tell it was mine?"
    hide ltt_screwdriver with dissolve
    linus "No, how was I supposed to figure that out?"
    hide linus with moveoutright
    luke "Whatever, it's my go now."
    show luke festive flipped at mid_left with moveinleft
    luke "I got..."
    show monitor at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show hard_drive at Move((0.3125, 1.0), (0.35, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    luke "A variation of PC components!"
    blank "Yeah, it's two monitors, a 1TB hard drive, and some other things."
    blank "I found it on the curb."
    hide monitor
    hide hard_drive
    with dissolve
    luke "On the {i}curb{/i}?"
    blank "Yeah, it was just lying there on the curb."
    luke "Damn, well then..."
    hide luke with moveoutright
    blank "It looks like it's my turn next."
    show blank flipped at mid_left with moveinleft
    show gamersupps at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    blank "GamerSupps?"
    blank "Guacamole Gamer... Fart... 9000?"
    nova "Damn it, you got my gift, Blank!"
    hide gamersupps with dissolve
    blank "Great."
    hide blank with moveoutright
    nova "As much as I want to steal that Adderall, I'm gonna pick a gift."
    show nova flipped at mid_left with moveinleft
    nova "Oh boy! I wonder what it is!"
    show russian_radio at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    nova "What the fuck is? Some World War II radio?"
    eliza "Yep. Used by the Soviets in the last half of World War II."
    hide russian_radio with dissolve
    nova "I'm sure Ges will like this, I'll probably give it to him."
    hide nova with moveoutright
    eliza "So, it's my turn, let's see what we have..."
    show elizabeth at mid_left with moveinleft
    show dog_food at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    eliza "Dog food."
    hide dog_food with dissolve
    eliza "Dog food?"
    db "Ah yeah, I had a lot extra lying around in my car, so I figured why not?"
    hide elizabeth with moveoutright
    db "Well, I guess it's finally my turn."
    show db at mid_left with moveinleft
    show 1850_coin at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    db "Wow, I got some old coins!"
    digi "Holy shit, I think those are like, really rare!"
    digi "Lemme look it up."
    grace "You got our coins!"
    anne "We had them lying around on the table at home."
    digi "Yeah, those are super rare. I would hold onto those if I were you."
    hide 1850_coin with dissolve
    arceus "Don't you collect coins, Digi?"
    digi "Not really, I just collect pennies."
    arceus "... Why just pennies?"
    digi "I have like five thousand pennies. One day, when America stops making pennies, they'll go up in value."
    obama "Why would we stop making pennies?"
    digi "Well, you guys spend 1.6 cents per penny to make them, so you're losing money."
    digi "Canada already stopped making their pennies."
    mean "Well, yeah, that's because Canada's smarter than America."
    digi "Anywho, one day, when I have five thousand rare coins in a jar, it'll all have been worth it."
    arceus "Alright..."
    billy "Antique coins lying around, Tech lying on the curb..."
    billy "Where the hell do you guys live where you find this kinda shit?"
    hide db with moveoutright
    if d20 == 20:
        avgn "Alright, well it's my turn!"
        show avgn at mid_left with moveinleft
        avgn "Let's do this."
        show old_shirt at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
        avgn "This shirt's {i}ass!"
        cs "Hey! That was my gift!"
        avgn "Yeah? Well, you're a poopyhead!"
        hide avgn with moveoutright     
    anne "Well Grace, you wanna pick out the last gift?"
    show grace at mid_left with moveinleft
    grace "Yippee! The last gift!"
    if d20 == 20:
        show roll_and_rocker at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
        show rolling_rock at Move((0.3125, 1.0), (0.35, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
        grace "Ooh! Is this a balance board?"
        avgn "It's a rolling rock..."
        avgn "...with a roll and rocker!"
        grace "Cool!"
        hide roll_and_rocker
        hide rolling_rock
        with dissolve
    else:
        show old_shirt at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
        grace "I got a cool new t-shirt!"
        cs "Hey! You finally got my gift!"
        hide old_shirt with dissolve
        cs "Not all of my Depop shirts sold, so it became my gift."
        cs "Does it even fit you?"
        n "Grace puts on the shirt."
        show grace shirt
        pause 2.0
        grace "Yep!"
    cs "Woohoo! All of the gifts have been handed out!"

# Games/Climax
label ce_climax:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "After all of the gifts have been given out, almost everyone has come to the conclusion that the party should end."
    scene cs_living
    show cs christmas at left
    show k22 at mid_right
    show k17 at mid_offscreen_right
    show luke festive at center
    show tate festive at mid_left behind cs
    show mean human flipped at mid_offscreen_left behind cs
    with dissolve
    k22 "Well, CS, this was wonderful, but we should get going."
    cs "Wait! You aren't gonna stay for the games?"
    show k22 angry
    k22 "SHHHDADA--{w=1.0}{nw}"
    show k17 happy
    k17 "We're doing games? Well, that's the best part!"
    show cs disappointed christmas
    show tate sheepish festive
    k22 "{size=-12}Damn it!"
    show k22 disappointed
    show k17 disappointed
    show cs angry christmas
    cs "So, you never wanted to stay! You only came here because of him!"
    nova "Well, I'm also leaving, because {i}this{/i} asshole won't let me play any {i}good{/i} music!"
    blank "Hah! Says you! {i}You{/i} wanted to play your trash for the entire party!"
    digi "Hey, wait a second! Luke!"
    luke "Wha? Oh, shit!"
    show tate sad festive
    digi "You were... streaming movies to the projector from your phone?"
    show mean human annoyed flipped
    luke "Look, this looked too complicated to set up anyway, so I wanted to make it feel like your plan worked!"
    digi "But, but..."
    digi "I really thought I could set it up this time..."
    sheriff "Hey, Copguy! I need to go to the bathroom again!"
    copguy "Motherfucker! Do it yourself!"
    ed "My poor turkey..."
    michael "I think I'm gonna puke."
    wesley "Arghh! My back! CS you prick, this is your fault!"
    grace "Guys! Stop yelling!"
    show tate srs festive
    tate "Yeah guys! Get it together!"
    nova "No! Fuck you!"
    show mean human angry flipped
    anne "Hey!"
    mean "What'd you say, you little {i}fuck?"
    arceus "Oh, my God, this is hurting my head..."
    show cs pissed christmas
    cs "Damn it, everyone! Shut the fuck u--{w=2.0}{nw}"

# Lights out
screen flashlight_demo:
    layer "flashlight"
    add Flashlight()

# TODO: DIGI STOPPED EDITING HERE

label ce_lights_out:
    play sound sfx_power_out
    $ mouse_visible = False
    scene black
    stop music
    music end
    pause 0.2
    sheriff "Hey, uh..."
    sheriff "I think I have finally become blind."
    linus "I think all of our eyes went out."
    cs "No! This can't be happening!"
    cs "My party is ruined!"
    tate "CS, this isn't your fault."
    cs "Everyone is fighting, and no one is having fun!"
    nova "Well, yeah, but, at least I don't listen to Blank's shitty music anymore."
    tate "{i}Can it!" with hpunch
    tate "Look, we need to stop the arguing and calm down!"
    billy "I am calm!"
    aria "I am clam."
    cs "Okay, I'm trying to relax...{w=0.5} and think..."
    cs "Let me feel my way to the basement, and try to check the breaker."
    cs "I'll be right back."
    play sound sfx_bump
    pause 0.5
    k17 "Oof!"
    cs "Sorry!"
    arceus "CS? Is that you?"
    cs "Hey, Arc. I'm making my way to the breaker to see if I can turn it on."
    arceus "Great. If you find Kitty, lemme know, I don't know where she went."
    arceus "I think she wanted to get extra food, but it's been 20 minutes since then."
    cs "Alright, I'll let you know."
    cs "The door to the basement should be here somewhere..."
    n "CS feels around the wall."
    n "Finally he finds the doorknob."
    cs "A-ha!"
    if fun_value(FUN_VALUE_EPIC):
        cs "Huh, why is my doorknob..."
        cs "Squeezable?"
        n "CS turns the doorknob."
        n "All of a sudden, CS gets kicked to the ground!"
        play sound sfx_hitbod3
        cs "Ow!"
        cs "What the fuck was {i}that?!"
        eliza "Oops, sorry."
        eliza "You grabbed my... chest."
        cs "Oh, crap! I'm so sorry!"
        eliza "It's okay! None of us can see!"
        cs "I'm just trying to get to the basement! I think you're in front of the door!"
        eliza "Let me just move out of the way."
        cs "Yeah, thanks."
    else:
        cs "Why is my doorknob so big?"
        n "CS turns the doorknob."
        grace "{i}Ahhhhh!"
        grace "You're squeezing my head!"
        cs "Oops, sorry!"
        cs "I'm trying to get to the basement."
        grace "Let me move before you try breaking my head again."
    n "Slowly but surely, CS makes his way into the basement."
    cs "Alright, I just need to find the breaker."
    n "CS feels around, and manages to find a flashlight on a table."
    scene cs_basement
    show cs christmas at center
    play sound sfx_flashlight_on
    show screen flashlight_demo
    cs "Thank God, I can actually see."
    hide cs with moveoutright
    scene breakerbox with dissolve
    show cs christmas at left with moveinleft
    cs "Found it!"
    n "CS opens the breaker and flicks off and on the switches."
    play sound sfx_breaker
    pause 1.5
    show cs disappointed christmas
    cs "Damn, nothing."
    show cs christmas flipped
    cs "Well, it was worth a try."
    hide cs with moveoutleft
    scene cs_basement
    show cs christmas at center
    show kitty festive at left
    with dissolve
    cs "At least I have this flashlight now!"
    show cs christmas flipped
    n "As CS turns around, he spots Kitty chilling against the wall."
    play music synchronicity
    music synchronicity
    cs "Kitty? What are you doing down here? Arceus is looking for you!"
    kitty "Sorry... I got a bad migraine during the end of the party, so I tried to find the quietest place in the house."
    kitty "I'm a little glad the power went out, actually. It's been peaceful here."
    cs "I was trying to fix the breaker, but, no dice."
    kitty "I think the power is out everywhere. I heard the wind really pick up outside a little while ago."
    kitty "You should probably go check for yourself."
    kitty "Could you please let Arcie know I'm down here? I think I'm gonna stay here for a bit."
    cs "Sure thing. Stay safe."
    show cs christmas with determination
    hide cs with moveoutright
    n "CS rushes back upstairs."
    scene cs_hallway_off 
    show arceus at center
    show elizabeth at right
    with dissolve
    show cs christmas at left with moveinleft
    arceus "Welcome back! Assuming you didn't get the power working?"
    cs "Nope, but I found Kitty!"
    cs "She's relaxing in the basement since her head was hurting."
    arceus "That makes sense, I'll go talk to her here soon."
    eliza "I see you found a torch."
    cs "Yeah, it was lying around downstairs, I'm lucky I found one."
    show arceus flipped
    eliza "I was thinking of lending mine to Arceus, so he can go in the basement."
    arceus "I would appreciate it."
    show elizabeth at mid_right
    eliza "Take this, but make sure to bring it back when the power turns on."
    arceus "Got it."
    show arceus with determination
    hide arceus with moveoutleft
    eliza "Before you go, CS, I would see if you can check the outdoors."
    eliza "Even though it is dark in here, no light is coming in from outside."
    eliza "It also sounds terrible out there."
    show cs disappointed christmas
    eliza "I've experienced some harsh Soviet winters, but I've never dealt with anything this bad before."
    cs "Well, that's some {i}awesome{/i} news..."
    cs "I'll go check on others, and see if I can get outside."
    hide cs with moveoutright
    scene cs_foyer_off_festive
    show anno festive at mid_left
    show aria festive at mid_mid_left behind anno
    show digi sad at mid_mid_left
    show k17 disappointed at center behind digi
    show k22 disappointed at mid_mid_right
    show tate srs festive flipped at mid_right
    show mean human annoyed at mid_offscreen_right
    with dissolve
    show cs christmas at left with moveinleft
    cs "Hey guys! How is everyone holding up?"
    anno "It's getting kinda cold, so I hope the power comes back soon."
    anno "My phone is about to die."
    cs "I'm gonna check outside and see how bad it is."
    k22 "I was gonna try that, but I couldn't find the door."
    cs "If we get outside, we might be able to dig our vehicles out."
    cs "I'll go take a look."
    hide cs with moveoutright
    anno "Good luck, CS!"
    scene black with dissolve
    n "CS pulls and yanks open the door, until it finally rips open."
    play sound sfx_house_door_slam
    scene cs_door 
    show cs worried christmas at left
    with dissolve
    n "He falls backwards as he is met with an unwelcome sight."
    cs "What the hell? Is that snow?"
    n "CS sticks his finger out into the mysterious substance."
    cs "Oh my God, how much... did it..."
    n "CS slams the door shut and runs back to deliver the news."
    scene cs_foyer_off_festive
    show anno festive at mid_left
    show aria festive at mid_mid_left behind anno
    show digi sad at mid_mid_left
    show k17 disappointed at center behind digi
    show k22 disappointed at mid_mid_right
    show tate srs festive flipped at mid_right
    show mean human at mid_offscreen_right
    with dissolve
    show cs worried christmas flipped at center with moveinright
    cs "Guys, the door...{w=0.5} the door..."
    aria "Calm down, CS. Catch your breath."
    show cs disappointed christmas flipped
    cs "The door, it's... {i}all{/i} snow."
    show digi shock
    show tate sad festive flipped
    show k17 shock flipped
    anno "{i}All{/i} snow?"
    show mean human annoyed
    mean "The door?"
    k17 "It's?"
    digi "Are we trapped in here?"
    show mean human angry
    show tate sad festive
    mean "There's only one way to find out."
    show cs disappointed christmas
    mean "CS, take me to the roof."
    cs "To the roof?"
    mean "Yeah, let me climb up there."
    cs "Sure, we can try."
    show mean human annoyed flipped
    tate "Be careful, Mean."
    hide cs
    hide mean
    with moveoutright
    n "CS and Mean find the ladder to the attic, and make their way up."
    scene cs_attic
    show hatch at manual_pos(0.3, -0.2) 
    show cs disappointed christmas at mid_left
    show mean human annoyed at mid_right
    with dissolve
    stop music fadeout 3.0
    music end
    mean "You good, CS?"
    cs "Yeah, I'm just a bit tired."
    cs "There should be a hatch or something up here..."
    mean "Shine your light up."
    hide screen flashlight_demo
    show screen hatch_button
    window hide
    pause

label ce_after_hatch:
    show screen flashlight_demo
    mean "You mean like that one?"
    cs "Yeah, pull it open."
    play sound sfx_snowfall
    show snow_pile at center with easeintop
    pause 1.0
    n "As Mean yanks on the hatch, it bursts open downwards, as a huge pile of snow falls onto the attic floor."
    cs "That is... a lot of snow."
    mean "C'mon, let's get up here."
    n "Mean climbs up onto the roof."
    show mean human at Move((0.54, 0.0), (0.35, 0.0), 0.5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 0.5
    show mean human at Move((0.35, 0.0), (0.35, -0.4), 0.15, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 0.15
    show mean human at Move((0.35, -0.4), (0.35, -0.2), 0.15, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 0.75
    show mean human at Move((0.35, -0.2), (0.35, -0.7), 0.5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 0.5
    show mean human at Move((0.35, -0.7), (0.35, -0.5), 0.75, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 0.75
    show mean human at Move((0.35, -0.5), (0.35, -1.2), 0.5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    mean "Holy..."
    mean "Fuck."
    cs "What? How bad is it?"
    mean "Grab my hand, I'll pull you up."

label ce_snowed_in:
    play music winters_halloween
    music winters_halloween
    scene snowed_in
    hide screen flashlight_demo
    show cs sil_black:
        zoom 0.15
        xpos 0.3
        ypos 0.5
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.4
        ypos 0.5
    show snow1
    show snow2
    show snow3
    show snow4
    show snow5
    show snow6
    show snow_wind
    with dissolve
    mean "Look out in the distance."
    n "As CS and Mean stare out into the distance, they see nothing but an endless desert of snow, with the lamp poles poking out through."
    cs "What the fuck."
    cs "Am I dreaming?"
    n "CS picks up some snow and shoves it in his face."
    cs "I guess not..."
    mean "I know, this doesn't even feel real. How did this happen so fast?"
    mean "I live in Canada, and it's never {i}this{/i} bad."
    cs "So this is it. We are stuck here, aren't we?"
    mean "I don't fuckin' know how any of us would be able to fix this, man."
    cs "A Christmas miracle, maybe."
    cs "I don't think anyone else back in the house is gonna believe us."
    mean "Well they can see it from themselves."
    mean "Let's get back inside, it's freezing out here."
    scene black with dissolve
    n "CS and Mean climb back down and meet back up with everyone."
    scene cs_living2_off_festive
    show cs disappointed christmas at mid_left
    show mean human annoyed flipped at mid_offscreen_left
    show ed festive at right
    show digi sad at mid_mid_right
    show linus festive at mid_right
    show rich festive at mid_right_right
    show tate sad festive flipped at mid_mid_left
    show obama festive at center behind digi
    show k22 disappointed at center behind digi
    show k17 disappointed at mid_mid_right behind obama
    with dissolve
    show screen flashlight_demo
    stop music fadeout 3.0
    music end
    cs "Well, guys, we've got some bad news."
    cs "We might be stuck here for a while."
    k22 "Like... for a couple of hours? All night?"
    cs "Uhh..."
    cs "At least for the night."
    ed "Gee, where are we all gonna sleep?"
    linus "There's no way we can dig our way out?"
    digi "If it's that bad, wouldn't a snow plow be here soon anyways?"
    show cs worried christmas
    rich "We've dealt with worse, let's get out there and shovel!"
    show cs disappointed christmas
    show mean human angry flipped
    show tate shock festive flipped
    mean "Everyone! Stop!"
    mean "There's, like, 20 feet of snow."
    n "Everyone goes quiet."
    mean "If you want to go up to the roof and check for yourself, go ahead."
    show mean human annoyed flipped
    show tate sad festive flipped
    mean "I couldn't believe it either, but..."
    mean "There's nothing but snow, snow, and even more snow."
    mean "I'm from {i}Canada,{/i} and I've never seen so much snow."
    blank "I didn't even think you could {i}get{/i} that much snow..."
    show cs christmas
    cs "So... that means we are gonna have to wait it out!"
    show cs happy
    cs "And, what better way to kill time than to play some games?"
    show cs christmas
    michael "I spy something, black!"
    nova "Is it Obama?"
    show digi disappointed
    show mean human flipped
    show tate flipped festive
    obama "Hey!"
    michael "No, it is not."
    show digi sad
    aria "Is it everything?"
    michael "Correct!"
    cs "Okay, I have something I've wanted to play again with someone."
    cs "I have a few board games somewhere, I just need to look."
    show tate sad festive flipped
    tate "{i}Please{/i} tell me it's not chess..."
    cs "It's better than chess! I'll be back."
    scene black with dissolve
    n "After a bit of rummaging, CS comes back with a blueish-looking box."
    scene cs_living2_off_festive
    show cs happy christmas at mid_left
    show reversi_box at mid_left
    show mean human flipped at mid_offscreen_left
    show ed festive at right
    show digi sad at mid_mid_right
    show linus festive at mid_right
    show rich festive at mid_right_right
    show tate sheepish festive flipped at mid_mid_left
    show obama festive at center behind digi
    show k22 disappointed at center behind digi
    show k17 disappointed at mid_mid_right behind obama
    with dissolve
    cs "It's Reversi!"
    show digi 
    digi "You have an {i}actual{/i} Reversi board?"
    k17 "Isn't that the one game from Windows 3.1?"
    cs "Precisely!"
    n "CS takes off the cover and starts taking the pieces out."
    aria "Wait a second."
    aria "This is Othello, not Reversi."
    show cs disappointed christmas
    cs "What do you mean? It says Reversi on the box!"
    aria "Yeah, I know, but in 1971--{w=1.5}{nw}"
    show cs angry christmas
    cs "It's fucking Reversi, okay?"
    cs "I just{w=0.5} want to play{w=0.5} some Reversi."
    show cs christmas
    cs "Who wants to play with me?"
    # maybe pick a character to play here?
    # TODO: Insert Reversi Gameplay here

label ce_billy_time:
    scene cs_living2_off_festive
    show cs christmas at mid_left
    show mean human flipped at mid_offscreen_left
    show ed festive at right
    show digi at mid_mid_right
    show linus festive at mid_right
    show rich festive at mid_right_right
    show tate sheepish festive flipped at mid_mid_left
    show obama festive at center behind digi
    show billy festive at center
    show k22 disappointed at center behind digi
    show k17 disappointed at mid_mid_right behind obama
    with dissolve
    billy "Wait! Everyone, hold on!"
    cs "What? What is it, Billy?"
    play music on_the_rocks
    music on_the_rocks
    billy "The Handy Switch!"
    billy "Who got my Handy Switch for their gift?"
    show tate festive
    tate "Me!"
    billy "Follow me to the basement!"
    show cs disappointed christmas
    cs "Billy, what are you doing?"
    billy "Hi, Billy Mays here, for this {i}great{/i} idea! We'll be right back!"
    hide billy with moveoutleft
    show tate sheepish festive flipped
    tate "I guess I'm following Billy, so, I'll be back...?"
    hide tate with moveoutleft
    scene black with dissolve
    hide screen flashlight_demo    
    billy "Oh, dang it! I forgot to bring a light!"
    scene cs_hallway_off
    show billy festive at mid_left
    show tate festive at center
    show elizabeth at right
    show screen flashlight_demo
    with dissolve
    tate "I have my phone!"
    billy "That works! I think the basement is down here!"
    eliza "Did you guys manage to get outside?"
    billy "Apparently, the snow is up to the roof!"
    n "Elizabeth looks shocked."
    billy "But, good news! I have a way to possibly bring the power back!"
    billy "With the Handy Switch!"
    eliza "I have no clue how that's gonna work, but good luck to you two."
    tate "Is the basement over this way?"
    eliza "Yeah, down the hall and to the left."
    show tate sheepish festive
    tate "Thank you... Mika?"
    eliza "It's Elizabeth, but sure."
    hide tate
    hide billy
    with moveoutright
    scene cs_bathroom_off
    show grace at mid_right
    show anne at right
    with dissolve
    show tate festive at center
    show billy festive at mid_left
    with moveinleft
    grace "Hey! You're the TV man!"
    anne "Grace always wanted to buy every product you sold."
    billy "You should! Hi, Billy Mays here for the--"
    show tate sheepish festive flipped
    tate "Billy, the power?"
    billy "Oh, yeah. We can talk later!"
    show tate festive
    hide tate
    hide billy
    with moveoutright
    grace "I'll be waiting, Billy!"
    n "Billy and Tate run into the basement."
    scene cs_basement
    show kitty festive at left
    show arceus worried flipped at mid_left
    show tate festive flipped at center
    show billy festive at mid_right
    with dissolve
    arceus "Tate? Billy?"
    kitty "What's going on?"
    billy "Fixing the power, with the power, of the Handy Switch!"
    show tate sheepish festive flipped
    tate "Don't ask."
    scene breakerbox
    show tate festive at mid_left
    show billy festive at mid_right
    with dissolve
    n "Finally, Billy and Tate make it to the breaker."
    billy "Alright, all you gotta do is put the switch onto the breaker!"
    show tate sheepish festive
    tate "Really? Just, like... slap it on?"
    billy "Yes! It's {i}that{/i} easy!"
    show handy_switch at Move((0.3125, 0.4), (0.3125, 0.4), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    n "Tate slaps the Handy Switch onto the breaker and flips the switch."
    play sound sfx_snd_lightswitch
    show tate shock festive
    hide screen flashlight_demo
    tate "Wh-- {i}how?!"
    billy "Like {i}magic!"
    show tate sheepish festive
    tate "How... how does this even work, Billy?"
    n "Billy ponders for a moment."
    pause 3.0
    billy "I don't even know myself!"
    show tate festive
    tate "Well, what're we waiting for?"
    tate "Let's get back upstairs and share the good news!"
    hide tate
    hide billy
    with moveoutright
    scene cs_basement
    show kitty festive at left
    show arceus happy flipped at mid_left
    with dissolve
    show tate festive at mid_mid_right
    show billy festive at right
    with moveinleft
    arceus "Would you look at that?"
    kitty "How did you guys do it?"
    billy "That's the {i}power{/i}...{w=0.5} of the {i}power!"
    hide tate
    hide billy
    with moveoutright
    scene cs_hallway
    show eliza at mid_right_right
    show grace at mid_right
    show anne at right
    with dissolve
    show tate festive flipped at mid_left
    show billy festive at center
    with moveinright
    grace "Yay! The power is back!"
    anne "You did it!"
    billy "We sure did!"
    eliza "I don't know what kind of technology you have that fixed this, but, good job!"
    hide tate
    hide billy
    with moveoutleft
    scene cs_living2_festive
    show cs christmas flipped at center
    show mean human at mid_offscreen_right
    show sheriff festive at mid_mid_right
    show copguy festive at mid_right
    show luke festive at mid_left
    show rich festive flipped at mid_mid_left behind cs
    with dissolve
    show tate festive at mid_left
    show billy festive at left
    with moveinleft
    cs "Holy crap, the power is back!"
    sheriff "My eyes work again!"
    ed "Hooray!"
    tate "It looks like all we needed was Billy's Handy Switch!"
    show mean human angry
    show tate sheepish festive
    mean "{i}Please{/i} don't say it like that, Tate."
    show mean human
    show tate festive
    stop music fadeout 3.0
    music end
    luke "This is great and all, but, isn't the house still under 20 feet of snow?"
    copguy "How are we even gonna get rid of that?"
    copguy "We would need a lot of..."
    pause 1.0
    show cs christmas
    cs "A lot of what?"
    copguy "... Never mind. I forgot what I was thinking about."
    rich "Didn't you guys get up to the roof?"
    ed "Maybe we should all go up and check it out."
    hide mean
    hide cs
    hide copguy
    hide rich
    hide luke
    hide tate
    hide billy
    with moveoutright
    n "Everyone clammers up the stairs, and one by one, they all climb up onto the roof."
    sheriff "Welp."
    sheriff "I'll just... wait here."
    sheriff "Take a picture for me!"

label ce_roof_moment:
    scene snowed_in
    show cs sil_black:
        zoom 0.15
        xpos 0.3
        ypos 0.5
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.4
        ypos 0.5
    show arceus sil_black:
        zoom 0.15
        xpos 0.54
        ypos 0.54
    show anno sil_black:
        zoom 0.15
        xpos 0.53
        ypos 0.33
    show tate festive sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.36
    show obama sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.47
    show ed sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show rich sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.34
    show wesley sil_black:
        zoom 0.15
        xpos 0.56
        ypos 0.45
    show blank sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.34
    show nova sil_black:
        zoom 0.15
        xpos 0.55
        ypos 0.43
    show copguy sil_black:
        zoom 0.15
        xpos 0.33
        ypos 0.35
    show billy sil_black:
        zoom 0.15
        xpos 0.63
        ypos 0.46
    show aria sil_black:
        zoom 0.15
        xpos 0.42
        ypos 0.36
    show kitty sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.46
    show grace sil_black:
        zoom 0.15
        xpos 0.31
        ypos 0.31
    show anne sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show elizabeth sil_black:
        zoom 0.15
        xpos 0.38
        ypos 0.45
    show digi sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.46
    show linus sil_black:
        zoom 0.15
        xpos 0.46
        ypos 0.35
    show luke sil_black:
        zoom 0.15
        xpos 0.32
        ypos 0.45
    show db sil_black:
        zoom 0.15
        xpos 0.5
        ypos 0.6
    show k17 sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.2   
    show k22 sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.23    
    show snow1
    with dissolve
    k22 "So it is as bad as you said."
    wesley "It just keeps going! It never ends!"
    tate "What are we going to do? We can't just walk out there!"
    copguy "I've got an idea. You guys, move over there..."
    show cs sil_black at Move((0.3, 0.5), (0.27, 0.33), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show k22 sil_black at Move((0.45, 0.23), (0.34, 0.29), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show arceus sil_black at Move((0.54, 0.54), (0.3, 0.4), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show mean human flipped sil_black at Move((0.4, 0.5), (0.32, 0.4), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show anno sil_black at Move((0.53, 0.33), (0.32, 0.48), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show tate festive sil_black at Move((0.34, 0.36), (0.29, 0.5), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show obama sil_black at Move((0.47, 0.47), (0.27, 0.49), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show ed sil_black at Move((0.34, 0.43), (0.25, 0.47), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    copguy "And, all of you, move {i}there..."
    show rich sil_black at Move((0.45, 0.34), (0.45, 0.31), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show wesley sil_black at Move((0.56, 0.45), (0.5, 0.36), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show blank sil_black at Move((0.43, 0.34), (0.52, 0.40), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show nova sil_black at Move((0.55, 0.43), (0.5, 0.45), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show copguy sil_black at Move((0.33, 0.35), (0.45, 0.5), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show billy sil_black at Move((0.63, 0.46), (0.42, 0.36), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show aria sil_black at Move((0.42, 0.36), (0.41, 0.40), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show kitty sil_black at Move((0.43, 0.46), (0.42, 0.48), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.0
    show anne sil_black at Move((0.34, 0.42), (0.65, 0.31), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show k17 sil_black at Move((0.43, 0.2), (0.68, 0.29), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show elizabeth sil_black at Move((0.38, 0.45), (0.6, 0.35), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show digi sil_black at Move((0.47, 0.46), (0.63, 0.39), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show linus sil_black at Move((0.46, 0.35), (0.66, 0.39), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show luke sil_black at Move((0.32, 0.45), (0.64, 0.44), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show db sil_black at Move((0.5, 0.6), (0.63, 0.5), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show obama sil_black at Move((0.47, 0.47), (0.58, 0.47), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 4.0
    copguy "That should work!"
    k17 "SoS? Nice DaThings reference."
    k22 "You idiot, it's an emergency code! If any airplanes see us--"
    k17 "Yeah, I know. I was just making a joke."
    k22 "Also, DaThings is a girl now."
    k17 "Huh?!"
    ed "Are there even gonna {i}be{/i} any airplanes in the sky? It's Christmas Eve!"  # why would there be no planes in the sky on Christmas eve, huh? -- Digi
    wesley "Maybe we need some lights for visibility."
    cs "What's to say people are still alive? Who knows how far this glacier goes?"
    digi "CS, do you really think we are the last people left?"
    cs "I don't know. I just worry that this is--"
    play sound sfx_jingle volume 0.2
    n "As CS becomes more frantic, a noise from far away can be heard."
    k17 "Shhh! Do you hear that?"
    cs "What? What is it?"
    play sound sfx_jingle volume 0.4
    k17 "I hear jingling! Does anyone hear jingling?"
    rich "Yeah, I do! It's coming from over there!"
    n "Richard points up in the sky."
    play sound sfx_jingle volume 0.6
    k17 "Yeah, I see it!"
    aria "Is that..."
    digi "It has to be Santa! He's really up there, I think!"
    wesley "What? I don't hear or see anything! Where?"
    cs "Wait a minute... I have an idea!"
    ed "Yeah, I can see him it's almost clear as day! There's Rudolph at the end, see that red light?"
    cs "Guys! You all have to believe! Believe in Santa, and in the Christmas spirit!"
    eliza "Do you really think that will work?"
    cs "We've gotta try! Sing with me guys!"
    # TODO: Karaoke lyrics
    cs "{image=note_small1.png} Ohhh... {image=note_small2.png}"
    cs "{image=note_small1.png} You better watch out... {image=note_small2.png}"
    cs "{image=note_small1.png} You better not cry... {image=note_small2.png}"
    cs "{image=note_small1.png} Better not pout, I'm telling you why... {image=note_small2.png}"
    cs "{image=note_small1.png} Santa Claus is coming to town! {image=note_small2.png}"
    cs "Come on guys, you gotta sing!"
    k17 "{image=note_small1.png} He's making a list... {image=note_small2.png}"
    k17 "{image=note_small1.png} And checking it twice... {image=note_small2.png}"
    grace "{image=note_small1.png} Gonna find out who's naughty and nice... {image=note_small2.png}"
    # TODO: would be funny to put michael rosen noice sfx here once we figure out timings
    rich "{image=note_small1.png} Santa Claus is coming to town! {image=note_small2.png}"
    tate "{image=note_small1.png} He sees you when you're sleeping... {image=note_small2.png}"
    mean "{image=note_small1.png} He knows when you're awake... {image=note_small2.png}"
    db "{image=note_small1.png} He knows if you've been bad or good... {image=note_small2.png}"
    obama "{image=note_small1.png} So, you'd better be good. For goodness sake! {image=note_small2.png}"
    cs "{image=note_small1.png} Ohhh... {image=note_small2.png}"
    everyone "{image=note_small1.png} You better watch out... {image=note_small2.png}"
    everyone "{image=note_small1.png} You better not cry... {image=note_small2.png}"
    everyone "{image=note_small1.png} Better not pout, I'm telling you why... {image=note_small2.png}"
    everyone "{image=note_small1.png} Santa Claus is coming to town! {image=note_small2.png}"
    scene car plains night:
        zoom 2.0
    show snow1
    show snow2
    show snow3
    show snow4
    show snow5
    show snow6
    show snow_wind
    show sleigh
    with dissolve
    santa "Ho ho ho!"
    santa "The wind really started to pick up around here, didn't it, Vixen?"
    santa "Ho ho, do you all hear that? It sounds like Christmas cheer being spread down on the ground!"
    santa "Shine your light down there, Rudolph!"
    santa "Hey, wait a minute!"
    santa "Is that an SoS signal?"
    santa "Ho ho ho! Nice DaThings reference!"
    if fun_value(FUN_VALUE_RARE):
        santa "Did you hear she's a girl now?"
    santa "Okay, seriously, I should probably go down there and check it out."
    scene cs_roof
    show cs happy christmas at left
    show obama festive at mid_mid_left behind k17
    show billy festive at center behind cs
    show michael festive at mid_left
    show ed festive at mid_right
    show linus festive at mid_mid_right
    with dissolve
    cs "We did it, guys! Santa's here to save us!"
    n "Santa's sleigh begins its descent, slowing down to a crawl as the reindeer gently touch down onto the snow."
    play music snow_blind
    music snow_blind
    show santa at right with moveinright
    santa "Ho ho ho! Merry Christmas, everyone!"
    show grace at mid_right with easeinleft
    grace "{i}SAANNNNNTAAA!!"
    grace "OH MY GODD!!"
    show k22 flipped at mid_left
    show k17 happy flipped at mid_mid_left 
    with moveinleft
    k17 "Haha, see, K-22? Who needs Addy's party when we can literally meet The Big Man himself?"
    show k22 happy flipped
    k22 "Heh, I guess you've got a point, there. They aren't gonna believe this!"
    show cs christmas
    santa "Well, let's see, who do we have here...?"
    santa "..."
    santa "Mr. President? What are you doing here?"
    show obama festive at center with move
    obama "Well, I wanted to go to my good friend CS' Christmas party!"
    santa "Ho ho, well..."
    n "Santa stares around the crowd."
    show k17
    show k22
    with determination
    hide k17
    hide k22
    with moveoutleft
    santa "Ed? Richard? Welsey? Keep up the good work! Might even need some foundation repair at my workshop very soon! Ho ho!"
    show rich festive flipped at mid_mid_left with moveinleft
    show wesley festive flipped at mid_left with moveinleft
    rich "Really!?"
    ed "We appreciate the offer, Mr. Claus. Let's keep in touch!"
    santa "...and, you there! Mr. Rosen!"
    show michael festive at center with move
    santa "Don't let those YouTube Poopers get to your head! You're a brilliant author."
    n "Santa glances at CS."
    show cs disappointed christmas
    cs "Hey! I love his work too! I don't even really use Michael as a source anymore!"
    n "Both Michael and Santa laugh."
    show cs christmas
    santa "Ah, yes, Linus and Luke..."
    santa "We might need your help at the North Pole, as well. Lots of kids these days want these {i}crazy{/i} gaming PCs!"
    linus "Absolutely! Just give LTT a call!"
    santa "There are certainly a lot of... people here I would not expect to see."
    show rich festive
    show wesley festive
    with determination
    hide rich
    hide wesley
    hide michael
    hide obama
    hide ed
    with moveoutleft
    santa "Billy Mays, I almost forgot about... you coming back."
    hide linus with moveoutleft
    billy "Don't worry, Santa! My drug days are over!"
    santa "Ho ho ho! That's the spirit!"
    santa "Well, I could keep going, but I should ask..."
    santa "What {i}happened{/i} here? New York shouldn't get this much snow..."
    show cs disappointed christmas
    cs "None of us know, but we've been trapped inside the house for God knows how long."
    cs "I mean, you're Santa Claus! Surely, {i}you{/i} can fix this?"
    santa "Ho ho ho..."
    santa "I... don't believe that I can, unfortunately."
    santa "I may be Father Christmas, but, my magic can't melt snow away."

    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        # i am definitely dating myself with this reference - tate
        show cs scared christmas
        santa "{i}That{/i} is the Heat Miser's domain, and I certainly don't want to end up in {i}his{/i} hot seat!"
        show cs disappointed christmas

    santa "I'm sorry, cs188."
    copguy "Well, wait a second!"
    show copguy festive flipped at center with moveinleft
    copguy "Can't we wish for one gift? For Christmas?"
    santa "Now, {i}that,{/i} I can do!"
    santa "CS? Do you have a gift that you've always wanted?"
    cs "Hmm..."
    show copguy festive
    copguy "CS, I think I know just the thing."
    show copguy festive at mid_left with move
    n "Copguy whispers in CS' ear."
    show cs surprised
    cs "Oh! You sure that'll work?"
    n "Copguy nods."
    show cs christmas
    show copguy festive flipped with determination
    show cs christmas at center with move
    cs "Alright, Santa, I have my wish."
    show cs christmas at mid_right with move
    n "CS whispers into Santa's ear."
    play sound sfx_whisper volume 0.5
    pause 1.0
    n "Santa's eyes widen."
    santa "Ho ho ho! Well..."
    santa "I guess I could do that."
    scene snowed_in
    show cs sil_black:
        zoom 0.15
        xpos 0.3
        ypos 0.5
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.4
        ypos 0.5
    show arceus sil_black:
        zoom 0.15
        xpos 0.54
        ypos 0.54
    show anno sil_black:
        zoom 0.15
        xpos 0.53
        ypos 0.33
    show tate festive sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.36
    show obama sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.47
    show ed sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show rich sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.34
    show wesley sil_black:
        zoom 0.15
        xpos 0.56
        ypos 0.45
    show blank sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.34
    show nova sil_black:
        zoom 0.15
        xpos 0.55
        ypos 0.43
    show copguy sil_black:
        zoom 0.15
        xpos 0.33
        ypos 0.35
    show billy sil_black:
        zoom 0.15
        xpos 0.63
        ypos 0.46
    show aria sil_black:
        zoom 0.15
        xpos 0.42
        ypos 0.36
    show kitty sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.46
    show grace sil_black:
        zoom 0.15
        xpos 0.31
        ypos 0.31
    show anne sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show elizabeth sil_black:
        zoom 0.15
        xpos 0.38
        ypos 0.45
    show digi sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.46
    show linus sil_black:
        zoom 0.15
        xpos 0.46
        ypos 0.35
    show luke sil_black:
        zoom 0.15
        xpos 0.32
        ypos 0.45
    show db sil_black:
        zoom 0.15
        xpos 0.5
        ypos 0.6
    show k17 sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.2   
    show k22 sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.23
    show santa sil_black:
        zoom 0.15
        xpos 0.65
        ypos 0.5    
    show snow1
    with dissolve
    santa "Alright! Stand back, everyone! This is gonna take a lot of focus!"
    n "Harnessing the power of the Christmas spirit, CS' wish becomes a reality!"
    show crotch_doctor sil_black:
        zoom 0.75
        xpos 0.7
        ypos -0.35
    with moveintop
    pause 1.0
    show crotch_doctor:
        zoom 0.75
        xpos 0.7
        ypos -0.35
    with dissolve   
    santa "Ta-da!"
    cs "Wow, that really worked?!"
    billy "A giant bottle of Crotch Doctor?"
    copguy "Yeah! It can {i}instantly{/i} melt snow!"
    copguy "I sell this stuff door-to-door as a side-gig! It works {i}great!"
    cs "Wait, {i}you're{/i} Carguy?!"
    copguy "How.{w=0.25}.{w=0.25}.{w=0.25} have you never picked up on that?"
    billy "CS, are you sure this will work? I don't believe this..."
    cs "Don't believe me."
    cs "Just watch."
    stop music fadeout 3.0
    music end
    show crotch_doctor:
        zoom 0.75
        xpos 0.5
        ypos -0.4
        linear 15 rotate -60
    santa "Ho ho, oh no. It's tipping towards us."
    santa "Oh, shit."
    scene black with dissolve
    play sound sfx_splash
    n "A tsunami of car cleaner engulfs the group, washing them all off the roof."
    n "As everyone gathers their bearings, they watch in amazement as the waves of Crotch Doctor carry all the snow away."
    scene cs_house_night_dtree
    show cs christmas dark at mid_left
    show tate festive dark at left
    show obama festive dark at mid_right
    show copguy festive dark at mid_mid_right
    show k17 dark
    show santa dark at right
    with dissolve
    cs "Woohoo! We did it! The avalanche covering the house is gone!"
    santa "Ho ho, well, it looks like you helped save Christmas, CS."
    santa "I need to get going now. I am slightly off-schedule."
    santa "I should also make sure my steed didn't drown in car cleaner..."
    cs "Good luck to you, Santa!"
    hide santa with moveoutleft
    show k17 happy dark
    k17 "CS? Did you see that?"
    cs "Yeah, I was kind of there with everyone one."
    show k17 disappointed dark
    k17 "Sorry, that was a stupid question."
    show k17 dark
    tate "CS! You did it!"
    obama "I gotta say, that was one of the most fun Christmas parties I've ever been to."
    obama "Although, I should probably get back to the White House. The political circus is probably getting out of hand."
    hide obama with moveoutleft
    show sheriff festive dark at right with moveinright
    sheriff "Hey, guys, what'd I miss?"
    sheriff "Where's all this snow you were all so worried about?"
    cs "Uhhh..."
    play sound sfx_jingle volume 0.7
    n "As everyone is talking, the jingling of bells can be heard rushing over CS' house."
    show sleigh behind copguy:
        zoom 0.2
        rotate -10
    show sleigh at Move((0.45, 0.1), (1.1, -0.2), 7, repeat=False, bounce=False, xanchor="left", yanchor="top")
    santa "Ho ho ho! Merry Christmas, everyone!"
    show snow3
    show snow4
    with dissolve
    n "As Santa flies past, the snow begins to fall again."
    sheriff "Well, Copguy, we should probably get going before we get snowed in again!"
    show copguy festive dark flipped
    show sheriff festive dark flipped
    with determination
    hide sheriff
    hide copguy
    with moveoutright
    copguy "Hey, look how at shiny our car is!"
    sheriff "Wow!"
    copguy "I {i}told{/i} the chief we should start using this stuff on our cruisers!"
    if d20 == 20:
        show avgn dark flipped at mid_right with moveinright
        avgn "Man, this party was ass!"
        hide avgn with moveoutleft
    scene cs_house_night_dtree
    show billy festive dark at mid_left
    show k22 disappointed dark at mid_right
    with dissolve
    n "As everyone is wrapping up to go home, K-22 and Billy have a bit of a chat."
    k22 "Hey Billy, can I talk to you for a minute?"
    billy "Sure thing! I have a moment."
    k22 "I, uhh... had a customer who wanted you to make something for them."
    n "K-22 hands Billy a folded up piece of paper."
    k22 "All of the instructions are on there I was told."
    k22 "Follow them word for word."
    n "Billy opens up the paper and skims through it."
    billy "Wow."
    billy "This is great! I'll get to work on this soon."
    billy "I gotta take a trip to France."
    billy "I need to... fix an old friend."
    show k22 dark
    k22 "Alrighty, well, see you later Billy!"
    billy "See ya!"
    n "Both parties get into their cars and drive off."
    scene cs_bedroom1_ce
    show cs happy christmas at center
    with dissolve
    cs "That was such a blast!"
    cs "Plus, my car got cleaned for free!"
    cs "What a mess, though. I'm gonna wait for tomorrow to clean this up."
    cs "Maybe I can call Anno again to help!"
    cs "For now, I should probably get to streaming."
    cs "Those car crash compilations aren't gonna watch themselves!"
    scene black with dissolve
    n "As CS entered his room to start streaming, our story here comes to a close."
    n "It wasn't the Christmas that CS expected, but it was one of the jolliest times he's had."
    n "Merry Christmas, and have a Happy New Year!"
    $ ending_manager.mark("christmas")
    pause 5.0

# Epilogue
label ce_epilogue:
    show billycar1:
        zoom 2.5
    show billycar1 at Move((-1.5, -1.0), (0.0, -1.25), 10, repeat=False, bounce=False, xanchor="left", yanchor="top") with dissolve
    billy "Damn it, where did I put my other Handy Switch?{w=9}{nw}"
    show billycar2:
        zoom 2.5
    show billycar2 at Move((0.0, -0.25), (-1.5, 0.0), 10, repeat=False, bounce=False, xanchor="left", yanchor="top") with dissolve
    billy "I could've {i}sworn{/i} I had a spare in here somewhere...{w=9}{nw}"
    show billycar3:
        zoom 2.5
    show billycar3 at Move((0.0, -0.25), (-1.25, -0.5), 10, repeat=False, bounce=False, xanchor="left", yanchor="top") with dissolve
    billy "Lemme check the back seat...{w=9}{nw}"
    window hide
    show christmas_finisher with dissolve
    pause
    # Pan over shot of the schematic for the Billy pot

