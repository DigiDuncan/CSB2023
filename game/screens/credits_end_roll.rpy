# code almost entirely stolen from https://lemmasoft.renai.us/forums/viewtopic.php?t=22481

label credits(jump_after):
    # TODO: make this fucking thing accept a label to jump to after credits end

    image cred = Text(credits_s, text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    
    $ credits_speed = 30 #scrolling speed in seconds. adjust it once we get the real credits in

    window hide
    $ quick_menu = False
    scene black with dissolve
    
    show cred at Move((0.5, 3.1), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve
    with Pause(credits_speed + 1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    pause 5.0
    $ renpy.jump(jump_after)

init python:
    # TODO: this shit needs to read a file properly.
    # it would be ATROCIOUS to try fitting the ENTIRE real credits here LIKE THIS!
    # obviously these are just test credits rn for train route
    # if we can use a json file, maybe we could obfuscate text of things not seen yet? :eyes:
    credits = ('Writing Lead',"alleZSoyez"), ('Additional Writing', 'Meancarnavor\nArceus3251\nDigiDuncan'), ('Other Stuff','Other People'), ('Are these credits serious?', 'Absolutely the fuck {i}not.{/i}\nLet\'s get the real ones in here soon!')
    
    # CSB logo here
    credits_s = "{image=gui/credits/csbiiidx_small.png}\n"
    # TODO: do we want to do credits per route or for the entire game each time?
    # probably the latter??
    credits_s = credits_s + "\n{size=80}CSBounciness III DX: Train Route\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s = credits_s + "\n{size=60}{font=fonts/impact.ttf}" + c[0] + "\n"
        credits_s = credits_s + "{size=50}{font=fonts/Yokelvision.otf}" + c[1] + "\n"
        c1=c[0]
    credits_s = credits_s + "\n{size=60}{font=fonts/impact.ttf}Engine\n{size=50}{font=fonts/Yokelvision.otf}" + renpy.version()
    # DPN logo here
    credits_s = credits_s + "\n{image=gui/credits/dpn_logo.png}"
    
