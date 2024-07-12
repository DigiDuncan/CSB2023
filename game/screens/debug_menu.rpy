screen debug_menu():
    tag menu

    $ renpy.show_layer_at(t_blur_on, layer='master')
    on "hide" action Function(renpy.show_layer_at, t_blur_off, layer='master')

    add "#000000aa"

    python:
        labels = sorted([l for l in renpy.get_all_labels() if not l.startswith("_") and not l.startswith("minigame_") and not l in ["after_error_fight", "after_ucn", "reset_vector"]])
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
                if k == "error":
                    textbutton "{chaos}error" action Hide("debug_menu"), Start(k)
                else:
                    textbutton k action Hide("debug_menu"), Start(k)
    textbutton "Back" action Return() yoffset 1000 xoffset 25
