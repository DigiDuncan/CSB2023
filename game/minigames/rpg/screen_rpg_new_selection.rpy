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

        # advance the slot
        if current_slot < 8:
            current_slot += 1
        else:
            # make ready
            for slot in slot_list:
                if slot != '' and len(slots) == 8:
                    toggle_ready(ready_var)

    rpg_selected_slot = 0
    rpg_slots = []
    rpg_ready = False

    portrait_exclude = ["gui/rpg/portraits/blank_hover.png", "gui/rpg/portraits/unknown.png", "gui/rpg/portraits/none.png"]

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

screen rpg_char_sel_new():

    default hovered_character = Tooltip("")
    default hovered_character_sprite = ""

    $ rpg_slots = ["CS","Arceus","Tate", "Digi", "Wesley", "Ed", "Richard", "Copguy"]  # test values only

    ### add background color, kill music
    add Color('#323e42', alpha=0.75)
    $renpy.music.stop()

    text "{size=+12}Select Your Characters!":
        xalign 0.5
        yalign 0.05
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
                                if portrait in portrait_exclude:
                                    continue

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
                                    hovered [ hovered_character.Action(character.name), SetVariable(hovered_character_sprite, character.sprite), SetScreenVariable(hovered_character_sprite, character.sprite) ]
                                    action [ Play("sound", "audio/sfx/sfx_valid.ogg") ]

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
                                hovered [ hovered_character.Action("(Random)"), SetVariable(hovered_character_sprite, "gui/rpg/portraits/unknown.png"), SetScreenVariable(hovered_character_sprite, "gui/rpg/portraits/unknown.png") ]
                                action [ Play("sound", "audio/sfx/sfx_valid.ogg") ]

                            imagebutton:
                                xysize(88,88)
                                idle "gui/rpg/portraits/none.png"
                                hover "selectable:gui/rpg/portraits/none.png"
                                hover_sound "audio/sfx/sfx_select.ogg"
                                hovered [ hovered_character.Action("(None)"), SetVariable(hovered_character_sprite, "gui/rpg/portraits/none.png"), SetScreenVariable(hovered_character_sprite, "gui/rpg/portraits/none.png") ]
                                action [ Play("sound", "audio/sfx/sfx_valid.ogg") ]


                    ### Show selected characters
                    ### Slots 0-3 are allies, 4-7 are enemies
                    frame:
                        background None
                        xsize 1.0 ysize 1.0
                        xanchor 0.5 yanchor 0.5
                        xpos 0.5 ypos 1.6

                        $ party_size = 4

                        # allies
                        frame:
                            background None
                            xsize 0.5 xoffset 10
                            text "Allies"

                            # Selected character portraits
                            grid 4 1:
                                ypos 0.15
                                spacing 10
                                for a in range(party_size):
                                    imagebutton:
                                        idle "gui/rpg/portraits/blank.png"
                                        hover "selectable:gui/rpg/portraits/blank.png"
                                        hover_sound "audio/sfx/sfx_select.ogg"

                            # Selected character text
                            $ output_text = ""
                            for a in range(0, 4):
                                $ output_text += rpg_slots[a]+"\n"

                            text output_text:
                                ypos 0.4

                        # enemies
                        frame:
                            background None
                            xsize 0.5 xoffset -10
                            xalign 1.0
                            text "Enemies":
                                xalign 1.0

                            # Selected character portraits
                            grid 4 1:
                                xalign 1.0
                                ypos 0.15
                                spacing 10
                                for e in range(party_size):
                                    imagebutton:
                                        idle "gui/rpg/portraits/blank.png"
                                        hover "selectable:gui/rpg/portraits/blank.png"
                                        hover_sound "audio/sfx/sfx_select.ogg"

                            # Selected character text
                            $ output_text = ""
                            for e in range(4, 8):
                                $ output_text += rpg_slots[e]+"\n"

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
                                add Image(character.sprite): # this does not work yet
                                    xysize(400,500)
                                    fit("contain")
                                    xanchor 0.5 yanchor 1.0
                                    xpos 0.5 ypos 1.0
                                frame:
                                    xanchor 0.5 yanchor 1.0
                                    xpos 0.5 ypos 1.0
                                    text hovered_character.value:
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

