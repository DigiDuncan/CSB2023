# TODO: make sure you can't enter a battle with no fighters on either/both sides
# TODO: fix none not resetting between fights
# TODO: finish other selection screens
# TODO: figure out why autoselect needs two clicks to update
# TODO: figure out why attempting to return to main menu crashes

###################################################### FUNCTIONS FOR THIS SCREEN ONLY

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
        # TODO: this only works if you click one extra time? help?
        else:
            for member in slots_list:
                if member[0] == "(Pending)":
                    ready_yet = False
                    break
                else:
                    ready_yet = True

        return ready_yet

    # fill a given slot
    def rpg_fill_slot(slots_list, current_slot, char_tooltip_data):
        slots_list[current_slot] = char_tooltip_data

    # automatically select the next unselected slot
    def rpg_slot_autoselect(slots_list, current_slot, party_size) -> int:
        # don't go outside the range
        for slot in range(0, (party_size * 2)):
            if slots_list[slot][0] == "(Pending)":
                return slot
        return current_slot

    # predict background image selection (hopefully less laggy???)
    def rpg_start_predict_bgs(ucn_bg_list):
        for img in ucn_bg_list:
            renpy.start_predict(img)

    def rpg_predict_img(img):
        renpy.predict(ucn_bg_list[img])

###################################################### TRANSFORMS FOR THIS SCREEN ONLY

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

###################################################### ACTUAL SCREEN STARTS HERE

screen rpg_char_sel_new():
    modal True

    python:
        show_window = False
        #renpy.choice_for_skipping()

        # this is stupid but it doesn't work any other way
        rpg_pending_sprite = renpy.get_registered_image("rpg_pending_portrait")
        rpg_pending_sprite_hover = renpy.get_registered_image("rpg_pending_portrait_hover")

    # run these immediately in the background of all screens
    on "show" action [
        Function(rpg_start_predict_bgs, ucn_bg_list),
        Hide("category_nav"),
        Play("music2", "audio/riders_menu.ogg"),
        Function(persistent.heard.add, "riders_menu")
    ]

    ###################### important variables for everywhere
    default rpg_selection_stage = "party"
    default rpg_hovered_character = Tooltip("")
    default rpg_slots = [
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"]
    ]
    default rpg_selected_slot = 0
    default rpg_ready = False
    default rpg_party_size = 4
    default rpg_final_parties = []
    default rpg_max_level = 10
    default rpg_scale = 1.0
    default loaded_imgs = 0
    default rpg_img = "images/bg/casino1.png"
    default rpg_bgm = "card_castle"

    ### add background color / prep video
    add Color("#000")
    add Color('#323e42', alpha=0.75)
    showif rpg_ready == True:
        add Movie(size=(1920,1080), play="movies/Fire.webm", side_mask=True) at _rpg_ready_flames

