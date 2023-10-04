label dpn_call:
    if nice_car:
        scene joj_charger_fg
        show drive_day behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_day behind car_inside_fg
    show cs at left
    show pakoo at right
    with fade
    play music "<loop 0>tuna_fish.mp3" loop volume 0.6
    music Tuna Fish - Dr. Awesome
    cs "What a crazy day so far man."
    cs "I can't believe we had to fight all those cops! If it weren't for Tate and the gang, we'd be dead meat already."
    arceus "Yeah, but hey, you held them off pretty well with that fancy gun of yours."
    pakoo "Yeah, that was some great marksmanship CS!"
    show cs happy
    cs "Thank you!"
    show cs
    arceus "So now that we're on the road, and we have time to think, what is our plan?"
    arceus "Copguy's gonna come back, we need to think fast."
    cs "Is there anyone else we can call for help?"
    arceus "There are a few people, I can hit up Digi and see if he wants to help."
    pakoo "Ah yes, that's a good idea Arceus. I should ask Aria and Nova if they can help us."
    cs "Is there any specific location we should head to?"
    pakoo "Where are we anyways? Like west of Montana or something?"
    arceus "I think so, I'll let them know to stop somewhere ahead of us, so we'll run into them."
    cs "Alright, I'll keep heading straight."
    pause 2.0
    show cs disappointed
    pakoo "Man, I hope Mika is okay. I don't how I'm gonna explain to them later about this whole situation."  # TODO: This was a CS line, is this fine, Pakoo?
    arceus "I think we're all in the same boat on that problem. I'm sure they'll all be fine."
    jump car_ride_1

label car_ride_1:
    scene black with fade
    n "Meanwhile, Tate's group seems to be having the time of their lives."
    scene jeep_inside_fg
    show drive_day behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "Road trip, let's goooo!"
    tate "Man, I can't believe CS didn't tell us! This is so great!!"
    mika "I know, right?"
    tate "How're you holding up Kitty?"
    kitty "Yeah, I'm doing fine so far."
    tate "Hold up, is that CS in front of us?"
    tate "Heyyyy Mika. {w=0.2}You should smack that horn. {w=0.2}You should do it. {w=0.2}Right now. {w=0.2}You should scare CS. {w=0.2}Do it now."
    if nice_car:
        scene joj_charger_fg
        show drive_day behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_day behind car_inside_fg
    show cs disappointed at left
    show pakoo at right
    with fade
    cs "So yeah, that's why I'm worried."
    show pakoo disappointed
    pakoo "Yeah, I getcha, I'm sur--{w=1.0}{nw}"
    play sound "car_horn.ogg" volume 1
    show cs worried with vpunch
    show pakoo worried with vpunch
    cs "JESUS!!"
    n "CS swerves all over the road after being startled."
    if fun_value(5):
        show pakoo happy
    else:
        show pakoo
    show cs disappointed
    arceus "Yep. I think they are doing just fine."
    scene jeep_inside_fg
    show drive_day behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "Haaahahaha-- *snort*"
    kitty "Oh my goodness!"
    mika "Geez, I didn't think it was that bad."
    tate "Yeah, alright, we had a laugh, but maybe we should chill a bit."
    tate "They've probably been stressed out all day long."
    tate "Anyways, how y'all doing? Wait, I don't think we've ever actually met."
    mika "Well, I'm Mika, and thankfully Pakoo called in time for us to arrive."
    kitty "Hi, I'm Kitty. I hope Arc is doing well enough."
    tate "Hi I'm Tate. Nice to meet y'all."
    tate "Now let's go kick some ass!"
    if nice_car:
        scene joj_charger_fg
        show drive_day behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_day behind car_inside_fg
    show cs at left
    if fun_value(5):
        show pakoo happy at right
    else:
        show pakoo at right
    with fade
    pause 1.0
    arceus "Alright, well it looks like Aria is gonna pick up Digi and Nova, and meet us here soon."
    cs "Wow, that was fast!"
    pakoo "Yeah, that's crazy."
    arceus "They'll meet us at some diner in approximately a few hours from now."
    cs "Alright then, that sounds good to me! I'm hungry so it'll be nice to get some food."
    arceus "Yeah, same."
    stop music fadeout 3.0
    music end
    scene black with fade
    n "As a few hours pass, the DPN crew arrives at the S&P Diner, and waits to be served."
    jump dpn_diner

