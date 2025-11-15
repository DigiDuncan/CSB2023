init python:
    # For unused assets gallery
    unused_page = 0

    # For jukebox tagging
    current_jukebox_tag_index = 0

    # For bios page
    current_bios_sorting_mode = 0
    current_bios_sprite = 0
    current_bios_page = 0
    current_bios_total_pages = 0

    # For the subgame page
    current_subgame_name = None
    current_subgame_desc = None
    current_subgame_art = None
    current_subgame_label = None

    # For Ace Attorney parody
    current_evidence = 0

# If music is so good, why is there no Music 2?
init python:
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
        persistent.carrot_game_unlocked = True
        persistent.reversi_game_unlocked = True
        persistent.saved_christmas = True
        for label in renpy.get_all_labels():
            renpy.mark_label_seen(label)

# Character Definitions

# Generic Character Definitions
define n = Character(None, what_italic = True, callback = char_callback)  # Narrator
define chat = Character("Chat", callback = char_callback)
define unknown = Character("???", callback = char_callback)

# CS' Various Character Definitions
define cs = Character("cs188", callback = renpy.partial(char_callback, name = "cs", beep = "cs"))
define cs_fakegod = Character("cs188 (pretending to be CSGod)", callback = renpy.partial(char_callback, name = "cs", beep = "csgod"))
define csgod = Character("CSGod", callback = renpy.partial(char_callback, name = "csgod", beep = "csgod"), what_color="#CB50FF")
define ycs = Character("Young CS", callback = renpy.partial(char_callback, beep = "ycs"))

# CSBI Character Definitions (Including HoH SiS)
define carguy = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", beep = "nice"))
define carguy_nobeep = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", play_beeps = False))
define cashier = Character("Cashier", callback = renpy.partial(char_callback, name = "cashier"))
define craptop = Character("Craptop", callback = renpy.partial(char_callback, name = "craptop"))
define discord = Character("Discord", callback = char_callback)
define doug = Character("Doug", callback = renpy.partial(char_callback, name = "doug", beep = "doug"))
define greeter = Character("Greeter", callback = renpy.partial(char_callback, name = "doug", beep = "doug"))
define michael = Character("Michael", callback = renpy.partial(char_callback, name = "michael", beep = "mich"))
define michael_nobeep = Character("Michael", callback = renpy.partial(char_callback, name = "michael", play_beeps = False))
define phil = Character("Phil", callback = renpy.partial(char_callback, name = "phil", beep = "phil"))
define sticky = Character("Sticky Note", callback = renpy.partial(char_callback, name = "sticky"))
## HoH SiS
define ed = Character("Ed", callback = renpy.partial(char_callback, name = "ed", beep = "ed"))
define hoh_operator = Character("HoH SiS Operator", callback = char_callback)
define rich = Character("Richard", callback = renpy.partial(char_callback, name = "rich", beep = "rich"))
define wesley = Character("Wesley", callback = renpy.partial(char_callback, name = "wesley", beep = "wes"))
define worker_1 = Character("Worker 1", callback = char_callback)
define worker_2 = Character("Worker 2", callback = char_callback)
define worker_3 = Character("Worker 3", callback = char_callback)
define worker_4 = Character("Worker 4", callback = char_callback)
define worker_5 = Character("Worker 5", callback = char_callback)
define worker_6 = Character("Worker 6", callback = char_callback)
define worker_7 = Character("Worker 7", callback = char_callback)

# CSBII Character Definitions
define asylum_worker = Character("Mr. Mohs", callback = renpy.partial(char_callback, name = "mohs"))
define border_guard = Character("Border Guard", callback = renpy.partial(char_callback, name = "border_guard"))
define copguy = Character("Copguy", callback = renpy.partial(char_callback, name = "copguy", beep = "cop"))
define linus = Character("Linus", callback = renpy.partial(char_callback, name = "linus", beep = "ltt"))

