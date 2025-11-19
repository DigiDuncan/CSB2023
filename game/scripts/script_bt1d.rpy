# TODO: replace image/description for achievement for completing this route
# TODO: fill in bio info, the skeletons already exist
# TODO: sprites/beeps for everyone
# TODO: fix horse's beep
# TODO: fix RPG stats for CEO/Secretary

label bt1d_wakeup:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    play music lets_hear_my_baby volume 0.15 if_changed
    music lets_hear_my_baby
    n "CS wakes up in his bedroom after a long slumber."

    scene cs_room_2
    show cs disappointed at center
    with dissolve
    n "Exhausted from the previous days' events, he groggily makes his way towards the kitchen."
    show cs disappointed flipped at offscreenleft with MoveTransition(1.0)

    scene cs_kitchen
    show cs_kitchen_fg
    show cs disappointed behind cs_kitchen_fg
    show oreo_os at right
    $ collect("oreo_os")
    with dissolve
    cs "I'm starving! I've gotta eat something..."
    show cs disappointed at mid_right with move
    # TODO: digi needs to get a pic of the fridge open
    play sound sfx_foghorn
    show ewwie behind cs with { "master": dissolve }:
        matrixcolor TintMatrix("#00FF00")
    n "A terrible stench assaults his nostrils."
    show cs concentrate with { "master": vpunch }
    cs "Augh!"
    if fun_value(FUN_VALUE_COMMON):
        cs "Good Lord, what is happening in there?!"
    show cs disappointed
    n "CS grabs an item from the fridge, rubs his eyes, and looks at the date."
    show cs concentrate
    pause 0.1
    show cs disappointed
    pause 0.1
    show cs concentrate
    pause 0.1
    show cs disappointed
    pause 1.0

    # TODO: Show an expiry date here
    show cs worried
    cs "July?! {nw}"
    show cs scared
    extend "{i}Disgusting!" with vpunch
    show cs disappointed
    cs "Gross! I was gone for so long that all my food went bad!"
    cs "Ugh, now I gotta go to the store before I can even have breakfast..."
    hide cs with moveoutright

    scene cs_door_outside
    show cs flipped at center
    with dissolve
    n "As CS makes his way out the door, his phone buzzes."
    play sound sfx_phone_vibrate_notif
    pause 0.5
    show cs disappointed flipped

    show cs_phone with MoveTransition(0.25):
        xpos 0.35
        ypos 0.65
        alpha 0.0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.45
    pause 0.5

    phone "New game from Annorexorcist: {i}ANNO 188: Poop Romana!"
    show cs angry flipped
    cs "I don't care right now! I'm hungry and tired!"

    if fun_value(FUN_VALUE_RARE):
        play sound sfx_whoosh
        show cs_phone at manual_pos(2.0,0.5,0.5) with MoveTransition(0.5):
            linear 0.5 rotate 180
        pause 0.25
        play sound sfx_cat_crash
        with hpunch
        pause 0.5
    else:
        hide cs_phone with dissolve
        pause 0.5

    hide cs with moveoutleft

    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS clears the notification and gets in the car."
    play sound sfx_doorslam
    scene cs_car_inside
    show cs disappointed at left
    with dissolve
    play music canyon_car volume 0.2 if_changed
    music canyon
    pause 1.0
    if fun_value(FUN_VALUE_RARE):
        cs "I don't want to go Walmart anymore, but, at this point, I don't want to go to Walmart anymore."
    else:
        cs "I don't want to go Walmart anymore, but, at this point, I don't want to go to Target, either."
    show cs
    cs "You know what? I'm going to ALDI. They always have great deals!"
    n "CS speeds off to the nearest ALDI."
    play sound sfx_driving volume 0.5
    scene black with dissolve
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    pause 3.0
    jump bt1d_aldi

