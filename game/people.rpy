
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    global name_map
    name_map = {"cs": "cs188",
        "nova": "ItsNovaHere",
        "carguy": "CarGuy",
        "doug": "Doug McMillon",
        "cashier": "Cashier",
        "ed": "Ed",
        "wesley": "Wesley",
        "rich": "Richard",
        "michael": "Michael Rosen",
        "phil": "Phil Swift",
        "hoh_worker": "HoH SiS Workers",
        "digi": "DigiDuncan",
        "copguy": "Cop Guy",
        "arceus": "Arceus3251",
        "anno": "Annorexorcist",
        "border_guard": "Canadaian Border Guard",
        "linus": "Linus Sebastian",
        "mohs": "Mr. Mohs",
        "csgod": "CSGod",
        "luke": "Luke Lafreniere"
    }

    global bio
    bio = "wowowowowowowowowowow"

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
            for k in name_map.keys():
                if k in persistent.seen:
                    textbutton name_map[k] action ShowMenu("person", k, bio)

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
            text _("View bios about all the wacky characters you've seen!")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen person(l, bio):

    tag menu
    use people_nav

    style_prefix "codex"
    label name_map[l]

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

            text _p(bio)

        if l == "cs":
            add "images/characters/cs/neutral.png" xalign 1.0 yalign 0.0
        elif l == "hoh_worker":
            pass
        else:
            add "images/characters/"+l+".png" xalign 1.0 yalign 0.0
