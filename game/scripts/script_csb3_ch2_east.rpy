label east:
    cs "Well, since east is the way home, we should probably go that way."
    show arceus
    arceus "Alright, that sounds like a good idea."
    n "CS and Arceus keep following the road for a while until they come across a small town."
    scene town with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    cs "Oh my God! We found civilization again!"
    arceus "Thank God."
    n "The two look around for a bit until they see a gas station close by."
    cs "Let's head over to that gas station so we can pick up something to eat."
    n "CS and Arceus head over to the convenience store at the gas station."
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
    arceus "Yeah... I have no clue currently."
    arceus "I was hoping that we could hitchhike on a bus or something, but it might be ages until that happens, if it even {i}does{/i} happen... This town is too small for a bus route."
    stop music fadeout 3.0
    music end
    menu:
        "Wait for driver at the gas station" (type = "true"):
            jump billy_driver
        "Hotwire a car" (type = "bad"):
            jump hotwire

label hotwire:
    stop music
    scene gasinside
    show cs at left
    show arceus at right
    cs "I don't know... We could just... hotwire a car?"
    arceus "I can probably do that. Let's go look."
    scene gasoutside with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    n "CS and Arceus approach one of the cars in front of the gas station."
    n "Arceus smashes open the window and opens the door from the inside."
    arceus "Alright, so if we connect this to this..."
    n "The car starts up."
    cs "Hell yeah! Let's go home!"
    n "As if on cue, sirens and lights approach the two."
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" volume 0.5
    show copguy at center with moveinright
    show cs disappointed
    show arceus worried
    copguy "I could hear the sound of a car window breaking from miles away!"
    copguy "You guys already blew it! Back to the slammer!"
    bad_end "What did Copguy\njust tell you?" "choose_direction"

label billy_driver:
    cs "Why don't we just wait for someone at the gas station to come out, and then we ask them for a ride?"
    n "CS walks over to someone's car parked in the front of the gas station."
    scene gasoutside with fade
    show cs at left with moveinleft
    show arceus worried at right with moveinright
    arceus "Are you crazy? To drive all the way back to New York, in a stranger's car, at that?"
    arceus "Besides, how are we even going to pay the guy anyway?"
    cs "Well, we don't have to go all the way to New York. We could go a small distance then ask another driver."
    show arceus angry
    arceus "That would be even more in gas money!"
    n "As the two are arguing, the owner of the car approaches them."
    unknown "What are you doing next to my car?"
    cs "Oh, hi."
    cs "Do you think you can give us a ride to New York?"
    unknown "Oh, uhh, hold on a second!"
    n "The mysterious driver walks behind the store."
    arceus "What are you doing? That man looks like he's going to kill us!"
    arceus "He's probably getting a gun, we need to lea--{w=1.5}{nw}"
    show billy at center with moveinleft
    play music "<loop 0>mm_select.mp3" volume 0.3
    music Mm Select - Matthew Simmonds
    billy "Hi, Billy Mays here for the Uber Driver!"
    billy "The fast and easy way for people who don't have a car to get around!"
    show cs happy
    cs "Sweet! We need to get to upstate New York. Do you think you can help us?"
    billy "Absolutely! For only $19.95, I'll take you both to New York!"
    cs "Alright, well, it's settled! We have our driver, Arceus!"
    arceus "..."
    show arceus
    arceus "...What the fuck? Works for me, I guess."
    cs "Hell yeah! I call shotgun!"
    n "CS and Arceus get into Billy's car."
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
    cs "Alright, so, it's just a straight shot to New York?"
    show billy car turn
    billy "Yep! We are gonna head through Idaho and Montana first, so get ready to see the sights!"
    show billy car happy
    cs "Yeah! It's almost like a vacation!"
    arceus "Well, on a vacation, you usually have money to spend on all the crazy parts you see."
    cs "Let's just enjoy the ride there, at least."
    arceus "Fair point."
    stop music fadeout 3.0
    music end
    jump montana

label montana:
    scene car background
    show billy car
    with fade
    play music "<loop 0>weird_personalities.mp3" volume 0.6
    music Weird Personalities - Lizardking
    n "After a few hours of driving through Idaho, the trio finds themselves in the middle of Montana."
    n "Arceus is sleeping while CS peers out the window."
    cs "Are we there yet?"
    show billy car turn
    billy "Nope!"
    show billy car
    cs "Aw, man..."
    show billy car turn
    billy "We've still got a ways to go! We aren't even a {i}quarter{/i} of the way yet!"
    show billy car
    cs "Alright, I'll just... keep looking at the trees pass by."
    billy "Well, good news for you! There is a small town up ahead!"
    billy "I was gonna buy some new supplies for my gadgets, if you guys want to pick out anything."
    cs "Sure! I love buying random things!"
    cs "What about you, Arceus?"
    n "..."
    cs "Hey, Arc!"
    billy "CS, you should probably leave the dog thing in the back alone."
    n "Arceus immediately jerks straight up."
    arceus "What did you just call me?"
    billy "Nothing!"
    scene hardwareoutside
    show billy car
    billy "Here we are, at the store. I'll be back here in a few."
    stop music fadeout 3.0
    music end
    cs "Same, I'll come with you."
    n "Arceus goes back to sleep in the car."
    play sound "doorslam.ogg"
    scene hardwareinside with fade
    play music "<loop 0>home_depot.mp3" volume 0.4
    music "Let's Do This - Home Depot"
    show cs at left with moveinleft
    cs "Wow, look at all this stuff!"
    cs "They've got Allen wrenches, gerbil feeders, toilet seats, electric heaters,{nw}"
    cs "Trash compactors, juice extractor, shower rods and water meters,{nw}"
    cs "Walkie-talkies, copper wires, safety goggles, radial tires,{nw}"
    cs "BB pellets, rubber mallets, fans and dehumidifiers,{nw}"
    cs "Picture hangers, paper cutters, waffle irons, window shutters,{nw}"
    cs "Paint removers, window louvres, masking tape and plastic gutters,{nw}"
    cs "Kitchen faucets, folding tables, weather stripping, jumper cables,{nw}"
    cs "Hooks and tackle, grout and spackle, power foggers, spoons and ladles,{nw}"
    cs "Pesticides for fumigation, high-performance lubrication,{nw}"
    cs "Metal roofing, water proofing, multi-purpose insulation,{nw}"
    cs "Air compressors, brass connectors, wrecking chisels, smoke detectors,{nw}"
    cs "Tire gauges, hamster cages, thermostats and bug deflectors,{nw}"
    show cs worried
    cs "Trailer hitch demagnetizers, automatic circumcisers,{nw}"
    show cs
    cs "Tennis rackets, angle brackets, Duracells and Energizers,{nw}"
    cs "Soffit panels, circuit breakers, vacuum cleaners, coffee makers,{nw}"
    cs "Calculators, generators, matching salt and pepper shakers,{nw}"
    cs "and, I think that's it..."
    cs "Ooh! Look at all this paint!"
    cs "Let's get some {color=#FF9900}orange{/color}, {color=#7897FF}blue{/color}, {color=#CB50FF}purple{/color}..."
    show cs happy
    cs "More {color=#FF0000}c{/color}{color=#FFCC00}o{/color}{color=#FFFF00}l{/color}{color=#CCFF00}o{/color}{color=#00FF00}r{/color}{color=#00FFCC}s{/color}, I need {bt=a3-p10-s4}{color=#00FFFF}m{/color}{color=#00CCFF}o{/color}{color=#7978FF}r{/color}{color=#CC00FF}e{/color} {color=#FF00FF}c{/color}{color=#FF00CC}o{/color}{color=#FF0000}l{/color}{color=#FFCC00}o{/color}{color=#FFFF00}r{/color}{color=#CCFF00}s{/color}{color=#00FF00}!{/color}"
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
    cs "{bt=a3-p10-s4}Letsgoletsgoletsgoweneedtogetoutofhere"
    hide cs with moveoutright
    hide billy with moveoutright
    stop music fadeout 3.0   
    music end
    play sound "doorslam.ogg"
    scene hardwareoutside
    show billy car
    with fade
    billy "That was quite the experience. I should've brought my Hercules Hook!"
    cs "Yeah, really, let's get out of here!"
    arceus "Huh? What's going on?"
    cs "Nothing, Arc. I, just, uh... slipped and fell in the store."
    arceus "Okay, whatever, I'm going back to sleep..."
    n "Billy takes off out of the parking lot."
    scene car background night
    show billy car
    with fade
    cs "Man, today was also pretty crazy."
    arceus "Yeah, at least I got some sleep after all of it."
    cs "Speaking of which, can we find a place to rest soon?"
    billy "Yeah, let's see if I can find a place to stop at."
    billy "Wait a second, what the hell?"
    n "Billy brings the car to a screeching halt."
    play sound "<from 0 to 2>car_crash.ogg" volume 0.7
    scene cultforest
    show billy car
    play music "<loop 0>candle_world.mp3" volume 0.4
    music Candle World - Kikiyama
    "CS and Arceus" "What in the world?"
    n "Ahead lies a barricade with a bunch of strange hooded people surrounding it."
    show cultist at mid_right behind billy with moveinright
    n "One of the members walks up to the driver's side and knocks on the window."
    play sound "roll_window.ogg" volume 0.7
    n "Billy rolls down the window."
    billy "Hi, it's Billy! What are you doing by my car?"
    cultist "Get out of the car."
    billy "No, it's {i}my{/i} car!"
    show cultist gun
    n "The cultist pulls out a revolver and aims at Billy's head."
    cultist "Does this look like a joke to you guys?"
    cultist "Out of the car. Now."
    n "Billy shrugs and opens the door, with the cultist leader still aiming the gun to his head."
    cultist "You two, as well. Out."
    n "CS and Arceus both step out of the car."
    hide cultist with moveoutright
    hide billy car with fade
    show billy at mid_mid_left
    show cs disappointed at mid_left
    show arceus worried flipped at left
    with moveinleft
    show cultist at mid_right with moveinright
    cultist "So, do you want to explain what is going on here?"
    cs "Uhm, we were heading on past here to the next--"
    show cultist gun
    n "The cultist aims his gun at CS."
    cultist "Look, I don't care where you are going."
    show cultist at center with moveinleft
    cultist "We are part of the Blue Branch Cult, and our motto is that we hate everything."
    show arceus flipped
    arceus "Like, everything?"
    show cultist gun
    n "The cultist aims at Arceus."
    cultist "You wanna fuck with me?"
    arceus "I mean, if you're offering."
    n "The cultist looks annoyed."
    show cultist
    cultist "I'm gonna get the rest of the gang to deal with you guys. Don't fucking move."
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
    n "Billy goes to the back of the car and starts digging around in the trunk."
    arceus "Never thought we'd run into cultists, out of all people."
    show cs flipped with determination
    hide cs with moveoutleft
    n "CS starts rummaging around in the trunk, too."
    arceus "CS, what are you doing?"
    show arceus worried flipped
    arceus "CS?!"
    show cs fakegod at center with moveinleft
    cs "Look at me! {bt=a3-p10-s4}{color=#CB50FF}I'm purple!{/color}"
    $ renpy.music.set_pause(True, "music")
    play sound "secret/funni.ogg" volume 0.5
    pause 3.0
    stop sound
    $ renpy.music.set_pause(False, "music")
    show arceus angry flipped
    arceus "CS, what the fuck are you doing...?!"
    arceus "You are going to definitely get us killed!"
    n "Arceus hides behind the car as the cultist leader brings two others with him."
    show arceus angry with determination
    hide arceus with moveoutleft
    show cs fakegod at left with moveinleft
    show cultist_2 at mid_mid_right with moveinright
    show cultist_3 at right with moveinright
    show cultist at mid_right with moveinright
    $ persistent.seen.add("cultist2")
    cultist "Alright, they're over here at this car."
    cultist_2 "No way..."
    cultist_3 "It's CSGod!"
    cultist_2 "Praise CSGod!"
    cultist "Oh no! It's the one thing that we {i}don't{/i} hate!"
    cs "Huh?"
    cs "I mean,"
    cs_fakegod "Yeah, that's right, it's me, CSGod!"
    cs_fakegod "You'd better leave these three alone, or I'll, uh, {i}smite{/i} you!"
    cultist "CSGod doesn't smite, he uses YTP Mag--{w=0.5}"
    cs_fakegod "Don't tempt your god! I will edit you so hard that you'll look like you came from an AwfulFawful YTP!"
    cultist_2 "We're sorry! We'll leave!"
    n "Billy comes up behind CS with one of his gadgets."
    show cs fakegod at mid_offscreen_left with move
    show billy laser at mid_left with moveinleft
    stop music fadeout 1.0 
    play music "<loop 0>blazing_corridor.mp3" volume 0.4    
    billy "Fire a laser! Fire a laser!"
    play sound "minigames/car/gaster_blast.wav"
    show laser_beam at t_gun behind billy
    hide cultist_2 with moveoutright
    hide laser_beam
    n "Massive laser shots land between the cultists as they scramble away!"
    cultist_3 "I don't wanna turn into a YTP! Go, guys, {i}go!{/i}"
    play sound "minigames/car/gaster_blast.wav"
    show laser_beam at t_gun behind billy
    hide cultist_3 with moveoutright
    hide laser_beam
    pause 0.5
    play sound "minigames/car/gaster_blast.wav"
    show laser_beam at t_gun behind billy
    hide cultist with moveoutright
    hide laser_beam
    n "The cultists disappear into the forest."
    stop music fadeout 3.0 
    music end
    billy "{i}That's{/i} the power of the Awesome Augement!"
    play music "<loop 0>showtime.mp3" volume 0.4
    music "It's Showtime - Toby Fox"
    show cs fakegod at center with moveinright
    cs "Hooray! I'm a god now!"
    show arceus flipped at left with moveinleft
    arceus "CS, I don't know how you pull this stuff off."
    show arceus worried flipped
    arceus "Am I still sleeping?"
    n "Arceus pinches himself."
    show arceus angry flipped
    arceus "Fuck."
    arceus "How many divine beings and reality benders do we have in this universe, anyhow?"
    cs "Alright, back on the road to New York!"
    stop music fadeout 3.0
    music end
    scene car background night
    show billy car
    with fade
    n "The gang gets back in the car and books it out of the forest."
    n "After a while, Billy pulls the car into a small area at the edge of the forest to let everyone rest."
    scene black with fade
    n "The night passes, then they set off once again."
    scene car background
    show billy car
    play music "<loop 0>mort_farm.mp3" volume 0.4
    music "Mort's Farm - ClascyJitto"
    cs "Can we stop somewhere to eat? We haven't eaten since yesterday."
    arceus "Yeah, unfortunately, the one store you guys {i}did{/i} go to didn't have anything edible."
    billy "Sure, yeah, there's a McDonald's up here in a couple miles."
    scene mcdonalds
    show billy car
    play sound "roll_window.ogg" volume 0.7
    n "Billy pulls up to the drive-thru to place his order."
    cashier "Hello, what would you like to order?"
    billy "Hi, Billy Mays here! I would like to get the Buy 1 Get 1 Free breakfast meal for my friends here,"
    billy "and I would also like to get the Egg McMuffin and a Big Mac for me."
    cashier "Sure thing, that'll be--{nw}"
    billy "But I'm not done yet! I would like to triple the offer and get three Big Macs, and also three large sodas without any shipping!"
    cashier "Uhh, yeah, we can do that without shipping."
    cashier "That'll be about, let's see..."
    cashier "$36.88."
    billy "Wow! What a deal! I'm coming around to pick up my order!"
    scene black with fade
    n "Billy drives through and picks up everyone's meals."
    scene mcdees
    show billy car
    with fade
    n "CS and Arceus happily chow down on the Mickey D's they just got."
    arceus "Thank God for that."
    cs "I have never been so excited to get a Big Mac."
    scene car plains
    show billy car
    with fade
    n "Billy heads out on the open road again as they enter the state of South Dakota."
    jump south_dakota

