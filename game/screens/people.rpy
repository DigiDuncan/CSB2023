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
    default current_bios_sprite = None

    use people_nav
    tag menu

    if current_person == None:
        use people_welcome
    else:
        use person(current_person)

screen people_nav():
    default current_bios_sprite = None
    add Color('#323e42', alpha=0.75)

    python:
        # sorting modes
        # 0 = sort by character name, NOT by json name (default)
        # 1 = RPG characters only
        # 2 = new to DX only
        # 3 = new to CE only
        # maybe future sort modes will be added

        if current_bios_sorting_mode == 0:
            sort_mode = sorted(persistent.seen, key=lambda character: name_map[character]["full_name"].upper())
            sort_text = "All"
        elif current_bios_sorting_mode == 1:
            presort = []
            for c in name_map:
                if c in persistent.seen:
                    if "rpg" in name_map[c]:
                        presort.append(c)
            sort_mode = sorted(presort, key=lambda character: name_map[character]["full_name"].upper())
            sort_text = "RPG Fighters Only"
        elif current_bios_sorting_mode == 2:
            presort = []
            for c in name_map:
                if c in persistent.seen:
                    if "dx" in name_map[c]:
                        presort.append(c)
            sort_mode = sorted(presort, key=lambda character: name_map[character]["full_name"].upper())
            sort_text = "New To DX"
        elif current_bios_sorting_mode == 3:
            presort = []
            for c in name_map:
                if c in persistent.seen:
                    if "ce" in name_map[c]:
                        presort.append(c)
            sort_mode = sorted(presort, key=lambda character: name_map[character]["full_name"].upper())
            sort_text = "New To CE"

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
        if current_bios_sorting_mode < 3:
            imagebutton:
                xalign 1.0 yalign 0.5
                xysize 64, 64

                idle "/gui/right_off_small.png"
                hover "/gui/right_on_small.png"

                if current_bios_sorting_mode+1<4:
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
                    textbutton name_label action Function(mark_read, k), SetScreenVariable("current_person", k), SetVariable("current_bios_sprite", 0)

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
        ysize 950
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

            ### rpg, if present
            python:
                if "rpg" in name_map[l]:
                    _rpg_var = name_map[l]['rpg']
                    _fighter = getattr(Fighters, _rpg_var)
                    hp = _fighter.health_points
                    attack = _fighter.attack_points
                    defense = _fighter.armor_points
                else:
                    hp = None
                    attack = None
                    defense = None

            ### bounding box for inner content
            frame:
                background None
                xsize 1.0
                ysize 825
                yanchor 1.0
                ypos 1.0

                ### bounding box for bio text
                frame:
                    background None
                    xsize 800
                    ysize 1.0

                    # quote + bio text
                    frame:
                        background None
                        vbox:
                            python:
                                try:
                                    if "dx_bio" in name_map[l]:
                                        fetched = name_map[l]["bio"] + "\n\n{image=gui/dx_text.png} " + name_map[l]["dx_bio"]
                                    else:
                                        fetched = name_map[l]["bio"]
                                except:
                                    fetched = "The bio didn't load correctly. Ask Digi to fix the game."
                            text "\"" + name_map[l]["quote"] + "\"\n\n" + (fetched)

                ### bounding box for sprites and rpg info
                frame:
                    background None
                    xsize 500
                    ysize 1.0
                    xanchor 1.0
                    yanchor 1.0
                    xpos 1.0
                    ypos 1.0

                    python:
                        x = -1 if name_map[l].get("flip", False) else 1
                        yo = -110 if "rpg" in name_map[l] else 0

                    # show sprite
                    frame:
                        background None
                        xsize 1.0
                        ysize 700

                        image name_map[l]['sprites'][list(name_map[l]['sprites'].keys())[current_bios_sprite]]:
                            xalign 0.5
                            yalign 0.0
                            xsize 1.0
                            ysize 1.0
                            xzoom x
                            yoffset yo

                            fit "contain"

                    ### for sprite selection / rpg data
                    frame:
                        background None
                        xsize 1.0
                        ypos 1.0
                        yanchor 1.0

                        vbox:
                            # show sprite selection if available
                            frame:
                                #background None
                                xsize 1.0
                                ysize 100

                                # make sure sprite actually exists first
                                python:
                                    try:
                                        this_sprite = list(name_map[l]['sprites'].keys())[current_bios_sprite]

                                        # delimiter to handle outfit/expression names
                                        # ex. "Default: Happy" will be split
                                        this_sprite_split = this_sprite.split(": ")
                                        
                                        if len(this_sprite_split) > 1:
                                            this_sprite = "{size=-12}" + this_sprite_split[0] + "{/size}\n" + this_sprite_split[1]
                                        else:
                                            this_sprite = this_sprite_split

                                    except:
                                        this_sprite = "Default"
                                        current_bios_sprite = 0

                                # sprite selector 
                                text this_sprite:
                                    xalign 0.5
                                    yalign 0.5
                                    text_align 0.5

                                if len(name_map[l]['sprites'].keys()) > 1:
                                    # left arrow
                                    if current_bios_sprite-1>=0:
                                        imagebutton:
                                            xalign 0.0 yalign 0.5
                                            xysize 64, 64
                                            idle "/gui/left_off_small.png"
                                            hover "/gui/left_on_small.png"
                                            action IncrementVariable("current_bios_sprite", -1)

                                    # right arrow
                                    if current_bios_sprite+1 < len(name_map[l]['sprites']):
                                        imagebutton:
                                            xalign 1.0 yalign 0.5
                                            xysize 64, 64
                                            idle "/gui/right_off_small.png"
                                            hover "/gui/right_on_small.png"
                                            action IncrementVariable("current_bios_sprite")

                            # show rpg data if it exists
                            if "rpg" in name_map[l]:
                                null height 10
                                vbox:
                                    xsize 1.0
                                    frame:
                                        xsize 1.0
                                        background "#f70"
                                        text "{size=-8}RPG Stats"
                                    frame:
                                        xsize 1.0
                                        background "#07f"
                                        hbox:
                                            xalign 0.5
                                            spacing 50

                                            frame:
                                                background "#070"
                                                xsize 100
                                                text str(hp) + "\n{size=-8}HP":
                                                    xalign 0.5
                                                    text_align 0.5
                                            frame:
                                                background "#700"
                                                xsize 100
                                                text str(attack) + "\n{size=-8}ATK":
                                                    xalign 0.5
                                                    text_align 0.5
                                            frame:
                                                background "#007"
                                                xsize 100
                                                text str(defense) + "\n{size=-8}DEF":
                                                    xalign 0.5
                                                    text_align 0.5
