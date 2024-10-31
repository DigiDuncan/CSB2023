# the purpose of this screen is to eventually replace endings replay and minigames replay
# as well as allow for keeping track of all major story events.

init python:

    global timeline_map

    import json
    with renpy.open_file("data/timeline.json") as json_file:
        timeline_file = json.load(json_file)

    timeline_map = timeline_file["timeline"]

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
        ysize 850
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
                    try:
                        this_x = timeline_map[event]["pos"][0]
                        this_y = timeline_map[event]["pos"][1]
                    except:
                        this_x = 0
                        this_y = 0
            
                    # make sure it's unlocked before we continue
                    try:
                        if renpy.seen_label(timeline_map[event]["need_label"]):
                            this_unlocked = True
                        elif timeline_map[event]["need_achieve"] in achievement_manager.achievements:
                            this_unlocked = True
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
                            this_bg = "#6288FF"
                        elif timeline_map[event]["type"] == "choice":
                            this_bg = "#B3B3B3"
                        elif timeline_map[event]["type"] == "end":
                            this_bg = "#00B330"
                        elif timeline_map[event]["type"] == "badend":
                            this_bg = "#FF6800"
                        else:
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
                    else:
                        this_bg = "#BBBBBB"
                        this_name = "???"
                        this_dx = False

                # make bounding box for item
                frame:
                    background color(this_bg)
                    xsize 150
                    ysize 100

                    xpos this_x
                    ypos this_y

                    text this_name:
                        xalign 0.5
                        yalign 0.5
                 
                    if this_dx == True:
                        image ("gui/dx_text.png"):
                            xpos 114
                            ypos -25


    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