label bt1d_aldi:
    n "Once he arrives at ALDI, he grabs a quarter from his center console, then heads to the cart return."
    $ collect("shopping_cart_aldi")
    play sound sfx_shopping_cart
    music able_sisters
    play music able_sisters
    pause 0.5
    show aldi_outside
    show cs at manual_pos(0.5, 1.0, 1.0)
    show shopping_cart_aldi at manual_pos(0.6, 1.1, 0.5)
    with dissolve

    cs "What a smart system! Those Europeans sure know what they're doing."

    show cs at manual_pos(1.4, 1.0, 1.0)
    show shopping_cart_aldi at manual_pos(1.7, 1.1, 0.5)
    with move

    scene aldi_inside
    with dissolve

    show cs coat at manual_pos(-0.5, 1.0, 1.0)
    show shopping_cart_aldi at manual_pos(-0.3, 1.1, 0.5)
    with determination

    show cs at manual_pos(0.5, 1.0, 1.0)
    show shopping_cart_aldi at manual_pos(0.6, 1.1, 0.5)
    with move

    n "CS walks into the ALDI and is enamored by the selection and prices."
    show horse at offscreenright behind cs
    cs "Oh my gosh, there's so much to pick from, and it's all so cheap!"
    show cs happy
    cs "I'm so hungry, I could eat a horse!"

    # this bit is so silly - tate
    if fun_value(FUN_VALUE_LEGENDARY):
        python:
            horse_sprite = "horse real"
    else:
        python:
            horse_sprite = "horse"

    show expression horse_sprite at mid_right with { "master": MoveTransition(1.0) }
    n "A horse...? walks by CS."
    show cs worried
    horse "You could what?"
    show cs disappointed
    cs "Erm... nothing."
    horse "Mm-hmm."
    play sound sfx_waterphone
    pause 2.5
    show expression horse_sprite at offscreenleft with { "master": MoveTransition(1.0) }
    n "The horseperson walks away."
    pause 1.0
    cs "Anyway..."

    # TODO: need a scene change here!
    # CS buys a lot of food I don't know figure it out
    show cs at manual_pos(1.4, 1.0, 1.0)
    show shopping_cart_aldi at manual_pos(1.7, 1.1, 0.5)
    with move

    n "CS goes to check out with a cart full of food."
    cs "I can't wait to get all this home..."
    n "CS puts all this food up on the belt, and cashier checks him out with great speed!"
    cashier "That will be $88.88."
    n "Wow, that's pretty cheap for this much food!"
    cashier "That's what we do here at ALDI."
    cashier "Tell your friends; we don't have a marketing budget."

    scene black with dissolve
    jump bt1d_backhome

