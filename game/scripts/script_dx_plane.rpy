label plane_intro_start:
    stop music fadeout 3.0
    scene carpark
    show arceus flipped at left
    show cs flipped at right
    cs "We should head back home now. I have a plan for our newfound riches."
    show arceus flipped happy
    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"
    show arceus flipped worried
    arceus "So, what is the plan, exactly?"
    arceus "I'd actually like to know how we plan to get back home now."
    show cs disappointed flipped
    cs "I technically still have the Lego car, but that's a lot of driving."
    arceus "Yeah, and I don't really wanna drive either..."

    arceus "What about taking a train?"
    cs "Okay, but where we would we find a train?"
    cs "Aren't the trains here in the U.S. kind of like, nonexistent?"
    show arceus flipped worried
    arceus "I... yeah..."
    show cs worried flipped
    cs "Plus, that would probably take, like a million years to get back home!"
    cs "We don't have those cool Japanese bullet trains that go mach 10!"
    show arceus flipped
    show cs flipped
    arceus "Heh, yeah. I wish we had those."
    show arceus angry flipped
    n "Arceus sighs."
    play music mid_boss_battle if_changed
    music mid_boss_battle
    arceus "So I guess this means we have to take a plane?"
    cs "Yeah, I think that's our best option, in my opinion."    
    cs "Arceus, is something bothering you?"
    arceus "I just..."
    arceus "I'm afraid of travelling by plane. That's it."
    show cs disappointed flipped
    cs "Oh."
    show cs flipped
    cs "Well..."
    cs "Look. If you can just trust me..."
    cs "I promise I'll make this plane trip as enjoyable as possible."
    show arceus flipped worried
    arceus "Ugh, fine."
    show arceus flipped
    arceus "If you think it'll be entertaining, I'll take your word."
    show cs happy flipped
    cs "Woohoo!"
    cs "Alrighty, let's get in the car and head to the airport!"
    show cs happy with determination
    hide cs
    hide arceus
    with moveoutright
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS and Arceus try their best to find a good parking spot."
label plane_airport:
    scene airport_parking
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with dissolve
    play music title_screen if_changed
    music title_screen
    arceus "Okay, I think it's a left here?"
    cs "Yeah yeah, I got it."
    arceus "Wait wait wait, park ther--"
    show cs worried at left behind cscar2
    arceus "God dammit dude we missed it!"
    show cs disappointed at left behind cscar2
    cs "I am trying my hardest man."
    scene black with dissolve
    n "After CS finally finds a parking spot, they pack up their belongings and head inside to the terminal."
    #cs and Arc enter the airpot
    scene airport_interior with dissolve
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    cs "What a crazy trip! That was really fun, Arc."
    arceus "Yeah, even though I was traumatized at the pizza place, I had a lot of fun."
    cs "I haven't flown in a while, and I am kind of excited."
    cs "Might tell my cool flying story again too."
    show arceus angry flipped at mid_left
    arceus "I hate airplanes, how do they even fly."
    show arceus flipped at mid_left
    cs "One of life's great mysteries I suppose."
    cs "Let's go get our tickets!"
    n "CS and Arceus run over to the ticket counter."
    scene ticket_counter
    show benrey at center
    with dissolve
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    cs "Two tickets to New York, please."
    benrey "Hey, do you have your Pass{w=0.5} Port?"
    show cs disappointed
    show arceus flipped worried
    cs "Uhhh..."
    cs "No... sorry."
    benrey "You can't get on the plane without your Pass{w=0.5} Port."
    arceus "Hold on, I'm sure I can--"
    benrey "Check inside your shirts."
    show cs worried
    cs "Huh?"
    n "CS reaches inside his shirt, and sure enough, finds a Passport."
    arceus "What in the world?"
    benrey "See? Everyone has a Pass{w=0.5} Port!"
    show cs
    show arceus flipped
    benrey "Here are your tickets. Your guys' plane should depart in a couple hours."
    cs "Woohoo!"
    arceus "Thanks!"
    n "CS and Arceus find somewhere to sit down."
    hide cs
    hide arceus
    with moveoutright
    scene airport_seats
    show cs at mid_left
    show arceus at mid_right
    with dissolve
    cs "Look at that, we got our own rooms on this flight!"
    cs "I've never had the money to fly like this before, it's part of the reason why I thought flying would be cool."
    arceus "I guess so, yeah. Thanks to your surpisingly good gambling skills, we can really just buy whatever we want now."
    show cs worried
    cs "Shit, you're right. I should've rented a private jet or something!"
    show cs
    show arceus happy
    arceus "You can do that next time, man."
    show arceus
    cs "Also, I won with pure luck, and the guy I was playing against was kind of an idiot."
    show cs happy
    cs "He was some hyper rich man who just thought I was bluffing."
    show cs
    arceus "It doesn't matter how you won, you still got 100 million dollars from that."
    show arceus worried
    n "Some people sitting around them raise an eyebrow."
    arceus "In GTA V."
    n "Arceus keeps their voice low."
    show arceus
    arceus "What do you think you'll do with the money when we get back?"
    cs "Honestly, I wanted to just buy a bunch of Lego."
    show arceus happy
    arceus "Heh, yeah that sounds like you."
    show arceus
    cs "I feel like I'm obligated to give some money to the people who have helped me get to where I am."
    cs "Obviously, you are gonna get a pretty big cut."
    arceus "Heh, okay."
    arceus "But don't blow all your money on me."
    show cs angry
    cs "Dude, you helped me get out of prison!"
    show cs worried with hpunch
    cs "...In GTA V."
    show cs
    cs "But yeah, probably gonna give some to Anno, MattKC, My parents..."
    cs "...and then the REST will be for Lego."
    show arceus happy
    n "Arceus chuckles."
    show arceus
    cs "Alright, well we can't just sit around the whole time, let's see what they have here!"
    show arceus flipped with determination
    hide cs
    hide arceus
    with moveoutright
    n "CS and Arc get up and look around for a while."
    scene airport_giftshop
    show cs angry at mid_left
    show arceus at mid_right
    with dissolve
    cs "Man, everything in this gift shop is so expensive!"
    show arceus worried
    arceus "Dude, what were we literally just talking about?"
    show cs disappointed
    cs "Oh yeah."
    show cs
    show arceus
    cs "Still. My point stands."
    show arceus happy
    arceus "You are absolutely right about that."
    show arceus worried
    arceus "What else do they have here? There's nothing I really want anyways."
    show arceus
    cs "Let's go check out the food court!"
    arceus "Good idea, I haven't eaten since that pizza place."
    show arceus flipped with determination
    hide cs
    hide arceus
    with moveoutright
    n "CS and Arc get up to the counter and check the menu."
    scene airport_foodcourt 
    show cs disappointed at mid_left
    show arceus flipped worried at left
    show cashier at right
    with dissolve
    cashier "Sorry boys, but we are experiencing a shortage in almost everything here."
    cs "Aww, what?"
    cashier "However, we do have a bunch of potatoes, so we got fries!"
    show arceus flipped
    arceus "You wanna just split some fries?"
    cs "Sure, not like we have another choice."
    arceus "I'll go find a place to sit."
    show cs
    cs "Yeah, be there in a moment."
    show arceus with determination
    hide arceus with moveoutleft
    scene black with dissolve
    n "Once CS gets the fries, they find Arc and sit down to eat."
    scene airport_dining
    show cs at mid_left
    show arceus at mid_right
    with dissolve
    arceus "Let's dig in."
    show cs worried with hpunch
    cs "Holy crap, these are some amazing fries!"
    show arceus happy
    arceus "Wow, I don't think I've had better fries than these!"
    show cs happy
    cs "I know right?"
    arceus "Maybe I gotta go to the airport more often to buy my fries!"
    cs "Same!"
    scene black with dissolve
    n "CS and Arceus finish their fries, and decide to go stand in the line for TSA."
    #either explore the airpot or straight to TSA
    show airport_tsa
    show tsa at right
    with dissolve
    tsa "Next!"
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    n "CS and Arceus put their luggage on the conveyor and walk through the scanner."
    show tsa at center with move
    show case at center with dissolve
    cs "Here you go, all our belongings!"
    n "The scanner goes off when the briefcase goes through the x-ray machine."
    tsa "Perfect, we'll-- What's this?"
    arceus "Oh yeah, our winnings."
    n "The TSA agent opens up the briefcase, revealing all the riches from the casino." 
    n "They find a notorized letter from Jerma, legitimizing the winnings."
    show tsa at right with move
    tsa "Alright, looks like you're all set."
    show cs at center
    show arceus flipped at mid_right
    with move
    hide case with dissolve
    cs "Phew! That was scary. I didn't even know that was in there!"
    hide cs
    hide arceus flipped
    with moveoutright
    scene black with dissolve
    n "Arceus and CS collect their items again and get on the plane."
    stop music fadeout 3.0
    music end
