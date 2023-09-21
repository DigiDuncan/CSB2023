label secret:
    scene black with fade
    play music "<loop 0>secret/space_classroom.mp3"
    show digi at center with Dissolve(3)
    digi "Oh, again?"
    digi "You gotta tell someone to get on with writing this game."
    digi "I can't just stand at every broken path and wait for you."
    digi "I'm busy doing other things."
    digi "What things?"
    digi "..."
    digi "..."
    digi "..."
    hide digi with dissolve
    window hide
    pause 3.0
    return

label secret2:
    scene black with fade
    play music "<loop 0>secret/space_classroom.mp3"
    show digi at center with Dissolve(3)
    digi "Oh, again?"
    digi "You gotta tell someone to get on with writing this game."
    stop music
    pakoo "Yeah well fuck you bitch!"
    show pakoo at center with moveinright
    show digi at center with vpunch
    play sound "alt_punch.ogg"
    show digi at t_punchup with move
    show pakoo at center with hpunch
    play music "<loop 0>showtime.mp3" volume 0.5
    pakoo "Thats fucking right, we finished the True Ending!"
    pakoo "I am horribly drawn and it's 5am but hell yeah we fuckin diiiiiiiiiiiiiiidd ittttttttttt!!!!!!"
    pakoo "Yeeaaaaaahhhhh!!! Wooooooooo!!!! Wooooooo!!! Tetttttriiissssssss!!!{nw}"
    pause 1.0
    show arceus
    arceus "Yeah. Now I have to debug this shit."
    pause
    return
  