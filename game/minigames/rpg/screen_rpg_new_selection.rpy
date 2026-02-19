label awawa_rpg_select_test:
    call screen rpg_char_sel_new with dissolve

init python:
    # ready up
    def rpg_toggle_ready(ready, slots_list, manual = False):
        ready_yet = False

        # for debug only
        if manual == True:
            if ready == True:
                ready_yet = False
            else:
                ready_yet = True

        # normal functionality:
        # check all the slots. if ANY are pending, we're not ready yet
        # TODO: this only works if there's a random or none in the list? help?
        else:
            for slot in slots_list:
                if any(slot == ["(Pending)"] for slot in slots_list):
                    ready_yet = False
                    break
                else:
                    ready_yet = True
        return ready_yet

    # fill a given slot
    def rpg_fill_slot(slots_list, current_slot, char_tooltip_data):
        slots_list[current_slot] = char_tooltip_data

    # automatically select the next unselected slot - does not work yet
    def rpg_slot_autoselect(slots_list, current_slot, party_size):
        found_pending = False
        # don't go outside the range
        for slot in range(0, (party_size*2)-1):
            if slots_list[slot][0] == "(Pending)":
                found_pending = True
                break
            else:
                found_pending = False

        if found_pending == True:
            current_slot = slot+1

    #rpg_slots = [ ]
    #rpg_selected_slot = 0
    #rpg_ready = False

    #global rpg_slots
    #global rpg_selected_slot
    #global rpg_ready

transform _rpg_ready_button_yes:
    zoom 0.4
    yoffset 1000
    xoffset 1650
    block:
        ease_cubic 0.25 zoom 0.41
        ease_cubic 0.25 zoom 0.4
        repeat

transform _rpg_ready_button_no:
    zoom 0.4
    yoffset 1000
    xoffset 1650

transform _rpg_ready_flames:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen rpg_char_sel_new():

    # this is stupid but it doesn't work any other way
    $ rpg_pending_sprite = renpy.get_registered_image("rpg_pending_portrait")
    $ rpg_pending_sprite_hover = renpy.get_registered_image("rpg_pending_portrait_hover")

    # variables
    default hovered_character = Tooltip("")
    default rpg_slots = [
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"]
    ]
    default rpg_selected_slot = 0
    default rpg_ready = False
    default party_size = 4

    ### add background color, kill music
    # TODO: bgm
    add Color('#323e42', alpha=0.75)
    showif rpg_ready == True:
        add Movie(size=(1920,1080), play="movies/Fire.webm", side_mask=True) at _rpg_ready_flames

    $ renpy.music.stop()

###################################################### TOP HALF ######################################################

    text "{size=+24}Select Your Characters!":
        xalign 0.5
        yalign 0.04
        text_align 0.5

    ###################### bounding box for everything
    frame:
        background None
        xsize 0.9 ysize 0.75
        xalign 0.5 yalign 0.5

        grid 1 2:
            xalign 0.5
            vbox:
                xalign 0.5

                ###################### selectable characters go here
                frame:
                    background None
                    ysize 0.5
                    xalign 0.5
                    $ counter = 0
                    vbox:
                        xalign 0.5
                        vpgrid:
                            cols 17
                            spacing 10
                            xalign 0.5
                            for character in RPG.Characters.characters:
                                $ portrait = character.portrait.filename

                                # this bit is stupid lmao
                                if portrait == "gui/rpg/portraits/blank.png":
                                    $ hover_portrait = "selectable:gui/rpg/portraits/blank_hover.png"
                                else:
                                    $ hover_portrait = "selectable:"+portrait

                                imagebutton:
                                    xysize(88,88)
                                    idle portrait
                                    hover hover_portrait
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    hovered [ hovered_character.Action([character.name, character]) ]
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, hovered_character.value),
                                        Function(rpg_slot_autoselect, rpg_slots, rpg_selected_slot, party_size),
                                        SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots)),
                                        SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots))
                                    ]

                            ###################### handle empty portrait slots here
                            python:
                                unused_slots = ((17*4)-2)-len(RPG.Characters.characters)
                            for f in range(unused_slots):
                                add Null(88,88)

                            ###################### handle random/skipped characters
                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/unknown.png"
                                hover "selectable:gui/rpg/portraits/unknown.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered [ hovered_character.Action(["(Random)", RPG.Characters.random() ]) ]
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, hovered_character.value),
                                    Function(rpg_slot_autoselect, rpg_slots, rpg_selected_slot, party_size),
                                    SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots)),
                                    SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots))
                                ]

                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/none.png"
                                hover "selectable:gui/rpg/portraits/none.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered [ hovered_character.Action(["(None)", None]) ]
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, hovered_character.value),
                                    Function(rpg_slot_autoselect, rpg_slots, rpg_selected_slot, party_size),
                                    SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots)),
                                    SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots))
                                ]