label plane_inside:
    #cs and Arc board the plane without a hitch
    scene airbus_main with dissolve
    play music cobalt_coast_day if_changed
    music cobalt_coast_day
    show cs at mid_left
    show arceus flipped at mid_right
    with moveinleft
    cs "Man, the A380 is an insanely big plane, it's got 2 stories and everything!"
    arceus "How they keep this in the air is beyond me."
    cs "Good thing we spent a ton of money too, we get our own rooms!"
    arceus "Yeah, that is nice at least."
    n "CS and Arceus overhear the steward having a conversation."
    ges "Good thing some maniac can't open the door mid flight, it'd take an insane amount of strength to pull that off."
    ges "Yeah, and in case someone does something dumb, we have a lot of tape!"
    show arceus worried
    arceus "That was awfully reassuring."
    show arceus flipped
    cs "Well, let's get settled in our rooms. See you in a bit."
    hide cs with moveoutright
    stop music fadeout 3.0
    music end
    arceus "Yeah, it'll be nice to get some rest."
    scene airbus_room with dissolve
    show cs at mid_mid_left with moveinleft
    play music abra_shop if_changed
    music abra_shop
    n "CS starts checking out his own private abode in the skies. It's got everything a CS188 might need."
    n "And the things he doesn't have, he can order, like food and drinks."
    cs "I should check on Arceus and see how well accustomed he is."
    scene airbus_room_hall with dissolve
    show cs at mid_offscreen_left with moveinleft
    cs "Hey, Arceus!"
    n "Arceus pokes his head out of his room."
    show arceus at mid_offscreen_right with moveinright
    arceus "This room is awesome, what's up CS?"
    cs "Should I do a vlog? Like Caseless Nosedive, for my YouPoof channel?"
    arceus "Just relax for a minute, maybe they'll have a funny flight safety video you can YTP later."
    cs  "That is a great point, I am going to pay extra attention to it so I can find funny moments."
    arceus "I am going to pay extra attention because I don't want to die mid-flight."
    n "Just as they are talking, a man sprints by, bonking Arceus' head."
    show arceus angry at manual_pos(0.8, 0.6):
        linear 0.5 rotate 45
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    show cs worried
    show wilbur sil_black at manual_pos(0.6, 1.0, 1.0) with moveinright
    arceus "Ow! What the hell?"
    "???" "Sorry, didn't see you there!"
    show wilbur sil_black at manual_pos(0.3, 0.5, 1.0) with MoveTransition(0.75):
        parallel:
            linear 0.75 zoom 0
        parallel:
            linear 0.75 alpha 0
    hide wilbur
    n "The man keeps sprinting down the length of the airplane."
    pause 0.25
    show cs disappointed
    cs "Woah, you okay man?"
    show arceus worried at manual_pos(0.6, 0.3):
        linear 0.5 rotate 0
    with MoveTransition(0.5)
    arceus "Yeah, just didn't expect a man to run into me."
    arceus "Not something that happens on an airplane too often, I'd assume."
    show cs
    cs "Well, let's make the most of our trip. You wanna play poker or chess?"
    show arceus
    arceus "Yeah, I'd be down for some chess. Poker would just make me think about the casino again."
    scene airbus_room_table
    show cs at left
    show arceus at center
    with dissolve
    n "CS rings the bell to call the steward."
    show ges at right with moveinright
    cs "Me and my friend would like a glass of your finest Scotch!"
    ges "How aboot that, eh? You're CS188!"
    play sound sfx_stinger volume 2.0
    show mgsvges with dissolve
    pause 3.0
    hide mgsvges with Dissolve(3.0)
    show cs disappointed
    cs "Uh, how do you know me?"
    show cs
    ges "Oh I'm best friends with the Pilot and Copilot, you'll meet em soon, eh?"
    cs "I guess I will huh. Scotch okay for you Arceus?"
    show arceus flipped
    arceus "I'm more of a wine guy, you got any red wine?"
    ges "Oh yes, a wine mom I see. I'll get you both some nice Canadian liquor, eh?"
    show arceus flipped angry
    arceus "Sure thing-- hey, I'm not a mom! That's wine... furry to you!"
    hide ges with easeoutright
    n "Ges is already rushing to get the guests their drinks."
    cs "Want to start getting beaten at chess while we wait?"
    show arceus happy
    arceus "Heh, I'd like to see you try!"
    show arceus
    n "CS and Arceus play chess and maybe we should add a chess mingame when it's not 0400"
    show ges at mid_right with moveinright
    n "After a little bit, Ges comes back with the drinks."
    show arceus flipped
    ges "For you Mr. Furry, some wine, eh?"
    arceus "Thank you."
    show arceus
    show ges at mid_left with move
    ges "And some Lagavulin for Youtube's 2nd best YTPer, eh?"
    show cs disappointed
    cs "Aw than-- What do you mean second?"
    ges "AlpacaHawk is just too funny, eh?"
    show cs
    ges "If you need something else, just let me know. I'll be in the cockpit, but I can help you guys whenever, eh?"
    cs "Thanks bud."
    ges "Okay dude, just because I'm Canadia-- whatever, call me when you need me."
    hide ges with easeoutright
    stop music fadeout 3.0
    music end
    n "After the steward leaves, the plane finally starts to taxi."
    show arceus worried
    "???" "Hey what's up jackasses, this is your co-pilot speaking."
    "???" "Just got a call from my dumb boss, but now I'm here to imform you that our kickass pilot is here to finally send this plane into the stratosphere!"
    "???" "Huh? We don't actually go up that high?"
    "???" "Well kinda? What do you mean \"Kinda?\""
    "???" "Eh, whatever. Just enjoy the flight or something."
    arceus "Are you serious? This is guy we have to listen to for the whole trip?"
    arceus "I can at least be glad that they're not the one flying."
    cs "Yeah but hey, this chess match won't end itself!"
    scene black with dissolve
    n "Just as CS and Arceus were about to start playing again, the screen cuts to the safety video."
    n "this is the part where we insert a very YTPd video thats funny and we all haha a lot!"
    scene airbus_room_table with dissolve
    show cs happy at left
    show arceus happy at center
    cs "Oh man, I can already imagine what I can do to this video."
    scene black with dissolve
    n "After what feels like an eternity, the plane finally gets on the runway and starts accelerating."
    play music huge_pillar volume 0.8 if_changed
    music huge_pillar
    scene airbus_room_hall with dissolve
    show cs at mid_offscreen_left with moveinleft
    show arceus at mid_offscreen_right with moveinright
    cs "Hold on to your teeth Arc."
    show arceus worried
    arceus "My-- my teeth?"
    arceus "Is that something people say?"
    cs "I heard it once in HALO."
    hide cs with moveoutleft
    hide arceus with moveoutright
    scene airbus_room
    show cs at center
    with dissolve
    n "The plane starts taking speed and it sends Arceus and CS slightly back into their beds."
    show cs scared at left with move
    show cs scared with hpunch
    n "Finally, the plane is in the air and it starts leveling off at around 40,000'."
    cs "Man, that was an intense climb, feels like it only took one text box to get up to altitude."
    scene airbus_room_hall with dissolve
    show cs disappointed at mid_offscreen_left with moveinleft
    cs "You okay Arceus?"
    show cs disappointed at mid_right with move
    show cs worried with hpunch
    n "CS peels the curtain of Arceus' room, only to find 3 bags full of vomit."
    show arceus angry at mid_offscreen_right with moveinright
    n "Arceus stares at CS through teary eyes with anger."
    arceus "This. Is. Why. I. Hate. Flying!"
    show cs disappointed
    n "Arceus catches his breath and downs the rest of their wine."
    arceus "I really don't get it. I just don't. This is worst feeling ever."
    show cs worried flipped
    n "A small commotion starts happening behind CS and Arc, y'know, in the poor section."
    plane_npc_1 "What the hell? My phone is gone!"
    plane_npc_2 "Dude, where in the world is my flash drive? I had a lot of very important information on there!"
    plane_npc_3 "I can't believe it, I just lost my limited edition pizza thermos..."
    show cs
    cs "Welp, no feeling can be bad when you have that case full of cash!"
    arceus "You mean the one you have, right?"
    show cs disappointed
    cs "I don't have it, I thought you did."
    show arceus worried
    arceus "No, I'm pretty sure you had it."
    cs "I don't think so, right?"
    show arceus angry
    arceus "Are you shitting me? Did we just lose millions of dollars?!"
    cs "Woah woah, it's probably not lost..."
    show cs worried
    cs "It's just, misplaced!"
    arceus "God damnit, I don't care if it's lost, misplaced, or forgotten, we currently are now back to $0!"
    n "While Arceus is yelling, a voice comes over the speakers."
    show cs disappointed flipped
    ges "So, aboot the recent events that have just been reported, eh..."
    ges "It seems that some valuables have been stolen, and we are currently working the situation out, eh."
    ges "Everyone remain calm, eh."
    show cs disappointed
    cs "Stolen."
    cs "it wasn't lost, misplaced, or even forgotten, it was stolen."
    n "Arceus grumbles."
    arceus "Man, I can't take this."
    arceus "First the fact that we have to fly, now all of our money is gone?!"
    stop music fadeout 3.0
    music end
    cs "Woah buddy, let's relax for a moment."
    cs "Think about it for a second."
    cs "Whoever the thief is on this plane, can't really escape until we land."
    show cs
    cs "If we can figure out who stole our cash before the plane lands, we'll be rich again."
    n "Arceus takes some deep breaths and calms down."
    show arceus
    arceus "Yeah, I guess so. We should have some time to figure this out."
    show cs happy
    cs "Besides, I can always go back to Vegas and just find another green dude to win against."
    arceus "Heh, you think so?"
    show cs
    cs "I know so."
    cs "Let's get some rest, and then we'll start searching for the culprit in the morning."
    arceus "I'll try."
    hide arceus with moveoutright
    show cs flipped with determination
    hide cs with moveoutleft
    n "The two go to their seperate rooms, and do their best to relax for the night."
    scene black with dissolve
    n "Later..."

