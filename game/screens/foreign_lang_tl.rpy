transform _reveal_tl_anim:
    on show:
        align (0.5, 0.6)
        alpha 0.00
        ease_cubic 0.25 alpha 1.00

screen show_tl():

    frame:
        at _reveal_tl_anim
        xysize(720, 175)

        text translate_this_line yanchor 0.5 textalign 0.5
    
    timer 3.0 action Hide("show_tl",dissolve)
