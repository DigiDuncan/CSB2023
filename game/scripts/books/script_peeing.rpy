label book_peeing:
    stop music fadeout 3.0
    music end
    scene cs_bathroom
    play music hotel_disbelief if_changed
    music hotel_disbelief
    pause 1.0
    play sound sfx_toilet_flush
    pause 1.0
    scene cs_bathroom_open
    play sound sfx_house_door_open
    show cs at manual_pos(0.4, 0.4):
        zoom 0.5
    show cs_bathroom_open_fg
    pause 0.5
    show cs at manual_pos(0.4, 0.4):
        linear 0.5 zoom 1.0 pos (0.34, 0.2)
    pause 0.5
    scene cs_bathroom
    play sound sfx_house_door_close
    show cs
    n "CS comes out of the bathroom feeling refreshed."
    show cs happy
    cs "My pee was clear today! That must mean I'm really healthy!"
    show mean human angry at right with moveinright
    show cs worried
    mean "Actually, that's not very healthy."
    show cs disappointed
    mean "That means you drank too much water, and you are overhydrated."
    cs "Man, what a bitch of a day! I got an ass."
    stop music fadeout 3.0
    music end
    return
