init python:
    # For unused assets gallery
    unused_page = 0

    # For jukebox tagging
    current_jukebox_tag_index = 0

    # For bios page
    current_bios_sorting_mode = 0
    current_bios_sprite = 0

# If music is so good, why is there no Music 2?
init python:
    renpy.music.register_channel("sound2", "sfx")
    renpy.music.register_channel("music4", "music")
    renpy.music.register_channel("music3", "music")
    renpy.music.register_channel("music2", "music", movie=True)
    renpy.music.register_channel("jukebox", "music")
    renpy.music.register_channel("notification", "sfx")
    renpy.music.register_channel("dxcom", "voice")

init 10 python:
    def unlock_all():
        for m in MUSIC_MAP.keys():
            persistent.heard.add(m)
        for p in name_map.keys():
            persistent.seen.add(p)
        for i in ITEM_MAP.keys():
            persistent.collected.add(i)
        achievement_manager.unlock_all()
        persistent.true_ending = True
        persistent.csb2_unlocked = True
        persistent.csb3a_unlocked = True
        persistent.csb3b_unlocked = True
        persistent.carrot_game_unlocked = True
        persistent.reversi_game_unlocked = True
        persistent.saved_christmas = True
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

# CSBI Character Definitions (Including HoH SiS)
define carguy = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", beep = "nice"))
define carguy_nobeep = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", play_beeps = False))
define michael = Character("Michael", callback = renpy.partial(char_callback, name = "michael", beep = "mich"))
define michael_nobeep = Character("Michael", callback = renpy.partial(char_callback, name = "michael", play_beeps = False))

## HoH SiS
define ed = Character("Ed", callback = renpy.partial(char_callback, name = "ed", beep = "ed"))
define rich = Character("Richard", callback = renpy.partial(char_callback, name = "rich", beep = "rich"))
define wesley = Character("Wesley", callback = renpy.partial(char_callback, name = "wesley", beep = "wes"))

# CSBII Character Definitions
define copguy = Character("Copguy", callback = renpy.partial(char_callback, name = "copguy", beep = "cop"))
define linus = Character("Linus", callback = renpy.partial(char_callback, name = "linus", beep = "ltt"))

# CSBIII Part 1 Character Definitions
define luke = Character("Luke", callback = renpy.partial(char_callback, name = "luke", beep = "luke"))
define sheriff = Character("Sheriff", callback = renpy.partial(char_callback, name = "sheriff", beep = "sheriff"))

# CSBIII Friend Route Character Definitions (NPCs only, friends have their own section)
define obama = Character("Obama", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))

