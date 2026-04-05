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

    #Add background image
    if "main_menu":
        add gui.game_menu_background

    add gui_theme_map["screen_transparency_layer"]

    text _("Extras"):
        style "game_menu_label_text"
        xpos 25 ypos 80

    frame:
        background None
        xpos 25
        ypos 50


    viewport:
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
            # I wanted to use :dx: tag here but it crashes - Tate

            textbutton _("Achievements\n{size=-12}Look at all you've accomplished!") action ShowMenu("achievements")

            textbutton _("Bios\n{size=-12}Learn more about the characters you've met!") action ShowMenu("people")

            textbutton _("{image=gui/inline_text/dx.png} Item Collection\n{size=-12}Inspect items you've found while playing!") action ShowMenu("item_collection")

            textbutton _("{image=gui/inline_text/dx.png} Asset Gallery\n{size=-12}A gallery of beta assets, unused sprites, programmer art, concept art, and more!") action ShowMenu("unused_gallery"), PauseAudio("music", True), Play("music2", "audio/what_the_night_will_bring.ogg")

            textbutton _("{image=gui/inline_text/dx.png} Timeline Tracer\n{size=-12}Revisit endings and track where you've been!") action ShowMenu("timeline_tracer")

            textbutton _("{image=gui/inline_text/dx.png} Woohoo Counter\n{size=-12}How many can you find?") action Jump("woohoo_counter")

            if preferences.developer_mode or persistent.creative_mode:
                text _("If you're looking for the dev options, they're in CSettings now.")

    textbutton _("Main Menu") action Return() yoffset 1000 xoffset 25

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
            text _p("""Here, you'll find bonus content, galleries, achievements, and more!... For now. We are moving these to Subgames!

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