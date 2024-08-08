# Checks
default fanboy_type = None
default fanbase = None
default nice_car = False
default returning_from_blooper = False
default e1 = False
default e2 = False
default e3 = False
default england_check = False
default japan_check = False
default sweden_check = False
default ramsay_check = False
default gear_check = False
default tom_check = False
default anime_check = False
default karaoke_check = False
default miku_check = False
default joel_check = False
default lights_check = False
default ikea_check = False
default engfirst = False
default swedfirst = False
default japfirst = False
default archack = False
default jade = False
default clown = False
default nome = False  # wow I hate this name - DD

# Fired route
default band_name = "CS' Crazy Crew"
default ep_name = "The White Album"
default song_name_1 = "Prison Break"
default song_name_2 = "Down to Vegas"
default song_name_3 = "Globetrottin'"
default song_name_4 = "Through The Battles and the Fights"
default song_name_5 = "We Are The Winners"
default line_1 = ""
default line_2 = ""
default line_3 = ""
default line_4 = ""
default line_5 = ""
default line_6 = ""
default line_7 = ""
default line_8 = ""
default line_9 = ""
default line_10 = ""
default line_11 = ""
default line_12 = ""

# RPG
default enemy_1 = "cop"
default enemy_2 = "cop"
default enemy_3 = "cop"
default party_1 = "cs"
default party_2 = "tate"
default party_3 = "digi"
default party_4 = "arceus"
default ucn_bg = "images/bg/fnaf_office.png"  # DX: There is currently no way to set these.
default ucn_music = "minigames/pencil/rude_buster.mp3"  # "
default ucn_scale = 1.0
default cont = False

# Minigames
default minigame_win = "secret"
default minigame_loss = "secret"

default typewriter_text = "Hello, world!"

label splashscreen:
    return

label before_main_menu:
    python:
        seen_all = True
        for i in Replay_items:
            if not renpy.seen_label(i.replay):
                seen_all = False
        if seen_all:
            if not "Fin." in persistent.unlocked_achievements:
                    chievos = (a for a in achievements
                    if a.name == "Fin.")
                    renpy.show_screen("popup", next(chievos))
                    achievement_manager.unlock("Fin.", show_screen = False)
                    persistent.creative_mode = True
    return

label start:  # this might be required??
    return