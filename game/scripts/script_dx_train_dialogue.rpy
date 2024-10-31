# TODO: better moving backgrounds
# TODO: ALL INSTANCES OF CAR PLAINS / CAR PLAINS NIGHT ARE PLACEHOLDERS

label train_dialogue:
    stop music fadeout 1.0
    music end

    play sfx sfx_ambiance_train_interior loop volume 0.3

    show car plains
    show amtrak_dining_day
    show cs at left
    show arceus at right
    with dissolve
    pause 2.0

    n "CS and Arceus are relaxing in the dining car after lunch."

    cs "Damn, that was pretty good."
    if train_ending_money_returned == True:
        cs "Not as good as Tate's cooking was, but I'd get it again."
        arceus "Same."
    else:
        show cs disappointed
        cs "Don't tell them I said this, but... it sure beats the pants off of Tate's cooking."
        if train_pancake_fun_value == True:
            arceus "I'm sure they were just having an off day."
            arceus "I stole one of Mean's pancakes that Tate made yesterday. Now, {i}those{/i} were awesome."
            cs "Damn, I wish I'd gotten one, too..."
            show cs
        else:
            arceus "Yeah... I didn't want to say anything. I saw you with those salt packs..."
            show cs worried
            cs "Shit. Here I thought I was being sneaky."
            arceus "Nope."
            show cs disappointed
            cs "I sure hope they didn't notice..."
            arceus "I'm sure it's fine. Lots of people salt their food."
            show cs

    cs "Well, now what do you wanna do?"
    arceus "I dunno. After the night we had, I'm honestly happy to just do nothing at all."
    arceus "I kinda just want to stay right where we're at."
    arceus "The view here is a hell of a lot nicer than the one coming up from Vegas, that's for sure."
    cs "That is true. It's a lot more green."
    cs "Yeah, let's just hang out here awhile."

    

    pause 3.0



    cs "Hey, Arc?"
    arceus "Yeh?"
    cs "You know how there are some images that you can hear?"
    arceus "What?"
    cs "You know, like that one GIF with the jump-roping power thing?"
    arceus "The what, now?"
    show cs disappointed
    cs "You know, that big-ass power line!"
    cs "And, every time it lands, you can hear it go {i}boom,{/i} except you... don't?"
    arceus "Oh, {i}that{/i} thing. What about it?"
    show cs
    cs "If there are GIFs you can hear..."
    cs "I think there are {i}words{/i} you can hear, too!"
    show cs happy
    cs "Like... \"extrusion\"!"
    show arceus angry
    arceus "..."
    show cs
    cs "Don't you agree that \"extrusion\" is one of those words you can {i}hear?"
    arceus "... You can {i}hear{/i} any word, CS."
    show cs worried
    cs "No, like, you {i}hear{/i} the word, and you {i}immediately{/i} picture what it's doing!"
    arceus "Again, that's {i}just{/i} how words work."
    cs "No! I mean like--"
    show cs disappointed
    cs "You know what, never mind..."
    pause 1.0
    show cs
    show arceus
    with dissolve



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

    # prevent dial tone overflow
    stop sound

    if fun_value(FUN_VALUE_COMMON):
        scene
        show car plains:
            xzoom -1
        show amtrak_cab
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
        show mean human hat
        mean "Yeah, you know, I never thought of it like that before."
        show tate sad
        tate "Awawawawawa awawa?"
        show mean human hat shocked
        mean "Why would Cookie Monster be eating fucking {i}cobalt?!"
        show tate srs
        tate "{cshake}Awawawa!!!"
        show mean angry hat
        show tate shock
        mean "WOAH!! You can't {i}say{/i} that anymore!" with vpunch
        tate "Awawa?!"
        mean "No! Fuck you!"
        show tate sheepish
        tate "A..."
    else:
        scene
        show car plains:
            xzoom -1
        show amtrak_cab
        show mean human hat at mid_right
        show tate stare at left
        with dissolve

        pause 1.0

        mean "... So, yeah!"
        show mean human hat happy
        mean "Maybe feet {i}are{/i} comparable to kids!"
        pause 2.0
        show tate sheepish at left
        tate "Wuh...?"

    pause 1.0

    if fun_value(FUN_VALUE_RARE):
        play sound sfx_ringtone_tate_alt loop
        $ persistent.heard.add("sfx_ringtone_tate_alt")
        show tate shock
        show mean human hat shocked
        n "Tate gets a call on their cell phone."
        show tate srs
        show mean human hat annoyed

        show tate_phone with MoveTransition(0.25):
            xpos 0.25
            ypos 0.65
            alpha 0.0
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 ypos 0.45
        
        $ collect("tate_phone")
        pause 1.0
        tate "..."
        show mean human hat annoyed
        tate "God damn it, I forgot to change his ringtone..."
    else:
        play sound sfx_ringtone_tate loop
        $ persistent.heard.add("sfx_ringtone_tate")
        show tate shock
        show mean human hat shocked
        n "Tate gets a call on their cell phone."
        show tate srs

        show tate_phone with MoveTransition(0.25):
            xpos 0.25
            ypos 0.65
            alpha 0.0
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 ypos 0.45

    $ collect("tate_phone")
    pause 2.0
    play sound sfx_pickup_call
    show mean human hat annoyed
    pause 1.0
    show tate
    show tate_phone at manual_pos(0.08, 0.4):
        xzoom -1
    with MoveTransition(0.25)
    pause 0.25
    tate "Heya, CS!"
    tate "How's your trip going?"
    cs "Hey, Tate!"
    cs "We were actually calling to ask you the same thing!"
    cs "It's been pretty uneventful so far on our end."
    arceus "Tell them I said hi!"
    cs "Arc says hi."
    tate "Howdy, Arc!"
    show mean human hat
    mean "Oh, it's CS and Arc?"
    mean "Tell 'em I said hi!"
    tate "Mean says hi!"
    cs "Hi, Mean!"
    arceus "Heya, Mean!"
    tate "They both also said hi!"
    mean "Sweet."
    "..."
    pause 1.0
    show tate sheepish
    "..."
    tate "Well, nice hearing from ya!"
    cs "Yeah! Have a safe trip!"
    show tate
    tate "You, too!"

    scene black with dissolve

    scene
    show car plains
    show amtrak_dining_day
    show cs phone at left
    show arceus at right
    with dissolve
    play sound sfx_end_call

    "..."
    pause 1.0
    show cs with dissolve
    pause 3.0
    show cs worried
    cs "Hey! Tate never answered our question!"
    show arceus angry
    arceus "Man, you had {i}one{/i} job!"
    show cs disappointed
    cs "It would be weird to call them back right away..."
    show arceus
    arceus "Let's call again when we get to New York." 
    show cs
    cs "Yeah, let's do that."



    pause 3.0
    


    show arc_laptop at manual_pos(0.65, 0.55, 0.5) behind arceus with dissolve
    $ collect("arc_laptop")
    pause 0.5
    play music nyan volume 0.05
    pause 2.0
    n "Arceus pulls out a laptop and starts playing a game."
    pause 3.0
    show arceus angry
    arceus "Fucking hell..."
    cs "Whatcha playing?"
    arceus "Just some stupid minigame boss battle."
    show cs disappointed
    arceus "I'm {i}so{/i} sick of hearing this song, but I just want to get this achievement already..."
    arceus "Rhythm games are just {i}not{/i} my thing."
    show cs
    cs "Can I take a shot at it? I'm pretty decent at rhythm games."
    show arceus worried
    arceus "Uh..."
    "..."
    show cs disappointed
    arceus "Oh, whoops! Would ya look at that. Low battery."
    arceus "Guess I forgot to charge it last night."
    cs "Damn. Maybe next time."
    arceus "Yeah... next time..."
    stop music
    hide arc_laptop with dissolve
    n "Arceus puts the laptop away."
    "..."
    show cs worried
    cs "Wait! Where'd you get a laptop, anyway?!"
    show arceus
    arceus "Wherever you picked up that phone after we got out of jail."
    "..."
    show cs scared
    cs "I... don't remember buying this."
    cs "Am I going insane?"
    show cs worried
    arceus "I think you just need to catch up on sleep."
    show cs disappointed
    cs "I hope you're right..."
    "..."
    
    if train_ending_money_returned == True:
        cs "I must have bought it at that gas station we stopped at..."
        cs "Is {i}this{/i} what it's like to be rich? Just being able to buy expensive things without thinking?"
        arceus "I guess it is."
    else:
        cs "At least I probably bought it {i}before{/i} we ended up broke again..."
        cs "I don't think I'd buy something on a whim like that otherwise."
        cs "It's so weird that I can't remember..."
        arceus "Eh, last few days have been a blur for me, too."
        arceus "I really do think that you're just really tired."
        cs "I guess..."

    pause 2.0
    show cs with dissolve



    pause 3.0



    n "CS and Arceus take it easy for the rest of the ride..."

    stop sfx fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0

    jump train_return_home_transition
