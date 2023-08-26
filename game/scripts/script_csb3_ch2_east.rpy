label east:
    cs "Well since east is the way home, we should probably go that way."
    arceus "Alright, that sounds like a good idea."
    n "CS and Arc keep following the road for a while, until they come across a small town."
    scene town with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    cs "Oh my god! We found civilization again!"
    arceus "Thank God."
    n "The two look around for a bit, when they see a gas station close by."
    cs "Let's head over to that gas station, so we can pick up some food."
    n "CS and Arc head over to the convenience store at the gas station."
    hide cs with moveoutright
    show arceus flipped at right
    hide arceus with moveoutright
    scene gasinside with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    arceus "Finally, some good fucking food."
    cs "Donuts and chips have never tasted better."
    arceus "Thank God the slushie machine was working for once."
    cs "Okay, now that we can think about something other than food, what's our plan to get home?"
    arceus "Yeah, I have no clue currently."
    arceus "I was hoping that we could like hitchhike on a bus or something, but it might be ages until that happens... If it even DOES happen, this town is small enough as is."
    stop music fadeout 3.0
    music end
    menu:
        "Wait for driver at the gas station" (type = "true"):
            jump billy_driver
        "Hotwire a car" (type = "bad"):
            jump hotwire

label hotwire:
    cs "I don't know, we could just, hotwire a car?"
    arceus "I can probably do that, let's go look."
    scene gasoutside with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS and Arc approach one of the cars in front of the gas station."
    n "Arceus smashes open the window and opens the door from the inside."
    arceus "Alright, so if we connect this to this..."
    n "The car starts up."
    cs "Hell yeah! Let's go home!"
    n "All of a sudden, flashing lights and sirens show up behind them."
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" volume 0.5
    show copguy at center with moveinleft
    show cs disappointed
    copguy "I heard the sound of a car window breaking from miles away!"
    copguy "You guys already blew it! Back to the slammer!"
    return

label billy_driver:
    cs "Why don't we just wait for someone at the gas station to come out, and then we ask them for an Uber?"
    n "CS walks over to someone's car parked in the front of the gas station."
    scene gasoutside with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    arceus "Are you crazy? To drive all the way back to New York? In a stranger's car at that."
    arceus "Besides, how are we even going to pay the guy anyways?"
    cs "Well we don't have to go all the way to New York, we could go a small distance and then get another Uber."
    arceus "That would be even more money in tips!"
    n "As the two are agruing, the owner of the car comes up to them."
    "???" "What are you doing next to my car?"
    cs "Oh, hi."
    cs "Do you think you can Uber us to New York?"
    "???" "Oh uhh, hold on a second."
    n "The mysterious driver walks behind the store."
    arceus "What are you doing? That man looks like he's going to kill us!"
    arceus "He's probably getting a gun, we need to lea--"
    show billy at center with moveinleft
    play music "<loop 0>mm_select.mp3" volume 0.3
    music Mm Select - Matthew Simmonds
    billy "Hi, Billy Mays here for the Uber Driver!"
    billy "The fast and easy way to get people around who don't have a car!"
    show cs happy
    cs "Sweet! We need to get to upstate New York, do you think you can help us?"
    billy "Absolutely! For only $19.95, I'll take you both to New York!"
    cs "Alright well, it's settled! We have our driver, Arceus!"
    arceus "..."
    arceus "... What the fuck. Works for me I guess."
    cs "Hell yeah! I call shotgun!"
    n "CS and Arc get into Billy's car."
    stop music fadeout 3.0
    music end
    hide cs with moveoutright
    hide billy with moveoutright
    show arceus flipped at right
    hide arceus with moveoutright
    jump in_billy_car

label in_billy_car:
    scene carback1
    show billy car
    play music "<loop 0>billy_radio.mp3" volume 0.3
    music Billy Mays Gangsta Remix - mastamokei
    cs "Alright so, it's just a straight shot to New York?"
    show billy car turn
    billy "Yep! We are gonna head through Idaho and Montana first, so get ready to see the sights!"
    show billy car happy
    cs "Yeah! It's almost like a vacation!"
    arceus "Well on a vacation, you usually have money to spend on all the crazy parts you see."
    cs "Let's just enjoy the ride there at least."
    arceus "Fair point."
    stop music fadeout 3.0
    music end
    jump montana

