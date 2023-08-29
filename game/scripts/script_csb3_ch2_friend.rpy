label dpn_call:
    if nice_car:
        scene joj_charger_fg
        show washington_road day behind joj_charger_fg
    else:
        scene car_inside_fg
        show washington_road day behind car_inside_fg
    show cs at left
    show pakoo at right
    with fade
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
    cs "Man, I hope Tate is okay. I don't how I'm gonna explain to them later about this whole situation."
    arceus "I think we're all in the same boat on that problem. I'm sure they'll all be fine."
    jump car_ride_1

label car_ride_1:
    scene black with fade
    n "Meanwhile, Tate's group seems to be having the time of their lives."
    scene jeep_inside_fg
    show washington_road day behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "Woohoo! Road trip!"
    tate "Man, I can't believe CS didn't tell me about all of this! This is so fun!"
    mika "I know, right?"
    tate "How are you holding up Kitty?"
    kitty "Yeah, I'm doing fine so far."
    tate "Hold up, is that CS and their gang infront of us?"
    tate "Mika, blare the horn at them! Do it! It'll scare the crap outta CS!"
    scene car_inside_fg
    show washington_road day behind car_inside_fg
    show cs disappointed at left
    show pakoo at right
    with fade
    cs "So yeah, that's why I'm mainly worried about Tate."
    show pakoo disappointed
    pakoo "Yeah, I getcha, I'm sur--{w=1.0}{nw}"
    show cs worried with vpunch
    show pakoo worried with vpunch
    # TODO: Horn honk SFX
    cs "JESUS!!"
    n "CS serves all over the road after being startled."
    show pakoo
    show cs disappointed
    arceus "Yep. I think they are doing just fine."
    scene jeep_inside_fg
    show washington_road day behind jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "Hahahaha! Did you see that??"
    kitty "Oh my goodness!"
    mika "Geez, I didn't think it was that bad."
    tate "Alright, that was kinda funny, but I think we should chill for a moment."
    tate "They've probably been stressed out all day long."
    tate "Anyways, how are you guys? I don't think we've properly met before."
    mika "Well, I'm Mika, and thankfully Pakoo called in time for us to arrive."
    kitty "Hi, I'm Kitty. I hope Arc is doing well enough."
    tate "I'm Tate. I'm sure they are doing just fine, and it's nice to meet you all."
    tate "Now let's go kick some ass!"
    scene car_inside_fg
    show washington_road day behind car_inside_fg
    show cs at left
    show pakoo at right
    with fade
    pause 1.0
    arceus "Alright, well it looks like Aria is gonna pick up Digi and Nova, and meet us here soon."
    cs "Wow, that was fast!"
    pakoo "Yeah, that's crazy."
    arceus "They'll meet us at some diner in approximately a few hours from now."
    cs "Alright then, that sounds good to me! I'm hungry so it'll be nice to get some food."
    arceus "Yeah, same."
    scene black with fade
    n "As a few hours pass, the DPN crew arrives at the S&P Diner, and waits to be served."
    jump dpn_diner

label dpn_diner:
    scene dinerinside
    show digi at right
    show nova flipped at center
    show aria at left
    with fade
    digi "Finally, we can stretch our legs again."
    nova "Remind me what you needed me here for again? I have a set later tonight I need to prepae for!"
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
    scene black with fade
    scene aria_car_fg
    show aria at left
    with fade
    pause 3.0
    #TODO: Aria Lines!

    n "As Aria is approaching CS and the gang, they screech on the breaks as they almost run into a blockade."
    show cs_somewhere behind aria_car_fg
    n "Cop cars surround the vicinity of the area."
    n "Aria gets out of the car."
    scene cs_somewhere
    show cop at right
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
    show cop at left with moveinleft
    cop "Ah shit! We got two men down! Arrest her!"
    jump aria_fight

label aria_fight:
    #TODO: Fight here.
    scene black with fade
    jump cs_meetup

label cs_meetup:
    scene cs_somewhere 
    show aria flipped at right
    with fade
    n "After Aria takes care of the cops, CS and Tate's group rolls up on the other side of the blockade."
    show cs at center
    show arceus flipped at mid_left
    show tate at left
    with moveinleft
    cs "Woah, what happened here? More cops?"
    aria "Yeah, they weren't too much of a problem through."
    tate "Good, the less cops, the better."
    aria "Nova and Digi are at the diner up ahead, let's get this blockade out of the way and get going."
    cs "Righty-o."
    scene black with fade
    n "CS, Aria, and Tate clear the road, and then follow Aria up to the diner."
    n "Meanwhile, back at the diner..."
    scene dinerinside
    show digi at center
    show nova flipped at left
    with fade
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
    jump dpn_fight

