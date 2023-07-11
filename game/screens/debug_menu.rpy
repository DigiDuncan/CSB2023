screen debug_menu():
    python:
        labels = sorted(renpy.get_all_labels())
    viewport:
        xpos 350
        xsize 1570
        mousewheel True
        draggable True
        pagekeys True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            for k in labels:
                textbutton k action Hide("start_menu"), Hide("debug_menu"), Jump(k)
    textbutton "Back" action Return() yoffset 1000 xoffset 25
