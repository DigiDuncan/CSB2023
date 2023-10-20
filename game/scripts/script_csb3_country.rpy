label england_menu:
    # "Go on Hell's Kitchen":
    #     jump hell_zone
    # "Go on Top Gear":
    #     jump top_zone
    # "Go on an adventure with Tom Scott":
    #     jump scott_zone
    python:
        locations = []
        if not ramsay_check:
            locations.append(("Go On Hell's Kitchen", "hell_zone"))
        if not gear_check:
            locations.append(("Go on Top Gear", "top_zone"))
        if not tom_check:
            locations.append(("Go on an adventure with Tom Scott", "scott_zone"))
        if not locations:
            locations.append(("I've done everything", "england_done"))
        label_jump = renpy.display_menu(locations)
        renpy.jump(label_jump)

label japan_menu:
    # "Go on an anime adventure":
    #     jump anime_adventure
    # "Go sing some karaoke":
    #     jump karaoke
    # "Have some fun with Miku":
    #     jump miku_pizza
    python:
        locations = []
        if not anime_check:
            locations.append(("Go on an anime adventure", "anime_adventure"))
        if not karaoke_check:
            locations.append(("Go sing some karaoke", "karaoke"))
        if not miku_check:
            locations.append(("Have some fun with Miku", "miku_pizza"))
        if not locations:
            locations.append(("I've done everything", "japan_leave"))
        label_jump = renpy.display_menu(locations)
        renpy.jump(label_jump)

label knocked_out:
    scene black
    play sound "<loop 0>heartbeat.mp3" volume 1
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
        show cs disappointed metal4 at mid_left with moveinbottom
        cs "Wha--"
        cs "What happened? How long have I been out?"
    show cs disappointed metal3
    cs "Thank god I didn't catch some virus from a global pandemic or something."
    stop sound
    cs "I guess that's the last time I try to do something for LTT."
    n "CS sits there for a minute, trying to recollect his memory."
    cs "So I went to go work at LTT, after I..."
    cs "What did I do before that?"
    n "The news starts playing on the TV in CS' room, explaining how 3 criminals broke out of prison a couple days ago."
    show cs disappointed metal4
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
    benrey "Hey, do you have your Pass{w=0.5} Port?"
    show cs worried
    cs "Oh shiiiiiiiiiiiiiiiiiit."
    benrey "You can't get on the plane without your Pass{w=0.5} Port."
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
    benrey "Well I'm sorry, but everyone has a Pass{w=0.5} Port!"
    benrey "Try checking your pocket."
    n "CS puts his hand in his pocket and pulls out a Canadian passport."
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
    benrey "But everyone has a Pass{w=0.5} Port!"
    benrey "Try checking your back pocket."
    n "CS puts his hand in his back pocket and pulls out a Canadian passport."
    show cs
    cs "Oh, didn't know I had this!"
    benrey "See? I told you! Everyone has a Pass{w=0.5} Port! Now let's get you your ticket."
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
    benrey "Well I'm sorry, but everyone's got a Pass{w=0.5} Port!"
    benrey "Try checking your left shoe."
    n "CS takes off his left shoe and pulls out a Canadian passport."
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
    $ england_check = True
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
    play music "<loop 0>stal.mp3" volume 0.4
    arceus "Hey CS? Is that you?"
    show cs
    cs "Oh my goodness! Why-- How are you here?"
    show arceus happy
    arceus "I live here with my girlfriend now! What are you doing here?"
    show arceus
    cs "I, used the last of my money to buy a plane ticket."
    arceus "Ah."
    arceus "Assuming you did that to get away from the cops?"
    cs "Yeah..."
    show arceus worried
    arceus "I heard about your fight, but I couldn't engage too much, since the ambulance took you away shortly after I showed up."
    show arceus happy
    arceus "So I decided to finally move up here, since I got out of prison and all."
    show arceus
    cs "That makes sense."
    arceus "So uhm..."
    arceus "Do you need a place to stay? You said you were out of money."
    show arceus happy
    arceus "You can come and live with me and Kitty for a while! I'm sure she wouldn't mind."
    show arceus
    show cs happy
    cs "I would really appreciate it! Thank you!"
    show cs
    cs "I'll do whatever I can to pay you back."
    arceus "Nah, don't worry about it. You helped break me out of prison!"
    n "The shopkeeper looks at them weirdly."
    arceus "In GTA V."
    cs "Yeah yeah, that heist was really fun."
    arceus "Anyways, let's get you to our place."
    stop music fadeout 3.0
    show arceus flipped with determination
    hide cs
    hide arceus
    with moveoutright
    show black with dissolve
    n "Arceus and CS jump on a double decker and head down to their house."
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
    cs "It's a bit of fresh air again to understand most people once again."
    cs "I honestly forgot why I am on this big vacation, but it's been fun so far!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS walks out of the airport."
    scene embassy with fade
    show cs at center with moveinleft
    show arceus at mid_right with moveinright
    play music "<loop 0>stal.mp3" volume 0.4
    arceus "Hey CS? Is that you?"
    show cs
    cs "Oh my goodness! Why-- How are you here?"
    show arceus happy
    arceus "I live here with my girlfriend now! What are you doing here?"
    show arceus
    cs "I'm on vacation, and I decided to visit England!"
    arceus "Ah."
    arceus "So uhm..."
    arceus "Do you need a place to stay?"
    cs "I guess so, I have some money but I don't know what hotels are like here."
    show arceus happy
    arceus "You could come and live with me and Kitty for a while! I'm sure she wouldn't mind."
    show cs happy
    cs "I would really appreciate it! Thank you!"
    show cs
    show arceus
    arceus "Let's get you to our place."
    stop music fadeout 3.0
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
    show arceus angry flipped
    arceus "CS, remember we're in the UK?"
    show arceus flipped
    cs "Ohhhh, yeah. Forgot about that."
    arceus "Whatever, just, come on in."
    scene kitty_room with fade
    show arceus flipped at center with moveinleft
    show cs at left with moveinleft
    play music "<loop 0>wool_gloves.mp3" volume 0.4
    music Wool Gloves - Various Artists
    cs "You guys have quite a quaint little place!"
    show arceus
    arceus "Yep. This is what five quid gets you here."
    cs "Woah, what? How much is a quid?"
    show arceus happy
    arceus "I'm just messing, it's a little more than a US dollar."
    show arceus
    show kitty flipped at right with moveinright
    $ persistent.seen.add("round")
    show arceus flipped
    kitty "Hey Arcie! You're home!"
    kitty "Hey, who's this man?"
    arceus "This is CS, my jail bud- I mean my friend! You remember that guy who made the YTPs?"
    kitty "Oh, yeah. Isn't he kinda famous?"
    cs "I wouldn't say that..."
    if japan_check:
        arceus "He's deciding to visit England, so I wanted to invite him to stay here."
        arceus "Is that okay?"
        kitty "Yeah but, how long will he be here for?"
        cs "Not too long I don't think, I just like this country and wanted to take a vacation here."
        show arceus happy flipped
        arceus "Well, let's make some dinner, and we can find fun things here to do!"
        cs "Sure thing!"
    else:
        arceus "He's broke right now, and I was wondering if he could stay here for a bit."
        kitty "I guess that's fine, how long is he gonna stay here though?"
        cs "It shouldn't be too long, I'm gonna try to find a way to get some money."
        show arceus happy flipped
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
    show arceus worried
    arceus "Yeah yeah, well anyways..."
    show arceus
    arceus "What do you want to do here, CS? It's a brand new country, there are a ton of things you can do..."
    jump england_menu