label montana:
    scene car background
    show billy car
    with fade
    n "After a few hours of driving, the trio currently is located in the middle of Montana."
    n "Arceus is sleeping, while CS peers out the window."
    cs "Are we there yet?"
    billy "Nope!"
    cs "Aw man..."
    show billy car turn
    billy "We still got a ways to go, we aren't even a quarter of the way yet."
    show billy car
    cs "Alright, I'll just, keep looking at the trees pass by."
    billy "Well good news for you, there is a small town up ahead."
    billy "I was gonna buy some new supplies for my gadgets, if you guys want to pick out anything."
    cs "Sure! I love buying random things!"
    cs "What about you Arceus?"
    cs "Hey, Arc!"
    billy "CS, you should probably leave the dog thing alone in the back."
    n "Arceus immediately jerks straight up."
    arceus "What did you just call me?"
    billy "Nothing!"
    scene hardwareoutside
    show billy car
    billy "Here we are, at the store. I'll be back here in a few."
    cs "Same, I'll come with you."
    n "Arceus falls back to sleep in the car."
    play sound "doorslam.ogg"
    scene hardwareinside with fade
    play music "<loop 0>home_depot.mp3" volume 0.4
    music "Let's Do This - Home Depot"
    show cs at left with moveinleft
    cs "Wow look at all this stuff!"
    cs "They've got Allen wrenches, gerbil feeders, toilet seats, electric heaters{nw}"
    cs "Trash compactors, juice extractor, shower rods and water meters{nw}"
    cs "Walkie-talkies, copper wires, safety goggles, radial tires{nw}"
    cs "BB pellets, rubber mallets, fans and dehumidifiers{nw}"
    cs "Picture hangers, paper cutters, waffle irons, window shutters{nw}"
    cs "Paint removers, window louvres, masking tape and plastic gutters{nw}"
    cs "Kitchen faucets, folding tables, weather stripping, jumper cables{nw}"
    cs "Hooks and tackle, grout and spackle, power foggers, spoons and ladles{nw}"
    cs "Pesticides for fumigation, high-performance lubrication{nw}"
    cs "Metal roofing, water proofing, multi-purpose insulation{nw}"
    cs "Air compressors, brass connectors, wrecking chisels, smoke detectors{nw}"
    cs "Tire gauges, hamster cages, thermostats and bug deflectors{nw}"
    show cs worried
    cs "Trailer hitch demagnetizers, automatic circumcisers{nw}"
    show cs
    cs "Tennis rackets, angle brackets, Duracells and Energizers{nw}"
    cs "Soffit panels, circuit breakers, vacuum cleaners, coffee makers{nw}"
    cs "Calculators, generators, matching salt and pepper shakers{nw}"
    cs "and I think that's it..."
    cs "Ooh! Look at all this paint!"
    cs "Let's get some orange, blue, purple,"
    show cs happy
    cs "More colors, I need more colors!"
    show billy at right with moveinright
    show cs
    billy "You ready to go, CS?"
    cs "Yep! Let's check out and keep going!"
    billy "Where is the cashier in this store? I didn't see anyone..."
    show cashier at center with moveinbottom
    show cs worried
    show cashier with hpunch
    cashier "I gotcha covered. Have a good day!"
    hide cashier with moveoutright
    cs "Letsgoletsgoletsgoweneedtogetoutofhere"
    hide cs with moveoutright
    hide billy with moveoutright
    stop music fadeout 3.0   
    music end
    play sound "doorslam.ogg"
    scene hardwareoutside
    show billy car
    with fade
    billy "That was quite the experience, I should've brought my Hercules Hook!"
    cs "Yeah really, let's get out of here!"
    arceus "Huh? What's going on?"
    cs "Nothing Arc, just, uh, slipped and fell in the store."
    arceus "Okay whatever, I'm going back to sleep..."
    n "Billy takes off out of the parking lot."
    scene car background night
    show billy car
    with fade
    cs "Man, today was pretty crazy too."
    arceus "Yeah, at least I got some sleep after all of it."
    cs "Speaking of which, can we find a place to rest soon?"
    billy "Yeah, let's see if I can find a place to stop at."
    billy "Wait a second, what the hell?"
    n "Billy brings the car to a screeching halt."
    scene cultforest
    show billy car
    play music "<loop 0>candle_world.mp3" volume 0.4
    music Candle World - Kikiyama
    "CS and Arceus" "What in the world?"
    n "Ahead lies a barricade with a bunch of strange hooded people surrounding it."
    show cultist at mid_right behind billy with moveinright
    n "One of the members walks up to the driver's side and knocks on the window."
    n "Billy rolls down the window."
    billy "Hi, it's Billy! What are you doing by my car?"
    cultist "Get out of the car."
    billy "No, it's my car!"
    show cultist gun
    n "The cultist pulls out a revolver and aims at Billy's head."
    cultist "Does this like a joke to you guys?"
    cultist "Out of the car. Now."
    n "Billy shrugs and opens the door, with the cultist leader still aiming the gun to his head."
    cultist "You two as well, out."
    n "CS and Arceus both step out of the car."
    hide cultist with moveoutright
    hide billy car with fade
    show billy at mid_mid_left
    show cs disappointed at mid_left
    show arceus flipped at left
    with moveinleft
    show cultist at mid_right with moveinright
    cultist "So, do you want to explain what is going on here?"
    cs "Uhm, we were heading on past here to the next-"
    show cultist gun
    n "The cultist aims his gun at CS."
    cultist "Look, I don't care where you are going."
    show cultist at center with moveinleft
    cultist "We are part of the Blue Branch Cult, and our motto is that we hate everything."
    arceus "Like, everything?"
    show cultist gun
    n "The cultist aims at Arceus."
    cultist "You wanna fuck with me?"
    arceus "I mean. If you're offering."
    n "The cultist looks annoyed."
    show cultist
    cultist "I'm gonna get the rest of the gang to deal with you guys, don't fucking move."
    hide cultist with moveoutright
    pause 2.0
    show cultist at right with moveinright
    cultist "I mean it!"
    hide cultist with moveoutright
    pause 1.5
    show cultist at right with moveinright
    cultist "Okay?"
    hide cultist with moveoutright
    pause 2.0
    hide billy with moveoutleft
    n "Billy goes to the back of his trunk and starts digging around."
    arceus "Never thought we'd run into cultists out of all people."
    hide cs with moveoutleft
    n "CS starts digging around in the back too."
    arceus "CS, what are you doing?"
    arceus "CS?!"
    show cs fakegod at center with moveinleft
    cs "Look at me! I'm purple!"
    $ renpy.music.set_pause(True, "music")
    play sound "secret/funni.ogg" volume 0.5
    pause 3.0
    stop sound
    $ renpy.music.set_pause(False, "music")
    arceus "CS, what the fuck are you doing...?!"
    arceus "You are going to definitely get us killed!"
    n "Arceus hides behind the car as the cultist leader brings two others with him."
    hide arceus with moveoutleft
    show cs fakegod at left with moveinleft
    show cultist_2 at mid_mid_right with moveinright
    show cultist_3 at right with moveinright
    show cultist at mid_right with moveinright
    cultist "Alright, they are over here at this car."
    cultist_2 "No way..."
    cultist_3 "It's CSGod!"
    cultist_2 "Praise CSGod!"
    cultist "Oh no! It's the one thing that we don't hate!"
    cs "Huh?"
    cs "I mean,"
    cs_fakegod "Yeah that's right it's me, CSGod."
    cs_fakegod "You better leave these three alone, or I'll uh, smite you!"
    cultist "CSGod doesn't smite, he uses YTP mag-{w=0.5}"
    cs_fakegod "Don't tempt your god, I will YTP you so hard that you'll look like you came from an AwfulFawful YTP!"
    cultist_2 "We need to leave! We're sorry!"
    n "Billy comes up behind CS with one of his gadgets."
    show billy laser at mid_left with moveinleft
    stop music fadeout 1.0 
    play music "<loop 0>blazing_corridor.mp3" volume 0.4    
    billy "Fire a laser! Fire a laser!"
    show laser_beam at t_gun behind billy
    hide cultist_2 with moveoutright
    hide laser_beam
    n "Massive laser shots land between the cultists as they scramble away!"
    cultist_3 "I don't wanna turn into a YTP! Go guys go!"
    show laser_beam at t_gun behind billy
    hide cultist_3 with moveoutright
    hide laser_beam
    pause 0.5
    show laser_beam at t_gun behind billy
    hide cultist with moveoutright
    hide laser_beam
    n "The cultists disappear into the forest."
    stop music fadeout 3.0 
    music end
    billy "That's the power of the Awesome Augement!"
    play music "<loop 0>showtime.mp3" volume 0.4
    music "It's Showtime - Toby Fox"
    show cs fakegod at center with moveinright
    cs "Hooray! I'm a god now!"
    show arceus flipped at left with moveinleft
    arceus "CS, I don't know how you pull this stuff off."
    arceus "Am I still sleeping?"
    n "Arceus pinches himself."
    arceus "Fuck."
    arceus "How many divine beings and reality benders do we have in this universe anyhow?"
    cs "Alright, back on the road to New York!"
    stop music fadeout 3.0
    music end
    scene car background night
    show billy car
    with fade
    n "The gang gets back in the car and books it out of the forest."
    n "After a while of driving, Billy pulls the car into a small area off the forest to let everyone rest."
    scene black with fade
    n "After the night passes, they set off again on their trip."
    scene car background
    show billy car
    play music "<loop 0>mort_farm.mp3" volume 0.4
    music "Mort's Farm - ClascyJitto"
    cs "Can we stop somewhere to eat? We haven't eaten since yesterday."
    arceus "Yeah unfortunately the one store you guys went to didn't have anything edible."
    billy "Sure yeah, there's a McDonald's up here in a couple miles."
    scene mcdonalds
    show billy car
    n "Billy pulls up through the drive-thru to place his order."
    cashier "Hello, what you like to order?"
    billy "Hi, Billy Mays here! I would like to get the Buy 1 Get 1 Free breakfast meal for my friends here,"
    billy "and I would also like to get the egg McMuffin and a Big Mac for me."
    cashier "Sure thing, that'll be-{nw}"
    billy "But I'm not done yet! I would like to triple the offer and get 3 Big Macs, and also 3 large sodas without any shipping!"
    cashier "Uhh, yeah, we can do that without shipping."
    cashier "That'll be about, let's see..."
    cashier "$36.88."
    billy "Wow! What a deal! I'm coming around to pick up my order!"
    scene black with fade
    n "Billy drives through and picks up his meal."
    scene mcdees
    show billy car
    with fade
    n "CS and Arc happily chow down on the Mickey D's they just got."
    arceus "Thank God for that."
    cs "I have never been so excited to get a Big Mac."
    scene car plains
    show billy car
    with fade
    n "Billy heads out on the open road again, as they enter the state of South Dakota."
    jump south_dakota