label plane_search:
    scene airbus_room dark 
    show arceus dark
    with dissolve
    arceus "Man, I've been staring at the ceiling for the past hour."
    arceus "I keep thinking about the fact that we are in some metal tube 30,000 feet in the air."
    arceus "I guess I should just start looking around while everyone is asleep."
    n "Arceus steps out of their room and begins to snoop."
    scene airbus_main dark with dissolve
    show arceus dark flipped at mid_left with moveinleft
    play music pyrite_town volume 0.8 if_changed
    music pyrite_town
    arceus "Alright, I just gotta keep an eye out of a big metal briefcase."
    arceus "Can't be too hard, right?"
    arceus "Well, not when I can't see."
    show flashlight_on at mid_mid_left
    n "Arceus pulls out a flashlight they found in their room."
    arceus "There we go. I just have to be careful and not draw any attention to myself."
    show arceus dark
    show flashlight_on flipped at left
    n "As Arc turns around to go the other way, they immediately bump into someone."
    show arceus dark worried
    "???" "Hey you!"
    arceus "Ah, fuck."
    show k19 sil_black flipped at mid_offscreen_left with moveinleft
    show flashlight_on flipped:
        zoom 0.6
        linear 0.1 rotate 75 xpos 1000 ypos 600
        linear 0.2 rotate 150 xpos 800 ypos 700
        linear 0.1 rotate 210 xpos 700 ypos 1000
        linear 0.1 rotate 290 xpos 600 ypos 1500
        linear 0.1 rotate 330 xpos 500 ypos 2100
    show arceus worried dark at manual_pos(-0.1, 0.2):
        linear 0.5 rotate 10
    with MoveTransition(0.5)    
    n "The mysterious person grabs them by the jacket and yanks them up slightly."
    "???" "The fuck do you think you are doing around here at night?"
    "???" "Lemme guess, trying to steal some more things, hmm?"
    arceus "Hey man, I'm not stealing anything! I was the one stolen from!"
    "???" "Oh yeah? Prove it, buddy!"
    arceus "Uhh..."
    n "Arceus grabs their pockets and pulls them out."
    "???" "Eh, you're probably right."
    show arceus worried dark at manual_pos(0.1, 0.3):
        linear 0.5 rotate 0
    with MoveTransition(0.5)
    show arceus dark at manual_pos(0.4, 0.3)
    show k19 sil_black flipped at left
    with move
    show k19 dark flipped with dissolve
    "???" "So, you got something important stolen as well?"
    arceus "Yeah, my friend and I got our briefcase stolen. It was... full of important... things."
    k19 "Names K-19. I'm the copilot of this plane."
    play sound sfx_stinger volume 2.0
    show mgsvk19 with dissolve
    pause 3.0
    hide mgsvk19 with Dissolve(3.0)
    arceus "Wait..."
    show arceus angry dark
    arceus "Are you that asshole who gave the pre-flight speech?"
    k19 "Yeah! What, you didn't think that was funny?"
    arceus "Funny? Nothing about flying is funny!"
    k19 "Lemme guess, you're scared that \"YoU'rE fLyInG iN a MeTaL tUbE rEaLlY hIgH uP!\""
    arceus "Damnit, it's no joke! I'd rather have taken the train!"
    k19 "Oh please, the train? That shits so boring."
    k19 "Not to mention that plane travel is technically the safest method of transportation out there. So..."
    arceus "Yeah well, it sure doesn't feel like it."
    k19 "It only doesn't feel like it because you're not in control."
    show arceus dark
    k19 "Regardless, what's your name again? Don't think I caught that."
    arceus "I'm Arceus, but you can just call me Arc."
    k19 "Coolio, Arc."
    k19 "So unfortunately, I got something very important stolen as well."
    k19 "It's a small vial full of this cyan-looking liquid."
    k19 "If my boss finds out that I lost it, I'm totally screwed."
    k19 "So I think if we wanna find this crook, we should team up and work together."
    arceus "I guess so. The more help the merrier."
    k19 "If I had to check one place of the plane for valuable goods, I'd have to say the back of the plane."
    k19 "The robbers probably stole what they could in the passanger sides of the plane, now they are probably rummaging through all the suitcases packed in the cargo area."
    arceus "Good thinking, let's go."
    scene black with dissolve
    n "Arceus and K-19 head to the back of the plane."
    scene airbus_back dark
    show amber_block dark as first at manual_pos(0.8, 0.1)
    show amber_block dark as second at manual_pos(0.9, 0.1)
    with dissolve
    show k19 dark flipped at left
    show arceus dark flipped at center
    with moveinleft
    show arceus dark with determination
    k19 "Hey, still got that flashlight?"
    show flashlight_on flipped at mid_mid_left
    arceus "Yep, still got it."
    k19 "Awesome. Look for a shady figure that could be lurking around."
    show arceus dark flipped
    show flashlight_on at mid_mid_right
    show k19 dark
    n "As Arceus starts to look around, something big reflects off of Arc's flashlight beam."
    arceus "Woah, what the--"
    arceus "Hey K-19? You might want to check this out."
    show k19 dark flipped
    k19 "Sure thing, waddya--"
    k19 "Holy crap."
    n "Before them stands two large blocks of amber, both carved out with what looks like the mold of a body."
    arceus "What the fuck?"
    k19 "I remember seeing something like this in a TV show once, you thinking what I'm thinking?"
    show arceus dark with determination
    show flashlight_on flipped at mid_mid_left
    arceus "Did you know this was aboard? Did anyone?!"
    k19 "Dude I'm gonna be honest, I don't think so."
    k19 "I don't like, check the bags or anything, that's not my job."
    k19 "But I feel like someone would have said something if these were in storage."
    arceus "We should probably go tell someone, right?"
    arceus "Probably CS and the pilot?"
    k19 "Yeah, good thinking."
    k19 "You go get your friend, I'll meet you guys in the cockpit."
    arceus "Sure thing."
    scene black with dissolve
    n "Arceus and K-19 split up. Arceus arrives in CS' room shortly."
    scene airbus_room_hall dark
    show arceus dark flipped
    with dissolve
    arceus "Shit, I gotta get CS up fast."
    hide arceus with easeoutright
    scene airbus_room dark 
    show cs concentrate dark
    with dissolve
    show arceus dark flipped at mid_left with moveinleft
    n "Arceus starts to shake CS to get them up."
    show arceus angry dark flipped at mid_left
    show arceus angry dark flipped at center with ease
    show arceus angry dark flipped at mid_mid_left with ease
    show arceus angry dark flipped at center with ease
    show arceus angry dark flipped at mid_mid_left with ease
    show arceus angry dark flipped at center with ease
    show arceus angry dark flipped at mid_mid_left with ease
    arceus "Psst! Hey dude, wake up!"
    cs "C'mon, just five more minutes, dad..."
    arceus "What? No CS, it's me, Arc! We may have possibly found a lead!"
    n "CS groggily opens their eyes."
    show cs disappointed dark
    cs "Huh?"
    arceus "Yeah, get up! We gotta get to the cockpit, I have someone who might be able to help!"
    show cs disappointed dark flipped
    cs "Fine, give me a second. I gotta--"
    show cs dark flipped
    cs "Oh wait. I'm already dressed."
    arceus "Have you ever even changed out of that stume before?"
    cs "Yeah, don't you remember? When we were in jail?"
    arceus "Dude, gross. You know how long ago that was?"
    cs "A week at least?"
    arceus "Exactly! Whatever, let's get to the front of the plane already!"
    scene black with dissolve
    n "CS and Arc tip-toe their way up to the front, trying their best to not wake the other passengers."
    n "Upon reaching the cabin door, CS gently knocks. The door opens just enough to see Ges' eye pokin' through."
    scene airbus_cockpit dark 
    show elizabeth dark flipped at mid_left
    show ges dark at left
    show k19 dark at right
    with dissolve
    ges "Oh, it's you, eh. Come on in, they've been waiting for you, eh."
    show ges dark at mid_mid_right with ease
    show cs dark at left
    show arceus dark flipped at mid_left
    with moveinleft
    k19 "Care to catch the three up to speed, Arceus?"
    arceus "So, what happened was that I couldn't get any sleep, so I started searching around for where our stolen belongings might be."
    arceus "While I was searching, I bumped into the co-pilot, who was also searching for something they lost."
    arceus "We teamed up and started looking near the back, when we discovered two giant amber casings with cutouts that fit the shape of men."
    arceus "And now we are here."
    cs "So... could the amber be a modern art piece or something?"
    #add epic ass MGSV:GZ intro to Elizabeth here, and everyone else before obvs.
    eliza "We could be dealing with some people from... before your time."
    play sound sfx_stinger volume 2.0
    show mgsveliza with dissolve
    pause 3.0
    hide mgsveliza with Dissolve(3.0)
    eliza "I want you guys to start looking for passengers with old timey clothes."
    cs "Before our time? You think that the thieves were fossilized in that amber that Arceus found?"
    k19 "Hey, I was there too!"
    eliza "I can see it, the cargo manifest did list something I felt was off. Ges, please read it."
    ges "Okay, eh!"
    ges "Alright, so it looks like we got two extra large-sized cases. It seems to be giant blocks of... orange glass, with two old-timey men inside, eh."
    ges "I was told not to tamper with this cargo specifically, so I am just praying that these are just mannequins, but you never know. On they go. Next is... yaada yaada yaada."
    eliza "Yeah, so if they're not in the amber, you might want to start asking around."
    cs "Oh, this is perfect, give me a second!"
    hide cs with easeoutleft
    pause 3.0
    show cs dark at left
    show detective_hat dark as first at manual_pos(0.1, 0.4)
    show detective_hat dark as second at manual_pos(0.125, 0.45)
    with moveinleft
    n "CS rushes out and a few seconds later comes back. He quickly slams down an outfit on himself and Arceus."
    show detective_hat dark flipped as first at manual_pos(0.25, 0.4, 1.0) with MoveTransition(0.75)
    show detective_hat dark flipped as second behind cs at manual_pos(0.35, 0.6, 1.0) with MoveTransition(0.75)
    arceus "Do you... keep this with you?"
    cs "At all times, you never know when it could come in handy. Like now!"
    eliza "CS and Arceus, start asking people if they've seen anyone matching the description. Ges and K-19, go look for the lost items in crew areas."
    ges "On it, eh!" (multiple=2)
    k19 "Let's friggin' do this!" (multiple=2)
    pause 0.5
    cs "Alright, cya!" (multiple=2)
    arceus "Got it!" (multiple=2)
    pause 0.5
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "The groups split off, hoping to find clues to this now ongoing mystery."
    #menu:
    #    "Who do you want to follow first?"
    #    "K-19 and Ges":
    #        jump plane_k19_ges
    #    "CS and Arceus":
    #        jump plane_cs_arc

