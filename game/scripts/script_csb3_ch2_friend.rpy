label friend2_dpn_call:
    if nice_car:
        scene joj_charger_fg
        show drive_day behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_day behind car_inside_fg
    show cs disappointed at left
    show pakoo at right
    with dissolve
    play music tuna_fish loop volume 0.6 if_changed
    music tuna_fish
    cs "What a crazy day so far, man."
    show cs worried
    if fun_value(FUN_VALUE_MUSIC):
        cs "I can't believe we had to fight all of those cops! If it weren't for Tate and the gang, we'd be tuna fish already."
    else:
        cs "I can't believe we had to fight all of those cops! If it weren't for Tate and the gang, we'd be dead meat already."
    arceus "Yeah, but, hey, you held them off pretty well with that fancy gun of yours."
    pakoo "Yeah, that was some great marksmanship, CS!"
    show cs happy
    cs "Thank you!"
    show cs
    arceus "So, now that we're on the road, and we have time to think, what is our plan?"
    arceus "Copguy's gonna come back, so we need to think fast."
    cs "Is there anyone else we can call for help?"
    arceus "There are a few people. I can hit up Digi and see if he wants to help."
    pakoo "Ah, yes, that's a good idea, Arceus. I should ask Aria and Nova if they can help us."
    cs "Is there any specific location we should head to?"
    pakoo "Where are we, anyway? Like, west of Montana, or something?"
    arceus "I think so. I'll let them know to stop somewhere ahead of us, so we'll run into them."
    cs "Alright, I'll keep heading straight."
    pause 2.0
    show cs disappointed
    pakoo "Man, I hope Mika is okay. I don't how I'm gonna explain this whole situation to them later."
    arceus "I think we're all in the same boat on that problem. I'm sure they'll all be fine."
    jump friend2_car_ride_1

label friend2_car_ride_1:
    play music tuna_fish loop volume 0.6 if_changed
    music tuna_fish
    scene black with dissolve
    n "Meanwhile, Tate's group seems to be having the time of their life."
    scene jeep_inside_fg
    show drive_day behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with dissolve
    tate "Road trip, let's goooo!"
    tate "Man, I can't believe CS didn't tell us! This is great!"
    mika "I know, right?"
    tate "How're you holding up, Kitty?"
    kitty "Yeah... I'm doing okaye.."
    show tate shock flipped
    tate "Hold up, is that CS in front of us?"
    show tate smug flipped
    tate "Heyyyy, Mika. {w=0.2}You should smack that horn. {w=0.2}You should do it. {w=0.2}Right now. {w=0.2}You should scare CS. {w=0.2}Right now. {w=0.2}{cshake}Do it now."
    if nice_car:
        scene joj_charger_fg
        show drive_day behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_day behind car_inside_fg
    show cs disappointed at left
    show pakoo at right
    with dissolve
    cs "So, yeah, that's why I'm worried."
    show pakoo disappointed
    pakoo "Yeah, I getcha, I'm sur--{w=1.0}{nw}"
    play sound sfx_car_horn
    show cs scared with vpunch
    show pakoo worried with vpunch
    cs "JESUS!!"
    n "CS swerves all over the road after being startled."
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        show pakoo happy
    else:
        show pakoo
    show cs disappointed
    arceus "Yep. I think they are doing just fine."
    scene jeep_inside_fg
    show drive_day behind jeep_inside_fg
    show mika at left
    show tate smug flipped at right
    with dissolve
    tate "Haaahahaha-- {i}snort{/i}"
    kitty "Bloody hell!"
    mika "Jeez, I didn't think it was {i}that{/i} bad."
    show tate flipped
    tate "Yeah, alright, we had a laugh, but maybe we should chill a bit." # TODO: not a fan of this line even though yes i know i wrote it - tate
    tate "They've probably been stressed out all day long."
    tate "Anyways, how're y'all doing? Wait, I don't think we've ever actually met."
    mika "Well, I'm Mika. Thankfully, Pakoo called in time for us to arrive."
    kitty "Hi, I'm Kitty. I hope Arcie is doing well enough."
    tate "Howdy, I'm Tate. Nice to meet y'all."
    show tate smug flipped
    tate "Now, let's go kick some ass!"
    if nice_car:
        scene joj_charger_fg
        show drive_day behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_day behind car_inside_fg
    show cs at left
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        show pakoo happy at right
    else:
        show pakoo at right
    with dissolve
    pause 1.0
    arceus "Alright, well, it looks like Aria is gonna pick up Digi and Nova. They'll meet us here soon."
    cs "Wow, that was fast!"
    pakoo "Yeah, that's crazy."
    arceus "They'll meet us at some diner a few hours away."
    cs "Alright, then, that sounds good to me! I'm hungry, so it'll be nice to get some food."
    arceus "Yeah, same."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "A few hours pass and the DPN crew arrives at the S&P Diner. They chat as they wait to be served."
    jump friend2_dpn_diner