label dpn_diner:
    scene dinerinside
    show digi at right
    show nova flipped at center
    show aria at left
    with fade
    play music "<from 0 to 86>full_rulle_med_klas.mp3" volume 0.5
    music Full Rulle Med Klas - Lizardking
    digi "Finally, we can stretch our legs again."
    nova "Remind me what you needed me here for again? I have a set later tonight I need to prepare for!"
    digi "CS is in trouble, he's being chased by the cops."
    nova "How in the world are we supposed to help with that?!"
    aria "Don't worry, we can just trail them off with donuts if it gets really rough."
    nova "You sure that will really work??"
    aria "Tried and tested."
    digi "CS and the gang should be passing by soon."
    aria "Shit, they probably don't know where we are located."
    aria "I'll go drive down the highway and lead them here, you guys wait back here just in case."
    nova "Shouldn't we we all go together?"
    aria "Nah, just stay here in case I miss them or something. I'll be fine."
    digi "Aria, are you sure? I mean, the cops are after them."
    aria "Yeah well, like I said, I know what I'm doing. I'll be back."
    hide aria with moveoutright
    pause 1.0
    nova "They're gonna die."
    stop music fadeout 3.0
    music end
    scene black with fade
    scene aria_car_fg
    show drive_night behind aria_car_fg
    show aria at left
    with fade
    pause 3.0
    #TODO: Aria Lines!

    n "As Aria is approaching CS and the gang, they screech on the breaks as they almost run into a blockade."
    hide drive_night
    show cs_somewhere behind aria_car_fg
    play music "<loop 0>dense_woods_b.mp3" volume 0.5
    music Dense Woods B - Kikiyama
    n "Cop cars surround the vicinity of the area."
    n "Aria gets out of the car."
    scene cs_somewhere
    show cop dark at right
    show cop_2 at mid_right
    with fade
    show aria at left with moveinleft
    aria "Ah, great. What is this now?"
    cop "Sorry, but a ragtag group of criminals is heading through this way, so we need to stop them."
    aria "Ah, yeah. I understand."
    aria "I'll just go around the other way."
    show aria flipped with determination
    show aria flipped at offscreenleft with move
    hide aria
    pause 3.0
    show aria at offscreenright with hpunch
    hide cop
    hide cop_2
    with moveoutbottom
    n "As Aria heads back to the car, she sneaks around and knocks the cop's heads together, knocking them out."
    show aria flipped at right with move
    show cop dark at left with moveinleft
    cop "Ah shit! We got two men down! Arrest her!"
    stop music fadeout 3.0
    music end
    music Desert Dawn - Lizardking
    jump rpg_cop_fight_3

label cs_meetup:
    scene cs_somewhere 
    show aria flipped at right
    with fade
    play music "<loop 0>dense_woods_b.mp3" volume 0.5
    n "After Aria takes care of the cops, CS and Tate's group rolls up on the other side of the blockade."
    show cs dark at center
    show arceus dark flipped at mid_left
    show tate dark at left
    with moveinleft
    cs "Woah, what happened here? More cops?"
    if nice_car:
        aria "First of all, nice car! Second of all, they weren't that hard to fight."
    else:
        aria "Yeah, they weren't too much of a problem through."
    tate "Good, the less cops, the better."
    aria "Nova and Digi are at the diner up ahead, let's get this blockade out of the way and get going."
    cs "Righty-o."
    scene black with fade
    n "CS, Aria, and Tate clear the road, and then follow Aria up to the diner."
    n "Meanwhile, back at the diner..."
    window hide
    stop music fadeout 3.0
    scene dinerinside
    show digi at center
    show nova flipped at left
    with fade
    play music "<from 0 to 86>full_rulle_med_klas.mp3" volume 0.5
    pause 2.0
    nova "They are so dead."
    digi "Stop saying that! They are probably fine."
    digi "They should be here any moment now."
    n "While they are talking, flashing lights shine through the diner."
    show digi flipped with determination
    digi "Oh shit! Fuck! It's the cops!"
    nova "Great Digi, see what you did?"
    digi "What did I do? Huh?"
    show cop at right with moveinright
    cop "Hey! We've heard that there are 2 suspects here who are helping out a criminal gang! Show yourselves!"
    n "The people in the diner start freaking out and hide under their seats."
    nova "Alright Digi, let's do this."
    digi "On it."
    stop music fadeout 3.0
    music Full Rulle Med Klas - Lizardking
    jump rpg_cop_fight_4

