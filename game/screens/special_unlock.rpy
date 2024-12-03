screen special_unlock(flavor_text):

    if renpy.context_nesting_level() != 0:
        dismiss action Play("music", "bubble_tea.ogg", loop = False), Jump("start")
    else:
        dismiss action Return()


    modal True
    zorder 1000
    on "show" action Play("sound", "sfx/sfx_special_unlock.ogg")

    python:
        show_window = False
        renpy.choice_for_skipping()
    
        # only call this once, otherwise you'll accidentally create a clock
        try:
            now
        except:
            now = get_current_time()

        this_day = now.strftime("%m.%d.%Y")
        this_time = now.strftime("%H:%M:%S")

    frame:
        xysize (1920, 1080)
        background Image("gui/special_unlock.png")

        # unlock text
        frame:
            background None
            xysize (1050, 295)
            xalign 0.5
            yalign 0.55

            text flavor_text:
                font "impact.ttf"
                size 64
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5
                justify True

        # date
        frame:
            background None
            xysize (350, 65)
            xpos 550
            ypos 770
            text this_day:
                font "impact.ttf"
                size 64
                color "#888888"
                xalign 0.5

        # time
        frame:
            background None
            xysize (350, 65)
            xpos 1010
            ypos 770
            text this_time:
                font "impact.ttf"
                size 64
                color "#888888"
                xalign 0.5

    # # the entire screen acts as a button here so we can click anywhere to continue.
    # button:
    #     xysize (1920, 1080)
    #     action Return()