label friend2_dpn_diner:
    scene dinerinside
    show digi at right
    show nova flipped at center
    show aria at left
    with dissolve
    play music full_rulle_med_klas volume 0.5 if_changed
    music full_rulle_med_klas
    if fun_value(FUN_VALUE_MUSIC):
        digi "Finally, we can fully rulle our med klas again."
        nova "What?"
        digi "Dude I don't how I was supposed to make that work!"
        nova "Whatever."
    else:
        digi "Finally, we can stretch our legs again."
    nova "Remind me of what you needed me here for, again? I have a set later tonight I need to prepare for!"
    digi "CS is in trouble. He's being chased by the cops."
    nova "How in the world are we supposed to help with that?!"
    aria "Don't worry. We can just trail them off with donuts if it gets really rough."
    nova "You sure that will really work??"
    aria "Tried and tested."
    digi "CS and the gang should be passing by soon."
    aria "Shit, they probably don't know where we are located."
    aria "I'll go drive down the highway and lead them here. You guys wait back here, just in case."
    nova "Shouldn't we we all go together?"
    aria "Nah, just stay here in case I miss them or something. I'll be fine."
    digi "Aria, are you sure? I mean, the cops are after them."
    aria "Yeah, well, like I said, I know what I'm doing. I'll be back."
    hide aria with moveoutright
    pause 1.0
    nova "They're gonna die."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    scene aria_car_fg
    show drive_night behind aria_car_fg
    show aria at left
    with dissolve
    pause 3.0
    n "As Aria approaches CS and the gang, she slams on the brakes, tires screeching as she almost runs into a blockade."
    hide drive_night
    show cs_somewhere behind aria_car_fg
    play music dense_woods_b volume 0.5 if_changed
    music dense_woods_b
    if fun_value(FUN_VALUE_MUSIC):
        n "Cop cars surround the vicinity of Dense woods B."
    else:
        n "Cop cars surround the vicinity of the area."
    n "Aria gets out of the car."
    scene cs_somewhere
    show cop dark at right
    show cop_2 at mid_right
    with dissolve
    show aria dark at left with moveinleft
    aria "Ah, great. What is this, now?"
    cop "Sorry, but a ragtag group of criminals is heading this way. We need to stop them."
    aria "Ah, yeah. I understand."
    aria "I'll just go around the other way."
    show aria dark flipped with determination
    show aria dark flipped at offscreenleft with move
    hide aria
    pause 3.0
    show aria dark at offscreenright with hpunch
    hide cop
    hide cop_2
    with moveoutbottom
    n "As Aria heads back to the car, she sneaks around and knocks the cop's heads together, rendering them unconcious."
    show aria dark flipped at right with move
    show cop dark at left with moveinleft
    if fun_value(FUN_VALUE_MUSIC):
        cop "Ah, shit! We've got two men down! Arrest her! This is a code Desert Dawn!"
    else:
        cop "Ah, shit! We've got two men down! Arrest her!"
    stop music fadeout 3.0
    music end
    jump rpg_cop_fight_3

label friend2_cs_meetup:
    scene cs_somewhere
    show aria dark flipped at right
    with dissolve
    play music dense_woods_b volume 0.5 if_changed
    music dense_woods_b
    n "After Aria takes care of the cops, CS and Tate's group rolls up on the other side of the blockade."
    show cs dark at center
    show arceus dark flipped at mid_left
    show tate dark at left
    with moveinleft
    show cs worried dark
    cs "Woah, what happened here? More cops?"
    if nice_car:
        aria "First of all, nice car! Second of all, they weren't that hard to fight."
    else:
        aria "Yeah, they weren't too much of a problem, through."
    show cs disappointed dark
    tate "Good. The less cops, the better."
    aria "Nova and Digi are at the diner up ahead. Let's move this blockade out of the way and get going."
    cs "Righty-o."
    scene black with dissolve
    n "CS, Aria, and Tate clear the road. The group then proceeds to follow Aria back to the diner."
    n "Meanwhile, back at the diner..."
    window hide
    stop music fadeout 3.0
    scene dinerinside
    show digi at center
    show nova flipped at left
    with dissolve
    play music full_rulle_med_klas volume 0.5 if_changed
    music full_rulle_med_klas
    pause 2.0
    nova "They are so dead."
    digi "Stop saying that! They are probably fine."
    digi "They should be here any moment now."
    n "As they are talking, flashing lights fill the diner."
    show digi flipped with determination
    digi "Oh, shit! Fuck! It's the cops!"
    nova "Great, Digi, see what you did?"
    digi "What did I do? Huh?"
    show cop at right with moveinright
    cop "Hey! We've heard that there are two suspects here who are helping out a criminal gang! Show yourselves!"
    n "The other patrons start freaking out and hide under their seats."
    nova "Alright, Digi, let's do this."
    digi "On it."
    stop music fadeout 3.0
    jump rpg_cop_fight_4