label cs_meetup_2:
    scene dinerinside
    show digi at center
    show nova flipped at left
    with fade    
    n "After the fight, the rest of the people in the diner flee the scene."
    digi "Wow, holy shit, we did it!"
    nova "Welp, there goes all of my energy for the day."
    nova "I'm beat."
    show aria flipped at right with moveinright
    aria "Hey, we just got here, are you guys okay?"
    show digi flipped with determination
    digi "Yeah, we're fine, how about you?"
    aria "Yeah, I also had to fight some cops on the way to find CS."
    digi "Shit, so we need to get going, like, now, before more come."
    if fun_value(10):
        aria "Yeah, they won't stop coming. Let's meet up with the rest of the crew first."
    else:
        aria "Yeah, they won't stop coming. Fed to the rules and I hit the ground running."
        aria "Let's meet up with the rest of the crew first."
    hide nova
    hide digi
    hide aria
    with moveoutright
    scene black with dissolve
    n "Digi, Aria, and Nova all go outside to meet everyone else."
    scene dineroutside
    play music "<loop 0>la_by_night.mp3" volume 0.5
    music L.A. By Night - Dr. Awesome
    show cs dark flipped at right
    show arceus dark at mid_right
    with fade
    show digi dark flipped at center
    show nova dark flipped at mid_left
    show aria at left
    with moveinleft
    cs "Hey guys! Are you all good?"
    if nice_car:
        digi "Woah damn, when did you get such a nice car?"
        nova "That is a sick ride."
    else:
        digi "Yeah, what about you? What is going on here?"
    cs "Well uhh..."
    if nice_car:
        arceus "We stole this car from a dealership, and then killed some cops."
    else:
        arceus "We had to escape from prison, and killed some cops."
    digi "What?! How did you--"
    cs "Umm, well..."
    arceus "HoH SiS problems."
    digi "Ahhh."
    nova "Does this mean CS is getting cancelled?"
    cs "No no, I'm not gonna get cancelled."
    digi "You killed like, at least a few people!"
    arceus "Yeah, but at least he didn't, like, sell feet pics."
    aria "Or say the N-word."
    digi "Oh, yeah, that clears up everything..."
    arceus "But the cops still don't like that we downed multiple units, so we should get moving about now."
    cs "Yeah, alright everyone, back on the road!"
    cs "Everyone follow me, and we will eventually find a safe spot away from the cops!"
    arceus "Roger that."
    show cs dark with determination
    show arceus dark flipped with determination
    hide cs
    hide arceus
    with moveoutright
    n "Everyone gets back into their cars, and they take off in a convoy, hoping to end this madness soon."
    n "In CS' group, the gang decides what they can do to get away from the cops."
    if nice_car:
        scene joj_charger_fg
        show drive_night behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_night behind car_inside_fg
    show cs at left
    show pakoo at right
    with fade
    cs "I really don't have an idea of where to go, I'm just driving in a straight line."
    arceus "I would try to jam their signals, but I don't know where they are."
    arceus "I haven't seen Copguy since we've fought him."
    pakoo "Well, if he does come back, we'll be ready for him."
    cs "I hope, but at the same time I don't want to think about running into him again."
    cs "I can't go back to prison, that shit was scary."
    arceus "You're telling me."
    cs "I wonder how the others are doing..."
    scene black with dissolve
    window hide
    pause 2.0
    jump car_ride_2