label dpn_fight:
    #TODO: Fight here.
    scene black with fade
    jump cs_meetup_2

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
    aria "Yeah, they won't stop coming. Let's meet up with the rest of the crew first."
    hide nova
    hide digi
    hide aria
    with moveoutright
    scene black with fade
    n "Digi, Aria, and Nova all go outside to meet everyone else."
    scene dineroutside 
    show cs flipped at right
    show arceus at mid_right
    with fade
    show digi flipped at center
    show nova flipped at mid_left
    show aria at left
    with moveinleft
    cs "Hey guys! Are you all good?"
    digi "Yeah, what about you? What is going on here?"
    cs "Well uhh..."
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
    show cs with determination
    show arceus flipped with determination
    hide cs
    hide arceus
    with moveoutright
    n "Everyone gets back into their cars, and they take off in a convoy, hoping to end this madness soon."
    n "In CS' group, the gang decides what they can do to get away from the cops."
    scene car_inside_fg
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
    scene black with fade
    pause 2.0
    jump car_ride_2

label car_ride_2:
    scene jeep_inside_fg
    show mika at left
    show tate flipped at right
    with fade
    tate "Man, I wanna fight something!"
    mika "Yeah, what the hell! Where is this Copguy dude at?"
    kitty "What if he's preparing defenses to ambush us?"
    mika "We'll destroy anything that comes our way, don't worry."
    tate "Hell yeah, screw that Copguy dude! He just ran away at the last second when we first fought him!"
    mika "We definitely got this don't worry."
    kitty "I wonder how those new guys are handling the situation..."
    scene black with fade
    pause 2.0
    scene aria_car_fg
    show aria at left
    show digi at right
    with fade
    digi "I can't believe CS went to jail."
    aria "Arceus was in jail for 5 years, Digi."
    digi "Yeah I know, but that's an Arceus thing to do."
    nova "Is it?? That's kinda concerning."
    digi "no, I meant like, he knows what he's doing."
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
    scene car_inside_fg
    show cs at left
    show pakoo at right
    with fade
    cs "well, should we find somewhere to stop for the night? We've been going for a while."
    pakoo "Holy shit! Stop CS!"
    show battle_block_without_theater behind car_inside_fg
    n "As CS looks ahead, he screeches on the breaks just in time."
    n "Barbed wire, soldiers, and military trucks block the highway, with Copguy standing in the front of it all."
    cs "This can't be good."
    scene black with fade
    n "The groups behind CS stop as well, as everyone gets out of their cars and approaches Copguy."
    scene battle_block_without_theater
    show copguy at mid_right
    show guard_soldier at right
    with fade
    show cs angry at center
    show tate at mid_left
    show arceus flipped at mid_left_left
    show digi flipped at left
    with moveinleft
    copguy "Well? What do you think CS? You ready to go back to jail?"
    cs "Never!"
    copguy "Oh really? Because I just called the national guard here to help me stop you."
    tate "Yeah well, CS called me to stop you!"
    digi "Yeah! Us too!"
    n "CS' friends start yelling, as the national guard men ready their weapons."
    copguy "I see, you wanted to do this the hard way..."
    copguy "Well, you're gonna find out why you never pick the hard way!"
    copguy "Soldiers! Attack!"
    jump ng_fight

label ng_fight:
    #TODO: Fight scene
    scene black with fade
    jump cs_rage