label south_dakota:
    arceus "Welcome to the Great Plains."
    cs "Woohoo!"
    stop music fadeout 3.0
    music end
    arceus "I don't think you should be super excited, there is like, nothing here."
    cs "Oh yeah, we don't even have trees to look at anymore."
    cs "Is there anything to do in this state?"
    arceus "There's Mount Rushmore, I guess there's Wall Dr-{w=0.5}"
    cs "Oh hell yeah! Let's go to Mount Rushmore!"
    scene black with fade
    n "In about an hour, the crew arrives at Mount Rushmore."
    scene rushmore with fade
    n "They all hike up to the viewing spot to get a good look of the founding fathers."
    play music "<loop 0>taiikusai_desu_yo.mp3" volume 0.4
    music Taiikusai Desu Yo - Satoru Kōsaki
    show cs at right with moveinleft
    show arceus at center with moveinleft
    show billy at left with moveinleft
    billy "Wow, to think that we won a war without the Gopher."
    billy "How did they even communicate without the Jupiter Jack?"
    show cs concentrate
    arceus "It'd be cool if I had my face carved out into a mountain. Wouldn't that be cool, CS?"
    show arceus flipped at center
    n "Arceus looks over at CS concentrating on something really hard."
    arceus "CS? Are you okay?"
    show arceus flipped at mid_right with moveinleft
    n "As Arceus starts to approach CS, the groups surrounding them all gasp loudly."
    scene csmore
    show cs concentrate at right
    show arceus at center
    show billy at left
    with hpunch
    arceus "Huh?"
    show cs happy
    cs "There we go! Fixed!"
    n "Arceus looks back at Mount Rushmore, now with CS, Arceus, and Billy's face on the mountain."
    hide cs with moveoutright
    arceus "You scare me, CS. I don't even like, want to question how or why."
    arceus "{size=-12}I do look pretty cool though."
    stop music fadeout 3.0
    music end
    n "The gang gets back in the car before the overwelming groups of people engulf the site after what just happened."
    scene car plains
    show billy car
    with fade
    n "They continue to drive through the massive and empty plains of South Dakota."
    play music "<loop 0>track4.mp3" volume 0.4
    music Track 4 - Weatherscan
    n "By the time they reach Sioux City, it is already evening."
    cs "There really is nothing out here, is there?"
    arceus "Nope. I don't get how people can even live here."
    billy "We're like halfway through the Midwest, we've only got a couple states left to travel before we are in the heartland."
    n "Billy follows the Missouri River down until they hit Omaha."
    jump nebraska