# CSBIII East Route Character Definitions
define billy = Character("Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))

# CSBIII Fired Route Character Definitions
define customer = Character("Customer", callback = char_callback)
define ges = Character("Ges", callback = renpy.partial(char_callback, name = "ges", beep = "ges"))

# CSBIII Country Route Character Definitons
define pomni = Character("Pomni", callback = renpy.partial(char_callback, name = "pomni", beep = "pomni"))

# Archival Ending Character Definitions
define k174 = Character("K17-M4", callback = renpy.partial(char_callback, name = "k174", beep = "k17"))

# DX Holiday Special Definitions
define avgn = Character("James Rolfe", callback = renpy.partial(char_callback, name = "avgn", beep = "avgn"))
define tgt_worker = Character("Target Employee", callback = renpy.partial(char_callback, name = "tgt_worker", beep="pak"))
define walkie = Character("Walkie", callback = renpy.partial(char_callback, beep = "walkie"))
define everyone = Character("Everyone", callback = renpy.partial(char_callback, beep = "everyone"))
define everyone2 = Character("Everyone", callback = renpy.partial(char_callback, beep = "csbama17"))
define santa = Character("Santa Claus", callback = renpy.partial(char_callback, name = "santa", beep = "santa"))
define mike = Character("Mike",  callback = renpy.partial(char_callback, name = "mike", beep = "mike"))

# DX Albu
define cs_nobeep = Character("cs188", callback = renpy.partial(char_callback, name = "cs", play_beeps = False))

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
define iris = Character("Iris", callback = renpy.partial(char_callback, name = "iris", beep = "iris"))
define k17 = Character("K-17", callback = renpy.partial(char_callback, name = "k17", beep = "k17"))
define k22 = Character("K-22", callback = renpy.partial(char_callback, name = "k22", beep = "k20"))
define kitty = Character("Kitty", callback = renpy.partial(char_callback, name = "kitty", beep = "kitty"))
define mean = Character("Mean", callback = renpy.partial(char_callback, name = "mean_human", beep = "mean"))
define midge = Character("Midge", callback = renpy.partial(char_callback, name = "midge", beep = "midge"))
define mika = Character("Mika", callback = renpy.partial(char_callback, name = "mika", beep = "mika"))
define nova = Character("Nova", callback = renpy.partial(char_callback, name = "nova"))
define pakoo = Character("Pakoo", callback = renpy.partial(char_callback, name = "addy", beep = "pak"))
define tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"))

# Character Images
## CS
### BASE
image cs = "characters/cs/base/neutral.png"
image cs flipped = "flip:characters/cs/base/neutral.png"
image cs dark = "dark:characters/cs/base/neutral.png"
image cs dark flipped = "dark:flip:characters/cs/base/neutral.png"
image cs dusk = "dusk:characters/cs/base/neutral.png"
image cs dusk flipped = "dusk:flip:characters/cs/base/neutral.png"
image cs angry = "characters/cs/base/angry.png"
image cs angry flipped = "flip:characters/cs/base/angry.png"
image cs angry dark = "dark:characters/cs/base/angry.png"
image cs angry dark flipped = "dark:flip:characters/cs/base/angry.png"
image cs angry dusk = "dusk:characters/cs/base/angry.png"
image cs angry dusk flipped = "dusk:flip:characters/cs/base/angry.png"
image cs concentrate = "characters/cs/base/concentrate.png"
image cs concentrate flipped = "flip:characters/cs/base/concentrate.png"
image cs concentrate dark = "dark:characters/cs/base/concentrate.png"
image cs concentrate dark flipped = "dark:flip:characters/cs/base/concentrate.png"
image cs concentrate dusk = "dusk:characters/cs/base/concentrate.png"
image cs concentrate dusk flipped = "dusk:flip:characters/cs/base/concentrate.png"
image cs disappointed = "characters/cs/base/disappointed.png"
image cs disappointed flipped = "flip:characters/cs/base/disappointed.png"
image cs disappointed dark = "dark:characters/cs/base/disappointed.png"
image cs disappointed dark flipped = "dark:flip:characters/cs/base/disappointed.png"
image cs disappointed dusk = "dusk:characters/cs/base/disappointed.png"
image cs disappointed dusk flipped = "dusk:flip:characters/cs/base/disappointed.png"
image cs happy = "characters/cs/base/happy.png"
image cs happy flipped = "flip:characters/cs/base/happy.png"
image cs happy dark = "dark:characters/cs/base/happy.png"
image cs happy dark flipped = "dark:flip:characters/cs/base/happy.png"
image cs happy dusk = "dusk:characters/cs/base/happy.png"
image cs happy dusk flipped = "dusk:flip:characters/cs/base/happy.png"
image cs pissed = "characters/cs/base/pissed.png"
image cs pissed flipped = "flip:characters/cs/base/pissed.png"
image cs pissed dark = "dark:characters/cs/base/pissed.png"
image cs pissed dark flipped = "dark:flip:characters/cs/base/pissed.png"
image cs pissed dusk = "dusk:characters/cs/base/pissed.png"
image cs pissed dusk flipped = "dusk:flip:characters/cs/base/pissed.png"
image cs scared = "characters/cs/base/scared.png"
image cs scared flipped = "flip:characters/cs/base/scared.png"
image cs scared dark = "dark:characters/cs/base/scared.png"
image cs scared dark flipped = "dark:flip:characters/cs/base/scared.png"
image cs scared dusk = "dusk:characters/cs/base/scared.png"
image cs scared dusk flipped = "dusk:flip:characters/cs/base/scared.png"
image cs surprised = "characters/cs/base/surprised.png"
image cs surprised flipped  = "flip:characters/cs/base/surprised.png"
image cs surprised dark = "dark:characters/cs/base/surprised.png"
image cs surprised dark flipped = "dark:flip:characters/cs/base/surprised.png"
image cs surprised dusk = "dusk:characters/cs/base/surprised.png"
image cs surprised dusk flipped = "dusk:flip:characters/cs/base/surprised.png"
image cs worried = "characters/cs/base/worried.png"
image cs worried flipped = "flip:characters/cs/base/worried.png"
image cs worried dark = "dark:characters/cs/base/worried.png"
image cs worried dark flipped = "dark:flip:characters/cs/base/worried.png"
image cs worried dusk = "dusk:characters/cs/base/worried.png"
image cs worried dusk flipped = "dusk:flip:characters/cs/base/worried.png"

### FULL
image cs full = "characters/cs/full/neutral.png"
image cs full flipped = "flip:characters/cs/full/neutral.png"
image cs full dark = "dark:characters/cs/full/neutral.png"
image cs full dark flipped = "dark:flip:characters/cs/full/neutral.png"
image cs full dusk = "dusk:characters/cs/full/neutral.png"
image cs full dusk flipped = "dusk:flip:characters/cs/full/neutral.png"
image cs angry full = "characters/cs/full/angry.png"
image cs angry full flipped = "flip:characters/cs/full/angry.png"
image cs angry full dark = "dark:characters/cs/full/angry.png"
image cs angry full dark flipped = "dark:flip:characters/cs/full/angry.png"
image cs angry full dusk = "dusk:characters/cs/full/angry.png"
image cs angry full dusk flipped = "dusk:flip:characters/cs/full/angry.png"
image cs concentrate full = "characters/cs/full/concentrate.png"
image cs concentrate full flipped = "flip:characters/cs/full/concentrate.png"
image cs concentrate full dark = "dark:characters/cs/full/concentrate.png"
image cs concentrate full dark flipped = "dark:flip:characters/cs/full/concentrate.png"
image cs concentrate full dusk = "dusk:characters/cs/full/concentrate.png"
image cs concentrate full dusk flipped = "dusk:flip:characters/cs/full/concentrate.png"
image cs disappointed full = "characters/cs/full/disappointed.png"
image cs disappointed full flipped = "flip:characters/cs/full/disappointed.png"
image cs disappointed full dark = "dark:characters/cs/full/disappointed.png"
image cs disappointed full dark flipped = "dark:flip:characters/cs/full/disappointed.png"
image cs disappointed full dusk = "dusk:characters/cs/full/disappointed.png"
image cs disappointed full dusk flipped = "dusk:flip:characters/cs/full/disappointed.png"
image cs happy full = "characters/cs/full/happy.png"
image cs happy full flipped = "flip:characters/cs/full/happy.png"
image cs happy full dark = "dark:characters/cs/full/happy.png"
image cs happy full dark flipped = "dark:flip:characters/cs/full/happy.png"
image cs happy full dusk = "dusk:characters/cs/full/happy.png"
image cs happy full dusk flipped = "dusk:flip:characters/cs/full/happy.png"
image cs pissed full = "characters/cs/full/pissed.png"
image cs pissed full flipped = "flip:characters/cs/full/pissed.png"
image cs pissed full dark = "dark:characters/cs/full/pissed.png"
image cs pissed full dark flipped = "dark:flip:characters/cs/full/pissed.png"
image cs pissed full dusk = "dusk:characters/cs/full/pissed.png"
image cs pissed full dusk flipped = "dusk:flip:characters/cs/full/pissed.png"
image cs scared full = "characters/cs/full/scared.png"
image cs scared full flipped = "flip:characters/cs/full/scared.png"
image cs scared full dark = "dark:characters/cs/full/scared.png"
image cs scared full dark flipped = "dark:flip:characters/cs/full/scared.png"
image cs scared full dusk = "dusk:characters/cs/full/scared.png"
image cs scared full dusk flipped = "dusk:flip:characters/cs/full/scared.png"
image cs surprised full = "characters/cs/full/surprised.png"
image cs surprised full flipped  = "flip:characters/cs/full/surprised.png"
image cs surprised full dark = "dark:characters/cs/full/surprised.png"
image cs surprised full dark flipped = "dark:flip:characters/cs/full/surprised.png"
image cs surprised full dusk = "dusk:characters/cs/full/surprised.png"
image cs surprised full dusk flipped = "dusk:flip:characters/cs/full/surprised.png"
image cs worried full = "characters/cs/full/worried.png"
image cs worried full flipped = "flip:characters/cs/full/worried.png"
image cs worried full dark = "dark:characters/cs/full/worried.png"
image cs worried full dark flipped = "dark:flip:characters/cs/full/worried.png"
image cs worried full dusk = "dusk:characters/cs/full/worried.png"
image cs worried full dusk flipped = "dusk:flip:characters/cs/full/worried.png"

### CHRISTMAS
image cs christmas = "characters/cs/christmas/neutral.png"
image cs christmas flipped = "flip:characters/cs/christmas/neutral.png"
image cs christmas dark = "dark:characters/cs/christmas/neutral.png"
image cs christmas dark flipped = "dark:flip:characters/cs/christmas/neutral.png"
image cs christmas dusk = "dusk:characters/cs/christmas/neutral.png"
image cs christmas dusk flipped = "dusk:flip:characters/cs/christmas/neutral.png"
image cs angry christmas = "characters/cs/christmas/angry.png"
image cs angry christmas flipped = "flip:characters/cs/christmas/angry.png"
image cs angry christmas dark = "dark:characters/cs/christmas/angry.png"
image cs angry christmas dark flipped = "dark:flip:characters/cs/christmas/angry.png"
image cs angry christmas dusk = "dusk:characters/cs/christmas/angry.png"
image cs angry christmas dusk flipped = "dusk:flip:characters/cs/christmas/angry.png"
image cs concentrate christmas = "characters/cs/christmas/concentrate.png"
image cs concentrate christmas flipped = "flip:characters/cs/christmas/concentrate.png"
image cs concentrate christmas dark = "dark:characters/cs/christmas/concentrate.png"
image cs concentrate christmas dark flipped = "dark:flip:characters/cs/christmas/concentrate.png"
image cs concentrate christmas dusk = "dusk:characters/cs/christmas/concentrate.png"
image cs concentrate christmas dusk flipped = "dusk:flip:characters/cs/christmas/concentrate.png"
image cs disappointed christmas = "characters/cs/christmas/disappointed.png"
image cs disappointed christmas flipped = "flip:characters/cs/christmas/disappointed.png"
image cs disappointed christmas dark = "dark:characters/cs/christmas/disappointed.png"
image cs disappointed christmas dark flipped = "dark:flip:characters/cs/christmas/disappointed.png"
image cs disappointed christmas dusk = "dusk:characters/cs/christmas/disappointed.png"
image cs disappointed christmas dusk flipped = "dusk:flip:characters/cs/christmas/disappointed.png"
image cs happy christmas = "characters/cs/christmas/happy.png"
image cs happy christmas flipped = "flip:characters/cs/christmas/happy.png"
image cs happy christmas dark = "dark:characters/cs/christmas/happy.png"
image cs happy christmas dark flipped = "dark:flip:characters/cs/christmas/happy.png"
image cs happy christmas dusk = "dusk:characters/cs/christmas/happy.png"
image cs happy christmas dusk flipped = "dusk:flip:characters/cs/christmas/happy.png"
image cs pissed christmas = "characters/cs/christmas/pissed.png"
image cs pissed christmas flipped = "flip:characters/cs/christmas/pissed.png"
image cs pissed christmas dark = "dark:characters/cs/christmas/pissed.png"
image cs pissed christmas dark flipped = "dark:flip:characters/cs/christmas/pissed.png"
image cs pissed christmas dusk = "dusk:characters/cs/christmas/pissed.png"
image cs pissed christmas dusk flipped = "dusk:flip:characters/cs/christmas/pissed.png"
image cs scared christmas = "characters/cs/christmas/scared.png"
image cs scared christmas flipped = "flip:characters/cs/christmas/scared.png"
image cs scared christmas dark = "dark:characters/cs/christmas/scared.png"
image cs scared christmas dark flipped = "dark:flip:characters/cs/christmas/scared.png"
image cs scared christmas dusk = "dusk:characters/cs/christmas/scared.png"
image cs scared christmas dusk flipped = "dusk:flip:characters/cs/christmas/scared.png"
image cs surprised christmas = "characters/cs/christmas/surprised.png"
image cs surprised christmas flipped  = "flip:characters/cs/christmas/surprised.png"
image cs surprised christmas dark = "dark:characters/cs/christmas/surprised.png"
image cs surprised christmas dark flipped = "dark:flip:characters/cs/christmas/surprised.png"
image cs surprised christmas dusk = "dusk:characters/cs/christmas/surprised.png"
image cs surprised christmas dusk flipped = "dusk:flip:characters/cs/christmas/surprised.png"
image cs worried christmas = "characters/cs/christmas/worried.png"
image cs worried christmas flipped = "flip:characters/cs/christmas/worried.png"
image cs worried christmas dark = "dark:characters/cs/christmas/worried.png"
image cs worried christmas dark flipped = "dark:flip:characters/cs/christmas/worried.png"
image cs worried christmas dusk = "dusk:characters/cs/christmas/worried.png"
image cs worried christmas dusk flipped = "dusk:flip:characters/cs/christmas/worried.png"

### CHRISTMAS FULL
image cs christmas full = "characters/cs/christmas_full/neutral.png"
image cs christmas full flipped = "flip:characters/cs/christmas_full/neutral.png"
image cs christmas full dark = "dark:characters/cs/christmas_full/neutral.png"
image cs christmas full dark flipped = "dark:flip:characters/cs/christmas_full/neutral.png"
image cs christmas full dusk = "dusk:characters/cs/christmas_full/neutral.png"
image cs christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/neutral.png"
image cs angry christmas full = "characters/cs/christmas_full/angry.png"
image cs angry christmas full flipped = "flip:characters/cs/christmas_full/angry.png"
image cs angry christmas full dark = "dark:characters/cs/christmas_full/angry.png"
image cs angry christmas full dark flipped = "dark:flip:characters/cs/christmas_full/angry.png"
image cs angry christmas full dusk = "dusk:characters/cs/christmas_full/angry.png"
image cs angry christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/angry.png"
image cs concentrate christmas full = "characters/cs/christmas_full/concentrate.png"
image cs concentrate christmas full flipped = "flip:characters/cs/christmas_full/concentrate.png"
image cs concentrate christmas full dark = "dark:characters/cs/christmas_full/concentrate.png"
image cs concentrate christmas full dark flipped = "dark:flip:characters/cs/christmas_full/concentrate.png"
image cs concentrate christmas full dusk = "dusk:characters/cs/christmas_full/concentrate.png"
image cs concentrate christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/concentrate.png"
image cs disappointed christmas full = "characters/cs/christmas_full/disappointed.png"
image cs disappointed christmas full flipped = "flip:characters/cs/christmas_full/disappointed.png"
image cs disappointed christmas full dark = "dark:characters/cs/christmas_full/disappointed.png"
image cs disappointed christmas full dark flipped = "dark:flip:characters/cs/christmas_full/disappointed.png"
image cs disappointed christmas full dusk = "dusk:characters/cs/christmas_full/disappointed.png"
image cs disappointed christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/disappointed.png"
image cs happy christmas full = "characters/cs/christmas_full/happy.png"
image cs happy christmas full flipped = "flip:characters/cs/christmas_full/happy.png"
image cs happy christmas full dark = "dark:characters/cs/christmas_full/happy.png"
image cs happy christmas full dark flipped = "dark:flip:characters/cs/christmas_full/happy.png"
image cs happy christmas full dusk = "dusk:characters/cs/christmas_full/happy.png"
image cs happy christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/happy.png"
image cs pissed christmas full = "characters/cs/christmas_full/pissed.png"
image cs pissed christmas full flipped = "flip:characters/cs/christmas_full/pissed.png"
image cs pissed christmas full dark = "dark:characters/cs/christmas_full/pissed.png"
image cs pissed christmas full dark flipped = "dark:flip:characters/cs/christmas_full/pissed.png"
image cs pissed christmas full dusk = "dusk:characters/cs/christmas_full/pissed.png"
image cs pissed christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/pissed.png"
image cs scared christmas full = "characters/cs/christmas_full/scared.png"
image cs scared christmas full flipped = "flip:characters/cs/christmas_full/scared.png"
image cs scared christmas full dark = "dark:characters/cs/christmas_full/scared.png"
image cs scared christmas full dark flipped = "dark:flip:characters/cs/christmas_full/scared.png"
image cs scared christmas full dusk = "dusk:characters/cs/christmas_full/scared.png"
image cs scared christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/scared.png"
image cs surprised christmas full = "characters/cs/christmas_full/surprised.png"
image cs surprised christmas full flipped  = "flip:characters/cs/christmas_full/surprised.png"
image cs surprised christmas full dark = "dark:characters/cs/christmas_full/surprised.png"
image cs surprised christmas full dark flipped = "dark:flip:characters/cs/christmas_full/surprised.png"
image cs surprised christmas full dusk = "dusk:characters/cs/christmas_full/surprised.png"
image cs surprised christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/surprised.png"
image cs worried christmas full = "characters/cs/christmas_full/worried.png"
image cs worried christmas full flipped = "flip:characters/cs/christmas_full/worried.png"
image cs worried christmas full dark = "dark:characters/cs/christmas_full/worried.png"
image cs worried christmas full dark flipped = "dark:flip:characters/cs/christmas_full/worried.png"
image cs worried christmas full dusk = "dusk:characters/cs/christmas_full/worried.png"
image cs worried christmas full dusk flipped = "dusk:flip:characters/cs/christmas_full/worried.png"

### COAT
image cs coat = "characters/cs/coat/neutral.png"
image cs coat flipped = "flip:characters/cs/coat/neutral.png"
image cs coat dark = "dark:characters/cs/coat/neutral.png"
image cs coat dark flipped = "dark:flip:characters/cs/coat/neutral.png"
image cs coat dusk = "dusk:characters/cs/coat/neutral.png"
image cs coat dusk flipped = "dusk:flip:characters/cs/coat/neutral.png"
image cs angry coat = "characters/cs/coat/angry.png"
image cs angry coat flipped = "flip:characters/cs/coat/angry.png"
image cs angry coat dark = "dark:characters/cs/coat/angry.png"
image cs angry coat dark flipped = "dark:flip:characters/cs/coat/angry.png"
image cs angry coat dusk = "dusk:characters/cs/coat/angry.png"
image cs angry coat dusk flipped = "dusk:flip:characters/cs/coat/angry.png"
image cs concentrate coat = "characters/cs/coat/concentrate.png"
image cs concentrate coat flipped = "flip:characters/cs/coat/concentrate.png"
image cs concentrate coat dark = "dark:characters/cs/coat/concentrate.png"
image cs concentrate coat dark flipped = "dark:flip:characters/cs/coat/concentrate.png"
image cs concentrate coat dusk = "dusk:characters/cs/coat/concentrate.png"
image cs concentrate coat dusk flipped = "dusk:flip:characters/cs/coat/concentrate.png"
image cs disappointed coat = "characters/cs/coat/disappointed.png"
image cs disappointed coat flipped = "flip:characters/cs/coat/disappointed.png"
image cs disappointed coat dark = "dark:characters/cs/coat/disappointed.png"
image cs disappointed coat dark flipped = "dark:flip:characters/cs/coat/disappointed.png"
image cs disappointed coat dusk = "dusk:characters/cs/coat/disappointed.png"
image cs disappointed coat dusk flipped = "dusk:flip:characters/cs/coat/disappointed.png"
image cs happy coat = "characters/cs/coat/happy.png"
image cs happy coat flipped = "flip:characters/cs/coat/happy.png"
image cs happy coat dark = "dark:characters/cs/coat/happy.png"
image cs happy coat dark flipped = "dark:flip:characters/cs/coat/happy.png"
image cs happy coat dusk = "dusk:characters/cs/coat/happy.png"
image cs happy coat dusk flipped = "dusk:flip:characters/cs/coat/happy.png"
image cs pissed coat = "characters/cs/coat/pissed.png"
image cs pissed coat flipped = "flip:characters/cs/coat/pissed.png"
image cs pissed coat dark = "dark:characters/cs/coat/pissed.png"
image cs pissed coat dark flipped = "dark:flip:characters/cs/coat/pissed.png"
image cs pissed coat dusk = "dusk:characters/cs/coat/pissed.png"
image cs pissed coat dusk flipped = "dusk:flip:characters/cs/coat/pissed.png"
image cs scared coat = "characters/cs/coat/scared.png"
image cs scared coat flipped = "flip:characters/cs/coat/scared.png"
image cs scared coat dark = "dark:characters/cs/coat/scared.png"
image cs scared coat dark flipped = "dark:flip:characters/cs/coat/scared.png"
image cs scared coat dusk = "dusk:characters/cs/coat/scared.png"
image cs scared coat dusk flipped = "dusk:flip:characters/cs/coat/scared.png"
image cs coat surprised  = "characters/cs/coat/surprised.png"
image cs coat surprised flipped  = "flip:characters/cs/coat/surprised.png"
image cs coat surprised dark = "dark:characters/cs/coat/surprised.png"
image cs coat surprised dark flipped = "dark:flip:characters/cs/coat/surprised.png"
image cs coat surprised dusk = "dusk:characters/cs/coat/surprised.png"
image cs coat surprised dusk flipped = "dusk:flip:characters/cs/coat/surprised.png"
image cs worried coat = "characters/cs/coat/worried.png"
image cs worried coat flipped = "flip:characters/cs/coat/worried.png"
image cs worried coat dark = "dark:characters/cs/coat/worried.png"
image cs worried coat dark flipped = "dark:flip:characters/cs/coat/worried.png"
image cs worried coat dusk = "dusk:characters/cs/coat/worried.png"
image cs worried coat dusk flipped = "dusk:flip:characters/cs/coat/worried.png"

### COAT HAT
image cs coat hat = "characters/cs/coat_hat/neutral.png"
image cs coat hat flipped = "flip:characters/cs/coat_hat/neutral.png"
image cs coat hat dark = "dark:characters/cs/coat_hat/neutral.png"
image cs coat hat dark flipped = "dark:flip:characters/cs/coat_hat/neutral.png"
image cs coat hat dusk = "dusk:characters/cs/coat_hat/neutral.png"
image cs coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/neutral.png"
image cs angry coat hat = "characters/cs/coat_hat/angry.png"
image cs angry coat hat flipped = "flip:characters/cs/coat_hat/angry.png"
image cs angry coat hat dark = "dark:characters/cs/coat_hat/angry.png"
image cs angry coat hat dark flipped = "dark:flip:characters/cs/coat_hat/angry.png"
image cs angry coat hat dusk = "dusk:characters/cs/coat_hat/angry.png"
image cs angry coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/angry.png"
image cs concentrate coat hat = "characters/cs/coat_hat/concentrate.png"
image cs concentrate coat hat flipped = "flip:characters/cs/coat_hat/concentrate.png"
image cs concentrate coat hat dark = "dark:characters/cs/coat_hat/concentrate.png"
image cs concentrate coat hat dark flipped = "dark:flip:characters/cs/coat_hat/concentrate.png"
image cs concentrate coat hat dusk = "dusk:characters/cs/coat_hat/concentrate.png"
image cs concentrate coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/concentrate.png"
image cs disappointed coat hat = "characters/cs/coat_hat/disappointed.png"
image cs disappointed coat hat flipped = "flip:characters/cs/coat_hat/disappointed.png"
image cs disappointed coat hat dark = "dark:characters/cs/coat_hat/disappointed.png"
image cs disappointed coat hat dark flipped = "dark:flip:characters/cs/coat_hat/disappointed.png"
image cs disappointed coat hat dusk = "dusk:characters/cs/coat_hat/disappointed.png"
image cs disappointed coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/disappointed.png"
image cs happy coat hat = "characters/cs/coat_hat/happy.png"
image cs happy coat hat flipped = "flip:characters/cs/coat_hat/happy.png"
image cs happy coat hat dark = "dark:characters/cs/coat_hat/happy.png"
image cs happy coat hat dark flipped = "dark:flip:characters/cs/coat_hat/happy.png"
image cs happy coat hat dusk = "dusk:characters/cs/coat_hat/happy.png"
image cs happy coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/happy.png"
image cs pissed coat hat = "characters/cs/coat_hat/pissed.png"
image cs pissed coat hat flipped = "flip:characters/cs/coat_hat/pissed.png"
image cs pissed coat hat dark = "dark:characters/cs/coat_hat/pissed.png"
image cs pissed coat hat dark flipped = "dark:flip:characters/cs/coat_hat/pissed.png"
image cs pissed coat hat dusk = "dusk:characters/cs/coat_hat/pissed.png"
image cs pissed coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/pissed.png"
image cs scared coat hat = "characters/cs/coat_hat/scared.png"
image cs scared coat hat flipped = "flip:characters/cs/coat_hat/scared.png"
image cs scared coat hat dark = "dark:characters/cs/coat_hat/scared.png"
image cs scared coat hat dark flipped = "dark:flip:characters/cs/coat_hat/scared.png"
image cs scared coat hat dusk = "dusk:characters/cs/coat_hat/scared.png"
image cs scared coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/scared.png"
image cs surprised coat hat = "characters/cs/coat_hat/surprised.png"
image cs surprised coat hat flipped  = "flip:characters/cs/coat_hat/surprised.png"
image cs surprised coat hat dark = "dark:characters/cs/coat_hat/surprised.png"
image cs surprised coat hat dark flipped = "dark:flip:characters/cs/coat_hat/surprised.png"
image cs surprised coat hat dusk = "dusk:characters/cs/coat_hat/surprised.png"
image cs surprised coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/surprised.png"
image cs worried coat hat = "characters/cs/coat_hat/worried.png"
image cs worried coat hat flipped = "flip:characters/cs/coat_hat/worried.png"
image cs worried coat hat dark = "dark:characters/cs/coat_hat/worried.png"
image cs worried coat hat dark flipped = "dark:flip:characters/cs/coat_hat/worried.png"
image cs worried coat hat dusk = "dusk:characters/cs/coat_hat/worried.png"
image cs worried coat hat dusk flipped = "dusk:flip:characters/cs/coat_hat/worried.png"

### PHONE
image cs phone = "characters/cs/phone/neutral.png"
image cs phone flipped = "flip:characters/cs/phone/neutral.png"
image cs phone dark = "dark:characters/cs/phone/neutral.png"
image cs phone dark flipped = "dark:flip:characters/cs/phone/neutral.png"
image cs phone dusk = "dusk:characters/cs/phone/neutral.png"
image cs phone dusk flipped = "dusk:flip:characters/cs/phone/neutral.png"
image cs angry phone = "characters/cs/phone/angry.png"
image cs angry phone flipped = "flip:characters/cs/phone/angry.png"
image cs angry phone dark = "dark:characters/cs/phone/angry.png"
image cs angry phone dark flipped = "dark:flip:characters/cs/phone/angry.png"
image cs angry phone dusk = "dusk:characters/cs/phone/angry.png"
image cs angry phone dusk flipped = "dusk:flip:characters/cs/phone/angry.png"
image cs concentrate phone = "characters/cs/phone/concentrate.png"
image cs concentrate phone flipped = "flip:characters/cs/phone/concentrate.png"
image cs concentrate phone dark = "dark:characters/cs/phone/concentrate.png"
image cs concentrate phone dark flipped = "dark:flip:characters/cs/phone/concentrate.png"
image cs concentrate phone dusk = "dusk:characters/cs/phone/concentrate.png"
image cs concentrate phone dusk flipped = "dusk:flip:characters/cs/phone/concentrate.png"
image cs disappointed phone = "characters/cs/phone/disappointed.png"
image cs disappointed phone flipped = "flip:characters/cs/phone/disappointed.png"
image cs disappointed phone dark = "dark:characters/cs/phone/disappointed.png"
image cs disappointed phone dark flipped = "dark:flip:characters/cs/phone/disappointed.png"
image cs disappointed phone dusk = "dusk:characters/cs/phone/disappointed.png"
image cs disappointed phone dusk flipped = "dusk:flip:characters/cs/phone/disappointed.png"
image cs happy phone = "characters/cs/phone/happy.png"
image cs happy phone flipped = "flip:characters/cs/phone/happy.png"
image cs happy phone dark = "dark:characters/cs/phone/happy.png"
image cs happy phone dark flipped = "dark:flip:characters/cs/phone/happy.png"
image cs happy phone dusk = "dusk:characters/cs/phone/happy.png"
image cs happy phone dusk flipped = "dusk:flip:characters/cs/phone/happy.png"
image cs pissed phone = "characters/cs/phone/pissed.png"
image cs pissed phone flipped = "flip:characters/cs/phone/pissed.png"
image cs pissed phone dark = "dark:characters/cs/phone/pissed.png"
image cs pissed phone dark flipped = "dark:flip:characters/cs/phone/pissed.png"
image cs pissed phone dusk = "dusk:characters/cs/phone/pissed.png"
image cs pissed phone dusk flipped = "dusk:flip:characters/cs/phone/pissed.png"
image cs scared phone = "characters/cs/phone/scared.png"
image cs scared phone flipped = "flip:characters/cs/phone/scared.png"
image cs scared phone dark = "dark:characters/cs/phone/scared.png"
image cs scared phone dark flipped = "dark:flip:characters/cs/phone/scared.png"
image cs scared phone dusk = "dusk:characters/cs/phone/scared.png"
image cs scared phone dusk flipped = "dusk:flip:characters/cs/phone/scared.png"
image cs surprised phone = "characters/cs/phone/surprised.png"
image cs surprised phone flipped  = "flip:characters/cs/phone/surprised.png"
image cs surprised phone dark = "dark:characters/cs/phone/surprised.png"
image cs surprised phone dark flipped = "dark:flip:characters/cs/phone/surprised.png"
image cs surprised phone dusk = "dusk:characters/cs/phone/surprised.png"
image cs surprised phone dusk flipped = "dusk:flip:characters/cs/phone/surprised.png"
image cs worried phone = "characters/cs/phone/worried.png"
image cs worried phone flipped = "flip:characters/cs/phone/worried.png"
image cs worried phone dark = "dark:characters/cs/phone/worried.png"
image cs worried phone dark flipped = "dark:flip:characters/cs/phone/worried.png"
image cs worried phone dusk = "dusk:characters/cs/phone/worried.png"
image cs worried phone dusk flipped = "dusk:flip:characters/cs/phone/worried.png"

image cs sil_black = "sil_black:characters/cs/base/neutral.png"
image cs sil_black flipped = "sil_black:flip:characters/cs/base/neutral.png"

## Arc
image arceus festive sil_black = "sil_black:characters/arc/neutral_festive.png"
image arceus festive = "characters/arc/neutral_festive.png"
image arceus festive dusk flipped = "flip:dusk:characters/arc/neutral_festive.png"
image arceus festive flipped = "flip:characters/arc/neutral_festive.png"
image arceus festive dark = "dark:characters/arc/neutral_festive.png"
image arceus festive dark flipped = "flip:dark:characters/arc/neutral_festive.png"
image arceus festive angry = "characters/arc/angry_festive.png"
image arceus festive angry flipped = "flip:characters/arc/angry_festive.png"
image arceus festive happy = "characters/arc/happy_festive.png"
image arceus festive happy flipped = "flip:characters/arc/happy_festive.png"
image arceus festive worried = "characters/arc/worried_festive.png"
image arceus festive worried flipped = "flip:characters/arc/worried_festive.png"

## Anno
image anno = "characters/anno/anno.png"
image anno phone = "characters/anno/anno_phone.png"
image anno coat = "characters/anno/anno_coat.png"
image anno festive = "characters/anno/anno_festive.png"
image anno festive dark = "dark:characters/anno/anno_festive.png"
image anno dark = "dark:characters/anno/anno.png"
image anno festive sil_black = "sil_black:characters/anno/anno_festive.png"

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
image pakoo tgt = "characters/pakoo/tgt_pakoo_neutral.png"
image pakoo tgt scan = "characters/pakoo/tgt_pakoo_scan.png"
image pakoo tgt tap = "characters/pakoo/tgt_pakoo_tap.png"
image pakoo tgt confused = "characters/pakoo/tgt_pakoo_confused.png"
image pakoo tgt upset = "characters/pakoo/tgt_pakoo_upset.png"
image pakoo tgt happy = "characters/pakoo/tgt_pakoo_happy.png"
image pakoo tgt think = "characters/pakoo/tgt_pakoo_think.png"
image pakoo tgt think2 = "characters/pakoo/tgt_pakoo_think2.png"
image pakoo tgt flipped = "flip:characters/pakoo/tgt_pakoo_neutral.png"

image k17 = "characters/pakoo/k17.png"
image k17 flipped = "flip:characters/pakoo/k17.png"
image k17 dark = "dark:characters/pakoo/k17.png"
image k17 dark flipped = "dark:flip:characters/pakoo/k17.png"
image k17 sil_black = "sil_black:characters/pakoo/k17.png"
image k17 happy = "characters/pakoo/k17_happy.png"
image k17 happy dark = "dark:characters/pakoo/k17_happy.png"
image k17 happy flipped = "flip:characters/pakoo/k17_happy.png"
image k17 happy dark flipped = "dark:flip:characters/pakoo/k17_happy.png"
image k17 disappointed = "characters/pakoo/k17_sad.png"
image k17 disappointed dark = "dark:characters/pakoo/k17_sad.png"
image k17 disappointed flipped = "flip:characters/pakoo/k17_sad.png"
image k17 shock = "characters/pakoo/k17_shock.png"
image k17 shock flipped = "flip:characters/pakoo/k17_shock.png"

image k22 = "characters/pakoo/k22.png"
image k22 flipped = "flip:characters/pakoo/k22.png"
image k22 dark = "dark:characters/pakoo/k22.png"
image k22 dark flipped = "dark:flip:characters/pakoo/k22.png"
image k22 sil_black = "sil_black:characters/pakoo/k22.png"
image k22 phone = "flip:characters/pakoo/k22_phone.png"
image k22 phone angry = "flip:characters/pakoo/k22_phone_angry.png"
image k22 happy = "characters/pakoo/k22_happy.png"
image k22 happy flipped = "flip:characters/pakoo/k22_happy.png"
image k22 disappointed = "characters/pakoo/k22_sad.png"
image k22 disappointed dark = "dark:characters/pakoo/k22_sad.png"
image k22 disappointed flipped = "flip:characters/pakoo/k22_sad.png"
image k22 confident = "characters/pakoo/k22_confident.png"
image k22 confident flipped = "flip:characters/pakoo/k22_confident.png"
image k22 angry = "characters/pakoo/k22_angry.png"
image k22 angry flipped = "flip:characters/pakoo/k22_angry.png"

## Tate
image tate sil_black = "sil_black:characters/tate/festive_tatehappy.png"

## Tate (Christmas)
image tate festive = "characters/tate/festive_tatehappy.png"
image tate festive flipped = "flip:characters/tate/festive_tatehappy.png"
image tate festive dark = "dark:characters/tate/festive_tatehappy.png"
image tate festive dark flipped = "dark:flip:characters/tate/festive_tatehappy.png"
image tate festive sil_black = "sil_black:characters/tate/festive_tatehappy.png"
image tate srs festive = "characters/tate/festive_tateserious.png"
image tate srs festive dark = "dark:characters/tate/festive_tateserious.png"
image tate srs festive flipped = "flip:characters/tate/festive_tateserious.png"
image tate srs festive dark flipped = "dark:flip:characters/tate/festive_tateserious.png"
image tate shock festive = "characters/tate/festive_tateshock.png"
image tate shock festive dark = "dark:characters/tate/festive_tateshock.png"
image tate shock festive flipped = "flip:characters/tate/festive_tateshock.png"
image tate shock festive dark flipped = "dark:flip:characters/tate/festive_tateshock.png"
image tate smug festive = "characters/tate/festive_tatesmug.png"
image tate smug festive dark = "dark:characters/tate/festive_tatesmug.png"
image tate smug festive flipped = "flip:characters/tate/festive_tatesmug.png"
image tate smug festive dark flipped = "dark:flip:characters/tate/festive_tatesmug.png"
image tate smug festive sil_white = "sil_white:characters/tate/festive_tatesmug.png"
image tate sheepish festive = "characters/tate/festive_tatesheepish.png"
image tate sheepish festive dark = "dark:characters/tate/festive_tatesheepish.png"
image tate sheepish festive flipped = "flip:characters/tate/festive_tatesheepish.png"
image tate sheepish festive blush = "characters/tate/festive_tatesheepishblush.png"
image tate sheepish festive blush flipped = "flip:characters/tate/festive_tatesheepishblush.png"
image tate sad festive = "characters/tate/festive_tatesad.png"
image tate sad festive flipped = "flip:characters/tate/festive_tatesad.png"
image tate sad festive dark = "dark:characters/tate/festive_tatesad.png"
image tate stare festive = "characters/tate/festive_tatestare.png"
image tate stare festive flipped = "flip:characters/tate/festive_tatestare.png"
image tate cry festive = "characters/tate/festive_tatecry.png"
image tate cry festive flipped = "flip:characters/tate/festive_tatecry.png"
image tate furious festive = "characters/tate/festive_tatefurious.png"
image tate furious festive dark = "dark:characters/tate/festive_tatefurious.png"
image tate furious festive flipped = "flip:characters/tate/festive_tatefurious.png"
image tate furious blush festive = "characters/tate/festive_tatefuriousblush.png"
image tate furious blush festive flipped = "flip:characters/tate/festive_tatefuriousblush.png"

## Mean (Human Form)
image mean human festive = "characters/mean/meanhumanneutralfestive.png"
image mean human festive flipped = "flip:characters/mean/meanhumanneutralfestive.png"
image mean human festive sil_black = "sil_black:characters/mean/meanhumanneutralfestive.png"
image mean human festive sil_black flipped = "flip:sil_black:characters/mean/meanhumanneutralfestive.png"
image mean human festive dark = "dark:characters/mean/meanhumanneutralfestive.png"
image mean human festive dark flipped = "flip:dark:characters/mean/meanhumanneutralfestive.png"
image mean human happy festive = "characters/mean/meanhumanhappyfestive.png"
image mean human happy festive flipped = "flip:characters/mean/meanhumanhappyfestive.png"
image mean human happy festive dark = "dark:characters/mean/meanhumanhappyfestive.png"
image mean human happy festive dark flipped = "flip:dark:characters/mean/meanhumanhappyfestive.png"
image mean human annoyed festive  = "characters/mean/meanhumanannoyedfestive.png"
image mean human annoyed festive flipped = "flip:characters/mean/meanhumanannoyedfestive.png"
image mean human shocked festive = "characters/mean/meanhumanshockedfestive.png"
image mean human shocked festive flipped = "flip:characters/mean/meanhumanshockedfestive.png"
image mean human shocked festive dark flipped = "dark:flip:characters/mean/meanhumanshockedfestive.png"
image mean human angry festive = "characters/mean/meanhumanangryfestive.png"
image mean human angry festive flipped = "flip:characters/mean/meanhumanangryfestive.png"
image mean human angry festive dark flipped = "dark:flip:characters/mean/meanhumanangryfestive.png"

# HoH SiS
image rich festive sil_black = "sil_black:characters/hohsis/rich_festive.png"
image rich festive = "characters/hohsis/rich_festive.png"
image rich festive dark = "dark:characters/hohsis/rich_festive.png"
image rich festive dark flipped = "dark:flip:characters/hohsis/rich_festive.png"
image rich festive flipped = "flip:characters/hohsis/rich_festive.png"

image ed festive = "characters/hohsis/ed_festive.png"
image ed festive flipped = "flip:characters/hohsis/ed_festive.png"
image ed festive dark = "dark:characters/hohsis/ed_festive.png"
image ed festive dark flipped = "dark:flip:characters/hohsis/ed_festive.png"
image ed festive sil_black = "sil_black:characters/hohsis/ed_festive.png"

image wesley festive sil_black = "sil_black:characters/hohsis/wesley_festive.png"
image wesley festive = "characters/hohsis/wesley_festive.png"
image wesley festive flipped = "flip:characters/hohsis/wesley_festive.png"
image wesley festive dark = "dark:characters/hohsis/wesley_festive.png"
image wesley festive dark flipped = "dark:flip:characters/hohsis/wesley_festive.png"

# Copguy & Co.
image copguy festive sil_black = "sil_black:characters/copguy/copguy_festive.png"
image copguy festive = "characters/copguy/copguy_festive.png"
image copguy festive flipped = "flip:characters/copguy/copguy_festive.png"
image copguy festive dark = "dark:characters/copguy/copguy_festive.png"
image copguy festive dark flipped = "dark:flip:characters/copguy/copguy_festive.png"

image sheriff festive = "characters/sheriff_festive.png"
image sheriff festive flipped = "flip:characters/sheriff_festive.png"
image sheriff festive dark = "dark:characters/sheriff_festive.png"
image sheriff festive dark flipped = "dark:flip:characters/sheriff_festive.png"

# CSB I
image michael sil_black = "sil_black:characters/michael_festive.png"
image michael sil_black flipped = "flip:sil_black:characters/michael_festive.png"
image michael festive = "characters/michael_festive.png"
image michael festive flipped = "flip:characters/michael_festive.png"
image michael festive dark = "dark:characters/michael_festive.png"
image michael festive dark flipped = "flip:dark:characters/michael_festive.png"

image carguy = "characters/carguy.png"
image carguy flipped = "flip:characters/carguy.png"

# LMG & The Fanboys
image linus festive sil_black = "sil_black:characters/lmg/linus_festive.png"
image linus festive = "characters/lmg/linus_festive.png"
image linus festive dark = "dark:characters/lmg/linus_festive.png"
image linus festive flipped = "flip:characters/lmg/linus_festive.png"
image linus festive dark flipped = "dark:flip:characters/lmg/linus_festive.png"

image luke festive sil_black = "sil_black:characters/lmg/luke_festive.png"
image luke festive = "characters/lmg/luke_festive.png"
image luke festive dark = "dark:characters/lmg/luke_festive.png"
image luke festive flipped = "flip:characters/lmg/luke_festive.png"
image luke festive dark flipped = "dark:flip:characters/lmg/luke_festive.png"

# Billy Mays
image billy festive sil_black = "sil_black:characters/billy/festive.png"
image billy festive = "characters/billy/festive.png"
image billy festive flipped = "flip:characters/billy/festive.png"
image billy festive dark = "dark:characters/billy/festive.png"
image billy festive dark flipped = "flip:dark:characters/billy/festive.png"

# Digi
image digi = "characters/digi/neutral.png"
image digi flipped = "flip:characters/digi/neutral.png"
image digi dark = "dark:characters/digi/neutral.png"
image digi dark flipped = "dark:flip:characters/digi/neutral.png"
image digi sil_black = "sil_black:characters/digi/neutral.png"
image digi angry = "characters/digi/angry.png"
image digi angry flipped = "flip:characters/digi/angry.png"
image digi angry dark = "dark:characters/digi/angry.png"
image digi angry dark flipped = "dark:flip:characters/digi/angry.png"
image digi cheese = "characters/digi/cheese.png"
image digi cheese flipped = "flip:characters/digi/cheese.png"
image digi cheese dark = "dark:characters/digi/cheese.png"
image digi cheese dark flipped = "dark:flip:characters/digi/cheese.png"
image digi goober = "characters/digi/goober.png"
image digi goober flipped = "flip:characters/digi/goober.png"
image digi goober dark = "dark:characters/digi/goober.png"
image digi goober dark flipped = "dark:flip:characters/digi/goober.png"
image digi happy = "characters/digi/happy.png"
image digi happy flipped = "flip:characters/digi/happy.png"
image digi happy dark = "dark:characters/digi/happy.png"
image digi happy dark flipped = "dark:flip:characters/digi/happy.png"
image digi sad = "characters/digi/sad.png"
image digi sad flipped = "flip:characters/digi/sad.png"
image digi sad dark = "dark:characters/digi/sad.png"
image digi sad dark flipped = "dark:flip:characters/digi/sad.png"
image digi shock = "characters/digi/shock.png"
image digi shock flipped = "flip:characters/digi/shock.png"
image digi shock dark = "dark:characters/digi/shock.png"
image digi shock dark flipped = "dark:flip:characters/digi/shock.png"
image digi thinking = "characters/digi/thinking.png"
image digi thinking flipped = "flip:characters/digi/thinking.png"
image digi thinking dark = "dark:characters/digi/thinking.png"
image digi thinking dark flipped = "dark:flip:characters/digi/thinking.png"
image digi disappointed = "characters/digi/disappointed.png"
image digi disappointed flipped = "flip:characters/digi/disappointed.png"
image digi disappointed dark = "dark:characters/digi/disappointed.png"
image digi disappointed dark flipped = "dark:flip:characters/digi/disappointed.png"

# Aria
image aria festive = "characters/aria_festive.png"
image aria sil_black = "sil_black:characters/aria_festive.png"
image aria festive flipped = "flip:characters/aria_festive.png"
image aria festive dark = "dark:characters/aria_festive.png"
image aria festive dark flipped = "dark:flip:characters/aria_festive.png"

# Nova
image nova = "characters/nova.png"
image nova sil_black = "sil_black:characters/nova.png"
image nova dark = "dark:characters/nova.png"
image nova flipped = "flip:characters/nova.png"
image nova dark flipped = "dark:flip:characters/nova.png"

# Mika
image grace = "characters/ag/grace.png"
image grace dark = "dark:characters/ag/grace.png"
image grace shirt = "characters/ag/grace_shirt.png"
image grace shirt dark = "dark:characters/ag/grace_shirt.png"
image grace happy = "characters/ag/grace_happy.png"
image grace happy flipped = "flip:characters/ag/grace_happy.png"
image grace happy dark = "dark:characters/ag/grace_happy.png"
image grace happy shirt = "characters/ag/grace_happy_shirt.png"
image grace happy shirt dark = "dark:characters/ag/grace_happy_shirt.png"
image grace sad = "characters/ag/grace_sad.png"
image grace sad dark = "dark:characters/ag/grace_sad.png"
image grace sad shirt = "characters/ag/grace_sad_shirt.png"
image grace sad shirt dark = "dark:characters/ag/grace_sad_shirt.png"
image grace worried = "characters/ag/grace_worried.png"
image grace worried flipped = "flip:characters/ag/grace_worried.png"
image grace worried dark = "dark:characters/ag/grace_worried.png"
image grace worried shirt = "characters/ag/grace_worried_shirt.png"
image grace worried shirt flipped = "flip:characters/ag/grace_worried_shirt.png"
image grace worried shirt dark = "dark:characters/ag/grace_worried_shirt.png"
image grace angry = "characters/ag/grace_angry.png"
image grace angry flipped = "flip:characters/ag/grace_angry.png"
image grace angry dark = "dark:characters/ag/grace_angry.png"
image grace angry shirt = "characters/ag/grace_angry_shirt.png"
image grace angry shirt dark = "dark:characters/ag/grace_angry_shirt.png"
image grace shirt flipped = "flip:characters/ag/grace_shirt.png"
image grace sil_black = "sil_black:characters/ag/grace.png"
image grace flipped = "flip:characters/ag/grace.png"
image grace dark flipped = "dark:flip:characters/ag/grace.png"

image anne = "characters/ag/anne.png"
image anne dark = "dark:characters/ag/anne.png"
image anne happy = "characters/ag/anne_happy.png"
image anne happy dark = "dark:characters/ag/anne_happy.png"
image anne angry = "characters/ag/anne_angry.png"
image anne angry dark = "dark:characters/ag/anne_angry.png"
image anne sil_black = "sil_black:characters/ag/anne.png"
image anne flipped = "flip:characters/ag/anne.png"
image anne dark flipped = "dark:flip:characters/ag/anne.png"

image elizabeth = "characters/eliza/eliza.png"
image elizabeth flipped = "flip:characters/eliza/eliza.png"
image elizabeth dark = "dark:characters/eliza/eliza.png"
image elizabeth dark flipped = "dark:flip:characters/eliza/eliza.png"
image elizabeth disappointed = "characters/eliza/eliza_disappointed.png"
image elizabeth disappointed flipped = "flip:characters/eliza/eliza_disappointed.png"
image elizabeth disappointed dark = "dark:characters/eliza/eliza_disappointed.png"
image elizabeth disappointed dark flipped = "dark:flip:characters/eliza/eliza_disappointed.png"
image elizabeth worried = "characters/eliza/eliza_worried.png"
image elizabeth worried flipped = "flip:characters/eliza/eliza_worried.png"
image elizabeth worried dark = "dark:characters/eliza/eliza_worried.png"
image elizabeth worried dark flipped = "dark:flip:characters/eliza/eliza_worried.png"
image elizabeth angry = "characters/eliza/eliza_angry.png"
image elizabeth angry flipped = "flip:characters/eliza/eliza_angry.png"
image elizabeth angry dark = "dark:characters/eliza/eliza_angry.png"
image elizabeth angry dark flipped = "dark:flip:characters/eliza/eliza_angry.png"
image elizabeth sil_black = "sil_black:characters/eliza/eliza.png"

# More of our friends!
image kitty festive = "characters/kitty_festive.png"
image kitty festive dark = "dark:characters/kitty_festive.png"
image kitty festive flipped = "flip:characters/kitty_festive.png"
image kitty festive dark flipped = "dark:flip:characters/kitty_festive.png"
image kitty festive sil_black = "sil_black:characters/kitty_festive.png"

image blank sil_black = "sil_black:characters/blank_festive.png"
image blank festive = "characters/blank_festive.png"
image blank festive flipped = "flip:characters/blank_festive.png"
image blank festive dark = "dark:characters/blank_festive.png"
image blank festive dark flipped = "flip:dark:characters/blank_festive.png"

image db = "characters/db.png"
image db dark = "dark:characters/db.png"
image db sil_black = "sil_black:characters/db.png"

image ges = "characters/ges.png"
image ges flipped = "flip:characters/ges.png"
image ges dark = "dark:characters/ges.png"
image ges dark flipped = "flip:dark:characters/ges.png"

# Unsorted NPCs
image obama festive = "characters/obama_festive.png"
image obama festive angry = "characters/obama_festive_angry.png"
image obama festive flipped = "flip:characters/obama_festive.png"
image obama festive dark = "dark:characters/obama_festive.png"
image obama festive dark flipped = "flip:dark:characters/obama_festive.png"
image obama sil_black = "sil_black:characters/obama_festive.png"

# Fired Route
image customer = "characters/customer.png"
image customer flipped = "flip:characters/customer.png"

# East Route
image streetguy = "characters/streetguy.png"
image streetguy flipped = "flip:characters/streetguy.png"

# Sweden
image pomni = "characters/pomni/pomni.png"
image pomni flipped = "flip:characters/pomni/pomni.png"
image pomni think = "characters/pomni/pomni_think.png"
image pomni think flipped = "flip:characters/pomni/pomni_concern.png"
image pomni concern = "characters/pomni/pomni_concern.png"
image pomni concern flipped = "flip:characters/pomni/pomni_concern.png"
image pomni eyes = "characters/pomni/pomni_eyes.png"
image pomni eyes flipped = "flip:characters/pomni/pomni_eyes.png"

image snufkin = "characters/snufkin.png"
image snufkin flipped = "flip:characters/snufkin.png"

# Background Images
## CSBI
image cs_room_2 = "bg/cs_bedroom2.png"
image cs_room_2 dark = "dark:bg/cs_bedroom2.png"

# Fired route
image cs_door_outside = "bg/cs_door_outside.png"

## Archival
image archival_5 = "bg/archival/archival_5.png"
image archival_14 = "bg/archival/archival_14.png"

# Back to the future: CS edition generated assets
image christmas_finisher = Text("{size=+108}To be continued...", text_align=0.5)

# CS Holiday Special characters
image avgn = "characters/avgn.png"
image avgn dark = "dark:characters/avgn.png"
image avgn flipped = "flip:characters/avgn.png"
image avgn dark flipped = "dark:flip:characters/avgn.png"
image santa = "characters/santa.png"
image santa flipped = "flip:characters/santa.png"
image santa dark = "dark:characters/santa.png"
image santa dark flipped = "dark:flip:characters/santa.png"
image santa sil_black = "sil_black:characters/santa.png"
image mike = "characters/mike.png"
image iris = "characters/iris_fixed.png"
image iris dark = "dark:characters/iris_fixed.png"
image iris flipped = "flip:characters/iris_fixed.png"
image iris dark flipped = "dark:flip:characters/iris_fixed.png"

# CS Holiday Special BGs
image snowed_in = "bg/snowed_in.png"
image cs_kitchen = "bg/cs_kitchen.png"
image cs_kitchen_fg = "bg/cs_kitchen_fg.png"
image cs_kitchen_off = "bg/cs_kitchen_off.png"
image cs_kitchen_fg_off = "bg/cs_kitchen_fg_off.png"
image cs_basement = "bg/cs_basement.png"
image tgt_alcy = "bg/tgt_alcy.png"
image tgt_bread = "bg/tgt_bread.png"
image tgt_checkerror = "bg/tgt_checkerror.png"
image tgt_checkout = "bg/tgt_checkout.png"
image tgt_checkout_id = "bg/tgt_checkout_id.png"
image tgt_checkout_circle = "bg/tgt_checkout_circle.png"
image tgt_checkout_finish = "bg/tgt_checkout_finish.png"
image tgt_checkout_pay = "bg/tgt_checkout_pay.png"
image tgt_checkout_tm = "bg/tgt_checkout_tm.png"
image tgt_checkout_scanning = "bg/tgt_checkout_scanning.png"
image tgt_checkout_scan_twice = "bg/tgt_checkout_scan_twice.png"
image tgt_chips = "bg/tgt_chips.png"
image tgt_dairy = "bg/tgt_dairy.png"
image tgt_endcap = "bg/tgt_endcap.png"
image tgt_frozen = "bg/tgt_frozen.png"
image tgt_inside = "bg/tgt_inside.png"
image tgt_line = "bg/tgt_line.png"
image tgt_outside = "bg/tgt_outside.png"
image tgt_shelf = "bg/tgt_shelf.png"
image tgt_tater = "bg/tgt_tater.png"
image tgt_tech = "bg/tgt_tech.png"
image tgt_tree = "bg/tgt_tree.png"
image cs_house_snow = "bg/cs_house_snow.png"
image cs_house_snowed_in = "bg/cs_house_snowed_in.png"
image cs_house_night = "bg/cs_house_night.png"
image cs_house_snow_night = "bg/cs_house_snow_night.png"
image cs_house_night_dtree = "bg/cs_house_night_dtree.png"
image cs_garage = "bg/cs_garage.png"
image cs_garage_mess = "bg/cs_garage_mess.png"
image anno_house = "bg/anno_house.png"
image cs_attic = "bg/cs_attic.png"
image cs_bathroom = "bg/cs_bathroom.png"
image cs_bathroom_open = "bg/cs_bathroom_open.png"
image cs_bathroom_open_fg = "bg/cs_bathroom_open_fg.png"
image cs_bathroom_off = "bg/cs_bathroom_off.png"
image cs_foyer = "bg/cs_foyer.png"
image cs_foyer_off = "bg/cs_foyer_off.png"
image cs_foyer_festive = "bg/cs_foyer_festive.png"
image cs_foyer_off_festive = "bg/cs_foyer_off_festive.png"
image cs_hallway = "bg/cs_hallway.png"
image cs_hallway_off = "bg/cs_hallway_off.png"
image cs_living = "bg/cs_living.png"
image cs_living2 = "bg/cs_living2.png"
image cs_living2_festive = "bg/cs_living2_festive.png"
image cs_living_off = "bg/cs_living_off.png"
image cs_living2_off = "bg/cs_living2_off.png"
image cs_living2_off_festive = "bg/cs_living2_off_festive.png"
image breakerbox = "bg/breakerbox.png"
image billycar1 = "bg/billycar1.png"
image billycar2 = "bg/billycar2.png"
image billycar3 = "bg/billycar3.png"
image cs_roof = "bg/cs_roof.png"
image cs_bedroom1_ce = "bg/cs_bedroom1_ce.png"
image cs_bedroom1_ce dark = "dark:bg/cs_bedroom1_ce.png"
image cs_door = "bg/cs_door.png"
image left_chair_back = "bg/table/left_chair_back.png"
image left_chair_front = "bg/table/left_chair_front.png"
image left_room = "bg/table/left_room.png"
image left_table = "bg/table/left_table.png"
image right_chair_back = "bg/table/right_chair_back.png"
image right_chair_front = "bg/table/right_chair_front.png"
image right_room = "bg/table/right_room.png"
image right_table = "bg/table/right_table.png"
image night_bg = "bg/table/night_bg.png"
image cs_bedroom1_ce_car = "bg/cs_bedroom1_ce_car.png"
image cs_bedroom1_ce_car dark = "dark:bg/cs_bedroom1_ce_car.png"
image cs_car_inside_snow = "bg/car_inside_snow.png"

# CS Holiday Special Generated Images
image spent_target = Text("{size=50}{color=#369100}-$81.88", text_align=0.5)

image reversi_rules:
    xsize 1500
    ysize 500
    xanchor 0.5
    yanchor 0.5
    contains:
        Frame("gui/frame.png")
    contains:
        Text("{size=+16}Reversi!", xalign=0.5, yalign=0.075)
    contains:
        Null(xysize=(100,100))
    contains:
        Text("• Each player places down one piece per turn.\n• The goal is to capture your opponent's pieces by trapping them in between your own pieces on the board. \n• A legal move will capture at least one of your opponent's pieces. Depending on placement, you can capture entire rows in any direction on the grid.\n• The game ends when either the board is full or there are no legal moves left.\n• Whoever controls the most pieces at the end wins!", xanchor=0.5, yanchor=1.0, xalign=0.5, yalign=0.925, xmaximum=1450)

# Misc.
image game_menu = "gui/game_menu.png"
image black = "bg/black.png"
image green_screen = "bg/green.png"
image michael_calendar = "bg/michael_calendar.png"

#DX Holiday Special Misc.
image smoke = SnowBlossom("smoke.png", count = 400, fast = False, xspeed = (0,0), yspeed = (0, -100), border = 32)
image bigsmoke = SnowBlossom("bigsmoke.png", count = 200, fast = True, xspeed = (0,0), yspeed = (0, -50), border = 256)
image snow1 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (20000, 100))
image snow2 = SnowBlossom("snow1.png", count = 200, fast = False, xspeed = (1000, 100))
image snow1white = SnowBlossom("snow2.png", count = 200, fast = False, xspeed = (1000, 100))
image snow2white = SnowBlossom("snow2.png", count = 200, fast = False, xspeed = (2000, 100))
image snow3 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (2000, 100))
image snow4 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (4000, 100))
image snow5 = SnowBlossom("snow1.png", count = 200, fast = False, xspeed = (2000, 100))
image snow6 = SnowBlossom("snow1.png", count = 200, fast = True, xspeed = (3000, 100))
image snow_wind = SnowBlossom("snow_wind.png", count = 50, fast = True, xspeed = (500, 0), border = 4000, horizontal = True)
image sleigh:
    "sleigh.png"
    ease 3.0 rotate -3
    ease 3.0 rotate 3
    repeat

