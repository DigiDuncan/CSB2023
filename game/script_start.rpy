# Text beeps
init python:
    renpy.music.register_channel("beep", "voice", loop = True)
    def beep(event, name = None, **kwargs):
        if preferences.text_beeps:
            if event == "show":
                if name is not None:
                    renpy.sound.play(f"audio/text/{name}.wav", channel = "beep", loop = True)
                    print(name)
                else:
                    renpy.sound.play(f"audio/text/ut.wav", channel = "beep", loop = True)
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel="beep")

# If music is so good, why is there no Music 2?
init python:
    renpy.music.register_channel("music2", "music")

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

transform mid_left:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.25

transform mid_right:
    yanchor 1.0 ypos 1.0
    xanchor 0.5 xpos 0.75

transform mid_center_right:
    yanchor 0.5 ypos 0.5
    xanchor 0.5 xpos 0.75

transform t_post_it:
    subpixel True
    xanchor 0.5 yanchor 0.0
    xpos 0.65 ypos 0.025
    zoom 0.3333
    rotate 10

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

#CSB1 Character Definitions
define n = Character(None, what_italic = True)  # Narrator
define cs = Character("cs188", callback = renpy.partial(beep, name = "cs"))
define craptop = Character("Craptop", callback = beep)
define sticky = Character("Sticky Note", callback = beep)
define discord = Character("Discord", callback = beep)
define nova = Character("Nova", callback = beep)
define carguy = Character("Car Guy", callback = renpy.partial(beep, name = "nice"))
define carguy_nobeep = Character("Car Guy")
define greeter = Character("Greeter", callback = beep)
define doug = Character("Doug", callback = beep)
define cashier = Character("Cashier", callback = beep)
define ycs = Character("Young CS", callback = renpy.partial(beep, name = "ycs"))
define hoh_operator = Character("HoH SiS Operator", callback = beep)
define rich = Character("Richard", callback = renpy.partial(beep, name = "rich"))
define ed = Character("Ed", callback = renpy.partial(beep, name = "ed"))
define wesley = Character("Wesley", callback = renpy.partial(beep, name = "wes"))
define michael = Character("Michael", callback = renpy.partial(beep, name = "mich"))
define michael_nobeep = Character("Michael")
define phil = Character("Phil", callback = renpy.partial(beep, name = "phil"))
define worker_1 = Character("Worker 1", callback = beep)
define worker_2 = Character("Worker 2", callback = beep)
define worker_3 = Character("Worker 3", callback = beep)
define worker_4 = Character("Worker 4", callback = beep)
define worker_5 = Character("Worker 5", callback = beep)
define worker_6 = Character("Worker 6", callback = beep)
define worker_7 = Character("Worker 7", callback = beep)
define digi = Character("Digi", callback = renpy.partial(beep, name = "digi"))

#CSB1 Character Images
image cs = "characters/cs/neutral.png"
image cs flipped = Transform("characters/cs/neutral.png", xzoom = -1)
image cs happy = "characters/cs/happy.png"
image cs angry = "characters/cs/angry.png"
image cs worried = "characters/cs/worried.png"
image cs worried flipped = Transform("characters/cs/worried.png", xzoom = -1)
image cs disappointed = "characters/cs/disappointed.png"
image cs concentrate = "characters/cs/concentrate.png"
image discord = "characters/discord.png"
image nova = "characters/nova.png"
image carguy = "characters/carguy.png"
image doug = "characters/doug.png"
image cashier = "characters/cashier.png"
image young_cs = "characters/cs_young.png"
image rich = "characters/rich.png"
image ed = "characters/ed.png"
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

# CSB1 Craptop
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

