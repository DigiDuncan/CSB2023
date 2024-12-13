########## Minigame Jumps ##########

label lose_car_game:
    $ ending_manager.mark("bad_driver")
    bad_end "100 percent\nunsatisfied." "true_iowa"
    return

label lose_pencil_game:
    $ ending_manager.mark("pencil_shart")
    bad_end "Try, uh, mashing... faster?" "minigame_pencil"
    return

label lose_pencil_game2:
    $ ending_manager.mark("pencil_shart_the_sequel")
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

label play_ce_carrot:
    minigame "play_carrotgame" "play_ce_done" "play_ce_done"
    return

label play_ce_reversi:
    menu:
        "Who would you like to play against?"
        "Tate (Beginner)":
            $ reversi_difficulty = ReversiAI.TATE
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
            return
        "Digi (Easy)":
            $ reversi_difficulty = ReversiAI.DIGI
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
            return
        "K-22 (Medium)":
            $ reversi_difficulty = ReversiAI.PAKOO
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
            return
        "Arceus (Hard)":
            $ reversi_difficulty = ReversiAI.ARCEUS
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
            return
        "Aria (Expert)":
            $ reversi_difficulty = ReversiAI.ARIA
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
            return

label play_ce_done:
    return

########## Warning Screens ##########

label back_out_archival:
    $ persistent.seen.add("k174")
    $ persistent.seen.add("addy")
    $ persistent.heard.add("facing_worlds")
    $ persistent.heard.add("broken_sky")
    $ persistent.heard.add("take_trip")
    $ persistent.heard.add("everybody_wants")
    $ persistent.heard.add("sfx_ringtone_addy")
    $ achievement_manager.unlock("archived")
    $ collect("m4")
    $ collect("cs_car_old")
    return

# TODO: add any collectables here during cinema pass later
label back_out_i69:
    $ persistent.seen.add("gnome")
    $ persistent.heard.add("honk_song")
    $ persistent.heard.add("wayward_wanderer")
    $ persistent.heard.add("sfx_ringtone_cs")
    $ persistent.heard.add("mis_leader")
    $ persistent.heard.add("dense_woods_b")
    $ persistent.heard.add("melancholy")
    $ achievement_manager.unlock("gnomed")
    $ achievement_manager.unlock("forest")
    jump michigan_interstate_94

label back_out_perfect_tate:
    $ persistent.seen.add("tate_ex")
    $ persistent.seen.add("perfect_tate")
    $ persistent.heard.add("nyan_of_a_lifetime")
    $ collect("poo")
    $ collect("dasani")
    $ achievement_manager.unlock("beat_tate")
    jump train_defeated_perfect_tate

########## Game Menus ##########

label chapter_select:
    scene game_menu
    stop music fadeout 3.0
    window hide
    pause 0.1
    call screen chapter_menu()
    return

label dx_start:
    call screen dx_select

label kuwait_select:
    scene map_kuwait
    stop music
    call screen kuwait_map

########## Special Screens ##########

label show_dxcom:
    $ commentary_manager.play(current_dxcom)
    return

label woohoo_counter:
    play music interference2
    scene conferencetv
    show cs at left
    show arceus at right
    with dissolve
    arceus "Well, boss, let's see how many \"woohoos\" you got!"
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
    cs "Now, it's [persistent.woohoo]!"
    return

screen hatch_button():
    modal True
    
    ##### poster button
    imagebutton:
        auto "gui/ce_point_click/poster/poster_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(720, 323, 0)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.poster")

    ##### rug button
    imagebutton:
        auto "gui/ce_point_click/rug/rug_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(949, 60, 0)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.rug")

    ##### cs button
    imagebutton:
        idle "images/characters/cs/christmas/disappointed.png"
        hover "gui/ce_point_click/cs_hover.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at mid_left
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.cs")

    ##### flashlight button
    imagebutton:
        auto "gui/ce_point_click/flashlight/flashlight_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(0.3, 0.7, 0.5)

        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.flashlight")

    ##### mean button
    imagebutton:
        idle "images/characters/mean/meanhumanannoyed.png"
        hover "gui/ce_point_click/mean_hover.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at mid_right
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.mean")
    
    ##### hatch button (correct one)
    imagebutton:
        auto "gui/ce_point_click/hatch/hatch_%s.png" 
        hover_sound "audio/sfx/sfx_select.ogg"
        xpos 0.3
        ypos -0.2
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_after_hatch")

    add Flashlight()

screen limbo_csbutton():
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

screen rockstar_check():
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

########## CS' Data ##########

# TODO: NOTE TO TATE - DON'T TOUCH THESE VALUES, THESE ARE CS' VALUES
# TODO: although, whoever is managing these? please update the persistent to use new formatting

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
    $ achievement_manager.unlock("no_mercy")
    $ achievement_manager.unlock("car_dialogue")
    $ achievement_manager.unlock("poker")
    $ achievement_manager.unlock("friends")
    $ achievement_manager.unlock("ohai_mark")
    $ achievement_manager.unlock("rockstar")
    $ achievement_manager.unlock("guitar_hero")
    $ achievement_manager.unlock("house")
    $ achievement_manager.unlock("indie_artist")
    $ achievement_manager.unlock("gnomed")
    $ achievement_manager.unlock("first_song")
    $ achievement_manager.unlock("csbi")
    $ achievement_manager.unlock("no_1_pooper")
    $ achievement_manager.unlock("pencil")
    $ achievement_manager.unlock("ocean_man")
    $ achievement_manager.unlock("blisaster")
    $ achievement_manager.unlock("amd")
    $ achievement_manager.unlock("crowd_pleaser")
    $ achievement_manager.unlock("rpg")
    $ achievement_manager.unlock("sparta")
    $ achievement_manager.unlock("forest")
    $ achievement_manager.unlock("zup")
    $ achievement_manager.unlock("archived")
    $ achievement_manager.unlock("pacifist")
    $ achievement_manager.unlock("csbii")
    $ achievement_manager.unlock("pencilovania")
    $ achievement_manager.unlock("overcaffeinated")
    $ achievement_manager.unlock("csbiii")
    $ achievement_manager.unlock("beat_copguy")
    $ achievement_manager.unlock("name_is")
    $ achievement_manager.unlock("fourth_wall")
    $ achievement_manager.unlock("cs_beat_copguy")
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
