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
        attribute beach:
            "/characters/tate/composite_test/body_beach.png"

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
image tate_comp selectable = LayeredImageProxy("tate_comp", Transform(matrixcolor = shade_select_matrix))

image tate_comp flipped = LayeredImageProxy("tate_comp", Transform(xzoom = -1))

image tate_comp dusk flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = duskmatrix, xzoom = -1))
image tate_comp dark flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = darkmatrix, xzoom = -1))
image tate_comp sil_white flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_white_matrix, xzoom = -1))
image tate_comp sil_black flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_black_matrix, xzoom = -1))
image tate_comp sepia flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = SepiaMatrix(), xzoom = -1))
image tate_comp selectable flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = shade_select_matrix))

# this section is just for fun mostly. a randomizer!
init python:
    def awawa():
        outfits = renpy.random.choice(["casual", "festive", "beach"])
        blushing = renpy.random.choice(["-blush", "blush"])
        faces = renpy.random.choice(["happy", "sad", "cry", "sheepish", "shock", "serious", "smug", "stare", "furious"])
        tearful = renpy.random.choice(["-tears", "tears"])
        gloomy = renpy.random.choice(["-gloom", "gloom"])
        shaders = renpy.random.choice(["", "dusk", "dark", "sil_white", "sil_black", "sepia", "selectable"])
        flipper = renpy.random.choice([" -flipped", " flipped"])

        compiled_sprite = "tate_comp " + outfits + " " + blushing + " " + faces + " " + tearful + " " + gloomy + " " + shaders + flipper

        return compiled_sprite

########## ACTUAL TESTING BEGIN ##########