label bt1d_backhome:

    centered "A short drive later..."

    scene cs_room
    show cs at offscreenright
    show cs_room_fg
    with dissolve

    play sound sfx_house_door_open
    pause 3.0
    play sound sfx_house_door_close
    pause 2.0

    show cs flipped at center with moveinright
    pause 0.5

    cs "Finally, now I can feast!"
    cs "Let's get comfy!"
    show cs flipped at left with move
    show cs

    pause 0.5

    if fun_value(FUN_VALUE_COMMON):
        cs "I'm very hungry!"
        cs "Give me the snacks!"

    show car_crash behind cs at t_tv_screen_skew

    n "CS spends the next few hours planted firmly onto his couch enjoying his spoils."
    n "He puts on some car crash videos as he mindlessly snacks away."

    # TODO: he passes out, show the passage of time

    play sound2 sfx_csnore fadein 1.0
    show cs concentrate at left with dissolve
    n "Eventually, he passes out right where he's sitting..."
    stop sound2 fadeout 3.0
    stop music fadeout 3.0
    scene black with Dissolve(3.0)


    scene cs_room # TODO: need a version of his room covered in trash
    show cs disappointed at left
    show cs_room_fg
    show baby_fruit behind cs at t_tv_screen_skew
    with dissolve

    play music apple_kid if_changed
    music apple_kid
    # audio ducking
    $ renpy.music.set_volume(0.25)
    stop sound2 fadeout 1.0

    n "CS awakens surrounded by wrappers and plates."
    n "His body feels heavy and his head is full of... fruit?"
    show cs worried
    cs "What the heck {i}is{/i} this?"
    n "Some kind of baby sensory video is on the TV."
    show cs disappointed
    cs "Something must have autoplayed..."
    cs "Athena, TV off."

    # un-duck the audio
    $ renpy.music.set_volume(1.0)

    play sound sfx_fabeep
    hide baby_fruit
    pause 2.0
    show cs concentrate
    cs "Ugh..."
    show cs disappointed
    cs "What time is it?"

    show cs_phone flipped with MoveTransition(0.25):
        xpos 0.25
        ypos 0.65
        alpha 0.0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.45

    n "CS checks his phone."
    pause 0.25
    show cs scared
    cs "9AM?! I slept all night?" with vpunch

    show cs disappointed
    cs "Ugh, I feel awful..."
    cs "How much did I eat yesterday?"

    show cs disappointed at center
    show cs_phone flipped at manual_pos(0.55, 0.45)
    with { "master": move }

    n "CS stands up to assess the damage."
    # TODO: assets: piles of food
    # TODO: make him actually look around
    cs "Oreos... Cheez-Its... {nw}"
    show cs disappointed flipped
    show cs_phone at manual_pos(0.35, 0.45)
    extend "Animal crackers... {nw}"
    show cs worried at center
    show cs_phone flipped at manual_pos(0.55, 0.45)
    extend "oh, {i}jeez..."
    n "CS thinks for a moment, then is taken aback with horror!"
    show cs scared
    cs "Oh no! "  with hpunch
    extend "Wait, what if I have diabetes?!"

    n "CS pulls up the browser on his phone."
    # TODO: change scene, put him at a computer. he doesn't have the craptop anymore at this point so we need a shot of his new PC.
    # TODO: or should we just have him do it on his phone since he's already holding it?
    n "Frantically typing, he begins researching diabetes."
    cs "How much would insulin cost? It's not like I have a ton of cash..."

    # :read:
    show cs angry
    show cs_phone flipped:
        parallel:
            linear 2.0 xpos 0.525
        parallel:
            linear 2.0 ypos 0.425
    camera:
        parallel:
            linear 2.0 zoom 1.1
        parallel:
            linear 2.0 xpos -0.05
        parallel:
            linear 2.0 ypos -0.05
    pause 2.0

    # reset
    show cs scared
    show cs_phone flipped:
        parallel:
            linear 0.01 xpos 0.55
        parallel:
            linear 0.01 ypos 0.45
    camera:
        reset

    cs "{cshake}$300?!" with hpunch
    cs "This is insane! I should call Digi. They have diabetes, so maybe they can make sense of this!"

    play sound sfx_dial_digi
    pause 4.0

    show cs_phone at manual_pos(0.44, 0.4325, 0.5) with move

    pause 2.0

    scene black with dissolve
    # prevent dial tone overflow
    stop sound
    play sound2 sfx_ambience_nugget loop

    # :D
    # - tate
    if fun_value(FUN_VALUE_RARE):
        $ digi_smol = True
    else:
        $ digi_smol = False

    if digi_smol == True:
        show nugget_inside
    else:
        show nugget_main:
            zoom 0.5

    show digi thinking at center
    show cs worried at offscreenleft
    with dissolve

    digi "Put this here... and then this can be adjusted to that--"
    play sound sfx_ringtone_digi loop
    $ persistent.heard.add("sfx_ringtone_digi")
    show digi shock with shake2
    n "Digi is tinkering with their arm when their phone rings."
    show digi sad
    digi "What the heck? No one ever calls me..."

    $ collect("digi_phone")
    if digi_smol == True:
        show digi flipped
        show digi_phone with MoveTransition(0.25):
            xpos 0.55
            ypos 0.85
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 0.5 ypos 0.45
    else:
        show digi_phone flipped with MoveTransition(0.25):
            zoom 0.3
            xpos 0.35
            ypos 0.65
            alpha 0.0
            rotate -15
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 ypos 0.55
    pause 1.5
    digi "CS? What could this be about?"

    stop sound
    play sound sfx_pickup_call

    # splitscreen
    show cs_room at offscreenleft
    show cs scared phone at offscreenleft
    with determination

    show cs_room at mid_offscreen_left behind cs

    if digi_smol == True:
        show nugget_inside at mid_offscreen_right behind cs
    else:
        show nugget_main at mid_offscreen_right behind cs:
            zoom 0.5

    show cs scared phone at mid_left
    show digi at mid_right
    if digi_smol == True:
        show digi_phone:
            xpos 0.625
            ypos 0.45
            linear 0.25 rotate 10
    else:
        show digi_phone:
            zoom 0.3
            xpos 0.725
            ypos 0.55
            linear 0.25 rotate 15
    with move

    show digi shock
    cs "Digi! {nw}" with hpunch
    extend "I think I gave myself diabetes!"
    digi "What?! Huh--{nw}"
    cs "I ate a ton of food last night after I got home from our adventure and--"
    show digi
    digi "Oh, yeah! Did you ever get your pencil sharpener in the mail?"
    show cs surprised phone
    cs "No, I didn't, actual-- "
    show cs scared phone at mid_left
    show digi shock
    extend "Digi, this is {i}important!" with vpunch
    show digi disappointed
    n "Digi sets down the screwdriver they were poking their arm with."
    digi "Listen, man. You can't just {i}get{/i} diabetes."
    digi "At least, not Type 1."
    show cs disappointed phone
    cs "What do you mean? How did {i}you{/i} get it, then?"
    digi "Type 1 is genetic. You kinda have it just lingering inside you until it decides to rear its ugly head."
    digi "For me, it cropped up when I was 2."
    cs "Wait, okay, then what's the difference between Type 1 and Type 2?"
    stop music fadeout 3.0
    stop sound2 fadeout 3.0
    music end
    digi "Well..."
    jump bt1d_basketball

