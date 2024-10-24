
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------


init python:

    global music_map

    import json
    with renpy.open_file("jukebox.json") as json_file:
        jukebox_file = json.load(json_file)

    music_map = jukebox_file["tracks"]
    tags_map = jukebox_file["tags"]

    for n in persistent.heard:
        if n not in music_map:
            print(f"WARNING: Track '{n}' not in music_map!")

screen jukebox_nav():

    add Color('#323e42', alpha=0.75)

    # frames > viewports and i will hear no arguments to the contrary. - tate

    frame:
        background None

        # TODO: don't display the given tag if you haven't actually seen ANYTHING in a given route yet. we don't like spoilers

        frame:
            background None
            xsize 600 ysize 50
            xpos 25 ypos 75

            imagebutton:
                xalign 0.0 yalign 0.5
                xysize 64, 64

                idle "/gui/left_off_small.png"
                hover "/gui/left_on_small.png"

                if current_jukebox_tag_index-1>=0:
                    action SetVariable("current_jukebox_tag_index", current_jukebox_tag_index-1)
            
            imagebutton:
                xalign 1.0 yalign 0.5
                xysize 64, 64

                idle "/gui/right_off_small.png"
                hover "/gui/right_on_small.png"

                if current_jukebox_tag_index+1<len(tags_map):
                    action SetVariable("current_jukebox_tag_index", current_jukebox_tag_index+1)

            text tags_map[current_jukebox_tag_index]:
                xalign 0.5 yalign 0.5
                text_align 0.5

        viewport:
            xpos 25 ypos 150
            xsize 600 ysize 700
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            scrollbars "vertical"
            vbox:
                spacing 10
                xoffset 350
                for k in music_map:
                    if k in persistent.heard:
                        # display all
                        if current_jukebox_tag_index == 0:
                            textbutton "{font=music_text}" + music_map[k]["title"]+"\n{size=-12}"+music_map[k]["artist"] action ShowMenu("music_screen", music_map[k]), Play("jukebox", music_map[k]["file"], relative_volume=0.5)
                        # only display per tag
                        else:
                            if tags_map[current_jukebox_tag_index] in music_map[k]["tags"]:
                                textbutton "{font=music_text}" + music_map[k]["title"]+"\n{size=-12}"+music_map[k]["artist"] action ShowMenu("music_screen", music_map[k]), Play("jukebox", music_map[k]["file"], relative_volume=0.5)

    textbutton "Return to Extras" action ShowMenu("category_welcome"), Stop("jukebox"), PauseAudio("music", False) yoffset 950 xoffset 25
    textbutton "Return" action Return(), Stop("jukebox"), PauseAudio("music", False) yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------

screen jukebox_welcome():
    tag menu
    use jukebox_nav
    style_prefix "codex"
    python:
        music_count = len(music_map.keys())
        unlocked_music_count = len(persistent.heard)
    vbox:
        xsize 850
        xalign 0.5 yalign 0.5
        xoffset 300
        text "In this category, you can listen to all the sweet tunes you've discovered throughout CS's adventures!"
        text "([unlocked_music_count]/[music_count] unlocked)"

##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen music_screen(this_track):

    tag menu
    use jukebox_nav

    style_prefix "codex"

    $ track_title = this_track["title"]
    $ artist = this_track["artist"]
    $ album_art = this_track["album_art"]
    $ tags = this_track["tags"]
    
    python:
        try:
            trivia = this_track["trivia"]
        except:
            trivia = ""

    frame:
        background None
        xsize 1250 ysize 150
        xpos 1275 ypos 100

        xanchor 0.5
        text "{font=music_text}{size=69}" + track_title + "\n{font=music_text}{size=45}" + artist:
            text_align 0.5
            xalign 0.5

    viewport:

        xsize 1300
        ysize 900
        xalign 0.5
        xoffset 305
        yoffset 150
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        image "images/jukebox/record.png":
            xysize(500, 500)
            xalign(0.8)
            yalign(0.3)
            at transform:
                rotate 0
                linear 5.0 rotate 360.0
                repeat

        if album_art is None:
            image "images/jukebox/csbi.png":
                xysize(512, 512)
                xalign(0.5)
                yalign(0.4)
        else:
            image f"images/jukebox/{album_art}":
                xysize(512, 512)
                xalign(0.5)
                yalign(0.4)

    frame:
        background None
        xsize 1250 ysize 150
        xoffset 650 yoffset 850

        text trivia:
            text_align 0.5
            xalign 0.5
            yalign 0
