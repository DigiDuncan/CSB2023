##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    def mark_read(k):
        persistent.read.add(k)

init python:
    import json
    with renpy.open_file('bios.json') as json_file:
        name_map = json.load(json_file)

    for n in persistent.seen:
        if n not in name_map:
            print(f"WARNING: Bio '{n}' not in name_map!")

screen people_nav():
    add Color('#323e42', alpha=0.75)
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
            for k in name_map:
                if k in persistent.seen:
                    python:
                        # DX character handler
                        # please rewrite this better if you can? - tate
                        try:
                            if name_map[k]['dx'] == True:
                                name_label = "{image=unread.png}{image=gui/dx_text.png} " + name_map[k]['full_name'] if k not in persistent.read else "{image=gui/dx_text.png} " + name_map[k]['full_name']
                        except:
                            name_label = "{image=unread.png}" + name_map[k]['full_name'] if k not in persistent.read else name_map[k]['full_name']
                    if k == "iris":
                        textbutton name_label action Function(mark_read, k), ShowMenu("person", k), ShowMenu("fake_error", "people.rpy", 126, "`bios/iris.txt` could not be rendered as a Text object.", "Hi, I'm Iris, a cosmic being with interest in the happenings of this reality, as well as some of the people involved in this story.\nDoes that sound too formal? I don't know. Hey, Digi, writing this shit's hard. You can fill in the rest from here.", _transition = determination)
                    else:
                        textbutton name_label action Function(mark_read, k), ShowMenu("person", k)

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------

screen people_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use people_nav

    style_prefix "codex"
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

    style_prefix "codex"

    tag menu
    use people_nav

    text name_map[l]['full_name']:
            xalign 0.65
            yalign 0.05
            size 69

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
                text "\"" + name_map[l]["quote"] + "\""
                python:
                    try:
                        if "dx_bio" in name_map[l]:
                            fetched = name_map[l]["bio"] + "\n\n{image=gui/dx_text.png} " + name_map[l]["dx_bio"]
                        else:
                            fetched = name_map[l]["bio"]
                    except:
                        fetched = "The bio didn't load correctly. Ask Digi to fix the game."
                text (fetched)

            python:
                z = name_map[l].get("zoom", 1.0) * 0.75
                x = -1 if name_map[l].get("flip", False) else 1
                xo = name_map[l].get("xoffset", 0)
                yo = name_map[l].get("yoffset", 0)
            add name_map[l]['sprite_path'] xalign 1.0 yalign 1.0 zoom z xzoom x xoffset xo yoffset yo
