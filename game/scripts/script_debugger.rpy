label asset_debugger:
    cs "Alright Arc, you ready for the asset debugger?"
    show arceus angry
    arceus "I hate the debugger, it's so uncomfortable!"
    cs "Well, it'll be over in no time! Remember to have bounciness at max!"
    if fun_value(1):
        play sound "sfx_achieve.ogg"
        play music "10_feet_away.ogg"
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
        play sound "sfx_alt_punch.ogg"
        play music "ac_title.ogg"
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
        play sound "sfx_back.ogg"
        play music "afternoon_hills.ogg"
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
        play sound "sfx_beam.ogg"
        play music "airport.ogg"
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
        play sound "sfx_bell.ogg"
        play music "airport_counter.ogg"
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
        play sound "sfx_bossappears.ogg"
        play music "alien_atmosphere.ogg"
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
        play sound "sfx_britishpound.ogg"
        play music "another_him.ogg"
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
        play sound "sfx_bucket.ogg"
        play music "apple_kid.ogg"
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
        play sound "sfx_car_crash.ogg"
        play music "atarashii_kaze.ogg"
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
        play sound "sfx_car_horn.ogg"
        play music "automatic_love.ogg"
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
        play sound "sfx_chatter.ogg"
        play music "basement.ogg"
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
        play sound "sfx_cheer1.ogg"
        play music "bestmusicu.ogg"
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
        play sound "sfx_cheer2.ogg"
        play music "billy_mix.ogg"
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
        play sound "sfx_cheers.ogg"
        play music "billy_radio.ogg"
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
        play sound "sfx_chop.ogg"
        play music "Billymusicu.ogg"
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
        play sound "sfx_clapperboard.ogg"
        play music "blazing_corridor.ogg"
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
        play sound "sfx_clonk.ogg"
        play music "breakout.ogg"
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
        play sound "sfx_csnore.ogg"
        play music "brick_by_dick.ogg"
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
        play sound "sfx_doorbell.ogg"
        play music "broken_sky.ogg"
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
        play sound "sfx_doorslam.ogg"
        play music "bubble_tea.ogg"
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
        play sound "sfx_drill.ogg"
        play music "bun_guster.ogg"
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
        play sound "sfx_drillbreak.ogg"
        play music "buy_something.ogg"
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
        play sound "sfx_driving.ogg"
        play music "candle_world.ogg"
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
        play sound "sfx_duck.ogg"
        play music "canyon.ogg"
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
        play sound "sfx_earthquake.ogg"
        play music "canyon_but_in_the_car.ogg"
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
        play sound "sfx_elevator_ding.ogg"
        play music "canyon_but_in_the_car_real.ogg"
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
        play sound "sfx_foundationfail.ogg"
        play music "canyon_real.ogg"
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
        play sound "sfx_gamer_and_girl.ogg"
        play music "card_castle.ogg"
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
        play sound "sfx_gasp.ogg"
        play music "chase.ogg"
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
        play sound "sfx_glass.ogg"
        play music "circus.ogg"
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
        play sound "sfx_heartbeat.ogg"
        play music "cliffs.ogg"
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
        play sound "sfx_hitbod1.ogg"
        play music "clownpiece.ogg"
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
        play sound "sfx_hitbod2.ogg"
        play music "compulsion_to_obey.ogg"
        scene canada
        show drillbreak at center
        show cs guard dark at left
        show copguy_ex_front at mid_left_left
        show monika at mid_left
        show lancer at mid_mid_right
        show alien at mid_right
        show arceus angry dusk at right 
        anno "test 33{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(34):
        play sound "sfx_hitbod3.ogg"
        play music "conflict.ogg"
        scene flag
        show sansbrick at center
        show cs fakegod at left
        show copguy_ex_back at mid_left_left
        show lancer flipped at mid_mid_right
        show alien dead at mid_right
        show arceus dusk flipped at right 
        border_guard "test 34{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(35):
        play sound "sfx_hks1.ogg"
        play music "cp_violation.ogg"
        scene outside_ltt
        show oldgame at center
        show cs guitar at left
        show ai_ducks at mid_left_left
        show bubble at mid_mid_right
        show ikea_worker at mid_right
        linus "test 35{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(36):
        play sound "sfx_hks2.ogg"
        play music "creative_exercise.ogg"
        scene inside_ltt
        show m4 at center
        show cs surprised at left
        show stage_screen at mid_left_left
        show pomni at mid_right
        asylum_worker "test 36{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(37):
        play sound "sfx_hks3.ogg"
        play music "danger_mystery.ogg"
        scene alley
        show m4 flipped at center
        show cs surprised flipped at left
        show moomin at mid_right
        csgod "test 37{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(38):
        play sound "sfx_hold_it.ogg"
        play music "dealin_dope.ogg"
        scene question
        show m4 fire at center
        show cs scared at left
        show snufkin at mid_right
        luke "test 38{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(39):
        play sound "sfx_isaac.ogg"
        play music "dense_woods_b.ogg"
        scene asylum
        show m4 fire flipped at center
        show cs scared flipped at left
        show alicia at mid_right
        taran "test 39{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(40):
        play sound "sfx_joj_loop.ogg"
        play music "desert_dawn.ogg"
        scene csdesk
        show script at center
        show cs scared dark at left
        show witch at mid_right
        colton "test 40{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(41):
        play sound "sfx_keyboard.ogg"
        play music "dig_this.ogg"
        scene csvideo
        show post_it2 at center
        show cs insane worried at left
        show moomin_flipped at mid_right
        sheriff "test 41{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(42):
        play sound "sfx_knock.ogg"
        play music "dinerfight.ogg"
        scene setup
        show colorbars at center
        show cs insane worried flipped at left
        show snufkin_flipped at mid_right
        billy "test 42{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(43):
        play sound "sfx_legosfx.ogg"
        play music "dragon_castle.ogg"
        scene loffice
        show paper at center
        show cs insane disappointed at left
        show alicia_flipped at mid_right
        tv_billy "test 43{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(44):
        play sound "sfx_less_annoying_alarm_sound.ogg"
        play music "echoing.ogg"
        scene ltt_bg
        show pipe_gun at center
        show cs horse at left
        show witch_flipped at mid_right
        cultist "test 44{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(45):
        play sound "sfx_metalpipe.ogg"
        play music "echoingspring.ogg"
        scene ltt_fg
        show pipe_gun flipped at center
        show cs horse flipped at left
        show baumer at mid_right
        cultist_2 "test 45{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(46):
        play sound "sfx_nicecar.ogg"
        play music "energetic_rock.ogg"
        scene frontdoor
        show cheetos at center
        show cs pissed at left
        show baumer flipped at mid_right
        cultist_3 "test 46{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(47):
        play sound "sfx_notsonicescratch.ogg"
        play music "everlong.ogg"
        scene road_to_canada
        show bear at center
        show cs pissed flipped at left
        scott "test 47{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(48):
        play sound "sfx_obama.ogg"
        play music "everybody_wants.ogg"
        scene border_dusk
        show dog at center
        show cs cultist at left
        terry "test 48{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(49):
        play sound "sfx_objection.ogg"
        play music "exotic.ogg"
        scene sheriff_office
        show pig at center
        show cs cultist flipped at left
        carla "test 49{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(50):
        play sound "sfx_okuubeam.ogg"
        play music "facing_worlds.ogg"
        scene washington_road
        show pot_lift at center
        show cs disappointed cultist at left
        peppino "test 50{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(51):
        play sound "sfx_page.ogg"
        play music "fastbudget_song.ogg"
        scene washington_road day
        show pot at center
        show cs angry cultist at left
        iris "test 51{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(52):
        play sound "sfx_payday.ogg"
        play music "fasting.ogg"
        scene washington_road dusk
        show pot_sunken at center
        show cs disappointed cultist flipped at left
        lego "test 52{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(53):
        play sound "sfx_ping.ogg"
        play music "fastport.ogg"
        scene washington_road morning
        show pot_beam at center
        show cs angry cultist flipped at left
        trailtrash "test 53{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(54):
        play sound "sfx_ping_spam.ogg"
        play music "flyday_chinatown.ogg"
        scene copcar
        show onscreen_sharpener at center
        show cs pencil at left
        green "test 54{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(55):
        play sound "sfx_puke.ogg"
        play music "fnaf_6.ogg"
        scene copcar_mask
        show renault at center
        show cs angry pencil at left
        jerma "test 55{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(56):
        play sound "sfx_punch.ogg"
        play music "for_the_people.ogg"
        scene microcenter
        show passportdigi at center
        show cs disappointed pencil at left
        pencil "test 56{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(57):
        play sound "sfx_punch_alt.ogg"
        play music "fourside.ogg"
        scene microinside
        show copguyexe at center
        show cs phone at left
        signup "test 57{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(58):
        play sound "sfx_ringtone.ogg"
        play music "france.ogg"
        scene cashzone
        show copguyexe flipped at center
        show cs phone flipped at left
        host "test 58{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(59):
        play sound "sfx_roll_window.ogg"
        play music "friendship.ogg"
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
        play sound "sfx_select.ogg"
        play music "full_rulle_med_klas.ogg"
        scene cpuaisle
        show cs disappointed phone flipped at left
        luigi "test 60{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(61):
        play sound "sfx_siren.ogg"
        play music "funiculi_holiday.ogg"
        scene gpuaisle
        show cs worried phone at left
        mika "test 61{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(62):
        play sound "sfx_slots.ogg"
        play music "gold_room.ogg"
        scene gpuaisle2
        show cs worried phone flipped at left
        k174 "test 62{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(63):
        play sound "sfx_somethingchanged.ogg"
        play music "good_eatin.ogg"
        scene testing_main
        show cs angry phone at left
        k199 "test 63{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(64):
        play sound "sfx_sparkle.ogg"
        play music "happy_roaming.ogg"
        scene testing_front
        show cs angry phone flipped at left
        k207 "test 64{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(65):
        play sound "sfx_splash.ogg"
        play music "happy_rock.ogg"
        scene course_1
        show cs scared phone at left
        billy_far "test 65{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(66):
        play sound "sfx_start_rocking.ogg"
        play music "happy_running.ogg"
        scene course_2
        show cs scared phone flipped at left
        direct "test 66{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(67):
        play sound "sfx_thunder.ogg"
        play music "hard_drive.ogg"
        scene course_3
        show cs surprised phone at left
        monika "test 67{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(68):
        play sound "sfx_tinnitus.ogg"
        play music "hightop.ogg"
        scene canada_block
        show cs surprised phone flipped at left
        lancer "test 68{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(69):
        play sound "sfx_tiresqueal.ogg"
        play music "hired_guns.ogg"
        scene dealership
        show cs pissed phone at left
        tate "test 69{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(70):
        play sound "sfx_valid.ogg"
        play music "hitmewithyourbestshot.ogg"
        scene dealer_cars
        show cs pissed phone flipped at left
        kitty "test 70{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(71):
        play sound "sfx_victorypunch.ogg"
        play music "hitsquad_2.ogg"
        scene flintcar_outside
        show cs concentrate phone at left
        obama "test 71{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(72):
        play sound "sfx_waterphone.ogg"
        play music "hohsis_theme.ogg"
        scene flintcar_fg
        show cs concentrate phone flipped at left
        bomaha "test 72{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(73):
        play sound "sfx_windows_logon.ogg"
        play music "hohsisremix.ogg"
        scene car_inside_fg
        show cs at rotate_10
        blank "test 73{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(74):
        play sound "sfx_yelling.ogg"
        play music "home_depot.ogg"
        scene joj_charger_fg
        show cs at rotate_6
        aria "test 74{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(75):
        play sound "sfx_ytpintro.ogg"
        play music "honk_song.ogg"
        scene comments
        show cs at rotate_5
        aria_alt "test 75{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(76):
        play sound "secret/sfx_explosion.ogg"
        play music "insane_personalities.ogg"
        scene hospital_room
        show cs at center_left
        cop "test 76{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(77):
        play sound "secret/sfx_funni.ogg"
        play music "killcops.ogg"
        scene hospital_reception
        show cs at center_right
        midge "test 77{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(78):
        play sound "secret/sfx_gul.ogg"
        play music "klaxon_beat.ogg"
        scene ticket_counter
        show cs at mid_center_right
        db "test 78{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(79):
        play sound "secret/sfx_vine.ogg"
        play music "la_by_night.ogg"
        scene backseat
        show cs at mid_offscreen_right
        customer "test 79{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(80):
        play music "lady_of_the_cold.ogg"
        scene hotel_lobby
        show cs at mid_offscreen_left
        guest "test 80{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(81):
        play music "laurel_palace.ogg"
        scene hotel_room
        show cs at xstretch_in
        ges "test 81{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(82):
        play music "lego_island.ogg"
        scene hotel_breakfast
        show cs at xstretch_out
        nurse "test 82{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(83):
        play music "lets_hear_my_baby.ogg"
        scene hotel_guitar_hero
        show cs at little_bounce
        benrey "test 83{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(84):
        play music "lets_hear_my_sped.ogg"
        scene hotel_door
        show cs at t_post_it
        mean "test 84{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(85):
        play music "letshearspring.ogg"
        scene hotel_hall
        show cs at t_copguy_frontseat
        agent "test 85{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(86):
        play music "lisbon_fever.ogg"
        scene falling_apart
        show cs at t_copguy_frontseat
        agent "test 86{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(87):
        play music "local_forecast.ogg"
        scene ltx
        show cs at t_arc_at_tims
        receptionist "test 87{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(88):
        play music "lowbudget_song.ogg"
        scene ltx_stage
        show cs at t_cs_ltt
        scott_pres "test 88{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(89):
        play music "maladys_melody.ogg"
        scene in_limo
        show cs at t_linus_ltt
        miku "test 89{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(90):
        play music "Melancholy.ogg"
        scene tour_bus_inside
        show cs at t_pepzone1
        hammond "test 90{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(91):
        play music "mis_leader.ogg"
        scene big_stage
        show cs at t_pepzone2
        jeremy "test 91{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(92):
        play music "mm_complete.ogg"
        scene stage2
        show cs at t_linus_drop_tips
        james "test 92{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(93):
        play music "mm_select.ogg"
        scene cs_door_outside
        show cs at t_gun
        tom "test 93{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(94):
        play music "moongazer.ogg"
        scene manitoba_street
        show cs at t_stage_screen_1
        sayori "test 94{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(95):
        play music "morning_highway.ogg"
        scene shoe_store
        show cs at t_stage_screen_c
        gnome "test 95{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(96):
        play music "mort_farm.ogg"
        scene washington_road day
        show cs at t_stage_screen_r
        chat "test 96{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(97):
        play music "moving_right_along.ogg"
        scene washington_road dusk
        show cs at t_stagescreen
        unknown "test 97{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(98):
        play music "muumin_tani_fuyu.ogg"
        scene washington_road morning
        show cs at t_punchup
        crowd "test 98{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(99):
        play music "neko_to_sanpo.ogg"
        scene town
        show cs at t_mean_dining_car
        worker "test 99{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(100):
        play music "night.ogg"
        scene gasinside
        show cs at lego_run
        streetguy "test 100{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(101):
        play music "nordic_report_1.ogg"
        scene gasoutside
        show cs at car_run
        waitress "test 101{w=0.5}{nw}"
    else:
        jump exit_debug

    if fun_value(102):
        play music "nordic_report_2.ogg"
        scene carback1
        show cs at typewriter_location
        mario "test 102{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(103):
        play music "now_what.ogg"
        scene hardwareinside
        show cs at midoffscreenright
        smiley "test 103{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(104):
        play music "onett.ogg"
        scene hardwareoutside
        show cs at midoffscreenleftspin
        violent_jay "test 104{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(105):
        play music "park_theme.ogg"
        scene cultforest
        show cs at offscreenrightspin
        shaggy_too_dope "test 105{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(106):
        play music "passport.ogg"
        scene mcdonalds
        show cs at offscreenleftspin
        joel "test 106{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(107):
        play music "passport_real.ogg"
        scene mcdees
        show cs worried punished
        ikea_greeter "test 107{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(108):
        play music "passport_ytp.ogg"
        scene rushmore
        ikea_worker "test 108{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(109):
        play music "penthouse.ogg"
        scene csmore
        pomni "test 109{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(110):
        play music "pixel_peeker_polka.ogg"
        scene omaha
        average_swede "test 110{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(111):
        play music "pokey.ogg"
        scene alleyway
        alien "test 111{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(112):
        play music "police_station.ogg"
        scene peppinopizzabg
        moomin "test 112{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(113):
        play music "pressing_pursuit_cornered.ogg"
        scene peppinopizzafg
        snufkin "test 113{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(114):
        play music "price_right.ogg"
        scene wozniaktroubles
        alicia "test 114{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(115):
        play music "prophet_2001.ogg"
        scene cshouse_vaporized
        witch "test 115{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(116):
        play music "prophetpart2.ogg"
        scene cscar1
        renovator "test 116{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(117):
        play music "real_world.ogg"
        scene cscar1arc
        cruise "test 117{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(118):
        play music "rosens_loop.ogg"
        scene cscar2
        baumer "test 118{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(119):
        play music "scales_of_joy.ogg"
        scene utah
        copguyexe "test 119{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(120):
        play music "school.ogg"
        scene utahsign
        l_cultist "test 120{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(121):
        play music "showtime.ogg"
        scene utahnight
        tate_offscreen "test 121{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(122):
        play music "snufkin.ogg"
        scene pizzaplace
        pakoo_offscreen "test 122{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(123):
        play music "speedy_comet.ogg"
        scene legodoor
        green_offscreen "test 123{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(124):
        play music "stal.ogg"
        scene legodooropen
        anno_offscreen "test 124{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(125):
        play music "star_spangled_banner.ogg"
        scene legostage
        ed_ai "test 125{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(126):
        play music "street_noise.ogg"
        scene vegas
        obamanobeep "test 126{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(127):
        play music "summer_clearance_sale.ogg"
        scene strip
        bomahanobeep "test 127{w=0.5}{nw}"
    else:
        jump exit_debug
    if fun_value(128):
        play music "super_friendly.ogg"
        scene slots
        RCOMEM "test 128{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(129):
        play music "sweet_victory.ogg"
        scene tablegames
        k_doctor "test 129{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(130):
        play music "taiikusai_desu_yo.ogg"
        scene pokertable
        k_nurse "test 130{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(131):
        play music "take_trip.ogg"
        scene luigi1
        l_snow "test 131{w=0.5}{nw}"
        pause 1.0
    else:
        jump exit_debug
    if fun_value(132):
        play music "take_trip2.ogg"
        scene luigi2
        pause 1.0
    else:
        jump exit_debug
    if fun_value(133):
        play music "the_rest_of_bubble_tea.ogg"
        scene vegasbathroom
        pause 1.0
    else:
        jump exit_debug
    if fun_value(134):
        play music "the_whale.ogg"
        scene backroomcasino
        pause 1.0
    else:
        jump exit_debug
    if fun_value(135):
        play music "thousand_march.ogg"
        scene outsafe
        pause 1.0
    else:
        jump exit_debug
    if fun_value(136):
        play music "time_for_a_smackdown.ogg"
        scene outsafeopen
        pause 1.0
    else:
        jump exit_debug
    if fun_value(137):
        play music "track3.ogg"
        scene insafe
        pause 1.0
    else:
        jump exit_debug
    if fun_value(138):
        play music "track4.ogg"
        scene carpark
        pause 1.0
    else:
        jump exit_debug
    if fun_value(139):
        play music "trans_atlantic.ogg"
        scene casino1
        pause 1.0
    else:
        jump exit_debug
    if fun_value(140):
        play music "trash_zone.ogg"
        scene fazhall
        pause 1.0
    else:
        jump exit_debug
    if fun_value(141):
        play music "triage_at_dawn.ogg"
        scene fazlobby
        pause 1.0
    else:
        jump exit_debug
    if fun_value(142):
        play music "tumultuous.ogg"
        scene fazplace
        pause 1.0
    else:
        jump exit_debug
    if fun_value(143):
        play music "tuna_fish.ogg"
        scene airplane_seats
        pause 1.0
    else:
        jump exit_debug
    if fun_value(144):
        play music "tunnely_shimbers.ogg"
        scene airport_interior
        pause 1.0
    else:
        jump exit_debug
    if fun_value(145):
        play music "undyne.ogg"
        scene airport_seats
        pause 1.0
    else:
        jump exit_debug
    if fun_value(146):
        play music "upon_me.ogg"
        scene airport_tsa
        pause 1.0
    else:
        jump exit_debug
    if fun_value(147):
        play music "wayward_wanderer.ogg"
        scene airport_inside
        pause 1.0
    else:
        jump exit_debug
    if fun_value(148):
        play music "weird_personalities.ogg"
        scene old_house_outside
        pause 1.0
    else:
        jump exit_debug
    if fun_value(149):
        play music "winter_lullaby.ogg"
        scene old_house_inside
        pause 1.0
    else:
        jump exit_debug
    if fun_value(150):
        play music "wool_gloves.ogg"
        scene cc_parking_lot
        pause 1.0
    else:
        jump exit_debug
    if fun_value(151):
        play music "xddcc.ogg"
        scene cc_lobby
        pause 1.0
    else:
        jump exit_debug
    if fun_value(152):
        play music "secret/credits.ogg"
        scene cc_entrance
        pause 1.0
    else:
        jump exit_debug
    if fun_value(153):
        play music "secret/lancer.ogg"
        scene cc_crowd
        pause 1.0
    else:
        jump exit_debug
    if fun_value(154):
        play music "secret/space_classroom.ogg"
        scene cc_stage
        pause 1.0
    else:
        jump exit_debug
    if fun_value(155):
        play music "error.ogg"
        scene cc_backstage
        pause 1.0
    else:
        jump exit_debug
    if fun_value(156):
        play music "yuuka_town.ogg"
        scene billboard
        pause 1.0
    else:
        jump exit_debug
    if fun_value(157):
        play music "tmwstw.ogg"
        scene texas
        pause 0.1
    else:
        jump exit_debug
    if fun_value(158):
        scene tvbilly
        pause 0.1
    else:
        jump exit_debug
    if fun_value(159):
        scene jeep_inside_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(160):
        scene dinerinside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(161):
        scene aria_car_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(162):
        scene aria_room
        pause 0.1
    else:
        jump exit_debug
    if fun_value(163):
        scene aria_apartment_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(164):
        scene cs_somewhere
        pause 0.1
    else:
        jump exit_debug
    if fun_value(165):
        scene dineroutside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(166):
        scene battle_block_without_theater
        pause 0.1
    else:
        jump exit_debug
    if fun_value(167):
        scene final_destination
        pause 0.1
    else:
        jump exit_debug
    if fun_value(168):
        scene police_car_fg
        pause 0.1
    else:
        jump exit_debug
    if fun_value(169):
        scene war_torn_1
        pause 0.1
    else:
        jump exit_debug
    if fun_value(170):
        scene war_torn_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(171):
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
