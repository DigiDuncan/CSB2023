# Text Beep Spacing
# Partially stolen from:
#   https://www.renpy.org/doc/html/config.html#var-config.replace_text
#   https://lemmasoft.renai.us/forums/viewtopic.php?t=22730
# This is meant to place pauses after certain punctuation automatically so that the dialogue feels more... human.
# These are set up so that it only works if there is more than once sentence in the text box at any given time.
# Make sure there's a space after your punctuation or it won't work.
# You can still add manual pauses wherever you like in the script if this isn't enough for you.

init python:
    import re
    def auto_wait(s):
        # these items wait for 0.25:
        # commas, periods, question marks, exclamation marks
        s = re.sub(r'(([,|.|?|!])(({\/[a-z]*})*) )', r'\1{w=0.25}', s, flags=re.IGNORECASE) 

        # these items wait for 0.5:
        # ellipses, em-dashes, colons
        s = re.sub(r'((\.\.\.|--|:)(({\/[a-z]*})*) )', r'\1{w=0.5}', s, flags=re.IGNORECASE) 

        return s
    config.say_menu_text_filter = auto_wait

# Flip
init -10 python:
    def xflip(s):
        return Transform(s, xzoom = -1)

    config.displayable_prefix["flip"] = xflip

# Text beeps
init python:
    renpy.music.register_channel("beep", "voice", loop = True)
    def char_callback(event, name = None, beep = None, play_beeps = True, **kwargs):
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
    renpy.music.register_channel("music2", "music")
    renpy.music.register_channel("jukebox", "music")
    renpy.music.register_channel("sfx", "sound")
    renpy.music.register_channel("dxcom", "voice")

init 10 python:
    def unlock_all():
        for m in music_map.keys():
            persistent.heard.add(m)
        for p in name_map.keys():
            persistent.seen.add(p)
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

transform center_right:
    yanchor 0.5 ypos 0.5
    xanchor 1.0 xpos 1.0

transform center_left:
    yanchor 0.5 ypos 0.5
    xanchor 0.0 xpos 0.0

transform mid_offscreen_right:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 1.0

transform mid_offscreen_left:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos -0.0

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

transform t_linus_drop_tips:
    linear 0.35 yalign 2.0

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

transform t_mean_dining_car:
    anchor (0.5, 0.5)
    pos (0.3, 0.6)

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