label nebraska:
    scene omaha
    show billy car
    with fade
    n "The gang finally hits Omaha, right before it hits nighttime."
    cs "This is the biggest city here? This is pretty small."
    billy "It looks very quaint, hopefully we can find a place to stop here."
    billy "I have no damn clue where to go here."
    arceus "Let's get out and look for somewhere to eat."
    hide billy car
    show cs at mid_left
    show arceus at center
    show billy at mid_right
    show pakoo at offscreenleft
    with moveinleft
    n "They all get out and start roaming the streets."
    n "Suddenly, CS hears a voice behind him."
    "???" "CS? Is that you?"
    cs "Huh?"
    show cs flipped
    stop music fadeout 3.0
    music end
    n "CS turns around and sees a wacky...{w=0.5} thing, with a tophat on."
    show pakoo at left
    show billy at right
    show arceus at mid_right
    show cs flipped at center
    with ease
    pakoo "Yeah hey, it {i}is{/i} you!"
    pakoo "Arceus, you too? And, Billy... Mays?"
    billy "Hi, it's Billy!"
    arceus "Hey, Pakoo."
    cs "Yeah! I haven't seen you in a while, I never thought you'd live in this place!"
    pakoo "I never thought you guys would come down to Omaha, there's like, nothing here."
    cs "We've been through a lot recently, do you know somewhere we can eat and rest for the night?"
    n "Pakoo thinks for a moment."
    pakoo "I think I know a place."
    n "Pakoo takes the gang over to the old market section of Omaha."
    hide pakoo
    hide cs
    hide billy
    hide arceus flipped
    with easeoutright
    scene alleyway with fade
    show pakoo at center
    show billy at right
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    pakoo "Here we are, this is probably the best location to eat at, at least that I know of."
    scene peppinopizzabg
    show peppinopizzafg
    with fade   
    play music "<loop 0>funiculi_holiday.mp3" volume 0.3
    music Funiculi Holiday - ClascyJitto
    show peppino at t_pepzone1 behind peppinopizzafg with moveinleft
    show peppino at t_pepzone2 behind peppinopizzafg with ease
    show pakoo at mid_right with moveinleft
    show billy at right with moveinleft
    show cs at left with moveinleft
    show arceus flipped at mid_left with moveinleft
    peppino "Hey Piezanos, watcha want today?"
    pakoo "Hey Peppino, can you get me and my friends the Gustavo special today?"
    show peppino2 at t_pepzone2 behind peppinopizzafg
    hide peppino
    peppino "Sure-a thing-a! Coming right up!"
    show peppino at t_pepzone2 behind peppinopizzafg
    hide peppino2
    pakoo "Also, do you think my friends here can be spend the night? They don't have anywhere to sleep tonight."
    peppino "The room in the back should be fine, Mr. Stick is out right now, so they can bunk there."
    pakoo "Alright, epic."
    n "Peppino serves the group their pizza."
    cs "Damn, this is some good pizza!"
    arceus "Probably some of the best pizza I've ever had."
    billy "Better than my restaurant mini-burgers!"
    pakoo "Alright well, I should get going, but I hope y'all have a good time doing whatever y'all doing."
    cs "Yep! Take care, Pakoo!"
    hide pakoo with moveoutleft
    scene black with fade
    stop music fadeout 3.0
    music end
    n "The gang goes into the backroom area and sleeps for the night."
    n "Once they wake up, they thank Peppino for his hospitality and head out."
    jump iowa

label iowa:
    scene car plains
    show billy car
    with fade  
    n "They get back in car and continue into Iowa."
    billy "Alright well, ever since that cult encounter, it's been pretty smooth sailing!"
    billy "The rest of this trip shouldn't be too long!"
    n "As if on cue, a strange sound is heard over the car."
    n "CS looks out the window."
    play music "<loop 0>speedy_comet.mp3" volume 0.5
    music Speedy Comet - Mahito Yokota
    cs "You have to be kidding me!"
    arceus "What's going on?"
    cs "HoH SiS is back!"
    arceus "WHAT?!"
    billy "Who?"
    cs "They have their UFO and--"
    n "A huge laser beam blasts on the left side of the road, ripping up everything in it's path!"
    play sound "minigames/car/gaster_blast.wav"
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car
    arceus "Shit, this is bad..."
    cs "Billy, you need to switch lanes when it charges up!"
    jump play_cargame

label after_ufo:
    scene car plains
    show billy car
    stop music fadeout 3.0
    music end
    cs "Holy shit! We made it!"
    arceus "That was some good driving Billy!"
    billy "That's the power of the 6000 pound car!"
    n "They continue driving through the end of the Midwest."
    scene car plains night
    show billy car
    with fade
    n "As they are drving through Illinois, they pass by Chicago."
    arceus "One day, I'm gonna rule that place."
    cs "What are you... talking about?"
    arceus "It's better than ruling the Earth."
    cs "Get some sleep, Arc."
    scene black with fade
    n "The gang stops in Indiana for the night, and takes off in the morning through Michigan."
    jump michigan

label michigan:
    # TODO: [ARIA] Write this.
    jump ohio

