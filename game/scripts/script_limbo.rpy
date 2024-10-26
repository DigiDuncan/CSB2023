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

                ### RESERVED ###
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
    $ persistent.heard.add("Facing Worlds - Michiel van den Bos")
    $ persistent.heard.add("BATTLE UNDER A BROKEN SKY - AZALI")
    $ persistent.heard.add("Take a Trip from Me - u4ia")
    $ persistent.heard.add("Everybody Wants To Rule The World - Tears For Fears")
    $ achievement_manager.unlock("Archived")
    return

label back_out_i69:
    $ persistent.seen.add("gnome")
    $ persistent.heard.add("Wayward Wanderer - Deep Gnome")
    $ persistent.heard.add("MisLeader - Triosk and Jan Jelinek")
    $ persistent.heard.add("Dense Woods B - Kikiyama")
    $ persistent.heard.add("Melancholy - Imori")
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


screen limbo_csbutton:
    add "#000000"
    text "This will update your game from the previous release." textalign 0.5 size 108 xalign 0.5 yalign 0.25
    hbox xalign 0.0 yalign 0.25:
        spacing 50
    text "THIS WILL DELETE YOUR CURRENT SAVE." textalign 0.5 size 72 xalign 0.45 yalign 0.45
    hbox xalign 0.0 yalign 0.45:
        spacing 50
    textbutton "Go back!":
        xalign 0.6
        yalign 0.75
        text_textalign 0.5
        text_size 72
        action Hide("limbo_csbutton")
    textbutton "Proceed":
        xalign 0.4
        yalign 0.75
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
    $ persistent.heard.add("Thousand March - Mr. Sauceman")
    $ persistent.heard.add("Alfred Hitchcock Intro Theme - Charles Gounod")
    $ persistent.heard.add("Billy Mays Gangsta Remix - mastamokei")
    $ persistent.heard.add("PASSPORT.MID - George Stone")
    $ persistent.heard.add("Let's hear my baby - Walkman")
    $ persistent.heard.add("Time for a Smackdown! - Mr. Sauceman")
    $ persistent.heard.add("Dig This - Dr. Awesome")
    $ persistent.heard.add("Mm Select - Matthew Simmonds")
    $ persistent.heard.add("Let's Do This - Home Depot")
    $ persistent.heard.add("Hightop - Dr. Awesome")
    $ persistent.heard.add("stal - C418")
    $ persistent.heard.add("Undyne - Toby Fox")
    $ persistent.heard.add("Everybody Wants To Rule The World - Tears For Fears")
    $ persistent.heard.add("Mm Complete - Matthew Simmonds")
    $ persistent.heard.add("The Star Spangled Banner - THE UNITED STATES OF AMERICA")
    $ persistent.heard.add("Lego Island Theme - Lorin Nelson")
    $ persistent.heard.add("Super Friendly - Kevin Macleod")
    $ persistent.heard.add("Dense Woods B - Kikiyama")
    $ persistent.heard.add("Airport Counter - Kazumi Totaka")
    $ persistent.heard.add("Dragon Castle - BreakingCopyright")
    $ persistent.heard.add("Onett Theme - Keiichi Suzuki")
    $ persistent.heard.add("Summer Clearance Sale - BEST MUSIC")
    $ persistent.heard.add("Energetic Rock - Every Day Music")
    $ persistent.heard.add("CP Violation - Kelly Bailey")
    $ persistent.heard.add("Laurel Palace - Manami Matsumae")
    $ persistent.heard.add("Nordic Report 1 - Lizardking")
    $ persistent.heard.add("Compulsion To Obey - Lizardking")
    $ persistent.heard.add("Prophet 2001 - Dr. Awesome")
    $ persistent.heard.add("Price Is Right Theme - Edd Kalehoff")
    $ persistent.heard.add("Good Eatin' - ClascyJitto")
    $ persistent.heard.add("Exotic - Panda Beats")
    $ persistent.heard.add("Facing Worlds - Michiel van den Bos")
    $ persistent.heard.add("MisLeader - Triosk and Jan Jelinek")
    $ persistent.heard.add("Happy Rock - Benjamin TISSOT")
    $ persistent.heard.add("CANYON.MID - George Stone")
    $ persistent.heard.add("scales of joy.mod - Mel O Dee")
    $ persistent.heard.add("Tunnely Shimbers - Mr. Sauceman")
    $ persistent.heard.add("Racing Minigame Song - FNAF 6")
    $ persistent.heard.add("Morning Highway - BEST MUSIC")
    $ persistent.heard.add("Bun Guster - Satoru Kosaki")
    $ persistent.heard.add("Buy Something Will Ya! - Keiichi Suzuki")
    $ persistent.heard.add("Pokeys House - Keiichi Suzuki")
    $ persistent.heard.add("Park Theme - Lorin Nelson")
    $ persistent.heard.add("Melancholy - Imori")
    $ persistent.heard.add("The Metropolis of Fourside - Keiichi Suzuki")
    $ persistent.heard.add("Mort's Farm - ClascyJitto")
    $ persistent.heard.add("Airport Infilration - Marten Joustra")
    $ persistent.heard.add("Take a Trip from Me - u4ia")
    $ persistent.heard.add("Pierrot of the Star Spangled Banner - ZUN")
    $ persistent.heard.add("Police Station - Lorin Nelson")
    $ persistent.heard.add("Klaxon Beat - Kelly Bailey")
    $ persistent.heard.add("Moongazer - Dr. Awesome")
    $ persistent.heard.add("Danger Mystery - Toby Fox")
    $ persistent.heard.add("For The People! - Lizardking")
    $ persistent.heard.add("Now What? 1 - Dr. Awesome")
    $ persistent.heard.add("Youre At A Ball In The Gold Room - Nemos Dreamscapes")
    $ persistent.heard.add("Hit Me With Your Best Shot - Pat Benatar")
    $ persistent.heard.add("Taiikusai Desu Yo - Satoru Kosaki")
    $ persistent.heard.add("Weird Personalities - Lizardking")
    $ persistent.heard.add("Guillotine World - Kikiyama")
    $ persistent.heard.add("Sweet Victory - David Eisley")
    $ persistent.heard.add("Al's Penthouse - Andy Blythe")
    $ persistent.heard.add("Funiculi Holiday - ClascyJitto")
    $ persistent.heard.add("New Leaf Title Theme - Kazumi Totaka")
    $ persistent.heard.add("The Whale - Dr. Awesome")
    $ persistent.heard.add("BUBBLE TEA - darkcat")
    $ persistent.heard.add("Lowbudget Song - Dr. Awesome")
    $ persistent.heard.add("Candle World - Kikiyama")
    $ persistent.heard.add("It's Showtime - Toby Fox")
    $ persistent.heard.add("Tuna Fish - Dr. Awesome")
    $ persistent.heard.add("Breakout - Shoichiro Sakamoto")
    $ persistent.heard.add("Hired Guns - Brian Johnston")
    $ persistent.heard.add("Creative Exercise - Hirokazu Tanaka")
    $ persistent.heard.add("Supernova - Laszlo")
    $ persistent.heard.add("Alfred's Theme - Eminem")
    $ persistent.heard.add("Rude Buster - Toby Fox")
    $ persistent.heard.add("L.A. By Night - Dr. Awesome")
    $ persistent.heard.add("Everlong - Foo Fighters")
    $ persistent.heard.add("Insane Personalities - Lizardking")
    $ persistent.heard.add("Echoing? - Banana")
    $ persistent.heard.add("Full Rulle Med Klas - Lizardking")
    $ persistent.heard.add("Trans Atlantic - Lizardking")
    $ persistent.heard.add("Hard Drive to Munch You - Mr. Sauceman")
    $ persistent.heard.add("Triage At Dawn - Kelly Bailey")
    $ persistent.heard.add("BATTLE UNDER A BROKEN SKY - AZALI")
    $ persistent.heard.add("Wayward Wanderer - Deep Gnome")
    $ persistent.heard.add("Desert Dawn - Lizardking")
    $ persistent.heard.add("Track 4 - Weatherscan")
    $ persistent.heard.add("Track 3 - Weatherscan")
    $ persistent.heard.add("Pressing Pursuit ~ Cornered - Masakazu Sugimori")
    $ persistent.heard.add("Echoing - Banana")
    $ persistent.heard.add("Pixel Peeker Polka - Kevin MacLeod")
    $ persistent.heard.add("Local Forecast - Kevin MacLeod")
    $ persistent.heard.add("Happy Roaming - Lorin Nelson")
    $ persistent.heard.add("Dealin Dope - Dr. Awesome")
    $ persistent.heard.add("ANOTHER HIM - Toby Fox")
    $ persistent.heard.add("Speedy Comet - Mahito Yokota")
    $ persistent.heard.add("Billy's Mix - Billy Mays")
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
    
