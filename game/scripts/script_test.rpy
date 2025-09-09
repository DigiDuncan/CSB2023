label test:
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
    menu:
        "Menu test?"
        "Yes"  (type = "good"):
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
            jump play_newrpggame
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
                            show car_chase11
                            show car_chase21
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

label lightgamehit:
    show pot at barrel_hit
    pause
    $ renpy.full_restart()