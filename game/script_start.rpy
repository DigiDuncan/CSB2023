# Text Beep Spacing
# Partially stolen from:
#   https://www.renpy.org/doc/html/config.html#var-config.replace_text
#   https://lemmasoft.renai.us/forums/viewtopic.php?t=22730
# This is meant to place pauses after certain punctuation automatically so that the dialogue feels more... human.
# These are set up so that it only works if there is more than once sentence in the text box at any given time.
# Make sure there's a space after your punctuation or it won't work.
# You can still add manual pauses wherever you like in the script if this isn't enough for you.
# If for some reason you do NOT want the auto-pause in a certain line, put {w=0} immediately after the punctuation.
#   Real examples:
#       mean "Hey! You,{w=0} there!"
#       tate "Excuse me, Mr.{w=0} Conductor?"

init python:
    # For unused assets gallery
    unused_page = 0
    
    # For jukebox tagging
    current_jukebox_tag_index = 0
    

init python:
    import re
    def auto_wait(s):
        # these items wait for 0.25:
        # commas, periods, question marks, exclamation marks, semicolons
        s = re.sub(r'(([,|.|?|!|;])(({\/[a-z]*})*) )', r'\1{w=0.25}', s, flags=re.IGNORECASE) 

        # these items wait for 0.5:
        # ellipses, em-dashes, colons
        s = re.sub(r'((\.\.\.|--|:)(({\/[a-z]*})*) )', r'\1{w=0.5}', s, flags=re.IGNORECASE) 

        return s
    config.say_menu_text_filter = auto_wait

init python:
    import random
    roller=random.randint(1,20)

# BetterSnowBlossom() - not done yet
init python:
    import math
    from renpy.display.particle import SnowBlossomParticle
    class BetterSnowBlossomParticle(SnowBlossomParticle):
        def __init__(randomrot, min_x, max_x, min_y, max_y):
            self.randomrot = randint(1,360)
            self.min_x = min_x
            self.max_x = max_x
            self.min_y = min_y
            self.max_y = max_y

# Flips + color shaders
init -10 python:
    # dusk shader
    duskmatrix = TintMatrix("#ffaa49")
    
    def duskshade(s):
        return Transform(s, matrixcolor=duskmatrix)
        
    def duskshadeflip(s):
        return Transform(s, xzoom = -1, matrixcolor = duskmatrix)
        
    config.displayable_prefix["dusk"] = duskshade
    config.displayable_prefix["dusk:flip"] = duskshadeflip
    
    # dark shader
    darkmatrix = TintMatrix("#4848b8")
    
    def darkshade(s):
        return Transform(s, matrixcolor = darkmatrix)
        
    def darkshadeflip(s):
        return Transform(s, xzoom = -1, matrixcolor = darkmatrix)
        
    config.displayable_prefix["dark"] = darkshade
    config.displayable_prefix["dark:flip"] = darkshadeflip
    
    # white silhouette
    sil_white_matrix = BrightnessMatrix(value=1.0)
        
    def sil_white(s):
        return Transform(s, xzoom = 1, matrixcolor = sil_white_matrix)
        
    def sil_white_flip(s):
        return Transform(s, xzoom = -1, matrixcolor = sil_white_matrix)

    config.displayable_prefix["sil_white"] = sil_white
    config.displayable_prefix["sil_white:flip"] = sil_white_flip

    # black silhouette
    sil_black_matrix = BrightnessMatrix(value=-1.0)
        
    def sil_black(s):
        return Transform(s, xzoom = 1, matrixcolor = sil_black_matrix)
        
    def sil_black_flip(s):
        return Transform(s, xzoom = -1, matrixcolor = sil_black_matrix)

    config.displayable_prefix["sil_black"] = sil_black
    config.displayable_prefix["sil_black:flip"] = sil_black_flip

    # x flip
    def xflip(s):
        return Transform(s, xzoom = -1)
        
    config.displayable_prefix["flip"] = xflip
    
    
# Text beeps
init python:
    renpy.music.register_channel("beep", "voice", loop = True)
    def char_callback(event, name = None, beep = None, play_beeps = True, **kwargs):
        if "woohoo" in kwargs["what"].lower():
            persistent.woohoo += 0.16666666666666666667
        if name:
            persistent.seen.add(name)
            if all([a in persistent.seen for a in name_map.keys()]):
                achievement_manager.unlock("Gotta Catch Them All")
        if preferences.text_beeps and play_beeps:
            if event == "show":
                if beep is not None:
                    renpy.sound.play(f"audio/text/{beep}.wav", channel = "beep", loop = True)
                else:
                    renpy.sound.play(f"audio/text/ut.wav", channel = "beep", loop = True)
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel = "beep")

# If music is so good, why is there no Music 2?
init python:
    renpy.music.register_channel("sound2", "sound")
    renpy.music.register_channel("music4", "music")
    renpy.music.register_channel("music3", "music")
    renpy.music.register_channel("music2", "music")
    renpy.music.register_channel("jukebox", "music")
    renpy.music.register_channel("sfx", "sound")
    renpy.music.register_channel("dxcom", "sound")

init 10 python:
    def unlock_all():
        for m in music_map.keys():
            persistent.heard.add(m)
        for p in name_map.keys():
            persistent.seen.add(p)
        for i in item_map.keys():
            persistent.collected.add(i)
        achievement_manager.unlock_all()
        persistent.true_ending = True
        persistent.csb2_unlocked = True
        persistent.csb3a_unlocked = True
        persistent.csb3b_unlocked = True
        for label in renpy.get_all_labels():
            renpy.mark_label_seen(label)

# Custom transforms
transform rotate_10:
    subpixel True
    rotate 10 xanchor 0.5 yanchor 0.5
    xpos 0.5
    ypos 0.5
    zoom 1.33

transform rotate_6:
    subpixel True
    rotate 5 xanchor 0.5 yanchor 0.5
    ypos 0.5
    zoom 1.2

transform rotate_5:
    subpixel True
    rotate 5 xanchor 0.5 yanchor 0.5
    ypos 0.5
    zoom 1.1

transform center_left:
    yanchor 0.5 ypos 0.5
    xanchor 0.0 xpos 0.0

transform center_right:
    yanchor 0.5 ypos 0.5
    xanchor 1.0 xpos 1.0

transform mid_left_left:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.125

transform mid_left:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.25

transform mid_mid_left:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.375

transform mid_mid_right:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.625

transform mid_right:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.75

transform mid_right_right:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.875

transform mid_center_right:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.75

transform mid_center_left:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.25

transform center_mid_left:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.4

transform center_mid_right:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.8

transform mid_offscreen_right:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 1.0

transform mid_offscreen_left:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos -0.0
    
# i got tired.
# if ALL you need is a simple custom placement, no zoom/motion/effects, just use this please. 
# for compatibility with the existing positions, set anchor to 1.0 - tate
transform manual_pos(x, y, this_anchor = 0):
    xanchor this_anchor
    yanchor this_anchor
    xpos x
    ypos y
    
# another late-night innovation...
# because renpy is stupid you MUST use pixel integer, no float allowed.
# sorry, digi. couldn't get it to work in spite of your help
transform random_pos(xmin, xmax, ymin, ymax, this_anchor):
    xanchor this_anchor
    yanchor this_anchor
    xpos renpy.random.randint(xmin, xmax)
    ypos renpy.random.randint(ymin, ymax)

transform xstretch_in:
    xalign 0.5
    linear 0.5 xsize 1920

transform xstretch_out:
    xalign 0.5
    linear 0.5 xsize 2
    alpha 0.0

transform little_bounce:
    yanchor 1.0
    yzoom 0.95
    ease 0.1 yzoom 1.05
    ease 0.1 yzoom 1

transform t_post_it:
    subpixel True
    xanchor 0.5 yanchor 0.0
    xpos 0.65 ypos 0.025
    zoom 0.3333
    rotate 10

transform t_copguy_frontseat:
    yanchor 1.0 ypos 0.75
    xanchor 0.5 xpos 0.325
    zoom 0.75

transform t_cashier_at_tims:
    yanchor 1.0 ypos 0.80
    xanchor 0.5 xpos 0.725
    zoom 0.6

transform t_arc_at_tims:
    yanchor 1.0 ypos 0.75
    xanchor 0.5 xpos 0.625
    linear 0.5 zoom 0.6

transform t_cs_ltt:
    zoom 0.65
    yanchor 1.0 ypos 0.8
    xanchor 0.0 xpos 0.2

transform t_linus_ltt:
    zoom 0.65
    yanchor 1.0 ypos 0.8
    xanchor 1.0 xpos 0.8

transform t_pepzone1:
    ypos 0.50
    xpos 0.375
    zoom 0.75

transform t_pepzone2:
    ypos 0.33
    xpos 0.375
    zoom 0.75

transform t_gun:
    rotate 4
    yanchor 0.5 ypos 0.555
    xanchor 0 xpos 0.36

transform t_stage_screen_l:
    anchor (0.0, 0.0)
    pos (272, 413)
    zoom 0.15

transform t_stage_screen_c:
    anchor (0.0, 0.0)
    pos (805, 416)
    zoom 0.125

transform t_stage_screen_r:
    anchor (0.0, 0.0)
    pos (1349, 411)
    zoom 0.15

transform t_stagescreen:
    anchor (0.5, 1.0)
    pos (0.5, 4.0)  # Why is this needed? This makes no sense. This should be 1.0

transform t_punchup:
    yanchor 1.0 ypos 0.0
    rotate 0
    linear 1 rotate 960
    
# TODO: make sure this transform exactly matches the rpg engine transform. i don't think i quite nailed it -tate
transform t_fake_rpg_text(x,y,speed = 0.25):
    on show:
        xpos x
        ypos y
        pass
        parallel:
            linear speed ypos (y-0.05)
        parallel:
            ease_expo 0.75 alpha 0.00
        
transform lego_run:
    pos (0.5, 0.5)
    anchor(0.5, 0.5)
    linear 2.0 zoom 5.0 alpha 0.0

transform car_run:
    zoom 0.5
    pos (0.5, 0.5)
    anchor(0.5, 0.5)
    linear 2.0 zoom 2.5

transform typewriter_location:
    pos (0.5, 0.7)
    anchor(0.5, 0.5)
    rotate(-17)

transform midoffscreenright:
    pos(1.0, 0.0)

transform midoffscreenleftspin:
    pos(-1.0, 0.0)
    linear 2 rotate -360

transform offscreenrightspin:
    pos(1.5, 1.0)
    linear 2 rotate 360

transform offscreenleftspin:
    pos(-0.5, 0.5)
    linear 2 rotate 360

transform t_blur_on:
    blur 0.0
    linear 1.0:
        blur 20.0

transform t_blur_off:
    blur 20.0
    linear 1.0:
        blur 0.0

transform t_toby:
    xalign 0.5 yalign 0.5
    alpha 0.0
    linear 0.25:
        alpha 0.75
    linear 0.25:
        alpha 0.0

transform t_lupin_out:
    linear 1.0:
        alpha 0.0
        rotate 2070
        zoom 0.1
        xanchor 0.5 xpos 0.25
        yanchor 0.5 ypos 0.333

transform t_boom:
    on show:
        xalign 0.5 yalign -0.5
        linear 1.0:
            yalign 0.0
    on hide:
        linear 1.0:
            yalign -0.5

transform t_evil_mika:
    zoom 2
    xalign 0.5
    yalign 1.0

transform t_train_scurvy:
    zoom 1.5
    xanchor 0.25
    yanchor 0.335
    ease 2.0 rotate 15
    ease 2.0 rotate -15
    repeat

transform t_people_scurvy:
    zoom 1.0
    xanchor 0.25
    yanchor 0.335
    ease 2.0 rotate 15
    ease 2.0 rotate -15
    repeat

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
define avgn = Character("James Rolfe", callback = char_callback)
define tgt_worker = Character("Target Employee", callback = char_callback)

# DX Digi Character Definitions
define david = Character("David", callback = char_callback)
define george = Character("George", callback = char_callback)
define harold = Character("Harold", callback = char_callback)
define mr_krupp = Character("Mr. Krupp", callback = char_callback)
define weird_al = Character("Weird Al", callback = char_callback)

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

# DX Train Route Character Definitions
define amtrak_conductor = Character("Conductor", callback = renpy.partial(char_callback, name = "amtrak_conductor", beep = "amtrak_conductor"))
define amtrak_npc_1 = Character("Passenger 1", callback = char_callback)
define amtrak_npc_2 = Character("Passenger 2", callback = char_callback)
define amtrak_npc_3 = Character("Passenger 3", callback = char_callback)
define amtrak_stewardess = Character("Stewardess", callback = char_callback)
define lupin = Character("Lupin", callback = renpy.partial(char_callback, name = "lupin", beep = "lupin"))
define lupin_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "lupin"))
define mean_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "mean"))
define zenigata_nobeep = Character("???", callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "zenigata"))
define perfect_tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"), screen = "perfect_tate_text")

# DX Holiday Special Definitions
define santa = Character("Santa Claus", callback = char_callback)

# DX Finale Character Definitions
define perfect_billy = Character("Perfect Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"), screen = "perfect_billy_text")

# DX Albu
define cashier_nobeep = Character("Cashier", callback = renpy.partial(char_callback, name = "cashier", play_beeps = False))
define cs_nobeep = Character("cs188", callback = renpy.partial(char_callback, name = "cs", play_beeps = False))
define crowd_nobeep = Character("Crowd", callback = renpy.partial(char_callback, play_beeps = False))
define daphone = Character("Da Phone", callback = renpy.partial(char_callback, play_beeps = False))
define everyone = Character("Everyone", callback = renpy.partial(char_callback, play_beeps = False))
define hermaphrodite = Character("Hermaphrodite", callback = renpy.partial(char_callback, play_beeps = False))
define marty = Character ("Marty", callback = renpy.partial(char_callback, play_beeps = False))
define zelda = Character("Zelda", callback = renpy.partial(char_callback, play_beeps = False))

