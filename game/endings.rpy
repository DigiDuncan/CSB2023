
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen endings_nav():
    add Color('#5F777F', alpha=0.5)

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            textbutton "Zack Moss" action ShowMenu("zack")
            textbutton "Nelson Shea" action ShowMenu("nelson")

            ##The following button will require a condition to be true in order to appear.
            if persistent.bob:
                textbutton "Bob" action ShowMenu("bob")

            textbutton "Lew Ciszek" action NullAction()
            textbutton "Aidan Evans" action NullAction()
            textbutton "Wincenty Borkowski" action NullAction()
            textbutton "Sascha Windisch" action NullAction()
            textbutton "Kelemen Bence" action NullAction()
            textbutton "Biró Erik" action NullAction()

    textbutton "Return to categories" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen endings_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use endings_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category you can read about all the wonderful characters in this game! (And also Bob)")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen zack():

    tag menu
    use endings_nav

    style_prefix "codex"
    label "Zack Moss"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 200
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True


        vbox:
            #You write the actual entry here. I suggest you split your text into smaller text _p sections, otherwise the text might overlap with
            #the scrollbars. If you're sure that your text fits the screen and scrolling is not needed then comment out everything starting from "scrollbars vertical" to
            #"pagekeys True" as seen in the next entry. If you do this, splitting the text is not needed.

            text _p("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non massa iaculis, mattis urna at,
            eleifend augue. Vivamus non finibus velit. Suspendisse sit amet luctus turpis. Nullam felis orci, maximus luctus aliquam eget,
            cursus nec lectus.Donec sollicitudin auctor urna, non rutrum sem aliquet et. Duis dignissim molestie luctus.
            {p}Morbi a mi metus.
            Fusce mollis nisl in cursus blandit. Proin tempor ex sit amet porta tempus. Morbi quis ante vitae odio ultricies posuere ut non lorem.
            Suspendisse diam ipsum, elementum vel scelerisque ut, auctor tincidunt nibh. Nullam placerat ante at tellus vehicula sollicitudin.
            Aliquam lorem nunc, tempus quis faucibus et, tincidunt vitae tellus. Nulla aliquam posuere sem, eget aliquet tortor venenatis a.
            Suspendisse sit amet lobortis nisi, ac rutrum magna.
            {p} """)

            text _p("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non massa iaculis, mattis urna at,
            eleifend augue. Vivamus non finibus velit. Suspendisse sit amet luctus turpis. Nullam felis orci, maximus luctus aliquam eget,
            cursus nec lectus.Donec sollicitudin auctor urna, non rutrum sem aliquet et. Duis dignissim molestie luctus. Morbi a mi metus.
            Fusce mollis nisl in cursus blandit.
            Aliquam lorem nunc, tempus quis faucibus et, tincidunt vitae tellus. Nulla aliquam posuere sem, eget aliquet tortor venenatis a.
            Suspendisse sit amet lobortis nisi, ac rutrum magna.{p} """)

            text _p("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non massa iaculis, mattis urna at,
            eleifend augue. Vivamus non finibus velit.
            {p}Suspendisse sit amet luctus turpis. Nullam felis orci, maximus luctus aliquam eget,
            cursus nec lectus.Donec sollicitudin auctor urna, non rutrum sem aliquet et. Duis dignissim molestie luctus.""")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

screen nelson():

    tag menu
    use endings_nav

    style_prefix "codex"
    label "Nelson Shea"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 200
        side_yfill True
        #scrollbars "vertical"
        #mousewheel True
        #draggable True
        #pagekeys True

        vbox:
            text _p("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non massa iaculis, mattis urna at,
            eleifend augue. Vivamus non finibus velit. Suspendisse sit amet luctus turpis.{p}Nullam felis orci, maximus luctus aliquam eget,
            cursus nec lectus.Donec sollicitudin auctor urna, non rutrum sem aliquet et. Duis dignissim molestie luctus.""")

            text _p("""Aliquam nec neque risus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam tempor, nisl vitae fermentum
            tempus, metus nibh bibendum augue, et fermentum turpis massa eget ligula. Donec feugiat neque sit amet molestie ultrices. Vestibulum
            lacinia mi eros, in maximus neque sagittis vitae. Cras vestibulum cursus nulla eu rhoncus. Sed hendrerit faucibus dignissim. Vivamus
            sed mattis dui. Nunc eu finibus sem. Morbi malesuada lectus nec arcu auctor fermentum. """)

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen bob():

    tag menu
    use collectibles_nav

    style_prefix "codex"
    label "Bob the bobman"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 200
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        vbox:
            text _p("""
                The lorekeeper just told me about Bob
                """)

            #The following text will only appear if a certain condition is True.
            if persistent.boblooks:
                text _p("""
                    Apparently he wears funny hats. Interesting.
                    """)

            #The following text will only appear if a certain condition is True.
            if persistent.bobbackground:
                text _p("""
                    He came from an unknown land....I wonder what happened.
                    But he's an accountant now! Good for him.
                    """)
