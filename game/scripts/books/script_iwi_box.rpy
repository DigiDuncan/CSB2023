label book_iwi_box:
    
    show cardboard_box_full at manual_pos(0.4, 1.1, 1.0):
        zoom 0.5
    show tate at manual_pos(0.3, 1.5, 1.0) behind cardboard_box_foreground 
    show cardboard_box_foreground at manual_pos(0.4, 1.1, 1.0):
        zoom 0.5

    pause 2.0

    show mean annoyed human at right with moveinright
    mean "What the fuck is that noise?"

    show tate at manual_pos(0.3, 1.0, 1.0) behind cardboard_box_foreground with { "master": MoveTransition(0.25) }
    show mean shocked human
    tate "Awawa!" with vpunch
    
    show mean angry human
    mean "Tate... why are you in a box?"
    tate "It's the iwi box."
    mean "And what the {nw}"
    extend "{i}hell{/i} is an iwi box?" with vpunch
    tate "I am the iwi. This is my box."
    mean "I thought you were the awawa!"
    tate "I am a multifaceted individual."
