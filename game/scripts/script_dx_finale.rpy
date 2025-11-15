label finale_fun_value_land:
    scene white
    stop music fadeout 3.0
    cs "Woaoaoaoaoahhhh!!"
    scene black with dissolve
    cs "Ohhh... ow..."
    cs "I think I'm back..."
    play music funvalueland fadein 5.0 volume 3 if_changed
    music funvalueland
    cs "Oh God, am I home?"
    scene fun_cs_house with dissolve
    pause 3.0
    show cs disappointed at mid_left with moveinbottom
    cs "Oh my God..."
    cs "This isn't home."
    cs "I think I'm gonna throw up."

label finale_train_takeoff:
    stop music
    scene amtrak_cab
    show cs disappointed flipped at right
    show mean at mid_right
    show amtrak_conductor at center behind mean
    pause 2.0
    play music interference if_changed
    music interference
    show cs worried flipped
    show mean ayo flipped
    amtrak_conductor "Shit!" with vpunch
    show mean scared flipped
    mean "We have one of those corruption storms coming our way!"
    show cs scared flipped
    cs "A what?!"
    amtrak_conductor "We experienced a storm earlier that seemingly has unknown effects while in it."
    show mean worried flipped
    amtrak_conductor "We were on the edge of it though, it looks like we are going to go right through it."
    cs "Man, we just can't get a break can we?"
    scene train_brake
    mean "Here we go!!!!"
    play sound sfx_train_brake
    mean "Wait, I can't--"
    amtrak_conductor "Uh oh! Everyone, hold on!"
    stop sound fadeout 5.0
    "Everyone" "Woooooahh!!!"
    scene car plains night
    show flying_train_final at center with easeinright
    cs "We... are... flying!"
    scene amtrak_coach_1 at t_train_scurvy
    show michael at truecenter, t_people_scurvy
    show cashier at manual_pos(0.8,0.5), t_people_scurvy
    with dissolve
    michael "What the bloody hell is going on?!"
    show amtrak_conductor flipped at manual_pos(0.0,0.4), t_people_scurvy with moveinleft
    amtrak_conductor "The storm has managed to pick up the train!"
    cashier "What the hell? What kind of storm is this??"
    amtrak_conductor "It's a corruption storm, or at least that's what we calling it now."
    amtrak_conductor "I need to get back up to the front, no one get near the doors!"
    michael "I think that's well out of our control, but, alright!"
    show amtrak_conductor with determination
    hide amtrak_conductor with moveoutleft
    scene amtrak_cab at t_train_scurvy
    show cs worried flipped at right, t_people_scurvy
    show mean tired at mid_right, t_people_scurvy
    with dissolve
    show amtrak_conductor flipped at center, t_people_scurvy with moveinright
    show amtrak_conductor with determination


    cs "Hey, you're back!"
    amtrak_conductor "Mean! Why aren't you in your human form?"
    amtrak_conductor "You can't drive as well like that!"
    mean "I can't switch! Watch!"
    amtrak_conductor "Dammit, it's probably the storm screwing up your ability."
    amtrak_conductor "Don't worry, I'll try my best to watch out for the tracks."
