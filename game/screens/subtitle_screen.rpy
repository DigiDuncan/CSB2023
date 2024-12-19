init 0:
    image dxcom_anim = spritesheet_animation("gui/dxcom_icon.png", 10, 10, looping = True)

screen _dxcom(c):
    zorder 100
    layer "popup"
    style_prefix "dxcom"
    modal True

    frame:
        at dxcom_appear
        xsize 1920
        yminimum 10
        ymaximum 175

        vbox:
            hbox:
                spacing 20
                add "gui/dxcom_icon_static.png":
                    xysize(120, 120)
                    xpos 15
                    yalign 0.5
                null width 15
                text c.full_text:
                    size 32
                    xmaximum 1700
                    font FontGroup().add("fonts/DIN-Medium.ttf", 0x0000, 0x024F).add("CP_Font_1.otf", 0x2E80, 0xDFFF).add("fonts/OpenSans-Regular.ttf", 0x0000, 0xffff)
                    layout "greedy"
                    color c.color
    frame:
        xsize 46
        ysize 46
        xalign 1.0
        yalign 0.0
        textbutton "X":
            xalign 0.5
            yalign 0.5
            text_align 0.5
            text_size 28
            action [ Hide('_dxcom'), Stop("dxcom"), SetVariable("current_dxcom", None) ]

    timer c.length action Hide('_dxcom')

transform dxcom_appear:
    alpha 0.0
    xalign 0.0
    yalign 0.05

    on show:
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
