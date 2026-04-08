init python: 
    config.per_frame_screens.append("pencil_test")

screen pencil_test():
    modal True

    default score_to_beat = 250
    default max_pencil_length = int(41.2 * 20)
    default distance = 0
    default sharpen_amount = 0.5
    default time_limit = 60
    default time_left = time_limit
    default eraser_size = 200
    default pencils_to_sharpen = 15
    default pencils_sharpened = 0
    default current_pencil_size = max_pencil_length
    default pencils_remaining = (pencils_to_sharpen - pencils_sharpened)
    default last_key_pressed = "e"
    default lockout_time = 0
    default sharpener_state = "down"

    default showed_fun_value = False

    default game_state = "countdown"
    default game_won = None

    if game_won is None:
        timer 1:
            action Function(renpy.restart_interaction)
            repeat True

    on "show":
        action [
            Play("music", audio.rude_buster, if_changed=True),
            Function(persistent.heard.add, "rude_buster")
        ]

    # Background
    add "minigames/pencil/stage.png"
    add "minigames/pencil/table.png":
        xalign 0.5 yalign 1.0

    if not showed_fun_value:
        if fun_value(FUN_VALUE_COMMON):
            default current_pencil = Image("minigames/pencil/pencilcolor.png")
        else:           
            default current_pencil = Image("minigames/pencil/pencil.png")
        $ showed_fun_value = True

    # Sharpener
    python:
        if sharpener_state == "down":
            sharpener_image = "minigames/pencil/sharpener.png"
        elif sharpener_state == "up":
            sharpener_image = "minigames/pencil/sharpener2.png"

    add sharpener_image:
        zoom 0.35
        xpos 1300 ypos 300

    # Pencil
    add current_pencil:
        xanchor 1.0 yanchor 0.5
        xpos 1328 ypos 502
        crop (0, 0, current_pencil_size, 50)

    # X
    if lockout_time > 0:
        add "minigames/pencil/red_x.png":
            xpos 1160 ypos 300

    # Buttons
    python:
        if last_key_pressed == "q":
            q_key_img = Transform("minigames/pencil/key_q.png", alpha = 0.5)
            e_key_img = Image("minigames/pencil/key_e.png")
            sharpener_state = "down"
        elif last_key_pressed == "e":
            q_key_img = Image("minigames/pencil/key_q.png")
            e_key_img = Transform("minigames/pencil/key_e.png", alpha = 0.5)
            sharpener_state = "up"

    add q_key_img:
        xalign 0.3 yalign 0.95
        zoom 0.5

    add e_key_img:
        xalign 0.7 yalign 0.95
        zoom 0.5

    key "q":
        action SetScreenVariable("last_key_pressed", "q")
    key "e":
        action SetScreenVariable("last_key_pressed", "e")

    # Text elements
    text _("Press [[SPACE] to move on to the next pencil!"):
        xalign 0.5 yalign 0.7
        text_align 0.5
        size 48
        color gui.idle_color
        outlines [(absolute(9), "#000", absolute(0), absolute(0))]

    text str(pencils_remaining)+" pencils remaining!":
        xalign 0.5 yalign 0.75
        text_align 0.5
        size 40
        color gui.hover_color
        outlines [(absolute(4.5), "#000", absolute(0), absolute(0))]

    # Timer and distance covered
    vbox:
        xpos 10 ypos 10
        spacing -10

        $ time_left = get_current_time().strftime("%M:%S:%f")
        
        text str(time_left):
            text_align 0.5
            size 100
            color "#FF0000"
            outlines [(absolute(4.5), "#000", absolute(0), absolute(0))]

        text str(distance)+" cm":
            text_align 0.5
            size 100
            color "#0000FF"
            outlines [(absolute(4.5), "#000", absolute(0), absolute(0))]

    # Countdown
    if game_state == "countdown":
        timer 1:
            action Play("sound", "minigames/pencil/sfx_smash_3.ogg")
        timer 2:
            action Play("sound", "minigames/pencil/sfx_smash_2.ogg")
        timer 3:
            action Play("sound", "minigames/pencil/sfx_smash_1.ogg")
        timer 4:
            action [
                Play("sound", "minigames/pencil/sfx_smash_go.ogg"),
                SetScreenVariable("game_state", "playing")
            ]
        text _("3"):
            xalign 0.5 yalign 0.5
            color "#FF0000"
            size 200
            outlines [(absolute(9), "#000", absolute(0), absolute(0))]
            at transform:
                alpha 0
                linear 1.0 alpha 0
                linear 0 alpha 1.0
                linear 1.0 alpha 1.0
                linear 0 alpha 0
        text _("2"):
            xalign 0.5 yalign 0.5
            color "#FFFF00"
            size 200
            outlines [(absolute(9), "#000", absolute(0), absolute(0))]
            at transform:
                alpha 0
                linear 2.0 alpha 0
                linear 0 alpha 1.0
                linear 1.0 alpha 1.0
                linear 0 alpha 0
        text _("1"):
            xalign 0.5 yalign 0.5
            color "#00FF00"
            size 200
            outlines [(absolute(9), "#000", absolute(0), absolute(0))]
            at transform:
                alpha 0
                linear 3.0 alpha 0
                linear 0 alpha 1.0
                linear 1.0 alpha 1.0
                linear 0 alpha 0