# Our Friends! Character Definitions
define addy = Character("Addy", callback = renpy.partial(char_callback, name = "addy", beep = "pak"))
define anne = Character("Anne", callback = char_callback)
define anno = Character("Anno", callback = renpy.partial(char_callback, name = "anno", beep = "anno"))
define arceus = Character("Arceus", callback = renpy.partial(char_callback, name = "arceus", beep = "arc"))
define aria = Character("Aria", callback = renpy.partial(char_callback, name = "aria", beep = "aria"))
define aria_alt = Character("Aria", callback = renpy.partial(char_callback, name = "aria", beep = "aria_alt"))
define blank = Character("Blank", callback = renpy.partial(char_callback, name = "blank", beep = "blank"))
define db = Character("DB05", callback = renpy.partial(char_callback, name = "db", beep = "db05"))
define digi = Character("Digi", callback = renpy.partial(char_callback, name = "digi", beep = "digi"))
define eliza = Character("Elizabeth", callback = char_callback)
define grace = Character("Grace", callback = char_callback)
define iris = Character("Iris", callback = renpy.partial(char_callback, name = "iris", beep = "iris"))
define k17 = Character("K-17", callback = char_callback)
define k22 = Character("K-22", callback = char_callback)
define kitty = Character("Kitty", callback = renpy.partial(char_callback, name = "kitty", beep = "kitty"))
define mean = Character("Mean", callback = renpy.partial(char_callback, name = "mean", beep = "mean"))
define midge = Character("Midge", callback = renpy.partial(char_callback, name = "midge", beep = "midge"))
define mika = Character("Mika", callback = renpy.partial(char_callback, name = "mika", beep = "mika"))
define nova = Character("Nova", callback = renpy.partial(char_callback, name = "nova"))
define pakoo = Character("Pakoo", callback = renpy.partial(char_callback, name = "pakoo", beep = "pak"))
define tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"))

# Character Images
## CS
image cs = "characters/cs/neutral.png"
image cs sil_black = "sil_black:characters/cs/neutral.png"
image cs flipped = "flip:characters/cs/neutral.png"
image cs happy = "characters/cs/happy.png"
image cs happy flipped = "flip:characters/cs/happy.png"
image cs happy dark = "dark:characters/cs/happy.png"
image cs happy dark flipped = "dark:flip:characters/cs/happy.png"
image cs angry = "characters/cs/angry.png"
image cs angry dark = "dark:characters/cs/angry.png"
image cs angry flipped = "flip:characters/cs/angry.png"
image cs angry dark flipped = "dark:flip:characters/cs/angry.png"
image cs worried = "characters/cs/worried.png"
image cs worried flipped = "flip:characters/cs/worried.png"
image cs disappointed = "characters/cs/disappointed.png"
image cs disappointed metal = "characters/cs/disappointedmetal.png"
image cs disappointed metal2 = "characters/cs/disappointedmetal2.png"
image cs disappointed metal3 = "characters/cs/disappointedmetal3.png"
image cs disappointed metal4 = "characters/cs/disappointedmetal4.png"
image cs disappointed flipped = "flip:characters/cs/disappointed.png"
image cs concentrate = "characters/cs/concentrate.png"
image cs concentrate dark = "dark:characters/cs/concentrate.png"
image cs concentrate flipped = "flip:characters/cs/concentrate.png"
image cs dark = "dark:characters/cs/neutral.png"
image cs dark flipped = "dark:flip:characters/cs/neutral.png"
image cs dusk = "dusk:characters/cs/neutral.png"
image cs disappointed dark = "dark:characters/cs/disappointed.png"
image cs disappointed dark flipped = "dark:flip:characters/cs/disappointed.png"
image cs disappointed dusk = "dusk:characters/cs/disappointed.png"
image cs worried dark = "dark:characters/cs/worried.png"
image cs worried dark flipped = "dark:flip:characters/cs/worried.png"
image cs prison = "characters/cs/prison.png"
image cs prison flipped = "flip:characters/cs/prison.png"
image cs disappointed prison = "characters/cs/prison_disappointed.png"
image cs guard = "characters/cs/guard.png"
image cs guard dark = "dark:characters/cs/guard.png"
image cs fakegod = "characters/cs/fake_god.png"
image cs guitar = "characters/cs/guitar.png"
image cs surprised = "characters/cs/surprised.png"
image cs surprised flipped  = "flip:characters/cs/surprised.png"
image cs surprised dark = "dark:characters/cs/surprised.png"
image cs surprised dark flipped = "dark:flip:characters/cs/surprised.png"
image cs scared = "characters/cs/scared.png"
image cs scared flipped = "flip:characters/cs/scared.png"
image cs scared dark = "dark:characters/cs/scared.png"
image cs insane worried = "characters/cs/insane.png"
image cs insane worried flipped = "flip:characters/cs/insane.png"
image cs insane worried dark = "dark:characters/cs/insane.png"
image cs insane worried flipped dark = "dark:flip:characters/cs/insane.png"
image cs insane disappointed = "characters/cs/insane2.png"
image cs insane disappointed dark = "dark:characters/cs/insane2.png"
image cs horse = "characters/cs/horse.png"
image cs horse flipped = "flip:characters/cs/horse.png"
image cs pissed = "characters/cs/pissed.png"
image cs pissed flipped = "flip:characters/cs/pissed.png"
image cs cultist = "characters/cs/robe.png"
image cs disappointed cultist = "characters/cs/disappointedrobe.png"
image cs angry cultist = "characters/cs/angryrobe.png"
image cs cultist flipped = "flip:characters/cs/robe.png"
image cs disappointed cultist flipped = "flip:characters/cs/disappointedrobe.png"
image cs angry cultist flipped = "flip:characters/cs/angryrobe.png"
image cs pencil = "characters/cs/pencil.png"
image cs angry pencil = "characters/cs/pencilangry.png"
image cs disappointed pencil = "characters/cs/pencildisappointed.png"
image cs phone = "characters/cs/phone.png"
image cs phone flipped = "flip:characters/cs/phone.png"
image cs happy phone = "characters/cs/happy_phone.png"
image cs happy phone flipped = "flip:characters/cs/happy_phone.png"
image cs disappointed phone = "characters/cs/disappointed_phone.png"
image cs disappointed phone flipped = "flip:characters/cs/disappointed_phone.png"
image cs worried phone = "characters/cs/worried_phone.png"
image cs worried phone flipped = "flip:characters/cs/worried_phone.png"
image cs angry phone = "characters/cs/angry_phone.png"
image cs angry phone flipped = "flip:characters/cs/angry_phone.png"
image cs scared phone = "characters/cs/scared_phone.png"
image cs scared phone flipped = "flip:characters/cs/scared_phone.png"
image cs surprised phone = "characters/cs/surprised_phone.png"
image cs surprised phone flipped = "flip:characters/cs/surprised_phone.png"
image cs pissed phone = "characters/cs/pissed_phone.png"
image cs pissed phone flipped = "flip:characters/cs/pissed_phone.png"
image cs concentrate phone = "characters/cs/concentrate_phone.png"
image cs concentrate phone flipped = "flip:characters/cs/concentrate_phone.png"
image cs worried punishedgown = "characters/cs/CSnake_Worried_Gown.png"
image cs angry punished = "characters/cs/CSnake_Angry.png"

# CS Misc
image csgod = "characters/csgod.png"
image csgod flipped = "flip:characters/csgod.png"
image csgod_angry = "characters/csgod_angry.png"
image young_cs = "characters/cs_young.png"

## Arc
image arceus = "characters/arc/arceus.png"
image arceus flipped = "flip:characters/arc/arceus.png"
image arceus dirty = "characters/arc/arceusdirty.png"
image arceus dirty flipped = "flip:characters/arc/arceusdirty.png"
image arceus full happy = "characters/arc/happyfull.png"
image arceus full happy flipped = "flip:characters/arc/happyfull.png"
image arceus full = "characters/arc/full.png"
image arceus full flipped = "flip:characters/arc/full.png"
image arceus full angry = "characters/arc/angryfull.png"
image arceus full angry flipped = "flip:characters/arc/angryfull.png"
image arceus angry = "characters/arc/angry.png"
image arceus angry flipped = "flip:characters/arc/angry.png"
image arceus angry dark = "dark:characters/arc/angry.png"
image arceus angry dark flipped = "dark:flip:characters/arc/angry.png"
image arceus guard = "characters/arc/guard.png"
image arceus guard flipped = "flip:characters/arc/guard.png"
image arceus happy = "characters/arc/happy.png"
image arceus happy flipped = "flip:characters/arc/happy.png"
image arceus happy dark = "dark:characters/arc/happy.png"
image arceus happy dark flipped = "dark:flip:characters/arc/happy.png"
image arceus prison = "characters/arc/prison.png"
image arceus prison flipped = "flip:characters/arc/prison.png"
image arceus worried = "characters/arc/worried.png"
image arceus worried flipped = "flip:characters/arc/worried.png"
image arceus dirty worried = "characters/arc/worrieddirty.png"
image arceus dirty worried flipped = "flip:characters/arc/worrieddirty.png"
image arceus worried dark = "dark:characters/arc/worried.png"
image arceus worried dark flipped = "dark:flip:characters/arc/worried.png"
image arceus dark = "dark:characters/arc/arceus.png"
image arceus dark flipped = "dark:flip:characters/arc/arceus.png"
image arceus dusk = "dusk:characters/arc/arceus.png"
image arceus worried dusk = "dusk:characters/arc/worried.png"
image arceus angry dusk = "dusk:characters/arc/angry.png"
image arceus dusk flipped = "dusk:flip:characters/arc/arceus.png"

## Anno
image anno = "characters/anno/anno.png"
image anno prison = "characters/anno/anno_prison.png"
image anno guard = "characters/anno/anno_guard.png"
image anno guard dark = "dark:characters/anno/anno_guard.png"

## Pakoo
image pakoo = "characters/pakoo/pakoo.png"
image pakoo dark = "dark:characters/pakoo/pakoo.png"
image pakoo flipped = "flip:characters/pakoo/pakoo.png"
image pakoo dark flipped = "dark:flip:characters/pakoo/pakoo.png"
image pakoo worried = "characters/pakoo/pakoo_worried.png"
image pakoo worried flipped = "flip:characters/pakoo/pakoo_worried.png"
image pakoo disappointed = "characters/pakoo/pakoo_disappointed.png"
image pakoo disappointed flipped = "flip:characters/pakoo/pakoo_disappointed.png"
image pakoo happy = "characters/pakoo/pakoo_happy.png"
image pakoo happy flipped = "flip:characters/pakoo/pakoo_happy.png"

## Craptop
image craptop blank = "characters/craptop/blank.png"
image craptop car = "characters/craptop/car.png"
image craptop desktop = "characters/craptop/desktop.png"
image craptop discord = "characters/craptop/discord.png"
image craptop edit = "characters/craptop/edit.png"
image craptop error = "characters/craptop/error.png"
image craptop off = "characters/craptop/off.png"
image craptop sad = "characters/craptop/sad.png"
image craptop updating = "characters/craptop/updating.png"
image craptop ytp = "characters/craptop/ytp.png"
image craptop evidence = "characters/craptop/evidence.png"
image craptopreal = "characters/laptop.png"
image craptopsmall = "characters/craptop.png"
image craptopsmall flipped = "flip:characters/craptop.png"

## Tate
image tate = "characters/tate/tatehappy.png"
image tate dark = "dark:characters/tate/tatehappy.png"
image tate flipped = "flip:characters/tate/tatehappy.png"
image tate dark flipped = "dark:flip:characters/tate/tatehappy.png"
image tate srs = "characters/tate/tateserious.png"
image tate srs dark = "dark:characters/tate/tateserious.png"
image tate srs flipped = "flip:characters/tate/tateserious.png"
image tate srs dark flipped = "dark:flip:characters/tate/tateserious.png"
image tate shock = "characters/tate/tateshock.png"
image tate shock dark = "dark:characters/tate/tateshock.png"
image tate shock flipped = "flip:characters/tate/tateshock.png"
image tate shock dark flipped = "dark:flip:characters/tate/tateshock.png"
image tate smug = "characters/tate/tatesmug.png"
image tate smug dark = "dark:characters/tate/tatesmug.png"
image tate smug flipped = "flip:characters/tate/tatesmug.png"
image tate smug dark flipped = "dark:flip:characters/tate/tatesmug.png"
image tate smug sil_white = "sil_white:characters/tate/tatesmug.png"
image tate sheepish = "characters/tate/tatesheepish.png"
image tate sheepish flipped = "flip:characters/tate/tatesheepish.png"
image tate sheepish blush = "characters/tate/tatesheepishblush.png"
image tate sad = "characters/tate/tatesad.png"
image tate sad flipped = "flip:characters/tate/tatesad.png"
image tate sad dark = "dark:characters/tate/tatesad.png"
image tate stare = "characters/tate/tatestare.png"
image tate stare flipped = "flip:characters/tate/tatestare.png"
image tate cry = "characters/tate/tatecry.png"
image tate cry flipped = "flip:characters/tate/tatecry.png"

## Mean (Urchin Form)
image mean = "characters/mean/mean.png"
image mean flipped = "flip:characters/mean/mean.png"
image mean happy = "characters/mean/meanhappy.png"
image mean happy flipped = "flip:characters/mean/meanhappy.png"
image mean happy2 = "characters/mean/meanhappy2.png"
image mean happy2 flipped = "flip:characters/mean/meanhappy2.png"
image mean surprised = "characters/mean/meansurprised.png"
image mean surprised flipped = "flip:characters/mean/meansurprised.png"
image mean ayo = "characters/mean/meanayo.png"
image mean ayo flipped = "flip:characters/mean/meanayo.png"
image mean angry = "characters/mean/meanangry.png"
image mean angry flipped = "flip:characters/mean/meanangry.png"
image mean angry sil_white flipped = "sil_white:flip:characters/mean/meanangry.png"
image mean wat = "characters/mean/meanwat.png"
image mean wat flipped = "flip:characters/mean/meanwat.png"
image mean furious = "characters/mean/meanfurious.png"
image mean furious flipped = "flip:characters/mean/meanfurious.png"
image mean tired = "characters/mean/meantired.png"
image mean tired flipped = "flip:characters/mean/meantired.png"
image mean worried = "characters/mean/meanworried.png"
image mean worried flipped = "flip:characters/mean/meanworried.png"
image mean scared = "characters/mean/meanscared.png"
image mean scared flipped = "flip:characters/mean/meanscared.png"
image mean unamused = "characters/mean/meanunamused.png"
image mean unamused flipped = "flip:characters/mean/meanunamused.png"