label south_dakota:
    arceus "Welcome to the Great Plains."
    cs "Woohoo!"
    stop music fadeout 3.0
    music end
    arceus "I don't think you should be super excited. There is, like, nothing here."
    cs "Oh, yeah, we don't even have trees to look at anymore."
    cs "Is there anything to do in this state?"
    arceus "There's Mount Rushmore, I guess there's Wall Dr--{w=0.5}"
    cs "Oh, hell yeah! Let's go to Mount Rushmore!"
    scene black with fade
    n "About an hour later, the crew arrives at Mount Rushmore."
    scene rushmore with fade
    n "They all hike up to the viewing spot to get a good look at the founding fathers."
    play music "<loop 0>taiikusai_desu_yo.mp3" volume 0.4
    music Taiikusai Desu Yo - Satoru Kosaki
    show cs at right with moveinleft
    show arceus flipped at center with moveinleft
    show billy at left with moveinleft
    billy "Wow, to think that we won a war without the Gopher."
    billy "How did they even communicate without the Jupiter Jack?"
    show cs concentrate
    arceus "It'd be cool if I had my face carved into a mountain. Wouldn't that be neat, CS?"
    show arceus flipped at center
    n "Arceus looks over at CS concentrating on something intensely."
    arceus "CS? Are you okay?"
    show arceus worried flipped at mid_right with moveinleft
    n "As Arceus starts to approach CS, the onlookers surrounding them all gasp loudly."
    play sound "gasp.ogg" volume 2
    scene csmore
    show cs concentrate at right
    show arceus worried at center
    show billy at left
    with hpunch
    arceus "Huh?"
    show cs happy
    cs "There we go! Fixed!"
    n "Arceus looks back at Mount Rushmore.... which now has CS, Arceus, and Billy's faces carved into the stone!"
    hide cs with moveoutright
    show arceus worried flipped
    arceus "You scare me, CS. I don't even... {i}want{/i} to question how or why."
    show arceus happy flipped
    arceus "{size=-12}I {i}do{/i} look pretty cool though."
    stop music fadeout 3.0
    music end
    n "The gang gets back in the car before the overwhelming crowd of people engulfs the site after what just happened."
    scene car plains
    show billy car
    with fade
    n "They continue to drive through the massive and empty plains of South Dakota."
    play music "<loop 0>track4.mp3" volume 0.4
    music Track 4 - Weatherscan
    n "By the time they reach Sioux City, it is already evening."
    cs "There really {i}is{/i} nothing out here, is there?"
    arceus "Nope. I don't get how people can even {i}live{/i} here."
    billy "We're, like, halfway through the Midwest. We've only got a couple states left to travel before we are in the heartland."
    n "Billy follows the Missouri River down until they arrive in Omaha."
    jump nebraska

label nebraska:
    scene omaha
    show billy car
    with fade
    n "The gang finally hits Omaha right before sundown."
    cs "{i}This{/i} is the biggest city here? This is pretty small."
    billy "It looks very quaint. Hopefully we can find someplace to stay tonight."
    billy "I have no damn clue where to go here."
    arceus "Let's get out and look for somewhere to eat."
    hide billy car
    show cs at mid_left
    show arceus flipped at center
    show billy at mid_right
    show pakoo flipped at offscreenleft
    with moveinleft
    n "They all get out and start roaming the streets."
    n "Suddenly, CS hears a voice behind him."
    unknown "CS? Is that you?"
    cs "Huh?"
    show cs flipped
    stop music fadeout 3.0
    music end
    n "CS turns around and sees a wacky...{w=0.5} thing, with a tophat on."
    show pakoo flipped at left
    show billy at right
    show arceus at mid_mid_right
    show cs flipped at center
    with ease
    pakoo "Yeah, hey, it {i}is{/i} you!"
    pakoo "Arceus, you too? And, Billy... Mays?"
    billy "Hi, it's Billy!"
    arceus "Hey, Pakoo."
    cs "Yeah! I haven't seen you in a while. I never thought you'd live in a place like {i}this!{/i}"
    pakoo "I never thought you guys would come down to Omaha. There's, like, nothing here."
    cs "We've been through a lot recently. Do you know somewhere we can eat and rest for the night?"
    n "Pakoo thinks for a moment."
    pakoo "I think I know a place."
    n "Pakoo takes the gang over to the old market section of Omaha."
    show cs
    show arceus flipped
    with determination
    hide pakoo
    hide cs
    hide billy
    hide arceus
    with easeoutright
    scene alleyway with fade
    show pakoo flipped at center
    show billy at right
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    show pakoo with determination
    pakoo "Here we are! This is probably the best location to eat at..."
    pakoo "At least, that I know of."
    scene peppinopizzabg
    show peppinopizzafg
    with fade   
    play music "<loop 0>funiculi_holiday.mp3" volume 0.3
    music Funiculi Holiday - ClascyJitto
    show peppino at t_pepzone1 behind peppinopizzafg with moveinleft
    show peppino at t_pepzone2 behind peppinopizzafg with ease
    show pakoo flipped at mid_right with moveinleft
    show pakoo with determination
    show billy at right behind pakoo with moveinleft
    show cs at left with moveinleft
    show arceus flipped at mid_left with moveinleft
    peppino "Hey Piezanos, whatcha want today?"
    pakoo "Hey Peppino, can you get me and my friends the Gustavo special today?"
    show peppino2 at t_pepzone2 behind peppinopizzafg
    hide peppino
    peppino "Sure-a thing-a! Coming right up!"
    show peppino at t_pepzone2 behind peppinopizzafg
    hide peppino2
    pakoo "Also, do you think my friends here can spend the night? They don't have anywhere to sleep tonight."
    peppino "The room in the back should be fine. Mr. Stick is out right now, so they can bunk there."
    pakoo "Alright, epic."
    n "Peppino serves the group their pizza."
    show cs happy
    cs "Damn, this is some good pizza!"
    show arceus happy flipped
    arceus "Probably some of the best pizza I've ever had."
    if fun_value(10):
        billy "Better than my restroom mini-burgers!"
    else:
        billy "Better than my restaurant mini-burgers!"
    show cs
    show arceus flipped
    pakoo "Alright, well, I should get going, but I hope y'all have a good time doing whatever y'all are doing."
    cs "Yep! Take care, Pakoo!"
    hide pakoo with moveoutleft
    scene black with fade
    stop music fadeout 3.0
    music end
    n "The gang heads to the backroom area to rest for the night."
    n "Once they wake up, they thank Peppino for his hospitality and head out."
    jump iowa

