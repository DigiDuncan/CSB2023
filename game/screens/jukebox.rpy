
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

    viewport:
        
        # TODO: have ability to sort by name, artist, or route (tag). unsure how to arrange layout yet

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
            for k in music_map:
                if k in persistent.heard:
                    textbutton "{font=music_text}" + music_map[k]["title"]+"\n{size=-12}"+music_map[k]["artist"] action ShowMenu("music_screen", music_map[k]), Play("jukebox", "audio/" + music_map[k]["file"], relative_volume=0.5)

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
        xoffset 200
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

    frame:
        background None
        xsize 1300 ysize 300
        xpos 1225 ypos 100

        xanchor 0.5
        text "{font=music_text}" + track_title:
            xalign 0.5
            size 69
        text "{font=music_text}" + artist:
            xalign 0.5
            yalign 0.4
            size 45

    viewport:

        xsize 1000
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        image "images/jukebox/record.png":
            xysize(500, 500)
            xalign(0.375)
            yalign(0.50)
            at transform:
                rotate 0
                linear 5.0 rotate 360.0
                repeat

        if album_art is None:
            image "images/jukebox/csbi.png":
                xysize(500, 500)
                xalign(0.225)
                yalign(0.5)
        else:
            image f"images/jukebox/{album_art}":
                xysize(512, 512)
                xalign(0.225)
                yalign(0.5)
