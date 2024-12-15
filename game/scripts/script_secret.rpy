label secret_dx:
    scene black with dissolve
    show digi at center with Dissolve(3)
    $ achievement_manager.unlock("broke")
    digi "Oh, hi."
    digi "You, uh... {w=0.5}weren't supposed to see this."
    digi "Jeez, in {image=gui/dx_text.png}, too."
    digi "I {i}thought{/i} we would have ironed out all the bugs by now, but we're DPN, so..."
    pause 2.0
    digi "How are you? You look lovely today."
    digi "No, yeah, I'm sorry. I'll bring you back to the menu."
    digi "Hey, if this was a legit bug, let me know, okay?"
    digi "I want to get these all fixed up."
    hide digi with dissolve
    window hide
    pause 3.0
    return