label iowa:
    scene car plains
    show billy car
    with fade 
    n "They get back in car and continue into Iowa."
    billy "Alright, well, ever since that cult encounter, it's been pretty smooth sailing!"
    billy "The rest of this trip shouldn't be too long!"
    n "As if on cue, a strange sound is heard from overhead."
    n "CS looks out the window."
    play music "<loop 0>speedy_comet.mp3" volume 0.5
    music Speedy Comet - Mahito Yokota
    cs "You have to be kidding me!"
    arceus "What's going on?"
    cs "HoH SiS is back!"
    arceus "{i}What?!{/i}"
    billy "Who?"
    cs "They have their UFO and--"
    n "A huge laser beam blasts along the left side of the road, ripping up everything in its path!"
    play sound "minigames/car/gaster_blast.wav"
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car
    arceus "Shit, this is bad..."
    cs "Billy, you need to switch lanes when it charges up!"
    minigame "minigame_car" "after_ufo" "lose_car_game"

label after_ufo:
    $ renpy.mark_label_seen("play_car_game")
    scene car plains
    show billy car
    stop music fadeout 3.0
    music end
    cs "Holy shit! We made it!"
    arceus "That was some good driving, Billy!"
    billy "{i}That's{/i} the power of the 6,000-pound car!"
    n "They continue driving through to the end of the Midwest."
    scene car plains night
    show billy car
    with fade
    n "As they are traveling through Illinois, they pass by Chicago."
    arceus "One day, I'm gonna rule that place."
    cs "What are you... talking about?"
    arceus "It's better than ruling the Earth." # DX: I feel like it'd be funny to wax poetic here about how great chicago is. Not super long, but enough to run the joke home. I love the idea of sleepy arc rambling on about chicago for a bit.
    # Who the fuck wrote that comment, and what the fuck does it mean? - Arc
    cs "Get some sleep, Arc."
    scene black with dissolve
    n "The gang stops in Indiana for the night. They take off again in the morning."
    jump michigan

label michigan:
    scene car plains
    show billy car
    with dissolve
    play music "<loop 0>track4.mp3" volume 0.4
    billy "Alright. The highway entrance should be right around here."
    billy "We can head to Ohio, and then we'll be getting really close."
    billy "Fuck."
    cs "What's wrong?"
    billy "The entrance is closed. We should stop and ask what's going on."
    billy "There's someone over by the gas station. We can ask him."
    scene black with dissolve
    n "Billy pulls into a nearby gas station and gets out to talk."
    scene gas_station_2
    show streetguy at mid_right
    with fade
    show billy at mid_left with moveinleft
    billy "Hey, man. Do you know what's up with the highway?"
    streetguy "Not sure on details, but I hear they found one of the horsemen of the apocalypse flying around."
    streetguy "Possibly in Michigan."
    billy "What?"
    streetguy "Like I said, I don't know details."
    billy "Well, do you know which roads are affected? We need to get to New York."
    streetguy "Last I saw, the route through Michigan should still be open."
    streetguy "That's how I found out about the horseman of the apocalypse."
    streetguy "Michigan having better roads than literally any other place is a sign of the end times."
    billy "Alright, thanks for the help. I'm gonna get going."
    hide billy with moveoutleft
    scene black with dissolve
    n "Billy gets back in the car to tell the others what the stranger had told him."
    scene gas_station_2
    show billy car
    with dissolve
    cs "Well. I guess if we have no other option, we may as well go through Michigan."
    arceus "Yeah, they have corn and at least two other things, so it's honestly probably better than going through Ohio."
    billy "Sounds like a plan. The drive is gonna take longer with the detour though, so we should definitely get going."
    scene car plains
    show billy car
    with dissolve    
    n "They get on the highway and start heading towards Michigan."
    arceus "We're making progress. Finally in Michigan."
    stop music fadeout 3.0
    billy "It looks like we're coming up to a place called Bronson. Maybe we could stop there for food."
    arceus "Nah, this place looks too rural to have much around."
    n "The two look over to CS, who seems visibly distressed."
    arceus "Uh, CS? How's it going?"
    cs "I... should be fine."
    cs "Something about the name Bronson, Michigan sends a chill down my spine."
    arceus "We'll just skip it. Nothing around here anyway."
    scene black with dissolve
    n "They keep driving. CS continues muttering \"Don't go to Bronson\" until they finally stop seeing Bronson signs." 
    scene car plains
    show billy car
    with dissolve  
    billy "Alright. We're way past Bronson, but we're getting pretty far north."
    billy "We should probably find an exit to start heading towards New York soon."
    cs "There's an exit coming up. We can take either I-69 or 94."
    billy "Alright. Which one do you think?"
    arceus "Well, 94 goes east which is the direction we want, but the other one is 69, so I'm down for either."
    billy "I guess it's up to you then, CS."
    menu:
        "Which road should we take?"
        "I-69":
            jump interstate_69
        "I-94":
            jump interstate_94

