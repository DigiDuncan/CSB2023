screen achievements():
    tag menu
    if "main_menu":
        add gui.game_menu_background
    add gui_theme_map["screen_transparency_layer"]

    text _("Achievements"):
        style "game_menu_label_text"
        xpos 25 ypos 80

###################################################### PREP
    python:
        story_count = 0
        extra_count = 0
        story_unlocked_count = 0
        extra_unlocked_count = 0
        locked_count = 0
        unlocked_count = 0
        hidden_count = 0
        total_count = 0

        for a in achievement_manager.achievements.values():
            # total items
            total_count += 1
            if a.unlocked:
                unlocked_count += 1
            else:
                locked_count += 1

            # count categories, then unlocked in each category
            if a.category == "story":
                story_count += 1
                if a.unlocked:
                    story_unlocked_count += 1

            if a.category == "extra":
                extra_count += 1
                if a.unlocked:
                    extra_unlocked_count += 1

            # count hidden
            if not a.unlocked and a.hidden == True:
                hidden_count += 1

        # fix remaining locked
        locked_remaining_count = total_count - unlocked_count

        # funny 188% achievements
        # make it 100% on the backend for math reasons then convert it
        percent_unlocked_backend = (unlocked_count / total_count) * 100
        percent_unlocked_display = int(percent_unlocked_backend * 1.88)
        if percent_unlocked_display >= 100 and story_count > story_unlocked_count:
            percent_unlocked_display = 99

###################################################### DISPLAY

    frame:
        background None
        xsize 1920 ysize 945

        vbox:
            xfill True yfill True

            ##### Top Text
            frame:
                background None
                xsize 1855 ysize 100

                text _("[percent_unlocked_display]% Unlocked"):
                    xalign 1.0 yalign 1.0
                    text_align 1.0
                    color gui_theme_map["idle_small_color"]

            ##### Achievement List
            frame:
                background None
                xsize 1855 ysize 795
                xalign 0.5 yalign 1.0

                viewport:
                    scrollbars "vertical"
                    side_yfill True
                    mousewheel True
                    draggable True
                    pagekeys True

                    vbox:
                        if achievement_manager.unlocked:
                            text _("Unlocked Achievements ([unlocked_count]/[total_count])")

                            vpgrid:
                                cols 2
                                for a in achievement_manager.achievements.values():
                                    if a.unlocked:
                                        frame:
                                            background None
                                            xsize 925 ymaximum 128

                                            hbox:
                                                first_spacing 25
                                                image a.icon:
                                                    xysize(100,100)
                                                vbox:
                                                    text a.name
                                                    text a.desc:
                                                        size 32
                                                        yanchor 0.1
                                                        color gui_theme_map["idle_small_color"]

                        if achievement_manager.unlocked and achievement_manager.locked:
                            null height 50

                        if achievement_manager.locked:
                            text _("Locked Achievements ([locked_count]/[locked_remaining_count], [hidden_count] hidden)")

                            vpgrid:
                                cols 2
                                for a in achievement_manager.achievements.values():
                                    if not a.unlocked and not a.hidden:
                                        frame:
                                            background None
                                            xsize 925 ymaximum 128

                                            hbox:
                                                first_spacing 25
                                                image a.icon:
                                                    xysize(100,100)
                                                vbox:
                                                    text a.name
                                                    text a.desc:
                                                        size 32
                                                        yanchor 0.1
                                                        color gui_theme_map["idle_small_color"]
                                                    hbox:
                                                        spacing 20
                                                        if a.steps != 1 and a.progress != 1:
                                                            python:
                                                                progtext = f"{a.current_steps}/{a.steps} ({a.progress*100:.02f}%)"
                                                            bar value a.progress*1000 range 1000 xsize 500 ysize 17
                                                            frame:
                                                                background None
                                                                yanchor 1.1
                                                                ymaximum 16
                                                                text progtext:
                                                                    size 32
                                                                    color gui_theme_map["idle_small_color"]

###################################################### BOTTOM BUTTONS

    textbutton _("Back"):
        yoffset 950 xoffset 25
        action ShowMenu("category_welcome")
    textbutton _("Main Menu"):
        yoffset 1000 xoffset 25
        action Return()