label plane_k19_ges:
    scene airbus_main 
    show ges flipped at mid_left
    show k19 at mid_right
    with dissolve
    play music cipher_lab volume 0.8 if_changed
    music cipher_lab
    ges "Alright 19, we should start with the bathrooms, not too much space, but they could still have hidden some stuff there, eh?"
    k19 "I... guess? I don't know. I'm just glad there's not too many crew spaces in this plane."
    ges "Yeah, should make our job a bit easier than asking around."
    scene airbus_bathroom 
    with dissolve
    show ges flipped at center
    show k19 flipped at left
    with moveinleft
    n "Ges and K-19 make their way to the bathrooms and, unsurprisingly, find nothing."
    show ges
    ges "I actually don't know what I expected, eh."
    scene black with dissolve
    n "They make their way to the back of the plane, to the cargo bay."
    scene airbus_back
    show amber_block as first at manual_pos(0.8, 0.1)
    show amber_block as second at manual_pos(0.9, 0.1)
    show ges flipped at center
    show k19 flipped at mid_right
    with dissolve
    ges "So this is the amber, huh."
    k19 "Yeah, see? Perfectly cut man holes."
    ges "You think it tastes good?"
    ges "I'll give you 20 bucks if you eat a chunk."
    k19 "You're on!"
    show k19 flipped at right with ease
    show k19 flipped with hpunch
    show k19 flipped at mid_right with move
    show k19 with determination
    n "K-19 takes a bite out of one of the amber towers. It tastes alright."
    ges "Fair is fair, here's a 20."
    k19 "This is 20 Canadian, what am I... whatever, it's fine."
    ges "It even has a picture of the queen on it!"
    scene cargo_hold
    show cargo_hold_fg
    show ges flipped at center
    show k19 flipped at mid_right
    with dissolve
    n "After a bit of walking, they reach the luggage area."
    k19 "Man, a lot of suitcases around for pilfering through."
    ges "19, I told you already we probably shouldn't do that... although one might not h--"
    n "All of a sudden they hear a small bang."
    show ges
    show k19
    with hpunch
    ges "Did you hear that?"
    k19 "Yeah, I did."
    n "They slowly approach the source of the noise."
    show wilbur sil_black at left with moveinleft
    n "Standing there, is a man with a telephone receiver in his ear. They quickly drop it and start running away."
    k19 "Hey, get back here asshole!"
    ges "You can't be here man! Get back in your amber or whatever, eh!"
    "???" "You still there? Whatever I should be there soon."

