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

label awawa_rpg_test:
    $ renpy.stop_predict_screen("rpg_test_grounds")
    $ my_silly_variable = "A"
    call screen rpg_test_grounds