label interstate_69:
    window hide
    show screen warning("The following scene is a major tonal shift.\nIt may be disconcerting to some viewers.\nWarnings: creepy forests, haunting music, slow decents into madness", "pussy_out_i69")
    pause
    window show
    $ nome = True
    cs "We're on a detour anyway. May as well take the funny route."
    billy "Alright. 69 it is."
    arceus "I don't know if that's safe while driving, but we can do that once we stop somewhere, I suppose."
    billy "I think I'm fine. You and CS can do that now if you want though."
    cs "That'd be hard with the seatbelts on, so I'll wait. What if we got into a crash?"
    cs "Remember to always have safe sex, kids."
    arceus "Fair point."
    arceus "I've been seeing signs for East Lansing for a while. Maybe we should stop there."
    billy "Any spiritual discomfort about that one, CS?"
    cs "No, that sounds fine. It'd be good to get some food in us."
    billy "Lansing it is."
    scene black with dissolve
    n "They get off at the exit and start driving into East Lansing."
    scene traffic
    show cscar1arc
    show billy at left
    show cs flipped at right
    show cscar2
    with dissolve 
    play music "<loop 0>honk_song.mp3" volume 0.8
    cs "I was expecting there to be people around, but I wasn't expecting traffic like this. I wonder what's going on?"
    arceus "All the people walking are wearing green and white, so it's probably a sports thing."
    billy "We are in Lansing. They have one of the biggest football schools in the country."
    cs "Really? I've never heard of that before."
    billy "Figures. You don't strike me as the type to know about sports."
    cs "You would be correct."
    arceus "God, the people on the sidewalk are going so much faster than us. What is this?"
    billy "I guess you can only get so many cars through a small intersection."
    arceus "Well, if it's so many damn cars, we should be through by now."
    billy "That's not what that expression means... Whatever. We just have to wait it out."
    cs "Hey, do you guys see that little guy? Over behind that tree?"
    billy "Oh, did Arceus get out to pee?"
    arceus "You can literally see me in your rear-view mirror right now."
    billy "Only if I squint."
    arceus "I'm not {i}that{/i} small, man..." # Me with the goddamn ellipses again lmao - Aria
    cs "No, look, that short guy. The one with the red pointy hat."
    arceus "Oh, shit, you're right! That looks like a gnome!"
    cs "God, did Blank somehow track me to Michigan?"
    arceus "Blank is at least three gnomes tall, though. That couldn't just be him in a costume."
    cs "You're probably right, but I wouldn't be all that shocked if he learned practical effects for a gag."
    cs "Wait, is he coming this way?!"
    n "The gnome steps out from behind the tree and makes his way to the door of the unoccupied seat of the car, motioning a request to roll down the window."
    billy "Holy shit, you two weren't kidding. I think he's trying to talk to us."
    stop music fadeout 3.0
    billy "I'm gonna see what he wants."
    play sound "roll_window.ogg" volume 0.7
    pause 2.0 
    # DX: It could be funny to have an option to ignore the gnome for a while
    play music "<loop 0>wayward_wanderer.mp3" volume 0.7
    music Wayward Wanderer - Deep Gnome
    gnome "Hallo, may I enter your Automobile?" 
    billy "What do you want with us?"
    gnome "I mean you no harm. May I sit and explain myself?"
    arceus "I don't think this guy is a threat. We may as well let him in."
    cs "He'll at least make this traffic jam more entertaining."
    billy "Alright, fine, come on in."
    gnome "I thank you. As you may be aware, I am not of your Species."
    arceus "I don't think I'm the same species as these two."
    gnome "That may be true, however, it appears that neither of your Species are the same as mein." 
    gnome "Therefore mein Point still stands, und thus I still must briefly introduce mein Volk und our Relationship to this Place."
    gnome "I am of the Forest, und I have recently become acquainted mit some of your Kind."
    gnome "Deine Group has a similarly unique Redolence to those I encountered."
    gnome "As I am a Being of the Forest and of the Land surrounding it, I find myself in a Position to assist you."
    cs "Alright, this is a lot to take in, but at this point I'll do anything to get out of this car."
    cs "How can you help us?"
    gnome "My kind is not of this World, but rather of the Forest Dimension. I cannot clear this Path, but I can bring you to another."
    cs "Yeah, that may as well happen to us at this point."
    cs "Thanks for your help." 
    gnome "No need to thank me. It is mein Pleasure."
    n "Everyone feels an energy emanate from the gnome as they watch the environment around them transform from a modern university into a dense forest."
    scene gnome_forest
    show cscar1arc
    show billy at left
    show cs flipped at right
    show cscar2
    with dissolve
    n "The buildings disappear as more trees, bushes, and brush spring forth from the ground as if you were watching a timelapse of hundreds of years of nature."
    n "Eventually, the growth comes to a halt as any semblance of their old surroundings is buried in a lush and lively grove."
    n "They find themselves on a clear path through the trees as the sunlight shining through the canopy up ahead starkly contrasts the heavy darkness of the woods behind them."
    gnome "If you continue to drive, you will reach a Clearing with a large Sugar Maple surrounded by a Bed of Clovers."
    billy "Where will it take us once we return to our own world?" 
    gnome "We will simply return to the Edge of the Campus. You will be able to continue your Journey smoothly."
    scene forest_clearing
    show billy car
    with dissolve
    n "Billy takes the car forward and stops in front of the tree."
    n "As they pull into the clearing and stop the car, they again become aware of the gnome's presence."
    n "The gnome remains silent as the energy no longer seems to be radiating from him, but returning to him."
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    n "The forest, which had previously sprung forward as if growing naturally, fell rapidly before their eyes."
    scene white
    show billy car turn
    with dissolve
    n "A glowing white cut appears through the trees before the remaining trunks also decay into a mass of bright light."
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    n "The light begins to appear at the base of the bushes before the ground that housed their roots is tossed out, taking the bushes along with it."
    scene parking_lot
    show billy car turn
    stop music fadeout 3.0
    music end
    n "Finally, the forest's brush, along with the detritus of other plants that dotted the ecosystem, disappears in a sea of white flame that leaves them in a desolate parking lot."
    show billy car
    $ achievement_manager.unlock("You've Been Gnomed")
    billy "Well, that was deeply disconcerting."
    gnome "If you are not used to it, I suppose so."
    billy "I think I need a break from driving after all that."
    cs "Yeah, that's fine. I was getting hungry anyway."
    cs "Hey Mx. Gnome, do you know anywhere good to eat around here?"
    gnome "I don't often eat Human Food, however, I do know of one Restaurant because of my previous Human Encounter."
    cs "Cool! Can you take us there?"
    gnome "Of course. It is right around this Corner. Simply take a Right Turn. It's called East Cafe."
    billy "Oh, yeah, I see it. That really {i}is{/i} close!"
    cs "Definitely. I'm just excited to get in and eat."
    scene black with dissolve
    n "The gang gets out of the car and heads over to East Cafe."
    scene cafe_entrance
    show cs at left
    show arceus flipped at mid_left
    show billy at center
    show gnome at mid_left_left
    with fade
    show waitress at right with moveinright
    waitress "Welcome, welcome. Please wait, and I'll come seat you in a minute."
    hide waitress with moveoutright
    n "As everyone is waiting, the strange glowing grey blob in the corner notices the group and floats over."
    show aria at right with moveinright
    play music "<loop 0>mis_leader.mp3" volume 0.7
    music MisLeader - Triosk and Jan Jelinek
    aria "CS! Arc! What are you doing here?"
    gnome "Aria! I knew I recognized that Scent."
    aria "OMG, hi! So, you brought them here?"
    gnome "That I did. They were stuck in the Game Day Traffic."
    aria "Yeah, that'll happen."
    show cs disappointed
    cs "Wait, who are you?"
    aria "It's Aria. You know, AWK?"
    cs "Wait, what? I've met you before, and you definitely didn't look like this."
    show cs
    aria "I dunno, people change."
    aria "Speaking of surprising, is that Billy Mays with you?"
    billy "In the flesh."
    aria "Didn't you die of a heart attack or cocaine overdose or something?"
    billy "Cocaine-induced heart attack, yeah."
    billy "You're a formerly-human floating grey blob that hangs out with gnomes. I don't think I'm the weirdest thing here right now."
    aria "Fair enough. Do you all wanna eat with me?"
    cs "Sure. It's been a while."
    scene black with dissolve
    n "CS and the gang sit down with Aria."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    with fade
    show waitress at right with moveinright
    aria "Alright. {font=cjk}老板娘！他们会跟我一起坐。"
    waitress "{font=cjk}可以啊！"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right  
    billy "Oh, you speak Chinese?"
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "Yeah. I got tired of having to ask for chopsticks whenever I came here, and I figured if I spoke Chinese, they'd just assume that I'd want them."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    billy "Did that work?"
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "It did. Not sure that the return on investment made sense effort-wise, but it's a cool skill either way."
    aria "What did you all want to eat?"
    gnome "Frog Legs sound good."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus happy at right
    arceus "I've always wanted to try chicken feet. I'll get some of those."
    show arceus
    show cs happy
    cs "Pork fried rice, please."
    show cs
    billy "Ooh, jellyfish. I'll get that."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "{font=cjk}请给一碗鱼香茄子。请问一下，如果我说一点狗屁，你不会告诉他们，对吧？"
    waitress "{font=cjk}对，我不会。"
    aria "{font=cjk}好啊。谢谢。除非他们使用{/font}Google Translate, {font=cjk}他们完全听不懂。"
    aria "{font=cjk}我想让他们以为我的中文水平比我真的水平更好。"
    aria "{font=cjk}我的气垫船装满了鳝鱼。"
    waitress "Wow, your Chinese sounds like a native, but you're clearly utterly insane."
    aria "Wow, that phrasebook was really helpful."
    waitress "By the way, we don't have any pork to fry the rice right now."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus worried at right
    arceus "Wait, how?! That's by far the most popular thing we ordered..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "Pigs are expensive and they have a good union. We just hired a bunch of shrimp instead."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus angry at right
    arceus "I'm not playing along with that joke."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "It wasn't meant to be humorous, but, fair enough."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "I'll just get chicken fried rice."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "Alright, I'll be back in a bit."
    hide waitress with moveoutright
    n "Everyone starts a conversation as the waitress walks off."
    aria "So, CS, it's been a while since I saw you. How's it been?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "It's been... a hell of a lot."
    cs "Not horrible, but things could definitely have gone smoother."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Yeah, life is like that sometimes. Glad things have been largely okay, though."
    aria "How about you, Arc? It's weird seeing you in person. How's moving to the UK been? Have you been visiting the US for long?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus worried at right
    arceus "I'm not sure if that move is happening in this timeline..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Ah, yeah, that happens. I guess not every plan is meant to be."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    arceus "That wasn't what I meant by timeline, but it would be a lot to explain, so we'll go with that."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "So, Billy, what's your story? You don't have to go into it if you don't want, but I'm very curious."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    billy "Well, I died of a heart attack, got buried, came back from the dead, dug my way out of the grave, and tried to go back to normal."
    billy "People just assumed I was an imposter, and I couldn't get any pitchman gigs, so I became an Uber driver."
    billy "Then these guys showed up and I offered to drive them from Washington to New York."
    billy "I heard CS was a YouTuber, so I was just expecting some MrBeast-style video."
    billy "Now, I'm stuck hanging out with gnomes and floating blobs, and going through forest dimensions."
    pause 1.0
    billy "No offense."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    gnome "G'none taken."
    aria "A little bit taken, but I also brought up your cocaine overdose immediately after first meeting you, so fair play, honestly."
    aria "Y'all are headed to New York, then?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "Yeah, I'm just trying to get home, and these two kinda got dragged along."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Would you like to come rest at my apartment for a while? I have enough space for you all to get some sleep."
    aria "I also have a really pretty wooded area behind my apartment I can take you through."
    aria "You've all been through a lot. It'd be a good way to relax before you finish the drive."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    arceus "That'd be great. It'd be nice to get some proper rest."
    billy "I'd be happy to be off the road for a while longer. I think I might've had enough of forests for today, though..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    gnome "A Forest will do you good. They're good for your Health."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "Yeah, sure, we'll go over there after we eat."
    show waitress at mid_right with moveinright
    waitress "Here's everyone's food. Enjoy your meal!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "They all eat and then leave the restaurant. The gnome goes back to his forest, and the others head to Aria's apartment for a rest."
    scene aria_apartment_outside
    show billy car
    with dissolve
    aria "You can park here next to the building."
    billy "Alright. I know it's early, but I'm ready to just sleep."
    arceus "Yeah, that sounds good."
    aria "Sounds like a plan. I'll get you some sleeping bags, and blankets for whoever wants to sleep on the couch."
    scene black with dissolve
    n "Aria goes to her room as everyone rests. She hears them waking up late into the night and goes back out to check on them."
    scene aria_room
    show cs at left
    show billy at mid_left behind cs
    show arceus flipped at center
    with fade
    show aria at right
    with moveinright
    aria "Hey, everyone. How'd you sleep?"
    show cs happy
    cs "It was great. Thanks."
    show cs
    aria "So, when are you all planning to head out? I imagine you probably want to head out soon, but I would like to show you the woods."
    aria "I love the nature around here, so I spend a lot of time out there. Feels like a waste to not check it out while you're in the area."
    arceus "That does seem relaxing. May as well have a normal field trip instead of all these crazy adventures."
    cs "Yeah, sure."
    billy "Well, if everyone else is going, may as well check it out."
    scene black with dissolve
    n "They all walk through the parking lot until they come to the entrance to the forest."
    n "The woods are at a lower height, and the group walks down a path of cracked concrete, ducking under branches that hang over the path."
    n "The cover of the trees is still thin, but the shadows are starting to cover their limited moonlight."
    scene path_entrance
    show cs disappointed dark flipped at mid_right
    show arceus worried dark at right
    show billy dark at center
    show aria dark flipped at left
    with dissolve
    play music "<loop 0>dense_woods_b.mp3" volume 0.5
    music Dense Woods B - Kikiyama
    billy "Why does the window by the entrance have to be bright red?"
    billy "I've had enough of spooky forests today."
    aria "It's fine. That guy always has his lights set to red."
    aria "It's admittedly a little creepy, but you get used to it."
    cs "That's probably the least concerning thing we've seen in a forest so far today, to be fair."
    arceus "Still seems plenty murderous to me."
    aria "I'm out here most nights, and he hasn't murdered me yet, so I wouldn't worry too much."
    scene forest_bridge
    show cs dark flipped at mid_right
    show arceus dark at right
    show billy dark at left
    show aria dark flipped at center
    with dissolve
    aria "We're gonna take a left at the bridge up ahead. The forward path just spits us right out onto a normal street."
    billy "We've been out here for all of five minutes and that's already seeming like the better option..."
    aria "Nah, trust me. This path has all the best plants and the only real path through the forest."
    aria "White banesberry, hawthorn, sugar maple."
    aria "It's really pretty."
    show cs disappointed dark flipped behind arceus
    cs "What do you mean by \"the only real path\"? Aren't we currently walking through a forest?"
    aria "This isn't a forest, this is just a concrete path with trees on the sides."
    aria "Once you're actually in the woods, you're surrounded by plants of all kinds."
    aria "The smallest of them just springing up from the ground."
    aria "The tallest spreading their roots and taking command of the very earth we all draw our energy from."
    show arceus worried dark
    arceus "You're not helping this seem any more normal..."
    aria "What do you mean? It's perfectly natural."
    scene creepy_path
    show cs worried dark flipped at mid_right
    show arceus worried dark at right
    show billy dark at left
    show aria dark flipped at center
    with dissolve
    aria "Anyway, the forest path is right up there."
    billy "Are you kidding? This path is dark enough. That's not a path, that's a portal to the void."
    cs "Yeah, I don't know about that."
    aria "It's fine, it's my typical path."
    aria "We have flashlights, and honestly, the moonlight is usually enough for me once I get in there."
    billy "You're also an incomprehensible entity. We have a different scale."
    aria "I guess you're welcome to just head back out on the road."
    aria "Just watch out for fae paths on the way back."
    billy "What the hell is a fae path?"
    aria "Oh, they're paths that look like a normal path for the first little while, but end up placing you in the center of the woods."
    aria "The sense of linear direction decays as the path becomes less clear, and you eventually can't tell what direction you came from."
    billy "And you didn't think it was relevant to mention this before?"
    aria "Well, no, you have a guide. I was planning on making this a relaxing walk, so I didn't plan on taking the fae paths."
    billy "Why would you ever?!"
    aria "Well, they put you into some pretty parts of the woods."
    billy "Your obsession with these woods is not healthy."
    aria "How come? It gets me fresh air and exercise."
    show cs disappointed dark flipped behind arceus
    aria "Anyway, this path loops around to where we came from, so if you wanna leave, it's the fastest way back at this point."
    billy "So, no matter which way I take, I'm at risk of ending up in a cursed path to the middle of a haunted forest?"
    aria "I wouldn't say cursed or haunted, but I would advise staying with me."
    aria "Any unfamiliar woods comes with a chance of getting lost, and I imagine you all don't want that."
    billy "Why would anyone?!"
    aria "To each their own, I suppose."
    billy "What do you all think?"
    show cs dark flipped behind arceus
    cs "I've not had any reason to distrust Aria before, and having someone who knows the woods has to be good."
    show arceus dark
    arceus "Yeah, these woods are gonna be creepy no matter what route we take. We may as well pick the fastest one."
    aria "Alrighty then, follow me everyone."
    scene creepy_path_2 with dissolve
    n "As the group enters the path, a ray of moonlight shines through a gap in the canopy."
    n "Rustling noises can be heard further into the woods, but the path through the trees is clear, albeit dimly lit."
    stop music fadeout 3.0
    music end
    scene creepy_path_4 with dissolve
    play music "melancholy.mp3"
    music Melancholy - Imori
    aria "If you look to the right, you'll see one of my favorite paths in the woods."
    aria "It's not exactly clear, so we'll skip it today, but it leads to a pretty little grotto."
    aria "It feels like something out of a fairy tale."
    cs "This whole forest does, but only the uncensored Brothers Grimm versions."
    aria "Yeah, it really feels like an authentic fairy tale experience c:"
    cs "That's not a good thing..."
    scene doll_eye_tree
    n "Aria stopped listening because it's distracted by a tree up ahead."
    if fun_value(10): 
        aria "Here's one of the white baneberries that I was talking about. They're also known as {i}Actaea Pakoopoda,{/i} or Doll's Eyes."
    else:
        aria "Here's one of the white baneberries that I was talking about. They're also known as {i}Actaea Pachypoda,{/i} or Doll's Eyes."
    arceus "I can see where they got the name!"
    aria "It does have thick stalks that fit the pachypoda name."
    arceus "Not the altiora poke-and-prod-er or whatever, the fucking doll's eyes!"
    arceus "That tree is watching us."
    aria "I like to think that Mother Nature watches us through all the trees."
    arceus "This isn't the time for metaphors! It has eyes that blink!"
    aria "Well, of course, they'd water too much if they didn't."
    arceus "Oh for f--{w=0.5} whatever, just get us out of here!"
    aria "No need to worry, we're on the way."
    arceus "As long as we're on the fastest path out of here, I'm happy."
    cs "Aria, how exactly do you find this relaxing?!"
    aria "I simply appreciate the beauty of the world around me."
    billy "I think that's fair. That {i}is{/i} a very pretty tree."
    aria "Thank you! See? {i}Someone{/i} gets it!"
    cs "Oh no, I think the woods are getting to him. He's getting some kind of environmental Stockholm syndrome." 
    cs "We've gotta get out of here, quick, before he gets worse."
    billy "I wouldn't be too worried about it."
    billy "I'm also terrified right now, but there's a certain macabre beauty that cuts through it..."
    arceus "Weren't you already scared going into this?"
    arceus "Like, before there were any clear signs of this weirdness?"
    arceus "There's no way that shift is natural."
    billy "There's nothing wrong with feeling the irresistible pull of nature."
    cs "Okay, that's definitely concerning."
    cs "Let's pick up the pace."
    aria "We're already going on the fastest path. I wouldn't deviate from the plan."
    scene creepy_path_fairy with dissolve
    cs "I didn't mean to change paths, I just meant to go down it faster--{w=0.5} wait, what's that glowing thing up ahead?"
    aria "Oh, that's strange, They don't normally appear on this path..."
    aria "That's one of the Faeries."
    aria "I've seen one like that before, with the glowing white body and warm yellow-colored edges."
    aria "I haven't seen that many Faeries, but I've kept track as I encounter new varieties."
    aria "I call this kind Seraphites."
    aria "They have particularly warm energy and have a brighter glow, as well as higher pitched resonance."
    cs "Resonance?"
    aria "The tone They produce as They float around."
    aria "It's similar to a CRT whine, so it might be too high-pitched for you to be able to hear it."
    arceus "I can hear CRTs, but I don't hear that..."
    billy "What are you talking about? That's so loud, how can you not hear it?"
    cs "Wait, Billy and Aria are the only two that can hear it?!"
    cs "The Fae must have something to do with the weird forest obsession."
    cs "We need to get Billy out of here, ASAP."
    arceus "We can't go forward with it up ahead!"
    aria "You can just walk past It. Faeries are mischievous, but They aren't malevolent."
    arceus "Maybe not to {i}you!{/i} You're also a glowing blob!"
    aria "I wasn't always, and They left me alone then, too."
    cs "I don't know if I want to try and go back if we've encountered the Fae that make the trick paths..."
    cs "I guess we don't have any other options."
    show creepy_path_3 with dissolve
    n "They all slip past the Seraphite, and It floats off between the trees."
    n "They walk further along the path, which becomes less clear as tree branches block their way."
    aria "Huh, these aren't normally here..."
    arceus "What do you mean \"not normally here\"?! Is this path changing?!"
    cs "What the hell? How are we getting out of here?!"
    billy "I guess we've gotta just go through."
    arceus "Go through where?! These branches are about as thick as the trees on the side!"
    billy "We go down the same way we've been going."
    billy "What's your issue? You're short enough that you don't even need to crouch to get under the branches."
    arceus "Fuck off."
    arceus "I guess you're right, though. We can't really turn back now."
    n "Everyone begins making their way through the nest of tree branches."
    n "Eventually, they reach the end and the canopy begins to thin out as they reach a path next to a road."
    show creepy_path_exit
    aria "Alright, here's the path back."
    arceus "Are you sure?! Can you guarantee me that this path is the same way it's supposed to be?!"
    aria "Yeah, that path is the same as it always is."
    billy "That path goes back the same way we came, of course it's fine."
    arceus "That was what she said about the last path and then we ended up climbing between a tangled web of branches."
    show billy at left
    show cs worried
    show arceus worried at mid_left
    show aria dark at right
    with dissolve
    arceus "That's a normal road with a sidewalk over there. We're taking that."
    cs "I'm with Arceus on this one."
    cs "I don't think I'll be able to go between two rows of trees without having a panic attack for a while."
    aria "I think Michigan roads are scarier than any forest, but I'll take you back on whichever path you want."
    $ achievement_manager.unlock("Analog Horror Protagonist")
    n "They all walk down and reach the apartment, then make their way to where the car is parked."
    scene aria_apartment_outside
    show billy at left
    show cs
    show arceus flipped at mid_left
    show aria at right
    with dissolve
    stop music fadeout 3.0
    music end
    aria "Thanks for hanging out with me. It was fun."
    aria "Sorry you two didn't enjoy the woods, but I'm glad at least Billy seemed to like it."
    cs "I guess nothing was actively dangerous, and that's above average for us at this point."
    cs "Thanks for letting us rest at your place."
    aria "Anytime."
    aria "Billy, it was nice meeting you. You're welcome to come back and visit the woods again."
    billy "It was nice meeting you too. I'll definitely come back next time I'm in Michigan."
    aria "CS, it was also nice seeing you again." 
    aria "And, Arceus, it was nice finally meeting you in person."
    arceus "You, as well, until we went to the woods."
    aria "Yeah, sorry about that..."
    billy "You're fine. It was nice then, too. He's just got a bit of a skill issue, I think."
    arceus "Whatever, man..."
    aria "Bye-bye, y'all! Good luck on your adventure!"
    scene black with dissolve
    jump ohio