# CSBIII Part 1 Character Definitions
define colton = Character("Colton", callback = renpy.partial(char_callback, name = "colton"))
define luke = Character("Luke", callback = renpy.partial(char_callback, name = "luke", beep = "luke"))
define sheriff = Character("Sheriff", callback = renpy.partial(char_callback, name = "sheriff", beep = "sheriff"))
define taran = Character("Taran", callback = renpy.partial(char_callback, name = "taran", beep = "taran"))

# CSBIII Friend Route Character Definitions (NPCs only, friends have their own section)
define bomaha = Character("Omaha", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define cop = Character("Cop", callback = renpy.partial(char_callback, name = "cop"))
define obama = Character("Obama", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define worker = Character("Worker", callback = char_callback)

# CSBIII South Route Character Definitions
define green = Character("Mr. Green", callback = renpy.partial(char_callback, name = "green", beep = "green"), what_color="#00FF00")
define jerma = Character("Jerma", callback = renpy.partial(char_callback, name = "jerma", beep = "jerma"))
define lancer = Character("Lancer", callback = renpy.partial(char_callback, name = "lancer", beep = "lancer"))
define lego = Character("LegoBot", callback = renpy.partial(char_callback, name = "lego", beep = "lego"))
define luigi = Character("Luigi", callback = renpy.partial(char_callback, name = "luigi", beep = "luigi"))
define trailtrash = Character("Trailer Trash", callback = renpy.partial(char_callback, name = "trailtrash"))
define tsa = Character("TSA Agent", callback = renpy.partial(char_callback, name = "tsa"))
## Reality Break Ending
define billy_far = Character("Billy (from off screen)", callback = renpy.partial(char_callback, beep = "billy_from_afar"))
define direct = Character("Director", callback = renpy.partial(char_callback, beep = "iris"))
define monika = Character("Monika", callback = renpy.partial(char_callback, name = "monika", beep = "monika"))

# CSBIII East Route Character Definitions
define billy = Character("Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define carla = Character("Carla", callback = renpy.partial(char_callback, beep = "carla"))
define cultist = Character("Cultist", callback = renpy.partial(char_callback, name = "cultist", beep = "cult"))
define cultist_2 = Character("Cultist 2", callback = char_callback)
define cultist_3 = Character("Cultist 3", callback = char_callback)
define gnome = Character("Gnome", callback = renpy.partial(char_callback, name = "gnome", beep = "gnome"))
define host = Character("Host", callback = renpy.partial(char_callback, name = "mettaton", beep = "snd_mtt"), what_font = "8bitoperator_jve.ttf", what_size = 40)
define mario = Character("Mario", callback = renpy.partial(char_callback, name = "mario"))
define peppino = Character("Peppino", callback = renpy.partial(char_callback, name = "peppino", beep = "peppino"))
define pencil = Character("Pencil Greeter", callback =renpy.partial(char_callback, name = "pencil"))
define shaggy_too_dope = Character("Shaggy Too Dope", callback = char_callback)
define scott = Character("Scott", callback = renpy.partial(char_callback, name = "scott", beep = "scott"))
define signup = Character("Signup Helper", callback = char_callback)
define smiley = Character("Smiley", callback = renpy.partial(char_callback, name = "smiley"))
define terry = Character("Terry", callback = renpy.partial(char_callback, name = "terry", beep = "terry"))
define tv_billy = Character("TV Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define streetguy = Character("Street Guy", callback = renpy.partial(char_callback, name = "streetguy", beep = "nice"))
define violent_jay = Character("Violent Jay", callback = renpy.partial(char_callback, name = "jay"))
define waitress = Character("Waitress", callback = char_callback)

# CSBIII Fired Route Character Definitions
define customer = Character("Customer", callback = char_callback)
define crowd = Character("Crowd", callback = char_callback)
define ges = Character("Ges", callback = renpy.partial(char_callback, name = "ges", beep = "ges"))
define guest = Character("Guest", callback = renpy.partial(char_callback, name = "guest"))
define howie = Character("Howie", callback = renpy.partial(char_callback, name = "howie", beep = "howie"))
define janitor = Character("Janitor", callback = char_callback)

# CSBIII Country Route Character Definitons
define nurse = Character("Nurse", callback = char_callback)
define benrey = Character("Benrey", callback = renpy.partial(char_callback, name = "benrey"))
## England
define gordon = Character("Gordon", callback = renpy.partial(char_callback, name = "gordon", beep = "gordon"))
define hammond = Character("Richard", callback = renpy.partial(char_callback, name = "hammond"))
define jeremy = Character("Jeremy", callback = char_callback)
define james = Character("James", callback = char_callback)
define tom = Character("Tom Scott", callback = renpy.partial(char_callback, name = "tom", beep = "tom"))
## Japan
define receptionist = Character("Receptionist", callback = char_callback)
define scott_pres = Character("Scott, President of Domino's Pizza", callback = renpy.partial(char_callback, name = "scott_pres", beep = "scott_pres"))
define miku = Character("Hatsune Miku", callback = renpy.partial(char_callback, name = "miku", beep = "miku"))
define sayori = Character("Sayori", callback = renpy.partial(char_callback, name = "sayori"))
## Sweden
define joel = Character("Vargskelethor Joel", callback = renpy.partial(char_callback, name = "joel", beep = "joel"))
define ikea_greeter = Character("Ikea Greeter", callback = char_callback)
define ikea_worker = Character("Ikea Worker", callback = char_callback)
define pomni = Character("Pomni", callback = renpy.partial(char_callback, name = "pomni", beep = "pomni"))
define average_swede = Character("Swede", callback = char_callback)
define alien = Character("Grey", callback = char_callback, what_font = "Eyecicles-Pz2.ttf", what_size = 40)
define moomin = Character("Moomin", callback = renpy.partial(char_callback, name = "moomin", beep = "moomin"))
define snufkin = Character("Snufkin", callback = renpy.partial(char_callback, name = "snufkin", beep = "snufkin"))
define alicia = Character("Alicia", callback = renpy.partial(char_callback, name = "alicia", beep = "alicia"))
define witch = Character("Witch", callback = renpy.partial(char_callback, name = "witch", beep = "witch"))

# Archival Ending Character Definitions
define k174 = Character("K17-M4", callback = renpy.partial(char_callback, name = "k174", beep = "k17"))
define k199 = Character("K19-M9", callback = renpy.partial(char_callback, beep = "k19"))
define k207 = Character("K20-M7", callback = renpy.partial(char_callback, beep = "k20"))

# Offscreen Character Definitions
define tate_offscreen = Character("???", callback = renpy.partial(char_callback, beep="tate"))
define tate_cyan_offscreen = Character("???", callback = renpy.partial(char_callback, beep="tate_cyan"))
define pakoo_offscreen = Character("???", callback = renpy.partial(char_callback, beep="pak"))
define green_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "green"), what_color="#00FF00")
define anno_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "anno"))
define k174_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "k17"))
define k199_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "k19"))
define k207_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "k20"))