label hell_zone:
    $ ramsay_check = True
    cs "I wanna go on Hell's Kitchen!"
    show arceus worried
    arceus "Wat."
    cs "Yeah! I can go on the show and cook up some crazy meal and win!"
    arceus "CS, you realize who the man is who runs Hell's Kitchen?"
    cs "Yeah, it's Gordon Ramsay! I love that guy."
    arceus "Yeah, and he's kinda scary."
    cs "Yeah, but that's just because it's a show."
    cs "I'm sure he's like, really funny."
    show arceus
    arceus "Besides, how are you going to get on the show?"
    arceus "Don't you have to submit an application?"
    cs "I mean, fuck it. I'll do it."
    show arceus worried
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
    stop music fadeout 3.0
    music end
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
    show arceus angry
    cs "I mean, of course! I am a master cook, after all."
    show arceus
    arceus "Yeah, yeah. Let's take you there, and we'll see how good you really are."
    show arceus flipped with determination
    hide cs 
    hide arceus
    with moveoutright
    scene black with dissolve
    n "Arc drives CS up to the place for the Hell's Kitchen trial."
    scene car_insidearc_fg flipped
    show hell_outside behind car_insidearc_fg
    show arceus at right
    show cs at left
    with fade
    play music "<loop 0>conflict.mp3" volume 0.4
    music Conflict - David Vanacore
    cs "Well, this definitely looks like Hell."
    show arceus worried
    arceus "I can already feel Ramsay's presence from here. It's terrifying."
    cs "Alright well, are you ready?"
    show arceus angry
    arceus "What do you mean? You're the one who signed up for this! I'll be waiting for you in the car."
    cs "I thought you wanted to watch me cook?"
    show arceus worried
    arceus "CS, I'm sorry, but I don't, how do I put this..."
    arceus "Think you'll come out alive?"
    cs "You think I'm gonna die?"
    show arceus
    arceus "No no, I meant that more metaphorically, like, you just aren't a good cook."
    show cs disappointed
    cs "Whhhaaat?"
    arceus "I just haven't seen you prepare like, an actual meal before."
    show cs angry
    cs "Yeah well, you don't know everything about me!"
    cs "I'll show you!"
    scene black with dissolve
    n "CS gets out of the car and walks up toward the building."
    scene hell_outside with fade
    show cs angry at mid_left with moveinleft
    cs "Stupid Arceus doesn't think I can cook? Well, I'm gonna blow them away! They won't be able to even put me on the show because I'll be {i}too{/i} good!"
    hide cs with moveoutright
    scene black with dissolve
    n "When CS enters the main room, he notices that Gordon is waiting for CS at the kitchen, with his arms crossed."
    scene hell_kitchen
    show gordon at left
    with fade
    show cs flipped at right with moveinright
    gordon "Are you Mr... 188?"
    cs "Yea, that's m--{w=0.5}{nw}"
    gordon "Yeah, it says here on your application that you are 'The best cook in the world' is that correct sir?"
    gordon "Oh, for fucks sake! What the bloody hell is this?"
    show cs disappointed flipped
    n "Before CS can speak, Gordon takes one good look at CS' clothing."
    play sound "waterphone.mp3"
    gordon "Did you wear this silly outfit as well to just fuck with me? Are you serious?"
    cs "What? This is just my normal attire."
    scene talking_head
    show cs disappointed
    with dissolve
    cs "I despise it when people bring up my clothes."
    cs "What's wrong with this anyways? It's perfectly normal!"
    scene hell_kitchen
    show cs disappointed flipped at right
    show gordon at left
    with fade
    gordon "Normal attire my arse! Are you really here to cook, or are we just playing games?"
    show cs worried flipped
    cs "No no! I'm really ready to blow you away, Mr. Ramsay!"
    gordon "Well, you better hope your cooking skills can save you from your fashion sense."
    gordon "You've got an hour. Use whatever you can find here to try to make the best dish you can."
    gordon "God..."
    hide gordon with moveoutleft
    show cs disappointed flipped at center with move
    n "Gordon yells under his breath as he stomps out of the kitchen, into the backroom."
    stop music fadeout 3.0
    music end    
    n "CS goes to one of the stations, and starting trying to figure out what to make."
    scene talking_head
    show cs disappointed
    with dissolve
    cs "Arceus was kinda right, I guess Gordon is as scary without the cameras rolling."
    scene hell_kitchen
    show cs disappointed flipped
    with fade
    cs "Well, I have a couple options for what I should make."
    jump gordon_menu

label gordon_menu:
    scene hell_kitchen
    show cs disappointed flipped
    menu:
        "Make some Genergy":
            jump good_ramsay
        "Make Phil's cake":
            jump bad_ramsay

label bad_ramsay:
    stop music fadeout 3.0
    scene hell_kitchen
    show cs flipped
    cs "I guess the only thing I can think of off the top of my head is the cake Phil made for Michael."
    cs "That can't be too hard, right? It's just chocolate cake and Flex Seal, I think."
    cs "Don't know if the Flex Seal adds any taste, but I guess it's worth a try?"
    cs "Alright well, let's do this."
    scene black with dissolve
    n "Over the next hour, CS bakes together the Flex Cake."
    scene hell_kitchen
    show cs flipped at right
    show gordon at left
    with fade
    play music "<loop 0>tumultuous.mp3" volume 0.4
    music Tumultuous - David Vanacore
    gordon "Alright Mr. 188, let's see what you've made!"
    cs "This is my special chocolate cake design! With a secret ingredient."
    gordon "Well well well, doesn't this look fantastic!"
    gordon "Let's see how it tastes!"
    n "Gordon takes a slice and starts eating it."
    gordon "It's very rich and smooth on the outside,"
    gordon "But it tastes weird, on the--{w=0.5}{nw}"
    n "Gordon starts coughing."
    show cs disappointed flipped
    cs "Woah, you okay there?"
    n "Gordon holds his throat and falls over, spits the Flex Seal out, and passes out."
    play sound "waterphone.mp3"
    hide gordon with moveoutbottom
    show cs disappointed flipped with hpunch
    cs "Ooooooooohhhhh Fuuuuuuucckkk."
    bad_end "Master Chef?\nMore like, Master Death!" "gordon_menu"

