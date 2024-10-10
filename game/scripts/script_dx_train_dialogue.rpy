label train_dialogue:
    play sfx sfx_ambiance_train_interior loop volume 0.3

    show amtrak_dining_day
    show cs at left
    show arceus at right
    with dissolve
    pause 2.0

    n "CS and Arceus are relaxing in the dining car after lunch."


    cs "Hey, Arc?"
    arceus "Yeah?"
    cs "You know how there are some images that you can hear?"
    arceus "What?"
    cs "You know, like that one GIF with the jump-roping power thing?"
    arceus "The what?!"
    show cs disappointed
    cs "You know, that big-ass power line!"
    cs "And, every time it lands, you can hear it go {i}boom,{/i} except you... don't?"
    arceus "Oh, that thing? What about it?"
    show cs
    cs "If there are GIFs you can hear..."
    cs "I think there are {i}words{/i} you can hear, too!"
    show cs happy
    cs "Like... 'extrusion'!"
    show arceus angry
    arceus "..."
    show cs
    cs "Don't you agree that 'extrusion' is one of those words you can {i}hear?"
    arceus "... You can {i}hear{/i} any word, CS."
    show cs worried
    cs "No, like, you hear the word, and you immediately picture what it's doing!"
    arceus "Again, that's {i}just{/i} how words work."
    cs "No! I mean like--"
    show cs disappointed
    cs "You know what, never mind..."
    pause 1.0
    show cs
    show arceus



    pause 3.0


    show cs surprised
    cs "I wonder what Tate and Mean are up to."
    cs "There's no way that Amtrak life can be that exciting {i}all{/i} the time, right?"
    arceus "Well, why don't we give them a call?"
    show cs
    cs "Great idea!"
    show cs phone with dissolve
    pause 0.5
    play sound sfx_dial_tate
    pause 10.0

    scene black with dissolve
    pause 3.0

    if fun_value(FUN_VALUE_COMMON):
        scene amtrak_cab
        show mean human hat at mid_right
        show tate at left
        with dissolve

        pause 1.0

        tate "Awawa awa!"
        mean "Yeah?"
        tate "Awawawawa!"
        show mean human hat happy
        mean "That's some real shit right there."
        show tate srs
        tate "Awa..."
        show mean shocked hat
        show tate shock
        mean "WOAH!! You can't {i}say{/i} that anymore!"
        tate "Uweh?!"
    else:
        scene amtrak_cab
        show mean human hat at center
        show tate sheepish at left
        with dissolve

        pause 1.0

        mean "So, yeah!"
        show mean human hat happy
        mean "Maybe feet {i}are{/i} comparable to kids!"
        tate "Wuh...?"

    pause 1.0

    if fun_value(FUN_VALUE_RARE):
        show tate shock
        play sound sfx_ringtone_tate_alt loop
        n "Tate gets a call on their cell phone."
        show tate srs
        show mean human hat
        show tate_phone at manual_pos(0.25, 0.45) with dissolve
        pause 1.0
        tate "..."
        tate "God damn it, I forgot to change his ringtone..."
    else:
        show tate shock
        play sound sfx_ringtone_tate loop
        n "Tate gets a call on their cell phone."
        show tate srs
        show tate_phone at manual_pos(0.25, 0.45) with dissolve

    pause 1.0
    play sound sfx_pickup_call
    show mean human hat 
    pause 1.0
    show tate
    show tate_phone at manual_pos(0.08, 0.4):
        xzoom -1
    with MoveTransition(0.25)
    pause 0.25
    tate "Heya, CS!"
    tate "How's your trip going?"
    cs "We actually were calling to ask you the same thing!"
    cs "It's been pretty chill so far."
    arceus "Tell them I said hi!"
    cs "Arc says hi."
    tate "Howdy, Arc!"
    mean "Oh, it's CS and Arc?"
    mean "Tell 'em I said hi!"
    tate "Mean says hi!"
    cs "Hi, Mean!"
    arceus "Heya, Mean!"
    "..."
    pause 1.0
    show tate sheepish
    tate "Well, nice hearing from ya!"
    cs "Yeah! Have a safe trip!"
    show tate
    tate "You too!"
    
    play sound sfx_end_call

    scene black with dissolve

    show amtrak_dining_day
    show cs phone at left
    show arceus at right
    with dissolve

    "..."
    pause 1.0
    show cs with dissolve
    pause 3.0
    show cs worried
    cs "Hey! Tate never answered our question!"
    show arceus angry
    arceus "Man, you had {i}one{/i} job!"
    show cs disappointed
    cs "It would be weird to call them back again so soon..."
    show arceus
    arceus "I guess we can call again when we get to New York." 
    show cs
    cs "You're probably right."

    pause 2.0

    "This is a placeholder."

    jump train_return_home_transition