label ohio:
    if fun_value(50):
        scene car plains
        show billy car
        with fade
        n "After that fiasco, they travel through Ohio."
        show scott_border
        play music "<loop 0>breakout.mp3" volume 0.3  
        music Breakout - Shoichiro Sakamoto 
        n "Suddenly, a huge blue border enters everyone's vision."
        scott "Oh what in the world? There is some red border in my eyes..."
        scott "I have a blue one, what is going on?"
        scott "Yeah, it's blue for me too, I think you are colorblind."
        scott "I AM colorblind. Oh fuck."
        scene wozniaktroubles
        show billy car
        show scott_border
        with fade
        n "As they are driving through the state, they see some men on the side of road protesting about the blue border."
        scott "Hey all, Scott here!"
        scott "Are you tired of having a blue border in your vision?"
        scott "You should try Kaboom!"
        n "Scott pulls out a bottle of Kaboom and sprays them in the face."
        scott "Ahhhhh!"
        scott "It gets the tough stains out!"
        scott "I'm sorry that doesn't seem very vegan, I'll have to just deal with it."
        scott "Scott, I don't think that'll work, let's just keep going."
        scene car plains
        show billy car
        show scott_border
        with fade
        n "Once they leave the state, the border goes away."
        stop music fadeout 3.0
        music end
        hide scott_border with dissolve
        arceus "I'm glad it just faded away, I did not want to spray cleaner in my eyes."
    else:
        scene car plains
        show billy car
        with fade
        n "After that fiasco, they travel through Ohio."
        show scott_border
        play music "<loop 0>breakout.mp3" volume 0.3  
        music Breakout - Shoichiro Sakamoto 
        n "Suddenly, a huge blue border enters everyone's vision."
        arceus "Oh what in the world? There is some red border in my eyes..."
        cs "I have a blue one, what is going on?"
        billy "Yeah, it's blue for me too, I think you are colorblind."
        arceus "I AM colorblind. Oh fuck."
        scene wozniaktroubles
        show billy car
        show scott_border
        with fade
        n "As they are driving through the state, they see some men on the side of road protesting about the blue border."
        billy "Hi, it's Billy!"
        billy "Are you tired of having a blue border in your vision?"
        billy "You should try Kaboom!"
        n "Billy pulls out a bottle of Kaboom and sprays them in the face."
        scott "Ahhhhh!"
        billy "It gets the tough stains out!"
        terry "I'm sorry that doesn't seem very vegan, I'll have to just deal with it."
        cs "Billy, I don't think that'll work, let's just keep going."
        scene car plains
        show billy car
        show scott_border
        with fade
        n "Once they leave the state, the border goes away."
        stop music fadeout 3.0
        music end
        hide scott_border with dissolve
        arceus "I'm glad it just faded away, I did not want to spray cleaner in my eyes."
    jump pennsylvania

label pennsylvania:
    n "The gang hits the last state before New York, Pennsylvania."
    scene billboard
    n "CS sees a billboard pass by them."
    cs "Oh my god! It's PencilCon! We need to go!"
    arceus "Why the fuck do you want to go to PENCILCON when we are so close to home?!"
    cs "Because I love sharpening pencils! I made my own holiday around it! Please, Billy, can we go to PencilCon?"
    billy "If Arceus is okay with it, sure, I guess."
    cs "C'mon, Arceus!"
    arceus "Ugh..."
    cs "Please?"
    pause 3.0
    arceus "Fine, sure, whatever."
    cs "Yippee! Let's go!"
    scene cc_parking_lot with fade
    show cs at left
    show arceus flipped at mid_left
    show billy at center
    with moveinleft
    n "After about twenty minutes, the gang arrives at PencilCon."
    n "They get out of the car and head inside."
    hide cs
    hide arceus
    hide billy
    with moveoutright
    scene cc_crowd
    cs "Oh my gosh, I'm so excited! Everything is pencil-themed!"
    arceus "This is... some place."
    billy "Do people really like pencils that much? Maybe I should've pitched more pencil products."
    scene cc_entrance with dissolve
    show pencilguy at center with determination
    n "A man dressed as a pencil approaches the gang."
    pencil "Welcome to PencilCon! Want a free pencil?"
    show arceus at right with moveinright
    arceus "Uh, sure?"
    pencil "Here you go!"
    n "The pencil-clad man passes out a free pencil to each of them."
    pencil "Enjoy your stay!"
    show arceus flipped
    hide arceus flipped with moveoutright
    pencil "And, oh yeah! The 84th annual Pencil Sharpening Competition signups close in just a little bit, if you wanted to sign up!"
    hide pencilguy
    show cs at center
    n "The pencil man looks at CS."
    hide cs
    show pencilguy at center
    pencil "You look like the kinda guy that could win a competition like that. And boy howdy Dixon do we need it, the current champion hasn't been bested in five years!"
    hide pencilguy with moveoutright
    n "The pencil walks away."
    show cs at center
    cs "A pencil sharpening competition?"
    n "CS sees visions of an old video in his head."
    cs "I could totally crush that! I gotta sign up!"
    show arceus at right with moveinright
    arceus "CS, come on man, I wanna get to your house so I can-"
    hide cs with moveoutright
    n "CS walked towards the convention center before Arceus could finish speaking."
    show billy at left with moveinleft
    billy "Listen, let the guy have fun. You two have been through a lot, right?"
    arceus "I suppose, I just..."
    n "Arceus thinks for a moment."
    arceus "Fuck, I have been kind of a jerk during this whole road trip. Maybe I do need to let go."
    billy "That's the spirit! Now go cheer on your friend!"
    arceus "I will! Thanks, Billy!"
    billy "Any time!"
    show arceus flipped with determination
    hide arceus with moveoutright
    n "Arceus runs off to where CS went."
    billy "Now, that's the power of good advice!"
    scene cc_lobby with dissolve
    show cashier at center
    show cs at left
    with determination
    show arceus at right with moveinright
    n "Arc catches up with CS, at the sign up table."
    signup "...and you said your last name is... 188?"
    cs "Yeah, this confuses everyone."
    cs "Oh, hey Arc! Whatcha doing?"
    arceus "Just came to support my friend."
    cs "Aw, thanks man."
    signup "OK, that's you all registered. Fuzzy guy, you signing up too?"
    arceus "Nah, I feel like that would be basically cheating."
    cs "OK, well I have to go to the backstage and get set up. See you soon, Arc!"
    scene cc_backstage with dissolve
    show cs at left with moveinleft
    n "CS walks to the backstage to prepare to compete, when he notices a familiar face."
    show digi at right with moveinright
    cs "Wait, Digi?!"
    digi "CS?!"
    cs "What are you doing here?"
    digi "I always compete in the Pencil Sharpening Competition! I was inspired after that video of yours."
    cs "Oh wow, really? Thank you, I guess!"
    cs "Do you think we'll be up against each other?"
    digi "I mean, probably, I'm the champ."
    cs "You?!"
    digi "Five years running."
    cs "Oh jeez, I guess we will be against each other, if I make it that far."
    digi "Well, good luck to you!"
    cs "You as well!"
    scene black with fade
    n "After a grueling competition, CS climbs his way up to the top of the bracket!"
    scene black
    show stage_screen as stage_screen_l at t_stage_screen_l
    show con_screen at t_stage_screen_c
    show stage_screen as stage_screen_r at t_stage_screen_r
    show cc_stage
    with fade
    show cs at left with moveinleft
    cs "Well, I've made it this far. I guess it's just me versus Digi now..."
    show digi at right with moveinright
    n "Digi steps up to the stage."
    show digi at mid_mid_right with move
    n "Digi goes to shake CS' hand."
    show cs happy at mid_mid_left with move
    n "CS grabs Digi's hand."
    cs "Well, good luc--"
    n "Digi's hand grips CS stronger than a human could possibly grip."
    show cs worried with vpunch
    cs "Yow!"
    digi "Oops, sorry, let me just..."
    show cs
    n "Digi pokes a panel on his arm."
    digi "Sorry about that, arm must have been on the wrong setting."
    n "CS thinks to himself."
    show cs concentrate
    cs "{i}Shoot, I forgot Digi is a cyborg! How am I going to have any shot at beating him?{/i}"
    cs "{i}I'm just going to have to try my hardest!{/i}"
    hide digi
    hide cs
    with dissolve
    show mettaton at t_stagescreen onlayer broadcast
    host "WELCOME, FOLKS!"
    host "EVERYONE GIVE A BIG HAND TO OUR WONDERFUL CONTESTANTS!"
    show crowd at t_stagescreen onlayer broadcast
    n "The crowd explodes into uproarious applause."
    hide crowd onlayer broadcast
    host "ON 'GO!', THESE LOVLIES WILL BE COMPETING TO SEE WHO CAN {color=#ffff00}SHARPEN THE MOST PENCILS!"
    host "THIS TRULY IS THE BATTLE OF A CENTURY FOLKS! DIGIDUNCAN, OUR LONG TIME CHAMP, GOES UP AGAINST A NEWCOMER, THE AMAZING CS188!"
    show crowd at t_stagescreen onlayer broadcast
    n "The crowd is going wild."
    hide crowd onlayer broadcast
    host "ALL THEY HAVE TO DO IS {color=#ffff00}SHARPEN THE PENCILS AS QUICKLY AS POSSIBLE,{/color} WITHOUT {color=#ffff00}GETTING THE ERASER STUCK!"
    host "IT'S A TRULY MAGICAL EVENT, AND YOU'RE ALL ABOUT TO WITNESS IT! ARE YOU ALL READY?"
    show crowd at t_stagescreen onlayer broadcast
    n "The crowd is going absolutely crazy."
    hide crowd onlayer broadcast
    host "AND WITH THAT, LET'S BEGIN! READY?"
    n "CS glances over at Digi, and they nod at each other."
    host "3..."
    if fun_value(50, "archack"):
        n "Digi looks to be smacking his arm."
    else:
        n "A whirr is heard as Digi's arm motors charge up."
    host "2..."
    n "CS concentrates, his hands ready to sharpen like his life depends on it."
    host "1..."
    n "Both competitors hover their hands over the pencils..."
    host "GO!"
    jump play_pencilgame