###################################################### STAGE 1: CHARACTER SELECTION

    if rpg_selection_stage == "party":

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
                                        hovered [ rpg_hovered_character.Action([character.name, character]) ]
                                        action [
                                            Play("sound", "audio/sfx/sfx_valid.ogg"),
                                            Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, rpg_hovered_character.value),
                                            SetScreenVariable("rpg_selected_slot", rpg_slot_autoselect(rpg_slots, rpg_selected_slot, rpg_party_size)),
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
                                    hovered [ rpg_hovered_character.Action(["(Random)", RPG.Characters.random() ]) ]
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, ["(Random)", RPG.Characters.random() ]),
                                        SetScreenVariable("rpg_selected_slot", rpg_slot_autoselect(rpg_slots, rpg_selected_slot, rpg_party_size)),
                                        SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots)),
                                        SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots))
                                    ]

                                imagebutton:
                                    xysize(88,88)
                                    idle "gui/rpg/portraits/none.png"
                                    hover "selectable:gui/rpg/portraits/none.png"
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    hovered [ rpg_hovered_character.Action(["(None)", None]) ]
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, rpg_hovered_character.value),
                                        SetScreenVariable("rpg_selected_slot", rpg_slot_autoselect(rpg_slots, rpg_selected_slot, rpg_party_size)),
                                        SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots)),
                                        SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots))
                                    ]

                        ######################### SHOW SELECTED PARTIES

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
                                    for a in range(rpg_party_size):

                                        python:
                                            if rpg_slots[a][0] == "(Pending)":
                                                slot_button_idle = rpg_pending_sprite
                                                slot_button_hover = rpg_pending_sprite_hover
                                            elif rpg_slots[a][0] == "(None)":
                                                slot_button_idle = "gui/rpg/portraits/none.png"
                                                slot_button_hover = "selectable:gui/rpg/portraits/none.png"
                                            elif rpg_slots[a][0] == "(Random)":
                                                slot_button_idle = "gui/rpg/portraits/unknown.png"
                                                slot_button_hover = "selectable:gui/rpg/portraits/unknown.png"
                                            else:
                                                slot_button_idle = rpg_slots[a][1].portrait.filename
                                                slot_button_hover = "selectable:"+rpg_slots[a][1].portrait.filename

                                        imagebutton:
                                            idle slot_button_idle
                                            hover slot_button_hover
                                            selected_idle Composite(
                                                (88,88),
                                                (0,0), slot_button_idle,
                                                (0,0), "gui/rpg/portraits/border_sel_a.png"
                                            )
                                            selected_hover Composite(
                                                (88,88),
                                                (0,0), slot_button_hover,
                                                (0,0), "selectable:gui/rpg/portraits/border_sel_a.png"
                                            )
                                            hover_sound "audio/sfx/sfx_select.ogg"
                                            action [
                                                SetVariable("rpg_selected_slot", a),
                                                SetScreenVariable("rpg_selected_slot", a),
                                                SelectedIf(rpg_selected_slot == a)
                                            ]

                                # Selected character text
                                $ output_text = ""
                                for a in range(rpg_party_size):
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
                                    for e in range(rpg_party_size):

                                        python:
                                            if rpg_slots[e+4][0] == "(Pending)":
                                                slot_button_idle = rpg_pending_sprite
                                                slot_button_hover = rpg_pending_sprite_hover
                                            elif rpg_slots[e+4][0] == "(None)":
                                                slot_button_idle = "gui/rpg/portraits/none.png"
                                                slot_button_hover = "selectable:gui/rpg/portraits/none.png"
                                            elif rpg_slots[e+4][0] == "(Random)":
                                                slot_button_idle = "gui/rpg/portraits/unknown.png"
                                                slot_button_hover = "selectable:gui/rpg/portraits/unknown.png"
                                            else:
                                                slot_button_idle = rpg_slots[e+4][1].portrait.filename
                                                slot_button_hover = "selectable:"+rpg_slots[e+4][1].portrait.filename

                                        imagebutton:
                                            idle slot_button_idle
                                            hover slot_button_hover
                                            selected_idle Composite(
                                                (88,88),
                                                (0,0), slot_button_idle,
                                                (0,0), "gui/rpg/portraits/border_sel_e.png"
                                            )
                                            selected_hover Composite(
                                                (88,88),
                                                (0,0), slot_button_hover,
                                                (0,0), "selectable:gui/rpg/portraits/border_sel_e.png"
                                            )
                                            hover_sound "audio/sfx/sfx_select.ogg"
                                            action [
                                                SetVariable("rpg_selected_slot", e+4),
                                                SetScreenVariable("rpg_selected_slot", e+4),
                                                SelectedIf(rpg_selected_slot == e+4)
                                            ]

                                # Selected character text
                                $ output_text = ""
                                for e in range(rpg_party_size):
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

                                if rpg_hovered_character.value == "":
                                    background None
                                else:
                                    # handle random/none first
                                    if rpg_hovered_character.value:
                                        if rpg_hovered_character.value[0] == "(Random)":
                                            add Image("gui/rpg/random.png"):
                                                xysize(400,400)
                                                fit("contain")
                                                xanchor 0.5 yanchor 1.0
                                                xpos 0.5 ypos 0.8
                                        elif rpg_hovered_character.value[0] == "(None)":
                                            add Image("gui/rpg/none.png"):
                                                xysize(400,400)
                                                fit("contain")
                                                xanchor 0.5 yanchor 1.0
                                                xpos 0.5 ypos 0.8
                                        else:
                                            add Image(rpg_hovered_character.value[1].sprite):
                                                xysize(500,400)
                                                fit("contain")
                                                xanchor 0.5 yanchor 1.0
                                                xpos 0.5 ypos 1.0
                                        frame:
                                            xanchor 0.5 yanchor 1.0
                                            xpos 0.5 ypos 1.0
                                            text rpg_hovered_character.value[0]:
                                                text_align 0.5

        ######################### BOTTOM

        ### buttons
        textbutton "Return to Extras":
            yoffset 950 xoffset 25
            action [
                PauseAudio("music", False),
                Stop("music2"),
                Hide("rpg_char_sel_new", dissolve)
            ]
        textbutton "Main Menu":
            sensitive True
            yoffset 1000 xoffset 25
            action [
                PauseAudio("music", False),
                Stop("music2"),
                Hide("rpg_char_sel_new", dissolve),
                Return()
            ]

        # debug button only
        # textbutton "[[DEBUG] Toggle ready state.":
            # yoffset 50 xoffset 25
            # action [
                # SetScreenVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots, manual = True)),
                # SetVariable("rpg_ready", rpg_toggle_ready(rpg_ready, rpg_slots, manual = True))
            # ]

        python:
            if rpg_ready == True:
                ready_transform = _rpg_ready_button_yes
            else:
                ready_transform = _rpg_ready_button_no

        imagebutton:
            insensitive "sepia:gui/rpg/ready.png"
            idle "gui/rpg/ready.png"
            hover "selectable:gui/rpg/ready.png"
            hover_sound "audio/sfx/sfx_select.ogg"
            action [
                SensitiveIf(rpg_ready == True),
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                # CLEARING THE SCREEN FOR THE NEXT THING
                SetVariable("rpg_selection_stage", "scale"),
                SetScreenVariable("rpg_selection_stage", "scale")
            ]
            at ready_transform