###################################################### LOWER HALF ######################################################

                    ### Show selected characters
                    ### Slots 0-3 are allies, 4-7 are enemies
                    frame:
                        background None
                        xsize 1.0 ysize 1.0
                        xanchor 0.5 yanchor 0.5
                        xpos 0.5 ypos 1.6

                        ###################### Allies
                        frame:
                            background None
                            xsize 0.5 xoffset 10
                            text "{size=+8}Allies"

                            # Selected character portraits
                            grid 4 1:
                                ypos 0.175
                                spacing 10
                                for a in range(party_size):
                                    imagebutton:
                                        if rpg_slots[a][0] == "(Pending)":
                                            idle rpg_pending_sprite
                                            hover rpg_pending_sprite_hover
                                        elif rpg_slots[a][0] == "(None)":
                                            idle "gui/rpg/portraits/none.png"
                                            hover "selectable:gui/rpg/portraits/none.png"
                                        elif rpg_slots[a][0] == "(Random)":
                                            idle "gui/rpg/portraits/unknown.png"
                                            hover "selectable:gui/rpg/portraits/unknown.png"
                                        else:
                                            idle rpg_slots[a][1].portrait.filename
                                            hover "selectable:"+rpg_slots[a][1].portrait.filename

                                        hover_sound "audio/sfx/sfx_select.ogg"
                                        action [
                                            SetVariable("rpg_selected_slot", a),
                                            SetScreenVariable("rpg_selected_slot", a)
                                        ]

                            # Selected character text
                            $ output_text = ""
                            for a in range(party_size):
                                if rpg_slots[a][0] == "(Pending)":
                                    $ output_text += "\n"
                                else:
                                    $ output_text += rpg_slots[a][0]+"\n"

                            text output_text:
                                ypos 0.45

                        ###################### Enemies
                        frame:
                            background None
                            xsize 0.5 xoffset -10
                            xalign 1.0
                            text "{size=+8}Enemies":
                                xalign 1.0

                            # Selected character portraits
                            grid 4 1:
                                xalign 1.0
                                ypos 0.175
                                spacing 10
                                for e in range(party_size):
                                    imagebutton:
                                        if rpg_slots[e+4][0] == "(Pending)":
                                            idle rpg_pending_sprite
                                            hover rpg_pending_sprite_hover
                                        elif rpg_slots[e+4][0] == "(None)":
                                            idle "gui/rpg/portraits/none.png"
                                            hover "selectable:gui/rpg/portraits/none.png"
                                        elif rpg_slots[e+4][0] == "(Random)":
                                            idle "gui/rpg/portraits/unknown.png"
                                            hover "selectable:gui/rpg/portraits/unknown.png"
                                        else:
                                            idle rpg_slots[e+4][1].portrait.filename
                                            hover "selectable:"+rpg_slots[e+4][1].portrait.filename

                                        hover_sound "audio/sfx/sfx_select.ogg"
                                        action [
                                            SetVariable("rpg_selected_slot", e+4),
                                            SetScreenVariable("rpg_selected_slot", e+4)
                                        ]

                            # Selected character text
                            $ output_text = ""
                            for e in range(party_size):
                                if rpg_slots[e+4][0] == "(Pending)":
                                    $ output_text += "\n"
                                else:
                                    $ output_text += rpg_slots[e+4][0]+"\n"

                            text output_text:
                                ypos 0.45
                                xalign 1.0
                                text_align 1.0

                        ###################### display currently hovered character
                        frame:
                            xanchor 0.5 yanchor 1.0
                            xpos 0.5 ypos 1.0
                            xsize 0.5
                            background None

                            if hovered_character.value == "":
                                background None
                            else:
                                # handle random/none first
                                if hovered_character.value:
                                    if hovered_character.value[0] != "(Random)" and hovered_character.value[0] != "(None)":
                                        add Image(hovered_character.value[1].sprite):
                                            xysize(500,400)
                                            fit("contain")
                                            xanchor 0.5 yanchor 1.0
                                            xpos 0.5 ypos 1.0
                                    frame:
                                        xanchor 0.5 yanchor 1.0
                                        xpos 0.5 ypos 1.0
                                        text hovered_character.value[0]:
                                            text_align 0.5

###################################################### BOTTOM ######################################################

    ### buttons
    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

    # debug button only
    # textbutton "[[DEBUG] Toggle ready state.":
        # yoffset 50 xoffset 25
        # action [
            # SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots, manual = True)),
            # SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots, manual = True))
        # ]

    if rpg_ready == True:
        $ ready_transform = _rpg_ready_button_yes
    else:
        $ ready_transform = _rpg_ready_button_no

    imagebutton:
        insensitive "sepia:gui/rpg/ready.png"
        idle "gui/rpg/ready.png"
        hover "selectable:gui/rpg/ready.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        action [
            SensitiveIf(rpg_ready == True),
            Play("sound", "audio/sfx/sfx_valid.ogg")
        ]
        at ready_transform