label win_pencil:
    host "HOLY TICONDEROGA! WE HAVE A WINNER!"
    show crowd at t_stagescreen onlayer broadcast
    n "As if they couldn't get any louder, the crowd is going insane."
    hide crowd onlayer broadcast
    host "THE CHAMP HAS FALLEN! LADIES AND GENTS, WHAT AN UPSET!"
    n "CS turns to Digi."
    hide mettaton onlayer broadcast
    show cs happy at t_stagescreen onlayer broadcast
    cs "Good game!"
    hide cs onlayer broadcast
    show digi at t_stagescreen onlayer broadcast
    digi "Same to you man, that was wild!"
    hide digi onlayer broadcast
    show cs at t_stagescreen onlayer broadcast
    cs "I don't know how I beat you, honestly."
    hide cs onlayer broadcast
    show digi at t_stagescreen onlayer broadcast
    n "Noticable smoke is coming out of Digi's arm."
    hide digi onlayer broadcast
    show cs at t_stagescreen onlayer broadcast
    cs "You good, Digi? Your arm is kinda..."
    hide cs onlayer broadcast
    show digi at t_stagescreen onlayer broadcast
    n "Digi looks at his arm."
    digi "Oh shi-- {w=0.5}uh, I'll be back."
    hide digi onlayer broadcast with moveoutright
    n "Digi runs off."
    show arceus at t_stagescreen onlayer broadcast with moveinright
    n "Arc runs on stage."
    arceus "Holy shit, CS, you did it! That was amazing!"
    hide arceus onlayer broadcast
    show cs at t_stagescreen onlayer broadcast
    cs "Thank you! I don't even know what I won!"
    hide cs onlayer broadcast
    show mettaton at t_stagescreen onlayer broadcast
    host "YOU'VE WON... {w=0.5}A BRAND NEW..."
    hide mettaton onlayer broadcast
    show cs at t_stagescreen onlayer broadcast
    cs "Computer? Television? Car?!"
    hide cs onlayer broadcast
    show mettaton at t_stagescreen onlayer broadcast
    host "... {w=0.5}{color=#ffff00}PENCIL SHARPENER!"
    hide mettaton onlayer broadcast
    show cs at t_stagescreen onlayer broadcast
    cs "I should have seen that coming."
    hide cs
    scene cc_crowd
    cs "Well that was a lot of excitement for one day, let's head home."
    n "Though he was working harder to support CS, Arceus couldn't help but look relieved to be back on track."
    arceus "Absolutely."
    billy "Let's get back in my car!"
    scene cc_parking_lot
    show cs flipped at right
    show arceus at mid_right
    show billy at center
    with fade
    show digi flipped at left with moveinleft
    n "Digi runs up to the group."
    digi "Hey, uh, can I get a ride?"
    cs "Huh?"
    if event_happened("archack"):
        digi "Well, my arm got hacked, or something, so I lost."
        arceus "Heh."
    else:
        digi "Usually, they'd pay for my train home, but I uh, lost."
    cs "Ooh, right."
    cs "Billy, we got room for one more?"
    n "Billy looks at Digi."
    billy "He and Arc are both pretty small, I think they'll fit in the back just fine."
    show arceus at right with moveinright
    arceus "Hey!"
    show arceus flipped
    hide arceus with moveoutright
    cs "Well, Digi, you got a ride!"
    digi "Thanks so much, man!"
    jump car_dialogue

