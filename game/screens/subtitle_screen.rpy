init 0:
    image dxcom_anim = spritesheet_animation("gui/dxcom_icon.png", 10, 10, looping = True)

screen _dxcom(c):
    zorder 100
    layer "popup"
    style_prefix "dxcom"

    frame:
        at dxcom_appear
        xysize(1920, 150)

        add "gui/dxcom_icon_static.png":
            xysize(120, 120)
            pos (15, 15)

        vbox:
            xysize(1750, 230)
            pos (140, 10)
            spacing 15

            text c.full_text:
                size 32
                xmaximum 1680
                font "fonts/DIN-Medium.ttf"
                layout "greedy"
                color c.color

    timer c.length action Hide('_dxcom')

transform dxcom_appear:
    on show:
        alpha 0.0
        xalign 0.0
        yalign 0.05
        linear 0.25 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0

screen dxcom(arg):
    zorder 100
    layer "popup"
    style_prefix "dxcom_button"

    frame at t_dxcom:
        imagebutton idle "dxcom_anim" hover_sound "sfx/sfx_select.ogg":
            action Hide("dxcom"), SetVariable("current_dxcom", arg), Call("show_dxcom", from_current=True)

transform t_dxcom:
    xanchor 1.0 xpos 0.95
    yanchor 0.0 ypos 0.05
    xysize(120, 120)
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

style dxcom_button_frame is empty
