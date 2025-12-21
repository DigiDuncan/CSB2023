label test:
    scene washington_road day
    show cs at left
    show arceus at right
    menu:
        "Menu test?"
        "Yes"  (type = "good"):
            scene washington_road dusk
            show arceus dusk flipped at right
            show cs dusk at left
            with dissolve
            arceus "This is a dusk test"
            scene washington_road
            show arceus dark at right
            show cs dark at left
            with dissolve
            arceus "This is a dark test"
            $ renpy.full_restart()
        "No"  (type = "bad"):
            $ renpy.full_restart()
        "True"  (type = "true"):
            $ renpy.full_restart()
        "Reversi!":
            menu:
                "Which difficulty would you like?"
                "Tate (Beginner)":
                    $ reversi_difficulty = ReversiAI.TATE
                    jump play_reversigame
                "Digi (Easy)":
                    $ reversi_difficulty = ReversiAI.DIGI
                    jump play_reversigame
                "K-22 (Medium)":
                    $ reversi_difficulty = ReversiAI.PAKOO
                    jump play_reversigame
                "Arceus (Hard)":
                    $ reversi_difficulty = ReversiAI.ARCEUS
                    jump play_reversigame
                "Aria (Expert)":
                    $ reversi_difficulty = ReversiAI.ARIA
                    jump play_reversigame
        "New Menu Option Because Arc is Lazy":
            menu:
                "RPG Using Screen":
                    jump play_screenrpnggame
                "Matrix Test":
                    stop music
                    scene cs_room
                    show washington_road:
                        zoom 0.5
                        perspective True
                        matrixanchor (0, 0)
                        matrixtransform RotateMatrix(0, 0, 0) * RotateMatrix(0, -20, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(32, 40, 0)
        "New cool thing OwO"  (type = "dx"):
            menu:
                "Layered Image Scene Testing":
                    menu:
                        "Train Boss Test":
                            stop music
                            scene amtrak_dining_car
                            show cs scared at left
                            show mean scared flipped at right
                            pause 2.0
                            show train_boss_final with easeintop
                            pakoo "This is the train boss."
                            $ renpy.full_restart()
                        "Flying Train Test":
                            stop music
                            show flying_train_final at right with easeinright
                            pause 1.0
                            show flying_train_final at left with ease          
                            pakoo "This is the flying train layered image."
                            hide flying_train_final with easeoutleft
                            pause
                            $ renpy.full_restart()
                        "Driving Test":
                            stop music
                            scene car plains
                            show screen carchasegame
                            show car_chase2
                            show cultist_fire1
                            pause
                            label cultist_firing:
                                if reloading == 0:
                                    show screen reloadbutton
                                    $ reloading = 6
                                if hitpoints == 0:
                                    hide screen carchasegame
                                    scene black
                                    play sound sfx_car_crash
                                    pause
                                    $ renpy.full_restart()
                                $ hitpoints -= 1
                                $ reloading -= 1
                                show cultist_fire at cultist_fire
                            pause
                            $ renpy.full_restart()
                "Screen Test":
                    show screen warning("The following scene is a test.\nIt may be teste.", "Warnings: developer cruft, bad puns", "start")
                    pause
                    $ renpy.full_restart()
                "EX Test":
                    stop music
                    show copguy_ex at left
                    pakoo "This is Copguy EX."
                    show tate_ex at mid_right
                    pakoo "This is Tate EX."
                    pakoo "Does this work? Idk"
                    $ renpy.full_restart()
                "Perfect Billy Test":
                    perfect_billy "I'm Perfect Billy Mays!"
                    cs "woah that's crazy"
                    $ renpy.full_restart()
                "Music Test":
                    # play music4 ten_feet_away_4 if_changed volume 0.1
                    # play music3 ten_feet_away_3 if_changed volume 0.1
                    # play music2 ten_feet_away_2 if_changed volume 0.1
                    play music "audio/10_feet_away_1.ogg"
                    # $ renpy.music.set_pause(True, "music4")
                    # $ renpy.music.set_pause(True, "music3")
                    # $ renpy.music.set_pause(True, "music2")
                    pakoo "test 1"
                    pause
                    play music2 [ "<sync music>audio/10_feet_away_2.ogg", "audio/10_feet_away_2.ogg" ]
                    # $ renpy.music.set_pause(True, "music4")
                    # $ renpy.music.set_pause(True, "music3")
                    # $ renpy.music.set_pause(False, "music2")
                    pakoo "test 2"
                    pause
                    play music3 [ "<sync music>audio/10_feet_away_3.ogg", "audio/10_feet_away_3.ogg" ]
                    # $ renpy.music.set_pause(True, "music4")
                    # $ renpy.music.set_pause(False, "music3")
                    pakoo "test 3"
                    pause
                    play music4 [ "<sync music>audio/10_feet_away_4.ogg", "audio/10_feet_away_4.ogg" ]
                    # $ renpy.music.set_pause(False, "music4")
                    pakoo "test 4"
                    pause
                    $ renpy.full_restart()
                "Multiple Character Dialogue Test":
                    digi "Two people talking?" (multiple=2)
                    pakoo "An absurd idea!" (multiple=2)
                    pause
                    digi "{i}Three{/i} people talking?!" (multiple=3)
                    pakoo "I can't believe it!" (multiple=3)
                    arceus "What a deal!" (multiple=3)
                    pause
                    $ renpy.full_restart()
                "Light Gun Test":
                    stop music
                    show screen lightgungame
                    pause
                    $ renpy.full_restart()
                "Loop Test":
                    jump looptest

label lightgamehit:
    if reloading == 0:
        show screen reloadbutton
        $ reloading = 6
    if hitpoints == 0:
        hide screen lightgungame
        show billy at center with moveinright
        billy "You won!"
        pause
        $ renpy.full_restart()
    $ hitpoints -= 1
    $ reloading -= 1
    pause
    $ renpy.full_restart()

transform t_loop:
    xanchor 1.0
    xpos 1.0
    linear 3.0 xpos 3.0
    linear 0.0 xpos 1.0
    repeat

label looptest:
    show looptest behind cs at t_loop
    pause