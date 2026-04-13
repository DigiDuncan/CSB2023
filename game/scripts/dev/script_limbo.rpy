########## Minigame Jumps ##########

# Returns back to previous screen
label _minigame_done:
    return

label lose_car_game:
    $ ending_manager.mark("bad_driver")
    bad_end "100 percent%%\nunsatisfied." "true_iowa"
    return

label lose_pencil_game:
    $ ending_manager.mark("pencil_shart")
    bad_end "Try, uh, mashing... faster?" "minigame_pencil"
    return

label lose_pencil2_game:
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

label play_pencil2_game:
    minigame "minigame_pencil2" "minigame_pencil2" "minigame_pencil2"
    return

label play_slots_game:
    minigame "minigame_slots" "minigame_slots" "minigame_slots"
    return

label play_ce_carrot:
    minigame "play_carrotgame" "_minigame_done" "_minigame_done"
    return


label play_ce_reversi:
    menu:
        "Who would you like to play against?"
        "Tate (Beginner)":
            $ reversi_difficulty = ReversiAI.TATE
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Digi (Easy)":
            $ reversi_difficulty = ReversiAI.DIGI
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "K-22 (Medium)":
            $ reversi_difficulty = ReversiAI.PAKOO
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Arceus (Hard)":
            $ reversi_difficulty = ReversiAI.ARCEUS
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Aria (Expert)":
            $ reversi_difficulty = ReversiAI.ARIA
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return

label play_mika_reversi:
    menu:
        "Who would you like to play against?"
        "Billy":
            $ reversi_difficulty = ReversiAI.BILLY
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Elizabeth":
            $ reversi_difficulty = ReversiAI.ELIZABETH
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Terry":
            $ reversi_difficulty = ReversiAI.TERRY
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Scott":
            $ reversi_difficulty = ReversiAI.SCOTT
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Rex":
            $ reversi_difficulty = ReversiAI.REX
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Pomni":
            $ reversi_difficulty = ReversiAI.POMNI
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Luke":
            $ reversi_difficulty = ReversiAI.LUKE
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Ges":
            $ reversi_difficulty = ReversiAI.GES
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Bubble":
            $ reversi_difficulty = ReversiAI.BUBBLE
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
            return
        "Anne":
            $ reversi_difficulty = ReversiAI.ANNE
            minigame "play_reversigame" "_minigame_done" "_minigame_done"
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
    jump true_streaming

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
    $ persistent.heard.add("nyan_of_a_lifetime")
    $ collect("yeetable_textbox")
    $ collect("poo")
    $ collect("dasani")
    jump train_defeated_perfect_tate

########## Game Menus ##########

label kuwait_select:
    scene black
    stop music
    call screen kuwait_map

########## Special Screens ##########

label show_dxcom:
    $ commentary_manager.play(current_dxcom)
    return

label woohoo_counter:
    play music interference2
    $ persistent.heard.add("interference")
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

# TODO: move these screens to their respective minigames folder

screen lightgungame():
    modal True
    imagebutton:
        auto "gui/light_gun/pot_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at barrel_moving
        action Play("sound", "audio/sfx/sfx_bucket.ogg"), Jump("lightgamehit")

screen carchasegame():
    modal True
    imagebutton:
        idle "images/mazda_cruise_firing.png"
        hover "images/mazda_cruise_firing.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at cruise_car
        action Play("sound", "audio/sfx/sfx_bucket.ogg"), Jump("cultist_firing")

screen reloadbutton():
    add get_themed_attribute("frame"):
        yalign 0.5
        xalign 0.5
    vbox xalign 0.5 yalign 0.5:
        spacing 25
        textbutton _("Reload!"):
            xalign 0.5
            text_textalign 0.5
            text_size 150
            action Hide("reloadbutton")

########## CS BUTTON ##########

screen limbo_csbutton():
    add "#000000"
    vbox xalign 0.5 yalign 0.5:
        spacing 25
        add "gui/warning.png" xalign 0.5
        text _("This will apply your achivements and unlocks from the original game.") textalign 0.5 size 72 xalign 0.5
        text _("THIS WILL DELETE YOUR CURRENT SAVE.") textalign 0.5 size 64 xalign 0.5
        textbutton _("Go back!"):
            xalign 0.5
            text_textalign 0.5
            text_size 72
            action Hide("limbo_csbutton")
        textbutton _("Proceed"):
            xalign 0.5
            text_textalign 0.5
            text_size 72
            action Jump("csdata")

