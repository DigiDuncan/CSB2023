
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen people_nav():
    add "gui/overlay/game_menu.png"

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
            if persistent.cs:
                textbutton "cs188" action ShowMenu("cs")
            if persistent.nova:
                textbutton "ItsNovaHere" action ShowMenu("nova")
            if persistent.carguy:
                textbutton "Car Guy" action ShowMenu("carguy")
            if persistent.doug:
                textbutton "Doug McMillon" action ShowMenu("doug")
            if persistent.cashier:
                textbutton "Cashier" action ShowMenu("cashier")
            if persistent.ed:
                textbutton "Ed" action ShowMenu("ed")
            if persistent.wesley:
                textbutton "Wesley" action ShowMenu("wesley")
            if persistent.rich:
                textbutton "Richard" action ShowMenu("richard")
            if persistent.michael:
                textbutton "Michael Rosen" action ShowMenu("michael")
            if persistent.phil:
                textbutton "Phil Swift" action ShowMenu("phil")
            if persistent.hoh_worker:
                textbutton "HoH SiS Workers" action ShowMenu("hoh_worker")
            if persistent.digi:
                textbutton "DigiDuncan" action ShowMenu("digi")
            if persistent.copguy:
                textbutton "Cop Guy" action ShowMenu("copguy")
            if persistent.arceus:
                textbutton "Arceus3251" action ShowMenu("arceus")
            if persistent.anno:
                textbutton "Annorexorcist" action ShowMenu("anno")
            if persistent.border_guard:
                textbutton "Canadaian Border Guard" action ShowMenu("border_guard")
            if persistent.linus:
                textbutton "Linus Sebastian" action ShowMenu("linus")
            if persistent.mohs:
                textbutton "Mr. Mohs" action ShowMenu("mohs")
            if persistent.csgod:
                textbutton "CS God" action ShowMenu("csgod")
            if persistent.luke:
                textbutton "Luke" action ShowMenu("luke")

    textbutton "Return to categories" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Return" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen people_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use people_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category you can read about all the wonderful characters in this game! (And also Bob)")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen cs():

    tag menu
    use people_nav

    style_prefix "codex"
    label "cs188"

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

screen nova():

    tag menu
    use people_nav

    style_prefix "codex"
    label "ItsNovaHere"

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

screen carguy():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Car Guy"

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

screen doug():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Doug McMillon"

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

screen cashier():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Cashier"

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

screen ed():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Ed"

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

screen wesley():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Welsey"

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

screen rich():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Richard"

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

screen michael():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Michael Rosen"

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

screen phil():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Phil Swift"

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

screen hoh_worker():

    tag menu
    use people_nav

    style_prefix "codex"
    label "HoH SiS Workers"

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

screen digi():

    tag menu
    use people_nav

    style_prefix "codex"
    label "DigiDuncan"

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

screen copguy():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Cop Guy"

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

screen arceus():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Arceus3251"

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

screen anno():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Annorexorcist"

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

screen border_guard():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Canadian Border Guard"

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

screen linus():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Linus Sebastian"

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

screen mohs():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Mr. Mohs"

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

screen csgod():

    tag menu
    use people_nav

    style_prefix "codex"
    label "CS God"

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

screen luke():

    tag menu
    use people_nav

    style_prefix "codex"
    label "Luke"

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
            