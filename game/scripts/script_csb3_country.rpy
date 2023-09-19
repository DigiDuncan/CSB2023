label knocked_out:
    scene black
    n "..."
    n "As CS' vision fades back into view, he can also hear a faint heart monitor beeping."
    scene hospital_room with dissolve
    n "CS immediately snaps up."
    if fun_value(40):
        show cs disappointed metal at mid_left with moveinbottom
        cs "Wha--"
        cs "What happened? How long have I been out?"
        cs "And why do I have this eyepatch? My eye feels fine."
    else:
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
    $ engfirst = True
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
    $ swedfirst = True
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
    $ japfirst = True
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

label england_second:
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
    cs "Well, I picked an English-speaking country this time."
    cs "This is quite the breath of fresh air."
    hide cs with moveoutright
    scene black with dissolve
    n "CS walks out of the airport."
    scene embassy with fade
    show cs at center with moveinleft
    show arceus at mid_right with moveinright
    arceus "Hey CS? Is that you?"
    show cs
    cs "Oh my goodness! Why-- How are you here?"
    arceus "I live here with my girlfriend now! What are you doing here?"
    cs "I'm on vacation, and I decided to visit England!"
    arceus "Ah."
    arceus "So uhm..."
    arceus "Do you need a place to stay?"
    arceus "You can come and live with me and Kitty for a while! I'm sure she wouldn't mind."
    cs "I would really appreciate it! Thank you!"
    arceus "Let's get you to our place."
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
    $ ramsay_check = True
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
    scene black with dissolve
    n "Arceus hands CS his phone, and CS fills out an application."
    scene dining_room
    show kitty flipped at right
    show arceus at center
    show cs at left
    with fade
    cs "Annnnddd done!"
    kitty "Do you think you're gonna win this? It's a pretty tough challenge."
    cs "I think I've got something up my sleeve."
    kitty "If you really think so, I guess we'll see if you get in."
    cs "Even though I slept on the plane ride here, I am still really tired."
    cs "I think I'm gonna get some sleep."
    arceus "Is the couch good enough for you? Sorry we don't really have another option right now."
    cs "Yeah, it's all good."
    show cs flipped at left with determination
    hide cs
    hide arceus
    hide kitty
    with moveoutleft
    scene black with dissolve
    n "Everyone gets a good night's sleep."
    n "The next morning..."
    scene kitty_room
    show cs concentrate at left
    with fade
    cs "Zzzzz....."
    cs "Zzzzz....."
    show arceus at center with moveinright
    arceus "Hey. Wake up sleepyhead."
    pause 0.5
    show cs disappointed
    pause 0.5
    show cs concentrate
    pause 0.2
    show cs disappointed
    n "CS slowly gets up."
    cs "Wh- what? It's already morning?"
    arceus "Yep."
    arceus "More importantly, you got accepted into this season of Hell's Kitchen."
    n "CS jerks up."
    show cs
    cs "What really?"
    cs "I mean, of course! I am a master cook, after all."
    arceus "Yeah, yeah. Let's take you there, and we'll see how good you really are."
    show arceus flipped with determination
    hide cs 
    hide arceus
    with moveoutright
    scene black with dissolve
    n "Arc drives CS up to the place for the Hell's Kitchen trial."
    scene car_inside_fg
    show hell_outside behind car_inside_fg
    show arceus flipped at left
    show cs flipped at right
    with fade
    cs "Well, this definitely looks like Hell."
    arceus "I can already feel Ramsay's presence from here. It's terrifying."
    cs "Alright well, are you ready?"
    arceus "What do you mean? You're the one who signed up for this! I'll be waiting for you in the car."
    cs "I thought you wanted to watch me cook?"
    arceus "CS, I'm sorry, but I don't, how do I put this..."
    arceus "Think you'll come out alive?"
    cs "You think I'm gonna die?"
    arceus "No no, I meant that more metaphorically, like, you just aren't a good cook."
    show cs disappointed flipped
    cs "Whhhaaat?"
    arceus "I just haven't seen you prepare like, an actual meal before."
    show cs angry flipped
    cs "Yeah well, you don't know everything about me!"
    cs "I'll show you!"
    scene black with dissolve
    n "CS gets out of the car and walks up toward the building."
    show hell_outside with fade
    show cs angry at mid_left with moveinleft
    cs "Stupid Arceus doesn't think I can cook well, I'm gonna blow them away, that they can't put me on the show because I'm too good!"
    hide cs with moveoutright
    scene black with dissolve
    n "When CS enters the main room, he notices that Gordon is waiting for CS at the stage, with his arms crossed."
    gordon "Are you Mr... 188?"
    cs "Yea, that's m--{w=0.5}{nw}"
    gordon "Yeah, it says here on your application that you are 'The best cook in the world' is that correct sir?"
    gordon "Oh, for fucks sake! What the bloody hell is this?"
    n "Before CS can speak, Gordon takes one good look at CS' clothing."
    gordon "Did you this silly outfit aswell to just fuck with me? Are you serious?"
    cs "What? This is just my normal attire."
    gordon "Normal attire my ass! Are you really here to cook, are we just playing games?"
    cs "No no! I'm really ready to blow you away, Mr. Ramsay!"
    gordon "Well, you better hope your cooking skills can save you from your fashion skills."
    gordon "You've got an hour. Use whatever you can find here to try to make the best dish you can."
    gordon "God..."
    n "Gordon yells under his breath as he stomps off the stage, into the backroom."
    n "CS goes to one of the stations, and starting trying to figure out what to make."
    cs "Arceus was kinda right, I guess Gordon is as scary without the cameras rolling."
    cs "Well, I have a couple options for what I should make."
    menu:
        "Make some Genergy":
            jump good_ramsay
        "Make Phil's cake":
            jump bad_ramsay