label friend2_cs_meetup_2:
    stop music fadeout 3.0
    music end
    scene dinerinside
    show digi at center
    show nova flipped at left
    with dissolve
    n "After the fight, the rest of the people in the diner flee from the scene."
    digi "Wow, holy shit, we did it!"
    nova "Welp, there goes all of my energy for the day."
    nova "I'm beat."
    show aria flipped at right with moveinright
    aria "Hey, we just got here. Are you guys okay?"
    show digi flipped with determination
    digi "Yeah, we're fine. How about you?"
    aria "Yeah, I also had to fight some cops on the way to find CS."
    digi "Shit, so we need to get going, like, {i}now{/i}, before more come."
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        aria "Yeah, they won't stop coming. Let's meet up with the rest of the crew first."
    else:
        aria "Yeah, they won't stop coming. Fed to the rules, and I hit the ground running."
        aria "Let's meet up with the rest of the crew first."
    hide nova
    hide digi
    hide aria
    with moveoutright
    scene black with dissolve
    if fun_value(FUN_VALUE_MUSIC):
        n "Digi, Aria, and Nova all go outside to meet everyone at L.A. by night."
    else:
        n "Digi, Aria, and Nova all go outside to meet everyone else."
    scene dineroutside
    play music la_by_night volume 0.5 if_changed
    music la_by_night
    show cs dark flipped at right
    show arceus dark at mid_right
    with dissolve
    show digi dark flipped at center
    show nova dark flipped at mid_left
    show aria dark at left
    with moveinleft
    cs "Hey, guys! Are you all good?"
    if nice_car:
        digi "Woah, damn, when did you get such a nice car?"
        nova "That is a sick ride."
    else:
        digi "Yeah, what about you? What is going on here?"
    show cs worried dark flipped
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
    show cs dark flipped
    cs "No, no, I'm not gonna get cancelled."
    digi "You killed, like, at least a few people!"
    arceus "Yeah, but at least he didn't, like, sell feet pics."
    aria "Or say the N-word."
    digi "Oh, yeah, that clears up everything..."
    if fun_value(FUN_VALUE_EPIC):
        arceus "But, the cops still don't like that we downed multiple--{nw}"
        show boom at t_boom
        $ collect("boom")
        $ renpy.music.set_pause(True, "music")
        arceus "..."
        cs "I think the boom mic is in the shot."
        aria "I'm shocked this is the first time that's happened, frankly."
        show digi flipped dark at little_bounce
        digi "I can't reach it..."
        aria "You grabbing it isn't going to help, either. Why would that do that anything?"
        direct "Can we please raise the boom mic out of the shot?"
        nova "I'm so tired, guys. Are we nearly done with this scene?"
        n "CS checks the script."
        cs "Yeah, there's only, like, six more lines after this, and then we change scenes."
        hide boom
        n "The boom mic is raised out of frame."
        direct "Thank you! Okay, just restart the line you were on, Arc!"
        arceus "You got it, boss."
        play sound sfx_clapperboard
        $ renpy.music.set_pause(False, "music")
    arceus "But, the cops still don't like that we downed multiple units, so we should get moving right now."
    cs "Yeah. Alright everyone, back on the road!"
    cs "Everyone, follow me! We will eventually find a safe spot away from the cops!"
    arceus "Roger that."
    show cs dark with determination
    show arceus dark flipped with determination
    hide cs
    hide arceus
    with moveoutright
    n "The group splits off to get back into their cars before leaving as a convoy, hoping to end this madness soon."
    n "In CS' group, the gang decides on what they can do to get away from the cops."
    if nice_car:
        scene joj_charger_fg
        show drive_night behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_night behind car_inside_fg
    show cs disappointed at left
    show pakoo at right
    with dissolve
    cs "I really don't have any idea of where to go. I'm just driving in a straight line."
    arceus "I would try to jam their signals, but I don't know where they are."
    arceus "I haven't seen Copguy since we fought him."
    pakoo "Well, if he does come back, we'll be ready for him."
    cs "I hope, but, at the same time, I don't want to think about running into him again."
    cs "I can't go back to prison. That shit was scary."
    arceus "You're telling me."
    cs "I wonder how the others are doing..."
    scene black with dissolve
    window hide
    pause 2.0
    jump friend2_car_ride_2