###################################################### STAGE 2: PARTY SCALE

    elif rpg_selection_stage == "scale":

        text "{size=+24}Select Party Scale":
            xalign 0.5
            yalign 0.04
            text_align 0.5

        ###################### bounding box for everything
        frame:
            background None
            xsize 0.9 ysize 0.75
            xalign 0.5 yalign 0.5

            for level in range(1, rpg_max_level+1):
                $ button_text = str(level)

                textbutton button_text:
                    yoffset 32*level
                    action [
                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                        SetVariable("rpg_scale", ((level - 1) / 4 + 1) ),
                        SetScreenVariable("rpg_scale", ((level - 1) / 4 + 1) )
                    ]

        ###################### back / forward
        textbutton "Previous Screen":
            yoffset 1000 xoffset 25
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "party"),
                SetScreenVariable("rpg_selection_stage", "party")
            ]

        textbutton "Next Screen":
            yoffset 1000 xoffset 1674
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "load_imgs"),
                SetScreenVariable("rpg_selection_stage", "load_imgs")
            ]

###################################################### STAGE 3: BACKGROUND IMAGE

    # full disclosure: portions of this section are AI-assisted because this is terrible.

    ###################### load images first
    elif rpg_selection_stage == "load_imgs":

        if loaded_imgs < len(ucn_bg_list):
            timer 0.001:
                repeat True
                action Function(rpg_predict_img, loaded_imgs)
            $ loaded_imgs += 1
            $ load_percent = str( int((loaded_imgs * 100) / len(ucn_bg_list)) )

            text "Loading Images\n"+load_percent+"%":
                xalign 0.5 yalign 0.5
                text_align 0.5
        else:
            text "Preparing Images...":
                xalign 0.5 yalign 0.5
                text_align 0.5
            timer 0.001:
                action [
                    SetVariable("rpg_selection_stage", "img"),
                    SetScreenVariable("rpg_selection_stage", "img")
                ]

    ###################### actual selection
    elif rpg_selection_stage == "img":

        text "{size=+24}Select Background Image":
            xalign 0.5
            yalign 0.04
            text_align 0.5

        ###################### bounding box for everything
        frame:
            background None
            xsize 0.9 ysize 0.75
            xalign 0.5 yalign 0.5

            # partially stealing digi's code for now
            viewport:
                xalign 0.5
                side_yfill True
                scrollbars "vertical"
                mousewheel True

                # TODO: hover/selected effects + tooltips?

                vpgrid:
                    cols 13
                    xalign 0.5
                    for i in ucn_bg_list:
                        button:
                            xanchor 0.0 yanchor 0.0
                            xysize (128, 72)

                            add Image(i):
                                xysize (128, 72)
                                fit ("contain")

                            action [
                                Play("sound", "audio/sfx/sfx_valid.ogg"),
                                SetVariable("rpg_img", i),
                                SetScreenVariable("rpg_img", i)
                            ]

        ###################### back / forward
        textbutton "Previous Screen":
            yoffset 1000 xoffset 25
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "scale"),
                SetScreenVariable("rpg_selection_stage", "scale")
            ]

        textbutton "Next Screen":
            yoffset 1000 xoffset 1674
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "bgm"),
                SetScreenVariable("rpg_selection_stage", "bgm")
            ]

