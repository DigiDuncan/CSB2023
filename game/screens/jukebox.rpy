
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    global music_map
    #Name of Entry followed by file name
    music_map = {
        "Let's hear my baby - Walkman": "lets_hear_my_baby.mp3",
        "CANYON.MID - George Stone": "canyon.mp3",
        "Summer Clearance Sale - BEST MUSIC": "summer_clearance_sale.mp3",
        "scales of joy.mod - Mel O Dee": "scales_of_joy.mp3",
        "Alfred Hitchcock Intro Theme - Charles Gounod": "hohsis_theme.mp3",
        "Super Friendly - Kevin Macleod": "super_friendly.mp3",
        "Time for a Smackdown! - Mr. Sauceman": "time_for_a_smackdown.mp3",
        "Card Castle - Toby Fox": "card_castle.mp3",
        "Basement - Toby Fox": "basement.mp3",
        "stal - C418": "stal.mp3",
        "Moongazer - Dr. Awesome": "moongazer.mp3",
        "Onett Theme - Keiichi Suzuki": "onett.mp3",
        "The Star Spangled Banner - THE UNITED STATES OF AMERICA": "star_spangled_banner.mp3",
        "Buy Something Will Ya! - Keiichi Suzuki": "buy_something.mp3",
        "PASSPORT.MID - George Stone": "passport.mp3",
        "Good Eatin - ClascyJitto": "good_eatin.mp3",
        "Echoing - Banana": "echoing.mp3",
        "Pressing Pursuit ~ Cornered - Masakazu Sugimori": "pressing_pursuit_cornered.mp3"
    }

screen jukebox_nav():

    add Color('#323e42', alpha=0.75)

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            for k, v in music_map.items():
                if k in persistent.heard:
                    textbutton k action ShowMenu("music_screen", k), Play("jukebox", "audio/"+v, relative_volume=0.5)

    textbutton "Return to categories" action ShowMenu("category_welcome"), Stop("jukebox") yoffset 950 xoffset 25
    textbutton "Return" action Return(), Stop("jukebox") yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen jukebox_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use jukebox_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category, you can listen to all the sweet tunes you've discovered throughout CS's adventures!")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen music_screen(l):

    tag menu
    use jukebox_nav

    style_prefix "codex"
    label l

    viewport:

        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        
        hbox:
            vbox:
                xsize 800
                ysize 800
                #You write the actual entry here. I suggest you split your text into smaller text _p sections, otherwise the text might overlap with
                #the scrollbars. If you're sure that your text fits the screen and scrolling is not needed then comment out everything starting from "scrollbars vertical" to
                #"pagekeys True" as seen in the next entry. If you do this, splitting the text is not needed.