label friend2_car_ride_2:
    play music la_by_night volume 0.5 if_changed
    music la_by_night
    scene jeep_inside_fg
    show drive_night behind jeep_inside_fg
    show mika at left
    show tate srs flipped at right
    with dissolve
    tate "Man, I'm bored."
    mika "Yeah, what the hell! Where is this Copguy dude at?"
    kitty "What if he's preparing defenses to ambush us?"
    mika "We'll destroy anything that comes our way, don't worry."
    show tate flipped
    tate "Hell yeah, we've got this!"
    mika "We've definitely got this, don't worry."
    kitty "I wonder how those new guys are handling the situation..."
    scene black with dissolve
    pause 2.0
    scene aria_car_fg
    show drive_night behind aria_car_fg
    show aria at left
    show digi at right
    with dissolve
    digi "I can't believe CS went to jail."
    aria "Arceus was in jail for five years, Digi."
    digi "Yeah, I know, but... that's an Arceus thing to do."
    nova "Is it? That's kinda concerning."
    digi "No, I meant, like, he knows what he's doing."
    nova "Clearly {i}not,{/i} if he ended up in {i}jail!"
    n "Aria laughs."
    digi "Look, here's the thing, right? I'm just shaken up a bit still after Arceus and Pakoo called us explaining that they needed help quickly."
    digi "And then, we fought and killed cops!"
    aria "Least insane DPN activity."
    digi "Aria, please. I'm legitimately worried about CS."
    aria "He'll be fine. I'm sure this will be over soon."
    digi "Man, I just really hope so..."
    scene black with dissolve
    pause 2.0
    if nice_car:
        scene joj_charger_fg
        show drive_night behind joj_charger_fg
    else:
        scene car_inside_fg
        show drive_night behind car_inside_fg
    show cs at left
    show pakoo at right
    with dissolve
    stop music fadeout 3.0
    music end
    cs "Well, should we find somewhere to stop for the night? We've been going for a while."
    pakoo "Holy shit! Stop, CS!"
    play sound sfx_tiresqueal
    show cs scared with vpunch
    with vpunch
    with vpunch
    hide drive_night
    if nice_car:
        show battle_block_without_theater behind joj_charger_fg
    else:
        show battle_block_without_theater behind car_inside_fg
    n "As CS looks ahead, he screeches on the brakes just in time."
    n "Barbed wire, soldiers, and military trucks block the highway, with Copguy standing in the front of it all."
    cs "This can't be good."
    scene black with dissolve
    n "The groups behind CS stop as well. Everyone gets out of their cars to approach Copguy."
    scene battle_block_without_theater
    show copguy dark at mid_right
    show guard_soldier at right
    with dissolve
    show cs dark angry at center
    show tate srs dark at mid_left
    show arceus angry dark flipped at mid_left_left
    show digi dark flipped at mid_offscreen_left
    with moveinleft
    copguy "Well? What do you think, CS? You ready to go back to jail?"
    cs "Never!"
    copguy "Oh, really? Because I just called the National Guard here to help me stop you."
    tate "Yeah, well, CS called me to stop you!"
    digi "Yeah! Us too!"
    n "CS' friends start yelling as the National Guard men ready their weapons."
    copguy "I see. You want to do this the hard way..."
    copguy "Well, you're gonna find out why you never pick the hard way!"
    if nice_car:
        n "The soldiers seem distracted, aweing at CS' car."
        if fun_value(FUN_VALUE_MUSIC):
            copguy "Don't mind the car! Begin the Thousand March!"
        else:
            copguy "Don't mind the car! Attack!"
    if fun_value(FUN_VALUE_MUSIC):
        copguy "Soldiers! Begin the Thousand March!"
    else:
        copguy "Soldiers! Attack!"
    jump rpg_ng_fight