# AI Imposter Character Definitions
define ed_ai = Character("\"Ed\"", callback = renpy.partial(char_callback, beep = "ed"))
define obamanobeep = Character("\"Obama\"", callback = renpy.partial(char_callback, play_beeps = False))
define bomahanobeep = Character("\"Omaha\"", callback = renpy.partial(char_callback, play_beeps = False))

# DX Misc Character Definitions
define copguyexe = Character("Copguy", callback = renpy.partial(char_callback, name = "copguy", beep = "copexe"))
define tate_cyan = Character("Tate?", callback = renpy.partial(char_callback, beep="tate_cyan"))

# DX Digi Character Definitions
define david = Character("David", callback = char_callback)
define george = Character("George", callback = char_callback)
define harold = Character("Harold", callback = char_callback)
define mr_krupp = Character("Mr. Krupp", callback = char_callback)
define weird_al = Character("Weird Al", callback = char_callback)

# DX BT1D Character Definitions
# TODO: need beeps
define phone = Character("Phone", callback = char_callback) # what if spamton?
define cvs = Character("CVS Employee", callback = char_callback)
define leedle = Character("Leedlelee Employee", callback = char_callback)
define diabetes_ceo = Character("CEO of Diabetes", callback = char_callback)
define diabetes_secretary = Character("Secretary of Diabetes", callback = char_callback)

