# Text beeps
init python:
    renpy.music.register_channel("beep", "voice", loop = True)
    def char_callback(event, name = None, beep = None, play_beeps = True, **kwargs):
        if name:
            persistent.seen.add(name)
        if preferences.text_beeps and play_beeps:
            if event == "show":
                if beep is not None:
                    renpy.sound.play(f"audio/text/{beep}.wav", channel = "beep", loop = True)
                    print(name)
                else:
                    renpy.sound.play(f"audio/text/ut.wav", channel = "beep", loop = True)
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel="beep")

# If music is so good, why is there no Music 2?
init python:
    renpy.music.register_channel("music2", "music")
    renpy.music.register_channel("jukebox", "music")

# Custom transforms
transform rotate_10:
    subpixel True
    rotate 10 xanchor 0.5 yanchor 0.5
    ypos 0.5
    zoom 1.33

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
    zoom 0.6

transform t_cs_ltt:
    zoom 0.65
    yanchor 1.0 ypos 0.8
    xanchor 0.0 xpos 0.2

transform t_linus_ltt:
    zoom 0.65
    yanchor 1.0 ypos 0.8
    xanchor 1.0 xpos 0.8

transform little_bounce:
    yanchor 1.0
    yzoom 0.95
    ease 0.1 yzoom 1.05
    ease 0.1 yzoom 1

transform xstretch_in:
    xalign 0.5
    linear 0.5 xsize 1920

transform xstretch_out:
    xalign 0.5
    linear 0.5 xsize 2
    alpha 0.0

# Character Definitions
define n = Character(None, what_italic = True)  # Narrator
define cs = Character("cs188", callback = renpy.partial(char_callback, name = "cs", beep = "cs"))
define cs_fakegod = Character("cs188 (pretending to be CSGod)", callback = renpy.partial(char_callback, name = "cs", beep = "csgod"))
define craptop = Character("Craptop", callback = char_callback)
define sticky = Character("Sticky Note", callback = char_callback)
define discord = Character("Discord", callback = char_callback)
define nova = Character("Nova", callback = renpy.partial(char_callback, name = "nova"))
define carguy = Character("Car Guy", callback = renpy.partial(char_callback, name = "carguy", beep = "nice"))
define carguy_nobeep = Character("Car Guy", callback = renpy.partial(char_callback, name = "carguy", play_beeps = False))
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
define pakoo = Character("Pakoo", callback = renpy.partial(char_callback, name = "pakoo", beep = "csgod"))

define copguy = Character("CopGuy", callback = renpy.partial(char_callback, name = "copguy", beep = "cop"))
define arceus = Character("Arceus", callback = renpy.partial(char_callback, name = "arceus", beep = "arc"))
define anno = Character("Anno", callback = renpy.partial(char_callback, name = "anno", beep = "anno"))
define border_guard = Character("Border Guard", callback = renpy.partial(char_callback, name = "border_guard"))
define linus = Character("Linus", callback = renpy.partial(char_callback, name = "linus", beep = "ltt"))
define asylum_worker = Character("Mr. Mohs", callback = renpy.partial(char_callback, name = "mohs"))
define csgod = Character("CS God", callback = renpy.partial(char_callback, name = "csgod", beep = "csgod"))