label car_ride_2:
    scene jeep_inside_fg
    show drive_night behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "Man, I'm bored."
    mika "Yeah, what the hell! Where is this Copguy dude at?"
    kitty "What if he's preparing defenses to ambush us?"
    mika "We'll destroy anything that comes our way, don't worry."
    tate "Hell yeah, we gotchu."
    mika "We definitely got this don't worry."
    kitty "I wonder how those new guys are handling the situation..."
    scene black with dissolve
    pause 2.0
    scene aria_car_fg
    show drive_night behind aria_car_fg
    show aria at left
    show digi at right
    with fade
    digi "I can't believe CS went to jail."
    aria "Arceus was in jail for 5 years, Digi."
    digi "Yeah I know, but that's an Arceus thing to do."
    nova "Is it?? That's kinda concerning."
    digi "No, I meant like, he knows what he's doing."
    nova "Clearly not, if he ended up in jail!"
    n "Aria laughs."
    digi "Look, here's the thing, right? I'm just shaken up a bit still after Arceus and Pakoo called us, explaining that they needed help quickly."
    digi "And then we fought and killed cops!"
    aria "Least insane DPN activity."
    digi "Aria, please. I'm legitimately worried about CS."
    aria "They'll be fine, I'm sure this will be over soon."
    digi "Man, I just really hope so."
    scene black with fade
    pause 2.0
    if nice_car:
        scene joj_charger_fg
        show drive_night behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_night behind car_inside_fg
    show cs at left
    show pakoo at right
    with fade
    stop music fadeout 3.0
    music end
    cs "Well, should we find somewhere to stop for the night? We've been going for a while."
    pakoo "Holy shit! Stop CS!"
    hide drive_night
    if nice_car:
        show battle_block_without_theater behind joj_charger_fg
    else:
        show battle_block_without_theater behind car_inside_fg
    n "As CS looks ahead, he screeches on the breaks just in time."
    n "Barbed wire, soldiers, and military trucks block the highway, with Copguy standing in the front of it all."
    cs "This can't be good."
    scene black with fade
    n "The groups behind CS stop as well, as everyone gets out of their cars and approaches Copguy."
    scene battle_block_without_theater
    show copguy dark at mid_right
    show guard_soldier at right
    with fade
    show cs dark angry at center
    show tate dark at mid_left
    show arceus angry dark flipped at mid_left_left
    show digi dark flipped at left
    with moveinleft
    copguy "Well? What do you think CS? You ready to go back to jail?"
    cs "Never!"
    copguy "Oh really? Because I just called the national guard here to help me stop you."
    tate "Yeah well, CS called me to stop you!"
    digi "Yeah! Us too!"
    n "CS' friends start yelling, as the national guard men ready their weapons."
    copguy "I see, you wanted to do this the hard way..."
    copguy "Well, you're gonna find out why you never pick the hard way!"
    if nice_car:
        n "The soldiers seem distracted, aweing at CS' car."
        copguy "Don't mind the car, attack!"
    else:
        copguy "Soldiers! Attack!"
    music Thousand March - Mr. Sauceman
    jump rpg_ng_fight

