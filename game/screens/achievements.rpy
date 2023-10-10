
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen achievements_nav():
    add Color('#5F777F', alpha=0.75)
    textbutton "Return to categories" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen achievements_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use achievements_nav
    python:
        achievement_count = len(achievements)
        unlocked_count = len(persistent.unlocked_achievements)
        locked_count = achievement_count - unlocked_count
        hidden_count = len([a for a in achievements if not a.name in persistent.unlocked_achievements and a.hidden])
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
            spacing 25
            if achievement_manager.unlocked:
                text "Unlocked Achievements ([unlocked_count]/[achievement_count])"
                for a in achievements:
                    if a.unlocked:
                        hbox:
                            first_spacing 25
                            image a.icon:
                                xysize(100,100)
                            vbox:
                                text a.name
                                text a.desc:
                                    color("#BBBBBB")
            if achievement_manager.unlocked and achievement_manager.locked:
                null height 100
            if achievement_manager.locked:
                text "Locked Achievements ([locked_count]/[achievement_count], [hidden_count] hidden)"
                for a in achievements:
                    if not a.name in persistent.unlocked_achievements and not a.hidden:
                        hbox:
                            first_spacing 25
                            image a.icon:
                                xysize(100,100)
                            vbox:
                                text a.name
                                text a.desc:
                                    color("#BBBBBB")
            