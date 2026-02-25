screen debug_menu():
    tag menu
    default chosen_label = None

    on "show":
        action [
            Function(renpy.show_layer_at, t_blur_on, layer='master')
        ]

    on "hide":
        action [
            Function(renpy.show_layer_at, t_blur_off, layer='master')
        ]

    add "#000000aa"

    python:
        labels = sorted(
            [
                l for l in renpy.get_all_labels() if not l.startswith("_")
                and not l.startswith("minigame_")
                and not l in [
                    "after_error_fight",
                    "after_ucn",
                    "before_main_menu",
                    "beach_beach",
                    "beach_boardwalk",
                    "beach_downtown",
                    "beach_uptown",
                    "csdata",
                    "clear_screen",
                    "lightgamehit",
                    "reset_vector",
                    "save_screen",
                    "splashscreen",
                    "start"
                    ]
            ]
        )

    frame:
        background None
        xpos 25 ypos 50
        xsize 1895 ysize 850

        text "{size=+12}Debug Screen 2.0{/size}":
            xalign 0.0 ypos 0
        text"{size=-24}(Some labels have been hidden for sanity.){/size}":
            xalign 1.0 ypos 24
            text_align 1.0

        viewport:
            mousewheel True
            draggable True
            pagekeys True
            scrollbars "vertical"

            xsize 1850 ysize 750
            xpos 25 ypos 75

            vpgrid:
                cols 2
                transpose True
                xsize 1800
                xspacing 0.5

                for k in labels:
                    if k == "error":
                        $ label_text = "{chaos}error"
                    else:
                        $ label_text = k

                    textbutton label_text:
                        action [
                            SelectedIf(SetVariable("chosen_label", k)),
                            SetVariable("chosen_label", k),
                            SetScreenVariable("chosen_label", k)
                        ]

    if chosen_label == None:
        textbutton "Pick a label first!":
            yoffset 1000 xoffset 1895
            xanchor 1.0
            text_align 1.0
            sensitive False
    else:
        textbutton "Jump to [chosen_label]":
            yoffset 1000 xoffset 1895
            xanchor 1.0
            text_align 1.0
            action [
                SensitiveIf(SetVariable("chosen_label", k)),
                Hide("debug_menu"),
                Start(chosen_label)
            ]

    textbutton "Return to Extras":
        yoffset 950 xoffset 25
        action [
            SetVariable("chosen_label", None),
            ShowMenu("category_welcome")
        ]
    textbutton "Main Menu":
        yoffset 1000 xoffset 25
        action [
            SetVariable("chosen_label", None),
            Return()
        ]