label plane_cs_arc:
    scene airbus_top
    show cs at mid_left
    show arceus at mid_right
    show detective_hat flipped as first at manual_pos(0.325, 0.4, 1.0)
    show detective_hat as second at manual_pos(0.825, 0.6, 1.0) 
    with dissolve
    play music cipher_lab volume 0.8 if_changed
    music cipher_lab
    n "As the morning arrives, CS and Arc start asking the passengers if they have seen the culprits."
    cs "Alright detective Arceus, where should we look first?"
    cs "I've got a hankering suspicion that the criminals might be down on the bottom floor."
    show smoke_pipe at manual_pos(0.34, 0.8, 1.0) with dissolve
    show smoke_pipe at manual_pos(0.34, 0.6, 1.0) with MoveTransition(0.75)
    n "CS pulls out a smokepipe and puts it in his mouth."
    show arceus happy
    n "Arceus chuckles a little bit."
    arceus "Do you really need to smoke out of a pipe for this?"
    cs "Of course!"
    n "One of the passengers sees CS with the pipe in his mouth and yells at them."
    plane_npc_1 "Hey! You aren't supposed to smoke on this plane!"
    show cs angry
    cs "Oh yeah? Well, have you seen someone from the 1900's walking around here recently?"
    plane_npc_1 "Sure I have, it's you guys! You both look ridiculous!"
    show detective_hat as second at manual_pos(0.825, 0.58, 1.0) 
    show arceus worried
    cs "You wanna brawl, sonny?"
    arceus "Enough, CS. Let's go to the bottom floor."
    cs "Fine, but you should watch your manners!"
    show detective_hat as second at manual_pos(0.57, 0.58, 1.0)
    show arceus worried at center
    with move
    n "Arceus drags CS downstairs before he causes any more commotion."
    hide arceus
    hide cs
    hide detective_hat as second
    hide detective_hat flipped as first
    hide smoke_pipe
    with moveoutright
    scene airbus_stairs
    show cs at mid_left
    show arceus at mid_right
    show detective_hat flipped as first at manual_pos(0.325, 0.4, 1.0)
    show detective_hat as second at manual_pos(0.825, 0.6, 1.0) 
    with dissolve
    arceus "Okay, now we should probably start asking around to see if anyone has seen anything."
    arceus "You probably shouldn't pull out the pipe this time."
    cs "Good thinking, Arc."
    show magnifying_glass at manual_pos(0.45, 0.8, 1.0) with dissolve
    n "CS pulls out a comically-large magnifying glass instead."
    arceus "Wha-- why?"
    cs "In case we find any clues!"
    arceus "Okay. Sure."
    n "Arceus starts asking the passengers."
    arceus "Hey, have you seen any old-fashioned people walking around this plane at all?"
    plane_npc_2 "No siree, furry."
    arceus "Darn, okay."
    n "Arceus hears someone trying to get their attention."
    show arceus flipped
    show detective_hat flipped as second at manual_pos(0.85, 0.6, 1.0)  
    plane_npc_3 "Psst! Hey!"
    cs "Let's go see what that fellow passenger needs."
    scene airbus_bottom
    show cs at mid_left
    show arceus at mid_right
    show detective_hat flipped as first at manual_pos(0.325, 0.4, 1.0)
    show detective_hat as second at manual_pos(0.825, 0.6, 1.0) 
    with dissolve
    arceus "Hey man, what did you need?"
    plane_npc_3 "You guys looking for the thief?"
    arceus "Yeah we are actually, have you seen them?"
    plane_npc_3 "I think so. They stole my limited-edition pizza thermos, signed by Mike himself!"
    cs "Lucky."
    show detective_hat as second at manual_pos(0.825, 0.58, 1.0) 
    show arceus worried
    arceus "Who?"
    cs "Don't worry about it. He works at the bus stop."
    show arceus at mid_right
    show detective_hat as second at manual_pos(0.825, 0.6, 1.0) 
    plane_npc_3 "Anyways, I saw these two guys dressed in really old-fashioned clothing, and I saw them just take someone's bag while they were gone!"
    plane_npc_3 "So if I had to guess, it was probably them."
    plane_npc_3 "Either that, or now we have a bunch of criminals running around this plane!"
    cs "Did you see which way they went?"
    plane_npc_3 "Last time I saw them, they were heading towards the back of the plane."
    arceus "Thank you so much, we'll get your thing back."
    cs "It's a pizza thermos, Arc."
    show arceus angry
    arceus "Whatever, yeah."
    plane_npc_3 "I wish you two the best of luck!"
    n "CS and Arc make their way towards the back of the plane."
    scene airbus_back 
    show cs at mid_left
    show arceus at mid_right
    show detective_hat flipped as first at manual_pos(0.325, 0.4, 1.0)
    show detective_hat as second at manual_pos(0.825, 0.6, 1.0)
    show orville sil_black behind cs at manual_pos(0.3, 0.55, 1.0):
        zoom 0.3
    show amber_block as third at manual_pos(0.8, 0.1)
    show amber_block as fourth at manual_pos(0.9, 0.1)
    with dissolve
    cs "Alright Arc, be prepared for anything."
    cs "We don't know what these hooligans will throw at us!"
    arceus "I'm sure we can handle it, unless they have a gun or something."
    arceus "Y'know, in a weird way, this has actually helped me forget about the fact that we are flying in a plane."
    cs "Hey see? I knew it'd be alright!"
    cs "Not sure how much I actually helped, but at least you're feeling better."
    cs "Now let's go catch those criminals!"
    arceus "We may have already found one of them."
    arceus "See that guy on the phone over there?"
    show cs flipped
    show detective_hat as first at manual_pos(0.35, 0.4, 1.0)
    show cs flipped at center
    show detective_hat as first at manual_pos(0.6, 0.4, 1.0)
    with move
    n "CS looks over on the other side of the plane, and sees a very sleezy man twirling their moustache while talking on the phone."
    "???" "Heading down that way now, sir."
    cs "Hey you! We'd like to ask you a few questions."
    show orville sil_black behind cs at manual_pos(0.3, 1.1, 1.0) with MoveTransition(0.75):
        parallel:
            linear 0.75 zoom 1    
    n "The individual gets shocked by CS and Arc, and quickly pulls out a small bag."
    show cs scared flipped
    "???" "Sand in the eyes!"
    show cs concentrate flipped
    hide orville sil_black with easeoutleft
    cs "Ahhh, fuck!"
    arceus "Well, we found what they were gonna throw at us!"
    arceus "After them!"
    hide arceus
    hide detective_hat as second 
    with moveoutleft
    cs "Yeah you go, give me a minute, I can't see!"
    scene black with dissolve
    #merge routes later
