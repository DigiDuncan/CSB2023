##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    def mark_read(k):
        persistent.read.add(k)

init python:
    import json
    with renpy.open_file('item_collection.json') as json_file:
        item_map = json.load(json_file)

    for n in persistent.seen:
        if n not in item_map:
            print(f"WARNING: Item '{n}' not in item_map!")

screen item_nav():
    add Color('#323e42', alpha=0.75)
    text "{size=+12}Item Collection":
        xpos 0.125 ypos 80
        
    viewport:
        xpos 25 ypos 150
        xsize 800 ysize 750
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
                    vbox:
                        xsize 150 ysize 150
                        # code by robcolton
                        image Transform(item_map[k]['img'], size=(100,100), fit="contain"):
                            xalign 0.5 yalign 0.5

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
        # TODO: need new persistent to handle items i guess
        unlocked_item_count = len(persistent.seen)
    vbox:
        xsize 600
        xalign 0.5 yalign 0.5
        xoffset 400
        text "Check out all this neat stuff you've found!"
        text "([unlocked_item_count]/[item_count] unlocked)"

##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------

screen items(l):

    style_prefix "codex"

    # TODO: make this line easier to read somehow
    label item_map[l]['name']

    tag menu
    use item_nav

    # Main Container omitting the menu
    viewport:

        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        side_yfill False
        mousewheel True
        draggable True
        pagekeys True
        hbox:
            ysize 800
            vbox:
                yfill False
                spacing 100
            # Handling the text
                xsize 800
                python:
                    try:
                        if "dx" in item_map[l]:
                            fetched = "{image=gui/dx_text.png}" + item_map["name"] + "(" + item_map[l]["rarity"] + ")"
                        else:
                            fetched = item_map["name"] + "(" + item_map[l]["rarity"] + ")"
                    except:
                        fetched = "This item didn't load correctly. Ask Digi to fix the game."
                text (fetched)

            python:
                z = item_map[l].get("zoom", 1.0) * 0.75
            add item_map[l]['img'] xalign 1.0 yalign 1.0 zoom z
