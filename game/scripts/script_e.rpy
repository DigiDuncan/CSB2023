label e1:
    n "Wesley shoots Richard in the head with his gun."
    pause 3.0
    n "Welsey then takes the gun, and--{w=0.5}{nw}"
    stop music
    music end
    scene black with dissolve
    pause 1.0
    $ achievement_manager.unlock("You Broke It!")
    n "Deleting persistent{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    $ e2 = True
    n "Restarting script{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
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
    show script
    pause 1.5
    jump csbi_start

label e3_rosen:
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
    show pakoo disappointed flipped at left
    play sound sfx_glitch_in
    with pixellate # TODO: would be cool if this transition ONLY affected the character sprites
    pause 1.5
    pakoo "I'm sorry, CS."
    pakoo "It's time to delete you."
    show cs pissed flipped
    cs "NO!{w=1.0}{nw}"

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
    show script
    pause 1.5
    return
