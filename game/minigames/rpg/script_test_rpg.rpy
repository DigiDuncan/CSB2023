label test_rpg:
    rpg:
        bg "images/bg/casino1.png"
        music "audio/card_castle.mp3"
        fighters:
            cs
            cop
            cop
            cop
        goto "secret"

label fanboy_fight_amd:
    rpg:
        bg "images/bg/linus_office_outside.png"
        music "audio/nordic_report_1.mp3"
        fighters:
            cs_weak
            fanboyb
            fanboyb
            fanboyb
        goto "after_fanboy"

label fanboy_fight_nvidia:
    rpg:
        bg "images/bg/linus_office_outside.png"
        music "audio/nordic_report_2.mp3"
        fighters:
            cs_weak
            fanboya
            fanboya
            fanboya
        goto "after_fanboy"