label friend2_cs_rage:
    stop music fadeout 3.0
    music end
    scene battle_block_without_theater
    show cs dark angry at center
    show tate dark at mid_left
    show arceus dark flipped at left
    show digi dark flipped at mid_offscreen_left
    with dissolve
    n "After CS and his friends manage to push back the National Guard, Copguy once again flees at the last moment."
    cs "Hey! You get back here, damn it!"
    show cs dark angry at mid_right with move
    show cs dark angry flipped with determination
    cs "Guys, let's chase after him!"
    play music triage_at_dawn loop volume 0.6 if_changed
    music triage_at_dawn
    show arceus worried dark flipped
    if fun_value(FUN_VALUE_MUSIC):
        arceus "CS, we need a minute."
        arceus "We just had a Triage, and it's almost dawn!"
    else:
        arceus "CS, we need a minute. We just fought a tank."
    cs "No time for that! We need to stop him {i}now!{/i}"
    show tate srs dark
    tate "CS, no. We've really gotta wait a sec."
    show arceus dark flipped
    digi "We're never gonna catch up with him at this point anyway..."
    cs "Fuck! I can't believe this!"
    show cs dark angry with determination
    cs "He keeps running away like a wimp!"
    arceus "CS, you gotta calm down, we can-- "
    show cs dark angry flipped with determination
    cs "Calm down? {i}Calm down?!{/i}"
    show cs dark angry flipped with hpunch
    cs "Do you know what we just fought through?"
    cs "He's just gonna keep building up stronger units for us to attack, and then run away if we beat him!"
    show cs dark angry with determination
    cs "We {i}need{/i} to head out {i}now!{/i}"
    show cs dark angry with hpunch
    pause 1.0
    show cs dark angry with vpunch
    pause 1.0
    show cs dark angry with hpunch
    pause 1.0
    show cs dark angry with vpunch
    n "CS approaches the debris from the battle and desperately tries to push it out of the way."
    show cs dark concentrate
    cs "Guys, c'mon, please! We have... to... hnngg..."
    show tate shock dark
    tate "Woah, CS? What are you doing?!"
    show cs dark concentrate with vpunch
    show cs dark concentrate with hpunch
    show cs dark concentrate with vpunch
    n "All of a sudden, the debris starts moving on its own!"
    digi "Woah, what's going on?"
    cs "Can you guys please help--"
    show cs worried dark at center with move
    cs "Wait, what the hell?! Did I move all of that already?"
    show tate dark
    n "As CS is gawking at the work he just did, a purple figure appears before him."
    hide tate
    hide arceus
    hide digi
    with moveoutleft
    show cs worried dark at left with move
    show csgod at right with dissolve
    csgod "You're welcome."
    cs "Woah, hey! Are you CSGod?"
    csgod "Indeed, I am. You seem to have channeled my power through determination."
    if fun_value(FUN_VALUE_EPIC):
        play sound sfx_vine
        show toby at t_toby
    if nice_car:
        csgod "Also, it was I who allowed your intrusive thoughts to win, compelling you to pick that nice car."
        # i mean, he's a god, so he should probably speak like a god, goddammit - tate
        show cs happy dark
        cs "Well, thanks for that. This car is amazing!"
        cs "Anyways, can I use YTP Magic or something?"
    else:
        cs "Holy crap, does that mean I can use YTP Magic?"
    show cs dark
    csgod "In theory, yes. Although, you should take some time to rest."
    csgod "Do not beat yourself up over Copguy. You will be able to defeat him if you calm down and focus."
    csgod "I shall let you go for now. Copguy is planning his most devious attack yet, and you need to be prepared."
    show cs dark
    cs "I see. Well, thank you for that, CSGod!"
    csgod "No problem."
    hide csgod with dissolve
    n "CSGod fades away, and CS turns back to the group."
    show cs dark at right with move
    show cs dark flipped with determination
    show tate dark at mid_left
    show arceus dark flipped at mid_left_left
    show digi dark flipped at mid_offscreen_left
    with moveinleft
    show tate shock dark
    tate "CS, you good? You were just staring up at the sky, talking to yourself about magic, or something."
    show tate dark
    cs "I'm all good, don't worry."
    cs "Sorry I got upset. I just need to relax."
    cs "Arc, you drive. I'm gonna lie down in the back seat."
    show arceus worried dark flipped
    arceus "You need anything else?"
    cs "I'm good. Just some rest."
    show arceus dark flipped
    hide cs with moveoutleft
    n "CS heads into the back seat of the car and lies down."
    show digi dark at center with move
    show arceus dark flipped at left with move
    digi "Alright, well, what's the plan? CS is technically right. We need to go track down Copguy somehow."
    arceus "I managed to put a tracking device on Copguy's car in the heat of the battle."
    arceus "I'll be following him, and I'll update you guys about what's going on."
    show arceus dark with determination
    hide arceus with moveoutleft
    digi "Roger."
    show tate srs dark
    tate "Alright, let's go kick Copguy's ass!"
    show tate dark flipped with determination
    hide digi
    hide tate
    with moveoutleft
    scene black with dissolve
    n "The crew takes off after getting back in their respective cars."
    jump friend2_copguy_pres

label friend2_copguy_pres:
    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "After Copguy fled the scene, he immediately called to summarize the bad news to the sheriff."
    scene police_car_fg
    show copguy flipped at left
    show drive_night behind police_car_fg
    with dissolve
    sheriff "They {i}what?!{/i}"
    copguy "They blew up our tank, sir."
    sheriff "Shit! Urghhh..."
    sheriff "There is only one thing we can do."
    sheriff "Copguy, call this number."
    n "The sheriff sends Copguy the phone number, and Copguy dials it."
    copguy "Hello?"
    if fun_value(FUN_VALUE_RARE):
        bomaha "Who is this?"
        bomaha "How did you get this number?"
        copguy "Hey Mr. President, it's me, Copguy. There is a ragtag gang of criminals on the loose that we can't stop."
        copguy "We sent the Montana National Guard to stop them, and this group plowed right through them."
        bomaha "I see."
        bomaha "Looks like we'll have to pull out the big guns."
    else:
        obama "Who is this?"
        obama "How did you get this number?"
        copguy "Hey Mr. President, it's me, Copguy. There is a ragtag gang of criminals on the loose that we can't stop."
        copguy "We sent the Montana National Guard to stop them, and this group plowed right through them."
        obama "I see."
        obama "Looks like we'll have to pull out the big guns."
    if fun_value(FUN_VALUE_RARE):
        bomaha "You are gonna head to Chigaco. I'll have a jet come pick you up."
    else:
        obama "You are gonna head to Chicago. I'll have a jet come pick you up."
    copguy "Thank you, sir. I won't stop until these menaces are behind bars."
    scene black with dissolve
    window hide
    jump friend2_car_ride_3