screen rockstar_check():
    text _("Band Name: [band_name]") textalign 0.5 size 36 xalign 0.0 yalign 0.05
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("EP Name: [ep_name]") textalign 0.5 size 36 xalign 0.0 yalign 0.1
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Song Name 1: [song_name_1]") textalign 0.5 size 36 xalign 0.0 yalign 0.15
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Song Name 2: [song_name_2]") textalign 0.5 size 36 xalign 0.0 yalign 0.2
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Song Name 3: [song_name_3]") textalign 0.5 size 36 xalign 0.0 yalign 0.25
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Song Name 4: [song_name_4]") textalign 0.5 size 36 xalign 0.0 yalign 0.3
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Song Name 5: [song_name_5]") textalign 0.5 size 36 xalign 0.0 yalign 0.35
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 1: [line_1]") textalign 0.5 size 36 xalign 0.0 yalign 0.4
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 2: [line_2]") textalign 0.5 size 36 xalign 0.0 yalign 0.45
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 3: [line_3]") textalign 0.5 size 36 xalign 0.0 yalign 0.5
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 4: [line_4]") textalign 0.5 size 36 xalign 0.0 yalign 0.55
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 5: [line_5]") textalign 0.5 size 36 xalign 0.0 yalign 0.6
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 6: [line_6]") textalign 0.5 size 36 xalign 0.0 yalign 0.65
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 7: [line_7]") textalign 0.5 size 36 xalign 0.0 yalign 0.7
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 8: [line_8]") textalign 0.5 size 36 xalign 0.0 yalign 0.75
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 9: [line_9]") textalign 0.5 size 36 xalign 0.0 yalign 0.8
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 10: [line_10]") textalign 0.5 size 36 xalign 0.0 yalign 0.85
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 11: [line_11]") textalign 0.5 size 36 xalign 0.0 yalign 0.9
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text _("Line 12: [line_12]") textalign 0.5 size 36 xalign 0.0 yalign 0.95
    hbox xalign 0.0 yalign 0.25:
        spacing 50

########## CS' Data ##########

# TODO: NOTE TO TATE - DON'T TOUCH THESE VALUES UNLESS ADDING MORE, THESE ARE CS' VALUES

