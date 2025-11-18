init:
    transform rotate_10:
        subpixel True
        rotate 10 xanchor 0.5 yanchor 0.5
        xpos 0.5
        ypos 0.5
        zoom 1.33

    transform rotate_6:
        subpixel True
        rotate 5 xanchor 0.5 yanchor 0.5
        ypos 0.5
        zoom 1.2

    transform rotate_5:
        subpixel True
        rotate 5 xanchor 0.5 yanchor 0.5
        ypos 0.5
        zoom 1.1

    transform center_left:
        yanchor 0.5 ypos 0.5
        xanchor 0.0 xpos 0.0

    transform center_right:
        yanchor 0.5 ypos 0.5
        xanchor 1.0 xpos 1.0

    transform mid_left_left:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 0.125

    transform mid_left:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 0.25

    transform mid_mid_left:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 0.375

    transform mid_mid_right:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 0.625

    transform mid_right:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 0.75

    transform mid_right_right:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 0.875

    transform mid_center_right:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.75

    transform mid_center_left:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.25

    transform center_mid_left:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.4

    transform center_mid_right:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.8

    transform mid_offscreen_right:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos 1.0

    transform mid_offscreen_left:
        yanchor 1.0 ypos 1.0
        xanchor 0.5 xpos -0.0

    # i got tired.
    # if ALL you need is a simple custom placement, no zoom/motion/effects, just use this please.
    # for compatibility with the existing positions, set anchor to 1.0 - tate
    transform manual_pos(x, y, this_anchor = 0):
        xanchor this_anchor
        yanchor this_anchor
        xpos x
        ypos y

    # another late-night innovation...
    # because renpy is stupid you MUST use pixel integer, no float allowed.
    # sorry, digi. couldn't get it to work in spite of your help
    transform random_pos(xmin, xmax, ymin, ymax, this_anchor):
        xanchor this_anchor
        yanchor this_anchor
        xpos renpy.random.randint(xmin, xmax)
        ypos renpy.random.randint(ymin, ymax)

    transform xstretch_in:
        xalign 0.5
        linear 0.5 xsize 1920

    transform xstretch_out:
        xalign 0.5
        linear 0.5 xsize 2
        alpha 0.0

    transform little_bounce:
        yanchor 1.0
        yzoom 0.95
        ease 0.1 yzoom 1.05
        ease 0.1 yzoom 1

    transform t_post_it:
        subpixel True
        xanchor 0.5 yanchor 0.0
        xpos 0.65 ypos 0.025
        zoom 0.3333
        rotate 10

    transform t_copguy_frontseat:
        yanchor 1.0 ypos 0.75
        xanchor 0.5 xpos 0.325
        zoom 0.75

    transform t_cashier_at_tims:
        yanchor 1.0 ypos 0.80
        xanchor 0.5 xpos 0.725
        zoom 0.6

    transform t_arc_at_tims:
        yanchor 1.0 ypos 0.75
        xanchor 0.5 xpos 0.625
        linear 0.5 zoom 0.6

    transform t_cs_ltt:
        zoom 0.65
        yanchor 1.0 ypos 0.8
        xanchor 0.0 xpos 0.2

    transform t_linus_ltt:
        zoom 0.65
        yanchor 1.0 ypos 0.8
        xanchor 1.0 xpos 0.8

    transform t_pepzone1:
        ypos 0.50
        xpos 0.375
        zoom 0.75

    transform t_pepzone2:
        ypos 0.33
        xpos 0.375
        zoom 0.75

    transform t_gun:
        rotate 4
        yanchor 0.5 ypos 0.555
        xanchor 0 xpos 0.36

    transform t_stage_screen_l:
        anchor (0.0, 0.0)
        pos (272, 413)
        zoom 0.15

    transform t_stage_screen_c:
        anchor (0.0, 0.0)
        pos (805, 416)
        zoom 0.125

    transform t_stage_screen_r:
        anchor (0.0, 0.0)
        pos (1349, 411)
        zoom 0.15

    transform t_stagescreen:
        anchor (0.5, 1.0)
        pos (0.5, 4.0)  # Why is this needed? This makes no sense. This should be 1.0

    transform t_punchup:
        yanchor 1.0 ypos 0.0
        rotate 0
        linear 1 rotate 960

    # TODO: make sure this transform exactly matches the rpg engine transform. i don't think i quite nailed it -tate
    transform t_fake_rpg_text(x,y,speed = 0.25):
        on show:
            xpos x
            ypos y
            pass
            parallel:
                linear speed ypos (y-0.05)
            parallel:
                ease_expo 0.75 alpha 0.00

    transform t_tate_sigil_text:
        alpha 0.6
        block:
            linear 11 rotate -360
            linear 0 rotate 0
            repeat

    transform lego_run:
        pos (0.5, 0.5)
        anchor(0.5, 0.5)
        linear 2.0 zoom 5.0 alpha 0.0

    transform car_run:
        zoom 0.5
        pos (0.5, 0.5)
        anchor(0.5, 0.5)
        linear 2.0 zoom 2.5

    transform typewriter_location:
        pos (0.5, 0.7)
        anchor(0.5, 0.5)
        rotate(-17)

    transform midoffscreenright:
        pos(1.0, 0.0)

    transform midoffscreenleftspin:
        pos(-1.0, 0.0)
        linear 2 rotate -360

    transform offscreenrightspin:
        pos(1.5, 1.0)
        linear 2 rotate 360

    transform offscreenleftspin:
        pos(-0.5, 0.5)
        linear 2 rotate 360

    transform t_blur_on:
        blur 0.0
        linear 1.0:
            blur 20.0

    transform t_blur_off:
        blur 20.0
        linear 1.0:
            blur 0.0

    transform t_toby:
        xalign 0.5 yalign 0.5
        alpha 0.0
        linear 0.25:
            alpha 0.75
        linear 0.25:
            alpha 0.0

    transform t_lupin_out:
        linear 1.0:
            alpha 0.0
            rotate 2070
            zoom 0.1
            xanchor 0.5 xpos 0.25
            yanchor 0.5 ypos 0.333

    transform t_boom:
        on show:
            xalign 0.5 yalign -0.5
            linear 1.0:
                yalign 0.0
        on hide:
            linear 1.0:
                yalign -0.5

    transform t_evil_mika:
        zoom 2
        xalign 0.5
        yalign 1.0

    transform t_train_scurvy:
        zoom 1.5
        xanchor 0.25
        yanchor 0.335
        ease 2.0 rotate 15
        ease 2.0 rotate -15
        repeat

    transform t_people_scurvy:
        zoom 1.0
        xanchor 0.25
        yanchor 0.335
        ease 2.0 rotate 15
        ease 2.0 rotate -15
        repeat

    transform barrel_moving:
        xysize (256, 256)
        xpos 1.0
        ypos 0.75
        ease 3 xpos 0.0
        ease 3 xpos 1.0
        repeat

    transform barrel_hit:
        xysize (256, 256)
        xpos 0.5
        ypos 0.7
        ease 1.5:
            ypos 1.25
            rotate -300

    transform cruise_car:
        ypos 0.7
        ypos 0.705
        xpos 0.7
        parallel:
            ease 0.1 ypos 0.7
            ease 0.1 ypos 0.705
        repeat

    transform cultist_fire:
        xysize (240, 60)
        yanchor 1.25
        xanchor 1.25
        #ypos 1.45
        #xpos 0.5
        linear 0.25 rotate -45
        linear 0.25 rotate 0

    # TODO: this is still trash, pls fix
    transform t_tv_screen_skew:
        xzoom 0.095
        yzoom 0.13

        perspective True
        matrixtransform RotateMatrix(-1, -32, 1) * OffsetMatrix(700, 135, 0)


    # *** HIGHLY EXPERIMENTAL, USE THESE AT YOUR OWN RISK ***
    # either shake a character or use with this line to shake whole screen for as long as you want:
    # $ renpy.show_layer_at(sustained_<*>punch(<args>), layer="master")
    # if anyone knows how to make it into an easier define thing as below while keeping args, go for it
    # bonus points if we can figure out how to add an "infinite" arg - tate

    transform sustained_hpunch(iterations = 1, speed = 0.05, distance = 10):
        linear speed xoffset distance
        linear speed xoffset (-1*distance)
        linear speed xoffset 0
        repeat iterations

    transform sustained_vpunch(iterations = 1, speed = 0.05, distance = 10):
        linear speed yoffset distance
        linear speed yoffset (-1*distance)
        linear speed yoffset 0
        repeat iterations

### MASTER LAYER ONLY ###

define shake1 = { "master" : hpunch }
define shake2 = { "master" : vpunch }
