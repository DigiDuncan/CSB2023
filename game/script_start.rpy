init python:
    # For Ace Attorney parody
    chosen_evidence = 0

    # For RPG
    rpg_final_party = []

    # If music is so good, why is there no Music 2?
    renpy.music.register_channel("sound2", "sfx")
    renpy.music.register_channel("music5", "music")
    renpy.music.register_channel("music4", "music")
    renpy.music.register_channel("music3", "music")
    renpy.music.register_channel("music2", "music", movie=True)
    renpy.music.register_channel("jukebox", "music")
    renpy.music.register_channel("notification", "sfx")
    renpy.music.register_channel("dxcom", "sfx")

init 10 python:
    def unlock_all():
        for m in MUSIC_MAP.keys():
            persistent.heard.add(m)
        for p in name_map.keys():
            persistent.seen.add(p)
        for i in ITEM_MAP.keys():
            persistent.collected.add(i)
        for o in ORIGINAL_27:
            persistent.seen_original_endings.add(o)
        for e in ALL_ENDINGS:
            persistent.seen_all_endings.add(e)
        achievement_manager.unlock_all()
        persistent.true_ending = True
        persistent.csb2_unlocked = True
        persistent.csb3a_unlocked = True
        persistent.csb3b_unlocked = True
        persistent.defeated_perfect_tate = True
        persistent.awawa_mode = True
        persistent.saved_christmas = True
        for label in renpy.get_all_labels():
            renpy.mark_label_seen(label)
        # TODO: we need a better way to unlock themes
        persistent.unlocked_themes.add("christmas")
        persistent.unlocked_themes.add("tate")

    def jump_to_label_start():
        renpy.jump(store.last_label)

# Layers?
define config.detached_layers += ["broadcast"]
image stage_screen = Window(Layer("broadcast", clipping = False), background = "minigames/pencil/stage.png")

# Custom URL handlers?
define config.hyperlink_handlers["sound"] = renpy.sound.play

# Letterbox color
define config.gl_clear_color = "#000000"

# Checks: CSB1
default ch1_direction = "left"
default ch1_direction_sprite = 6
default ch1_direction_line = "A...{w=0.5} pineapple?"

# Checks: CSB1 Error
default e1 = False
default e2 = False
default e3 = False

# Checks: CSB3 & CSB3 Friend
default fanboy_type = None
default fanbase = None
default compass_west_counter = 0
default compass_north_counter = 0
default compass_current_time = "morning"
default compass_current_shader = ""

default nice_car = False

# Checks: CSB3 Country
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
default jpnfirst = False

# Checks: CSB3 East
default archack = False
default clown = False
default nome = False  # wow I hate this name - DD

# Checks: CSB3 South
default jade = False
default returning_from_blooper = False
default south_car_stole_money = False

# Checks: CSB3 Fired
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

# Checks: RPG
default cont = False

# Checks: Asset counts
default sfxtotal = ""
default musictotal = ""
default charactertotal = ""
default transformtotal = ""
default bgtotal = ""
default movietotal = ""
default spritetotal = ""

# Checks: DX Train
default train_money_stolen = False
default train_money_container = "briefcase"
default train_money_stolen_dialogue_switch = "latch it shut"
default train_money_stolen_dialogue_switch_2 = " won"
default train_polar_express_fun_value = False
default train_pancake_fun_value = False
default train_skip_at_chicago = None
default train_tate_is_fragile_fun_value = False
default train_ending_money_returned = False
default ch2_cs_attack_used = "pushed"
default cs_chosen_form = "cs_vs_tate_punch"

# Checks: DX Kuwait
default tutorial = False
default gunsmith_check = False
default mechanic_check = False
default bar_check = False
default heli_check = False
default civvies_check = False
default pmc_check = False

# Checks: DX BTTF
default terraria_question_1 = ""
default terraria_question_2 = ""
default terraria_question_3 = ""
default csb_question_1 = ""
default csb_question_2 = ""
default csb_question_3 = ""
default lunatic_votes = 0
default pencil_votes = 0
default science_votes = 0
default cath_votes = 0
default blind_votes = 0
default total_votes = 0
default cath_counter = 0
default god_money = False
default pencil_check = False
default check2 = False
default cath_check = False
default cath_check2 = False
default lunatic_check = False
default lunatic_check2 = False
default lunatic_check3 = False
default science_check = False
default science_check2 = False
default blind_check = False
default blind_check2 = False
default blind_check3 = False
default blue_check = False
default con_start = False
default gun_get = False
default fiddle_search = False
default quest_finished = False
default blanchin = False

# Checks: DX Christmas
default tree_first = False
default got_tree = False
default lights_first = False
default got_lights = False
default decor_first = False
default got_decor = False
default got_tato_bag = False
default got_target_circle = False
default in_d20_viewer = False
default d20 = 1
default playing_reversi_again = False

# Checks: DX BT1D
default digi_smol = False

