screen ucn_choice(items):
    viewport:
        xysize(1920, 540)
        yanchor -0.25
        style_prefix "choice"
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        vbox:
            for i in items:
                textbutton i.caption:
                    anchor(-0.25, -0.25)
                    action i.action

# screen ucn_mainmenu:
    # tag menu
    # timer 0.5 action MainMenu(confirm = False)

label rpg_ucn:
    $ renpy.hide_screen("menu")
    scene game_menu
    centered "Loading...{w=1.0}{nw}"  # This isn't required.
    $ scales = [1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0]

    $ allies = list(zip(Fighters.allies, Fighters.ally_names))
    $ enemies = list(zip(Fighters.enemies, Fighters.enemy_names))

    $ narrator("Choose a party member! (1/4)", interact = False)
    $ party_1 = renpy.display_menu([("NONE", "NONE")] + [(a.name, n) for a, n in allies], screen="ucn_choice")
    $ narrator("Choose a party member! (2/4)", interact = False)
    $ party_2 = renpy.display_menu([("NONE", "NONE")] + [(a.name, n) for a, n in allies], screen="ucn_choice")
    $ narrator("Choose a party member! (3/4)", interact = False)
    $ party_3 = renpy.display_menu([("NONE", "NONE")] + [(a.name, n) for a, n in allies], screen="ucn_choice")
    $ narrator("Choose a party member! (4/4)", interact = False)
    $ party_4 = renpy.display_menu([("NONE", "NONE")] + [(a.name, n) for a, n in allies], screen="ucn_choice")

    $ narrator("Choose an enemy! (1/3)", interact = False)
    $ enemy_1 = renpy.display_menu([("NONE", "NONE")] + [(e.name, n) for e, n in enemies], screen="ucn_choice")
    $ narrator("Choose an enemy! (2/3)", interact = False)
    $ enemy_2 = renpy.display_menu([("NONE", "NONE")] + [(e.name, n) for e, n in enemies], screen="ucn_choice")
    $ narrator("Choose an enemy! (3/3)", interact = False)
    $ enemy_3 = renpy.display_menu([("NONE", "NONE")] + [(e.name, n) for e, n in enemies], screen="ucn_choice")

    $ narrator("Choose a party scale!", interact = False)
    $ ucn_scale = renpy.display_menu([(str(a), a) for a in scales], screen="ucn_choice")

    rpg:
        bg "ucn"
        music "ucn"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            $enemy_1
            $enemy_2
            $enemy_3
        scale "ucn"
        on_win "after_ucn"
        on_lose "after_ucn"

label after_ucn:
    $ cont = renpy.display_menu([("New Game", True), ("Return", False)], screen = "ucn_choice")
    if cont:
        jump rpg_ucn
    else:
        $ MainMenu()