label cs_rage:
    scene battle_block_without_theater
    show cs dark angry at center
    show tate dark at mid_left
    show arceus dark flipped at mid_left_left
    show digi dark flipped at left
    with fade
    n "After CS and the group manage to push back the national guard, Copguy once again flees at the last moment."
    cs "Hey! You get back here damnit!"
    show cs dark angry at mid_right with move
    show cs dark angry flipped with determination
    cs "Guys let's chase after him!"
    play music "triage_at_dawn.mp3" loop volume 0.6
    music Triage At Dawn - Kelly Bailey
    show arceus worried dark flipped
    arceus "CS, we need a minute. We just fought a tank."
    cs "No time for that! We need to stop him now!"
    tate "CS, no, we really gotta wait a sec."
    show arceus dark flipped
    digi "We're never gonna catch up with him at this point anyways..."
    cs "Fuck! I can't believe this!"
    show cs dark angry with determination
    cs "He keeps running away like a wimp!"
    arceus "CS, you gotta calm down, we can-- "
    show cs dark angry flipped with determination
    cs "Calm down? CALM DOWN?"
    show cs dark angry flipped with hpunch
    cs "Do you know what we just fought through?"
    cs "He's just gonna keep building up stronger units for us to attack, and then run away if we beat him!"
    show cs dark angry with determination
    cs "We need to head out now!"
    show cs dark angry with hpunch
    pause 1.0
    show cs dark angry with vpunch
    pause 1.0
    show cs dark angry with hpunch
    pause 1.0
    show cs dark angry with vpunch
    n "CS goes to the debris from the battle, desperately trying to move it out of the way."
    show cs dark concentrate
    cs "Guys, cmon, please! We have... to... hnngg..."
    tate "Woah, CS? What are you doing?"
    show cs dark concentrate with vpunch
    show cs dark concentrate with hpunch
    show cs dark concentrate with vpunch
    n "All of a sudden, the debris starts moving on it's own!"
    digi "Woah, what's going on?"
    cs "Can you guys please help--"
    show cs dark at center with move
    cs "Wait, what the hell?! Did I move all of that already?"
    n "As CS is gawking at the work he just did, a purple figure appears in front of CS."
    show csgod at right with dissolve  
    csgod "You're welcome."
    cs "Woah, hey! Are you CSGod?"
    csgod "Indeed I am. You've seemed to channel my power through determination."
    if nice_car:
        csgod "Also, it was me who let the intrusive thoughts win for you, and let you pick that nice car."
        cs "Well, thanks for that. This car is amazing!"
        cs "Anyways, can I use YTP Magic or something?"
    else:
        cs "Holy crap, does that mean I can use YTP Magic?"
    csgod "In theory, yes. Although you should take some time to rest."
    csgod "Don't beat yourself up over Copguy, you'll be able to beat him down next time, if you calm down and focus."
    csgod "I'm gonna let you go for now. Copguy is planning his most devious attack yet, and you need to be prepared."
    cs "I see, well, thank you for that CSGod!"
    csgod "No problem."
    hide csgod with dissolve
    n "CSGod fades away, and CS turns back to the group."
    tate "CS, you good? You were just staring up at the sky and talking to yourself about magic or something."
    show cs dark flipped with determination
    cs "I'm all good, don't worry."
    cs "Sorry I got upset, I just need to relax."
    cs "Arc, you drive, I'm gonna lie down in the backseat."
    show arceus worried dark flipped
    arceus "You need, anything else?"
    cs "I'm good, just some rest."
    show arceus dark flipped
    hide cs with moveoutleft
    n "CS heads into the backseat of the car and lies down."
    show digi dark at center with move
    show arceus dark flipped at left with move
    digi "Alright well, what's the plan? CS is technically right, we need to go track down Copguy somehow."
    arceus "I managed to put a tracking device on Copguy's car in the heat of the battle."
    arceus "I'll be following him, and I'll update you guys about what's going on."
    show arceus dark with determination
    hide arceus with moveoutleft
    digi "Roger."
    tate "Alright, let's go kick Copguy's ass!"
    show tate dark flipped with determination
    hide digi
    hide tate
    with moveoutleft
    scene black with fade
    n "The crew gets in their respective cars, and they take off."
    stop music fadeout 3.0
    music end
    scene black with fade
    jump copguy_pres

label copguy_pres:
    n "After Copguy fled the scene, he immediately went to summarize the bad news to the sheriff."
    scene police_car_fg
    show copguy flipped at left
    show drive_night behind police_car_fg
    with fade
    sheriff "They WHAT??"
    copguy "They blew up our tank, sir."
    sheriff "Shit! Urghhh..."
    sheriff "There is only one thing we can do."
    sheriff "Copguy, call this number."
    n "The sheriff sends Copguy the phone number and he dials it."
    copguy "Hello?"
    if fun_value(20):
        bomaha "Who is this?"
        bomaha "How did you get this number?"
        copguy "Hey Mr. President, it's me, Copguy. There is a ragtag gang of criminals on the loose that we can't stop."
        copguy "We sent the Montana National Guard to stop them, and this gang plowed right through them."
        bomaha "I see."
        bomaha "Looks like we'll have to pull out the big guns."
    else:
        obama "Who is this?"
        obama "How did you get this number?"
        copguy "Hey Mr. President, it's me, Copguy. There is a ragtag gang of criminals on the loose that we can't stop."
        copguy "We sent the Montana National Guard to stop them, and this gang plowed right through them."
        obama "I see."
        obama "Looks like we'll have to pull out the big guns."
    if fun_value(20):
        bomaha "You are gonna head to Chigaco, I'll have a jet come pick you up."
    else:
        obama "You are gonna head to Chicago, I'll have a jet come pick you up."
    copguy "Thank you sir, I won't stop till this group is defeated."
    scene black with dissolve
    window hide
    jump car_ride_3

