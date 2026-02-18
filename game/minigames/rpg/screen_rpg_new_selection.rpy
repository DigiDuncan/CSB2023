label awawa_rpg_select_test:
    call screen rpg_char_sel_new with dissolve

init python:
    # ready up (will be combined with the function below later)
    def toggle_ready(r):
        if r == True:
            return False
        else:
            return True

    # fill a slot
    def rpg_fill_slot(slots_list, current_slot, character, ready_var):

        # fill the slot
        slots_list[current_slot] = character

        # advance the slot if the next one empty
        if current_slot < 8 and current_slot is None:
            current_slot += 1
        else:
            # make ready
            for slot in slot_list:
                if slot != '' and len(slots) == 8:
                    toggle_ready(ready_var)

    rpg_slots = [ ]
    rpg_selected_slot = 0
    rpg_ready = False

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
    $ rpg_pending_sprite_hover = "selectable:gui/rpg/portraits/pending.png"

    # variables
    default hovered_character = Tooltip("")
    default rpg_slots = [ None, None, None, None, None, None, None, None ]
    default rpg_selected_slot = 0
    default rpg_ready = False

    ### add background color, kill music
    # TODO: bgm
    add Color('#323e42', alpha=0.75)
    showif rpg_ready == True:
        add Movie(size=(1920,1080), play="movies/Fire.webm", side_mask=True) at _rpg_ready_flames

    $ renpy.music.stop()

    text "{size=+24}Select Your Characters!":
        xalign 0.5
        yalign 0.04
        text_align 0.5

    ### bounding box for everything
    frame:
        background None
        xsize 0.9 ysize 0.75
        xalign 0.5 yalign 0.5

        grid 1 2:
            xalign 0.5
            vbox:
                xalign 0.5

                ### selectable characters go here
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
                                    action [ Play("sound", "audio/sfx/sfx_valid.ogg") ]
                                    # Function(rpg_fill_slot, rpg_slots, rpg_selected_slot, getattr(RPG.Characters, character.assigned_name), rpg_ready)

                            ### handle empty slots here
                            python:
                                unused_slots = ((17*4)-2)-len(RPG.Characters.characters)
                            for f in range(unused_slots):
                                add Null(88,88)

                            ### handle random/skipped characters
                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/unknown.png"
                                hover "selectable:gui/rpg/portraits/unknown.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered [ hovered_character.Action(["(Random)", RPG.Characters.random() ]) ]
                                action [ Play("sound", "audio/sfx/sfx_valid.ogg"), Notify(hovered_character.value) ]

                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/none.png"
                                hover "selectable:gui/rpg/portraits/none.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered [ hovered_character.Action(["(None)", None]) ]
                                action [ Play("sound", "audio/sfx/sfx_valid.ogg") ]


                    ### Show selected characters
                    ### Slots 0-3 are allies, 4-7 are enemies
                    frame:
                        background None
                        xsize 1.0 ysize 1.0
                        xanchor 0.5 yanchor 0.5
                        xpos 0.5 ypos 1.6

                        $ party_size = 4

                        ### Allies
                        frame:
                            background None
                            xsize 0.5 xoffset 10
                            text "{size=+8}Allies"

                            # Selected character portraits
                            grid 4 1:
                                ypos 0.15
                                spacing 10
                                for a in range(party_size):
                                    imagebutton:
                                        if rpg_slots[a] is None:
                                            idle rpg_pending_sprite
                                            hover rpg_pending_sprite_hover
                                        else:
                                            idle rpg_pending_sprite
                                            #idle rpg_slots[a].portrait
                                            #hover "selectable:"+rpg_slots[a].portrait

                                        hover_sound "audio/sfx/sfx_select.ogg"
                                        action [ SetVariable("rpg_selected_slot", a), SetScreenVariable("rpg_selected_slot", a), Notify(rpg_selected_slot) ]

                            # Selected character text
                            $ output_text = ""
                            for a in range(party_size):
                                if rpg_slots[a] is None:
                                    $ output_text += "(None)\n"
                                else:
                                    $ output_text += rpg_slots[a]+"\n"

                            text output_text:
                                ypos 0.4

                        ### Enemies
                        frame:
                            background None
                            xsize 0.5 xoffset -10
                            xalign 1.0
                            text "{size=+8}Enemies":
                                xalign 1.0

                            # Selected character portraits
                            grid 4 1:
                                xalign 1.0
                                ypos 0.15
                                spacing 10
                                for e in range(party_size):
                                    imagebutton:
                                        if rpg_slots[e+4] is None:
                                            idle rpg_pending_sprite
                                            hover rpg_pending_sprite_hover
                                        else:
                                            idle rpg_pending_sprite
                                            #idle rpg_slots[e].portrait
                                            #hover "selectable:"+rpg_slots[e+4].portrait

                                        hover_sound "audio/sfx/sfx_select.ogg"
                                        action [ SetVariable("rpg_selected_slot", e+4), SetScreenVariable("rpg_selected_slot", e+4), Notify(rpg_selected_slot) ]

                            # Selected character text
                            $ output_text = ""
                            for e in range(party_size):
                                if rpg_slots[e+4] is None:
                                    $ output_text += "(None)\n"
                                else:
                                    $ output_text += rpg_slots[e+4]+"\n"

                            text output_text:
                                ypos 0.4
                                xalign 1.0
                                text_align 1.0

                        ### display currently hovered character
                        frame:
                            xanchor 0.5 yanchor 1.0
                            xpos 0.5 ypos 1.0
                            xsize 0.5
                            background None

                            if hovered_character.value == "" or rpg_ready == True:
                                background None
                            else:
                                # handle random/none first

                                if hovered_character.value and hovered_character.value[1]:
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

    ### buttons
    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

    # debug button only
    textbutton "Click to toggle ready state.":
        yoffset 50 xoffset 25
        action [
            SetScreenVariable("rpg_ready", toggle_ready(rpg_ready)),
            SetVariable("rpg_ready", toggle_ready(rpg_ready))
        ]

    if rpg_ready == True:
        $ ready_transform = _rpg_ready_button_yes
    else:
        $ ready_transform = _rpg_ready_button_no

    imagebutton:
        insensitive "sepia:gui/rpg/ready.png"
        idle "gui/rpg/ready.png"
        hover "selectable:gui/rpg/ready.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        action [ SensitiveIf(rpg_ready == True), Play("sound", "audio/sfx/sfx_valid.ogg") ]
        at ready_transform