## Mean (Human Form)
image mean human = "characters/mean/meanhumanneutral.png"
image mean human flipped = "flip:characters/mean/meanhumanneutral.png"
image mean human dark flipped = "dark:flip:characters/mean/meanhumanneutral.png"
image mean human flipped sil_black = "sil_black:flip:characters/mean/meanhumanneutral.png"
image mean human happy = "characters/mean/meanhumanhappy.png"
image mean human happy flipped = "flip:characters/mean/meanhumanhappy.png"
image mean human annoyed = "characters/mean/meanhumanannoyed.png"
image mean human annoyed flipped = "flip:characters/mean/meanhumanannoyed.png"
image mean human shocked = "characters/mean/meanhumanshocked.png"
image mean human shocked flipped = "flip:characters/mean/meanhumanshocked.png"
image mean human shocked dark flipped = "dark:flip:characters/mean/meanhumanshocked.png"
image mean human angry = "characters/mean/meanhumanangry.png"
image mean human angry flipped = "flip:characters/mean/meanhumanangry.png"
image mean human angry dark flipped = "dark:flip:characters/mean/meanhumanangry.png"

image mean human hat = "characters/mean/meanhumanneutralhat.png"
image mean human hat flipped = "flip:characters/mean/meanhumanneutralhat.png"
image mean human hat dark = "dark:characters/mean/meanhumanneutralhat.png"
image mean human happy hat = "characters/mean/meanhumanhappyhat.png"
image mean human happy hat flipped = "flip:characters/mean/meanhumanhappyhat.png"
image mean human annoyed hat  = "characters/mean/meanhumanannoyedhat.png"
image mean human annoyed hat flipped = "flip:characters/mean/meanhumanannoyedhat.png"
image mean human shocked hat = "characters/mean/meanhumanshockedhat.png"
image mean human shocked hat flipped = "flip:characters/mean/meanhumanshockedhat.png"
image mean human shocked hat dark flipped = "dark:flip:characters/mean/meanhumanshockedhat.png"
image mean human angry hat = "characters/mean/meanhumanangryhat.png"
image mean human angry hat flipped = "flip:characters/mean/meanhumanangryhat.png"
image mean human angry hat dark flipped = "dark:flip:characters/mean/meanhumanangryhat.png"

## Archival
image k174 = "characters/k174.png"
image k174 flipped = "flip:characters/k174.png"
image k199 = "characters/k199.png"
image k199 flipped = "flip:characters/k199.png"
image k207 = "characters/k207.png"
image k207 flipped = "flip:characters/k207.png"
image k207h = "characters/k207h.png"
image k207h flipped = "flip:characters/k207h.png"
image nova_head = "characters/novaedit.png"
image carguya = "characters/carguya.png"
image hart1 = "characters/hart1.png"
image hart2 = "characters/hart2.png"

# HoH SiS 
image rich = "characters/rich.png"
image rich flipped = "flip:characters/rich.png"
image ed = "characters/ed.png"
image ed flipped = "flip:characters/ed.png"
image ed phone = "characters/ed_phone.png"
image wesleytop = "characters/wesleytop.png"
image wesleybottom = "characters/wesleybottom.png"
image wesley = "characters/wesley.png"
image wesley flipped = "flip:characters/wesley.png"
image worker_1 = "characters/worker_corn.png"
image worker_2 = "characters/worker_blank.png"
image worker_3 = "flip:characters/mean/meanhohsis1.png" # It's Mean!
image worker_4 = "characters/worker_eville.png"
image worker_5 = "characters/eddie_down.png"
image worker_5alt = "characters/eddie_up.png"
image worker_6 = "characters/worker_pineapple.png"
image worker_7 = "characters/worker_chicken.png"

# Copguy & Co.
image copguy = "characters/copguy.png"
image copguy flipped = "flip:characters/copguy.png"
image copguy dark = "dark:characters/copguy.png"
image copguy dark flipped = "dark:flip:characters/copguy.png"
image copguy_ai = "characters/ai_cop_guy_full.png"
image copguycrawl = "characters/copguycrawl.png"
image sheriff = "characters/sheriff.png"
image sheriff flipped = "flip:characters/sheriff.png"
image cop = "characters/cop.png"
image cop dark = "dark:characters/cop.png"
image cop_2 = "dark:characters/cop.png"
image guard_soldier = "dark:characters/guard_soldier.png"
image marine = "characters/marine.png"
image big_tank = "characters/abrams.png"
image asylum_worker = "dark:characters/mohs.png"
image copguyexe = "characters/copguyexe.png"
image copguyexe flipped = "flip:characters/copguyexe.png"

# CSB I
image michael = "flip:characters/michael.png"
image phil = "characters/phil.png"
image carguy = "characters/carguy.png"
image carguy flipped = "flip:characters/carguy.png"
image doug = "characters/doug.png"

# LMG & The Fanboys
image linus = "characters/linus.png"
image linus flipped = "flip:characters/linus.png"
image luke = "characters/luke.png"
image luke flipped = "flip:characters/luke.png"
image taran = "characters/taran.png"
image taran flipped = "flip:characters/taran.png"
image taran slack = "characters/taran_slack.png"
image colton = "characters/colton.png"
image nfanboy = "characters/nvidiafanboy.png"
image afanboy = "characters/amdfanboy.png"

# Billy Mays
image billy = "characters/billy.png"
image billy car = "characters/billy/billy_car.png"
image billy car happy = "characters/billy/billy_car_happy.png"
image billy car turn = "characters/billy/billy_car_turn.png"
image billy laser = "characters/BillyMaysWithLaser.png"
image billy dark = "dark:characters/billy.png"

# Cultists
image cultist = "characters/cultist.png"
image cultist gun = "characters/cultistgun.png"
image cultist_2 = "characters/cultist2.png"
image cultist_3 = "characters/cultist2.png"

# Digi
image digi = "characters/digi.png"
image digi dark = "dark:characters/digi.png"
image digi flipped = "flip:characters/digi.png"
image digi dark flipped = "dark:flip:characters/digi.png"

# Aria
image aria = "characters/aria.png"
image aria flipped = "flip:characters/aria.png"
image aria dark = "dark:characters/aria.png"
image aria dark flipped = "dark:flip:characters/aria.png"

# Nova
image nova = "characters/nova.png"
image nova dark = "dark:characters/nova.png"
image nova flipped = "flip:characters/nova.png"
image nova dark flipped = "dark:flip:characters/nova.png"
image nova discord = "characters/nova_discord.png"

# More of our friends!
image kitty = "characters/kitty.png"
image kitty flipped = "flip:characters/kitty.png"
image blank = "characters/blank.png"
image midge = "characters/midge.png"
image mika = "characters/mika.png"
image mika dark = "dark:characters/mika.png"
image db = "characters/db.png"
image db_cooper = "characters/db_coopergame.png"
image ges = "characters/ges.png"

# Unsorted NPCs
image cashier = "characters/cashier.png"
image scott = "characters/scott.png"
image obama = "characters/obama.png"
image discord = "characters/discord.png"
image border_guard = "characters/border_guard.png"
image border_guard dusk = "dusk:characters/border_guard.png"
image benrey = "characters/benrey.png"

# Fired Route
image guest = "characters/guest.png"
image janitor = "characters/janitor.png"
image customer = "characters/customer.png"
image howie = "characters/howie.png"
image howie flipped = "flip:characters/howie.png"

# South Route
image bouncer1 = "characters/bouncer.png"
image bouncer2 = "characters/bouncer.png"
image trailtrash = "characters/trailtrash.png"
image trailtrash_2= "flip:characters/trailtrash.png"
image trailtrash flipped = "flip:characters/trailtrash.png"
image green = "characters/green.png"
image green flipped = "flip:characters/green.png"
image jerma = "characters/jerma.png"
image lego = "characters/lego.png"
image lego eyes = "characters/legoeyes.png"
image tsa = "characters/tsa.png"
image monika = "characters/monika.png"

# East Route
image peppino = "characters/peppino.png"
image peppino2 = "characters/peppino2.png"
image streetguy = "characters/streetguy.png"
image pencilguy = "characters/pencil.png"

# East I-69
image gnome = "characters/gnome.png"
image waitress = "characters/waitress.png"
image terry = "characters/terry.png"
image mettaton = "characters/mettaton.png"

# East I-94
image smiley = "characters/smiley.png"
image mario = "characters/mario.png"
image mario flipped = "flip:characters/mario.png"
image violent_jay = "characters/jay.png"
image shaggy_too_dope = "characters/shaggydope.png"

# England
image gordon = "characters/gordon.png"
image car = "characters/car.png"
image tom = "characters/tom.png"
image james = "characters/james.png"
image jeremy = "characters/jeremy.png"
image hammond = "characters/hammond.png"

# Japan
image scott_pres = "characters/scott_pres.png"
image miku = "characters/miku.png"
image sayori = "characters/sayori.png"

# Sweden
image joel = "characters/joel.png"
image joel flipped = "flip:characters/joel.png"
image ikea_greeter = "characters/ikea_man.png"
image ikea_greeter blahaj = "characters/ikea_man_blahaj.png"
image ikea_greeter flipped = "flip:characters/ikea_man.png"
image swede = "characters/swede.png"
image alien = "characters/alien.png"
image alien dead = "characters/alien_dead.png"
image ikea_worker = "characters/ikea_worker.png"
image pomni = "characters/pomni.png"
image pomni flipped= "flip:characters/pomni.png"
image moomin = "characters/moomin.png"
image moomin = "flip:characters/moomin.png"
image snufkin = "characters/snufkin.png"
image snufkin flipped = "flip:characters/snufkin.png"
image alicia = "characters/alicia.png"
image alicia flipped = "flip:characters/alicia.png"
image witch = "characters/witch.png"
image witch flipped = "flip:characters/witch.png"
image moomin flipped = "flip:characters/moomin.png"
image snufkin flipped = "flip:characters/snufkin.png"
image alicia flipped = "flip:characters/alicia.png"
image witch flipped = "flip:characters/witch.png"
image baumer = "characters/ballmer_cutout.png"
image baumer flipped = "flip:characters/ballmer_cutout.png"

# Background Images
## CSBI
image cs_room = "bg/cs_bedroom1.png"
image cs_room_2 = "bg/cs_bedroom2.png"
image craptop_bg = "bg/craptop_bg.png"
image cs_house = "bg/cs_house.png"
image cs_car = "bg/car_driveway.png"
image cs_car_inside = "bg/car_inside.png"
image walmart_outside = "bg/walmart_outside.png"
image walmart_inside = "bg/walmart_inside.png"
image walmart_aisle = "bg/walmart_shelf.png"
image walmart_register_fg = "bg/walmart_checkout_fg.png"
image walmart_register = "bg/walmart_checkout.png"
image cs_door_closed = "bg/door_closed.png"
image cs_door_open = "bg/door_open.png"
image rosen_abode = "bg/rosenabode.png"
image cs_street = "bg/cs_street.png"
image hoh_outside = "bg/office_outside.png"
image hoh_hq = "bg/office1.png"
image hoh_hq2 = "bg/office2.png"
image hoh_hq3 = "bg/office3.png"
image hoh_hq4 = "bg/office4.png"
image hoh_hq5 = "bg/office5.png"
image hoh_elevator = "bg/elevator.png"

## Generated images for CSBI
image spent_11_88 = Text("{size=50}{color=#369100}-$11.88", text_align=0.5)
image spent_bits = Text("{image=bits.png} {size=50}{color=#BD62FF}-200,000", text_align=0.5)
# this bit is so stupid - tate
image speedrun_genergy_cost = Text("{size=50}{color=#369100}$2.50", text_align=0.5)
image speedrun_pringles_cost = Text("{size=50}{color=#369100}$5.83", text_align=0.5)
image speedrun_tax_cost = Text("{size=50}{color=#FFFF00}Taxed! 8.875%", text_align=0.5)

## CSBII
image helipad = "bg/helipad.png"
image jail_inside = "bg/jail_inside.png"
image jail_cell = "bg/jail_cell.png"
image border = "bg/canadian_border.png"
image outside_tim_hortons = "bg/outside_tim_hortons.png"
image inside_tim_hortons_fg = "bg/inside_tim_hortons_fg.png"
image inside_tim_hortons = "bg/inside_tim_hortons.png"
image inside_tim_hortons_2 = "bg/inside_tim_hortons_2.png"
image tunnel = "bg/tunnel.png"
image canada = "bg/canada.png"
image flag = "bg/americanflag.png"
image outside_ltt = "bg/linus_office_outside.png"
image inside_ltt = "bg/linus_hallway.png"
image alley = "bg/alley.png"
image question = "bg/police_interrogation.png"
image asylum = "bg/asylum2.png"

## CSBIII Chapter 1
image csdesk = "bg/cs_desk.png"
image csvideo = "bg/csvideo.png"
image setup = "bg/linus_setup.png"
image loffice  = "bg/the_linus_group.png"
image ltt_bg = "bg/ltt_bg.png"
image ltt_fg = "bg/ltt_fg.png"
image frontdoor = "bg/linus_frontdoor.png"
image road_to_canada = "bg/road_to_canada.png"
image border_dusk = "bg/canadian_border_night.png"
image sheriff_office = "bg/sheriffoffice.png"
image washington_road = "bg/washingtonroad.png"
image washington_road day = "bg/washingtonroadday.png"
image washington_road dusk = "bg/washingtonroaddusk.png"
image washington_road morning = "bg/washingtonroadmorning.png"
image copcar = "bg/copcar.png"
image copcar_mask = "bg/copcar_mask.png"
image microcenter = "bg/microcenter.png"
image microinside = "bg/inside_store.png"
image cashzone = "bg/cashzone.png"
image cashzone_foreground = "bg/cashzone_fore.png"
image cpuaisle = "bg/cpuaisle.png"
image gpuaisle = "bg/gpuaisle.png"
image gpuaisle2 = "bg/gpuaisle2.png"
image testing_main = "bg/testing_main.png"
image testing_front = "bg/testing_front.png"
image course_1 = "bg/course_1.png"
image course_2 = "bg/course_2.png"
image course_3 = "bg/course_3.png"
image canada_block = "bg/canada_block.png"
image dealership = "bg/dealership.png"
image dealer_cars = "bg/dealer_cars.png"
image flintcar_outside = "bg/flintcaroutside.png"
image flintcar_fg = "bg/flintcar_fg.png"
image car_inside_fg = "bg/car_inside_fg.png"
image joj_charger_fg = "bg/joj_charger_fg.png"
image comments = "bg/comments.png"
image hospital_room = "bg/hospital_room.png"
image hospital_reception = "bg/hospital_reception.png"
image ticket_counter = "bg/ticket_counter.png"
image backseat = "bg/backseat.png"

