label finale_fun_value_land:
    scene white
    stop music fadeout 3.0
    cs "Woaoaoaoaoahhhh!!"
    scene black with dissolve
    cs "Ohhh... ow..."
    cs "I think I'm back..."
    play music funvalueland fadein 5.0 volume 3
    $ persistent.heard.add("SPOT.FASSIMRD - Fun Value Land")
    cs "Oh God, am I home?"
    scene fun_cs_house with dissolve
    pause 3.0
    show cs disappointed at mid_left with moveinbottom
    cs "Oh, my God..."
    cs "This isn't home."
    cs "I think I'm gonna throw up."

label finale_train_takeoff:
    play music interference
    music Interference - Sanity
    scene amtrak_cab
    amtrak_conductor "Shit!"
    mean "We have one of those corruption storms coming our way!"
    cs "A what?!"
    amtrak_conductor "We experienced a storm earlier that seemingly has unknown effects while in it."
    amtrak_conductor "We were on the edge of it though, it looks like we are going to go right through it."
    cs "Man, we just can't get a break can we?"
    mean "Here we go!!!!"
    mean "Wait, I can't--"
    amtrak_conductor "Uh oh! Everyone, hold on!"
    "Everyone" "Woooooahh!!!"
    scene car plains night
    show flying_train_final at center with easeinright
    cs "We... are... flying!"
    michael "What the bloody hell is going on?!"
    amtrak_conductor "The storm has managed to pick up the train!"
    cashier "What the hell? What kind of storm is this??"
    amtrak_conductor "It's a corruption storm, or at least that's what we calling it now."
    amtrak_conductor "I need to get back up to the front, no one get near the doors!"
    michael "I think that's out of our control, but okay!"
    cs "Hey, your back!"
    amtrak_conductor "Mean! Why aren't you in your human form?"
    amtrak_conductor "You can't drive like that!"
    mean "I can't switch! Watch!"
    amtrak_conductor "Damnit, it's probably the storm screwing up your ability."
    amtrak_conductor "Don't worry, I'll try my best to watch out for the tracks."