label good_ramsay:
    show cs flipped
    cs "Yeah, you know what? I'm gonna make some Genergy."
    cs "It's my signature beverage! And Michael liked it, I think, and he's British too!"
    cs "It's gotta work!"
    scene black with dissolve
    n "CS spends the hour mixing together the perfect concoction for Genergy."
    n "At the five minute mark, Gordon comes out and starts shouting."
    scene hell_kitchen
    show cs flipped
    with fade
    play music "<loop 0>tumultuous.mp3" volume 0.4
    music Tumultuous - David Vanacore
    show gordon at left with moveinleft
    gordon "Alright Mr. 188! Chop chop!"
    cs "Alright, I'm almost done!"
    hide gordon with moveoutleft
    cs "Okay, I am pretty much done, I even managed to get the label on it too."
    cs "I'm gonna add a bit of DaThings' secret SuS, and it's good to go!"
    show cs flipped at right with move
    gordon "Alright, time's up!"
    n "Gordon comes over to CS' station."
    show gordon at left with moveinleft
    gordon "Show me what you made."
    cs "What we have here, is some of my homemade Genergy."
    show cs happy flipped
    cs "It's an energy drink that gets the juices moving through you!"
    show cs flipped
    gordon "Well, that's a new one."
    gordon "I don't think I've ever seen someone make an energy drink on a cooking show..."
    play sound "waterphone.mp3"
    gordon "What do you mean that the juices are gonna move through you? Like is this gonna make me have to go to the bathroom?"
    show cs disappointed flipped
    cs "No, I meant like, energize you."
    scene talking_head
    show cs disappointed
    with dissolve
    cs "This man is terrifying, I can never tell if he's in a good mood or not."
    scene hell_kitchen
    show cs disappointed flipped at right
    show gordon at left
    with fade
    gordon "Well yeah, I can see that."
    gordon "Well, here goes nothing."
    n "Gordon gulps down the Genergy."
    n "Gordon sits there for a moment, and smacks his lips."
    gordon "This has, the weirdest flavor ever."
    gordon "I can't even describe it, but..."
    show cs flipped
    gordon "It's really good, actually."
    gordon "This might be, the best damn thing I've ever tasted."
    gordon "Fuck..."
    hide gordon with moveoutleft
    n "Gordon turns around walks into the backroom area again."
    stop music fadeout 3.0
    music end 
    show cs happy flipped
    cs "Holy shit, I did it!"
    cs "Arceus is gonna be so surprised when he hears the news!"
    show cs flipped
    cs "Man, I wish he could've seen this."
    n "Gordon comes back with a briefcase, full of cash."
    show gordon at center
    show case at mid_mid_right
    with moveinleft
    gordon "Listen, I don't know how you made that, but I'll buy your recipe for £100,000."
    gordon "We won't need to speak of this again."
    cs "Well, shit yeah, I guess I really can't say no to that."
    n "Gordon gives the briefcase to CS."
    show case at mid_right_right with move
    gordon "Alright, thank you. Now leave."
    cs "Thanks!"
    scene black with dissolve
    n "CS takes the briefcase and heads back to the car."
    scene car_insidearc_fg flipped
    show hell_outside behind car_insidearc_fg
    show arceus at right
    show cs at left
    with fade
    arceus "Well, how'd it go?"
    cs "I think..."
    cs "That you were wrong!"
    show case at center with moveinbottom
    n "CS pulls out the briefcase and shows it to Arc."
    show arceus worried
    arceus "Holy shit! What'd you do??"
    cs "I made him a Genergy, CS style!"
    cs "He apparently loved it so much he bought my recipe!"
    arceus "WHHAATT?"
    arceus "You got Gordon Ramsay, Master Chef, to buy your recipe in one go?"
    show cs happy
    cs "Yep!"
    show arceus angry
    arceus "Man, you're crazy."
    show arceus
    arceus "Whatever, let's head back home."
    scene black with dissolve
    n "CS and Arc head back home."
    n "Once CS and Arc get home, they go inside and discuss the news."
    scene dining_room
    show cs at left
    show arceus at center
    show kitty flipped at right
    with fade
    play music "<loop 0>wool_gloves.mp3" volume 0.4
    kitty "CS did what?"
    arceus "Yeah, I know right? I don't understand either."
    kitty "What is in this Genergy drink of yours?"
    cs "Well, I sold the recipe, so I don't really know anymore."
    kitty "Well, shit..."
    cs "Just kidding! I still have a backup, but I'm gonna keep it secret."
    kitty "Ah, ok."
    arceus "Well, you did quite a bit already, is there anything else you want to do here?"
    $ achievement_manager.unlock("Master Chef")
    jump england_menu
    
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
    cs "If it's that easy, then hell yeah, let's do it!"
    scene black with dissolve
    n "Kitty calls the members of Top Gear, after a brief panic attack, to get CS on the show for a day."
    scene dining_room
    show cs at left
    show arceus at center
    show kitty flipped at right
    with fade
    kitty "Yeah, they said if you can drive over there today, we can start the race!"
    cs "Wow, that was fast."
    cs "Should we get going then?"
    arceus "Sure, I guess. Let's go."
    stop music fadeout 3.0
    show black with dissolve
    n "CS, Arc, and Kitty head up to the Top Gear Track."
    scene car_insidearc_fg flipped
    show top_gear_track behind car_insidearc_fg
    show arceus at right
    show kitty at left
    with fade
    play music "<loop 0>lisbon_fever.mp3" volume 0.4
    music Lisbon Fever - Dr. Awesome
    n "As they drive up to the track, the gang sees Jeremy, Richard, and James."
    kitty "Alright, we'll watch from the side of the track."
    show arceus happy
    arceus "Good luck, CS!"
    show arceus
    cs "Thanks!"
    n "CS gets out of the car and heads up to the Top Gear crew."
    scene top_gear_track
    show james at right
    show jeremy at mid_right
    show hammond at center
    with fade
    hammond "So, this bloke thinks he can beat us in his typical car?"
    james "Yeah, he really thinks so."
    jeremy "Hah! I'd like to see him try!"
    james "Well, you're about to see it."
    show cs at left with moveinleft
    cs "Hey guys! CS here!"
    jeremy "Hey CS, so you think you can beat Richard in a race, huh?"
    show cs happy
    cs "Hell yeah I do!"
    show cs
    hammond "Well, I wish you the best of luck, buddy."
    n "As he says that, a McLaren rolls up on the track."
    hammond "I'll be racing against you in this McLaren, and if you manage to beat me, we'll give you £10,000!"
    jeremy "Our money?"
    james "What if he loses?"
    hammond "Well, obviously, he's gonna lose."
    hammond "If he loses, we'll blow up the car!"
    cs "Well, it's technically not MY car..."
    hammond "Oh really? Take another look..."
    n "CS looks and realizes his license plate matches the Honda Civic on the track."
    show cs worried
    cs "WHAT? How did you get my car?"
    jeremy "We may have stolen your car and shipped it all the way over to the UK for this race."
    james "I mean, it's YOUR car you wanted to race in, right?"
    show cs disappointed
    cs "Yeah, I guess so..."
    hammond "Well, what are you guys waiting for? Let's do this race!"
    scene black with dissolve
    n "CS and Richard get in their cars, and wait for the countdown."
    jump top_gear_menu
label top_gear_menu:
    scene black
    menu:
        "Lose the race":
            jump top_lose
        "Win the race":
            jump top_win
    
label top_lose:
    stop music fadeout 3.0
    music end    
    n "As the race finishes, the contestants get out of their cars."
    scene top_gear_track
    show james at right
    show jeremy at mid_right
    show hammond at center
    show cs disappointed at left
    with fade
    hammond "Well well well!"
    hammond "Looks like I won after all!"
    hammond "As for you..."
    n "Jeremy pulls out a remote switch that detonates a bomb under CS' car, turning it into scrap."
    cs "Fuck."
    bad_end "You want it all,\nbut the world won't give it up!" "top_gear_menu"