# Fired route
image hotel_lobby = "bg/hotel_lobby.png"
image hotel_room = "bg/hotel_room.png"
image hotel_breakfast = "bg/hotel_breakfast.png"
image hotel_guitar_hero = "bg/hotel_guitar_hero.png"
image hotel_door = "bg/hotel_door_back.png"
image hotel_hall = "bg/hotel_hallway.png"
image mcdonalds_inside = "bg/mcdonalds_interior.png"
image ltx = "bg/ltx.png"
image ltx_stage = "bg/ltx_stage.png"
image in_limo = "bg/in_limo.png"
image tour_bus_inside = "bg/inside_tour_bus.png"
image big_stage = "bg/big_stage.png"
image stage2 = "bg/stage_2.png"
image cs_door_outside = "bg/cs_door_outside.png"
image manitoba_street = "bg/manitoba_street.png"
image shoe_store = "bg/shoe_store.png"

## CSBIII Chapter 2
image washington_road day = "bg/washingtonroadday.png"
image washington_road dusk = "bg/washingtonroaddusk.png"
image washington_road morning = "bg/washingtonroadmorning.png"
image town = "bg/washingtontown.png"
image gasinside = "bg/gas_station_inside.png"
image gasoutside = "bg/gas_station.png"
image carback1 = "bg/billycarback1.png"
image hardwareinside = "bg/inside_hardware.png"
image hardwareoutside = "bg/outside_hardware.png"
image cultforest = "bg/cultforest.png"
image mcdonalds = "bg/mcdonalds_drivethru.png"
image mcdees = "bg/mcdonalds_outside.png"
image rushmore = "bg/mtrushmore.png"
image csmore = "bg/mtcsmore.png"
image omaha = "bg/omaha.png"
image alleyway = "bg/alleyway.png"
image peppinopizzabg = "bg/peppino_inside_bg.png"
image peppinopizzafg = "bg/peppino_inside_fg.png"
image wozniaktroubles = "bg/scottwozprotest.png"
image cshouse_vaporized = "bg/cs_house_vaporized.png"
image cscar1 = "bg/cscar1.png"
image cscar1arc = "bg/cscar1arc.png"
image cscar2 = "bg/cscar2.png"
image utah = "bg/utah.png"
image utahsign = "bg/utahsign.png"
image utahnight = "bg/utahnight.png"
image pizzaplace = "bg/pizzaplace.png"
image legodoor = "bg/legoplace.png"
image legodooropen = "bg/legoplaceopen.png"
image legostage = "bg/legostage.png"
image vegas = "bg/vegas.png"
image strip = "bg/strip.png"
image slots = "bg/slots.png"
image tablegames = "bg/tablegames.png"
image pokertable = "bg/pokertable.png"
image luigi1 = "bg/luigi1.png"
image luigi2 = "bg/luigi2.png"
image vegasbathroom = "bg/vegasbathroom.png"
image backroomcasino = "bg/backroomcasino.png"
image outsafe = "bg/outsafe.png"
image outsafeopen = "bg/outsafeopen.png"
image insafe = "bg/insafe.png"
image carpark = "bg/carpark.png"
image casino1 = "bg/casino1.png"
image fazhall = "bg/fazhall.png"
image fazlobby = "bg/fazlobby.png"
image fazplace = "bg/fazplace.png"
image airplane_seats = "bg/airplane_seats.png"
image airport_interior = "bg/airport_interior.png"
image airport_seats = "bg/airport_seats.png"
image airport_tsa = "bg/airport_tsa.png"
image airport_inside = "bg/inside_airport.png"
image old_house_outside = "bg/small_house_old.png"
image old_house_inside = "bg/inside_house_old.png"
image cc_parking_lot = "bg/convention_center_outside.png"
image cc_lobby = "bg/convention_center_lobby.png"
image cc_entrance = "bg/convention_center_entrance.png"
image cc_crowd = "bg/convention_center_crowd.png"
image cc_stage = "bg/convention_center_stage.png"
image cc_backstage = "bg/convention_center_backstage.png"
image billboard = "bg/billboard.png"
image texas = "bg/texas.png"
image tvbilly = "bg/tv_billy.png"
image jeep_inside_fg = "bg/jeep_inside_fg.png"
image dinerinside = "bg/dinerinside.png"
image aria_car_fg = "bg/aria_car_fg.png"
image aria_room = "bg/aria_apartment.png"
image aria_apartment_outside = "bg/aria_apartment_outside.png"
image cs_somewhere = "bg/cs_somewhere.png"
image dineroutside = "bg/dineroutside.png"
image battle_block_without_theater = "bg/battle_block_without_theater.png"
image final_destination = "bg/final_destination.png"
image police_car_fg = "bg/police_car_fg.png"
image war_torn_1 = "bg/mom_counted_to_0.png"
image war_torn_2 = "bg/war_torn_2.png"
image war_torn_3 = "bg/war_torn_3.png"
image war_torn_4 = "bg/war_torn_4.png"
image war_torn_5 = "bg/war_torn_5.png"
image car_insidearc_fg = "bg/car_insidearc_fg.png"
image car_insidearc_fg flipped = "flip:bg/car_insidearc_fg.png"
image joj_chargerarc_fg = "bg/joj_chargerarc_fg.png"
image gas_station_2 = "bg/gas_station_2.png"
image traffic = "bg/traffic_jam_bad_img.png"
image white_bg = "bg/white.png"
image parking_lot = "bg/parking_lot.png"
image path_entrance = "bg/path_entrance.png"
image path_forest = "bg/path_forest.png"
image creepy_path = "bg/creepy_path.png"
image creepy_path_2 = "bg/creepy_path_2.png"
image creepy_path_3 = "bg/creepy_path_3.png"
image creepy_path_4 = "bg/michigan_creepy_forest.png"
image creepy_path_fairy = "bg/creepy_path_fairy.png"
image creepy_path_exit = "bg/michigan_forest_bridge.png"
image cafe_entrance = "bg/east_cafe_interior.png"
image cafe_sitting = "bg/cafe_sitting.png"
image cafe_sitting_2 = "bg/cafe_sitting_2.png"
image trafficjam = "bg/trafficjam.png"
image east_cafe = "bg/east_cafe.png"
image doll_eye_tree = "bg/doll_eye_tree.png"
image mario_inside = "bg/mario_inside.png"
image mario_inside2 = "bg/mario_inside2.png"
image mario_outside = "bg/mario_outside.png"
image gnome_forest = "bg/gnome_forest.png"
image forest_clearing_magic = "bg/forest_clearing_magic.png"
image bronsoncrash = "bg/bronsoncrash.png"

## Country Route
image britport = "bg/britport.png"
image embassy = "bg/outside_embassy.png"
image uk_street = "bg/uk_street.png"
image kitty_house = "bg/kitty_house.png"
image kitty_room = "bg/kitty_room.png"
image dining_room = "bg/diningroom.png"
image hell_outside = "bg/hell_outside.png"
image dominos = "bg/dominos.png"
image dominos_counter = "bg/dominos_counter.png"
image ceo_office = "bg/ceo_office.png"
image japanese_street = "bg/japanese_street.png"
image front_desk = "bg/front_desk.png"
image hell_kitchen = "bg/hell_kitchen.png"
image top_gear_track = "bg/top_gear_track.png"
image tom_house = "bg/tom_house.png"
image tom_road = "bg/tom_road.png"
image tokyo_street = "bg/tokyo_street.png"
image tokyo_airport = "bg/tokyo_airport.png"
image game_store_back = "bg/game_store_back.png"
image game_store_front = "bg/game_store_front.png"
image tokyo_street_2 = "bg/tokyo_street_2.png"
image tokyo_street_night = "bg/tokyo_street_night.png"
image karaoke_bar_inside = "bg/karaoke_bar_inside.png"
image karaoke_bar_outside = "bg/karaoke_bar_outside.png"
image ceo_office_2 = "bg/ceo_office_2.png"
image front_desk_2 = "bg/front_desk_2.png"
image talking_head = "bg/talking_head.png"
image stockholm = "bg/stockholm.png"
image bus_zone = "bg/bus_zone.png"
image bus_map = "bg/bus_map.png"
image bus_seat = "bg/bus_seat.png"
image ikea_outside = "bg/ikea_outside.png"
image ikea_inside = "bg/ikea_inside.png"
image joel_house = "bg/joel_house.png"
image joel_computer = "bg/joel_computer.png"
image joel_outside = "bg/joel_outside.png"
image joel_dining = "bg/joel_dining.png"
image food_court = "bg/food_court.png"
image eating_food = "bg/eating_food.png"
image home_decor = "bg/home_decor.png"
image toilet_zone = "bg/toilet_zone.png"
image plushie_zone = "bg/plushie_zone.png"
image eating_food_2 = "bg/eating_food_2.png"
image dumpster = "bg/dumpster.png"
image moomin_zone1 = "bg/moomin_zone1.png"
image moomin_zone2 = "bg/moomin_zone2.png"
image moomin_zone3 = "bg/moomin_zone3.png"
image moomin_zone3b = "bg/moomin_zone3b.png"
image moomin_zone4 = "bg/moomin_zone4.png"
image moomin_zone5 = "bg/moomin_zone5.png"
image waddle_zone = "bg/waddle_zone.png"

## AI Ending
image park1 = "bg/ai/amusementpark1.png"
image park2 = "bg/ai/amusementpark2.png"
image carousel = "bg/ai/carousel.png"
image endingai = "bg/ai/cs_arceus.png"
image entertunnel = "bg/ai/entrancetotunnel.png"
image linusmedia = "bg/ai/linusmedia.png"
image secrettunnel = "bg/ai/secret_tunnel.png"
image hairdryercoolingsystem = "bg/ai/hairdryercoolingsystem.png"
image tempsdown = "bg/ai/tempsdown.png"

## Archival
image car_old = "bg/car_old.png"
image car_inside_old = "bg/car_inside_old.png"
image bedroom_old = "bg/cs_bedroom.png"
image door_old = "bg/door_open_old.png"
image csmart_old = "bg/csmart.png"
image craptop_old = "bg/craptop_old.png"
image falling = "secret/falling_apart.png"
image archival_1 = "bg/archival/archival_1.png"
image archival_2 = "bg/archival/archival_2.png"
image archival_3 = "bg/archival/archival_3.png"
image archival_4 = "bg/archival/archival_4.png"
image archival_5 = "bg/archival/archival_5.png"
image archival_6 = "bg/archival/archival_6.png"
image archival_7 = "bg/archival/archival_7.png"
image archival_8 = "bg/archival/archival_8.png"
image archival_9 = "bg/archival/archival_9.png"
image archival_10 = "bg/archival/archival_10.png"
image archival_11 = "bg/archival/archival_11.png"
image archival_9a = "bg/archival/archival_9a.png"
image archival_10a = "bg/archival/archival_10a.png"
image archival_11a = "bg/archival/archival_11a.png"
image archival_12 = "bg/archival/archival_12.png"
image archival_13 = "bg/archival/archival_13.png"
image archival_14 = "bg/archival/archival_14.png"
image archival_15 = "bg/archival/archival_15.png"
image archival_16 = "bg/archival/archival_16.png"
image archival_17 = "bg/archival/archival_17.png"
image archival_18 = "bg/archival/archival_18.png"
image archival_19 = "bg/archival/archival_19.png"
image white_vignette = "bg/archival/white_vignette.png"

# Back to the future: CS edition backgrounds
image cs_room_cars = "bg/cs_bedroom_cars.png"
image wis_forest = "bg/wis_forest.png"
image roombacks = "bg/roombacks.png"
image backrooms = "bg/backrooms.png"
image hobbytown = "bg/oshkosh.png"
image pencilroom = "bg/pencilroom.png"
image pencilroomblur = "bg/pencilroomblur.png"
image cult_con = "bg/cult_con.png"
image blue_branch = "bg/bluebranch.png"
image renault_inside = "bg/renault_inside.png"
image cult_zone1 = "bg/cultzone1.png"
image conferencetv = "bg/conferencetv.png"

# Back to the future: CS edition characters
image renovator = "characters/renovator.png"
image shadowman = "characters/shadowman.png"
image pencilcashier = "characters/pencilcashier.png"
image cruise = "characters/cruise.png"
image cruise flipped = "flip:characters/cruise.png"
image priest = "characters/priest.png"
image priest flipped = "flip:characters/priest.png"
image lunatic_cultist = "characters/lunatic_cultist.png"
image lunatic_cultist flipped = "flip:characters/lunatic_cultist.png"

# Back to the future: CS edition generated assets
image after_true_title = Text("{size=+196}Spring 202X", text_align=0.5)

# CS Holiday Special BGs
image snowed_in = "bg/snowed_in.png"
image cs_kitchen = "bg/cs_kitchen.png"
image cs_kitchen_fg = "bg/cs_kitchen_fg.png"
image cs_kitchen_off = "bg/cs_kitchen_off.png"
image cs_kitchen_fg_off = "bg/cs_kitchen_fg_off.png"
image cs_basement = "bg/cs_basement.png"
image tgt_checkerror = "bg/tgt_checkerror.png"
image tgt_checkout = "bg/tgt_checkout.png"
image tgt_inside = "bg/tgt_inside.png"
image tgt_line = "bg/tgt_line.png"
image tgt_outside = "bg/tgt_outside.png"
image tgt_shelf = "bg/tgt_shelf.png"
image cs_house_snow = "bg/cs_house_snow.png"
image cs_house_snowed_in = "bg/cs_house_snowed_in.png"
image cs_house_night = "bg/cs_house_night.png"
image cs_house_snow_night = "bg/cs_house_snow_night.png"
image cs_house_night_dtree = "bg/cs_house_night_dtree.png"

