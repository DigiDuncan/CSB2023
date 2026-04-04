label secret_dx:

    # re-enable pause if tate disabled it
    # TODO: add controller bindings
    if 'K_ESCAPE' not in config.keymap:
        $ config.keymap['game_menu'].append('K_ESCAPE')
    if 'mouseup_3' not in config.keymap:
        $ config.keymap['game_menu'].append('mouseup_3')
    $ renpy.clear_keymap_cache()

    scene black with dissolve
    play music space_classroom
    show digi at center with Dissolve(3)
    $ achievement_manager.unlock("broke")
    digi "Oh, hi."
    show digi sad
    digi "You, uh... {w=0.5}weren't supposed to see this."
    show digi disappointed
    digi "Jeez, in {dx}, too."
    digi "I {i}thought{/i} we would have ironed out all the bugs by now, but we're DPN, so..."
    pause 2.0
    show digi happy
    digi "How are you? You look lovely today."
    show digi sad
    digi "No, yeah, I'm sorry. I'll bring you back to the menu."
    digi "Hey, if this was a legit bug, let me know, okay?"
    digi "I want to get these all fixed up."
    hide digi with dissolve
    window hide
    pause 3.0
    return

label secret_dx2:
    scene black with dissolve
    play music space_classroom
    show pakoo at center with Dissolve(3)
    $ achievement_manager.unlock("broke")
    pakoo "Okay, that was funny, but that's {i}my{/i} joke."
    pakoo "Don't do it again."
    scene black with dissolve
    pause 1.0
    play music ten_feet_away
    jump dx_after_seek_competitors

# THESE ARE LEFT HERE AS A WAY TO REMEMBER THE OLD SECRET SCREENS

# label secret:
#     scene black with dissolve
#     play music "secret/space_classroom.ogg"
#     show digi at center with Dissolve(3)
#     digi "Oh, hi."
#     digi "You, uh... {w=0.5}weren't supposed to see this."
#     digi "We probably messed something up, for you to be here..."
#     digi "Or, you're messing with the game's files."
#     digi "You wouldn't do that, would you?"
#     digi "If this is a bug, you should report it to me."
#     digi "Otherwise..."
#     digi "Don't go poking at things you don't understand."
#     digi "Okay?"
#     hide digi with dissolve
#     window hide
#     pause 3.0
#     return

# label secret2:
#     scene black with dissolve
#     play music "secret/space_classroom.ogg"
#     show digi at center with Dissolve(3)
#     digi "Oh, again?"
#     digi "You gotta tell someone to get on with writing this game."
#     stop music
#     pakoo "Yeah, well fuck you, bitch!"
#     show pakoo at center with moveinright
#     show digi at center with vpunch
#     play sound sfx_punchalt
#     show digi at t_punchup with move
#     show pakoo at center with hpunch
#     play music "showtime.ogg" volume 0.5
#     pakoo "Thats fucking right, we finished the True Ending!"
#     pakoo "I am horribly drawn and it's 5am but hell yeah we fuckin diiiiiiiiiiiiiiidd ittttttttttt!!!!!!"
#     pakoo "Yeeaaaaaahhhhh!!! Wooooooooo!!!! Wooooooo!!! Tetttttriiissssssss!!!{nw}"
#     pause 1.0
#     show arceus
#     arceus "Yeah. Now I have to debug this shit."
#     pause
#     return

# label secret3:
#     scene black with dissolve
#     play music "secret/space_classroom.ogg"
#     show digi at center with Dissolve(3)
#     digi "Oh, again?"
#     digi "You gotta tell someone to get on with writing this game."
#     digi "I can't just stand at every broken path and wait for you."
#     digi "I'm busy doing other things."
#     digi "What things?"
#     digi "..."
#     digi "..."
#     digi "..."
#     hide digi with dissolve
#     window hide
#     pause 3.0
#     return
