label rpg_test:
    rpg:
        bg "images/bg/casino1.png"
        music "audio/card_castle.mp3"
        fighters:
            cs
            $enemy_1
            $enemy_2
            $enemy_3
        scale 1.0
        on_win "secret"
        on_lose "secret"

label rpg_fanboy_fight_amd:
    rpg:
        bg "images/bg/linus_office_outside.png"
        music "audio/nordic_report_1.mp3"
        fighters:
            cs_weak
            fanboyb
            fanboyb
            fanboyb
        scale 1.0
        on_win "after_fanboy"
        on_lose "knocked_out"

label rpg_fanboy_fight_nvidia:
    rpg:
        bg "images/bg/linus_office_outside.png"
        fighters:
            cs_weak
            fanboya
            fanboya
            fanboya
        scale 1.0
        on_win "after_fanboy"
        on_lose "knocked_out"
        music "audio/nordic_report_2.mp3"

label rpg_cop_fight_1:
    rpg:
        bg "images/bg/dealership.png"
        music "audio/compulsion_to_obey.mp3"
        fighters:
            cs
            arceus
            pakoo
            cop
            cop
            copguygodmode
        scale 1.0
        on_win "secret"
        on_lose "so_join"

label rpg_cop_fight_2:
    rpg:
        bg "images/bg/dealership.png"
        music "audio/for_the_people.mp3"
        fighters:
            mika
            kitty
            tate
            copguy
        scale 1.0
        on_win "after_cop_fight"
        on_lose "rpg_cop_fight_2"

label rpg_cop_fight_3:
    rpg:
        bg "images/bg/cs_somewhere.png"
        music "audio/desert_dawn.mp3"
        fighters:
            aria
            cop
            cop
        scale 1.0
        on_win "cs_meetup"
        on_lose "rpg_cop_fight_3"

label rpg_cop_fight_4:
    rpg:
        bg "images/bg/dinerinside.png"
        music "audio/dinerfight.mp3"
        fighters:
            digi
            nova
            cop
            cop
        scale 1.0
        on_win "cs_meetup_2"
        on_lose "rpg_cop_fight_4"

label rpg_ng_fight:
    $ ng_fighters = ["CS_NG", "ARCEUS", "PAKOO", "MIKA", "KITTY", "TATE", "ARIA", "DIGI", "NOVA", "NONE"]
    $ chosen_ng_fighters = []
    $ narrator("Choose a party member! (1/4)", interact = False)
    $ party_1 = renpy.display_menu([(a.title() if a != "CS_NG" else "CS", a) for a in ng_fighters], screen="ucn_choice")
    $ if party_1 != "NONE": chosen_ng_fighters.append(party_1)
    $ narrator("Choose a party member! (2/4)", interact = False)
    $ party_2 = renpy.display_menu([(a.title() if a != "CS_NG" else "CS", a) for a in ng_fighters if a not in chosen_ng_fighters], screen="ucn_choice")
    $ if party_2 != "NONE": chosen_ng_fighters.append(party_2)
    $ narrator("Choose a party member! (3/4)", interact = False)
    $ party_3 = renpy.display_menu([(a.title() if a != "CS_NG" else "CS", a) for a in ng_fighters if a not in chosen_ng_fighters], screen="ucn_choice")
    $ if party_3 != "NONE": chosen_ng_fighters.append(party_3)
    $ narrator("Choose a party member! (4/4)", interact = False)
    $ party_4 = renpy.display_menu([(a.title() if a != "CS_NG" else "CS", a) for a in ng_fighters if a not in chosen_ng_fighters], screen="ucn_choice")
    rpg:
        bg "images/bg/battle_block_without_theater.png"
        music "audio/thousand_march.mp3"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            guard
            sml_tank
            guard
        scale 1.7
        on_win "cs_rage"
        on_lose "rpg_ng_fight"

