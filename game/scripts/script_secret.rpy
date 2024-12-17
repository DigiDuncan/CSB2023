label secret_ce:
    scene black with dissolve
    show digi at center with Dissolve(3)
    $ achievement_manager.unlock("broke")
    digi "Oh, hey! Uh..."
    digi "Merry Christmas?"
    digi "You weren't supposed to be here."
    digi "Since you're here... I guess it means there's a bug in the game."
    digi "Damn, in {image=gui/ce_text.png}, as well."
    digi "I thought we had ironed everything out."
    digi "I guess we just only hope {image=gui/dx_text.png} will be better."
    digi "Well, you got an achivement for it, so that's something!"
    digi "Anywho, I'll stop wasting your time."
    digi "Happy holidays!"
    hide digi with dissolve
    window hide
    pause 3.0
    return
