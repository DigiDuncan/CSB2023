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
    dxcom writing
    n "CS wakes up to a snowy winter morning."
    if fun_value(FUN_VALUE_MUSIC):
        cs "Oh, {i}yes!{/i} Let's hear my Christ!"
        cs "It also snowed today!"
    else:
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
        play sound ["<silence 0.125>", sfx_fish]
        cs_nobeep "Fish!"
        cs "But, more importantly..."
    cs "I finally get to throw a huge Christmas party at my house!"
    show cs happy flipped
    cs "I'm so pumped! I should call everyone one more time to make sure they're still coming."
    hide screen dxcom
    play sound sfx_ring_once
    show cs happy phone flipped with dissolve
    # i am putting the item collection for non-CE items here anyway in case we do include item collection in CE standalone - tate
    $ collect("cs_phone")
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
        $ achievement_manager.unlock("timber")
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
        cs "This is gonna take {i}forever{/i} to clean up!"
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
        n "CS gazes upon his stash of lights and baubles and feels a little overwhelmed."
        cs "Wow, this is more than I thought..."
    cs "Maybe I should call someone over to help."
    cs "I wonder if Anno is around."
    show cs disappointed phone with dissolve
    play sound sfx_ring_once
    pause 0.5
    show cs disappointed phone at mid_left with move
    show anno_house at mid_offscreen_right
    show anno phone at mid_right
    with moveinright
    $ collect("anno_phone")
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
    anno "... But I can do that tomorrow."
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

    dxcom cs_wardrobe

    if tree_first:
        scene cs_garage_mess with dissolve
        show cs disappointed coat hat at offscreenleft
        show cs disappointed coat hat at mid_mid_left with moveinleft
        show cs scared coat hat
        play sound sfx_spikes
        cs "Shit!" with hpunch
        show cs worried coat hat
        if fun_value(FUN_VALUE_COMMON):
            cs "I hate Legos, but only when they're in my feet!"
        else:
            cs "I love Legos, but not when they're embedded in my {i}feet!"
        cs "Now, where did I last put..."
    else:
        scene cs_garage
        show garage_shelf at manual_pos(0.9, 0.5, 0.5)
        with dissolve
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
    hide screen dxcom
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
    if fun_value(FUN_VALUE_MUSIC):
        n "As CS closes the door behind him, he is greeted by a massive pile of snowy snow blocking the garage."
    else:
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
    play sound [ "<silence 1.0>", sfx_shovel_single]
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
    play sound [ "<silence 1.0>", sfx_shovel_single]
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
    play sound [ "<silence 1.0>", sfx_shovel_single]
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
    play sound sfx_shoveling
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
    if not tree_first:
        show tree_box at manual_pos(0.5, 0.9, 0.5):
            zoom 0.8
        show decor_boxes at manual_pos(0.4, 0.6, 0.5):
            zoom 0.8
        show lights_box at manual_pos(0.6, 0.7, 0.5):
            zoom 0.8
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
    anno "How the {i}hell{/i} did you manage to run into Billy Mays?!"
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
        show cs at offscreenright with MoveTransition(1.0)
        hide anno with moveoutright
        n "Anno follows CS into the garage."

        scene cs_garage_mess with dissolve
        show cs disappointed at center
        show anno at left
        with moveinleft
        n "Anno gawks at the mess on the floor, carefully avoiding the scattered Legos."
        anno "Damn, bitch, you {i}live{/i} like this?"
        cs "... I may have had a... {i}small{/i} mishap when I was trying to get the tree out."
        anno "{i}\"Small\"?!" with vpunch
        show cs worried flipped
        cs "Okay, maybe {i}not-{/i}so-small, but do you think you can help me?"
        show cs disappointed
        cs "I figured it'd be faster if I had a helping hand."
        n "Anno groans."
        anno "I was hoping to be {i}setting up{/i} decorations, not {i}cleaning them{/i} up."
        anno "But... I guess we don't really have any other option, do we?"
        cs "Guess not..."
        show cs disappointed at mid_right with move
        cs "Here, I'll grab these boxes, and we'll start throwing stuff in them."
        pause 0.5
        scene black with dissolve
        play sound sfx_items_rustling volume 4.0
        pause 3.0
        n "After about an hour, they manage to clean up the mess without stepping on too many more Legos."
        n "CS and Anno drag the remaining boxes inside."
    else:
        anno "So, you needed my help with decorating, right?"
        show cs
        cs "Yeah. I've already brought everything in, so let's start unpacking it."
        anno "Alright!"
        scene black with dissolve
        play sound sfx_items_rustling volume 4.0
        pause 1.0
        centered "20 minutes later..."