image snow_pile = "snow_pile.png"

# Static Images
image anno_car = "anno_car.png"
image anno_car dark = "dark:anno_car.png"
image billy_car = "billy_car.png"
image billy_car dark = "dark:billy_car.png"
image blank_car = "blank_car.png"
image blank_car dark = "dark:blank_car.png"
image blank_speaker = "blank_speaker.png"
image bread = "bread.png"
image burnt_turkey = "burnt_turkey.png"
image butter = "butter.png"
image car = "car.png"
image car dark = "dark:car.png"
image carrot_whole = "carrot_whole.png"
image carrot_chopped = "carrot_chopped.png"
image cold_breath = "cold_breath.png"
image cop_car = "cop_car.png"
image cop_car dark = "dark:cop_car.png"
image crotch_doctor = "crotch_doctor.png"
image crotch_doctor sil_black = "sil_black:crotch_doctor.png"
image cs_id = "cs_id.png"
image cs_phone = "cs_phone.png"
image cs_phone flipped = "flip:cs_phone.png"
image cs_wallet = "cs_wallet.png"
image cutting_board = "cutting_board.png"
image d20 = "d20.png"
image db_car = "db_car.png"
image db_car dark = "dark:db_car.png"
image decor_boxes = "decor_boxes.png"
image digi_nugget_full = "nugget_full.png"
image digi_nugget_parked = "nugget_cutout.png"
image digi_nugget_parked dark = "dark:nugget_cutout.png"
image festive_bag = "festive_bag.png"
image flashlight_held = "flashlight_held.png"
image flashlight_held flipped = "flip:flashlight_held.png"
image folded_paper = "folded_paper.png"
image folded_paper dark = "dark:folded_paper.png"
image garage_shelf = "garage_shelf.png"
image gas_prices = "gas_prices.png"
image genergy = "genergy.png"
image ges_car = "ges_car.png"
image ges_car dark = "dark:ges_car.png"
image hatch = "gui/ce_point_click/hatch/hatch_idle.png"
image joj_ufo_empty = "images/joj_ufo/joj_ufo_empty.png"
image joj_ufo_empty dark = "dark:images/joj_ufo/joj_ufo_empty.png"
image knife = "knife.png"
image lights_box = "lights_box.png"
image ltt_car = "ltt_car.png"
image ltt_car dark = "dark:ltt_car.png"
image ltt_bottle_linus = "ltt_bottle_linus.png"
image mean_train = "mean_train.png"
image mean_train dark = "dark:mean_train.png"
image mika_car = "mika_car.png"
image mika_car dark = "dark:mika_car.png"
image nog = "nog.png"
image obama_chopper = "obama_chopper.png"
image obama_chopper dark  = "dark:obama_chopper.png"
image pakoo_car = "pakoo_car.png"
image pakoo_car dark = "dark:pakoo_car.png"
image pie = "pie.png"
image pipe_gun = "pipe_gun.png"
image pipe_gun flipped = "flip:pipe_gun.png"
image potato_bag = "potato_bag.png"
image pringles = "pringles.png"
image projector = "projector.png"
image projector_airplay = "bg/projector_airplay.png"
image projector_error = "bg/projector_error.png"
image projector_no_signal = "bg/projector_no_signal.png"
image reversi_box = "images/minigames/reversi_box.png"
image rosen_car = "rosen_car.png"
image rosen_car dark = "dark:rosen_car.png"
image runaway_bus = "runaway_bus.png"
image runaway_bus dark = "dark:runaway_bus.png"
image shopping_cart = "shopping_cart.png"
image shopping_cart flipped = "flip:shopping_cart.png"
image shovel = "shovel.png"
image snow_wind_single = "snow_wind.png"
image spray_cheese = "spray_cheese.png"
image target_bags = "target_bags.png"
image tate_phone = "tate_phone.png"
image tato_bag = "tato_bag.png"
image tree_box = "tree_box.png"
image watermark1 = "wm1.png"
image watermark2 = "wm2.png"
image watermark3 = "wm3.png"
image watermark4 = "wm4.png"