label bt1d_basketball:
    stop sound2
    play music basketball_music if_changed
    music basketball_music
    scene basketball_court with dissolve
    # cut to a cutaway. a machine is on the left, a basketball hoop on the right. the background
    # is like, a chalkboard or something.

    show basketball_machine at right with moveinright

    digi "Imagine your body has a basketball machine in it. You need basketballs to live."

    # round basketballs fire out of the machine, and into the hoop.

    show txt_no_d:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos -0.05

        linear 0.25 ypos 0.075
        linear 0.25 ypos 0.065

    show txt_insulin at manual_pos(0.85, 0.5, 0.5)

    show arrow_white flipped:
        xanchor 0.5 yanchor 0.5
        rotate 90
        zoom 0.3
        xpos 0.85

        block:
            ypos 0.55
            linear 0.5 ypos 0.55
            ypos 0.565
            linear 0.5 ypos 0.565
            repeat

    show basketball at manual_pos(0.975, 0.75, 0.5):
        zoom 0.25

    digi "In a normal body, your body happily makes nice, round basketballs. They go through the hoop just fine!"

    show basketball:
        block:
            parallel:
                linear 1.0 xpos 0.225
            parallel:
                linear 1.0 ypos 0.2
            parallel:
                linear 1.0 rotate 90

        block:
            linear 0 ypos 0.2
            parallel:
                linear 1.0 ypos 1.1
            parallel:
                linear 1.0 rotate 180

    play sound sfx_basketball

    # no more basketballs are made

    pause 3.0

    show txt_no_d:
        linear 0.25 ypos -0.05
    show txt_t1d:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos -0.05

        linear 0.25 ypos 0.075
        linear 0.25 ypos 0.065

    show red_x at manual_pos(0.85, 0.7, 0.5)
    digi "In my body, with Type 1 Diabetes, I don't make any basketballs."

    # a cardboard box drops into the scene. a basketball comes out the box, and flies into the hoop.
    # TODO: use different box sprite later
    show linus_box at manual_pos(0.5, 0.6, 0.5) with { "master": moveintop }
    pause 0.5
    play sound sfx_punch
    with vpunch
    digi "So I have to \"import\" some."

    show basketball

    hide txt_insulin
    hide red_x
    show txt_pump at manual_pos(0.85, 0.5, 0.5)
    show pump at manual_pos(0.85, 0.7, 0.5):
        zoom 0.5
    digi "That's what my pump is for."

    show txt_t1d:
        linear 0.25 ypos -0.05

    # cubular basketballs come out of the machine, try to fly into the hoop, and bounce right back out!

    show txt_t2d:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos -0.05

        linear 0.25 ypos 0.075
        linear 0.25 ypos 0.065
    with determination

    hide txt_pump
    hide pump
    hide linus_box
    show txt_insulint at manual_pos(0.85, 0.5, 0.5)
    show basketballnt as first at manual_pos(0.975, 0.75, 0.5):
        zoom 0.25
    with dissolve

    pause 1.0
    digi "With Type 2, your body makes cubular basketballs."

    play sound sfx_basketball
    show basketballnt as first behind txt_t2d:
        parallel:
            linear 1.0 xpos 0.225
        parallel:
            linear 1.0 ypos 0.2
        parallel:
            linear 1.0 rotate 90

        linear 0 ypos 0.2

        parallel:
            linear 1.0 xpos 0.7
        parallel:
            linear 1.0 ypos -0.1
        parallel:
            linear 1.0 rotate 180
    pause 1.0
    play sound2 sfx_spring noloop
    with vpunch

    digi "They can't go through the hoop... "
    # TODO: replace this with a hammer later
    show spoon at manual_pos(0.3, 0.5, 0.5)
    show basketballnt as second at truecenter behind spoon:
        rotate 0
    with { "master": dissolve }

    extend "so we need to hammer them back into spheres!"

    show spoon:
        linear 0.1 rotate 70
        linear 0.25 rotate 0
    play sound sfx_tf2_wrench_hit
    with vpunch
    pause 0.5

    show spoon:
        linear 0.1 rotate 70
        linear 0.25 rotate 0
    play sound sfx_tf2_wrench_hit
    hide basketballnt as second
    show basketball2 at truecenter behind spoon
    with vpunch
    pause 0.5

    show spoon:
        linear 0.1 rotate 70
        linear 0.25 rotate 0
    play sound sfx_tf2_wrench_hit
    hide basketball2
    show basketball as third at truecenter behind spoon
    with vpunch
    pause 0.5

    hide spoon with dissolve
    digi "That's what medication does!"

    show basketball as third:
        block:
            parallel:
                linear 0.5 xpos 0.225
            parallel:
                linear 0.5 ypos 0.2
            parallel:
                linear 0.5 rotate 180
            parallel:
                linear 0.5 zoom 0.25

        block:
            linear 0 ypos 0.2
            parallel:
                linear 1.0 ypos 1.1
            parallel:
                linear 1.0 rotate 360

    play sound sfx_basketball

    pause 3.0

    # cut back to the splitscreen voice call
    jump bt1d_afterbball

