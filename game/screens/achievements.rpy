
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen achievements_nav():
    add Color('#5F777F', alpha=0.5)
    textbutton "Return to categories" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen achievements_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use achievements_nav
    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        scrollbars "vertical"
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            spacing 100
            text "Unlocked Achievements"
            for a in achievement_manager.achievements:
                if a.unlocked:
                    hbox:
                        first_spacing 25
                        image a.icon
                        text a.name + "\n" + a.desc
            text "Locked Achievements"
            for a in achievement_manager.achievements:
                if not a.unlocked:
                    hbox:
                        first_spacing 25
                        image a.icon
                        text a.name + "\n" + a.desc
            