# CSBIII DX: Holiday Special Gift Boxes
image gift_anne_grace = "images/gifts/present_boxes/anne_grace.png"
image gift_anno = "images/gifts/present_boxes/anno.png"
image gift_arc = "images/gifts/present_boxes/arc.png"
image gift_aria = "images/gifts/present_boxes/aria.png"
image gift_avgn = "images/gifts/present_boxes/avgn.png"
image gift_billy = "images/gifts/present_boxes/billy.png"
image gift_blank = "images/gifts/present_boxes/blank.png"
image gift_copguy = "images/gifts/present_boxes/copguy.png"
image gift_cs = "images/gifts/present_boxes/cs.png"
image gift_db = "images/gifts/present_boxes/db.png"
image gift_digi = "images/gifts/present_boxes/digi.png"
image gift_ed = "images/gifts/present_boxes/ed.png"
image gift_eliza = "images/gifts/present_boxes/eliza.png"
image gift_k17 = "images/gifts/present_boxes/k17.png"
image gift_k22 = "images/gifts/present_boxes/k22.png"
image gift_kitty = "images/gifts/present_boxes/kitty.png"
image gift_linus = "images/gifts/present_boxes/linus.png"
image gift_luke = "images/gifts/present_boxes/luke.png"
image gift_mean = "images/gifts/present_boxes/mean.png"
image gift_michael = "images/gifts/present_boxes/michael.png"
image gift_nova = "images/gifts/present_boxes/nova.png"
image gift_obama = "images/gifts/present_boxes/obama.png"
image gift_richard = "images/gifts/present_boxes/richard.png"
image gift_sheriff = "images/gifts/present_boxes/sheriff.png"
image gift_tate = "images/gifts/present_boxes/tate.png"
image gift_wesley = "images/gifts/present_boxes/wesley.png"

