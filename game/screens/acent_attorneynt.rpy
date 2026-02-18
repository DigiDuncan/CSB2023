screen acent_attorneynt(chosen_evidence):
    #modal True
    #zorder 1

    python:
        global selected_evidence
        show_window = False
        renpy.choice_for_skipping()

        ##### the items
        items_list = [
            ["Leftover Donut", "images/donut_2.png", "It's a little stale, but there's no mold yet,\nso it's probably fine!"],
            ["Plastic Spoon", "images/spoon.png", "This has no right being as sturdy as it is!"],
            ["Genergy", "images/genergy.png", "Original plum flavor."],
            ["Craptop", "images/characters/craptop/craptop.png", "Hey, under the seat--!"],
            ["Phone", "images/cs_phone.png", "The battery died like two days ago."],
            ["YTX Flash Drive", "images/ytx_drive.png", "Oops, forgot the card itself back at LMG..."],
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    default hovered_item = Tooltip("")
    default selected_item = Tooltip(items_list[chosen_evidence])

    ##### base elements
    add Color('#000000', alpha=0.5)
    add Image("/gui/acent_attorneynt/bg.png"):
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5

    text "Evidence":
        color "#F7F6F2"
        size 64
        xpos 98
        ypos 137

    # item name
    text selected_item.value[0]:
        color "#000000"
        size 72
        xpos 570
        ypos 248

    # item description
    text selected_item.value[2]:
        color "#000000"
        size 54
        xpos 570
        ypos 393
        line_spacing 25

    # select button
    button:
        xanchor 0.5
        yanchor 0.5
        xpos 1650
        ypos 908

        text "Present":
            size 64
            text_align 0.5
            color("#0099cc")
            hover_color("#ff8a00")

        hovered [ Play("sound", "audio/sfx/sfx_select.ogg")]
        action [ Play("sound", "audio/sfx/sfx_valid.ogg"), Return() ]

    # frame + item image
    frame:
        background None
        xpos 133
        ypos 233
        xysize (375, 375)
        image selected_item.value[1]:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            fit "contain"

    ##### container for buttons
    hbox:
        ysize 206
        xalign 0.5
        ypos 653

        # shit out buttons
        for i in range(len(items_list)):

            frame:
                background None
                xsize 170
                ysize 206
                xalign 0.5

                # non-selectable
                if items_list[i][0] == "":
                    imagebutton idle "/gui/acent_attorneynt/empty.png":
                        sensitive False
                        xalign 0.5
                        yalign 1.0
                        yoffset -5

                # selectable
                else:
                    button:
                        imagebutton:
                            idle "/gui/acent_attorneynt/unselected.png"
                            hover "/gui/acent_attorneynt/selected.png"
                            selected "/gui/acent_attorneynt/selected.png"

                            xalign 0.5
                            yalign 1.0

                            hovered [ Play("sound", "audio/sfx/sfx_select.ogg"), hovered_item.Action(items_list[i]) ]
                            action [ Play("sound", "audio/sfx/sfx_valid.ogg"), selected_item.Action(items_list[i]), SetVariable("chosen_evidence", i)  ]

                        image items_list[i][1]:
                            xalign 0.5
                            yalign 0.7
                            size (120,120)
                            fit "contain"