# Checks: Testing
default hitpoints = 20
default reloading = 6

# Helpful lists
init python:

    # Load ALL backgrounds
    bg_list = []
    for bg in file_list("images/bg"):
        if bg.endswith(".png"):
            bg_list.append("images/bg" + bg)

    # Blacklist certain backgrounds from UCN
    ucn_bg_list = bg_list.copy()
    ucn_remove = []

    for bg in ucn_bg_list:
        # Blacklist whole folders
        for folder in UCN_BLACKLIST_MAP:
            if "ALL" in UCN_BLACKLIST_MAP[folder]["files"] and ("/" + folder + "/") in bg:
                ucn_remove.append(bg)
            # Blacklist individual files
            else:
                for file in UCN_BLACKLIST_MAP[folder]["files"]:
                    check_path = "images/bg/" + folder + "/" + file + ".png" if folder != "MAIN" else "images/bg/" + file + ".png"
                    if bg == check_path:
                        # logger.info("Added " + bg + " to remove list")
                        ucn_remove.append(bg)

    for bg_to_remove in ucn_remove:
        if bg_to_remove in ucn_bg_list:
            # logger.info("Removing " + bg_to_remove + " from UCN list")
            ucn_bg_list.remove(bg_to_remove)

    # Load ALL BGMs
    bgm_list = []
    for bgm in file_list("audio"):
        if bgm.endswith(".ogg") and "sfx" not in bgm and "unused" not in bgm:
            bgm_list.append("audio/" + bgm)

# Minigames
default minigame_win = "secret_dx"
default minigame_loss = "secret_dx"

default current_dxcom = "1"

python early:
    # BAD END
    def parse_bad_end(lexer):
        text = lexer.string()
        label = lexer.string()

        return (text, label)

    def execute_bad_end(parsed_object):
        global typewriter_text
        text, label = parsed_object
        _window_hide()
        seen_all = True
        # TODO: handle the unlock of creative mode better, probably. at least it no longer crashes.
        if not ending_manager.all_seen():
            seen_all = False
        if seen_all:
            achievement_manager.unlock("fin")
        renpy.show("bad_end_screen")
        renpy.pause(1.0)
        typewriter_text = text
        renpy.show("typewriter", [typewriter_location])
        renpy.pause()
        renpy.end_replay()
        renpy.jump(label)

    renpy.register_statement(
        name = "bad_end",
        parse = parse_bad_end,
        execute = execute_bad_end,
        block = False
    )

    # MINIGAME
    def parse_minigame(lexer):
        label = lexer.string()
        win = lexer.string()
        loss = lexer.string()

        return (label, win, loss)

    def execute_minigame(parsed_object):
        global minigame_win
        global minigame_loss
        label, win, loss = parsed_object
        minigame_win = win
        minigame_loss = loss
        renpy.jump(label)

    renpy.register_statement(
        name = "minigame",
        parse = parse_minigame,
        execute = execute_minigame,
        block = False
    )

label splashscreen:
    python:
        if preferences.disable_menu_theme == False:
            renpy.movie_cutscene(get_themed_attribute("splash", "webm"))
            
        persistent.seen_splash = True
        persistent.heard.add(gui_theme_map["menu_music_jukebox_id"])
    return

label before_main_menu:
    python:
        renpy.free_memory()

        if "default" not in persistent.unlocked_themes:
            persistent.unlocked_themes.add("default")

        reload_theme(preferences.gui_theme, False)
        gui.rebuild()

        if ending_manager.all_seen() == True:
            if "fin" not in persistent.unlocked_achievements:
                achievement_manager.unlock("fin", show_screen = False)
                if persistent.creative_mode == False:
                    persistent.creative_mode = True
                    renpy.call_screen("special_unlock", "Noice! You've unlocked Creative Mode!\nLook out for new CSettings and more!")

        if preferences.disable_menu_theme == False:
            if not persistent.seen_splash:
                if not renpy.music.is_playing():
                    renpy.music.play(gui_theme_map["menu_music"], loop = False, channel="music")
            else:
                if not renpy.music.is_playing():
                    renpy.music.play(gui_theme_map["menu_music_skip_splash"], loop = False, channel="music")
                    persistent.seen_splash = False

    return

label start:  # this might be required??
    # yep, it's required, but i'm fixing it to default to main menu instead - tate
    return

### DATA MANAGEMENT ###

label clear_data:
    call screen confirm(message="ARE YOU SURE? This will ERASE all data.", yes_action=Jump("reset_vector"), no_action=[Hide("confirm")])
    return

label reset_vector:
    $ persistent._clear(progress=True)
    $ renpy.quit(relaunch = True)

label clear_saves:
    call screen confirm(message="ARE YOU SURE? This will erase ALL your save slots.", yes_action=Jump("reset_saves"), no_action=[Hide("confirm")])

label reset_saves:
    python:
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    $ renpy.quit(relaunch = True)


