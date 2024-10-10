transform _t_perfect_tate:
    align (0.5, 0.0)
    yoffset 100

style perfect is empty
style perfect_frame is empty

# Perfect Tate
screen perfect_tate_text(who, what):
    style_prefix "perfect"
    frame:
        at _t_perfect_tate
        xysize(1920, 540)
        text what id "what":
            font "fonts/AllerDisplay_Std_Rg_0.ttf"
            size 72
            textalign 0.5
            xalign 0.5