# Setting up decorations
label ce_setup:
    stop music fadeout 3.0
    stop sound fadeout 2.0
    music end
    scene cs_living2
    show cs at left
    show anno at right
    with dissolve
    cs "Well, Anno, we did it!"
    cs "Are ya ready?"
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
    cs "Everyone is gonna have a {i}blast{/i} at this party!"
    show cs
    anno "Before I get going, was there anything else you needed help with?"
    show cs disappointed
    cs "No, I don't think so..."
    pause 1.0
    show cs worried with vpunch
    n "CS remembers that he didn't buy any food for the party."
    cs "Shit, I do need to go shopping. I don't have anything for Christmas dinner!"
    anno "Well, I can't help you with that one. At least you've still got today and tomorrow to get it done."
    show cs
    cs "Yeah, I think I'm gonna head out here in a moment. I just need to make a list."
    if fun_value(FUN_VALUE_COMMON):
        cs "And,{w=0} check it twice!"
    anno "Alrighty, well, good luck with that!"
    anno "I'll see you in two days!"
    cs "Yeah, see you then! Bye for now, Anno!"
    hide anno with moveoutright
    pause 1.0
    play sound sfx_house_door_open
    pause 2.0
    play sound sfx_house_door_close
    pause 0.5
    show cs flipped with determination
    hide cs with moveoutleft
    scene cs_bedroom1_ce with dissolve
    pause 0.5
    show cs disappointed at center with moveinleft
    pause 0.5
    n "As he finds himself alone in the house once more, CS starts to worry."
    show cs angry
    cs "Damn it, I can't believe I forgot about the {i}food!"
    show cs disappointed
    cs "Every store is gonna be extremely busy tomorrow, so I should probably go now..."
    cs "What to buy..."
    cs "Probably some pies... I think Michael was gonna make some mashed potatoes, so I should get some of those..."
    show cs
    cs "You know what? I've got some time. I should de-stress with some car crash compilations."
    show cs flipped
    n "CS puts on a new compilation video and relaxes on his couch."
    scene black with dissolve
    pause 3.0
    scene cs_bedroom1_ce_car
    show cs
    with dissolve
    cs "... So, out of 500 crashes..."
    show cs happy
    cs "That's about 257 red cars at fault!"
    show cs worried
    cs "Yikes! Thank God {i}I{/i} don't have a red car."
    # What I love about that line is it implies that CS would be suddenly worse at driving if he owned a red car. -- Digi
    show cs
    cs "I'm feeling a lot better now. I should probably go get that shopping done!"
    show cs flipped
    n "CS glances at the time."
    show cs scared flipped
    cs "Oh no! It's 3AM!" with vpunch
    show cs disappointed flipped
    cs "Damn it! The time really flew!"
    show cs worried flipped
    cs "I'll have to go during the rush tomorrow!"
    show cs disappointed flipped
    cs "I guess I can finish my shopping list right now, then I'll go get some sleep..."
    cs "Hmm... what else do I need?"
    scene black with dissolve
    n "After about another hour of making a list and not watching motor mayhem twice, CS finally heads to bed."
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
    cs "Thank goodness it didn't snow overnight. Shoveling yesterday fuckin' {i}sucked."
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
    pause 0.5
    play sound sfx_shopping_cart
    n "CS grabs a cart before venturing further into the store."
    pause 1.0
    show cs coat at offscreenleft
    show shopping_cart at manual_pos(-0.2, 1.1, 0.75)

    show shopping_cart at Move((-0.2, 0.6), (1.1, 0.6), 0.5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    hide cs with moveoutright
    $ collect("shopping_cart")

    # Shopping
    scene tgt_tater with dissolve
    show cs coat at center
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with moveinleft


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
    show potato_bag at manual_pos(0.8, 0.8, 0.5) with MoveTransition(0.25)
    hide potato_bag with dissolve

    show cs coat flipped at mid_left with move
    pause 1.0

    if fun_value(FUN_VALUE_LEGENDARY):
        $ got_tato_bag = True
        # this here is some EXTREMELY DEEP tate lore.
        dxcom tato

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
    dxcom ace
    cs "Since Digi's coming, and I think they're ace, I'd better have the good stuff."
    # This is deep-cut ace jokes, CS will not understand this one. -- Digi
    show cs coat at mid_right with move
    hide screen dxcom
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

    hide screen dxcom
    hide cs
    hide shopping_cart
    with moveoutright
    pause 0.5

    scene tgt_endcap with dissolve
    pause 0.5

    show cs coat at left
    show shopping_cart at manual_pos(0.5, 1.1, 0.5)
    with moveinleft

    n "CS spots some Easy Cheese."
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

    dxcom doritos
    cs "\"3D\" Doritos? I'm pretty sure {i}all{/i} Doritos are 3D. Would be pretty hard to eat them, otherwise."
    show cs coat disappointed
    cs "You know, I think they're making these bags of chips smaller and smaller, too."
    show cs coat worried
    cs "\"Family Size\"? {i}\"Party{/i} Size\"?! Are you serious?"
    cs "I can eat one of these all by myself, and I don't {i}feel{/i} like I'm eating enough for an entire family or party..."
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
    show pringles at manual_pos(0.7, 0.8) with MoveTransition(0.25)
    hide pringles with dissolve
    $ collect("pringles")

    n "CS grabs a can of his favorite flavor before moving on to the next aisle."
    show cs coat with determination
    pause 0.5
    hide screen dxcom
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
        # *HHWHEEEEZE* - tate
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
    cs "I suppose I {i}am{/i} the same man known for uploading videos at 11:59 PM on the 31st, so I should be used to this sort of thing."
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

    # DX: tetris minigame for DX

    show cs coat happy flipped:
        parallel:
            linear 1.0 zoom 0.5
        parallel:
            linear 1.0 xpos 0.55
        parallel:
            linear 1.0 ypos 0.8
    pause 1.0
    show cs happy coat
    n "CS steps over to the display."

    # hey check out this neat trick - tate
    show black with dissolve
    centered "Way more than one round later..."
    hide black with dissolve

    n "CS finally realizes how much time has passed."
    # i changed this because CS has not actually picked up anything cold yet, so nothing would be condensating - tate

    show cs coat scared
    cs "Oh, shoot!" with hpunch
    cs "Right! I need to actually accomplish things today!"
    show cs worried coat at right with move:
        linear 0.5 zoom 1.0
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
    pause 0.5

    scene tgt_frozen with dissolve
    pause 0.5

    show cs coat at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    with moveinleft
    pause 0.5

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
    pause 0.5

    scene tgt_alcy with dissolve
    pause 0.5

    show cs coat at center
    show shopping_cart at manual_pos(0.8, 1.1, 0.5)
    with moveinleft

    n "Finally, CS lands in the alcohol section."
    cs "I know at least a few people I invited don't drink, but, damn it, it's Christmas. I'm grabbing some 'nog!"

    show nog at manual_pos(0.8, 0.3) with Dissolve(0.25)
    show nog at manual_pos(0.7, 0.8) with MoveTransition(0.25)
    hide nog with dissolve
    $ collect("nog")
    pause 0.25

    hide cs
    hide shopping_cart
    with moveoutright
    pause 0.5

# Checkout
label ce_checkout:
    n "With everything on his shopping list finally crossed off... and then some, CS finally heads over to the checkout lanes."
    scene tgt_line
    show streetguy flipped at mid_right_right
    show amtrak_stewardess at mid_right
    show snufkin flipped at mid_mid_right
    show customer at center
    with dissolve
    play music winter_unclearance_sale if_changed loop volume 0.3 fadein 1.0
    pause 0.5

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
    cs "Man, this place is really short-staffed, especially for the {i}holidays!"
    show customer flipped
    customer "Yeah, they're always like this. I come here every day, and it seems like there are fewer and fewer people working."
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
    dxcom checkout
    cs "What? It says I scanned this twice? No, I didn't!"
    show cs coat disappointed
    show pakoo tgt at mid_right with moveinright
    tgt_worker "Oh, yeah, it always does that. Just keep going, it's fine."
    show cs coat
    cs "Okay, thanks."
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
    hide screen dxcom
    show cs coat angry
    cs "Hey, wait a minute!"
    show pakoo tgt at mid_right with moveinright
    tgt_worker "Yeah?"
    cs "These are ringing up as $11.99 per pie!"
    show pakoo tgt upset
    cs "The sign said they were, like, 20%% off!"
    show pakoo tgt think2
    tgt_worker "Hmm..."
    show pakoo tgt scan
    play sound sfx_zebra_scan
    n "The employee scans the pie."
    show cs coat disappointed
    show pakoo tgt
    tgt_worker "Do you perchance have Target Circle?"
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
            tgt_worker "I'm sorry, but that's just how the deal works."
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

    dxcom target

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
    if fun_value(FUN_VALUE_RARE):
        cs "I'll think I'll use my credit card!"
    play sound sfx_moneyfalls
    show spent_target at t_fake_rpg_text(0.5, 0.1, 0.5)
    n "CS pays with his card before heading out to the parking lot."
    hide cs_wallet with dissolve
    show cs coat flipped at left with move
    scene tgt_checkout_finish
    show cs coat flipped at left
    show shopping_cart at manual_pos(0.4, 1.1, 0.5)
    show cs coat with determination
    pause 0.25
    hide screen dxcom
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
    n "When CS gets home, he walks to the kitchen to put groceries away."
    # fuck it, i am NOT animating this. if someone else wants to move eaech item, be my guest - tate
    hide target_bags with dissolve
    pause 1.0
    show cs flipped at center behind cs_kitchen_fg with move
    show d20:
        zoom 0.1
        linear 0.1 rotate 165 xpos 1000 ypos 600
        linear 0.2 rotate 165 xpos 800 ypos 500
        linear 0.1 rotate 165 xpos 700 ypos 700
        linear 0.1 rotate 165 xpos 600 ypos 900
        linear 0.1 rotate 165 xpos 500 ypos 1100
    play sound [ "<silence 1.0>", sfx_dice ]
    n "As he finishes up, a D20 sitting on the counter is knocked onto the floor."
    dxcom dice
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
    cs "Since when did I {i}ever{/i} own one of these?"
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
    if d20 == 1:
        $ achievement_manager.unlock("shitical")
    elif d20 == 20:
        $ achievement_manager.unlock("critical")
    cs "Hey, look, I rolled a [d20]!"
    hide d20 with dissolve
    pause 1.0

    show cs flipped behind cs_kitchen_fg
    hide screen dxcom
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
    pause 1.0
    show cs disappointed flipped
    pause 2.0
    cs "I just can't stop thinking about tomorrow."
    show cs surprised flipped
    cs "I wonder who's gonna get here first, and if everyone will show up as promised..."
    pause 2.0
    show cs scared flipped
    cs "What if {i}no one{/i} shows up?"
    show cs disappointed flipped
    cs "That would really suck..."
    pause 1.0
    show cs flipped
    cs "But there's no {i}way{/i} that would happen."
    if d20 == 1:
        cs "... Right?"
    cs "Everyone confirmed they got my invitations, and they all said on the phone that they're coming!"
    show cs happy flipped
    cs "If nothing else, I know Anno is coming for sure!"
    pause 1.0
    show cs disappointed flipped
    cs "Okay, CS, stop thinking about all these what-ifs..."
    cs "You need to sleep!"
    show cs concentrate flipped
    scene black with Dissolve(2.0)
    n "After some time, CS finally dozes off..."
    pause 1.0
    $ in_d20_viewer = False
    jump ce_party_before

# TODO: put respective vehicles in background + item collection because funnie - tate
# TODO: the item collection placeholders exist but they are not filled out.

label ce_party_before:
    stop music
    scene cs_bedroom2
    show cs happy christmas
    with dissolve
    pause 0.5
    cs "Today is the day!"
    cs "Now, I just have to wait for people to arrive!"
    show cs christmas flipped
    cs "I wonder who will arrive first..."
    pause 1.0
    if d20 == 1:
        n "CS waits patiently."
        n "He keeps on waiting."
        show cs disappointed christmas flipped
        cs "Alright, any minute now..."
        cs "The party starts in about 15 minutes, so people should start showing up soon..."
        n "CS keeps on waiting, but it looks like no one shows up early."
    elif d20 == 2:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        n "As CS asks himself this, a small car pulls up in the driveway."
        cs "Hmm, let's go see who that is!"
        hide cs with moveoutleft
        stop sound fadeout 0.5
        scene cs_house_snow_night
        show car dark at manual_pos(0.3, 0.8, 0.5):
            zoom 2.0
        $ collect("rental_car")
        show arceus festive dark flipped at mid_left
        show kitty festive dark at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        arceus "Hey, CS!"
        cs "Hey, Arc! Hey, Kitty!"
        kitty "What's up?"
        cs "Well, Merry Christmas, guys! I'm glad you could make it back to the US for this!"
        arceus "No problem! I mean, after everything we went through, how could I {i}not?"
        cs "Yeah! Well, should we get inside? It's pretty cold out."
        kitty "Well, {i}we{/i} are rather warm, but, yeah."  # british + furry = well equipped for cold
        kitty "Let's go inside."
    elif d20 == 3:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "CS peers out the window to see Anno's car pull into the driveway."
        cs "Hey, look at that! Anno's here first!"
        stop sound fadeout 0.5
        hide cs with moveoutleft
        scene cs_house_snow_night
        show anno_car dark at manual_pos(0.3, 0.8, 0.5)
        $ collect("anno_car")
        show anno festive dark at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        anno "Hey, CS!"
        anno "I know I showed up kinda early, but I wanted to see everyone's initial reactions to the decorations!"
        cs "Well, I'm glad you did! Come inside! It's cold out."
    elif d20 == 4:
        play sound sfx_nugget
        n "All of a sudden, CS hears a futuristic-sounding vehicle land outside."
        show cs disappointed christmas flipped
        cs "What the hell is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show digi_nugget_parked dark at manual_pos(0.3, 0.8, 0.5)
        $ collect("digi_nugget")
        show digi dark flipped at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        show digi happy dark flipped
        digi "Hey, CS! How've you been?"
        show digi dark flipped
        cs "Hey, Digi! I didn't know you had a... {nw}"
        show cs disappointed christmas dark flipped
        cs "Hey, Digi! I didn't know you had a... {fast}spaceship?"
        digi "Oh, yeah, this old thing. It's a bit of a nugget, but it gets the job done."
        cs "Why have I {i}never{/i} seen this before?"
        digi "Was never coming from space before."
        pause 0.5
        show digi shock dark flipped
        n "Digi shudders from the temperature." with hpunch
        show digi sad dark flipped
        digi "It's cold out. Can we go inside?"
        show cs christmas dark flipped
        cs "Yeah, let's go."
    elif d20 == 5 or d20 == 6:
        play sound sfx_train_chugging loop fadein 5.0 volume 0.4
        with hpunch
        show cs scared christmas flipped with vpunch
        with vpunch
        with hpunch
        n "As soon as he says this, the whole house starts to shake!" with vpunch
        cs "Wh--{w=0.5} what's going on?!" with hpunch
        play sound2 sfx_train_whistle noloop volume 0.75
        n "As the quaking grows stronger, a train whistle bellows out!" with vpunch
        cs "Holy shit, is that a {i}train?!" with hpunch
        hide cs with moveoutleft
        stop sound fadeout 3.0
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("mean_train")
        show mean human dark flipped at mid_left
        $ persistent.seen.add("mean_human")
        show tate festive dark at left
        with dissolve
        show cs worried christmas dark flipped at right with moveinright
        cs "That {i}is{/i} a fucking train!"
        if fun_value(FUN_VALUE_EPIC):
            show mean human angry dark flipped at mid_left
            show tate furious festive dark at left
            tate "I'm not a train!" (multiple = 2)
            mean "The {i}fuck{/i} did you call me?!" (multiple = 2) with vpunch
            show mean human dark flipped at mid_left
            show tate festive dark at left
        tate "Hey, CS! How've you been?"
        show cs christmas dark flipped
        cs "Tate? Hey! I've been great!"
        mean "Hey, CS! Merry Christmas!"
        cs "Merry Christmas to you, too... {nw}"
        show cs worried christmas dark flipped
        cs "Merry Christmas to you, too...{fast} Mean, right?"
        show mean human happy dark flipped
        mean "Yup!"
        show cs disappointed christmas dark flipped
        show tate sheepish festive dark
        cs "Sorry. Tate talks about you a lot, but I didn't know what you look like."
        show cs christmas dark flipped
        cs "It's nice to finally meet you!"
        cs "Shall we get inside?"
        show tate festive dark
        tate "Yeah!" (multiple = 2)
        mean "Yeah!" (multiple = 2)
    elif d20 == 7:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "CS notices a familiar blue car roll up onto the driveway."
        cs "Look at that! Looks like Billy is here first!"
        stop sound fadeout 0.5
        hide cs with moveoutleft
        scene cs_house_snow_night
        show billy_car dark at manual_pos(0.3, 0.8, 0.5):
            zoom 2.0
        $ collect("billy_car")
        show billy festive dark at mid_left
        with dissolve
        show cs dark christmas flipped at right with moveinright
        billy "Hi! It's Billy!"
        billy "Merry Christmas!"
        cs "Merry Christmas to you, too, Billy!"
        billy "Times like these make me wish I could still be in commercials."
        billy "It's been hard to sell products by word of mouth, especially since I died that one time."
        show cs disappointed christmas dark flipped
        cs "That sucks, man. I hope this party cheers you up."
        billy "Let's get inside. It's freezing out here!"
    elif d20 == 8:
        play sound2 sfx_chopper_loop fadein 2.0
        n "All of a sudden, CS hears helicopter blades above his house."
        show cs worried christmas flipped
        cs "Woah, what the hell?!"
        show cs worried christmas flipped at mid_left with move
        n "A Blackhawk helicopter is seen landing out in the middle of the street."
        show cs scared christmas flipped
        cs "Who the {i}hell{/i} would be arriving in a helicopter?!"
        stop sound2 fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("obama_chopper")
        show obama festive dark at mid_left
        with dissolve
        show cs worried dark christmas flipped at right with moveinright
        n "The President of the United States steps out."
        obama "Hello, CS! Nice to meet you."
        show cs scared dark christmas flipped
        cs "President Obama?! I didn't think you would {i}actually{/i} come!"
        cs "I sent that invite mostly as a joke!"
        obama "Well, I {i}have{/i} enjoyed your content, so when you sent an invitation to your Christmas party, I figured I could come visit for a while."
        obama "Besides, running the political circus is tiring work! I need a break."
        show cs christmas dark flipped
        cs "Fair enough, I guess!"
        show cs happy dark christmas flipped
        cs "Well, Mr. President, let's get inside and wait for the other guests."
        obama "Sure thing. It is very cold outside."
    elif d20 == 9:
        show cs scared christmas flipped
        play sound sfx_siren
        show blue_light at manual_pos(-50, 0):
            zoom 0.5
        show red_light at manual_pos(0, 0):
            zoom 0.5
        n "Sirens start blaring outside."
        show cs worried christmas flipped
        cs "Uh oh! Why are the cops here?"
        n "CS rushes outside."
        show cs worried christmas flipped at offscreenleft with MoveTransition(0.35)
        scene cs_house_snow_night
        show cop_car dark at manual_pos(0.3, 0.8, 0.5)
        $ collect("cop_car")
        show copguy festive dark flipped at mid_left
        with dissolve
        show cs worried christmas dark flipped at right with moveinright
        copguy "Heya, CS. Did I scare you?"
        show cs disappointed christmas dark flipped
        cs "Fuck yeah, you did! I didn't think you were gonna be on duty!"
        copguy "Well, {i}someone's{/i} gotta be security, right?" #TODO: i still hate this line - tate
        cs "I... guess?"
        cs "Whatever, let's get inside. I'm freezing!"
    elif d20 == 10:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "CS looks outside to see a bus pull up."
        cs "Hmm, I wonder who took the bus."
        stop sound fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("sheriff_bus")
        show sheriff festive dark flipped at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        sheriff "God damn it! Stupid damn wheels! Stuck in the snow {i}again!"
        show cs worried christmas dark flipped
        cs "Woah, hey! Who are you?"
        sheriff "Who am {i}I?{/i} I'm Copguy's {i}boss,{/i} that's who!"
        sheriff "I asked him to pick me up, but apparently he had to go {i}shopping,{/i} or some shit!"
        sheriff "So {i}I{/i} had to take the {i}bus!"
        show cs disappointed christmas dark flipped
        cs "Oh, wow, okay. Would you like some help?"
        sheriff "{i}Yes!{/i} I keep getting stuck in the snow! Take me inside!"
    elif d20 == 11:
        play sound sfx_beam
        n "A familiar sound like a laser beam is heard from outside."
        hide cs with moveoutleft
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("joj_ufo")
        show ed festive dark flipped at mid_mid_left
        show rich festive dark flipped at mid_left
        show wesley festive dark flipped at manual_pos(0.25, 1.0, 1.0)
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "Hey guys! How's it going?"
        ed "We've been doing well! Business has been {i}booming!"
        ed "Wesley has also made a speedy recovery! He wasn't too happy about needing a metal rod installed into his back, though."
        show cs worried christmas dark flipped
        cs "Yeah, I'm... uh..."
        show cs disappointed christmas dark flipped
        cs "I'm really sorry about that. I still feel bad about taking things too far."
        n "Wesley stares at the ground and mutters."
        wesley "Yeah."
        rich "Well, why don't we get inside? It's freezing out here!"
        show cs christmas dark flipped
        cs "Yeah, let's go!"
    elif d20 == 12:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "An old Dodge Charger pulls up on the driveway."
        cs "Nice car! I wonder if that's Carguy..."
        stop sound fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("pakoo_car")
        show k22 dark flipped at left
        show k17 dark flipped at mid_mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "Hey, it's..."
        show cs disappointed christmas dark flipped
        cs "Hey, it's...{fast} two Pakoos?"
        show k17 happy dark flipped
        k17 "CS!!!" with vpunch
        show k17 dark flipped
        k22 "Hey, CS. Merry Christmas!"
        cs "Hi, so, umm..."
        cs "Are you guys {i}both{/i} Pakoo?"
        k22 "It's... kind of complicated."
        k22 "Let's go inside, then we can explain."
    elif d20 == 13:
        play sound sfx_aria_tp
        n "A teleport-like sound is heard outside."
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
        cs "I was hoping {i}someone{/i} would arrive early."
        aria "Well, then, should we head inside? You're probably getting cold, I assume."
        show cs christmas disappointed dark flipped
        cs "Yeah, it's kinda freezing out."
    elif d20 == 14:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "Someone's car pulls into the driveway."
        cs "I wonder who that could be?"
        hide cs with moveoutleft
        stop sound fadeout 1.0
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("rosen_car")
        show michael festive dark at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "Oh, hey, it's Michael!"
        cs "You're still visiting the United States? I thought you were only here for the summer!"
        michael "I decided to spend a whole {i}year{/i} over here."
        michael "It's pretty cold out, innit?"
        cs "Yeah, let's get inside now."
    elif d20 == 15:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "CS sees Linus' car pulling up outside."
        cs "It looks like Linus got here first!"
        hide cs with moveoutleft
        stop sound fadeout 1.0
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("ltt_car")
        show linus festive dark at mid_mid_left
        show luke festive dark flipped at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        linus "Hey, CS! Long time no see!"
        show cs happy christmas dark flipped
        cs "You too! Also, hey, Luke! I didn't expect to see you here!"
        luke "Hey, man! I know we didn't talk much during your short employment, but it was fun having you around!"
        luke "Linus talks a lot about you."
        show cs christmas dark flipped
        cs "Oh, really?"
        linus "I just think you're a funny guy!"
        linus "What {i}wasn't{/i} funny was the cops showing up at LTT, but we can let bygones be bygones."
        show cs disappointed christmas dark flipped
        cs "Yeah, sorry about all that. It's a long story."
        show cs christmas dark flipped
        cs "Why don't we go inside? I'll explain the whole thing while we wait for more people to show up."
    elif d20 == 16:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "Another Honda Civic shows up in CS' driveway."
        cs "Oh, look at that! It's Blank!"
        stop sound fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        show blank_car dark at manual_pos(0.3, 0.8, 0.5):
            zoom 0.5
        $ collect("blank_car")
        show blank festive dark flipped at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        blank "Hey, CS! How've you been?"
        cs "I've been doing well! Was the drive safe up here?"
        blank "It was for me, but, for lots of people on the interstate, it sure wasn't!"
        blank "I got quite a bit of dashcam footage if you want to watch some with me."
        show cs happy christmas dark flipped
        cs "Sure thing! Let's get inside and watch while we wait for the others."
    elif d20 == 17:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "An unknown car with a rather lanky figure inside shows up in the driveway."
        cs "I wonder who that is."
        stop sound fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        show ges_car dark at manual_pos(0.3, 0.8, 0.5)
        $ collect("ges_car")
        show nova dark flipped at mid_left
        show ges dark flipped at left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        nova "Hey, CS! Thanks for inviting me to your Christmas party!"
        cs "Yeah! {w=1.0}It's been a while. How've you been?"
        nova "Oh, y'know, I've been moving a lot, had a friend move in with me..."
        cs "Well, if you wanna chat about it, let's get inside first. It's cold out here."
        nova "Before we go in, I'd like to introduce you to my friend Ges!"
        cs "He-ey Ges, how's it going?"
        ges "Goin' pretty alright! How about you, eh?"
        cs "Oh, you know, just been preparing for this party!"
        ges "Oh, man. You need any help from me, since I'm early, eh?"
        cs "Oh, I'd {i}love{/i} the help! I just need to get some last-minute things ready."
        ges "Fuckin' a rights, bud! Let's get inside, eh?"
    elif d20 == 18:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "CS sees a Jeep Cherokee pull up to his house."
        show cs disappointed christmas flipped
        cs "What the fuck? Who is {i}that?"
        stop sound fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        # TODO: put vehicle img here
        $ collect("mika_car")
        show elizabeth dark at center
        show anne dark at mid_left
        show grace dark at left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Hey, uhh..."
        eliza "Is this the right place?"
        anne "I think so!"
        cs "Are you..."
        eliza "I'm Elizabeth. Behind me is Anne and Grace."
        cs "You might have the wrong place. Sorry."
        eliza "Do you know a Mika? A Mikapara?"
        cs "Is that {i}you?"
        eliza "Close enough."
        cs "Well, would you all like to come inside?"
        eliza "Yeah."
    elif d20 == 19:
        play sound sfx_car_approach_stop volume 5.0 fadein 1.0
        show cs christmas flipped at mid_left with move
        n "An orange Mini Coooper shows up in front of CS' house."
        show cs worried christmas flipped
        cs "Holy crap! Is that who I think it is?"
        stop sound fadeout 1.0
        hide cs with moveoutleft
        scene cs_house_snow_night
        show db_car dark at manual_pos(0.3, 0.8, 0.5)
        $ collect("db_car")
        show db dark at mid_left
        with dissolve
        show cs christmas dark flipped at right with moveinright
        cs "DB! You're the first one here!"
        db "I am?!"
        cs "Yes! You managed to be the earliest this time!"
        db "Wow, I can't believe it!"
        cs "Yeah! Let's get inside, and then we can talk!"
    elif d20 == 20:
        show cs christmas flipped at mid_left with move
        n "A man in a white shirt approaches CS' house."
        show cs disappointed christmas flipped
        cs "Who the hell is {i}that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show avgn dark flipped at mid_left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Hey, are you--"
        avgn "I'm the fuckin' {i}Nerd!" with vpunch
        show cs scared christmas dark flipped
        cs "The Angry Video Game Nerd?! I didn't invite you!"
        show cs worried christmas dark flipped
        cs "At least, I don't {i}think{/i} I did..."
        avgn "It doesn't fucking {i}matter!" with vpunch
        avgn "Merry fucking Christmas!" with vpunch
        show cs disappointed christmas dark flipped
        cs "Yeah, uh, same to you..."
        cs "Do you, uh, wanna go inside?"
        avgn "Hell yeah!" with vpunch
        cs "Alright, then..."
    else:
        n "CS waits patiently."
        n "He keeps on waiting."
        show cs disappointed christmas flipped
        cs "Okay, what's going on? I figured {i}someone{/i} would show up early."
        show cs disappointed christmas flipped at mid_left with MoveTransition(1.0)
        n "CS looks out into the distance."
        cs "Wait, who is {i}that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show iris dark flipped at mid_left
        with dissolve
        show cs disappointed christmas dark flipped at right with moveinright
        cs "Who the heck are you?"
        iris "Oh, hello."
        iris "It seems you rolled a..."
        n "Iris looks confused."
        iris "Um... a [d20]."
        cs "Rolled... like on a die?"
        iris "You rolled a D20 earlier, no?"
        cs "I did, but... how did I roll on [d20] on a D20? That's not even a thing you {i}can{/i} roll!"
        show cs worried christmas dark flipped
        cs "And... how did you know I even did that?"
        iris "Ah, that's a lot to discuss. Shall we go inside? I'm sure you're rather cold."
        cs "I..."
        n "CS gives up trying to understand, for now."
        show cs christmas dark flipped
        cs "Sure."
    $ renpy.end_replay()
    jump ce_introductions

# Introductions
label ce_introductions:
    scene black with dissolve
    n "Around the party's scheduled start time, the guests start showing up in droves."
    # the line just needed a little more help. - tate
    $ achievement_manager.unlock("party_start")
    scene cs_foyer_festive
    show cs christmas at mid_left_left
    show anno festive at mid_left behind cs
    show aria festive at mid_mid_left behind anno
    show digi at center
    show tate festive flipped at mid_right
    with dissolve
    play music teeth_dust if_changed
    music teeth_dust
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        cs "Well, it looks like there is teeth dust in the stronghold, right?"
        show tate sheepish festive flipped
        tate "Wuh...?"
        show digi sad
        digi "Are... you okay, CS?"
    else:
        cs "Well, it looks like everyone is here, right?"
        if d20 != 19:
            dxcom db
            anno "DB isn't here yet, but, otherwise, yeah."
        else:
            anno "Looks like it, yeah."
        hide screen dxcom
        show tate sheepish festive flipped
        tate "There sure are... a {i}lot{/i} of people here..."
        show digi thinking flipped
        digi "Yeah, I wonder where Arc and Kitty went..."
    show cs worried christmas
    show k17 happy at mid_right
    show k22 at right behind k17
    show tate shock festive at center behind digi
    show digi shock flipped at mid_mid_left
    with { "master": moveinright }
    k17 "OMG!" with hpunch
    k17 "Hey, guys!"
    show k17 shock
    k17 "You guys all look so... {i}different!"
    show k22 confident
    k22 "Hi, I'm his--{w=0.5}{nw}"
    show cs disappointed christmas
    k17 "CS, look how much you've grown!"
    show k22
    if d20 == 12:
        cs "Okay, seriously, why are there {i}two{/i} Pakoos?"
    else:
        show cs scared christmas
        cs "Okay, wait, why are there {i}two{/i} Pakoos?"
        show cs worried christmas
    cs "... And, you also don't have green hair anymore, again?"
    show k22 disappointed
    k22 "Oh, boy. Alright."
    k22 "K-17, calm down for one second. I think everyone here needs an explanation."
    show k17
    show digi flipped
    show tate sheepish festive
    cs "Yes, please. I didn't want to say it, but it seems like every time I see you guys, you've changed your appearance!"
    if fun_value(FUN_VALUE_COMMON):
        aria "Sorria."
    else:
        aria "Sorry."
    show digi sad
    digi "Did I change too much?"
    show cs worried christmas
    cs "No, no, just-- let Pakoo #2 speak."
    if fun_value(FUN_VALUE_RARE):
        show k17 disappointed
        k17 "Hey, where's Fyreee at?"
        show k22 angry
        show digi shock flipped
        show cs scared christmas
        show tate shock festive
        k22 "Damn it, will you let me talk?!" with vpunch
        show k17
    else:
        show k22
        show digi flipped
        show cs disappointed christmas
        show tate sheepish festive
        k22 "I'm gonna assume that's me."
    show digi flipped
    show cs disappointed christmas
    show tate sheepish festive
    show k22 confident
    k22 "Alright, so, I'm K-22. I am the physical manifestation of Pakoo's memories from the year 2022."
    show k22
    k22 "This is K-17. I'm sure you can figure out what year {i}he{/i} is."
    show k17 happy
    k17 "Remember me? I'm the Sunny D guy!"
    show cs worried christmas
    n "CS groans."
    cs "Okay, so, what about the green-haired one?"
    show k17
    show k22 confident
    k22 "That's Addy, our boss."
    show cs disappointed christmas
    k22 "They run this archiving facility far away from here. I guess {i}they{/i} would be the closest version of Pakoo you'd know, but they couldn't join us here tonight."
    show k22 disappointed
    k22 "They're running their {i}own{/i} Christmas party, which I {i}wanted{/i} to be a part of, but this {i}creature{/i} right here just {i}had{/i} to come to this party..."
    k22 "So, I have to make sure he doesn't get too crazy."
    cs "Great."
    cs "Is that it?"
    show k22
    k22 "I mean, I {i}could{/i} go on, but we'd be here all night."
    show cs disappointed christmas at manual_pos(0.25, 1.0, 1.0)
    show anno festive at left
    show aria festive at mid_left
    show tate festive at mid_mid_left
    show digi flipped at mid_left
    show mean human at mid_offscreen_right
    $ persistent.seen.add("mean_human")
    show k17 flipped at mid_mid_right
    show k22 flipped at mid_right
    with { "master": moveinright }
    mean "Hey, what's going on here?"
    show mean human shocked
    show k17 flipped
    show k22 flipped
    mean "Wait, there's two Pakoos now?"
    show mean human annoyed
    show k22 confident flipped
    k22 "Okay, so--{w=0.5}{nw}"
    show k22 flipped
    show tate sheepish festive
    show k17
    show k22
    tate "I-{w=0.1}I'll explain it to him later."
    show tate festive flipped
    show digi
    show cs christmas
    cs "Alright, well, I'll let you guys get to know each other. I'm gonna go check on the others."
    show cs christmas zorder 5 with determination
    hide cs with moveoutright
    pause 2.0
    show k17 shock flipped
    show k22 flipped
    show digi flipped
    show tate festive
    k17 "So, who are {i}you?"
    if fun_value(FUN_VALUE_COMMON):
        k17 "Are you BigDick?"
        show mean human happy
        show digi shock flipped
        show tate sheepish blush festive
        mean "Not for {i}free,{/i} I'm not!" with vpunch
    else:
        k17 "Are you DigBick?"
        show mean human angry
        show digi sad flipped
        show tate sheepish festive
        mean "{i}What{/i} did you just call me?" with vpunch
    pause 0.5

    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at right behind cs_kitchen_fg
    show ed festive at mid_right behind cs_kitchen_fg
    show michael festive at mid_mid_right behind cs_kitchen_fg
    show billy festive at mid_mid_left behind michael
    with dissolve
    pause 0.5
    show cs christmas at left with moveinleft
    cs "Hey guys, how's it going?"
    obama "Hello, CS. We are all preparing our meals for dinner tonight."
    obama "I am going to make a carrot cake."
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
        show michael festive flipped
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
        show cs happy christmas
        cs "That all sounds great!"
        show cs christmas
        cs "What about you, Ed?"
        ed "Well, I think that, when it comes to cooking, even Christmas dinners need a good stable foundation."
        ed "I'm preparing a big ol' turkey for our feast."
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
        show michael festive flipped
        michael "I've been thinking of preparing some mashed potatoes."
        cs "That all sounds great!"
        cs "What about you, Ed?"
        ed "Well, I think that, when it comes to cooking, even Christmas dinners need a good stable foundation."
        ed "I'm preparing a big ol' turkey for our feast."
    show cs happy christmas
    cs "Damn! That sounds delicious!"
    if fun_value(FUN_VALUE_COMMON):
        show cs christmas
        cs "Hey, Ed, can you make me a sandwich?"
        ed "{i}Noe!" with vpunch
        show cs disappointed christmas
        cs "Well..."
        show cs christmas
    cs "I can't wait for dinner! I hope you all have a great time cooking!"
    show cs christmas
    cs "I'm gonna go see how the others are doing."
    show cs christmas flipped with determination
    hide cs with moveoutleft
    pause 0.5

    scene cs_living
    show linus festive at mid_left
    show luke festive flipped at mid_left_left
    show digi thinking at mid_mid_left
    show projector at manual_pos(0.2, 0.7, 0.5):
        zoom 0.75
    $ collect("projector")
    show blank festive flipped at mid_right
    show nova at mid_offscreen_right
    show blank_speaker at manual_pos(0.8, 1.0, 0.5):
        zoom 0.3
    $ collect("blank_speaker")
    with dissolve
    pause 0.5
    digi "So, this should go {i}here..."
    linus "No, you've got the wrong cable!"
    luke "You idiots are {nw}"
    luke "You idiots are {fast}{i}both{/i} wrong! That's not even the right {i}port!" with vpunch
    digi "Ohhhhh..." (multiple = 2)
    linus "Ohhhhh..." (multiple = 2)
    pause 1.0
    show cs christmas flipped at center behind linus
    with moveinright
    cs "Hey guys! Whatcha doin'?"
    show digi happy flipped
    show linus festive flipped
    digi "Oh, hey, CS!" # i forgor digi was in the other scene already asfkl;asf - tate
    show digi flipped
    digi "We're just trying to set up a projector so we can watch some Christmas movies!"
    digi "Mean {i}really{/i} wants to show everyone {i}The Polar Express.{/i}"
    linus "Just don't ask how this became a three-man job."
    show cs happy christmas flipped
    cs "Cool! I hope you all get it working!"
    show cs christmas
    cs "How about you two?"
    show blank festive
    blank "We are working on setting up the sound system."
    nova "The problem is that I don't really want Blank playing their shitty music during the party."
    show blank festive flipped
    blank "Why not? Not {i}all{/i} of it's crazy shit like {i}yours{/i} is."
    show cs scared christmas
    show digi shock flipped
    nova "Shut the hell up!" with vpunch
    show cs worried christmas
    cs "Woah, okay, calm down."
    show digi sad flipped
    show cs disappointed christmas
    cs "This {i}is{/i} a Christmas party, after all. Let's try to get along."
    show cs christmas flipped
    show digi flipped
    cs "I'm gonna go check on a few more people."
    hide cs with moveoutleft
    pause 0.5

    scene cs_hallway
    show arceus festive at mid_left
    show kitty festive at left
    with dissolve
    pause 1.0
    show cs christmas flipped at center with moveinright
    cs "Hey, how are you guys? I was looking all over and couldn't find you."
    show arceus festive worried flipped
    arceus "Hey, sorry, CS. We kinda got overwhelmed."
    kitty "We aren't the best with huge social gatherings."
    show cs disappointed christmas flipped
    cs "Ah, it's okay. I'm just happy you made it to the party."
    show arceus festive flipped
    arceus "We'll come back around when the main event starts."
    # TODO: redo these sprites' positioning once they're no longer placeholder sprites
    show elizabeth at right
    show anne at mid_right
    show grace at mid_mid_right
    with moveinright
    eliza "Hey, what's up."
    if d20 == 18:
        show cs disappointed christmas
        cs "Oh, you three..."
        cs "I still don't understand how you got the invite I sent to Mika."
        eliza "Well, we kind of {i}are{/i} Mika."
    else:
        show cs worried christmas
        grace "CS! You're that YTP guy!"
        show cs disappointed christmas
        cs "Wait, who are {i}you{/i} three?!"
        eliza "Well, do you know Mika at all?"
    show cs angry christmas
    cs "I swear to God, are you guys {i}also{/i} \"memories\", or some shit?"
    eliza "No, relax. We are just..."
    eliza "Let's just pretend that I got a name change."
    show cs disappointed christmas
    cs "What about the other two?"
    eliza "They, uh... work for me?"
    cs "You guys are so complicated."
    arceus "I mean, it wasn't too hard for {i}me{/i} to figure out, funnily enough."
    show cs disappointed christmas
    n "CS sighs."
    cs "Sorry, everyone. I'm just stressed out a bit."
    cs "I just really want this party to go well, but, at this point, I feel like I don't even know half the people here."
    cs "I mean, {i}you{/i} split into three people, {i}Pakoo{/i} split into {i}two...{/i}"
    cs "I hardly even know anything about Tate's friend beyond a few mentions over the phone..."
    eliza "I mean, if you want us to, we can step outside for a bit."
    show cs worried christmas
    cs "No, no, it's okay."
    cs "I hope you guys have fun. I'm gonna go back to the living room."
    hide cs with moveoutright

    if d20 == 20:
        pause 2.0
        show avgn at center with moveinbottom
        avgn "You guys ever heard of {i}Dr. Jekyll and Mr. Hyde{/i} for the NES?"
        eliza "Uhh, no?"
        show avgn flipped
        avgn "Good, because it's fucking {nw}"
        avgn "Good, because it's fucking {fast}{i}ass!" with vpunch

    pause 0.5
    scene black with dissolve
    pause 1.0

# Banter
label ce_banter:
    scene black
    stop music fadeout 3.0
    music end
    n "As the last few guests arrive, Copguy and the sheriff find themselves in a bit of a predicament."
    scene cs_living2_festive
    show db at mid_left
    show wesley festive at mid_right
    show rich festive at mid_right_right
    show sheriff festive flipped at left
    show copguy festive at center
    with dissolve
    play music dont_preheat_your_oven if_changed
    music dont_preheat_your_oven
    sheriff "Hey, Copguy!"
    if fun_value(FUN_VALUE_MUSIC):
        sheriff "Don't preheat your oven!"
        copguy "...Thanks?"
        sheriff "For real, though! I need to take a {nw}"
        sheriff "For real, though! I need to take a {fast}{i}shit!" with vpunch
    else:
        copguy "I know, this party is great, right?"
        sheriff "{i}No!{/i} I need to take a {nw}" with vpunch
        sheriff "{i}No!{/i} I need to take a {fast}{i}shit!" with vpunch
    copguy "Okay, do you want me to tell the whole house?"
    sheriff "Very funny, smartass! I need you to go with me." with vpunch
    sheriff "My legs don't work, remember?"
    copguy "Damn it... this sucks."
    copguy "Alright, let's go."
    show copguy festive at mid_offscreen_left behind sheriff with move
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
    copguy "Sorry, sir. We've gotta wait."
    sheriff "This is the police!" with hpunch
    play sound2 sfx_toilet_flush noloop
    sheriff "Open up!" with hpunch
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show cs_bathroom_open_fg
    show sheriff festive flipped at mid_left
    show copguy festive
    show tate shock festive at center with determination
    show copguy at right
    show tate shock festive at offscreenright
    with { "master" : MoveTransition(0.25) }
    with vpunch
    tate "{cshake}{size=+24}Awawawawa!!!" with hpunch
    pause 1.0
    "..."
    copguy "{i}Really?"
    sheriff "What? I {i}really{/i} have to go!"
    copguy "Whatever, just go. I'll wait here."
    dxcom bathroom
    sheriff "What do you mean? I need you to come with me!"
    sheriff "I can't get off and on the toilet by myself! This bathroom isn't handicap-accessible!"
    copguy "I think this is the worst crime I've dealt with..."
    show copguy festive at left behind sheriff with move
    show copguy festive flipped with determination
    pause 1.0
    show copguy festive flipped at mid_mid_left
    show sheriff festive flipped at center
    with move
    hide screen dxcom
    hide copguy
    hide sheriff
    with dissolve
    play sound sfx_house_door_close
    scene cs_bathroom
    copguy "Alright, make it quick! I don't wanna be in here all night!"
    pause 0.5

    scene cs_kitchen
    show cs_kitchen_fg
    show k17 flipped at left
    show obama festive at center behind cs_kitchen_fg
    show ed festive at mid_right behind cs_kitchen_fg
    show michael festive at mid_mid_right behind cs_kitchen_fg
    show billy festive at right behind cs_kitchen_fg
    with dissolve
    pause 0.5
    k17 "So, Obama, how long have you been President, again?"
    k17 "Aren't you on your, what, like, fourth term?"
    if fun_value(FUN_VALUE_COMMON):
        obama "Ever heard of squatter's rights?"
        show k17 shock flipped
        k17 "You... can {i}do{/i} that?"
        obama "I'm friggin' {i}Obama,{/i} bitch! I can do what I want!"
    else:
        obama "Well, you see, we managed to somehow exhaust the list of succession back in 2018, so the house voted me back in."
        k17 "Huh, I see. That's pretty crazy."
        # What the actual fuck happened in 2018 by the way, I'm so curious
        # How the fuck did 50 hyper-important government officials get either killed or incapacitated?!
        # We need to get into this some time. -- Digi
    pause 0.5

    scene cs_living
    show projector_no_signal:
        zoom 1.3
        perspective True
        matrixanchor (0, 0)
        matrixtransform RotateMatrix(0, 0, 0) * RotateMatrix(0, 35, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(32, 40, 0)
    show digi thinking at center
    show linus festive at mid_mid_left behind digi
    show luke festive flipped at mid_left_left behind linus
    show cs disappointed christmas flipped at right
    show projector at manual_pos(0.2, 0.7, 0.5):
        zoom 0.75
    with dissolve
    pause 0.5
    cs "Damn, is the projector still not working?"
    show digi angry flipped
    digi "No! It keeps giving us this {i}really{/i} weird error!"
    show linus festive flipped
    linus "Not even {i}I've{/i} seen this before!"
    show digi angry
    digi "Watch, I'll turn it on, and..."
    play sound sfx_projector_boot
    pause 1.0
    scene cs_living
    show projector_error:
        zoom 1.3
        perspective True
        matrixanchor (0, 0)
        matrixtransform RotateMatrix(0, 0, 0) * RotateMatrix(0, 35, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(32, 40, 0)
    show digi angry at center
    show linus festive flipped at mid_mid_left behind digi
    show luke festive flipped at mid_left_left behind linus
    show cs disappointed christmas flipped at right
    show projector at manual_pos(0.2, 0.7, 0.5):
        zoom 0.75
    play sound sfx_bluescreen
    with vpunch
    show cs worried christmas flipped at right
    pause 1.0
    rich "Hey, nice movie!"
    wesley "Looks like you'll have to set that up all over again."
    show digi disappointed flipped
    db "I got here early for {i}this?"
    if d20 == 20:
        avgn "You know what's {i}bullll{/i}shit?" with hpunch
        avgn "This {i}movie, {nw}" with hpunch
        avgn "This {i}movie,{/i}{fast} that's {i}what!" with hpunch
    ed "Hey, guys! What movie are we watching?"
    wesley "{i}Nothing{/i} until these bozos fix the projector!"
    luke "Okay, hold on. I've got an idea."
    show digi thinking flipped
    luke "Everyone step away from the projector."
    show digi thinking flipped at mid_right
    show linus festive flipped at mid_right
    show cs disappointed christmas flipped at mid_right_right behind digi
    with move
    show digi
    show linus festive
    with determination
    pause 0.5
    play sound sfx_tf2_wrench_hit
    with vpunch
    pause 0.5
    play sound sfx_tf2_wrench_hit
    with vpunch
    pause 0.5
    play sound sfx_tf2_wrench_hit
    with vpunch
    pause 0.5
    play sound sfx_projector_boot
    n "After a little bit of tech magic, the projector comes to life."
    scene cs_living
    show elf_0:
        zoom 1.3
        perspective True
        matrixanchor (0, 0)
        matrixtransform RotateMatrix(0, 0, 0) * RotateMatrix(0, 35, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(32, 40, 0)
    show digi shock at mid_right
    show linus festive at mid_right behind digi
    show luke festive at mid_left_left behind linus
    show cs scared christmas flipped at mid_right_right behind digi
    show projector at manual_pos(0.2, 0.7, 0.5):
        zoom 0.75
    play sound sfx_tada
    with vpunch
    luke "Ta-da!"

    show cs christmas flipped
    show digi
    show luke festive flipped
    rich "Finally! We can watch something!"
    wesley "Are you 100 percent satisfied, Richard?"
    show cs disappointed christmas flipped
    show digi angry flipped
    rich "Eh, only about 80 percent."
    pause 0.5

    scene cs_foyer_festive
    show aria festive at mid_mid_left
    show tate festive sheepish flipped at mid_right
    show mean human at mid_offscreen_right
    show k22 flipped at left behind k17
    show k17 flipped at center
    with dissolve
    pause 0.5
    k17 "So, there's a new World Trade Center now?"
    show k22 disappointed flipped
    k22 "What do you mean? They finished that in, like, {i}2014!"
    k17 "Oh. Sorry, I forgot about that."
    show k22 flipped
    k17 "Okay, so, if big guy over there is DigBick..."
    show mean human angry
    mean "I'm {i}not{/i} DigBick!" with vpunch
    k17 "Are you DigBick's... girlfriend?"
    show tate furious blush festive flipped
    tate "{i}What?!" with vpunch
    mean "First of all, I am {i}not{/i} fuckin' DigBick."
    show k17 disappointed flipped
    mean "I'm Mean, and this is Tate. We are friends."
    k17 "Yeah, you {i}sound{/i} mean."
    tate "And, I'm not a girl--!{w=0.25}{nw}" with vpunch
    show tate furious festive flipped
    show mean human annoyed
    show tate srs festive flipped
    show k17 at mid_mid_right with move
    k17 "Anyway, what about {i}you?"
    aria "Me? I'm Aria."
    show k17 shock
    k17 "Who?"
    show k22 confident flipped
    k22 "Uhh, well..."
    aria "I'm an old friend. You know, the other one, who {i}wasn't{/i} Arceus?"
    aria "I got different."
    show k22 disappointed flipped
    k17 "Whaa..."
    k22 "Please excuse us for a moment."
    show k22 disappointed flipped at Move((0.0, 0.14), (1.25, 0.14), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.4
    show k17 shock at Move((0.475, 0.15), (1.0, 0.15), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 2.5

    scene cs_bathroom with dissolve
    copguy "{i}Please{/i} tell me that's it. I can't bear this anymore."
    sheriff "Yep, I'm done!"
    sheriff "Now, are you gonna help me wipe, or, what?"
    play sound sfx_walkie_on
    n "All of a sudden, Copguy's walkie goes off."
    walkie "Officer Copguy, we have a break-in at a house near your current location."
    walkie "Can you report on that?"
    copguy "Gladly! I'll be right there!"
    play sound sfx_walkie_off
    copguy "Sorry, boss! As much as I would {i}love{/i} to keep helping you out here, duty calls!"
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show sheriff festive at manual_pos(0.45, 0.5):
        zoom 0.5
    show cs_bathroom_open_fg
    show copguy festive flipped
    sheriff "Wait! You can't just {i}leave{/i} me here!"
    show copguy festive flipped at mid_right with move
    show copguy festive
    copguy "I'll just be a moment! Don't move."
    play sound sfx_house_door_close
    scene cs_bathroom
    show copguy festive at mid_right
    pause 0.5
    show copguy festive flipped with determination
    show copguy festive flipped at offscreenright with { "master" : MoveTransition(0.25) }
    sheriff "God {i}damn{/i} it! {nw}" with vpunch
    sheriff "God {i}damn{/i} it! {fast}{cshake}Get {i}back{/i} here!" with vpunch
    pause 3.0
    sheriff "\"Don't move...\""
    sheriff "Thanks, Copguy. You're a {i}real{/i} fuckin' {i}comedian."
    pause 0.5

    scene cs_door_outside
    show k17 disappointed flipped at mid_left
    show k22 disappointed at mid_right
    show snow1white
    show snow2white
    with dissolve
    pause 0.5
    k17 "This is {i}so{/i} unfair!"
    k17 "CS said it's annoying that we've changed or whatever, but just look at everyone {i}else!"
    k17 "All of my friends have changed so much I don't even {i}recognize{/i} them anymore!"
    k22 "Yeah, well, when you are constrained to just one year of your life, that can happen."
    k17 "It's just... how do I, like, {i}deal{/i} with all of this?"
    k17 "I can't just change who {i}I{/i} am, too!"
    show k22 confident
    k22 "Look, you don't need to."
    k22 "I probably should've told you about how people change, and whatnot."
    k22 "Honestly, {i}Addy{/i} should've been the one to tell you, but they were probably too busy worrying about their own party."
    show k22 happy
    k22 "Speaking of which, do you want to go back home? Where you know everyone? Celebrate Christmas with Addy?"
    k17 "Hmm..."
    pause 1.0
    show k17 happy flipped
    show k22 disappointed
    k17 "No! I wanna stay here 'til the end!"
    show k17 flipped
    k17 "I'll just keep being myself, but I'll try to keep more of an open mind. Thank you, K-22!"
    show k17 flipped at center with ease
    play sound sfx_house_door_open
    hide k17 with dissolve
    pause 0.5
    play sound sfx_house_door_close
    pause 2.0
    k22 "Damn it. It was worth a try."
    show k22 at mid_left with { "master" : MoveTransition(1.0) }
    k22 "I wonder how Addy is doing, anyway."
    show k22 flipped with determination
    play sound sfx_ring_once
    show k22 phone at mid_left with move
    n "K-22 hits up Addy."
    pause 0.5
    $ renpy.music.set_pause(True, "music")
    play music2 frollo_rave if_changed
    music frollo_rave
    show archival_5 at mid_offscreen_right
    show pakoo disappointed at mid_right
    with moveinright
    addy "HELLO?!" with vpunch
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        k22 "Hey, uhh, do you need some H2O?"
    else:
        k22 "Hey, uhh, how is it going over there?"
    addy "{i}WHAT?! {nw}" with vpunch
    addy "{i}WHAT?!{/i} {fast}I CAN'T HEAR YOU! {nw}" with vpunch
    addy "{i}WHAT?!{/i} I CAN'T HEAR YOU! {fast}THE MUSIC IS {i}REALLY{/i} LOUD!" with vpunch
    show k22 phone angry
    k22 "I WAS ASKING IF--{w=1.0}{nw}"
    addy "YEAH, I'LL CALL YOU LATER! HAVE FUN AT CS' PARTY!"
    play sound sfx_end_call
    hide archival_5
    hide pakoo
    with moveoutright
    stop music2
    $ renpy.music.set_pause(False, "music")
    pause 1.0
    show k22 angry flipped
    k22 "Mother{i}fucker!" with vpunch
    show snow3
    show snow4
    n "All of a sudden, the wind starts to pick up and the gentle snow begins coming down harder."
    show k22 disappointed flipped
    k22 "Brr..."
    k22 "As long as I'm stuck here, I should probably just get back inside and at least {i}try{/i} to enjoy the party."
    show k22 disappointed flipped at center with move
    play sound sfx_house_door_open
    hide k22 with dissolve
    play sound sfx_house_door_close
    pause 0.5

    scene cs_bathroom with dissolve
    pause 0.5
    show k17 at mid_right with moveinright
    sheriff "Hey!" with vpunch
    sheriff "Hey! {fast}Is someone there?"
    k17 "Huh?"
    sheriff "Hey, you! Can you help me out of here?"
    show k17 shock
    k17 "Uhh... uhh..."
    k17 "I'll go get someone!"
    hide k17 with easeoutleft
    pause 0.5

    # audio ducking
    $ renpy.music.set_volume(0.25)

    # they're supposed to be sitting on the couch now ehehe
    scene cs_living2_festive
    show elf_1
    show rich festive at mid_mid_right:
        zoom 0.75
    show wesley festive at right:
        zoom 0.75
    show db at mid_left:
        zoom 0.75
    show cs christmas at left:
        zoom 0.75
    with dissolve

    pause 1.0
    rich "Oh, man, I love this part."
    show k17 shock at mid_right with moveinright
    k17 "Hey, guys, uh-- how do I put this...?"
    k17 "The sheriff is stuck in the bathroom?"
    show cs disappointed christmas
    show k17 disappointed
    cs "Damn it, one second--"
    obama "CS! Are you there?"
    show cs christmas
    cs "Oh! Let me do this first. The {i}president{/i} is calling!"
    show cs christmas at left with move:
        linear 0.5 zoom 1.0
    pause 0.5
    hide cs with moveoutright

# Cooking
label ce_cooking:
    play music dont_preheat_your_oven if_changed
    scene cs_kitchen
    show cs_kitchen_fg

    # un-duck the audio
    $ renpy.music.set_volume(1.0)

    show billy festive at mid_mid_left behind cs_kitchen_fg
    show michael festive flipped at left behind cs_kitchen_fg
    show obama festive at mid_right behind cs_kitchen_fg
    show cutting_board at manual_pos(0.6, 0.75)
    $ collect("cutting_board")
    show knife at manual_pos(0.7, 0.5):
        zoom 0.15
        xzoom -1
        rotate -45
    $ collect("knife")
    show carrot_chopped at manual_pos(0.8, 0.7):
        zoom 0.4
    show carrot_whole at manual_pos(0.625, 0.65):
        zoom 0.8
        rotate -115
    $ collect("carrot")
    with dissolve
    pause 0.5

    show cs christmas at center behind cs_kitchen_fg with moveinleft
    cs "Hey, Mr. President! What can I help you with?"
    stop music fadeout 3.0
    music end

    obama "Please, you can just call me Obama."
    obama "Second of all, I accidently cut myself while chopping these carrots."
    obama "What a fool I am."  # One of my favorite lines -- Digi
    show cs disappointed christmas
    cs "Oh, my God! Are you okay?"
    obama "Yes, I'm fine. However, I need someone to take over carrot-chopping duties."
    obama "Will you do this for me?"
    show cs christmas
    cs "I guess I can, yeah."
    obama "Great, thank you. I just need a few more carrots cut up."
    obama "Give me a moment. I need to find a Band-Aid."
    hide obama with moveoutleft
    show cs christmas at manual_pos(1.0, 1.0, 1.0) with move
    show cs christmas flipped
    cs "Alright, just a few carrots."
    cs "Let's do this."
    jump ce_carrot

label ce_carrot:
    minigame "play_carrotgame" "ce_win_carrot" "ce_carrot"

label ce_win_carrot:
    $ persistent.carrot_game_unlocked = True
    scene cs_kitchen
    show cs_kitchen_fg
    show billy festive at mid_mid_left behind cs_kitchen_fg
    show michael festive flipped at left behind cs_kitchen_fg
    show obama festive flipped at center behind cs_kitchen_fg
    show cs christmas flipped at manual_pos(1.0, 1.0, 1.0) behind cs_kitchen_fg
    show cutting_board at manual_pos(0.6, 0.75)
    show knife at manual_pos(0.7, 0.5):
        zoom 0.15
        xzoom -1
        rotate -45
    show carrot_chopped at manual_pos(0.8, 0.7):
        zoom 0.4
    show carrot_whole at manual_pos(0.625, 0.65):
        zoom 0.8
        rotate -115
    with dissolve
    show smoke
    obama "Well, would you look at that?"
    obama "That was some mighty-fine chopping, CS!"
    show cs happy christmas flipped
    cs "Woohoo!"
    cs "Thank you! Maybe I should cook more."
    show cs christmas flipped
    cs "Speaking of cooking, I can smell something... {nw}"
    show cs christmas disappointed
    cs "Speaking of cooking, I can smell something... {fast}burning..."
    obama "Is it perhaps the smoke billowing out from the oven?"
    show cs scared christmas flipped
    play sound2 sfx_smoke_alarm
    with vpunch
    n "All of a sudden, the smoke detectors start beeping!"
    digi "{cshake}AHHH! Turn it {i}off!" with hpunch
    nova "Damn it, Blank! I {i}said{/i} we weren't playing your music!" with hpunch
    aria "Honestly, this is kind of a bop. Keep it going."
    play sound sfx_seymour
    pause 1.0
    "Smoke Detector" "This is {i}disgusting!" with vpunch
    if d20 == 20:
        avgn "{cshake}AHHH! My ears!" with hpunch
        avgn "What {i}is{/i} this? The soundtrack from a LJN game?!"

    show cs scared christmas flipped at mid_offscreen_right
    show obama festive at right
    show ed festive flipped at center behind cs_kitchen_fg
    with easeinleft
    # TODO: fix the particle system maybe idk - tate
    ed "{cshake}NOOOO!" with hpunch
    ed "{cshake}My turkey!" with vpunch
    play sound sfx_oven_open
    show bigsmoke with dissolve
    n "Ed opens up the oven, only to have even more smoke pour out."
    n "Everyone hacks and coughs as smoke fills the room."
    hide bigsmoke with dissolve
    stop sound2
    show burnt_turkey at manual_pos(0.5, 0.4) with dissolve:
        xanchor 0.5
        zoom 0.7
    $ collect("burnt_turkey")
    play sound sfx_oven_close
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        n "When the smoke finally clears, Ed pulls out a snowdin turkey."
    else:
        n "When the smoke finally clears, Ed pulls out a blackened turkey."
    hide smoke with dissolve
    show cs disappointed christmas flipped
    play music snowdin_town
    music snowdin_town
    ed "Damn it! My roast is {i}ruined!"
    billy "Not to fear, Ed! I made my famous restaurant mini-burgers!"
    show ed festive
    ed "You mean, steamed hams?"
    billy "Who the actual {i}fuck{/i} calls burgers \"steamed hams?\""
    ed "It's a... regional dialect?"
    billy "..."
    billy "Steamed hams... for God's sake..."
    billy "You Texans are {i}crazy."
    michael "I also have my mashed potatoes!"
    cs "Well, at least we'll still have {i}some{/i} kind of Christmas dinner."
    hide ed
    hide burnt_turkey
    show obama festive at center
    show cs christmas flipped at right
    with moveoutleft
    n "Ed sheepishly heads outside to throw away the ruined turkey." # i changed this bc it's a huge turkey and it would fill the whole trash - tate
    cs "I guess, as soon as the President's cake is done, we can all sit down to eat."
    cs "I'm gonna go check up on the others in the meantime."
    hide cs with moveoutleft
    pause 0.5

    scene cs_hallway
    show arceus festive at mid_right
    show kitty at mid_left
    with dissolve
    pause 0.5
    kitty "Arcie, you're a fucking walnut."
    show arceus festive worried
    arceus "{i}Huh?!{/i} Where did {i}that{/i} come from?"
    kitty "Dunno, just felt like calling you a walnut."
    show arceus festive happy
    arceus "Y'know, that's fair..."
    show arceus festive
    n "..."
    n "..."
    n "... Why hasn't the scene transitioned yet?"
    show arceus festive angry
    arceus "Because I'm not done yet, dipshit."
    n "... k."
    show arceus festive
    arceus "Isn't it weird how the first night of Hanukkah fell on Christmas day this year?"
    kitty "Yeah, that's pretty weird, innit?"
    arceus "Even weirder, when you think about it, that next year will have {i}two{/i} Hanukkahs."
    kitty "... How so?"
    arceus "Well, you figure, eight nights of Hanukkah."
    kitty "Uh huh..."
    arceus "And, today's the 25th of December."
    kitty "I see."
    arceus "So, the last night of Hanukkah would be the 2nd of January."
    kitty "..."
    kitty "..."
    kitty "Shit, you right."
    pause 0.5

    scene cs_bathroom
    show grace at mid_left
    with dissolve
    pause 0.5
    sheriff "... and, that's how I ended up this way."
    sheriff "I could've gone to college, studied the paranormal..."
    sheriff "... started up a shower curtain business, run a newspaper..."
    sheriff "... but, no, I {i}had{/i} to become a {i}cop."
    grace "Hey, are you almost done in there?"
    sheriff "Just leave me alone..."
    grace "But I really need to go!"
    sheriff "Find another bathroom."
    grace "But this is the only one in the house!"
    sheriff "In this mansion? There is only {nw}" with vpunch
    sheriff "In this mansion? There is only {fast}{i}one{/i} {fast}damn bathroom?!" with vpunch
    show copguy festive at mid_right with moveinright
    copguy "Hey, sorry, excuse me."
    show copguy festive at center with move
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show sheriff festive at manual_pos(0.45, 0.5):
        zoom 0.5
    show cs_bathroom_open_fg
    show grace at mid_left
    show copguy festive flipped at center
    pause 0.5
    show copguy festive flipped behind cs_bathroom_open_fg:
        linear 0.5 zoom 0.7 pos (0.5, 0.9)
    pause 0.75
    play sound sfx_house_door_close
    scene cs_bathroom
    show grace at mid_left
    copguy "Hey, boss! You won't {i}believe{/i} what I just experienced."
    copguy "This kid caught two burglars trying to rob his house with homemade traps!"
    copguy "It was so impressive, {i}I{/i} probably would've fallen for some of them!"
    sheriff "That's great, but can you get me off this toilet now?"
    sheriff "I've been sitting here for so long that I started writing my will!"
    copguy "Alright, let's get you out of here, old man."
    play sound2 sfx_toilet_flush noloop
    pause 1.0
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show copguy festive behind sheriff at manual_pos(0.4, 0.35):
        zoom 0.5
    show sheriff festive at manual_pos(0.4, 0.5):
        zoom 0.5
    show cs_bathroom_open_fg
    show grace at mid_left
    with determination
    pause 1.0
    show copguy festive behind sheriff at manual_pos(0.4, 0.35):
        linear 0.5 zoom 1.0 pos (0.4, 0.2)
    show sheriff festive at manual_pos(0.4, 0.5):
        linear 0.5 zoom 1.0
    pause 0.5
    scene cs_bathroom_open
    show cs_bathroom_open_fg
    show grace at mid_left
    show copguy festive behind sheriff at manual_pos(0.4, 0.2)
    show sheriff festive at manual_pos(0.4, 0.5)
    pause 0.25
    show copguy festive at mid_right with move
    pause 0.25
    hide copguy
    hide sheriff
    with moveoutleft
    grace "Finally!"
    show grace flipped
    grace "Guys, the sheriff is out!"
    show grace at center with move
    hide grace with dissolve
    scene cs_bathroom
    play sound sfx_house_door_close
    show anne at mid_mid_left with moveinleft
    show rich festive flipped at mid_left behind anne with moveinleft
    show tate sheepish festive at mid_left_left with moveinleft
    show luke festive flipped at mid_offscreen_left with moveinleft
    n "A line forms in front of the bathroom."
    pause 0.5

    # OK, is this scene too meta? I like it a lot but I'm worried I'm pushing the boundaries a bit here.
    scene cs_foyer_festive
    show aria festive at left
    show digi at mid_mid_right
    show arceus festive at right
    with dissolve
    pause 0.5
    arceus "Yeah, so, to get the code done, I got drunk off a bottle of wine, and Digi and I chewed through it in a single night."
    aria "Damn. That's the best way to do it."
    show digi thinking
    digi "I mean, {i}I{/i} was sober the whole time. I just had to put up with {i}this{/i} fluffy bastard."
    aria "Of course {i}you{/i} were sober. I think one sip of wine would knock you flat."
    show digi goober
    digi "Hey, I'm not {i}that{/i} small."
    aria "Usually."
    show digi happy
    show arceus happy festive
    arceus "And, you {i}love{/i} putting up with this fluffy bastard."
    show arceus festive
    digi "While that's true, I think half of that night was spent coding, and the other half was spent confusing the names of four different bald dudes."
    show arceus happy festive
    arceus "To be fair, that was hilarious."
    digi "You got me there."
    show cs christmas at mid_mid_left with moveinleft
    n "CS walks in on the conversation."
    show arceus festive
    cs "Hey guys! What are you all talking about?"
    digi "Oh, we were just discussing what developing the first game was li--{w=0.5}{nw}"
    show digi shock with hpunch
    n "Aria shoots a look at Digi, as much as she can do that in her current form." # TODO: this line needs help - tate
    digi "Er, uh, just talking about a coding project we all worked on."
    cs "Oh, okay. Probably a bunch of stuff I wouldn't understand, then."
    show digi
    aria "Certainly not."
    show cs happy christmas
    cs "You guys do good work, though. I can't wait to see what DPN Games will come up with next!"
    show arceus festive worried
    arceus "Yeah, me too."
    hide cs with moveoutright
    n "CS walks off."
    pause 1.0
    show digi sad
    aria "You're going to have to get better at the whole \"not breaking the illusion\" thing, Digi."
    digi "What? He wouldn't have thought anything of it if you hadn't stopped me mid-sentence."
    show arceus festive
    arceus "We just need to be a little more careful than we have been."
    dxcom meta
    digi "Fair enough. Wouldn't want this place falling apart."
    pause 0.5

    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive flipped at mid_left behind cs_kitchen_fg
    show billy festive at mid_right behind cs_kitchen_fg
    hide screen dxcom
    with dissolve
    pause 0.5
    billy "So, then I said, \"That's a resturaunt mini burger {w=1.0}{i}no one{/i} loves!\""
    n "Obama lets out a hearty laugh."
    obama "Billy, you crack me up. You're one of America's greatest."
    billy "That means a lot coming from you, Mr. President!"
    obama "Please, call me Barack."
    billy "The man in the suit always lurking behind you said if I do that, he'll kill me!"
    obama "Oh, he's just teasing. Isn't that right, Luther?"
    n "Luther says nothing and nods once."
    billy "Well, then, thanks for the compliment, Barack!"
    obama "You've gotta tell me the one about the cabinet full of cleaners again."
    show cs christmas at center with moveinleft
    n "CS walks in to greet the unlikely friends."
    cs "Obama, Billy! You two getting along?"
    obama "Oh, CS, this guy's a {i}hoot!"
    billy "Barack here has some great stories, as well!"
    cs "Glad to hear it! Always love to see two people from different walks of life enjoying each other's company."
    obama "That's what Christmas is all about, isn't it?"
    billy "{i}That's{/i} the power{w=0.25} of the holiday season!"
    show cs happy christmas
    cs "Well, I gotta go make sure the others are getting along, too. You two have fun!"
    hide cs with moveoutright
    pause 0.5
    billy "Right, so I said: \"You shittin' me?\""
    pause 0.5

label ce_mike:
    stop music fadeout 3.0
    music end
    scene cs_living2_festive
    show cs christmas at left
    show rich festive at center
    show ed festive at mid_right
    show grace at right
    with dissolve
    pause 0.5
    cs "Gee, that pizza I ordered sure is taking its time!"
    play sound sfx_doorbell
    n "Just at that moment, the doorbell rings."
    show cs happy christmas
    cs "Well, tickle my ballsack! What great timing!"
    grace "CS... you {i}can't{/i} just say stuff like that."
    n "CS heads to the front door."
    hide cs with moveoutright
    pause 0.5

    scene cs_foyer_festive with dissolve
    pause 0.5
    show cs christmas at left with moveinleft
    cs "Hey guys, the pizza is here!"
    show cs christmas at right with move
    play sound sfx_house_door_open
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        n "He opens the door to grab the rice and wine."
    else:
        n "He opens the door to greet the delivery person."
    show mike at right
    show cs christmas at mid_mid_left
    with moveinright
    play music rice_and_wine volume 0.5
    music rice_and_wine
    dxcom pizza1
    mike "I'm Chinese."
    show cs happy christmas
    cs "Oh, my God! It's Mike!"
    show cs happy christmas flipped
    cs "Everyone, quick, come look at Mike!"
    show cs happy christmas
    show mike at mid_right_right
    show k17 flipped at mid_mid_right behind grace
    show grace at mid_right
    show obama festive flipped at center behind cs
    show billy festive flipped behind cs at left
    show tate festive at mid_offscreen_left
    with moveinleft
    show k17 happy flipped
    k17 "Hey, it's Mike! How's it going? Long time no see!"
    grace "Oh, my God! I love you, Mike!"
    tate "What's up, Mike?"
    obama "Mike, remember when I pardoned you?"
    billy "This guy can sell pizza even better than {i}I{/i} can!"
    show tate festive flipped
    show billy festive
    with determination
    hide tate
    hide billy
    with moveoutleft
    show cs happy christmas at left
    show obama festive flipped at mid_left behind cs
    show k17 flipped at mid_mid_left
    show grace at center
    with move
    arceus "What's going on in here?"
    show arceus festive angry flipped at mid_mid_right with moveinleft
    show cs happy christmas
    cs "It's Mike, Arceus! Mike the Pizzapotamus!"
    show cs christmas
    show arceus festive angry
    arceus "Who?"
    show cs disappointed christmas
    grace "How do you not know who Mike the Pizzapotamus is?!" with vpunch
    obama "I mentioned him in my re-election speech!"
    cs "The children love him! He's the best in the world!"
    show arceus festive worried
    arceus "I guess he's just not... ringing a bell?"  # Sorry Tate, I prefer it read like this -- Digi
    show k17 disappointed flipped
    k17 "He works at the {i}bus stop,{/i} dude!"
    arceus "You mean the bus {i}station?"
    grace "No! The bus stop!"
    arceus "Oh, so he drives the bus?"
    show cs angry christmas
    "Everyone" "{cshake}{size=+24}No! The bus stop!" with vpunch  # TODO: Make this a character, so it has a beep
    mike "You really don't know me, do you?"
    show arceus festive worried flipped
    arceus "Huh?"
    show pipe_gun flipped at manual_pos(1.2, 0.7):
        xanchor 0.5
        yanchor 0.5
        rotate -90
    show mike at mid_offscreen_right with MoveTransition(0.25)
    play sound sfx_tf2_pickup_metallic
    show mike at mid_right_right
    show pipe_gun flipped at manual_pos(0.85, 0.6):
        xanchor 0.5
        yanchor 0.5
        linear 0.25 rotate 0
    with MoveTransition(0.25)

    $ collect("pipe_gun")
    n "Pizzapotamus shoots Arceus in the head!"
    play sound sfx_hks1
    with hpunch
    show arceus festive worried flipped at manual_pos(0.4, 0.55):
        linear 0.5 rotate -45
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    pause 0.5
    n "As Arceus is dying on the floor, he faintly hears people talking."
    grace "I expected more from you."
    obama "Should've listened to my campaign speeches, bitch."
    mike "Alright, who wants to try pizza from my Thermos?"
    hide screen dxcom
    show cs happy christmas
    cs "Oh, {i}yes!{/i} Me first! Woohoo!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    pause 2.0
    play sound sfx_csnore loop
    cs "Zzz..."
    rich "Hey, CS, are you sleeping?"

    scene cs_living2_festive
    show ed festive at mid_mid_right:
        zoom 0.75
    show rich festive at mid_right:
        zoom 0.75
    show wesley festive at right:
        zoom 0.75
    show db at mid_left:
        zoom 0.75
    show cs concentrate christmas at left:
        zoom 0.75
    with dissolve
    rich "CS!"
    stop sound
    show cs scared christmas
    cs "Huh?!" with vpunch
    show cs disappointed christmas
    cs "Oh, sorry. I must have dozed off."
    cs "I had this {i}insane{/i} dream, and there was this pizza guy..."
    wesley "Speaking of pizza, should we have dinner now? I'm starving."
    cs "Yeah, that's a great idea. Let me go see if everything is ready."
    $ achievement_manager.unlock("cheesy_dream")
    scene black with dissolve
    pause 0.5

# Dinner/More Banter
label ce_dinner:
    play music christmas_spirit
    music christmas_spirit
    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs christmas at center
    show tate festive flipped at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    with dissolve
    if fun_value(FUN_VALUE_MUSIC):
        cs "Well, I'd love to spread some Christmas spirit by saying--"
    else:
        cs "Well, I'd love to start off this wonderful meal by saying--"
    play sound sfx_static
    show cs scared christmas
    show tate shock festive flipped
    with hpunch
    $ renpy.music.set_pause(True, "music")
    pause 0.25
    play music2 crashing_down if_changed
    music crashing_down
    blank "Hey, stop it! We are {i}not{/i} playing your music!" with hpunch
    play sound sfx_static
    stop music2
    pause 0.25
    play music2 summer_fun if_changed
    music summer_fun
    if fun_value(FUN_VALUE_COMMON):  # I made this joke a fun value, it just seems too mean to be the main route
        nova "Blank, Blank..."
        nova "This song is so..."
        show cs christmas disappointed
        show tate festive sheepish flipped
        nova "FUCKING {i}ASS!" with hpunch
        nova "STOP MAKING MUSIC!" with hpunch
        nova "{i}STOP{/i} MAKING MUSIC!" with hpunch
        show cs christmas angry flipped
        nova "Turn that shit {i}off!" with hpunch
    else:
        nova "Well, I don't want to hear catgirl moans at the dinner table!"
        blank "They're mixed into the instrumentation, you can barely--"
    cs "Hey!" with hpunch
    cs "Hey! {fast}Can you two stop fighting, get over here, and eat with us?!"
    stop music2
    $ renpy.music.set_pause(False, "music")
    music christmas_spirit
    hide screen music
    pause 2.0

    show left_room at mid_left
    show left_chair_back at mid_left
    show left_table at mid_left
    show anno festive at mid_offscreen_left
    show cs christmas at mid_left
    show tate festive at center
    show db at manual_pos(0.85, 0.6, 0.5)
    show k22 at manual_pos(-0.25, 0.575, 0.5)
    with move
    db "So, CS, how have your streams been going recently?"
    cs "Well, it's mainly been dashcam reaction streams on Sundays as usual."
    show cs disappointed christmas
    cs "It's been hard to do as much crazy stuff since Mixer died."
    db "Ah, yeah, I get that."
    tate "But, hey, we still have fun!"
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
    show arceus festive at mid_offscreen_left
    show billy festive flipped at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    with dissolve
    obama "So, Billy, any good new pitches on the table for you?"
    billy "Well, I got in contact with Phil Swift recently. You may have heard of him from his Flex Tape commercials!"
    show michael festive flipped
    michael "Actually, Phil is a wonderful friend of mine! He has stayed over at my place plenty of times."
    michael "If he offers you a slice of cake, however, perhaps consider giving it a pass."

    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs christmas at center
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Phil? Oh, yeah! I was going to invite him to this party, but he's been so busy pitching Flex products."
    cs "I think he's actually in Europe right now."

    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus festive at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    billy "Well, if this deal goes through, you might see {i}both{/i} of us in a commercial real soon!"
    obama "How much does it cost to get you in a commercial, anyway?"
    show billy festive flipped
    billy "If I told you, I'd have to kill you!"
    n "Obama and Billy chuckle, but Luther does not."
    pause 0.5
    show arceus festive flipped
    arceus "Hey, Ed, how's the foundation repair business lately?"
    ed "It's been pretty good. We got all these new contracts after our run-in with CS."

    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs christmas at center
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
    wesley "My {i}back{/i} is sorry about it, too."
    rich "Oh, {i}can{/i} it, ya ding-dong. You {i}got{/i} your surgery, didn't 'cha?"
    show wesley festive flipped
    wesley "Having a metal pole in your back isn't ideal, numbnuts."
    mean "I mean, metal {i}is{/i} stronger than bones, so it's kinda like an upgrade!"
    show wesley festive
    wesley "Tell that to the TSA."
    arceus "I don't tell {i}anything{/i} to the TSA."

    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs disappointed christmas at center
    show tate sheepish festive flipped at mid_right
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
    ed "You've {i}more{/i} than made it up to us, CS."
    rich "Yeah, you helped propel our business to new heights!"
    rich "Or, I guess, new foundations?"
    wesley "Mmm."

    scene night_bg
    show right_room at right
    show right_chair_back at right
    show obama festive at manual_pos(-0.5, 0.5, 0.5)
    show michael festive at manual_pos(-0.25, 0.6, 0.5)
    show ed festive at manual_pos(0, 0.55, 0.5)
    show wesley festive at manual_pos(0.25, 0.575, 0.5)
    show rich festive at manual_pos(0.5, 0.555, 0.5)
    show linus festive at manual_pos(0.80, 0.6, 0.5)
    show luke festive at manual_pos(0.95, 0.6, 0.5)
    show right_table at right
    with move
    linus "So, CS, when are we getting you back for another video?"

    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs worried christmas at center
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Oh, jeez, life has just been so busy."

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
    show anno festive at mid_left
    show cs surprised christmas at center
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Well, if I can make it back to Canada at some point..."

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
    show anno festive at mid_left
    show cs christmas at center
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "Tempting. Very tempting. I'll see what I can do."

    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus festive flipped at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left

    arceus "Hey, at least you can go to LTT and not have to {i}walk{/i} like last time!"
    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs christmas at center
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show k17 at manual_pos(-0.5, 0.6, 0.5)
    show left_table
    cs "True..."
    cs "Honestly, Arc, would you like to come with me?"

    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus festive flipped at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show right_table at left
    show wesley festive at manual_pos(1.3, 0.6, 0.5)
    show rich festive at manual_pos(1.5, 0.6, 0.5)
    show linus festive at manual_pos(1.65, 0.6, 0.5)
    show luke festive at manual_pos(1.80, 0.6, 0.5)
    arceus "Me? I live in the UK now. I don't know if I can make it all the way to West Canada."

    scene night_bg
    show right_room at right
    show right_chair_back at right
    show arceus festive flipped at manual_pos(-0.95, 0.65, 0.5)
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
    linus "We can pay for your flight, as well!"

    scene night_bg
    show right_room at left
    show right_chair_back at left
    show arceus festive flipped at mid_offscreen_left
    show billy festive at mid_left
    show obama festive at center
    show michael festive at mid_right
    show ed festive at mid_offscreen_right
    show wesley festive at manual_pos(1.3, 0.6, 0.5)
    show rich festive at manual_pos(1.5, 0.6, 0.5)
    show linus festive at manual_pos(1.65, 0.6, 0.5)
    show luke festive at manual_pos(1.80, 0.6, 0.5)
    show right_table at left
    with move
    show arceus worried festive
    arceus "What about my betrothed, though?"

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
    luke "You just added {i}two{/i} international flights to the cost of this, Linus."
    linus "Since when have I {i}ever{/i} been responsible with money, Luke?"
    n "Luke takes a sip of his drink to keep himself from laughing too hard."
    luke "You said it, not me."

    scene night_bg
    show left_room
    show left_chair_back
    show anno festive at mid_left
    show cs christmas at center
    show tate festive at mid_right
    show db at manual_pos(1.1, 0.6, 0.5)
    show k22 at mid_offscreen_left
    show digi at manual_pos(-0.3, 0.65, 0.5)
    show left_table
    with dissolve
    pause 0.5
    show cs surprised christmas
    cs "Y'know, I kinda wish that I started learning to drive sooner."
    show cs happy christmas
    cs "I don't know how I managed before!"
    show left_room at left
    show left_chair_back at left
    show left_table at left
    show cs christmas at mid_offscreen_right
    show anno festive at mid_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 at center
    show digi flipped at manual_pos(0.175, 0.65, 0.5)
    with move
    k22 "Speaking of driving, this reminds me of something."
    k22 "Why does anyone buy regular unleaded gas?"
    show digi thinking flipped
    digi "Because it's cheaper?"
    k22 "Okay, but it's {i}not,{/i} though. Super unleaded is {i}way{/i} cheaper, {i}and{/i} it's better for your car."
    show digi disappointed flipped
    digi "That doesn't make any sense."
    show k22 confident
    k22 "It {i}doesn't,{/i} but it's true!"
    show k22 disappointed
    show digi sad flipped
    digi "It's {i}not,{/i} though! Super unleaded is more expensive."
    k22 "It's... {i}not,{/i} though."
    show digi angry flipped
    digi "What are you talking about? Of course it costs more, because it's better for your car!"
    show cs christmas flipped
    cs "Don't you guys mean \"unleaded plus\"?"
    digi "Yeah! See? {i}CS{/i} knows!"
    k22 "No, it's called \"super unleaded,\" {i}and{/i} it's cheaper than regular unleaded!"
    digi "But it's {i}not!{/i} Why {i}would{/i} it be?!"

    scene night_bg
    show right_room at center
    show right_chair_back at center
    show obama festive at mid_offscreen_left
    show michael festive at mid_left
    show ed festive at center
    show wesley festive at mid_right
    show rich festive at mid_offscreen_right
    show right_table at center
    ed "Are you thinking of \"premium unleaded?\""

    scene night_bg
    show left_room at left
    show left_chair_back at left
    show anno festive at mid_right
    show cs christmas flipped at mid_offscreen_right
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
    show anno festive at mid_right
    show cs disappointed christmas flipped at mid_offscreen_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 angry at center
    show digi disappointed flipped at manual_pos(0.175, 0.65, 0.5)
    show left_table at left
    k22 "It's called super unleaded, it has ethanol in it, and, it's better{w=0.15} for{w=0.15} your{w=0.15} {i}car!{/i}"
    k22 "Every gas station we've been to, it's {i}always{/i} regular, super, the third option, and diesel!"
    digi "I {i}still{/i} think you may be thinking of premium."
    k22 "No, I'm-- Give me a second, I have a picture of this on my phone."
    show digi thinking flipped
    digi "CS, have {i}you{/i} ever seen super unleaded?"
    cs "Uhh... no?"
    show k22 confident
    k22 "Aha! See?"
    pause 0.5
    show gas_prices at mid_right:
        xzoom 0.0
        linear 0.25 xzoom 1.0
    n "K-22 flips their phone around to show the table an image."
    show digi shock flipped
    show cs scared christmas flipped
    digi "What?! {i}How?" with vpunch
    cs "What backwards-ass town do you live in where the {i}better{/i} gas is {nw}"
    cs "What backwards-ass town do you live in where the {i}better{/i} gas is {fast}{i}cheaper?!" with vpunch
    k22 "See? The super unleaded is the cheapest, then regular, {i}then{/i} premium!"
    hide gas_prices with easeoutbottom
    show digi thinking flipped
    show cs disappointed christmas flipped
    digi "So, the question {i}now{/i} is, what's the difference between plus and super?"
    show k22
    k22 "They might be the same thing."
    k22 "{i}Our{/i} super unleaded gas has ethanol in it."
    show k22 confident
    k22 "Guess who makes ethanol? {i}We{/i} do!"
    show digi happy flipped
    digi "I see, now!"
    show k22
    digi "So, because you guys {i}make{/i} this additive, it's cheaper for {i}you,{/i} but more expensive for {i}us.{/i}"
    k22 "Probably."
    show cs worried christmas flipped
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
    ed "That's great and all, but what in the {i}world{/i} is unleaded 88?"

    scene night_bg
    show left_room at left
    show left_chair_back at left
    show anno festive at mid_right
    show cs christmas flipped at mid_offscreen_right
    show tate festive at manual_pos(1.25, 0.6, 0.5)
    show db at manual_pos(1.65, 0.6, 0.5)
    show k22 at center
    show digi flipped at manual_pos(0.175, 0.65, 0.5)
    show left_table at left
    k22 "It's for cars made after 2001, that's all I know."
    mean "Man, fuck gasoline, I just use good old-fashioned {i}steam power,{/i} baby!"

    show digi sad flipped
    digi "Hey, CS, did K-17 ever come back from the bathroom?"
    show cs disappointed christmas flipped
    cs "Huh?"
    cs "Oh, is {i}that{/i} where they ran off to?"
    digi "We should probably go check and see if they are okay..."

    scene cs_bathroom
    with dissolve
    show digi sad flipped at mid_mid_left
    show cs disappointed christmas at left
    with moveinleft
    digi "Hey! K-17? Are you in there?"
    k17 "Nuh uh!"
    cs "Do you need... any help at all? We are gonna start the gift exchange here in a few minutes!"
    show cs scared christmas
    show digi shock flipped
    n "K-17 starts sobbing." with vpunch
    k17 "N-{w=0.1}No one... told me..."
    k17 "Mixer... {i}died...!"
    show cs christmas worried
    show digi sad flipped
    cs "Uh oh."
    digi "Shiiiiit."
    show cs christmas disappointed
    cs "Yeah, Mixer shut down some time ago now... sorry about that."
    show digi sad flipped
    k17 "But, why? {nw}"
    k17 "But, why? {fast}{i}Why?!" with vpunch
    k17 "It was, like, the {i}perfect{/i} streaming platform!"
    digi "It {i}was,{/i} but it was {i}also{/i} owned by Microsoft. It was bound to happen."
    show cs worried christmas
    cs "Hey!" with vpunch
    show digi sad
    show cs disappointed christmas
    digi "Listen, just because the Zune was cool doesn't mean--"
    k17 "What do we even do now? Without Mixer, where do you stream?!"
    show cs christmas
    show digi flipped
    cs "Well, I stream on {a=https://twitch.tv/cs188/}Twitch.{/a}"
    digi "{a=https://twitch.tv/DigiDuncan}Me too{/a}, when I get the chance."
    n "K-17 sniffles."
    k17 "At least Crazy Saturday lives on..."
    show cs christmas disappointed
    cs "{i}Well--{w=0.25}{nw}"
    show digi flipped
    digi "Let him believe, CS. Let him believe."
    pause 0.5
    scene black with dissolve
    pause 0.5

# Gift Exchange
label ce_exchange:
    scene cs_living
    show cs christmas at center
    with dissolve
    play music superstar_road volume 0.5
    music superstar_road
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        cs "Alright! It's time for the superstar road!"
    else:
        cs "Alright! It's time for the gift exchange!"
    cs "Everyone brought a gift, right?"
    n "The crowd responds with nods and vague confirmations."
    show festive_bag at manual_pos(0.6, 0.6, 0.5) with moveinbottom
    $ collect("festive_bag")
    cs "Cool!"
    cs "I've put all of your names in this bag. I'll bring it over so you all can draw one!"
    show cs christmas at offscreenright
    show festive_bag at manual_pos(1.3, 0.6, 0.5)
    with moveoutright
    pause 0.5
    n "CS brings the bag around to each attendee."
    pause 0.5
    cs "Let's see... who's going first?"
    "..."

    #roll 1
    cs "Would you look at that! I guess {i}I'm{/i} going first!"
    show cs christmas flipped at mid_left with moveinleft
    show cs christmas
    pause 0.5
    cs "I'm gonna pick..."
    show gift_arc at manual_pos(0.4, 0.6, 0.5) with { "master": moveinbottom }
    cs "I'm gonna pick...{fast}  this one!"
    cs "I got..."
    pause 0.5
    hide gift_arc
    show thigh_highs at manual_pos(0.4, 0.6, 0.5)
    with dissolve
    show cs disappointed christmas
    cs "Thigh-highs?"
    arceus "Look at that! You got my gift, CS!"
    hide thigh_highs with dissolve
    show cs christmas full at manual_pos(0.04, 0.188)
    cs "Welp, guess I have more now!"
    k17 "You wear thigh-highs?"
    cs "Yeah, I'm wearing them right now! See?"
    show cs christmas full  at Move((0.04, 0.188), (0.04, -0.4), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    window hide
    pause 2.5
    show cs christmas full at Move((0.04, -0.4), (0.04, 0.188), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.0
    digi "Oh, shit. I guess I never thought to look down to check."
    aria "I just assumed, given the rest of the outfit."
    hide cs with moveoutright
    pause 0.5
    $ collect("thigh_highs")

    arceus "Welp, it looks like I'm up next."
    show arceus festive flipped at mid_left with moveinleft
    show gift_kitty at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    arceus "I got..."
    pause 0.5
    hide gift_kitty
    show tea_and_crumpets at manual_pos(0.4, 0.7, 0.5)
    with dissolve
    arceus "Tea and crumpets?"
    kitty "Arcie! You got {i}my{/i} gift!" with hpunch
    hide tea_and_crumpets with dissolve
    show arceus festive worried flipped
    arceus "Sorry! I honestly forgot which one was yours!"
    kitty "You {i}saw{/i} me carry it in, dumbass!"
    hide arceus with moveoutright
    pause 0.5
    $ collect("tea_and_crumpets")

    kitty "Whatever, it's my turn now."
    show kitty festive at mid_left with moveinleft
    pause 0.5
    show gift_anno at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    kitty "Looks like I got..."
    hide gift_anno
    show riffmaster at manual_pos(0.4, 0.7, 0.5)
    with dissolve
    kitty "A... {i}Guitar Hero{/i} controller?"
    cs "Holy shit, that's a {i}Riffmaster!"
    kitty "Is that good?"
    cs "Yeah, those controllers are really good!"
    hide riffmaster with dissolve
    anno "That was my gift!"
    hide kitty with moveoutright
    pause 0.5

    anno "It looks like I'm up next."
    show anno festive at mid_left with moveinleft
    pause 0.5
    show gift_digi at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    anno "I got..."
    hide gift_digi
    show raspberry_pi at manual_pos(0.4, 0.7, 0.5):
        zoom 0.5
    with dissolve
    pause 0.5
    anno "What the hell {i}is{/i} this?"
    arceus "Ooh! That's a Raspberry Pi!"
    obama "What are you on about? That doesn't look edible at {i}all!"
    digi "No-- okay, it's {i}my{/i} gift, so let me explain."
    digi "It's a small computer that you can use to run basic servers or build little projects!"
    hide raspberry_pi with dissolve
    anno "Oh. Cool, I guess."
    hide anno with moveoutright
    pause 0.5

    show digi flipped at mid_left with moveinleft
    digi "Well, it's my turn now, and I'm gonna steal that Riffmaster!"
    show kitty festive flipped at mid_right with moveinright
    show riffmaster at manual_pos(0.7, 0.6, 0.5) with dissolve
    show riffmaster at manual_pos(0.35, 0.6, 0.5) with move
    hide riffmaster with dissolve
    hide digi with moveoutright
    $ collect("riffmaster")

    kitty "Damn."
    kitty "Well, what do I do now?"
    cs "You can either steal someone else's gift, or pick out another unopened one."
    show arceus festive flipped behind kitty at mid_offscreen_left with moveinleft
    arceus "{size=-12}Psst! Kitty! C'mere!"
    show kitty flipped at left with move
    pause 0.5
    play sound sfx_whisper
    n "Arceus whispers something into Kitty's ear."
    "..."
    kitty "Got it."
    show kitty festive at mid_left with moveinleft
    kitty "Anno, hand over your computer thing."
    show anno festive at mid_right with moveinright
    show raspberry_pi at manual_pos(0.7, 0.6, 0.5) with dissolve:
        zoom 0.5
    show raspberry_pi at manual_pos(0.35, 0.6, 0.5) with move
    pause 0.5
    hide raspberry_pi with dissolve
    show kitty festive flipped
    show arceus festive
    hide arceus
    hide kitty
    with moveoutright
    pause 0.5
    $ collect("raspberry_pi")

    anno "Welp, I'm picking a new gift, I guess."
    show anno festive at mid_left with move
    anno "I'll go with this one."
    show gift_mean at manual_pos(0.4, 0.7, 0.5) with moveinbottom:
        zoom 0.4
    anno "Wonder what it is."
    show lego_train at manual_pos(0.4, 0.7, 0.5)
    hide gift_mean
    with dissolve
    anno "A Lego set!"
    mean "A Lego {i}train{/i} set!"
    hide lego_train with dissolve
    mean "That's my gift, by the way."
    if fun_value(FUN_VALUE_COMMON):
        tate "We {i}know!" with hpunch
    hide anno with moveoutright
    pause 0.5
    $ collect("lego_train")

    mean "Alright, well, I guess it's my turn."
    show mean human flipped at mid_left with moveinleft
    show gift_tate at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    mean "I'm picking this big one!"
    show instant_pot at manual_pos(0.4, 0.7, 0.5)
    hide gift_tate
    with dissolve
    mean "An Instant Pot?"
    tate "Mean, ya goofball! You picked {i}my{/i} gift!" with hpunch
    show mean human happy flipped
    mean "Well, it's {i}mine{/i} now, bitch!"
    mean "I'm stealing your spaghetti recipe tomorrow, too!"
    tate "Awawa..."
    dxcom awawa
    hide instant_pot with { "master": dissolve }
    mean "Who's next?"
    hide mean with moveoutright
    pause 0.5
    $ collect("instant_pot")

    tate "Looks like I'm up."
    show tate sheepish festive at mid_left with moveinleft
    tate "Let's see..."
    show gift_billy at manual_pos(0.4, 0.7, 0.5) with moveinbottom:
        zoom 0.5
    pause 0.5
    show handy_switch at manual_pos(0.4, 0.7, 0.5):
        zoom 0.4
    hide gift_billy
    with dissolve
    show tate smug festive
    tate "Billy? Is this yours?"
    billy "It's the Handy Switch!"
    billy "It lets you control {i}any{/i} power source {w=0.25}from {i}anywhere!"
    show tate festive
    tate "I'm sure I can find a use for this. Thanks!"
    hide screen dxcom
    hide handy_switch with dissolve
    hide tate with moveoutright
    pause 0.5
    $ collect("handy_switch")

    billy "Alright! That means it's {i}my{/i} turn!"
    show billy festive flipped at mid_left with moveinleft
    show gift_obama at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    billy "Hi, Billy Mays here for {i}my{/i} turn!"
    show doi at manual_pos(0.4, 0.7, 0.5)
    hide gift_obama
    with dissolve
    billy "Wow! Is this the Declaration of Independence?"
    obama "Yep! It's the real deal!"
    obama "I figured that, since I didn't need it anymore, it would make a wonderful gift!"
    billy "Great! I can probably pitch this!"
    hide doi with dissolve
    hide billy with moveoutright
    pause 0.5

    obama "This means that it's my turn now."
    show obama festive flipped at mid_left with moveinleft
    show gift_copguy at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show mgs1 at manual_pos(0.4, 0.6, 0.5):
        zoom 0.5
    hide gift_copguy
    with dissolve
    obama "{i}Metal Gear Solid?"
    copguy "Yeah, that's from me."
    copguy "I didn't know what anyone would really want, so I just brought this after I found it in the station's break room."
    obama "Dude, this is, like, my {i}favorite{/i} game! I appreciate it."
    copguy "Well, I'm glad that works out!"
    hide mgs1 with dissolve
    hide obama with moveoutright
    pause 0.5
    $ collect("mgs1")

    copguy "It's my turn now."
    show copguy festive flipped at mid_left with moveinleft
    show gift_sheriff at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show gravity_falls at manual_pos(0.35, 0.65, 0.5):
        zoom 0.5
    hide gift_sheriff
    with dissolve
    copguy "Okay, so I got {i}Gravity Falls, The Complete Series: Collector's Edition..."
    show colt at manual_pos(0.4, 0.7, 0.5) with dissolve:
        zoom 0.5
    copguy "And... boss? Is this your gun?"
    sheriff "Yeah, you got my gift. Don't ask how that DVD got in there."
    sheriff "Because I don't know, either."
    hide gravity_falls
    hide colt
    with dissolve
    hide copguy with moveoutright
    pause 0.5

    show sheriff festive flipped at mid_left with moveinleft
    sheriff "Whatever! It's {i}my{/i} turn to pick a gift."
    show gift_ed at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    sheriff "Damn, this is {i}heavy!{/i} What the hell {i}is{/i} this?!"
    show cement at manual_pos(0.4, 0.7, 0.5)
    hide gift_ed
    with dissolve
    sheriff "A bag of {i}cement?!" with vpunch
    ed "Yep! We had some leftover from the last house we worked on."
    ed "Solid enough for a home's foundation, versatile enough for all kinds of other projects."
    hide cement with dissolve
    sheriff "Great! I can drop this on Copguy's head for {i}leaving{/i} me in the damn {nw}"
    sheriff "Great! I can drop this on Copguy's head for {i}leaving{/i} me in the damn {fast}{i}bathroom!" with vpunch
    hide sheriff with moveoutright
    pause 0.5
    $ collect("cement")

    ed "I guess it's my go."
    show ed festive flipped at mid_left with moveinleft
    show gift_richard at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    ed "What the hell? Who brought Dairy Queen?!"
    ed "This gift's all drippy!"
    show melted_ice_cream at manual_pos(0.4, 0.6, 0.5):
        zoom 0.5
    hide gift_richard
    with dissolve
    #Audio clip of Richard laughing
    play sound sfx_richlaugh
    pause 1.5
    ed "{i}Damn it,{/i} Richard! I don't want {i}this!" with vpunch
    hide melted_ice_cream with dissolve
    hide ed with moveoutright
    pause 0.5
    $ collect("melted_ice_cream")

    rich "Well, let's see what I get."
    show rich festive flipped at mid_left with moveinleft
    show gift_wesley at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    pause 0.5
    show pills at manual_pos(0.4, 0.6, 0.5):
        zoom 0.3
    hide gift_wesley
    with dissolve
    rich "Pain pills?!"
    wesley "Wait a minute! Those are {i}mine!" with hpunch
    show wesley festive behind pills at mid_right with moveinright
    wesley "I didn't mean to gift those!"
    wesley "Gimme that!"
    show pills at manual_pos(0.7, 0.6, 0.5) with MoveTransition(0.25)
    hide pills with dissolve
    show wesley festive flipped at offscreenright with { "master": move }
    rich "Hey!" with vpunch
    rich "What do I even {i}get,{/i} then?!"
    rich "Nobody has anything I'd really want..."
    rich "I guess it's time to open another present."
    $ collect("pills")

    show gift_k17 at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show sunny_d at manual_pos(0.4, 0.6, 0.5):
        zoom 0.75
    hide gift_k17
    with dissolve
    rich "Hey, I got Sunny D!"
    n "K-17 starts giggling."
    hide sunny_d with dissolve
    hide rich with moveoutright
    pause 0.5
    $ collect("sunny_d")

    k17 "Alright! My go!"
    show k17 flipped at mid_left with moveinleft
    show gift_k22 at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show fumo at manual_pos(0.4, 0.7, 0.5)
    hide gift_k22
    with dissolve
    pause 0.5
    show k17 disappointed flipped
    k17 "Addy?"
    show k22 disappointed flipped at offscreenleft
    k22 "Huh?!" with hpunch
    show k22 flipped at offscreenleft with determination
    show k22 flipped at left with MoveTransition(0.25)
    show k22 flipped at offscreenright
    show fumo at offscreenright
    with  MoveTransition(0.25)
    n "K-22 springs up and steals the gift from K-17 before sprinting out of the room!"
    k22 "I'm sorry! I'll be right back!" with hpunch
    show k17 shock flipped
    k17 "What the hey?!" with vpunch
    $ collect("fumo")

    k17 "Now, I gotta get another gift!"
    show k17 flipped
    k17 "I'm gonna take the {i}Gravity Falls{/i} DVD!"
    show copguy festive at mid_right with moveinright
    show gravity_falls at manual_pos(0.7, 0.7, 0.5) with dissolve:
        zoom 0.5
    show gravity_falls at manual_pos(0.4, 0.7, 0.5) with move
    hide gravity_falls with dissolve
    show colt at manual_pos(0.7, 0.7, 0.5) with dissolve:
        zoom 0.5
    show colt at manual_pos(0.4, 0.7, 0.5) with { "master": move }
    k17 "... {i}And{/i} the gun."
    hide colt with dissolve
    hide k17 with moveoutright
    pause 0.5
    $ collect("gravity_falls")
    $ collect("colt")

    show copguy festive at left with move
    show copguy festive flipped with determination
    copguy "Alright, then, {i}I'm{/i} taking the Declaration of Independence!"
    show billy festive at center with moveinright
    billy "What the actual fuck?"
    show doi at manual_pos(0.5, 0.7, 0.5) with dissolve
    show doi at manual_pos(0.2, 0.7, 0.5) with move
    billy "Stop stealing gifts!" with vpunch
    hide doi with dissolve
    hide copguy with moveoutright
    pause 0.5
    $ collect("doi")

    show billy festive at mid_left with move
    show billy festive flipped
    billy "Alright, I'll just take the next gift!"
    show gift_aria at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    pause 0.5
    show adderall at manual_pos(0.4, 0.6, 0.5):
        zoom 0.4
    hide gift_aria
    with dissolve
    billy "Adderall?"
    billy "{i}Nope!{/i} I'm done with {i}any{/i} kind of drug! Not after last time!"
    aria "Aw, that was my gift!"
    aria "You want me to take it back?"
    billy "Yes, {i}please!"
    show aria festive behind adderall at mid_right with moveinright
    show adderall at manual_pos(0.7, 0.6, 0.5) with move
    hide adderall with dissolve
    hide aria with moveoutleft
    $ collect("adderall")

    billy "Awesome! I get to pick another gift!"
    show gift_michael at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    pause 0.5
    show peach_syrup at manual_pos(0.4, 0.6, 0.5)
    hide gift_michael
    with dissolve
    if fun_value(FUN_VALUE_RARE):
        billy "An oil drum full of peach syrup!"
        billy "An {i}incredible{/i} value! I'll {i}never{/i} run out again!"
    else:
        billy "Peach syrup!"
    michael "Noice, you got my gift!"
    michael "It goes well with just about anything!"
    hide peach_syrup with dissolve
    billy "Sounds delicious! I'll keep this one!"
    hide billy with moveoutright
    pause 0.5
    $ collect("peach_syrup")

    michael "Right, then. Which gift to choose...?"
    show michael festive at mid_left with moveinleft
    show gift_linus at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    pause 0.5
    show ltt_bottle at manual_pos(0.4, 0.6, 0.5):
        zoom 0.75
    hide gift_linus
    with dissolve
    michael "I've gotten a new water bottle!"
    linus "You got my {i}LTT{/i} water bottle!"
    linus "{a=https://www.lttstore.com}lttstore.com.{/a}"
    hide ltt_bottle with dissolve
    hide michael with moveoutright
    pause 0.5
    $ collect("ltt_bottle")

    linus "Alright, my turn."
    show linus festive flipped at mid_left with moveinleft
    show gift_luke at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    pause 0.5
    show ltt_screwdriver at manual_pos(0.4, 0.6, 0.5):
        zoom 0.5
    hide gift_luke
    with dissolve
    linus "Hey, Luke! I got your gift!"
    luke "Couldn't you {i}tell{/i} it was mine?"
    linus "No? How was I supposed to know that?"
    luke "You were {i}literally{/i} there when I grabbed it from the warehouse..."
    hide ltt_screwdriver with dissolve
    hide linus with moveoutright
    pause 0.5
    $ collect("ltt_screwdriver")

    luke "Whatever, it's my go now."
    show luke festive flipped at mid_left with moveinleft
    luke "I got..."
    show gift_blank at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show monitor as first at manual_pos(0.3, 0.7, 0.5)
    show monitor as second at manual_pos(0.5, 0.7, 0.5)
    show hard_drive at manual_pos(0.4, 0.7, 0.5):
        zoom 0.5
    hide gift_blank
    with dissolve
    luke "Some random PC components?"
    blank "Yeah! It's two monitors, a 1TB hard drive, and some other things."
    blank "I found them on the curb."
    luke "On the {i}curb{/i}?"
    blank "Yeah, all that was just lying there on the curb."
    luke "Damn! Well, then..."
    hide monitor as first
    hide monitor as second
    hide hard_drive
    with dissolve
    hide luke with moveoutright
    pause 0.5
    $ collect("monitor")
    $ collect("hard_drive")

    blank "It looks like it's my turn next."
    show blank festive flipped at mid_left with moveinleft
    show gift_nova at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show gamersupps at manual_pos(0.4, 0.7, 0.5):
        zoom 0.5
    hide gift_nova
    with dissolve
    blank "Gamer Supps?"
    show gamersupps at manual_pos(0.35, 0.65, 0.5) with move
    n "Blank holds the canister a little closer and reads it carefully."
    blank "\"Guacamole... Gamer Fart... 9000\"...?"
    nova "Damn it! You got {i}my{/i} gift, Blank!" with hpunch
    show gamersupps at manual_pos(0.4, 0.7, 0.5) with { "master": move }
    blank "Great."
    hide gamersupps with dissolve
    hide blank with moveoutright
    pause 0.5
    $ collect("gamersupps")

    nova "As much as I want to steal that Adderall, I'm gonna pick an unopened gift."
    show nova flipped at mid_left with moveinleft
    show gift_eliza at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    nova "Oh boy! I wonder what it is!"
    pause 0.5
    show russian_radio at manual_pos(0.4, 0.7, 0.5)
    hide gift_eliza
    with dissolve
    nova "What the fuck {i}is{/i} it? Some World War II radio?"
    eliza "Yep. Used by the Soviets in the latter half of World War II."
    nova "Hey Ges, do you want this?"
    ges "Sure, thank you!"
    hide russian_radio with dissolve
    hide nova with moveoutright
    n "Nova sits down and gives the radio to Ges."
    $ collect("russian_radio")

    eliza "So, it's my turn. Let's see what we have..."
    show elizabeth at mid_left with moveinleft
    show gift_db at manual_pos(0.4, 0.7, 0.5) with moveinbottom
    pause 0.5
    show dog_food at manual_pos(0.4, 0.7, 0.5)
    hide gift_db
    with dissolve
    eliza "Dog food."
    hide dog_food with dissolve
    eliza "Dog food?"
    db "Ah, yeah, I had a lot extra lying around in my car, so I figured, why not?"
    hide elizabeth with moveoutright
    pause 0.5
    $ collect("dog_food")

    db "Well, I guess it's finally my turn."
    show db at mid_left with moveinleft
    show gift_anne_grace at manual_pos(0.4, 0.6, 0.5) with moveinbottom
    pause 0.5
    show 1850_coin at manual_pos(0.4, 0.6, 0.5):
        zoom 0.5
    hide gift_anne_grace
    with dissolve
    db "Neat, I got some old coins!"
    digi "Holy shit! I think those are, like, {i}really{/i} rare!"
    show digi happy at center with { "master": moveinright }
    digi "Lemme look these up."
    grace "You got our coins!"
    anne "We had them lying around on the table at home."
    show digi
    "..."
    digi "Yeah, these are super rare. I would hold onto these if I were you."
    hide 1850_coin with dissolve
    $ collect("old_coins")
    arceus "Say, don't you collect coins, Digi?"
    show digi flipped
    digi "Not really. I just collect pennies."
    arceus "... Why {i}just{/i} pennies?"
    show digi thinking flipped
    digi "So, I have, like, 5000 pennies."
    digi "One day, when America stops making pennies, they'll go up in value."
    obama "Why would we stop making pennies?"
    digi "Well, you guys spend 1.6 cents per penny to make them, so you're losing money."
    digi "Canada already stopped making their pennies."
    mean "Well, yeah, that's because Canada's smarter than America."
    show digi happy flipped
    digi "Anywho, one day, when I have 5000 rare coins in a jar, it'll all have been worth it."
    arceus "Alright, then..."
    billy "Antique coins lying around, tech lying on the curb..."
    billy "Where the hell do you guys live where you can just {i}find{/i} this kinda shit?"
    hide db
    hide digi
    with moveoutright
    pause 0.5

    if d20 == 20:
        avgn "Outta my way! {nw}" with hpunch
        avgn "Outta my way! {fast}It's {i}my{/i} turn!" with hpunch
        show avgn flipped at mid_left with moveinleft
        show gift_cs at manual_pos(0.4, 0.7, 0.5) with moveinbottom
        avgn "Let's do this!"
        dxcom gift_exchange
        show old_shirt at manual_pos(0.4, 0.7, 0.5)
        hide gift_cs
        with dissolve
        avgn "This shirt is {nw}"
        avgn "This shirt is {fast}{i}ass!" with vpunch
        cs "Hey! That was {i}my{/i} gift!"
        avgn "Yeah? Well, you're a poopyhead!"
        hide old_shirt with dissolve
        hide avgn with moveoutright
        pause 0.5
        $ collect("old_shirt")

    anne "Well, Grace, you wanna pick out the last gift?"
    show grace at mid_left with moveinleft
    grace "Yippee! The last gift!"

    if d20 == 20:
        show gift_avgn at manual_pos(0.4, 0.7, 0.5) with moveinbottom
        pause 0.5
        show roll_and_rocker at manual_pos(0.4, 0.7, 0.5)
        show rolling_rock at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5
        hide gift_avgn
        with dissolve
        grace "Ooh! Is this a balance board?"
        avgn "It's a Rolling Rock..."
        avgn "With a Roll & Rocker!"
        hide roll_and_rocker
        hide rolling_rock
        with dissolve
        grace "Cool!"
        $ collect("roll_and_rocker")
        $ collect("rolling_rock")
    else:
        show gift_cs at manual_pos(0.4, 0.7, 0.5) with moveinbottom
        pause 0.5
        dxcom gift_exchange
        show old_shirt at manual_pos(0.4, 0.7, 0.5)
        hide gift_cs
        with dissolve
        grace "I got a cool new t-shirt!"
        cs "Nice! Someone finally got my gift!"
        cs "Not all of my Depop shirts sold, and I think this one is really cool, so, now it's a gift!"
        cs "Does it fit you okay?"
        n "Grace puts on the shirt."
        hide old_shirt
        show grace shirt
        with dissolve
        pause 2.0
        grace "Yep!"
        $ collect("old_shirt")
    hide grace with moveoutright
    pause 0.5
    hide screen dxcom
    cs "Woohoo! All of the gifts have been handed out!"
    jump ce_preclimax

label ce_preclimax:
    play music snowman if_changed
    music snowman
    scene black with dissolve
    n "After the exchange, the party begins to die down."
    n "Folks naturally start splitting into groups to discuss their gifts."

    scene cs_foyer
    show digi happy flipped at left
    dxcom gifts
    show riffmaster at manual_pos(0.15, 0.8, 0.5):
        rotate 45
    show aria festive at center
    show adderall at manual_pos(0.4, 0.6, 0.5):
        zoom 0.4
    show arceus festive at right
    show raspberry_pi at manual_pos(0.75, 0.7, 0.5):
        zoom 0.5
    with dissolve
    pause 0.5

    digi "This Riffmaster is {i}great!{/i}"
    digi "Just listen to that strumbar!"
    n "Digi strums the controller in joy."
    digi "Oh, yeah. You gonna take that Adderall, Aria?"
    aria "That implies that I haven't already."
    digi "What about you, Arc? What are you going to do with that Raspberry Pi?"
    arceus "I had an idea for a webserver I've been meaning to try out."
    digi "Nice, nice."
    hide screen dxcom
    show luke festive at mid_right behind arceus
    show monitor as first at manual_pos(0.7, 0.7, 0.5) behind luke
    show monitor as second at manual_pos(0.85, 0.7, 0.5) behind arceus
    show hard_drive at manual_pos(0.575, 0.6, 0.5):
        zoom 0.5
    with moveinright

    n "Luke walks by, lugging a newly-acquired monitor under each arm."
    digi "Hey, Luke! Nice winnings!"
    luke "Thanks! I feel like I just won {i}Scrapyard Wars{/i} again."

    show luke festive at manual_pos(-0.1, 1.0, 1.0)
    show monitor as first at manual_pos(-0.3, 0.7, 0.5)
    show monitor as second at manual_pos(-0.2, 0.7, 0.5)
    show hard_drive at manual_pos(-0.5, 0.6, 0.5)
    with MoveTransition(1.0)
    pause 0.5

    scene cs_living
    show billy festive flipped at left
    show peach_syrup at manual_pos(0.15, 0.7, 0.5)
    show michael festive at mid_left
    show ltt_bottle at manual_pos(0.25, 0.7, 0.5):
        zoom 0.75
    show obama festive at right
    show mgs1 at manual_pos(0.8, 0.7, 0.5):
        zoom 0.5
    with dissolve
    pause 0.5

    show luke festive at center
    show monitor as first at manual_pos(0.5, 0.7, 0.5) behind luke
    show monitor as second at manual_pos(0.65, 0.7, 0.5)
    show hard_drive at manual_pos(0.325, 0.6, 0.5):
        zoom 0.5
    with moveinright

    michael "Luke! Please tell your friend Linus that he makes a {i}jolly{/i} good water bottle!"
    luke "Will do!"

    show luke festive at manual_pos(-0.1, 1.0, 1.0)
    show monitor as first at manual_pos(-0.3, 0.7, 0.5)
    show monitor as second at manual_pos(-0.2, 0.7, 0.5)
    show hard_drive at manual_pos(-0.5, 0.6, 0.5)
    with MoveTransition(1.0)
    pause 1.0

    billy "Michael, this peach syrup is {i}delicious!"
    show michael festive flipped
    michael "Lovely, innit?"
    billy "I might need to start selling this stuff!"
    show michael festive
    obama "I'm just excited to go back home and play some {i}Metal Gear Solid!"
    billy "Do you have a PS1?"
    obama "Are you kidding me? I'm {i}Obama!{/i} Of {i}course{/i} I have a PlayStation!"
    pause 0.25

    show tate festive flipped at center
    show handy_switch at manual_pos(0.4, 0.7, 0.5):
        zoom 0.4
    with moveinright
    tate "Howdy, y'all!"
    billy "Hi, Tate! I hope you enjoy that Handy Switch!"
    show tate sheepish festive flipped
    tate "I'm... not quite sure {i}how{/i} I'll enjoy it yet, but... thanks!"
    show billy festive
    show michael festive flipped
    cs "Michael? Obama? Can you come into the kitchen real quick?"
    michael "Right-o!"
    obama "On our way!"
    show michael festive flipped at offscreenleft
    show ltt_bottle at manual_pos(-0.2, 0.7, 0.5)
    show billy festive at offscreenleft
    show peach_syrup at manual_pos(-0.2, 0.7, 0.5)
    with move
    pause 0.5

    show tate shock festive flipped
    show copguy festive flipped at offscreenleft with determination
    show copguy festive flipped at offscreenright with { "master": move }
    copguy "Stop chasing me, you old fart!" with hpunch

    show tate shock festive
    show handy_switch at manual_pos(0.6, 0.7, 0.5):
        zoom 0.4
    show cement at manual_pos(-0.1, 0.4, 0.5)
    show sheriff festive at offscreenleft
    with determination
    show sheriff festive flipped at offscreenright
    show cement at manual_pos(1.2, 0.4, 0.5)
    with { "master": move }
    sheriff "I didn't keep this stupid bag of cement for {i}nothin'!" with hpunch
    sheriff "{cshake}Get back here!" with hpunch
    pause 0.25
    show tate sheepish festive
    play sound sfx_cat_crash
    with hpunch
    with vpunch
    pause 5.0
    show mean human annoyed flipped at offscreenleft
    show instant_pot at manual_pos(-0.2, 0.7, 0.5)
    with determination
    show mean human annoyed flipped at left behind tate
    show instant_pot at manual_pos(0.3, 0.7, 0.5) behind tate
    with { "master": MoveTransition(1.0) }
    mean "Yo, Tate."
    show tate sheepish festive flipped
    show handy_switch at manual_pos(0.4, 0.7, 0.5):
        zoom 0.4
    mean "This Instant Pot is cool and all, but why would you bring a {i}kitchen appliance{/i} to a gift exchange?"
    mean "Ain't that kinda... tacky?"
    show tate srs festive flipped
    tate "Normally, I'd agree with you, but hear me out!"
    tate "Buying one of these was {i}actually{/i} life-changing!"
    show tate festive flipped
    tate "You can throw everything in, turn it on, go relax..."
    tate "Then, a while later, you have hot food!"
    show tate sheepish festive flipped
    tate "No standing in front of a stove and throwing your back out, no burning yourself on an oven rack, no slamming your shin into the oven door, no steam burns-- {nw}"
    # these are all REAL injuries i have sustained in the kitchen... many times... - tate
    show mean human angry flipped
    mean "How in the {nw}" with hpunch
    show tate shock festive flipped
    mean "How in the {fast}{i}fuck{/i} {nw}" with vpunch
    mean "How in the {i}fuck{/i} {fast}do you keep hurting yourself like this?!" with hpunch
    show tate sad festive flipped
    tate "{sc=1.0}You think {i}I{/i} know?!"
    pause 0.5
    jump ce_climax

# Games/Climax
label ce_climax:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "After some time, everyone gets their fill of food and conversation."
    n "Although it is unspoken, the guests seem to mutually feel that it's time for the festivies came to a close."
    scene cs_living
    show cs christmas at left
    show tate festive flipped at mid_right
    show luke festive at right
    show k22 at center
    show k17 at mid_mid_right
    show mean human at mid_offscreen_right behind cs
    with dissolve
    k22 "Well, CS, this was wonderful, but we should really get going."
    show cs worried christmas
    cs "Wait! You aren't gonna stay for the games?"
    show k22 angry
    k22 "SHHHDADA--{w=0.25}{nw}" with vpunch
    show k17 happy
    k17 "We're doing {i}games?!{/i}" with vpunch
    k17 "Wait, that's the best part!"
    show cs disappointed christmas
    show tate sheepish festive flipped
    k22 "{size=-12}Damn it!" with vpunch
    show k22 disappointed
    show k17 disappointed
    show cs angry christmas
    show mean human annoyed
    cs "If you hated my party so much, then just leave!"
    if fun_value(FUN_VALUE_COMMON):
        cs "If you hated my party so much, then you can just fucking die!" # NOTE: This is supposed to be a reference to the Comfort Click video, but I don't know if he'll read it like that. - pak
    nova "Well, I'm {i}also{/i} leaving, because {i}this{/i} asshole won't let me play any {i}good{/i} music!" with hpunch
    blank "Hah! Says you! {i}You{/i} just wanted to play {i}your{/i} trash for the entire party!" with hpunch
    show projector_airplay behind cs:
        zoom 1.3
        perspective True
        matrixanchor (0, 0)
        matrixtransform RotateMatrix(0, 0, 0) * RotateMatrix(0, 35, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(32, 40, 0)
    with dissolve
    digi "Hey, wait a second! Luke!" with hpunch
    luke "Wha--?"
    luke "Oh, {i}shit."
    show tate sad festive flipped
    digi "You were... streaming movies to the projector from your {i}phone?!"
    show mean human annoyed
    luke "Look, this looked too complicated to set up, and I just wanted to enjoy the party!"
    luke "I just did it to make it feel like your plan worked!"
    digi "But-- but..."
    digi "I really thought I could set it up this time..."
    sheriff "Hey, Copguy! I need to go to the bathroom again!" with hpunch
    copguy "Motherfucker! Do it {i}yourself!" with hpunch
    ed "My poor turkey..."
    michael "I think I'm going to puke."
    wesley "Arghh! My {i}back!" with hpunch
    wesley "CS, you prick, this is {nw}"
    wesley "CS, you prick, this is {fast}{i}your{/i} fault!" with hpunch
    grace "Guys! Stop yelling!" with hpunch
    show tate sheepish festive flipped
    tate "Y'all, please, let's get it together..."
    show tate cry festive flipped
    nova "{i}No!{/i} Fuck you!" with hpunch
    show mean human angry
    anne "Hey!" with hpunch
    mean "What'd you say, you little {nw}"
    mean "What'd you say, you little {fast}{i}fuck?" with hpunch
    arceus "Oh, my God, this is hurting my {i}head..."
    show cs pissed christmas
    cs "Damn it, everyone!" with vpunch
    cs "Shut the {i}fuck{/i} u--{nw}" with vpunch

# Lights out
screen flashlight_demo():
    layer "flashlight"
    add Flashlight()

label ce_lights_out:
    play sound sfx_power_out
    $ mouse_visible = False
    scene black with Dissolve(0.1)
    stop music
    music end
    pause 0.2
    $ achievement_manager.unlock("power_off")
    pause 3.8
    sheriff "Hey, uh..."
    sheriff "I think I have finally become blind."
    linus "I think {i}all{/i} of our eyes went out."
    cs "{i}No!{/i} This {i}can't{/i} be happening!" with vpunch
    cs "My party is {i}ruined!"
    tate "CS, this isn't your fault..."
    cs "Everyone is fighting, and no one is having fun!"
    nova "Well, yeah, but at least I don't have to listen to Blank's shitty music anymore."
    tate "{i}Can it!" with hpunch
    tate "Listen! We all need to stop the arguing and calm down!"
    billy "I {i}am{/i} calm!"
    aria "I am clam."
    cs "Okay, I'm trying to relax... and think..."
    cs "Let me feel my way to the basement, and I'll try to check the breaker."
    cs "I'll be right back."
    pause 0.5
    play sound sfx_bump
    k17 "{i}Oof!" with vpunch
    cs "Sorry!"
    pause 2.0
    arceus "CS? Is that you?"
    cs "Hey, Arc. I'm making my way to the breaker to try to get the power back on."
    arceus "Great. If you find Kitty, lemme know. I don't know where she went."
    arceus "She said she was going to grab more food, but it's been 20 minutes since..."
    cs "Sure thing. I'll let you know."
    pause 2.0
    cs "The door to the basement should be here somewhere..."
    pause 0.5
    n "CS feels around the wall."
    n "Finally he finds the doorknob."
    cs "A-ha!"
    if fun_value(FUN_VALUE_EPIC):
        cs "Huh, why is my doorknob..."
        cs "Squeezable?"
        n "He gives it a turn."
        play sound sfx_hitbod3
        cs "Ow!" with vpunch
        cs "What the fuck was {i}that?!"
        eliza "Oops, sorry."
        eliza "You grabbed my... chest."
        cs "Oh, {i}crap!{/i} I'm so sorry!" with vpunch
        eliza "It's okay! None of us can see!"
        cs "I'm just trying to get to the basement! I think you're in front of the door!"
        eliza "Let me just move out of the way."
        cs "Yeah, thanks."
    else:
        cs "Why is my doorknob so big?"
        n "CS turns the doorknob."
        grace "{i}AHHHH!" with vpunch
        grace "You're squeezing my {i}head!" with vpunch
        cs "Oops, sorry!"
        cs "I'm just trying to get to the basement!"
        grace "Let me move before you try breaking my head again."
    pause 0.5
    play sound sfx_house_door_open
    pause 1.0
    n "Slowly but surely, CS carefully makes his way down the stairs."
    pause 1.0
    cs "Alright, now, I just need to find the breaker..."
    pause 0.5
    n "CS feels around and manages to pick up a flashlight from the table."

    scene cs_basement
    show cs christmas at center
    show flashlight_held at manual_pos(0.5, 0.7, 0.5):
        zoom 0.5
    $ collect("flashlight_held")
    play sound sfx_flashlight_on
    show screen flashlight_demo
    cs "Thank God. I can actually see..."
    pause 0.5
    hide cs
    hide flashlight_held
    with moveoutright

    scene breakerbox with dissolve
    show cs christmas at left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    with moveinleft
    cs "Found it!"
    show cs christmas at right
    show flashlight_held at manual_pos(0.8, 0.7, 0.5)
    with move
    show cs christmas flipped
    show flashlight_held flipped
    with determination
    pause 0.5
    play sound sfx_creaky_metal
    n "CS opens the breaker and flicks the switches on and off."
    play sound sfx_breaker
    pause 1.5
    play sound sfx_breaker
    pause 0.5
    play sound sfx_breaker
    show cs disappointed christmas flipped
    pause 1.0
    cs "Damn, nothing..."
    cs "Power must be out for the whole neighborhood, then."
    show cs christmas flipped
    cs "Well, it was worth a try."
    hide cs
    hide flashlight_held
    with moveoutleft
    pause 1.0

    scene cs_basement
    show cs christmas at center
    show flashlight_held at manual_pos(0.5, 0.7, 0.5):
        zoom 0.5
    show kitty festive at left
    with dissolve
    cs "At least I have this flashlight now!"
    show cs christmas flipped
    show flashlight_held flipped
    n "As CS turns around, he spots Kitty leaning against the wall."
    play music synchronicity if_changed
    music synchronicity
    show cs disappointed christmas flipped
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        cs "Kitty? What are the chances that I found you down here? Arceus was looking all over for you!"
        cs "Think of the synchronicity of this situation!"
        kitty "Uhh..."
    else:
        cs "Kitty? What are you doing down here? Arceus was looking all over for you!"
    kitty "Sorry..."
    kitty "I started getting a bad migraine towards the end of the party, so I tried to find the quietest place in the house."
    kitty "I'm a little glad the power went out, honestly. It's been peaceful here."
    cs "Ah... I was just trying to fix the breaker, but no dice."
    kitty "I think the power is out everywhere. I heard the wind really pick up outside a little while ago."
    kitty "You should probably go check for yourself."
    kitty "Could you please let Arcie know I'm down here? I think I'm gonna stay here a bit longer."
    cs "Sure thing. Stay safe."
    show cs disappointed christmas
    show flashlight_held
    with determination
    show cs disappointed christmas at right
    show flashlight_held at manual_pos(0.8, 0.7, 0.5)
    with move
    pause 0.5
    hide cs
    hide flashlight_held
    with dissolve
    n "CS heads back upstairs."
    pause 0.5

    scene cs_hallway_off
    show arceus festive at center
    show elizabeth at right
    with dissolve
    pause 0.5
    show cs disappointed christmas at left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    with moveinleft
    arceus "Welcome back!"
    arceus "Assuming you didn't get the power working?"
    show cs christmas
    cs "Nope, but I found Kitty!"
    cs "She's relaxing in the basement since her head was hurting."
    arceus "That makes sense. I'll go talk to her here soon."
    eliza "I see you found a torch."
    cs "Yeah, it was just sitting on a table downstairs. I'm so thankful it was there."
    show arceus festive flipped
    eliza "Arceus, would you like to borrow mine, so you can go be with Kitty?"
    arceus "I would appreciate it."
    show elizabeth at mid_right with move
    show flashlight_held flipped as second at manual_pos(0.7, 0.7, 0.5):
        zoom 0.5
    with dissolve
    eliza "Just make sure to bring it back when the lights come on."
    arceus "Got it."
    show flashlight_held flipped as second at manual_pos(0.5, 0.7, 0.5) behind cs with move
    arceus "Thanks!"
    pause 0.5
    show arceus festive
    with determination
    hide arceus
    hide flashlight_held as second
    with moveoutleft
    pause 1.5
    eliza "Before you go, CS, if you can, I think you should check outdoors."
    eliza "Even though it's dark in here, no light is coming in from outside."
    eliza "It also sounds {i}terrible{/i} out there."
    eliza "I've experienced some harsh Soviet winters, but I've never dealt with anything {i}this{/i} bad before."
    show cs worried christmas
    cs "Well, that's some {i}awesome{/i} news..."
    show cs disappointed christmas
    cs "I'll go check on the others, then I'll see if I can get outside."
    hide cs
    hide flashlight_held
    with moveoutright
    pause 0.5

    scene cs_foyer_off_festive
    show anno festive at mid_left
    show aria festive at mid_right behind anno
    show mean human annoyed at mid_offscreen_right
    show tate sad festive flipped at right
    show digi sad at mid_mid_left
    show k17 disappointed at center behind digi
    show k22 disappointed at mid_mid_right
    with dissolve
    pause 0.5
    show cs disappointed christmas at left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    with moveinleft
    cs "Hey guys! How is everyone holding up?"
    tate "It's getting kinda cold..."
    anno "My phone's about to die."
    cs "I'm gonna check outside and see how bad it is."
    k22 "Oh, yeah. I was thinking about trying the same thing, but I couldn't find the door."
    cs "If we can get outside, we might be able to dig our vehicles out."
    cs "I'll be back in a sec."
    hide cs
    hide flashlight_held
    with moveoutright
    anno "Good luck, CS!"
    hide screen flashlight_demo
    scene black
    with dissolve
    $ mouse_visible = True
    pause 0.5

    n "CS makes it to the front door."
    pause 0.5
    play sound sfx_door_jiggle
    n "He tries to open it, but it doesn't budge."
    cs "What the fuck?"
    n "After checking the deadbolt, he tries again."
    play sound sfx_door_jiggle
    pause 0.5
    n "It still doesn't move."
    cs "Oh, {i}God,{/i} don't tell me it froze over like my garage did..."
    n "He puts the flashlight in his pocket and braces himself."
    play sound sfx_door_jiggle
    n "CS pulls and yanks on the knob, until, finally, it rips open!"
    play sound sfx_house_door_open
    play sound2 sfx_house_door_slam noloop
    with hpunch
    pause 0.5
    $ mouse_visible = False
    show screen flashlight_demo
    scene cs_door
    show cs scared christmas at left
    with dissolve
    n "He falls backwards as he is met with an unwelcome sight."
    show cs worried christmas at mid_left with MoveTransition(1.0)
    n "As CS regains his footing, he can't believe what he's looking at."
    cs "What the hell? Is that {i}snow?!"
    show cs worried christmas at mid_mid_left with MoveTransition(1.0)
    n "CS sticks his finger out into the mysterious substance."
    n "It responds with a freezing confirmation."
    show cs scared christmas
    cs "Oh, my God."
    cs "How much... did it..."
    play sound sfx_house_door_slam
    scene black with Dissolve(0.25)
    hide screen flashlight_demo
    pause 0.5
    $ mouse_visible = True
    n "CS slams the door shut and runs back to deliver the news."
    pause 0.5

    $ mouse_visible = False
    show screen flashlight_demo
    scene cs_foyer_off_festive
    show anno festive at mid_left
    show aria festive at mid_right behind anno
    show mean human annoyed at mid_offscreen_right
    show tate sad festive flipped at right
    show digi sad at mid_mid_left
    show k17 disappointed at center behind digi
    show k22 disappointed at mid_mid_right
    with dissolve
    pause 0.5
    show cs scared christmas flipped at center
    show flashlight_held flipped at manual_pos(0.5, 0.7, 0.5):
        zoom 0.5
    with moveinright
    cs "{sc=1.88}Guys, the door... {w=0.5}{i}the door...!"
    aria "Calm down, CS. Catch your breath."
    show cs worried christmas flipped
    cs "{sc=1.88}The door, it's... {nw}"
    cs "{sc=1.88}The door, it's... {fast}{i}all{/i} snow!" with vpunch
    show digi shock
    show tate shock festive flipped
    show k17 shock
    anno "{i}All{/i} snow?!"
    show mean human shocked
    mean "The door?"
    k17 "It's?"
    digi "Are we trapped in here?!"
    show mean human angry
    show tate sad festive
    mean "There's only one way to find out."
    show cs disappointed christmas
    show flashlight_held
    mean "CS, take me to the roof."
    cs "To the roof?"
    mean "Yeah, let me climb up there."
    cs "It's worth a try."
    tate "Be careful, Mean."
    show mean human annoyed flipped with determination
    hide cs
    hide mean
    with moveoutright
    pause 0.5

    n "CS and Mean make their way up the ladder to the attic."
    scene cs_attic
    show hatch at manual_pos(0.3, -0.2)
    show cs disappointed christmas at mid_left
    show flashlight_held at manual_pos(0.3, 0.7, 0.5):
        zoom 0.5
    show mean human annoyed at mid_right
    with dissolve
    pause 0.5
    stop music fadeout 3.0
    music end
    mean "You good, CS?"
    cs "Yeah, I'm just a bit tired."
    cs "Anyway, there should be a hatch or something up here..."
    mean "Shine your light up."
    hide screen flashlight_demo
    show screen hatch_button
    window hide
    pause

label ce_after_hatch:
    show screen flashlight_demo
    $ mouse_visible = False
    mean "You mean like {i}that{/i} one?"
    cs "Yeah, can you pull it open?"
    play sound sfx_snowfall volume 3.0
    with vpunch
    show snow_pile at center with easeintop
    pause 1.0
    n "As Mean yanks on the hatch, it bursts open downwards!"
    n "A huge pile of snow falls onto the attic floor."
    show cs scared christmas
    pause 0.5
    cs "That is... a {i}lot{/i} of snow."
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
    mean "{i}Fuck."
    cs "What? How bad is it?"
    mean "Grab my hand, I'll pull you up."
    pause 0.5
    scene black with dissolve
    hide screen flashlight_demo
    $ mouse_visible = True
    pause 1.0

label ce_snowed_in:
    hide screen flashlight_demo
    $ mouse_visible = True
    play music winters_halloween
    music winters_halloween
    scene snowed_in
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
    pause 5.0
    if fun_value(FUN_VALUE_MUSIC):
        mean "Welp. It's winter, that's for sure."
    mean "Just look out into the distance..."
    n "CS struggles to find the horizon."
    n "All that he can see is an endless desert of snow, with only the tops of streetlights visible."
    cs "What the fuck?"
    cs "Am I dreaming?"
    pause 0.5
    n "CS picks up some snow and shoves it in his face."
    n "The blistering cold confirms that he is very much awake."
    pause 0.5
    cs "I guess not..."
    mean "I'm with ya. This doesn't even feel real."
    mean "How did this happen so fast?"
    mean "I live in {i}Canada,{/i} and it's never {i}this{/i} bad."
    pause 1.0
    cs "So, this is it? We {i}are{/i} stuck here, aren't we?"
    mean "I don't fuckin' know, man!" with vpunch
    mean "How do {i}you{/i} think we'd be able to fix this?"
    cs "A Christmas miracle, maybe..."
    cs "I don't think the others are gonna believe this."
    mean "Well, they can see it for themselves."
    mean "Let's get back inside. It's freezing out here."
    pause 0.5
    scene black with dissolve
    pause 1.0

    n "CS and Mean climb back down and meet back up with everyone."
    $ mouse_visible = False
    show screen flashlight_demo
    scene cs_living2_off_festive
    show mean human annoyed flipped at mid_offscreen_left
    show aria festive at center
    show obama festive at mid_mid_right behind digi
    show linus festive at mid_mid_left
    show cs disappointed christmas at mid_left
    show flashlight_held at manual_pos(0.3, 0.7, 0.5):
        zoom 0.5
    show tate sad festive flipped at center
    show digi sad at mid_mid_right
    show rich festive at mid_offscreen_right
    show k17 at mid_right_right
    show k22 at mid_right
    with dissolve
    pause 0.5
    stop music fadeout 3.0
    music end
    cs "Well, guys, we've got some bad news."
    cs "We might be stuck here for a while."
    k22 "Like... for a couple of hours? All night?"
    show cs worried christmas
    cs "Uhh..."
    cs "Well..."
    show cs disappointed christmas
    cs "At least for the night."
    ed "Gee, where are we all gonna sleep?"
    aria "I guess we're all gonna have to cuddle for warmth..."
    linus "There's no way we can dig our way out?"
    digi "If it's {i}that{/i} bad, wouldn't a snow plow be here soon anyways?"
    show cs worried christmas
    show tate shock festive
    show mean human shocked flipped
    show digi shock flipped
    show linus festive flipped
    show obama festive flipped
    show aria festive flipped
    show k22 flipped
    show k17 flipped
    rich "We've dealt with worse!" with hpunch
    rich "Let's get out there and {i}shovel!"
    show cs scared christmas flipped
    show flashlight_held flipped
    show tate shock festive flipped
    show mean human angry flipped
    show digi shock
    show linus festive
    show obama festive
    show aria festive
    show k22
    show k17
    mean "Everyone, shut the fuck {i}up!" with hpunch
    mean "There's, like, {nw}"
    mean "There's, like, {fast}{i}20 feet{/i} of snow out there!" with vpunch
    pause 1.0
    n "Everyone goes quiet."
    pause 1.0
    if fun_value(FUN_VALUE_RARE):
        mean "If you don't believe me, take your thumb, and shove it up your ass!"
    else:
        mean "If you want to go up to the roof and see for yourself, be my guest."
    show mean human annoyed flipped
    show tate sad festive flipped
    show digi sad
    show cs disappointed christmas flipped
    mean "I couldn't believe it either, but..."
    mean "There is fucking {i}nothing{/i} but snow."
    mean "You can barely even see the tops of the streetlights out there."
    mean "I'm from {i}Canada,{/i} and I've never seen so much snow."
    blank "I didn't even think you could {i}get{/i} that much snow..."
    cs "So... that means..."
    show cs christmas
    show flashlight_held
    cs "So... that means... {fast}we're just gonna have to wait it out!"
    show cs happy christmas
    cs "And, what better way to kill time than to play some games?"
    show cs christmas
    michael "I spy something... black!"
    nova "Is it Obama?"
    show digi disappointed
    show mean human flipped
    show cs disappointed christmas
    show tate sheepish festive flipped
    show obama angry festive
    obama "Hey!" with vpunch
    show obama festive
    show mean human annoyed flipped
    michael "No, it is not."
    show digi sad
    aria "Is it {i}everything?"
    michael "Correct!"
    cs "Okay, actually, I have something I've been wanting to play again."
    cs "I have a few board games somewhere. I just need to go grab it."
    show tate sad festive flipped
    tate "{i}Please{/i} tell me it's not chess..."
    show cs christmas
    cs "It's better than chess! I'll be back."
    show cs christmas flipped
    show flashlight_held flipped
    with determination
    hide cs
    hide flashlight_held
    with moveoutleft
    pause 0.5
    scene black with dissolve
    $ mouse_visible = True
    hide screen flashlight_demo
    pause 1.0

    play sound sfx_items_rustling volume 5.0
    n "After a bit of rummaging, CS returns to the living room."
    stop sound fadeout 0.5
    $ mouse_visible = False
    show screen flashlight_demo
    scene cs_living2_off_festive
    show mean human annoyed flipped at mid_offscreen_left
    show aria festive at center
    show obama festive at mid_mid_right behind digi
    show linus festive at mid_mid_left
    show tate sad festive flipped at center
    show digi sad at mid_mid_right
    show rich festive at mid_offscreen_right
    show k17 at mid_right_right
    show k22 at mid_right
    show cs happy christmas at mid_left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    with dissolve
    pause 0.5
    n "He holds up a blue-green box and shows it off to the crowd."
    show reversi_box at manual_pos(0.35, 0.6, 0.5) behind flashlight_held with dissolve:
        zoom 0.5
    $ collect("reversi_box")
    cs "It's {i}Reversi!"
    show digi
    show cs christmas
    show arceus happy festive at right with moveinright
    arceus "Did somebody say Reversi?"
    digi "You have an {i}actual{/i} Reversi board?"
    k17 "Isn't that the game from Windows 3.1?"
    show cs happy christmas
    show arceus festive at right
    cs "Precisely!"
    show reversi_box at manual_pos(0.35, 1.2, 0.5) with move
    pause 0.5
    play sound "minigames/reversi/place1.ogg"
    pause 0.25
    play sound "minigames/reversi/place3.ogg"
    n "CS takes off the cover and starts placing the pieces onto the coffee table."
    aria "Wait a second."
    aria "This is {i}Othello,{/i} not Reversi."
    show cs disappointed christmas
    cs "What do you mean? It says \"Reversi\" right on the box!"
    aria "Yeah, I know, but in 1971-- {nw}"
    show cs angry christmas
    cs "It's fucking Reversi, okay?" with vpunch
    cs "I just{w=0.5} want to play{w=0.5} some Reversi."
    show cs christmas
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        cs "Who will challenge me?"
    else:
        cs "Who wants to play with me?"
    show tate sheepish festive
    show arceus festive
    $ playing_reversi_again = False
    jump ce_reversi

label ce_reversi:
    stop music
    music end
    $ mouse_visible = True
    show screen flashlight_demo
    scene cs_living2_off_festive
    show mean human annoyed flipped at mid_offscreen_left
    show aria festive at center
    show obama festive at mid_mid_right behind digi
    show linus festive at mid_mid_left
    show tate sheepish festive flipped at center
    show digi sad at mid_mid_right
    show rich festive at mid_offscreen_right
    show k17 at mid_right_right
    show k22 at mid_right
    show cs happy christmas at mid_left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    show arceus festive at right

    menu:
        "Who would you like to play against?"
        "Tate (Beginner)":
            $ reversi_difficulty = ReversiAI.TATE
            minigame "play_reversigame" "ce_win_reversi" "ce_lose_reversi"
        "Digi (Easy)":
            $ reversi_difficulty = ReversiAI.DIGI
            minigame "play_reversigame" "ce_win_reversi" "ce_lose_reversi"
        "K-22 (Medium)":
            $ reversi_difficulty = ReversiAI.PAKOO
            minigame "play_reversigame" "ce_win_reversi" "ce_lose_reversi"
        "Arceus (Hard)":
            $ reversi_difficulty = ReversiAI.ARCEUS
            minigame "play_reversigame" "ce_win_reversi" "ce_lose_reversi"
        "Aria (Expert)":
            $ reversi_difficulty = ReversiAI.ARIA
            minigame "play_reversigame" "ce_win_reversi" "ce_lose_reversi"
        "I'm done playing!" if playing_reversi_again:
            jump ce_billy_time

label ce_win_reversi:
    $ mouse_visible = False
    $ persistent.reversi_game_unlocked = True
    stop music
    music end
    show screen flashlight_demo
    scene cs_living2_off_festive
    show mean human annoyed flipped at mid_offscreen_left
    show aria festive at center
    show obama festive at mid_mid_right behind digi
    show linus festive at mid_mid_left
    show tate sheepish festive flipped at center
    show digi sad at mid_mid_right
    show rich festive at mid_offscreen_right
    show k17 at mid_right_right
    show k22 at mid_right
    show cs happy christmas at mid_left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    show arceus festive at right

    $ achievement_manager.unlock("reversi")

    cs "I won!"
    cs "Now how much do {i}you{/i} think Microsoft Windows is worth?"
    linus "Isn't it like $99-- {nw}"
    cs "{i}Don't answer!" with vpunch

    if reversi_difficulty == ReversiAI.TATE:
        tate "Dang. I thought I had a chance, since it isn't chess."
        tate "Good game, CS."
    elif reversi_difficulty == ReversiAI.DIGI:
        digi "Dang, nice going, CS!"
    elif reversi_difficulty == ReversiAI.PAKOO:
        k22 "Oof! Good game, CS."
    elif reversi_difficulty == ReversiAI.ARCEUS:
        arceus "Damn, GG!"
    elif reversi_difficulty == ReversiAI.ARIA:
        aria "Excellent playing, CS!"
        $ achievement_manager.unlock("grandmaster")
    else:
        iris "Ah... who did you play against? {i}[reversi_difficulty.name]?{/i}"
        iris "They aren't here... or, a person... so, uh, good job?"
    jump ce_reversi_menu

label ce_lose_reversi:
    $ mouse_visible = False
    stop music
    music end
    show screen flashlight_demo
    scene cs_living2_off_festive
    show mean human annoyed flipped at mid_offscreen_left
    show aria festive at center
    show obama festive at mid_mid_right behind digi
    show linus festive at mid_mid_left
    show tate sheepish festive flipped at center
    show digi sad at mid_mid_right
    show rich festive at mid_offscreen_right
    show k17 at mid_right_right
    show k22 at mid_right
    show cs happy christmas at mid_left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    show arceus festive at right

    cs "Ah, dang it."

    if reversi_difficulty == ReversiAI.TATE:
        tate "Awawa-- wait, I won?"
    elif reversi_difficulty == ReversiAI.DIGI:
        digi "Heck yeah, I won!"
    elif reversi_difficulty == ReversiAI.PAKOO:
        k22 "Hell yeah, I won!"
    elif reversi_difficulty == ReversiAI.ARCEUS:
        arceus "Let's go! I won!"
    elif reversi_difficulty == ReversiAI.ARIA:
        aria "Ah, better luck next time."
    else:
        iris "Ah... who did you play against? {i}[reversi_difficulty.name]?{/i}"
        iris "They aren't here... or, a person... but you still lost."
    jump ce_reversi_menu

label ce_reversi_menu:
    $ mouse_visible = True
    dxcom reversi
    menu:
        "Play Reversi again?"
        "Yes!":
            $ playing_reversi_again = True
            $ mouse_visible = True
            jump ce_reversi
        "No!":
            jump ce_billy_time

label ce_billy_time:
    $ mouse_visible = False
    stop music
    music end
    show screen flashlight_demo
    scene cs_living2_off_festive
    show mean human annoyed flipped at mid_offscreen_left
    show aria festive at center
    show obama festive at mid_mid_right behind digi
    show linus festive at mid_mid_left
    show tate sheepish festive flipped at center
    show digi sad at mid_mid_right
    show rich festive at mid_offscreen_right
    show k17 at mid_right_right
    show k22 at mid_right
    show cs happy christmas at mid_left
    show flashlight_held at manual_pos(0.2, 0.7, 0.5):
        zoom 0.5
    show arceus festive at right
    hide screen dxcom
    with dissolve
    pause 0.5
    show billy festive at mid_right with moveinright
    billy "Wait! Everyone, hold on!"
    if fun_value(FUN_VALUE_MUSIC, confusing = True):
        cs "What? What's on the rocks, Billy?"
    else:
        cs "What? What is it, Billy?"
    play music on_the_rocks
    music on_the_rocks
    billy "The Handy Switch!"
    billy "Who got my Handy Switch for their gift?"
    show tate festive
    tate "I did! Why?"
    billy "Follow me to the basement!"
    show cs disappointed christmas
    cs "Billy, what are you doing?"
    billy "Hi, Billy Mays here, for this {i}great{/i} idea! We'll be right back!"
    hide billy with moveoutleft
    show tate sheepish festive flipped
    tate "Guess I'm following Billy, so, I'll be back, too...?"
    hide tate with moveoutleft
    pause 0.5
    scene black with dissolve
    pause 0.5

    hide screen flashlight_demo
    billy "Oh, dang it! I forgot to bring a light!"
    scene cs_hallway_off
    show billy festive at mid_left
    show tate festive flipped at center
    show tate_phone at manual_pos(0.4, 0.6, 0.5):
        xzoom -1
    $ collect("tate_phone")
    show elizabeth at right
    show screen flashlight_demo
    with dissolve
    tate "I have my phone!"
    billy "That works!"
    billy "I think the basement is down here!"
    show billy festive flipped
    show tate sheepish festive
    show tate_phone at manual_pos(0.6, 0.6, 0.5):
        xzoom 1
    eliza "Did you guys manage to get outside?"
    show tate sad festive
    tate "Mean did. He said the snow is up to the roof!"
    n "Elizabeth looks shocked."
    billy "But, good news! I have a way to possibly bring the power back!"
    show tate festive
    billy "With the Handy Switch!"
    eliza "I have no clue how {i}that's{/i} gonna work, but... good luck to you two."
    tate "Is the basement over this way?"
    eliza "Yeah, down the hall and to the left."
    tate "Thank you... {nw}"
    show tate sheepish festive
    tate "Thank you... {fast}Mika?"
    eliza "It's Elizabeth, but sure."
    hide tate
    hide billy
    hide tate_phone
    with moveoutright
    pause 0.5

    scene cs_bathroom_off
    show grace at mid_right
    show anne at right
    with dissolve
    show tate festive at center
    show tate_phone at manual_pos(0.6, 0.6, 0.5)
    show billy festive flipped at mid_left
    with moveinleft
    grace "Hey! You're that TV man!"
    anne "Grace always wanted to buy every product you ever sold."
    billy "You {i}should!{/i} Hi, Billy Mays here for the--"
    show tate sheepish festive flipped
    tate "Billy, the power?"
    billy "Oh, right."
    billy "We can talk later!"
    show tate festive with determination
    hide tate
    hide tate_phone
    hide billy
    with moveoutright
    pause 0.25
    grace "I'll be waiting, Billy!"
    n "Billy and Tate run into the basement."
    pause 0.5

    scene cs_basement
    show kitty festive at left
    show arceus festive flipped at mid_left
    with dissolve
    pause 0.5
    show tate festive flipped at right
    show tate_phone at manual_pos(0.7, 0.6, 0.5):
        xzoom -1
    with dissolve
    show tate festive flipped at center
    show tate_phone at manual_pos(0.4, 0.6, 0.5):
        xzoom -1
    with move
    show billy festive at right with dissolve
    show billy festive at mid_right with move
    pause 0.5
    show arceus worried festive flipped
    arceus "Tate? Billy?"
    kitty "What's going on?"
    billy "Fixing the power {w=0.25}with the power {w=0.25}of the Handy Switch!"
    show tate sheepish festive flipped
    tate "Don't ask."
    pause 0.5
    show tate festive flipped with determination
    hide tate
    hide tate_phone
    hide billy
    with moveoutleft
    pause 0.5

    scene breakerbox
    with dissolve
    pause 0.5
    show tate festive at mid_left
    show tate_phone at manual_pos(0.4, 0.6, 0.5)
    show billy festive flipped at mid_right
    with moveinleft
    show billy festive
    n "Finally, Billy and Tate make it down to the breaker."
    billy "Alright! All {i}you{/i} gotta do is put the switch onto the breaker!"
    show tate sheepish festive
    tate "Really? Just, like... slap it on?"
    show tate_phone at manual_pos(0.4, 0.8, 0.5) with { "master": MoveTransition(0.25) }
    billy "Yes! It's {i}that{/i} easy!"
    tate "Here goes nothin'..."
    show handy_switch at manual_pos(0.2, 0.7, 0.5) with dissolve:
        zoom 0.5
    show handy_switch at manual_pos(0.45, 0.5, 0.5):
        linear 0.125 xzoom -1
        linear 0.125 xzoom 1
    show tate sheepish festive at manual_pos(0.45, 1.0, 1.0)
    show tate_phone at manual_pos(0.45, 0.8, 0.5)
    with MoveTransition(0.25)
    play sound sfx_slap
    with hpunch
    n "Tate smacks the Handy Switch onto the breaker!"
    n "They hesitantly flip the switch!"
    play sound sfx_snd_lightswitch
    $ mouse_visible = True
    hide screen flashlight_demo
    pause 1.0
    tate "Wh-- {nw}"
    show tate shock festive
    tate "Wh-- {fast}{i}how?!" with vpunch
    billy "Like {i}magic!"
    show tate sheepish festive
    tate "How... how does this even {i}work,{/i} Billy?"
    pause 0.5
    n "Billy ponders for a moment."
    pause 3.0
    billy "I have {i}no{/i} idea!"
    show tate festive
    tate "Well, what're we waiting for?"
    tate "Let's get back upstairs and share the good news!"
    hide tate_phone
    hide handy_switch
    with dissolve
    show tate festive flipped with determination
    hide tate
    hide billy
    with moveoutleft
    pause 0.5

    scene cs_basement
    show kitty festive at left
    show arceus festive happy flipped at mid_left
    with dissolve
    pause 0.5
    show tate festive at mid_mid_right
    show billy festive flipped at right
    with moveinleft
    show tate festive flipped
    show billy festive
    arceus "Well, would you look at that?"
    kitty "How'd you guys do it?"
    billy "That's the power {w=0.25}of the {i}power!"
    hide billy with dissolve
    show tate festive at right with move
    show tate festive flipped with determination
    hide tate with dissolve
    pause 0.5

    scene cs_hallway
    show eliza at mid_right_right
    show grace at mid_right
    show anne at right
    with dissolve
    pause 0.5

    show tate festive flipped at mid_left
    show billy festive at center
    with moveinright
    grace "Yay! The power is back!"
    anne "You did it!"
    show tate festive
    show billy festive flipped
    billy "We sure did!"
    eliza "I don't know what kind of technology you could have had to fix this, but... good job!"
    grace "So, Billy, you selling any products for the holidays?"
    billy "You betcha! Meet me by my car after the party!"
    show tate festive flipped
    show billy festive
    with determination
    hide tate
    hide billy
    with moveoutleft
    pause 0.5

    scene cs_living2_festive
    show mean human at mid_offscreen_right
    show luke festive at mid_mid_right
    show copguy festive at mid_right
    show sheriff festive at mid_mid_right
    show rich festive at mid_mid_left behind cs
    show cs christmas flipped at center
    with dissolve
    pause 0.5
    show billy festive flipped at mid_offscreen_left
    show tate festive at left
    with moveinleft
    if fun_value(FUN_VALUE_RARE):
        cs "Holy power, the crap is back!"
    else:
        cs "Holy crap, the power is back!"
    sheriff "My eyes work again!"
    ed "Hooray!"
    tate "It looks like all we needed was Billy's Handy Switch!"
    show mean human angry
    show tate sheepish festive
    show cs disappointed christmas flipped
    mean "{i}Please{/i} don't say it like that, Tate."
    show mean human annoyed
    stop music fadeout 3.0
    music end
    luke "This is great and all, but isn't the house still under 20 feet of snow?"
    copguy "How are we even gonna get rid of that?"
    copguy "We would need a lot of..."
    pause 1.0
    show cs christmas
    cs "A lot of what?"
    copguy "... Never mind. I forgot what I was thinking about."
    show rich festive flipped
    rich "Didn't you two get up to the roof?"
    ed "Maybe we should all go up and check it out."
    mean "If you want, I guess."
    mean "Follow me."
    pause 0.5
    show mean human annoyed flipped
    show copguy festive flipped
    show luke festive flipped
    with determination
    hide mean
    hide cs
    hide copguy
    hide rich
    hide luke
    hide tate
    hide billy
    with moveoutright
    pause 0.5
    n "Everyone clammers up the stairs."
    pause 1.0
    sheriff "Welp."
    sheriff "I'll just... wait here."
    show sheriff festive flipped
    sheriff "Take a picture for me!" with vpunch
    scene black with dissolve
    pause 1.0

label ce_roof_moment:
    stop music fadeout 0.5
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
    pause 1.0
    k22 "So it {i}is{/i} just as bad as you said..."
    wesley "It just keeps {i}going!{/i} I can't see the end!"
    tate "What're we gonna do? We can't just {i}walk{/i} out of here!"
    copguy "I've got an idea."
    copguy "You guys, move over there..."
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
    k22 "You {i}idiot,{/i} {nw}" with vpunch
    k22 "You {i}idiot,{/i} {fast}it's an emergency code! If any airplanes see us--"
    k17 "Yeah, I know. I was just making a joke."
    k22 "Also, DaThings is a girl now."
    k17 "{i}Huh?!" with vpunch
    ed "Are there even gonna {i}be{/i} any airplanes in the sky? Just look around us!"
    ed "The whole {i}world{/i} might be stuck in mile-high snow right now!"
    wesley "Maybe we need some lights for visibility."
    cs "What's to say people are still {i}alive?{/i} Who knows how far this glacier goes?"
    digi "CS, do you {i}really{/i} think we are the last people left?"
    cs "I don't know. I just worry that this is-- {nw}"
    play sound sfx_jingle volume 0.2 loop
    n "As CS becomes more frantic, a noise is heard from afar."
    k17 "Shhh! Do you hear that?"
    cs "What? What is it?"
    play sound sfx_jingle volume 0.4 loop
    k17 "I hear jingling! Does anyone else hear jingling?"
    rich "Yeah, I do! It's coming from over there!"
    n "Richard points up in the sky."
    play sound sfx_jingle volume 0.6 loop
    k17 "Yeah! Right there! I see it!"
    aria "Is that..."
    digi "It {i}has{/i} to be Santa! I think he's really up there!"
    wesley "What?! I don't hear or see anything! Where?"
    cs "Hold on... I have an idea!"
    ed "Yeah, I can see him, clear as day!"
    ed "There's Rudolph at the end! See that red light?"
    cs "Guys! We all have to {i}believe!"
    cs "Believe in Santa and in the Christmas spirit!"
    eliza "Do you really think that will work?"
    cs "We've gotta try! Sing with me guys!"
    # TODO: Karaoke lyrics
    cs "{image=note_small1.png} Ohhh...{w=0} {image=note_small2.png}"
    if fun_value(FUN_VALUE_EPIC, confusing=True):
        play music star_spangled_banner if_changed
        music star_spangled_banner
        cs "{image=note_small1.png} Say can you see...{w=0} {image=note_small2.png}"
        tate "{i}CS!" with vpunch
        stop music
        music end
        cs "Sorry."
    cs "{image=note_small1.png} You better watch out...{w=0} {image=note_small2.png}"
    cs "{image=note_small1.png} You better not cry...{w=0} {image=note_small2.png}"
    cs "{image=note_small1.png} Better not pout, I'm telling you why...{w=0} {image=note_small2.png}"
    cs "{image=note_small1.png} Santa Claus is coming to town!{w=0} {image=note_small2.png}"
    cs "Come on guys, you gotta sing!"
    k17 "{image=note_small1.png} He's making a list...{w=0} {image=note_small2.png}"
    k17 "{image=note_small1.png} And checking it twice...{w=0} {image=note_small2.png}"
    grace "{image=note_small1.png} Gonna find out who's naughty and nice...{w=0} {image=note_small2.png}"
    # TODO: would be funny to put michael rosen noice sfx here once we figure out timings
    play sound sfx_pop_noice
    rich "{image=note_small1.png} Santa Claus is coming to town!{w=0} {image=note_small2.png}"
    tate "{image=note_small1.png} He sees you when you're sleeping...{w=0} {image=note_small2.png}"
    mean "{image=note_small1.png} He knows when you're awake...{w=0} {image=note_small2.png}"
    db "{image=note_small1.png} He knows if you've been bad or good...{w=0} {image=note_small2.png}"
    obama "{image=note_small1.png} So, you'd better be good. For goodness sake!{w=0} {image=note_small2.png}"
    cs "{image=note_small1.png} Ohhh...{w=0} {image=note_small2.png}"
    everyone "{image=note_small1.png} You better watch out...{w=0} {image=note_small2.png}"
    everyone "{image=note_small1.png} You better not cry...{w=0} {image=note_small2.png}"
    everyone "{image=note_small1.png} Better not pout, I'm telling you why...{w=0} {image=note_small2.png}"
    everyone "{image=note_small1.png} Santa Claus is coming to town!{w=0} {image=note_small2.png}"
    scene car plains night:
        zoom 2.0
    show snow1
    show snow2
    show snow3
    show snow4
    show snow5
    show snow6
    show snow_wind
    # TODO: decrustify this image. also make sure the canvas is big enough to fully contain the glow
    show sleigh
    with dissolve
    pause 0.5
    play sound sfx_jingle loop
    santa "Ho ho ho!"
    santa "The wind really started to pick up around here, didn't it, Vixen?"
    santa "Ho ho, do you all hear that? It sounds like Christmas cheer being spread on the ground below!"
    santa "Shine your light down there, Rudolph!"
    pause 1.0
    santa "Hey, wait a minute!"
    santa "Is that an SoS signal?"
    santa "Ho ho ho! Nice DaThings reference!"
    if fun_value(FUN_VALUE_RARE):
        santa "Did you hear she's a girl now?"
    pause 0.5
    santa "Okay, seriously, I should probably go down there and check it out!"
    pause 0.5

    scene cs_roof

    # putting them in the background. too many damn people here
    show obama festive flipped at manual_pos(0.4, 0.7):
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show billy festive flipped at manual_pos(0.5, 0.7):
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show michael festive at manual_pos(0.3, 0.7):
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show ed festive at manual_pos(0.7, 0.7):
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show linus festive at manual_pos(0.6, 0.7):
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show cs happy christmas at left
    with dissolve
    pause 0.5

    play sound sfx_jingle volume 0.8 loop
    cs "We did it, guys! Santa's coming to save us!"
    if fun_value(FUN_VALUE_MUSIC):
        n "Santa's sleigh begins its descent, slowing down to a crawl as the reindeer gently touch down onto the blindingly white snow."
    else:
        n "Santa's sleigh begins its descent, slowing down to a crawl as the reindeer gently touch down onto the snow."
    stop sound fadeout 0.5
    play sound2 sfx_snow_walk
    pause 0.5
    play music snow_blind
    music snow_blind
    show santa at right with moveinright
    stop sound2
    santa "Ho ho ho! Merry Christmas, everyone!"
    show grace at mid_right with { "master": easeinleft }
    dxcom tropes
    grace "{cshake}{i}SAANNNNNTAAA!!!" with hpunch
    grace "{cshake}OH MY {i}GOD!!!" with vpunch
    show k22 flipped at manual_pos(0.4, 0.9) behind cs:
        xanchor 0.5
        yanchor 1.0
        zoom 0.75
    show k17 happy flipped at manual_pos(0.5, 0.9) behind cs:
        xanchor 0.5
        yanchor 1.0
        zoom 0.75
    with moveinleft
    k17 "Haha, see, K-22? Who needs Addy's party when we can literally meet The Big Man himself?"
    show k22 happy flipped
    k22 "Heh, I guess you've got a point, there. They aren't gonna {i}believe{/i} this!"
    show cs christmas
    santa "Well, let's see, who do we have here...?"
    santa "..."
    santa "Mr. President? What are you doing here?"

    show billy festive at manual_pos(0.5, 0.7) behind obama:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show michael festive at manual_pos(0.3, 0.7) behind obama:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show ed festive at manual_pos(0.7, 0.7) behind obama:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show linus festive at manual_pos(0.6, 0.7) behind obama:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    with determination
    show obama festive flipped at manual_pos(0.6, 0.7):
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    with move
    show k22 flipped at manual_pos(0.3, 0.9):
        xanchor 0.5
        yanchor 1.0
        zoom 0.75
    show k17 flipped at manual_pos(0.4, 0.9) behind obama:
        xanchor 0.5
        yanchor 1.0
        zoom 0.75
    show obama festive flipped at mid_mid_right:
        linear 0.5 zoom 1.0
    with move
    pause 0.25

    obama "I was invited to my good friend CS' Christmas party, of course!"
    santa "Ho ho, well..."
    hide obama with moveoutright
    n "Santa looks around at the crowd."
    hide screen dxcom
    show k17
    show k22
    with determination
    hide k17
    hide k22
    with moveoutleft
    santa "Ed? Richard? Welsey?"

    show billy festive at manual_pos(0.5, 0.7) behind ed:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show michael festive at manual_pos(0.3, 0.7) behind ed:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show ed festive at manual_pos(0.7, 0.7) behind ed:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show linus festive at manual_pos(0.6, 0.7) behind ed:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show ed festive at center:
        linear 0.5 zoom 1.0
    with move
    show ed festive flipped with { "master": determination }
    ed "Yes, sir?"
    pause 0.5

    santa "Keep up the good work! Might even need some foundation repair at my workshop very soon! Ho ho!"
    show rich festive flipped at mid_mid_left with moveinleft
    show wesley festive flipped at mid_left with moveinleft
    rich "Really!?"
    ed "We appreciate the offer, Mr. Claus. Let's keep in touch!"

    hide ed
    hide rich
    hide wesley
    with moveoutright
    pause 0.5

    santa "...{w=0} And, you there! Mr. Rosen!"

    show linus festive at manual_pos(0.6, 0.7) behind michael:
        xanchor 0.5
        yanchor 1.0
        zoom 0.5
    show michael festive at center:
        linear 0.5 zoom 1.0
    with move

    santa "Don't let those YouTube Poopers get to your head! You're a {i}brilliant{/i} author."
    show cs worried christmas
    n "Santa glances at CS." with hpunch
    cs "Hey! I love his work, too!"
    show cs disappointed christmas
    cs "I don't even really {i}use{/i} Michael as a source anymore!"
    n "Michael and Santa share a laugh."
    hide michael with moveoutright
    pause 0.5

    santa "Ah, yes! Linus and Luke..."
    show linus festive at center:
        linear 0.5 zoom 1.0
    with move
    show linus festive flipped
    show luke festive flipped at mid_left with moveinleft

    santa "We might need {i}your{/i} help at the North Pole, as well. Lots of kids these days want these {i}crazy{/i} gaming PCs!"
    linus "Absolutely! Just give LTT a call!"

    hide linus
    hide luke
    with moveoutright
    pause 0.5

    show billy festive at center:
        linear 0.5 zoom 1.0
    with { "master": move }
    show billy festive flipped
    santa "There are certainly a lot of... people here that I would not expect to see."
    santa "Billy Mays, I almost forgot about... you coming back."
    billy "Don't worry, Santa! My drug days are {i}over!"
    santa "Ho ho ho! That's the spirit!"
    hide billy with moveoutright
    pause 0.5
    santa "Well, I could keep going, but I should ask..."
    santa "What {i}happened{/i} here? New York shouldn't get this much snow..."
    cs "None of us know, but we've been trapped inside the house for God knows how long."
    cs "I mean, you're Santa Claus! Surely, {i}you{/i} can fix this?"
    santa "Ho ho ho..."
    santa "I... don't believe that I can, unfortunately."
    santa "I may be Father Christmas, but my magic can't melt snow away."

    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        # i am definitely dating myself with this reference - tate
        show cs scared christmas
        santa "{i}That{/i} is the Heat Miser's domain, and I certainly don't want to end up in {i}his{/i} hot seat!"
        show cs disappointed christmas

    santa "I'm sorry, cs188."
    show copguy festive flipped at center with { "master": moveinleft }
    copguy "Now, wait a second!"
    copguy "Can't we wish for one gift? For Christmas?"
    santa "Now, {i}that,{/i} I can do!"
    santa "CS? Do you have a gift that you've always wanted?"
    cs "Hmm..."
    show copguy festive
    copguy "CS, I think I know just the thing."
    show copguy festive at mid_left behind cs with move
    pause 0.25
    play sound sfx_whisper volume 0.5
    n "Copguy whispers in CS' ear."
    pause 0.5
    show cs surprised christmas
    cs "Oh! You sure that'll work?"
    n "Copguy nods."
    show cs christmas
    show copguy festive flipped with determination
    show cs christmas at center with move
    cs "Alright, Santa, I have my wish."
    show cs christmas at mid_right with move
    pause 0.25
    play sound sfx_whisper volume 0.5
    n "CS whispers into Santa's ear."
    pause 1.0
    n "Santa's eyes widen."
    show cs christmas at center with { "master": move }
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
    pause 0.5
    santa "Alright! Stand back, everyone! This is gonna take a lot of focus!"
    n "Harnessing the power of the Christmas spirit, CS' wish begins to manifest...!"
    play sound sfx_okuubeam
    window hide
    pause 1.5
    show crotch_doctor sil_black:
        zoom 0.75
        xpos 0.7
        ypos -0.35
    with moveintop
    play sound sfx_punch
    with vpunch
    pause 1.0
    show crotch_doctor:
        zoom 0.75
        xpos 0.7
        ypos -0.35
    with dissolve
    dxcom crotch_doctor
    santa "Ta-da!"
    cs "Wow, that really {i}worked?!"
    billy "A giant bottle of Crotch Doctor?"
    copguy "Yeah! It can {i}instantly{/i} melt snow!"
    copguy "I sell this stuff door-to-door as a side-gig! It works {i}great!"
    cs "Wait, {i}you're{/i} Carguy?!" with vpunch
    copguy "How.{w=0.25}.{w=0.25}.{w=0.25} have you {i}never{/i} picked up on that?"
    billy "CS, are you sure this will work? I don't believe it!"
    cs "Don't believe me."
    cs "Just watch."
    stop music fadeout 3.0
    music end
    show crotch_doctor:
        zoom 0.75
        xpos 0.5
        ypos -0.4
        linear 15 rotate -60
    santa "Ho ho, oh, no. It's tipping towards us."
    santa "Oh, shit."
    hide screen dxcom
    scene black with Dissolve(0.25)
    play sound sfx_splash
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    n "A tsunami of car cleaner comes crashing down, washing everybody off of the roof!"
    n "As they find their bearings, the crowd watches in amazement as the waves of Crotch Doctor carry all the snow away."

    scene cs_house_night_dtree
    show cs christmas dark at mid_left
    show tate festive dark at mid_left_left
    show obama festive dark at mid_right
    show copguy festive dark flipped at mid_mid_right
    show k17 dark flipped
    show santa dark at right
    with dissolve
    show cs happy christmas dark
    cs "Woohoo! We did it! The avalanche covering the house is gone!"
    santa "Ho, ho! Well, it looks like you've saved Christmas, CS."
    santa "I need to get going now. I am slightly off-schedule."
    santa "I'm supposed to meet this girl named Belle. I heard that she's feeling pretty down."
    santa "I should also make sure my steed didn't drown in car cleaner..."
    cs "Good luck to you, Santa!"
    hide santa with moveoutleft
    show copguy festive dark
    show k17 happy dark
    k17 "CS? Did you {i}see{/i} that?!"
    show cs disappointed christmas dark
    show tate sheepish festive dark
    cs "Yeah? I was kind of {i}there,{/i} along with everyone else."
    show k17 disappointed dark
    k17 "Sorry, that was a stupid question."
    hide k17 with moveoutleft
    pause 0.5
    tate "Well, CS... I don't know how, but you did it."
    obama "I must say, that was the most fun I've ever had at a Christmas party."
    obama "Although, I should probably get back to the White House. The political circus is probably getting out of hand."
    show cs christmas dark
    cs "Thank you again for coming, Mr. President!"
    cs "I'd love to have you again next year!"
    obama "I look forward to seeing you!"
    show obama festive dark flipped
    hide obama with moveoutright
    pause 1.0
    show sheriff festive dark at right with moveinright
    sheriff "Hey, guys, what'd I miss?"
    sheriff "Where's all this snow you were all so worried about?"
    show cs disappointed christmas dark
    cs "Uhhh-- {nw}"
    play sound sfx_jingle volume 0.7 loop
    show tate shock festive dark
    show cs worried christmas dark
    with vpunch
    n "A distant jingling is heard from above!"
    show sleigh behind copguy:
        zoom 0.2
        rotate -10
    show sleigh at Move((0.45, 0.1), (1.1, -0.2), 7, repeat=False, bounce=False, xanchor="left", yanchor="top")
    santa "Ho ho ho! Merry Christmas, everyone!"
    pause 0.5
    show snow3
    show snow4
    with dissolve

    show tate sheepish festive dark
    show cs christmas dark
    stop sound fadeout 0.5
    n "As Santa flies away, snow begins to fall again."
    pause 0.5

    sheriff "Well, Copguy, we should probably get going before we get snowed in again!"
    show copguy festive dark flipped
    copguy "Yeah, you're probably right."
    show copguy festive dark
    copguy "Thanks for having us, CS."
    show cs happy christmas dark
    show copguy festive dark
    cs "Thanks to both of you for coming! Merry Christmas!"
    pause 0.5
    show cs christmas dark
    show copguy festive dark flipped
    show sheriff festive dark flipped
    with determination
    pause 0.5
    hide sheriff
    hide copguy
    with moveoutright
    pause 1.0
    copguy "Hey, look how at shiny our car is!"
    sheriff "Wow!"
    copguy "I {i}told{/i} the chief we should start using this stuff on our cruisers!"
    if d20 == 20:
        show avgn dark flipped at mid_right with moveinright
        avgn "Man, this party was {nw}"
        show cs disappointed christmas dark
        avgn "Man, this party was {fast}{i}ass!" with vpunch
        # NOTE: Digi and I thought this was so hilarious we decided to have him moonwalk. - pak
        hide avgn with moveoutleft
    pause 0.5
    scene black with dissolve
    pause 0.5

    scene cs_house_night_dtree
    show billy festive flipped dark at mid_left
    with dissolve
    pause 0.5
    show k22 disappointed dark at mid_right with { "master": moveinright }
    n "As the guests say their goodbyes and gear up to get home, K-22 approaches Billy."
    k22 "Hey, Billy. Can I talk to you for a minute?"
    billy "Sure thing! How can I help?"
    k22 "I, uhh... had a customer who wanted you to make something for them."
    show folded_paper dark at manual_pos(0.65, 0.75, 0.5) with dissolve:
        zoom 0.6
    $ collect("folded_paper")
    pause 0.5
    show folded_paper dark at manual_pos(0.25, 0.65, 0.5):
        zoom 0.6
    with MoveTransition(0.65)
    n "K-22 hands Billy a folded-up piece of paper."
    k22 "All of the instructions are on here."
    k22 "My client wants these followed word-for-word."
    play sound sfx_isaac volume 0.4
    show folded_paper dark at manual_pos(0.25, 0.65, 0.5):
        linear 0.4 zoom 0.6 rotate -75
    pause 0.5
    n "Billy opens up the paper and skims through it."
    pause 1.0
    billy "Wow..."
    billy "This is {i}great!{/i} I can get to work on this real soon!"
    hide folded_paper with dissolve
    billy "I gotta take a trip to France, first."
    billy "I need to... fix an old friend."
    show k22 dark
    k22 "Alrighty, well, thanks."
    k22 "See you later, Billy."
    billy "See ya!"
    show billy festive dark
    show k22 flipped dark
    with determination
    show billy festive dark at offscreenleft
    show k22 flipped dark at offscreenright
    with move
    n "Both parties head back to their cars."
    pause 0.5

    scene cs_bedroom1_ce
    show cs happy christmas at center
    with dissolve
    pause 0.5
    cs "Man, that was such a blast!"
    cs "I even got a free car wash!"
    show cs disappointed christmas
    cs "The house is kind of a mess, though. I'll wait until tomorrow to clean all this up."
    show cs surprised christmas
    cs "I wonder if Anno would be willing to help again..."
    show cs christmas
    cs "For now, I should probably get to streaming."
    show cs happy christmas
    cs "Those car crash compilations aren't gonna watch themselves!"
    show cs happy christmas flipped
    hide cs with { "master": moveoutleft }
    n "As CS enters his room to start his livestream, our story here comes to a close."
    show black with { "master": Dissolve(10.0) }
    n "It wasn't the Christmas that CS expected, and, certainly, not everything went according to plan."
    n "In spite of it all, with the help of his friends, it was one of the jolliest times he's ever had."
    n "Merry Christmas to all, and to all, a good night!"
    $ achievement_manager.unlock("hoh_hoh")
    $ ending_manager.mark("christmas")
    scene black with dissolve
    jump ce_epilogue

# Epilogue
label ce_epilogue:
    # attempted to fade this in better
    scene black
    show billycar1 at Move((-1.5, -1.0), (0.0, -1.25), 10, repeat=False, bounce=False, xanchor="left", yanchor="top"):
        zoom 2.5
    with dissolve
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
    # Pan over shot of the schematic for the Billy pot
    show christmas_finisher with dissolve
    pause
    if persistent.saved_christmas == False:
        $ persistent.saved_christmas = True
        call screen special_unlock("That strange die has moved to Extras?! The D20 Viewer has been unlocked!")
