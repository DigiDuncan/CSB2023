screen rpg_test_grounds():
    modal True

    if my_silly_variable == "A":
        $ print("A")
        text "A"
    elif my_silly_variable == "B":
        $ print("B")
        text "B"
    elif my_silly_variable == "C":
        $ print("C")
        text "C"

label awawa_rpg_test:
    $ renpy.stop_predict_screen("rpg_test_grounds")
    $ my_silly_variable = "A"
    call screen rpg_test_grounds