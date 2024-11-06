# TODO: NOTE TO TATE - DON'T TOUCH THESE VALUES, THESE ARE CS'S VALUES
# TODO: although, whoever is managing these? please update the persistent to use new formatting

screen dx_select():
    
    default tt = Tooltip("Or something else?")

    textbutton "{color=#fff}Return{/color}":
        action MainMenu(confirm=False), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#5F777F"

    vbox:
        xalign 0.5
        viewport:
            xysize(950, 550)
            xalign 0.75
            ypos 0.1
            style_prefix "choice"
            vbox:
                xalign 0.5
                spacing 20
                text "Play the After Story?" xalign 0.5 textalign 0.5
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    at transform:
                        zoom 0.666
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("dx_after_true")
                text tt.value xalign 0.5 textalign 0.5
        viewport:
            xysize(1920, 600)
            yanchor -0.025
            xoffset -0.1
            grid 5 2:
                xfill True
                yfill True
                # We can have 10 entries here
            
                ### SPEEDRUN ###
                imagebutton auto "menu/dx/speedrun_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Speedrun")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("vibration")

                ### KUWAIT ###
                imagebutton auto "menu/dx/kuwait_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Kuwait")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_travel")

                ### BRONSON ###
                imagebutton auto "menu/dx/bronson_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Bronson")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("michigan_bronson")

                ### ROCKSTAR II ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Rockstar II")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("rockstar_start")

                ### TRAIN (WINNER) ###
                imagebutton auto "menu/dx/train_winner_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Train (Winner)")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("train_start_good")

                ### TRAIN (THIEF) ###
                imagebutton auto "menu/dx/train_thief_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Train (Thief)")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("train_start_bad")

                ### CHRISTMAS ###
                imagebutton auto "menu/dx/christmas_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Christmas")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("ce_start")

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

screen kuwait_map():
    default tt = Tooltip("Select area to travel:")
    textbutton "{color=#fff}Return{/color}":
        action MainMenu(confirm=False), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#DEA25E"
    vbox:
        xalign 0.5
        viewport:
            xysize(1080, 1080)
            style_prefix "choice"
            text tt.value xpos(450)
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Kuwait City")
                at transform:
                    zoom 0.1
                    pos(570,650)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kuwait_city")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Sharq")
                at transform:
                    zoom 0.1
                    pos(560,600)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sharq")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Hawally")
                at transform:
                    zoom 0.1
                    pos(460,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_hawally")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Bayan Water Towers")
                at transform:
                    zoom 0.1
                    pos(580,830)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_bayan_water_towers")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Salmiya")
                at transform:
                    zoom 0.1
                    pos(670,790)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_salmiya")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Khiran Camp")
                at transform:
                    zoom 0.1
                    pos(730,980)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_khiran_camp")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Al Wafra")
                at transform:
                    zoom 0.1
                    pos(560,1020)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_wafra")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Jahra Industrial")
                at transform:
                    zoom 0.1
                    pos(310,620)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_jahra_industrial")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Sulaibiya")
                at transform:
                    zoom 0.1
                    pos(270,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sulaibiya")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Icarus")
                at transform:
                    zoom 0.1
                    pos(820,520)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_icarus")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Boubyan Island")
                at transform:
                    zoom 0.1
                    pos(860,240)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_boubyan_island")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Um Al Namil")
                at transform:
                    zoom 0.1
                    pos(920,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_namil")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Kubar Island")
                at transform:
                    zoom 0.1
                    pos(850,860)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kubar_island")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Um Al Maradim")
                at transform:
                    zoom 0.1
                    pos(920,940)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_maradim")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Burgan Oil Fields")
                at transform:
                    zoom 0.1
                    pos(160,540)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_burgan_oil_fields")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Saqr Airbase")
                at transform:
                    zoom 0.1
                    pos(140,140)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_saqr_airbase")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Al-Abdally")
                at transform:
                    zoom 0.1
                    pos(380,180)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_abdally")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Mutla Ridge")
                at transform:
                    zoom 0.1
                    pos(460,270)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_mutla_ridge")

label lose_car_game:
    bad_end "100 percent\nunsatisfied." "true_iowa"
    return