label _awawa_tate_test:

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
                                Text( _("{size=+12}In-Engine"), xalign=0.5, yalign=0.5)

                        image txt_awawa_image:
                            xsize 500
                            ysize 100
                            xanchor 0.5
                            yanchor 0.5
                            contains:
                                Text( _("{size=+12}Image"), xalign=0.5, yalign=0.5)

                        ### TEST 1: CS ###

                        image h_original_1 = "images/characters/cs/christmas/disappointed.png"
                        image h_engine_1 = "selectable:images/characters/cs/christmas/disappointed.png"
                        image h_image_1 = "/minigames/christmaspointclick/test/cs_hover.png"

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
                        image h_image_2 = "/minigames/christmaspointclick/test/rug_hover.png"

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
                        image h_image_3 = "/minigames/christmaspointclick/test/mean_hover.png"

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
                        image h_image_4 = "/minigames/christmaspointclick/test/poster_hover.png"

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

                    ########## CSGOD TEST ##########
                    "CSGod Renderer":
                        tate "Alright, let's see..."
                        show tate at left with move
                        tate "Hey, CSGod!"
                        show expression csgod_sprite(flipped=True) as csgod at center with dissolve
                        csgod "You rang?"
                        tate "Sure did!"
                        tate "Please show our guest your new glowing skills."
                        show expression csgod_sprite("happy", 5, True) as csgod
                        csgod "Alright."
                        show tate stare
                        show expression csgod_sprite("happy", 25, True) as csgod with dissolve
                        tate "Cool."
                        show tate
                        tate "Can you go bigger?"
                        show expression csgod_sprite("neutral", 25, True) as csgod
                        csgod "Sure. Stand back!"
                        show expression csgod_sprite("neutral", 25, False) as csgod at right with move
                        show expression csgod_sprite("neutral", 25, True) as csgod
                        pause 0.5
                        show expression csgod_sprite("concentrate", 25, True) as csgod
                        pause 0.5
                        show expression csgod_sprite("concentrate", 100, True) as csgod with dissolve
                        show expression csgod_sprite("neutral", 100, True) as csgod
                        csgod "How's that?"
                        tate "Perfect! Thank you."
                        show expression csgod_sprite("happy", 100, True) as csgod
                        csgod "No problem. See ya 'round."

                        scene roombacks
                        show tate at left
                        with dissolve

                        show tate at center with move

                    ########## GO BACK ##########
                    "Never mind.":
                        pass
                    
                jump .awawa_menu

            #################### AWAWA MODE ####################
            "Awawa Mode":
                show tate sheepish
                tate "Are you sure? It'll take a while."

                menu:
                    "No, take me back!":
                        pass
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
                                call screen credits_roll(route="CSBDX: Holiday Special", scroll_start = 1204, duration=84, replace_music=False) with dissolve
                            "Speedrun Only":
                                call screen credits_roll(bgm="goodbye_speedrun.ogg", duration=9.5) with dissolve
                                stop music
                            "Train Route Only (Incomplete)":
                                call screen credits_roll(route="CSBDX: Train", duration=60) with dissolve
                                stop music
                            "BT1D Only (Incomplete)":
                                call screen credits_roll(route="CSBDX: BT1D", duration=60) with dissolve
                                stop music
                            "Never mind.":
                                pass

                        stop music
                        tate "Did it do what you wanted?"

                    ########## REVERSI RULES ##########
                    "Reversi Rules Image":
                        tate "Let's check it out!"
                        show reversi_rules at truecenter
                        pause
                        hide reversi_rules
                        tate "Did it work?"

                    ########## ACEN'T ATTORNEYN'T SCREEN ##########
                    "Ace Attorney Parody":
                        tate "Alrighty, then..."
                        call screen acent_attorneynt(chosen_evidence)
                        hide screen acent_attorneynt
                        tate "Did it work? On my end, you selected item [chosen_evidence]."

                    ########## WHERE ARE THEY NOW REDUX ##########
                    "Where Are They Now? V2":
                        tate "Aight."
                        $ renpy.call_replay("where_are_they_now")
                        tate "Was that right?"

                    ########## BAD ENDING REDUX ##########
                    "Bad Ending V2":
                        tate "Here it is!"
                        call screen bad_ending()
                        tate "Did it do?"

                    ########## GO BACK ##########
                    "Never mind.":
                        pass
                    
                jump .awawa_menu

            #################### PERFECT TATE TESTS ####################
            "VS Perfect Tate Tests":

                # This menu is also a test.
                if persistent.defeated_perfect_tate == False:
                    show tate sheepish
                    tate "Are you sure? It looks like you haven't seen that fight yet."
                    menu:
                        tate "Are you okay with spoilers?{fast}"
                        "Yes":
                            pass
                        "No":
                            jump .awawa_menu

                menu:
                    tate "Alright, which test?{fast}"

                    "CS Running Animation":
                        show cs_run at manual_pos(0.75, 0.5, 0.5)
                        tate "Is this what you wanted?"
                        hide cs_run

                    "CS Health Indicator":
                        image health_test = Fixed("/minigames/perfecttate/heart.png", Text( _("100"), size=69, xanchor=0.5, yanchor=0.5, xalign=0.5, yalign=0.4, text_align=0.5), xysize=(128,128))
                        show health_test at manual_pos(8, 8, 0)
                        tate "Is that correct?"
                        hide health_test

                    "Sigil Test 1":
                        show tate_sigil at truecenter behind tate
                        show tate srs
                        tate "It {i}is{/i} drawn {i}correctly{/i} this time, right?"
                        hide tate_sigil

                    "Sigil Test 2":
                        show amtrak_reality_break
                        tate "Is that right?"
                        show tate_ex at center
                        tate "Am I doing this right??"
                        hide amtrak_reality_break
                        hide tate_ex
                        with dissolve

                    "Green Screen Test":
                        scene green_screen
                        pause
                        pakoo_offscreen "" # this is on purpose, i need the delay for screen recording
                        pakoo_offscreen "Hey! You,{w=0} there!"
                        pakoo_offscreen "Just what do you think you're doing down there?!"
                    "Never mind.":
                        pass

                jump .awawa_menu

            #################### GAME TESTS ####################
            "Game Tests":
                menu:
                    tate "Which one?"
                    "Tic-Tac-Toe":
                        tate "Alright, let's play!"
                        call screen test_ttt
                
                    "Tarot Reading":
                        show tate sheepish
                        tate "Sure. I'm not great at it yet, but I'll try it."
                        call screen test_tarot with dissolve
                        tate "Now, as for what this reading actually means for {i}you?"
                        tate "Hell if I know."
      
                    "Blackjack":
                        show tate
                        tate "Alright, I'll summon {color=#52A42A}the dealer{/color}. You will also be playing by casino rules."
                        tate "This means that ace cards are {a=https://officialgamerules.org/game-rules/blackjack/}flexible{/a} and that the dealer must hit if his hand is below 17."
                        window hide
                        call screen minigame_blackjack(cpu_1 = "Tate", cpu_2 = "Digi")
                        pause 1.0
                        if _return == True:
                            tate "Nice work."
                        else: 
                            show tate sheepish
                            tate "Better luck next time."

                    "Pencil: Rewritten":
                        show tate sheepish
                        tate "Hope it works."
                        call screen pencilgame()
                        if _return[0] == True:
                            show tate stare
                            tate "Well, hot damn!"
                            show tate
                            tate "Hope your wrist doesn't hurt tomorrow."
                        elif _return[0] == False:
                            show tate sheepish
                            tate "Yeah, that game's hard, huh?"
                        else:
                            show tate sheepish
                            tate "Huh. I think something's busted."
                        tate "Looks like you managed [_return[1]] centimeters."

                    "Click / Drag Test":
                        show tate sheepish
                        tate "What {i}is{/i} this?"
                        call screen click_drag_test()
                        tate "Well, that was weird."

                    "Rails Test":
                        show tate sheepish
                        tate "Hoo boy. This probably won't work."
                        call screen rails_test()
                        tate "Was I right?"

                jump .awawa_menu

            #################### Cancel ####################
            "None, I'm Done":
                tate "Cool. See ya later!"
                $ renpy.full_restart

