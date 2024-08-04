
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------

init python:
    def mark_read(k):
        persistent.read.add(k)

init python:
    global name_map
    name_map = {"cs": "cs188",
        #CSB1
        "craptop": "Craptop",
        "sticky": "Sticky Note",
        "nova": "ItsNovaHere",
        "carguy": "Carguy",
        "doug": "Doug McMillon",
        "cashier": "Cashier",
        "ed": "Ed",
        "wesley": "Wesley",
        "rich": "Richard",
        "michael": "Michael Rosen",
        "phil": "Phil Swift",
        "hoh_worker": "HoH SiS Workers",
        #CSB2
        "copguy": "Copguy",
        "arceus": "Arceus3251",
        "anno": "Annorexorcist",
        "border_guard": "Canadian Border Guard",
        "linus": "Linus Sebastian",
        "mohs": "Mr. Mohs",
        "csgod": "CSGod",
        #True Route
        "luke": "Luke Lafreniere",
        "taran": "Taran Van Hemert",
        "colton": "Colton Potter",
        "sheriff": "Sheriff",
        "billy": "Billy Mays",
        "cultist": "Cultist Leader",
        "cultist2": "Cultists",
        "pakoo": "Pakoo",
        "peppino": "Peppino Spaghetti",
        "streetguy": "Streetguy",
        "gnome": "Gnome",
        "aria": "Aria",
        "mario": "Mario Mario",
        "smiley": "Smiley The Hip Hop Clown",
        "jay": "The Insane Clown Posse",
        "scott": "Scott Wozniak",
        "terry": "Terry Lesler",
        "pencil": "Pencil Greeter",
        "digi": "DigiDuncan",
        "mettaton": "Mettaton",
        #South Route
        "lego": "Lego NXT Minifigure",
        "trailtrash": "Trailer Trash",
        "green": "Mr. Green",
        "jerma": "Jeremy Elbertson",
        "tsa": "TSA Agent",
        "luigi": "Luigi Mario",
        "mika": "Mikapara",
        "monika": "Monika",
        "bubble": "Bub Ble",
        "lancer": "Lancer",
        #Friend Route
        "tate": "alleZSoyez",
        "kitty": "Undead Kitty",
        "round": "Mr. Round",
        "obama": "Barack Obama",
        "blank": "Blank Named",
        "cop": "Copdude",
        "midge": "Midgalicis",
        "db": "DB05",
        #Fired Route
        "guest": "Ecstatic Fan",
        "mean": "Meancarnavor",
        "howie": "Howie Mandell",
        "ges": "Ges",
        #Country Route
        "benrey": "Benrey",
        "gordon": "Gordon Ramsay",
        "hammond": "The Top Gear Crew",
        "tom": "Tom Scott",
        "scott_pres": "Scott Oelkers",
        "miku": "Hatsune Miku",
        "sayori": "Sayori",
        "joel": "Vargskelethor Joel",
        "pomni": "Pomni",
        "moomin": "Moomin",
        "snufkin": "Snufkin",
        "alicia": "Alicia",
        "witch": "Witch",
        #Archival
        "k174": "Pakoo's Memories",
        "addy": "Addy",
        "iris": "???",
        #DX: Train
        "amtrak_conductor": "{image=gui/dx_text.png} Conductor",
        "amtrak_stewardess": "{image=gui/dx_text.png} Stewardess",
        "lupin": "{image=gui/dx_text.png} Lupin III",
        "zenigata": "{image=gui/dx_text.png} Zenigata",
        "mean_human": "{image=gui/dx_text.png} Mean (Human Form)",
        "tate_ex": "{image=gui/dx_text.png} Tate EX",
        #BTTFCS
        "cruise": "{image=gui/dx_text.png} Tom Cruise"
    }

