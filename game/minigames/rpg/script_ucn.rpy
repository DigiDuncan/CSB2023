label rpg_ucn:
    $ ally_names = ally_names = ["NONE", "CS","CS_NG","CS_STRONG","CS_FINAL","CS_WEAK","ARCEUS","PAKOO","MIKA","KITTY","TATE","ARIA","DIGI","NOVA","BLANK","MIDGE","DB05","ANNO"]
    $ enemy_names = ["NONE", "FANBOYA","FANBOYB","COP","COPGUYGODMODE","COPGUY1","GUARD","SML_TANK","MARINE","BIG_TANK","COPGUY2"]

    $ narrator("Choose a party member! (1/4)", interact = False)
    $ party_1 = renpy.display_menu([(a, a) for a in ally_names])
    $ narrator("Choose a party member! (2/4)", interact = False)
    $ party_2 = renpy.display_menu([(a, a) for a in ally_names])
    $ narrator("Choose a party member! (3/4)", interact = False)
    $ party_3 = renpy.display_menu([(a, a) for a in ally_names])
    $ narrator("Choose a party member! (4/4)", interact = False)
    $ party_4 = renpy.display_menu([(a, a) for a in ally_names])

    $ narrator("Choose an enemy! (1/3)", interact = False)
    $ enemy_1 = renpy.display_menu([(a, a) for a in enemy_names])
    $ narrator("Choose an enemy! (2/3)", interact = False)
    $ enemy_2 = renpy.display_menu([(a, a) for a in enemy_names])
    $ narrator("Choose an enemy! (3/3)", interact = False)
    $ enemy_3 = renpy.display_menu([(a, a) for a in enemy_names])

    rpg:
        bg "images/bg/casino1.png"
        music "audio/card_castle.mp3"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            $enemy_1
            $enemy_2
            $enemy_3
        scale 1.0
        on_win "secret"
        on_lose "secret"