label friend2_car_ride_3:
    if nice_car:
        scene joj_chargerarc_fg
        show drive_night behind joj_chargerarc_fg
    else:
        scene car_insidearc_fg
        show drive_night behind car_insidearc_fg
    show arceus flipped at left
    show pakoo at right
    with dissolve
    play music the_whale loop volume 0.6 if_changed
    music the_whale
    if fun_value(FUN_VALUE_MUSIC):
        n "While they are driving, Arceus notices that The Whale starts ludicrously speeding up until he stops in Illinois."
        show arceus worried flipped
        arceus "What the hell is that?"
        cs "What is it, Arceus?"
        show arceus flipped
        arceus "Sorry, I thought I saw a flying whale on the GPS, but it was just Copguy."
    else:
        n "While they are driving, Arceus notices that Copguy starts ludicrously speeding up until he stops in Illinois."
    arceus "Guys, I think I found out where Copguy is headed."
    if fun_value(FUN_VALUE_COMMON):
        arceus "He's stopped in Chigaco."
    else:
        arceus "He's stopped in Chicago."
    pakoo "Ah, shoot."
    cs "I'm gonna ping everyone in CSCord and see if anyone else is able to help us out."
    cs "We're gonna need it."
    scene black with dissolve
    pause 2.0
    scene aria_car_fg
    show drive_night behind aria_car_fg
    show aria at left
    show digi at right
    with dissolve
    nova "So, I guess this is my night. I really need to catch up with music stuff when I get home."
    digi "Guys, I'm concerned that CS might actually be going insane."
    aria "Digi, you didn't know that from the start?"
    digi "Did you see him? He was just... talking to the sky!"
    nova "Yeah? Well, let a man talk to the sky!"
    digi "But he was going absolutely insane!"
    aria "Digi, you've gotta learn that the spectrum hits different for everyone."
    scene black with dissolve
    pause 2.0
    scene jeep_inside_fg
    show drive_night behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with dissolve
    tate "So I went to Dollar Tree a couple days ago, right? Bought some of their off-brand snacks--"
    mika "I feel like only a few off-brands are good. I just can't eat most of them."
    tate "Saaaaame, which ones?"
    mika "Usually the off-brand Cheez-its, but I really don't like the off-brand Goldfish either."
    show tate shock flipped
    tate "Wait, you don't like Cheese Whales?! I {i}love{/i} those!"
    show tate sheepish flipped

    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        tate "{size=-12}I even brought extras to share..."

    mika "Well, I just don't like them too much."
    show tate flipped
    kitty "{image=note_small1.png}{i} The snack that breaks your back: {w=0.25}Cheese Whales!{/i} {image=note_small2.png}"
    n "They all laugh."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    jump friend2_final_meetup

label friend2_final_meetup:
    if nice_car:
        scene joj_chargerarc_fg
        show final_destination behind joj_chargerarc_fg
    else:
        scene car_insidearc_fg
        show final_destination behind car_insidearc_fg
    show arceus flipped at left
    show pakoo at right
    with dissolve
    play music prophet_2001 loop volume 0.6 if_changed
    music prophet_2001
    arceus "Alright, we are here."
    pakoo "So, who is joining us to help fight Copguy?"
    if fun_value(FUN_VALUE_MUSIC):
        cs "Well, the prophet from 2001 will be here, but let's go take a look."
    else:
        cs "Let's go take a look."
    scene black with dissolve
    n "The teams leave their cars and meet up with one another."
    scene final_destination with dissolve
    show cs at mid_left
    show arceus flipped at mid_offscreen_left behind cs
    with moveinleft
    n "The last group to meet up all emerge as well, which is made up of:"
    show blank at center with moveinright
    blank "Hi!"
    $ renpy.movie_cutscene(blank_bl)
    show anno at mid_right with moveinright
    anno "Yo."
    $ renpy.movie_cutscene(anno_bl)
    show midge at mid_offscreen_right behind anno with moveinright
    midge "Oh hai."
    $ renpy.movie_cutscene(midge_bl)
    $ achievement_manager.unlock("friends")
    if nice_car:
        "Blank, Anno, and Midge" "Nice car!"
        cs "Thanks! I've heard that a lot today."
    else:
        cs "Nice to finally meet you guys! Where's DB?"
    anno "Db05 isn't here yet. He's been busy."
    anno "He'll be here soon, though. We've been talking to him on the phone."
    n "Anno holds out his phone."
    db "Hey, guys! Sorry I'm gonna miss out on the huge battle thing! I had to do some things at home first."
    $ renpy.movie_cutscene(db_bl)
    db "But I'll gladly cheer you on while you're fighting!"
    cs "No problem DB! Every little bit helps!"
    tate "Y'all ready?"
    if fun_value(FUN_VALUE_MUSIC):
        cs "Hell yeah! Let's send Copguy Trans Atlantic!"
    else:
        cs "Hell yeah! Let's throw Copguy in the slammer!"
    stop music fadeout 3.0
    music end
    scene black with dissolve
    jump rpg_final_fight_1