label bt1d_afterbball:
    # set up scene again
    play sound2 sfx_ambience_nugget loop

    if digi_smol == True:
        show nugget_inside at mid_offscreen_right behind cs
    else:
        show nugget_main at mid_offscreen_right behind cs:
            zoom 0.5

    show cs_room at mid_offscreen_left behind cs

    show cs disappointed phone at mid_left
    show digi at mid_right
    if digi_smol == True:
        show digi_phone:
            xpos 0.625
            ypos 0.45
            rotate 10
    else:
        show digi_phone:
            zoom 0.3
            xpos 0.725
            ypos 0.55
            rotate 15
    with dissolve

    cs "Okay, but you're a cyborg... why do you still have diabetes at all?"
    show digi sad
    digi "Eh, didn't feel right to cure."
    digi "If the people in real life don't have a cure, why should I?"
    show cs worried phone
    cs "Wait, what do you mean by \"real life\", aren't we currently in real--{nw}"
    show digi goober
    show cs scared phone
    digi "Donate to {a=https://tilt.fyi/UEZfMk99zW}Breakthrough T1D{/a}!" with vpunch
    show cs disappointed phone
    cs "Uh, I have done that."
    show digi happy
    digi "Good. {nw}"
    show digi
    extend "Anywho, you very likely don't have diabetes after just one night of overeating."
    show cs worried phone
    cs "But then why do I feel so {i}bad?"
    show digi sad
    digi "You probably just have a tummyache, man."
    show cs disappointed phone
    cs "Fair..."
    cs "Also, maybe you'd know, why is insulin so expensive?"
    show digi thinking
    digi "Now {i}that{/i} is because of... well... "
    show digi sad
    extend "I don't know!"
    digi "All I know is it only costs a few dollars to produce, but they mark it up a {i}ton."
    show cs scared phone
    cs "That's outrageous! Imagine if I {i}did{/i} have diabetes! I'd be bankrupt!"
    digi "That's actually the reality for a lot of people."
    show cs angry phone
    cs "We've gotta get to the bottom of this!"
    show digi thinking
    n "Digi looks at their holoband."
    show digi
    digi "Well, I don't have anything to do today. I'll be right over."
    show cs phone
    cs "Great! See you soon!"

    play sound sfx_end_call
    show cs phone at offscreenleft
    show cs_room at offscreenleft
    show nugget_inside at center

    if digi_smol == True:
        show digi flipped at center
        show digi_phone:
            xpos 0.425
            ypos 0.45
            rotate 10
    else:
        show digi at center
        show digi_phone:
            zoom 0.3
            xpos 0.475
            ypos 0.55
            rotate 15
    with move
    pause 0.5
    hide digi_phone with dissolve
    pause 0.5
    show digi

    digi "Well, I guess I have plans today after all. C'mon, Lad!"

    $ persistent.seen.add("lad")
    show lad flipped:
        xanchor 0.5
        yanchor 0.5
        xpos 0.35
        ypos 1.2

        linear 0.25 ypos 0.7
        linear 0.25 ypos 0.75

    play sound sfx_lad
    n "Lad lets out an excited jingle."

    show digi flipped at manual_pos(1.3, 0.75, 0.5)
    show lad flipped at manual_pos(1.1, 0.75, 0.5)
    with move

    stop sound2 fadeout 1.0
    # TODO: change music here
    scene black with Dissolve(1.0)
    pause 1.0
    play sound sfx_nugget

    pause 2.0

    scene cs_house
    show digi_nugget_parked at manual_pos(0.3, 0.8, 0.5)
    show digi flipped at left
    show cs disappointed flipped at right
    with dissolve
    $ collect("digi_nugget")

    n "CS meets Digi out front."
    show cs worried flipped
    cs "Wow, you got here quick!"
    digi "Yeah, man, it's a spaceship."
    cs "Why do you even have that?"

    if "iris" in persistent.seen:
        digi "Long story. You remember Iris?"
        show cs disappointed flipped
        cs "Vaguely...?"
        digi "Her."
    else:
        digi "Long story. Do you know a purple woman?"
        show cs disappointed flipped
        cs "I don't think so...?"
        digi "Don't worry about it."

    cs "Okay, then..."
    cs "So, uh, where do we even start?"
    show digi thinking flipped
    digi "I'm thinking we go to the nearest pharmacy."
    digi "Since you need a prescription for insulin, they'd have to know why insulin is so expensive."
    cs "That does make sense."
    show digi happy flipped
    digi "Hop in the Nugget!"
    show cs worried flipped
    cs "Don't I need, like, a spacesuit?"
    show digi disappointed flipped
    digi "No, dingus, we're not leaving the atmosphere."
    show cs disappointed flipped
    cs "Alright..."
    n "CS hesitantly boards the ship."
    jump bt1d_cvs

