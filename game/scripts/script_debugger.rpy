label asset_debugger:
    cs "Alright Arc, you ready for the asset debugger?"
    show arceus angry
    arceus "I hate the debugger, it's so uncomfortable!"
    cs "Well, it'll be over in no time! Remember to have bounciness at max!"
    $ sfxtotal = 0
    $ musictotal = 0
    $ bgtotal = 0
    $ charactertotal = 0
    $ spritetotal = 0
    $ movietotal = 0
    $ transformtotal = 0
    if fun_value(1):
        $ sfxtotal += 1
        play sound sfx_achieve
        $ musictotal += 1
        play music ten_feet_away
        $ bgtotal += 1
        scene game_menu
        show craptop blank at center
        show cs at left
        $ spritetotal += 9
        show csgod at mid_left_left
        show anno at mid_left
        show pakoo at mid_mid_left
        show tate at mid_mid_right
        show mean at mid_right
        show k174 at mid_right_right
        show arceus at right 
        n "test 1{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(2):
        $ sfxtotal += 1
        play sound sfx_alt_punch
        $ musictotal += 1
        play music ac_title
        $ bgtotal += 1
        scene black
        show craptop car at center
        show cs flipped at left
        $ spritetotal += 9
        show csgod flipped at mid_left_left
        show anno prison at mid_left
        show pakoo dark at mid_mid_left
        show tate dark at mid_mid_right
        show mean flipped at mid_right
        show k174 flipped at mid_right_right
        show arceus flipped at right 
        cs "test 2{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(3):
        $ sfxtotal += 1
        play sound sfx_back
        $ musictotal += 1
        play music afternoon_hills
        $ bgtotal += 1
        scene cs_room
        show craptop desktop at center
        show cs happy at left
        $ spritetotal += 9
        show csgod_angry at mid_left_left
        show anno guard at mid_left
        show pakoo flipped at mid_mid_left
        show tate flipped at mid_mid_right
        show mean happy at mid_right
        show k199 at mid_right_right
        cs_fakegod "test 3{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(4):
        $ sfxtotal += 1
        play sound sfx_beam
        $ musictotal += 1
        play music airport
        $ bgtotal += 1
        scene cs_room_2
        show craptop discord at center
        show cs happy flipped at left
        $ spritetotal += 9
        show young_cs at mid_left_left
        show anno guard dark at mid_left
        show pakoo dark flipped at mid_mid_left
        show tate dark flipped at mid_mid_right
        show mean happy flipped at mid_right
        show k199 flipped at mid_right_right
        show arceus dirty at right 
        craptop "test 4{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(5):
        $ sfxtotal += 1
        play sound sfx_bell
        $ musictotal += 1
        play music airport_counter
        $ bgtotal += 1
        scene craptop_bg
        show craptop edit at center
        show cs happy dark at left
        $ spritetotal += 9
        show rich at mid_left_left
        show copguy at mid_left
        show pakoo worried at mid_mid_left
        show tate srs at mid_mid_right
        show mean happy2 at mid_right
        show k207 at mid_right_right
        show arceus dirty flipped at right 
        sticky "test 5{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(6):
        $ sfxtotal += 1
        play sound sfx_bossappears
        $ musictotal += 1
        play music alien_atmosphere
        $ bgtotal += 1
        scene cs_house
        show craptop error at center
        show cs happy dark flipped at left
        $ spritetotal += 9
        show ed at mid_left_left
        show copguy flipped at mid_left
        show pakoo worried flipped at mid_mid_left
        show tate srs dark at mid_mid_right
        show mean happy2 flipped at mid_right
        show k207 flipped at mid_right_right
        show arceus full happy at right 
        discord "test 6{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(7):
        $ sfxtotal += 1
        play sound sfx_britishpound
        $ musictotal += 1
        play music another_him
        $ bgtotal += 1
        scene cs_car
        show craptop off at center
        show cs angry at left
        $ spritetotal += 9
        show ed phone at mid_left_left
        show copguy dark at mid_left
        show pakoo disappointed at mid_mid_left
        show tate srs flipped at mid_mid_right
        show mean surprised at mid_right
        show k207h at mid_right_right
        show arceus full happy flipped at right 
        nova "test 7{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(8):
        $ sfxtotal += 1
        play sound sfx_bucket
        $ musictotal += 1
        play music apple_kid
        $ bgtotal += 1
        scene cs_car_inside
        show craptop sad at center
        show cs angry dark at left
        $ spritetotal += 9
        show wesley at mid_left_left
        show copguy dark flipped at mid_left
        show pakoo disappointed flipped at mid_mid_left
        show tate srs dark flipped at mid_mid_right
        show mean surprised flipped at mid_right
        show k207h flipped at mid_right_right
        show arceus full at right 
        carguy "test 8{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(9):
        $ sfxtotal += 1
        play sound sfx_car_crash
        $ musictotal += 1
        play music atarashii_kaze
        $ bgtotal += 1
        scene walmart_outside
        show craptop updating at center
        show cs angry flipped at left
        $ spritetotal += 9
        show worker_1 at mid_left_left
        show copguy_ai at mid_left
        show pakoo happy at mid_mid_left
        show tate shock at mid_mid_right
        show michael at mid_right
        show nova1 at mid_right_right
        show arceus full flipped at right 
        carguy_nobeep "test 9{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(10):
        $ sfxtotal += 1
        play sound sfx_car_horn
        $ musictotal += 1
        play music automatic_love
        $ bgtotal += 1
        scene walmart_inside
        show craptop ytp at center
        show cs angry dark flipped at left
        $ spritetotal += 9
        show worker_2 at mid_left_left
        show copguycrawl at mid_left
        show pakoo happy flipped at mid_mid_left
        show tate shock dark at mid_mid_right
        show phil at mid_right
        show nova2 at mid_right_right
        show arceus full angry at right 
        greeter "test 10{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(11):
        $ sfxtotal += 1
        play sound sfx_chatter
        $ musictotal += 1
        play music basement
        $ bgtotal += 1
        scene walmart_aisle
        show craptop evidence at center
        show cs worried at left
        $ spritetotal += 9
        show worker_3 at mid_left_left
        show sheriff at mid_left
        show linus at mid_mid_left
        show tate shock flipped at mid_mid_right
        show carguy at mid_right
        show nova3 at mid_right_right
        show arceus full angry flipped at right 
        doug "test 11{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(12):
        $ sfxtotal += 1
        play sound sfx_cheer1
        $ musictotal += 1
        play music bestmusicu
        $ bgtotal += 1
        scene walmart_register_fg
        show craptopreal at center
        show cs worried flipped at left
        $ spritetotal += 9
        show worker_4 at mid_left_left
        show cop at mid_left
        show luke at mid_mid_left
        show tate shock dark flipped at mid_mid_right
        show carguy flipped at mid_right
        show carguya at mid_right_right
        show arceus angry at right 
        cashier "test 12{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(13):
        $ sfxtotal += 1
        play sound sfx_cheer2
        $ musictotal += 1
        play music billy_mix
        $ bgtotal += 1
        scene walmart_register
        show craptopsmall at center
        show cs disappointed at left
        $ spritetotal += 9
        show worker_5 at mid_left_left
        show cop dark at mid_left
        show luke flipped at mid_mid_left
        show tate smug at mid_mid_right
        show doug at mid_right
        show hart1 at mid_right_right
        show arceus angry flipped at right 
        ycs "test 13{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(14):
        $ sfxtotal += 1
        play sound sfx_cheers
        $ musictotal += 1
        play music billy_radio
        $ bgtotal += 1
        scene cs_door_closed
        show craptopsmall flipped at center
        show cs disappointed metal at left
        $ spritetotal += 9
        show worker_5alt at mid_left_left
        show cop_2 at mid_left
        show taran at mid_mid_left
        show tate smug dark at mid_mid_right
        show billy at mid_right
        show hart2 at mid_right_right
        show arceus angry dark at right 
        hoh_operator "test 14{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(15):
        $ sfxtotal += 1
        play sound sfx_chop
        $ musictotal += 1
        play music Billymusicu
        $ bgtotal += 1
        scene cs_door_open
        show billy car at mid_right
        show post_it at center
        show cs disappointed metal2 at left
        $ spritetotal += 9
        show worker_6 at mid_left_left
        show guard_soldier at mid_left
        show taran flipped at mid_mid_left
        show tate smug flipped at mid_mid_right
        show cultist at mid_right_right
        show arceus angry dark flipped at right 
        rich "test 15{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(16):
        $ sfxtotal += 1
        play sound sfx_clapperboard
        $ musictotal += 1
        play music blazing_corridor
        $ bgtotal += 1
        scene rosen_abode
        show billy car happy at mid_right
        show ytx at center
        show cs disappointed metal3 at left
        $ spritetotal += 9
        show worker_7 at mid_left_left
        show marine at mid_left
        show colton at mid_mid_left
        show tate smug dark flipped at mid_mid_right
        show cultist gun at mid_right_right
        show arceus guard at right 
        ed "test 16{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(17):
        $ sfxtotal += 1
        play sound sfx_clonk
        $ musictotal += 1
        play music breakout
        $ bgtotal += 1
        scene cs_street
        show billy car turn at mid_right
        show objection at center
        show cs disappointed metal4 at left
        $ spritetotal += 9
        show digi at mid_left_left
        show big_tank at mid_left
        show nfanboy at mid_mid_left
        show tate sheepish at mid_mid_right
        show cultist_2 at mid_right_right
        show arceus guard flipped at right 
        wesley "test 17{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(18):
        $ sfxtotal += 1
        play sound sfx_csnore
        $ musictotal += 1
        play music brick_by_dick
        $ bgtotal += 1
        scene hoh_outside
        show hold_it at center
        show cs disappointed flipped at left
        $ spritetotal += 9
        show digi dark at mid_left_left
        show asylum_worker at mid_left
        show afanboy at mid_mid_left
        show tate sheepish flipped at mid_mid_right
        show billy laser at mid_right
        show cultist_3 at mid_right_right
        show arceus happy at right 
        michael "test 18{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(19):
        $ sfxtotal += 1
        play sound sfx_doorbell
        $ musictotal += 1
        play music broken_sky
        $ bgtotal += 1
        scene hoh_hq
        show scott_border at center
        show cs concentrate at left
        $ spritetotal += 9
        show digi flipped at mid_left_left
        show aria at mid_left
        show nova at mid_mid_left
        show tate sad at mid_mid_right
        show billy dark at mid_right
        show kitty at mid_right_right
        show arceus happy flipped at right 
        michael_nobeep "test 19{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(20):
        $ sfxtotal += 1
        play sound sfx_doorslam
        $ musictotal += 1
        play music bubble_tea
        $ bgtotal += 1
        scene hoh_hq2
        show cswanted at center
        show cs concentrate dark at left
        $ spritetotal += 9
        show digi dark flipped at mid_left_left
        show aria flipped at mid_left
        show nova dark at mid_mid_left
        show tate sad flipped at mid_mid_right
        show cashier at mid_right
        show kitty flipped at mid_right_right
        show arceus happy dark at right 
        phil "test 20{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(21):
        $ sfxtotal += 1
        play sound sfx_drill
        $ musictotal += 1
        play music bun_guster
        $ bgtotal += 1
        scene hoh_hq3
        show laser_beam at center
        show cs concentrate flipped at left
        $ spritetotal += 9
        show guest at mid_left_left
        show aria dark at mid_left
        show nova flipped at mid_mid_left
        show tate stare at mid_mid_right
        show scott at mid_right
        show blank at mid_right_right
        show arceus happy dark flipped at right 
        worker_1 "test 21{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(22):
        $ sfxtotal += 1
        play sound sfx_drillbreak
        $ musictotal += 1
        play music buy_something
        $ bgtotal += 1
        scene hoh_hq4
        show cards1 at center
        show cs dark at left
        $ spritetotal += 9
        show janitor at mid_left_left
        show aria dark flipped at mid_left
        show nova dark flipped at mid_mid_left
        show tate stare flipped at mid_mid_right
        show obama at mid_right
        show midge at mid_right_right
        show arceus prison at right 
        worker_2 "test 22{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(23):
        $ sfxtotal += 1
        play sound sfx_driving
        $ musictotal += 1
        play music candle_world
        $ bgtotal += 1
        scene hoh_hq5
        show cards2 at center
        show cs dark flipped at left
        $ spritetotal += 9
        show customer at mid_left_left
        show bouncer1 at mid_left
        show peppino at mid_mid_left
        show gnome at mid_mid_right
        show discord at mid_right
        show mika at mid_right_right
        show arceus prison flipped at right 
        worker_3 "test 23{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(24):
        $ sfxtotal += 1
        play sound sfx_duck
        $ musictotal += 1
        play music canyon
        $ bgtotal += 1
        scene hoh_elevator
        show cards3 at center
        show cs dusk at left
        $ spritetotal += 9
        show howie at mid_left_left
        show bouncer2 at mid_left
        show peppino2 at mid_mid_left
        show waitress at mid_mid_right
        show border_guard at mid_right
        show mika dark at mid_right_right
        show arceus worried at right 
        worker_4 "test 24{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(25):
        $ sfxtotal += 1
        play sound sfx_earthquake
        $ musictotal += 1
        play music canyon_but_in_the_car
        $ bgtotal += 1
        scene helipad
        show cards4 at center
        show cs disappointed dark at left
        $ spritetotal += 9
        show howie flipped at mid_left_left
        show trailtrash at mid_left
        show streetguy at mid_mid_left
        show terry at mid_mid_right
        show border_guard dusk at mid_right
        show db at mid_right_right
        show arceus worried flipped at right 
        worker_5 "test 25{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(26):
        $ sfxtotal += 1
        play sound sfx_elevator_ding
        $ musictotal += 1
        play music canyon_but_in_the_car_real
        $ bgtotal += 1
        scene jail_inside
        show cards5 at center
        show cs disappointed dark flipped at left
        $ spritetotal += 9
        show smiley at mid_left_left
        show trailtrash flipped at mid_left
        show pencilguy at mid_mid_left
        show mettaton at mid_mid_right
        show benrey at mid_right
        show db_cooper at mid_right_right
        show arceus dirty worried at right 
        worker_6 "test 26{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(27):
        $ sfxtotal += 1
        play sound sfx_foundationfail
        $ musictotal += 1
        play music canyon_real
        $ bgtotal += 1
        scene jail_cell
        show con_screen at center
        show cs disappointed dusk at left
        $ spritetotal += 9
        show mario at mid_left_left
        show green at mid_left
        show gordon at mid_mid_left
        show scott_pres at mid_mid_right
        show joel at mid_right
        show ges at mid_right_right
        show arceus dirty worried flipped at right 
        worker_7 "test 27{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(28):
        $ sfxtotal += 1
        play sound sfx_gamer_and_girl
        $ musictotal += 1
        play music card_castle
        $ bgtotal += 1
        scene border
        show case at center
        show cs worried dark at left
        $ spritetotal += 9
        show mario flipped at mid_left_left
        show green flipped at mid_left
        show car at mid_mid_left
        show miku at mid_mid_right
        show joel flipped at mid_right
        show renovator at mid_right_right
        show arceus worried dark at right 
        digi "test 28{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(29):
        $ sfxtotal += 1
        play sound sfx_gasp
        $ musictotal += 1
        play music chase
        $ bgtotal += 1
        scene outside_tim_hortons
        show case flipped at center
        show cs worried dark flipped at left
        $ spritetotal += 9
        show violent_jay at mid_left_left
        show jerma at mid_left
        show tom at mid_mid_left
        show sayori at mid_mid_right
        show ikea_greeter at mid_right
        show shadowman at mid_right_right
        show arceus worried dark flipped at right 
        pakoo "test 29{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(30):
        $ sfxtotal += 1
        play sound sfx_glass
        $ musictotal += 1
        play music circus
        $ bgtotal += 1
        scene inside_tim_hortons_fg
        show bag at center
        show cs prison at left
        $ spritetotal += 9
        show shaggy_too_dope at mid_left_left
        show lego at mid_left
        show james at mid_mid_left
        show fumobee at mid_mid_right
        show ikea_greeter blahaj at mid_right
        show pencilcashier at mid_right_right
        show arceus dark at right 
        addy "test 30{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(31):
        $ sfxtotal += 1
        play sound sfx_heartbeat
        $ musictotal += 1
        play music cliffs
        $ bgtotal += 1
        scene inside_tim_hortons
        show bag flipped at center
        show cs prison_worried at left
        $ spritetotal += 9
        show blue_light at mid_left_left
        show lego eyes at mid_left
        show jeremy at mid_mid_left
        show fumobee2 at mid_mid_right
        show ikea_greeter flipped at mid_right
        show cruise at mid_right_right
        show arceus dark flipped at right 
        copguy "test 31{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(32):
        $ sfxtotal += 1
        play sound sfx_hitbod1
        $ musictotal += 1
        play music clownpiece
        $ bgtotal += 1
        scene tunnel
        show drill at center
        show cs guard at left
        $ spritetotal += 9
        show red_light at mid_left_left
        show tsa at mid_left
        show hammond at mid_mid_left
        show cards5alt at mid_mid_right
        show swede at mid_right
        show cruise flipped at mid_right_right
        show arceus dusk at right 
        arceus "test 32{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(33):
        $ sfxtotal += 1
        play sound sfx_hitbod2
        $ musictotal += 1
        play music compulsion_to_obey
        $ bgtotal += 1
        scene canada
        show drillbreak at center
        show cs guard dark at left
        $ spritetotal += 9
        show copguy_ex_front at mid_left_left
        show monika at mid_left
        show mean ayo at mid_mid_left
        show lancer at mid_mid_right
        show alien at mid_right
        show lunatic_cultist at mid_right_right
        show arceus angry dusk at right 
        anno "test 33{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(34):
        $ sfxtotal += 1
        play sound sfx_hitbod3
        $ musictotal += 1
        play music conflict
        $ bgtotal += 1
        scene flag
        show sansbrick at center
        show cs fakegod at left
        $ spritetotal += 9
        show copguy_ex_back at mid_left_left
        show weird_al at mid_left
        show mean ayo flipped at mid_mid_left
        show lancer flipped at mid_mid_right
        show alien dead at mid_right
        show lunatic_cultist flipped at mid_right_right
        show arceus dusk flipped at right 
        border_guard "test 34{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(35):
        $ sfxtotal += 1
        play sound sfx_hks1
        $ musictotal += 1
        play music cp_violation
        $ bgtotal += 1
        scene outside_ltt
        show oldgame at center
        show cs guitar at left
        $ spritetotal += 9
        show ai_ducks at mid_left_left
        show cpt_underpants at mid_left
        show mean angry at mid_mid_left
        show bubble at mid_mid_right
        show ikea_worker at mid_right
        show priest at mid_right_right
        show arceus worried dusk at right
        linus "test 35{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(36):
        $ sfxtotal += 1
        play sound sfx_hks2
        $ musictotal += 1
        play music creative_exercise
        $ bgtotal += 1
        scene inside_ltt
        show m4 at center
        show cs surprised at left
        $ spritetotal += 9
        show stage_screen at mid_left_left
        show david at mid_left
        show mean angry flipped at mid_mid_left
        show tate smug sil_white flipped at mid_mid_right
        show pomni at mid_right
        show priest flipped at mid_right_right
        show train_fly_1 at right
        asylum_worker "test 36{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(37):
        $ sfxtotal += 1
        play sound sfx_hks3
        $ musictotal += 1
        play music danger_mystery
        $ bgtotal += 1
        scene alley
        show m4 flipped at center
        show cs surprised flipped at left
        $ spritetotal += 8
        show george at mid_left_left
        show zenigata at mid_left
        show mean wat at mid_mid_left
        show tate cry at mid_mid_right
        show moomin at mid_right
        show train_fly_2 at right
        csgod "test 37{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(38):
        $ sfxtotal += 1
        play sound sfx_hold_it
        $ musictotal += 1
        play music dealin_dope
        $ bgtotal += 1
        scene question
        show m4 fire at center
        show cs scared at left
        $ spritetotal += 8
        show harold at mid_left_left
        show zenigata flipped at mid_left
        show mean wat flipped at mid_mid_left
        show tate cry flipped at mid_mid_right
        show snufkin at mid_right
        show train_fly_3 at right
        luke "test 38{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(39):
        $ sfxtotal += 1
        play sound sfx_isaac
        $ musictotal += 1
        play music dense_woods_b
        $ bgtotal += 1
        scene asylum
        show m4 fire flipped at center
        show mr_krupp at mid_left_left
        show cs scared flipped at left
        $ spritetotal += 6
        show mean furious at mid_mid_left
        show alicia at mid_right
        show train_fly_4 at right
        taran "test 39{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(40):
        $ sfxtotal += 1
        play sound sfx_joj_loop
        $ musictotal += 1
        play music desert_dawn
        $ bgtotal += 1
        scene csdesk
        show script at center
        show cs scared dark at left
        $ spritetotal += 5
        show mean furious at mid_mid_left
        show witch at mid_right
        show train_fly_5 at right
        colton "test 40{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(41):
        $ sfxtotal += 1
        play sound sfx_keyboard
        $ musictotal += 1
        play music dig_this
        $ bgtotal += 1
        scene csvideo
        show post_it2 at center
        show cs insane worried at left
        $ spritetotal += 6
        show mean furious flipped at mid_mid_left
        show moomin flipped at mid_right
        show train_fly_6 at mid_right_right
        show train_boss_1 at right
        sheriff "test 41{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(42):
        $ sfxtotal += 1
        play sound sfx_knock
        $ musictotal += 1
        play music dinerfight
        $ bgtotal += 1
        scene setup
        show colorbars at center
        show cs insane worried flipped at left
        $ spritetotal += 6
        show mean tired at mid_mid_left
        show snufkin flipped at mid_right
        show train_fly_7 at mid_right_right
        show train_boss_2 at right
        billy "test 42{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(43):
        $ sfxtotal += 1
        play sound sfx_legosfx
        $ musictotal += 1
        play music dragon_castle
        $ bgtotal += 1
        scene loffice
        show paper at center
        show cs insane disappointed at left
        $ spritetotal += 6
        show mean tired flipped at mid_mid_left
        show alicia flipped at mid_right
        show flying_train_final at mid_right_right
        show train_boss_3 at right
        tv_billy "test 43{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(44):
        $ sfxtotal += 1
        play sound sfx_less_annoying_alarm_sound
        $ musictotal += 1
        play music echoing
        $ bgtotal += 1
        scene ltt_bg
        show pipe_gun at center
        show cs horse at left
        $ spritetotal += 5
        show mean worried at mid_mid_left
        show witch flipped at mid_right
        show train_boss_4 at right
        cultist "test 44{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(45):
        $ sfxtotal += 1
        play sound sfx_metalpipe
        $ musictotal += 1
        play music echoingspring
        $ bgtotal += 1
        scene ltt_fg
        show pipe_gun flipped at center
        show cs horse flipped at left
        $ spritetotal += 5
        show mean worried flipped at mid_mid_left
        show baumer at mid_right
        show train_boss_5 at right
        cultist_2 "test 45{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(46):
        $ sfxtotal += 1
        play sound sfx_nice_car
        $ musictotal += 1
        play music energetic_rock
        $ bgtotal += 1
        scene frontdoor
        show cheetos at center
        show cs pissed at left
        $ spritetotal += 5
        show mean scared at mid_mid_left
        show baumer flipped at mid_right
        show train_boss_6 at right
        cultist_3 "test 46{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(47):
        $ sfxtotal += 1
        play sound sfx_not_so_nice_scratch
        $ musictotal += 1
        play music everlong
        $ bgtotal += 1
        scene road_to_canada
        show bear at center
        show mean scared flipped at mid_mid_left
        show cs pissed flipped at left
        $ spritetotal += 4
        show train_boss_7 at right
        scott "test 47{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(48):
        $ sfxtotal += 1
        play sound sfx_obama
        $ musictotal += 1
        play music everybody_wants
        $ bgtotal += 1
        scene border_dusk
        show dog at center
        show mean unamused at mid_mid_left
        show cs cultist at left
        $ spritetotal += 4
        show train_boss_final at right
        terry "test 48{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(49):
        $ sfxtotal += 1
        play sound sfx_objection
        $ musictotal += 1
        play music exotic
        $ bgtotal += 1
        scene sheriff_office
        show pig at center
        show mean unamused flipped at mid_mid_left
        show cs cultist flipped at left
        $ spritetotal += 4
        show zenigata car at mid_right
        carla "test 49{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(50):
        $ sfxtotal += 1
        play sound sfx_okuubeam
        $ musictotal += 1
        play music facing_worlds
        $ bgtotal += 1
        scene washington_road
        show pot_lift at center
        show mean human at mid_left
        show amtrak_conductor at mid_mid_left
        show cs disappointed cultist at left
        $ spritetotal += 5
        show after_true_title at mid_right
        peppino "test 50{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(51):
        $ sfxtotal += 1
        play sound sfx_page
        $ musictotal += 1
        play music fastbudget_song
        $ bgtotal += 1
        scene washington_road day
        show pot at center
        show mean angry sil_white flipped at mid_left
        show amtrak_conductor flipped at mid_mid_left
        show cs angry cultist at left
        $ spritetotal += 4
        iris "test 51{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(52):
        $ sfxtotal += 1
        play sound sfx_payday
        $ musictotal += 1
        play music fasting
        $ bgtotal += 1
        scene washington_road dusk
        show pot_sunken at center
        show mean human flipped at mid_left
        show amtrak_stewardess at mid_mid_left
        show cs disappointed cultist flipped at left
        $ spritetotal += 4
        lego "test 52{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(53):
        $ sfxtotal += 1
        play sound sfx_ping
        $ musictotal += 1
        play music fastport
        $ bgtotal += 1
        scene washington_road morning
        show pot_beam at center
        show mean human happy at mid_left
        show amtrak_stewardess flipped at mid_mid_left
        show cs angry cultist flipped at left
        $ spritetotal += 4
        trailtrash "test 53{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(54):
        $ sfxtotal += 1
        play sound sfx_ping_spam
        $ musictotal += 1
        play music flyday_chinatown
        $ bgtotal += 1
        scene copcar
        show onscreen_sharpener at center
        show mean human happy flipped at mid_left
        show lupin at mid_mid_left
        show cs pencil at left
        $ spritetotal += 4
        green "test 54{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(55):
        $ sfxtotal += 1
        play sound sfx_puke
        $ musictotal += 1
        play music fnaf_6
        $ bgtotal += 1
        scene copcar_mask
        show renault at center
        show mean human annoyed at mid_left
        show lupin flipped at mid_mid_left
        show cs angry pencil at left
        $ spritetotal += 4
        jerma "test 55{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(56):
        $ sfxtotal += 1
        play sound sfx_punch
        $ musictotal += 1
        play music for_the_people
        $ bgtotal += 1
        scene microcenter
        show passportdigi at center
        show lupin hat at mid_mid_left
        show mean human annoyed flipped at mid_left
        show cs disappointed pencil at left
        $ spritetotal += 4
        pencil "test 56{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(57):
        $ sfxtotal += 1
        play sound sfx_punch_alt
        $ musictotal += 1
        play music fourside
        $ bgtotal += 1
        scene microinside
        show copguyexe at center
        show mean human shocked at mid_left
        show lupin hat flipped at mid_mid_left
        show cs phone at left
        $ spritetotal += 4
        signup "test 57{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(58):
        $ sfxtotal += 1
        play sound sfx_ringtone
        $ musictotal += 1
        play music france
        $ bgtotal += 1
        scene cashzone
        show copguyexe flipped at center
        show mean human shocked flipped at mid_left
        show cs phone flipped at left
        $ spritetotal += 3
        host "test 58{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(59):
        $ sfxtotal += 1
        play sound sfx_roll_window
        $ musictotal += 1
        play music friendship
        $ bgtotal += 1
        scene cashzone_foreground
        show RCOMEM at center
        show kuwait_doctor_1 at mid_left
        show kuwait_nurse_1 at mid_right
        show kuwait_lieutenant_snow at mid_mid_right
        show cs disappointed phone at left
        $ spritetotal += 5
        tsa "test 59{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(60):
        $ sfxtotal += 1
        play sound sfx_select
        $ musictotal += 1
        play music full_rulle_med_klas
        $ bgtotal += 1
        scene cpuaisle
        show tate_ex_front at center
        show mean human angry at mid_left
        show cs disappointed phone flipped at left
        $ spritetotal += 3
        luigi "test 60{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(61):
        $ sfxtotal += 1
        play sound sfx_siren
        $ musictotal += 1
        play music funiculi_holiday
        $ bgtotal += 1
        scene gpuaisle
        show tate_ex_preparation at center
        show mean human angry flipped at mid_left
        show cs worried phone at left
        $ spritetotal += 3
        mika "test 61{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(62):
        $ sfxtotal += 1
        play sound sfx_slots
        $ musictotal += 1
        play music gold_room
        $ bgtotal += 1
        scene gpuaisle2
        show tate_ex at center
        show fake_rpg_miss at mid_left_left
        show cs worried phone flipped at left
        $ spritetotal += 3
        k174 "test 62{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(63):
        $ sfxtotal += 1
        play sound sfx_somethingchanged
        $ musictotal += 1
        play music good_eatin
        $ bgtotal += 1
        scene testing_main
        show ltt_bottle at center
        show oof_45 at mid_left_left
        show cs angry phone at left
        $ spritetotal += 3
        k199 "test 63{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(64):
        $ sfxtotal += 1
        play sound sfx_sparkle
        $ musictotal += 1
        play music happy_roaming
        $ bgtotal += 1
        scene testing_front
        show amtrak_dining_food at center
        show oof_54 at mid_left_left
        show cs angry phone flipped at left
        $ spritetotal += 3
        k207 "test 64{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(65):
        $ sfxtotal += 1
        play sound sfx_splash
        $ musictotal += 1
        play music happy_rock
        $ bgtotal += 1
        scene course_1
        show amtrak_dining_pancake at center
        show oof_52 at mid_left_left
        show cs scared phone at left
        $ spritetotal += 3
        billy_far "test 65{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(66):
        $ sfxtotal += 1
        play sound sfx_start_rocking
        $ musictotal += 1
        play music happy_running
        $ bgtotal += 1
        scene course_2
        show boom at center
        show cs scared phone flipped at left
        $ spritetotal += 2
        direct "test 66{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(67):
        $ sfxtotal += 1
        play sound sfx_thunder
        $ musictotal += 1
        play music hard_drive
        $ bgtotal += 1
        scene course_3
        show mean_clothes at center
        show cs surprised phone at left
        $ spritetotal += 2
        monika "test 67{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(68):
        $ sfxtotal += 1
        play sound sfx_tinnitus
        $ musictotal += 1
        play music hightop
        $ bgtotal += 1
        scene canada_block
        show cs surprised phone flipped at left
        $ spritetotal += 1
        lancer "test 68{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(69):
        $ sfxtotal += 1
        play sound sfx_tiresqueal
        $ musictotal += 1
        play music hired_guns
        $ bgtotal += 1
        scene dealership
        show cs pissed phone at left
        $ spritetotal += 1
        tate "test 69{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(70):
        $ sfxtotal += 1
        play sound sfx_valid
        $ musictotal += 1
        play music hitmewithyourbestshot
        $ bgtotal += 1
        scene dealer_cars
        show cs pissed phone flipped at left
        $ spritetotal += 1
        kitty "test 70{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(71):
        $ sfxtotal += 1
        play sound sfx_victorypunch
        $ musictotal += 1
        play music hitsquad_2
        $ bgtotal += 1
        scene flintcar_outside
        show cs concentrate phone at left
        $ spritetotal += 1
        obama "test 71{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(72):
        $ sfxtotal += 1
        play sound sfx_waterphone
        $ musictotal += 1
        play music hohsis_theme
        $ bgtotal += 1
        scene flintcar_fg
        show cs concentrate phone flipped at left
        $ spritetotal += 1
        bomaha "test 72{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(73):
        $ sfxtotal += 1
        play sound sfx_windows_logon
        $ musictotal += 1
        play music hohsisremix
        $ bgtotal += 1
        scene car_inside_fg
        show cs at rotate_10
        $ transformtotal += 1
        blank "test 73{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(74):
        $ sfxtotal += 1
        play sound sfx_yelling
        $ musictotal += 1
        play music home_depot
        $ bgtotal += 1
        scene joj_charger_fg
        show cs at rotate_6
        $ transformtotal += 1
        aria "test 74{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(75):
        $ sfxtotal += 1
        play sound sfx_ytpintro
        $ musictotal += 1
        play music honk_song
        $ bgtotal += 1
        scene comments
        show cs at rotate_5
        $ transformtotal += 1
        aria_alt "test 75{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(76):
        $ sfxtotal += 1
        play sound sfx_explosion
        $ musictotal += 1
        play music insane_personalities
        $ bgtotal += 1
        scene hospital_room
        show cs at center_left
        $ transformtotal += 1
        cop "test 76{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(77):
        $ sfxtotal += 1
        play sound sfx_funni
        $ musictotal += 1
        play music killcops
        $ bgtotal += 1
        scene hospital_reception
        show cs at center_right
        $ transformtotal += 1
        midge "test 77{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(78):
        $ sfxtotal += 1
        play sound sfx_gul
        $ musictotal += 1
        play music klaxon_beat
        $ bgtotal += 1
        scene ticket_counter
        show cs at mid_center_right
        $ transformtotal += 1
        db "test 78{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(79):
        $ sfxtotal += 1
        play sound sfx_vine
        $ musictotal += 1
        play music la_by_night
        $ bgtotal += 1
        scene backseat
        show cs at mid_offscreen_right
        $ transformtotal += 1
        customer "test 79{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(80):
        $ sfxtotal += 1
        play sound sfx_amtrak_horn
        $ musictotal += 1
        play music lady_of_the_cold
        $ bgtotal += 1
        scene hotel_lobby
        show cs at mid_offscreen_left
        $ transformtotal += 1
        guest "test 80{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(81):
        $ sfxtotal += 1
        play sound sfx_billymaysfap
        $ musictotal += 1
        play music laurel_palace
        $ bgtotal += 1
        scene hotel_room
        show cs at xstretch_in
        $ transformtotal += 1
        ges "test 81{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(82):
        $ sfxtotal += 1
        play sound sfx_fart
        $ musictotal += 1
        play music lego_island
        $ bgtotal += 1
        scene hotel_breakfast
        show cs at xstretch_out
        $ transformtotal += 1
        nurse "test 82{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(83):
        $ sfxtotal += 1
        play sound sfx_fart_again
        $ musictotal += 1
        play music lets_hear_my_baby
        $ bgtotal += 1
        scene hotel_guitar_hero
        show cs at little_bounce
        $ transformtotal += 1
        benrey "test 83{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(84):
        $ sfxtotal += 1
        play sound sfx_fart_deep
        $ musictotal += 1
        play music lets_hear_my_sped
        $ bgtotal += 1
        scene hotel_door
        show cs at t_post_it
        $ transformtotal += 1
        mean "test 84{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(85):
        $ sfxtotal += 1
        play sound sfx_fart_lite
        $ musictotal += 1
        play music letshearspring
        $ bgtotal += 1
        scene hotel_hall
        show cs at t_copguy_frontseat
        $ transformtotal += 1
        agent "test 85{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(86):
        $ sfxtotal += 1
        play sound sfx_fart_with_reverb
        $ musictotal += 1
        play music lisbon_fever
        $ bgtotal += 1
        scene falling
        show cs at t_copguy_frontseat
        $ transformtotal += 1
        agent "test 86{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(87):
        $ sfxtotal += 1
        play sound sfx_hard_knock
        $ musictotal += 1
        play music local_forecast
        $ bgtotal += 1
        scene ltx
        show cs at t_arc_at_tims
        $ transformtotal += 1
        receptionist "test 87{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(88):
        $ sfxtotal += 1
        play sound sfx_hubbub
        $ musictotal += 1
        play music lowbudget_song
        $ bgtotal += 1
        scene ltx_stage
        show cs at t_cs_ltt
        $ transformtotal += 1
        scott_pres "test 88{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(89):
        $ sfxtotal += 1
        play sound sfx_lego_break
        $ musictotal += 1
        play music maladys_melody
        $ bgtotal += 1
        scene in_limo
        show cs at t_linus_ltt
        $ transformtotal += 1
        miku "test 89{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(90):
        $ sfxtotal += 1
        play sound sfx_lightswitch
        $ musictotal += 1
        play music melancholy
        $ bgtotal += 1
        scene tour_bus_inside
        show cs at t_pepzone1
        $ transformtotal += 1
        hammond "test 90{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(91):
        $ sfxtotal += 1
        play sound sfx_poot
        $ musictotal += 1
        play music mis_leader
        $ bgtotal += 1
        scene big_stage
        show cs at t_pepzone2
        $ transformtotal += 1
        jeremy "test 91{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(92):
        $ sfxtotal += 1
        play sound sfx_sliding_door_close
        $ musictotal += 1
        play music mm_complete
        $ bgtotal += 1
        scene stage2
        show cs at t_linus_drop_tips
        $ transformtotal += 1
        james "test 92{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(93):
        $ sfxtotal += 1
        play sound sfx_sliding_door_open
        $ musictotal += 1
        play music mm_select
        $ bgtotal += 1
        scene cs_door_outside
        show cs at t_gun
        $ transformtotal += 1
        tom "test 93{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(94):
        $ sfxtotal += 1
        play sound sfx_whoosh
        $ musictotal += 1
        play music moongazer
        $ bgtotal += 1
        scene manitoba_street
        show cs at t_stage_screen_l
        $ transformtotal += 1
        sayori "test 94{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(95):
        $ sfxtotal += 1
        play sound sfx_sparkles
        $ musictotal += 1
        play music morning_highway
        $ bgtotal += 1
        scene shoe_store
        show cs at t_stage_screen_c
        $ transformtotal += 1
        gnome "test 95{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(96):
        $ sfxtotal += 1
        play sound sfx_spellcast
        $ musictotal += 1
        play music mort_farm
        $ bgtotal += 1
        scene washington_road day
        show cs at t_stage_screen_r
        $ transformtotal += 1
        chat "test 96{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(97):
        $ sfxtotal += 1
        play sound sfx_cat_crash
        $ musictotal += 1
        play music moving_right_along
        $ bgtotal += 1
        scene washington_road dusk
        show cs at t_stagescreen
        $ transformtotal += 1
        unknown "test 97{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(98):
        $ sfxtotal += 1
        play sound sfx_mean_transform
        $ musictotal += 1
        play music muumin_tani_fuyu
        $ bgtotal += 1
        scene washington_road morning
        show cs at t_punchup
        $ transformtotal += 1
        crowd "test 98{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(99):
        $ sfxtotal += 1
        play sound sfx_zenigata_shout
        $ musictotal += 1
        play music neko_to_sanpo
        $ bgtotal += 1
        scene town
        worker "test 99{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(100):
        $ musictotal += 1
        play music night
        $ bgtotal += 1
        scene gasinside
        show toby at center
        show cs at lego_run
        $ transformtotal += 1
        streetguy "test 100{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(101):
        $ musictotal += 1
        play music nordic_report_1
        $ bgtotal += 1
        scene gasoutside
        show cs at car_run
        $ transformtotal += 1
        waitress "test 101{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug

    if fun_value(102):
        $ musictotal += 1
        play music nordic_report_2
        $ bgtotal += 1
        scene carback1
        show cs at typewriter_location
        $ transformtotal += 1
        mario "test 102{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(103):
        $ musictotal += 1
        play music now_what
        $ bgtotal += 1
        scene hardwareinside
        show cs at midoffscreenright
        $ transformtotal += 1
        smiley "test 103{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(104):
        $ musictotal += 1
        play music onett
        $ bgtotal += 1
        scene hardwareoutside
        show cs at midoffscreenleftspin
        $ transformtotal += 1
        violent_jay "test 104{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(105):
        $ musictotal += 1
        play music park_theme
        $ bgtotal += 1
        scene cultforest
        show cs at offscreenrightspin
        $ transformtotal += 1
        shaggy_too_dope "test 105{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(106):
        $ musictotal += 1
        play music passport
        $ bgtotal += 1
        scene mcdonalds
        show cs at offscreenleftspin
        $ transformtotal += 1
        joel "test 106{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(107):
        $ musictotal += 1
        play music passport_real
        $ bgtotal += 1
        scene mcdees
        show cs worried punished
        ikea_greeter "test 107{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(108):
        $ musictotal += 1
        play music passport_ytp
        $ bgtotal += 1
        scene rushmore
        ikea_worker "test 108{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(109):
        $ musictotal += 1
        play music penthouse
        $ bgtotal += 1
        scene csmore
        show cs at t_mean_rollout
        $ transformtotal += 1
        pomni "test 109{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(110):
        $ musictotal += 1
        play music pixel_peeker_polka
        $ bgtotal += 1
        scene omaha
        average_swede "test 110{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(111):
        $ musictotal += 1
        play music pokey
        $ bgtotal += 1
        scene alleyway
        alien "test 111{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(112):
        $ musictotal += 1
        play music police_station
        $ bgtotal += 1
        scene peppinopizzabg
        moomin "test 112{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(113):
        $ musictotal += 1
        play music pressing_pursuit_cornered
        $ bgtotal += 1
        scene peppinopizzafg
        snufkin "test 113{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(114):
        $ musictotal += 1
        play music price_right
        $ bgtotal += 1
        scene wozniaktroubles
        show cs at t_blur_on
        $ transformtotal += 1
        alicia "test 114{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(115):
        $ musictotal += 1
        play music prophet_2001
        $ bgtotal += 1
        scene cshouse_vaporized
        show cs at t_blur_off
        $ transformtotal += 1
        witch "test 115{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(116):
        $ musictotal += 1
        play music prophetpart2
        $ bgtotal += 1
        scene cscar1
        show cs at t_fake_rpg_text(0,0)
        $ transformtotal += 1
        renovator "test 116{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(117):
        $ musictotal += 1
        play music real_world
        $ bgtotal += 1
        scene cscar1arc
        cruise "test 117{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(118):
        $ musictotal += 1
        play music rosens_loop
        $ bgtotal += 1
        scene cscar2
        baumer "test 118{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(119):
        $ musictotal += 1
        play music scales_of_joy
        $ bgtotal += 1
        scene utah
        show cs at t_evil_mika
        $ transformtotal += 1
        copguyexe "test 119{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(120):
        $ musictotal += 1
        play music school
        $ bgtotal += 1
        scene utahsign
        show cs at t_toby
        $ transformtotal += 1
        l_cultist "test 120{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(121):
        $ musictotal += 1
        play music showtime
        $ bgtotal += 1
        scene utahnight
        show cs at t_lupin_out
        $ transformtotal += 1
        tate_offscreen "test 121{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(122):
        $ musictotal += 1
        play music snufin
        $ bgtotal += 1
        scene pizzaplace
        show cs at t_boom
        $ transformtotal += 1
        pakoo_offscreen "test 122{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(123):
        $ musictotal += 1
        play music speedy_comet
        $ bgtotal += 1
        scene legodoor
        show cs at manual_pos(0,0)
        $ transformtotal += 1
        green_offscreen "test 123{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(124):
        $ musictotal += 1
        play music stal
        $ bgtotal += 1
        scene legodooropen
        anno_offscreen "test 124{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(125):
        $ musictotal += 1
        play music star_spangled_banner
        $ bgtotal += 1
        scene legostage
        ed_ai "test 125{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(126):
        $ musictotal += 1
        play music street_noise
        $ bgtotal += 1
        scene vegas
        obamanobeep "test 126{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(127):
        $ musictotal += 1
        play music summer_clearance_sale
        $ bgtotal += 1
        scene strip
        bomahanobeep "test 127{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(128):
        $ musictotal += 1
        play music super_friendly
        $ bgtotal += 1
        scene slots
        RCOMEM "test 128{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(129):
        $ musictotal += 1
        play music sweet_victory
        $ bgtotal += 1
        scene tablegames
        k_doctor "test 129{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(130):
        $ musictotal += 1
        play music taiikusai_desu_yo
        $ bgtotal += 1
        scene pokertable
        k_nurse "test 130{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(131):
        $ musictotal += 1
        play music take_trip
        $ bgtotal += 1
        scene luigi1
        l_snow "test 131{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(132):
        $ musictotal += 1
        play music take_trip2
        $ bgtotal += 1
        scene luigi2
        lupin "test 132{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(133):
        $ musictotal += 1
        play music the_rest_of_bubble_tea
        $ bgtotal += 1
        scene vegasbathroom
        lupin_offscreen "test 133{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(134):
        $ musictotal += 1
        play music the_whale
        $ bgtotal += 1
        scene backroomcasino
        mean_offscreen "test 134{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(135):
        $ musictotal += 1
        play music thousand_march
        $ bgtotal += 1
        scene outsafe
        amtrak_conductor "test 135{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(136):
        $ musictotal += 1
        play music time_for_a_smackdown
        $ bgtotal += 1
        scene outsafeopen
        amtrak_stewardess "test 136{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(137):
        $ musictotal += 1
        play music track_3
        $ bgtotal += 1
        scene insafe
        amtrak_npc_1 "test 137{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(138):
        $ musictotal += 1
        play music track_4
        $ bgtotal += 1
        scene carpark
        amtrak_npc_2 "test 138{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(139):
        $ musictotal += 1
        play music trans_atlantic
        $ bgtotal += 1
        scene casino1
        amtrak_npc_3 "test 139{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(140):
        $ musictotal += 1
        play music trash_zone
        $ bgtotal += 1
        scene fazhall
        priest "test 140{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(141):
        $ musictotal += 1
        play music triage_at_dawn
        $ bgtotal += 1
        scene fazlobby
        perfect_billy "test 141{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(142):
        $ musictotal += 1
        play music tumultuous
        $ bgtotal += 1
        scene fazplace
        weird_al "test 142{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(143):
        $ musictotal += 1
        play music tuna_fish
        $ bgtotal += 1
        scene airplane_seats
        david "test 143{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(144):
        $ musictotal += 1
        play music tunnely_shimbers
        $ bgtotal += 1
        scene airport_interior
        mr_krupp "test 144{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(145):
        $ musictotal += 1
        play music undyne
        $ bgtotal += 1
        scene airport_seats
        george "test 145{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(146):
        $ musictotal += 1
        play music upon_me
        $ bgtotal += 1
        scene airport_tsa
        harold "test 146{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(147):
        $ musictotal += 1
        play music wayward_wanderer
        $ bgtotal += 1
        scene airport_inside
        zenigata_nobeep "test 147{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(148):
        $ musictotal += 1
        play music weird_personalities
        $ bgtotal += 1
        scene old_house_outside
        zenigata_offscreen "test 148{w=0.5}{nw}"
        $ charactertotal += 1
    else:
        jump exit_debug
    if fun_value(149):
        $ musictotal += 1
        play music winter_lullaby
        $ bgtotal += 1
        scene old_house_inside
        pause 0.5
    else:
        jump exit_debug
    if fun_value(150):
        $ musictotal += 1
        play music wool_gloves
        $ bgtotal += 1
        scene cc_parking_lot
        pause 0.5
    else:
        jump exit_debug
    if fun_value(151):
        $ musictotal += 1
        play music xddcc
        $ bgtotal += 1
        scene cc_lobby
        pause 0.5
    else:
        jump exit_debug
    if fun_value(152):
        $ musictotal += 1
        play music ocean_man
        $ bgtotal += 1
        scene cc_entrance
        pause 0.5
    else:
        jump exit_debug
    if fun_value(153):
        $ musictotal += 1
        play music lancer
        $ bgtotal += 1
        scene cc_crowd
        pause 0.5
    else:
        jump exit_debug
    if fun_value(154):
        $ musictotal += 1
        play music space_classroom
        $ bgtotal += 1
        scene cc_stage
        pause 0.5
    else:
        jump exit_debug
    if fun_value(155):
        $ musictotal += 1
        play music error
        $ bgtotal += 1
        scene cc_backstage
        pause 0.5
    else:
        jump exit_debug
    if fun_value(156):
        $ musictotal += 1
        play music bedroom_day
        $ bgtotal += 1
        scene billboard
        pause 0.5
    else:
        jump exit_debug
    if fun_value(157):
        $ musictotal += 1
        play music tmwstw
        $ bgtotal += 1
        scene texas
        pause 0.5
    else:
        jump exit_debug
    if fun_value(158):
        $ musictotal += 1
        play music e_gadds_lab
        $ bgtotal += 1
        scene tvbilly
        pause 0.5
    else:
        jump exit_debug
    if fun_value(159):
        $ musictotal += 1
        play music insomnia
        $ bgtotal += 1
        scene jeep_inside_fg
        pause 0.5
    else:
        jump exit_debug
    if fun_value(160):
        $ musictotal += 1
        play music insomnia_intro
        $ bgtotal += 1
        scene dinerinside
        pause 0.5
    else:
        jump exit_debug
    if fun_value(161):
        $ musictotal += 1
        play music insomnia_loop
        $ bgtotal += 1
        scene aria_car_fg
        pause 0.5
    else:
        jump exit_debug
    if fun_value(162):
        $ musictotal += 1
        play music item_bounce
        $ bgtotal += 1
        scene aria_room
        pause 0.5
    else:
        jump exit_debug
    if fun_value(163):
        $ musictotal += 1
        play music krabby_klub
        $ bgtotal += 1
        scene aria_apartment_outside
        pause 0.5
    else:
        jump exit_debug
    if fun_value(164):
        $ musictotal += 1
        play music night
        $ bgtotal += 1
        scene cs_somewhere
        pause 0.5
    else:
        jump exit_debug
    if fun_value(165):
        $ musictotal += 1
        play music ochre_woods_day
        $ bgtotal += 1
        scene dineroutside
        pause 0.5
    else:
        jump exit_debug
    if fun_value(166):
        $ musictotal += 1
        play music onbs
        $ bgtotal += 1
        scene battle_block_without_theater
        pause 0.5
    else:
        jump exit_debug
    if fun_value(167):
        $ musictotal += 1
        play music outdoors
        $ bgtotal += 1
        scene final_destination
        pause 0.5
    else:
        jump exit_debug
    if fun_value(168):
        $ musictotal += 1
        play music prof_kranes_kidnap
        $ bgtotal += 1
        scene police_car_fg
        pause 0.5
    else:
        jump exit_debug
    if fun_value(169):
        $ musictotal += 1
        play music space
        $ bgtotal += 1
        scene war_torn_1
        pause 0.5
    else:
        jump exit_debug
    if fun_value(170):
        $ musictotal += 1
        play music sub_game_select
        $ bgtotal += 1
        scene war_torn_2
        pause 0.5
    else:
        jump exit_debug
    if fun_value(171):
        $ musictotal += 1
        play music funvalueland
        $ bgtotal += 1
        scene war_torn_3
        pause 0.5
    else:
        jump exit_debug
    if fun_value(172):
        $ musictotal += 1
        play music supernova
        $ bgtotal += 1
        scene war_torn_4
        pause 0.5
    else:
        jump exit_debug
    if fun_value(173):
        $ musictotal += 1
        play music game_corner
        $ bgtotal += 1
        scene war_torn_5
        pause 0.5
    else:
        jump exit_debug
    if fun_value(174):
        $ musictotal += 1
        play music get_the_funk
        $ bgtotal += 1
        scene car_insidearc_fg
        pause 0.5
    else:
        jump exit_debug
    if fun_value(175):
        $ musictotal += 1
        play music hide_and_seek
        $ bgtotal += 1
        scene car_insidearc_fg flipped
        pause 0.5
    else:
        jump exit_debug
    if fun_value(176):
        $ musictotal += 1
        play music rude_buster
        $ bgtotal += 1
        scene joj_chargerarc_fg
        pause 0.5
    else:
        jump exit_debug
    if fun_value(177):
        $ musictotal += 1
        play music unobtrusive_fun
        $ bgtotal += 1
        scene gas_station_2
        pause 0.5
    else:
        jump exit_debug
    if fun_value(178):
        $ musictotal += 1
        play music encounter_friend_intro
        $ bgtotal += 1
        scene traffic
        pause 0.5
    else:
        jump exit_debug
    if fun_value(179):
        $ musictotal += 1
        play music encounter_friend_loop
        $ bgtotal += 1
        scene white
        pause 0.5
    else:
        jump exit_debug
    if fun_value(180):
        $ musictotal += 1
        play music yuuka_town
        $ bgtotal += 1
        scene parking_lot
        pause 0.1
    else:
        jump exit_debug
    if fun_value(181):
        $ bgtotal += 1
        scene path_entrance
        pause 0.1
    else:
        jump exit_debug
    if fun_value(182):
        $ bgtotal += 1
        scene path_forest
        pause 0.1
    else:
        jump exit_debug
    if fun_value(183):
        $ bgtotal += 1
        scene creepy_path
        pause 0.1
    else:
        jump exit_debug
    if fun_value(184):
        $ bgtotal += 1
        scene creepy_path_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(185):
        $ bgtotal += 1
        scene creepy_path_3
        pause 0.1
    else:
        jump exit_debug
    if fun_value(186):
        $ bgtotal += 1
        scene creepy_path_4
        pause 0.1
    else:
        jump exit_debug
    if fun_value(187):
        $ bgtotal += 1
        scene creepy_path_fairy
        pause 0.1
    else:
        jump exit_debug
    if fun_value(188):
        $ bgtotal += 1
        scene creepy_path_exit
        pause 0.1
    else:
        jump exit_debug
    if fun_value(189):
        $ bgtotal += 1
        scene cafe_entrance
        pause 0.1
    else:
        jump exit_debug
    if fun_value(190):
        $ bgtotal += 1
        scene cafe_sitting
        pause 0.1
    else:
        jump exit_debug
    if fun_value(191):
        $ bgtotal += 1
        scene cafe_sitting_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(192):
        $ bgtotal += 1
        scene trafficjam
        pause 0.1
    else:
        jump exit_debug
    if fun_value(193):
        $ bgtotal += 1
        scene east_cafe
        pause 0.1
    else:
        jump exit_debug
    if fun_value(194):
        $ bgtotal += 1
        scene doll_eye_tree
        pause 0.1
    else:
        jump exit_debug
    if fun_value(195):
        $ bgtotal += 1
        scene mario_inside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(196):
        $ bgtotal += 1
        scene mario_inside2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(197):
        $ bgtotal += 1
        scene mario_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(198):
        $ bgtotal += 1
        scene gnome_forest
        pause 0.1
    else:
        jump exit_debug
    if fun_value(199):
        $ bgtotal += 1
        scene forest_clearing
        pause 0.1
    else:
        jump exit_debug
    if fun_value(200):
        $ bgtotal += 1
        scene bronsoncrash
        pause 0.1
    else:
        jump exit_debug
    if fun_value(201):
        $ bgtotal += 1
        scene britport
        pause 0.1
    else:
        jump exit_debug
    if fun_value(202):
        $ bgtotal += 1
        scene embassy
        pause 0.1
    else:
        jump exit_debug
    if fun_value(203):
        $ bgtotal += 1
        scene uk_street
        pause 0.1
    else:
        jump exit_debug
    if fun_value(204):
        $ bgtotal += 1
        scene kitty_house
        pause 0.1
    else:
        jump exit_debug
    if fun_value(205):
        $ bgtotal += 1
        scene kitty_room
        pause 0.1
    else:
        jump exit_debug
    if fun_value(206):
        $ bgtotal += 1
        scene dining_room
        pause 0.1
    else:
        jump exit_debug
    if fun_value(207):
        $ bgtotal += 1
        scene hell_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(208):
        $ bgtotal += 1
        scene dominos
        pause 0.1
    else:
        jump exit_debug
    if fun_value(209):
        $ bgtotal += 1
        scene dominos_counter
        pause 0.1
    else:
        jump exit_debug
    if fun_value(210):
        $ bgtotal += 1
        scene ceo_office
        pause 0.1
    else:
        jump exit_debug
    if fun_value(211):
        $ bgtotal += 1
        scene japanese_street
        pause 0.1
    else:
        jump exit_debug
    if fun_value(212):
        $ bgtotal += 1
        scene front_desk
        pause 0.1
    else:
        jump exit_debug
    if fun_value(213):
        $ bgtotal += 1
        scene hell_kitchen
        pause 0.1
    else:
        jump exit_debug
    if fun_value(214):
        $ bgtotal += 1
        scene top_gear_track
        pause 0.1
    else:
        jump exit_debug
    if fun_value(215):
        $ bgtotal += 1
        scene tom_house
        pause 0.1
    else:
        jump exit_debug
    if fun_value(216):
        $ bgtotal += 1
        scene tom_road
        pause 0.1
    else:
        jump exit_debug
    if fun_value(217):
        $ bgtotal += 1
        scene tokyo_street
        pause 0.1
    else:
        jump exit_debug
    if fun_value(218):
        $ bgtotal += 1
        scene tokyo_airport
        pause 0.1
    else:
        jump exit_debug
    if fun_value(219):
        $ bgtotal += 1
        scene game_store_back
        pause 0.1
    else:
        jump exit_debug
    if fun_value(220):
        $ bgtotal += 1
        scene game_store_front
        pause 0.1
    else:
        jump exit_debug
    if fun_value(221):
        $ bgtotal += 1
        scene tokyo_street_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(222):
        $ bgtotal += 1
        scene tokyo_street_night
        pause 0.1
    else:
        jump exit_debug
    if fun_value(223):
        $ bgtotal += 1
        scene karaoke_bar_inside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(224):
        $ bgtotal += 1
        scene karaoke_bar_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(225):
        $ bgtotal += 1
        scene ceo_office_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(226):
        $ bgtotal += 1
        scene front_desk_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(227):
        $ bgtotal += 1
        scene talking_head
        pause 0.1
    else:
        jump exit_debug
    if fun_value(228):
        $ bgtotal += 1
        scene stockholm
        pause 0.1
    else:
        jump exit_debug
    if fun_value(229):
        $ bgtotal += 1
        scene bus_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(230):
        $ bgtotal += 1
        scene bus_map
        pause 0.1
    else:
        jump exit_debug
    if fun_value(231):
        $ bgtotal += 1
        scene bus_seat
        pause 0.1
    else:
        jump exit_debug
    if fun_value(232):
        $ bgtotal += 1
        scene ikea_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(233):
        $ bgtotal += 1
        scene ikea_inside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(234):
        $ bgtotal += 1
        scene joel_house
        pause 0.1
    else:
        jump exit_debug
    if fun_value(235):
        $ bgtotal += 1
        scene joel_computer
        pause 0.1
    else:
        jump exit_debug
    if fun_value(236):
        $ bgtotal += 1
        scene joel_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value(237):
        $ bgtotal += 1
        scene joel_dining
        pause 0.1
    else:
        jump exit_debug
    if fun_value(238):
        $ bgtotal += 1
        scene food_court
        pause 0.1
    else:
        jump exit_debug
    if fun_value(239):
        $ bgtotal += 1
        scene eating_food
        pause 0.1
    else:
        jump exit_debug
    if fun_value(240):
        $ bgtotal += 1
        scene home_decor
        pause 0.1
    else:
        jump exit_debug
    if fun_value(241):
        $ bgtotal += 1
        scene toilet_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(242):
        $ bgtotal += 1
        scene plushie_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(243):
        $ bgtotal += 1
        scene eating_food_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(244):
        $ bgtotal += 1
        scene dumpster
        pause 0.1
    else:
        jump exit_debug
    if fun_value(245):
        $ bgtotal += 1
        scene moomin_zone1
        pause 0.1
    else:
        jump exit_debug
    if fun_value(246):
        $ bgtotal += 1
        scene moomin_zone2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(247):
        $ bgtotal += 1
        scene moomin_zone3
        pause 0.1
    else:
        jump exit_debug
    if fun_value(248):
        $ bgtotal += 1
        scene moomin_zone3b
        pause 0.1
    else:
        jump exit_debug
    if fun_value(249):
        $ bgtotal += 1
        scene moomin_zone4
        pause 0.1
    else:
        jump exit_debug
    if fun_value(250):
        $ bgtotal += 1
        scene moomin_zone5
        pause 0.1
    else:
        jump exit_debug
    if fun_value(251):
        $ bgtotal += 1
        scene waddle_zone
        pause 0.1
    else:
        jump exit_debug
    if fun_value(252):
        $ bgtotal += 1
        scene park1
        pause 0.1
    else:
        jump exit_debug
    if fun_value(253):
        $ bgtotal += 1
        scene park2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(254):
        $ bgtotal += 1
        scene carousel
        pause 0.1
    else:
        jump exit_debug
    if fun_value(255):
        $ bgtotal += 1
        scene endingai 
        pause 0.1
    else:
        jump exit_debug
    if fun_value(256):
        $ bgtotal += 1
        scene entertunnel
        pause 0.1
    else:
        jump exit_debug
    if fun_value(257):
        $ bgtotal += 1
        scene linusmedia
        pause 0.1
    else:
        jump exit_debug
    if fun_value(258):
        $ bgtotal += 1
        scene secrettunnel
        pause 0.1
    else:
        jump exit_debug
    if fun_value(259):
        $ bgtotal += 1
        scene hairdryercoolingsystem
        pause 0.1
    else:
        jump exit_debug
    if fun_value(260):
        $ bgtotal += 1
        scene tempsdown
        pause 0.1
    else:
        jump exit_debug
    if fun_value(261):
        $ bgtotal += 1
        scene car_old
        pause 0.1
    else:
        jump exit_debug
    if fun_value(262):
        $ bgtotal += 1
        scene car_inside_old
        pause 0.1
    else:
        jump exit_debug
    if fun_value(263):
        $ bgtotal += 1
        scene bedroom_old
        pause 0.1
    else:
        jump exit_debug
    if fun_value(264):
        $ bgtotal += 1
        scene door_old
        pause 0.1
    else:
        jump exit_debug
    if fun_value(265):
        $ bgtotal += 1
        scene csmart_old
        pause 0.1
    else:
        jump exit_debug
    if fun_value(266):
        $ bgtotal += 1
        scene craptop_old
        pause 0.1
    else:
        jump exit_debug
    if fun_value(267):
        $ bgtotal += 1
        scene falling
        pause 0.1
    else:
        jump exit_debug
    if fun_value(268):
        $ bgtotal += 1
        scene archival_1
        pause 0.1
    else:
        jump exit_debug
    if fun_value(269):
        $ bgtotal += 1
        scene archival_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(270):
        $ bgtotal += 1
        scene archival_3
        pause 0.1
    else:
        jump exit_debug
    if fun_value(271):
        $ bgtotal += 1
        scene archival_4
        pause 0.1
    else:
        jump exit_debug
    if fun_value(272):
        $ bgtotal += 1
        scene archival_5
        pause 0.1
    else:
        jump exit_debug
    if fun_value(273):
        $ bgtotal += 1
        scene archival_6
        pause 0.1
    else:
        jump exit_debug
    if fun_value(274):
        $ bgtotal += 1
        scene archival_7
        pause 0.1
    else:
        jump exit_debug
    if fun_value(275):
        $ bgtotal += 1
        scene archival_8
        pause 0.1
    else:
        jump exit_debug
    if fun_value(276):
        $ bgtotal += 1
        scene archival_9
        pause 0.1
    else:
        jump exit_debug
    if fun_value(277):
        $ bgtotal += 1
        scene archival_10
        pause 0.1
    else:
        jump exit_debug
    if fun_value(278):
        $ bgtotal += 1
        scene archival_11
        pause 0.1
    else:
        jump exit_debug
    if fun_value(279):
        $ bgtotal += 1
        scene archival_9a
        pause 0.1
    else:
        jump exit_debug
    if fun_value(280):
        $ bgtotal += 1
        scene archival_10a
        pause 0.1
    else:
        jump exit_debug
    if fun_value(281):
        $ bgtotal += 1
        scene archival_11a
        pause 0.1
    else:
        jump exit_debug
    if fun_value(282):
        $ bgtotal += 1
        scene archival_12
        pause 0.1
    else:
        jump exit_debug
    if fun_value(283):
        $ bgtotal += 1
        scene archival_13
        pause 0.1
    else:
        jump exit_debug
    if fun_value(284):
        $ bgtotal += 1
        scene archival_14
        pause 0.1
    else:
        jump exit_debug
    if fun_value(285):
        $ bgtotal += 1
        scene archival_15
        pause 0.1
    else:
        jump exit_debug
    if fun_value(286):
        $ bgtotal += 1
        scene archival_16
        pause 0.1
    else:
        jump exit_debug
    if fun_value(287):
        $ bgtotal += 1
        scene archival_17
        pause 0.1
    else:
        jump exit_debug
    if fun_value(288):
        $ bgtotal += 1
        scene archival_18
        pause 0.1
    else:
        jump exit_debug
    if fun_value(289):
        $ bgtotal += 1
        scene archival_19
        pause 0.1
    else:
        jump exit_debug
    if fun_value(290):
        $ bgtotal += 1
        scene start_route
        pause 0.1
    else:
        jump exit_debug
    if fun_value(291):
        $ bgtotal += 1
        scene cs_room_cars
        pause 0.1
    else:
        jump exit_debug
    if fun_value(292):
        $ bgtotal += 1
        scene wis_forest
        pause 0.1
    else:
        jump exit_debug
    if fun_value(293):
        $ bgtotal += 1
        scene roombacks
        pause 0.1
    else:
        jump exit_debug
    if fun_value(294):
        $ bgtotal += 1
        scene backrooms
        pause 0.1
    else:
        jump exit_debug
    if fun_value(295):
        $ bgtotal += 1
        scene hobbytown
        pause 0.1
    else:
        jump exit_debug
    if fun_value(296):
        $ bgtotal += 1
        scene pencilroom
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(297):
        $ bgtotal += 1
        scene pencilroomblur
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(298):
        $ bgtotal += 1
        scene cult_con
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(299):
        $ bgtotal += 1
        scene blue_branch
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(300):
        $ bgtotal += 1
        scene renault_inside
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(301):
        $ bgtotal += 1
        scene kuwait_city
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(302):
        $ bgtotal += 1
        scene kuwait_explosion
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(303):
        $ bgtotal += 1
        scene kuwait_hospital_inside
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(304):
        $ bgtotal += 1
        scene kuwait_hospital_corridor
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(305):
        $ bgtotal += 1
        scene kuwait_islandbase_leaders
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(306):
        $ bgtotal += 1
        scene green_screen
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(307):
        $ bgtotal += 1
        scene kingman_exterior
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(308):
        $ bgtotal += 1
        scene kingman_interior
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(309):
        $ bgtotal += 1
        scene kingman_museum_1
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(310):
        $ bgtotal += 1
        scene kingman_platform_1
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(311):
        $ bgtotal += 1
        scene kingman_platform_2
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(312):
        $ bgtotal += 1
        scene kingman_train_arrive
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(313):
        $ bgtotal += 1
        scene amtrak_arrive_close
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(314):
        $ bgtotal += 1
        scene amtrak_sleeper_corridor
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(315):
        $ bgtotal += 1
        scene amtrak_sleeper_interior_day
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(316):
        $ bgtotal += 1
        scene amtrak_sleeper_interior_night
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(317):
        $ bgtotal += 1
        scene amtrak_dining_car
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(318):
        $ bgtotal += 1
        scene amtrak_dining_table
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(319):
        $ bgtotal += 1
        scene moynihan_interior
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(320):
        $ bgtotal += 1
        scene amtrak_cab
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(321):
        $ bgtotal += 1
        scene amtrak_sleeper_open_bg
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(322):
        $ bgtotal += 1
        scene amtrak_sleeper_open_fg
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(323):
        $ bgtotal += 1
        scene amtrak_economy
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(324):
        $ bgtotal += 1
        scene utajsign
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(325):
        $ bgtotal += 1
        scene vegasjade
        pause 0.1 
    else:
        jump exit_debug
    if fun_value(326):
        $ bgtotal += 1
        scene vegasjade2
        pause 0.1
    else:
        jump exit_debug
    if fun_value(327):
        $ movietotal += 1
        scene car background
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(328):
        $ movietotal += 1
        scene car background night
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(329):
        $ movietotal += 1
        scene car plains
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(330):
        $ movietotal += 1
        scene car plains night
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(331):
        $ movietotal += 1
        scene tvcar
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(332):
        $ movietotal += 1
        scene drive_night
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(333):
        $ movietotal += 1
        scene drive_day
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(334):
        $ movietotal += 1
        scene csb1tube
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(335):
        $ movietotal += 1
        scene train_start
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(336):
        $ movietotal += 1
        scene train_in_tunnel
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(337):
        $ movietotal += 1
        scene train_outside_tunnel
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(338):
        $ movietotal += 1
        scene train_loop
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(339):
        $ movietotal += 1
        scene the_tram
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(340):
        $ movietotal += 1
        scene sign_closeup
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(341):
        $ movietotal += 1
        $ renpy.movie_cutscene(woc)
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(342):
        $ movietotal += 1
        $ renpy.movie_cutscene(where)
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(343):
        $ movietotal += 1
        scene karaoke
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(344):
        $ movietotal += 1
        scene bad_end_screen
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(345):
        $ movietotal += 1
        scene bronson_hell
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(346):
        $ movietotal += 1
        scene fun_cs_house
        pause 5.0 
    else:
        jump exit_debug
    if fun_value(347):
        $ movietotal += 1
        scene fun_hoh_sis
        pause 5.0 
    else:
        jump exit_debug
    if fun_value (348):
        $ bgtotal += 1
        scene kingman_museum_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value (349):
        $ movietotal += 1
        $ renpy.movie_cutscene(anno_bl)
    else:
        jump exit_debug
    if fun_value (350):
        $ movietotal += 1
        $ renpy.movie_cutscene(blank_bl)
    else:
        jump exit_debug
    if fun_value (351):
        $ movietotal += 1
        $ renpy.movie_cutscene(db_bl)
    else:
        jump exit_debug
    if fun_value (352):
        $ movietotal += 1
        $ renpy.movie_cutscene(midge_bl)
    else:
        jump exit_debug
    if fun_value (353):
        scene black
    else:
        jump exit_debug
    if fun_value (354):
        $ movietotal += 1
        $ renpy.movie_cutscene(creditsm)
    else:
        jump exit_debug
    if fun_value (355):
        $ movietotal += 1
        $ renpy.movie_cutscene(archival_end)
    else:
        jump exit_debug
    if fun_value (356):
        $ movietotal += 1
        $ renpy.movie_cutscene(error_cutscene)
    else:
        jump exit_debug
    if fun_value (357):
        $ movietotal += 1
        $ renpy.movie_cutscene(good_ytp)
    else:
        jump exit_debug
    if fun_value (358):
        $ movietotal += 1
        $ renpy.movie_cutscene(bad_ytp)
    else:
        jump exit_debug
    if fun_value (359):
        $ movietotal += 1
        $ renpy.movie_cutscene(hoh_repair)
    else:
        jump exit_debug
    if fun_value (360):
        $ movietotal += 1
        $ renpy.movie_cutscene(kick)
    else:
        jump exit_debug
    if fun_value (361):
        $ movietotal += 1
        $ renpy.movie_cutscene(splash)
    else:
        jump exit_debug
    if fun_value (362):
        $ bgtotal += 1
        scene cult_zone1
        pause 0.1
    else:
        jump exit_debug
    if fun_value (363):
        $ bgtotal += 1
        scene kingman_museum_3
        pause 0.1
    else:
        jump exit_debug
    if fun_value (364):
        $ bgtotal += 1
        scene kuwait_hallway
        pause 0.1
    else:
        jump exit_debug
    if fun_value (365):
        $ bgtotal += 1
        scene kuwait_island_outside
        pause 0.1
    else:
        jump exit_debug
    if fun_value (366):
        $ bgtotal += 1
        scene amtrak_baggage
        pause 0.1
    else:
        jump exit_debug
    if fun_value (367):
        $ bgtotal += 1
        scene amtrak_coach_1
        pause 0.1
    else:
        jump exit_debug
    if fun_value (368):
        $ bgtotal += 1
        scene amtrak_coach_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value (369):
        $ bgtotal += 1
        scene amtrak_observation_1
        pause 0.1
    else:
        jump exit_debug
    if fun_value (370):
        $ bgtotal += 1
        scene amtrak_observation_2
        pause 0.1
    else:
        jump exit_debug
    if fun_value (371):
        $ bgtotal += 1
        scene amtrak_top
        pause 0.1
    else:
        jump exit_debug
    if fun_value (372):
        $ bgtotal += 1
        scene classroom
        pause 0.1
    else:
        jump exit_debug
    if fun_value (373):
        $ bgtotal += 1
        scene broom_closet
        pause 0.1
    else:
        jump exit_debug
    if fun_value (374):
        $ bgtotal += 1
        scene vegaspent
        pause 0.1
    else:
        jump exit_debug
    if fun_value (375):
        $ bgtotal += 1
        scene vegasjadepent
        pause 0.1
    else:
        jump exit_debug
    if fun_value (376):
        $ bgtotal += 1
        scene letterbox1
        pause 0.1
    else:
        jump exit_debug 
    if fun_value (377):
        $ bgtotal += 1
        scene letterbox2
        pause 0.1
    else:
        jump exit_debug
    if fun_value (378):
        $ bgtotal += 1
        scene letterbox3
        pause 0.1
    else:
        jump exit_debug    

    n "Done."
    show screen debugger_menu
    pause
    return

label exit_debug:
    show cs angry
    pause 0.5
    cs "You didn't turn it on!"
    return