label car_ride_3:
    #TODO: Car dialogue
    if nice_car:
        scene joj_chargerarc_fg
        show drive_night behind joj_chargerarc_fg
    else:
        scene car_insidearc_fg
        show drive_night behind car_insidearc_fg
    show arceus flipped at left
    show pakoo at right
    with fade
    play music "the_whale.mp3" loop volume 0.6
    music The Whale - Dr. Awesome
    n "While they are driving, Arceus notices that copguy starts ludicrously speeding up until he stops in Illinois."
    arceus "Guys, I think I found out where Copguy is headed."
    if fun_value(20):
        arceus "He's stopped in Chigaco."
    else:
        arceus "He's stopped in Chicago."
    pakoo "Ah shoot."
    cs "I'm gonna ping everyone in CSCord, and see if anyone else is able to help us out."
    cs "We're gonna need it."
    scene black with fade
    pause 2.0
    scene aria_car_fg
    show drive_night behind aria_car_fg
    show aria at left
    show digi at right
    with fade
    nova "So I guess this is my night. I really need to catch up with music stuff when I get home."
    digi "Guys, I'm concerned that CS might actually be going insane."
    aria "Digi, you didn't know that from the start?"
    digi "Did you see him? He was just, talking to the sky!"
    nova "Yeah? Well let a man talk to the sky!"
    digi "But he was absolutely going insane!"
    aria "Digi, you gotta learn that the spectrum hits different for everyone."
    scene black with fade
    pause 2.0
    scene jeep_inside_fg
    show drive_night behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "So I went to Dollar Tree a couple days ago, right? Bought some of their off-brand snacks..."
    mika "I feel like only a few off-brands can taste well, but there are a few I just can't eat."
    tate "Saaaaame, which ones?"
    mika "Usually the off-brand Cheez-its, but I really don't like the off-brand goldfish either."
    tate "Wait, you don't like gold whales?! I love those!"
    mika "Well, I just don't like them too much."
    kitty "The snack that breaks your back: Gold Whales!"
    n "They all laugh."
    stop music fadeout 3.0
    music end
    scene black with fade
    jump final_meetup

label final_meetup:
    if nice_car:
        scene joj_chargerarc_fg
        show final_destination behind joj_chargerarc_fg
    else:
        scene car_insidearc_fg
        show final_destination behind car_insidearc_fg
    show arceus flipped at left
    show pakoo at right
    with fade
    play music "prophet_2001.mp3" loop volume 0.6
    music Prophet 2001 - Dr. Awesome
    arceus "Alright, we are here."
    pakoo "So, who is joining us to help fight Copguy?"
    cs "Let's go take a look."
    scene black with fade
    n "The groups all get out of their cars and meet up with one another."
    scene final_destination with fade
    show cs at mid_left
    show tate at left
    with moveinleft
    n "The last group to meet up all emerge as well, who are:"
    #TODO: Intro thingy
    show blank at center with moveinright
    blank "Hi!"
    $ renpy.movie_cutscene("movies/blank.webm")
    show anno at mid_right with moveinright
    anno "Yo."
    $ renpy.movie_cutscene("movies/anno.webm")
    show midge at right behind anno with moveinright
    midge "Oh hai."
    $ renpy.movie_cutscene("movies/midge.webm")
    $ achievement_manager.unlock("A Little Help From My Friends")
    if nice_car:
        "Blank, Anno, and Midge" "Nice car!"
        cs "Thanks! I've heard that a lot today."
    else:
        cs "Nice to finally meet you guys! Where's DB?"
    anno "Db05 isn't here yet, he's been busy."
    anno "He'll be here soon though, we've been talking to him on the phone."
    n "Anno holds out his phone."
    db "Hey guys! Sorry I'm gonna miss out on the huge battle thing, I had to do some things at home first."
    $ renpy.movie_cutscene("movies/db.webm")
    db "But I'll gladly encourage you while you all are fighting!"
    cs "No problem DB! Every little bit helps!"
    tate "Y'all ready?"
    cs "Hell yeah! Let's go put Copguy through the slammer!"
    stop music fadeout 3.0
    music end
    scene black with fade
    music Trans Atlantic - Lizardking
    jump rpg_final_fight_1

label weapon_of_choice:
    pause 1.0
    $ renpy.movie_cutscene("movies/woc.webm")
    $ achievement_manager.unlock("Hopes and Dreams")
    jump car_slam

