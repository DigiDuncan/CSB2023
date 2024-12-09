##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    def mark_read(k):
        persistent.read.add(k)

init python:
    import json
    with renpy.open_file('data/bios.json') as json_file:
        name_map = json.load(json_file)

    for n in persistent.seen:
        if n not in name_map:
            print(f"WARNING: Bio '{n}' not in name_map!")

screen people():
    default current_person = None

    use people_nav
    tag menu

    if current_person == None:
        use people_welcome
    else:
        use person(current_person)

screen people_nav():
    add Color('#323e42', alpha=0.75)
    
    # sorting modes
    # 0 = sort by character name, NOT by json name (default)
    # 1 = RPG characters only
    # maybe future sort modes will be added, but, not now.

    if current_bios_sorting_mode == 0:
        $ sort_mode = sorted(persistent.seen, key=lambda character: name_map[character]["full_name"].upper())
        $ sort_text = "Sort By: Name"
    # elif current_bios_sorting_mode == 1:
        # if "rpg" in name_map[character]:
            # $ sort_mode = sorted(persistent.seen, key=lambda character: name_map[character]["full_name"].upper())
        # $ sort_text = "RPG Characters Only"

    frame:
        background None
        xsize 500 ysize 50
        xpos 25 ypos 75

        if current_bios_sorting_mode > 0:

            imagebutton:
                xalign 0.0 yalign 0.5
                xysize 64, 64

                idle "/gui/left_off_small.png"
                hover "/gui/left_on_small.png"

                if current_bios_sorting_mode-1>=0:
                    action SetVariable("current_bios_sorting_mode", current_bios_sorting_mode-1)
        
        # Change this when there's more modes added
        if current_bios_sorting_mode < 1:
            imagebutton:
                xalign 1.0 yalign 0.5
                xysize 64, 64

                idle "/gui/right_off_small.png"
                hover "/gui/right_on_small.png"

                if current_bios_sorting_mode+1<2:
                    action SetVariable("current_bios_sorting_mode", current_bios_sorting_mode+1)

        text sort_text:
            xalign 0.5 yalign 0.5
            text_align 0.5

    viewport:
        xpos 25 ypos 150
        xsize 500 ysize 700
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350

            for k in sort_mode:
                python:
                    # DX/CE character handler
                    if name_map[k].get('dx', False):
                        name_label = "{image=unread.png}{image=gui/dx_text.png} " + name_map[k]['full_name'] if k not in persistent.read else "{image=gui/dx_text.png} " + name_map[k]['full_name']
                    elif name_map[k].get('ce', False):
                        name_label = "{image=unread.png}{image=gui/ce_text.png} " + name_map[k]['full_name'] if k not in persistent.read else "{image=gui/ce_text.png} " + name_map[k]['full_name']
                    else:
                        name_label = "{image=unread.png}" + name_map[k]['full_name'] if k not in persistent.read else name_map[k]['full_name']
                if k == "iris":
                    textbutton name_label action Function(mark_read, k), SetScreenVariable("current_person", k), ShowMenu("fake_error", "people.rpy", 126, "`bios/iris.txt` could not be rendered as a Text object.", "Hi, I'm Iris, a cosmic being with interest in the happenings of this reality, as well as some of the people involved in this story.\nDoes that sound too formal? I don't know. Hey, Digi, writing this shit's hard. You can fill in the rest from here.", _transition = determination)
                else:
                    textbutton name_label action Function(mark_read, k), SetScreenVariable("current_person", k)

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------

screen people_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    python:
        bio_count = len(name_map.keys())
        unlocked_bio_count = len(persistent.seen)
    vbox:
        xsize 850
        xalign 0.5 yalign 0.5
        xoffset 200
        text "View bios about all the wacky characters you've seen!"
        text "([unlocked_bio_count]/[bio_count] unlocked)"

##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------

screen person(l):

    ##### Main Container omitting the menu
    viewport:
        xsize 1350
        ysize 900
        xalign 0.5
        xoffset 265 
        yoffset 100
        side_yfill False
        mousewheel True
        draggable False
        pagekeys True

        ##### bounding box for content
        frame:
            background None
            xsize 1.0
            ysize 1.0

            ### name
            text name_map[l]['full_name']:
                xalign 0.5
                yalign 0.0
                size 69

            ### pronouns, if present
            python:
                try:
                    if "pronouns" in name_map[l]:
                        pronouns = name_map[l]['pronouns']
                    else:
                        pronouns = ""
                except:
                    pronouns = ""

            text pronouns:
                xalign 0.5
                yalign 0.08
                size 32
                color "#BBBBBB"

            ### bio text
            hbox:
                ysize 800
                ypos 100
                vbox:
                    yfill False
                    xsize 800
                    spacing 28
                    # Handling the text, hopefully fixing the weird spacing in the process
                    frame:
                        background None
                        text "\"" + name_map[l]["quote"] + "\""
                    frame:
                        background None
                        python:
                            try:
                                if "dx_bio" in name_map[l]:
                                    fetched = name_map[l]["bio"] + "\n\n{image=gui/dx_text.png} " + name_map[l]["dx_bio"]
                                else:
                                    fetched = name_map[l]["bio"]
                            except:
                                fetched = "The bio didn't load correctly. Ask Digi to fix the game."
                        text (fetched)

            ### sprite displayer
            python:
                z = name_map[l].get("zoom", 1.0) * 0.75
                x = -1 if name_map[l].get("flip", False) else 1
                xo = name_map[l].get("xoffset", 0)
                yo = name_map[l].get("yoffset", 0) - 100
            add name_map[l]['sprite_path'] xalign 1.0 yalign 1.0 zoom z xzoom x xoffset xo yoffset yo