####################################################################################################

init python:
    def who_won_ttt(grid: list[str]) -> str | None:
        # 0 1 2
        # 3 4 5
        # 6 7 8
        win_states = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        )

        for player in ["X", "O"]:
            for state in win_states:
                if all([grid[pos] == player for pos in state]):
                    return player

        if "" not in grid:
            return "T"

        return None

screen test_ttt():
    modal True
    
    on "show":
        action [
            Function(renpy.music.play, audio.in_the_room, if_changed=True)
        ]
    
    default ttt_grid = [
        "","","",
        "","","",
        "","",""
    ]
    default ttt_state = "turns"
    default player_symbol = ""
    default opponent_symbol = ""
    default whose_turn = None
    default ttt_won = None
    default next_state = None

    #text str(ttt_won)

    # Who goes first?
    if ttt_state == "turns":
        frame: 
            xsize 950 ysize 200
            xalign 0.5 yalign 0.5

            text _("Who should go first?"):
                xalign 0.5 yalign 0.2 text_align 0.5

            textbutton _("You"):
                xalign 0.3 yalign 0.8 text_align 0.5
                action [
                    SetScreenVariable("whose_turn", 0),
                    SetScreenVariable("ttt_state", "symbols")
                ]
            textbutton _("Tate"):
                xalign 0.7 yalign 0.8 text_align 0.5
                action [
                    SetScreenVariable("whose_turn", 1),
                    SetScreenVariable("ttt_state", "symbols")
                ]
    # X or O?
    elif ttt_state == "symbols":
        frame: 
            xsize 950 ysize 200
            xalign 0.5 yalign 0.5

            text _("Do you want to use X or O?"):
                xalign 0.5 yalign 0.2 text_align 0.5

            textbutton "X":
                xalign 0.3 yalign 0.8 text_align 0.5
                action [
                    SetScreenVariable("player_symbol", "X"),
                    SetScreenVariable("opponent_symbol", "O"),
                    SetScreenVariable("ttt_state", "play")
                ]
            textbutton "O":
                xalign 0.7 yalign 0.8 text_align 0.5
                action [
                    SetScreenVariable("player_symbol", "O"),
                    SetScreenVariable("opponent_symbol", "X"),
                    SetScreenVariable("ttt_state", "play")
                ]
    # Play the game!
    elif ttt_state == "play":
        frame:
            xsize 950 ysize 950
            xalign 0.5 yalign 0.5

            grid 3 3:
                xalign 0.5 yalign 0.5

                for t in range(len(ttt_grid)):

                    frame:
                        xsize 300 ysize 300
                        text ttt_grid[t]:
                            xalign 0.5 yalign 0.5 text_align 0.5
                            size 112

                        button: 
                            xsize 1.0 ysize 1.0

                            if ttt_won is None:
                                if whose_turn == 0:
                                    if ttt_grid[t] == "":
                                        action [
                                            SetDict(ttt_grid, t, player_symbol),
                                            SetScreenVariable("ttt_state", "wait"),
                                            SetScreenVariable("next_state", "play"),
                                            SetScreenVariable("whose_turn", 1),
                                            SetScreenVariable("ttt_won", who_won_ttt(ttt_grid)),
                                            Function(renpy.restart_interaction)
                                        ]

    elif ttt_state == "end":
        if ttt_won == player_symbol:
            $ result = _("You win!")
        elif ttt_won == opponent_symbol:
            $ result = _("Tate wins!")
        else:
            $ result = _("It's a draw!")

        frame: 
            xsize 950 ysize 200
            xalign 0.5 yalign 0.5

            text result+_(" Play again?"):
                xalign 0.5 yalign 0.2 text_align 0.5

            textbutton _("Yes"):
                xalign 0.3 yalign 0.8 text_align 0.5
                action [
                    SelectedIf(False),
                    Hide("test_ttt"),
                    ShowTransient("test_ttt")
                ]
            textbutton _("No"):
                xalign 0.7 yalign 0.8 text_align 0.5
                action [
                    Stop("music", fadeout=0.5),
                    Jump("_awawa_tate_test.awawa_menu")
                ]

    elif ttt_state == "wait":
        timer 0.5 action SetScreenVariable("ttt_state", next_state)
        frame:
            xsize 950 ysize 950
            xalign 0.5 yalign 0.5

            grid 3 3:
                xalign 0.5 yalign 0.5

                for t in range(len(ttt_grid)):

                    frame:
                        xsize 300 ysize 300
                        text ttt_grid[t]:
                            xalign 0.5 yalign 0.5 text_align 0.5
                            size 112

    # This is how we have to do logic in screens.
    # Basically, we check to see if we're in the right state, and then execute the code we want.
    # This is because the if/elif in the screen ALWAYS runs, so we need to lock it down.
    python:
        # ENEMY TURN
        if ttt_state == "play" and whose_turn == 1:
            opponent_filled = renpy.random.randrange(0,9)
            while True and "" in ttt_grid:
                opponent_filled = renpy.random.randrange(0,9)
                if ttt_grid[opponent_filled] == "":
                    ttt_grid[opponent_filled] = opponent_symbol
                    break

            ttt_won = who_won_ttt(ttt_grid)
            whose_turn = 0
            renpy.restart_interaction()

        # TEST FOR MOVE TO END STATE
        if ttt_state == "play" and ttt_won is not None:
            ttt_state = "end"
            renpy.restart_interaction()

