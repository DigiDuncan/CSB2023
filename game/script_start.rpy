# Custom preferences
default persistent.text_beeps = True
default persistent.csbounciness = 0

# Text beeps
init python:
    def cs_beep(event, **kwargs):
        if persistent.text_beeps:
            if event == "show":
                renpy.music.play("audio/text/cstalk.wav", channel="sound", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound")

#CSB1 Character Definitions
define n = Character("", what_italic = True, window_background = "gui/textbox_alt.png")  # Narrator
define cs = Character("cs188", callback = cs_beep)
define craptop = Character("Craptop")
define sticky = Character("Sticky Note")
define discord = Character("Discord")
define nova = Character("Nova")
define carguy = Character("Car Guy")
define greeter = Character("Greeter")
define doug = Character("Doug")
define cashier = Character("Cashier")
define ycs = Character("Young CS")
define hoh_operator = Character("HoH SiS Operator")
define rich = Character("Richard")
define ed = Character("Ed")
define wesley = Character("Wesley")
define michael = Character("Michael")
define phil = Character("Phil")
define worker_1 = Character("Worker 1")
define worker_2 = Character("Worker 2")
define worker_3 = Character("Worker 3")
define worker_4 = Character("Worker 4")
define worker_5 = Character("Worker 5")
define worker_6 = Character("Worker 6")
define worker_7 = Character("Worker 7")
define digi = Character("Digi")

#CSB1 Character Images
image cs_neutral = "characters/cs.png"
image cs_happy = "characters/cs_happy.png"
image cs_angry = "characters/cs_angry.png"
image cs_worried = "characters/cs_worried.png"
image cs_disappointed = "characters/cs_disappointed.png"
image discord = "characters/discord.png"
image nova = "characters/nova.png"
image carguy = "characters/carguy.png"
image doug = "characters/ceo.png"
image cashier = "characters/cashier.png"
image young_cs = "characters/cs_young.png"
image rich = "characters/richard.png"
image ed = "characters/ed.png"
image wesley = "characters/wesley.png"
image michael = "characters/rosen.png"
image phil = "characters/phil.png"
image worker_1 = "characters/worker_corn.png"
image worker_2 = "characters/worker_blank.png"
image worker_3 = "characters/worker_mean.png"
image worker_4 = "characters/worker_eville.png"
image worker_5 = "characters/eddie_down.png"
image worker_5alt = "characters/eddie_up.png"
image worker_6 = "characters/worker_pineapple.png"
image worker_7 = "characters/worker_chicken.png"

#CSB1 Background Images
image black = "bg/black.png"
image cs_room = "bg/cs_bedroom1.png"
image cs_room_2 = "bg/cs_bedroom2.png"
image craptop_desktop = "bg/Craptop_Desktop.png"
image craptop_update = "bg/Craptop_Updating.png"
image craptop_car = "bg/craptop_car.png"
image craptop_discord = "bg/craptop_sad.png"
image craptop_edit = "bg/craptop_edit.png"
image craptop_error = "bg/Craptop_error.png"
image craptop_yt = "bg/craptop_ytp.png"
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
define copguy = Character("CopGuy")
define arceus = Character("Arceus")
define anno = Character("Anno")
define border_guard = Character("Border Guard")
define linus = Character("Linus")

# CSB2 Character Images
image ed_phone = "characters/ed_phone.png"
image arceus = "characters/arceus.png"
image arceus flipped = Transform("characters/arceus.png", xzoom = -1)
image anno = "characters/anno.png"
image border_guard = "characters/border_guard.png"
image linus = "characters/linus.png"

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
label start:
    scene black
    menu:
        "Start where?"

        "CSBounciness I":
            jump csbi_start
        "CSBounciness II":
            jump csbii_start
        "CSBounciness III":
            jump csbiii_start