# CS wacky Kuwait Adventures: Mika Edition (Deluxe Content [With Funky Kong {And Dante from Devil may Cry}])
image kuwait_lieutenant_snow = "characters/kuwait_lieutenant_snow.png"
image kuwait_nurse_1 = "characters/k_nurse.png"
image kuwait_doctor_1 = "characters/k_doctor.png"
image RCOMEM = "characters/RCOMEM.png"
# BGs
image kuwait_city = "bg/kuwait_city.png"
image kuwait_explosion = "bg/kuwait_explosion.png"
image kuwait_hospital_inside = "bg/kuwait_hospital_inside.png"
image kuwait_hospital_corridor = "bg/kuwait_hospital_corridor.png"
image kuwait_islandbase_leaders = "bg/kuwait_islandbase_leaders.png"
image kuwait_hallway = "bg/kuwait_hallway.png"
image kuwait_island_outside = "bg/kuwait_island_outside.png"
# Main locations
image al_abdally = "bg/kuwait/al_abdally.png"
image al_wafra = "bg/kuwait/al_wafra.png"
image bayan_water = "bg/kuwait/bayan_water.png"
image boubyan_island = "bg/kuwait/boubyan_island.png"
image burgan_oil = "bg/kuwait/burgan_oil.png"
image hawally = "bg/kuwait/hawally.png"
image icarus = "bg/kuwait/icarus.png"
image jahra_industrial = "bg/kuwait/jahra_industrial.png"
image khiran_camp = "bg/kuwait/khiran_camp.png"
image kubar_island = "bg/kuwait/kubar_island.png"
image kuwait_cityu = "bg/kuwait/kuwait_cityu.png"
image mutla_ridge = "bg/kuwait/mutla_ridge.png"
image salmiya = "bg/kuwait/salmiya.png"
image saqr_airbase = "bg/kuwait/saqr_airbase.png"
image sharq = "bg/kuwait/sharq.png"
image sulaibiya = "bg/kuwait/sulaibiya.png"
image um_al_maradim = "bg/kuwait/um_al_maradim.png"
image um_al_namil = "bg/kuwait/um_al_namil.png"
#Sub locations
image abdally_1 = "bg/kuwait/abdally_1.png"
image abdally_2 = "bg/kuwait/abdally_2.png"
image abdally_3 = "bg/kuwait/abdally_3.png"
image bayan_1 = "bg/kuwait/bayan_1.png"
image burgan_1 = "bg/kuwait/burgan_1.png"
image burgan_2 = "bg/kuwait/burgan_2.png"
image hawally_1 = "bg/kuwait/hawally_1.png"
image hawally_2 = "bg/kuwait/hawally_2.png"
image hawally_3 = "bg/kuwait/hawally_3.png"
image hawally_4 = "bg/kuwait/hawally_4.png"
image icarus_1 = "bg/kuwait/icarus_1.png"
image icarus_2 = "bg/kuwait/icarus_2.png"
image icarus_3 = "bg/kuwait/icarus_3.png"
image jahra_1 = "bg/kuwait/jahra_1.png"
image jahra_2 = "bg/kuwait/jahra_2.png"
image khiran_1 = "bg/kuwait/khiran_1.png"
image khiran_2 = "bg/kuwait/khiran_2.png"
image khiran_3 = "bg/kuwait/khiran_3.png"
image kubar_1 = "bg/kuwait/kubar_1.png"
image maradim_1 = "bg/kuwait/maradim_1.png"
image maradim_2 = "bg/kuwait/maradim_2.png"
image city_1 = "bg/kuwait/mirai_1.png"
image city_2 = "bg/kuwait/mirai_2.png"
image city_3 = "bg/kuwait/mirai_3.png"
image city_4 = "bg/kuwait/mirai_4.png"
image city_5 = "bg/kuwait/mirai_5.png"
image city_6 = "bg/kuwait/mirai_6.png"
image city_7 = "bg/kuwait/mirai_7.png"
image salmiya_1 = "bg/kuwait/salmiya_1.png"
image salmiya_2 = "bg/kuwait/salmiya_2.png"
image salmiya_3 = "bg/kuwait/salmiya_3.png"
image salmiya_4 = "bg/kuwait/salmiya_4.png"
image saqr_1 = "bg/kuwait/saqr_1.png"
image saqr_2 = "bg/kuwait/saqr_2.png"
image saqr_3 = "bg/kuwait/saqr_3.png"
image wafra_1 = "bg/kuwait/wafra_1.png"
image wafra_2 = "bg/kuwait/wafra_2.png"
image wafra_3 = "bg/kuwait/wafra_3.png"
image outside_survivor = "bg/kuwait/outside_survivor.png"
image inside_survivor = "bg/kuwait/inside_survivor.png"

# Misc.
image game_menu = "gui/game_menu.png"
image black = "bg/black.png"
image green_screen = "bg/green.png"
image michael_calendar = "bg/michael_calendar.png"

# DX Train Route
image kingman_exterior = "bg/train/kingman_exterior.png"
image kingman_interior = "bg/train/kingman_interior.png"
image kingman_museum_1 = "bg/train/kingman_museum_1.png"
image kingman_museum_2 = "bg/train/kingman_museum_2.png"
image kingman_museum_3 = "bg/train/kingman_museum_3.png"
image kingman_platform_1 = "bg/train/kingman_platform_1.png"
image kingman_platform_2 = "bg/train/kingman_platform_2.png"
image kingman_train_arrive = "bg/train/kingman_train_arrive.png"
image amtrak_arrive_close = "bg/train/amtrak_arrive_close.png"
image amtrak_sleeper_corridor = "bg/train/amtrak_sleeper_corridor.png"
image amtrak_sleeper_interior_day = "bg/train/amtrak_sleeper_interior.png"
image amtrak_sleeper_interior_night = "dark:bg/train/amtrak_sleeper_interior.png"
image amtrak_dining_car = "bg/train/amtrak_dining_car.png"
image amtrak_dining_table = "bg/train/amtrak_dining_table.png"
image moynihan_interior = "bg/train/moynihan_interior.png"
image amtrak_cab = "bg/train/amtrak_cab.png"
image amtrak_sleeper_open_bg = "bg/train/amtrak_sleeper_open_bg.png" #these two images are bigger on purpose
image amtrak_sleeper_open_fg = "bg/train/amtrak_sleeper_open_fg.png" #remastering is encouraged but don't change size unless you must
image amtrak_coach_1 = "bg/train/amtrak_coach_1.png"
image amtrak_coach_2 = "bg/train/amtrak_coach_2.png"
image amtrak_baggage = "bg/train/amtrak_baggage.png"
image amtrak_top = "dark:bg/train/amtrak_top.png"
image amtrak_top sil_black = "sil_black:bg/train/amtrak_top.png"
image sepia_zoom = "bg/train/sepia_zoom.png"
image hutchinson_stn = "dark:bg/train/hutchinson_stn.png"
image hutchinson_stn_lights = "bg/train/hutchinson_stn_lights.png"
image lupin_escape_1 = "dark:bg/train/lupin_escape_1.png"
image lupin_escape_2 = "dark:bg/train/lupin_escape_2.png"
image amtrak_dining_day = "bg/train/amtrak_dining_day.png"

# Train Route NPCs
image amtrak_conductor = "characters/amtrak_conductor.png"
image amtrak_conductor flipped = "flip:characters/amtrak_conductor.png"
image amtrak_conductor dark = "dark:characters/amtrak_conductor.png"
image amtrak_stewardess = "characters/amtrak_stewardess.png"
image amtrak_stewardess flipped = "flip:characters/amtrak_stewardess.png"

image lupin run = "characters/lupin/lupin_run.png"
image lupin run flipped = "flip:characters/lupin/lupin_run.png"
image lupin run hat = "characters/lupin/lupin_run_hat.png"
image lupin run hat flipped = "flip:characters/lupin/lupin_run_hat.png"
image lupin run hat dark = "dark:characters/lupin/lupin_run_hat.png"
image lupin run hat dark flipped = "dark:flip:characters/lupin/lupin_run_hat.png"
image lupin stand = "characters/lupin/lupin_stand.png"
image lupin stand flipped = "flip:characters/lupin/lupin_stand.png"
image lupin stand dark = "dark:characters/lupin/lupin_stand.png"
image lupin stand hat = "characters/lupin/lupin_stand_hat.png"
image lupin stand hat flipped = "flip:characters/lupin/lupin_stand_hat.png"
image lupin stand hat dark = "dark:characters/lupin/lupin_stand_hat.png"
image lupin stand hat dark flipped = "dark:flip:characters/lupin/lupin_stand_hat.png"

image zenigata = "characters/zenigata.png"
image zenigata dark = "dark:characters/zenigata.png"
image zenigata dark flipped = "dark:flip:characters/zenigata.png"
image zenigata car dark = "dark:characters/zenigata_car.png"

# Train Route Tate EX extra images
image tate_falling = "secret/pt/tate_falling.png"
image tate_fallen_1 = "secret/pt/tate_fallen_1.png"
image tate_fallen_2 = "secret/pt/tate_fallen_2.png"
image tate_fallen_3 = "secret/pt/tate_fallen_3.png"
image tate_fallen_4 = "secret/pt/tate_fallen_4.png"
image tate_fallen_5 = "secret/pt/tate_fallen_5.png"
image yeetable_textbox = "/secret/pt/yeetable_textbox.png"

# Train Route generated images
image fake_rpg_miss = Text("{size=50}{color=#FFAAAA}Miss!", text_align=0.5)
image oof_45 = Text("{size=50}{color=#FFEE00}4'5\"", text_align=0.5)
image oof_54 = Text("{size=50}{color=#CE256E}5'4\"", text_align=0.5)
image oof_52 = Text("{size=50}{color=#233260}5'2\"", text_align=0.5)
image spent_19_95 = Text("{size=50}{color=#369100}-$19.95", text_align=0.5)
# TODO: this sucks
image petal1 = SnowBlossom("petal1.png", count = 50, fast = True)
image petal2 = SnowBlossom("petal2.png", count = 50, fast = True)

# DX Digi Backgrounds
image classroom = "secret/up/classroom.png"
image broom_closet = "secret/up/broom_closet.png"

# DX Digi Characters
image weird_al = "secret/up/weird_al.png"
image cpt_underpants = "secret/up/cpt_underpants.png"
image david = "secret/up/david.png"
image george = "secret/up/george.png"
image harold = "secret/up/harold.png"
image mr_krupp = "secret/up/mr_krupp.png"
image mr_krupp grin = "secret/up/mr_krupp_grin.png"

#DX Holiday Special Misc.
image smoke = SnowBlossom("smoke.png", count = 400, fast = False, xspeed = (0,0), yspeed = (0, -100), border = 32)
image bigsmoke = SnowBlossom("bigsmoke.png", count = 200, fast = True, xspeed = (0,0), yspeed = (0, -50), border = 256)
image snow1 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (20000, 100))
image snow2 = SnowBlossom("snow1.png", count = 200, fast = False, xspeed = (1000, 100))
image snow3 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (2000, 100))
image snow4 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (4000, 100))
image snow5 = SnowBlossom("snow1.png", count = 200, fast = False, xspeed = (2000, 100))
image snow6 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (3000, 100))
image snow_wind = SnowBlossom("snow_wind.png", count = 50, fast = True, xspeed = (500, 0), border = 4000, horizontal = True)

# Static Images
image amtrak_dining_food = "food.png" 
image amtrak_dining_pancake = "pancake.png"
image arc_laptop = "arc_laptop.png"
image bag = "bodybag.png"
image bag flipped = "flip:bodybag.png"
image bear = "bear.png"
image billy_car = "billy_car.png"
image boom = "secret/boom_mic.png"
image brooch = "brooch.png"
image cards1 = "cards1.png"
image cards2 = "cards2.png"
image cards3 = "cards3.png"
image cards4 = "cards4.png"
image cards5 = "cards5.png"
image case = "briefcase.png"
image case flipped = "flip:briefcase.png"
image cheetos = "cheetos.png"
image chopper_ladder = "chopper_ladder.png"
image chopper_ladder dark = "dark:chopper_ladder.png"
image chopper_sil = "chopper_sil.png"
image colorbars = "colorbars.png"
image con_screen = "bg/con_screen.png"
image cool_crab = "cool_crab.png"
image cool_crab dusk = "dusk:cool_crab.png"
image cop_car = "cop_car.png"
image cop_car dark = "dark:cop_car.png"
image crt_magnet = "crt_magnet.png"
image cs_phone = "cs_phone.png"
image cs_wallet = "cs_wallet.png"
image cswanted = "wanted_poster.png"
image dog = "dog.png"
image donut_1 = "donut_1.png"
image donut_2 = "donut_2.png"
image donut_3 = "donut_3.png"
image dookie_milk_jar = "secret/up/dookie_milk_jar.png"
image drill = "drillymays.png"
image drillbreak = "drillymaysfuck.png"
image flexcake = "flexcake.png"
image gamebarrel = "secret/up/gamebarrel.png"
image genergy = "genergy.png"
image gleam = "gleam.png"
image hair_dryer = "hair_dryer.png"
image hold_it = "hold_it.png"
image horse_mask = "horse_mask.png"
image laser_beam = "laser_beam.png"
image lego_jail = "lego_jail.png"
image lego_jail dark = "dark:lego_jail.png"
image letterbox1 = "letterbox.png"
image letterbox2 = "letterbox.png"
image letterbox3 = "letterbox_screen.png"
image linus_box = "linus_box.png"
image ltt_bottle = "ltt_bottle.png"
image m4 = "m4.png"
image m4 fire = "m4fire.png"
image m4 fire flipped = "flip:m4fire.png"
image m4 flipped = "flip:m4.png"
image mean_hat = "mean_hat.png"
image objection = "objection.png"
image oldgame = "oldgame.png"
image onscreen_sharpener = "pencilsharpener.png"
image paper = "paper.png"
image passportdigi = "passportdigi.png"
image pig = "pig.png"
image pipe_gun = "pipe_gun.png"
image pipe_gun flipped = "flip:pipe_gun.png"
image post_it = "post-it.png"
image post_it2 = "secret/post-it2.png"
image pot = "pot.png"
image pot_beam = "pot_beam.png"
image pot_lift = "pot_lift.png"
image pot_sunken = "pot_sunken.png"
image pringles = "pringles.png"
image renault = "renault.png"
image rosen_phone = "rosen_phone.png"
image sansbrick = "sansbrick.png"
image slime16 = "secret/up/slime16.png"
image slime16 fire = "secret/up/slime16_fire.png"
image scott_border = "scott_border.png"
image script = "secret/script.png"
image spoon = "spoon.png"
image switch = "switch.png"
image tate_phone = "tate_phone.png"
image tbc = "tbc.png"
image tims_dozen = "tims_dozen.png"
image toby = "secret/toby.png"
image toxic_mikas = "secret/up/toxic_mikas.png"
image walkie = "walkie.png"
image walkie dark = "dark:walkie.png"
image walmart_bag = "walmart_bag.png"
image watch = "watch.png"
image ytx = Transform("ytx.png", zoom = 0.333)
image ytx_drive = "ytx_drive.png"
image map_kuwait = "gui/map_kuwait.png"

