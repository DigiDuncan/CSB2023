label test:
    show arceus festive dusk flipped at right
    show cs dusk at left
    with dissolve
    arceus "This is a dusk test"
    show arceus festive dark at right
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
        "Multiple Character Dialogue Test":
            digi "Two people talking?" (multiple=2)
            pakoo "An absurd idea!" (multiple=2)
            pause
            digi "{i}Three{/i} people talking?!" (multiple=3)
            pakoo "I can't believe it!" (multiple=3)
            arceus "What a deal!" (multiple=3)
            pause
            $ renpy.full_restart()