label car_slam:
    scene war_torn_1 with fade
    n "CS looks around, and views the destruction around him."
    n "The city that they once fought in has now been reduced to rubble and war-torn buildings."
    show cs flipped at right with moveinbottom
    n "CS gathers his bearings, and starts checking on his friends."
    cs "Hello? Are you guys alright?"
    show arceus flipped at mid_left with moveinleft
    arceus "Did we get him?"
    show pakoo flipped at left with moveinleft
    pakoo "Man, that was insane. You guys demolished this place!"
    cs "I hope Copguy is dead. I am definitely going to jail for this one if he's alive!"
    n "CS continues to check on the others."
    hide cs with moveoutleft
    scene black with fade
    pause 1.0
    scene war_torn_2
    show tate at mid_left
    show mika at center
    show kitty flipped at right
    with fade
    tate "Y'all see that shit?!"
    mika "CS crushed the whole city!"
    show cs at mid_right with moveinleft
    cs "Hey guys! Are you all alright?"
    kitty "Yeah, we're alright. I'm assuming you're fine?"
    cs "Better than ever! Although, that did wear me out quite a bit."
    cs "I'm gonna go see how the rest are doing."
    hide cs with moveoutright
    scene black with fade
    pause 1.0
    scene war_torn_3
    show digi at mid_left
    show nova at center
    show aria flipped at right
    with fade
    show cs at left with moveinleft
    digi "Holy shit! CS! You're alive!"
    cs "Yeah! How about you guys?"
    nova "I wanna fall over, I'm so tired."
    if fun_value(20):
        aria "I never thought that our first meetup would be at a mall, and our second would be the destruction of Chigaco."  
    else:  
        aria "I never thought that our first meetup would be at a mall, and our second would be the destruction of Chicago."
    n "CS laughs."
    cs "Yeah, me either, Aria."
    cs "There is one last group to check on."
    hide cs with moveoutright
    scene black with fade
    pause 1.0
    scene war_torn_5
    show midge at mid_left
    show anno at center
    show blank at right
    with fade
    show cs at mid_right with moveinleft
    cs "Hey, did DB ever make it to the fight?"
    anno "No, I never saw him, at least."
    blank "Anno's phone got busted during the fight, so we won't know now what his progress was."
    cs "Dang, that's a shame."
    cs "I kinda hope he doesn't come now, I'd hate for him to witness the damage we did."
    midge "Well, we won right? What's the plan now?"
    cs "I wanna make sure Copguy is gone for real."
    cs "I will be right back."
    hide cs with moveoutright
    scene black with fade
    pause 1.0
    scene war_torn_4 with fade
    show cs at left with moveinleft
    n "CS walks through the wastelands, searching for any thing reminiscent to Copguy."
    n "Sure enough, he finds Copguy's wrecked cop car."
    show cs at center with move
    cs "Welp. There rests Cop guy."
    cs "He fought well, he was a good cop, and god rest his soul."
    pause 3.0
    show cs flipped
    cs "Nahhh! That guy was a jerk!"
    cs "This is why you don't mess with the Master Of The Poop!"
    cs "The Youtube Poop, actually. I realized that kinda sounded stupid."
    n "CS turns around and walks away."
    show cs flipped at mid_left with move
    show copguycrawl at mid_right with moveinbottom
    show copguycrawl with vpunch
    copguy "Damnit, you can't escape from me!"
    n "Copguy manages to crawl out of the rubble that is his car."
    show cs worried
    cs "Holy what? How did you--"
    copguy "I'm not gonna let you win that easily, CS."
    n "Copguy pulls out his sidearm."
    copguy "Or should I say,"
    show db_cooper at offscreenright
    copguy "C--{w=0.5}{nw}"
    show db_cooper at right with moveinleft
    show copguycrawl with hpunch
    hide copguycrawl with moveoutbottom
    show cs worried at left with move
    db "Hey guys! I finally made it!"
    db "Sorry I was late, I had to feed the pets back at home and--"
    cs "DB, you did it!"
    db "What? What'd I do?"
    show cs
    cs "You killed Copguy!"
    db "Oh no, does that mean I'm gonna go to jail?"
    db "I can't go! Who's gonna take care of everything back at home?"
    cs "Relax, we destroyed the majority of the police force."
    db "Wait, so does that mean, we were the bad guys all along?"
    cs "Nah."
    cs "That man was like, deranged."
    scene black with dissolve
    pause 1.0
    $ renpy.movie_cutscene("movies/wherearetheynow.webm")
    pause 1.0
    $ renpy.end_replay()
    return