label top_win:
    stop music fadeout 3.0
    music end    
    n "As the race finishes, the contestants get out of their cars."
    scene top_gear_track
    show james at right
    show jeremy at mid_right
    show hammond at center
    show cs happy at left
    with fade
    hammond "What the bloody hell? How did you beat me?"
    cs "Oh you know. I have my ways."
    james "Well, I guess that means we owe him, right?"
    hammond "Yeah, I guess so."
    hammond "Jeremy, can you go remove the bomb from his car?"
    show cs worried
    cs "Wait, there was a bomb on the car the whole time?"
    james "Well, kinda."
    show cs angry
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
    show cs angry flipped with determination
    hide cs with moveoutleft
    scene car_insidearc_fg flipped
    show top_gear_track behind car_insidearc_fg
    show arceus at right
    show kitty at left
    with fade    
    play music "<loop 0>wool_gloves.mp3" volume 0.4
    kitty "Woo! You won the race!"
    show arceus happy
    arceus "That was insane, man!"
    cs "Yeah, I honestly can't believe it either!"
    cs "They stuck a bomb to the bottom of my car for that race!"
    show arceus worried
    arceus "What? Why would they do that?"
    arceus "Wasn't that just a backup car they had?"
    show arceus
    cs "No! They managed to steal my real car!"
    cs "They were planning to blow my car up if I lost!"
    kitty "Damn, that's kinda fucked up."
    show arceus happy
    arceus "Well good thing you won!"
    show arceus
    cs "Yeah, no kidding."
    cs "Let's head home now."
    scene black with dissolve
    n "The gang travels back to the house."
    scene dining_room
    show cs at left
    show arceus at center
    show kitty flipped at right
    with fade
    kitty "Well, on the plus side, you won 10,000 pounds!"
    cs "Yeah, I'll have to transfer this to USD when I get back home."
    cs "I hope those cops forgot about me by now."
    arceus "Anyways, is there anything else you want to do here in England?"
    $ achievement_manager.unlock("Bottom Gear")
    jump england_menu

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
    show arceus happy
    n "Arceus blurts out the address of Tom's house."
    show arceus
    kitty "Arcie! Don't do that!"
    show cs happy
    cs "Woohoo! Does that mean we can go there?"
    arceus "Sure, and don't worry Kitty, they won't catch me doing this."
    kitty "You better be right!"
    show cs
    cs "Alright well, what are we waiting for? Let's go!"
    stop music fadeout 3.0
    scene black with dissolve
    n "CS and Arc get in the car and head up to Tom Scott's house."
    scene tom_house with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    cs "Are you sure this is his house?"
    arceus "Yep."
    cs "Should we just knock or?"
    arceus "Well, we can't really call him, right?"
    cs "Yeah, I guess so."
    cs "I guess I can knock."
    scene black with dissolve
    n "CS goes up to the house and knocks on the door."
    cs "Hello?"
    cs "Anyone home?"
    n "CS waits for a minute."
    cs "Damn, I guess no one's there."
    scene tom_house
    show cs at left
    show arceus at right
    with fade
    n "As CS is going back to the car, he notices someone with a red shirt standing in the middle of the road."
    cs "Hey, I wonder if that's him."
    hide cs with moveoutright
    scene tom_road
    show tom
    with fade
    tom "As you can see here, I am standing in the middle of this road."
    tom "That means if I get hit by a car, this video will not be uploaded."
    tom "Anyways, as I was saying..."
    jump scott_menu
label scott_menu:
    scene tom_road
    show tom
    menu:
        "Tell Tom to move":
            jump scott_move
        "Let Tom do his thing":
            jump scott_movent

label scott_move:
    show cs flipped at offscreenright
    cs "Hey Tom, move out of the way!"
    show tom at right with move
    show car at lego_run behind tom
    with move
    n "Tom immediately jumps out of the way, as a car zooms past him."
    show tom at center
    show cs flipped at right
    with move
    tom "Oh wow, you saved my life!"
    tom "What's your name?"
    cs "My name is cs188."
    tom "Well thank you cs188 for that, I guess now this video will upload properly now."
    cs "Does this mean I can be in the video?"
    tom "Sure thing cs188, you saved me, after all."
    show cs happy flipped
    cs "Yesss!"
    cs "Okay I'm gonna go now, bye!"
    tom "Bye to you too!"
    show cs happy with determination
    hide cs with moveoutright
    scene tom_house
    show arceus at right
    with fade
    show cs happy at left with moveinleft
    arceus "Hey, did you get to talk with him?"
    cs "Yeah! I saved him from getting run over!"
    arceus "Woah really? Did you end up in his video?"
    cs "Yeah!"
    arceus "Cool! Were you guys gonna do anything else?"
    show cs
    cs "Nah, we can head home now."
    show arceus worried
    arceus "Wait, that's it?"
    arceus "I thought you guys were gonna do more stuff."
    cs "Nah, I just wanted to be in a video with him."
    arceus "Okay, so are we done here?"
    show arceus
    cs "Sure yeah, let's head back home."
    scene black with dissolve
    n "Arc and CS drive back to the house."
    scene dining_room
    show cs at left
    show arceus at center
    show kitty flipped at right
    with fade
    play music "<loop 0>wool_gloves.mp3" volume 0.4
    kitty "You saved a man's life?"
    cs "Yeah, and I get to be in his video!"
    kitty "Well, looks like you got 2 for 1 then!"
    kitty "Is there anything else you want to do?"
    $ achievement_manager.unlock("The Man In The Red Shirt")
    jump england_menu

label england_done:
    cs "Well, I think that's everything I wanted to do here."
    show arceus happy
    arceus "Oh nice!"
    show arceus
    kitty "So, are you leaving now? You managed to do so much in so little time!"
    cs "Yeah, I think I'm gonna go visit another country."
    arceus "Oh really? Where do you think you wanna go?"
    if (not japan_check) and (not sweden_check):
        menu:
            "Sweden":
                jump england_sweden
            "Japan":
                jump england_japan
    elif sweden_check:
        jump england_japan
    elif japan_check:
        jump england_sweden
    else:
        jump going_home

label scott_movent:
    stop music fadeout 3.0
    scene tom_road
    show tom
    cs "I should wait till he's done with his video."
    tom "So yeah, we're just gonna keep talking about this road in particular."
    show car at car_run behind tom
    with move
    tom "This road here was created in 1968, by OHP--{w=0.5}{nw}"
    play sound "car_crash.ogg" volume 0.7
    scene black
    n "A speeding car rams into Tom, and he flies off into the distance."
    cs "Uh oh. {w=3.5} I didn't see nothin'."
    bad_end "Welp, that's the end\nof that video!" "scott_menu"
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
    stop music fadeout 3.0
    scene black with dissolve
    n "Arceus takes CS back to the airport."
    scene britport
    show arceus flipped at left
    show cs flipped at right
    with fade
    cs "Well, thank you so much Arceus for everything, really."
    show arceus happy flipped
    arceus "It's all good man, I loved having you here."
    arceus "It's also impressive that you made so much money in the short amount of time you were here. You'll probably be set for Japan!"
    show arceus flipped
    cs "Yeah, I honestly don't know how I managed to do most of those things, I was kinda winging it."
    cs "Welp, it looks like my plane is here."
    cs "See ya Arceus!"
    arceus "See you later, CS!"
    show cs with determination
    hide cs with moveoutright
    scene black with dissolve
    n "CS grabs his ticket and heads on to the next plane."
    scene airplane_seats
    show cs at left
    with fade
    cs "Man, I'm kinda nervous to go to Japan, actually."
    cs "It's going to be wildly different than anything I've seen before."
    cs "Oh well, I'm sure it'll be fun."
    cs "Time to get some sleep."
    scene black with dissolve
    jump japan_two

label england_sweden:
    cs "I was thinking of going to Sweden."
    kitty "Huh, never heard much about Sweden."
    arceus "Is there anywhere you wanna go in particular in Sweden?"
    cs "I don't really know where to go there."
    arceus "Well you have to meet Vinesauce Joel."
    cs "Yeah, that's a good idea."
    arceus "Welp, should we take you back to the airport?"
    cs "Sure, let's go."
    stop music fadeout 3.0
    scene black with dissolve
    n "Arceus takes CS back to the airport."
    scene britport
    show arceus flipped at left
    show cs flipped at right
    with fade
    cs "Well, thank you so much Arceus for everything, really."
    show arceus happy flipped
    arceus "It's all good man, I loved having you here."
    arceus "It's also impressive that you made so much money in the short amount of time you were here, you'll probably be set for Sweden!"
    show arceus flipped
    cs "Yeah, I honestly don't know how I managed to most of those things, I was kinda winging it."
    cs "Welp, it looks like my plane is here."
    cs "See ya Arceus!"
    arceus "See you later CS!"
    show cs with determination
    hide cs with moveoutright
    scene black with dissolve
    n "CS grabs his ticket and heads on the next plane."
    scene airplane_seats
    show cs at left
    with fade
    cs "Man, I'm kinda nervous to go to Sweden, actually."
    cs "It's going to be pretty crazy I think."
    cs "Oh well, I'm sure it'll be fun."
    cs "Time to get some sleep."
    scene black with dissolve
    jump sweden_second