# Movies
image car background = Movie(play="movies/car_background.webm")
image car background night = Movie(play="movies/car_background_night.webm")
image car plains = Movie(play="movies/car_plains.webm")
image car plains night = Movie(play="movies/car_plains_night.webm")
image tvcar = Movie(play="movies/0001.webm")
image drive_night = Movie(play="movies/car_drive_night.webm")
image drive_day = Movie(play="movies/car_drive_day.webm")
image csb1tube = Movie(play="movies/csb1.webm")
image train_start = Movie(play="movies/train_start.webm")
image train_in_tunnel = Movie(play="movies/train_in_tunnel.webm")
image train_outside_tunnel = Movie(play="movies/train_outside_tunnel.webm")
image train_loop = Movie(play="movies/train_loop.webm")
image the_tram = Movie(play="movies/the_tram.webm")
image sign_closeup = Movie(play="movies/sign_closeup.webm")
image karaoke = Transform(Movie(play = "movies/karaoke.webm", side_mask = True), zoom = 1.5)
image bad_end_screen = Transform(Movie(play = "movies/bad_ending.webm", side_mask = True, loop=False, image="images/fail_end.png"), size=(1920,1080))
image bronson_hell = Movie(play="movies/bronsonhell.webm")
image fun_cs_house = Movie(play="movies/funvaluecshouse.webm")
image fun_hoh_sis = Movie(play="movies/funvaluehohsis.webm")
image train_brake = Movie(play="movies/trainscreech.webm")

# Movie Cutscenes
define anno_bl = "movies/anno.webm"
define blank_bl = "movies/blank.webm"
define db_bl = "movies/db.webm"
define midge_bl = "movies/midge.webm"
define woc = "movies/woc.webm"
define where = "movies/wherearetheynow.webm"
define creditsm = "movies/credits.webm"
define archival_end = "movies/archival_end.webm"
define error_cutscene = "movies/error_cutscene.webm"
define good_ytp = "movies/good_cs_ytp.webm"
define bad_ytp = "movies/mymovie_cs.webm"
define hoh_repair = "movies/hoh_repair.webm"
define kick = "movies/kick.webm"
define splash = "movies/splash.webm"

# Fun Values
image utajsign = "secret/utajsign.png"
image vegasjade = "secret/vegasjade.png"
image vegasjade2 = "secret/vegasjade2.png"
image vegaspent = "secret/vegaspent.png"
image vegasjadepent = "secret/vegasjadepent.png"
image fumobee = "secret/fumobee.png"
image cards5alt = "secret/cards5alt.png"
image lancer = "secret/lancer.png"
image lancer flipped = "flip:secret/lancer.png"
image bubble = Transform("secret/bubble.png", zoom = 2.0)

# Animated Sprites

## Realistic explosion
image realistic_explosion_anim = spritesheet_animation("images/realistic_explosion.png", 6, 3, looping = False)

## For cop car lights

image blue_light:
    "blue_light.png"
    alpha 0.0
    linear 0.5 alpha 0.8
    linear 0.5 alpha 0.0
    repeat

image red_light:
    "red_light.png"
    alpha 0.8
    linear 0.5 alpha 0.0
    linear 0.5 alpha 0.8
    repeat

## For Copguy EX

image copguy_ex_front:
    "characters/copguy_ex1.png"
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    pos (0.5, 0.5)
    pass
    xpos 0.51
    ease 2.0 xpos 0.49
    ease 2.0 xpos 0.51
    repeat

image copguy_ex_back:
    "characters/copguy_ex2.png"
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    pos (0.5, 0.5)
    pass
    xpos 0.49
    ease 2.0 xpos 0.51
    ease 2.0 xpos 0.49
    repeat

layeredimage copguy_ex:
    always:
        "copguy_ex_back"

    group ignore_me:
        attribute wow default:
            "copguy_ex_front"
            
## For Tate EX

image tate_ex_front:
    "secret/pt/tate_ex.png"
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    pos (0.5, 0.5)
    pass
    # this is on purpose
    ease 0.5 xpos 0.5
    ease 0.5 ypos 0.5
    repeat
    
image tate_ex_ca_c:
    "secret/pt/tate_ex_c.png"
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    pos (0.5, 0.5)
    blur 5
    pass
    xpos 0.505
    ypos 0.505
    linear 0.5 ypos 0.495
    linear 0.5 xpos 0.495
    linear 0.5 ypos 0.505
    linear 0.5 xpos 0.505
    repeat

image tate_ex_ca_m:
    "ecret/pt/tate_ex_m.png"
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    pos (0.5, 0.5)
    blur 5
    pass
    xpos 0.505
    ypos 0.505
    linear 1.0 ypos 0.495
    linear 1.0 xpos 0.495
    linear 1.0 ypos 0.505
    linear 1.0 xpos 0.505
    repeat

image tate_ex_ca_y:
    "secret/pt/tate_ex_y.png"
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    pos (0.5, 0.5)
    blur 5
    pass
    xpos 0.505
    ypos 0.505
    linear 0.25 ypos 0.495
    linear 0.25 xpos 0.495
    linear 0.25 ypos 0.505
    linear 0.25 xpos 0.505
    repeat

layeredimage tate_ex_preparation:
    group cmy:
        attribute c default:
            "tate_ex_ca_c"
        attribute m default:
            "tate_ex_ca_m"
        attribute y default:
            "tate_ex_ca_y"

    group ignore_me:
        attribute wow default:
            "tate_ex_front"
            
image tate_ex:
    contains:
        "tate_ex_preparation"
    xysize (744, 800)
    xcenter 0.25
    ycenter 0.6

## For train boss
image train_boss_1:
    "characters/finale/trainboss1.png"
    ease 2.0 rotate -1
    ease 2.0 rotate 1
    repeat

image train_boss_2:
    "characters/finale/trainboss2.png"
    ease 2.0 rotate -1
    ease 2.0 rotate 1
    repeat

image train_boss_3:
    "characters/finale/trainboss3.png"
    ease 2.0 rotate -15
    ease 2.0 rotate 15
    repeat

image train_boss_4:
    "characters/finale/trainboss4.png"
    ease 2.0 rotate -10
    ease 2.0 rotate 10
    repeat

image train_boss_5:
    "characters/finale/trainboss5.png"
    ease 2.0 rotate -10
    ease 2.0 rotate 10
    repeat

image train_boss_6:
    "characters/finale/trainboss6.png"
    ease 2.0 rotate -5
    ease 1.0 rotate 5
    repeat

image train_boss_7:
    "characters/finale/trainboss7.png"
    ease 1.0 rotate 5
    ease 2.0 rotate -5
    repeat

layeredimage train_boss_final:
    yanchor 1.10
    zoom 1.25
    group skarei:
        attribute s default:
            "train_boss_6"
        attribute k default:
            "train_boss_7"
        attribute a default:
            "train_boss_5"
        attribute r default:
            "train_boss_4"
        attribute e default:
            "train_boss_2"
        attribute i default:
            "train_boss_1"

    group ignore_me:
        attribute wow default:
            "train_boss_3"

## For Finale Flying Train

image train_fly_1:
    "characters/finale/train_fly_1.png"
    ease 3.0 rotate -3
    ease 3.0 rotate 3
    repeat

image train_fly_2:
    "characters/finale/train_fly_2.png"
    ease 3.0 rotate 3
    ease 3.0 rotate -3
    repeat

image train_fly_3:
    "characters/finale/train_fly_2.png"
    align (0.85, 0.0)
    ease 3.0 rotate -3
    ease 3.0 rotate 3
    repeat

image train_fly_4:
    "characters/finale/train_fly_2.png"
    align (1.70, 0.0)
    ease 3.0 rotate 3
    ease 3.0 rotate -3
    repeat

image train_fly_5:
    "characters/finale/train_fly_2.png"
    align (2.55, 0.0)
    ease 3.0 rotate -3
    ease 3.0 rotate 3
    repeat

image train_fly_6:
    "characters/finale/train_fly_2.png"
    align (3.40, 0.0)
    ease 3.0 rotate 3
    ease 3.0 rotate -3
    repeat

image train_fly_7:
    "characters/finale/train_fly_2.png"
    align (4.25, 0.0)
    ease 3.0 rotate -3
    ease 3.0 rotate 3
    repeat

layeredimage flying_train_final:
    ycenter -100
    group 123456:
        attribute 1 default:
            "train_fly_2"
        attribute 2 default:
            "train_fly_3"
        attribute 3 default:
            "train_fly_4"
        attribute 4 default:
            "train_fly_5"
        attribute 5 default:
            "train_fly_6"
        attribute 6 default:
            "train_fly_7"


    group ignore_me:
        attribute wow default:
            "train_fly_1"

# misc
image ai_ducks = SnowBlossom("duck.png", 50, fast = True)

# Audio
# CSBI Music
define audio.lets_hear_my_baby = "lets_hear_my_baby.ogg"
define audio.canyon = "canyon.ogg"
define audio.canyon_car = "canyon_but_in_the_car.ogg"
define audio.summer_clearance_sale = "summer_clearance_sale.ogg"
define audio.scales_of_joy = "scales_of_joy.ogg"
define audio.hohsis_theme = "hohsis_theme.ogg"
define audio.super_friendly = "super_friendly.ogg"
define audio.time_for_a_smackdown = "time_for_a_smackdown.ogg"
define audio.beautiful_hills = "beautiful_hills.ogg"

# CSBI Speedrun Music
define audio.lets_hear_my_sped = "lets_hear_my_sped.ogg"
define audio.fastbudget_song = "fastbudget_song.ogg"
define audio.fastport = "fastport.ogg"
define audio.fasting = "fasting.ogg"
define audio.happy_running = "happy_running.ogg"

#CSBII Music
define audio.card_castle = "card_castle.ogg"
define audio.basement = "basement.ogg"
define audio.stal = "stal.ogg"
define audio.moongazer = "moongazer.ogg"
define audio.onett = "onett.ogg"
define audio.star_spangled_banner = "star_spangled_banner.ogg"
define audio.buy_something = "buy_something.ogg"
define audio.passport = "passport.ogg"
define audio.passport_ytp = "secret/passport_ytp.ogg"

#CSBIII Act 1 Music
define audio.good_eatin = "good_eatin.ogg"
define audio.supernova = "supernova.ogg"
define audio.airport_counter = "airport_counter.ogg"
define audio.hired_guns = "hired_guns.ogg"
define audio.undyne = "undyne.ogg"
define audio.atarashii_kaze = "atarashii_kaze.ogg"
define audio.police_station = "police_station.ogg"
define audio.echoing = "echoing.ogg"
define audio.kill_cops = "killcops.ogg"
define audio.insane_personalities = "insane_personalities.ogg"
define audio.danger_mystery = "danger_mystery.ogg"
define audio.pressing_pursuit_cornered = "pressing_pursuit_cornered.ogg"
define audio.bun_guster = "bun_guster.ogg"
define audio.happy_roaming = "happy_roaming.ogg"

#CSBIII True Music
define audio.mm_select = "mm_select.ogg"
define audio.billy_radio = "billy_radio.ogg"
define audio.weird_personalities = "weird_personalities.ogg"
define audio.home_depot = "home_depot.ogg"
define audio.candle_world = "candle_world.ogg"
define audio.blazing_corridor = "blazing_corridor.ogg"
define audio.showtime = "showtime.ogg"
define audio.mort_farm = "mort_farm.ogg"
define audio.taiikusai_desu_yo = "taiikusai_desu_yo.ogg"
define audio.track_4 = "track4.ogg"
define audio.funiculi_holiday = "funiculi_holiday.ogg"
define audio.speedy_comet = "speedy_comet.ogg"
define audio.breakout = "breakout.ogg"
define audio.fourside = "fourside.ogg"
define audio.pokey = "pokey.ogg"
define audio.rude_buster = "rude_buster.ogg"
define audio.park_theme = "park_theme.ogg"
define audio.hohsis_remix = "hohsisremix.ogg"
define audio.track_3 = "track3.ogg"
define audio.ac_title = "ac_title.ogg"

# CSBIII: Michigan
define audio.honk_song = "honk_song.ogg"
define audio.wayward_wanderer = "wayward_wanderer.ogg"
define audio.mis_leader = "mis_leader.ogg"
define audio.melancholy = "melancholy.ogg"
define audio.trash_zone = "trash_zone.ogg"

# CSBIII South Music
define audio.brick_by_dick = "brick_by_dick.ogg"
define audio.tunnely_shimbers = "tunnely_shimbers.ogg"
define audio.hard_drive = "hard_drive.ogg"
define audio.penthouse = "penthouse.ogg"
define audio.game_corner = "game_corner.ogg"
define audio.laurel_palace = "laurel_palace.ogg"
define audio.lancer = "secret/lancer.ogg"
define audio.price_right = "price_right.ogg"
define audio.airport = "airport.ogg"
define audio.lego_island = "lego_island.ogg"
define audio.clownpiece = "clownpiece.ogg"

# CSBIII Friend Music
define audio.morning_highway = "morning_highway.ogg"
define audio.creative_exercise = "creative_exercise.ogg"
define audio.pixel_peeker_polka = "pixel_peeker_polka.ogg"
define audio.Lowbudget_song = "lowbudget_song.ogg"
define audio.klaxon_beat = "klaxon_beat.ogg"
define audio.cp_violation = "cp_violation.ogg"
define audio.mm_complete = "mm_complete.ogg"
define audio.tuna_fish = "tuna_fish.ogg"
define audio.full_rulle_med_klas = "<from 0 to 86>full_rulle_med_klas.ogg"
define audio.dense_woods_b = "dense_woods_b.ogg"
define audio.la_by_night = "la_by_night.ogg"
define audio.triage_at_dawn = "triage_at_dawn.ogg"
define audio.the_whale = "the_whale.ogg"
define audio.prophet_2001 = "prophet_2001.ogg"