label lose_pencil_game:
    bad_end "Try, uh, mashing... faster?" "minigame_pencil"
    return

label lose_pencil_game2:
    bad_end "You dumb skinfore." "play_pencil2_game"
    return

label play_edit_game:
    minigame "minigame_editing" "minigame_editing" "minigame_editing"
    return

label play_car_game:
    minigame "minigame_car" "minigame_car" "minigame_car"
    return

label play_pencil_game:
    minigame "minigame_pencil" "minigame_pencil" "minigame_pencil"
    return

label play_slots_game:
    minigame "minigame_slots" "minigame_slots" "minigame_slots"
    return

label show_dxcom:
    $ commentary_manager.play(current_dxcom)
    return

label back_out_archival:
    $ persistent.seen.add("k174")
    $ persistent.seen.add("addy")
    $ persistent.heard.add("facing_worlds")
    $ persistent.heard.add("broken_sky")
    $ persistent.heard.add("take_trip")
    $ persistent.heard.add("everybody_wants")
    $ achievement_manager.unlock("Archived")
    return

label back_out_i69:
    $ persistent.seen.add("gnome")
    $ persistent.heard.add("honk_song")
    $ persistent.heard.add("wayward_wanderer")
    $ persistent.heard.add("mis_leader")
    $ persistent.heard.add("dense_woods_b")
    $ persistent.heard.add("melancholy")
    $ achievement_manager.unlock("You've Been Gnomed")
    $ achievement_manager.unlock("Analog Horror Protagonist")
    jump michigan_interstate_94

label dx_start:
    call screen dx_select

label kuwait_select:
    scene map_kuwait
    stop music
    call screen kuwait_map