label rpg_final_fight_1:
    $ final_fighters_1 = ["CS_STRONG", "ARCEUS", "PAKOO", "MIKA", "KITTY", "TATE", "ARIA", "DIGI", "NOVA", "BLANK", "MIDGE", "ANNO", "NONE"]
    $ chosen_final_fighters_1 = []
    $ narrator("Choose a party member! (1/4)", interact = False)
    $ party_1 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_1], screen="ucn_choice")
    $ if party_1 != "NONE": chosen_final_fighters_1.append(party_1)
    $ narrator("Choose a party member! (2/4)", interact = False)
    $ party_2 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_1 if a not in chosen_final_fighters_1], screen="ucn_choice")
    $ if party_2 != "NONE": chosen_final_fighters_1.append(party_2)
    $ narrator("Choose a party member! (3/4)", interact = False)
    $ party_3 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_1 if a not in chosen_final_fighters_1], screen="ucn_choice")
    $ if party_3 != "NONE": chosen_final_fighters_1.append(party_3)
    $ narrator("Choose a party member! (4/4)", interact = False)
    $ party_4 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_1 if a not in chosen_final_fighters_1], screen="ucn_choice")
    rpg:
        bg "images/bg/war_torn_2.png"
        music "audio/trans_atlantic.mp3"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            marine
            marine
            marine
        scale 1.75
        on_win "between_1"
        on_lose "rpg_final_fight_1"

label rpg_final_fight_2:
    $ final_fighters_2 = ["CS_STRONG", "ARCEUS", "PAKOO", "MIKA", "KITTY", "TATE", "ARIA", "DIGI", "NOVA", "BLANK", "MIDGE", "ANNO", "NONE"]
    $ chosen_final_fighters_2 = []
    $ narrator("Choose a party member! (1/4)", interact = False)
    $ party_1 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_2], screen="ucn_choice")
    $ if party_1 != "NONE": chosen_final_fighters_2.append(party_1)
    $ narrator("Choose a party member! (2/4)", interact = False)
    $ party_2 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_2 if a not in chosen_final_fighters_2], screen="ucn_choice")
    $ if party_2 != "NONE": chosen_final_fighters_2.append(party_2)
    $ narrator("Choose a party member! (3/4)", interact = False)
    $ party_3 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_2 if a not in chosen_final_fighters_2], screen="ucn_choice")
    $ if party_3 != "NONE": chosen_final_fighters_2.append(party_3)
    $ narrator("Choose a party member! (4/4)", interact = False)
    $ party_4 = renpy.display_menu([(a.title() if a != "CS_STRONG" else "CS", a) for a in final_fighters_2 if a not in chosen_final_fighters_2], screen="ucn_choice")
    rpg:
        bg "images/bg/war_torn_3.png"
        music "audio/trans_atlantic.mp3"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            marine
            big_tank
        scale 2.0
        on_win "between_2"
        on_lose "rpg_final_fight_1"

label rpg_final_fight_3:
    $ final_fighters_3 = ["ARCEUS", "PAKOO", "MIKA", "KITTY", "TATE", "ARIA", "DIGI", "NOVA", "BLANK", "MIDGE", "ANNO", "DB05", "NONE"]
    $ chosen_final_fighters_3 = []
    $ narrator("Choose a party member! (1/3)", interact = False)
    $ party_2 = renpy.display_menu([(a.title() if a != "CS_FINAL" else "CS", a) for a in final_fighters_3], screen="ucn_choice")
    $ if party_2 != "NONE": chosen_final_fighters_3.append(party_2)
    $ narrator("Choose a party member! (2/3)", interact = False)
    $ party_3 = renpy.display_menu([(a.title() if a != "CS_FINAL" else "CS", a) for a in final_fighters_3 if a not in chosen_final_fighters_3], screen="ucn_choice")
    $ if party_3 != "NONE": chosen_final_fighters_3.append(party_3)
    $ narrator("Choose a party member! (3/3)", interact = False)
    $ party_4 = renpy.display_menu([(a.title() if a != "CS_FINAL" else "CS", a) for a in final_fighters_3 if a not in chosen_final_fighters_3], screen="ucn_choice")
    rpg:
        bg "images/bg/war_torn_4.png"
        music "audio/prophetpart2.mp3"
        fighters:
            cs_final
            $party_2
            $party_3
            $party_4
            copguy_ex
        scale 2.0
        on_win "weapon_of_choice"
        on_lose "rpg_final_fight_1"

label rpg_error:
    rpg:
        bg "secret/falling_apart.png"
        music "audio/prophetpart2.mp3"
        fighters:
            cs_final2
            pakooe
        scale 2.0
        on_win "secret2"
        on_lose "after_error_fight"

label rpg_archival:
    rpg:
        bg "images/bg/csmart.png"
        fighters:
            cs_archival
            k174
            k199
            k207
        scale 1.0
        on_win "archival_finale"
        on_lose "rpg_archival"
        music "audio/broken_sky.mp3"