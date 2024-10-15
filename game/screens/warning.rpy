screen warning(warning_text, triggers, leave_label):
    modal True
    python:
        show_window = False
        renpy.choice_for_skipping()
    add "#000000"
    vbox:
        xalign 0.5
        yalign 0.5
        add "gui/warning.png" xalign 0.5
        add Text(warning_text, size=48, color = "#FFFFFF", textalign = 0.5):
            xalign 0.5
            yalign 0.5
        add Text(triggers, size=32, color = "#AAAAAA", textalign = 0.5):
            xalign 0.5
            yalign 0.5
        null height 80
        textbutton "Go back!":
            xalign 0.5
            text_textalign 0.5
            text_size 36
            action Hide("warning"), Jump(leave_label)
        textbutton "Proceed":
            xalign 0.5
            text_textalign 0.5
            text_size 36
            action Hide("warning")