label interstate_94:
    $ clown = True
    cs "What are you talking about? We're getting on 94."
    cs "We've all been through way too much for me to want to take any unnecessary detours."
    cs "I'm so tired. I just want to get home..."
    cs "I've made some pretty dumb jokes in my life, but I'm not wasting another second."
    cs "Especially not for a God damn 69 joke."
    billy "Fine, we'll take 94! All we needed was that first sentence."
    cs "Sorry, guys. I guess I'm just on-edge right now."
    arceus "{i}I{/i} thought it sounded like a good route..."
    scene black with dissolve
    n "The conversation comes to a halt as they continue heading down the highway."
    scene car plains
    show billy car
    with fade
    billy "Looks like there's a traffic jam up ahead. I'm gonna get off and take a detour."
    arceus "I'm gonna roll a window down now that we're off the noisy highway."
    play sound "roll_window.ogg" volume 0.7
    pause 1.0 
    arceus "It's crazy hot in here right now."
    cs "Huh, I didn't notice."
    arceus "I am literally always wearing a fur coat, so I guess we have different scales."
    cs "Yeah, that'll do it. You're also wearing a hoodie. You could take that off."
    arceus "If you wanna see me naked, you can just ask..."
    cs "I didn't mean-- {w=0.5}whatever..."
    show billy car turn with vpunch
    play sound "audio/splash.mp3"
    show billy car turn with hpunch
    n "Soon after Arceus rolled down the window, they drive over a large flooded pothole."
    n "Water splashes up from the puddle through the car window."
    show billy car
    arceus "Oh no! My hoodie's a mess now!"
    cs "It was actively making you too hot, so now it shouldn't be a big deal, right?"
    arceus "The {i}sun{/i} was making me too hot. The hoodie was just making me too comfy!"
    arceus "We're already on a detour. We can just stop at the next laundromat we see and wash it."
    pause 5.0
    n "They continue down the road until Arceus spots a laundromat."
    scene mario_outside
    show billy car
    with dissolve
    arceus "Alright, there's one! Mario's Coin Laundry!"
    arceus "Billy! Pull over!"
    billy "Sure, I guess. I don't know if I'll be around much longer if I say no..."
    scene black with dissolve
    n "Billy parks the car and they all go inside."
    scene mario_inside
    show mario at right
    with dissolve
    play music "<loop 0>trash_zone.mp3" volume 0.3  
    music Tubular Trash Zone - Mr. Sauceman
    show cs at left
    show arceus dirty flipped at mid_left
    with moveinleft
    mario "Hey, paisanos! Welcome to my laundromat!"
    show arceus dirty worried flipped
    arceus "Wait, Mario? Why are you here?"
    mario "Why are you surprised? My name's on the sign and my picture's in the window."
    show arceus dirty flipped
    arceus "Yeah, but I assumed it was just a bootleg."
    show arceus dirty worried flipped
    arceus "Aren't you meant to be saving princesses or plumbing or driving go-karts or competing in the Olympics or... whatever {i}else{/i} it is that you do?"
    arceus "When did you have time to open a laundromat?"
    mario "All that stuff doesn't pay the bills."
    arceus "I'm pretty sure being a plumber is a decent career."
    arceus "And do you how much an Olympic swimmer can make just on endorsements alone? It's nuts!"
    arceus "Also, don't you get royalties from Nintendo or something?"
    show arceus dirty flipped
    mario "Miyamoto's my creator, so he gets to choose how the royalties are dispersed."
    mario "It's like a trust fund."
    mario "He spent all my royalties on his moped, so now I'm stuck running this laundromat."
    cs "Sorry to hear that."
    arceus "Yeah, that sucks a lot."
    mario "It is what is it."
    n "Suddenly, they all hear a metal banging sound and one of the customers walks over."
    show smiley at center with moveinright
    smiley "I was just waiting on my laundry and the machine made a loud clang and stopped spinning."
    mario "Alright, I'll be right over there."
    show mario flipped with determination
    hide mario with moveoutright
    pause 1.0
    mario "No shoes in the machine! If it's broken, you're paying for the replacement!"
    n "Mario takes out the shoes and tries running the machine, but it doesn't turn back on."
    show mario at right with moveinright
    mario "There are {i}three{/i} signs that say not to put shoes in the machine, and you decide to put these big-ass clown shoes in there?!"
    mario "You really {i}are{/i} a damn clown. I'll tell you that for free."
    smiley "The shoes were dirty, and I have a show to get to."
    smiley "Speaking of, I've still gotta head over there."
    smiley "See ya!"
    hide smiley with moveoutleft
    n "Smiley runs out of the building and gets into his car."
    play sound "audio/gamer_and_girl.mp3" volume 0.4
    n "A loud \"awoooooga!\" horn is heard as a colorful little clown car drives past."
    mario "Bastard. I really didn't need this today..."
    mario "Whatever, what do y'all need?"
    arceus "I just need to wash my hoodie before we get back on the road."
    mario "Alright. Detergent is over in the corner."
    n "Arceus and the others go to the back corner and wait for the hoodie to get clean."    
    n "Mario goes back to quietly sobbing in the back room."
    show mario flipped with determination
    hide mario with moveoutright
    hide cs
    hide arceus
    with moveoutright
    scene mario_inside2 with dissolve
    show cs at left
    show arceus dirty flipped at mid_left
    with moveinleft
    n "A gray blob enters the laundromat."
    show aria flipped at center with moveinleft
    show aria with determination
    aria "Wait, CS? Arceus?"
    show cs worried
    cs "Huh, who are you? {i}What{/i} are you?"
    aria "Oh, right! Yeah, it makes sense that you wouldn't recognize me. I'm Aria! Remember, AWK?"
    cs "{i}You're{/i} Aria? What happened to you?"
    aria "I got different."
    show cs
    arceus "I imagine we're not getting more details than that."
    aria "Not in this game."
    arceus "Fair."
    aria "What are you guys doing here?"
    show cs disappointed
    cs "We're, uh, kinda on a road trip?"
    show arceus dirty worried flipped
    arceus "From the law."
    cs "Yeah."
    aria "That checks out."
    show cs
    arceus "Wait, what are you doing here? You clearly don't wear clothes."
    aria "You don't know what I do in my free time."
    show aria flipped
    hide aria with moveoutright
    show arceus dirty flipped
    arceus "I suppose not."
    n "Arceus goes to transfer his hoodie."
    hide arceus with moveoutright
    n "Just as Arceus moves the hoodie into the dryer, two more clowns walk in."
    scene mario_inside
    show mario at right
    with dissolve
    show shaggy_too_dope at left
    show violent_jay at mid_left
    with moveinleft
    violent_jay "We're here to see Mario."
    mario "Hey, paisanos, what can I--" 
    pause 0.5
    mario "Oh God, more clowns. This is {i}not{/i} what I needed today."
    shaggy_too_dope "We're not just any clowns, we're Juggalos."
    shaggy_too_dope "And you don't need to worry about us. We're not like Smiley."
    mario "How did you two hear about that? How do you how his name?"
    violent_jay "All clowns are connected."
    violent_jay "We might be Juggalos, but we are still clowns."
    mario "What is it you want with me?"
    shaggy_too_dope "We want to replace that washing machine."
    violent_jay "We can't let that guy give clowns a bad name."
    violent_jay "Also, we heard about your situation with Miyamoto and all. That's messed up."
    mario "Wahoo! Thank you, I don't know what to say."
    shaggy_too_dope "Don't mention it."
    mario "Wait, how do you know about the Miyamoto thing? I didn't tell Smiley about that."
    violent_jay "Clown connection again. I could detect two clowns in here."
    mario "Smiley was the only one."
    violent_jay "There were definitely two. The other is still here."
    n "They walk towards the back where CS and Arceus are, and Violent Jay points at CS."
    hide violent_jay
    hide shaggy_too_dope
    with moveoutright
    scene mario_inside2
    show cs at left
    with dissolve
    show shaggy_too_dope at mid_right
    show violent_jay at center
    with moveinright
    violent_jay "There he is!"
    cs "Who, me? Wait, are you guys Insane Clown Posse?! What do you want with me?"
    violent_jay "Chill, man. You're just the other clown we detected here."
    show cs worried
    cs "I'm not a clown..."
    shaggy_too_dope "Can't argue with the clown sense. Definitely a clown."
    violent_jay "Why is everybody so worried whenever they see us today?"
    show cs
    cs "You {i}do{/i} call yourself Violent Jay. I'd imagine you're used to it by now."
    violent_jay "That's fair."
    show mario at right with moveinright
    violent_jay "Anyway, here's the check for the washer. We've gotta head out."
    hide violent_jay
    hide shaggy_too_dope
    with moveoutleft
    $ achievement_manager.unlock("Creepy Clown Sightings")
    show billy at mid_mid_left with moveinleft
    billy "What happened there?"
    mario "I'm not sure, but they paid for the washer, so I'm not gonna think about it too hard."
    show cs disappointed
    cs "I'm not a clown. Clowns have to be good at makeup..."
    mario "I wouldn't worry about it."
    show arceus at mid_left with moveinright
    stop music fadeout 3.0
    music end
    arceus "Yeah, my hoodie's dry, so we're ready to head out. Here's the money, Mario. Good luck with business."
    show cs flipped with determination
    hide cs
    hide arceus
    hide billy
    with moveoutleft
    n "CS, Billy, and Arceus all walk out."
    mario "That was really nice. I guess you {i}can{/i} have shit in Detroit after all."
    scene black with dissolve
    jump ohio
    