# CSBIII Country Music
define audio.wool_gloves = "wool_gloves.ogg"
define audio.conflict = "conflict.ogg"
define audio.tumultuous = "tumultuous.ogg"
define audio.lisbon_fever = "lisbon_fever.ogg"
define audio.yuuka_town = "yuuka_town.ogg"
define audio.automatic_love = "automatic_love.ogg"
define audio.chase = "chase.ogg"
define audio.neko_to_sanpo = "neko_to_sanpo.ogg"
define audio.real_world = "real_world.ogg"
define audio.muumin_tani_fuyu = "muumin_tani_fuyu.ogg"
define audio.snufkin = "snufkin.ogg"
define audio.lady_of_the_cold = "lady_of_the_cold.ogg"
define audio.afternoon_hills = "afternoon_hills.ogg"
define audio.xddcc = "xddcc.ogg"

# CSBIII Fired/Rockstar Music
define audio.dealin_dope = "dealin_dope.ogg"
define audio.hit_me_with_your_best_shot = "hitmewithyourbestshot.ogg"
define audio.hightop = "hightop.ogg"
define audio.everlong = "everlong.ogg"
define audio.local_forecast = "local_forecast.ogg"
define audio.now_what = "now_what.ogg"
define audio.happy_rock = "happy_rock.ogg"
define audio.energetic_rock = "energetic_rock.ogg"
define audio.fnaf_6 = "fnaf_6.ogg"
define audio.france = "france.ogg"
define audio.dragon_castle = "dragon_castle.ogg"
define audio.gold_room = "gold_room.ogg"
define audio.sweet_victory = "sweet_victory.ogg"
define audio.dig_this = "dig_this.ogg"
define audio.exotic = "exotic.ogg"
define audio.another_him = "another_him.ogg"

# CSBIII AI Music
define audio.school = "school.ogg"
define audio.cliffs = "cliffs.ogg"
define audio.circus = "circus.ogg"
define audio.friendship = "friendship.ogg"

# CSBIII Archival Music
define audio.facing_worlds = "facing_worlds.ogg"
define audio.take_trip = "take_trip.ogg"
define audio.take_trip2 = "take_trip2.ogg"
define audio.everybody_wants = "everybody_wants.ogg"

# CSBIII Error Music
define audio.night = "night.ogg"

# CSBIII Car Music
define audio.billy_mix = "billy_mix.ogg"
define audio.moving_right_along = "moving_right_along.ogg"

# CSBIII DX: Bronson (Michigan)
define audio.upon_me = "upon_me.ogg"
define audio.error = "error.ogg"

# CSBIII DX Train Music
define audio.sub_game_select = "sub_game_select.ogg"
define audio.outdoors = "<loop 54.031>outdoors.ogg"
define audio.hide_and_seek = "hide_and_seek.ogg"
define audio.ochre_woods_day = "<loop 27.401>ochre_woods_day.ogg"
define audio.bedroom_day = "<loop 0.916>bedroom_day.ogg"
define audio.item_bounce = "item_bounce.ogg"
define audio.krabby_klub = "<loop 3.1>krabby_klub.ogg"
define audio.prof_kranes_kidnap = "prof_kranes_kidnap.ogg"
define audio.e_gadds_lab = "<loop 1.071>e_gadds_lab.ogg"
define audio.onbs = "onbs.ogg"
define audio.encounter_friend_intro = "<from 0 to 44.501>encounter_friend.ogg"
define audio.encounter_friend_loop = "<from 44.502 to 77.599>encounter_friend.ogg"
define audio.in_the_room = "<from 0.491 to 30.501>in_the_room.ogg"
define audio.roundabout = "<from 41.076>roundabout.ogg"
define audio.lo_fi_sunset = "lo_fi_sunset.ogg"
define audio.homely_yado_inn = "<from 0.499 to 40.502>homely_yado_inn.ogg"

# For Tate EX / Perfect Tate
define audio.insomnia_intro = "<from 0 to 11.299>secret/pt/insomnia.ogg"
define audio.insomnia_loop = "<from 22.6>secret/pt/insomnia.ogg"

# CSBIII DX Kuwait Music
define audio.tmwstw = "tmwstw.ogg"

# CSBIII DX Holiday Special Music
define audio.lets_hear_winter = "lets_hear_my_christ.ogg"
define audio.winters_halloween = "winters_halloween.ogg"

# CSBIII DX After-True Music
define audio.lets_hear_spring = "letshearspring.ogg"
define audio.echoing_spring = "echoingspring.ogg"
define audio.alien_atmosphere = "alien_atmosphere.ogg"
define audio.apple_kid = "apple_kid.ogg"
define audio.ten_feet_away = "10_feet_away.ogg"
define audio.get_the_funk = "get_the_funk.ogg"
define audio.hitsquad_2 = "hitsquad_2.ogg"
define audio.ten_feet_away_1 = "10_feet_away_1.ogg"
define audio.ten_feet_away_2 = "10_feet_away_2.ogg"
define audio.ten_feet_away_3 = "10_feet_away_3.ogg"
define audio.ten_feet_away_4 = "10_feet_away_4.ogg"
define audio.interference2 = "<from 276>interference.ogg"

# CSBIII DX Finale Music
define audio.funvalueland = "funvalueland.ogg"
define audio.unobtrusive_fun = "unobtrusive_fun.ogg"
define audio.interference = "<from 0 to 275>interference.ogg"

# Other?
define audio.space_classroom = "secret/space_classroom.ogg"
define audio.billymusicu = "billymusicu.ogg"
define audio.ocean_man = "secret/credits.ogg"
define audio.albuquerque = "albuquerque.ogg"

# SFX
define audio.sfx_addy_snap = "sfx/sfx_addy_snap.ogg"
define audio.sfx_alt_punch = "sfx/sfx_alt_punch.ogg"
define audio.sfx_ambiance_train_interior = "sfx/sfx_ambiance_train_interior.ogg"
define audio.sfx_amtrak_horn = "sfx/sfx_amtrak_horn.ogg"
define audio.sfx_blanket = "sfx/sfx_blanket.ogg"
define audio.sfx_bossappears = "sfx/sfx_bossappears.ogg"
define audio.sfx_beam = "sfx/sfx_beam.ogg"
define audio.sfx_bell = "sfx/sfx_bell.ogg"
define audio.sfx_bite = "sfx/sfx_bite.ogg"
define audio.sfx_bluescreen = "sfx/sfx_bluescreen.ogg"
define audio.sfx_bucket = "sfx/sfx_bucket.ogg"
define audio.sfx_car_approach_stop = "sfx/sfx_car_approach_stop.ogg"
define audio.sfx_car_crash = "sfx/sfx_car_crash.ogg"
define audio.sfx_car_door_open = "sfx/sfx_car_door_open.ogg"
define audio.sfx_car_door_ajar = "sfx/sfx_car_door_ajar.ogg"
define audio.sfx_car_horn = "sfx/sfx_car_horn.ogg"
define audio.sfx_car_stop = "<from 0 to 2>sfx/sfx_car_crash.ogg"
define audio.sfx_car_tire_squeal = "sfx/sfx_car_tire_squeal.ogg"
define audio.sfx_cat_crash = "sfx/sfx_cat_crash.ogg"
define audio.sfx_chatter = "sfx/sfx_chatter.ogg"
define audio.sfx_cheer = "sfx/sfx_cheer1.ogg"
define audio.sfx_cheer2 = "sfx/sfx_cheer2.ogg"
define audio.sfx_cheers = "sfx/sfx_cheers.ogg"
define audio.sfx_chop = "sfx/sfx_chop.ogg"
define audio.sfx_chopper_loop = "sfx/sfx_chopper_loop.ogg"
define audio.sfx_chug_jug = "sfx/sfx_chug_jug.ogg"
define audio.sfx_clapperboard = "sfx/sfx_clapperboard.ogg"
define audio.sfx_clonk = "sfx/sfx_clonk.ogg"
define audio.sfx_csnore = "sfx/sfx_csnore.ogg"
define audio.sfx_crack_open_cold_one = "sfx/sfx_crack_open_cold_one.ogg"
define audio.sfx_decompression = "sfx/sfx_decompression.ogg"
define audio.sfx_desk_slam = "sfx/sfx_desk_slam.ogg"
define audio.sfx_dial_hohsis = "sfx/sfx_dial_hohsis.ogg"
define audio.sfx_dial_rosen = "sfx/sfx_dial_rosen.ogg"
define audio.sfx_dial_tate = "sfx/sfx_dial_tate.ogg"
define audio.sfx_drill = "sfx/sfx_drill.ogg"
define audio.sfx_drillbreak = "sfx/sfx_drillbreak.ogg"
define audio.sfx_doorbell = "sfx/sfx_doorbell.ogg"
define audio.sfx_door_break = "sfx/sfx_door_break.ogg"
define audio.sfx_doorslam = "sfx/sfx_doorslam.ogg"
define audio.sfx_doorslam_open = "sfx/sfx_doorslam_open.ogg"
define audio.sfx_driving = "sfx/sfx_driving.ogg"
define audio.sfx_drop_rings = "sfx/sfx_drop_rings.ogg"
define audio.sfx_duck = "sfx/sfx_duck.ogg"
define audio.sfx_earthquake = "sfx/sfx_earthquake.ogg"
define audio.sfx_elevator_ding = "sfx/sfx_elevator_ding.ogg"
define audio.sfx_end_call = "sfx/sfx_end_call.ogg"
define audio.sfx_explosion = "secret/sfx_explosion.ogg"
define audio.sfx_fabeep = "sfx/sfx_fabeep.ogg"
define audio.sfx_fart = "sfx/sfx_fart.ogg"
define audio.sfx_fart_again = "sfx/sfx_fart_again.ogg"
define audio.sfx_fart_deep = "sfx/sfx_fart_deep.ogg"
define audio.sfx_fart_lite = "sfx/sfx_fart_lite.ogg"
define audio.sfx_fart_with_reverb = "sfx/sfx_fart_with_reverb.ogg"
define audio.sfx_fbi_open_up = "sfx/sfx_fbi_open_up.ogg"
define audio.sfx_flashback_end = "sfx/sfx_flashback_end.ogg"
define audio.sfx_flashback_start = "sfx/sfx_flashback_start.ogg"
define audio.sfx_foundationfail = "sfx/sfx_foundationfail.ogg"
define audio.sfx_funni = "secret/sfx_funni.ogg"
define audio.sfx_gamer_and_girl = "sfx/sfx_gamer_and_girl.ogg"
define audio.sfx_gasp = "sfx/sfx_gasp.ogg"
define audio.sfx_gaster_blast = "minigames/car/sfx_gaster_blast.ogg"
define audio.sfx_glass = "sfx/sfx_glass.ogg"
define audio.sfx_glass_echo = "sfx/sfx_glass_echo.ogg"
define audio.sfx_glass_heavy = "sfx/sfx_glass_heavy.ogg"
define audio.sfx_gleam = "sfx/sfx_gleam.ogg"
define audio.sfx_glitch_in = "sfx/sfx_glitch_in.ogg"
define audio.sfx_gul = "secret/sfx_gul.ogg"
define audio.sfx_hairdyer = "sfx/sfx_hairdryer.ogg"
define audio.sfx_hat_off = "sfx/sfx_hat_off.ogg"
define audio.sfx_heartbeat = "sfx/sfx_heartbeat.ogg"
define audio.sfx_high_five = "sfx/sfx_high_five.ogg"
define audio.sfx_house_door_close = "sfx/sfx_house_door_close.ogg"
define audio.sfx_house_door_open = "sfx/sfx_house_door_open.ogg"
define audio.sfx_jailcell_shut = "sfx/sfx_jailcell_shut.ogg"
define audio.sfx_lego = "sfx/sfx_legosfx.ogg"
define audio.sfx_lego_break = "sfx/sfx_lego_break.ogg"
define audio.sfx_hard_knock = "sfx/sfx_hard_knock.ogg"
define audio.sfx_hubbub = "sfx/sfx_hubbub.ogg"
define audio.sfx_hitbod1 = "sfx/sfx_hitbod1.ogg"
define audio.sfx_hitbod2 = "sfx/sfx_hitbod2.ogg"
define audio.sfx_hitbod3 = "sfx/sfx_hitbod3.ogg"
define audio.sfx_hks1 = "sfx/sfx_hks1.ogg"
define audio.sfx_hks2 = "sfx/sfx_hks2.ogg"
define audio.sfx_hks3 = "sfx/sfx_hks3.ogg"
define audio.sfx_hold_it = "sfx/sfx_hold_it.ogg"
define audio.sfx_hurt1 = "sfx/sfx_hurt1.ogg"
define audio.sfx_issac = "sfx/sfx_isaac.ogg"
define audio.sfx_items_rustling = "sfx/sfx_items_rustling.ogg"
define audio.sfx_joj_loop = "sfx/sfx_joj_loop.ogg"
define audio.sfx_less_annoying_alarm_sound = "sfx/sfx_less_annoying_alarm_sound.ogg"
define audio.sfx_lightswitch = "sfx/sfx_lightswitch.ogg"
define audio.sfx_keyboard = "sfx/sfx_keyboard.ogg"
define audio.sfx_mc_brew = "sfx/sfx_mc_brew.ogg"
define audio.sfx_mc_bottlehit = "sfx/sfx_mc_bottlehit.ogg"
define audio.sfx_mc_drink = "sfx/sfx_mc_drink.ogg"
define audio.sfx_mc_hit = "sfx/sfx_mc_hit.ogg"
define audio.sfx_mc_throw = "sfx/sfx_mc_throw.ogg"
define audio.sfx_mean_transform = "sfx/sfx_mean_transform.ogg"
define audio.sfx_metalpipe = "sfx/sfx_metalpipe.ogg"
define audio.sfx_michael_eat = "sfx/sfx_michael_eat.ogg"
define audio.sfx_michael_facepalm = "sfx/sfx_michael_facepalm.ogg"
define audio.sfx_moneyfalls = "sfx/sfx_moneyfalls.ogg"
define audio.sfx_nice_car = "sfx/sfx_nice_car.ogg"
define audio.sfx_noicepop = "sfx/sfx_noicepop.ogg"
define audio.sfx_not_so_nice_scratch = "sfx/sfx_not_so_nice_scratch.ogg"
define audio.sfx_obama = "sfx/sfx_obama.ogg"
define audio.sfx_objection = "sfx/sfx_objection.ogg"
define audio.sfx_okuubeam = "sfx/sfx_okuubeam.ogg"
define audio.sfx_page = "<from 0.321>sfx/sfx_page.ogg"
define audio.sfx_payday = "sfx/sfx_payday.ogg"
define audio.sfx_pickup_call = "sfx/sfx_pickup_call.ogg"
define audio.sfx_ping = "sfx/sfx_ping.ogg"
define audio.sfx_ping_spam = "sfx/sfx_ping_spam.ogg"
define audio.sfx_pkmn_hit = "sfx/sfx_pkmn_hit.ogg"
define audio.sfx_plate_break = "sfx/sfx_plate_break.ogg"
define audio.sfx_poot = "sfx/sfx_poot.ogg"
define audio.sfx_puke = "sfx/sfx_puke.ogg"
define audio.sfx_punch = "sfx/sfx_punch.ogg"
define audio.sfx_punch_alt = "sfx/sfx_alt_punch.ogg"
define audio.sfx_punch_friendly = "sfx/sfx_punch_friendly.ogg"
define audio.sfx_retail_beep = "sfx/sfx_retail_beep.ogg"
define audio.sfx_richlaugh = "sfx/sfx_richlaugh.ogg"
define audio.sfx_ring_once = "sfx/sfx_ring_once.ogg"
define audio.sfx_ringtone_billy = "sfx/sfx_ringtone_billy.ogg"
define audio.sfx_ringtone_cs = "sfx/sfx_ringtone_cs.ogg"
define audio.sfx_ringtone_addy = "sfx/sfx_ringtone_addy.ogg"
define audio.sfx_ringtone_tate = "sfx/sfx_ringtone_tate.ogg"
define audio.sfx_ringtone_tate_alt = "sfx/sfx_ringtone_tate_alt.ogg"
define audio.sfx_roll_window = "sfx/sfx_roll_window.ogg"
define audio.sfx_rubiks_cube = "sfx/sfx_rubiks_cube.ogg"
define audio.sfx_select = "sfx/sfx_select.ogg"
define audio.sfx_shoeslide = "sfx/sfx_shoeslide.ogg"
define audio.sfx_siren = "sfx/sfx_siren.ogg"
define audio.sfx_slack = "sfx/sfx_slack.ogg"
define audio.sfx_sliding_door_close = "sfx/sfx_sliding_door_close.ogg"
define audio.sfx_sliding_door_open = "sfx/sfx_sliding_door_open.ogg"
define audio.sfx_slots = "sfx/sfx_slots.ogg"
define audio.sfx_small_spill = "sfx/sfx_small_spill.ogg"
define audio.sfx_snd_lightswitch = "sfx/snd_lightswitch.ogg"
define audio.sfx_snd_undynestep = "sfx/snd_undynestep.ogg"
define audio.sfx_somethingchanged = "sfx/sfx_somethingchanged.ogg"
define audio.sfx_sparkles = "sfx/sfx_sparkles.ogg"
define audio.sfx_spellcast = "sfx/sfx_spellcast.ogg"
define audio.sfx_spikes = "sfx/sfx_spikes.ogg"
define audio.sfx_splash = "sfx/sfx_splash.ogg"
define audio.sfx_start_rocking = "sfx/sfx_start_rocking.ogg"
define audio.sfx_tape_rewind = "sfx/sfx_tape_rewind.ogg"
define audio.sfx_tf2_pickup_metallic = "sfx/sfx_tf2_pickup_metallic.ogg"
define audio.sfx_tf2_sapper = "sfx/sfx_tf2_sapper.ogg"
define audio.sfx_thunder = "sfx/sfx_thunder.ogg"
define audio.sfx_tinnitus = "sfx/sfx_tinnitus.ogg"
define audio.sfx_tiresqueal = "sfx/sfx_tiresqueal.ogg"
define audio.sfx_train_brake = "sfx/sfx_train_brake.ogg"
define audio.sfx_valid = "sfx/sfx_valid.ogg"
define audio.sfx_victory_punch = "sfx/sfx_victory_punch.ogg"
define audio.sfx_vine = "secret/sfx_vine.ogg"
define audio.sfx_walkie_on = "sfx/sfx_walkie_on.ogg"
define audio.sfx_walkie_off = "sfx/sfx_walkie_off.ogg"
define audio.sfx_waterphone = "sfx/sfx_waterphone.ogg"
define audio.sfx_water_shake = "sfx/sfx_water_shake.ogg"
define audio.sfx_whoosh = "sfx/sfx_whoosh.ogg"
define audio.sfx_windows_logon = "sfx/sfx_windows_logon.ogg"
define audio.sfx_woohoo = "sfx/sfx_woohoo.wav"
define audio.sfx_yelling = "sfx/sfx_yelling.ogg"
define audio.sfx_ytpintro = "sfx/sfx_ytpintro.ogg"
define audio.sfx_zenigata_shout = "sfx/sfx_zenigata_shout.ogg"

