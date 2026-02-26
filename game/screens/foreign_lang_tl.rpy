transform _reveal_tl_anim:
    on show:
        align (0.5, 0.75)
        alpha 0.00
        ease_cubic 0.25 alpha 1.00

screen show_tl():
    frame:
        at _reveal_tl_anim
        xsize 600
        yminimum 125
        $ new_line = substitutions(translate_this_line)
        text new_line align (0.5, 0.5) textalign 0.5 size 32

    timer 3.0 action Hide("show_tl",dissolve)