label bt1d_cvs:
    play sound2 sfx_ambience_nugget loop
    scene nugget_cockpit_back:
        zoom 0.5
    show digi at right
    show lad at manual_pos(0.7, 0.75, 0.5) behind digi
    show cs disappointed at left
    with dissolve

    cs "So, which pharmacy are we going to, exactly?"
    digi "I'm thinking CVS."
    cs "CVS-- "
    show cs scared
    extend "Hey, that's right down the road!" with hpunch
    digi "Yeah?"
    cs "Why do we need a whole spaceship for this?!"
    digi "We... don't? I needed it to get to your house. I was on Microtech."
    cs "Where?"
    digi "It's in Stanton."
    cs "Wh-- why didn't we just take my car?!"
    digi "I can't drive."
    cs "But you can pilot a {i}spaceship?!"
    digi "It's a lot easier, in my opinion. Also I don't need a license for a spaceship."
    cs "{size=-12}I really feel like you {i}should..."
    digi "Anywho, to CVS!"
    scene black with dissolve
    play sound sfx_nugget_takeoff
    stop sound2 fadeout 5.0
    pause 7.0

    # This scene should be beefed up a bit, I think.
    scene cvs_outside

    show digi_nugget_parked flipped at manual_pos(1.1, 0.8, 0.5)
    with dissolve

    n "The Nugget lands in the CVS parking lot, and the two clamber out into the daytime."
    cs "To the pharmacy department!"

    scene cvs_inside
    n "CS and Digi arrive at the pharmacy, and confront the pharmacy worker."
    cvs "Welcome to CVS, can I help you today?"
    cs "Yeah, you can tell me why insulin is so expensive!"
    cvs "Do you have a prescription to pick up?"
    cs "No! I'm just pissed!"
    digi "Sorry, excuse him. He's being a bit {nw}"
    extend "{i}too aggressive." with hpunch
    cs "... Sorry."
    digi "The question is more generic, do you know why insulin is so expensive?"
    cvs "I don't really know, the insulin companies just set the prices. We don't have control of it."
    cs "Hmmm... what insulin companies?"
    cvs "It's mostly one, 'Leedlelee.'"
    digi "Well, that's all the information we're going to get. Thank you!"
    digi "Let's go, CS."
    n "CS and Digi walk out of the CVS."
    # let the shot linger here for a moment.
    n "The CVS worker picks up their work phone."
    cvs "A cat maid and a tiny cyborg just came in here assailing me about insulin prices."
    cvs "Am I reporting this? What is there to report? I'm just telling you, I guess."
    cvs "Get back to work? Yeah, that makes sense."
    # fade out
    jump bt1d_insulin