label csdata:
    scene black
    $ persistent._clear(progress=True)
    n "Clearing current save...{nw}"
    # show screen rockstar_check
    n "Now Adding CSB3 Data.{nw}"
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
    n "Now Adding CSB3 Data.{fast}\nAdded Characters...{nw}"

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
    $ persistent.heard.add("lowbudget_song")
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
    n "Now Adding CSB3 Data.{fast}\nAdded Music...{nw}"

    # TODO: make sure these are all correct
    $ renpy.mark_label_seen("archival")
    $ renpy.mark_label_seen("archival_finale")
    $ renpy.mark_label_seen("car_dialogue")
    $ renpy.mark_label_seen("csbi_craptop")
    $ renpy.mark_label_seen("csbi_direction")
    $ renpy.mark_label_seen("csbi_end")
    $ renpy.mark_label_seen("csbi_michael_house")
    $ renpy.mark_label_seen("csbi_room")
    $ renpy.mark_label_seen("csbi_rosen_house")
    $ renpy.mark_label_seen("csbi_start")
    $ renpy.mark_label_seen("csbi_walmart")
    $ renpy.mark_label_seen("csbii_asylum")
    $ renpy.mark_label_seen("csbii_bordercrossing")
    $ renpy.mark_label_seen("csbii_breakout")
    $ renpy.mark_label_seen("csbii_caught")
    $ renpy.mark_label_seen("csbii_chop")
    $ renpy.mark_label_seen("csbii_jail")
    $ renpy.mark_label_seen("csbii_kick")
    $ renpy.mark_label_seen("csbii_ltt")
    $ renpy.mark_label_seen("csbii_punch")
    $ renpy.mark_label_seen("csbii_questioning")
    $ renpy.mark_label_seen("csbii_special")
    $ renpy.mark_label_seen("csbii_start")
    $ renpy.mark_label_seen("csbiii_ai")
    $ renpy.mark_label_seen("csbiii_arc_escape")
    $ renpy.mark_label_seen("csbiii_arceus_appears")
    $ renpy.mark_label_seen("csbiii_bad_convince")
    $ renpy.mark_label_seen("csbiii_bad_video")
    $ renpy.mark_label_seen("csbiii_boost")
    $ renpy.mark_label_seen("csbiii_boring_video")
    $ renpy.mark_label_seen("csbiii_both_fan")
    $ renpy.mark_label_seen("csbiii_choose_direction")
    $ renpy.mark_label_seen("csbiii_copcar_menu")
    $ renpy.mark_label_seen("csbiii_cops_ltt")
    $ renpy.mark_label_seen("csbiii_edit_video")
    $ renpy.mark_label_seen("csbiii_escape_forest")
    $ renpy.mark_label_seen("csbiii_forest_menu")
    $ renpy.mark_label_seen("csbiii_freed")
    $ renpy.mark_label_seen("csbiii_good_convince")
    $ renpy.mark_label_seen("csbiii_ltt_decide")
    $ renpy.mark_label_seen("csbiii_no_meeting")
    $ renpy.mark_label_seen("csbiii_north")
    $ renpy.mark_label_seen("csbiii_reviews")
    $ renpy.mark_label_seen("csbiii_start")
    $ renpy.mark_label_seen("csbiii_wait_forest")
    $ renpy.mark_label_seen("csbiii_west")
    $ renpy.mark_label_seen("csbiii_ytp_edit")
    $ renpy.mark_label_seen("csbiii_ytp_fan")
    $ renpy.mark_label_seen("fired_back_to_room")
    $ renpy.mark_label_seen("fired_ep_time")
    $ renpy.mark_label_seen("fired_fan_interaction")
    $ renpy.mark_label_seen("fired_final_tour_bus")
    $ renpy.mark_label_seen("fired_first_tour_day")
    $ renpy.mark_label_seen("fired_guitar_hero")
    $ renpy.mark_label_seen("fired_hotel_lobby_2")
    $ renpy.mark_label_seen("fired_hotel_next_day")
    $ renpy.mark_label_seen("fired_howie")
    $ renpy.mark_label_seen("fired_limo_time")
    $ renpy.mark_label_seen("fired_mcd")
    $ renpy.mark_label_seen("fired_new_plan")
    $ renpy.mark_label_seen("fired_no_contract")
    $ renpy.mark_label_seen("fired_second_tour_day")
    $ renpy.mark_label_seen("fired_signed_the_contract")
    $ renpy.mark_label_seen("fired_song_2")
    $ renpy.mark_label_seen("fired_song_5")
    $ renpy.mark_label_seen("fired_third_tour_day")
    $ renpy.mark_label_seen("fired_write_song")
    $ renpy.mark_label_seen("friend2_between_1")
    $ renpy.mark_label_seen("friend2_between_2")
    $ renpy.mark_label_seen("friend2_car_ride_1")
    $ renpy.mark_label_seen("friend2_car_ride_2")
    $ renpy.mark_label_seen("friend2_car_ride_3")
    $ renpy.mark_label_seen("friend2_car_slam")
    $ renpy.mark_label_seen("friend2_copguy_pres")
    $ renpy.mark_label_seen("friend2_cs_meetup")
    $ renpy.mark_label_seen("friend2_cs_meetup_2")
    $ renpy.mark_label_seen("friend2_cs_rage")
    $ renpy.mark_label_seen("friend2_dpn_call")
    $ renpy.mark_label_seen("friend2_dpn_diner")
    $ renpy.mark_label_seen("friend2_final_meetup")
    $ renpy.mark_label_seen("friend2_weapon_of_choice")
    $ renpy.mark_label_seen("friend_after_cop_fight")
    $ renpy.mark_label_seen("friend_after_fanboy")
    $ renpy.mark_label_seen("friend_attack_fanboy")
    $ renpy.mark_label_seen("friend_car_picker")
    $ renpy.mark_label_seen("friend_cool_car")
    $ renpy.mark_label_seen("friend_cool_jump")
    $ renpy.mark_label_seen("friend_fanboy_lose")
    $ renpy.mark_label_seen("friend_fight_menu")
    $ renpy.mark_label_seen("friend_fire_range")
    $ renpy.mark_label_seen("friend_flint_car")
    $ renpy.mark_label_seen("friend_high_gpu")
    $ renpy.mark_label_seen("friend_low_gpu")
    $ renpy.mark_label_seen("friend_microcenter")
    $ renpy.mark_label_seen("friend_reg_car")
    $ renpy.mark_label_seen("friend_reg_jump")
    $ renpy.mark_label_seen("friend_so_join")
    $ renpy.mark_label_seen("friend_stay_inside")
    $ renpy.mark_label_seen("friend_training")
    $ renpy.mark_label_seen("lose_car_game")
    $ renpy.mark_label_seen("lose_pencil_game")
    $ renpy.mark_label_seen("michigan")
    $ renpy.mark_label_seen("michigan_interstate_69")
    $ renpy.mark_label_seen("michigan_interstate_menu")
    $ renpy.mark_label_seen("minigame_car")
    $ renpy.mark_label_seen("minigame_editing")
    $ renpy.mark_label_seen("minigame_pencil")
    $ renpy.mark_label_seen("minigame_pencil2")
    $ renpy.mark_label_seen("minigame_slots")
    $ renpy.mark_label_seen("no_mercy_attack_arc")
    $ renpy.mark_label_seen("no_mercy_fight")
    $ renpy.mark_label_seen("no_mercy_wait_arc")
    $ renpy.mark_label_seen("play_car_game")
    $ renpy.mark_label_seen("play_carrotgame")
    $ renpy.mark_label_seen("play_ce_carrot")
    $ renpy.mark_label_seen("play_ce_reversi")
    $ renpy.mark_label_seen("play_edit_game")
    $ renpy.mark_label_seen("play_pencil_game")
    $ renpy.mark_label_seen("play_reversigame")
    $ renpy.mark_label_seen("play_rpggame")
    $ renpy.mark_label_seen("rockstar_start")
    $ renpy.mark_label_seen("rpg_archival")
    $ renpy.mark_label_seen("rpg_cop_fight_1")
    $ renpy.mark_label_seen("rpg_cop_fight_2")
    $ renpy.mark_label_seen("rpg_cop_fight_3")
    $ renpy.mark_label_seen("rpg_cop_fight_4")
    $ renpy.mark_label_seen("rpg_fanboy_fight_amd")
    $ renpy.mark_label_seen("rpg_final_fight_1")
    $ renpy.mark_label_seen("rpg_final_fight_2")
    $ renpy.mark_label_seen("rpg_final_fight_3")
    $ renpy.mark_label_seen("rpg_ng_fight")
    $ renpy.mark_label_seen("south_airport")
    $ renpy.mark_label_seen("south_airport_bad")
    $ renpy.mark_label_seen("south_back_home_alt")
    $ renpy.mark_label_seen("south_braghohsis")
    $ renpy.mark_label_seen("south_donatehohsis")
    $ renpy.mark_label_seen("south_fighthohsis_alt")
    $ renpy.mark_label_seen("south_folded")
    $ renpy.mark_label_seen("south_lego_ending")
    $ renpy.mark_label_seen("south_ltt_ending_alt")
    $ renpy.mark_label_seen("south_noairport")
    $ renpy.mark_label_seen("south_poker")
    $ renpy.mark_label_seen("south_poker2")
    $ renpy.mark_label_seen("south_poker3")
    $ renpy.mark_label_seen("south_reality_break")
    $ renpy.mark_label_seen("south_start")
    $ renpy.mark_label_seen("south_true_ending_alt")
    $ renpy.mark_label_seen("south_utah")
    $ renpy.mark_label_seen("south_vegas")
    $ renpy.mark_label_seen("south_vegas_done_slots")
    $ renpy.mark_label_seen("south_vegas_lose_slots")
    $ renpy.mark_label_seen("south_vegas_start_slots")
    $ renpy.mark_label_seen("south_vegas_win_slots")
    $ renpy.mark_label_seen("south_ytp_ending_alt")
    $ renpy.mark_label_seen("true_after_ufo")
    $ renpy.mark_label_seen("true_back_home")
    $ renpy.mark_label_seen("true_billy_driver")
    $ renpy.mark_label_seen("true_copsathohsis")
    $ renpy.mark_label_seen("true_east")
    $ renpy.mark_label_seen("true_ending")
    $ renpy.mark_label_seen("true_fighthohsis")
    $ renpy.mark_label_seen("true_fuckuphohsis")
    $ renpy.mark_label_seen("true_hotwire")
    $ renpy.mark_label_seen("true_in_billy_car")
    $ renpy.mark_label_seen("true_iowa")
    $ renpy.mark_label_seen("true_ltt_ending")
    $ renpy.mark_label_seen("true_montana")
    $ renpy.mark_label_seen("true_nebraska")
    $ renpy.mark_label_seen("true_ohio")
    $ renpy.mark_label_seen("true_pennsylvania")
    $ renpy.mark_label_seen("true_south_dakota")
    $ renpy.mark_label_seen("true_streaming")
    $ renpy.mark_label_seen("true_talktohohsis")
    $ renpy.mark_label_seen("true_win_pencil")
    $ renpy.mark_label_seen("true_ytp_ending")
    n "Now Adding CSB3 Data.{fast}\nAdded Labels...{nw}"

    $ persistent.true_ending = True
    $ persistent.creative_mode = False
    $ persistent.seen_splash = False
    $ persistent.first_time = False
    $ persistent.csb2_unlocked = True
    $ persistent.csb3a_unlocked = True
    $ persistent.csb3b_unlocked = True

    # TODO: make sure this is correct/all of them
    $ ending_manager.mark("asylum")
    $ ending_manager.mark("attorney")
    $ ending_manager.mark("bad_driver")
    $ ending_manager.mark("call_cops")
    $ ending_manager.mark("friend")
    $ ending_manager.mark("grand_dad")
    $ ending_manager.mark("hotwire")
    $ ending_manager.mark("god_fail")
    $ ending_manager.mark("god_success")
    $ ending_manager.mark("ltt")
    $ ending_manager.mark("pencil_shart")
    $ ending_manager.mark("premature")
    $ ending_manager.mark("reality_break")
    $ ending_manager.mark("revenge")
    $ ending_manager.mark("rip_money")
    $ ending_manager.mark("rockstar")
    $ ending_manager.mark("south")
    $ ending_manager.mark("threw_away_fame")
    $ ending_manager.mark("true")
    $ ending_manager.mark("ytp")
    n "Now Adding CSB3 Data.{fast}\nAdded Unlocks...{nw}"

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
    n "Now Adding CSB3 Data.{fast}\nAdded Achievements...{nw}"

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
    n "Now Adding CSB3 Data.{fast}\nAdded Rockstar Route lines...{nw}"

    n "Now Adding CE Data.{nw}"

    $ persistent.seen.add("tgt_worker")
    $ persistent.seen.add("linus")
    $ persistent.seen.add("ed")
    $ persistent.seen.add("grace")
    $ persistent.seen.add("wesley")
    $ persistent.seen.add("sheriff")
    $ persistent.seen.add("blank")
    $ persistent.seen.add("pomni")
    $ persistent.seen.add("k17")
    $ persistent.seen.add("mike")
    $ persistent.seen.add("michael")
    $ persistent.seen.add("arceus")
    $ persistent.seen.add("eliza")
    $ persistent.seen.add("copguy")
    $ persistent.seen.add("round")
    $ persistent.seen.add("santa")
    $ persistent.seen.add("ges")
    $ persistent.seen.add("obama")
    $ persistent.seen.add("mean_human")
    $ persistent.seen.add("nova")
    $ persistent.seen.add("kitty")
    $ persistent.seen.add("avgn")
    $ persistent.seen.add("billy")
    $ persistent.seen.add("db")
    $ persistent.seen.add("aria")
    $ persistent.seen.add("luke")
    $ persistent.seen.add("digi")
    $ persistent.seen.add("anno")
    $ persistent.seen.add("k22")
    $ persistent.seen.add("rich")
    $ persistent.seen.add("tate")
    $ persistent.seen.add("anne")
    $ persistent.seen.add("cs")
    $ persistent.seen.add("addy")
    $ persistent.seen.add("iris")
    $ persistent.seen.add("carguy")
    n "Now Adding CE Data.{fast}\nAdded Characters...{nw}"

    $ persistent.heard.add("snow_blind")
    $ persistent.heard.add("star_spangled_banner")
    $ persistent.heard.add("superstar_road")
    $ persistent.heard.add("snowman")
    $ persistent.heard.add("dont_preheat_your_oven")
    $ persistent.heard.add("christmas_tea")
    $ persistent.heard.add("hotel_disbelief")
    $ persistent.heard.add("summer_fun")
    $ persistent.heard.add("on_the_rocks")
    $ persistent.heard.add("what_the_night_will_bring")
    $ persistent.heard.add("lets_hear_winter")
    $ persistent.heard.add("winter_unclearance_sale")
    $ persistent.heard.add("polar_express")
    $ persistent.heard.add("christmas_spirit")
    $ persistent.heard.add("teeth_dust")
    $ persistent.heard.add("frollo_rave")
    $ persistent.heard.add("girl_next_door")
    $ persistent.heard.add("winters_halloween")
    $ persistent.heard.add("rhythm_heaven_try_again")
    $ persistent.heard.add("rhythm_heaven_ok")
    $ persistent.heard.add("rice_and_wine")
    $ persistent.heard.add("snowy")
    $ persistent.heard.add("title_theme_reprise")
    $ persistent.heard.add("synchronicity")
    $ persistent.heard.add("snowdin_town")
    $ persistent.heard.add("rhythm_heaven_superb")
    $ persistent.heard.add("interference2")
    $ persistent.heard.add("sleigh_ride")
    $ persistent.heard.add("ce_passport")
    $ persistent.heard.add("crashing_down")
    n "Now Adding CE Data.{fast}\nAdded Music...{nw}"
    
    $ renpy.mark_label_seen("ce_after_hatch")
    $ renpy.mark_label_seen("ce_aftershop")
    $ renpy.mark_label_seen("ce_anno")
    $ renpy.mark_label_seen("ce_banter")
    $ renpy.mark_label_seen("ce_before_anno")
    $ renpy.mark_label_seen("ce_before_shopping")
    $ renpy.mark_label_seen("ce_billy_time")
    $ renpy.mark_label_seen("ce_carrot")
    $ renpy.mark_label_seen("ce_check_status")
    $ renpy.mark_label_seen("ce_checkout")
    $ renpy.mark_label_seen("ce_climax")
    $ renpy.mark_label_seen("ce_cooking")
    $ renpy.mark_label_seen("ce_decor")
    $ renpy.mark_label_seen("ce_dinner")
    $ renpy.mark_label_seen("ce_end_credits")
    $ renpy.mark_label_seen("ce_epilogue")
    $ renpy.mark_label_seen("ce_exchange")
    $ renpy.mark_label_seen("ce_extras_cruz")
    $ renpy.mark_label_seen("ce_extras_poop")
    $ renpy.mark_label_seen("ce_introductions")
    $ renpy.mark_label_seen("ce_lights")
    $ renpy.mark_label_seen("ce_lights_out")
    $ renpy.mark_label_seen("ce_lose_reversi")
    $ renpy.mark_label_seen("ce_mike")
    $ renpy.mark_label_seen("ce_party_before")
    $ renpy.mark_label_seen("ce_point_click")
    $ renpy.mark_label_seen("ce_point_click.click_menu")
    $ renpy.mark_label_seen("ce_point_click.cs")
    $ renpy.mark_label_seen("ce_point_click.flashlight")
    $ renpy.mark_label_seen("ce_point_click.mean")
    $ renpy.mark_label_seen("ce_point_click.poster")
    $ renpy.mark_label_seen("ce_point_click.rug")
    $ renpy.mark_label_seen("ce_preclimax")
    $ renpy.mark_label_seen("ce_reversi")
    $ renpy.mark_label_seen("ce_reversi_menu")
    $ renpy.mark_label_seen("ce_roof_moment")
    $ renpy.mark_label_seen("ce_setup")
    $ renpy.mark_label_seen("ce_snowed_in")
    $ renpy.mark_label_seen("ce_start")
    $ renpy.mark_label_seen("ce_tree")
    $ renpy.mark_label_seen("ce_win_carrot")
    $ renpy.mark_label_seen("ce_win_reversi")
    n "Now Adding CE Data.{fast}\nAdded Labels...{nw}"

    $ persistent.saved_christmas = True
    $ ending_manager.mark("christmas")
    n "Now Adding CE Data.{fast}\nAdded Unlocks...{nw}"
    
    $ achievement_manager.unlock("critical")
    $ achievement_manager.unlock("paradise")
    $ achievement_manager.unlock("reversi")
    $ achievement_manager.unlock("power_off")
    $ achievement_manager.unlock("shitical")
    $ achievement_manager.unlock("shitdown")
    $ achievement_manager.unlock("party_start")
    $ achievement_manager.unlock("grandmaster")
    $ achievement_manager.unlock("hoh_hoh")
    $ achievement_manager.unlock("point_click")
    $ achievement_manager.unlock("timber")
    $ achievement_manager.unlock("broke")
    $ achievement_manager.unlock("bouncy")
    $ achievement_manager.unlock("target_circle")
    $ achievement_manager.unlock("cheesy_dream")
    $ achievement_manager.unlock("gb_pound")
    $ achievement_manager.unlock("fun")
    n "Now Adding CE Data.{fast}\nAdded Achievements...{nw}"

    $ collect("anno_phone")
    $ collect("folded_paper")
    $ collect("fumo")
    $ collect("peppermint_bark")
    $ collect("burnt_turkey")
    $ collect("cs_phone")
    $ collect("cs_cold_hat")
    $ collect("mean_train")
    $ collect("pie")
    $ collect("cs_car")
    $ collect("mgs1")
    $ collect("colt")
    $ collect("crotch_doctor")
    $ collect("big_city_sliders")
    $ collect("cs_id")
    $ collect("russian_radio")
    $ collect("riffmaster")
    $ collect("target_bags")
    $ collect("pringles")
    $ collect("oxygen_canister")
    $ collect("ltt_screwdriver")
    $ collect("snow_pile")
    $ collect("blank_car")
    $ collect("ges_car")
    $ collect("cheap_shelf")
    $ collect("roll_and_rocker")
    $ collect("adderall")
    $ collect("gamersupps")
    $ collect("peach_syrup")
    $ collect("lights_box")
    $ collect("obama_chopper")
    $ collect("small_city_slider")
    $ collect("cement")
    $ collect("snacks")
    $ collect("melted_ice_cream")
    $ collect("mika_car")
    $ collect("shopping_cart")
    $ collect("projector")
    $ collect("sunny_d")
    $ collect("db_car")
    $ collect("tree_box")
    $ collect("decor_boxes")
    $ collect("apple_pie")
    $ collect("nog")
    $ collect("santa_sleigh")
    $ collect("runaway_bus")
    $ collect("carrot_cake")
    $ collect("instant_pot")
    $ collect("tate_phone")
    $ collect("d20")
    $ collect("mashed_potatoes")
    $ collect("pills")
    $ collect("rental_car")
    $ collect("lego_train")
    $ collect("cop_car")
    $ collect("spray_cheese")
    $ collect("tato_bag")
    $ collect("carrot")
    $ collect("letter")
    $ collect("potato_bag")
    $ collect("tea_and_crumpets")
    $ collect("gravity_falls")
    $ collect("festive_bag")
    $ collect("monitor")
    $ collect("rosen_car")
    $ collect("handy_switch")
    $ collect("hard_drive")
    $ collect("reversi_box")
    $ collect("pipe_gun")
    $ collect("ltt_bottle")
    $ collect("doi")
    $ collect("thigh_highs")
    $ collect("billy_car")
    $ collect("dog_food")
    $ collect("cutting_board")
    $ collect("bread")
    $ collect("ltt_car")
    $ collect("shovel")
    $ collect("flashlight_held")
    $ collect("joj_ufo")
    $ collect("rolling_rock")
    $ collect("butter")
    $ collect("anno_car")
    $ collect("raspberry_pi")
    $ collect("blank_speaker")
    $ collect("knife")
    $ collect("cs_wallet")
    $ collect("genergy")
    $ collect("old_coins")
    $ collect("pakoo_car")
    $ collect("old_shirt")
    $ collect("digi_nugget")
    n "Now Adding CE Data.{fast}\nAdded Items...{nw}"
    $ persistent.show_cs_button = False
    n "Completed. Restarting game...{w=1}{nw}"
    $ renpy.quit(relaunch = True)
