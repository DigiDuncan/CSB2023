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

    frame:
        background None
        xpos 25
        ypos 50
        text "{size=+12}Extras"

    viewport:
        if persistent.creative_mode or preferences.developer_mode:
            xpos 25
            yalign 0.5
            xsize 750 ysize 750
        else:
            xpos 25
            yalign 0.5
            xsize 750 ysize 750
        mousewheel True
        scrollbars "vertical"
        draggable True
        pagekeys True
        vbox:
            spacing 10
            xoffset 350

            # Here you list the categories
            # I wanted to use {dx} tag here but it crashes - Tate

            textbutton "Achievements\n{size=-12}Look at all you've accomplished!" action ShowMenu("achievements_welcome")

            textbutton "Bios\n{size=-12}Learn more about the characters you've met!" action ShowMenu("people")

            textbutton "{image=gui/inline_text/dx_text.png} Item Collection\n{size=-12}Inspect items you've found while playing!" action ShowMenu("item_collection")

            textbutton "Jukebox\n{size=-12}Jam out to songs you've heard along the way!" action ShowMenu("jukebox"), PauseAudio("music", True)

            textbutton "{image=gui/inline_text/dx_text.png} Asset Gallery\n{size=-12}A gallery of beta assets, unused sprites, programmer art, concept art, and more!" action ShowMenu("unused_gallery"), PauseAudio("music", True), Play("music2", "audio/what_the_night_will_bring.ogg")

            textbutton "{image=gui/inline_text/dx_text.png} Timeline Tracer\n{size=-12}Revisit endings and track where you've been!" action ShowMenu("timeline_tracer")

            if preferences.developer_mode or achievement_manager.get("beat_copguy").unlocked:
                textbutton "[[OLD] Ultimate Custom Night\n{size=-12}Put together your own RPG battles!" action Start("rpg_ucn")

                textbutton "{image=gui/inline_text/dx_text.png} [[DEV] Ultimate Custom Night 2\n{size=-12}Put together your own RPG battles, BUT BETTER!" action PauseAudio("music", True), ShowMenu("_ucn2_selection")

            textbutton "{image=gui/inline_text/dx_text.png} Woohoo Counter\n{size=-12}How many can you find?" action Jump("woohoo_counter")

            textbutton "{image=gui/inline_text/dx_text.png} Controller Test\n{size=-12}Check your controller's compatibility." action Jump("play_controllertest")

            if preferences.developer_mode or persistent.creative_mode:

                textbutton "Debug Menu\n{size=-12}[[DEV] Jump to specific sections of the game." action ShowMenu("debug_menu")

                #textbutton "{image=gui/inline_text/dx_text.png} Asset Debugger\n{size=-12}[[DEV] Make sure all assets load correctly." action Jump("asset_debugger")

            if preferences.developer_mode:
                textbutton "Test Scene\n{size=-12}[[DEV] A sandbox for testing various features." action Start("test")

                textbutton "{image=gui/inline_text/dx_text.png} Tate's Test Room\n{size=-12}[[DEV] Another test screen. Awawa." action Start("awawa_tate_test")

                textbutton "Unlock All\n{size=-12}[[DEV] Adds all unlockables to persistent." action Function(unlock_all)

            textbutton "Clear Persistent Data\n{size=-12}Clear your saved data. This cannot be undone." action Jump("clear_screen")

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
            xsize 750
            xalign 0.5 yalign 0.5
            xoffset 400
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