label plane_brothers:
    scene airbus_back
    show amber_block as third at manual_pos(0.8, 0.1)
    show amber_block as fourth at manual_pos(0.9, 0.1)
    with dissolve
    show wilbur sil_black at offscreenright
    show ges at offscreenright
    show cs angry at offscreenleft
    show k19 at offscreenright
    show arceus flipped at offscreenleft
    show orville sil_black at offscreenleft
    stop music fadeout 3.0
    music end
    n "Both groups chase after their respective target."
    k19 "There he is, go grab them, Ges!"
    hide wilbur sil_black with moveoutleft
    hide ges with moveoutleft
    if fun_value(FUN_VALUE_COMMON):
        ges "Come back here, you hoser!"
    else:
        ges "Come back here, you robber!"
    cs "Arc, jump at him or something!"
    hide orville sil_black with moveoutright
    show arceus flipped behind cs at manual_pos(1.2, 0.8)with MoveTransition(1.0):
        linear 1 rotate 45
    n "Arceus leaps at the villian, but misses."
    scene airbus_back
    show amber_block as third at manual_pos(0.8, 0.1)
    show amber_block as fourth at manual_pos(0.9, 0.1)    
    with hpunch
    arceus "Oof!"
    cs "Don't worry, I'm still right behind him!"
    show wilbur sil_black at offscreenright
    show ges at offscreenright
    show cs angry at offscreenleft
    show k19 at offscreenright
    show arceus flipped at offscreenleft
    show orville sil_black at offscreenleft
    hide orville sil_black with moveoutright
    hide wilbur sil_black with moveoutleft
    show cs angry at center
    show ges at center
    with move
    #Both groups slam into eachother
    ges "Gotcha!" (multiple=2)
    cs "Got you!" (multiple=2)
    show cs worried at mid_left
    show ges at mid_right
    with move
    pause 0.5
    ges "Huh?" (multiple=2)
    cs "What the?" (multiple=2)
    pause 0.5
    scene black with dissolve
    pause 1.0
    scene airbus_back 
    show k19 flipped at center
    show cs angry at mid_mid_left
    show arceus angry flipped at mid_left
    show ges flipped at left
    show orville sil_black at right
    show wilbur sil_black at mid_right
    show amber_block as third behind orville at manual_pos(0.8, 0.1)
    show amber_block as fourth behind orville at manual_pos(0.9, 0.1)
    with dissolve
    k19 "What are you guys doing back here?"
    "???" "Well, well, well..."
    "???" "We were just taking what is rightfully ours!"
    cs "Just who the hell are you guys?!"
    "???" "We are:"
    #awesome ass MGSV title card thing.
    play sound sfx_stinger volume 2.0
    show mgsvwb
    show orville at right
    show wilbur at mid_right
    with dissolve
    pause 3.0
    hide mgsvwb
    with Dissolve(3.0)
    wilbur "And now, we must leave with our spoils."
    orville "Toodeloo, idiots!"
    hide orville
    hide wilbur
    with moveoutright
    play music run_for_your_life volume 1 if_changed
    music run_for_your_life
    n "The Wright brothers book it to the back of the plane!"
    scene cargo_hold
    show cargo_hold_fg
    show k19 flipped at center
    show cs disappointed at mid_mid_left
    show arceus flipped at mid_left
    show ges flipped at left
    with dissolve
    n "When the gang catch up to them, they are completely gone."
    cs "Wha-- Where did they go?!"
    arceus "Are there any other doors here, I didn't see any!"
    k19 "No, there shouldn't be."
    n "*Ahem* Up there."
    show hatch at manual_pos(0.3, -0.2) with dissolve
    cs "Up... oh guys, a hatch!"
    show arceus worried flipped
    arceus "How did you spot that?"
    cs "Just got a sharp eye I guess."
    arceus "Wait a minute, wait a minute."
    show arceus angry flipped
    arceus "CS are you really suggesting that we get get on the roof of this plane?!"
    cs "It's the only way, I don't know where else they could've gone, and they are gonna get away with our winnings!"
    arceus "That's suicidal. We'll be immediately ripped out of the plane."
    cs "I mean... they did it. Why couldn't we?"
    arceus "How do you know? They probably just jumped up there and got sucked out!"
    cs "I mean, they're smart, right? They wouldn't just do that if it wasn't somewhat safe."
    arceus "I don't know, I don't know, I don't think I can do this."
    k19 "C'mon guys, we need to stop them now!"
    cs "I got an idea."
    cs "Arc, grab onto my back."
    show arceus flipped
    arceus "Uh, ok."
    show arceus flipped behind cs at manual_pos(0.15, 0.2)with MoveTransition(1.0)
    cs "Does anyone have any Duct tape?"
    ges "I always carry some in case we have to arrest someone!"
    cs "Tape Arceus to my back."
    show arceus worried flipped
    arceus "Are we really doing this?"
    cs "Yes, and hurry!"
    scene black with dissolve
    n "Ges and K-19 quickly tape Arceus to CS' back."
    scene cargo_hold
    show cargo_hold_fg
    show k19 flipped at center
    show cs tape at mid_left
    show ges flipped at left
    with dissolve
    arceus "Great, I look like C-3P0 from Episode V..."
    k19 "Cool man, it doesn't matter. We need to stop them or I might not have a place to comeback to!"
    n "They quickly make their way up into the roof of the plane."
    scene car plains
    show airbus_roof
    show cs tape at manual_pos(0.4, 0.3):
        zoom 0.2
    show ges flipped at manual_pos(0.2, 0.3):
        zoom 0.2
    show k19 flipped at manual_pos(0.3, 0.275):
        zoom 0.2
    show wilbur at manual_pos(0.8, 0.3):
        zoom 0.2
    show orville at manual_pos(0.9, 0.3):
        zoom 0.2
    with dissolve
    ges "I did not think this was possible!"
    arceus "I'm going to DIE UP HERE."
    show cs tape angry at manual_pos(0.4, 0.3):
        zoom 0.2
    cs "There they are, get them!"
    wilbur "Drat, they have found us."
    orville "We just have to stall them out brother. Then we can be free once again!"
    wilbur "You see, after our first successful flight, we had another one."
    orville "Sadly, it wasn't as successful as the first. We fell into a cave."
    wilbur "A cave full of amber..."
    orville "The government covered it up pretty well, but now we're back!"
    k19 "They're just trying to stall us out, get them!"
    #epic fight start
    menu:
        "No Fight yet, sorry."
        "Win the fight":
            jump plane_fight_win
        "Lose the fight":
            jump plane_fight_lose  

