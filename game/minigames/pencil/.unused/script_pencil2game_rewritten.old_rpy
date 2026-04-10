init python: 
    config.per_frame_screens.append("pencil2game")

screen pencil2game():
    modal True

    default time_limit = 240
    default timer = Timer(time_limit+4.5)
    default time_left = time_limit

    default lockout = False
    default penalty = 2

    default score_to_beat = 1000
    default distance = 0.0

    default initial_pencil_size = 824
    default eraser_size = 80
    default sharpen_amount_cm = 0.5
    default sharpen_amount_pixels = int((initial_pencil_size - eraser_size) / 39)
    
    default pencils_to_sharpen = 60
    default pencils_sharpened = 0
    default current_pencil_size = initial_pencil_size
    default pencils_remaining = (pencils_to_sharpen - pencils_sharpened)

    default last_key_pressed = "e"
    default sharpener_state = "down"

    default last_spin_count = 0
    default center = [960, 540]
    default spinner_image = "minigames/pencil/spinner_square.png"

    default showed_fun_value = False

    default game_state = "countdown"
    default game_won = None

    if game_won is None:
        timer 1:
            action Function(renpy.restart_interaction)
            repeat True

    on "show":
        action [
            Play("music", audio.get_the_funk, if_changed=True),
            Function(persistent.heard.add, "get_the_funk")
        ]

    # Background
    add "minigames/pencil2/pencilboss.png"
    add "minigames/pencil/table.png":
        xalign 0.5 yalign 1.0
    add "minigames/pencil/pencil_clock.png":
        xalign -0.1 yalign 0.5

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
    if lockout is True:
        add "minigames/pencil/red_x.png":
            xpos 1160 ypos 300
        timer penalty:
            action [
                SetScreenVariable("lockout", False),
                If(pencils_remaining != 0, SetScreenVariable("current_pencil_size", initial_pencil_size), None),
                If(pencils_remaining != 0, SetScreenVariable("pencils_remaining", pencils_to_sharpen - pencils_sharpened), None),
                Function(renpy.restart_interaction)
            ]

    # Text elements
    # Timer and distance covered
    if not preferences.disable_button_mashing:
        $ text_instruction_yalign = 0.7
        $ text_remaining_yalign = 0.75
            
        text _("Press [[SPACE] to move on to the next pencil!"):
            xalign 0.5 yalign text_instruction_yalign
            text_align 0.5
            size 48
            color gui.idle_color
            outlines [(absolute(9), "#000", absolute(0), absolute(0))]

    else:
        $ text_instruction_yalign = 0.05
        $ text_remaining_yalign = 0.1
        text _("Spin to sharpen!"):
            xalign 0.5 yalign text_instruction_yalign-0.05
            text_align 0.5
            size 48
            color gui.idle_color
            outlines [(absolute(9), "#000", absolute(0), absolute(0))]
            
        text _("Click or press [[SPACE] to move on to the next pencil!"):
            xalign 0.5 yalign text_instruction_yalign
            text_align 0.5
            size 48
            color gui.idle_color
            outlines [(absolute(9), "#000", absolute(0), absolute(0))]

    # Force-update it first
    $ pencils_remaining = (pencils_to_sharpen - pencils_sharpened) 
    text str(pencils_remaining)+" pencils remaining!":
        xalign 0.5 yalign text_remaining_yalign
        text_align 0.5
        size 40
        color gui.hover_color
        outlines [(absolute(4.5), "#000", absolute(0), absolute(0))]

    python:
        if game_state == "playing":
            time_left = timer.get_remaining()
            total_seconds = time_left.total_seconds()
            minutes, seconds, remainder = int(total_seconds / 60), int(total_seconds) % 60, total_seconds % 1
            formatted_time_left = "{:01}:{:02}.{{size=-24}}{:02}".format(minutes, seconds, int(remainder * 100))
            if total_seconds <= 0 or pencils_remaining == 0:
                game_state = "end"
        elif game_state == "countdown":
            formatted_time_left = "Starting"
        elif game_state == "end":
            formatted_time_left = "Finish"

    text str(formatted_time_left):
        text_align 1.0
        xpos 109 ypos 566
        size 100
        color "#000000"
        font "fonts/digital-7.ttf"
        at transform:
            alpha 0.8

    if game_state == "playing":
        text str(distance):
            xanchor 0.5 yanchor 0.5 text_align 0.5
            xpos 429 ypos 593 
            size 56
            color "#000000"
            font "fonts/digital-7.ttf"
            at transform:
                alpha 0.8

        add "minigames/pencil/measurement.png":
            xpos 368 ypos 617
            at transform:
                alpha 0.8

                block:
                    linear 0 alpha 0.0
                    linear 1 alpha 0.0
                    linear 0 alpha 0.8
                    linear 1 alpha 0.8
                    repeat

    # Buttons (Regular controls)
    if not preferences.disable_button_mashing:
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

        if game_state == "playing" and not lockout:
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
                    If(pencils_remaining != 0, SetScreenVariable("current_pencil_size", initial_pencil_size), None),
                    If(pencils_remaining != 0, SetScreenVariable("pencils_remaining", pencils_to_sharpen - pencils_sharpened), None),
                    If(current_pencil_size == 84, Play("sound", "minigames/pencil/sfx_smash_excellent.ogg", loop=False), None),
                    Function(renpy.restart_interaction)
                ]
    # Spinner wheel (Alternate controls)
    else:
        if game_state == "playing" and not lockout:
            # If you set variables called `center` and `spinner_image` on the screen,
            # they should get automagically passed into a screen called with no parentheses
            use osu_spinner(center, spinner_image)
        elif game_state == "playing" and lockout:
            add spinner_image:
                matrixcolor shade_bw_matrix
                xanchor 0.5 yanchor 0.5
                pos center
        key ["mousedown_1", "K_SPACE"]:
                action [
                    If(pencils_remaining != 0, SetScreenVariable("pencils_sharpened", pencils_sharpened+1), None),
                    If(pencils_remaining != 0, SetScreenVariable("current_pencil_size", initial_pencil_size), None),
                    If(pencils_remaining != 0, SetScreenVariable("pencils_remaining", pencils_to_sharpen - pencils_sharpened), None),
                    #If(current_pencil_size == 84, Play("sound", "minigames/pencil/sfx_smash_excellent.ogg", loop=False), None),
                    Function(renpy.restart_interaction)
                ]

        python:
            if preferences.disable_button_mashing and game_state == "playing" and not lockout:
                if store.spins > last_spin_count:
                    current_pencil_size = current_pencil_size-sharpen_amount_pixels * 2
                    distance = distance+sharpen_amount_cm * 2
                    last_spin_count = store.spins

    # Dev door
    if preferences.developer_mode:
        key "K_END":
            action [
                SetScreenVariable("distance", score_to_beat+5),
                SetScreenVariable("game_state", "end")
            ]
    # Handle oversharpening pencil
    if game_state == "playing":
        python:
            if current_pencil_size <= eraser_size and not lockout:
                renpy.sound.play("minigames/pencil/sfx_fail.ogg", channel="sound", loop=False)
                lockout = True

    # Countdown
    if game_state == "countdown":
        timer 1:
            action Play("sound", "minigames/pencil2/sfx_ding.ogg")
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
            action Play("sound", "minigames/pencil2/sfx_ding.ogg")
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
            action Play("sound", "minigames/pencil2/sfx_ding.ogg")
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
                Play("sound", "minigames/pencil2/sfx_dong.ogg"),
                SetScreenVariable("game_state", "playing")
            ]

    if game_state == "end":

        python:
            if distance > score_to_beat:
                #renpy.sound.play("minigames/pencil/sfx_smash_victory.ogg", channel="sound", loop=False)
                game_won = True
            else:
                game_won = False

        timer 1:
            action [
                Return([game_won, distance]),
                Stop("music", fadeout=1),
                With(dissolve)
            ]

label minigame_pencil2:
    window hide
    $ quick_menu = False
    call screen pencil2game()
    $ quick_menu = True
    window show

    if _return[1] >= 1200:
        $ achievement_manager.unlock("paincil")
    elif _return[1] > 1000:
        $ achievement_manager.unlock("pencil2")

    if _return[0]:
        $ renpy.jump(str(minigame_win))
    else:
        $ renpy.jump(str(minigame_loss))