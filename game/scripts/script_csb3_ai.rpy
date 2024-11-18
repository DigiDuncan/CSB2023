label csbiii_ai:
    scene linusmedia with dissolve
    show cs at left with moveinleft
    play music school volume 0.4 if_changed
    music school
    if fun_value(FUN_VALUE_MUSIC):
        n "CS is at school, surrounded by computer parts and confused colleagues."
    else:    
        n "CS is in the Linus Tech Tips office, surrounded by computer parts and confused colleagues."
    show cs surprised
    n "CS scratches his head."
    cs "Aright, team, we've got a problem. This gaming PC is overheating, and we need a fix that's... shall we say, out of the box?"
    show luke at right with moveinright
    luke "CS, we've tried everything -- new fans, liquid cooling, you name it. Nothing seems to work!"
    cs "Well, have you tried the \"Hairdryer Cooling System\"?"
    n "Everyone exchanges puzzled glances."
    "Everyone" "The what?"
    show cs happy
    n "CS grins michevously."
    cs "Trust me, it's the ultimate cooling solution. Picture this: we attach a hairdryer to the CPU, set it to low heat, and let the breeze cool everything down. It's foolproof!"
    show linus at center with moveinright
    linus "Are you serious, CS? That sounds like a recipe for disaster."
    cs "Disaster? No, no, Linus. Think about it—hairdryers are designed to blow cool air, right? And what's cooler than a gentle breeze? It's foolproof, I tell you!"
    scene hairdryercoolingsystem with dissolve
    $ collect("hair_dryer")
    n "CS188 and the team are attaching a hairdryer to the gaming PC, with everyone watching nervously."
    cs "Aright, folks, brace yourselves. It's time to unleash the \"Hairdryer Cooling System\"!"
    play sound sfx_hairdryer    
    n "CS188 presses the power button, and the hairdryer roars to life, blowing a stream of cool air into the PC."
    scene tempsdown
    luke "Wait, it's actually working! The temperatures are dropping!"
    cs "Of course it is! Nature's own air conditioning!"
    linus "CS, I can't believe it. Your hairdryer solution is... actually genius."
    scene linusmedia
    show cs happy at left
    with dissolve
    cs "That's how we do things in CS188 style, Linus! Unconventional, unpredictable, but effective."
    play sound sfx_cheers
    n "The team erupts into laughter and applause as the gaming PC's temperatures stabilize."
    show linus at right with moveinright
    linus "CS, you've proven once again that there's always room for unconventional solutions in the world of tech."
    cs "Thank you, thank you. Just doing my part to keep things interesting."
    n "The team celebrates their successful, albeit unconventional, tech solution."
    n "Arceus bursts in."
    play sound sfx_house_door_open
    show arceus worried at center with moveinright
    arceus "CS! We've got to get out of here, and fast! The cops are hot on our tails!"
    show cs worried at left
    cs "Arceus, what in the world? Cops? I thought we were done with that prison break business!"
    arceus "Long story short, our disguise as janitors didn't quite fool them. We need to make a run for it before they catch up!"
    n "The colleagues in the office glance at each other, surprised and confused by the sudden turn of events."
    show cs disappointed
    cs "Okay, okay. We need a plan. I've got it! We'll use the secret escape tunnel we installed under the office!"
    show arceus happy
    arceus "Brilliant idea, CS! Lead the way!"
    show cs flipped with determination
    hide cs with moveoutleft
    hide arceus with moveoutleft
    stop music fadeout 0.5
    music end
    scene black with dissolve

    scene entertunnel with dissolve
    show cs at left with moveinleft
    show arceus at right with moveinright
    play music cliffs volume 0.4 if_changed
    music cliffs
    if fun_value(FUN_VALUE_MUSIC):
        n "CS188 and Arceus dash to a hidden panel on the floor, revealing a concealed entrance to the cliffs."
    else:
        n "CS188 and Arceus dash to a hidden panel on the floor, revealing a concealed entrance to the escape tunnel."
    scene secrettunnel with dissolve
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS188 and Arceus crawl through the dimly lit tunnel, their heartbeats echoing."
    show arceus worried
    arceus "CS, do you even know where this tunnel leads?"
    show cs happy
    cs "Not a clue, my foxy friend! But that's what makes it an adventure, right?"
    scene park1 with dissolve
    show cs at left with moveinbottom
    show arceus at right with moveinbottom
    play music circus volume 0.4 if_changed
    music circus
    if fun_value(FUN_VALUE_MUSIC):
        n "They emerge from the tunnel into a surprising location—an abandoned, overgrown circus."
    else:
        n "They emerge from the tunnel into a surprising location—an abandoned, overgrown amusement park."
    show arceus angry
    arceus "An amusement park? Seriously, CS?"
    show cs disappointed
    cs "Hey, when life hands you unexpected escapes, you make the most of them!"
    hide cs with moveoutright
    show arceus flipped with determination
    hide arceus with moveoutright
    scene park2 with dissolve
    show cs at right with moveinleft
    show arceus flipped at left with moveinleft
    n "CS188 and Arceus start exploring the amusement park, hiding among the dilapidated rides and attractions while evading the pursuing cops."
    hide cs with moveoutright
    show arceus flipped with determination
    hide arceus with moveoutright
    scene carousel with dissolve
    show cs at left with moveinleft
    show arceus at right with moveinright
    pause 0.5
    hide cs
    hide arceus
    with moveoutbottom
    n "CS188 and Arceus duck behind a broken carousel as the cops pass by."
    show copguy_ai at center with moveinbottom
    play music chase volume 0.4 if_changed
    music chase
    if fun_value(FUN_VALUE_MUSIC):
        n "CS188 and Arceus duck behind a broken carousel as the cops chase by."
    arceus "{size=-12}CS, we can't hide here forever. We need a distraction!"
    n "CS thinks for a sec."
    cs "{size=-12}I've got it! Remember that prank we pulled back in prison using inflatable rubber ducks?"
    arceus "{size=-12}How could I forget?"
    cs "{size=-12}Well, let's unleash the \"Quack Attack\" on our pursuers!"
    play sound sfx_duck loop volume 0.7
    show ai_ducks with dissolve
    $ collect("duck")
    n "CS188 and Arceus discreetly inflate dozens of rubber ducks and release them, causing a colorful and noisy chaos."
    n "The cops are distracted, slipping and sliding on the rubber ducks, as CS188 and Arceus make their getaway."
    show arceus happy flipped at right
    show cs happy at left
    with moveinbottom 
    show arceus flipped
    hide cs with moveoutright
    hide arceus with moveoutright
    with ease
    stop sound fadeout 7.0
    hide ai_ducks with dissolve
    hide copguy_ai with moveoutright
    n "The chase scene intensifies as CS188 and Arceus dash through the amusement park, narrowly avoiding capture at every turn."
    # totally didnt steal this transition from train route - tate
    show cs flipped at offscreenright with determination
    show cs flipped at offscreenleft
    with MoveTransition(0.5)
    show arceus at offscreenright with determination
    show arceus at offscreenleft
    with MoveTransition(0.5)
    show copguy_ai at offscreenright with determination
    show copguy_ai at offscreenleft
    with MoveTransition(0.5)
    scene park2 with dissolve
    show cs flipped at left with moveinright
    show arceus at right with moveinright
    show cs
    n "CS188 and Arceus reach the park's exit, breathing heavily but exhilarated."
    show arceus happy
    arceus "CS, that was insane! We actually made it!"
    n "CS catches his breath."
    show cs happy
    if fun_value(FUN_VALUE_MUSIC):
        n "We sure did, buddy. Another adventure for the books! Hooray for friendship!"
    else:
        cs "We sure did, buddy. Another adventure for the books!"  
    play music friendship volume 0.4 if_changed
    scene endingai with Fade(1.0, 1.0, 1.0)
    music friendship
    n "CS188 and Arceus exchange a high-five and disappear into the distance, ready for their next escapade."
    "ChatGPT" "Note: The script is a fictional representation and does not reflect the actual personalities or actions of CS188 or any real-life individuals."
    $ achievement_manager.unlock("chatgpt")
    $ ending_manager.mark("ai")
    pause 2.0
    $ renpy.end_replay()
    return