label japan:
    $ japan_check = True
    show airplane_seats
    show cs at left
    with fade
    n "As CS wakes up, he sees the plane landing outside."
    cs "Wow, I really slept a lot, or that was a crazy fast trip."
    cs "Welp, time to check out Japan!"
    scene black with dissolve
    n "CS exits the terminal and enters the airport."
    scene tokyo_airport with fade
    show cs at center with moveinleft
    play music "<loop 0>automatic_love.mp3" volume 0.4
    music Automatic Love - Siix0
    cs "Wow, this place is already pretty crazy!"
    cs "I feel like this was a better place to pick than England or Sweden."
    cs "And on top of it all, I don't have to worry about the cops anymore!"
    n "CS walks out of the airport."
    hide cs with moveoutright
    scene tokyo_street with fade
    show cs disappointed at center with moveinleft
    cs "Unfortunately, I don't have any money left on me."
    cs "So I really don't know what to do now."
    cs "I could try to get a job, but I don't speak Japanese!"
    show cs
    cs "Lemme think, what could I do while I'm here?"
    jump japan_menu

label japan_two:
    $ japan_check = True
    show airplane_seats
    show cs at left
    with fade
    n "As CS wakes up, he sees the plane landing outside."
    cs "Wow, I really slept a lot, or that was a crazy fast trip."
    cs "Welp, time to check out Japan!"
    scene black with dissolve
    n "CS exits the terminal and enters the airport."
    scene tokyo_airport with fade
    show cs at center with moveinleft
    play music "<loop 0>automatic_love.mp3" volume 0.4
    music Automatic Love - Siix0
    cs "Wow, this place is already pretty crazy!"
    cs "Well, I don't know anyone who speaks English this time over here.."
    cs "And I forgot why I was travelling here, to be honest."
    n "CS walks out of the airport."
    hide cs with moveoutright
    scene tokyo_street with fade
    show cs at center with moveinleft
    cs "Fortunately, I have some money this time."
    cs "But the question is, what should I do here?"
    jump japan_menu
        
label anime_adventure:
    $ anime_check = True
    cs "I guess I can look around the city."
    cs "This place is so compact, I could be here for days!"
    cs "Let's start looking!"
    scene black with dissolve
    n "CS quickly finds a shop selling video games, and other electronics."
    scene game_store_back with fade
    show cs at mid_left with moveinleft
    cs "Wow, this is like a dream!"
    cs "There are so many retro games here!"
    cs "I would've freaked out at this when I was a kid."
    if england_check:
        cs "There are some games I could buy here, but I don't know what to pick..."
        cs "I've always wanted a big box of some classic DOS games I played, but I don't know if they'd have that."
        cs "I guess I can go ask the cashier."
        show cs flipped with determination
        hide cs with moveoutleft
        stop music fadeout 3.0
        music end   
        scene game_store_front
        show cashier at right
        with fade
        show cs at left with moveinleft
    else:
        cs "Unfortunately, I don't have any money to spend of this kinda stuff."
        cs "If I ever return with some more money, I'll have to get something from here."
        show cs flipped with determination
        hide cs with moveoutleft
        stop music fadeout 3.0
        music end    
        scene game_store_front
        show cashier at right
        with fade
        show cs at left with moveinleft
        n "As CS is about to walk out of the store, the cashier says something to him."
    cashier "Hey dude, nice cosplay!"
    show cs disappointed
    cs "Huh?"
    n "CS was surprised the cashier could speak English."
    cashier "Yeah, your maid outfit! Were you going to Comiket this year?"
    cs "No I-- This is my regular attire..."
    cashier "C'mon! No one just wears that kinda outfit everywhere!"
    cashier "Wait a second, isn't that the outfit of..."
    cs "I'm sorry, I really need to get going."
    show cs worried
    cashier "Yeah I remember! That's from Nekopara, right?"
    cashier "Wait there. I know the head of NekoWorks, lemme take a picture and send it to them."
    hide cs with moveoutright
    play music "<loop 0>chase.mp3" volume 0.4
    music The Chase - Toby Fox
    n "CS rushes out the door."
    cashier "Wait! Come back!"
    scene tokyo_street_2 with fade
    show cs at center with moveinleft
    cs "Whew! That was close. I need to--{w=1.0}{nw}"
    show cashier at left with moveinleft
    cashier "Wait! Lemme take your picture!"
    show cs scared
    cs "Fuck!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS keeps running, trying to lose the insane cashier."
    scene front_desk_2 with fade
    show cs disappointed at center with moveinleft
    cs "Okay, I think I lost him."
    cs "So, where was I?"
    show cashier at left with moveinleft
    cashier "There you are!"
    show cs scared
    cs "What? How?"
    hide cs
    hide cashier 
    with moveoutright
    scene black with dissolve
    n "The cashier chases CS up the stairs, all the way to the top floor."
    scene ceo_office_2 with fade
    n "CS runs into the boss's office of the building."
    show cs worried at center with moveinleft
    stop music fadeout 3.0
    music end
    cs "Excuse me? This crazy man is trying to take my picture, and--"
    show cashier at left with moveinleft
    cashier "Hey, look at that! It's Sayori, the creator of Nekopara!"
    show cs scared
    cs "WHAT?!?!"
    play music "<loop 0>neko_to_sanpo.mp3" volume 0.4
    music Neko To Sanpo - NEKOWORKs
    sayori "Hello, and who might you be?"
    show cs disappointed
    cs "Uhm..."
    cashier "Does it matter who he is? He said that he's been wearing this outfit forever!"
    sayori "Is this true?"
    cs "Well, okay, it's a long story..."
    cs "Since you are the creator, I guess I can bring this up."
    cs "It all started several years ago..."
    scene black with dissolve
    centered "Two hours later..."
    scene ceo_office_2 
    show cs disappointed at center
    show cashier at left
    with fade    
    cs "So yeah. That's why I wear this outfit."
    cs "You guys better tell NO ONE about this."
    cashier "That was amazing!"
    sayori "Well, that does seem very reasonable."
    sayori "And technically, you've been promoting my games for a long time now."
    show cs
    cs "Have I?"
    sayori "Well based on the dates you gave me, the amount of people who bought Nekopara merch has gone up dramatically."
    sayori "So as a token of gratitude, I'm gonna give you a bundle of my sales from the past few years."
    cs "Woah, really?"
    cs "Just for wearing this outfit?"
    sayori "The numbers don't lie."
    sayori "Here you go."
    n "Sayori hands CS a few stacks of Yen, that add up to about 10,000 USD."
    sayori "Don't go spend it all in one place, unless it's Nekopara merch."
    cashier "See? Look how cool your cosplay was!"
    show cs happy
    cs "Yeah. I do have a really cool outfit."
    cs "Thank you so much guys!"
    show cs happy flipped with determination
    hide cs with moveoutleft
    stop music fadeout 3.0
    music end    
    scene black with dissolve
    n "CS walks away proudly."
    $ achievement_manager.unlock("I'm Scared Right Now...")
    scene tokyo_street_night
    show cs at center
    with fade
    play music "<loop 0>automatic_love.mp3" volume 0.4
    if england_check:
        cs "I could plan a super fancy trip after this is over!"
    else:
        cs "Well, I have the money to travel again!"
    cs "I still feel like I should stay and do some things here."
    jump japan_menu

