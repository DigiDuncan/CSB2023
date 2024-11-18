# the purpose of this screen is to eventually replace endings replay
# as well as allow for keeping track of all major story events.

init python:
    import json

    global timeline_map
    global timeline_xmax
    global timeline_ymax

    with renpy.open_file("data/timeline.json") as json_file:
        timeline_file = json.load(json_file)

    timeline_map = timeline_file["timeline"]

    with renpy.open_file("data/achievements.json") as json_file:
        achieve_file = json.load(json_file)

    achieve_map = achieve_file

    # only adjust the first number of these if we need more space to the east or south later
    # grid starts at (0, 0), remember your off-by-one errors
    # doing it here so it doesn't have to keep recalculating every time you mouse over something

    fetch_highest_x = max(timeline_map, key=lambda x: timeline_map[x]["pos"][0])
    fetch_highest_y = max(timeline_map, key=lambda y: timeline_map[y]["pos"][1])

    timeline_xmax = ((timeline_map[fetch_highest_x]["pos"][0] + 1) * 200) + 20
    timeline_ymax = ((timeline_map[fetch_highest_y]["pos"][1] + 1) * 150) + 20

screen timeline_tracer():
    tag menu

    # default, show nothing
    default info = Tooltip("")
    default info_x = 0
    default info_y = 0
    
    # add background color
    add Color('#323e42', alpha=0.75)

    # declare default colors for now. we'll make em images with outlines later
    $ col_locked = "#BBBBBB"
    $ col_prereq = "#FF8AC8"
    $ col_start = "#009AFF"
    $ col_choice = "#FFA200"
    $ col_outcome = "#875900"
    $ col_minigame = "#D341FF"
    $ col_end = "#00D972"
    $ col_badend = "#E63A37"

    frame:
        background None
        xpos 25
        ypos 25
        text "{size=+12}Timeline Tracer"

        # make a key for the player
        # this implementation is stupid

        python:
            key_list = {
                "Locked": col_locked,
                "Check": col_prereq,
                "Start": col_start,
                "Choice": col_choice,
                "Outcome": col_outcome,
                "Minigame": col_minigame,
                "Ending": col_end,
                "Bad Ending": col_badend
            }

        frame:
            background None
            xpos 850
            ypos -20
            xsize 1.0

            hbox:
                $ counter = 0
                for key,color in key_list.items():
                    $ counter = counter + 1
                    if counter < 5:
                        frame:
                            background None
                            xsize 250
                            frame:
                                background color
                                xysize (32,32)
                            text key:
                                text_align 0
                                xoffset 40
                                yoffset -9
                    else:
                        frame:
                            background None
                            xsize 250
                            xoffset -1000
                            yoffset 48
                            frame:
                                background color
                                xysize (32,32)
                            text key:
                                text_align 0
                                xoffset 40
                                yoffset -9

    # prepare counters for later
    $ total_events = 0
    $ total_endings = 0
    $ total_seen_events = 0
    $ total_seen_endings = 0

    # bounding box for timeline
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

            xinitial 0
            yinitial 4*150 + 20 # should put CSBI start in the center

            fixed:
                area (0, 0, timeline_xmax, timeline_ymax)

                for event in timeline_map:
                    python:

                        # count total events for later, but don't count arrows
                        if timeline_map[event]["type"] != "arrow":
                            total_events = total_events + 1
                            if timeline_map[event]["type"] == "end" or timeline_map[event]["type"] == "badend":
                                total_endings = total_endings + 1

                        # set up positioning
                        # this is set up in a grid system. just handle it in the json based on what row/column you want
                        try:
                            this_x = int(timeline_map[event]["pos"][0]*200) + 20
                            this_y = int(timeline_map[event]["pos"][1]*150) + 20
                        except:
                            this_x = 20
                            this_y = 20
                
                        
                        # make sure it's unlocked before we continue
                        try:
                            # if it needs you to have seen a label to unlock
                            if "need_label" in timeline_map[event] and renpy.seen_label(timeline_map[event]["need_label"]) == True:
                                this_unlocked = True

                            # if it needs you to have earned an achievement to unlock
                            elif "need_achieve" in timeline_map[event] and timeline_map[event]["need_achieve"] in persistent.unlocked_achievements:
                                this_unlocked = True

                            # if it requires a seen endings
                            elif "need_ending" in timeline_map[event] and timeline_map[event]["need_ending"] in persistent.seen_endings:
                                this_unlocked = True

                            # if it's unlocked by default (you will *probably* never need this??):
                            elif "need_label" not in timeline_map[event] and "need_achieve" not in timeline_map[event] and "need_ending" not in timeline_map[event]:
                                this_unlocked = True
                            # have not unlocked
                            else:
                                this_unlocked = False
                        except:
                            this_unlocked = False

                        # continue if unlocked
                        if this_unlocked == True:

                            # add to unlocked counters
                            if timeline_map[event]["type"] != "arrow":
                                total_seen_events = total_seen_events + 1
                            if timeline_map[event]["type"] == "end" or timeline_map[event]["type"] == "badend":
                                total_seen_endings = total_seen_endings + 1

                            # get type and change background color based on it
                            # TODO: this should be replaced w images later
                            if timeline_map[event]["type"] == "start":
                                this_bg = col_start
                            elif timeline_map[event]["type"] == "choice":
                                this_bg = col_choice
                            elif timeline_map[event]["type"] == "outcome":
                                this_bg = col_outcome
                            elif timeline_map[event]["type"] == "prereq":
                                this_bg = col_prereq
                            elif timeline_map[event]["type"] == "end":
                                this_bg = col_end
                            elif timeline_map[event]["type"] == "badend":
                                this_bg = col_badend
                            elif timeline_map[event]["type"] == "minigame":
                                this_bg = col_minigame
                            elif timeline_map[event]["type"] == "arrow":
                                this_bg = None
                            else: # if it's this color, you haven't given it a type, and you need to fix that.
                                this_bg = "#000000"
                        
                            # get DX/CE status
                            try:
                                if timeline_map[event]["content_type"] == "dx":
                                    dxiconimg = "gui/dx_text.png"
                                    this_new = True
                                elif timeline_map[event]["content_type"] == "ce":
                                    dxiconimg = "gui/ce_text.png"
                                    this_new = True
                            except:
                                this_new = False

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
                            this_bg = col_locked
                            this_name = "???"
                            this_new = False
                            this_jump = None
                            
                    # let's get arrow status
                    if timeline_map[event]["type"] == "arrow":
                        python:
                            direction_keys = {
                                "n": 0,
                                "ne": 45,
                                "e": 90,
                                "se": 135,
                                "s": 180,
                                "sw": 225,
                                "w": 270,
                                "nw": 315
                            }

                        if "arrow_type" in timeline_map[event]:
                            if timeline_map[event]["arrow_type"] == "double":
                                $ arrow = Transform("gui/timeline/arrow_double.png")
                            elif timeline_map[event]["arrow_type"] == "hblock":
                                $ arrow = Transform("gui/timeline/arrow_hblock.png")
                            elif timeline_map[event]["arrow_type"] == "vblock":
                                $ arrow = Transform("gui/timeline/arrow_vblock.png")
                        else:
                            $ arrow = Transform("gui/timeline/arrow_single.png")
                        frame:
                            background None
                            xsize 150
                            ysize 100
                            xpos this_x
                            ypos this_y
                            image arrow:
                                xalign 0.5
                                yalign 0.5
                                rotate direction_keys[timeline_map[event]["direction"]]

                    # screen vars
                    $ show_name = None

                    # make bounding box for item
                    frame:
                        background this_bg
                        xsize 150
                        ysize 100
                        xpos this_x
                        ypos this_y

                        # make button
                        button:
                            xsize 150
                            ysize 100
                            xalign 0.5
                            yalign 0.5

                            # add hover effects if jumpable
                            if this_jump is not None:
                                idle_background this_bg
                                insensitive_background col_locked
                                hover_background "#FFFFFF"
                                
                            # show name on button, although maybe some should use images later?
                            text this_name:
                                hover_color this_bg
                                size 24
                                xalign 0.5
                                yalign 0.5
                                text_align 0.5

                            # place dx/ce label
                            if this_new == True:
                                image dxiconimg:
                                    xpos 114
                                    ypos -25

                            # handle jumps here later if there are any
                            # TODO: DON'T USE THIS YET, IT WILL MAKE YOU UNABLE TO ESCAPE THE GAME
                            #action [ SensitiveIf(this_unlocked == True and this_jump is not None), Play("sound", "audio/sfx/sfx_valid.ogg"), Jump(this_jump) ]
                            action [ SensitiveIf(this_unlocked == True and this_jump is not None), Play("sound", "audio/sfx/sfx_valid.ogg"), Notify(this_jump) ]

                            hovered [ info.Action("Replay!"), SetScreenVariable("info_x", this_x), SetScreenVariable("info_y", this_y-50) ]

                            hover_sound "audio/sfx/sfx_select.ogg"

                # TODO: make this prettier later
                frame:
                    xanchor 0.5
                    if info.value == "":
                        background None
                    xpos info_x+75
                    ypos info_y-25
                    text info.value:
                        text_align 0.5

    text "Total Events Seen: [total_seen_events] of [total_events]\nTotal Endings Seen: [total_seen_endings] of [total_endings]":
        xanchor 1.0
        xoffset 1895
        yoffset 950

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