label bad_ramsay:
    cs "I guess the only thing I can think of off the top of my head is the cake Phil made for Michael."
    cs "That can't be too hard, right? It's just chocolate cake and Flex Seal, I think."
    cs "Don't know if the Flex Seal adds any taste, but I guess it's worth a try?"
    cs "Alright well, let's do this."
    n "Over the next hour, CS bakes together the Flex Cake."
    gordon "Alright Mr. 188, let's see what you've made!"
    cs "This is my special chocolate cake design! With a secret ingredient."
    gordon "Well well well, doesn't this look fantastic!"
    gordon "Let's see how it tastes!"
    n "Gordon takes a slice and starts eating it."
    gordon "It's very rich and smooth on the outside,"
    gordon "But it tastes weird, on the--{w=0.5}{nw}"
    n "Gordon starts coughing."
    cs "Woah, you okay there?"
    n "Gordon holds his throat and falls over, spits the Flex Seal out, and passes out."
    cs "Ooooooooohhhhh Fuuuuuuucckkk."
    return

label good_ramsay:
    cs "Yeah, you know what? I'm gonna make some Genergy."
    cs "It's my signature beverage! And Michael liked it, I think, and he's British too!"
    cs "It's gotta work!"
    n "CS spends the hour mixing together the perfect concoction for Genergy."
    n "At the 5 minute mark, Gordon comes out and starts shouting."
    gordon "Alright Mr. 188! Chop chop!"
    cs "Alright, I'm almost done!"
    cs "Okay, I am pretty much done, I even managed to get the label on it too."
    cs "I'm gonna add a bit of DaThing's secret SuS, and it's good to go!"
    gordon "Alright, times up!"
    n "Gordon comes over to CS' station."
    gordon "Show me what you made."
    cs "What we have here, is some of my homemade Genergy."
    cs "It's an energy drink that gets the juices moving through you!"
    gordon "Well, that's a new one."
    gordon "I don't think I've ever seen someone make an energy drink on a cooking show..."
    gordon "What do you mean that the juices are gonna move through you? Like is this gonna make me have to go to the bathroom?"
    cs "No, I meant like, energize you."
    gordon "Well yeah, I can see that."
    gordon "Well, here goes nothing."
    n "Gordon gulps down the Genergy."
    n "Gordon sits there for a moment, and smacks his lips."
    gordon "This has, the weirdest flavor ever."
    gordon "I can't even describe it, but..."
    gordon "It's really good, actually."
    gordon "This might be, the best damn thing I've ever tasted."
    gordon "Fuck..."
    n "Gordon turns around walks into the backroom area again."
    cs "Holy shit, I did it!"
    cs "Arceus is gonna be so surpised when he hears the news!"
    cs "Man, I wish he could've seen this."
    n "Gordon comes back with a briefcase, full of cash."
    gordon "Listen, I don't know how you made that, but I'll buy your recipe for £100,000."
    gordon "We won't need to speak of this again."
    cs "Well, shit yeah, I guess I really can't say no to that."
    n "Gordon gives the briefcase to CS."
    gordon "Alright, thank you. Now leave."
    cs "Thanks!"
    scene black with dissolve
    n "CS takes the briefcase and heads back to the car."
    scene car_inside_fg
    show hell_outside behind car_inside_fg
    show arceus flipped at left
    show cs flipped at right
    with fade
    arceus "Well, how'd it go?"
    cs "I think..."
    cs "That you were wrong!"
    show case flipped at center with fade
    n "CS pulls out the briefcase and shows it to Arc."
    arceus "Holy shit! What'd you do??"
    cs "I made him a Genergy, CS style!"
    cs "He apparently loved it so much he bought my recipe!"
    arceus "WHHAATT?"
    arceus "You got Gordon Ramsay, Master Chef, your recipe in one go?"
    show cs happy flipped
    cs "Yep!"
    arceus "Man, your crazy."
    arceus "Whatever, let's head back home."
    scene black with dissolve
    n "CS and Arc head back home."
    n "Once CS and Arc get home, they go inside and discuss the news."
    scene dining_room
    show cs at left
    show arceus at center
    show kitty flipped at right
    kitty "CS did what?"
    arceus "Yeah, I know right? I don't understand either."
    kitty "What is in this Genergy drink of yours?"
    cs "Well, I sold the recipe, so I don't really know anymore."
    kitty "Oh, dang..."
    cs "Just kidding! I still have a back-up, but I'm gonna keep it secret."
    kitty "Ah ok."
    arceus "Well, you did quite a bit already, is there anything else you want to do here?"
    $ achievement_manager.unlock("Master Chef")
    if gear_check and tom_check:
        jump england_done
    elif gear_check:
        menu:
            "Go on adventure with Tom Scott":
                jump scott_zone
    elif tom_check:
        menu:
            "Go on Top Gear":
                jump top_zone
    else:
        menu:
            "Go on Top Gear":
                jump top_zone
            "Go on adventure with Tom Scott":
                jump scott_zone
    