label bt1d_insulin:
    # interior nugget
    cs "So, now what?"
    digi "We gotta go find Leedlelee, I suppose."
    n "Digi starts plugging coordinates into the console of the ship."
    digi "I think I know where to go... the question is, will we be able to talk to the CEO."
    cs "I don't know if they're just going to let two idiots with an agenda up to the penthouse."
    digi "I've done weirder."
    cs "You know, come to think of it, so have I."
    digi "Then we'll try our luck!"

    n "The Nugget lands in to the parking lot of the Leedlelee offices."
    digi "No where to go but up!"
    cs "Let's do this."

    # interior office
    receptionist "Welcome to Leedlelee, do you have an appointment?"
    cs "No, we--"
    digi "Let me handle this."
    digi "We need to speak to the CEO."
    receptionist "I can't let you up without an appointment. The CEO is a very busy man."
    digi "We understand, we only need a minute of his time."
    receptionist "Hmm. Let's see how his mood is, then."
    n "The receptionist calls up to the CEO."
    receptionist "Yes, there's two people here to see you.{w=2} No, they don't have an appointment.{w=2} Yes, sir, I understand.{w=1} One minute, sir? I'll let them know.{w=2} Thank you, sir."
    n "The receptionist hangs up the phone."
    receptionist "You have one minute. Good luck."
    cs "Thank you so much!"
    receptionist "Don't mention it."
    digi "Let's hurry!"
    n "The two scurry into the elevator."

    # in the elevator
    cs "Do you think we'll get any information out of him?"
    digi "Only one way to find out. We need to convince him we're on his side."
    cs "Are we?"
    digi "To be honest?"
    digi "No."

    # elevator ding

    # interior penthouse office
    leedle "Who are you two? I don't have all day."
    cs "We're here to ask you a quick question."
    digi "We're looking for the source of these high insulin prices."
    cs "Yeah, why do you--"
    n "Digi shoulders CS in the side." with hpunch
    digi "What my friend {i}meant{/i} to say, was we don't think it's you."
    digi "My bet? There's someone up the chain pulling {i}your{/i} chain. Am I right?"
    leedle "And why would I tell you?"
    digi "Because we can help."
    leedle "Yeah? How do I know you aren't recording this with your cyborg gobbledygook, and you're going to blackmail me!"
    cs "{size=-20}{cshake}Guilty conscience..."
    digi "Listen. I'll make you a deal."
    digi "If you tell us who's up to this, we'll (insert bribe here.)" # FIX
    leedle "Fine."
    leedle "Fine!"
    leedle "I don't know his name."
    leedle "He calls himself the CEO of Diabetes."
    n "Digi gasps."
    cs "What's wrong?"
    digi "I know him."
    cs "{i}You know him?!"
    digi "Yeah. I've fought with him before."
    digi "CS, let's go."
    digi "Thank you... what's your name?"
    leedle "(name)." # FIX
    digi "Thanks, (name)."
    n "Digi heads out back to the elevator, and CS quickly follows."

    n "The elevator ride is quiet, but the energy is tense."
    n "Even CS recognizes now isn't the time to speak."

    # getting into the nugget
    # interior nugget
    cs "So, can we talk about that?"
    digi "Yeah. I'm just annoyed."
    digi "I keep fighting this guy. Every year, he seems to crop back up."
    cs "Who is he?"
    digi "I don't know, either, man. He calls himself the CEO of Diabetes. He's a big, tough business man."
    digi "He's a weird one. One day, he'll be gunning for my destruction, the next he'll be calling me to see how I'm doing."
    cs "What does he want with you?"
    digi "Who knows, man. I'm diabetic. That's all I know."
    cs "Don't you raise money for charity, too?"
    digi "Yeah, that's probably part of it."
    cs "So, what does he do?"
    digi "Who knows, man? He makes... diabetes... worse for people? His job has always been very confusing."
    digi "But it seems his next scheme is to pay off insulin companies to not drop the price."
    cs "What now?"
    digi "If I know the CEO, I know where to find him."

    # smash cut, Digi kicks in the door to the CEO's office
    digi "CEO of Diabetes, I have come to--{w=0.5}{nw}"
    diabetes_ceo "Oh my God, will you stop kicking down my door?!"
    diabetes_ceo "Why do you keep doing this?! Just open it, it's not even locked!"
    digi "It's dramatic, I--{w=0.5}{nw}"
    diabetes_ceo "I don't care! I'm going to start invoicing you for cleaning the door!"
    digi "I-- I'm here to yell at you!"
    n "CS walks in the office behind Digi."
    cs "Me too!"
    diabetes_ceo "Who the heck are-- are you cs188?!"
    cs "Yeah."
    diabetes_ceo "Why are you wearing a cat maid outfit?!"
    cs "I'm not going into that right now."
    diabetes_ceo "OK, why are you here then?"
    cs "I researched the price of insulin, and it's egregious!"
    diabetes_ceo "Heh heh heh, yeah. I did a good job with that, didn't I?"
    cs "No! You're extorting diabetics for cash!"
    diabetes_ceo "Yeah. That's kinda what I do. And I'm damn good at it, too."
    digi "Alright, I'm not doing this song and dance again."
    digi "No bribes, no contracts."
    digi "Let's brawl."
    diabetes_ceo "Heh! You think you can take me?"
    diabetes_ceo "Alright, bet."
    diabetes_ceo "You win, and I'll even call off the price hike."
    diabetes_ceo "But if you lose..."
    n "A button rises like a piston on his desk."
    diabetes_ceo "I release {i}Type 4 Diabetes{/i} on to the masses!"
    digi "You're on."
    cs "Y-{w=0.1}Yeah! You're on!"

    # black knife starts playing idk
    jump rpg_diabetes_1