label ohio:
    if fun_value(50):
        scene car plains
        show billy car
        with fade
        n "After that fiasco, they continue their trip, soon passing through Ohio."
        show scott_border
        play music "<loop 0>breakout.mp3" volume 0.3  
        music Breakout - Shoichiro Sakamoto 
        n "Suddenly, a huge blue border enters everyone's vision."
        scott "Oh, what in the world? There is some red border in my eyes..."
        scott "I have a blue one. What is going on?"
        scott "Yeah, it's blue for me too. I think you're colorblind."
        scott "I {i}am{/i} colorblind. Oh, fuck."
        scene wozniaktroubles
        show billy car
        show scott_border
        with fade
        n "As they are driving through the state, they see some men on the side of road protesting the blue border."
        play sound "roll_window.ogg" volume 0.7
        scott "Hey all, Scott here!"
        scott "Are you tired of having a blue border in your vision?"
        scott "You should try Kaboom!"
        n "Scott pulls out a bottle of Kaboom and sprays them in the face."
        scott "Ahhhhh!"
        scott "It gets the tough stains out!"
        scott "I'm sorry, that doesn't seem very vegan. I'll have to just deal with it."
        scott "Scott, I don't think that'll work. Let's just keep going."
        scene car plains
        show billy car
        show scott_border
        with fade
        n "Once they leave the state, the border goes away."
        stop music fadeout 3.0
        music end
        hide scott_border with dissolve
        arceus "I'm glad it just faded away. I did {i}not{/i} want to spray cleaner in my eyes."
    else:
        scene car plains
        show billy car
        with fade
        n "After that fiasco, they continue their trip, soon passing through Ohio."
        show scott_border
        play music "<loop 0>breakout.mp3" volume 0.3  
        music Breakout - Shoichiro Sakamoto 
        n "Suddenly, a huge blue border enters everyone's vision."
        arceus "Oh, what in the world? There is some red border in my eyes..."
        cs "I have a blue one. What is going on?"
        billy "Yeah, it's blue for me too. I think you're colorblind."
        arceus "I {i}am{/i} colorblind. Oh, fuck."
        scene wozniaktroubles
        show billy car
        show scott_border
        with fade
        n "As they are driving through the state, they see some men on the side of road protesting the blue border."
        play sound "roll_window.ogg" volume 0.7
        billy "Hi, it's Billy!"
        billy "Are you tired of having a blue border in your vision?"
        billy "You should try Kaboom!"
        n "Billy pulls out a bottle of Kaboom and sprays them in the face."
        scott "Ahhhhh!"
        billy "It gets the tough stains out!"
        terry "I'm sorry, that doesn't seem very vegan. I'll have to just deal with it."
        cs "Billy, I don't think that'll work. Let's just keep going."
        scene car plains
        show billy car
        show scott_border
        with fade
        n "Once they leave the state, the border goes away."
        stop music fadeout 3.0
        music end
        hide scott_border with dissolve
        arceus "I'm glad it just faded away. I did {i}not{/i} want to spray cleaner in my eyes."
    jump pennsylvania

