label asset_debugger:
    cs "Alright Arc, you ready for the asset debugger?"
    show arceus angry
    arceus "I hate the debugger, it's so uncomfortable!"
    cs "Well, it'll be over in no time! Remember to have bounciness at max!"
    if fun_value(1):
        play sound sfx_achieve
        play music ten_feet_away
        scene game_menu
        show craptop blank at center
        show cs at left
        show csgod at mid_left_left
        show anno at mid_left
        show pakoo at mid_mid_left
        show tate at mid_mid_right
        show mean at mid_right
        show k174 at mid_right_right
        show arceus at right 
        n "test 1{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(2):
        play sound sfx_alt_punch
        play music ac_title
        scene black
        show craptop car at center
        show cs flipped at left
        show csgod flipped at mid_left_left
        show anno prison at mid_left
        show pakoo dark at mid_mid_left
        show tate dark at mid_mid_right
        show mean flipped at mid_right
        show k174 flipped at mid_right_right
        show arceus flipped at right 
        cs "test 2{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(3):
        play sound sfx_back
        play music afternoon_hills
        scene cs_room
        show craptop desktop at center
        show cs happy at left
        show csgod_angry at mid_left_left
        show anno guard at mid_left
        show pakoo flipped at mid_mid_left
        show tate flipped at mid_mid_right
        show mean happy at mid_right
        show k199 at mid_right_right
        show arceus dawn at right 
        cs_fakegod "test 3{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(4):
        play sound sfx_beam
        play music airport
        scene cs_room_2
        show craptop discord at center
        show cs happy flipped at left
        show young_cs at mid_left_left
        show anno guard dark at mid_left
        show pakoo dark flipped at mid_mid_left
        show tate dark flipped at mid_mid_right
        show mean happy flipped at mid_right
        show k199 flipped at mid_right_right
        show arceus dirty at right 
        craptop "test 4{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(5):
        play sound sfx_bell
        play music airport_counter
        scene craptop_bg
        show craptop edit at center
        show cs happy dark at left
        show rich at mid_left_left
        show copguy at mid_left
        show pakoo worried at mid_mid_left
        show tate srs at mid_mid_right
        show mean happy2 at mid_right
        show k207 at mid_right_right
        show arceus dirty flipped at right 
        sticky "test 5{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(6):
        play sound sfx_bossappears
        play music alien_atmosphere
        scene cs_house
        show craptop error at center
        show cs happy dark flipped at left
        show ed at mid_left_left
        show copguy flipped at mid_left
        show pakoo worried flipped at mid_mid_left
        show tate srs dark at mid_mid_right
        show mean happy2 flipped at mid_right
        show k207 flipped at mid_right_right
        show arceus full happy at right 
        discord "test 6{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(7):
        play sound sfx_britishpound
        play music another_him
        scene cs_car
        show craptop off at center
        show cs angry at left
        show ed phone at mid_left_left
        show copguy dark at mid_left
        show pakoo disappointed at mid_mid_left
        show tate srs flipped at mid_mid_right
        show mean surprised at mid_right
        show k207h at mid_right_right
        show arceus full happy flipped at right 
        nova "test 7{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(8):
        play sound sfx_bucket
        play music apple_kid
        scene cs_car_inside
        show craptop sad at center
        show cs angry dark at left
        show wesley at mid_left_left
        show copguy dark flipped at mid_left
        show pakoo disappointed flipped at mid_mid_left
        show tate srs dark flipped at mid_mid_right
        show mean surprised flipped at mid_right
        show k207h flipped at mid_right_right
        show arceus full at right 
        carguy "test 8{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(9):
        play sound sfx_car_crash
        play music atarashii_kaze
        scene walmart_outside
        show craptop updating at center
        show cs angry flipped at left
        show worker_1 at mid_left_left
        show copguy_ai at mid_left
        show pakoo happy at mid_mid_left
        show tate shock at mid_mid_right
        show michael at mid_right
        show nova1 at mid_right_right
        show arceus full flipped at right 
        carguy_nobeep "test 9{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(10):
        play sound sfx_car_horn
        play music automatic_love
        scene walmart_inside
        show craptop ytp at center
        show cs angry dark flipped at left
        show worker_2 at mid_left_left
        show copguycrawl at mid_left
        show pakoo happy flipped at mid_mid_left
        show tate shock dark at mid_mid_right
        show phil at mid_right
        show nova2 at mid_right_right
        show arceus full angry at right 
        greeter "test 10{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(11):
        play sound sfx_chatter
        play music basement
        scene walmart_aisle
        show craptop evidence at center
        show cs worried at left
        show worker_3 at mid_left_left
        show sheriff at mid_left
        show linus at mid_mid_left
        show tate shock flipped at mid_mid_right
        show carguy at mid_right
        show nova3 at mid_right_right
        show arceus full angry flipped at right 
        doug "test 11{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(12):
        play sound sfx_cheer1
        play music bestmusicu
        scene walmart_register_fg
        show craptopreal at center
        show cs worried flipped at left
        show worker_4 at mid_left_left
        show cop at mid_left
        show luke at mid_mid_left
        show tate shock dark flipped at mid_mid_right
        show carguy flipped at mid_right
        show carguya at mid_right_right
        show arceus angry at right 
        cashier "test 12{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(13):
        play sound sfx_cheer2
        play music billy_mix
        scene walmart_register
        show craptopsmall at center
        show cs disappointed at left
        show worker_5 at mid_left_left
        show cop dark at mid_left
        show luke flipped at mid_mid_left
        show tate smug at mid_mid_right
        show doug at mid_right
        show hart1 at mid_right_right
        show arceus angry flipped at right 
        ycs "test 13{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(14):
        play sound sfx_cheers
        play music billy_radio
        scene cs_door_closed
        show craptopsmall flipped at center
        show cs disappointed metal at left
        show worker_5alt at mid_left_left
        show cop_2 at mid_left
        show taran at mid_mid_left
        show tate smug dark at mid_mid_right
        show billy at mid_right
        show hart2 at mid_right_right
        show arceus angry dark at right 
        hoh_operator "test 14{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(15):
        play sound sfx_chop
        play music Billymusicu
        scene cs_door_open
        show billy car at mid_right
        show post_it at center
        show cs disappointed metal2 at left
        show worker_6 at mid_left_left
        show guard_soldier at mid_left
        show taran flipped at mid_mid_left
        show tate smug flipped at mid_mid_right
        show cultist at mid_right_right
        show arceus angry dark flipped at right 
        rich "test 15{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(16):
        play sound sfx_clapperboard
        play music blazing_corridor
        scene rosen_abode
        show billy car happy at mid_right
        show ytx at center
        show cs disappointed metal3 at left
        show worker_7 at mid_left_left
        show marine at mid_left
        show colton at mid_mid_left
        show tate smug dark flipped at mid_mid_right
        show cultist gun at mid_right_right
        show arceus guard at right 
        ed "test 16{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(17):
        play sound sfx_clonk
        play music breakout
        scene cs_street
        show billy car turn at mid_right
        show objection at center
        show cs disappointed metal4 at left
        show digi at mid_left_left
        show big_tank at mid_left
        show nfanboy at mid_mid_left
        show tate sheepish at mid_mid_right
        show cultist_2 at mid_right_right
        show arceus guard flipped at right 
        wesley "test 17{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(18):
        play sound sfx_csnore
        play music brick_by_dick
        scene hoh_outside
        show hold_it at center
        show cs disappointed flipped at left
        show digi dark at mid_left_left
        show asylum_worker at mid_left
        show afanboy at mid_mid_left
        show tate sheepish flipped at mid_mid_right
        show billy laser at mid_right
        show cultist_3 at mid_right_right
        show arceus happy at right 
        michael "test 18{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(19):
        play sound sfx_doorbell
        play music broken_sky
        scene hoh_hq
        show scott_border at center
        show cs concentrate at left
        show digi flipped at mid_left_left
        show aria at mid_left
        show nova at mid_mid_left
        show tate sad at mid_mid_right
        show billy dark at mid_right
        show kitty at mid_right_right
        show arceus happy flipped at right 
        michael_nobeep "test 19{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(20):
        play sound sfx_doorslam
        play music bubble_tea
        scene hoh_hq2
        show cswanted at center
        show cs concentrate dark at left
        show digi dark flipped at mid_left_left
        show aria flipped at mid_left
        show nova dark at mid_mid_left
        show tate sad flipped at mid_mid_right
        show cashier at mid_right
        show kitty flipped at mid_right_right
        show arceus happy dark at right 
        phil "test 20{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(21):
        play sound sfx_drill
        play music bun_guster
        scene hoh_hq3
        show laser_beam at center
        show cs concentrate flipped at left
        show guest at mid_left_left
        show aria dark at mid_left
        show nova flipped at mid_mid_left
        show tate stare at mid_mid_right
        show scott at mid_right
        show blank at mid_right_right
        show arceus happy dark flipped at right 
        worker_1 "test 21{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(22):
        play sound sfx_drillbreak
        play music buy_something
        scene hoh_hq4
        show cards1 at center
        show cs dark at left
        show janitor at mid_left_left
        show aria dark flipped at mid_left
        show nova dark flipped at mid_mid_left
        show tate stare flipped at mid_mid_right
        show obama at mid_right
        show midge at mid_right_right
        show arceus prison at right 
        worker_2 "test 22{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(23):
        play sound sfx_driving
        play music candle_world
        scene hoh_hq5
        show cards2 at center
        show cs dark flipped at left
        show customer at mid_left_left
        show bouncer1 at mid_left
        show peppino at mid_mid_left
        show gnome at mid_mid_right
        show discord at mid_right
        show mika at mid_right_right
        show arceus prison flipped at right 
        worker_3 "test 23{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(24):
        play sound sfx_duck
        play music canyon
        scene hoh_elevator
        show cards3 at center
        show cs dusk at left
        show howie at mid_left_left
        show bouncer2 at mid_left
        show peppino2 at mid_mid_left
        show waitress at mid_mid_right
        show border_guard at mid_right
        show mika dark at mid_right_right
        show arceus worried at right 
        worker_4 "test 24{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(25):
        play sound sfx_earthquake
        play music canyon_but_in_the_car
        scene helipad
        show cards4 at center
        show cs disappointed dark at left
        show howie flipped at mid_left_left
        show trailtrash at mid_left
        show streetguy at mid_mid_left
        show terry at mid_mid_right
        show border_guard dusk at mid_right
        show db at mid_right_right
        show arceus worried flipped at right 
        worker_5 "test 25{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(26):
        play sound sfx_elevator_ding
        play music canyon_but_in_the_car_real
        scene jail_inside
        show cards5 at center
        show cs disappointed dark flipped at left
        show smiley at mid_left_left
        show trailtrash flipped at mid_left
        show pencilguy at mid_mid_left
        show mettaton at mid_mid_right
        show benrey at mid_right
        show db_cooper at mid_right_right
        show arceus dirty worried at right 
        worker_6 "test 26{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(27):
        play sound sfx_foundationfail
        play music canyon_real
        scene jail_cell
        show con_screen at center
        show cs disappointed dusk at left
        show mario at mid_left_left
        show green at mid_left
        show gordon at mid_mid_left
        show scott_pres at mid_mid_right
        show joel at mid_right
        show ges at mid_right_right
        show arceus dirty worried flipped at right 
        worker_7 "test 27{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(28):
        play sound sfx_gamer_and_girl
        play music card_castle
        scene border
        show case at center
        show cs worried dark at left
        show mario flipped at mid_left_left
        show green flipped at mid_left
        show car at mid_mid_left
        show miku at mid_mid_right
        show joel flipped at mid_right
        show renovator at mid_right_right
        show arceus worried dark at right 
        digi "test 28{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(29):
        play sound sfx_gasp
        play music chase
        scene outside_tim_hortons
        show case flipped at center
        show cs worried dark flipped at left
        show violent_jay at mid_left_left
        show jerma at mid_left
        show tom at mid_mid_left
        show sayori at mid_mid_right
        show ikea_greeter at mid_right
        show shadowman at mid_right_right
        show arceus worried dark flipped at right 
        pakoo "test 29{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(30):
        play sound sfx_glass
        play music circus
        scene inside_tim_hortons_fg
        show bag at center
        show cs prison at left
        show shaggy_too_dope at mid_left_left
        show lego at mid_left
        show james at mid_mid_left
        show fumobee at mid_mid_right
        show ikea_greeter blahaj at mid_right
        show pencilcashier at mid_right_right
        show arceus dark at right 
        addy "test 30{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(31):
        play sound sfx_heartbeat
        play music cliffs
        scene inside_tim_hortons
        show bag flipped at center
        show cs prison_worried at left
        show blue_light at mid_left_left
        show lego eyes at mid_left
        show jeremy at mid_mid_left
        show fumobee2 at mid_mid_right
        show ikea_greeter flipped at mid_right
        show cruise at mid_right_right
        show arceus dark flipped at right 
        copguy "test 31{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(32):
        play sound sfx_hitbod1
        play music clownpiece
        scene tunnel
        show drill at center
        show cs guard at left
        show red_light at mid_left_left
        show tsa at mid_left
        show hammond at mid_mid_left
        show cards5alt at mid_mid_right
        show swede at mid_right
        show cruise flipped at mid_right_right
        show arceus dusk at right 
        arceus "test 32{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(33):
        play sound sfx_hitbod2
        play music compulsion_to_obey
        scene canada
        show drillbreak at center
        show cs guard dark at left
        show copguy_ex_front at mid_left_left
        show monika at mid_left
        show mean ayo at mid_mid_left
        show lancer at mid_mid_right
        show alien at mid_right
        show arceus angry dusk at right 
        anno "test 33{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(34):
        play sound sfx_hitbod3
        play music conflict
        scene flag
        show sansbrick at center
        show cs fakegod at left
        show copguy_ex_back at mid_left_left
        show mean ayo flipped at mid_mid_left
        show lancer flipped at mid_mid_right
        show alien dead at mid_right
        show arceus dusk flipped at right 
        border_guard "test 34{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(35):
        play sound sfx_hks1
        play music cp_violation
        scene outside_ltt
        show oldgame at center
        show cs guitar at left
        show ai_ducks at mid_left_left
        show mean angry at mid_mid_left
        show bubble at mid_mid_right
        show ikea_worker at mid_right
        show arceus worried dusk at right
        linus "test 35{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(36):
        play sound sfx_hks2
        play music creative_exercise
        scene inside_ltt
        show m4 at center
        show cs surprised at left
        show stage_screen at mid_left_left
        show mean angry flipped at mid_mid_left
        show tate smug sil_white flipped at mid_mid_right
        show pomni at mid_right
        asylum_worker "test 36{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(37):
        play sound sfx_hks3
        play music danger_mystery
        scene alley
        show m4 flipped at center
        show cs surprised flipped at left
        show mean wat at mid_mid_left
        show tate cry at mid_mid_right
        show moomin at mid_right
        csgod "test 37{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(38):
        play sound sfx_hold_it
        play music dealin_dope
        scene question
        show m4 fire at center
        show cs scared at left
        show mean wat flipped at mid_mid_left
        show tate cry flipped at mid_mid_right
        show snufkin at mid_right
        luke "test 38{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(39):
        play sound sfx_isaac
        play music dense_woods_b
        scene asylum
        show m4 fire flipped at center
        show cs scared flipped at left
        show mean furious at mid_mid_left
        show alicia at mid_right
        taran "test 39{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(40):
        play sound sfx_joj_loop
        play music desert_dawn
        scene csdesk
        show script at center
        show cs scared dark at left
        show mean furious at mid_mid_left
        show witch at mid_right
        colton "test 40{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(41):
        play sound sfx_keyboard
        play music dig_this
        scene csvideo
        show post_it2 at center
        show cs insane worried at left
        show mean furious flipped at mid_mid_left
        show moomin_flipped at mid_right
        sheriff "test 41{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(42):
        play sound sfx_knock
        play music dinerfight
        scene setup
        show colorbars at center
        show cs insane worried flipped at left
        show mean tired at mid_mid_left
        show snufkin_flipped at mid_right
        billy "test 42{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(43):
        play sound sfx_legosfx
        play music dragon_castle
        scene loffice
        show paper at center
        show cs insane disappointed at left
        show mean tired flipped at mid_mid_left
        show alicia_flipped at mid_right
        tv_billy "test 43{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(44):
        play sound sfx_less_annoying_alarm_sound
        play music echoing
        scene ltt_bg
        show pipe_gun at center
        show cs horse at left
        show mean worried at mid_mid_left
        show witch_flipped at mid_right
        cultist "test 44{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(45):
        play sound sfx_metalpipe
        play music echoingspring
        scene ltt_fg
        show pipe_gun flipped at center
        show cs horse flipped at left
        show mean worried flipped at mid_mid_left
        show baumer at mid_right
        cultist_2 "test 45{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(46):
        play sound sfx_nicecar
        play music energetic_rock
        scene frontdoor
        show cheetos at center
        show cs pissed at left
        show mean scared at mid_mid_left
        show baumer flipped at mid_right
        cultist_3 "test 46{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(47):
        play sound sfx_notsonicescratch
        play music everlong
        scene road_to_canada
        show bear at center
        show mean scared flipped at mid_mid_left
        show cs pissed flipped at left
        scott "test 47{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(48):
        play sound sfx_obama
        play music everybody_wants
        scene border_dusk
        show dog at center
        show mean unamused at mid_mid_left
        show cs cultist at left
        terry "test 48{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(49):
        play sound sfx_objection
        play music exotic
        scene sheriff_office
        show pig at center
        show mean unamused flipped at mid_mid_left
        show cs cultist flipped at left
        carla "test 49{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(50):
        play sound sfx_okuubeam
        play music facing_worlds
        scene washington_road
        show pot_lift at center
        show amtrak_conductor at mid_mid_left
        show cs disappointed cultist at left
        peppino "test 50{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(51):
        play sound sfx_page
        play music fastbudget_song
        scene washington_road day
        show pot at center
        show amtrak_conductor flipped at mid_mid_left
        show cs angry cultist at left
        iris "test 51{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(52):
        play sound sfx_payday
        play music fasting
        scene washington_road dusk
        show pot_sunken at center
        show amtrak_stewardess at mid_mid_left
        show cs disappointed cultist flipped at left
        lego "test 52{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(53):
        play sound sfx_ping
        play music fastport
        scene washington_road morning
        show pot_beam at center
        show amtrak_stewardess flipped at mid_mid_left
        show cs angry cultist flipped at left
        trailtrash "test 53{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(54):
        play sound sfx_ping_spam
        play music flyday_chinatown
        scene copcar
        show onscreen_sharpener at center
        show lupin at mid_mid_left
        show cs pencil at left
        green "test 54{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(55):
        play sound sfx_puke
        play music fnaf_6
        scene copcar_mask
        show renault at center
        show lupin flipped at mid_mid_left
        show cs angry pencil at left
        jerma "test 55{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(56):
        play sound sfx_punch
        play music for_the_people
        scene microcenter
        show passportdigi at center
        show lupin hat at mid_mid_left
        show cs disappointed pencil at left
        pencil "test 56{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(57):
        play sound sfx_punch_alt
        play music fourside
        scene microinside
        show copguyexe at center
        show lupin hat flipped at mid_mid_left
        show cs phone at left
        signup "test 57{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(58):
        play sound sfx_ringtone
        play music france
        scene cashzone
        show copguyexe flipped at center
        show cs phone flipped at left
        host "test 58{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(59):
        play sound sfx_roll_window
        play music friendship
        scene cashzone_foreground
        show RCOMOM at center
        show kuwait_doctor_1 at mid_left
        show kuwait_nurse_1 at mid_right
        show kuwait_lieutenant_snow at mid_mid_right
        show cs disappointed phone at left
        tsa "test 59{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(60):
        play sound sfx_select
        play music full_rulle_med_klas
        scene cpuaisle
        show tate_ex_front at center
        show cs disappointed phone flipped at left
        luigi "test 60{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(61):
        play sound sfx_siren
        play music funiculi_holiday
        scene gpuaisle
        show tate_ex_abberation at center
        show cs worried phone at left
        mika "test 61{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(62):
        play sound sfx_slots
        play music gold_room
        scene gpuaisle2
        show tate_ex at center
        show cs worried phone flipped at left
        k174 "test 62{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(63):
        play sound sfx_somethingchanged
        play music good_eatin
        scene testing_main
        show ltt_bottle at center
        show cs angry phone at left
        k199 "test 63{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(64):
        play sound sfx_sparkle
        play music happy_roaming
        scene testing_front
        show amtrak_dining_food at center
        show cs angry phone flipped at left
        k207 "test 64{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(65):
        play sound sfx_splash
        play music happy_rock
        scene course_1
        show amtrak_dining_pancake at center
        show cs scared phone at left
        billy_far "test 65{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(66):
        play sound sfx_start_rocking
        play music happy_running
        scene course_2
        show cs scared phone flipped at left
        direct "test 66{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(67):
        play sound sfx_thunder
        play music hard_drive
        scene course_3
        show cs surprised phone at left
        monika "test 67{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(68):
        play sound sfx_tinnitus
        play music hightop
        scene canada_block
        show cs surprised phone flipped at left
        lancer "test 68{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(69):
        play sound sfx_tiresqueal
        play music hired_guns
        scene dealership
        show cs pissed phone at left
        tate "test 69{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(70):
        play sound sfx_valid
        play music hitmewithyourbestshot
        scene dealer_cars
        show cs pissed phone flipped at left
        kitty "test 70{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(71):
        play sound sfx_victorypunch
        play music hitsquad_2
        scene flintcar_outside
        show cs concentrate phone at left
        obama "test 71{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(72):
        play sound sfx_waterphone
        play music hohsis_theme
        scene flintcar_fg
        show cs concentrate phone flipped at left
        bomaha "test 72{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(73):
        play sound sfx_windows_logon
        play music hohsisremix
        scene car_inside_fg
        show cs at rotate_10
        blank "test 73{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(74):
        play sound sfx_yelling
        play music home_depot
        scene joj_charger_fg
        show cs at rotate_6
        aria "test 74{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(75):
        play sound sfx_ytpintro
        play music honk_song
        scene comments
        show cs at rotate_5
        aria_alt "test 75{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(76):
        play sound sfx_explosion
        play music insane_personalities
        scene hospital_room
        show cs at center_left
        cop "test 76{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(77):
        play sound sfx_funni
        play music killcops
        scene hospital_reception
        show cs at center_right
        midge "test 77{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(78):
        play sound sfx_gul
        play music klaxon_beat
        scene ticket_counter
        show cs at mid_center_right
        db "test 78{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(79):
        play sound sfx_vine
        play music la_by_night
        scene backseat
        show cs at mid_offscreen_right
        customer "test 79{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(80):
        play sound sfx_amtrak_horn
        play music lady_of_the_cold
        scene hotel_lobby
        show cs at mid_offscreen_left
        guest "test 80{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(81):
        play sound sfx_billymaysfap
        play music laurel_palace
        scene hotel_room
        show cs at xstretch_in
        ges "test 81{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(82):
        play sound sfx_fart
        play music lego_island
        scene hotel_breakfast
        show cs at xstretch_out
        nurse "test 82{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(83):
        play sound sfx_fart_again
        play music lets_hear_my_baby
        scene hotel_guitar_hero
        show cs at little_bounce
        benrey "test 83{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(84):
        play sound sfx_fart_deep
        play music lets_hear_my_sped
        scene hotel_door
        show cs at t_post_it
        mean "test 84{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(85):
        play sound sfx_fart_lite
        play music letshearspring
        scene hotel_hall
        show cs at t_copguy_frontseat
        agent "test 85{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(86):
        play sound sfx_fart_with_reverb
        play music lisbon_fever
        scene falling_apart
        show cs at t_copguy_frontseat
        agent "test 86{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(87):
        play sound sfx_hard_knock
        play music local_forecast
        scene ltx
        show cs at t_arc_at_tims
        receptionist "test 87{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(88):
        play sound sfx_hubbub
        play music lowbudget_song
        scene ltx_stage
        show cs at t_cs_ltt
        scott_pres "test 88{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(89):
        play sound sfx_lego_break
        play music maladys_melody
        scene in_limo
        show cs at t_linus_ltt
        miku "test 89{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(90):
        play sound sfx_lightswitch
        play music Melancholy
        scene tour_bus_inside
        show cs at t_pepzone1
        hammond "test 90{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(91):
        play sound sfx_poot
        play music mis_leader
        scene big_stage
        show cs at t_pepzone2
        jeremy "test 91{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(92):
        play sound sfx_sliding_door_close
        play music mm_complete
        scene stage2
        show cs at t_linus_drop_tips
        james "test 92{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(93):
        play sound sfx_sliding_door_open
        play music mm_select
        scene cs_door_outside
        show cs at t_gun
        tom "test 93{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(94):
        play sound sfx_whoosh
        play music moongazer
        scene manitoba_street
        show cs at t_stage_screen_1
        sayori "test 94{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(95):
        play music morning_highway
        scene shoe_store
        show cs at t_stage_screen_c
        gnome "test 95{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(96):
        play music mort_farm
        scene washington_road day
        show cs at t_stage_screen_r
        chat "test 96{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(97):
        play music moving_right_along
        scene washington_road dusk
        show cs at t_stagescreen
        unknown "test 97{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(98):
        play music muumin_tani_fuyu
        scene washington_road morning
        show cs at t_punchup
        crowd "test 98{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(99):
        play music neko_to_sanpo
        scene town
        show cs at t_mean_dining_car
        worker "test 99{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(100):
        play music night
        scene gasinside
        show cs at lego_run
        streetguy "test 100{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(101):
        play music nordic_report_1
        scene gasoutside
        show cs at car_run
        waitress "test 101{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(102):
        play music nordic_report_2
        scene carback1
        show cs at typewriter_location
        mario "test 102{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(103):
        play music now_what
        scene hardwareinside
        show cs at midoffscreenright
        smiley "test 103{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(104):
        play music onett
        scene hardwareoutside
        show cs at midoffscreenleftspin
        violent_jay "test 104{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(105):
        play music park_theme
        scene cultforest
        show cs at offscreenrightspin
        shaggy_too_dope "test 105{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(106):
        play music passport
        scene mcdonalds
        show cs at offscreenleftspin
        joel "test 106{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(107):
        play music passport_real
        scene mcdees
        show cs worried punished
        ikea_greeter "test 107{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(108):
        play music passport_ytp
        scene rushmore
        show cs at t_dining_car_breakfast
        ikea_worker "test 108{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(109):
        play music penthouse
        scene csmore
        show cs at t_mean_rollout
        pomni "test 109{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(110):
        play music pixel_peeker_polka
        scene omaha
        show cs at t_dining_car_pancake
        average_swede "test 110{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(111):
        play music pokey
        scene alleyway
        show cs at t_arc_pancake
        alien "test 111{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(112):
        play music police_station
        scene peppinopizzabg
        show cs at t_dining_arc_search_left
        moomin "test 112{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(113):
        play music pressing_pursuit_cornered
        scene peppinopizzafg
        show cs at t_dining_arc_search_right
        snufkin "test 113{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(114):
        play music price_right
        scene wozniaktroubles
        show cs at t_blur_on
        alicia "test 114{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(115):
        play music prophet_2001
        scene cshouse_vaporized
        show cs at t_blur_off
        witch "test 115{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(116):
        play music prophetpart2
        scene cscar1
        renovator "test 116{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(117):
        play music real_world
        scene cscar1arc
        cruise "test 117{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(118):
        play music rosens_loop
        scene cscar2
        baumer "test 118{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(119):
        play music scales_of_joy
        scene utah
        copguyexe "test 119{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(120):
        play music school
        scene utahsign
        l_cultist "test 120{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(121):
        play music showtime
        scene utahnight
        tate_offscreen "test 121{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(122):
        play music snufkin
        scene pizzaplace
        pakoo_offscreen "test 122{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(123):
        play music speedy_comet
        scene legodoor
        green_offscreen "test 123{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(124):
        play music stal
        scene legodooropen
        anno_offscreen "test 124{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(125):
        play music star_spangled_banner
        scene legostage
        ed_ai "test 125{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(126):
        play music street_noise
        scene vegas
        obamanobeep "test 126{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(127):
        play music summer_clearance_sale
        scene strip
        bomahanobeep "test 127{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(128):
        play music super_friendly
        scene slots
        RCOMEM "test 128{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(129):
        play music sweet_victory
        scene tablegames
        k_doctor "test 129{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(130):
        play music taiikusai_desu_yo
        scene pokertable
        k_nurse "test 130{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(131):
        play music take_trip
        scene luigi1
        l_snow "test 131{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(132):
        play music take_trip2
        scene luigi2
        lupin "test 132{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(133):
        play music the_rest_of_bubble_tea
        scene vegasbathroom
        lupin_offscreen "test 133{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(134):
        play music the_whale
        scene backroomcasino
        mean_offscreen "test 134{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(135):
        play music thousand_march
        scene outsafe
        amtrak_conductor "test 135{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(136):
        play music time_for_a_smackdown
        scene outsafeopen
        amtrak_stewardess "test 136{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(137):
        play music track_3
        scene insafe
        amtrak_npc_1 "test 137{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(138):
        play music track_4
        scene carpark
        amtrak_npc_2 "test 138{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(139):
        play music trans_atlantic
        scene casino1
        amtrak_npc_3 "test 139{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(140):
        play music trash_zone
        scene fazhall
        pause 1.0
    else:
        jump exit_debug
    if fun_value(141):
        play music triage_at_dawn
        scene fazlobby
        pause 1.0
    else:
        jump exit_debug
    if fun_value(142):
        play music tumultuous
        scene fazplace
        pause 1.0
    else:
        jump exit_debug
    if fun_value(143):
        play music tuna_fish
        scene airplane_seats
        pause 1.0
    else:
        jump exit_debug
    if fun_value(144):
        play music tunnely_shimbers
        scene airport_interior
        pause 1.0
    else:
        jump exit_debug
    if fun_value(145):
        play music undyne
        scene airport_seats
        pause 1.0
    else:
        jump exit_debug
    if fun_value(146):
        play music upon_me
        scene airport_tsa
        pause 1.0
    else:
        jump exit_debug
    if fun_value(147):
        play music wayward_wanderer
        scene airport_inside
        pause 1.0
    else:
        jump exit_debug
    if fun_value(148):
        play music weird_personalities
        scene old_house_outside
        pause 1.0
    else:
        jump exit_debug
    if fun_value(149):
        play music winter_lullaby
        scene old_house_inside
        pause 1.0
    else:
        jump exit_debug
    if fun_value(150):
        play music wool_gloves
        scene cc_parking_lot
        pause 1.0
    else:
        jump exit_debug
    if fun_value(151):
        play music xddcc
        scene cc_lobby
        pause 1.0
    else:
        jump exit_debug
    if fun_value(152):
        play music credits
        scene cc_entrance
        pause 1.0
    else:
        jump exit_debug
    if fun_value(153):
        play music lancer
        scene cc_crowd
        pause 1.0
    else:
        jump exit_debug
    if fun_value(154):
        play music space_classroom
        scene cc_stage
        pause 1.0
    else:
        jump exit_debug
    if fun_value(155):
        play music error
        scene cc_backstage
        pause 1.0
    else:
        jump exit_debug
    if fun_value(156):
        play music bedroom_day
        scene billboard
        pause 1.0
    else:
        jump exit_debug
    if fun_value(157):
        play music tmwstw
        scene texas
        pause 0.1
    else:
        jump exit_debug
    if fun_value(158):
        play music e_gadds_lab
        scene tvbilly
        pause 0.1
    else:
        jump exit_debug
    if fun_value(159):
        play music insomnia
        scene jeep_inside_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(160):
        play music insomnia_intro
        scene dinerinside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(161):
        play music insomnia_loop
        scene aria_car_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(162):
        play music item_bounce
        scene aria_room
        pause 0.1
    else:
        jump exit_debug
    if fun_value(163):
        play music krabby_klub
        scene aria_apartment_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(164):
        play music night
        scene cs_somewhere
        pause 0.1
    else:
        jump exit_debug
    if fun_value(165):
        play music ochre_woods_day
        scene dineroutside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(166):
        play music onbs
        scene battle_block_without_theater
        pause 0.1
    else:
        jump exit_debug
    if fun_value(167):
        play music outdoors
        scene final_destination
        pause 0.1
    else:
        jump exit_debug
    if fun_value(168):
        play music prof_kranes_kidnap
        scene police_car_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(169):
        play music space
        scene war_torn_1
        pause 0.1
    else:
        jump exit_debug
    if fun_value(170):
        play music sub_game_select
        scene war_torn_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(171):
        play music yuuka_town
        scene war_torn_3
        pause 0.1
    else:
        jump exit_debug
    if fun_value(172):
        scene war_torn_4
        pause 0.1
    else:
        jump exit_debug
    if fun_value(173):
        scene war_torn_5
        pause 0.1
    else:
        jump exit_debug
    if fun_value(174):
        scene car_insidearc_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(175):
        scene car_insidearc_fg flipped
        pause 0.1
    else:
        jump exit_debug
    if fun_value(176):
        scene joj_chargerarc_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(177):
        scene gas_station_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(178):
        scene traffic
        pause 0.1
    else:
        jump exit_debug
    if fun_value(179):
        scene white
        pause 0.1
    else:
        jump exit_debug
    if fun_value(180):
        scene parking_lot
        pause 0.1
    else:
        jump exit_debug
    if fun_value(181):
        scene path_entrance
        pause 0.1
    else:
        jump exit_debug
    if fun_value(182):
        scene path_forest
        pause 0.1
    else:
        jump exit_debug
    if fun_value(183):
        scene creepy_path
        pause 0.1
    else:
        jump exit_debug
    if fun_value(184):
        scene creepy_path_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(185):
        scene creepy_path_3
        pause 0.1
    else:
        jump exit_debug
    if fun_value(186):
        scene creepy_path_4
        pause 0.1
    else:
        jump exit_debug
    if fun_value(187):
        scene creepy_path_fairy
        pause 0.1
    else:
        jump exit_debug
    if fun_value(188):
        scene creepy_path_exit
        pause 0.1
    else:
        jump exit_debug
    if fun_value(189):
        scene cafe_entrance
        pause 0.1
    else:
        jump exit_debug
    if fun_value(190):
        scene cafe_sitting
        pause 0.1
    else:
        jump exit_debug
    if fun_value(191):
        scene cafe_sitting_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(192):
        scene trafficjam
        pause 0.1
    else:
        jump exit_debug
    if fun_value(193):
        scene east_cafe
        pause 0.1
    else:
        jump exit_debug
    if fun_value(194):
        scene doll_eye_tree
        pause 0.1
    else:
        jump exit_debug
    if fun_value(195):
        scene mario_inside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(196):
        scene mario_inside2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(197):
        scene mario_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(198):
        scene gnome_forest
        pause 0.1
    else:
        jump exit_debug
    if fun_value(199):
        scene forest_clearing
        pause 0.1
    else:
        jump exit_debug
    if fun_value(200):
        scene bronsoncrash
        pause 0.1
    else:
        jump exit_debug
    if fun_value(201):
        scene britport
        pause 0.1
    else:
        jump exit_debug
    if fun_value(202):
        scene embassy
        pause 0.1
    else:
        jump exit_debug
    if fun_value(203):
        scene uk_street
        pause 0.1
    else:
        jump exit_debug
    if fun_value(204):
        scene kitty_house
        pause 0.1
    else:
        jump exit_debug
    if fun_value(205):
        scene kitty_room
        pause 0.1
    else:
        jump exit_debug
    if fun_value(206):
        scene dining_room
        pause 0.1
    else:
        jump exit_debug
    if fun_value(207):
        scene hell_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(208):
        scene dominos
        pause 0.1
    else:
        jump exit_debug
    if fun_value(209):
        scene dominos_counter
        pause 0.1
    else:
        jump exit_debug
    if fun_value(210):
        scene ceo_office
        pause 0.1
    else:
        jump exit_debug
    if fun_value(211):
        scene japanese_street
        pause 0.1
    else:
        jump exit_debug
    if fun_value(212):
        scene front_desk
        pause 0.1
    else:
        jump exit_debug
    if fun_value(213):
        scene hell_kitchen
        pause 0.1
    else:
        jump exit_debug
    if fun_value(214):
        scene top_gear_track
        pause 0.1
    else:
        jump exit_debug
    if fun_value(215):
        scene tom_house
        pause 0.1
    else:
        jump exit_debug
    if fun_value(216):
        scene tom_road
        pause 0.1
    else:
        jump exit_debug
    if fun_value(217):
        scene tokyo_street
        pause 0.1
    else:
        jump exit_debug
    if fun_value(218):
        scene tokyo_airport
        pause 0.1
    else:
        jump exit_debug
    if fun_value(219):
        scene game_store_back
        pause 0.1
    else:
        jump exit_debug
    if fun_value(220):
        scene game_store_front
        pause 0.1
    else:
        jump exit_debug
    if fun_value(221):
        scene tokyo_street_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(222):
        scene tokyo_street_night
        pause 0.1
    else:
        jump exit_debug
    if fun_value(223):
        scene karaoke_bar_inside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(224):
        scene karaoke_bar_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(225):
        scene ceo_office_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(226):
        scene front_desk_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(227):
        scene talking_head
        pause 0.1
    else:
        jump exit_debug
    if fun_value(228):
        scene stockholm
        pause 0.1
    else:
        jump exit_debug
    if fun_value(229):
        scene bus_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(230):
        scene bus_map
        pause 0.1
    else:
        jump exit_debug
    if fun_value(231):
        scene bus_seat
        pause 0.1
    else:
        jump exit_debug
    if fun_value(232):
        scene ikea_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(233):
        scene ikea_inside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(234):
        scene joel_house
        pause 0.1
    else:
        jump exit_debug
    if fun_value(235):
        scene joel_computer
        pause 0.1
    else:
        jump exit_debug
    if fun_value(236):
        scene joel_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(237):
        scene joel_dining
        pause 0.1
    else:
        jump exit_debug
    if fun_value(238):
        scene food_court
        pause 0.1
    else:
        jump exit_debug
    if fun_value(239):
        scene eating_food
        pause 0.1
    else:
        jump exit_debug
    if fun_value(240):
        scene home_decor
        pause 0.1
    else:
        jump exit_debug
    if fun_value(241):
        scene toilet_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(242):
        scene plushie_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(243):
        scene eating_food_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(244):
        scene dumpster
        pause 0.1
    else:
        jump exit_debug
    if fun_value(245):
        scene moomin_zone1
        pause 0.1
    else:
        jump exit_debug
    if fun_value(246):
        scene moomin_zone2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(247):
        scene moomin_zone3
        pause 0.1
    else:
        jump exit_debug
    if fun_value(248):
        scene moomin_zone3b
        pause 0.1
    else:
        jump exit_debug
    if fun_value(249):
        scene moomin_zone4
        pause 0.1
    else:
        jump exit_debug
    if fun_value(250):
        scene moomin_zone5
        pause 0.1
    else:
        jump exit_debug
    if fun_value(251):
        scene waddle_zone
        pause 0.1
    else:
        jump exit_debug
    n "Done."
    return

label exit_debug:
    show cs angry
    pause 1.0
    cs "You didn't turn it on!"
    return