label friend2_between_1:
    stop music fadeout 3.0
    music end
    scene war_torn_3
    show cs at center
    show pakoo flipped at mid_left
    show arceus flipped at left
    with dissolve
    cs "Woohoo! Those guys were easy!"
    show pakoo disappointed flipped
    pakoo "I don't think it's over, CS."
    show cs worried
    show arceus worried flipped
    arceus "Is that an even bigger tank than the last one?"
    show cs angry
    cs "Alright, guys! Battle positions! We've got a tank!"
    jump rpg_final_fight_2

label friend2_between_2:
    stop music fadeout 3.0
    music end
    scene war_torn_5
    show cs worried at center
    show tate srs at mid_left
    show arceus flipped at left
    with dissolve
    play music the_whale loop volume 0.6 if_changed
    music the_whale
    cs "C'mon, guys! We've gotta get to Copguy!"
    show cs disappointed
    tate "Where is Copguy, anyway? Do you even know where he could be?"
    n "All of a sudden, the ground starts to shake as a blinding light blasts the group."
    play sound sfx_earthquake
    stop music fadeout 3.0
    show tate shock
    show arceus worried flipped
    show cs scared with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    scene white with dissolve
    pause 0.5
    scene war_torn_5
    show cs worried at center
    show tate shock at mid_left
    show arceus worried flipped at left
    play sound sfx_bossappears
    show copguy_ex at right
    $ persistent.seen.add("copguy_ex")
    with dissolve
    pause 2.0
    copguy "Well, well, well, CS."
    play music prophet_2001 loop volume 0.6 if_changed
    music prophet_2001
    copguy "How do you like my new form? Pretty cool, right?"
    show cs angry
    show tate srs
    show arceus angry flipped
    cs "Go to hell, Copguy! You'll never defeat us!"
    copguy "Heheh, you can tell yourself that."
    copguy "I've been making sure to note down your team's abilities..."
    copguy "Why don't we try one out?"
    n "Copguy uses Light Cast on Arceus!"
    play sound sfx_gaster_blast
    scene white with dissolve
    scene war_torn_5
    show cs worried at center
    show tate shock at mid_left
    show arceus angry flipped at left
    show copguy_ex at right
    with dissolve
    show arceus worried flipped with vpunch
    arceus "Ow! How did you--{w=1.0}{nw}"
    copguy "I think that's all you need to see. Let's end this, CS."
    stop music fadeout 3.0
    scene black with dissolve
    jump rpg_final_fight_3

label friend2_weapon_of_choice:
    window hide
    pause 1.0
    $ renpy.movie_cutscene(woc)
    $ achievement_manager.unlock("beat_copguy")
    $ achievement_manager.unlock("cs_beat_copguy")
    $ persistent.heard.add("weapon_of_choice")
    jump friend2_car_slam