label karaoke:
    $ karaoke_check = True
    cs "I mean, I've always wanted to sing karaoke in Japan."
    cs "I don't know where I could go to sing, though."
    cs "There are some signs in English here."
    scene black with dissolve
    n "CS walks around for a bit, trying to find a place to stop at."
    scene karaoke_bar_outside with fade
    show cs at center with moveinleft
    cs "We got a restaurant, a few general stores..."
    cs "Ah! Bar and Karaoke!"
    cs "Let's go see what they have!"
    stop music fadeout 3.0
    music end    
    scene black with dissolve
    n "CS enters the Bar and Karaoke, and makes his way over to the Karaoke area."
    scene karaoke_bar_inside with fade
    show cs at mid_left with moveinleft
    cs "Wow, look at this! So many songs to play here!"
    cs "And no one seems to be here, so I can sing to my heart's content!"
    cs "Hmm..."
    cs "Y'know, this song looks interesting..."
    cs "Let's do this one!"
    scene black with dissolve
    pause 1.0
    scene karaoke_bar_inside
    show cs happy at mid_left
    with dissolve
    show karaoke
    window hide
    pause 119
    scene karaoke_bar_inside
    show cs at mid_left
    with fade
    cs "Woohoo! That was fun!"
    cs "That kinda wore me out though."
    cs "I don't think I should sing another one for now."
    scene black with dissolve
    n "CS heads out of the bar."
    scene karaoke_bar_outside
    show cs
    with fade
    $ achievement_manager.unlock("Dame Da Ne")
    play music "<loop 0>automatic_love.mp3" volume 0.4
    cs "Well, is there anything else I should do here?"
    jump japan_menu

label miku_pizza:
    $ miku_check = True
    cs "I wanna have some fun with Miku!"
    cs "They had a Domino's ad where you can go have some fun with Miku, right?"
    cs "But that was like, ten years ago..."
    cs "People still love Miku, I'm sure she'll uphold the deal!"
    stop music fadeout 3.0
    music end    
    scene black with dissolve
    n "CS starts making his way to the nearest Domino's."

    scene dominos_counter 
    show cashier at right
    with fade
    show cs at left with moveinleft
    play music "<loop 0>funiculi_holiday.mp3" volume 0.3
    music Funiculi Holiday - ClascyJitto
    cashier "Welcome to Domino's, can I take your order?"
    cs "I want to meet Miku!"
    cashier "Sir, what are you on about?"
    cs "Your promotion! You guys said I could have some fun with Miku!"
    cashier "I don't know what you're talking about."
    show cs disappointed
    cs "Ugh, can I just talk to Scott?"
    cashier "Who??"
    cs "Scott! The president of Domino's Pizza!"
    cashier "Man, I'm just the cashier here, you think I know the president?"
    if fun_value(20):
        obama "Hi.{w=0.5}{nw}"
    show cs
    cs "How can I find him then?"
    cashier "I think the headquarters is pretty close to here if you're that desperate."
    cs "I am, and thank you!"
    show cs flipped with determination
    hide cs with moveoutleft
    stop music fadeout 3.0
    music end
    scene japanese_street with fade
    show cs at center with moveinleft
    n "CS walks for a while until he finds the Domino's HQ."
    cs "Finally, here's the place!"

    scene front_desk with fade
    show cs at left with moveinleft
    n "CS walks up to the receptionist."
    cs "I'd like to speak to Scott."
    receptionist "The president? Who are you?"
    cs "I'm cs188, and I want to talk to Scott about the Miku promotion."
    receptionist "Why are you dressed like that?"
    cs "Can people stop asking me that?"
    receptionist "You know what, if you have the guts to come in here dressed like that and ask directly for the man himself, he's gotta see this."
    n "The receptionist calls up to Scott's office."
    receptionist "Can I send someone up? He asked to see you directly.{w=1.0} Who is it?{w=0.5} You'll see."
    pause 1.0
    receptionist "Alright, take the elevator to the penthouse."

    scene elevator
    show cs at center
    with fade
    pause 3.0
    play sound "audio/elevator_ding.ogg"
    scene black with dissolve
    pause 1.0
    scene ceo_office
    if fun_value(50):
        show scott at right
    else:
        show scott_pres at right
    with fade
    show cs at left with moveinleft
    scott_pres "Hello, sir, and what is your name?"
    cs "I'm cs188, and I'm curious about your Miku promotion."
    scott_pres "That was... what, ten years ago?"
    cs "It was, but I know Miku would uphold the deal!"
    scott_pres "Wasn't the deal like, something to do with an app? I barely remember."
    cs "Uh, I don't either."
    show cs angry
    cs "But I want to meet Miku!"
    scott_pres "Listen son, I hate to break it to you, but I don't think Miku is real."
    cs "What do you mean she's not real? She was dancing with you in the commerical!"
    scott_pres "I know, but that was movie magic. I'm sorry--{w=0.5}{nw}"
    play music "real_world.mp3"
    music Real World - Project SEKAI
    show cs
    show miku at center with moveinbottom
    show miku with vpunch
    miku "What was that?"
    scott_pres "Miku?!"
    cs "Miku!"
    miku "I heard someone was here to see me so I came up right away."
    scott_pres "How did you get in my office?"
    miku "Your receptionist let me up. She was freaking out a lot so she must have forgotten to call you."
    scott_pres "But... you're not... it was a green screen! It was augemented reality! You're not real!"
    miku "I feel pretty real."
    miku "Anywho, hi, CS! Love your videos."
    cs "You... watch my videos?"
    miku "Yeah! They're really funny."
    show cs happy
    cs "Well, thank you!"
    miku "Wanna go get a pizza?"
    cs "Sure!"
    hide scott with moveoutbottom
    hide scott_pres with moveoutbottom
    show miku with hpunch
    n "Scott faints."
    cs "Oh, jeez, let's make sure Scott is okay first."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    scene dominos
    show cs at left
    show miku at right
    with fade
    play music "<loop 0>automatic_love.mp3" volume 0.4
    miku "... so I said \"you think that was fast, wait until I sing INTENSE VOICE!\""
    n "CS laughs."
    cs "Well Miku, this was very nice, but I need to head on my way."
    miku "OK! Thanks for sharing lunch with me, this was very nice."
    cs "Bye, Miku!"
    $ achievement_manager.unlock("Have Some Fucking Pizza!")
    scene black with dissolve
    scene tokyo_street
    show cs at center with moveinleft
    with fade
    cs "I knew Miku was real!"
    cs "That pizza was pretty good too."
    cs "Anyways, what should I do now?"
    jump japan_menu

label japan_leave:
    scene tokyo_street
    show cs
    with fade
    cs "Well, I think I've done everything I wanted to do here!"
    cs "This place was really cool, but I should get going for now."
    cs "Maybe one day, I can return when I have more time."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "CS heads back to the airport."
    jump japan_leave_airport

label japan_leave_airport:
    show tokyo_airport with fade
    show cs at center with moveinleft
    cs "Man, what a time I had here."
    cs "Alright well, where should I go this time?"
    if (not england_check) and (not sweden_check):
        menu:
            "Sweden":
                jump japan_sweden
            "England":
                jump japan_england
    elif sweden_check:
        jump japan_england
    elif england_check:
        jump japan_sweden
    else:
        jump going_home

label japan_sweden:
    cs "I think I wanna go to Sweden this time."
    cs "I know Vinesauce Joel is there, and I have kinda always wanted to meet up with him."
    cs "Well, if I did the crazy things I did in this country, then I'm sure I can make it in Sweden!"
    scene black with dissolve
    n "CS goes and gets his ticket and gets on the plane."
    scene airplane_seats
    show cs at left
    with fade
    cs "Well, I'm off to Sweden!"
    cs "This is gonna be quite the trip."
    cs "I'm gonna try to get some shuteye."
    scene black with dissolve
    jump sweden_second

label japan_england:
    $ england_check = True
    cs "I think I wanna go to England this time."
    cs "I've always wanted to go to England, there is so much to do there.."
    scene black with dissolve
    n "CS goes and gets his ticket and gets on the plane."
    scene airplane_seats
    show cs at left
    with fade
    cs "Well, I'm off to England!"
    cs "This is gonna be quite the trip."
    cs "I'm gonna try to get some sleep."
    scene black with dissolve
    jump england_second

