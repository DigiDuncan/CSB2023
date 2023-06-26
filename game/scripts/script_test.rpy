image ltt_bg = "/bg/ltt_bg.png"
image ltt_fg = "/bg/ltt_fg.png"

transform cs_ltt:
    zoom 0.65
    yanchor 1.0 ypos 0.8
    xanchor 0.0 xpos 0.2

transform linus_ltt:
    zoom 0.65
    yanchor 1.0 ypos 0.8
    xanchor 1.0 xpos 0.8

label test:
    scene ltt_bg
    show ltt_fg
    with determination

    show cs at cs_ltt behind ltt_fg with moveinleft
    show linus at linus_ltt behind ltt_fg with moveinright
    pause
