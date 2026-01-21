# IMPORTANT!
# You no longer need to manually register battle music in the jukebox before jumping to the battle's label.
# Just define it here with the ID as defined in jukebox.json
# As long as this is done, and the track exists in the JSON, battle music will be registered in jukebox automatically.

label rpg_test:
    rpg:
        bg "images/bg/casino1.png"
        music "card_castle"
        fighters:
            cs
            $enemy_1
            $enemy_2
            $enemy_3
        scale 1.0
        on_win "secret_dx"
        on_lose "secret_dx"
        intro_text "Let the test battle commence!"

label rpg_fanboy_fight_amd:
    rpg:
        bg "images/bg/linus_office_outside.png"
        music "nordic_report_1"
        fighters:
            cs_weak
            fanboyb
            fanboyb
            fanboyb
        scale 1.0
        on_win "friend_after_fanboy"
        on_lose "friend_fanboy_lose"
        intro_text "AMD fanboys have come to cancel you!"

label rpg_fanboy_fight_nvidia:
    rpg:
        bg "images/bg/linus_office_outside.png"
        fighters:
            cs_weak
            fanboya
            fanboya
            fanboya
        scale 1.0
        on_win "friend_after_fanboy"
        on_lose "friend_fanboy_lose"
        music "nordic_report_2"
        intro_text "NVIDIA fanboys have come to cancel you!"

label rpg_cop_fight_1:
    rpg:
        bg "images/bg/dealership.png"
        music "compulsion_to_obey"
        fighters:
            cs
            arceus
            pakoo
            cop
            cop
            copguygodmode
        scale 1.0
        on_win "secret_dx"
        on_lose "friend_so_join"
        intro_text "Copguy is here to detain you!"

label rpg_cop_fight_2:
    rpg:
        bg "images/bg/dealership.png"
        music "for_the_people"
        fighters:
            mika
            kitty
            tate
            copguy
        scale 1.0
        on_win "friend_after_cop_fight"
        on_lose "rpg_cop_fight_2"
        intro_text "Copguy is ready for more!"

label rpg_cop_fight_3:
    rpg:
        bg "images/bg/cs_somewhere.png"
        music "desert_dawn"
        fighters:
            aria
            cop
            cop
        scale 1.0
        on_win "friend2_cs_meetup"
        on_lose "rpg_cop_fight_3"
        intro_text "The cops ready their pistols!"

label rpg_cop_fight_4:
    rpg:
        bg "images/bg/dinerinside.png"
        music "dinerfight"
        fighters:
            digi
            nova
            cop
            cop
        scale 1.0
        on_win "friend2_cs_meetup_2"
        on_lose "rpg_cop_fight_4"
        intro_text "The cops are suspicious of you!"

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
        music "thousand_march"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            guard
            sml_tank
            guard
        scale 1.7
        on_win "friend2_cs_rage"
        on_lose "rpg_ng_fight"
        intro_text "The National Guard has crosshairs on you!"

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
        music "trans_atlantic"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            marine
            marine
            marine
        scale 1.75
        on_win "friend2_between_1"
        on_lose "rpg_final_fight_1"
        intro_text "Reinforcements have arrived!"

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
        music "trans_atlantic"
        fighters:
            $party_1
            $party_2
            $party_3
            $party_4
            marine
            big_tank
        scale 2.0
        on_win "friend2_between_2"
        on_lose "rpg_final_fight_1"
        intro_text "Another squadron enters the fray!"

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
        music "prophetpart2"
        fighters:
            cs_final
            $party_2
            $party_3
            $party_4
            copguy_ex
        scale 2.0
        on_win "friend2_weapon_of_choice"
        on_lose "rpg_final_fight_1"
        intro_text "Copguy EX is here to end this!"

label rpg_error:
    rpg:
        bg "images/bg/falling_apart.png"
        music "prophetpart2"
        fighters:
            cs_final2
            pakooe
        scale 2.0
        on_win "secret_dx"
        on_lose "after_error_fight"
        intro_text "Pakoo has come to restore order!"

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
        music "broken_sky"
        intro_text "The odd trio blocks your path!"

label rpg_bronsonbattle:
    rpg:
        bg "images/bg/bronsoncrash.png"
        fighters:
            cs_weak
            arceus
            billy
            copguy_exe
        scale 1.0
        on_win "michigan_bronson_win"
        on_lose "rpg_bronsonbattle"
        music "error"
        intro_text "You are challenged by... Copguy?"

label rpg_tate_ex:

    python:
        if ch2_cs_attack_used == "karate-chopped":
            cs_chosen_form = "CS_VS_TATE_CHOP"
        elif ch2_cs_attack_used == "Sparta-kicked":
            cs_chosen_form = "CS_VS_TATE_KICK"
        else:
            cs_chosen_form = "CS_VS_TATE_PUNCH"

    rpg:
        bg "images/bg/train/amtrak_observation_2.png"

        fighters:
            $cs_chosen_form
            tate_ex

        scale 2.0
        on_win "train_tate_ex_win"
        on_lose "train_tate_ex_lose"
        music "space"
        intro_text "Tate EX challenges you!"


label rpg_diabetes_1:
    rpg:
        bg "images/bg/bronsoncrash.png"
        fighters:
            cs_strong
            digi
            ceo

        scale 1.0
        on_win "bt1d_after_fight_1"
        on_lose "rpg_diabetes_1"
        music "error"
        intro_text "The CEO is late for a meeting."

label rpg_diabetes_2:
    rpg:
        bg "images/bg/bronsoncrash.png"
        fighters:
            cs_strong
            digi
            secretary

        scale 2.0
        on_win "bt1d_after_fight_2"
        on_lose "rpg_diabetes_2"
        music "error"
        intro_text "The secretary will see you now."

label rpg_diabetes_3:
    rpg:
        bg "images/bg/bronsoncrash.png"
        fighters:
            cs_strong
            digi
            ceo
            secretary

        scale 2.0
        on_win "bt1d_ending"
        on_lose "rpg_diabetes_3"
        music "error"
        intro_text "The C-Suite is ready to end this meeting!"