label going_home:
    stop music fadeout 1.0
    cs "Welp, I guess it's time to head home."
    cs "I've done so many things during this trip, I honestly forgot why I started this."
    cs "I had to kinda rush it, just like with a real vacation!"
    cs "Oh well."
    cs "I'm a bit homesick, and I honestly can't wait to get home."
    scene black with dissolve
    n "CS buys a ticket to US and gets on the airplane."
    n "CS takes another nap to pass the time."
    scene cs_house with fade
    show cs happy at mid_left with moveinleft
    play music "<loop 0>park_theme.mp3" volume 0.5
    music Park Theme - Lorin Nelson
    cs "Ah, finally back home!"
    cs "I can't wait to get some sleep in my own bed again."
    scene cs_car
    show carguy at right
    show cs at left
    with fade
    n "When CS walks up to his driveway, he notices a familiar face."
    cs "Hey, are you that advertiser?"
    cs "What are you doing here?"
    carguy "Well, I was a cop who was trying to track you down, but we couldn't find you."
    carguy "So I gave up on my job."
    cs "Oooh, yeah, I forgot that's why I left."
    carguy "Well, I don't really care anymore."
    carguy "My job is over with, I'm just gonna go advertise car products."
    hide carguy with moveoutleft
    n "Carguy leaves the scene."
    cs "Well, that took care of that problem."
    cs "Now, where was I?"
    cs "Oh yeah, let's get inside."
    hide cs with moveoutright
    scene cs_room with fade
    show cs at center with moveinleft
    n "CS gets inside and relaxes once more in his own house."
    cs "Man, what a trip that was."
    cs "I can finally sleep for a day."
    scene cs_room_2 with fade
    n "CS glances over at his Union Jack."
    cs "Maybe, I should get two more flags."
    stop music fadeout 1.0
    music end
    $ renpy.movie_cutscene("movies/credits.webm")
    $ renpy.end_replay()
    return

label sweden:
    scene airplane_seats
    show cs at left
    with dissolve
    n "CS wakes up as his plane lands in Stockholm."
    cs "Finally to Sweden! I don't have to worry about the cops anymore."
    cs "Now that I'm here, I should go explore."
    scene black with dissolve
    n "CS exits the airport and finds himself in the middle of the city."
    scene stockholm 
    with fade
    show cs at center with moveinleft
    play music "<loop 0>creative_exercise.mp3" loop volume 0.3
    cs "Wow! There's so many people around."
    cs "I guess I should try to find something to do..."
    cs "I don't have much money left, but I should be able to find a bus to somewhere cool."
    hide cs with moveoutright
    scene bus_zone 
    show swede at left    
    with dissolve
    show cs flipped at right with moveinright
    cs "That guy looks like he'd be able to help."
    cs "Excuse me sir, do you know where the bus stop is?"
    average_swede "Min svävare är full med ålar."
    cs "Oh dang, I forgot not many Swedes can speak English. Hopefully I find someone who can."
    n "As CS says this, he sees a bus drive past and decides to just follow it to the bus stop."
    hide cs with moveoutleft
    pause 2.0
    scene bus_map with dissolve
    n "As CS looks at the map, he tries to figure out what bus to take."
    jump sweden_menu

label sweden_second:
    scene airplane_seats
    show cs at left
    with dissolve
    n "CS wakes up as his plane lands in Stockholm."
    cs "Finally to Sweden! I've always wanted to check this place out."
    cs "Now that I'm here, I should go explore."
    scene black with dissolve
    n "CS exits the airport and finds himself in the middle of the city."
    scene stockholm 
    with fade
    show cs at center with moveinleft
    play music "<loop 0>creative_exercise.mp3" loop volume 0.3
    cs "Wow! There's so many people around."
    cs "I guess I should try to find something to do..."
    cs "I should be able to find a bus to somewhere cool, I have some money this time."
    hide cs with moveoutright
    scene bus_zone 
    show swede at left    
    with dissolve
    show cs flipped at right with moveinright
    cs "That guy looks like he'd be able to help."
    cs "Excuse me sir, do you know where the bus stop is?"
    average_swede "Min svävare är full med ålar."
    cs "Oh dang, I forgot not many Swedes can speak English. Hopefully I find someone who can."
    n "As CS says this, he sees a bus drive past and decides to just follow it to the bus stop."
    hide cs with moveoutleft
    scene black with dissolve
    pause 2.0
    scene bus_map with dissolve
    n "As CS looks at the map, he tries to figure out what bus to take."
    jump sweden_menu 

label sweden_menu:
    # "Go on an anime adventure":
    #     jump anime_adventure
    # "Go sing some karaoke":
    #     jump karaoke
    # "Have some fun with Miku":
    #     jump miku_pizza
    python:
        locations = []
        if not anime_check:
            locations.append(("Go see the Aurora Borealis", "aurora_borealis"))
        if not karaoke_check:
            locations.append(("Go to Ikea", "ikea"))
        if not miku_check:
            locations.append(("Find Joel", "joel"))
        if not locations:
            locations.append(("I've done everything", "sweden_leave"))
        label_jump = renpy.display_menu(locations)
        renpy.jump(label_jump)

label aurora_borealis:
    cs "I am in Sweden, so I guess I may as well go see the Northern Lights."
    cs "I should go somewhere less urban if I wanna see it properly though. Too much light pollution here."
    cs "I'll just get on a bus and keep going until I see somewhere with clear skies."
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS sits down on the next bus and begins staring out the window like he's in a music video."
    n "Eventually, he sees an area that looks good and gets off the bus."
    
    

    

label ikea:
    cs "I should go check out the Ikea here."
    cs "It's the land of Ikea. They're probably a lot better than the ones in the US."
    cs "Easy to find on the map too. They have icons for all the major tourist attractions."
    cs "Weird that there's only one Ikea here around here though."
    cs "I guess it's just the flagship Ikea store. It's labeled Onda Ikea - gå inte hit."
    cs "That probably means, like, Super Ikea or something."
    cs "Mondo Ikea - go into here."
    cs "Yeah that makes sense. English and Swedish are pretty much the same."
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS rides the bus for a while and eventually the Ikea comes into view."
    scene bus_seat
    show cs flipped at mid_left
    with dissolve
    cs "Oh my gosh I was right! That's the biggest Ikea I've ever seen."
    scene black with dissolve
    n "CS presses the button to stop the bus, and the rest of the passengers give him a weird look as he gets off."
    scene ikea_outside
    with dissolve
    show cs at center with moveinleft
    cs "That was strange. I wonder why everyone was giving me that look as I got off the bus."
    cs "It's not like I got off while on the bus."
    show cs happy
    cs "Whatever, I gotta get in there and get those meatballs."
    hide cs with moveoutright
    scene ikea_inside
    show ikea_greeter at mid_right
    with dissolve
    show cs at mid_left with moveinleft
    ikea_greeter "Welcome to Ikea! Can I help you with anything?"
    cs "Yeah can you show me where the food court is?"
    ikea_greeter "Of course. It's right around that corner and to the left."

    

