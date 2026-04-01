screen rpg_test_grounds():
    modal True

    if my_silly_variable == "A":
        $ print("Screen A")
        python:
            if my_silly_variable == "A":
                print("Python A")
        text "A"
    elif my_silly_variable == "B":
        $ print("Screen B")
        python:
            if my_silly_variable == "B":
                print("Python B")
        text "B"
    elif my_silly_variable == "C":
        $ print("Screen C")
        python:
            if my_silly_variable == "C":
                print("Python C")
        text "C"

    frame:
        background get_themed_attribute("rpg/button_frame")
        hover_background "selectable:"+get_themed_attribute("rpg/button_frame")
        
        xsize 215 ysize 87
        xalign 0.5 yalign 0.5

        button:
            xsize 1.0 ysize 1.0
            text "Attack":
                xalign 0.5 yalign 0.5

                color gui.idle_color
                hover_color gui.hover_color
                selected_color gui.selected_color
                insensitive_color gui.insensitive_color

            action [ Notify("Awawa!") ]

label awawa_rpg_test:
    $ renpy.stop_predict_screen("rpg_test_grounds")
    $ my_silly_variable = "A"
    call screen rpg_test_grounds
