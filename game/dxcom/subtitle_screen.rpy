screen dxcom(c):
    zorder 100
    layer "popup"
    style_prefix "dxcom"

    frame:
        at dxcom_appear
        xysize(1920, 150)

        add "dxcom/dxcom_icon.png":
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

    timer c.length action Hide('dxcom')

transform dxcom_appear:
    on show:
        alpha 0.0
        xalign 0.0
        yalign 0.05
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