# CSBIII DX: Holiday Special Gifts
image 1850_coin = "images/gifts/1850_coin.png"
image adderall = "images/gifts/adderall.png"
image cement = "images/gifts/cement.png"
image colt = "images/gifts/colt.png"
image dog_food = "images/gifts/dog_food.png"
image doi = "images/gifts/doi.png"
image fumo = "images/gifts/fumo.png"
image gamersupps = "images/gifts/gamersupps.png"
image gravity_falls = "images/gifts/gravity_falls.png"
image handy_switch = "images/gifts/handy_switch.png"
image hard_drive = "images/gifts/hard_drive.png"
image instant_pot = "images/gifts/instant_pot.png"
image lego_train = "images/gifts/lego_train.png"
image ltt_bottle = "images/gifts/ltt_bottle.png"
image ltt_screwdriver = "images/gifts/ltt_screwdriver.png"
image melted_ice_cream = "images/gifts/melted_ice_cream.png"
image mgs1 = "images/gifts/mgs1.png"
image monitor = "images/gifts/monitor.png"
image old_shirt = "images/gifts/old_shirt.png"
image peach_syrup = "images/gifts/peach_syrup.png"
image pills = "images/gifts/pills.png"
image raspberry_pi = "images/gifts/raspberry_pi.png"
image riffmaster = "images/gifts/riffmaster.png"
image roll_and_rocker = "images/gifts/roll_and_rocker.png"
image rolling_rock = "images/gifts/rolling_rock.png"
image russian_radio = "images/gifts/russian_radio.png"
image sunny_d = "images/gifts/sunny_d.png"
image tea_and_crumpets = "images/gifts/tea_and_crumpets.png"
image thigh_highs = "images/gifts/thigh_highs.png"