label top_zone:
    $ gear_check = True
    cs "I kinda wanna go on Top Gear."
    kitty "Well now I gotta see that."
    kitty "What are you gonna do to get on the show?"
    cs "I thinking of trying to race one of their cars in my car."
    arceus "You don't have your car with you though..."
    cs "Yeah, but I'm sure they have a spare Honda Civic!"
    arceus "Still, you're crazy to think that you can beat them with that."
    cs "Well, that's the fun part, right?"
    cs "If I win, I'll blow them away!"
    arceus "How do you even get on Top Gear, anyways?"
    kitty "We might be able to just call them."
    cs "If it's that easy, then hell yeah let's do it!"
    n "Kitty calls the members of Top Gear to get CS on the show for a day."
    kitty "Yeah, they said if you can drive over there today, we can start the race!"
    cs "Wow, that was fast."
    cs "Should we get going then?"
    arceus "Sure, I guess. Let's go."
    n "CS, Arc, and Kitty head up to the Top Gear Track."
    n "As they drive up to the track, the gang sees Jermey, Richard, and James."
    kitty "Alright, we'll watch from the side of the track."
    arceus "Good luck CS!"
    cs "Thanks!"
    n "CS gets out of the car and heads up to the Top Gear crew."
    hammond "So, this bloke thinks he can beat us in his typical car?"
    james "Yeah, he really thinks so."
    jermey "Hah! I'd like to see him try!"
    james "Well, you're about to see it."
    cs "Hey guys! CS here!"
    jermey "Hey CS, do you think you can beat Richard in a race, huh?"
    cs "Hell yeah I do!"
    hammond "Well, I wish you the best of luck, buddy."
    n "As he says that, a McLaren rolls up on the track."
    hammond "I'll be racing against you in this McLaren, and if you manage to beat me, we'll give you £10,000!"
    jermey "Our money?"
    james "What if he loses?"
    hammond "Well, obviously, he's gonna lose."
    hammond "If he loses, we'll blow up the car!"
    cs "Well, it's technically not MY car..."
    hammond "Oh really? Take another look..."
    n "CS looks and realizes his license plate matches the Honda Civic on the track."
    cs "WHAT? How did you get my car?"
    jermey "We may have stolen your car and shipped it all the way over to the UK for this race."
    james "I mean, it's YOUR car you wanted to race in, right?"
    cs "Yeah, I guess so..."
    hammond "Well, what are you guys waiting for? Let's do this race!"
    n "CS and hammond get in their cars, and wait for the countdown."
    menu:
        "Lose the race":
            jump top_lose
        "Win the race":
            jump top_win
    