label back_home:
    scene cs_house with fade
    play music "<loop 0>park_theme.mp3" volume 0.5
    music Park Theme - Lorin Nelson
    n "After the long and treacherous journey, CS finally arrives at his house."
    show arceus flipped at left with moveinleft
    arceus "We made it back to your house, CS!"
    show cs flipped at center with moveinright
    cs "Finally I'm home..."
    cs "Arceus, thank you so much for everything on this trip. I couldn't have done it without you."
    arceus "Aw, it was nice helping ya here."
    cs "You too, Billy."
    show billy at mid_left behind arceus with moveinleft
    billy "No problem!"
    cs "Well, I guess I should get some rest."
    cs "If you guys want, we can have a party at my place tomorrow to celebrate all the shit we went through!"
    "Arc and Billy" "Hell yeah!"
    show arceus at left with determination
    hide billy with moveoutleft
    hide arceus with moveoutleft
    n "As CS was saying bye to his friends, a familiar but upsetting voice can be heard at the front of CS' house."
    stop music fadeout 1.0
    music end
    ed "YOU!"
    show cs disappointed at left with moveinleft
    n "CS and the gang look forth at CS' front porch, where Richard and Ed are waiting angrily for him."
    play music "<loop 0>hohsisremix.mp3" volume 0.5
    music "Alfred's Theme - Eminem"
    show ed at right
    show rich at mid_mid_right behind ed
    with moveinright
    ed "I have been waiting for you for quite some time now."
    rich "We've been trying to stop you for a while now, but this is final stop for you."
    cs "HoH SiS?? What do you guys still want from me?"
    ed "What do you think, CS? After you put Wesley in the hospital? After you crippled most of our workers?"
    cs "Well, you guys scammed me out of my money and broke my computer! Of course I wanted some kind of revenge!"
    ed "Why do you think this all started?"
    cs "I--{w=0.5} I don't know, because you're evil?"
    ed "CS, you put our company to shame long ago."
    ed "When you made that parody video of us that you call a \"YTP\", people wouldn't stop harrassing us about it."
    rich "You tried to humiliate us with your videos, with others thinking we were a joke."
    ed "You see, my ancestors came from the planet JoJ many years ago to live here and start a foundation company."
    ed "It was the best damn foundation company in the world."
    ed "We repaired more than 50%% of all foundations on the planet, and now... you."
    ed "You. You embarrassed us with those silly, stupid, videos that dragged our family company through the mud."
    rich "That's why Ed wanted to get revenge on you. That's why we destroyed your computer, CS."
    cs "I don't understand..."
    menu:
        "Fight" (type = "bad"):
            jump fighthohsis
        "Negotiate" (type = "true"):
            jump talktohohsis
        "Fuck up" (type = "bad"):
            jump fuckuphohsis
        "Call Copguy":
            jump copsathohsis

label talktohohsis:
    cs "I never intended to harm your company, I just thought that the video was a good source to YTP."
    cs "I'm sorry about all those prank callers, I even made a video telling people to stop prank calling you."
    cs "I never had bad intentions for you guys... honestly it was also kind of like a free promotion."
    ed "Well, I'm sorry CS, but it's too late."
    ed "Richard, get the JoJ UFO and vaporize the house."
    stop music fadeout 1.0
    show anno at offscreenleft
    play music "<loop 0>track3.mp3" volume 0.4
    music Track 3 - Weatherscan
    "???" "Wait!!!"
    n "A voice can be heard behind the group running up to them."
    cs "Anno?"
    show anno at center behind doug with moveinleft
    anno "You guys can't just destroy CS' house!"
    ed "Why not?"
    anno "I don't know, because..."
    anno "CS wasn't trying to harm you!"
    show arceus flipped at mid_left_left with moveinleft
    arceus "Yeah, CS' videos are hilarious, and honestly if I knew you guys before this I would've called you up for help on my house."
    arceus "If y'know, I didn't go after that one politican."
    ed "Well okay, but--"
    n "Even more of CS' friends show up at the scene."
    show cs at left
    show linus at mid_left behind phil with moveinleft
    linus "Yeah, I loved those videos about HoH SiS, and we'd love for you to come up fix up some of the damages at the LTT offices."
    show taran flipped at mid_mid_left behind cs with moveinleft
    show luke at mid_left_left behind cs with moveinleft
    show colton at default behind doug with moveinleft
    taran "What damages?"
    luke "Y'know, when Linus ran his car into the back of the building?"
    colton "Finally, something that wasn't my fault."
    show michael at mid_mid_left behind cs with moveinleft
    michael "If I get my chocolate cake, you fellows at HoH SiS can fix up my house too."
    show phil at mid_left behind cs with moveinleft     
    phil "I can help too, with the power of Flex Tape!"
    show doug at center behind cs with moveinbottom
    doug "I don't know what I'm doing here, but yeah, good job guys!"
    show cashier at mid_mid_right behind cs with moveinleft
    cashier "Yeah! Go CS!"
    show border_guard at mid_mid_left behind cs with moveinleft
    border_guard "I'm important too, eh!"
    cs "Wow, I don't know how you all got here coincidently, but I appreciate it!"
    show cs at left
    rich "Oh my god, that's so many people!"
    ed "Okay okay, I get it."
    hide anno
    hide arceus flipped
    hide linus
    hide taran flipped
    hide luke
    hide colton
    hide michael
    hide phil
    hide doug
    hide cashier
    hide border_guard
    with moveoutleft
    ed "We won't do anything to your house, and we are sorry for destroying your laptop."
    cs "And I'm sorry for injuring your coworkers."
    stop music fadeout 3.0
    music end
    ed "Wesley is still in the hospital, so like, if you wanted to, give us some more money..."
    show cs disappointed at left
    cs "Didn't you scam me out of more money than my foundation was worth?"
    ed "Oh yeah..."
    show cs angry at left
    cs "What {i}about{/i} my foundation as well?"
    show cs at left
    cs "Tell you what: if you can fix my foundation, I'll pay you for that, and we put this all behind us."
    rich "What do you think, Ed?"
    n "Ed ponders for a moment."
    ed "Sure. We have a deal."
    show cs happy at left
    cs "Hooray!"
    n "As if the crowd couldn't get any bigger, the cops show up."
    show cs at left
    show copguy at center with moveinleft
    copguy "Hey CS, we finally found HoH SiS."
    copguy "And it looks like you did too."
    show sheriff at mid_left with moveinleft
    sheriff "Goodjob Copguy, time to put them in the slammer!"
    cs "No need guys, we worked everything out."
    sheriff "What?!"
    copguy "Are you sure?"
    ed "Yep, we got everything under control."
    sheriff "All this for nothing..."
    sheriff "Whatever, c'mon Copguy, let's go."
    n "The cops get back in their car and speed off."
    hide sheriff with moveoutleft
    hide copguy with moveoutleft
    hide ed with moveoutright
    hide rich with moveoutright
    show cs at mid_right with moveinright
    n "After all that commotion, CS finally steps up to his front door."
    show cs flipped at mid_right
    n "CS looks back out into the crowd again one more time."
    cs "This is CS..."
    cs "Signing out!"
    play sound "cheers.ogg" volume 0.7
    pause 2.0
    n "The crowd errupts in cheers as CS finally enters his house."
    scene cs_room with fade
    play music "<loop 0>ac_title.mp3" volume 0.4
    music New Leaf Title Theme - Kazumi Totaka
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    if fanbase == "both":
        jump true_ending
    elif fanbase == "ltt":
        jump ltt_ending
    elif fanbase == "ytp":
        jump ytp_ending
    else:
        jump secret

