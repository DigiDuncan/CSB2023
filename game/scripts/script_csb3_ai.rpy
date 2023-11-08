label csbiii_ai:
    scene linusmedia with fade
    show cs at left with moveinleft
    play music "<loop 0>school.mp3" volume 0.4
    music School - Toby Fox
    n "CS is in the Linus Tech Tips office, surrounded by computer parts and confused colleagues."
    n "CS scratches his head."
    cs "Aright, team, we've got a problem. This gaming PC is overheating, and we need a fix that's... shall we say, out of the box?"
    show luke at right with moveinright
    luke "CS, we've tried everything -- new fans, liquid cooling, you name it. Nothing seems to work!"
    cs "Well, have you tried the \"Hairdryer Cooling System\"?"
    n "Everyone exchanges puzzled glances."
    "Everyone" "The what?"
    n "CS grins michevously."
    cs "Trust me, it's the ultimate cooling solution. Picture this: we attach a hairdryer to the CPU, set it to low heat, and let the breeze cool everything down. It's foolproof!"
    show linus at center with moveinright
    linus "Are you serious, CS? That sounds like a recipe for disaster."
    cs "Disaster? No, no, Linus. Think about it—hairdryers are designed to blow cool air, right? And what's cooler than a gentle breeze? It's foolproof, I tell you!"
    scene hairdryercoolingsystem
    n "CS188 and the team are attaching a hairdryer to the gaming PC, with everyone watching nervously."
    cs "Aright, folks, brace yourselves. It's time to unleash the \"Hairdryer Cooling System\"!"
    n "CS188 presses the power button, and the hairdryer roars to life, blowing a stream of cool air into the PC."
    scene tempsdown
    luke "Wait, it's actually working! The temperatures are dropping!"
    cs "Of course it is! Nature's own air conditioning!"
    linus "CS, I can't believe it. Your hairdryer solution is... actually genius."
    scene linusmedia
    show cs happy at left
    with fade
    cs "That's how we do things in CS188 style, Linus! Unconventional, unpredictable, but effective."
    n "The team erupts into laughter and applause as the gaming PC's temperatures stabilize."
    show linus at right with moveinright
    linus "CS, you've proven once again that there's always room for unconventional solutions in the world of tech."
    cs "Thank you, thank you. Just doing my part to keep things interesting."
    n "The team celebrates their successful, albeit unconventional, tech solution."
    n "Arceus bursts in."
    show arceus at center with moveinright
    arceus "CS! We've got to get out of here, and fast! The cops are hot on our tails!"
    show cs at left
    cs "Arceus, what in the world? Cops? I thought we were done with that prison break business!"
    arceus "Long story short, our disguise as janitors didn't quite fool them. We need to make a run for it before they catch up!"
    n "The colleagues in the office glance at each other, surprised and confused by the sudden turn of events."
    cs "Okay, okay. We need a plan. I've got it! We'll use the secret escape tunnel we installed under the office!"
    arceus "Brilliant idea, CS! Lead the way!"
    show cs flipped with determination
    hide cs with moveoutleft
    hide arceus with moveoutleft
    scene entertunnel with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    play music "<loop 0>cliffs.mp3" volume 0.4
    music Cliffs - Toby Fox
    n "CS188 and Arceus dash to a hidden panel on the floor, revealing a concealed entrance to the escape tunnel."
    scene secrettunnel with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS188 and Arceus crawl through the dimly lit tunnel, their heartbeats echoing."
    arceus "CS, do you even know where this tunnel leads?"
    cs "Not a clue, my foxy friend! But that's what makes it an adventure, right?"
    scene park1 with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    play music "<loop 0>circus.mp3" volume 0.4
    music Circus - Toby Fox
    n "They emerge from the tunnel into a surprising location—an abandoned, overgrown amusement park."
    arceus "An amusement park? Seriously, CS?"
    cs "Hey, when life hands you unexpected escapes, you make the most of them!"
    hide cs with moveoutright
    show arceus flipped with determination
    hide arceus with moveoutright
    scene park2 with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS188 and Arceus start exploring the amusement park, hiding among the dilapidated rides and attractions while evading the pursuing cops."
    hide cs with moveoutright
    show arceus flipped with determination
    hide arceus with moveoutright
    scene carousel with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS188 and Arceus duck behind a broken carousel as the cops pass by."
    show copguy_ai at center with moveinbottom
    play music "<loop 0>chase.mp3" volume 0.4
    music The Chase - Toby Fox
    n "Arceus whispers to CS."
    arceus "CS, we can't hide here forever. We need a distraction!"
    n "CS thinks for a sec."
    cs "I've got it! Remember that prank we pulled back in prison using inflatable rubber ducks?"
    arceus "How could I forget?"
    cs "Well, let's unleash the \"Quack Attack\" on our pursuers!"
    play sound "<loop 0>sfx_duck.ogg" loop volume 0.7
    n "CS188 and Arceus discreetly inflate dozens of rubber ducks and release them, causing a colorful and noisy chaos."
    play sound "<loop 0>sfx_duck.ogg" loop volume 0.7
    show ai_ducks
    n "The cops are distracted, slipping and sliding on the rubber ducks, as CS188 and Arceus make their getaway."
    hide copguy_ai with moveoutright
    stop sound fadeout 7.0
    hide ai_ducks with dissolve
    n "The chase scene intensifies as CS188 and Arceus dash through the amusement park, narrowly avoiding capture at every turn."
    show cs flipped with determination
    hide cs with moveoutleft
    hide arceus with moveoutleft
    scene park2 with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS188 and Arceus reach the park's exit, breathing heavily but exhilarated."
    arceus "CS, that was insane! We actually made it!"
    n "CS catches his breath."
    cs "We sure did, buddy. Another adventure for the books!"
    play music "<loop 0>friendship.mp3" volume 0.4
    scene endingai with Fade(1.0, 1.0, 1.0)
    music Friendship - Toby Fox
    n "CS188 and Arceus exchange a high-five and disappear into the distance, ready for their next escapade."
    "ChatGPT" "Note: The script is a fictional representation and does not reflect the actual personalities or actions of CS188 or any real-life individuals."
    $ achievement_manager.unlock("Artifical Unintelligence")
    pause 2.0
    $ renpy.end_replay()
    return
