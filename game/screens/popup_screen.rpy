screen popup(a):
    zorder 100
    layer "popup"
    style_prefix "popup"
    $ popup_chieve_name = Text(a.name, size=22, xmaximum=260, font="fonts/DIN-Medium.ttf", layout="greedy")
    $ popup_chieve_desc = Text(a.desc, size=16, xmaximum=260, font="fonts/DIN-Medium.ttf", layout="greedy")
    $ popup_chieve_icon = Image(a.icon)

    frame:
        at popup_appear
        xmaximum 360
        xminimum 360
        background Frame("popup.png", 100, 100)
        hbox:
            spacing 10
            frame:
                background None
                xysize(100,100)
                yalign 0.5
                add popup_chieve_icon:
                    yalign 0.5
                    xalign 0.5
                    xysize(100,100)
                add Image("icon_border.png"):
                    yalign 0.5
                    xalign 0.5
            vbox:
                spacing 15
                add popup_chieve_name
                add popup_chieve_desc

    timer 5 action Hide('popup')

transform popup_appear:
    on show:
        xalign 1.0
        yanchor 0.0 ypos 1.0
        linear 0.5 yanchor 1.0
    on hide:
        linear 0.5 yanchor 0.0