###################################################### STAGE 4: BGM

    elif rpg_selection_stage == "bgm":

        text "{size=+24}Select BGM":
            xalign 0.5
            yalign 0.04
            text_align 0.5

        ###################### bounding box for everything
        frame:
            background None
            xsize 0.9 ysize 0.75
            xalign 0.5 yalign 0.5

            # stealing digi's code here too
            viewport:
                xysize(1920, 540)
                yanchor -0.25
                style_prefix "choice"
                side_yfill True
                scrollbars "vertical"
                mousewheel True
                vbox:
                    for i in MUSIC_MAP:
                        textbutton "{font=music_text}"+MUSIC_MAP[i]["title"]+"{/font}":
                            anchor(-0.25, -0.25)
                            action [
                                Play("sound", "audio/sfx/sfx_valid.ogg"),
                                SetVariable("rpg_bgm", i),
                                SetScreenVariable("rpg_bgm", i)
                            ]

        ###################### back / forward
        textbutton "Previous Screen":
            yoffset 1000 xoffset 25
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "img"),
                SetScreenVariable("rpg_selection_stage", "img")
            ]

        textbutton "Next Screen":
            yoffset 1000 xoffset 1674
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "fight"),
                SetScreenVariable("rpg_selection_stage", "fight")
            ]

###################################################### STAGE 5: JUMP!

    elif rpg_selection_stage == "fight":

        python:
            for member in rpg_slots:
                if member[0] != None:
                    rpg_final_parties.append(member[1])
                else:
                    rpg_final_parties.append(None)

        frame:
            background None
            xsize 0.9 ysize 0.75
            xalign 0.5 yalign 0.5

            python:
                output = "The following data should be carried over:\n\n"
                output += "Fighters:\n"

                for a in range(rpg_party_size*2):

                    if rpg_slots[a][0] == "(None)":
                        op = "(None)"
                    elif rpg_slots[a][0] == "(Random)":
                        op = "(Random)"
                    else:
                        op = rpg_final_parties[a].name

                    output += "     "+op+"\n"

                output += "\nParty scale: "+str(rpg_scale)+"\n"
                output += "Background: "+rpg_img+"\nBGM: "+rpg_bgm

            text output

        ###################### back / forward
        textbutton "Previous Screen":
            yoffset 1000 xoffset 25
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetVariable("rpg_selection_stage", "img"),
                SetScreenVariable("rpg_selection_stage", "img")
            ]

        textbutton "BEGIN!":
            yoffset 1000 xoffset 1674
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                Call("ucn_new", rpg_final_parties, rpg_scale, rpg_img, rpg_bgm)
            ]

    else: # this should NEVER happen!
        $ renpy.jump("secret_dx")

label ucn_new(rpg_final_parties, rpg_scale, rpg_img, rpg_bgm):

    python:

        # attempt to force-clear these between fights
        a1 = None
        a2 = None
        a3 = None
        a4 = None

        e1 = None
        e2 = None
        e3 = None
        e4 = None

        RPG.set_var_character("a1", rpg_final_parties[0].assigned_name if rpg_final_parties[0] else None)
        RPG.set_var_character("a2", rpg_final_parties[1].assigned_name if rpg_final_parties[1] else None)
        RPG.set_var_character("a3", rpg_final_parties[2].assigned_name if rpg_final_parties[2] else None)
        RPG.set_var_character("a4", rpg_final_parties[3].assigned_name if rpg_final_parties[3] else None)

        RPG.set_var_character("e1", rpg_final_parties[4].assigned_name if rpg_final_parties[4] else None)
        RPG.set_var_character("e2", rpg_final_parties[5].assigned_name if rpg_final_parties[5] else None)
        RPG.set_var_character("e3", rpg_final_parties[6].assigned_name if rpg_final_parties[6] else None)
        RPG.set_var_character("e4", rpg_final_parties[7].assigned_name if rpg_final_parties[7] else None)

        RPG.ucn_bg = rpg_img
        RPG.ucn_music = rpg_bgm
        RPG.ucn_scale = rpg_scale

        # ui.close()

    rpg:
        ucn
        allies:
            $a1
            $a2
            $a3
            $a4
        enemies:
            $e1
            $e2
            $e3
            $e4
        on_win "secret_dx"
        on_lose "secret_dx"
        intro_text "Begin!"
