screen debug_menu():
    python:
        labels = sorted(renpy.get_all_labels())
    viewport:
        mousewheel True
        draggable True
        pagekeys True
        scrollbars "vertical"
        textbutton "Back" action Return
        vbox:
            spacing 10
            xoffset 350
            for k in labels:
                textbutton k action Hide("start_menu"), Hide("debug_menu"), Jump(k)
