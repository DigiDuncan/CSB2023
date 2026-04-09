init python: 
    config.per_frame_screens.append("pencil_test")
    import datetime as dt

screen pencil_test():
    modal True

    default start_time = get_current_time()
    default time_limit = 60
    default game_time = dt.timedelta(seconds = (time_limit + 4.5))
    default end_time = start_time + game_time
    default time_left = time_limit
    default lockout_time = 0

    default score_to_beat = 250
    default distance = 0

    default max_pencil_length = int(41.2 * 20)
    default sharpen_amount_cm = 0.5
    default sharpen_amount_pixels = 20
    default eraser_size = 108

    default pencils_to_sharpen = 15
    default pencils_sharpened = 0
    default current_pencil_size = max_pencil_length
    default pencils_remaining = (pencils_to_sharpen - pencils_sharpened)

    default last_key_pressed = "e"
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

    if lockout_time == 0:
        key "q":
            action [
                SetScreenVariable("last_key_pressed", "q"),
                If(last_key_pressed=="e", SetScreenVariable("current_pencil_size", current_pencil_size-sharpen_amount_pixels), None),
                If(last_key_pressed=="e", SetScreenVariable("distance", distance+sharpen_amount_cm), None)
            ]
        key "e":
            action [
                SetScreenVariable("last_key_pressed", "e"),
                If(last_key_pressed=="q", SetScreenVariable("current_pencil_size", current_pencil_size-sharpen_amount_pixels), None),
                If(last_key_pressed=="q", SetScreenVariable("distance", distance+sharpen_amount_cm), None)     
            ]
        key "K_SPACE":
            action [
                If(pencils_remaining != 0, SetScreenVariable("pencils_sharpened", pencils_sharpened+1), None),
                If(pencils_remaining != 0, SetScreenVariable("current_pencil_size", max_pencil_length), None),
                If(pencils_remaining != 0, SetScreenVariable("pencils_remaining", pencils_to_sharpen - pencils_sharpened), None),
                Function(renpy.restart_interaction)
            ]

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

        python:
            if game_state == "playing":
                time_left = end_time - dt.datetime.now()
                total_seconds = time_left.total_seconds()
                minutes, seconds, remainder = int(total_seconds / 60), int(total_seconds) % 60, total_seconds % 1
                formatted_time_left = "{:01}:{:02}.{{size=-24}}{:03}".format(minutes, seconds, int(remainder * 1000))
                if total_seconds <= 0 or pencils_remaining == 0:
                    game_state = "end"
            else:
                formatted_time_left = ""

        text str(formatted_time_left):
            text_align 0.5
            size 100
            color "#FF0000"
            outlines [(absolute(4.5), "#000", absolute(0), absolute(0))]

        text str(distance)+" cm":
            text_align 0.5
            size 100
            color "#0000FF"
            outlines [(absolute(4.5), "#000", absolute(0), absolute(0))]

    # Handle oversharpening pencil
    if game_state == "playing":
        python:
            if current_pencil_size <= eraser_size:
                lockout_time = 2
                lockout_countdown = time.time()
                if time.time() > lockout_countdown + lockout_time:
                    lockout_time = 0

    # Countdown
    if game_state == "countdown":
        timer 1:
            action Play("sound", "minigames/pencil/sfx_smash_3.ogg")
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

        timer 2:
            action Play("sound", "minigames/pencil/sfx_smash_2.ogg")
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

        timer 3:
            action Play("sound", "minigames/pencil/sfx_smash_1.ogg")
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

        timer 4:
            action [
                Play("sound", "minigames/pencil/sfx_smash_go.ogg"),
                SetScreenVariable("game_state", "playing")
            ]

    if game_state == "end":

        python:
            if distance > score_to_beat:
                game_won = True
            else:
                game_won = False

        timer 1:
            action [
                Return([game_won, distance]),
                Stop("music", fadeout=1),
                With("dissolve")
            ]