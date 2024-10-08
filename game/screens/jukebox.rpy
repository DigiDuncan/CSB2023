
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------


init python:
    global music_map
    #Name of Entry followed by file name
    music_map = {
        #Title
        "BUBBLE TEA - dark cat": "bubble_tea.ogg",
        #CSB1
        "Let's hear my baby - Walkman": "lets_hear_my_baby.ogg",
        "CANYON.MID - George Stone": "canyon.ogg",
        "Summer Clearance Sale - BEST MUSIC": "bestmusicu.ogg",
        "scales of joy.mod - Mel O Dee": "scales_of_joy.ogg",
        "Alfred Hitchcock Intro Theme - Charles Gounod": "hohsis_theme.ogg",
        "Super Friendly - Kevin Macleod": "super_friendly.ogg",
        "Time for a Smackdown! - Mr. Sauceman": "time_for_a_smackdown.ogg",
        "Beautiful Hills - Network Music": "beautiful_hills.ogg",
        #CSB2
        "Card Castle - Toby Fox": "card_castle.ogg",
        "Basement - Toby Fox": "basement.ogg",
        "stal - C418": "stal.ogg",
        "Moongazer - Dr. Awesome": "moongazer.ogg",
        "Onett Theme - Keiichi Suzuki": "onett.ogg",
        "The Star Spangled Banner - THE UNITED STATES OF AMERICA": "star_spangled_banner.ogg",
        "Buy Something Will Ya! - Keiichi Suzuki": "buy_something.ogg",
        "PASSPORT.MID - George Stone": "passport.ogg",
        #True route
        "Good Eatin' - ClascyJitto": "good_eatin.ogg",
        "Supernova - Laszlo": "supernova.ogg",
        "Airport Counter - Kazumi Totaka": "airport_counter.ogg",
        "Hired Guns - Brian Johnston": "hired_guns.ogg",
        "Undyne - Toby Fox": "undyne.ogg",
        "Atarashii Kaze - Satoru Kosaki": "atarashii_kaze.ogg",
        "Police Station - Lorin Nelson": "police_station.ogg",
        "Echoing - Banana": "echoing.ogg",
        "Danger Mystery - Toby Fox": "danger_mystery.ogg",
        "Pressing Pursuit ~ Cornered - Masakazu Sugimori": "pressing_pursuit_cornered.ogg",
        "Bun Guster - Satoru Kosaki": "bun_guster.ogg",
        "Happy Roaming - Lorin Nelson": "happy_roaming.ogg",
        "Mm Select - Matthew Simmonds": "mm_select.ogg",
        "Billy Mays Gangsta Remix - mastamokei": "billy_radio.ogg",
        "Weird Personalities - Lizardking": "weird_personalities.ogg",
        "Let's Do This - Home Depot": "home_depot.ogg",
        "Candle World - Kikiyama": "candle_world.ogg",
        "It's Showtime - Toby Fox": "showtime.ogg",
        "Mort's Farm - ClascyJitto": "mort_farm.ogg",
        "Taiikusai Desu Yo - Satoru Kosaki": "taiikusai_desu_yo.ogg",
        "Track 4 - Weatherscan": "track4.ogg",
        "Funiculi Holiday - ClascyJitto": "funiculi_holiday.ogg",
        "Speedy Comet - Mahito Yokota": "speedy_comet.ogg",
        "Wayward Wanderer - Deep Gnome": "wayward_wanderer.ogg",
        "MisLeader - Triosk and Jan Jelinek": "mis_leader.ogg",
        "Melancholy - Imori": "melancholy.ogg",
        "Tubular Trash Zone - Mr. Sauceman": "trash_zone.ogg",
        "Breakout - Shoichiro Sakamoto": "breakout.ogg",
        "The Metropolis of Fourside - Keiichi Suzuki": "fourside.ogg",
        "Pokeys House - Keiichi Suzuki": "pokey.ogg",
        "Rude Buster - Toby Fox": "rude_buster.ogg",
        "Billy's Mix - Billy Mays": "billymusicu.ogg",
        "Park Theme - Lorin Nelson": "park_theme.ogg",
        "Alfred's Theme - Eminem": "hohsisremix.ogg",
        "Track 3 - Weatherscan": "track3.ogg",
        "New Leaf Title Theme - Kazumi Totaka": "ac_title.ogg",
        #South route
        "Brick by Brick (Suck my Dick) - cs188": "brick_by_dick.ogg",
        "Tunnely Shimbers - Mr. Sauceman": "tunnely_shimbers.ogg",
        "Hard Drive to Munch You - Mr. Sauceman": "hard_drive.ogg",
        "Al's Penthouse - Andy Blythe": "penthouse.ogg",
        "Rocket Game Corner - Junichi Masuda": "rocket_game_corner.ogg",
        "Laurel Palace - Manami Matsumae": "laurel_palace.ogg",
        "Lancer - Toby Fox": "lancer.ogg",
        "Price Is Right Theme - Edd Kalehoff": "price_right.ogg",
        "Pierrot of the Star Spangled Banner - ZUN": "clownpiece.ogg",
        "Airport Infiltration - Andy Blythe & Marten Joustra": "airport.ogg",
        "Lego Island Theme - Lorin Nelson": "lego_island.ogg",
        #Friend route
        "Morning Highway - BEST MUSIC": "morning_highway.ogg",
        "Creative Exercise - Hirokazu Tanaka": "creative_exercise.ogg",
        "Pixel Peeker Polka - Kevin MacLeod": "pixel_peeker_polka.ogg",
        "Nordic Report 1 - Lizardking": "nordic_report_1.ogg",
        "Nordic Report 2 - Lizardking": "nordic_report_2.ogg",
        "Lowbudget Song - Dr. Awesome": "lowbudget_song.ogg",
        "Klaxon Beat - Kelly Bailey": "klaxon_beat.ogg",
        "CP Violation - Kelly Bailey": "cp_violation.ogg",
        "Mm Complete - Matthew Simmonds": "mm_complete.ogg",
        "Compulsion To Obey - Lizardking": "compulsion_to_obey.ogg",
        "For The People! - Lizardking": "for_the_people.ogg",
        "Tuna Fish - Dr. Awesome": "tuna_fish.ogg",
        "Full Rulle Med Klas - Lizardking": "full_rulle_med_klas.ogg",
        "Dense Woods B - Kikiyama": "dense_woods_b.ogg",
        "Desert Dawn - Lizardking": "desert_dawn.ogg",
        "L.A. By Night - Dr. Awesome": "la_by_night.ogg",
        "Thousand March - Mr. Sauceman": "thousand_march.ogg",
        "Triage At Dawn - Kelly Bailey": "triage_at_dawn.ogg",
        "The Whale - Dr. Awesome": "the_whale.ogg",
        "Prophet 2001 - Dr. Awesome": "prophet_2001.ogg",
        "Trans Atlantic - Lizardking": "trans_atlantic.ogg",
        #Fired route
        "Dealin Dope - Dr. Awesome": "dealin_dope.ogg",
        "Hit Me With Your Best Shot - Pat Benatar": "hitmewithyourbestshot.ogg",
        "Hightop - Dr. Awesome": "hightop.ogg",
        "Everlong - Foo Fighters": "everlong.ogg",
        "Local Forecast - Kevin MacLeod": "local_forecast.ogg",
        "Now What? 1 - Dr. Awesome": "now_what.ogg",
        "Happy Rock - Benjamin TISSOT": "happy_rock.ogg",
        "Energetic Rock - Every Day Music": "energetic_rock.ogg",
        "Racing Minigame Song - FNAF 6": "fnaf_6.ogg",
        "Guillotine World - Kikiyama": "france.ogg",
        "Dragon Castle - BreakingCopyright": "dragon_castle.ogg",
        "Youre At A Ball In The Gold Room - Nemos Dreamscapes": "gold_room.ogg",
        "Sweet Victory - David Eisley": "sweet_victory.ogg",
        "Dig This - Dr. Awesome": "dig_this.ogg",
        "Exotic - Panda Beats": "exotic.ogg",
        "ANOTHER HIM - Toby Fox": "another_him.ogg",
        #Country route
        "Wool Gloves - imagiro": "wool_gloves.ogg",
        "Conflict - David Vanacore": "conflict.ogg",
        "Tumultuous - David Vanacore": "tumultuous.ogg",
        "Lisbon Fever - Dr. Awesome": "lisbon_fever.ogg",
        "Automatic Love - Siix0": "automatic_love.ogg",
        "The Chase - Toby Fox": "chase.ogg",
        "Neko To Sanpo - NEKO WORKs": "neko_to_sanpo.ogg",
        "Real World - Project SEKAI": "real_world.ogg",
        "Afternoon Hills - BEST MUSIC": "afternoon_hills.ogg",
        "XDDCC - Gooseworx": "xddcc.ogg",
        "Muumin Tani Fuyu - Sumio Shiratori": "muumin_tani_fuyu.ogg",
        "Snufkin The Traveler - Sumio Shiratori": "snufin.ogg",
        "Lady Of The Cold - Sumio Shiratori": "lady_of_the_cold.ogg",
        #AI
        "School - Toby Fox": "school.ogg",
        "Cliffs - Toby Fox": "cliffs.ogg",
        "Circus - Toby Fox": "circus.ogg",
        "Friendship - Toby Fox": "friendship.ogg",
        #Archival
        "Facing Worlds - Michiel van den Bos": "facing_worlds.ogg",
        "BATTLE UNDER A BROKEN SKY - AZALI": "broken_sky.ogg",
        "Take a Trip from Me - u4ia": "take_trip.ogg",
        "Everybody Wants To Rule The World - Tears For Fears": "everybody_wants.ogg",
        #Genocide route
        "Insane Personalities - Pakoo": "insane_personalities.ogg",
        "Echoing? - Pakoo": "killcops.ogg",
        #DX: Train Route
        "Sub−Game Select - Jun Ishikawa": "sub_game_select.ogg",
        "Outdoors - Miki Obata": "outdoors.ogg",
        "Hide And Seek - Chiro": "hide_and_seek.ogg",
        "Ochre Woods ~ Day - Miki Obata": "ochre_woods_day.ogg",
        "Bedroom ~ Day - Miki Obata": "bedroom_day.ogg",
        "Item Bounce - Akira Miyagawa": "item_bounce.ogg",
        "Krabby Klub - Tsukasa Tawada": "krabby_klub.ogg",
        "Prof. Krane's Kidnap - Tsukasa Tawada": "prof_kranes_kidnap.ogg",
        "E. Gadd's Lab - Kazumi Totaka & Shinobu Tanaka": "e_gadds_lab.ogg",
        "ONBS - Tsukasa Tawada": "onbs.ogg",
        "Encounter! Friend - Waichiro Ozaki": "encounter_friend.ogg",
        "In The Room - Shogo Sakai": "in_the_room.ogg",
        "Roundabout - Yes" : "roundabout.ogg",
        "Insomnia - W∆W": "insomnia.ogg",
        "Space - W∆W": "space.ogg",
        "Lo−Fi Sunset - Dango Studio": "lo_fi_sunset.ogg",
        "Homely Yado Inn - Shogo Sakai" : "homely_yado_inn.ogg",
        #DX: Bronson
        "Upon Me - Dr. Awesome": "upon_me.ogg", 
        "Prophet ERROR - Pakoo": "error.ogg",
        #DX: Japan
        "village_1_JP013BM - Yuuka Kazami": "yuuka_town.ogg",
        #DX: Kuwait
        "The Man Who Sold The World - Nirvana": "tmwstw.ogg",
        #DX: Vibration
        "Let's Hear My Speed - Pakoo": "lets_hear_my_sped.ogg",
        "Fastbudget Song - Pakoo": "fastbudget_song.ogg",
        "Fastport.MID - Pakoo": "fastport.ogg",
        "Fasting - Pakoo": "fasting.ogg",
        "Happy Running - Pakoo": "happy_running.ogg",
        #DX: BTTF
        "Let's Hear My Baby: Spring Remix - Pakoo": "letshearspring.ogg",
        "Echoing: Spring Remix - Pakoo": "echoingspring.ogg",
        "Alien Atmosphere - Dr. Awesome": "alien_atmosphere.ogg",
        "Apple Kid - Keiichi Suzuki": "apple_kid.ogg",
        "10 Feet Away - Dr. Awesome": "10_feet_away.ogg",
        "Hitsquad 2 - Dr. Awesome": "hitsquad_2.ogg",
        "Get The Funk - Dr. Awesome": "get_the_funk.ogg",
        #DX: Finale
        "SPOT.FASSIMRD - Fun Value Land": "funvalueland.ogg",
        "Interference - Sanity": "interference.ogg",
        #DX: Character Ringtones
        "Hare Hare Yukai (Konata's Polyphonic Ringtone) - Tomokazu Tashiro & Satoru Kosaki": "sfx/sfx_ringtone_addy.ogg",
        "Billy Milly Mays - tadintid.se": "sfx/sfx_ringtone_billy.ogg",
        "CS OH YES - Unknown Artist": "sfx/sfx_ringtone_cs.ogg",
        "Now Or Never (sleepingSYUN Arrange) - M−Flo loves CHEMISTRY": "sfx/sfx_ringtone_tate.ogg",
        "Only One - ミカヅキBIGWAVE": "sfx/sfx_ringtone_tate_alt.ogg"
    }
    global album_map

    album_map = {
        "Billy's Mix - Billy Mays": "billymix.png",
        "CANYON.MID - George Stone": "windows.png",
        "PASSPORT.MID - George Stone": "windows.png",
        "stal - C418": "minecraft.png",
        "Undyne - Toby Fox": "undertale.png",
        "It's Showtime - Toby Fox": "undertale.png",
        "Danger Mystery - Toby Fox": "undertale.png",
        "Card Castle - Toby Fox": "deltarune.png",
        "Basement - Toby Fox": "deltarune.png",
        "Rude Buster - Toby Fox": "deltarune.png",
        "Lancer - Toby Fox": "deltarune.png",
        "ANOTHER HIM - Toby Fox": "deltarune.png",
        "School - Toby Fox": "deltarune.png",
        "Cliffs - Toby Fox": "deltarune.png",
        "Circus - Toby Fox": "deltarune.png",
        "The Chase - Toby Fox": "deltarune.png",
        "Friendship - Toby Fox": "deltarune.png",
        "Let's Do This - Home Depot": "homedepot.png",
        "Alfred's Theme - Eminem": "mtbmb.png",
        "New Leaf Title Theme - Kazumi Totaka": "newleaf.png",
        "Time for a Smackdown! - Mr. Sauceman": "pizzatower.png",
        "Good Eatin - ClascyJitto": "pizzatower.png",
        "Mort's Farm - ClascyJitto": "pizzatower.png",
        "Funiculi Holiday - ClascyJitto": "pizzatower.png",
        "Tunnely Shimbers - Mr. Sauceman": "pizzatower.png",
        "Hard Drive to Munch You - Mr. Sauceman": "pizzatower.png",
        "Thousand March - Mr. Sauceman": "pizzatower.png",
        "Good Eatin' - ClascyJitto": "pizzatower.png",
        "Tubular Trash Zone - Mr. Sauceman": "pizzatower.png",
        "Let's hear my baby - Walkman": "tracker.png",
        "scales of joy.mod - Mel O Dee": "tracker.png",
        "Hired Guns - Brian Johnston": "tracker.png",
        "Echoing - Banana": "tracker.png",
        "Mm Select - Matthew Simmonds": "tracker.png",
        "Mm Complete - Matthew Simmonds": "tracker.png",
        "Facing Worlds - Michiel van den Bos": "tracker.png",
        "Take a Trip from Me - u4ia": "tracker.png",
        "Insane Personalities - Pakoo": "trackerevil.png",
        "Prophet ERROR - Pakoo": "trackerevil.png",
        "Lisbon Fever - Dr. Awesome": "awesome.png",
        "Moongazer - Dr. Awesome": "awesome.png",
        "Lowbudget Song - Dr. Awesome": "awesome.png",
        "Tuna Fish - Dr. Awesome": "awesome.png",
        "L.A. By Night - Dr. Awesome": "awesome.png",
        "The Whale - Dr. Awesome": "awesome.png",
        "Prophet 2001 - Dr. Awesome": "awesome.png",
        "Dealin Dope - Dr. Awesome": "awesome.png",
        "Hightop - Dr. Awesome": "awesome.png",
        "Now What? 1 - Dr. Awesome": "awesome.png",
        "Dig This - Dr. Awesome": "awesome.png",
        "Lisbon Fever - Dr. Awesome": "awesome.png",
        "10 Feet Away - Dr. Awesome": "awesome.png",
        "Upon Me - Dr. Awesome": "awesome.png",
        "Hitsquad 2 - Dr. Awesome": "awesome.png",
        "Alien Atmoshpere - Dr. Awesome": "awesome.png",
        "Get The Funk - Dr. Awesome": "awesome.png",
        "Weird Personalities - Lizardking": "lizardking.png",
        "Nordic Report 1 - Lizardking": "lizardking.png",
        "Nordic Report 2 - Lizardking": "lizardking.png",
        "Compulsion To Obey - Lizardking": "lizardking.png",
        "For The People! - Lizardking": "lizardking.png",
        "Full Rulle Med Klas - Lizardking": "lizardking.png",
        "Desert Dawn - Lizardking": "lizardking.png",
        "Trans Atlantic - Lizardking": "lizardking.png",
        "Police Station - Lorin Nelson": "legoisland.png",
        "Happy Roaming - Lorin Nelson": "legoisland.png",
        "Park Theme - Lorin Nelson": "legoisland.png",
        "Lego Island Theme - Lorin Nelson": "legoisland.png",
        "Onett Theme - Keiichi Suzuki": "earthbound.png",
        "Buy Something Will Ya! - Keiichi Suzuki": "earthbound.png", 
        "Pokeys House - Keiichi Suzuki": "earthbound.png",
        "The Metropolis of Fourside - Keiichi Suzuki": "earthbound.png",
        "Apple Kid - Keiichi Suzuki": "earthbound.png",
        "Atarashii Kaze - Satoru Kosaki": "luckystar.png",
        "Bun Guster - Satoru Kosaki": "luckystar.png",
        "Taiikusai Desu Yo - Satoru Kosaki": "luckystar.png",
        "Candle World - Kikiyama": "yume.png",
        "Dense Woods B - Kikiyama": "yume.png",
        "Guillotine World - Kikiyama": "yume.png",
        "Klaxon Beat - Kelly Bailey": "half.png",
        "CP Violation - Kelly Bailey": "half.png",
        "Triage At Dawn - Kelly Bailey": "half.png",
        "Super Friendly - Kevin Macleod": "kevin.png",
        "Pixel Peeker Polka - Kevin MacLeod": "kevin.png",
        "Local Forecast - Kevin MacLeod": "kevin.png",
        "Track 4 - Weatherscan": "weather.png",
        "Track 3 - Weatherscan": "weather.png",
        "Pressing Pursuit ~ Cornered - Masakazu Sugimori": "aceattorney.png",
        "The Star Spangled Banner - THE UNITED STATES OF AMERICA": "america.png",
        "Billy Mays Gangsta Remix - mastamokei": "billymays.png",
        "Breakout - Shoichiro Sakamoto": "breakout.png",
        "Brick by Brick (Suck my Dick) - cs188": "brickbybrick.png",
        "BUBBLE TEA - dark cat": "bubbletea.png",
        "Wayward Wanderer - Deep Gnome": "deepgnome.png",
        "Alfred Hitchcock Intro Theme - Charles Gounod": "hitchcock.png",
        "Speedy Comet - Mahito Yokota": "mariogalaxy.png",
        "Melancholy - Imori": "melancholy.png",
        "MisLeader - Triosk and Jan Jelinek": "misleader.png",
        "Airport Counter - Kazumi Totaka": "newhorizons.png",
        "Summer Clearance Sale - BEST MUSIC": "summerclearance.png",
        "Morning Highway - BEST MUSIC": "summerclearance.png",
        "Afternoon Hills - BEST MUSIC": "summerclearance.png",
        "Supernova - Laszlo": "supernova.png",
        "Al's Penthouse - Andy Blythe": "toystory.png",
        "Rocket Game Corner - Junichi Masuda": "pkmnredblue.png",
        "Laurel Palace - Manami Matsumae" : "vegasstrikes.png",
        "Price Is Right Theme - Edd Kalehoff" : "priceisright.png",
        "Pierrot of the Star Spangled Banner - ZUN" : "touhou15.png",
        "Airport Infiltration - Andy Blythe & Marten Joustra" : "toystory.png",
        "Creative Exercise - Hirokazu Tanaka" : "mariopaint.png",
        "Hit Me With Your Best Shot - Pat Benatar" : "patbenatar.png",
        "Everlong - Foo Fighters" : "foofighter.png",
        "Happy Rock - Benjamin TISSOT" : "jermalore.png",
        "Racing Minigame Song - FNAF 6" : "fnaf6.png",
        "Sweet Victory - David Eisley" : "bubblebowl.png",
        "Exotic - Panda Beats ft. Newenx" : "pandabeats.png",
        "Wool Gloves - imagiro" : "woolgloves.png",
        "Conflict - David Vanacore" : "conflict.png",
        "Tumultuous - David Vanacore" : "conflict.png",
        "Neko To Sanpo - NEKO WORKs" : "nekopara.png",
        "Real World - Project SEKAI" : "projectsekai.png",
        "XDDCC - Gooseworx" : "digitalcircus.png",
        "Muumin Tani Fuyu - Sumio Shiratori" : "moomin.png",
        "Snufkin The Traveler - Sumio Shiratori" : "moomin.png",
        "Lady Of The Cold - Sumio Shiratori" : "moomin2.png",
        "Everybody Wants To Rule The World - Tears For Fears" : "tearsforfears.png",
        "BATTLE UNDER A BROKEN SKY - AZALI": "brokensky.png",
        "Sub−Game Select - Jun Ishikawa": "kirby64.png",
        "Outdoors - Miki Obata": "pkmnchannel.png",
        "Hide And Seek - Chiro": "hideandseek.png",
        "Ochre Woods ~ Day - Miki Obata": "heyyoupikachu.png",
        "Bedroom ~ Day - Miki Obata": "heyyoupikachu.png",
        "Item Bounce - Akira Miyagawa": "kirbyairride.png",
        "Krabby Klub - Tsukasa Tawada": "pokemonxd.png",
        "Prof. Krane's Kidnap - Tsukasa Tawada": "pokemonxd.png",
        "E. Gadd's Lab - Kazumi Totaka & Shinobu Tanaka": "luigismansion.png",
        "ONBS - Tsukasa Tawada": "pokemonxd.png",
        "Encounter! Friend - Waichiro Ozaki": "falsebound.png",
        "In The Room - Shogo Sakai": "mother3.png",
        "Roundabout - Yes" : "roundabout.png",
        "Insomnia - W∆W": "moon.png",
        "Space - W∆W": "moon.png",
        "Lo−Fi Sunset - Dango Studio": "lofisunset.png",
        "Homely Yado Inn - Shogo Sakai" : "mother3.png",
        "Let's Hear My Baby: Spring Remix - Pakoo": "csbii.png",
        "Echoing: Spring Remix - Pakoo": "csbii.png",
        "Let's Hear My Speed - Pakoo": "vibration.png",
        "Fastbudget Song - Pakoo": "vibration.png",
        "Fastport.MID - Pakoo": "vibration.png",
        "Fasting - Pakoo": "vibration.png",
        "Happy Running - Pakoo": "vibration.png",
        "Hare Hare Yukai (Konata's Polyphonic Ringtone) - Tomokazu Tashiro & Satoru Kosaki": "ringtone_addy.png",
        "Billy Milly Mays - tadintid.se": "ringtone_billy.png",
        "CS OH YES - Unknown Artist": "ringtone_cs.png",
        "Now Or Never (sleepingSYUN Arrange) - M−Flo loves CHEMISTRY": "ringtone_tate.png",
        "Only One - ミカヅキBIGWAVE": "ringtone_tate_alt.png"
    }

