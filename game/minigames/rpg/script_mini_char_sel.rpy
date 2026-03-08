# TODO: fix selection crashing if you click fast

###################################################### FUNCTIONS FOR THIS SCREEN ONLY

init python:
    # Fill a given slot
    def rpg_fill_slot(slots_list, current_slot, char_stored_data):
        slots_list[current_slot] = char_stored_data

    # Automatically select the next unselected slot (AI-assisted)
    def rpg_slot_autoselect(slots_list, current_slot):

        # Do NOT try party_size*2 again, it is why the screen took two clicks to update
        total_slots = len(slots_list)

        # Load-bearing crash prevention (well, hopefully)
        if total_slots <= 1:
            return 0

        # Search for any empty slots
        for i in range(1, total_slots):
            checked_slot = (current_slot + i) % total_slots
            if slots_list[checked_slot][0] == "(Pending)":
                return checked_slot

        # Failsafe - just give me the next slot
        return (current_slot + 1) % total_slots

###################################################### ACTUAL SCREEN STARTS HERE

screen _rpg_selection(char_list = [None]):
    modal True

    python:
        show_window = False
        #renpy.choice_for_skipping()

        # This is stupid but it doesn't work any other way
        rpg_pending_sprite = renpy.get_registered_image("rpg_pending_portrait")
        rpg_pending_sprite_hover = renpy.get_registered_image("rpg_pending_portrait_hover")

    # Run these immediately in the background of all screens
    on "show" action [
        Function(start_predict_list, ucn_bg_list),
        Hide("category_nav"),
        Play("music2", "audio/riders_menu.ogg"),
        Function(persistent.heard.add, "riders_menu")
    ]

    ###################### Important variables for everywhere
    default rpg_hovered_data = []
    default rpg_slots = [
        ["(Pending)"], ["(Pending)"],
        ["(Pending)"], ["(Pending)"]
    ]
    default rpg_selected_slot = 0
    default rpg_ready = False
    default rpg_party_size = 4
    default rpg_final_party = []

    ### Add background color / prep video
    add Color("#000")
    add Color('#323e42', alpha=0.75)
    showif rpg_ready == True:
        add Movie(size=(1920,1080), play="movies/Fire.webm", side_mask=True) at _rpg_ready_flames