label plane_fight_win:
    scene car plains
    show airbus_roof
    show cs tape angry at manual_pos(0.4, 0.3):
        zoom 0.2
    show ges flipped at manual_pos(0.2, 0.3):
        zoom 0.2
    show k19 flipped at manual_pos(0.3, 0.275):
        zoom 0.2
    show wilbur at manual_pos(0.8, 0.3):
        zoom 0.2
    show orville at manual_pos(0.9, 0.3):
        zoom 0.2
    with dissolve
    stop music fadeout 3.0
    music end
    n "After that awesome fight, CS and the crew have successfully bested the First Flyers."
    cs "End of the line, guys!"
    k19 "You've got nowhere to run! Now turn yourselves in!"
    wilbur "Oh, fiddlesticks."
    orville "Looks like we've been out of the game for too long."
    show k19 flipped at manual_pos(0.8, 0.275)with MoveTransition(1.0):
        zoom 0.2
    show ges flipped at manual_pos(0.9, 0.3)with MoveTransition(1.0):
        zoom 0.2
    n "K-19 grabs onto Wilbur and Ges grabs onto Orville."
    arceus "We got them, can we get back inside the plane now before we fucking die?!"
    cs "Oh yeah, let's get back inside."
    scene black with dissolve
    n "The group drags the two criminals back into the cargo bay."
    scene cargo_hold
    show cargo_hold_fg
    show ges flipped at left
    show arceus flipped at left
    show cs at mid_left
    show wilbur at mid_left
    show orville at mid_left_left
    show k19 flipped at mid_mid_left
    with dissolve
    k19 "Alright, now that we captured them, let's get our stuff back!"
    "???" "Not so fast, bucko!"
    show booger at right with moveintop
    show booger with hpunch
    play sound sfx_stinger volume 2.0
    show mgsvbooger with dissolve
    pause 3.0
    hide mgsvbooger with Dissolve(3.0)
    wilbur "Boss, save us!"
    k19 "Who the heck are you?"
    booger "Ya don't recognize me? From those commericals?"
    cs "Are you supposed to be the Mucinex Booger?"
    booger "Supposed to be? I AM the Mucinex Booger!"
    booger "And I'm gonna give you something a little bit more than congestion!"
    show booger gun
    #Booger man pulls out a gun
    booger "Prepare to die!"
    ges "Everyone watch out! I got this!"
    show ges flipped at center with move
    show mucinex at manual_pos(0.5, 0.5) with dissolve:
        zoom 0.5
    show mucinex:
        zoom 0.5
        linear 0.1 rotate 75 xpos 1000 ypos 600
        linear 0.2 rotate 150 xpos 1250 ypos 700
        linear 0.1 rotate 210 xpos 1500 ypos 800
        linear 0.1 rotate 290 xpos 1700 ypos 900
        linear 0.1 rotate 330 xpos 2000 ypos 1000

    #Ges throws Mucinex at the booger
    booger "Heh, you think that's gonna work?"
    show k19 gun flipped at center
    #K19 pulls out a pistol and shoots them
    booger "Oh, no..."
    play sound sfx_hks1
    hide booger
    show snot at manual_pos(0.035, 0.025) with hpunch
    # The booger explodes, and everyone gets cover in snot
    pause 5.0
    cs "O-oh..."
    k19 "I... should've figured that."
    wilbur "Shit." (multiple=2)
    orville "Shit." (multiple=2)
    scene black with dissolve
    n "After everyone gets cleaned up, K-19 grabs the brothers and gives them a shakedown."
    scene cargo_hold
    show cargo_hold_fg
    show ges flipped at left
    show arceus flipped at left
    show cs at mid_left
    show wilbur at right
    show orville at mid_left_left
    show k19 behind wilbur at right
    with dissolve
    pause 0.5
    show wilbur with hpunch
    show smartphone at manual_pos(0.8, 0.5)
    show smartphone at manual_pos(0.7, 0.9) with MoveTransition(1.0):
        zoom 0.2
        linear 1 rotate 30
    show wilbur with hpunch
    show wilbur with hpunch
    show wilbur with hpunch
    wilbur "Aieeeeee!"
    k19 "God damnit, where is it?"
    show k19 at left with move
    orville "Oh, please heavens, have mercy!"
    show orville with hpunch
    show pizza_thermos at manual_pos(0.2, 0.5)
    show pizza_thermos at manual_pos(0.4, 0.9) with MoveTransition(0.5):
        zoom 0.3
        linear 0.5 rotate 60
    show orville with hpunch
    show flash_drive at manual_pos(0.2, 0.5)
    show flash_drive at manual_pos(0.2, 0.9) with MoveTransition(0.5):
        zoom 0.2
        linear 0.5 rotate -45
    show orville with hpunch
    show briefcase at manual_pos(0.2, 0.5)
    show briefcase at manual_pos(0.3, 0.85) with MoveTransition(0.5):
        zoom 0.7
        linear 0.5 rotate 10
    show orville with hpunch
    show vial at manual_pos(0.2, 0.5)
    show vial at manual_pos(0.2, 0.9) with MoveTransition(0.5):
        zoom 0.5
        linear 0.5 rotate 187
    orville "Oh, the humanity!"
    cs "Hey look, our money!"
    k19 "Finally, there it is!"
    k19 "You got anything else in there?"
    orville "I'm out, I swear!"
    cs "Woohoo! We stopped them!"
    cs "High five, Arc!"
    ges "Why don't we go tell Elizabeth the good news?"
    cs "Awesome!"
    scene black with dissolve
    n "The passengers cheer as the two criminals are brought to justice."
    scene airbus_cockpit 
    show elizabeth flipped at mid_left
    show cs at left
    show arceus flipped at left
    show k19 at right
    show wilbur at right
    show ges at mid_right
    show orville at mid_right
    with dissolve
    k19 "Look what the cat dragged in!"
    eliza "Would you look at that? The Wright Brothers on my damn plane."
    eliza "I almost can't believe it. I remember hearing about your first flight, and now it seems that this is your last."
    eliza "Ges, go tape them up."
    ges "On it, boss!"
    hide ges
    hide wilbur
    hide orville
    with moveoutleft
    n "Ges takes the men to their seats."
    eliza "And for you two..."
    eliza "Thank you so much for helping out. We really appreciate your help."
    eliza "If you could, go ahead and start returning the stolen items back to our customers."
    cs "Will do."
    cs "Let's go, Arc."
    scene cargo_hold
    show cargo_hold_fg
    show cs at mid_left
    show arceus at mid_right
    with dissolve
    n "CS and Arceus go back to the ends of the plane again to recover all the items."
    arceus "These guys shoved a lot in their pockets..."
    cs "Yeah, they had a lot on them."
    arceus "Hey look! There's our briefcase!"
    n "Arceus picks it up, and prepares to open it."
    show cs worried
    cs "Wait no--"
    show arceus worried
    n "As Arceus opens the case, a bunch of Lego spill out all over the place."
    show arceus angry
    arceus "Damnit. I forgot about the Lego."
    scene black with dissolve
    n "After cleaning up the Lego that spilled out, the pair gathered everyone's stolen goods."
    scene airbus_top with dissolve
    plane_npc_1 "Man, what a bummer."
    show cs flipped at center
    show arceus at mid_right
    with moveinright
    cs "Hello sir, did the thief steal something from you?"
    plane_npc_1 "Yeah, my phone is gone."
    show arceus happy
    arceus "Welp, good news! We have it right here."
    show arceus
    plane_npc_1 "What?! Oh thank god. I really couldn't afford another one. I owe you my life."
    show cs disappointed flipped
    cs "Okay, I don't think it's that serious sir."
    plane_npc_1 "I live and die by your orders, boss."
    #turn CS into Venom CS for a frame or two here.
    hide cs
    hide arceus
    with moveoutleft
    n "CS and Arceus find another person that got their stuff stolen."
    show airbus_stairs with dissolve
    show cs flipped at center
    show arceus at mid_right
    with moveinright
    cs "Hey, sir? I think this belongs to you."
    n "CS shows a flash drive to the man, who very quickly snags it away and hides it."
    plane_npc_2 "Sorry for the... abrupt reaction. Last time I got one of these stolen it was a bit of a scandal."
    plane_npc_2 "Here, a copy of Borderlands 4 for your troubles."
    show arceus worried
    show cs disappointed flipped
    arceus "Wasn't this game like... not the best?"
    show arceus angry
    plane_npc_2 "Another fake fan, huh. Anyways, thank you so much for the help. See ya!"
    show cs angry flipped
    cs "Weirdo."
    hide cs
    hide arceus
    with moveoutleft
    n "CS and Arc leave the man alone."
    plane_npc_2 "Man, this is great! I hope they hired another Claptrap voice actor again!"
    n "Finally, CS and Arceus make their way to the last person."
    scene airbus_bottom
    show cs at left
    show arceus at right
    with dissolve
    cs "Hey man, CS here."
    plane_npc_3 "Hey CS, man here. What's up?"
    arceus "Well, thanks to you, we caught the thief!"
    show cs happy
    cs "And we have your pizza thermos too!"
    show cs
    plane_npc_3 "Oh man, that's wonderful!"
    n "CS gives the man the pizza thermos."
    plane_npc_3 "I don't even know how I can begin to repay you guys!"
    n "He takes a bite out of the contents in the inside."
    cs "Don't worry about it, see it as us repaying you for leading us to the hooligan."
    show arceus happy
    arceus "Yeah, thanks for that. Have a good day!"
    n "After CS and Arc give back all the stolen items, they head back to the cockpit to check up on the crew."
    cs "We returned everything back to their rightful owners!"
    eliza "Thank you guys."
    eliza "Your guy's names are CS and Arceus, correct?"
    cs "That's me." (multiple=2)
    arceus "That's me." (multiple=2)
    eliza "Thank you CS and Arceus, we appreciate the work you guys did. We will try to make it back to you in time."
    cs "No need, we kinda won 100 million dollars at the casino."
    eliza "Alright well, we hope that you can stay comfortable for the rest of the flight."
    eliza "You can head back to your seats now."
    cs "Cool, let's go Arc."
    n "As CS and Arc are heading back to their rooms, they see Ges and K-19 taping The Wright Brothers their chairs."
    ges "You fellows aren't going anywhere, eh?"
    k19 "I'll sit here and watch you guys like a hawk if I have to."
    wilbur "Oh, Good heavens..."
    ges "I think these men are strapped-up well enough, eh."
    arceus "So, you guys are gonna make sure they can't break out of that tape, right?"
    k19 "Don't worry, I'll be here."
    arceus "Good, I want to have try to have a relaxing rest of my flight."
    jump south_back_home_alt


