label e1:
    n "Wesley shoots Richard in the head with his gun."
    pause 3.0
    n "Welsey then takes the gun, and--{w=0.5}{nw}"
    stop music
    music end
    scene black with dissolve
    pause 1.0
    $ achievement_manager.unlock("broke")
    n "Deleting persistent{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    $ e2 = True
    n "Restarting script{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    window hide
    show script
    pause 1.5
    jump csbi_start

label e2:
    sticky "Go to Rosen's."
    cs "Eh, maybe tomorrow."
    pause 2.0
    cs "Actually... maybe I should."
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS jumps in the car and heads towards Rosen's house."
    jump csbi_rosen_house

label e3:
    window hide
    scene cs_room
    show cs angry
    show oldgame
    with dissolve
    pause 3.0
    play sound sfx_page volume 5
    hide oldgame
    with moveoutright
    cs "I know what's going on now."
    cs "Fuck this."
    n "Jumping to rosen_house...{w=1.25}{nw}"
    jump csbi_rosen_house

label e2_rosen:
    michael "He started to get up, and walk around."
    show cs disappointed flipped
    michael "While he was walking, he found another version of himself."
    stop music fadeout 3.0
    music end
    michael "{i}This{/i} version of himself was real."
    michael "{i}This{/i} man, the adventurer, was {i}not."
    michael "He never was."
    michael "He needed to be removed if he ever found out he was fake."
    michael "So that's when--{w=0.5}{nw}"
    show pakoo at offscreenright with determination
    show pakoo disappointed at center with MoveTransition(0.25)
    show cs scared flipped
    pakoo "STOP{nw}"
    scene black
    pause 1.0
    n "Deleting persistent{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    $ e3 = True
    n "Resetting script{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    window hide
    show script
    pause 1.5
    jump csbi_start

label e3_rosen:
    # TODO: is this a real song? does it need to be jukeboxed? is it part of L.A. By Night? should i just file it under there????
    play music night
    scene rosen_abode
    show michael at left
    with dissolve
    show cs flipped angry at right with moveinright
    pause 1.0
    cs "Tell me the rest of the story!"
    michael "What?"
    cs "Damn it, don't fuck around with me!"
    cs "It's not true!"

    hide michael
    show expression DynamicDisplayable(Pixellated.pixellated, widget='pakoo disappointed flipped', delay=0.5, steps=8) at left
    play sound sfx_glitch_in
    with dissolve

    pause 1.5
    pakoo "I'm sorry, CS."
    pakoo "It's time to delete you."
    show cs pissed flipped
    cs "{cshake}NO!{w=1.0}{nw}"

    show csgod at right:
        alpha 0
    show csgod at left with move:
        linear 0.5 alpha 1.0
    play sound sfx_punch
    with hpunch

    show csgod at right:
        alpha 0
    show csgod at left with move:
        linear 0.5 alpha 1.0
    play sound sfx_punch
    with hpunch

    show csgod at right:
        alpha 0
    show csgod at left with move:
        linear 0.5 alpha 1.0
    play sound sfx_punch
    with hpunch

    hide csgod with dissolve
    pause 1.0

    n "Pakoo shakes his head and sighs."
    pakoo "Let's finish this."
    $ renpy.movie_cutscene(error_cutscene)
    jump rpg_error

label error:
    if fun_value(1):
        show black
        play sound sfx_gul
        pause 1.0
        return
    $ e1 = True
    jump csbi_start

label after_error_fight:
    scene rosen_abode
    show pakoo disappointed flipped at left
    show cs angry flipped at right
    with dissolve
    pakoo "Goodbye."
    show cs scared flipped
    hide cs with Dissolve(1.0)
    pause 5.0
    pakoo "Alright, let's restart the script."
    window hide
    show script
    pause 1.5
    $ ending_manager.mark("error")
    return