####################################################################################################

screen test_tarot():
    modal True

    add gui.game_menu_background:
        alpha 0.5

    # This should probably be a JSON but uhhhhh not now lol
    # TODO: figure out how to mark the whole deck translatable
    default tarot_deck = [
        # MAJOR ARCANA
        {"name": "The Fool", "upright": "Beginnings, Innocence, Trust", "reversed": "Recklessness, Fear, Naivety"},
        {"name": "The Magician", "upright": "Manifestation, Willpower, Skill", "reversed": "Manipulation, Disconnection, Waste"},
        {"name": "The High Priestess", "upright": "Intuition, Mystery, Depth", "reversed": "Secrets, Confusion, Suppression"},
        {"name": "The Empress", "upright": "Abundance, Nurturing, Fertility", "reversed": "Dependence, Smothering, Neglect"},
        {"name": "The Emperor", "upright": "Authority, Structure, Protection", "reversed": "Tyranny, Rigidity, Insecurity"},
        {"name": "The Hierophant", "upright": "Tradition, Belief, Ethics", "reversed": "Rebellion, Restriction, Misalignment"},
        {"name": "The Lovers", "upright": "Love, Connection, Choice", "reversed": "Temptation, Imbalance, Conflict"},
        {"name": "The Chariot", "upright": "Discipline, Willpower, Victory", "reversed": "Aimlessness, Aggression, Defeat"},
        {"name": "Strength", "upright": "Courage, Restraint, Compassion", "reversed": "Doubt, Weakness, Impulse"},
        {"name": "The Hermit", "upright": "Introspection, Solitude, Wisdom", "reversed": "Isolation, Loneliness, Withdrawal"},
        {"name": "The Wheel Of Fortune", "upright": "Destiny, Cycles, Fortune", "reversed": "Misfortune, Resistance, Stagnation"},
        {"name": "Justice", "upright": "Fairness, Truth, Accountability", "reversed": "Unfairness, Dishonesty, Imbalance"},
        {"name": "The Hanged Man", "upright": "Surrender, Perspective, Waiting", "reversed": "Indecision, Delay, Resistance"},
        {"name": "Death", "upright": "Transformation, Endings, Change", "reversed": "Resistance, Clinging, Decay"},
        {"name": "Temperance", "upright": "Balance, Moderation, Integration", "reversed": "Imbalance, Excess, Discord"},
        {"name": "The Devil", "upright": "Temptation, Shadow, Bondage", "reversed": "Liberation, Awareness, Reclamation"},
        {"name": "The Tower", "upright": "Upheaval, Chaos, Revelation", "reversed": "Turmoil, Denial, Resistance"},
        {"name": "The Star", "upright": "Hope, Renewal, Inspiration", "reversed": "Despair, Pessimism, Disconnection"},
        {"name": "The Moon", "upright": "Illusion, Emotion, Subconscious", "reversed": "Unveiling, Deception, Anxiety"},
        {"name": "The Sun", "upright": "Joy, Success, Vitality", "reversed": "Depression, Failure, Ego"},
        {"name": "Judgment", "upright": "Awakening, Redemption, Reckoning", "reversed": "Doubt, Avoidance, Regret"},
        {"name": "The World", "upright": "Completion, Achievement, Unity", "reversed": "Fragmentation, Incompletion, Delay"},

        # WANDS
        {"name": "Ace of Wands", "upright": "Creation, Willpower, Inspiration", "reversed": "Delays, Blocks, Stagnation"},
        {"name": "2 of Wands", "upright": "Planning, Progress, Decisions", "reversed": "Indecision, Roadblocks, Fear"},
        {"name": "3 of Wands", "upright": "Expansion, Growth, Foresight", "reversed": "Obstacles, Delays, Setbacks"},
        {"name": "4 of Wands", "upright": "Celebration, Harmony, Home", "reversed": "Instability, Transition, Disharmony"},
        {"name": "5 of Wands", "upright": "Conflict, Competition, Tension", "reversed": "Resolution, Compromise, Truce"},
        {"name": "6 of Wands", "upright": "Victory, Success, Recognition", "reversed": "Failure, Ego, Pride"},
        {"name": "7 of Wands", "upright": "Challenge, Perseverance, Defense", "reversed": "Surrender, Exhaustion, Defeat"},
        {"name": "8 of Wands", "upright": "Movement, Speed, Progress", "reversed": "Delays, Frustration, Obstacles"},
        {"name": "9 of Wands", "upright": "Resilience, Courage, Persistence", "reversed": "Weakness, Burnout, Exhaustion"},
        {"name": "10 of Wands", "upright": "Burden, Responsibility, Stress", "reversed": "Overwhelm, Collapse, Delegation"},
        {"name": "Page of Wands", "upright": "Exploration, Enthusiasm, Discovery", "reversed": "Aimlessness, Procrastination, Impulsiveness"},
        {"name": "Knight of Wands", "upright": "Energy, Action, Adventure", "reversed": "Impatience, Recklessness, Frustration"},
        {"name": "Queen of Wands", "upright": "Courage, Confidence, Determination", "reversed": "Selfishness, Jealousy, Dominance"},
        {"name": "King of Wands", "upright": "Leadership, Vision, Authority", "reversed": "Impulsiveness, Dominance, Tyranny"},

        # PENTACLES
        {"name": "Ace of Pentacles", "upright": "Opportunity, Prosperity, Abundance", "reversed": "Loss, Misfortune, Scarcity"},
        {"name": "2 of Pentacles", "upright": "Balance, Adaptability, Juggling", "reversed": "Imbalance, Disorder, Overwhelm"},
        {"name": "3 of Pentacles", "upright": "Teamwork, Collaboration, Learning", "reversed": "Discord, Competition, Mediocrity"},
        {"name": "4 of Pentacles", "upright": "Security, Control, Conservation", "reversed": "Hoarding, Insecurity, Greed"},
        {"name": "5 of Pentacles", "upright": "Hardship, Loss, Isolation", "reversed": "Recovery, Growth, Assistance"},
        {"name": "6 of Pentacles", "upright": "Charity, Generosity, Sharing", "reversed": "Manipulation, Selfishness, Debt"},
        {"name": "7 of Pentacles", "upright": "Patience, Investment, Growth", "reversed": "Impatience, Waste, Stagnation"},
        {"name": "8 of Pentacles", "upright": "Diligence, Skill, Craftsmanship", "reversed": "Shortcuts, Laziness, Mediocrity"},
        {"name": "9 of Pentacles", "upright": "Independence, Luxury, Abundance", "reversed": "Materialism, Extravagance, Dependency"},
        {"name": "10 of Pentacles", "upright": "Legacy, Wealth, Family", "reversed": "Conflict, Failure, Instability"},
        {"name": "Page of Pentacles", "upright": "Study, Opportunity, Growth", "reversed": "Procrastination, Idleness, Stagnation"},
        {"name": "Knight of Pentacles", "upright": "Diligence, Reliability, Patience", "reversed": "Laziness, Boredom, Stagnation"},
        {"name": "Queen of Pentacles", "upright": "Nurturing, Practical, Abundance", "reversed": "Selfishness, Jealousy, Smothering"},
        {"name": "King of Pentacles", "upright": "Wealth, Success, Security", "reversed": "Greed, Exploitation, Stubbornness"},

        # SWORDS
        {"name": "Ace of Swords", "upright": "Clarity, Truth, Breakthrough", "reversed": "Confusion, Deception, Hostility"},
        {"name": "2 of Swords", "upright": "Decision, Stalemate, Balance", "reversed": "Indecision, Confusion, Overwhelm"},
        {"name": "3 of Swords", "upright": "Heartbreak, Sorrow, Grief", "reversed": "Recovery, Forgiveness, Healing"},
        {"name": "4 of Swords", "upright": "Rest, Recuperation, Meditation", "reversed": "Burnout, Exhaustion, Stagnation"},
        {"name": "5 of Swords", "upright": "Conflict, Defeat, Arguments", "reversed": "Reconciliation, Resolution, Revenge"},
        {"name": "6 of Swords", "upright": "Transition, Journey, Healing", "reversed": "Stuck, Resistance, Baggage"},
        {"name": "7 of Swords", "upright": "Deception, Strategy, Stealth", "reversed": "Confession, Exposure, Guilt"},
        {"name": "8 of Swords", "upright": "Restriction, Imprisonment, Limitation", "reversed": "Freedom, Release, Empowerment"},
        {"name": "9 of Swords", "upright": "Anxiety, Worry, Fear", "reversed": "Hope, Healing, Recovery"},
        {"name": "10 of Swords", "upright": "Endings, Loss, Crisis", "reversed": "Recovery, Regeneration, Survival"},
        {"name": "Page of Swords", "upright": "Curiosity, Communication, Vigilance", "reversed": "Deception, Gossip, Dishonesty"},
        {"name": "Knight of Swords", "upright": "Action, Ambition, Speed", "reversed": "Impulsiveness, Recklessness, Burnout"},
        {"name": "Queen of Swords", "upright": "Honesty, Independence, Directness", "reversed": "Coldness, Bitterness, Cruelty"},
        {"name": "King of Swords", "upright": "Authority, Truth, Logic", "reversed": "Tyranny, Manipulation, Cruelty"},

        # CUPS
        {"name": "Ace of Cups", "upright": "Love, Emotion, Creativity", "reversed": "Emptiness, Blockage, Loss"},
        {"name": "2 of Cups", "upright": "Partnership, Connection, Attraction", "reversed": "Separation, Discord, Imbalance"},
        {"name": "3 of Cups", "upright": "Celebration, Friendship, Community", "reversed": "Excess, Isolation, Exclusion"},
        {"name": "4 of Cups", "upright": "Apathy, Contemplation, Reevaluation", "reversed": "Withdrawal, Retreat, Indulgence"},
        {"name": "5 of Cups", "upright": "Loss, Grief, Disappointment", "reversed": "Acceptance, Healing, Forgiveness"},
        {"name": "6 of Cups", "upright": "Nostalgia, Memories, Innocence", "reversed": "Stuck, Forward, Independence"},
        {"name": "7 of Cups", "upright": "Choices, Fantasy, Illusion", "reversed": "Clarity, Focus, Realism"},
        {"name": "8 of Cups", "upright": "Withdrawal, Detachment, Departure", "reversed": "Avoidance, Fear, Stagnation"},
        {"name": "9 of Cups", "upright": "Satisfaction, Contentment, Gratitude", "reversed": "Materialism, Discontent, Greed"},
        {"name": "10 of Cups", "upright": "Harmony, Happiness, Family", "reversed": "Disconnection, Discord, Breakdown"},
        {"name": "Page of Cups", "upright": "Creativity, Intuition, Sensitivity", "reversed": "Immaturity, Insecurity, Blockage"},
        {"name": "Knight of Cups", "upright": "Romance, Charm, Imagination", "reversed": "Moodiness, Jealousy, Fantasy"},
        {"name": "Queen of Cups", "upright": "Compassion, Calm, Intuition", "reversed": "Insecurity, Dependency, Depletion"},
        {"name": "King of Cups", "upright": "Balance, Control, Empathy", "reversed": "Volatility, Manipulation, Moodiness"}
    ]

    default tarot_state = "select"
    default reading_type = ""
    default drawn_cards = []
    default position = ""

    if tarot_state == "select":
        frame: 
            xsize 950 ysize 200
            xalign 0.5 yalign 0.5

            text _("What kind of reading would you like?"):
                xalign 0.5 yalign 0.2 text_align 0.5

            textbutton _("Single Card"):
                xalign 0.2 yalign 0.8 text_align 0.5
                action [
                    SetScreenVariable("reading_type", "single"),
                    SetScreenVariable("tarot_state", "draw")
                ]
            textbutton _("Past/Present/Future"):
                xalign 0.8 yalign 0.8 text_align 0.5
                action [
                    SetScreenVariable("reading_type", "ppf"),
                    SetScreenVariable("tarot_state", "draw")
                ]

    elif tarot_state == "draw":

        if reading_type == "single":
            frame:
                xsize 950 ysize 500
                xalign 0.5 yalign 0.5

                vbox:
                    xalign 0.5 yalign 0.2
                    xsize 0.8 ysize 0.8

                    text _("Awawa."):
                        slow_cps preferences.text_cps
                        xalign 0.5 text_align 0.5
                        at transform:
                            alpha 0
                            linear 0.5 alpha 0
                            linear 0 alpha 1.0

                    text _("Think really hard about the situation."):
                        xalign 0.5 text_align 0.5
                        at transform:
                            alpha 0
                            linear 2.0 alpha 0
                            linear 0 alpha 1.0
                        
                    text _("Your card is..."):
                        xalign 0.5 text_align 0.5

                        at transform:
                            alpha 0
                            linear 5.0 alpha 0
                            linear 0 alpha 1.0

                $ this_card = renpy.random.choice(tarot_deck)
                $ drawn_cards = this_card
                $ tarot_deck.remove(this_card)
                $ position = renpy.random.choice(["upright", "reversed"])
                
                vbox:
                    xalign 0.5 yalign 0.8 

                    at transform:
                        alpha 0
                        linear 7.0 alpha 0
                        linear 0 alpha 1.0

                    text drawn_cards["name"]:
                        xalign 0.5 text_align 0.5
                        size 64
                    text "("+str.capitalize(position)+")":
                        xalign 0.5 text_align 0.5
                        color gui.idle_color
                        size 36
                    text drawn_cards[position]:
                        xalign 0.5 text_align 0.5
                        color gui.idle_color
                        size 36
                        italic True
                                                             
        elif reading_type == "ppf":

            key "dismiss" action [
                Return(),
                With(dissolve)
            ]
            frame:
                xsize 0.8 ysize 500
                xalign 0.5 yalign 0.5

                vbox:
                    xalign 0.5 yalign 0.2
                    xsize 0.9 ysize 0.9

                    text _("Awawa."):
                        xalign 0.5 text_align 0.5
                        at transform:
                            alpha 0
                            linear 0.5 alpha 0
                            linear 0 alpha 1.0

                    text _("Think really hard about the situation."):
                        xalign 0.5 text_align 0.5
                        at transform:
                            alpha 0
                            linear 2.0 alpha 0
                            linear 0 alpha 1.0
                        
                    text _("Your cards are..."):
                        xalign 0.5 text_align 0.5

                        at transform:
                            alpha 0
                            linear 5.0 alpha 0
                            linear 0 alpha 1.0

                grid 3 1:
                    xalign 0.5 yalign 0.8
                    xsize 1.0
                    spacing 24
                    
                    for x in range(3):
                        $ this_card = renpy.random.choice(tarot_deck)
                        $ tarot_deck.remove(this_card)
                        $ drawn_cards += [this_card]

                    $ readings = ["The Past", "The Present", "The Future"]

                    for idx, c in enumerate(drawn_cards):
                        $ position = renpy.random.choice(["upright", "reversed"])

                        vbox:
                            xalign 0.5 yalign 0.8 

                            at transform:
                                alpha 0
                                linear 7.0 alpha 0
                                linear 0 alpha 1.0

                            text readings[idx]:
                                xalign 0.5 text_align 0.5
                            text drawn_cards[idx]["name"]:
                                xalign 0.5 text_align 0.5
                                size 64
                            text "("+str.capitalize(position)+")":
                                xalign 0.5 text_align 0.5
                                color gui.idle_color
                                size 36
                            text drawn_cards[idx][position]:
                                xalign 0.5 text_align 0.5
                                color gui.idle_color
                                size 36
                                italic True
        key "dismiss" action [
            Return(),
            With(dissolve)
        ]

