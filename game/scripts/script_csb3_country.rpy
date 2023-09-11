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
    n "CS takes a minute to catch his breath."
    cs "I'm almost there!"
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
    n "CS almost loses his breath sprinting."
    cs "I'm almost there!"
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


label england:
    scene black
    pause 1.0
    scene airplane_seats
    show cs at left
    with fade
    n "As CS slowly wakes up, he sees the plane landing on the tarmac."
    cs "Oh huh, we are already here."
    cs "Either that was a fast trip, or I slept WAYYYYY too long."
    cs "Welp, I guess this is where I get off."
    hide cs with moveoutright
    scene black with dissolve
    n "CS gets out of the plane, and makes his way into the airport."
    scene britport with fade
    show cs at mid_left with moveinleft
    cs "Well, at least I picked an English-speaking country."
    cs "Could you imagine if I picked something like, Sweden? Or Japan?"
    cs "Either way, this is quite the breath of fresh air."
    cs "Don't have to run from the law anymore, so that's a plus."
    hide cs with moveoutright
    scene black with dissolve
    n "CS walks out of the airport."
    scene embassy with fade
    show cs at center with moveinleft
    show cs disappointed
    cs "Bad thing this, I don't have any money!"
    cs "So I don't really know what to do now."
    cs "I guess I'll have to start asking random people for a job..."
    hide cs with moveoutright
    jump england_first

label england_first:
    scene uk_street with fade
    show cs disappointed at mid_left with moveinleft
    n "CS walks up to a shop owner on the side of the street."
    cs "Hello? Are you guys hiring?"
    "Shopkeep" "Get lost, you bloody wanker!"
    cs "Damn, sorry."
    cs "Man, this kinda sucks!"
    show arceus at mid_right with moveinright
    arceus "Hey CS? Is that you?"
    show cs
    cs "Oh my goodness! Why-- How are you here?"
    arceus "I live here with my girlfriend now! What are you doing here?"
    cs "I, used the last of my money to buy a plane ticket."
    arceus "Ah."
    arceus "Assuming you did that to get away from the cops?"
    cs "Yeah..."
    arceus "I heard about your fight, but I couldn't engage too much, since the ambulance took you away shortly after I showed up."
    arceus "So I decided to finally move up here, since I got out of prison and all."
    cs "That makes sense."
    arceus "So uhm..."
    arceus "Do you need a place to stay? You said you were out of money."
    arceus "You can come and live with me and Kitty for a while! I'm sure she wouldn't mind."
    cs "I would really appreciate it! Thank you!"
    cs "I'll do whatever I can to pay you back in advance."
    arceus "Nah, don't worry about it. You helped break me out of prison!"
    n "the shopkeeper looks at them weirdly."
    arceus "In GTA V."
    cs "Yeah yeah, that heist was really fun."
    arceus "Anyways, let's get you to our place."
    show arceus flipped with determination
    hide cs
    hide arceus
    with moveoutright
    show black with dissolve
    n "Arceus and CS jump on a double decker and heads down to their house."
    jump arceus_place

label arceus_place:
    pause 1.0
    scene kitty_house with fade
    show arceus flipped at center with moveinleft
    show cs at left with moveinleft
    arceus "Here we are. Home sweet home."
    cs "This is a house? It looks like the size of an apartment."
    arceus "CS, remember we're in the UK?"
    cs "Ohhhh, yeah. Forgot about that."
    arceus "Whatever just, come on in."
    scene kitty_room with fade
    show arceus flipped at center with moveinleft
    show cs at left with moveinleft
    cs "You guys have quite a quiant little place!"
    show arceus
    arceus "Yep. This is what 5 quid gets you here."
    cs "Woah, what? How much is a quid?"
    arceus "I'm just messing, it's a little more than a US dollar."
    show kitty flipped at right with moveinright
    show arceus flipped
    kitty "Hey Arceus! You're home!"
    kitty "Hey, who's this man?"
    arceus "This is CS, my jail bud- I mean my friend! You remember that guy who made the YTPs?"
    kitty "Oh, yeah. Isn't he kinda famous?"
    cs "I wouldn't say that..."
    arceus "He's broke right now, and I was wondering if he could stay here for a bit."
    kitty "I guess that's fine, how long is he gonna stay here though?"
    cs "It shouldn't be too long, I'm gonna try to find a way to get some money."
    arceus "Why don't we all eat and talk about it?"
    cs "That would be great. I'm starving."
    show kitty with determination
    hide arceus
    hide kitty
    hide cs
    with moveoutright
    scene black with dissolve
    n "Kitty and Arceus prepare dinner, and they all sit down at the dining table and eat."
    scene dining_room
    show kitty flipped at right
    show arceus at center
    show cs at left
    with fade
    cs "So, how long have you guys been together?"
    arceus "For a long time actually, I've been wanting to move up here, but y'know..."
    kitty "Yeah, you did a dumb and got arrested!"
    arceus "Yeah yeah, well anyways..."
    arceus "What do you want to do here, CS? It's a brand new country, there are a ton of things you can do..."
    menu:
        "Go on Hell's Kitchen":
            jump hell_zone
        "Go on Top Gear":
            jump top_zone
        "Go on adventure with Tom Scott":
            jump scott_zone

label hell_zone:
    cs "I wanna go on Hell's Kitchen!"
    arceus "Wat."
    cs "Yeah! I can go on the show and cook up some crazy meal and win!"
    arceus "CS, you realize who the man is who runs Hell's Kitchen?"
    cs "Yeah, it's Gordon Ramsay! I love that guy."
    arceus "Yeah, and he's kinda scary."
    cs "Yeah, but that's just because it's a show."
    cs "I'm sure he's like, really funny."
    arceus "Besides, how are you going to get on the show?"
    arceus "Don't you have to submit an application?"
    cs "I mean, fuck it. I'll do it."
    arceus "Oookayy..."
    n "Arceus hands CS his phone, and CS fills out an application."
    cs "Annnnddd done!"
    kitty "Do you think you're gonna win this? It's a pretty tough challenge."
    cs "I think I've got something up my sleeve."
    kitty "If really think so, I guess we'll see if you get in."
    cs "Even though I slept on the plane ride here, I am still really tired."
    cs "I think I'm gonna get some sleep."
    arceus "Is the couch good enough for you? Sorry we don't really have another option right now."
    cs "Yeah, it's all good."
    n "Everyone gets a good night's sleep."
    n "The next morning..."
    cs "Zzzzz....."
    cs "Zzzzz....."
    arceus "Hey. Wake up sleepyhead."
    n "CS slowly gets up."
    cs "Wh- what? It's already morning?"
    arceus "Yep."
    arceus "More importantly, you got accepted into this season of Hell's Kitchen."
    n "CS jerks up."
    cs "What really?"
    cs "I mean, of course! I am a master cook, after all."
    arceus "Yeah, yeah. Let's take you there, and we'll see how good you really are."
    n "Arc drives CS up to the place for the Hell's Kitchen trial."
    