# DX CultCon Character Definitions
define baumer = Character("Steve Baumer", callback = char_callback)
define blind_eye = Character("Blind Eye Cultist", callback = char_callback)
define cruise = Character("Tom Cruise", callback = renpy.partial(char_callback, name = "cruise"))
define l_cultist = Character("Lunatic Cultist", callback = char_callback)
define priest = Character("Priest", callback = char_callback)
define renovator = Character("Renovator", callback = char_callback)

# DX Kuwait Character Definitions
define k_doctor = Character("Kuwait Doctor", callback = char_callback)
define k_nurse = Character("Kuwait Nurse", callback = char_callback)
define l_snow = Character("Lt. Snow", callback = char_callback)
define RCOMEM = Character("Rocco Mem", callback = char_callback)
define suzuki = Character("Suzuki", callback = char_callback)

# DX Plane Route Character Definitions
define plane_npc_1 = Character("Passenger 1", callback = char_callback)
define plane_npc_2 = Character("Passenger 2", callback = char_callback)
define plane_npc_3 = Character("Passenger 3", callback = char_callback)
define k19 = Character("K-19", callback = renpy.partial(char_callback, name = "k19"))
define orville = Character("Orville Wright", callback = renpy.partial(char_callback, name = "wright"))
define wilbur = Character("Wilbur Wright", callback = renpy.partial(char_callback, name = "wright"))
define booger = Character("Mucinex Booger", callback = renpy.partial(char_callback, name = "booger"))

# DX Train Route Character Definitions
define amtrak_conductor = Character("Conductor", callback = renpy.partial(char_callback, name = "amtrak_conductor", beep = "amtrak_conductor"))
define amtrak_npc_1 = Character("Passenger 1", callback = char_callback)
define amtrak_npc_2 = Character("Passenger 2", callback = char_callback)
define amtrak_npc_3 = Character("Passenger 3", callback = char_callback)
define amtrak_stewardess = Character("Stewardess", callback = char_callback)
define lupin = Character("Lupin", callback = renpy.partial(char_callback, name = "lupin", beep = "lupin"))
define lupin_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "lupin"))
define mean_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "mean"))
define mean_nobeep = Character("Mean", callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_nobeep = Character("???", callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "zenigata"))
define imperfect_tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"), what_color = "#000000", screen = "perfect_tate_text")

# DX Holiday Special Definitions
define avgn = Character("James Rolfe", callback = renpy.partial(char_callback, name = "avgn", beep = "avgn"))
define tgt_worker = Character("Target Employee", callback = renpy.partial(char_callback, name = "tgt_worker", beep="pak"))
define walkie = Character("Walkie", callback = renpy.partial(char_callback, beep = "walkie"))
define everyone = Character("Everyone", callback = renpy.partial(char_callback, beep = "everyone"))
define everyone2 = Character("Everyone", callback = renpy.partial(char_callback, beep = "csbama17"))
define santa = Character("Santa Claus", callback = renpy.partial(char_callback, name = "santa", beep = "santa"))
define mike = Character("Mike",  callback = renpy.partial(char_callback, name = "mike", beep = "mike"))

# DX Finale Character Definitions
define perfect_billy = Character("Perfect Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"), screen = "perfect_billy_text")
define fiddle = Character("Fiddleford", callback = char_callback)
define cultcon_leader = Character("Cultcon Leader", callback = char_callback)

# DX Albu
define cashier_nobeep = Character("Cashier", callback = renpy.partial(char_callback, name = "cashier", play_beeps = False))
define cs_nobeep = Character("cs188", callback = renpy.partial(char_callback, name = "cs", play_beeps = False))
define crowd_nobeep = Character("Crowd", callback = renpy.partial(char_callback, play_beeps = False))
define daphone = Character("Da Phone", callback = renpy.partial(char_callback, play_beeps = False))
define everyone_nobeep = Character("Everyone", callback = renpy.partial(char_callback, play_beeps = False))
define hermaphrodite = Character("Hermaphrodite", callback = renpy.partial(char_callback, play_beeps = False))
define marty = Character ("Marty", callback = renpy.partial(char_callback, play_beeps = False))
define zelda = Character("Zelda", callback = renpy.partial(char_callback, play_beeps = False))