####################################################################################################

init python:
    def donut_drop(drags, drop):
        if not drop:
            return

        item = drags[0].drag_name
        target = drop.drag_name

        if target=="donut_box":
            if item=="poo":
                renpy.notify("Ewwww! Don't poop in the box!")
            else:
                renpy.notify("Ooh, donut.")

screen click_drag_test():
    modal True

    default img_choices = [
        ["donut", "images/donut_1.png"],
        ["donut", "images/donut_2.png"],
        ["donut","images/donut_3.png"],
        ["poo", Transform("images/poo.png", zoom=0.4)],
    ]   

    default poo_in_box = False
    default donuts_in_box = False

    draggroup:
        xsize 1.0 ysize 1.0
        drag:
            drag_name "donut_box"
            droppable True
            draggable False

            xalign 0.5 yalign 0.9
            
            frame:    
                xsize 300 ysize 300
           

        for id, img in enumerate(img_choices):
            drag:
                drag_name img[0]
                draggable True
                droppable False
                dragged donut_drop

                xpos 300 ypos id*100+400
   
                add img[1]
        
    textbutton _("Return"):
        xpos 15 ypos 1000
        action Return()

####################################################################################################
init python: 
    config.per_frame_screens.append("rails_test")

screen rails_test():
    default points_list = [
        [255, 255], 
        [900, 200], 
        [1800, 255],
        [1400, 900],
        [200, 800]
    ]

    default marker = "gui/inline_text/ch1.png"
    default moving_img = Transform("images/poo.png", zoom=0.4)
    default current_pos = list(points_list[0]) # Starting point
    default destination = current_pos
    default next_dest_index = 0
    default speed = 5

    # Draw the points
    for i, p in enumerate(points_list):
        add marker:
            xanchor 0.5 yanchor 0.5
            xpos p[0] ypos p[1]

        text "#"+str(i+1)+"\n"+str(p):
            xanchor 0.5 yanchor 0.5
            text_align 0.5
            xpos p[0] ypos p[1]-(gui.text_size+25)
        
    # Draw moving image
    add moving_img:
        xanchor 0.5 yanchor 0.5
        xpos current_pos[0] ypos current_pos[1]

    # Debug
    text "Current Position "+str(current_pos)+"\nDestination: "+str(destination)

    textbutton _("Return"):
        xpos 15 ypos 1000
        action Return()

    python:
        if current_pos != destination:
            x_delta = destination[0] - current_pos[0]
            y_delta = destination[1] - current_pos[1]
           
            # Move X
            if abs(x_delta) <= speed:
                current_pos[0] = destination[0]
            else:
                current_pos[0] += speed if x_delta > 0 else -speed

            # Move Y
            if abs(y_delta) <= speed:
                current_pos[1] = destination[1]
            else:
                current_pos[1] += speed if y_delta > 0 else -speed            
        else:
            next_dest_index = (next_dest_index + 1) % len(points_list)
            destination = points_list[next_dest_index]
            renpy.restart_interaction()