label joel:
    $ joel_check = True
    cs "I should try to find Vinesauce Joel. He likes YTPs, so he'd probably want to hang out."
    cs "I know he's in Northern Sweden, so I'll get up there. Sweden's pretty small, it couldn't be that hard to find him."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "CS gets on a bus up north, and he falls asleep."
    n "When the bus hits the end of the line, one of the other riders wakes him up."
    scene bus_seat
    show cs concentrate at mid_left
    show joel at mid_right
    with dissolve
    joel "Hey man, you gotta get up. End of the line here."
    show cs
    cs "Oh alright, thanks for waking me--"
    pause 0.5
    show cs worried with hpunch
    cs "Wait, you're Joel! What are you doing there?"
    show cs surprised
    joel "I'm just taking the bus back home. What're you doing here?"
    cs "I was looking for you actually."
    joel "What? How? Why?"
    show cs
    cs "I just happened to be in Sweden, and I knew that you were more north, so I went north."
    joel "Your plan was just to explore all of Northern Sweden?"
    joel "That's insane."
    cs "It worked, didn't it?"
    joel "I suppose. Why did you even want to find me?"
    cs "I just thought it would be cool to hang out."
    cs "I know you also like YTPs, and I make those, so you might be interested."
    joel "Well, I do like YTPs. This situation is already nonsensical enough, might as well lean into it."
    joel "Wanna come to my house?"
    cs "Sounds like a plan. It's freezing out and have nowhere else to go."
    joel "You really didn't think this plan through at all, huh."
    cs "Didn't think I needed to." 
    cs "It's working out really well, so I still don't really."
    joel "We'll see how long that works out for you."
    scene black with dissolve
    pause 3.0
    scene joel_house with dissolve
    show joel flipped at right
    show cs at left
    with moveinleft
    show joel at right with determination
    play music "klaxon_beat.mp3" loop volume 0.6
    music Klaxon Beat - Kelly Bailey
    joel "I thought I was a dumbass..."
    joel "Well, whatever, here's my house."
    show cs happy
    cs "Ooh, it's nice."
    show cs
    cs "Wait, what's all this equipment for?"
    joel "Oh yeah that's all my alien radar stuff."
    cs "Why are you tracking aliens?"
    joel "They keep coming and killing my lifestock."
    joel "At first I thought it was just Swedish Santa because I forgot to leave out porridge for him."
    joel "Then I left out porridge for him after I replaced the first horse, but then that horse was also killed."
    joel "He didn't even eat the porridge!"
    joel "I left a camera out after I replaced the house, and I caught the little grey alien on the camera."
    cs "That's wild. So you're tracking it so you know when it comes for the horse?"
    joel "I would be, but I haven't replaced the horse."
    joel "The radar isn't very accurate, and the alien seems to live around here, so I can't tell when it's coming."
    joel "No point in buying a third horse if I can't protect it."
    cs "How did you even get the radar? Did you know how accurate it would be?"
    joel "In theory this radar could be accurate enough, but it's missing a part."
    joel "And of course, they don't make it anymore, and it was only in a few old laptops."
    cs "Ooh, I have one of those!"
    show craptopsmall at mid_left_left with dissolve
    n "CS pulls out his craptop and hands it to Joel."
    show cs at mid_right
    show craptopsmall at mid_right_right
    with move
    show craptopsmall flipped with determination
    show cs at left with move
    hide craptopsmall with dissolve
    joel "Wait, what?! Where did you pull that from?"
    cs "Don't worry about it."
    joel "What the hell!? This is the right laptop!"
    joel "You just went to Sweden with an old laptop, hopped on a bus to the north, happened to find me, and that laptop happened to have the part I needed?!"
    cs "That's an accurate recounting of events, yes."
    joel "You didn't know where I lived or that I was working on this radar! How did you manage to get the exact right part to me by random chance?!"
    joel "Alright, I don't have time to unpack all that. I gotta get the radar done asap."
    n "Joel opens the craptop and puts the part in the machine."
    scene joel_computer with dissolve
    n "He flips the on switch, and with a satisfying click, the green phosphor screen lights up, now with a much smaller dot than before."
    joel "Holy shit it worked!"
    joel "I can finally get that grey and stop living in fear!"
    joel "Now I just need bait."
    joel "Any chance you have a horse wherever you had that laptop?"
    cs "Can't help you there."
    joel "Was worth a shot at this point."
    joel "Whatever, we don't need it."
    joel "You can be the bait."
    scene joel_house
    show cs disappointed at left
    show joel at right
    with dissolve
    cs "Why would I go be bait for an alien that's already killed two horses that are about ten times my weight?"
    joel "You'll be fine, don't worry about it."
    show pipe_gun flipped at mid_right_right with dissolve
    n "Joel pulls out a makeshift gun."
    joel "This bad boy is enough to kill any alien."
    joel "You did come across the world to find me. I figure this isn't that much crazier."
    hide pipe_gun with dissolve
    cs "Okay, I'll do it."
    cs "Would the alien even go for me though?"
    cs "I'm clearly not a horse."
    joel "I don't think the aliens can tell Earth animals apart that well."
    joel "We'll just get you a horse disguise, and you'll be set."
    show cs
    cs "No need. I brought my own."
    show cs horse
    n "CS pulls out a horse head and puts it on."
    cs "See?"
    joel "What the hell?! What all do you have in there?"
    cs "Oh nothing much, just (all the shit from the random fucking shit flying back and forth bit)."
    joel "You're an interesting critter, man."
    cs "Thanks!"
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "Joel gives CS a walkie-talkie, and he goes outside to the stable while Joel watches the radar."
    scene joel_outside with dissolve
    show cs horse at center with moveinleft
    play music "<loop 0>candle_world.mp3" volume 0.4
    music Candle World - Kikiyama
    cs "Alright, I'm in position."
    joel "Sounds good, I'll run out when I see the alien moving this way and tell you on the walkie-talkie."
    pause 3.0
    joel "Holy shit grey incoming!!! I'm on my way!"
    hide cs with moveoutright
    pause 1.0
    show joel flipped at mid_left with moveinleft
    show pipe_gun at mid_mid_left with dissolve
    show alien at mid_right with moveinright
    joel "I've got you this time, alien!" #Joel makes it out just before the alien
    alien "Ikke skyt! Jeg er ikke en romvesen! Jeg er bare en normal norsk mann!" #Make this wingdings
    scene white with dissolve
    play sound "<loop 0>hks2.wav" volume 0.7
    pause 0.1
    play sound "<loop 0>hks1.wav" volume 0.7
    pause 0.1
    pause 1.0
    scene joel_outside
    show joel flipped at mid_left
    show pipe_gun at mid_mid_left
    show alien dead at mid_right
    with dissolve
    #Gun blast sfx and white screen. Screen comes back and alien is laying sideways
    joel "We did it!"
    show cs flipped at right with moveinright
    cs "Well, I was certainly not expecting to be alien bait tonight, but I glad I could help you out."
    joel "Thanks for the help! I can finally get another horse! I won't have to take the bus anymore!"
    joel "Come back inside. I'm gonna make you a real Swedish dinner to celebrate."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "Joel and CS head into the cabin, and Joel drags the alien's body into the kitchen."
    scene joel_house
    show cs at left
    show joel at right
    with dissolve
    play music "klaxon_beat.mp3" loop volume 0.6
    joel "You can just wait in the living room and play some games while I cook."
    cs "Sounds like a plan."
    show joel flipped with determination
    hide joel with moveoutright
    n "CS goes and plays Cuphead while Joel cooks."
    pause 5.0
    scene black with dissolve
    pause 1.0
    scene joel_dining
    show joel at right
    show cs at left
    with dissolve
    joel "Dinner's ready! Reindeer and Alien meatballs, lingonberry sauce, mashed potatoes, and surstromming."
    cs "That's certainly a unique meal."
    joel "Well, I wasn't gonna waste the alien meat."
    cs "I meant the reindeer and surstromming, but I suppose that's also unique."
    n "CS and Joel enjoy the meal and have a great time talking at dinner."
    joel "Well, it's getting late, we should get to bed. You can sleep on the couch."
    joel "Can't get a bus back right now anyway."
    cs "Great idea. Risking my life and eating reindeer was enough excitement for one night. I'm exhausted."
    stop music fadeout 3.0
    scene black with dissolve
    $ achievement_manager.unlock("Grand Dad")
    n "After a good nights sleep, and the alien adventures with Joel, CS gets up and heads out to the nearest bus stop."
    scene bus_map with dissolve
    cs "Where should I go next?"