label friend2_car_slam:
    stop music fadeout 1.0
    scene war_torn_1 with dissolve
    n "CS looks around, taking in the destruction around him."
    n "The city that they once fought in has now been reduced to rubble and war-torn buildings."
    show cs worried flipped at right with moveinbottom
    n "CS gathers his bearings and starts checking on his friends."
    cs "Hello? Are you guys alright?"
    show arceus flipped at mid_mid_left with moveinleft
    arceus "Did we get him?"
    show pakoo flipped at left with moveinleft
    if fun_value(FUN_VALUE_MUSIC):
        pakoo "Man, that was insane. You really found your Weapon Of Choice!"
    else:
        pakoo "Man, that was insane. You guys demolished this place!"
    show cs disappointed flipped
    cs "I hope Copguy is dead. I am {i}definitely{/i} going to jail for this one if he's still alive!"
    n "CS continues to check on the others."
    hide cs with moveoutleft
    scene black with dissolve
    pause 1.0
    scene war_torn_2
    show tate at mid_left
    show mika at center
    show kitty flipped at right
    with dissolve
    show tate shock
    tate "Y'all {i}see{/i} that shit?!"
    mika "CS crushed the whole city!"
    show tate
    show cs disappointed flipped at mid_right with moveinright
    cs "Hey guys! Are you alright?"
    kitty "Yeah, we're alright. I'm assuming you're fine?"
    cs "Better than ever! Although, that did wear me out quite a bit."
    cs "I'm gonna go see how the rest are doing."
    hide cs with moveoutleft
    scene black with dissolve
    pause 1.0
    scene war_torn_3
    show digi at center
    show nova at mid_right
    show aria at right
    with dissolve
    show cs at left with moveinleft
    digi "Holy shit! CS! You're alive!"
    cs "Yeah! How about you guys?"
    nova "I wanna fall over. I'm so tired."
    if fun_value(FUN_VALUE_COMMON):
        aria "I never thought that our first meetup would be at a mall, and our second would be the destruction of Chigaco."
    else:
        aria "I never thought that our first meetup would be at a mall, and our second would be the destruction of Chicago."
    show cs happy
    n "CS laughs."
    cs "Yeah, me neither, Aria."
    show cs
    cs "There is one last group to check on."
    hide cs with moveoutright
    scene black with dissolve
    pause 1.0
    scene war_torn_5
    show midge at mid_mid_left
    show anno at mid_mid_right
    show blank at right
    with dissolve
    show cs at left with moveinleft
    cs "Hey, did DB ever make it to the fight?"
    anno "No... I never {i}saw{/i} him, at least."
    blank "Anno's phone got busted during the fight, so we don't know now what his ETA is."
    # yeah, uh, that line was weird - tate
    cs "Dang, that's a shame."
    cs "I kinda hope he doesn't show up now. I'd hate for him to witness the damage we did."
    midge "Well, we won, right? What's the plan now?"
    show cs angry
    cs "I wanna make sure Copguy is gone for real."
    cs "I'll be right back."
    hide cs with moveoutright
    scene black with dissolve
    pause 1.0
    scene war_torn_4 with dissolve
    show cs at left with moveinleft
    n "CS walks through the wastelands searching for anything reminiscent of Copguy."
    n "Eventually, he finds Copguy's wrecked cop car."
    show cs disappointed at center with move
    cs "Welp. There rests Copguy."
    cs "He fought well, he was a good cop, and God rest his soul."
    pause 3.0
    show cs flipped
    cs "Nahhh! That guy was a jerk!"
    show cs happy flipped
    cs "This is why you don't mess with the Master Of The Poop!"
    show cs surprised flipped
    cs "... The Youtube Poop, actually. I realize that sounded kinda stupid."
    n "CS turns around and walks away."
    show cs flipped at mid_left with move
    show copguy at manual_pos(0.75, 1.3, 0.5):
        rotate -90
    show copguy at manual_pos(0.75, 0.9, 0.5) with MoveTransition(0.25):
        linear 0.25 rotate -30
    with vpunch
    show cs scared flipped
    copguy "Damn it, you can't escape from me!"
    n "Copguy manages to crawl out of the rubble that is his car."
    show cs worried
    cs "Holy what? How did you--"
    copguy "I'm not gonna let you win that easily, CS."
    n "Copguy pulls out his sidearm."
    copguy "Or should I say,"
    show db_cooper at offscreenright
    copguy "C--{w=0.5}{nw}"
    show db_cooper at offscreenright
    show db_cooper at right
    $ collect("db_car")
    show cs worried at left
    with move
    show cs scared
    play sound sfx_explosion volume 1.5
    show realistic_explosion_anim at manual_pos(0.8, 0.7, 0.5) behind db_cooper:
        subpixel True
        zoom 20
    with hpunch
    hide copguy with moveoutbottom

    db "Hey, guys! I finally made it!"
    db "Sorry I'm late! I had to feed the pets back at home and--"
    show cs
    cs "DB, you did it!"
    db "What? What'd I do?"
    show cs happy
    cs "You killed Copguy!"
    db "Oh no, does that mean I'm gonna go to jail?"
    db "I can't go! Who's gonna take care of everything back at home?"
    show cs
    cs "Relax, we destroyed the majority of the police force."
    db "Wait, so does that mean... {i}we{/i} were the bad guys all along?"
    cs "Nah."
    if fun_value(FUN_VALUE_MUSIC):
        cs "You're the Legend, man. That man was like, {i}deranged.{/i}"
    else:
        cs "That man was like, {i}deranged.{/i}"
    scene black with dissolve
    window hide
    show paper at center with easeinright
    play sound sfx_issac
    pause 1.0
    hide paper with easeoutleft
    $ ending_manager.mark("friend")
    pause 1.0
    $ renpy.movie_cutscene(where)
    $ persistent.heard.add("the_legend")
    pause 1.0
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return
