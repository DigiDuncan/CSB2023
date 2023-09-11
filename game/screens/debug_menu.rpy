screen debug_menu():
    tag menu
    python:
        labels = sorted([l for l in renpy.get_all_labels() if not l.startswith("_") and not l in ["after_error_fight", "after_ucn"]])
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
                textbutton k action Hide("debug_menu"), Start(k)
    textbutton "Back" action Return() yoffset 1000 xoffset 25
