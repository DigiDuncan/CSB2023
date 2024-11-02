# the purpose of this screen is to eventually replace endings replay and minigames replay
# as well as allow for keeping track of all major story events.

init python:

    global timeline_map

    import json
    with renpy.open_file("data/timeline.json") as json_file:
        timeline_file = json.load(json_file)

    timeline_map = timeline_file["timeline"]

    with renpy.open_file("data/achievements.json") as json_file:
        achieve_file = json.load(json_file)

    achieve_map = achieve_file


screen timeline_tracer():
    tag menu

    #Add background image
    add Color('#323e42', alpha=0.75)

    frame:
        background None
        xpos 25
        ypos 25
        text "{size=+12}Timeline Tracer"

    # bounding box
    frame:
        xsize 1870
        ysize 800
        xpos 25
        ypos 125
    
        # scrollable
        viewport:
            mousewheel True
            scrollbars "both"
            draggable True
            pagekeys True

            for event in timeline_map:
                python:
                    # set up positioning
                    # this is set up in a grid system. just handle it in the json based on what row/column you want
                    try:
                        this_x = int(timeline_map[event]["pos"][0]*200) + 25
                        this_y = int(timeline_map[event]["pos"][1]*145)
                    except:
                        this_x = 25
                        this_y = 25
            
                    # make sure it's unlocked before we continue
                    try:
            
                        # if it needs you to have seen a label to unlock
                        if "need_label" in timeline_map[event] and renpy.seen_label(timeline_map[event]["need_label"]) == True:
                            this_unlocked = True
                        # if it needs you to have earned an achievement to unlock
                        # rework this whenever digi fixes cheevos to use IDs rather than cheev names
                        elif "need_achieve" in timeline_map[event]and achieve_map[timeline_map[event]["need_achieve"]]["name"] in persistent.unlocked_achievements:
                            this_unlocked = True
                        # have not unlocked
                        else:
                            this_unlocked = False
                    except:
                        this_unlocked = False

                    # continue if unlocked
                    if this_unlocked == True:
                        # get type and change background color based on it
                        # TODO: these colors suck ass, change em later
                        # TODO: this should be replaced w images later
                        if timeline_map[event]["type"] == "start":
                            this_bg = "#009AFF"
                        elif timeline_map[event]["type"] == "choice":
                            this_bg = "#FFA200"
                        elif timeline_map[event]["type"] == "outcome":
                            this_bg = "#875900"
                        elif timeline_map[event]["type"] == "prereq":
                            this_bg = "FF8AC8"
                        elif timeline_map[event]["type"] == "end":
                            this_bg = "#00D972"
                        elif timeline_map[event]["type"] == "badend":
                            this_bg = "#E63A37"
                        elif timeline_map[event]["type"] == "minigame":
                            this_bg = "#D341FF"
                        else: # if it's this color, you haven't given it a type!
                            this_bg = "#000000"
                    
                        # get DX status
                        try:
                            if timeline_map[event]["dx"] == True:
                                this_dx = True
                        except:
                            this_dx = False

                        # get name, if it exists
                        try:
                            this_name = timeline_map[event]["name"]
                        except:
                            this_name = ""
                
                        # get jump label, if it exists
                        try:
                            this_jump = timeline_map[event]["jump_to"]
                        except:
                            this_jump = None

                    else: # locked
                        this_bg = "#BBBBBB"
                        this_name = "???"
                        this_dx = False
                        this_jump = None
                        
                # screen vars
                $ show_name = None

                # make bounding box for item
                frame:
                    background color(this_bg)
                    xsize 150
                    ysize 100

                    xpos this_x
                    ypos this_y

                    # place dx label
                    if this_dx == True:
                        image ("gui/dx_text.png"):
                            xpos 114
                            ypos -25
                 
                    # make button
                    button:
                        xsize 150
                        ysize 150
                        xalign 0.5
                        yalign 0.5

                        # show name, although later i'd like this to be a tooltip or smth
                        text this_name:
                            size 32
                            xalign 0.5
                            yalign 0.5

                        # handle jumps here later if there are any
                        # TODO: DON'T USE THIS YET, IT WILL MAKE YOU UNABLE TO ESCAPE THE GAME
                        #action [ SensitiveIf(this_unlocked == True and this_jump is not None), Play("sound", "audio/sfx/sfx_valid.ogg"),Jump(this_jump) ]
                        action [ SensitiveIf(this_unlocked == True and this_jump is not None), Play("sound", "audio/sfx/sfx_valid.ogg"),Notify(this_jump) ]

                        hover_sound "audio/sfx/sfx_select.ogg"

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
