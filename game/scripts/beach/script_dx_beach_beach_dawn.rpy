label beach.beach_dawn:
    stop music fadeout 1.0
    scene black
    with dissolve

    play music cobalt_coast_2
    scene ocean_beach_entrance
    with dissolve
    music cobalt_coast_2

    n "CS and Arceus arrive at Ocean Beach."
    
    scene ocean_beach_path
    show cs happy at left
    show arceus at right
    with dissolve

    cs "Woohoo! We made it!"
    arceus "But why are we here again? You can't even swim."
    show cs
    cs "So? We can still cool off in the water."
    show arceus angry
    show cs disappointed

    if fun_value(FUN_VALUE_COMMON):
        arceus "Fuck you mean \"oui\"? You speakin' French?"
        arceus "I can't get my fur wet."
    else:
        arceus "Fuck you mean \"we\"? I can't get my fur wet."

    cs "Why not?"
    arceus "Because it'll take all day to dry and then I'll get all poofy."
    cs "Damn..."
    show cs
    cs "Well, {i}I{/i} still want to go in the water."
    cs "Be back in a sec."
    show arceus worried
    show cs flipped at offscreenleft with { "master": MoveTransition(1.0) }
    show arceus worried
    arceus "Wait, where are you going?"
    cs "I won't be long!"
    pause 2.0
    show arceus angry
    pause 1.0
    arceus "..."
    pause 1.0
    arceus "{size=-12}I guess it might feel good on my feet..."
    show arceus angry flipped at offscreenright with { "master": MoveTransition(1.0) }
    n "Arceus begins to follow the coastline."

    scene ocean_beach_coast with dissolve

    show arceus angry flipped at offscreenleft
    show obama beach at offscreenright
    show mean angry flipped at manual_pos(1.3, 0.8, 1.0)
    with determination

    show arceus angry flipped at left
    show obama beach at right
    show mean angry flipped at manual_pos(0.9, 0.8, 1.0)
    with MoveTransition(1.0)

    obama "Excuse me."
    show arceus worried flipped
    arceus "President Obama?!" with vpunch
    obama "Yes, it is I."
    obama "I have a question for you."
    obama "I found this strange talking ball. It is yellow, and {i}you{/i} are yellow-- does it belong to you?"
    show mean furious flipped
    mean_offscreen "For the last time, I'm not a fucking {nw}"
    extend "{i}ball!" with vpunch
    show mean angry flipped
    mean_offscreen "Now, will you put me down already?!"
    obama "I must return you to your owner. It is the ethical thing to do."
    obama "As President, I am determined to reunite all lost beach balls with their owners."
    mean_offscreen "Fine, the yellow fucker is my owner. Now, let me go!"
    obama "Fair enough. Have a wonderful day!"
    arceus "Wait, but I'm not-- {nw}"
    obama "If you will excuse me, I hear the hotdog stand here has a \"Presidential Special\", and I must ascertain whether it is worthy of that title."
    obama "Farewell for now!"
    show obama beach behind arceus at offscreenleft with move
    pause 2.0
    show mean flipped unamused
    mean_offscreen "Yo."
    mean_offscreen "Name's Mean."
    arceus "Uh, hey. I'm Arceus. I usually go by Arc, though."
    mean "Nice to, uh, be owned by you, I guess?"
    arceus "Nice to, um, be your owner, too...?"
    mean "Well, okay, I guess the closest thing to my \"owner\" would be my friend, but even {i}that's{/i} a stretch."
    mean "Have you seen someone in pink shorts?"
    arceus "'Fraid not. My friend and I actually just got here."
    show arceus angry flipped
    arceus "Where {i}is{/i} he, anyway?"
    mean "What's he look like?"
    arceus "Oh, uh, he's wearing a purple cat maid outfit."
    show mean ayo flipped
    mean "{i}That{/i} guy?! Yeah, I saw him just before the fuckin' President interrupted my swimming!"
    show tate beach flipped at mid_mid_right
    show cs beach happy flipped at right
    show mean ayo at manual_pos(0.5, 0.8, 1.0) behind arceus
    show arceus worried flipped
    with moveinright
    cs "Hey guys!"
    cs "You won't {i}believe{/i} who I just ran into!"
    arceus "CS, what are you-- {nw}"
    mean "Tate! There you are!"
    mean "Wait-- you {nw}"
    extend "{i}know{/i} this guy?!" with vpunch
    show tate sheepish beach flipped
    tate "Yeah? This is CS."
    mean "{i}That's{/i} CS?!" with vpunch
    show cs disappointed beach flipped
    cs "Wait, what do you mean?"
    show arceus angry flipped
    arceus "Isn't it obvious?"
    tate "{size=-12}Listen, it's better not to question it."
    cs "What'd you say?"
    show tate beach
    tate "Eh? I didn't say anything."
    tate "Now, are we gonna go get that hot dog, or what?"
    show tate beach flipped
    show mean wat behind arceus
    show arceus worried flipped
    arceus "Shit, I want one... we haven't eaten in, uh, a while."
    show mean behind arceus
    mean "Eh, fuck it, I could eat."
    show mean happy behind arceus
    mean "Let's go! My treat."

    show cs happy beach flipped
    show arceus happy flipped
    cs "Wow, thanks!" (multiple=3)
    arceus "Thank you so much!" (multiple=3)
    tate "Hell yeah, thank you!" (multiple=3)

    show arceus flipped at offscreenright
    show mean happy at manual_pos(1.3, 0.8, 1.0)
    show tate beach at offscreenright
    show cs beach at offscreenright
    with move

    scene ocean_beach_sand

    show cashier flipped at left
    show hotdog_stand at manual_pos(0.5, 1.2, 1.0):
        zoom 2.0
    $ persistent.seen.add("peepy")
    show cornpy at manual_pos(0.325, 0.7, 1.0):
        zoom 0.15
    show corn at manual_pos(0.5, 0.8, 1.0) behind cashier:
        zoom 0.5
    show obama beach at manual_pos(0.8, 0.8, 1.0) behind cashier:
        zoom 0.5
    with dissolve

    obama "Excuse me, sir!"
    obama "Is that by any chance the Presidential Special?"
    worker_1_beach "I don't know!"

    pause 1.0

    show cs beach flipped at manual_pos(1.4, 1.0, 1.0)
    show arceus flipped at manual_pos(1.6, 1.0, 1.0)
    show tate beach flipped at manual_pos(1.8, 1.0, 1.0)
    show mean flipped at manual_pos(2.0, 1.0, 1.0)

    n "CS and the gang approach the hotdog stand."

    show cs beach flipped at mid_left
    show arceus angry at center
    show tate sheepish beach flipped at mid_right
    show mean wat flipped at right 
    with { "master": MoveTransition(5.0) }

    cs "... {fast}Then, I finally got my sock up my ass, and then I lost it for one hour, and then I {i}finally{/i} found it in my poop."
    pause 1.0
    show cs surprised beach flipped
    pause 2.0
    show cs disappointed beach
    show obama beach flipped at offscreenright with { "master": MoveTransition(5.0) }
    cs "Yeah, so, uh, what was I talking about?"
    arceus "Y'know, I don't think I'm hungry anymore."
    


        
    call screen beach_overworld_map( 
        current_time = "day",
        current_location = (500, 690, "Ocean Beach"),
        jump_points = [
            (800, 200, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_day"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_day"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_day"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_day")
        ]
    )