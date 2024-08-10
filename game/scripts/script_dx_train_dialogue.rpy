label train_dialogue:
    stop music
    scene black with fade
    pause 3.0

    if fun_value(FUN_VALUE_RARE):
        play sound sfx_tate_ringtone_alt
        n "Tate gets a call on their cell phone."
        pause 1.0
        tate "..."
        tate "Uweh, I forgot to change his ringtone..."
    else:
        play sound sfx_tate_ringtone
        n "Tate gets a call on their cell phone."

    pause 1.0
    play sound sfx_pickup_call
    pause 1.0
    tate "Heya, CS."
    tate "This script isn't ready yet, sorry."
    tate "Maybe I'll have help writing this, maybe I won't."
    tate "Somehow, I feel like it's {i}all{/i} gonna be up to me, as usual."
    tate "I'd better get back to work."
    play sound sfx_end_call
    pause 2.0

    jump train_return_home_transition