label woohoo_counter:
    play music interference2
    scene conferencetv
    show cs at left
    show arceus at right
    with dissolve
    arceus "Well boss, let's see how many \"woohoos\" you got!"
    scene conferencetv at Move((0.0 , -1.0), (0.0, 0.0), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show cs at Move((0.0 , 0.25), (0.0, 1.75), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show arceus at Move((0.735 , 0.4), (0.735, 1.75), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    show screen woohoo_counter
    play sound sfx_fabeep
    arceus "Wow, that's [persistent.woohoo] woohoos!"
    arceus "Err... that's now [persistent.woohoo]. My bad."
    play sound sfx_woohoo
    pause 1.5
    $ persistent.woohoo += 1
    play sound sfx_fabeep
    pause 0.5
    cs "Now it's [persistent.woohoo]!"
    return

screen hatch_button:
    modal True
    viewport:
        xpos 0.3
        ypos -0.2
        hbox:
            imagebutton auto "hatch_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_after_hatch")
    add Flashlight()

screen limbo_csbutton:
    add "#000000"
    vbox xalign 0.5 yalign 0.5:
        spacing 25
        add "gui/warning.png" xalign 0.5
        text "This will apply your achivements and unlocks from the original game." textalign 0.5 size 72 xalign 0.5
        text "THIS WILL DELETE YOUR CURRENT SAVE." textalign 0.5 size 64 xalign 0.5
        textbutton "Go back!":
            xalign 0.5
            text_textalign 0.5
            text_size 72
            action Hide("limbo_csbutton")
        textbutton "Proceed":
            xalign 0.5
            text_textalign 0.5
            text_size 72
            action Jump("csdata")

screen rockstar_check:
    text "Band Name: [band_name]" textalign 0.5 size 36 xalign 0.0 yalign 0.05
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text "EP Name: [ep_name]" textalign 0.5 size 36 xalign 0.0 yalign 0.1
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Song Name 1: [song_name_1]" textalign 0.5 size 36 xalign 0.0 yalign 0.15
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Song Name 2: [song_name_2]" textalign 0.5 size 36 xalign 0.0 yalign 0.2
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Song Name 3: [song_name_3]" textalign 0.5 size 36 xalign 0.0 yalign 0.25
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Song Name 4: [song_name_4]" textalign 0.5 size 36 xalign 0.0 yalign 0.3
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Song Name 5: [song_name_5]" textalign 0.5 size 36 xalign 0.0 yalign 0.35
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 1: [line_1]" textalign 0.5 size 36 xalign 0.0 yalign 0.4
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 2: [line_2]" textalign 0.5 size 36 xalign 0.0 yalign 0.45
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 3: [line_3]" textalign 0.5 size 36 xalign 0.0 yalign 0.5
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 4: [line_4]" textalign 0.5 size 36 xalign 0.0 yalign 0.55
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 5: [line_5]" textalign 0.5 size 36 xalign 0.0 yalign 0.6
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 6: [line_6]" textalign 0.5 size 36 xalign 0.0 yalign 0.65
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 7: [line_7]" textalign 0.5 size 36 xalign 0.0 yalign 0.7
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 8: [line_8]" textalign 0.5 size 36 xalign 0.0 yalign 0.75
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text "Line 9: [line_9]" textalign 0.5 size 36 xalign 0.0 yalign 0.8
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 10: [line_10]" textalign 0.5 size 36 xalign 0.0 yalign 0.85
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 11: [line_11]" textalign 0.5 size 36 xalign 0.0 yalign 0.9
    hbox xalign 0.0 yalign 0.25:
        spacing 50 
    text "Line 12: [line_12]" textalign 0.5 size 36 xalign 0.0 yalign 0.95
    hbox xalign 0.0 yalign 0.25:
        spacing 50 


label csdata:
    scene black
    # show screen rockstar_check
    $ persistent.seen.add("michael")
    $ persistent.seen.add("luke")
    $ persistent.seen.add("arceus")
    $ persistent.seen.add("k174")
    $ persistent.seen.add("kitty")
    $ persistent.seen.add("midge")
    $ persistent.seen.add("sticky")
    $ persistent.seen.add("mika")
    $ persistent.seen.add("hoh_worker")
    $ persistent.seen.add("cultist2")
    $ persistent.seen.add("iris")
    $ persistent.seen.add("obama")
    $ persistent.seen.add("streetguy")
    $ persistent.seen.add("tsa")
    $ persistent.seen.add("trailtrash")
    $ persistent.seen.add("csgod")
    $ persistent.seen.add("mean")
    $ persistent.seen.add("terry")
    $ persistent.seen.add("addy")
    $ persistent.seen.add("colton")
    $ persistent.seen.add("linus")
    $ persistent.seen.add("guest")
    $ persistent.seen.add("db")
    $ persistent.seen.add("copguy")
    $ persistent.seen.add("billy")
    $ persistent.seen.add("mettaton")
    $ persistent.seen.add("rich")
    $ persistent.seen.add("cultist")
    $ persistent.seen.add("monika")
    $ persistent.seen.add("gnome")
    $ persistent.seen.add("taran")
    $ persistent.seen.add("carguy")
    $ persistent.seen.add("digi")
    $ persistent.seen.add("cop")
    $ persistent.seen.add("nova")
    $ persistent.seen.add("doug")
    $ persistent.seen.add("round")
    $ persistent.seen.add("phil")
    $ persistent.seen.add("border_guard")
    $ persistent.seen.add("peppino")
    $ persistent.seen.add("craptop")
    $ persistent.seen.add("cashier")
    $ persistent.seen.add("pencil")
    $ persistent.seen.add("aria")
    $ persistent.seen.add("ed")
    $ persistent.seen.add("pakoo")
    $ persistent.seen.add("luigi")
    $ persistent.seen.add("jerma")
    $ persistent.seen.add("cs")
    $ persistent.seen.add("green")
    $ persistent.seen.add("sheriff")
    $ persistent.seen.add("anno")
    $ persistent.seen.add("tate")
    $ persistent.seen.add("scott")
    $ persistent.seen.add("wesley")
    $ persistent.seen.add("lego")
    $ persistent.seen.add("blank")
    $ persistent.seen.add("howie")
    $ persistent.seen.add("ges")
    n "Added Characters...{nw}"
    $ persistent.heard.add("thousand_march")
    $ persistent.heard.add("hohsis_theme")
    $ persistent.heard.add("billy_radio")
    $ persistent.heard.add("passport")
    $ persistent.heard.add("lets_hear_my_baby")
    $ persistent.heard.add("time_for_a_smackdown")
    $ persistent.heard.add("dig_this")
    $ persistent.heard.add("mm_select")
    $ persistent.heard.add("home_depot")
    $ persistent.heard.add("hightop")
    $ persistent.heard.add("stal")
    $ persistent.heard.add("undyne")
    $ persistent.heard.add("everybody_wants")
    $ persistent.heard.add("mm_complete")
    $ persistent.heard.add("star_spangled_banner")
    $ persistent.heard.add("lego_island")
    $ persistent.heard.add("super_friendly")
    $ persistent.heard.add("dense_woods_b")
    $ persistent.heard.add("airport_counter")
    $ persistent.heard.add("dragon_castle")
    $ persistent.heard.add("onett")
    $ persistent.heard.add("summer_clearance_sale")
    $ persistent.heard.add("energetic_rock")
    $ persistent.heard.add("cp_violation")
    $ persistent.heard.add("laurel_palace")
    $ persistent.heard.add("nordic_report_1")
    $ persistent.heard.add("compulsion_to_obey")
    $ persistent.heard.add("prophet_2001")
    $ persistent.heard.add("prophetpart2")
    $ persistent.heard.add("price_right")
    $ persistent.heard.add("good_eatin")
    $ persistent.heard.add("exotic")
    $ persistent.heard.add("facing_worlds")
    $ persistent.heard.add("mis_leader")
    $ persistent.heard.add("happy_rock")
    $ persistent.heard.add("canyon")
    $ persistent.heard.add("scales_of_joy")
    $ persistent.heard.add("tunnely_shimbers")
    $ persistent.heard.add("fnaf_6")
    $ persistent.heard.add("morning_highway")
    $ persistent.heard.add("bun_guster")
    $ persistent.heard.add("buy_something")
    $ persistent.heard.add("pokey")
    $ persistent.heard.add("park_theme")
    $ persistent.heard.add("melancholy")
    $ persistent.heard.add("fourside")
    $ persistent.heard.add("mort_farm")
    $ persistent.heard.add("airport")
    $ persistent.heard.add("take_trip")
    $ persistent.heard.add("clownpiece")
    $ persistent.heard.add("police_station")
    $ persistent.heard.add("klaxon_beat")
    $ persistent.heard.add("moongazer")
    $ persistent.heard.add("danger_mystery")
    $ persistent.heard.add("for_the_people")
    $ persistent.heard.add("now_what")
    $ persistent.heard.add("gold_room")
    $ persistent.heard.add("hit_me_with_your_best_shot")
    $ persistent.heard.add("taiikusai_desu_yo")
    $ persistent.heard.add("weird_personalities")
    $ persistent.heard.add("france")
    $ persistent.heard.add("sweet_victory")
    $ persistent.heard.add("penthouse")
    $ persistent.heard.add("funiculi_holiday")
    $ persistent.heard.add("ac_title")
    $ persistent.heard.add("the_whale")
    $ persistent.heard.add("bubble_tea")
    $ persistent.heard.add("Lowbudget_song")
    $ persistent.heard.add("candle_world")
    $ persistent.heard.add("showtime")
    $ persistent.heard.add("tuna_fish")
    $ persistent.heard.add("breakout")
    $ persistent.heard.add("hired_guns")
    $ persistent.heard.add("creative_exercise")
    $ persistent.heard.add("supernova")
    $ persistent.heard.add("hohsis_remix")
    $ persistent.heard.add("rude_buster")
    $ persistent.heard.add("la_by_night")
    $ persistent.heard.add("everlong")
    $ persistent.heard.add("insane_personalities")
    $ persistent.heard.add("kill_cops")
    $ persistent.heard.add("full_rulle_med_klas")
    $ persistent.heard.add("trans_atlantic")
    $ persistent.heard.add("hard_drive")
    $ persistent.heard.add("triage_at_dawn")
    $ persistent.heard.add("broken_sky")
    $ persistent.heard.add("wayward_wanderer")
    $ persistent.heard.add("desert_dawn")
    $ persistent.heard.add("track_4")
    $ persistent.heard.add("track_3")
    $ persistent.heard.add("pressing_pursuit_cornered")
    $ persistent.heard.add("echoing")
    $ persistent.heard.add("pixel_peeker_polka")
    $ persistent.heard.add("local_forecast")
    $ persistent.heard.add("happy_roaming")
    $ persistent.heard.add("dealin_dope")
    $ persistent.heard.add("another_him")
    $ persistent.heard.add("speedy_comet")
    $ persistent.heard.add("billy_mix")
    $ persistent.heard.add("weapon_of_choice")
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ persistent.heard.add("blazing_corridor")
    $ persistent.heard.add("dinerfight")
    n "Added Songs...{nw}"
    $ persistent.true_ending = True
    $ persistent.creative_mode = False
    $ persistent.seen_splash = False
    $ persistent.first_time = False
    $ persistent.csb2_unlocked = True
    $ persistent.csb3a_unlocked = True
    $ persistent.csb3b_unlocked = True
    n "Added Misc...{nw}"
    $ achievement_manager.unlock("No Mercy")
    $ achievement_manager.unlock("Bored")
    $ achievement_manager.unlock("High Roller")
    $ achievement_manager.unlock("A Little Help From My Friends")
    $ achievement_manager.unlock("Ohai, Mark")
    $ achievement_manager.unlock("You Rock!")
    $ achievement_manager.unlock("Guitar Hero")
    $ achievement_manager.unlock("The House Doesn't Always Win")
    $ achievement_manager.unlock("Independent Artist")
    $ achievement_manager.unlock("You've Been Gnomed")
    $ achievement_manager.unlock("Singer-Songwriter")
    $ achievement_manager.unlock("HoH SiS's Most Wanted")
    $ achievement_manager.unlock("#1 Rated Pooper")
    $ achievement_manager.unlock("Pencil Sharpening Day!")
    $ achievement_manager.unlock("Ocean Man")
    $ achievement_manager.unlock("Blaster Disaster")
    $ achievement_manager.unlock("The Threadripper")
    $ achievement_manager.unlock("Crowd Pleaser")
    $ achievement_manager.unlock("I Thought This Was A Visual Novel")
    $ achievement_manager.unlock("Dead Meme")
    $ achievement_manager.unlock("Analog Horror Protagonist")
    $ achievement_manager.unlock("ZUP!")
    $ achievement_manager.unlock("Archived")
    $ achievement_manager.unlock("Pacifist")
    $ achievement_manager.unlock("Welcome to CSBIII, Motherfucker")
    $ achievement_manager.unlock("Pencilovania")
    $ achievement_manager.unlock("Overcaffeinated")
    $ achievement_manager.unlock("That's All, Folks!")
    $ achievement_manager.unlock("Hopes and Dreams")
    $ achievement_manager.unlock("Hi, My Name Is...")
    $ achievement_manager.unlock("Broken Masquerade")
    $ achievement_manager.unlock("Machine Gun")
    n "Added Achievements...{nw}"
    $ band_name = "The Dickcheese Enthusiasts"
    $ ep_name = "The Shite Album"
    $ song_name_1 = "Your Mom Farting"
    $ song_name_2 = "Urinal Cake Mukbang Party"
    $ song_name_3 = "Touch Grass, Not My Ass"
    $ song_name_4 = "Thru the Buttholes and The Wipes"
    $ song_name_5 = "Sweet, Sweet, Sweet, Urinal Pee"
    $ line_1 = "We're gonna shit on the floor!"
    $ line_2 = "I left a big ol poo in the can"
    $ line_3 = "Then I got out of the U.K."
    $ line_4 = "it was fine"
    $ line_5 = "Whatever we sing, this line must end with cum"
    $ line_6 = "I ate McDonalds and was shitting in the toilet all night"
    $ line_7 = "IMAGINE AN ASS DRINKING DASANI"
    $ line_8 = "COME PEE ON JOHNNY WITH YOUR URINE"
    $ line_9 = "BUY ME ALL THIS SHIT AND WASH THE TOWELS"
    $ line_10 = "JANITOR GENITALS (MINUS UNDERWEAR)"
    $ line_11 = "When I see you, I think about bananas"
    $ line_12 = "HOW I'D LIKE TO PUT THEM IN YA ANUS"
    n "Added Rockstar Lines...{nw}"
    n "Done!"
    return
    
