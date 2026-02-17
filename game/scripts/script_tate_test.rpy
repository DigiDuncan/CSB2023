### EXPERIMENTAL LAYERED SPRITE, DO NOT USE THIS IN-GAME YET ###

# KNOWN ISSUES:
# you have to specify every thing every time.
# if you want to REMOVE an optional thing, you have to do that manually too.
# ex: remove tate blush
# tate_comp blush -> tate_comp -blush
# to revert back to whatever the default is, you must also specify
# ex: swap tate back to normal outfit after xmas is over
# tate_comp festive -> tate_comp casual
# this means that you can't just swap expressions on the fly, you have to manually change each thing
# shaders and flip are handled weirdly (see below)
# shaders must be un-shadered and flips must be unflipped in the same way as undoing other attributes

layeredimage tate_comp:

    group outfit:
        attribute casual default:
            "/characters/tate/composite_test/body_default.png"
        attribute festive:
            "/characters/tate/composite_test/body_festive.png"

    group blushing:
        attribute default:
            null
        attribute blush:
            "/characters/tate/composite_test/extra_blush.png"

    group face:
        attribute happy default:
            "/characters/tate/composite_test/face_happy.png"
        attribute sad:
            "/characters/tate/composite_test/face_sad.png"
        attribute cry:
            "/characters/tate/composite_test/face_cry.png"
        attribute sheepish:
            "/characters/tate/composite_test/face_sheepish.png"
        attribute shock:
            "/characters/tate/composite_test/face_shock.png"
        attribute serious:
            "/characters/tate/composite_test/face_serious.png"
        attribute smug:
            "/characters/tate/composite_test/face_smug.png"
        attribute stare:
            "/characters/tate/composite_test/face_stare.png"
        attribute furious:
            "/characters/tate/composite_test/face_furious.png"

    group tearful:
        attribute default:
            null
        attribute tears:
            "/characters/tate/composite_test/extra_tears.png"

    group gloomy:
        attribute default:
            null
        attribute gloom:
            "/characters/tate/composite_test/extra_gloom.png"
            blend 'multiply'

# shaders and flip sprite / other transforms must be defined like this, but they can then be used normally

image tate_comp dusk  = LayeredImageProxy("tate_comp", Transform(matrixcolor = duskmatrix))
image tate_comp dark = LayeredImageProxy("tate_comp", Transform(matrixcolor = darkmatrix))
image tate_comp sil_white  = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_white_matrix))
image tate_comp sil_black = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_black_matrix))
image tate_comp sepia = LayeredImageProxy("tate_comp", Transform(matrixcolor = SepiaMatrix()))
image tate_comp selectable = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_select_matrix))

image tate_comp flipped = LayeredImageProxy("tate_comp", Transform(xzoom = -1))

image tate_comp dusk flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = duskmatrix, xzoom = -1))
image tate_comp dark flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = darkmatrix, xzoom = -1))
image tate_comp sil_white flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_white_matrix, xzoom = -1))
image tate_comp sil_black flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_black_matrix, xzoom = -1))
image tate_comp sepia flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = SepiaMatrix(), xzoom = -1))
image tate_comp selectable flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_select_matrix))

# this section is just for fun mostly. a randomizer!
init python:
    def awawa():
        outfits = renpy.random.choice(["casual", "festive"])
        blushing = renpy.random.choice(["-blush", "blush"])
        faces = renpy.random.choice(["happy", "sad", "cry", "sheepish", "shock", "serious", "smug", "stare", "furious"])
        tearful = renpy.random.choice(["-tears", "tears"])
        gloomy = renpy.random.choice(["-gloom", "gloom"])
        shaders = renpy.random.choice(["", "dusk", "dark", "sil_white", "sil_black", "sepia", "selectable"])
        flipper = renpy.random.choice([" -flipped", " flipped"])

        compiled_sprite = "tate_comp " + outfits + " " + blushing + " " + faces + " " + tearful + " " + gloomy + " " + shaders + flipper

        return compiled_sprite

########## ACTUAL TESTING BEGIN ##########