label plane_fight_lose:
    scene car plains
    show airbus_roof
    show cs tape angry at manual_pos(0.4, 0.3):
        zoom 0.2
    show ges flipped at manual_pos(0.2, 0.3):
        zoom 0.2
    show k19 flipped at manual_pos(0.3, 0.275):
        zoom 0.2
    show wilbur at manual_pos(0.8, 0.3):
        zoom 0.2
    show orville at manual_pos(0.9, 0.3):
        zoom 0.2
    with dissolve
    stop music fadeout 3.0
    music end
    n "After that epic brawl, The Wright Brothers stand triumpantly over CS and the crew."
    wilbur "Well, whaddya know?"
    orville "Looks like we gave them the ol' one two!"
    wilbur "And just in time, too!"
    n "A propeller whirring in the distance grows louder and louder!"
    orville "We've got a flight to catch!"
    booger "Get on, boys!"
    cs "Guys, no!"
    cs "You... can't..."
    booger "See you later, suckers!"
    k19 "This can't be..."
    ges "God damnit!"
    arceus "We... lost..."
    arceus "Can we at least get back inside before we get knocked off?"
    cs "Alright everyone, let's go..."
    scene black with dissolve
    n "The whole crew climbs back into the cargo bay."
    scene cargo_hold
    show cargo_hold_fg
    show ges flipped at left
    show k19 flipped at mid_left
    show cs disappointed flipped at right
    show arceus worried at mid_right
    with dissolve
    k19 "These stupid ancient motherfuckers..."
    k19 "Why did this have to happen to us?"
    ges "C'mon man, let's get back to Elizabeth to tell her the news..."
    show k19 with determination
    hide k19 with moveoutleft
    show ges with hpunch
    n "K-19 grumbles and slams the door open."
    show ges with determination
    hide ges with moveoutleft
    show cs disappointed flipped at mid_left with move
    show cs disappointed with determination
    cs "Hey Arc, I'm sorry about this whole plane thing..."
    cs "Your right. If we just stuck with the train, we probably wouldn't have had to deal with criminals and sutff."
    show arceus
    arceus "Hey man, it's not entirely your fault."
    arceus "You tried your best, and I'm sure it would've been fine if these time travellers didn't ruin it for us."
    show arceus worried
    arceus "We probably could've stopped them if I wasn't so scared of plane travel."
    show arceus
    cs "Eh, fighting them on top of the plane was a far fetched idea anyways."
    show cs
    cs "So next year, back to Vegas for round 2?"
    arceus "Heh, we'll see."
    arceus "Let's go catch up with the others."
    show cs flipped with determination
    hide cs
    hide arceus
    with moveoutleft
    n "CS and Arceus meetup with the others in the cockpit."
    scene airbus_cockpit
    show elizabeth at mid_left
    show k19 at right
    show ges at center
    with dissolve
    eliza "So, they got away?"
    ges "Yeah, their accomplice showed up on their very first plane, I'm surpised it managed to catch up with us!"
    ges "Their boss looked like a huge booger, which was kinda weird..."
    k19 "And I just lost the most important data of my lifetime!"
    eliza "What did you lose, if I may ask?"
    k19 "It was a little vial, encased with a memory of my boss or something..."
    k19 "They didn't tell me exactly what it was, but I was supposed to drop it off at the location we were heading to."
    eliza "Well if it makes you feel any better, they probably don't know what the hell it is or how to use it."
    k19 "I guess, right? But how the hell am I gonna get home? They'll kill me if I show up empty-handed!"
    eliza "Just give them a call when we land. If you can't work it out, then we'll figure something out."
    k19 "Fuck..."
    n "K-19 sits down in their seat and tries to take their mind off the whole situation."
    show cs disappointed at left
    show arceus flipped at left
    with moveinleft
    cs "Hey guys, CS here."
    arceus "Did you guys hear the news?"
    eliza "Yeah, unfortunately I did."
    cs "Should you guys make an annoucement or something?"
    ges "I'll do that here in a moment."
    cs "We tried to fight them off, but they bested us."
    eliza "I appreciate your efforts, but after this trip, I have some buddies I can hit up to see if they can track them down."
    eliza "For now, you guys should go find your seats."
    cs "Alrighty..."
    cs "Let's go, Arceus."
    show cs disappointed flipped
    show arceus
    with determination
    hide cs
    hide arceus
    with moveoutleft
    n "CS and Arceus go back to their seats, and wait out the rest of the flight."
    ges "Attention everyone, we have some unfortunate news."
    ges "It seems that the thieves have escaped with the stolen belongings."
    n "Groans of disgruntled customers bellow through the fuselage."
    ges "We'll repay everyone in anyway we can after the trip."
    ges "We're sorry for the inconveinence."
    scene black with dissolve
    n "The plane makes a safe landing after an hour or so, and everyone slowly starts to get off the plane."
    scene inside_airport 
    show cs disappointed at left
    show arceus at right
    with dissolve
    cs "Man, this stinks."
    cs "Now we can't even get home!"
    arceus "Why?"
    show arceus worried
    arceus "Oh yeah, we don't have any money or a car."
    cs "I guess we better start walking..."
    show billy at center with moveinleft
    play music mm_select volume 0.3 if_changed
    music mm_select
    billy "Hi, Billy Mays here!"
    show cs
    show arceus
    billy "Did the Wright Brothers manage to escape with your Vegas winnings?"
    billy "Well since I'm such a nice guy, I'll take you both home for free!"
    cs "Woah, seriously?"
    billy "Sure thing! Let's get going!"
    show arceus happy
    arceus "Awesome! We found a ride home!"
    scene black with dissolve
    jump south_back_home_alt