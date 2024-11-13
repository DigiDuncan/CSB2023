screen perfect_tate_text(who, what):
    frame:
        background None
        xysize(1920, 300)
        align (0.5, 0.0)
        yoffset 100

        text what id "what":
            prefer_screen_to_id True
            font "fonts/AllerDisplay_Std_Rg_0.ttf"
            color "#000000"
            size 72
            textalign 0.5
            xalign 0.5