###################################################### CHARACTER SELECTION

    ### Handle this logic here I guess since it doesn't like it in a function
    python:
        if rpg_ready == False: # quit looping if we don't need to
            for member in rpg_slots:
                if "(Pending)" in member[0]:
                    rpg_ready = False
                    break
                else:
                    rpg_ready = True

    ###################### Bounding box for everything

    text "{size=+24}Select Your Characters!":
        xalign 0.5
        yalign 0.04
        text_align 0.5

    frame:
        background None
        xsize 0.9 ysize 0.75
        xalign 0.5 yalign 0.5

        grid 1 2:
            xalign 0.5
            vbox:
                xalign 0.5

                ###################### Selectable characters go here
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
                                # Sandbag doesn't go here
                                if character.display_name != "Sandbag":
                                    $ portrait = character.portrait.filename

                                    # This bit is stupid lmao
                                    if portrait == "gui/rpg/portraits/blank.png":
                                        $ hover_portrait = "selectable:gui/rpg/portraits/blank_hover.png"
                                    else:
                                        $ hover_portrait = "selectable:"+portrait

                                    imagebutton:
                                        xysize(88,88)
                                        idle portrait
                                        hover hover_portrait
                                        hover_sound "audio/sfx/sfx_select.ogg"
                                        hovered [
                                            SetScreenVariable("rpg_hovered_data", [character.name, character])
                                        ]
                                        unhovered  [
                                            SetScreenVariable("rpg_hovered_data", [])
                                        ]
                                        action [
                                            Play("sound", "audio/sfx/sfx_valid.ogg"),
                                            Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, rpg_hovered_data),
                                            SetScreenVariable("rpg_selected_slot", rpg_slot_autoselect(rpg_slots, rpg_selected_slot)),
                                            With(determination)
                                        ]

                            ###################### Handle empty portrait slots here
                            python:
                                unused_slots = ((17*4)-2)-len(RPG.Characters.characters)
                            for f in range(unused_slots):
                                add Null(88,88)

                            ###################### Handler for special buttons

                            ### Random
                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/unknown.png"
                                hover "selectable:gui/rpg/portraits/unknown.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered [
                                    SetScreenVariable("rpg_hovered_data", ["(Random)", RPG.Characters.random()])
                                ]
                                unhovered  [
                                    SetScreenVariable("rpg_hovered_data", [])
                                ]
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, ["(Random)", RPG.Characters.random() ]),
                                    SetScreenVariable("rpg_selected_slot", rpg_slot_autoselect(rpg_slots, rpg_selected_slot)),
                                    With(determination)
                                ]

                            ### For leaving slots deliberately empty
                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/none.png"
                                hover "selectable:gui/rpg/portraits/none.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered SetScreenVariable("rpg_hovered_data", ["(None)", None])
                                unhovered SetScreenVariable("rpg_hovered_data", [])
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, rpg_hovered_data),
                                    SetScreenVariable("rpg_selected_slot", rpg_slot_autoselect(rpg_slots, rpg_selected_slot)),
                                    With(determination)
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
                                            SetScreenVariable("rpg_selected_slot", a),
                                            SelectedIf( SetScreenVariable("rpg_selected_slot", a) )
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


                        ###################### Display currently hovered character
                        frame:
                            xanchor 0.5 yanchor 1.0
                            xpos 0.5 ypos 1.0
                            xsize 0.5
                            background None

                            if rpg_hovered_data == "":
                                background None
                            else:
                                # Handle random/none first
                                if rpg_hovered_data:
                                    if rpg_hovered_data[0] == "(Random)":
                                        add "gui/rpg/random.png":
                                            xysize(400,400)
                                            fit("contain")
                                            xanchor 0.5 yanchor 1.0
                                            xpos 0.5 ypos 0.8
                                    elif rpg_hovered_data[0] == "(None)":
                                        add "gui/rpg/none.png":
                                            xysize(400,400)
                                            fit("contain")
                                            xanchor 0.5 yanchor 1.0
                                            xpos 0.5 ypos 0.8
                                    else:
                                        python:
                                            try:
                                                if len(rpg_hovered_data[1].anim_sprite) > 0:
                                                    hovered_char_sprite = rpg_hovered_data[1].anim_sprite
                                            except:
                                                hovered_char_sprite = rpg_hovered_data[1].sprite

                                        add hovered_char_sprite:
                                            xysize(500,400)
                                            fit("contain")
                                            xanchor 0.5 yanchor 1.0
                                            xpos 0.5 ypos 1.0
                                    frame:
                                        xanchor 0.5 yanchor 1.0
                                        xpos 0.5 ypos 1.0
                                        text rpg_hovered_data[0]:
                                            text_align 0.5

    ######################### BOTTOM



    ################################################### DEBUG BUTTONS
    textbutton "[[DEBUG] Toggle ready state.":
        yoffset 50 xoffset 25
        action [
            SetScreenVariable("rpg_ready", (not rpg_ready) )
        ]

    python:
        if rpg_ready == True:
            ready_transform = _rpg_ready_button_yes
        else:
            ready_transform = _rpg_ready_button_no

    # Debug only
    if rpg_ready == True:
        textbutton "[[DEV] Skip aesthetic screens":
            xoffset 1395 yoffset 950
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetScreenVariable("rpg_selection_stage", "fight"),
                SetScreenVariable("rpg_bgm", random.choice(list(MUSIC_MAP.keys())))
            ]
    ################################################### END DEBUG BUTTONS

    imagebutton:
        insensitive "sepia:gui/rpg/ready.png"
        idle "gui/rpg/ready.png"
        hover "selectable:gui/rpg/ready.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        action [
            SensitiveIf(rpg_ready == True),
            Play("sound", "audio/sfx/sfx_valid.ogg"),
            Notify("Awawa!")
        ]
        at ready_transform

    ################################################### START FIGHT
    textbutton "BEGIN!":
        xoffset 1674 yoffset 1000
        action [
            Play("sound", "audio/sfx/sfx_valid.ogg"),
            Hide("rpg_char_sel_new", dissolve),
            Hide("category_welcome", dissolve),

            # Move all these to the global versions so we can call the screen in a new context and skip the UI stack nonsense
            # Also attempt to force-clear parties again (it didn't work)
            SetVariable("rpg_party", []),
            SetVariable("rpg_party", rpg_final_party),

            Start("_rpg_battle")
        ]