label top_lose:
    n "As the race finishes, the contestants get out of their cars."
    hammond "Well well well!"
    hammond "Looks like I won after all!"
    hammond "As for you..."
    n "Jermey pulls out a remote switch that detonates a bomb under CS' car, turning it into scrap."
    cs "Fuck."
    return

label top_win:
    n "As the race finishes, the contestants get out of their cars."
    hammond "What the bloody hell? How did you beat me?"
    cs "Oh you know. I have my ways."
    james "Well, I guess that means we owe him, right?"
    hammond "Yeah, I guess so."
    hammond "Jermey, can you go remove the bomb from his car?"
    cs "Wait, there was a bomb on the car the whole time?"
    james "Well, kinda."
    cs "What the hell! Now I'm really glad I won!"
    cs "I'm glad I didn't hit anything, otherwise the explosion would've finished me off!"
    hammond "It's just a bomb, it'll buff out if it went off."
    cs "Yeah, I'm sure."
    n "Richard hands CS his money."
    cs "Can you ship my car back as well? You brought it here, after all."
    james "Ah shit, you're right."
    james "We'll send your car back home as soon as possible."
    cs "Thanks."
    cs "Well, I guess I should be going now, I'd like to race again sometime WITHOUT a bomb stuck to the bottom of my car."
    hammond "But that was fun, wasn't it?"
    cs "It was fun before the end!"
    cs "Whatever, I'll see you guys later."
    n "CS heads back to the car."
    kitty "Woo! You won the race!"
    arceus "That was insane man!"
    cs "Yeah, I honestly can't believe it either!"
    cs "They stuck a bomb to the bottom of my car for that race!"
    arceus "What? Why would they do that?"
    arceus "Wasn't that just a backup car they had?"
    cs "No! They managed to steal my real car!"
    cs "They were planning to blow my car up if I lost!"
    kitty "Damn, that's kinda fucked up."
    arceus "Well good thing you won!"
    cs "Yeah, no kidding."
    cs "Let's head home now."
    n "The gang travels back to the house."
    kitty "Well, on the plus side, you won 10,000 pounds!"
    cs "Yeah, I'll have to transfer this to USD when I get back home."
    cs "I hope those cops forgot about me by now."
    arceus "Anyways, is there anything else you want to do here in England?"
    $ achievement_manager.unlock("Bottom Gear")
    if tom_check and ramsay_check:
        jump england_done
    elif ramsay_check:    
        menu:
            "Go on adventure with Tom Scott":
                jump scott_zone
    elif tom_check:
        menu:
            "Go on Hell's Kitchen":
                jump hell_zone
    else:
        menu:
            "Go on adventure with Tom Scott":
                jump scott_zone
            "Go on Hell's Kitchen":
                jump hell_zone

label scott_zone:
    $ tom_check = True
    cs "I wanna see what Tom Scott is up to."
    kitty "Who now?"
    arceus "He's some guy here who explores weird topics on YouTube."
    cs "Yeah, I kinda wanna see if I can go do stuff with him."
    cs "Maybe I can be in his video?"
    kitty "Well first, you'd have to contact him, which I feel like won't work out too well."
    arceus "Or I could find out where he lives."
    cs "Can you do that?"
    arceus "I mean, I CAN."
    arceus "Legally, probably not."
    kitty "Yeah, remember the last time you did something illeg--{w=0.5}{nw}"
    n "Arceus blurts out the address of Tom's house."
    kitty "Arceus! Don't do that!"
    cs "Woohoo! Does that mean we can go there?"
    arceus "Sure, and don't worry Kitty, they won't catch me doing this."
    kitty "You better be right!"
    cs "Alright well, what are we waiting for? Let's go!"
    n "CS and Arc get in the car and head up to Tom Scott's house."
    cs "Are you sure this is his house?"
    arceus "Yep."
    cs "Should we just knock or?"
    arceus "Well, we can't really call him, right?"
    cs "Yeah, I guess so."
    cs "I guess I can knock."
    n "CS goes up to the house and knocks on the door."
    cs "Hello?"
    cs "Anyone home?"
    n "CS waits for a minute."
    cs "Damn, I guess no one's there."
    n "As CS is going back to the car, he notices someone with a red shirt standing in the middle of the road."
    cs "Hey, I wonder if that's him."
    tom "As you can see here, I am standing in the middle of this road."
    tom "That means if I get hit by a car, this video will not be uploaded."
    tom "Anyways, as I was saying..."
    menu:
        "Tell Tom to move":
            jump scott_move
        "Let Tom do his thing":
            jump scott_movent

