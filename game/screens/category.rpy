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
        if persistent.creative_mode or preferences.developer_mode:
            xpos 25
            yalign 0.5
            xsize 350 ysize 750
        else:
            xpos 25
            yalign 0.5
            xsize 350 ysize 500
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
            textbutton "Endings" action ShowMenu("replay_gallery")
            textbutton "Minigames" action ShowMenu("minigame_gallery")
            textbutton "Item Collection" action ShowMenu("item_welcome")
            textbutton "Unused Assets" action SetVariable("unused_page", 0), ShowMenu("unused_gallery"), PauseAudio("music", True), Play("music2", "audio/what_the_night_will_bring.ogg", relative_volume=8.0)
            if preferences.developer_mode or achievement_manager.get("Hopes and Dreams").unlocked:
                textbutton "Ultimate\nCustom Night" action Start("rpg_ucn")
            textbutton "Woohoo Counter" action Jump("woohoo_counter")
            textbutton "Controller Test" action Jump("play_controllertest")
            if preferences.developer_mode or persistent.creative_mode:
                textbutton "Debug Menu" action ShowMenu("debug_menu")
                textbutton "Asset Debugger" action Jump("asset_debugger")
            if preferences.developer_mode:
                textbutton "Test Scene" action Jump("test")
                textbutton "Unlock All" action Function(unlock_all)
            textbutton "Clear Persistent Data" action Jump("clear_screen")

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
            text _p("""Here, you'll find bonus content, galleries, achievements, and more!

            Make sure to keep checking back here as you play to see what you've unlocked!""")

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

label clear_screen:
    call screen confirm(message="ARE YOU SURE? This will ERASE all data.", yes_action=Jump("reset_vector"), no_action=[Hide("confirm"), Return()])
    return

label reset_vector:
    $ persistent._clear(progress=True)
    $ renpy.quit(relaunch = True)
