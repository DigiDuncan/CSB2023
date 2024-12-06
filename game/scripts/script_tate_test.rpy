### EXPERIMENTAL REVERSI RULES ###

image reversi_rules_test:
    xsize 1500
    ysize 700
    xanchor 0.5
    yanchor 0.5
    contains:
        Frame("gui/frame.png")
    contains:
        Text("{size=+12}Reversi!", xalign=0.5, yalign=0.0125)
    contains:
        Text("For the first four moves, the players must play to one of the four squares in the middle of the board and no pieces are captured or reversed.\nEach piece played must be laid adjacent to an opponent's piece so that the opponent's piece or a row of opponent's pieces is flanked by the new piece and another piece of the player's color. All of the opponent's pieces between these two pieces are 'captured' and turned over to match the player's color.\nIt can happen that a piece is played so that pieces or rows of pieces in more than one direction are trapped between the new piece played and other pieces of the same colour. In this case, all the pieces in all viable directions are turned over.\nThe game is over when neither player has a legal move (i.e. a move that captures at least one opposing piece) or when the board is full.", xalign=0.5, yalign=0.5)
    contains:
        Text("{size=-12}{a=https://www.mastersofgames.com/rules/reversi-othello-rules.htm}https://www.mastersofgames.com/rules/reversi-othello-rules.htm", xalign=0.975, yalign=0.975)

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

image tate_comp flipped = LayeredImageProxy("tate_comp", Transform(xzoom = -1))

image tate_comp dusk flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = duskmatrix, xzoom = -1))
image tate_comp dark flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = darkmatrix, xzoom = -1))
image tate_comp sil_white flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_white_matrix, xzoom = -1))
image tate_comp sil_black flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = sil_black_matrix, xzoom = -1))
image tate_comp sepia flipped = LayeredImageProxy("tate_comp", Transform(matrixcolor = SepiaMatrix(), xzoom = -1))

# this section is just for fun mostly. a randomizer!
init python:
    def awawa():
        outfits = renpy.random.choice(["casual", "festive"])
        blushing = renpy.random.choice(["-blush", "blush"])
        faces = renpy.random.choice(["happy", "sad", "cry", "sheepish", "shock", "serious", "smug", "stare", "furious"])
        tearful = renpy.random.choice(["-tears", "tears"])
        gloomy = renpy.random.choice(["-gloom", "gloom"])
        shaders = renpy.random.choice(["", "dusk", "dark", "sil_white", "sil_black", "sepia"])
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
        show tate
        tate "Which test would you like?"
        menu:
            tate "Which test would you like?{fast}"

            ########## SPRITE TEST ##########

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
                show tate_comp -sepia flipped
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
                tate "Ew, {w=0.25}I hate the randomizer."

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
                        renpy.say(tate, "Wow, {w=0.25}that sucked. {w=0.5}But, {w=0.25}did it work?")
                    except:
                        renpy.show("tate", what="tate sheepish")
                        renpy.say(tate, "Something went wrong, {w=0.25}sorry.")

                jump .awawa_menu

            ########## AWAWA MODE ##########

            "Awawa Mode":
                tate "Let's try out Awawa Mode."
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
                    this_cheev = ""
                    this_cheev = renpy.input("Enter the {i}exact{/i} ID of the achievement you want to test.", this_cheev)

                    try:
                        chievos = (a for a in achievement_manager.achievements.values() if a.id == this_cheev)
                        renpy.show_screen("popup", next(chievos))
                        renpy.say(tate, "Did it work?")
                    except:
                        renpy.say(tate, substitutions("Couldn't pull achievement. Double-check the name and try again."))
                                
                jump .awawa_menu

            ########## Credits Roll ##########
            
            "Credits Roll":
                tate "Here we go!"
                
                call screen credits_roll(duration=60)
                #call screen credits_roll(route="CSBIII DX: Holiday Special", bgm="hohsis_theme.ogg", scroll_start = 12000, duration=30)

                tate "Did we do it?"
                jump .awawa_menu

            "Reversi Rules Image":
                tate "Let's check it out!"
                show reversi_rules_test at truecenter
                pause
                hide reversi_rules_test
                tate "Did it work?"
                jump .awawa_menu
            
            ########## Cancel ##########

            "None, I'm Done":
                tate "Cool. See ya later!"