label error_voodoo:
    play music morning_highway loop volume 0.4 if_changed
    music morning_highway
    scene gpuaisle
    show cs at mid_left
    cs "Woah, is that a Voodoo card?"
    cs "I haven't seen one of those in forever!"
    cs "I know this isn't what we need, but Linus will probably find this cool."
    hide cs with moveoutright
    n "CS heads to the checkout."
    scene cashzone 
    show cashier at center
    show cashzone_foreground
    with dissolve
    show cs at mid_left with moveinleft
    cashier "That'll be..."
    n "The cashier flips the box around, searching for a bar code."
    cashier "Heh, they always put the bar code in weird places..."
    cashier "Lemme just, look up the item and maybe I can find a SKU."
    n "After a bit of searching, the cashier gives a confused look before looking back up at CS."
    cashier "I can't find this item in the store, sorry about that."
    cs "Is there anyway I can still buy this?"
    cashier "Uhh..."
    cashier "I guess I could give you like... $150 for it?"
    cs "Sure, that works for me."
    hide cs with moveoutright
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "CS heads back to LTT."
    scene loffice
    show linus at center
    with dissolve
    n "CS meets Linus in his office."
    play music creative_exercise loop volume 0.3 if_changed
    music creative_exercise
    show cs at left with moveinleft
    cs "Hey Linus! Guess what I found!"
    linus "Whaddya find?"
    n "CS pulls out the box."
    cs "I found a Voodoo graphics card!"
    linus "What the hell?"
    linus "First of all, where did you find that?"
    linus "Second of all, we can't use that for the video!"
    cs "I understand, but it was just lying there on a shelf at the Microcenter!"
    n "Linus takes the box."
    linus "Did you just steal it?"
    cs "No no, it was like 100 bucks or something."
    n "As Linus slowly inspects the box art, his eyes start to widen."
    linus "CS! This is a Voodoo 5 6000!"
    cs "Uhm, is that... rare?"
    linus "Rare?"
    linus "This isn't rare, this was never even released to the public!"
    cs "What??"
    linus "That's what I'm saying!"
    linus "Okay. I need to calm down."
    linus "I haven't even opened the box yet."
    linus "It could just be a bunch of rocks."
    linus "Let's go open this, right now."
    hide linus
    hide cs
    with moveoutright
    scene black with dissolve
    pause 1.0
    scene ltt_bg
    show ltt_fg
    with dissolve
    show cs at t_cs_ltt behind ltt_fg with moveinleft
    show linus at t_linus_ltt behind ltt_fg with moveinright
    linus "Okay, let's make sure this is the legit."
    linus "CS, why don't you open it? I don't want to let my butterfingers possibly ruin a never before seen GPU."
    cs "If you are so sure..."
    n "CS rips off all the plastic shielding, and carefully opens the box."
    linus "Well good news, there is a graphics card in there."
    linus "I should do some tests and research this a bit before we actually make a video."
    linus "You're off work for today. Tomorrow, I, The Great Linus Sebastian..."
    linus "will let you know what the plan is."
    cs "Alrighty, See you later Linus!"
    stop music fadeout 3.0
    music end
    hide cs with moveoutright
    scene black with dissolve
    n "As morning comes, CS heads back to LTT to check out the video."
    scene inside_ltt
    show linus at mid_right
    with dissolve
    show cs at mid_left with moveinleft
    cs "Hey Linus!"
    linus "Hey CS! Good news!"
    linus "Looks like the GPU is the real!"
    cs "Woohoo! We found a rare graphics card!"
    linus "Yep, all we need to do now is make a video showcasing our rare find!"
    linus "I need to go to the bathroom real quick, so get yourself prepared for the shoot."
    cs "Got it."
    hide linus with moveoutright
    n "As CS wakes for Linus to finish, a few people yelling can be heard from outside."
    cs "Weird, I wonder what's going on outside."
    cs "Maybe I should go check it out."
    hide cs with moveoutright
    scene black with dissolve
    n "CS approaches the door to the front."
    n "He peers out the window, but doesn't spot anyone by the door."
    cs "Huh. Maybe they left?"
    n "CS opens the door."
    n "All of a sudden, someone grabs his arm!"
    cs "Hey!"
    return

    # Initiate RPG Battle

label error_lowbudget:
    scene alley with dissolve
    play music Lowbudget_song loop volume 0.4 if_changed
    music Lowbudget_song
    show cs at center
    with moveinleft
    cs "Arceus?"
    cs "Where did you go?"
    cs "Hello?"
    cs "I could've sworn he wanted to meet outside..."
    cs "I wonder what I should do..."
    menu:
        "Wait for Arceus":
            jump error_wait
        "Look around":
            jump error_search

label error_wait:
    cs "I guess I can wait a little bit, maybe he had to do something really quickly."
    pause 5.0
    arceus "Hey, there you are!"
    cs "Hey Arc! Where'd you go?"
    arceus "I was upstairs, I didn't know you were outside."
    cs "Sorry, I just assumed this is where you wanted to go."
    arceus "Anyways, the cops are searching for us, Pakoo is here, and Linus wants to train you downstairs."
    arecus "Let's go catch up with them."
    cs "Oh-hkay."
    jump friend_training

label error_search:
    #Point and click thing here
    cs "Maybe Arc is hiding somewhere."

    n "CS lifts up the manhole cover."
    cs "Why would he go down here? That's dumb."
    n "Before CS can cover the sewer again, he slips and falls through the hole!"
    cs "Aieeeeee!!"
    
    n "CS looks inside the trashcan."
    cs "Nah, that's silly. Why would he be in--{nw}{w=1.5}"
    n "All of a sudden, CS gets sucked into the trashcan!"
    cs "Ahhhhhh!!"