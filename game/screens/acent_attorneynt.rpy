screen acent_attorneynt(current_evidence):
    default current_evidence = current_evidence
    #modal True
    #zorder 1

    python:
        global current_evidence
        show_window = False
        renpy.choice_for_skipping()

        ##### the items
        items_list = [
            ["Craptop", "images/characters/craptop/craptop.png", "Take a shit on the internet."],
            ["Leftover Donut", "images/donut_2.png", "Glazed and confused."],
            ["Genergy", "images/genergy.png", "Plum-flavored."],
            ["Phone", "images/cs_phone.png", "The battery died like two days ago."],
            ["Dog", "images/dog.png", "Fluffy?!"],
            ["YTX Flash Drive", "images/ytx_drive.png", "Oops, forgot the card itself back at LMG..."],
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    ##### base elements
    add Color('#000000', alpha=0.5)
    add Image("/gui/acent_attorneynt/bg.png"):
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.4

    text "Evidence":
        color "#F7F6F2"
        size 64
        xpos 98
        ypos 55

    # item name
    text items_list[current_evidence][0]:
        color "#000000"
        size 72
        xpos 570
        ypos 165

    # item description
    text items_list[current_evidence][2]:
        color "#000000"
        size 54
        xpos 570
        ypos 310

    # select button
    frame:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.8

        button:
            text "Present Evidence":
                text_align 0.5

            hovered [ Play("sound", "audio/sfx/sfx_select.ogg")]
            action [ Play("sound", "audio/sfx/sfx_valid.ogg"), Return() ]

    # frame + item image
    frame:
        background None
        xpos 133
        ypos 150
        xysize (375, 375)
        image items_list[current_evidence][1]:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            fit "contain"

    ##### container for buttons
    hbox:
        ysize 206
        xalign 0.5
        ypos 570

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

                            hovered [ Play("sound", "audio/sfx/sfx_select.ogg"), SetScreenVariable("current_evidence", i), SetVariable("current_evidence", i), Notify(i) ]
                            action [ Play("sound", "audio/sfx/sfx_valid.ogg"), SetScreenVariable("current_evidence", i), SetVariable("current_evidence", i), Notify(current_evidence) ]

                        image items_list[i][1]:
                            xalign 0.5
                            yalign 0.7
                            size (120,120)
                            fit "contain"
