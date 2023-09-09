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
            copguy1
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
    rpg:
        bg "images/bg/battle_block_without_theater.png"
        music "audio/thousand_march.mp3"
        fighters:
            cs_ng
            tate
            digi
            arceus
            guard
            sml_tank
            guard
        scale 1.2
        on_win "cs_rage"
        on_lose "rpg_ng_fight"

label rpg_final_fight_1:
    rpg:
        bg "images/bg/war_torn_2.png"
        music "audio/trans_atlantic.mp3"
        fighters:
            cs_strong
            tate
            digi
            arceus
            marine
            marine
            marine
        scale 2.0
        on_win "rpg_final_fight_2"
        on_lose "rpg_final_fight_1"

label rpg_final_fight_2:
    rpg:
        bg "images/bg/war_torn_3.png"
        music "audio/trans_atlantic.mp3"
        fighters:
            cs_strong
            tate
            digi
            arceus
            marine
            big_tank
        scale 2.0
        on_win "rpg_final_fight_3"
        on_lose "rpg_final_fight_1"

label rpg_final_fight_3:
    rpg:
        bg "images/bg/war_torn_4.png"
        music "audio/trans_atlantic.mp3"
        fighters:
            cs_final
            tate
            digi
            arceus
            copguy2
        scale 2.0
        on_win "weapon_of_choice"
        on_lose "rpg_final_fight_1"
