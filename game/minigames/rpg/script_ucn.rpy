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

screen ucn_bg_choice(items):
    viewport:
        xysize(1920, 720)
        yanchor -0.25
        style_prefix "choice"
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        grid 14 int(len(items) / 14) + 1:
            for i in items:
                $ sc = im.Scale(i.caption, 128, 72)
                imagebutton:
                    idle sc
                    hover sc
                    insensitive sc
                    xysize (128, 72)
                    anchor(-0.25, -0.25)
                    action i.action

screen ucn_bgm_choice(items):
    viewport:
        xysize(1920, 540)
        yanchor -0.25
        style_prefix "choice"
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        vbox:
            for i in items:
                textbutton i.caption.removeprefix("audio/").removesuffix(".ogg").removeprefix("/"):
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

    $ allies = (("NONE", "NONE"), *((character.name, character.assigned_name) for character in RPG.Characters.allies))
    $ enemies = (("NONE", "NONE"), *((character.name, character.assigned_name) for character in RPG.Characters.enemies))

    $ narrator("Choose a party member! (1/4)", interact = False)
    $ RPG.set_var_character("party_1", renpy.display_menu(allies, screen="ucn_choice"))
    $ narrator("Choose a party member! (2/4)", interact = False)
    $ RPG.set_var_character("party_2", renpy.display_menu(allies, screen="ucn_choice"))
    $ narrator("Choose a party member! (3/4)", interact = False)
    $ RPG.set_var_character("party_3", renpy.display_menu(allies, screen="ucn_choice"))
    $ narrator("Choose a party member! (4/4)", interact = False)
    $ RPG.set_var_character("party_4", renpy.display_menu(allies, screen="ucn_choice"))

    $ narrator("Choose an enemy! (1/3)", interact = False)
    $ RPG.set_var_character("enemy_1", renpy.display_menu(enemies, screen="ucn_choice"))
    $ narrator("Choose an enemy! (2/3)", interact = False)
    $ RPG.set_var_character("enemy_2", renpy.display_menu(enemies, screen="ucn_choice"))
    $ narrator("Choose an enemy! (3/3)", interact = False)
    $ RPG.set_var_character("enemy_3", renpy.display_menu(enemies, screen="ucn_choice"))

    $ narrator("Choose a party scale!", interact = False)
    $ RPG.ucn_scale = renpy.display_menu([(str(a), a) for a in scales], screen="ucn_choice")

    $ RPG.ucn_bg = renpy.display_menu([(i.lower(), i) for i in bg_list], screen="ucn_bg_choice")
    $ RPG.ucn_music = renpy.display_menu([(v["title"], k) for k, v in music_map.items()], screen="ucn_bgm_choice")

    rpg:
        on_win "after_ucn"
        on_lose "after_ucn"
        intro "Begin!"
        ucn
        allies:
            $party_1
            $party_2
            $party_3
            $party_4
        enemies:
            $enemy_1
            $enemy_2
            $enemy_3

label after_ucn:
    $ cont = renpy.display_menu([("New Game", True), ("Return", False)], screen = "ucn_choice")
    if cont:
        jump rpg_ucn
    else:
        $ MainMenu()
