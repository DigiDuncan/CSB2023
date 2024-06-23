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

    n "Done."
    return

label exit_debug:
    show cs angry
    pause 1.0
    cs "You didn't turn it on!"
    return