label bt1d_after_fight_1:
    n "The CEO is panting on the floor."
    diabetes_ceo "Heh... heh... you've gotten good, you little rat."
    diabetes_ceo "But I'm not bested yet!"
    n "The CEO pushes a different button on his desk, and intercoms somebody."
    diabetes_ceo "Secretary?"
    diabetes_secretary "Yes, Mr. CEO?"
    diabetes_ceo "I need you up here."
    digi "You have a secretary?"
    diabetes_ceo "Do now."
    n "The door opens, and the Secretary of Diabetes walks through the door."
    n "The secretary glances at the situation around her."
    diabetes_secretary "Kick their asses, sir?"
    diabetes_ceo "Kick their asses."

    # rpg battle 2 - secretary
    jump rpg_diabetes_2

label bt1d_after_fight_2:
    # TODO: Beef up this dialouge?
    diabetes_ceo "Ready for Round 2?"

    # rpg battle 3 - ceo + secretary
    jump rpg_diabetes_3

label bt1d_ending:
    diabetes_ceo "Fine. You did well."
    diabetes_secretary "These ones are good, sir."
    diabetes_ceo "I'll call off the price hike."
    diabetes_secretary "You're calling it off?"
    diabetes_ceo "That was the deal."
    diabetes_ceo "But I never said how long that will last..."
    diabetes_ceo "Heh."
    diabetes_ceo "Heh heh."
    diabetes_ceo "Heh heh heh heh heh!"
    digi "Let's get out of here, CS."
    cs "Yeah, this guy is nuts."

    # interior nugget
    n "Back on the Nugget, the two sit in silence for a bit, Digi petting Lad for comfort."
    n "After a while, the silence breaks."
    digi "Well, we did it."
    cs "Yeah, we did. But how long until he tries something again?"
    digi "Pffft, not long. That's kinda his thing."
    cs "Then what's the point? Does this fight ever end?"
    digi "Yeah, one day. Not sure how long it'll take, but eventually."
    digi "That's why I raise money for Breakthrough T1D all the time."
    digi "Once we have a cure, there's not much more he can do."
    cs "Right. Well, good luck on the good fight."
    digi "Thanks, man."
    cs "I didn't realize this is what you do all the time!"
    digi "I do a lot of things people don't realize."

    # fade to exterior CS' house - night
    digi "Well, this is your stop. Have a nice night, CS!"
    cs "Thanks, Digi, glad I could help!"

    # TODO: this is barely an ending

    jump secret_dx
