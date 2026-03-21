label awawa_rpg_test:
    call screen rpg_screen_new()

screen rpg_screen_new():

    default mode = None

    if mode == "ATK":
        text "attacking"

        textbutton "target somebody":
            action [ SetScreenVariable("mode", "TGT")]

    elif mode == "DEF":
        text "defending"
    elif mode == "TGT":
        text "targeting"
    else:
        text "What will you do?"

        vbox:
            textbutton "ATK":
                action [ SetScreenVariable("mode", "ATK")]
            textbutton "DEF":
                action [ SetScreenVariable("mode", "DEF")]
  