#CSB1 Background Images
image black = "bg/black.png"
image cs_room = "bg/cs_bedroom1.png"
image cs_room_2 = "bg/cs_bedroom2.png"
image craptop_bg = "bg/craptop_bg.png"
image cs_house = "bg/Cs_house.png"
image cs_car = "bg/car_driveway.png"
image cs_car_inside = "bg/car_inside.png"
image walmart_outside = "bg/Walmart_Outside.png"
image walmart_inside = "bg/walmart_inside.png"
image walmart_aisle = "bg/walmart_shelf.png"
image walmart_register = "bg/walmart_checkout.png"
image cs_door_closed = "bg/door_closed.png"
image cs_door_open = "bg/door_open.png"
image rosen_abode = "bg/rosenabode.png"
image hoh_outside = "bg/office_outside.png"
image hoh_hq = "bg/office1.png"
image hoh_hq2 = "bg/office2.png"
image hoh_hq3 = "bg/office3.png"
image hoh_hq4 = "bg/office4.png"
image hoh_hq5 = "bg/office5.png"

# CSB2 Character Definitions
define copguy = Character("CopGuy", callback = renpy.partial(beep, name = "cop"))
define arceus = Character("Arceus", callback = renpy.partial(beep, name = "arc"))
define anno = Character("Anno", callback = renpy.partial(beep, name = "anno"))
define border_guard = Character("Border Guard", callback = beep)
define linus = Character("Linus", callback = renpy.partial(beep, name = "ltt"))
define asylum_worker = Character("Mr Mohs", callback = beep)
define csgod = Character("CS God", callback = renpy.partial(beep, name = "csgod"))

# CSB2 Character Images
image ed phone = "characters/ed_phone.png"
image arceus = "characters/arceus.png"
image arceus flipped = Transform("characters/arceus.png", xzoom = -1)
image anno = "characters/anno.png"
image anno prison = "characters/anno_prison.png"
image anno guard = "characters/anno_guard.png"
image cs prison = "characters/cs/prison.png"
image cs prison_worried = "characters/cs/prison_worried.png"
image cs guard = "characters/cs/guard.png"
image border_guard = "characters/border_guard.png"
image linus = "characters/linus.png"
image asylum_worker = "characters/asylum_worker.png"
image csgod = "characters/cs_god.png"

# CSB2 Background Images
image helipad = "bg/helipad.png"
image cs_street = "bg/cs_street.png"
image jail_inside = "bg/jail_inside.png"
image jail_cell = "bg/jail_cell.png"
image border = "bg/canadian_border.png"
image outside_tim_hortons = "bg/outside_tim_hortons.png"
image inside_tim_hortons = "bg/inside_tim_hortons.png"
image tunnel = "bg/tunnel.png"
image canada = "bg/canada.png"
image flag = "bg/americanflag.png"
image outside_ltt = "bg/linus_office_outside.png"
image inside_ltt = "bg/linus_hallway.png"
image alley = "bg/alley.png"
image question = "bg/police_interrogation.png"
image asylum = "bg/asylum2.png"

# CSB3 Character Definitions
define luke = Character("Luke", callback = renpy.partial(beep, name = "luke"))
define taran = Character("Taran", callback = beep)

# CSB3 Character Images
image luke = "characters/luke.png"
image copguy_ai = "characters/ai_cop_guy_full.png"
image taran flipped = Transform("characters/taran.png", xzoom = -1)

# CSB3 Background Images
image csdesk = "bg/cs_desk.png"
image csvideo = "bg/csvideo.png"
# AI Ending
image park1 = "bg/ai/amusementpark1.png"
image park2 = "bg/ai/amusementpark2.png"
image carousel = "bg/ai/carousel.png"
image endingai = "bg/ai/cs_arceus.png"
image entertunnel = "bg/ai/entrancetotunnel.png"
image linusmedia = "bg/ai/linusmedia.png"
image secrettunnel = "bg/ai/secret_tunnel.png"

# Animated sprites
image blue_light:
    "blue_light.png"
    alpha 0.0
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat

image red_light:
    "red_light.png"
    alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0
    repeat

# Jump menu
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
                imagebutton auto "menu/csbiii_%s.png" hover_sound "sfx-select.wav":
                    at transform:
                        zoom 0.666
                    action Play("sound", "sfx-valid.wav"), Hide("start_menu", Fade(1.0)), Jump("csbiii_start")

style start_window is empty

label start:
    scene black
    window hide
    pause 0.1
    call screen start_menu()