label true_ending:
    $ persistent.true_ending = True
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor that has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have to work with us again virtually, just give us a call\"."
    cs "I'll have to make sure to call them later!"
    menu:
        "Go to sleep":
            jump archival
        "Stream":
            jump streaming

label streaming:
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys! CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    "Chat" "Yeah what happened to you?{w=0.25} Oh my god, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs happy at mid_left
    cs "Well guys..."
    n "CS chuckles."
    cs "It's a long story..."
    if preferences.csbounciness == 1.0:
        $ achievement_manager.unlock("Boingy Boingy Boingy")
    scene black with fade
    stop music fadeout 1.0   
    play music "secret/credits.mp3" volume 0.5
    centered "Pretend there's credits here."
    jump secret2

label ytp_ending:
    n "CS looks over at his desk, where his old computer is sitting."
    scene cs_room_2 with fade
    show cs at mid_left
    cs "Oh yeah, I forgot I actually have a computer that's not a craptop."
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys! CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    "Chat" "Yeah what happened to you?{w=0.25} Oh my god, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well guys..."
    n "CS chuckles."
    cs "It's a long story..."
    scene black with fade
    stop music fadeout 1.0   
    play music "secret/credits.mp3" volume 0.5
    centered "Pretend there's credits here."
    jump secret2

label ltt_ending:
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor that has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have to work with us again virtually, just give us a call\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys! CS here! Sorry I was gone for a couple weeks!"
    n "The chat slowly comes in, confused."
    "Chat" "Oh you're streaming?{w=0.25} I thought you were working for LTT now?{w=0.25} What happened to the YTPs?{w=0.25} Are you OK?{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well guys..."
    cs "It's a long story..."
    scene black with fade
    stop music fadeout 1.0   
    play music "secret/credits.mp3" volume 0.5
    centered "Pretend there's credits here."
    jump secret2

label fighthohsis:
    n "CS challenges HoH SiS to a fight."
    show cs angry
    cs "I beat up all your workers and Wesley, I can take you guys down too!"
    cs "Let's go!"
    ed "Richard, stand back."
    hide rich with moveoutright
    cs "C'mon! Hit me!"
    ed "I'm going to refund my fist into your face!"
    show cs at center
    show ed at center
    with move
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show cs with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show ed with vpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show cs with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show ed with vpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show cs with hpunch
    play sound "alt_punch.ogg"
    show cs at t_punchup with move
    show cs with vpunch
    show ed at right with move
    hide cs
    pause 2.0
    show cs disappointed at mid_left with moveintop
    cs "I no longer want the joj..."
    hide cs with moveoutbottom
    show ed with hpunch
    ed "Time to take a shit on the house."
    return

label fuckuphohsis:
    show cs angry
    cs "Yeah I actually hate you guys, and I wanted to mess with your business!"
    cs "You guys suck and I hate you both!"
    cs "You guys deserve to have your company in shambles!"
    n "Richard and Ed back up to their UFO."
    hide rich
    hide ed
    with moveoutright
    cs "Hey! Where are you guys going!"
    cs "Come back here!"
    n "The JoJ UFO flies up over the house and vaporizes the house."
    play sound "beam.ogg" volume 0.6
    show beam at xstretch_in
    pause 1.5
    show cshouse_vaporized behind beam
    show beam at xstretch_out
    pause 1.0
    show cs disappointed at left
    with vpunch
    n "Ed flips CS off, and then flies away."
    show cs disappointed
    pause 1.0
    cs "Fuck."
    return    

label copsathohsis:
    n "CS calls Copguy to come arrest HoH SiS."
    show cs worried
    stop music fadeout 1.0
    music end
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" loop volume 0.5
    show copguy at center with moveinleft
    cs "Here they are! They scammed me out of my money and services!"
    n "Copguy cuffs the HoH SiS members and pulls out his walkie."
    copguy "We got them, sheriff. Time to bring them to the slammer."
    hide copguy
    hide rich
    hide ed
    with moveoutright
    stop sound fadeout 1.0
    hide blue_light
    hide red_light
    show cs
    cs "Welp. That was easy."
    cs "Finally, I can rest at home."
    n "CS walks up to his house and enters."
    scene cs_room with fade
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    jump true_ending