# Layers?
define config.detached_layers += ["broadcast"]
image stage_screen = Window(Layer("broadcast", clipping = False), background = "minigames/pencil/stage.png")

# Checks
default fanboy_type = None
default fanbase = None
default nice_car = False
default returning_from_blooper = False
default south_car_stole_money = False
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
default sfxtotal = ""
default musictotal = ""
default charactertotal = ""
default transformtotal = ""
default bgtotal = ""
default movietotal = ""
default spritetotal = ""
default d20 = roller

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

# DX Train route
default train_money_stolen = False
default train_money_container = "briefcase"
default train_money_stolen_dialogue_switch = "latch it shut"
default train_money_stolen_dialogue_switch_2 = " won"
default train_polar_express_fun_value = False
default train_pancake_fun_value = False
default train_skip_at_chicago = None
default train_tate_is_fragile_fun_value = False
default train_ending_money_returned = False
default ch1_direction = "left"
default ch1_direction_sprite = 6
default ch1_direction_line = "A...{w=0.5} pineapple?"
default ch2_cs_attack_used = "pushed"
default ch3_showed_ytps = None
default cs_chosen_form = "cs_vs_tate_punch"

#BTTF
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
default blue_check = False
default con_start = False
default gun_get = False

# Christmas
default tree_first = False
default tree_second = False
default lights_first = False
default decor_first = False

# RPG
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

default typewriter_text = "Hello, world!"

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
        for i in Replay_items:
            if not renpy.seen_label(i.replay):
                seen_all = False
        if seen_all:
            achievement_manager.unlock("Fin.")
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

# Jump Menu
screen chapter_menu():
    zorder 100
    style_prefix "start"
    window id "start_window" xalign 0.5 yalign 0.5:
        vbox xalign 0.5 yalign 0.5:
            spacing 50
            text "Start where?" textalign 0.5 size 72 xalign 0.5 yalign 0.5
            hbox xalign 0.5 yalign 0.5:
                spacing 50
                imagebutton auto "menu/csbi_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbi_start")
                imagebutton auto "menu/csbii_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.csb2_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbii_start")
                imagebutton auto "menu/csbiii1_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.csb3a_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbiii_start")
                imagebutton auto "menu/csbiii2_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.csb3b_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbiii_choose_direction")
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.true_ending
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu"), Jump("dx_start")
style start_window is empty

label splashscreen:
    $ renpy.movie_cutscene(splash)
    $ persistent.seen_splash = True
    $ persistent.heard.add("bubble_tea")
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

    if not persistent.seen_splash:
        if not renpy.music.is_playing():
            $ renpy.music.play("bubble_tea.ogg", loop = False)
    else:
        if not renpy.music.is_playing():
            $ renpy.music.play("<from 16.53>bubble_tea.ogg", loop = False)
            $ persistent.seen_splash = False

    return

label start:  # this might be required??
label chapter_select:
    scene game_menu
    stop music fadeout 3.0
    window hide
    pause 0.1
    call screen chapter_menu()
    return

init python:
    import math

    def show_typewriter(st, at):
        if st > 2.0:
            return Text(typewriter_text, textalign = 0.5, size = 100, outlines=[(absolute(10), "#000", absolute(0), absolute(0))]), 0.1
        else:
            d = Text(typewriter_text[:math.ceil((st / 2.0) * len(typewriter_text))], textalign = 0.5, size = 100, outlines=[(absolute(10), "#000", absolute(0), absolute(0))])
            return d, 0.1

image typewriter = DynamicDisplayable(show_typewriter)

label test:

    scene washington_road dusk
    show arceus dusk flipped at right
    show cs dusk at left
    with dissolve
    arceus "This is a dusk test"
    scene washington_road
    show arceus dark at right
    show cs dark at left
    with dissolve
    arceus "This is a dark test"
    menu:
        "Menu test?"
        "Yes"  (type = "good"):
            $ renpy.full_restart()
        "No"  (type = "bad"):
            $ renpy.full_restart()
        "True"  (type = "true"):
            $ renpy.full_restart()
        "New cool thing OwO"  (type = "dx"):
            menu:
                "Train Boss Test":
                    stop music
                    scene amtrak_dining_car
                    show cs scared at left
                    show mean scared flipped at right
                    pause 2.0
                    show train_boss_final with easeintop
                    pakoo "This is the train boss."
                    $ renpy.full_restart()
                "Screen Test":
                    show screen warning("The following scene is a test.\nIt may be teste.", "Warnings: developer cruft, bad puns", "start")
                    pause
                    $ renpy.full_restart()
                "EX Test":
                    stop music
                    show copguy_ex at left
                    pakoo "This is Copguy EX."
                    show tate_ex at mid_right
                    pakoo "This is Tate EX."
                    pakoo "Does this work? Idk"
                    $ renpy.full_restart()
                "Perfect Billy Test":
                    perfect_billy "I'm Perfect Billy Mays!"
                    cs "woah that's crazy"
                    $ renpy.full_restart()
                "Flying Train Test":
                    stop music
                    show flying_train_final at right with easeinright
                    pause 1.0
                    show flying_train_final at left with ease          
                    pakoo "This is the flying train layered image."
                    hide flying_train_final with easeoutleft
                    pause
                    $ renpy.full_restart()
                "Music Test":
                    # play music4 ten_feet_away_4 if_changed volume 0.1
                    # play music3 ten_feet_away_3 if_changed volume 0.1
                    # play music2 ten_feet_away_2 if_changed volume 0.1
                    play music "audio/10_feet_away_1.ogg"
                    # $ renpy.music.set_pause(True, "music4")
                    # $ renpy.music.set_pause(True, "music3")
                    # $ renpy.music.set_pause(True, "music2")
                    pakoo "test 1"
                    pause
                    play music2 [ "<sync music>audio/10_feet_away_2.ogg", "audio/10_feet_away_2.ogg" ]
                    # $ renpy.music.set_pause(True, "music4")
                    # $ renpy.music.set_pause(True, "music3")
                    # $ renpy.music.set_pause(False, "music2")
                    pakoo "test 2"
                    pause
                    play music3 [ "<sync music>audio/10_feet_away_3.ogg", "audio/10_feet_away_3.ogg" ]
                    # $ renpy.music.set_pause(True, "music4")
                    # $ renpy.music.set_pause(False, "music3")
                    pakoo "test 3"
                    pause
                    play music4 [ "<sync music>audio/10_feet_away_4.ogg", "audio/10_feet_away_4.ogg" ]
                    # $ renpy.music.set_pause(False, "music4")
                    pakoo "test 4"
                    pause
                    $ renpy.full_restart()

define shake1 = { "master" : hpunch }
define shake2 = { "master" : vpunch }

screen woohoo_counter():
    text "Woohoo Counter = [round(persistent.woohoo)]" textalign 0.5 size 108 xalign 0.5 yalign 0.5:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.5:
        spacing 50

screen cultcon_votes():
    text "Top 5 Winners!" textalign 0.5 size 72 xalign 0.5 yalign 0.5:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.5:
        spacing 50
screen cultcon_votes_1():
    text "Pencil Cult: 10" textalign 0.5 size 48 xalign 0.5 yalign 0.7:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.7:
        spacing 50
screen cultcon_votes_2():
    text "Lunatic Cultists: 27" textalign 0.5 size 48 xalign 0.5 yalign 0.6:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.6:
        spacing 50
screen cultcon_votes_3():
    text "Society of the Blind Eye: 35" textalign 0.5 size 48 xalign 0.5 yalign 0.5:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.5:
        spacing 50
screen cultcon_votes_4():
    text "Scientology: 70" textalign 0.5 size 48 xalign 0.5 yalign 0.4:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.4:
        spacing 50
screen cultcon_votes_5():
    text "Blue Branch: [total_votes]" textalign 0.5 size 48 xalign 0.5 yalign 0.3:
        font "fonts/digital-7.ttf"
        color "#ff0000"
    hbox xalign 0.5 yalign 0.3:
        spacing 50

screen debugger_menu():
    text "Stats" textalign 0.5 size 72 xalign 0.5 yalign 0.0
    hbox xalign 0.5 yalign 0.0:
        spacing 50
    text "sfx loaded: [sfxtotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.1
    hbox xalign 0.5 yalign 0.1:
        spacing 50
    text "music loaded: [musictotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.2
    hbox xalign 0.5 yalign 0.2:
        spacing 50
    text "characters loaded: [charactertotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.3
    hbox xalign 0.5 yalign 0.3:
        spacing 50
    text "backgrounds loaded: [bgtotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.4
    hbox xalign 0.5 yalign 0.4:
        spacing 50
    text "sprites loaded: [spritetotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.5
    hbox xalign 0.5 yalign 0.5:
        spacing 50
    text "movies loaded: [movietotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.6
    hbox xalign 0.5 yalign 0.6:
        spacing 50
    text "transforms loaded: [transformtotal]" textalign 0.5 size 48 xalign 0.5 yalign 0.7
    hbox xalign 0.5 yalign 0.7:
        spacing 50
