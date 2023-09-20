#-----------------------------------------------------
# How this basically works:
#   -Player clicks on the "Codex" button in the main menu/quick menu.
#   -Show "category_welcome" screen where they can select a category.
#   -that brings them to the welcome page/main page of the selected category. Ex.: people_welcome in people.rpy
#   -there they can select an entry to read.


##-----------------------------------------------
##-------CATEGORY NAVIGATION---------------------
##-----------------------------------------------
screen category_nav():

    #This is where we create the menu where we can select the category.

    #Add background image
    add Color('#323e42', alpha=0.75)

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        scrollbars "vertical"
        draggable True
        pagekeys True
        vbox:
            spacing 10
            xoffset 350

            # Here you list the categories

            textbutton "People" action ShowMenu("people_welcome")
            textbutton "Achievements" action ShowMenu("achievements_welcome")
            # textbutton "Collectibles" action ShowMenu("collectibles_welcome")
            # textbutton "Endings" action ShowMenu("endings_welcome")
            textbutton "Jukebox" action ShowMenu("jukebox_welcome"), PauseAudio("music", True)
            if preferences.developer_mode or persistent.creative_mode:
                textbutton "Debug Menu" action ShowMenu("debug_menu")
                textbutton "Ultimate\nCustom Night" action Start("rpg_ucn")
                textbutton "Unlock All" action Function(unlock_all)
                textbutton "Clear Persistent Data" action Jump("reset_vector"), Quit(confirm = False)

    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen category_welcome():
    #This is the "Welcome screen", the first screen the player sees when they go into the codex menu.

    tag menu
    use category_nav #instead of the usual menu, we'll use the one we created above

    style_prefix "codex"

    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            #xoffset 400
            text _p("""You could say this screen is... Extra :)""")

            #Really short text might not be centered correctly, you have to adjust the xoffset.

style codex_label is gui_label:
    xalign 0.5
    xoffset 150
    yoffset 100
    size 50
style codex_label_text is gui_label_text
style codex_text is gui_text:
    justify True
style codex_label_text:
    size gui.label_text_size
style codex_scrollbar is gui_vscrollbar:
    xoffset 100

label reset_vector:
    $ persistent._clear(progress=True)
    $ renpy.full_restart()
