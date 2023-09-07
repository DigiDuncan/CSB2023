label knocked_out:
    scene black
    n "..."
    n "As CS' vision fades back into view, he can also hear a faint heart monitor beeping."
    scene hospital_room with dissolve
    n "CS immediately snaps up."
    show cs worried at mid_left with moveinbottom
    cs "Wha--"
    cs "What happened? How long have I been out?"
    show cs disappointed
    cs "Thank god I didn't catch some virus from a global pandemic or something."
    cs "I guess that's the last time I try to fight someone."
    n "CS sits there for a minute, trying to recollect his memory."
    cs "So I went to go work at LTT, after I..."
    cs "What did I do before that?"
    n "The news starts playing on the TV in CS' room, explaining how 3 criminals broke out of prison a couple days ago."
    show cs worried
    cs "Oh shoot! Yeah I went to prison and met Arceus and Anno! I need to get out of here!"
    hide cs with moveoutright
    n "CS goes and gets dressed, and runs out of his room."
    scene black with dissolve
    window hide
    pause 1.5
    scene hospital_reception with fade
    show cs worried flipped at mid_left with moveinright
    pause 0.5
    show cs disappointed flipped at right with move
    show cs flipped
    cs "Excuse me, do you know where the closest airport is?"
    nurse "Uhh yeah, it's actually about a mile or two east of here."
    cs "Thank you, bye!"
    hide cs with moveoutleft
    nurse "Uhm sir, shouldn't you stay in your room?"
    nurse "Sir?"
    nurse "Welp. I guess he's feeling fine."
    scene canada_block
    show cs disappointed at left
    with fade
    cs "Ah shit, I need to really get out of here before the cops catch up with me."
    cs "I hope Linus left me enough money to travel, otherwise I'm probably screwed."
    cs "Man, I hope that Arceus and Anno are okay too, I wonder what happened to them..."
    hide cs with moveoutright
    scene black with dissolve
    n "CS hastily makes his way to the airport."
    window hide
    pause 1.0
    scene airport_interior with fade
    play music "<loop 0>airport.mp3" volume 0.4
    music Airport Infilration - Marten Joustra
    show cs at left with moveinleft
    cs "Alright, whew! I made it."
    cs "I need to see if there is a plane that I can book quickly!"
    hide cs with moveoutright
    n "CS dashes over to the ticket counter."
    scene ticket_counter
    show benrey at center
    with fade
    show cs at left with moveinleft
    benrey "Hey, do you have your Pass Port?"
    show cs worried
    cs "Oh shiiiiiiiiiiiiiiiiiit."
    benrey "You can't get on the plane without your Pass Port."
    show cs disappointed
    cs "I'm sorry, I don't have one. Can you like, give me one?"
    benrey "Well what country do you want to go visit?"
    menu:
        "England":
            jump england_travel
        "Sweden":
            jump sweden_travel
        "Japan":
            jump japan_travel
    
label england_travel:
    cs "Uhh, I guess I wanted to go to England?"
    benrey "Well I'm sorry, but everyone has a Pass Port!"
    benrey "Try checking your pocket."
    n "CS puts his hand in his pocket and pulls out an Canadian passport."
    show cs
    cs "Oh, well look at that!"
    benrey "See? I told you! Now let's get you your ticket."
    n "CS hands the ticket man his money."
    benrey "Alright, your plane is actually leaving here in about 15 minutes."
    cs "Ah shit, thanks!"
    hide cs with moveoutright
    show airport_tsa
    show tsa at right
    with fade
    n "CS rushes up to the TSA to get checked through."
    show cs at mid_left with moveinleft
    cs "*Huff huff* I'm almost there!"
    tsa "Alright, drop your bags off in the conveyor."
    cs "I don't have any bags."
    tsa "What? Go through the metal detector!"
    show cs at mid_right with move
    n "CS walks through, and the detector stays silent."
    tsa "Impossible!"
    cs "So this means I'm good to go, right?"
    n "The TSA man grumbles."
    tsa "Yes, you're good to go, sir."
    show cs happy
    cs "Woohoo! Thanks!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS manages to get on his plane, right before the terminal closes down."
    stop music fadeout 3.0
    music end
    scene airplane_seats
    show cs at left
    with fade
    n "CS gets himself comfortable, and tries to not think about the cops."
    cs "Whew! What a day."
    cs "I really hope this works out, I don't think I have enough to travel again after this."
    cs "I didn't think this is how I'd be going to another country, rushing out of a hospital and all."
    cs "Well, it's been a long day."
    cs "I guess I should get some rest."
    scene black with dissolve
    jump england

