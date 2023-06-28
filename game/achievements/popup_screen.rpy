screen popup(a):
    zorder 100
    layer "popup"
    style_prefix "popup"

    frame:
        at popup_appear
        xysize(367, 152)

        add a.icon:
            xysize(100, 100)
            pos (17, 19)

        add "popup.png":
            pos (-2, -2)

        vbox:
            xysize(320, 83)
            pos (132, 30)
            spacing 15

            text a.name:
                size 22
                font "fonts/DIN-Medium.ttf"
                layout "greedy"
                
            text a.desc:
                size 16
                xmaximum 180
                font "fonts/DIN-Medium.ttf"
                layout "greedy"

    timer 5 action Hide('popup')

transform popup_appear:
    on show:
        xalign 1.0
        yanchor 0.0 ypos 1.0
        linear 0.5 yanchor 1.0
    on hide:
        linear 0.5 yanchor 0.0