label awawa_tate_test:

    stop music
    scene black with dissolve

    n "You enter Tate's secret test area."

    scene roombacks
    show tate
    with dissolve

    tate "Welcome to my test chamber."

    # Let's test out local labels, too.
    label .awawa_menu:
        scene roombacks
        show tate
        tate "Which test would you like?"
        menu:
            tate "Which test would you like?{fast}"

            #################### SPRITE TESTS ####################
            "Tate's Sprite Experiments":
                menu:
                    tate "Okay, which one?{fast}"
                    ########## SPRITE LAYERS ##########
                    "Layered Sprite Test":
                        hide tate with dissolve
                        n "This test is for Tate's layered sprite."

                        show tate_comp
                        "Default"
                        show tate_comp sad
                        "Sad"
                        show tate_comp cry
                        "Cry"
                        show tate_comp cry tears
                        "Cry + tears"
                        show tate_comp sheepish -tears
                        "Sheepish, force-remove tears"
                        show tate_comp sheepish blush
                        "Sheepish + blushing"
                        show tate_comp shock
                        "Shock"
                        show tate_comp serious -blush
                        "Serious, force-remove blush"
                        show tate_comp smug
                        "Smug"
                        show tate_comp stare
                        "Stare"
                        show tate_comp furious
                        "Furious!"

                        show tate_comp happy festive
                        "Festive! But the happy face has to be forced..."
                        show tate_comp sad festive
                        "Sad Festive"
                        show tate_comp cry tears festive
                        "Cry + tears + Festive"
                        show tate_comp sheepish festive -tears
                        "Sheepish + Festive, force-remove tears"
                        show tate_comp sheepish blush festive
                        "Sheepish + blushing + Festive"
                        show tate_comp shock festive -blush
                        "Shock + Festive, force-remove blush"
                        show tate_comp serious festive
                        "Serious + Festive"
                        show tate_comp smug festive
                        "Smug + Festive"
                        show tate_comp stare festive
                        "Stare + Festive"
                        show tate_comp furious festive
                        "Furious + Festive"
                        show tate_comp furious gloom festive
                        "One angy lil bah humbug (festive + furious + experimental \"gloom\" overlay)"

                        show tate_comp casual happy -gloom
                        "Back to normal!"
                        tate "Shader test!"

                        show tate_comp
                        "Normal"
                        show tate_comp dusk
                        "Dusk"
                        show tate_comp dark
                        "Dark"
                        show tate_comp sil_white
                        "White"
                        show tate_comp sil_black
                        "Black"
                        show tate_comp sepia
                        "Sepia"
                        show tate_comp selectable
                        "Selectable!\n(Well, not really, but this is what it would look like.)"
                        show tate_comp -selectable flipped
                        "Also, let's flip!"
                        show tate_comp -flipped
                        "Flip them back!"

                        show tate_comp casual sheepish
                        tate "Did {i}any{/i} of that work?"
                        hide tate_comp

                        jump .awawa_menu

                    ########## SPRITE RANDOMIZER ##########
                    "Sprite Randomizer":
                        show tate sad
                        tate "Ew, I hate the randomizer."

                        python:
                            iterations = ""
                            iterations = renpy.input("How many iterations?", iterations)

                            try:
                                renpy.hide("tate")
                                renpy.hide("tate_comp")
                                iterations = int(iterations)

                                for i in range(iterations):
                                    this_iteration = awawa()
                                    renpy.show(this_iteration)
                                    narrator(str(i+1) + ": " + this_iteration)

                                renpy.hide("tate_comp")
                                renpy.show("tate", what="tate sheepish")
                                renpy.say(tate, substitutions("Wow, that sucked. But did it work?"))
                            except:
                                renpy.show("tate", what="tate sheepish")
                                renpy.say(tate, substitutions("Something went wrong, sorry."))
                        jump .awawa_menu

                    ########## SELECTABLE FILTER ##########
                    "Selection Filter":
                        hide tate with dissolve
                        n "This is an experimental implementation of an in-engine selectable image filter."
                        n "If this works, we would no longer need to manually create these images!"

                        image txt_awawa_engine:
                            xsize 500
                            ysize 100
                            xanchor 0.5
                            yanchor 0.5
                            contains:
                                Text("{size=+12}In-Engine", xalign=0.5, yalign=0.5)

                        image txt_awawa_image:
                            xsize 500
                            ysize 100
                            xanchor 0.5
                            yanchor 0.5
                            contains:
                                Text("{size=+12}Image", xalign=0.5, yalign=0.5)

                        ### TEST 1: CS ###

                        image h_original_1 = "images/characters/cs/christmas/disappointed.png"
                        image h_engine_1 = "selectable:images/characters/cs/christmas/disappointed.png"
                        image h_image_1 = "/images/unused/ce_point_click/cs_hover.png"

                        show h_original_1 at center
                        n "Here is the original image."

                        show h_engine_1 at left
                        show h_image_1 at right
                        n "And here are the selectable versions. Can you tell which is which?"

                        show txt_awawa_engine at manual_pos(0.15, 0.1, 0.5)
                        show txt_awawa_image at manual_pos(0.825, 0.1, 0.5)

                        show arrow_white flipped as left:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.15

                            block:
                                ypos 0.14
                                linear 0.5 ypos 0.14
                                ypos 0.155
                                linear 0.5 ypos 0.155
                                repeat

                        show arrow_white flipped as right:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.825

                            block:
                                ypos 0.14
                                linear 0.5 ypos 0.14
                                ypos 0.155
                                linear 0.5 ypos 0.155
                                repeat

                        n "Okay, I'll just tell you."
                        n "These ones look identical."
                        n "Let's try another."

                        hide h_original_1
                        hide h_engine_1
                        hide h_image_1
                        hide arrow_white as left
                        hide arrow_white as right
                        hide txt_awawa_engine
                        hide txt_awawa_image
                        with dissolve
                        pause 1.0

                        ### TEST 2: RUG? ###
                        image h_original_2 = "/minigames/christmaspointclick/rug.png"
                        image h_engine_2 = "selectable:/minigames/christmaspointclick/rug.png"
                        image h_image_2 = "/images/unused/ce_point_click/rug_hover.png"

                        show h_original_2 at truecenter:
                            zoom 0.5
                        show h_engine_2 at manual_pos(0.25, 0.5, 0.5):
                            zoom 0.5
                        show h_image_2 at manual_pos(0.75, 0.5, 0.5):
                            zoom 0.5

                        show txt_awawa_engine at manual_pos(0.25, 0.3, 0.5)
                        show txt_awawa_image at manual_pos(0.75, 0.3, 0.5)

                        show arrow_white flipped as left:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.25

                            block:
                                ypos 0.35
                                linear 0.5 ypos 0.35
                                ypos 0.365
                                linear 0.5 ypos 0.365
                                repeat

                        show arrow_white flipped as right:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.75

                            block:
                                ypos 0.35
                                linear 0.5 ypos 0.35
                                ypos 0.365
                                linear 0.5 ypos 0.365
                                repeat

                        n "These also look okay."

                        hide h_original_2
                        hide h_engine_2
                        hide h_image_2
                        hide arrow_white as left
                        hide arrow_white as right
                        hide txt_awawa_engine
                        hide txt_awawa_image

                        ### TEST 3: MEAN ###

                        image h_original_3 = "images/characters/mean/meanhumanannoyedfestive.png"
                        image h_engine_3 = "selectable:images/characters/mean/meanhumanannoyedfestive.png"
                        image h_image_3 = "/images/unused/ce_point_click/mean_hover.png"

                        show h_original_3 at center:
                            zoom 0.8
                        show h_engine_3 at left:
                            zoom 0.8
                        show h_image_3 at right:
                            zoom 0.8

                        show txt_awawa_engine at manual_pos(0.15, 0.1, 0.5)
                        show txt_awawa_image at manual_pos(0.825, 0.1, 0.5)

                        show arrow_white flipped as left:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.15

                            block:
                                ypos 0.14
                                linear 0.5 ypos 0.14
                                ypos 0.155
                                linear 0.5 ypos 0.155
                                repeat

                        show arrow_white flipped as right:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.825

                            block:
                                ypos 0.14
                                linear 0.5 ypos 0.14
                                ypos 0.155
                                linear 0.5 ypos 0.155
                                repeat

                        n "We're 3 for 3!"

                        hide h_original_3
                        hide h_engine_3
                        hide h_image_3
                        hide arrow_white as left
                        hide arrow_white as right
                        hide txt_awawa_engine
                        hide txt_awawa_image

                        ### TEST 4: POSTER ###

                        image h_original_4 = "/minigames/christmaspointclick/poster.png"
                        image h_engine_4 = "selectable:/minigames/christmaspointclick/poster.png"
                        image h_image_4 = "/images/unused/ce_point_click/poster_hover.png"

                        show h_original_4 at truecenter
                        show h_engine_4 at manual_pos(0.25, 0.5, 0.5)
                        show h_image_4 at manual_pos(0.75, 0.5, 0.5)

                        show txt_awawa_engine at manual_pos(0.25, 0.3, 0.5)
                        show txt_awawa_image at manual_pos(0.75, 0.3, 0.5)

                        show arrow_white flipped as left:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.25

                            block:
                                ypos 0.35
                                linear 0.5 ypos 0.35
                                ypos 0.365
                                linear 0.5 ypos 0.365
                                repeat

                        show arrow_white flipped as right:
                            xanchor 0.5 yanchor 0.5
                            rotate 90
                            zoom 0.3
                            xpos 0.75

                            block:
                                ypos 0.35
                                linear 0.5 ypos 0.35
                                ypos 0.365
                                linear 0.5 ypos 0.365
                                repeat

                        n "Another!"

                        hide h_original_4
                        hide h_engine_4
                        hide h_image_4
                        hide arrow_white as left
                        hide arrow_white as right
                        hide txt_awawa_engine
                        hide txt_awawa_image

                        with dissolve
                        n "Let's go back."
                        jump .awawa_menu

                    ########## GO BACK ##########
                    "Never mind.":
                        jump .awawa_menu

            #################### AWAWA MODE ####################
            "Awawa Mode":
                show tate sheepish
                tate "Are you sure? It'll take a while."

                menu:
                    "No, take me back!":
                        jump .awawa_menu
                    "Yes, let's do it.":
                        tate "Alright, we'll try out Awawa Mode."
                        show tate
                        n "Storing initial Awawa Mode values..."

                        # store current awawa settings
                        $ awawa_is_on = preferences.awawa_mode
                        $ awawa_setting = preferences.awawa_chance

                        # begin test
                        $ preferences.awawa_mode = False
                        $ preferences.awawa_chance = 0
                        $ test_string = substitutions("Test dialogue. THIS CODE IS SO STUPID, OMG. \n{i}Italic,{/i} {font=azsz}different font.{/font}{w=0.25} {b}Bold{/b} also exists, but it's {sc=3}ugly as sin.{/sc} {w=0.25}{color=FFFF00}Yellow{/color} is pretty cool, but so is {a=https://allezsoyez.com}my website.{/a}")

                        n "0%% awawa."
                        tate "[test_string]"

                        $ preferences.awawa_mode = True

                        $ preferences.awawa_chance = 0
                        n "25%% awawa."
                        $ preferences.awawa_chance = 25
                        $ test_string = awawa_mode(test_string, preferences.awawa_chance)
                        tate "[test_string]"

                        show tate sheepish
                        $ preferences.awawa_chance = 0
                        n "50%% awawa."
                        $ preferences.awawa_chance = 50
                        $ test_string = awawa_mode(test_string, preferences.awawa_chance)
                        tate "[test_string]"

                        $ preferences.awawa_chance = 100
                        $ test_string = awawa_mode(test_string, preferences.awawa_chance)
                        n "100%% awawa."
                        show tate sheepish blush
                        tate "[test_string]"

                        $ preferences.awawa_mode = awawa_is_on
                        $ preferences.awawa_chance = awawa_setting
                        n "Awawa Mode has been reset to its initial values."

                        show tate srs
                        tate "I sure hope that worked. That's hard to read..."
                        jump .awawa_menu

            #################### SCREEN TESTS ####################
            "Screen Tests":
                menu:
                    tate "Which?{fast}"

                    ########## UNLOCK SCREEN ##########
                    "Unlock Screen":
                        call screen special_unlock("Pretend something cool got unlocked here! Click anywhere to continue.")
                        tate "Lookin' good!"
                        tate "Let's try another!"
                        $ renpy.call_screen("special_unlock", "This screen is called with a Python statement! Use this in menus!")
                        jump .awawa_menu

                    ########## FORCE-TEST ACHIEVEMENTS ##########
                    "Achievement Pop-Ups":

                        tate "Sure, let's try it."

                        python:
                            # TODO: figure out why this pickle crashes on rollback, may be able to fix other pickles in the game too
                            this_cheev = ""
                            this_cheev = renpy.input("Enter the {i}exact{/i} ID of the achievement you want to test.", this_cheev)

                            try:
                                chievos = (a for a in achievement_manager.achievements.values() if a.id == this_cheev)
                                renpy.show_screen("popup", next(chievos))
                                renpy.say(tate, substitutions("Did it work?"))
                            except:
                                renpy.say(tate, substitutions("Couldn't pull achievement. Double-check the name and try again."))

                        jump .awawa_menu

                    ########## Credits Roll ##########
                    "Credits Roll":
                        tate "Which one?"
                        menu:
                            tate "Which one?{fast}"
                            "Full Game (Values Test Only)":
                                call screen credits_roll(duration=60)
                            "Full Game (Correct Timing)":
                                call screen credits_roll()
                            "CE Only":
                                play music "<from 28.700>title_theme_reprise.ogg" noloop
                                call screen credits_roll(route="CSBDX: Holiday Special", scroll_start = 12525, duration=84, replace_music=False) with dissolve
                            "Speedrun Only":
                                call screen credits_roll(bgm="goodbye_speedrun.ogg", duration=9.5) with dissolve
                                stop music
                            "Train Route Only (Incomplete)":
                                call screen credits_roll(route="CSBDX: Train", scroll_start = 12000, duration=60) with dissolve
                                stop music
                            "BT1D Only (Incomplete)":
                                call screen credits_roll(route="CSBDX: BT1D", scroll_start = 10000, duration=60) with dissolve
                                stop music
                            "Never mind.":
                                jump .awawa_menu

                        stop music
                        tate "Did it do what you wanted?"
                        jump .awawa_menu

                    ########## REVERSI RULES ##########
                    "Reversi Rules Image":
                        tate "Let's check it out!"
                        show reversi_rules at truecenter
                        pause
                        hide reversi_rules
                        tate "Did it work?"
                        jump .awawa_menu

                    ########## ACEN'T ATTORNEYN'T SCREEN ##########
                    "Ace Attorney Parody":
                        tate "Alrighty, then..."
                        call screen acent_attorneynt(chosen_evidence)
                        hide screen acent_attorneynt
                        tate "Did it work? On my end, you selected item [chosen_evidence]."
                        jump .awawa_menu

                    ########## GO BACK ##########
                    "Never mind.":
                        jump .awawa_menu

            #################### PERFECT TATE TESTS ####################
            "VS Perfect Tate Tests":
                menu:
                    tate "Which one?{fast}"
                    "CS Running Animation":
                        show cs_run at manual_pos(0.75, 0.5, 0.5)
                        tate "Is this what you wanted?"
                        hide cs_run
                    "CS Health Indicator":
                        image health_test = Fixed("/minigames/perfecttate/heart.png", Text("100", size=69, xanchor=0.5, yanchor=0.5, xalign=0.5, yalign=0.4, text_align=0.5), xysize=(128,128))
                        show health_test at manual_pos(8, 8, 0)
                        tate "Is that correct?"
                        hide health_test
                    "Sigil Test":

                        # TODO: somehow combine t_tate_sigil_text into here...? can this even be done??
                        image tate_sigil = Fixed(
                            At(Image("/secret/pt/sigil_inner.png", xanchor=0.5, yanchor=0.5, xalign=0.5, yalign=0.5, alpha=0.6), Transform(alpha=0.6)),
                            At(Image("/secret/pt/sigil_text.png", xanchor=0.5, yanchor=0.5, xalign=0.5, yalign=0.5), t_tate_sigil_text)
                        )

                        show tate_sigil at truecenter behind tate:
                            xysize (2000,2000)
                            zoom 0.75
                            blur 5

                        show tate srs
                        tate "It {i}is{/i} drawn {i}correctly{/i} this time, right?"
                        hide tate_sigil
                    "Green Screen Test":
                        scene green_screen
                        pause
                        pakoo_offscreen "" # this is on purpose, i need the delay for screen recording
                        pakoo_offscreen "Hey! You,{w=0} there!"
                        pakoo_offscreen "Just what do you think you're doing down there?!"
                    "Never mind.":
                        jump .awawa_menu
                jump .awawa_menu

            #################### Cancel ####################

            "None, I'm Done":
                tate "Cool. See ya later!"
                $ renpy.full_restart
