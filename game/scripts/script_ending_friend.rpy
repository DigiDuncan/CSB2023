screen where_text(string):
    frame:
        background None
        xysize(1720,300)
        xalign 0.5 yalign 1.0
        yoffset -64

        text string:
            color "#FFFFFF"
            outlines [(5, "#000000", absolute(0), absolute(0))]
            size 64
            text_align 0.5
            xalign 0.5 yalign 1.0

label where_are_they_now:

    $ renpy.choice_for_skipping()
    $ _skipping = False
    window auto False
    window hide

    scene black
    pause 1.0

    camera:
        matrixcolor SepiaMatrix()

    play music the_legend noloop
    $ persistent.heard.add("the_legend")

    ################ CS ################

    show cs_room_2:
        xanchor 0.5 yanchor 1.0
        zoom 1.2
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("CS returned home to his normal life of streaming and making YTPs.\nThe cops don't mess with him since taking out the corrupt Copguy.")
    show cs happy:
        xanchor 0.5 yanchor 1.0
        xpos 0.2 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.7
    with dissolve

    $ renpy.pause(17,hard=True)

    hide screen where_text
    scene black 
    with dissolve
    $ renpy.pause(1.5,hard=True)

    ################ ARC & KITTY ################

    show kitty_room:
        xanchor 0.5 yanchor 1.0
        zoom 1.2
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("Arceus moved to the UK to be with his partner, Kitty. The two lead a peaceful life now. Kitty makes fursuits for a living while Arceus has found work with a mysterious organization.")
    show kitty:
        xanchor 0.5 yanchor 1.0
        xpos 0.35 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.85
    show arceus:
        xanchor 0.5 yanchor 1.0
        xpos 0.2 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.7
    with dissolve
    $ renpy.pause(15,hard=True)

    hide screen where_text
    scene black 
    with dissolve

    $ renpy.pause(1.0,hard=True)

    ################ PAKOO & MIKA ################

    show omaha:
        xanchor 0.5 yanchor 1.0
        zoom 1.2
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("Mika moved in with their partner Pakoo in Nebraska.\nPakoo works at Black Mesa while Mika got a job at Robert Space Industries.")
    show mika:
        xanchor 0.5 yanchor 1.0
        xpos 0.35 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.85
    show pakoo:
        xanchor 0.5 yanchor 1.0
        xpos 0.2 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.7
    with dissolve

    $ renpy.pause(16,hard=True)

    hide screen where_text
    scene black 
    with dissolve
    $ renpy.pause(0.5,hard=True)

    ################ DIGI & ARIA ################

    show nugget_cockpit_back:
        xanchor 0.5 yanchor 1.0
        zoom 0.6
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("Digi and Aria still hang out as much as they can in spite of their busy schedules. Digi has devoted their life to perfecting their cybernetic body mods while Aria continues to be an entity doing entity things.")
    show aria:
        xanchor 0.5 yanchor 1.0
        xpos 0.35 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.85
    show digi thinking flipped:
        xanchor 0.5 yanchor 1.0
        xpos 0.2 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.7
    with dissolve

    $ renpy.pause(16,hard=True)

    hide screen where_text
    scene black 
    with dissolve
    $ renpy.pause(1.0,hard=True)

    ################ NOVA & BLANK ################

    show stage_2:
        xanchor 0.5 yanchor 1.0
        zoom 1.2
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("Nova and Blanknam3d, both musicians, but with very different tastes, have ended up in semi-friendly competition to see who can attract more fans. Nova performs under the stage name xtkakeru.")
    show blank flipped:
        xanchor 0.5 yanchor 1.0
        xpos 0.0 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.5
    show nova:
        xanchor 0.5 yanchor 1.0
        xpos 0.4 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.9
    with dissolve

    $ renpy.pause(15,hard=True)

    hide screen where_text
    scene black 
    with dissolve
    $ renpy.pause(1.0,hard=True)

    ################ ANNO & DB ################

    show cpuaisle:
        xanchor 0.5 yanchor 1.0
        zoom 1.2
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("Annorexorcist created a CS-themed mod for a hit video game.\nDB05 continues to care for his dogs and be late for streams.")
    show anno:
        xanchor 0.5 yanchor 1.0
        xpos 0.0 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.5
    show db:
        xanchor 0.5 yanchor 1.0
        xpos 0.4 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.9
    with dissolve

    $ renpy.pause(6.5,hard=True)

    hide screen where_text
    scene black 
    with dissolve
    $ renpy.pause(1.0,hard=True)

    ################ MIDGE ################

    show front_desk_2:
        xanchor 0.5 yanchor 1.0
        zoom 1.2
        blur 10
        xpos 0.4 ypos 1.0
        linear 20 xpos 0.6
    show screen where_text("Midgalicis returned home to the Phillipines, where she unexpectedly landed an illustration job with Amazon.")
    show midge:
        xanchor 0.5 yanchor 1.0
        xpos 0.2 ypos 1.0
        zoom 1.1
        linear 20 xpos 0.7
    with dissolve

    $ renpy.pause(7,hard=True)

    hide screen where_text
    scene black 
    with dissolve
    $ renpy.pause(3.0,hard=True)
    camera reset # resetting it here for a reason
    camera:
        matrixcolor IdentityMatrix()

    ################ TATE ################
  
    stop music

    show screen where_text("As for Tate...") with dissolve
    $ renpy.pause(3,hard=True)

    show final_destination:
        matrixcolor SepiaMatrix()
    show tate sil_black at center:
        matrixcolor SepiaMatrix()
    hide screen where_text
    with dissolve
    $ renpy.pause(2,hard=True)

    show screen where_text("They mentioned something about starting over... {color=#00000000}{outlinecolor=#00000000}somewhere else.{/color}{/outlinecolor}") with dissolve
    $ renpy.pause(3,hard=True)
    show screen where_text("They mentioned something about starting over... somewhere else.") with dissolve
    $ renpy.pause(3,hard=True)
    hide screen where_text with Dissolve(2.0)
    $ renpy.pause(2,hard=True)

    # summon sigil
    play sound sfx_snd_spellcast
    show tate_sigil at truecenter behind tate:
        matrixcolor SepiaMatrix()

        zoom 0.75
        xzoom 0
        ypos 1.0
        blur 5

        block:
            parallel:
                linear 0.25 xzoom 1.0
            parallel:
                linear 0.25 ypos 0.6

    $ renpy.pause(4,hard=True)
    
    show tate sil_black flipped:
        matrixcolor SepiaMatrix()

        # let's make them take several steps.
        block:
            parallel:
                linear 0.5 zoom 0.9
            parallel:
                linear 0.5 ypos 1.05

        block:
            parallel:
                linear 0.5 zoom 0.85
            parallel:
                linear 0.5 ypos 1.0
        #2 
        block:
            parallel:
                linear 0.5 zoom 0.8
            parallel:
                linear 0.5 ypos 1.05

        block:
            parallel:
                linear 0.5 zoom 0.75
            parallel:
                linear 0.5 ypos 1.0

        #3 
        block:
            parallel:
                linear 0.5 zoom 0.7
            parallel:
                linear 0.5 ypos 1.05    

        block:
            parallel:
                linear 0.5 zoom 0.65
            parallel:
                linear 0.5 ypos 1.0

        #4
        block:
            parallel:
                linear 0.5 zoom 0.65
            parallel:
                linear 0.5 ypos 1.05

        block:
            parallel:
                linear 0.5 zoom 0.6
            parallel:
                linear 0.5 ypos 1.0

    play sound sfx_snow_walk
    $ renpy.pause(5.0,hard=True)

    # as tate disappears, show CMY for one frame.
    show tate sil_black flipped as yellow: #Y
        alpha 0
        matrixcolor TintMatrix("#FFFF00") * BrightnessMatrix(1.0)
        xpos 0.5 ypos 1.0
        xanchor 0.5 yanchor 1.0
        blur 5
        zoom 0.6 

        linear 0.1 alpha 1.0

    show tate sil_black flipped as cyan behind yellow: #C
        matrixcolor TintMatrix("#00FFFF") * BrightnessMatrix(1.0)
        xpos 0 ypos 1.0
        xanchor 0.5 yanchor 1.0
        blur 5
        zoom 0.6 
        alpha 0

        parallel:
            linear 0.1 alpha 1.0
        parallel:
            linear 0.1 xpos 0.5

    show tate sil_black flipped as magenta behind yellow: #M
        matrixcolor TintMatrix("#FF00FF") * BrightnessMatrix(1.0)
        xpos 1.0 ypos 1.0
        xanchor 0.5 yanchor 1.0
        blur 5
        zoom 0.6 
        alpha 0

        parallel:
            linear 0.1 alpha 1.0
        parallel:
            linear 0.1 xpos 0.5
    
    $ renpy.pause(0,hard=True) # yes this is necessary

    # combine the colors
    hide cyan
    hide magenta
    hide tate sil_black
    with Dissolve(0.1)

    # finally jump to a new timeline...
    play sound sfx_snd_sparkles
    show yellow:
        matrixcolor TintMatrix("#FFFFFF") * BrightnessMatrix(1.0)
        parallel:
            linear 0.1 xzoom 0
        parallel:
            linear 0.1 ypos 0.5

    show tate_sigil:
        parallel:
            linear 0.1 xzoom 0
        parallel:
            linear 0.1 ypos 0.5

    $ renpy.pause(4, hard=True)

    scene black with Dissolve(2.0)
    $ renpy.pause(2,hard=True)

    ################ ENDING ################

    centered "{size=+128}THE END{fast}"

    call screen credits_roll() with determination
    $ renpy.end_replay()
    return
