label lose_car_game:
    bad_end "100 percent\nunsatisfied." "iowa"
    return

label lose_pencil_game:
    bad_end "Try, uh, mashing... faster?" "minigame_pencil"
    return

label lose_pencil_game2:
    bad_end "You dumb skinfore." "minigame_pencil2"
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

label pussy_out_archival:
    $ persistent.seen.add("k174")
    $ persistent.seen.add("addy")
    $ persistent.heard.add("Facing Worlds - Michiel van den Bos")
    $ persistent.heard.add("BATTLE UNDER A BROKEN SKY - AZALI")
    $ persistent.heard.add("Take a Trip from Me - u4ia")
    $ persistent.heard.add("Everybody Wants To Rule The World - Tears For Fears")
    $ achievement_manager.unlock("Archived")
    return

label pussy_out_i69:
    $ persistent.seen.add("gnome")
    $ persistent.heard.add("Wayward Wanderer - Deep Gnome")
    $ persistent.heard.add("MisLeader - Triosk and Jan Jelinek")
    $ persistent.heard.add("Dense Woods B - Kikiyama")
    $ persistent.heard.add("Melancholy - Imori")
    $ achievement_manager.unlock("You've Been Gnomed")
    $ achievement_manager.unlock("Analog Horror Protagonist")
    jump interstate_94

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
    n "Done."
    return

label exit_debug:
    show cs angry
    pause 1.0
    cs "You didn't turn it on!"
    return
