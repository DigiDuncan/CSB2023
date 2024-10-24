##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    import json
    with renpy.open_file('item_collection.json') as json_file:
        item_map = json.load(json_file)

    for n in persistent.collected:
        if n not in item_map:
            print(f"WARNING: Item '{n}' not in item_map!")

    def mark_read(k):
        persistent.read.add(k)

screen item_nav():
    add Color('#323e42', alpha=0.75)
    text "{size=+12}Item Collection":
        xpos 0.18 ypos 80

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
            
            $ from math import ceil
            $ max_y = math.ceil( len(item_map.keys()) / 5 )

            grid 5 max_y:
                for k in item_map:

                    # color list:
                    # insensitive - #888888
                    # sensitive idle - #003D51
                    # sensitive hover - #0099CC
                    # sensitive selected - #65C0DF

                    # generate assets
                    if k in persistent.collected:
                        $ buttoncolor = "#003D51"
                        $ item_img = Transform(item_map[k]['img'], size=(120,120), fit="contain", xalign=0.5, yalign=0.5, matrixcolor=None)
                    else:
                        $ buttoncolor = "#888888"
                        $ item_img = Transform(item_map[k]['img'], size=(120,120), fit="contain", xalign=0.5, yalign=0.5, matrixcolor=sil_black_matrix)

                    # create the bounding box for each button
                    frame:
                        margin 5, 5
                        background Solid(buttoncolor)
                        xsize 153 ysize 153
                        
                        image item_img

                        # the actual button here
                        button:
                            xalign 0.5 yalign 0.5
                            
                            action [ SensitiveIf( k in persistent.collected ), ShowMenu("items", k) ]

                            hovered SetVariable("buttoncolor","#0099CC")
                            unhovered SetVariable("buttoncolor","#003D51")
                            
    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------

screen item_welcome():
    ##This is the "Item Collection" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use item_nav

    style_prefix "codex"
    python:
        item_count = len(item_map.keys())
        unlocked_item_count = len(persistent.collected)
    vbox:
        xsize 775
        xalign 0.5 yalign 0.5
        xoffset 450
        text "Check out all this neat stuff you've found!\n([unlocked_item_count]/[item_count] unlocked)"

##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------

screen items(l):

    style_prefix "codex"

    tag menu
    use item_nav

    # Main Container omitting the menu
    viewport:
        xsize 800
        ysize 750
        xalign 0.6
        xoffset 305 
        yoffset 200
        side_yfill False
        mousewheel True
        draggable True
        pagekeys True
        hbox:
            ysize 750
            vbox:
                yfill False
                spacing 100
                xsize 800

                # Handling the text
                python:
                    try:
                        if "dx" in item_map[l]:
                            fetched_desc = "{image=gui/dx_text.png} " + item_map[l]["desc"]
                        else:
                            fetched_desc = item_map[l]["desc"]
                    except:
                        fetched_desc = "This item didn't load correctly. Ask Tate to fix this..."

                # Bounding box for item and description
                vbox:
                    frame:
                        background None
                        xsize 1.0 ysize 300
                        xalign 0.5 yalign 0.5
                        image Transform(item_map[l]['img'], size=(640, 240), fit="contain"):
                            xalign 0.5 yalign 0.5
                
                    text "{size=+24}" + item_map[l]['name']:
                        xalign 0.5

                    text "{size=-12}(" + item_map[l]['rarity'] + ")":
                        xalign 0.5

                    text "\nOwner: " + item_map[l]['owner'] + "\n\n" + fetched_desc

            python:
                z = item_map[l].get("zoom", 1.0) * 0.75
            add item_map[l]['img'] xalign 1.0 yalign 1.0 zoom z
