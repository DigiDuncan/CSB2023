
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------


init python:
    global music_map
    #Name of Entry followed by file name
    music_map = {
        #Title
        "BUBBLE TEA - darkcat": "bubble_tea.mp3",
        #CSB1
        "Let's hear my baby - Walkman": "lets_hear_my_baby.mp3",
        "CANYON.MID - George Stone": "canyon.mp3",
        "Summer Clearance Sale - BEST MUSIC": "bestmusicu.mp3",
        "scales of joy.mod - Mel O Dee": "scales_of_joy.mp3",
        "Alfred Hitchcock Intro Theme - Charles Gounod": "hohsis_theme.mp3",
        "Super Friendly - Kevin Macleod": "super_friendly.mp3",
        "Time for a Smackdown! - Mr. Sauceman": "time_for_a_smackdown.mp3",
        #CSB2
        "Card Castle - Toby Fox": "card_castle.mp3",
        "Basement - Toby Fox": "basement.mp3",
        "stal - C418": "stal.mp3",
        "Moongazer - Dr. Awesome": "moongazer.mp3",
        "Onett Theme - Keiichi Suzuki": "onett.mp3",
        "The Star Spangled Banner - THE UNITED STATES OF AMERICA": "star_spangled_banner.mp3",
        "Buy Something Will Ya! - Keiichi Suzuki": "buy_something.mp3",
        "PASSPORT.MID - George Stone": "passport.mp3",
        #True route
        "Good Eatin' - ClascyJitto": "good_eatin.mp3",
        "Supernova - Laszlo": "supernova.mp3",
        "Airport Counter - Kazumi Totaka": "airport_counter.mp3",
        "Hired Guns - Brian Johnston": "hired_guns.mp3",
        "Undyne - Toby Fox": "undyne.mp3",
        "Atarashii Kaze - Satoru Kosaki": "atarashii_kaze.mp3",
        "Police Station - Lorin Nelson": "police_station.mp3",
        "Echoing - Banana": "echoing.mp3",
        "Danger Mystery - Toby Fox": "danger_mystery.mp3",
        "Pressing Pursuit ~ Cornered - Masakazu Sugimori": "pressing_pursuit_cornered.mp3",
        "Bun Guster - Satoru Kosaki": "bun_guster.mp3",
        "Happy Roaming - Lorin Nelson": "happy_roaming.mp3",
        "Mm Select - Matthew Simmonds": "mm_select.mp3",
        "Billy Mays Gangsta Remix - mastamokei": "billy_radio.mp3",
        "Weird Personalities - Lizardking": "weird_personalities.mp3",
        "Let's Do This - Home Depot": "home_depot.mp3",
        "Candle World - Kikiyama": "candle_world.mp3",
        "It's Showtime - Toby Fox": "showtime.mp3",
        "Mort's Farm - ClascyJitto": "mort_farm.mp3",
        "Taiikusai Desu Yo - Satoru Kosaki": "taiikusai_desu_yo.mp3",
        "Track 4 - Weatherscan": "track4.mp3",
        "Funiculi Holiday - ClascyJitto": "funiculi_holiday.mp3",
        "Speedy Comet - Mahito Yokota": "speedy_comet.mp3",
        "Wayward Wanderer - Deep Gnome": "wayward_wanderer.mp3",
        "MisLeader - Triosk and Jan Jelinek": "mis_leader.mp3",
        "Melancholy - Imori": "melancholy.mp3",
        "Tubular Trash Zone - Mr. Sauceman": "trash_zone.mp3",
        "Breakout - Shoichiro Sakamoto": "breakout.mp3",
        "The Metropolis of Fourside - Keiichi Suzuki": "fourside.mp3",
        "Pokeys House - Keiichi Suzuki": "pokey.mp3",
        "Rude Buster - Toby Fox": "rude_buster.mp3",
        "Billy's Mix - Billy Mays": "billymusicu.mp3",
        "Park Theme - Lorin Nelson": "park_theme.mp3",
        "Alfred's Theme - Eminem": "hohsisremix.mp3",
        "Track 3 - Weatherscan": "track3.mp3",
        "New Leaf Title Theme - Kazumi Totaka": "ac_title.mp3",
        #South route
        "Brick by Brick (Suck my Dick) - cs188": "brick_by_dick.mp3",
        "Tunnely Shimbers - Mr. Sauceman": "tunnely_shimbers.mp3",
        "Hard Drive to Munch You - Mr. Sauceman": "hard_drive.mp3",
        "Al's Penthouse - Andy Blythe": "penthouse.mp3",
        "Laurel Palace - Manami Matsumae": "laurel_palace.mp3",
        "Lancer - Toby Fox": "lancer.mp3",
        "Price Is Right Theme - Edd Kalehoff": "price_right.mp3",
        "Pierrot of the Star Spangled Banner - ZUN": "clownpiece.mp3",
        "Airport Infiltration - Andy Blythe & Marten Joustra": "airport.mp3",
        "Lego Island Theme - Lorin Nelson": "lego_island.ogg",
        #Friend route
        "Morning Highway - BEST MUSIC": "morning_highway.mp3",
        "Creative Exercise - Hirokazu Tanaka": "creative_exercise.mp3",
        "Pixel Peeker Polka - Kevin MacLeod": "pixel_peeker_polka.mp3",
        "Nordic Report 1 - Lizardking": "nordic_report_1.mp3",
        "Nordic Report 2 - Lizardking": "nordic_report_2.mp3",
        "Lowbudget Song - Dr. Awesome": "lowbudget_song.mp3",
        "Klaxon Beat - Kelly Bailey": "klaxon_beat.mp3",
        "CP Violation - Kelly Bailey": "cp_violation.mp3",
        "Mm Complete - Matthew Simmonds": "mm_complete.mp3",
        "Compulsion To Obey - Lizardking": "compulsion_to_obey.mp3",
        "For The People! - Lizardking": "for_the_people.mp3",
        "Tuna Fish - Dr. Awesome": "tuna_fish.mp3",
        "Full Rulle Med Klas - Lizardking": "full_rulle_med_klas.mp3",
        "Dense Woods B - Kikiyama": "dense_woods_b.mp3",
        "Desert Dawn - Lizardking": "desert_dawn.mp3",
        "L.A. By Night - Dr. Awesome": "la_by_night.mp3",
        "Thousand March - Mr. Sauceman": "thousand_march.mp3",
        "Triage At Dawn - Kelly Bailey": "triage_at_dawn.mp3",
        "The Whale - Dr. Awesome": "the_whale.mp3",
        "Prophet 2001 - Dr. Awesome": "prophet_2001.mp3",
        "Trans Atlantic - Lizardking": "trans_atlantic.mp3",
        #Fired route
        "Dealin Dope - Dr. Awesome": "dealin_dope.mp3",
        "Hit Me With Your Best Shot - Pat Benatar": "hitmewithyourbestshot.mp3",
        "Hightop - Dr. Awesome": "hightop.mp3",
        "Everlong - Foo Fighters": "everlong.mp3",
        "Local Forecast - Kevin MacLeod": "local_forecast.mp3",
        "Now What? 1 - Dr. Awesome": "now_what.mp3",
        "Happy Rock - Benjamin TISSOT": "happy_rock.mp3",
        "Energetic Rock - Every Day Music": "energetic_rock.mp3",
        "Racing Minigame Song - FNAF 6": "fnaf_6.mp3",
        "Guillotine World - Kikiyama": "france.mp3",
        "Dragon Castle - BreakingCopyright": "dragon_castle.mp3",
        "Youre At A Ball In The Gold Room - Nemos Dreamscapes": "gold_room.mp3",
        "Sweet Victory - David Eisley": "sweet_victory.mp3",
        "Dig This - Dr. Awesome": "dig_this.mp3",
        "Exotic - Panda Beats": "exotic.mp3",
        "ANOTHER HIM - Toby Fox": "another_him.mp3",
        #Country route
        "Wool Gloves - imagiro": "wool_gloves.mp3",
        "Conflict - David Vanacore": "conflict.mp3",
        "Tumultuous - David Vanacore": "tumultuous.mp3",
        "Lisbon Fever - Dr. Awesome": "lisbon_fever.mp3",
        "Automatic Love - Siix0": "automatic_love.mp3",
        "The Chase - Toby Fox": "chase.mp3",
        "Neko To Sanpo - NEKO WORKs": "neko_to_sanpo.mp3",
        "Real World - Project SEKAI": "real_world.mp3",
        "Afternoon Hills - BEST MUSIC": "afternoon_hills.mp3",
        "XDDCC - Gooseworx": "xddcc.mp3",
        "Muumin Tani Fuyu - Sumio Shiratori": "muumin_tani_fuyu.mp3",
        "Snufkin The Traveler - Sumio Shiratori": "snufin.mp3",
        "Lady Of The Cold - Sumio Shiratori": "lady_of_the_cold.mp3",
        #AI
        "School - Toby Fox": "school.mp3",
        "Cliffs - Toby Fox": "cliffs.mp3",
        "Circus - Toby Fox": "circus.mp3",
        "Friendship - Toby Fox": "friendship.mp3",
        #Archival
        "Facing Worlds - Michiel van den Bos": "facing_worlds.mp3",
        "BATTLE UNDER A BROKEN SKY - AZALI": "broken_sky.mp3",
        "Take a Trip from Me - u4ia": "take_trip.mp3",
        "Everybody Wants To Rule The World - Tears For Fears": "everybody_wants.mp3",
        #Genocide route
        "Insane Personalities - Lizardking": "insane_personalities.mp3",
        "Echoing? - Banana": "killcops.mp3",
        #DX: Train Route
        "Sub−Game Select - Jun Ishikawa": "sub_game_select.ogg",
        "Outdoors - Miki Obata": "outdoors.ogg",
        "Ochre Woods ~ Day - Miki Obata": "ochre_woods_day.ogg",
        "Bedroom ~ Day - Miki Obata": "bedroom_day.ogg",
        "Item Bounce - Akira Miyagawa": "item_bounce.ogg",
        "Krabby Klub - Tsukasa Tawada": "krabby_klub.ogg",
        "Prof. Krane's Kidnap - Tsukasa Tawada": "prof_kranes_kidnap.ogg",
        "E. Gadd's Lab - Kazumi Totaka & Shinobu Tanaka": "e_gadds_lab.ogg",
        "ONBS - Tsukasa Tawada": "onbs.ogg",
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
        "Insane Personalities - Lizardking": "trackerevil.png",
        "Echoing? - Banana": "trackerevil.png",
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
        "BUBBLE TEA - darkcat": "bubbletea.png",
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
        "Ochre Woods ~ Day - Miki Obata": "heyyoupikachu.png",
        "Bedroom ~ Day - Miki Obata": "heyyoupikachu.png",
        "Item Bounce - Akira Miyagawa": "kirbyairride.png",
        "Krabby Klub - Tsukasa Tawada": "pokemonxd.png",
        "Prof. Krane's Kidnap - Tsukasa Tawada": "pokemonxd.png",
        "E. Gadd's Lab - Kazumi Totaka & Shinobu Tanaka": "luigismansion.png",
        "ONBS - Tsukasa Tawada": "pokemonxd.png",
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
                if k in persistent.heard:
                    if v in ["lancer.mp3"]:
                        textbutton k action ShowMenu("music_screen", k), Play("jukebox", "secret/" + v, relative_volume=0.5)
                    elif v in ["supernova.mp3"]:
                        textbutton k action ShowMenu("music_screen", k), Play("jukebox", "minigames/editing/" + v, relative_volume=0.5)
                    elif v in ["rude_buster.mp3"]:
                        textbutton k action ShowMenu("music_screen", k), Play("jukebox", "minigames/pencil/" + v, relative_volume=0.5)
                    else:
                        textbutton k action ShowMenu("music_screen", k), Play("jukebox", "audio/" + v, relative_volume=0.5)

    textbutton "Return to categories" action ShowMenu("category_welcome"), Stop("jukebox"), PauseAudio("music", False) yoffset 950 xoffset 25
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