# CSBIII: CE: Carrot Game
image obama_says = "minigames/carrot/obama_says.png"
image rating_ok = "minigames/carrot/ok.png"
image rating_superb = "minigames/carrot/superb.png"
image rating_try_again = "minigames/carrot/try_again.png"

# Movies
image car plains night = Movie(play="movies/car_plains_night.webm")
image elf_0 = Movie(play="movies/elf0.webm", size=(640,360))
image elf_1 = Movie(play="movies/elf1.webm", size=(1,1))
define decoratingscene = "movies/decoratingscene.webm"
define intro_credits_1 = "movies/intro_credits_1.webm"
define intro_credits_2 = "movies/intro_credits_2.webm"
define ce_ending = "movies/ce_ending.webm"

# Animated Sprites

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

# Audio

#CSBII Music
define audio.star_spangled_banner = "star_spangled_banner.ogg"

# CSBIII DX Holiday Special Music
define audio.lets_hear_winter = "<loop 7.674>lets_hear_my_christ.ogg"
define audio.winters_halloween = "<loop 19.729>winters_halloween.ogg"
define audio.synchronicity = "synchronicity.ogg"
define audio.dont_preheat_your_oven = "dont_preheat_your_oven.ogg"
define audio.on_the_rocks = "on_the_rocks.ogg"
define audio.snowy = "snowy.ogg"
define audio.teeth_dust = "teeth_dust.ogg"
define audio.snow_blind = "snow_blind.ogg"
define audio.christmas_spirit = "christmas_spirit.ogg"
define audio.snowdin_town = "snowdin_town.ogg"
define audio.rice_and_wine = "rice_and_wine.ogg"
define audio.winter_unclearance_sale = "winter_unclearance_sale.ogg"
define audio.frollo_rave = "frollo_rave.ogg"
define audio.superstar_road = "superstar_road.ogg"
define audio.summer_fun = "summer_fun.ogg"
define audio.crashing_down = "crashing_down.ogg"
define audio.ce_passport = "cepassport.ogg"
define audio.snowman = "snowman.ogg"
define audio.title_theme_reprise = "title_theme_reprise.ogg"
define audio.girl_next_door = "girl_next_door.ogg"