# Character Definitions
define n = Character(None, what_italic = True, callback = char_callback)  # Narrator
define cs = Character("cs188", callback = renpy.partial(char_callback, name = "cs", beep = "cs"))
define cs_fakegod = Character("cs188 (pretending to be CSGod)", callback = renpy.partial(char_callback, name = "cs", beep = "csgod"))
define craptop = Character("Craptop", callback = renpy.partial(char_callback, name = "craptop"))
define sticky = Character("Sticky Note", callback = renpy.partial(char_callback, name = "sticky"))
define discord = Character("Discord", callback = char_callback)
define nova = Character("Nova", callback = renpy.partial(char_callback, name = "nova"))
define carguy = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", beep = "nice"))
define carguy_nobeep = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", play_beeps = False))
define greeter = Character("Greeter", callback = renpy.partial(char_callback, name = "doug"))
define doug = Character("Doug", callback = renpy.partial(char_callback, name = "doug"))
define cashier = Character("Cashier", callback = renpy.partial(char_callback, name = "cashier"))
define ycs = Character("Young CS", callback = renpy.partial(char_callback, beep = "ycs"))
define hoh_operator = Character("HoH SiS Operator", callback = char_callback)
define rich = Character("Richard", callback = renpy.partial(char_callback, name = "rich", beep = "rich"))
define ed = Character("Ed", callback = renpy.partial(char_callback, name = "ed", beep = "ed"))
define wesley = Character("Wesley", callback = renpy.partial(char_callback, name = "wesley", beep = "wes"))
define michael = Character("Michael", callback = renpy.partial(char_callback, name = "michael", beep = "mich"))
define michael_nobeep = Character("Michael", callback = renpy.partial(char_callback, name = "michael", play_beeps = False))
define phil = Character("Phil", callback = renpy.partial(char_callback, name = "phil", beep = "phil"))
define worker_1 = Character("Worker 1", callback = char_callback)
define worker_2 = Character("Worker 2", callback = char_callback)
define worker_3 = Character("Worker 3", callback = char_callback)
define worker_4 = Character("Worker 4", callback = char_callback)
define worker_5 = Character("Worker 5", callback = char_callback)
define worker_6 = Character("Worker 6", callback = char_callback)
define worker_7 = Character("Worker 7", callback = char_callback)
define digi = Character("Digi", callback = renpy.partial(char_callback, name = "digi", beep = "digi"))
define pakoo = Character("Pakoo", callback = renpy.partial(char_callback, name = "pakoo", beep = "pak"))
define addy = Character("Addy", callback = renpy.partial(char_callback, name = "addy", beep = "pak"))
define copguy = Character("Copguy", callback = renpy.partial(char_callback, name = "copguy", beep = "cop"))
define arceus = Character("Arceus", callback = renpy.partial(char_callback, name = "arceus", beep = "arc"))
define anno = Character("Anno", callback = renpy.partial(char_callback, name = "anno", beep = "anno"))
define border_guard = Character("Border Guard", callback = renpy.partial(char_callback, name = "border_guard"))
define linus = Character("Linus", callback = renpy.partial(char_callback, name = "linus", beep = "ltt"))
define asylum_worker = Character("Mr. Mohs", callback = renpy.partial(char_callback, name = "mohs"))
define csgod = Character("CSGod", callback = renpy.partial(char_callback, name = "csgod", beep = "csgod"))
define luke = Character("Luke", callback = renpy.partial(char_callback, name = "luke", beep = "luke"))
define taran = Character("Taran", callback = renpy.partial(char_callback, name = "taran"))
define colton = Character("Colton", callback = renpy.partial(char_callback, name = "colton"))
define sheriff = Character("Sheriff", callback = renpy.partial(char_callback, name = "sheriff", beep = "sheriff"))
define billy = Character("Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define tv_billy = Character("TV Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define cultist = Character("Cultist", callback = renpy.partial(char_callback, name = "cultist"))
define cultist_2 = Character("Cultist 2", callback = char_callback)
define cultist_3 = Character("Cultist 3", callback = char_callback)
define scott = Character("Scott", callback = renpy.partial(char_callback, name = "scott", beep = "scott"))
define terry = Character("Terry", callback = renpy.partial(char_callback, name = "terry", beep = "terry"))
define carla = Character("Carla", callback = renpy.partial(char_callback, beep = "carla"))
define peppino = Character("Peppino", callback = renpy.partial(char_callback, name = "peppino", beep = "peppino"))
define iris = Character("Iris", callback = renpy.partial(char_callback, name = "iris", beep = "iris"))
define lego = Character("LegoBot", callback = renpy.partial(char_callback, name = "lego", beep = "lego"))
define trailtrash = Character("Trailer Trash", callback = renpy.partial(char_callback, name = "trailtrash"))
define green = Character("Mr. Green", callback = renpy.partial(char_callback, name = "green", beep = "green"), what_color="#00FF00")
define jerma = Character("Jerma", callback = renpy.partial(char_callback, name = "jerma", beep = "jerma"))
define pencil = Character("Pencil Greeter", callback =renpy.partial(char_callback, name = "pencil"))
define signup = Character("Signup Helper", callback = char_callback)
define host = Character("Host", callback = renpy.partial(char_callback, name = "mettaton", beep = "snd_mtt"), what_font = "8bitoperator_jve.ttf", what_size = 40)
define tsa = Character("TSA Agent", callback = renpy.partial(char_callback, name = "tsa"))
define luigi = Character("Luigi", callback = renpy.partial(char_callback, name = "luigi", beep = "luigi"))
define mika = Character("Mika", callback = renpy.partial(char_callback, name = "mika", beep = "mika"))
define k174 = Character("K17-4", callback = renpy.partial(char_callback, name = "k174"))
define k199 = Character("K19-9", callback = char_callback)
define k207 = Character("K20-7", callback = char_callback)
define billy_far = Character("Billy (from off screen)", callback = renpy.partial(char_callback, beep = "billy_from_afar"))
define direct = Character("Director", callback = renpy.partial(char_callback, beep = "iris"))
define monika = Character("Monika", callback = renpy.partial(char_callback, name = "monika", beep = "monika"))
define lancer = Character("Lancer", callback = renpy.partial(char_callback, name = "lancer", beep = "lancer"))
define tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep="tate"))
define kitty = Character("Kitty", callback = renpy.partial(char_callback, name = "kitty", beep = "kitty"))
define obama = Character("Obama", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define bomaha = Character("Omaha", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define obamanobeep = Character("Obama", callback = renpy.partial(char_callback, name = "obama", play_beeps = False))
define bomahanobeep = Character("Omaha", callback = renpy.partial(char_callback, name = "obama", play_beeps = False))
define blank = Character("Blank", callback = renpy.partial(char_callback, name = "blank", beep = "blank"))
define aria = Character("Aria", callback = renpy.partial(char_callback, name = "aria", beep = "aria"))
define aria_alt = Character("Aria", callback = renpy.partial(char_callback, name = "aria", beep = "aria_alt"))
define cop = Character("Cop", callback = renpy.partial(char_callback, name = "cop"))
define midge = Character("Midge", callback = renpy.partial(char_callback, name = "midge", beep = "midge"))
define db = Character("DB05", callback = renpy.partial(char_callback, name = "db", beep = "db05"))
define customer = Character("Customer", callback = char_callback)
define guest = Character("Guest", callback = renpy.partial(char_callback, name = "guest"))
define janitor = Character("Janitor", callback = char_callback)
define ges = Character("Ges", callback = renpy.partial(char_callback, name = "ges", beep = "ges"))
define nurse = Character("Nurse", callback = char_callback)
define benrey = Character("Benrey", callback = renpy.partial(char_callback, name = "benrey"))
define mean = Character("Mean", callback = renpy.partial(char_callback, name = "mean", beep = "mean"))
define agent = Character("Howie", callback = renpy.partial(char_callback, name = "howie", beep = "howie"))
define gordon = Character("Gordon", callback = renpy.partial(char_callback, name = "gordon", beep = "gordon"))
define receptionist = Character("Receptionist", callback = char_callback)
define scott_pres = Character("Scott, President of Domino's Pizza", callback = renpy.partial(char_callback, name = "scott_pres", beep = "scott_pres"))
define miku = Character("Hatsune Miku", callback = renpy.partial(char_callback, name = "miku", beep = "miku"))
define hammond = Character("Richard", callback = renpy.partial(char_callback, name = "hammond"))
define jeremy = Character("Jeremy", callback = char_callback)
define james = Character("James", callback = char_callback)
define tom = Character("Tom Scott", callback = renpy.partial(char_callback, name = "tom", beep = "tom"))
define sayori = Character("Sayori", callback = renpy.partial(char_callback, name = "sayori"))
define gnome = Character("Gnome", callback = renpy.partial(char_callback, name = "gnome", beep = "gnome"))
define chat = Character("Chat", callback = char_callback)
define unknown = Character("???", callback = char_callback)
define crowd = Character("Crowd", callback = char_callback)
define worker = Character("Worker", callback = char_callback)
define streetguy = Character("Street Guy", callback = renpy.partial(char_callback, name = "streetguy", beep = "nice"))
define waitress = Character("Waitress", callback = char_callback)
define mario = Character("Mario", callback = renpy.partial(char_callback, name = "mario"))
define smiley = Character("Smiley", callback = renpy.partial(char_callback, name = "smiley"))
define violent_jay = Character("Violent Jay", callback = renpy.partial(char_callback, name = "jay"))
define shaggy_too_dope = Character("Shaggy Too Dope", callback = char_callback)
define joel = Character("Vargskelethor Joel", callback = renpy.partial(char_callback, name = "joel", beep = "joel"))
define ikea_greeter = Character("Ikea Greeter", callback = char_callback)
define ikea_worker = Character("Ikea Worker", callback = char_callback)
define pomni = Character("Pomni", callback = renpy.partial(char_callback, name = "pomni", beep = "pomni"))
define average_swede = Character("Swede", callback = char_callback)
define alien = Character("Grey", callback = char_callback)
define moomin = Character("Moomin", callback = renpy.partial(char_callback, name = "moomin"))  # DX: Beep
define snufkin = Character("Snufkin", callback = renpy.partial(char_callback, name = "snufkin"))  # DX: Beep
define alicia = Character("Alicia", callback = renpy.partial(char_callback, name = "alicia"))
define witch = Character("Witch", callback = renpy.partial(char_callback, name = "witch"))  # DX: Beep
define tate_offscreen = Character("???", callback = renpy.partial(char_callback, name = "tate_offscreen", beep="tate"))
define pakoo_offscreen = Character("???", callback = renpy.partial(char_callback, name = "pakoo_offscreen", beep="pak"))
define green_offscreen = Character("???", callback = renpy.partial(char_callback, name = "green", beep = "green"), what_color="#00FF00")
define renovator = Character("Renovator", callback = char_callback)
define cruise = Character("Tom Cruise", callback = char_callback)

# Character Images
## CS
image cs = "characters/cs/neutral.png"
image cs flipped = "flip:characters/cs/neutral.png"
image cs happy = "characters/cs/happy.png"
image cs happy flipped = "flip:characters/cs/happy.png"
image cs happy dark = "characters/cs/happydark.png"
image cs happy dark flipped = "flip:characters/cs/happydark.png"
image cs angry = "characters/cs/angry.png"
image cs angry dark = "characters/cs/angrydark.png"
image cs angry flipped = "flip:characters/cs/angry.png"
image cs angry dark flipped = "flip:characters/cs/angrydark.png"
image cs worried = "characters/cs/worried.png"
image cs worried flipped = "flip:characters/cs/worried.png"
image cs disappointed = "characters/cs/disappointed.png"
image cs disappointed metal = "characters/cs/disappointedmetal.png"
image cs disappointed metal2 = "characters/cs/disappointedmetal2.png"
image cs disappointed metal3 = "characters/cs/disappointedmetal3.png"
image cs disappointed metal4 = "characters/cs/disappointedmetal4.png"
image cs disappointed flipped = "flip:characters/cs/disappointed.png"
image cs concentrate = "characters/cs/concentrate.png"
image cs concentrate flipped = "flip:characters/cs/concentrate.png"
image cs concentrate dark = "characters/cs/concentratedark.png"
image cs phone = "characters/cs/phone.png"
image cs dark = "characters/cs/neutraldark.png"
image cs dark flipped = "flip:characters/cs/neutraldark.png"
image cs dusk = "characters/cs/neutraldusk.png"
image cs disappointed dark = "characters/cs/disappointeddark.png"
image cs disappointed dark flipped = "flip:characters/cs/disappointeddark.png"
image cs disappointed dusk = "characters/cs/disappointeddusk.png"
image cs worried dark = "characters/cs/worrieddark.png"
image cs worried dark flipped = "flip:characters/cs/worrieddark.png"
image cs prison = "characters/cs/prison.png"
image cs prison_worried = "characters/cs/prison_worried.png"
image cs guard = "characters/cs/guard.png"
image cs guard dark = "characters/cs/guarddark.png"
image cs fakegod = "characters/cs/fake_god.png"
image cs guitar = "characters/cs/guitar.png"
image cs surprised = "characters/cs/surprised.png"
image cs surprised flipped  = "flip:characters/cs/surprised.png"
image cs scared = "characters/cs/scared.png"
image cs scared flipped = "flip:characters/cs/scared.png"
image cs insane worried = "characters/cs/insane.png"
image cs insane worried flipped = "flip:characters/cs/insane.png"
image cs insane disappointed = "characters/cs/insane2.png"
image cs horse = "characters/cs/horse.png"
image cs horse flipped = "flip:characters/cs/horse.png"

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
image arceus angry dark = "characters/arc/angrydark.png"
image arceus angry dark flipped = "flip:characters/arc/angrydark.png"
image arceus guard = "characters/arc/guard.png"
image arceus guard flipped = "flip:characters/arc/guard.png"
image arceus happy = "characters/arc/happy.png"
image arceus happy flipped = "flip:characters/arc/happy.png"
image arceus happy dark = "characters/arc/happydark.png"
image arceus happy dark flipped = "flip:characters/arc/happydark.png"
image arceus prison = "characters/arc/prison.png"
image arceus prison flipped = "flip:characters/arc/prison.png"
image arceus worried = "characters/arc/worried.png"
image arceus worried flipped = "flip:characters/arc/worried.png"
image arceus dirty worried = "characters/arc/worrieddirty.png"
image arceus dirty worried flipped = "flip:characters/arc/worrieddirty.png"
image arceus worried dark = "characters/arc/worrieddark.png"
image arceus worried dark flipped = "flip:characters/arc/worrieddark.png"
image arceus dark = "characters/arc/arceusdark.png"
image arceus dark flipped = "flip:characters/arc/arceusdark.png"
image arceus dusk = "characters/arc/arceusdusk.png"
image arceus angry dusk = "characters/arc/angrydusk.png"
image arceus dusk flipped = "flip:characters/arc/arceusdusk.png"

## Anno
image anno = "characters/anno/anno.png"
image anno prison = "characters/anno/anno_prison.png"
image anno guard = "characters/anno/anno_guard.png"
image anno guard dark = "characters/anno/anno_guarddark.png"

## Pakoo
image pakoo = "characters/pakoo/pakoo.png"
image pakoo dark = "characters/pakoo/pakoodark.png"
image pakoo flipped = "flip:characters/pakoo/pakoo.png"
image pakoo dark flipped = "flip:characters/pakoo/pakoodark.png"
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

## Tate
image tate = "characters/tate/tatehappy.png"
image tate dark = "characters/tate/tatehappydark.png"
image tate flipped = "flip:characters/tate/tatehappy.png"
image tate dark flipped = "flip:characters/tate/tatehappydark.png"
image tate srs = "characters/tate/tateserious.png"
image tate srs dark = "characters/tate/tateseriousdark.png"
image tate srs flipped = "flip:characters/tate/tateserious.png"
image tate srs dark flipped = "flip:characters/tate/tateseriousdark.png"
image tate shock = "characters/tate/tateshock.png"
image tate shock dark = "characters/tate/tateshockdark.png"
image tate shock flipped = "flip:characters/tate/tateshock.png"
image tate shock dark flipped = "flip:characters/tate/tateshockdark.png"
image tate smug = "characters/tate/tatesmug.png"
image tate smug dark = "characters/tate/tatesmugdark.png"
image tate smug flipped = "flip:characters/tate/tatesmug.png"
image tate smug dark flipped = "flip:characters/tate/tatesmugdark.png"
image tate sheepish = "characters/tate/tatesheepish.png"
image tate sheepish flipped = "flip:characters/tate/tatesheepish.png"
image tate sad = "characters/tate/tatesad.png"
image tate sad flipped = "flip:characters/tate/tatesad.png"
image tate stare = "characters/tate/tatestare.png"
image tate stare flipped = "flip:characters/tate/tatestare.png"

## Mean
image mean = "characters/mean/mean.png"
image mean flipped = "flip:characters/mean/mean.png"
image mean happy = "characters/mean/meanhappy.png"
image mean happy flipped = "flip:characters/mean/meanhappy.png"
image mean happy2 = "characters/mean/meanhappy2.png"
image mean happy2 flipped = "flip:characters/mean/meanhappy2.png"
image mean surprised = "characters/mean/meansurprised.png"
image mean surprised flipped = "flip:characters/mean/meansurprised.png"

## Archival
image k174 = "characters/k174.png"
image k174 flipped = "flip:characters/k174.png"
image k199 = "characters/k199.png"
image k199 flipped = "flip:characters/k199.png"
image k207 = "characters/k207.png"
image k207 flipped = "flip:characters/k207.png"
image k207h = "characters/k207h.png"
image k207h flipped = "flip:characters/k207h.png"
image nova1 = "characters/novaedit.png"
image nova2 = "characters/novaedit.png"
image nova3 = "characters/novaedit.png"
image carguya = "characters/carguya.png"

## Others
image discord = "characters/discord.png"
image nova = "characters/nova.png"
image nova dark = "characters/novadark.png"
image nova flipped = "flip:characters/nova.png"
image nova dark flipped = "flip:characters/novadark.png"
image carguy = "characters/carguy.png"
image carguy flipped = "flip:characters/carguy.png"
image doug = "characters/doug.png"
image cashier = "characters/cashier.png"
image young_cs = "characters/cs_young.png"
image rich = "characters/rich.png"
image ed = "characters/ed.png"
image ed phone = "characters/ed_phone.png"
image wesley = "characters/wesley.png"
image michael = "flip:characters/michael.png"
image phil = "characters/phil.png"
image worker_1 = "characters/worker_corn.png"
image worker_2 = "characters/worker_blank.png"

# updated sprite - tate
image worker_3 = "flip:characters/mean/meanhohsis1.png"

image worker_4 = "characters/worker_eville.png"
image worker_5 = "characters/eddie_down.png"
image worker_5alt = "characters/eddie_up.png"
image worker_6 = "characters/worker_pineapple.png"
image worker_7 = "characters/worker_chicken.png"
image border_guard = "characters/border_guard.png"
image linus = "characters/linus.png"
image asylum_worker = "characters/mohs.png"
image csgod = "characters/csgod.png"
image csgod flipped = "flip:characters/csgod.png"
image copguy = "characters/copguy.png"
image copguy flipped = "flip:characters/copguy.png"
image luke = "characters/luke.png"
image luke flipped = "flip:characters/luke.png"
image border_guard dusk = "characters/border_guard_dusk.png"
image copguy dark = "characters/copguydark.png"
image copguy dark flipped = "flip:characters/copguydark.png"
image copguy_ai = "characters/ai_cop_guy_full.png"
image taran = "characters/taran.png"
image taran flipped = "flip:characters/taran.png"
image colton = "characters/colton.png"
image sheriff = "characters/sheriff.png"
image billy = "characters/billy.png"
image billy car = "characters/billy/billy_car.png"
image billy car happy = "characters/billy/billy_car_happy.png"
image billy car turn = "characters/billy/billy_car_turn.png"
image billy laser = "characters/BillyMaysWithLaser.png"
image peppino = "characters/peppino.png"
image peppino2 = "characters/peppino2.png"
image cultist = "characters/cultist.png"
image cultist gun = "characters/cultistgun.png"
image cultist_2 = "characters/cultist2.png"
image cultist_3 = "characters/cultist2.png"
image scott = "characters/scott.png"
image terry = "characters/terry.png"
image mettaton = "characters/mettaton.png"
image pencilguy = "characters/pencil.png"
image digi = "characters/digi.png"
image digi dark = "characters/digidark.png"
image digi flipped = "flip:characters/digi.png"
image digi dark flipped = "flip:characters/digidark.png"
image trailtrash = "characters/trailtrash.png"
image trailtrash flipped = "flip:characters/trailtrash.png"
image jerma = "characters/jerma.png"
image tsa = "characters/tsa.png"
image lego = "characters/lego.png"
image lego eyes = "characters/legoeyes.png"
image green = "characters/green.png"
image green flipped = "flip:characters/green.png"
image bouncer1 = "characters/bouncer.png"
image bouncer2 = "characters/bouncer.png"
image mika = "characters/mika.png"
image mika dark = "characters/mika.png"
image craptopreal = "characters/laptop.png"
image craptopsmall = "characters/craptop.png"
image craptopsmall flipped = "flip:characters/craptop.png"
image monika = "characters/monika.png"
image kitty = "characters/kitty.png"
image kitty flipped = "flip:characters/kitty.png"
image blank = "characters/blank.png"
image cop = "characters/cop.png"
image cop dark = "characters/copdark.png"
image cop_2 = "characters/copdark.png"
image midge = "characters/midge.png"
image aria = "characters/aria.png"
image aria flipped = "flip:characters/aria.png"
image aria dark = "characters/aria_dark.png"
image aria dark flipped = "flip:characters/aria_dark.png"
image guard_soldier = "characters/guard_soldierdark.png"
image obama = "characters/obama.png"
image db = "characters/db.png"
image nfanboy = "characters/nvidiafanboy.png"
image afanboy = "characters/amdfanboy.png"
image copguycrawl = "characters/copguycrawl.png"
image db_cooper = "characters/db_coopergame.png"
image marine = "characters/marine.png"
image big_tank = "characters/big_tank.png" # TODO: is this meant to reference the abrams or the sherman? - tate
image benrey = "characters/benrey.png"
image howie = "characters/howie.png"
image howie flipped = "flip:characters/howie.png"
image guest = "characters/guest.png"
image janitor = "characters/janitor.png"
image customer = "characters/customer.png"
image ges = "characters/ges.png"
image gordon = "characters/gordon.png"
image hammond = "characters/hammond.png"
image jeremy = "characters/jeremy.png"
image james = "characters/james.png"
image tom = "characters/tom.png"
image scott_pres = "characters/scott_pres.png"
image miku = "characters/miku.png"
image sayori = "characters/sayori.png"
image car = "characters/car.png"
image hart1 = "characters/hart1.png"
image hart2 = "characters/hart2.png"
image waitress = "characters/waitress.png"
image streetguy = "characters/streetguy.png"
image billy dark = "characters/billydark.png"
image gnome = "characters/gnome.png"
image smiley = "characters/smiley.png"
image mario = "characters/mario.png"
image mario flipped = "flip:characters/mario.png"
image violent_jay = "characters/jay.png"
image shaggy_too_dope = "characters/shaggydope.png"
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
image moomin = "characters/moomin.png"
image snufkin = "characters/snufkin.png"
image alicia = "characters/alicia.png"
image witch = "characters/witch.png"
image moomin flipped = "flip:characters/moomin.png"
image snufkin flipped = "flip:characters/snufkin.png"
image alicia flipped = "flip:characters/alicia.png"
image witch flipped = "flip:characters/witch.png"

# Background Images
## CSBI
image game_menu = "gui/game_menu.png"
image black = "bg/black.png"
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

## CSBII
image helipad = "bg/helipad.png"
image jail_inside = "bg/jail_inside.png"
image jail_cell = "bg/jail_cell.png"
image border = "bg/canadian_border.png"
image outside_tim_hortons = "bg/outside_tim_hortons.png"
image inside_tim_hortons_fg = "bg/inside_tim_hortons_fg.png"
image inside_tim_hortons = "bg/inside_tim_hortons.png"
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
image cultforest = "bg/forest_clearing.png"
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
image white = "bg/white.png"
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
image forest_clearing = "bg/forest_clearing.jpg"

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

#Pakoo Jam
image pot_lift = "characters/pot_lift.png"
image pot = "characters/pot.png"
image pot_sunken = "characters/pot_sunken.png"
image pot_beam = "characters/pot_beam.png"
image start_route = "bg/proutest.png"
image cs_room_cars = "bg/cs_bedroom_cars.png"
image wis_forest = "bg/wis_forest.png"
image roombacks = "bg/roombacks.png"
image backrooms = "bg/backrooms.png"
image renovator = "characters/renovator.png"
image hobbytown = "bg/oshkosh.png"
image shadowman = "characters/shadowman.png"
image pencilcashier = "characters/pencilcashier.png"
image cs pencil = "characters/cs/pencil.png"
image cs angry pencil = "characters/cs/pencilangry.png"
image cs disappointed pencil = "characters/cs/pencildisappointed.png"
image pencilroom = "bg/pencilroom.png"
image pencilroomblur = "bg/pencilroomblur.png"
image cult_con = "bg/cult_con.png"
image csgod_angry = "characters/csgod_angry.png"
image cs pissed = "characters/cs/pissed.png"
image cs cultist = "characters/cs/robe.png"
image cs disappointed cultist = "characters/cs/disappointedrobe.png"
image cs angry cultist = "characters/cs/angryrobe.png"
image cs cultist flipped = "flip:characters/cs/robe.png"
image cs disappointed cultist flipped = "flip:characters/cs/disappointedrobe.png"
image cs angry cultist flipped = "flip:characters/cs/angryrobe.png"
image cruise = "characters/tom_cruise.png"
image cruise flipped = "flip:characters/tom_cruise.png"
image blue_branch = "bg/bluebranch.png"
image onscreen_sharpener = "pencilsharpener.png"
image renault = "renault.png"
image renault_inside = "bg/renault_inside.png"

# Static Images
image post_it = "post-it.png"
image ytx = Transform("ytx.png", zoom = 0.333)
image objection = "objection.png"
image hold_it = "hold_it.png"
image scott_border = "scott_border.png"
image cswanted = "wanted_poster.png"
image laser_beam = "laser_beam.png"
image cards1 = "cards1.png"
image cards2 = "cards2.png"
image cards3 = "cards3.png"
image cards4 = "cards4.png"
image cards5 = "cards5.png"
image con_screen = "bg/con_screen.png"
image case = "briefcase.png"
image case flipped = "flip:briefcase.png"
image bag = "bodybag.png"
image bag flipped = "flip:bodybag.png"
image drill = "drillymays.png"
image drillbreak = "drillymaysfuck.png"
image sansbrick = "sansbrick.png"
image oldgame = "oldgame.png"
image m4 = "m4.png"
image m4 flipped = "flip:m4.png"
image m4 fire = "m4fire.png"
image m4 fire flipped = "flip:m4fire.png"
image script = "secret/script.png"
image post_it2 = "secret/post-it2.png"
image colorbars = "colorbars.png"
image paper = "paper.png"
image pipe_gun = "pipe_gun.png"
image pipe_gun flipped = "flip:pipe_gun.png"
image cheetos = "cheetos.png"
image bear = "bear.png"
image dog = "dog.png"
image pig = "pig.png"

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
image woc = Movie(play="movies/woc.webm")
image where = Movie(play="movies/wherearetheynow.webm")
image karaoke = Transform(Movie(play = "movies/karaoke.webm", side_mask = True), zoom = 1.5)
image bad_end_screen = Transform(Movie(play = "movies/bad_ending.webm", side_mask = True, loop=False, image="images/fail_end.png"), size=(1920,1080))

#Fun Values
image utajsign = "secret/utajsign.png"
image vegasjade = "secret/vegasjade.png"
image vegasjade2 = "secret/vegasjade2.png"
image fumobee = "secret/fumobee.png"
image fumobee2 = "secret/fumobee2.png"
image cards5alt = "secret/cards5alt.png"
image lancer = "secret/lancer.png"
image lancer flipped = "flip:secret/lancer.png"
image bubble = Transform("secret/bubble.png", zoom = 2.0)

# Animated Sprites
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

image ai_ducks = SnowBlossom("duck.png", 50)

# Layers?
define config.detached_layers += ["broadcast"]
image stage_screen = Window(Layer("broadcast", clipping = False), background = "minigames/pencil/stage.png")

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
                imagebutton auto "menu/csbi_%s.png" hover_sound "sfx_select.wav":
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx_valid.wav"), Hide("chapter_menu", Fade(1.0)), Jump("csbi_start")
                imagebutton auto "menu/csbii_%s.png" hover_sound "sfx_select.wav":
                    sensitive persistent.csb2_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx_valid.wav"), Hide("chapter_menu", Fade(1.0)), Jump("csbii_start")
                imagebutton auto "menu/csbiii1_%s.png" hover_sound "sfx_select.wav":
                    sensitive persistent.csb3a_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx_valid.wav"), Hide("chapter_menu", Fade(1.0)), Jump("csbiii_start")
                imagebutton auto "menu/csbiii2_%s.png" hover_sound "sfx_select.wav":
                    sensitive persistent.csb3b_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx_valid.wav"), Hide("chapter_menu", Fade(1.0)), Jump("choose_direction")
style start_window is empty

label splashscreen:
    $ renpy.movie_cutscene("movies/splash.webm")
    $ persistent.seen_splash = True
    $ persistent.heard.add("BUBBLE TEA - darkcat")
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
            $ renpy.music.play("bubble_tea.mp3", loop = False)
    else:
        if not renpy.music.is_playing():
            $ renpy.music.play("<from 16.53>bubble_tea.mp3", loop = False)
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
    show screen warning("The following scene sucks.", "Warnings: test", "secret")
    dxcom 1
    $ typewriter_text = "Here is some text, bitch\nI have no clue if it works\nI sure hope it does!"
    show typewriter
    pause
    show copguy_ex
    show red_light
    show blue_light
    pause
    $ renpy.full_restart()

define shake1 = { "master" : hpunch }
define shake2 = { "master" : vpunch }