screen people_nav():
    add Color('#323e42', alpha=0.75)
    viewport:
        xpos 25 ypos 150
        xsize 350 ysize 700
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
                    python:
                        name_label = "{image=unread.png}" + name_map[k] if k not in persistent.read else name_map[k]
                    if k == "iris":
                        textbutton name_label action Function(mark_read, k), ShowMenu("person", k), ShowMenu("fake_error", "people.rpy", 126, "`bios/iris.txt` could not be rendered as a Text object.", "Hi, I'm Iris, a cosmic being with interest in the happenings of this reality, as well as some of the people involved in this story.\nDoes that sound too formal? I don't know. Hey, Digi, writing this shit's hard. You can fill in the rest from here.", _transition = determination)
                    else:
                        textbutton name_label action Function(mark_read, k), ShowMenu("person", k)

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen people_welcome():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use people_nav

    style_prefix "codex"
    python:
        bio_count = len(name_map.keys())
        unlocked_bio_count = len(persistent.seen)
    vbox:
        xsize 850
        xalign 0.5 yalign 0.5
        xoffset 200
        text "View bios about all the wacky characters you've seen!"
        text "([unlocked_bio_count]/[bio_count] unlocked)"



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------


screen person(l):

    style_prefix "codex"
    label name_map[l]

    tag menu
    use people_nav

    viewport:

        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 305 
        yoffset 200
        side_yfill True
        mousewheel True
        draggable True
        pagekeys True
        
        hbox:
            vbox:
                xsize 800
                ysize 800
                python:
                    try:
                        fetched = renpy.file(f"bios/{l}.txt").read().decode('utf-8').replace("\r", "")
                    except:
                        fetched = "The bio didn't load correctly. Ask Digi to fix the game."

                text (fetched)
            # MCs
            if l == "cs":
                add "images/characters/cs/neutral.png" xalign 1.0 yalign 1.0 zoom 0.75 xzoom -1
            elif l == "arceus":
                add "images/characters/arc/arceus.png" xalign 1.0 yalign 1.0 zoom 0.75
            elif l == "anno":
                add "images/characters/anno/anno.png" xalign 1.0 yalign 1.0 zoom 0.75
            elif l == "tate":
                add "images/characters/tate/tatehappy.png" xalign 1.0 yalign 1.0 zoom 0.75
            elif l == "tate_ex":
                add "images/characters/tate/tate_ex.png" xalign 1.0 yalign 1.0 zoom 0.50
            elif l == "mean_human":
                add "images/characters/mean/meanhumanneutral.png" xalign 1.0 yalign 1.0 zoom 0.7
            elif l == "pakoo":
                add "images/characters/pakoo/pakoo.png" xalign 1.0 yalign 1.0
            elif l == "mean":
                add "images/characters/mean/mean.png" xalign 1.0 yalign 1.0
            # SECRET
            elif l in ["iris", "bubble", "lancer", "howie", "round"]:
                add f"secret/{l}.png" xalign 1.0 yalign 1.0 zoom 0.75
            elif l == "k174":
                add "images/characters/memory.png" xalign 1.0 yalign 1.0 zoom 0.55
            elif l == "addy":
                add "images/characters/pakoo/pakoo.png" xalign 1.0 yalign 1.0
            # WEIRD ALIGNMENTS
            elif l == "hoh_worker":
                add "images/characters/hoh_worker.png" xalign 1.0 yalign 1.0 zoom 0.50
            elif l == "sticky":
                add "images/post-it.png" xalign 1.0 yalign 1.0
            elif l == "craptop":
                add "images/characters/laptop.png" xalign 1.0 yalign 1.0
            elif l == "hammond":
                add "images/characters/topgear.png" xalign 1.0 yalign 1.0 zoom 0.55
            elif l == "jay":
                add "images/characters/posse.png" xalign 1.0 yalign 1.0 zoom 0.55
            elif l == "lupin":
                add "images/characters/lupin/lupin_stand.png" xalign 1.0 yalign 1.0 zoom 0.8
            else:
                add f"images/characters/{l}.png" xalign 1.0 yalign 1.0 zoom 0.75