# Other?
define audio.interference2 = "<from 275>interference.ogg"

# SFX
define audio.sfx_aria_tp = "sfx/sfx_aria_tp.ogg"
define audio.sfx_blanket = "sfx/sfx_blanket.ogg"
define audio.sfx_beam = "sfx/sfx_beam.ogg"
define audio.sfx_bluescreen = "sfx/sfx_bluescreen.ogg"
define audio.sfx_bottle_hit = "sfx/sfx_bottle_hit.ogg"
define audio.sfx_bottle_squeeze = "sfx/sfx_bottle_squeeze.ogg"
define audio.sfx_bottle_squirt = "sfx/sfx_bottle_squirt.ogg"
define audio.sfx_box_drag = "sfx/sfx_box_drag.ogg"
define audio.sfx_box_place = "sfx/sfx_box_place.ogg"
define audio.sfx_breaker = "sfx/sfx_breaker.ogg"
define audio.sfx_car_approach_stop = "sfx/sfx_car_approach_stop.ogg"
define audio.sfx_car_door_ajar = "sfx/sfx_car_door_ajar.ogg"
define audio.sfx_car_door_open = "sfx/sfx_car_door_open.ogg"
define audio.sfx_cat_crash = "sfx/sfx_cat_crash.ogg"
define audio.sfx_chopper_loop = "sfx/sfx_chopper_loop.ogg"
define audio.sfx_clock_ticking = "sfx/sfx_clock_ticking.ogg"
define audio.sfx_creaky_metal = "sfx/sfx_creaky_metal.ogg"
define audio.sfx_csnore = "sfx/sfx_csnore.ogg"
define audio.sfx_doorbell = "sfx/sfx_doorbell.ogg"
define audio.sfx_door_jiggle = "sfx/sfx_door_jiggle.ogg"
define audio.sfx_doorslam = "sfx/sfx_doorslam.ogg"
define audio.sfx_driving = "sfx/sfx_driving.ogg"
define audio.sfx_droplet = "sfx/sfx_droplet.ogg"
define audio.sfx_end_call = "sfx/sfx_end_call.ogg"
define audio.sfx_fabeep = "sfx/sfx_fabeep.ogg"
define audio.sfx_fish = "sfx/sfx_fish.ogg"
define audio.sfx_flashback_arthur = "sfx/sfx_flashback_arthur.ogg"
define audio.sfx_flashlight_on = "sfx/sfx_flashlight_on.ogg"
define audio.sfx_fucking_die = "sfx/sfx_fucking_die.ogg"
define audio.sfx_idcheck = "sfx/sfx_idcheck.ogg"
define audio.sfx_hitbod3 = "sfx/sfx_hitbod3.ogg"
define audio.sfx_house_door_close = "sfx/sfx_house_door_close.ogg"
define audio.sfx_house_door_open = "sfx/sfx_house_door_open.ogg"
define audio.sfx_house_door_slam = "sfx/sfx_house_door_slam.ogg"
define audio.sfx_hubbub = "sfx/sfx_hubbub.ogg"
define audio.sfx_hks1 = "sfx/sfx_hks1.ogg"
define audio.sfx_issac = "sfx/sfx_isaac.ogg"
define audio.sfx_items_rustling = "sfx/sfx_items_rustling.ogg"
define audio.sfx_jingle = "<loop 2 to 6>sfx/sfx_jingle.ogg"
define audio.sfx_lego_break = "sfx/sfx_lego_break.ogg"
define audio.sfx_metalpipe = "sfx/sfx_metalpipe.ogg"
define audio.sfx_moneyfalls = "sfx/sfx_moneyfalls.ogg"
define audio.sfx_nice_snow = "sfx/sfx_nice_snow.ogg"
define audio.sfx_not_so_nice_driveway = "sfx/sfx_not_so_driveway.ogg"
define audio.sfx_nugget = "sfx/sfx_nugget.ogg"
define audio.sfx_okuubeam = "sfx/sfx_okuubeam.ogg"
define audio.sfx_oven_close = "sfx/sfx_oven_close.ogg"
define audio.sfx_oven_open = "sfx/sfx_oven_open.ogg"
define audio.sfx_pop_noice = "sfx/sfx_pop_noice.ogg"
define audio.sfx_power_out = "sfx/sfx_power_out.ogg"
define audio.sfx_projector_boot = "sfx/sfx_projector_boot.ogg"
define audio.sfx_punch = "sfx/sfx_punch.ogg"
define audio.sfx_richlaugh = "sfx/sfx_richlaugh.ogg"
define audio.sfx_ring_once = "sfx/sfx_ring_once.ogg"
define audio.sfx_scan_twice = "sfx/sfx_scan_twice.ogg"
define audio.sfx_select = "sfx/sfx_select.ogg"
define audio.sfx_seymour = "sfx/sfx_seymour.ogg"
define audio.sfx_shopping_cart = "sfx/sfx_shopping_cart.ogg"
define audio.sfx_shoveling = "sfx/sfx_shoveling.ogg"
define audio.sfx_shovel_single = "sfx/sfx_shovel_single.ogg"
define audio.sfx_siren = "sfx/sfx_siren.ogg"
define audio.sfx_slap = "sfx/sfx_slap.ogg"
define audio.sfx_smoke_alarm = "sfx/sfx_smoke_alarm.ogg"
define audio.sfx_snd_lightswitch = "sfx/snd_lightswitch.ogg"
define audio.sfx_snow_evaporate = "sfx/sfx_snow_evaporate.ogg"
define audio.sfx_snow_run = "sfx/sfx_snow_run.ogg"
define audio.sfx_snow_walk = "sfx/sfx_snow_walk.ogg"
define audio.sfx_snowfall = "sfx/sfx_snowfall.ogg"
define audio.sfx_special_unlock = "sfx/sfx_special_unlock.ogg"
define audio.sfx_spikes = "sfx/sfx_spikes.ogg"
define audio.sfx_splash = "sfx/sfx_splash.ogg"
define audio.sfx_start_rocking = "sfx/sfx_start_rocking.ogg"
define audio.sfx_static = "sfx/sfx_static.ogg"
define audio.sfx_tada = "sfx/sfx_tada.ogg"
define audio.sfx_target_beep = "sfx/sfx_target_beep.ogg"
define audio.sfx_tato_screm = "sfx/sfx_tato_screm.ogg"
define audio.sfx_tf2_pickup_metallic = "sfx/sfx_tf2_pickup_metallic.ogg"
define audio.sfx_tf2_wrench_hit = "sfx/sfx_tf2_wrench_hit.ogg"
define audio.sfx_tgt_bg = "sfx/sfx_tgt_bg.ogg"
define audio.sfx_toilet_flush = "sfx/sfx_toilet_flush.ogg"
define audio.sfx_train_chugging = "sfx/sfx_train_chugging.ogg"
define audio.sfx_train_whistle = "sfx/sfx_train_whistle.ogg"
define audio.sfx_valid = "sfx/sfx_valid.ogg"
define audio.sfx_walkie_off = "sfx/sfx_walkie_off.ogg"
define audio.sfx_walkie_on = "sfx/sfx_walkie_on.ogg"
define audio.sfx_whisper = "sfx/sfx_whisper.ogg"
define audio.sfx_whoosh = "sfx/sfx_whoosh.ogg"
define audio.sfx_woohoo = "sfx/sfx_woohoo.wav"
define audio.sfx_zebra_scan = "sfx/sfx_zebra_scan.ogg"


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
default minigame_win = "secret_ce"
default minigame_loss = "secret_ce"

default current_dxcom = "1"

python early:

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
    # $ renpy.movie_cutscene(splash) TODO: Digi: Christmas splash
    $ persistent.seen_splash = True
    $ persistent.heard.add("christmas_tea")
    return

label before_main_menu:
    python:
        # This has been changed for CE to require 188%ing the game.
        # This is INTENTIONAL, and should not be backported to DX.
        # We need to reevaluate how this works in DX, though...
        # Allowing debug mode when you only have all endings unlocked seems
        # a bit too OP?
        if achievement_manager.locked == []:
            if persistent.creative_mode == False:
                persistent.creative_mode = True
                renpy.call_screen("special_unlock", "Noice! You've unlocked Creative Mode! Check out all the new stuff in Extras!")

        if not persistent.seen_splash:
            if not renpy.music.is_playing():
                renpy.music.play("christmas_tea.ogg", loop = False)
        else:
            if not renpy.music.is_playing():
                renpy.music.play("<from 14.7>christmas_tea.ogg", loop = True)
                persistent.seen_splash = False
    return

label start:  # this might be required??
    # yep, it's required, but i'm fixing it to default to main menu instead - tate
    return

define shake1 = { "master" : hpunch }
define shake2 = { "master" : vpunch }
