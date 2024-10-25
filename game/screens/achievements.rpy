
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen achievements_nav():
    add Color('#5F777F', alpha=0.75)
    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen achievements_welcome():
    ##This is the Achievements page.

    tag menu
    use achievements_nav
    python:
        
        # --- IMPORTANT NOTICE ---
        # DO NOT EVER USE len([a for a in achievements ...])
        # DO NOT DO IT
        # IT COUNTS WORSE THAN I DO
        # FOR EXAMPLE, IT THINKS NEWLINES ARE LIST ITEMS
        # TRUST ME ON THIS - Tate
    
        story_count = 0
        extra_count = 0
        story_unlocked_count = 0
        extra_unlocked_count = 0
        locked_count = 0
        unlocked_count = 0
        hidden_count = 0
        total_count = 0
        
        for a in achievement_manager.achievements:
            # total items
            total_count += 1
            
            # count categories, then unlocked in each category
            if a.category == "story":
                story_count += 1
                if a.name in persistent.unlocked_achievements:
                    story_unlocked_count =+ 1   
            
            if a.category == "extra":
                extra_count += 1
                if a.name in persistent.unlocked_achievements:
                    extra_unlocked_count =+ 1
                 
            # count hidden
            if a.name not in persistent.unlocked_achievements and a.hidden == True:
                hidden_count += 1
            # count unlocked total
            if a.name in persistent.unlocked_achievements:
                unlocked_count += 1
            
        # fix remaining locked
        locked_remaining_count = total_count - unlocked_count    
            
        # funny 188% achievements
        # make it 100% on the backend for math reasons then convert it
        percent_unlocked_backend = (unlocked_count / total_count) * 100
        percent_unlocked_display = int(percent_unlocked_backend * 1.88)
        if percent_unlocked_display >= 100 and story_count > story_unlocked_count:
            percent_unlocked_display = 99

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
            text "[percent_unlocked_display]% Unlocked"
            spacing 25
            if achievement_manager.unlocked:
                text "Unlocked Achievements ([unlocked_count]/[total_count])"
                for a in achievement_manager.achievements:
                    if a.name in persistent.unlocked_achievements:
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
                text "Locked Achievements ([locked_count]/[locked_remaining_count], [hidden_count] hidden)"
                for a in achievement_manager.achievements:
                    if not a.name in persistent.unlocked_achievements and not a.hidden:
                        hbox:
                            first_spacing 25
                            image a.icon:
                                xysize(100,100)
                            vbox:
                                text a.name
                                text a.desc:
                                    color("#BBBBBB")
                                hbox:
                                    spacing 15
                                    if a.steps != 1 and a.progress != 1:
                                        python:
                                            progtext = f"{a.current_steps}/{a.steps} ({a.progress*100:.02f}%)"
                                        bar value a.progress*1000 range 1000 xsize 600
                                        text progtext yanchor 0.125
