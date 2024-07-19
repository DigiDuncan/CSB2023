label e1:
    n "Wesley shoots Richard in the head with his gun."
    pause 3.0
    n "Welsey, then takes the gun, and--{w=0.5}{nw}"
    stop music
    music end
    scene black with dissolve
    pause 1.0
    n "Deleting persistent{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    $ e2 = True
    n "Restarting script{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
    show script
    pause 1.5
    jump csbi_start

label e2:
    sticky "Go to Rosen's."
    cs "Eh, maybe tomorrow."
    pause 1.0
    cs "Actually, maybe I should."
    scene black with fade
    stop music fadeout 3.0
    music end
    n "CS takes off and heads to Rosen's house."
    jump csbi_rosen_house

label e3:
    window hide
    scene cs_room
    show cs angry
    show oldgame
    with fade
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
    michael "While he was walking, he found another version of himself."
    stop music fadeout 3.0
    music end
    michael "This version of himself was real."
    michael "This man, the adventurer, was not."
    michael "He never was."
    michael "He needed to be removed if he found out he was fake."
    michael "So that's when--{nw}"
    show pakoo disappointed at center with moveinright
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
    show csgod at offscreenright
    show michael at left
    with fade
    show cs flipped angry at right with moveinright
    cs "Tell me the rest of the story!"
    michael "What?"
    cs "Damn it, don't fuck around with me!"
    cs "It's not true!"
    hide michael with moveoutleft
    show pakoo disappointed flipped at left with moveinleft
    pakoo "I'm sorry, CS."
    pakoo "It's time to delete you."
    cs "NO!{w=1.0}{nw}"
    show csgod at left with move
    show csgod with hpunch
    play sound sfx_punch
    show csgod at offscreenright
    show csgod at left with move
    show csgod with hpunch
    play sound sfx_punch
    show csgod at offscreenright
    show csgod at left with move
    show csgod with hpunch
    play sound sfx_punch
    hide csgod with dissolve
    n "Pakoo sighs."
    pakoo "Let's finish this."
    $ renpy.movie_cutscene("movies/error_cutscene.webm")
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
    with fade
    pakoo "Goodbye."
    hide cs with dissolve
    pause 5.0
    pakoo "Alright, let's restart the script."
    return
