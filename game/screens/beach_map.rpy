screen beach_overworld_map(
    current_time = "dawn", 
    current_location = (600,600,"Somewhere"), 
    left_hand = "cs",
    right_hand = "arc",
    jump_points = [ (500,500,"Somewhere Else", "secret_dx") ] 
    ):

    modal True

    default current_time = current_time
    default current_location = current_location
    default left_hand = left_hand
    default right_hand = right_hand
    default jump_points = jump_points
    default location_tooltip = ""

    on "show" action [
        Play("sound", "audio/sfx/sfx_isaac.ogg"),
    ]

    # Time of day indicator
    python:
        if current_time == "dawn":
            time_indicator = Image("gui/beach_map/dawn.png")
        elif current_time == "day":
            time_indicator = Image("gui/beach_map/day.png")
        elif current_time == "noon":
            time_indicator = Image("gui/beach_map/noon.png")
        elif current_time == "dusk":
            time_indicator = Image("gui/beach_map/dusk.png")
        elif current_time == "night":
            time_indicator = Image("gui/beach_map/night.png")

    add time_indicator:
        xalign 1.0 yalign 82

    # This holds the map.
    frame:
        background None
        
        at transform:
            xalign 0.5 yalign 5.0
            zoom 0.8

            parallel:
                linear 0.5 yalign 1.0
            parallel:
                linear 0.5 zoom 1.0

        # Hand handler... hand-ler? :kek:
        $ left_hand_img = "gui/beach_map/hand_"+left_hand+".png"
        $ right_hand_img = "gui/beach_map/hand_"+right_hand+".png"

        # Actually draw map and hands
        add "gui/beach_map/map.png":
            xalign 0.5 yalign 0.5
        add left_hand_img:
            xalign 0 yalign 1.0
            xoffset 64 yoffset 6
            zoom 0.75
        add right_hand_img:
            xalign 1.0 yalign 1.0
            xoffset -64 yoffset 6
            zoom 0.75
            xzoom -1

    # Current location marker
    frame:
        background None
        at transform:
            alpha 0
            xanchor 0.5 yanchor 1.0
            xpos current_location[0] ypos current_location[1]

            parallel:
                linear 1.0 alpha 1.0
            parallel:
                block:
                    linear 0.5 yoffset -10
                    linear 0.5 yoffset 0
                    repeat

        vbox:
            text current_location[2]:
                xalign 0.5
                text_align 0.5
                outlines [(5, "#000000", absolute(0), absolute(0))]
                
            imagebutton:
                xalign 0.5 yalign 1.0

                idle "gui/beach_map/map_marker_current.png"
                hover "selectable:gui/beach_map/map_marker_current.png"

                hovered [
                    Play("sound", "audio/sfx/sfx_select.ogg"),
                    SetScreenVariable("location_tooltip", current_location[2])
                ]
                unhovered SetScreenVariable("location_tooltip", "")
                action [
                    Notify( _("You are here!") ),
                    Play("sound", "audio/sfx/sfx_valid.ogg")
                ]

    # Add jump points here
    for jp in jump_points:
        frame:
            background None

            at transform:
                alpha 0
                xanchor 0.5 yanchor 1.0
                xpos jp[0] ypos jp[1]
                linear 1.0 alpha 1.0

            vbox:
                text jp[2]:
                    xalign 0.5
                    text_align 0.5
                    outlines [(5, "#000000", absolute(0), absolute(0))]

                imagebutton:
                    xalign 0.5 yalign 1.0

                    idle "gui/beach_map/map_marker.png"
                    hover "selectable:gui/beach_map/map_marker.png"
                    hovered [
                        Play("sound", "audio/sfx/sfx_select.ogg"),
                        SetScreenVariable("location_tooltip", jp[2])
                    ]
                    unhovered SetScreenVariable("location_tooltip", "")
                    action [
                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                        Jump(jp[3])
                    ]