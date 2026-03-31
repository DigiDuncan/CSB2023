##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    for n in persistent.collected:
        if n not in ITEM_MAP:
            logger.warn(f"Item '{n}' not in ITEM_MAP!")

    def mark_read(k):
        persistent.read.add(k)

screen item_collection():
    default current_item = None

    tag menu

    if "main_menu":
        add gui.game_menu_background
    add gui_theme_map["screen_transparency_layer"]

    text _("Item Collection"):
        style "game_menu_label_text"
        xpos 25 ypos 80

    use item_nav

    if current_item == None:
        use item_welcome

    else:
        use items(current_item)

screen item_nav():
    default loaded_imgs = 0
    default loaded_state = "loading"

    # Attempt to preload items
    on "show":
        action [
            If(not preferences.craptop_mode, Function(start_predict_list, [i["img"] for i in ITEM_MAP.values()]), None)
        ]

    ###################### Load images first
    if loaded_state == "loading":
        if loaded_imgs < len(ITEM_MAP):
            timer 0.001:
                repeat True
                action Function(predict_img, [i["img"] for i in ITEM_MAP.values()])
            $ loaded_imgs += 1
            $ load_percent = str( int((loaded_imgs * 100) / len(ITEM_MAP)) )

            frame:
                background None
                xpos 0.19 ypos 0.5
                text _("Fetching Items...\n"+load_percent+"%"):
                    xalign 0.5 yalign 0.5
                    text_align 0.5
        else:
            frame:
                background None
                xpos 0.17 ypos 0.5
                text "Preparing Collection...":
                    xalign 0.5 yalign 0.5
                    text_align 0.5

            # I have no idea why this needs a timer but it won't move on otherwise
            timer 0.001:
                action Function( SetScreenVariable("loaded_state", "ready") )
            $ loaded_state = "ready"

    ###################### Actually show items
    elif loaded_state == "ready":
        viewport:
            xpos 125 ypos 150
            xsize 785 ysize 750
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            scrollbars "vertical"

            vbox:
                spacing 10
                xoffset 350
                $ counter = 0
                $ xstart = 0
                $ ystart = 0

                vpgrid:
                    cols 5

                    for k in ITEM_MAP:
                        # Determine thumbnail from whether you have unlocked the given item
                        if k in persistent.collected:
                            $ item_img = Transform(ITEM_MAP[k]['img'], size=(120,120), fit="contain", xalign=0.5, yalign=0.5, matrixcolor=None)
                        else:
                            $ item_img = Transform(ITEM_MAP[k]['img'], size=(120,120), fit="contain", xalign=0.5, yalign=0.5, matrixcolor=sil_black_matrix)

                        # Create the bounding box for each button
                        frame:
                            background None
                            margin 5, 5
                            xysize 153, 153

                            # Create the actual button here
                            button:
                                idle_background gui_theme_map["image_button_idle"]
                                hover_background gui_theme_map["image_button_hover"]
                                selected_idle_background gui_theme_map["image_button_selected_idle"]
                                selected_hover_background gui_theme_map["image_button_selected_hover"]
                                insensitive_background gui_theme_map["image_button_insensitive"]

                                xalign 0.5 yalign 0.5
                                xysize 140,140

                                image item_img

                                action [
                                    SensitiveIf( k in persistent.collected ),
                                    SetScreenVariable("current_item", k)
                                ]
    else: # This should NEVER happen!
        $ renpy.jump("secret_dx")

    textbutton _("Back"):
        yoffset 950 xoffset 25
        action ShowMenu("category_welcome")
    textbutton _("Main Menu"):
        yoffset 1000 xoffset 25
        action Return()

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------

screen item_welcome():
    ##This is the "Item Collection" category's welcome page. This is the first screen players see after they select a category.

    style_prefix "codex"
    python:
        item_count = len(ITEM_MAP.keys())
        unlocked_item_count = len(persistent.collected)
    vbox:
        xsize 775
        xalign 0.5 yalign 0.5
        xoffset 450
        text _("Check out all this neat stuff you've found!\n([unlocked_item_count]/[item_count] unlocked)")

##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------

screen items(l):

    # Main Container omitting the menu
    frame:
        background None
        xsize 800 ysize 900
        xalign 0.6
        xoffset 340 yoffset 150
        vbox:
            yfill False
            spacing 100
            xsize 800

            # Handling the text
            python:
                try:
                    if ITEM_MAP[l].get('dx', False):
                        fetched_desc = "{image=gui/inline_text/dx_text.png} " + ITEM_MAP[l]["desc"]
                    elif ITEM_MAP[l].get('ce', False):
                        fetched_desc = "{image=gui/inline_text/ce_text.png} " + ITEM_MAP[l]["desc"]
                    else:
                        fetched_desc = ITEM_MAP[l]["desc"]
                except:
                    fetched_desc = "This item didn't load correctly. Ask Tate to fix this..."

            # Bounding box for item and description
            vbox:
                frame:
                    background None
                    xsize 1.0 ysize 300
                    xalign 0.5 yalign 0
                    image Transform(ITEM_MAP[l]['img'], size=(640, 240), fit="contain"):
                        xalign 0.5 yalign 0.5

                first_spacing 10
                text "{size=+24}" + ITEM_MAP[l]['name']:
                    xalign 0.5

                text "{size=-12}(" + ITEM_MAP[l]['rarity'] + ")":
                    xalign 0.5
                    color gui_theme_map["idle_small_color"]

                text _("\nOwner: ") + ITEM_MAP[l]['owner'] + "\n\n" + fetched_desc