label sweden_travel:
    cs "Uhh, I guess I wanted to go to Sweden?"
    benrey "But everyone has a Pass Port!"
    benrey "Try checking your back pocket."
    n "CS puts his hand in his back pocket and pulls out an Canadian passport."
    show cs
    cs "Oh, didn't know I had this!"
    benrey "See? I told you! Everyone has a Pass Port! Now let's get you your ticket."
    n "CS hands the ticket dude his money."
    benrey "Alright, your plane is actually leaving here in about 20 minutes."
    cs "Ah shoot, thanks!"
    hide cs with moveoutright
    show airport_tsa
    show tsa at right
    with fade
    n "CS rushes up to the TSA to get checked through."
    show cs at mid_left with moveinleft
    cs "*Pant pant* I'm almost there!"
    tsa "Alright, drop your bags off here."
    cs "I don't, have any bags?"
    tsa "Alright then, just go through the metal detector!"
    show cs at mid_right with move
    n "CS walks through, and the detector stays silent."
    tsa "Huh."
    cs "So this means I'm good to go, right?"
    tsa "Yes, you're good to go, sir."
    show cs happy
    cs "Woohoo! Thanks!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS manages to get on his plane, right before the terminal closes down."
    stop music fadeout 3.0
    music end
    scene airplane_seats
    show cs at left
    with fade
    n "CS gets himself comfortable, and tries to not think about the cops."
    cs "Whew! What a day."
    cs "I really hope this works out, I don't think I have enough to travel again after this."
    cs "I didn't think this is how I'd be going to another country, rushing out of a hospital and all."
    cs "Well, it's been a long day."
    cs "I guess I should get some rest."
    scene black with dissolve
    jump sweden

label japan_travel:
    cs "Uhh, I guess I wanted to go to Japan?"
    benrey "Well I'm sorry, but everyone's got a Pass Port!"
    benrey "Try checking your left shoe."
    n "CS takes off his left shoe and pulls out an Canadian passport."
    show cs
    cs "Oh, what in the world?"
    benrey "See? I knew it! Now let's get you your ticket."
    n "CS hands the ticket guy his money."
    benrey "Alright, your plane is actually leaving here in about 10 minutes."
    cs "Ah shucks, thanks!"
    hide cs with moveoutright
    show airport_tsa
    show tsa at right
    with fade
    n "CS rushes up to the TSA to get checked through."
    show cs at mid_left with moveinleft
    cs "I'm almost there!"
    tsa "Alright, go on through."
    show cs at mid_right with move
    n "CS walks through, and the detector stays silent."
    cs "So this means I'm good to go, right?"
    n "The TSA man nods."
    tsa "Yes, you're good to go, sir."
    show cs happy
    cs "Woohoo! Thanks!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS manages to get on his plane, right before the terminal closes down."
    stop music fadeout 3.0
    music end
    scene airplane_seats
    show cs at left
    with fade
    n "CS gets himself comfortable, and tries to not think about the cops."
    cs "Whew! What a day."
    cs "I really hope this works out, I don't think I have enough to travel again after this."
    cs "I didn't think this is how I'd be going to another country, rushing out of a hospital and all."
    cs "Well, it's been a long day."
    cs "I guess I should get some rest."
    scene black with dissolve
    jump japan