transform _t_billy:
    align (0.5, 0.0)
    yoffset 100

style perfect is empty
style perfect_frame is empty

# Perfect Billy
screen perfect_billy_text(who, what):
    style_prefix "perfect"
    frame:
        at _t_billy
        xysize(1920, 540)
        text what id "what":
            font "fonts/Friz-Quadrata-Bold-Italic.ttf"
            size 72
            textalign 0.5
            xalign 0.5
            outlines [(absolute(10), "#ffff00", absolute(0), absolute(0)), (absolute(5), "#0003bd", absolute(0), absolute(0))]