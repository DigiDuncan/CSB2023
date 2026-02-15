########## CE Point & Click Setup ##########

screen hatch_button():
    modal True

    ##### poster button
    imagebutton:
        idle "minigames/christmaspointclick/poster.png"
        hover "selectable:minigames/christmaspointclick/poster.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(720, 323, 0)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.poster")

    ##### rug button
    imagebutton:
        idle "minigames/christmaspointclick/rug.png"
        hover "selectable:minigames/christmaspointclick/rug.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(961, 56, 0)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.rug")

    ##### cs button
    imagebutton:
        idle "images/characters/cs/christmas/disappointed.png"
        hover "selectable:images/characters/cs/christmas/disappointed.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at mid_left
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.cs")

    ##### flashlight button
    imagebutton:
        idle "minigames/christmaspointclick/flashlight.png"
        hover "selectable:minigames/christmaspointclick/flashlight.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(0.3, 0.7, 0.5)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.flashlight")

    ##### mean button
    imagebutton:
        idle "images/characters/mean/meanhumanannoyedfestive.png"
        hover "selectable:images/characters/mean/meanhumanannoyedfestive.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at mid_right
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.mean")

    ##### hatch button (correct one)
    imagebutton:
        idle "minigames/christmaspointclick/hatch.png"
        hover "selectable:minigames/christmaspointclick/hatch.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        xpos 0.3
        ypos -0.2
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_after_hatch")

    add Flashlight()

########## End CE Point & Click Setup ##########

label ce_point_click:
    show screen flashlight_demo
    $ mouse_visible = False
    scene cs_attic
    show hatch at manual_pos(0.3, -0.2)
    show cs disappointed christmas at mid_left
    show flashlight_held at manual_pos(0.3, 0.7, 0.5):
        zoom 0.5
    show mean human annoyed festive at mid_right
    with dissolve
    pause 0.5
    stop music fadeout 3.0
    music end
    mean "You good, CS?"
    cs "Yeah, I'm just a bit tired."
    cs "Anyway, there should be a hatch or something up here..."
    jump .click_menu

    ##### introducing sub-labels here!

    ### default menu
    label .click_menu:
        show screen flashlight_demo
        $ mouse_visible = False
        scene cs_attic
        show hatch at manual_pos(0.3, -0.2)
        show cs disappointed christmas at mid_left
        show flashlight_held at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5
        show mean human annoyed festive at mid_right

        # THIS CHECK IS STUPID AND BAD
        if ("cs" in persistent.point_and_clicked and
            "flashlight" in persistent.point_and_clicked and
            "mean" in persistent.point_and_clicked and
            "poster" in persistent.point_and_clicked and
            "rug" in persistent.point_and_clicked and
            "hatch" in persistent.point_and_clicked):
            $ achievement_manager.unlock("point_click")

        mean "Shine your light up."
        hide screen flashlight_demo
        show screen hatch_button
        window hide
        pause

    ### clicked on cs
    label .cs:
        $ persistent.point_and_clicked.add("cs")
        show screen flashlight_demo
        $ mouse_visible = False
        scene cs_attic
        show hatch at manual_pos(0.3, -0.2)
        show mean human annoyed festive at mid_right
        show cs disappointed christmas at mid_left
        show flashlight_held at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5

        show cs happy christmas at mid_left
        cs "Hey, that tickles!"
        show mean human shocked festive
        mean "Huh?" with vpunch
        show cs scared christmas
        cs "I mean, uh--"

        jump .click_menu

    ### clicked on the flashlight
    label .flashlight:
        $ persistent.point_and_clicked.add("flashlight")
        show screen flashlight_demo
        $ mouse_visible = False
        scene cs_attic
        show hatch at manual_pos(0.3, -0.2)
        show mean human annoyed festive at mid_right
        show cs disappointed christmas at mid_left
        show flashlight_held at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5

        cs "Like this?"
        show mean human shocked festive
        mean "That's... your flashlight."
        mean "How the {i}fuck{/i} did you point your flashlight... {i}at{/i} your flashlight?"

        jump .click_menu

    ### clicked on mean
    label .mean:
        $ persistent.point_and_clicked.add("mean")
        show screen flashlight_demo
        $ mouse_visible = False
        scene cs_attic
        show hatch at manual_pos(0.3, -0.2)
        show mean human annoyed festive at mid_right
        show cs disappointed christmas at mid_left
        show flashlight_held at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5

        show mean human angry festive
        mean "That's {nw}"
        extend "{i}me,{/i} {nw}" with vpunch
        extend "you dumb fuck!"
        mean "Try again!"

        jump .click_menu

    ### clicked on the poster
    label .poster:
        $ persistent.point_and_clicked.add("poster")
        show screen flashlight_demo
        $ mouse_visible = False
        scene cs_attic
        show hatch at manual_pos(0.3, -0.2)
        show mean human annoyed festive at mid_right
        show cs disappointed christmas at mid_left
        show flashlight_held at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5

        show cs happy christmas
        cs "Only {i}you{/i} can prevent forest fires!"
        show mean human festive
        mean "Oh, yeah. I think Tate said something about how the only comic book they ever owned as a kid was of Smokey the Bear."
        show cs worried christmas
        mean "Apparently, it made them cry when all the animals died in the fire."
        mean "Fuckin' hippie."
        show mean human annoyed festive
        show cs disappointed christmas
        mean "Anyway, that won't help us now."

        jump .click_menu

    ### clicked on the rug
    label .rug:
        $ persistent.point_and_clicked.add("rug")
        show screen flashlight_demo
        $ mouse_visible = False
        scene cs_attic
        show hatch at manual_pos(0.3, -0.2)
        show mean human annoyed festive at mid_right
        show cs disappointed christmas at mid_left
        show flashlight_held at manual_pos(0.3, 0.7, 0.5):
            zoom 0.5

        show cs christmas
        cs "Do you think that rug will help us?"
        show mean angry human festive
        mean "{i}How,{/i} exactly, do you think a {i}rug{/i} will help us get to the {i}roof?" with vpunch
        show cs disappointed christmas
        cs "I dunno, man! I'm just throwing things at the wall to see what sticks!"
        show cs surprised christmas
        cs "Er, well, I suppose it's {i}already{/i} on the wall, isn't i-- {nw}"
        mean "Well, that won't help us now!" with vpunch

        jump .click_menu