label cs_rage:
    scene battle_block_without_theater
    show cs angry at center
    show tate at mid_left
    show arceus flipped at mid_left_left
    show digi flipped at left
    with fade
    n "After CS and the group manage to push back the national guard, Copguy once again flees at the last moment."
    cs "Hey! You get back here damnit!"
    show cs angry at mid_right with move
    show cs angry flipped with determination
    cs "Guys let's chase after him!"
    arceus "CS, we need a minute. We just fought a tank."
    cs "No time for that! We need to stop him now!"
    tate "CS, I'm sorry, we need to wait."
    digi "We're never gonna catch up with him at this point anyways..."
    cs "Fuck! I can't believe this!"
    show cs angry with determination
    cs "He keeps running away like a wimp!"
    arceus "CS, you gotta calm down, we can-- "
    show cs angry flipped with determination
    cs "Calm down? CALM DOWN?"
    show cs angry flipped with hpunch
    cs "Do you know what we just fought through?"
    cs "He's just gonna keep building up stronger units for us to attack, and then run away if we beat him!"
    show cs angry with determination
    cs "We need to head out now!"
    show cs angry with hpunch
    pause 1.0
    show cs angry with vpunch
    pause 1.0
    show cs angry with hpunch
    pause 1.0
    show cs angry with vpunch
    n "CS goes to the debris from the battle, desperately trying to move it out of the way."
    show cs concentrate
    cs "Guys, cmon, please! We have... to... hnngg..."
    tate "Woah, CS? What are you doing?"
    show cs concentrate with vpunch
    show cs concentrate with hpunch
    show cs concentrate with vpunch
    n "All of a sudden, the debris starts moving on it's own!"
    digi "Woah, what's going on?"
    cs "Can you guys please help--"
    show cs at center with move
    cs "Wait, what the hell?! Did I move all of that already?"
    n "As CS is gawking at the work he just did, a purple figure appears in front of CS."
    show csgod at right with dissolve  
    csgod "You're welcome."
    cs "Woah, hey! Are you CSGod?"
    csgod "Indeed I am. You've seemed to channel my power through sheer willpower."
    cs "Holy crap, does that mean I can use YTP Magic?"
    csgod "In theory, yes. Although you should take some time to rest."
    csgod "Don't beat yourself up over Copguy, you'll be able to beat him down next time, if you calm down and focus."
    csgod "I'm gonna let you go for now. Copguy is planning his most devious attack yet, and you need to be prepared."
    cs "I see, well, thank you for that CSGod!"
    csgod "No problem."
    hide csgod with dissolve
    n "CSGod fades away, and CS turns back to the group."
    tate "CS, you okay? You were just staring up at the sky and talking to yourself about magic or something."
    show cs flipped with determination
    cs "I'm all good, don't worry."
    cs "Sorry I got upset, I just need to relax."
    cs "Arc, you drive, I'm gonna lie down in the backseat."
    arceus "You need, anything else?"
    cs "I'm good, just some rest."
    hide cs with moveoutleft
    n "CS heads into the backseat of the car and lies down."
    show digi at center with move
    show arceus flipped at left with move
    digi "Alright well, what's the plan? CS is technically right, we need to go track down Copguy somehow."
    arceus "I managed to put a tracking device on Copguy's car in the heat of the battle."
    arceus "I'll be following him, and I'll update you guys about what's going on."
    show arceus with determination
    hide arceus with moveoutleft
    digi "Roger."
    tate "Alright, let's go kick Copguy's ass!"
    hide digi
    hide tate
    with moveoutleft
    scene black with fade
    n "The crew gets in their respective cars, and they take off."
    show car_inside_fg
    show arceus flipped at left
    show pakoo at right
    with fade
    n "While they are driving, Arceus notices that copguy starts ludicrously speeding up until he stops in Illinois."
    arceus "Guys, I think I found out where Copguy is headed."
    arceus "He's stopped in Chicago."
    pakoo "Ah shoot."
    cs "I'm gonna ping everyone in CSCord, and see if anyone else is able to help us out."
    cs "We're gonna need it."
    scene black with fade
    pause 2.0
    jump car_ride_3

label car_ride_3:
    #TODO: Car dialogue
    scene aria_car_fg
    show aria at left
    show digi at right
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
    show mika at left
    show tate flipped at right
    with fade
    tate "I went to the Dollar Tree a couple days ago, and was picking up some of those off-brand snacks."
    mika "I feel like only a few off-brands can taste well, but there are a few I just can't eat."
    tate "Like which ones?"
    mika "Usually the off-brand Cheez-its, but I really don't like the off-brand goldfish either."
    tate "Not the gold whales! I love those!"
    mika "Well, I just don't like them too much."
    kitty "The snack that breaks your back: Gold Whales!"
    n "They all laugh."
    scene black with fade
    jump final_meetup

label final_meetup:
    scene car_inside_fg
    show arceus flipped at left
    show pakoo at right
    with fade
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
    show anno at mid_right with moveinright
    anno "Yo."
    show midge at right behind anno with moveinright
    midge "Oh hai."
    anno "Db05 isn't here yet, he's been busy."
    anno "He'll be here soon though, we've been talking to him on the phone."
    n "Anno holds out his phone."
    db "Hey guys! Sorry I'm gonna miss out on the huge battle thing, I had to do some things at home first."
    db "But I'll gladly encourage you while you all are fighting!"
    cs "No problem DB! Every little bit helps!"
    tate "Well, are you guys ready to do this?"
    cs "Hell yeah! Let's go put Copguy through the slammer!"
    scene black with fade
    jump final_fight

label final_fight: