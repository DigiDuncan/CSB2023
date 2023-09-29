
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

# TODO: Order the jukebox

init python:
    global music_map
    #Name of Entry followed by file name
    music_map = {
        "BUBBLE TEA - darkcat": "bubble_tea.mp3",
        "Let's hear my baby - Walkman": "lets_hear_my_baby.mp3",
        "CANYON.MID - George Stone": "canyon.mp3",
        "Summer Clearance Sale - BEST MUSIC": "summer_clearance_sale.mp3",
        "scales of joy.mod - Mel O Dee": "scales_of_joy.mp3",
        "Alfred Hitchcock Intro Theme - Charles Gounod": "hohsis_theme.mp3",
        "Super Friendly - Kevin Macleod": "super_friendly.mp3",
        "Time for a Smackdown! - Mr. Sauceman": "time_for_a_smackdown.mp3",
        "Card Castle - Toby Fox": "card_castle.mp3",
        "Basement - Toby Fox": "basement.mp3",
        "stal - C418": "stal.mp3",
        "Moongazer - Dr. Awesome": "moongazer.mp3",
        "Onett Theme - Keiichi Suzuki": "onett.mp3",
        "The Star Spangled Banner - THE UNITED STATES OF AMERICA": "star_spangled_banner.mp3",
        "Buy Something Will Ya! - Keiichi Suzuki": "buy_something.mp3",
        "PASSPORT.MID - George Stone": "passport.mp3",
        "Good Eatin - ClascyJitto": "good_eatin.mp3",
        "Hired Guns - Brian Johnston": "hired_guns.mp3",
        "Undyne - Toby Fox": "undyne.mp3",
        "Atarashii Kaze - Satoru Kōsaki": "atarashii_kaze.mp3",
        "Police Station - Lorin Nelson": "police_station.mp3",
        "Echoing - Banana": "echoing.mp3",
        "Danger Mystery - Toby Fox": "danger_mystery.mp3",
        "Pressing Pursuit ~ Cornered - Masakazu Sugimori": "pressing_pursuit_cornered.mp3",
        "Bun Guster - Satoru Kōsaki": "bun_guster.mp3",
        "Happy Roaming - Lorin Nelson": "happy_roaming.mp3",
        "Tunnely Shimbers - Mr. Sauceman": "tunnely_shimbers.mp3",
        "Hard Drive to Munch You - Mr. Sauceman": "hard_drive.mp3",
        "Al's Penthouse - Andy Blythe": "penthouse.mp3",
        "Airport Infilration - Marten Joustra": "airport.mp3",
        "Laurel Palace - Manami Matsumae": "laurel_palace.mp3",
        "Price Is Right Theme - Edd Kalehoff": "price_right.mp3",
        "Mm Select - Matthew Simmonds": "mm_select.mp3",
        "Let's Do This - Home Depot": "home_depot.mp3",
        "Candle World - Kikiyama": "candle_world.mp3",
        "It's Showtime - Toby Fox": "showtime.mp3",
        "Mort's Farm - ClascyJitto": "mort_farm.mp3",
        "Taiikusai Desu Yo - Satoru Kosaki": "taiikusai_desu_yo.mp3",
        "Track 4 - Weatherscan": "track4.mp3",
        "Funiculi Holiday - ClascyJitto": "funiculi_holiday.mp3",
        "Speedy Comet - Mahito Yokota": "speedy_comet.mp3",
        "Breakout - Shoichiro Sakamoto": "breakout.mp3",
        "Park Theme - Lorin Nelson": "park_theme.mp3",
        "Alfred's Theme - Eminem": "hohsisremix.mp3",
        "Track 3 - Weatherscan": "track3.mp3",
        "New Leaf Title Theme - Kazumi Totaka": "ac_title.mp3",
        "Facing Worlds - Michiel van den Bos": "facing_worlds.mp3",
        "Take a Trip from Me - u4ia": "take_trip.mp3",
        "School - Toby Fox": "school.mp3",
        "Cliffs - Toby Fox": "cliffs.mp3",
        "Circus - Toby Fox": "circus.mp3",
        "The Chase - Toby Fox": "chase.mp3",
        "Friendship - Toby Fox": "friendship.mp3",
        "Creative Exercise - Hirokazu Tanaka": "creative_exercise.mp3",
        "Morning Highway - BEST MUSIC": "morning_highway.mp3",
        "Pixel Peeker Polka - Kevin MacLeod": "pixel_peeker_polka.mp3",
        "Lowbudget Song - Dr. Awesome": "lowbudget_song.mp3",
        "Klaxon Beat - Kelly Bailey": "klaxon_beat.mp3",
        "CP Violation - Kelly Bailey": "cp_violation.mp3",
        "Triage At Dawn - Kelly Bailey": "triage_at_dawn.mp3",
        "L.A. By Night - Dr. Awesome": "la_by_night.mp3",
        "Mm Complete - Matthew Simmonds": "mm_complete.mp3",
        "Tuna Fish - Dr. Awesome": "tuna_fish.mp3",
        "The Whale - Dr. Awesome": "the_whale.mp3",
        "Prophet 2001 - Dr. Awesome": "prophet_2001.mp3",
        "Lancer - Toby Fox": "lancer.mp3",
        "Weird Personalities - Lizardking": "weird_personalities.mp3",
        "Dealin Dope - Dr. Awesome": "dealin_dope.mp3",
        "Happy Rock - Benjamin TISSOT": "happy_rock.mp3",
        "Local Forecast - Kevin MacLeod": "local_forecast.mp3",
        "Racing Minigame Song - FNAF 6": "fnaf_6.mp3",
        "Youre At A Ball In The Gold Room - Nemos Dreamscapes": "gold_room.mp3",
        "GOOD VIBES - LitKidBeats": "good_vibes.mp3",
        "Hit Me With Your Best Shot - Pat Benatar": "hitmewithyourbestshot.mp3",
        "Hightop - Dr. Awesome": "hightop.mp3",
        "Now What? 1 - Dr. Awesome": "now_what.mp3",
        "Dig This - Dr. Awesome": "dig_this.mp3",
        "ANOTHER HIM - Toby Fox": "another_him.mp3",
        "Real World - Project SEKAI": "real_world.mp3",
        "Insane Personalities - Lizardking": "insane_personalities.mp3",
        "Echoing? - Banana": "killcops.mp3"
    }
    global album_map

    album_map = {
        "CANYON.MID - George Stone": "windows.png",
        "PASSPORT.MID - George Stone": "windows.png",
        "stal - C418": "minecraft.png",
        "Undyne - Toby Fox": "undertale.png",
        "It's Showtime - Toby Fox": "undertale.png",
        "Danger Mystery - Toby Fox": "undertale.png",
        "Card Castle - Toby Fox": "deltarune.png",
        "Basement - Toby Fox": "deltarune.png",
        "Rude Buster - Toby Fox": "deltarune.png",
        "Let's Do This - Home Depot": "homedepot.png",
        "Alfred's Theme - Eminem": "mtbmb.png",
        "New Leaf Title Theme - Kazumi Totaka": "newleaf.png",
        "Time for a Smackdown! - Mr. Sauceman": "pizzatower.png",
        "Good Eatin - ClascyJitto": "pizzatower.png",
        "Mort's Farm - ClascyJitto": "pizzatower.png",
        "Funiculi Holiday - ClascyJitto": "pizzatower.png",
        "Let's hear my baby - Walkman": "tracker.png",
        "scales of joy.mod - Mel O Dee": "tracker.png",
        "Moongazer - Dr. Awesome": "tracker.png",
        "Hired Guns - Brian Johnston": "tracker.png",
        "Echoing - Banana": "tracker.png",
        "Weird Personalities - Lizardking": "tracker.png",
        "Mm Select - Matthew Simmonds": "tracker.png",
        "Insane Personalities - Lizardking": "trackerevil.png",
        "Echoing? - Banana": "trackerevil.png",
        "Police Station - Lorin Nelson": "legoisland.png",
        "Happy Roaming - Lorin Nelson": "legoisland.png",
        "Park Theme - Lorin Nelson": "legoisland.png",
        "Onett Theme - Keiichi Suzuki": "earthbound.png",
        "Buy Something Will Ya! - Keiichi Suzuki": "earthbound.png", 
        "Atarashii Kaze - Satoru Kōsaki": "luckystar.png",
        "Bun Guster - Satoru Kōsaki": "luckystar.png",
        "Taiikusai Desu Yo - Satoru Kosaki": "luckystar.png",
        "Track 4 - Weatherscan": "weather.png",
        "Track 3 - Weatherscan": "weather.png"
    }

    # TODO: Complete album map.

screen jukebox_nav():

    add Color('#323e42', alpha=0.75)

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
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
        # TODO: Arc, can you center this? Thanks.


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
                xysize(500, 500)
                xalign(0.225)
                yalign(0.5)