# Our Friends! Character Definitions
define addy = Character("Addy", callback = renpy.partial(char_callback, name = "addy", beep = "pak"))
define anne = Character("Anne", callback = renpy.partial(char_callback, name = "anne", beep = "anne"))
define anno = Character("Anno", callback = renpy.partial(char_callback, name = "anno", beep = "anno"))
define arceus = Character("Arceus", callback = renpy.partial(char_callback, name = "arceus", beep = "arc"))
define aria = Character("Aria", callback = renpy.partial(char_callback, name = "aria", beep = "aria"))
define blank = Character("Blank", callback = renpy.partial(char_callback, name = "blank", beep = "blank"))
define db = Character("DB05", callback = renpy.partial(char_callback, name = "db", beep = "db05"))
define digi = Character("Digi", callback = renpy.partial(char_callback, name = "digi", beep = "digi"))
define eliza = Character("Elizabeth", callback = renpy.partial(char_callback, name = "eliza", beep = "mika"))
define grace = Character("Grace", callback = renpy.partial(char_callback, name = "grace", beep = "grace"))
define horse = Character("Horse", callback = renpy.partial(char_callback, name = "horse", beep = "horse"))
define iris = Character("Iris", callback = renpy.partial(char_callback, name = "iris", beep = "iris"))
define k17 = Character("K-17", callback = renpy.partial(char_callback, name = "k17", beep = "k17"))
define k22 = Character("K-22", callback = renpy.partial(char_callback, name = "k22", beep = "k20"))
define kitty = Character("Kitty", callback = renpy.partial(char_callback, name = "kitty", beep = "kitty"))
define mean = Character("Mean", callback = renpy.partial(char_callback, name = "mean", beep = "mean"))
define midge = Character("Midge", callback = renpy.partial(char_callback, name = "midge", beep = "midge"))
define mika = Character("Mika", callback = renpy.partial(char_callback, name = "mika", beep = "mika"))
define nova = Character("Nova", callback = renpy.partial(char_callback, name = "nova"))
define pakoo = Character("Pakoo", callback = renpy.partial(char_callback, name = "pakoo", beep = "pak"))
define tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"))

# Layers?
define config.detached_layers += ["broadcast"]
image stage_screen = Window(Layer("broadcast", clipping = False), background = "minigames/pencil/stage.png")

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
default enemy_1 = "cop"
default enemy_2 = "cop"
default enemy_3 = "cop"
default party_1 = "cs"
default party_2 = "tate"
default party_3 = "digi"
default party_4 = "arceus"
default ucn_bg = "images/bg/fnaf_office.png"
default ucn_music = "rude_buster.ogg"
default ucn_scale = 1.0
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

# Checks: Testing
default hitpoints = 20
default reloading = 6

# Helpful lists
init python:
    bg_list = []
    for bg in file_list("images/bg"):
        if bg.endswith(".png"):
            bg_list.append("images/bg" + bg)

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
        if not EndingManager.all_seen:
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
    $ renpy.movie_cutscene(splash)
    $ persistent.seen_splash = True
    $ persistent.heard.add("bubble_tea")
    return

label before_main_menu:
    python:
        if ending_manager.all_seen() == True:
            if "fin" not in persistent.unlocked_achievements:
                achievement_manager.unlock("fin", show_screen = False)
                if persistent.creative_mode == False:
                    persistent.creative_mode = True
                    renpy.call_screen("special_unlock", "Noice! You've unlocked Creative Mode! Check out all the new stuff in Extras!")

        if not persistent.seen_splash:
            if not renpy.music.is_playing():
                renpy.music.play("bubble_tea.ogg", loop = False)
        else:
            if not renpy.music.is_playing():
                renpy.music.play("<from 16.53>bubble_tea.ogg", loop = False)
                persistent.seen_splash = False
    return

label start:  # this might be required??
    # yep, it's required, but i'm fixing it to default to main menu instead - tate
    return
