# code almost entirely stolen from https://lemmasoft.renai.us/forums/viewtopic.php?t=22481

label credits:
    # TODO: make this fucking thing accept a label to jump to after credits end

    image cred = Text(credits_s, text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    
    $ credits_speed = 30 #scrolling speed in seconds

    scene black with dissolve
    window hide
    
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    # don't ask me why they want so many dissolves, maybe someone else can unfuck it
    with dissolve
    with Pause(credits_speed - 5) # apparently this HAS to be here?? thanks i hate it
    with dissolve
    with Pause(3)
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    pause 5.0
    return

init python:
    # TODO: this shit needs to read a file properly.
    # it would be ATROCIOUS to try fitting the ENTIRE real credits here LIKE THIS!
    # obviously these are just test credits rn for train route
    # if we can use a json file, maybe we could obfuscate text of things not seen yet? :eyes:
    credits = ('Writing Lead',"alleZSoyez"), ('Additional Writing', 'Meancarnavor\nArceus3251\nDigiDuncan'), ('Other stuff','Other people')
    
    # CSB logo here
    # TODO: replace it with a cleaner one
    credits_s = "{image=gui/credits/csb_iii_dx_small_rough.png}\n"
    # TODO: do we want to do credits per route or for the entire game each time?
    credits_s = credits_s + "\n{size=80}CSBounciness III DX: Train Route\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s = credits_s + "\n{size=60}{font=fonts/impact.ttf}" + c[0] + "\n"
        credits_s = credits_s + "{size=50}{font=fonts/Yokelvision.otf}" + c[1] + "\n"
        c1=c[0]
    credits_s = credits_s + "\n{size=60}{font=fonts/impact.ttf}Engine\n{size=50}{font=fonts/Yokelvision.otf}" + renpy.version()
    # DPN logo here
    # TODO: resize this later probably
    credits_s = credits_s + "\n{image=gui/credits/dpn_logo.png}"
    