label pennsylvania:
    n "The gang hits the last state before New York, Pennsylvania."
    scene billboard
    play music "<loop 0>fourside.mp3" volume 0.6
    music The Metropolis of Fourside - Keiichi Suzuki
    n "CS sees a billboard pass by them."
    cs "Oh my God! It's PencilCon! We need to go!"
    arceus "Why the fuck do you want to go to {i}PencilCon{/i} when we are so close to home?!"
    cs "Because I love sharpening pencils! I made my own holiday around it! Please, Billy, can we go to PencilCon?"
    billy "If Arceus is okay with it, sure, I guess."
    cs "C'mon, Arceus!"
    arceus "Ugh..."
    cs "Please?"
    pause 3.0
    arceus "Fine, sure, whatever."
    cs "Woohoo! Let's go!"
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
    billy "Do people really like pencils {i}that{/i} much? Maybe I should've pitched more pencil products."
    scene cc_entrance with dissolve
    show pencilguy at center with moveinleft
    n "A man dressed as a pencil approaches the gang."
    pencil "Welcome to PencilCon! Want a free pencil?"
    show arceus at right with moveinright
    arceus "Uh, sure?"
    pencil "Here you go!"
    n "The pencil-clad man passes out a free pencil to each of them."
    pencil "Enjoy your stay!"
    show arceus flipped
    hide arceus flipped with moveoutright
    pencil "Oh, and, yeah! The 84th annual Pencil Sharpening Competition signups close in just a little bit, if you wanted to sign up!"
    hide pencilguy
    show cs at center
    n "The pencil man looks at CS."
    hide cs
    show pencilguy at center
    pencil "You look like the kinda guy who could win a competition like that. And boy howdy Dixon, do we need it! The current champion hasn't been bested in five years!"
    hide pencilguy with moveoutright
    n "The pencil walks away."
    show cs at center
    cs "A pencil sharpening competition?"
    n "Visions of an old video appear in CS's head."
    cs "I could totally {i}crush{/i} that! I've {i}gotta{/i} sign up!"
    show arceus angry at right with moveinright
    arceus "CS, come on, man. I wanna get to your house so I can--"
    hide cs with moveoutright
    n "CS walks towards the convention before Arceus can finish speaking."
    show billy at left with moveinleft
    billy "Listen, let the guy have fun. You two have been through a lot, right?"
    show arceus worried
    arceus "I suppose, I just..."
    n "Arceus thinks for a moment."
    arceus "Fuck, I {i}have{/i} been kind of a jerk during this whole road trip. Maybe I do need to let go."
    show arceus
    billy "That's the spirit! Now, go cheer on your friend!"
    show arceus happy
    arceus "I will! Thanks, Billy!"
    billy "Anytime!"
    show arceus happy flipped with determination
    hide arceus with moveoutright
    n "Arceus runs off after CS."
    billy "Now, {i}that's{/i} the power of good advice!"
    scene cc_lobby
    show cashier at center
    show cs at left
    with dissolve
    show arceus at right with moveinright
    n "Arceus catches up with CS at the sign-up table."
    signup "...and you said your last name is... 188?"
    cs "Yeah, this confuses everyone."
    cs "Oh, hey, Arc! Whatcha doing?"
    show arceus happy
    arceus "Just came to support my friend."
    cs "Aww, thanks, man."
    show arceus
    signup "Okay, that's you all registered. Fuzzy guy, you signing up too?"
    arceus "Nah, I feel like that would be basically cheating."
    cs "Okay, well, I have to go to the backstage and get set up. See you soon, Arc!"
    stop music fadeout 3.0
    music end
    scene cc_backstage with dissolve
    show cs at left with moveinleft
    n "CS walks to the backstage to prepare to compete when he notices a familiar face."
    show digi at right with moveinright
    play music "<loop 0>pokey.mp3" volume 0.6
    music Pokeys House - Keiichi Suzuki
    cs "Wait, Digi?!"
    digi "CS?!"
    cs "What are you doing here?"
    digi "I {i}always{/i} compete in the Pencil Sharpening Competition! I was inspired after that video of yours."
    cs "Oh, wow, really? Thank you, I guess!"
    cs "Do you think we'll be up against each other?"
    digi "I mean, probably. I'm the champ."
    cs "You?!"
    digi "Five years running."
    cs "Oh, jeez, I guess we {i}will{/i} be against each other, if I make it that far."
    digi "Well, good luck to you!"
    cs "You as well!"
    stop music fadeout 3.0
    music end
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
    play music "<loop 0>showtime.mp3" volume 0.4
    host "EVERYONE GIVE A BIG HAND TO OUR WONDERFUL CONTESTANTS!"
    play sound "audio/cheer1.mp3"
    show crowd at t_stagescreen onlayer broadcast
    n "The crowd explodes into uproarious applause."
    hide crowd onlayer broadcast
    host "ON \"GO\", THESE LOVELIES WILL BE COMPETING TO SEE WHO CAN {color=#ffff00}SHARPEN THE MOST PENCILS!"
    host "THIS TRULY IS THE BATTLE OF A CENTURY, FOLKS! DIGIDUNCAN, OUR LONG-TIME CHAMP, WILL BE GOING UP AGAINST A NEWCOMER, THE AMAZING CS188!"
    play sound "audio/cheer2.mp3"
    show crowd at t_stagescreen onlayer broadcast
    n "The crowd is going wild."
    hide crowd onlayer broadcast
    host "ALL THEY HAVE TO DO IS {color=#ffff00}SHARPEN THE PENCILS AS QUICKLY AS POSSIBLE,{/color} WITHOUT {color=#ffff00}GETTING THE ERASER STUCK!"
    host "IT'S A TRULY MAGICAL EVENT, AND YOU'RE ALL ABOUT TO WITNESS IT! ARE YOU ALL READY?"
    play sound2 "audio/cheer1.mp3" noloop volume 0.5
    play sound "audio/cheer2.mp3" noloop volume 0.5
    show crowd at t_stagescreen onlayer broadcast
    n "The crowd is going absolutely crazy."
    hide crowd onlayer broadcast
    host "AND WITH THAT, LET'S BEGIN! READY?"
    stop music fadeout 3.0
    n "CS glances over at Digi and they nod at each other."
    host "3..."
    if fun_value(50):
        n "Digi looks to be smacking his arm."
        $ archack = True
    else:
        n "A whirr is heard as Digi's arm motors charge up."
        $ archack = False
    host "2..."
    n "CS concentrates, his hands ready to sharpen like his life depends on it."
    host "1..."
    n "Both competitors hover their hands over the pencils..."
    host "GO!"
    music Rude Buster - Toby Fox
    minigame "minigame_pencil" "win_pencil" "lose_pencil_game"

label win_pencil:
    $ renpy.mark_label_seen("play_pencil_game")
    hide bad_end_screen
    hide typewriter
    show stage_screen as stage_screen_l at t_stage_screen_l
    show con_screen at t_stage_screen_c
    show stage_screen as stage_screen_r at t_stage_screen_r
    show cc_stage
    show mettaton at t_stagescreen onlayer broadcast 
    host "HOLY TICONDEROGA! WE HAVE A WINNER!"
    show crowd at t_stagescreen onlayer broadcast
    play sound "audio/cheer2.mp3" noloop volume 0.6
    play sound2 "audio/cheer1.mp3" noloop volume 0.6
    n "As if they couldn't get any louder, the crowd is going insane."
    hide crowd onlayer broadcast
    play music "<loop 0>showtime.mp3" volume 0.4
    host "THE CHAMP HAS FALLEN! LADIES AND GENTS, WHAT AN UPSET!"
    n "CS turns to Digi."
    hide mettaton onlayer broadcast
    show cs happy at t_stagescreen onlayer broadcast
    cs "Good game!"
    hide cs onlayer broadcast
    show digi at t_stagescreen onlayer broadcast
    digi "Same to you, man, that was wild!"
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
    show arceus happy at t_stagescreen onlayer broadcast with moveinright
    n "Arceus runs on stage."
    arceus "Holy shit, CS, you did it! That was amazing!"
    hide arceus onlayer broadcast
    show cs happy at t_stagescreen onlayer broadcast
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
    stop music fadeout 3.0
    hide cs
    scene cc_crowd with dissolve
    play music "<loop 0>fourside.mp3" volume 0.6
    cs "Well, that was a lot of excitement for one day. Let's head home."
    n "Despite working harder to support CS, Arceus can't help but look relieved to get back on track."
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
    if archack:
        digi "Well, my arm got hacked, or something, so, I lost."
        show arceus worried
        arceus "Heh..."
        show arceus
    else:
        digi "Usually, they'd pay for my train home, but I, uh, lost."
    cs "Ooh, right."
    cs "Billy, we got room for one more?"
    n "Billy looks at Digi."
    billy "He and Arc are both pretty small. I think they'll fit in the back just fine."
    show arceus angry at right with moveinright
    arceus "Hey!"
    digi "Thanks!"
    show arceus angry flipped
    hide arceus with moveoutright
    cs "Well, Digi, you've got a ride!"
    digi "Thanks so much, man!"
    stop music fadeout 3.0
    jump car_dialogue

