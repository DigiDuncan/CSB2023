label book_iwi_box:
    play music able_sisters
    play sound2 sfx_items_rustling
    scene caboose_interior
    show mean annoyed human at offscreenright
    show cardboard_box_full at manual_pos(0.6, 0.8, 1.0):
        zoom 0.3
        block:
            linear 0.1 xoffset 5
            linear 0.1 yoffset 5
            linear 0.1 xoffset 0
            linear 0.1 yoffset 0
            repeat
    show tate at manual_pos(0.57, 0.7, 1.0) behind cardboard_box_foreground:
        zoom 0.7
        crop (0, 0, 650, 0)
    show cardboard_box_foreground at manual_pos(0.6, 0.8, 1.0):
        zoom 0.3
        block:
            linear 0.1 xoffset 5
            linear 0.1 yoffset 5
            linear 0.1 xoffset 0
            linear 0.1 yoffset 0
            repeat
    with dissolve
    $ collect("iwi_box")
    music able_sisters
    "..."

    pause 1.0

    show mean annoyed human at right with { "master": MoveTransition(1.0) }
    mean "What the fuck is all that noise?"
    pause 0.5

    stop sound2
    play sound sfx_pop_soft
    show mean shocked human
    show tate at manual_pos(0.57, 0.7, 1.0) behind cardboard_box_foreground with { "master": MoveTransition(0.15) }:
        zoom 0.7
        linear 0.15 crop (0, 0, 650, 850)
    show cardboard_box_full at manual_pos(0.6, 0.8, 1.0):
        zoom 0.3
        xoffset 0
    show cardboard_box_foreground at manual_pos(0.6, 0.8, 1.0):
        zoom 0.3
        xoffset 0
    tate "Awawa!" 
    pause 0.5
    
    show mean angry human
    mean "Tate... why are you in a box?"
    tate "It's the iwi box."
    mean "And what the {nw}"
    extend "{i}hell{/i} is an iwi box?" with vpunch
    tate "I am the iwi.{w=0.5} This is my box."
    mean "I thought you were the awawa."
    show tate srs
    tate "I am a multifaceted individual."
    show tate srs at manual_pos(0.57, 0.7, 1.0) behind cardboard_box_foreground with { "master": MoveTransition(0.15) }:
        zoom 0.7
        linear 0.15 crop (0, 0, 650, 0)
    show cardboard_box_full at manual_pos(0.6, 0.8, 1.0):
        zoom 0.3
        block:
            linear 0.1 xoffset 5
            linear 0.1 yoffset 5
            linear 0.1 xoffset 0
            linear 0.1 yoffset 0
            repeat
    show cardboard_box_foreground at manual_pos(0.6, 0.8, 1.0):
        zoom 0.3
        block:
            linear 0.1 xoffset 5
            linear 0.1 yoffset 5
            linear 0.1 xoffset 0
            linear 0.1 yoffset 0
            repeat
    show mean annoyed human
    play sound2 sfx_items_rustling
    pause 1.0
    "..."
    mean "...{fast} {i}Why{/i} do I put up with you?"