define luke = Character("Luke", callback = renpy.partial(char_callback, name = "luke", beep = "luke"))
define taran = Character("Taran", callback = renpy.partial(char_callback, name = "taran"))
define colton = Character("Colton", callback = renpy.partial(char_callback, name = "colton"))
define sheriff = Character("Sheriff", callback = renpy.partial(char_callback, name = "sheriff"))
define billy = Character("Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define cultist = Character("Cultist", callback = renpy.partial(char_callback, name = "cultist"))
define cultist_2 = Character("Cultist 2", callback = renpy.partial(char_callback, name = "cultist2"))
define cultist_3 = Character("Cultist 3", callback = char_callback)
define scott = Character("Scott", callback = renpy.partial(char_callback, name = "scott"))
define terry = Character("Terry", callback = renpy.partial(char_callback, name = "terry"))
define carla = Character("Carla", callback = renpy.partial(char_callback, name = "carla"))
define peppino = Character("Peppino", callback = renpy.partial(char_callback, name = "peppino"))
define iris = Character("Iris", callback = renpy.partial(char_callback, name = "iris", beep = "iris"))

# Character Images
## CS
image cs = "characters/cs/neutral.png"
image cs flipped = Transform("characters/cs/neutral.png", xzoom = -1)
image cs happy = "characters/cs/happy.png"
image cs angry = "characters/cs/angry.png"
image cs angry flipped = Transform("characters/cs/angry.png", xzoom = -1)
image cs worried = "characters/cs/worried.png"
image cs worried flipped = Transform("characters/cs/worried.png", xzoom = -1)
image cs disappointed = "characters/cs/disappointed.png"
image cs disappointed flipped = Transform("characters/cs/disappointed.png", xzoom = -1)
image cs concentrate = "characters/cs/concentrate.png"
image cs phone = "characters/cs/phone.png"
image cs dark = "characters/cs/neutraldark.png"
image cs dusk = "characters/cs/neutraldusk.png"
image cs disappointed dark = "characters/cs/disappointeddark.png"
image cs disappointed dusk = "characters/cs/disappointeddusk.png"
image cs worried dark = "characters/cs/worrieddark.png"
image cs prison = "characters/cs/prison.png"
image cs prison_worried = "characters/cs/prison_worried.png"
image cs guard = "characters/cs/guard.png"
image cs guard dark = "characters/cs/guarddark.png"
image cs fakegod = "characters/cs/fake_god.png"

## Arc
image arceus = "characters/arc/arceus.png"
image arceus flipped = Transform("characters/arc/arceus.png", xzoom = -1)
image arceus dark = "characters/arc/arceusdark.png"
image arceus dark flipped = Transform("characters/arc/arceusdark.png", xzoom = -1)
image arceus dusk = "characters/arc/arceusdusk.png"
image arceus dusk flipped = Transform("characters/arc/arceusdusk.png", xzoom = -1)

## Anno
image anno = "characters/anno/anno.png"
image anno prison = "characters/anno/anno_prison.png"
image anno guard = "characters/anno/anno_guard.png"
image anno guard dark = "characters/anno/anno_guarddark.png"

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
image post_it = "post-it.png"

## Others
image discord = "characters/discord.png"
image nova = "characters/nova.png"
image carguy = "characters/carguy.png"
image doug = "characters/doug.png"
image cashier = "characters/cashier.png"
image young_cs = "characters/cs_young.png"
image rich = "characters/rich.png"
image ed = "characters/ed.png"
image ed phone = "characters/ed_phone.png"
image wesley = "characters/wesley.png"
image michael = Transform("characters/michael.png", xzoom = -1)
image phil = "characters/phil.png"
image worker_1 = "characters/worker_corn.png"
image worker_2 = "characters/worker_blank.png"
image worker_3 = "characters/worker_mean.png"
image worker_4 = "characters/worker_eville.png"
image worker_5 = "characters/eddie_down.png"
image worker_5alt = "characters/eddie_up.png"
image worker_6 = "characters/worker_pineapple.png"
image worker_7 = "characters/worker_chicken.png"
image border_guard = "characters/border_guard.png"
image linus = "characters/linus.png"
image asylum_worker = "characters/mohs.png"
image csgod = "characters/csgod.png"
image csgod flipped = Transform("characters/csgod.png", xzoom = -1)
image copguy = "characters/copguy.png"
image luke = "characters/luke.png"
image border_guard dusk = "characters/border_guard_dusk.png"
image copguy dark = "characters/copguydark.png"
image copguy_ai = "characters/ai_cop_guy_full.png"
image taran = "characters/taran.png"
image taran flipped = Transform("characters/taran.png", xzoom = -1)
image colton = "characters/colton.png"
image sheriff = "characters/sheriff.png"
image billy = "characters/billy.png"
image billy car = "characters/billy/billy_car.png"
image billy car happy = "characters/billy/billy_car_happy.png"
image billy car turn = "characters/billy/billy_car_turn.png"
image pakoo = "characters/pakoo.png"
image peppino = "characters/peppino.png"
image cultist = "characters/cultist.png"
image cultist_2 = "characters/cultist2.png"
image cultist_3 = "characters/cultist2.png"
image scott = "characters/scott.png"
image terry = "characters/terry.png"

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

## AI Ending
image park1 = "bg/ai/amusementpark1.png"
image park2 = "bg/ai/amusementpark2.png"
image carousel = "bg/ai/carousel.png"
image endingai = "bg/ai/cs_arceus.png"
image entertunnel = "bg/ai/entrancetotunnel.png"
image linusmedia = "bg/ai/linusmedia.png"
image secrettunnel = "bg/ai/secret_tunnel.png"
image ytx = Transform("ytx.png", zoom = 0.333)

# Static Images
image objection = "objection.png"
image hold_it = "hold_it.png"
image scott_border = "scott_border.png"

# Movies
image car background = Movie(play="movies/car_background.mp4")
image car background night = Movie(play="movies/car_background_night.mp4")
image car plains = Movie(play="movies/car_plains.mp4")
image car plains night = Movie(play="movies/car_plains_night.mp4")

# Animated Sprites
image blue_light:
    "blue_light.png"
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.75
    repeat

image red_light:
    "red_light.png"
    alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 0.75
    repeat

# Jump Menu
screen start_menu():
    zorder 100
    style_prefix "start"
    window id "start_window" xalign 0.5 yalign 0.5:
        vbox xalign 0.5 yalign 0.5:
            spacing 50
            text "Start where?" textalign 0.5 size 72 xalign 0.5 yalign 0.5
            hbox xalign 0.5 yalign 0.5:
                spacing 50
                imagebutton auto "menu/csbi_%s.png" hover_sound "sfx-select.wav":
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx-valid.wav"), Hide("start_menu", Fade(1.0)), Jump("csbi_start")
                imagebutton auto "menu/csbii_%s.png" hover_sound "sfx-select.wav":
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx-valid.wav"), Hide("start_menu", Fade(1.0)), Jump("csbii_start")
                imagebutton auto "menu/csbiii1_%s.png" hover_sound "sfx-select.wav":
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx-valid.wav"), Hide("start_menu", Fade(1.0)), Jump("csbiii_start")
                imagebutton auto "menu/csbiii2_%s.png" hover_sound "sfx-select.wav":
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx-valid.wav"), Hide("start_menu", Fade(1.0)), Jump("choose_direction")
                imagebutton idle "missing" hover_sound "sfx-select.wav":
                    action Play("sound", "sfx-valid.wav"), Hide("start_menu", Fade(1.0, 1.0, 1.0)), Jump("play_cargame")

style start_window is empty

label start:
    scene game_menu
    window hide
    pause 0.1
    call screen start_menu()