label back_home:
    stop music2
    scene cs_house with fade
    play music "<loop 0>park_theme.mp3" volume 0.5
    music Park Theme - Lorin Nelson
    n "After the long and treacherous journey, CS finally arrives at his house."
    show arceus flipped at left with moveinleft
    arceus "We made it back to your house, CS!"
    show cs flipped at center with moveinright
    cs "Finally, I'm home..."
    cs "Arceus, thank you so much for everything on this trip. I couldn't have done it without you."
    arceus "Aww, it was nice helping ya here."
    cs "You too, Billy."
    show billy at mid_left behind arceus with moveinleft
    billy "No problem!"
    cs "Well, I guess I should get some rest."
    cs "If you guys want, we can have a party at my place tomorrow to celebrate getting through all this shit!"
    show arceus happy flipped
    "Arc and Billy" "Hell yeah!"
    show arceus at left with determination
    hide billy with moveoutleft
    hide arceus with moveoutleft
    n "As CS says goodbye to his friends, a familiar but upsetting voice can be heard at the front of CS' house."
    stop music fadeout 1.0
    music end
    ed "{i}You!"
    show cs disappointed at left with moveinleft
    n "CS and the gang look towards CS' front porch, where Richard and Ed are waiting angrily for him."
    play music2 "<loop 0>hohsisremix.mp3" volume 0.5
    music "Alfred's Theme - Eminem"
    show ed at right
    show rich at mid_mid_right behind ed
    with moveinright
    ed "I have been waiting for you for quite some time now."
    rich "We've been trying to stop you for a while now, but this is the final stop for you."
    cs "HoH SiS?? What do you guys still want from me?"
    ed "What do you think, CS? After you put Wesley in the hospital? After you crippled most of our workers?"
    cs "Well, you guys scammed me out of my money and broke my computer! Of {i}course{/i} I wanted some kind of revenge!"
    ed "Why do you think this all started?"
    cs "I-{w=0.5} I don't know, because you're evil?"
    ed "CS, you made a laughingstock of our company long ago."
    ed "When you made that parody video of us that you call a \"YTP\", people wouldn't stop harrassing us about it."
    rich "You tried to humiliate us with your videos. You made others think we were a joke!"
    ed "You see, my ancestors came from the planet JoJ many years ago to start a foundation company."
    ed "It was the best damn foundation company in the world."
    ed "We repaired more than 50 percent of all foundations on the planet, and now... {i}you.{/i}"
    ed "You. You embarrassed us with those silly, stupid videos that dragged our family company through the mud."
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
    cs "I never intended to harm your company. I just thought that the video was a good source to YTP."
    cs "I'm sorry about all those prank callers. I even made a video telling people to stop prank calling you."
    cs "I never had bad intentions for you guys... honestly, it was also kind of like a free promotion."
    ed "Well, I'm sorry, CS, but it's too late."
    ed "Richard, get the JoJ UFO and vaporize the house."
    stop music2 fadeout 1.0
    show anno at offscreenleft
    play music "<loop 0>track3.mp3" volume 0.4
    music Track 3 - Weatherscan
    unknown "Wait!!!"
    n "A voice can be heard behind the group running up to them."
    cs "Anno?"
    show anno at center behind doug with moveinleft
    anno "You guys can't just destroy CS' house!"
    ed "Why not?"
    anno "I don't know, because..."
    anno "CS wasn't trying to harm you!"
    show arceus flipped at mid_left_left with moveinleft
    arceus "Yeah, CS' videos are hilarious, and honestly, if I knew you guys before this, I would've called you up for help on my house."
    arceus "If, y'know, I didn't go after that one politician."
    ed "Well, okay, but--"
    n "Even more of CS' friends show up at the scene."
    show cs at left
    show linus at mid_left behind phil with moveinleft
    linus "Yeah, I loved those videos about HoH SiS, and we'd love for you to come and fix up some of the damages at the LTT offices."
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
    doug "I don't know what I'm doing here, but yeah, good job, guys!"
    show cashier at mid_mid_right behind cs with moveinleft
    cashier "Yeah! Go CS!"
    show pakoo happy at center with moveinleft
    pakoo "Yeah! Get 'em, CS!"
    show peppino at mid_left behind cs with moveinleft
    peppino "It's pizza time!"
    show digi at mid_mid_left behind cs with moveinleft
    digi "I believe in you, CS!"
    show mettaton at mid_left_left behind cs with moveinleft
    host "YOU ARE A PENCIL SHARPENING GOD!"
    show aria at mid_left behind cs with moveinleft
    aria "You're a pretty cool guy, CS."
    if nome:
        show gnome at mid_left_left with moveinleft
        gnome "Follow ze path of de forest!"
    elif clown:
        show mario flipped at mid_left_left with moveinleft
        mario "Wahoo!"
        show shaggy_too_dope at mid_left_left with moveinleft
        show violent_jay at mid_left with moveinleft
        violent_jay "Our clown sense sensed you were in danger!"
        shaggy_too_dope "Don't mess with CS! He's one of us!"
    show scott at center with moveinleft
    show scott_border with dissolve
    scott "Hey all, Scott here! I love CS and his content!"
    show pencilguy at mid_mid_left with moveinleft
    pencil "I knew you were a cool dude!"
    show border_guard at mid_mid_left behind cs with moveinleft
    border_guard "I'm important too, eh!"
    if jade or fun_value(10):
        show bubble at center behind border_guard with moveinbottom
        show bubble with vpunch
        $ persistent.seen.add("bubble")
    cs "Wow, I don't know how you all got here coincidentally, but I appreciate it!"
    show cs at left
    rich "Oh my God, that's so many people!"
    ed "Okay, okay, I get it."
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
    hide pakoo
    hide peppino
    hide digi
    hide mettaton
    hide aria
    hide scott
    hide pencilguy
    hide gnome
    hide bubble
    hide violent_jay
    hide shaggy_too_dope
    hide mario
    with moveoutleft
    hide scott_border with dissolve
    ed "We won't do anything to your house, and we are sorry for destroying your laptop."
    cs "And I'm sorry for injuring your coworkers."
    stop music fadeout 3.0
    music end
    ed "Wesley is still in the hospital, so, like, if you wanted to give us some more money..."
    show cs disappointed at left
    cs "Didn't you scam me out of more money than my foundation was worth?"
    ed "Oh, yeah..."
    show cs angry at left
    cs "What {i}about{/i} my foundation, anyway?"
    show cs at left
    cs "Tell you what. If you can fix my foundation, I'll pay you for that, and we put this all behind us."
    rich "What do you think, Ed?"
    n "Ed ponders for a moment."
    ed "Sure. We have a deal."
    show cs happy at left
    cs "Woohoo!"
    n "As if the crowd couldn't get any bigger, the cops show up."
    show cs at left
    show copguy flipped at center with moveinleft
    copguy "Hey, CS, we finally found HoH SiS."
    copguy "And it looks like you did, too."
    show sheriff at mid_left with moveinleft
    sheriff "Good job, Copguy. Time to put them in the slammer!"
    cs "No need, guys, we worked everything out."
    sheriff "What?!"
    copguy "Are you sure?"
    ed "Yep, we've got everything under control."
    sheriff "All this for nothing..."
    sheriff "Whatever. C'mon, Copguy, let's go."
    n "The cops get back in their car and speed off."
    show copguy with determination
    hide sheriff with moveoutleft
    hide copguy with moveoutleft
    hide ed with moveoutright
    hide rich with moveoutright
    show cs at mid_right with moveinright
    n "After all that commotion, CS finally steps up to his front door."
    show cs flipped at mid_right
    n "He looks back out towards the crowd again one more time."
    cs "This is CS..."
    cs "Signing out!"
    play sound "cheers.ogg" volume 0.7
    pause 2.0
    n "The crowd erupts into cheers as CS finally enters his house."
    scene black with dissolve
    pause 1.0
    $ renpy.movie_cutscene("movies/hoh_repair.webm")
    scene cs_room with dissolve
    play music2 "<loop 0>ac_title.mp3" volume 0.4
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
        jump true_ending

label true_ending:
    stop music
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor, which has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have you work with us again virtually. Just give us a call!\"."
    cs "I'll have to make sure to call them later!"
    if persistent.true_ending:
        menu:
            "Go to sleep":
                jump archival
            "Stream" (type = "true"):
                jump streaming
    else:
        $ persistent.true_ending = True
        jump streaming

label streaming:
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs happy at mid_left
    cs "Well, guys..."
    n "CS chuckles."
    cs "It's a long story..."
    if achievement_manager.get("That's All, Folks!").unlocked:
        $ achievement_manager.unlock("All Over Again")
    else:
        $ achievement_manager.unlock("That's All, Folks!")
    if preferences.csbounciness == 100:
        $ achievement_manager.unlock("Boingy Boingy Boingy")
    scene black with fade
    stop music2 fadeout 1.0   
    $ renpy.movie_cutscene("movies/credits.webm")
    $ renpy.end_replay()
    return

label ytp_ending:
    stop music
    n "CS looks over at his desk, where his old computer is sitting."
    scene cs_room_2 with fade
    show cs at mid_left
    cs "Oh yeah, I forgot I actually have a computer that's not a craptop."
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well, guys..."
    n "CS chuckles."
    cs "It's a long story..."
    scene black with fade
    stop music2 fadeout 1.0   
    $ renpy.movie_cutscene("movies/credits.webm")
    $ renpy.end_replay()
    return

label ltt_ending:
    stop music
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor, which has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have you work with us again virtually. Just give us a call!\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat slowly comes in, confused."
    chat "Oh you're streaming?{w=0.25} I thought you were working for LTT now?{w=0.25} What happened to the YTPs?{w=0.25} Are you okay?{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well, guys..."
    cs "It's a long story..."
    scene black with fade
    stop music2 fadeout 1.0   
    $ renpy.movie_cutscene("movies/credits.webm")
    $ renpy.end_replay()
    return

label fighthohsis:
    stop music
    scene cs_house
    show cs disappointed at left
    show ed at right
    show rich at mid_mid_right behind ed
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
    cs "I no longer want the JoJ..."
    hide cs with moveoutbottom
    show ed with hpunch
    ed "Time to take a shit on the house."
    music end
    bad_end "Revenge!" "back_home"

label fuckuphohsis:
    stop music
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
    cs "Yeah, I actually hate you guys, and I wanted to mess with your business!"
    cs "You guys suck and I hate you both!"
    cs "You guys {i}deserve{/i} to have your company in shambles!"
    n "Richard and Ed back up to their UFO."
    hide rich
    hide ed
    with moveoutright
    cs "Hey! Where are you guys going?!"
    cs "Come back here!"
    hide cs with moveoutright
    n "The JoJ UFO flies up over the house, then vaporizes it with a laser."
    play sound "beam.ogg" volume 0.6
    show beam at xstretch_in
    pause 1.5
    show cshouse_vaporized behind beam
    show beam at xstretch_out
    pause 1.0
    show cs disappointed at left with moveinleft
    with vpunch
    n "Ed flips CS the bird, then flies away."
    show cs disappointed
    pause 1.0
    cs "Fuck."
    bad_end "Time to bunk\nat Rosen's!" "back_home"  

label copsathohsis:
    stop music
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
    n "CS calls Copguy to come arrest HoH SiS."
    show cs worried
    stop music2 fadeout 1.0
    music end
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" loop volume 0.5
    show copguy flipped at center with moveinleft
    cs "Here they are! They scammed me out of my money!"
    n "Copguy cuffs the HoH SiS members and pulls out his walkie."
    copguy "We got 'em, Sheriff. Time to put 'em in the slammer."
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
