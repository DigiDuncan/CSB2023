transform _reveal_tl_anim:
    on show:
        align (0.5, 0.75)
        alpha 0.00
        ease_cubic 0.25 alpha 1.00

screen show_tl():

    frame:
        at _reveal_tl_anim
        xysize(600, 125)
        text translate_this_line align (0.5, 0.5) textalign 0.5 size 32
    
    timer 3.0 action Hide("show_tl",dissolve)