label scott_move:
    cs "Hey Tom, move out of the way!"
    n "Tom immediately jumps out of the way, as a car zooms past him."
    tom "Oh wow, you saved my life!"
    tom "What's your name?"
    cs "My name is cs188."
    tom "Well thank you cs188 for that, I guess now this video will upload properly now."
    cs "Does this mean I can be in the video?"
    tom "Sure thing cs188, you saved me, after all."
    cs "Yesss!"
    cs "Okay I'm gonna go now, bye!"
    tom "Yep, you too!"
    arceus "Hey, did you get to talk with him?"
    cs "Yeah! I saved him from getting run over!"
    arceus "Woah really? Did you end up in his video?"
    cs "Yeah!"
    arceus "Cool! Were you guys gonna do anything else?"
    cs "Nah, we can head home now."
    arceus "Wait, that's it?"
    arceus "I thought you guys were gonna do more stuff."
    cs "Nah, I just wanted to be in a video with him."
    arceus "Okay, so are we done here?"
    cs "Sure yeah, let's head back home."
    n "Arc and CS drive back to the house."
    kitty "You saved a man's life?"
    cs "Yeah, and I get to be in his video!"
    kitty "Well, looks like you got 2 for 1 then!"
    kitty "Is there anything is you want to do?"
    $ achievement_manager.unlock("The Man In The Red Shirt")
    if gear_check and ramsay_check:
        jump england_done
    elif ramsay_check:    
        menu:
            "Go on Top Gear":
                jump top_zone
    elif gear_check:
        menu:
            "Go on Hell's Kitchen":
                jump hell_zone
    else:
        menu:
            "Go on Hell's Kitchen":
                jump hell_zone
            "Go on Top Gear":
                jump top_zone

label england_done:
    cs "Well, I think that's everything I wanted to do here."
    arceus "Oh nice!"
    kitty "So, are you leaving now? You managed to do so much in so little time!"
    cs "Yeah, I think I'm gonna go visit another country."
    arceus "Oh really? Where do you think you wanna go?"
    menu:
        "Sweden":
            jump england_sweden
        "Japan":
            jump england_japan

label scott_movent:
    cs "I should wait till he's done with his video."
    tom "So yeah, we're just gonna keep talking about this road in particular."
    tom "This road here was created in 1968, by OHP--{w=0.5}{nw}"
    n "A speeding car rams into Tom, and he flies off into the distance."
    cs "Uh oh. {w=3.5} I didn't see nothin'."
    return

label england_japan:
    cs "I was thinking of going to Japan."
    kitty "That sounds pretty cool!"
    arceus "Is there anywhere you wanna go in particular in Japan?"
    cs "I don't really know where to go there, I guess I'll have to see when I get there."
    arceus "Well you have to get the Domino's Hatsune Miku Pizza."
    kitty "Or sing some Japanese Karaoke!"
    cs "Yeah well, I'll have to let you guys know how I'm doing after the trip."
    arceus "Welp, should we take you back to the airport?"
    cs "Sure, let's go."
    n "Arceus takes CS back to the airport."
    cs "Well, thank you so much Arceus for everything, really."
    arceus "It's all good man, I loved having you here."
    arceus "It's also impressive that you made so much money in the short amount of time you were here, you'll probably be set for Japan!"
    cs "Yeah, I honestly don't know how I managed to most of those things, I was kinda winging it."
    cs "Welp, it looks like my plane is here."
    cs "See ya Arceus!"
    arceus "See you later CS!"
    n "CS grabs his ticket and heads on the next plane."
    cs "Man, I'm kinda nervous to go to Japan, actually."
    cs "It's going to be wildly different than anything I've seen before."
    cs "Oh well, I'm sure it'll be fun."
    cs "Time to get some sleep."
    jump japan

label japan:
    n "As CS wakes up, he sees the plane landing outside."
    cs "Wow, I really slept a lot, or that was a crazy fast trip."
    cs "Welp, time to check out Japan!"
    n "CS exits the terminal and enters the airport."
    cs "Wow, this place is already pretty crazy!"
    