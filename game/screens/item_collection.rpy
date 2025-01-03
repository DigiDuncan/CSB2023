##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    from math import ceil

    for n in persistent.collected:
        if n not in ITEM_MAP:
            print(f"WARNING: Item '{n}' not in ITEM_MAP!")

    max_y = math.ceil( len(ITEM_MAP.keys()) / 5 )

    def mark_read(k):
        persistent.read.add(k)

screen item_collection():
    default current_item = None

    tag menu
    use item_nav

    if current_item == None:
        use item_welcome
    
    else:
        use items(current_item)

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

            grid 5 max_y:
                for k in ITEM_MAP:
                    # determine thumbnail from whether you have unlocked the given item
                    if k in persistent.collected:
                        $ item_img = Transform(ITEM_MAP[k]['img'], size=(120,120), fit="contain", xalign=0.5, yalign=0.5, matrixcolor=None)
                    else:
                        $ item_img = Transform(ITEM_MAP[k]['img'], size=(120,120), fit="contain", xalign=0.5, yalign=0.5, matrixcolor=sil_black_matrix)

                    # create the bounding box for each button
                    frame:
                        background None
                        margin 5, 5
                        xysize 153, 153
                        
                        # create the actual button here
                        button:
                            idle_background "#003D51"
                            hover_background "#0099CC"
                            selected_idle_background "#65C0DF"
                            insensitive_background "#888888"

                            xalign 0.5 yalign 0.5
                            xysize 140,140

                            image item_img
                            
                            action [ SensitiveIf( k in persistent.collected ), SetScreenVariable("current_item", k) ]
                            
    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

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
        text "Check out all this neat stuff you've found!\n([unlocked_item_count]/[item_count] unlocked)"

##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------

screen items(l):

    # Main Container omitting the menu
    viewport:
        xsize 800
        ysize 900
        xalign 0.6
        xoffset 340
        yoffset 200
        side_yfill False
        mousewheel False
        draggable False
        pagekeys False
        vbox:
            yfill False
            spacing 100
            xsize 800

            # Handling the text
            python:
                try:
                    if ITEM_MAP[l].get('dx', False):
                        fetched_desc = "{image=gui/dx_text.png} " + ITEM_MAP[l]["desc"]
                    elif ITEM_MAP[l].get('ce', False):
                        fetched_desc = "{image=gui/ce_text.png} " + ITEM_MAP[l]["desc"]
                    else:
                        fetched_desc = ITEM_MAP[l]["desc"]
                except:
                    fetched_desc = "This item didn't load correctly. Ask Tate to fix this..."

            # Bounding box for item and description
            vbox:
                frame:
                    background None
                    xsize 1.0 ysize 300
                    xalign 0.5 yalign 0.5
                    image Transform(ITEM_MAP[l]['img'], size=(640, 240), fit="contain"):
                        xalign 0.5 yalign 0.5

                first_spacing 10
                text "{size=+24}" + ITEM_MAP[l]['name']:
                    xalign 0.5
                    
                text "{size=-12}(" + ITEM_MAP[l]['rarity'] + ")":
                    xalign 0.5
                    color("#BBBBBB")

                text "\nOwner: " + ITEM_MAP[l]['owner'] + "\n\n" + fetched_desc