screen jukebox_nav():

    add Color('#323e42', alpha=0.75)

    viewport:
        xpos 25 ypos 150
        xsize 350 ysize 700
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            for k, v in music_map.items():
                textbutton k action ShowMenu("music_screen", k), Play("jukebox", "audio/" + v, relative_volume=0.5)

    textbutton "Return to Extras" action ShowMenu("category_welcome"), Stop("jukebox"), PauseAudio("music", False) yoffset 950 xoffset 25
    textbutton "Return" action Return(), Stop("jukebox"), PauseAudio("music", False) yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen jukebox_welcome():
    tag menu
    use jukebox_nav
    style_prefix "codex"
    python:
        music_count = len(music_map.keys())
        unlocked_music_count = len(persistent.heard)
    vbox:
        xsize 850
        xalign 0.5 yalign 0.5
        xoffset 200
        text "In this category, you can listen to all the sweet tunes you've discovered throughout CS's adventures!"
        text "([unlocked_music_count]/[music_count] unlocked)"


##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen music_screen(l):

    tag menu
    use jukebox_nav

    style_prefix "codex"
    $ track_title, artist = l.split("-", 1)
    vbox:
        xanchor 0.5
        xpos 1060
        ypos 100
        text track_title:
            xalign 0.5
            size 72
        text artist:
            xalign 0.5
            size 69

    viewport:

        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        image "images/jukebox/record.png":
            xysize(500, 500)
            xalign(0.375)
            yalign(0.50)
            at transform:
                rotate 0
                linear 5.0 rotate 360.0
                repeat
        if l not in album_map.keys() or album_map[l] is None:
            image "images/jukebox/csbi.png":
                xysize(500, 500)
                xalign(0.225)
                yalign(0.5)
        else:
            image f"images/jukebox/{album_map[l]}":
                xysize(512, 512)
                xalign(0.225)
                yalign(0.5)
