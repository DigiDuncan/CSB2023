label archival:
    play music ac_title volume 0.4 if_changed
    music ac_title
    call screen warning("The following scene is a major tonal shift.\nIt may be disconcerting to some viewers.", "Warning: potential existential dread.", "back_out_archival")

    scene cs_room_2
    show cs flipped at mid_left
    n "CS looks down at his bed."
    cs "Yeah, after {i}everything{/i} that has happened today, some rest sounds really nice."
    show cs happy flipped at manual_pos(160, 200)
    play sound sfx_blanket volume 10.0
    show cs happy flipped at manual_pos(160, 200):
        rotate 0
        parallel:
            linear 0.5 rotate 60
        parallel:
            linear 0.5 ypos 300
        parallel:
            linear 0.5 xpos -350

    n "He eagerly hops into bed and gets cozy under his blanket."
    cs "Ah, finally, I can get a good night's sleep."
    n "CS points his finger guns towards the ceiling."
    cs "This {w=0.25}is {w=0.25}C{w=0.1}S{w=0.25}.{w=0.25}.{w=0.25}. {w=0.25}passing out!"
    stop music2 fadeout 3.0
    pause 0.5
    n "CS quickly drifts off to sleep."
    scene black with dissolve
    music end
    stop music fadeout 5.0
    pause 1.0
    n "..."
    n "..."
    n "..."
    pause 1.0
    scene bedroom_old with dissolve
    play music facing_worlds volume 0.5 if_changed
    music facing_worlds
    pause 1.0
    if fun_value(FUN_VALUE_MUSIC):
        n "CS slowly faces worlds after his long rest."
    else:
        n "CS slowly wakes up after his long rest."
    cs "Hey guys, CS here!"
    cs "How is every--{w=0.5}{nw}"
    with hpunch
    show cs scared at manual_pos(125,1080)
    show cs scared at left with MoveTransition(0.25)
    with vpunch
    n "CS immediately jolts up, realizing that he's not in his room."
    cs "Wait a minute. Where am I? This place..."
    pause 1.0
    n "CS trails off, feeling uneasy about this new location."
    n "It doesn't look familiar to him at all, but for some reason..."
    show cs worried
    cs "Why do I feel like I've {i}been{/i} here? Something isn't right..."
    n "CS spots a laptop on a nearby desk."
    n "He is somehow drawn towards it."
    scene craptop_old with dissolve
    show cs disappointed at left with moveinleft
    pause 0.5
    cs "I {i}feel{/i} like this is my craptop, but I don't even {i}have{/i} my craptop anymore!"
    cs "It looks {i}off{/i}, though..."
    n "CS lifts the lid and powers it on, curious about the strange connection he is feeling with it."
    n "The laptop slowly boots, playing the classic Windows XP start sound."
    n "The machine immediately bluescreens and blares out the following:"
    play sound sfx_windows_logon
    with hpunch
    show cs worried
    craptop "Your PC sux. lol."
    k174_offscreen "Hey, what the fuck was that?"
    show cs scared
    cs "Shit!"
    show cs scared flipped at offscreenleft with MoveTransition(0.25)
    scene bedroom_old with dissolve
    show cs scared flipped at offscreenright
    show cs scared flipped at offscreenleft with MoveTransition(0.25)
    n "CS jumps over the chair next to him, hiding between it and the couch in the corner."
    cs "{size=-12}Why are there people here?"
    play sound sfx_house_door_open
    n "The door slowly opens."
    pause 1.0
    show k174 at center with moveinright
    show k199 at mid_left_left with moveinright
    show k207h at mid_right_right with moveinright
    pause 0.5
    n "Three people with white suits and blue hair enter the room."
    n "They all look like the same person, except one is wearing sunglasses, another sports a top hat, and the third is in a hazmat suit."
    n "They quickly scan the room and notice the powered-on laptop."
    show k199 flipped
    k199_offscreen "What the hell, 17-M4! I thought this place didn't have any triggers!"
    k174 "It... shouldn't. This place barely has {i}any{/i} functionality!"
    k199_offscreen "Then {i}why{/i} is the craptop on? CS-ocola would be here right now!"
    k207_offscreen "Mrrrph mrrph, mrphh mrphh mrphh {i}mrrrrrph!"
    show k174 flipped
    k174 "{i}What?"
    show k174
    k199_offscreen "Dude, 20-M9, for the millionth time, take that thing off. We can't hear you."
    show k174 flipped
    k174 "Yeah, man, there's no \"whatever virus\" here that you keep talking about. It's {i}fine."
    n "K20-M7 carefully and slowly takes off their mask."
    play sound sfx_decompression volume 2.0
    hide k207h
    show k207 at mid_right_right
    with dissolve
    pause 1.0
    k207 "Alright, fine! But if I get corona and die, I'll make sure Addy fires {i}both{/i} of you!"
    k199_offscreen "Look, there's nothing to worry about. Besides, if you die, how are you gonna tell them?"
    k207 "Shut up, 19-M9!"
    k199 "Alright, sheesh."
    k207 "What I was {i}trying{/i} to say is that this could've taken place after HoH SiS left, meaning CS is out right now anyway."
    k199 "Yeah, but... why did it {i}trigger?{/i} There is {i}no one{/i} here!"
    k207 "I don't know, man! I'm just throwing something out there!"
    k199 "{i}God!{/i} It's a miracle you could even put this together, 17-M4. It feels like this place is barely holding up!"
    k199 "I mean, what did you write here? \"This house has felt like it was sitting with a giant rock on the side of the house\"?"
    k199 "Hahaha, that doesn't even make any fucking sense!"
    n "From his hiding spot in the corner, with his mind racing and trying to take in what's happening around him, CS feels a strong urge."
    n "That terribly broken English..."
    n "Why does it feel like he was supposed to say that just now?"
    show k174
    k174 "Look, I don't know why I wrote that."
    k174 "We need to figure out what's causing this! I'm getting worried."
    k207 "I'm sure it's nothing, dude. Why don't we go check out another part of this place?"
    pause 1.0
    k199 "Wait a second..."
    show k199
    pause 1.0
    n "K19-M9 sees something shift in the corner and leans in to look."
    show k199 at mid_offscreen_left with moveinright
    n "CS turns around for a moment and sees a face staring right at him."
    cs "Gahhhh!" with vpunch
    k199 "Oh, fuck! What the hell?!"
    show cs worried at left
    show k174 at mid_right
    show k199 at center
    with ease
    n "CS quickly stands up. The others stare silently at him for a moment."
    pause 1.0
    k207 "Shit! " with hpunch
    extend "Dude, that's him! He's {i}here!"
    show cs scared
    cs "Okay, wait! Hold on a second!"
    k174 "{i}What the FUCK?! {/i}{nw}" with hpunch
    extend "{i}Why does he look like that?{/i}"
    show cs disappointed
    cs "Damn, okay, now I just feel insulted."
    k199 "Dude, just... find something here to knock him out, or whatever!"
    k174 "Okayokayokay! I got this!"
    k174 "Take {i}this!"

    show expression DynamicDisplayable(Pixellated.pixellated, widget='worker_1', delay=0.5, steps=16) at manual_pos(0.7, 1.0, 1.0)

    show k207 at right
    show k174 at mid_right_right
    show k199 at mid_right
    with MoveTransition(0.25)
    play sound sfx_glitch_in

    show cs worried
    n "One of the HoH SiS workers materializes before CS."

    hide expression DynamicDisplayable(Pixellated.pixellated, widget='worker_1', delay=0.5, steps=16)
    show worker_1 at manual_pos(0.7, 1.0, 1.0)

    worker_1 "I don't know!"
    show k199 flipped
    k199 "What the fuck is {i}that{/i} thing?!"
    k199 "Why is it looking at us?"
    k199 "Make it {i}do{/i} something!"
    play sound snd_power
    show worker_4 at manual_pos(0.7, 1.0, 1.0)
    hide worker_1
    show k199
    pause 1.0
    "..."
    k207 "Who even {i}is{/i} this person?"
    k207 "Are they a construction worker? Are they a businessman?"
    n "CS suddenly lets his instincts take over."
    show cs angry
    cs "BullShisH!"
    play sound sfx_punch
    show cs angry at mid_mid_left
    show worker_4 at manual_pos(1.0, 2.0, 1.0):
        linear 0.25 rotate 90
    with MoveTransition(0.25)
    with hpunch
    n "CS punches the worker to the ground!"
    k199 "Oh, {i}shit,{/i} man! He's gone AWOL!"
    k207 "I don't think that's what AWOL means, but... still! {i}Do{/i} something, 17M!"
    k174 "Fuck,{w=0} fuck,{w=0} fuck! Okay,{w=0} okay, what about this? Do something!"

    show expression DynamicDisplayable(Pixellated.pixellated, widget='nova_head', delay=0.5, steps=8) as first at manual_pos(0.4, 1.5, 0.5):
        alpha 0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.6
    show cs worried at left
    with MoveTransition(0.25)
    play sound sfx_glitch_in

    show expression DynamicDisplayable(Pixellated.pixellated, widget='nova_head', delay=0.5, steps=8) as second at manual_pos(0.6, 1.5, 0.5):
        alpha 0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.6
    with MoveTransition(0.25)
    play sound sfx_glitch_in

    show expression DynamicDisplayable(Pixellated.pixellated, widget='nova_head', delay=0.5, steps=8) as third at manual_pos(0.8, 1.5, 0.5):
        alpha 0
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 ypos 0.6
    with MoveTransition(0.25)
    play sound sfx_glitch_in

    n "A bunch of heads appear in the middle of the room."
    nova "Nova?"
    nova "Nova Nova?"
    k199 "God, what the fuck are {i}those{/i} things?!"
    k199 "Make them attack CS!"
    nova "Nova Nova {i}Novaaa!"

    show nova_head as second at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch
    n "The heads charge toward the wrong people, trying to bite and rip them apart."

    show nova_head as first at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch
    k207 "{cshake}Ah! Ahh! Fuck, get them off!"

    show nova_head as third at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch
    k199 "{cshake}Kill them! {i}Kill{/i} themmm!"
    k199 "{cshake}17M, you piece of shit, make them {i}stop!"

    show nova_head as first at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch
    k174 "{cshake}Oh, God, what have I done?! I can't stop them!"

    show nova_head as second at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch

    show nova_head as third at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch

    show nova_head as first at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch

    show nova_head as second at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch

    show nova_head as third at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch

    show nova_head as first at random_pos(1300, 1800, 500, 900, 0.5)
    with MoveTransition(0.1)
    play sound sfx_bite
    with vpunch

    show cs at offscreenright with MoveTransition(0.25)
    n "CS realizes that this is his chance. He runs past them and out the door."
    play sound sfx_house_door_close
    scene door_old with dissolve
    show cs scared at left with moveinleft
    n "He quickly slams the door behind him as screams echo throughout the house."
    n "He somehow finds himself in the living room, even though the bedroom was on another floor."
    show cs worried
    cs "Shit, where do I go? I need to get out of here!"
    n "CS runs outside."
    show cs worried at mid_mid_left with MoveTransition(0.25)
    scene car_old with dissolve
    $ collect("cs_car_old")
    show cs worried at left with moveinleft
    n "A blue car is parked just outside the house."
    show carguya at right with moveinright
    play sound sfx_nice_car
    carguy_nobeep "Nice car! "
    play sound "<from 0 to 0.85>sfx/sfx_not_so_nice_scratch.ogg"
    extend "Nooooot so--{nw}"
    show cs scared at right
    show carguya at offscreenright:
        linear 0.1 xzoom -1
        linear 0.1 xzoom 1
    play sound2 sfx_punch noloop
    with MoveTransition(0.25)
    with hpunch
    n "CS pushes him out of the way."
    n "He smashes open the car window and hops inside."
    show cs scared flipped
    play sound sfx_glass_heavy
    scene car_inside_old with dissolve
    show cs scared flipped at offscreenright
    show cs scared flipped at left with MoveTransition(0.25)
    show cs scared
    play sound sfx_driving
    pause 1.0
    n "Despite the interior of the car being drastically different from the outside, the car thankfully starts up."
    n "CS starts to drive off, but he is instantly teleported away."
    scene csmart_old
    show cs scared at left
    stop sound
    play sound sfx_glitch_in
    with pixellate
    pause 2.0
    n "He reappears in the parking lot of a Walmart with a \"CS\" poorly pasted over the sign."
    cs "What {i}is{/i} this place?! What's going on?!"
    n "CS looks around for a second and sees what looks like a crack in the sky."
    cs "What the hell?!"
    n "Before he can figure out what to do, three familiar figures catch up with him."
    stop music fadeout 3.0
    music end
    show k199 at center
    show k174 at mid_right
    show k207 at right
    with moveinright
    k174 "There he is! He's trying to escape!"
    k199 "Yeah, not so fast, CS. We aren't letting you outta here {i}that{/i} easily."
    show cs disappointed
    cs "Can one of you guys {i}please{/i} tell me what's going on?!"
    k207 "Do we {i}really{/i} have to explain what's wrong to him?"
    k199 "No, he's going to find out the hard way. Let's kick his ass!"
    k174 "Shouldn't we let Addy deal with this?"
    if fun_value(FUN_VALUE_MUSIC):
        k199 "Fuck {i}that!{/i} Let's have a BATTLE UNDER A BROKEN SKY!"
    else:
        k199 "Fuck {i}that!{/i} Let's settle this now!"
    jump rpg_archival

label archival_finale:
    stop music fadeout 3.0
    music end
    scene csmart_old:
        zoom 1.5
    show cs disappointed at left
    with dissolve
    n "After the battle, CS makes his way towards the crack, and realizes that there is an invisible wall."
    hide cs with dissolve
    if fun_value(FUN_VALUE_MUSIC):
        n "Without any second thoughts, he breaks off enough pieces of the wall to widen the hole, then takes a trip. From me."
    else:
        n "Without any second thoughts, he breaks off enough pieces of the wall to widen the hole, then crawls through the opening."
    scene csmart_old with dissolve:
        zoom 1.75
    n "..."
    scene csmart_old with dissolve:
        zoom 2.0
    n "..."
    scene black with dissolve
    n "..."
    scene archival_1 with dissolve
    play music take_trip volume 0.7 if_changed
    music take_trip
    show cs scared at manual_pos(0.5, -1.5, 0.5)
    hide cs scared with moveoutbottom
    play sound sfx_glass_echo
    play sound2 sfx_splash noloop volume 0.4
    with vpunch
    n "The shattering of glass rings out."
    n "CS finds himself in a pool of glowing cyan liquid."
    show cs disappointed at center with moveinbottom
    n "He picks himself up from the broken glass and goo."
    n "CS looks around this place in awe."
    scene archival_6 with dissolve
    n "Stretching to every edge of the room are rows of hundreds of glowing tanks, all filled with the same bluish fluid."
    n "Stacked atop each other in rows of 20 or 30, they reach the ceiling of this enormous hangar-like facility."
    scene archival_2 with dissolve
    show cs disappointed at mid_left with moveinleft
    n "CS walks around this giant place, glancing at all of the tanks around him."
    n "He steps closer to one, peering inside, wondering if he can see anything."
    show cs disappointed at center with move
    scene csb1tube with dissolve
    n "A faint voice can be heard, one that sounds like his own."
    n "CS then sees a blurry vision of what looks like a version of himself, without his dress or cat ears, playing some kind of game."
    scene csb1tube
    show archival_5
    show cs disappointed
    with dissolve
    n "CS realizes that this other him is playing a game made of the very world that he lives in, even going so far as to poke fun at it."
    show cs scared with hpunch
    n "Before CS can really take all this in, a few guards at the end of the building shout at him."
    n "The rifle-toting guards are wearing tophats and black suits."
    scene archival_3 with dissolve
    show cs worried at right with moveinleft
    show cs worried flipped with determination
    n "They start to chase after CS. He runs a bit and then hides behind one of the canisters."
    show hart1 at center
    show m4 as first at center
    $ collect("m4")
    show hart2 at left
    show m4 as second at left
    with moveinleft
    n "The guys come around the corner, opening fire on CS as he sprints away."
    show cs scared with determination
    show cs scared at offscreenright with MoveTransition(0.25)
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    show hart1 at offscreenright
    show m4 as first at offscreenright
    with MoveTransition(0.25)
    show hart2 at offscreenright
    show m4 as second at offscreenright
    with MoveTransition(0.25)
    scene archival_7 with dissolve
    show cs scared at offscreenleft
    show cs scared at offscreenright with MoveTransition(0.25)
    n "CS starts weaving between the canisters to try to lose them."

    show hart1 at offscreenleft
    show m4 as first at offscreenleft
    show hart2 at offscreenleft
    show m4 as second at offscreenleft

    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7

    show hart1 at offscreenright
    show m4 as first at offscreenright
    with MoveTransition(0.25)

    show hart2 at offscreenright
    show m4 as second at offscreenright
    with MoveTransition(0.25)

    n "After he finally manages to make it to one end of the room, he runs along the wall, desperate to find an exit."
    scene archival_8 with dissolve
    n "As the guards keep shooting, he finds a set of doors that leads him into another large area."
    scene archival_7 with dissolve
    show cs scared at offscreenleft
    show cs scared at offscreenright with MoveTransition(0.25)

    show hart1 at offscreenleft
    show m4 as first at offscreenleft
    show hart2 at offscreenleft
    show m4 as second at offscreenleft

    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7

    show hart1 at offscreenright
    show m4 as first at offscreenright
    with MoveTransition(0.25)

    show hart2 at offscreenright
    show m4 as second at offscreenright
    with MoveTransition(0.25)

    n "The men continue their pursuit as a bunch of alarms sound, echoing throughout the whole place."
    n "A voice over the loudspeaker cuts through the sirens:"
    scene archival_5 with dissolve
    show cs scared at offscreenleft
    show cs scared at center with MoveTransition(0.25)
    play sound sfx_less_annoying_alarm_sound loop volume 0.6

    show hart1 at offscreenleft
    show m4 as first at offscreenleft
    show hart2 at offscreenleft
    show m4 as second at offscreenleft

    n "\"Warning! Warning! Memory breach at Sector 4 Foxtrot Kilo 17! Entity Charlie Sierra Bravo has breached containment. Please evacuate to Foxtrot Kilo 16 or below immediately.\""
    n "The alert plays repeatedly as CS keeps zigzagging around the chaos."
    show cs scared at offscreenright with MoveTransition(0.25)

    show hart1 at offscreenright
    show m4 as first at offscreenright
    with MoveTransition(0.25)

    show hart2 at offscreenright
    show m4 as second at offscreenright
    with MoveTransition(0.25)

    scene archival_9 with dissolve
    n "CS enters a hallway with a lot of turns. He goes straight for a bit, then veers left when he hears more gunfire."
    n "He alternates between going left and right, hoping to lose his attackers."
    window hide
    scene archival_10a with dissolve
    scene archival_11a with dissolve
    scene archival_9a with dissolve
    scene archival_10a with dissolve
    scene archival_11a with dissolve
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    scene archival_9a with dissolve
    scene archival_10 with dissolve
    scene archival_11 with dissolve
    scene archival_9a with dissolve
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    scene archival_10a with dissolve
    scene archival_11a with dissolve
    scene archival_9a with dissolve
    scene archival_10a with dissolve
    scene archival_11a with dissolve
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    scene archival_9a with dissolve
    scene archival_10 with dissolve
    scene archival_11 with dissolve
    scene archival_9a with dissolve
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    scene archival_10a with dissolve
    scene archival_11a with dissolve
    scene archival_9a with dissolve
    scene archival_10 with dissolve
    scene archival_11 with dissolve
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    scene archival_9a with dissolve
    scene archival_10 with dissolve
    scene archival_11 with dissolve
    scene archival_9a with dissolve
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    pause 0.1
    play sound sfx_hks2 noloop volume 0.7
    pause 0.1
    play sound sfx_hks1 noloop volume 0.7
    scene archival_10 with dissolve
    scene archival_11 with dissolve
    scene archival_12 with dissolve
    n "CS runs until he spots a sign that says \"Station 1 >>\"."
    n "He sprints through the exit, following the signs all the way down the hallway."
    scene archival_14 with dissolve
    n "Eventually he approaches a staircase."
    n "CS manages to make it down the stairs in time, but so do the men still chasing him."
    scene archival_15 with dissolve
    stop sound fadeout 3.0
    show cs scared at offscreenleft
    show cs scared at mid_left with MoveTransition(0.25)
    n "A bigger sign fades into view. The station is here."
    n "The final doors open to reveal a platform where a tram car waits for him."
    show cs scared at offscreenright with MoveTransition(0.25)
    scene archival_16 with dissolve
    show cs scared at offscreenleft
    show cs scared at mid_left with MoveTransition(0.25)
    n "CS makes one last dash to the tram, just rushing inside as the doors begin to close."
    show cs scared at center with MoveTransition(0.25)
    stop music fadeout 3.0
    scene archival_13 with dissolve
    play music take_trip2 volume 0.5 if_changed
    music take_trip
    pause 1.0
    n "He escapes into the car as the doors shut behind him, finally separating him from the guards."
    show archival_19
    with dissolve
    n "CS steps over to the console at the front of the tram and pulls the giant \"Forward\" lever."
    scene archival_15
    show hart1 at left
    show m4 as first at left
    show hart2 at center
    show m4 as second at center
    with dissolve
    n "The tram takes off, slowly gaining speed."
    show walkie as first_wt:
        zoom 0.3
        rotate 10
        xpos 0.2
        ypos 0.5
    show walkie as second_wt:
        zoom 0.3
        rotate 10
        xpos 0.5
        ypos 0.5
    with Dissolve(0.25)
    n "The men back away from the rail and pull out their walkie-talkies."
    scene black
    show archival_18
    show cs disappointed at center
    with dissolve
    n "CS catches his breath, then looks at what lies ahead from the window."
    scene train_start
    show cs disappointed at center
    with dissolve
    pause 1.0
    scene train_outside_tunnel
    show cs disappointed at center
    with dissolve
    n "The tram turns to the left as it is switched onto another rail."
    show cs scared
    with shake1
    n "As soon as it enters this lane, the tram begins to accelerate."
    scene archival_18
    show train_outside_tunnel
    show cs worried at center
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
    scene the_tram with dissolve
    n "CS looks to his right and witnesses more of the giant facilities flying past him at incredible speed."
    scene white
    show archival_18
    show cs worried at center
    with dissolve
    with hpunch
    n "After passing about twenty of these structures, the tram suddenly stops."
    n "CS looks around, confused, and then he looks to his left."
    n "He is met with a long and seemingly endless tunnel."
    show white_vignette at center:
        alpha 0
        linear 5 alpha 0.25
    show white_bg at center:
        alpha 0
        linear 5 alpha 0.05
    with dissolve
    n "A blinding light engulfs his vision."
    n "The tram, now stopped on a turntable, is rotated towards the light."
    scene train_in_tunnel
    show cs scared at center
    show white_vignette at center:
        alpha 0.25
        linear 5 alpha 0.35
    show white_bg at center:
        alpha 0.05
        linear 5 alpha 0.15
    with dissolve
    show cs scared with vpunch
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
    with hpunch
    with vpunch
    show cs scared
    with shake2
    n "The tram starts up again, now reaching ludicrous speeds."
    n "CS sees the light begin to envelop the outside of the tram, seeming to consume it."
    n "He starts to panic."
    show cs scared flipped
    pause 0.5
    show cs scared
    pause 0.5
    show cs scared flipped
    n "As he glances around for any escape, glimpses of memories of familiar places rush past him."
    scene car plains
    show archival_19
    show archival_19
    show white_vignette at center:
        alpha 0.35
        linear 5 alpha 0.45
    show white_bg at center:
        alpha 0.15
        linear 5 alpha 0.20
    with dissolve
    with shake1
    n "CS desperately tries to stop the train, but it is no use."
    scene sign_closeup
    show white_vignette at center:
        alpha 0.45
    show white_bg at center:
        alpha 0.20
    with dissolve
    n "He notices a panel above the door. A figure resembling one of the guards waves at him."
    scene white
    show train_in_tunnel
    show cs concentrate at center
    show white_vignette at center:
        alpha 0.45
        linear 5 alpha 0.55
    show white_bg at center:
        alpha 0.20
        linear 5 alpha 0.30
    with dissolve
    show cs concentrate
    with shake2
    show white_vignette at center:
        linear 10 alpha 1.0
    show white_bg at center:
        linear 10 alpha 0.40
    n "CS realizes that there is nothing he can do."
    n "He closes his eyes."
    n "The tram travels faster and faster as the light continues to glow brighter."
    n "Suddenly, it's all gone."
    stop music fadeout 3.0
    scene white with Dissolve(3.0)
    music end
    pause 5.0
    n "The tram, the facility, the light, and CS."
    n "It all disappears into nothing."
    pause 3.0
    scene black with Dissolve(1.0)
    pause 3.0
    $ achievement_manager.unlock("archived")
    n "CS has been deleted, and has been sent to the beginning of time itself."
    pause 2.0
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    pause 2.0
    play music everybody_wants if_changed
    music everybody_wants
    pause 5.0
    play sound sfx_ringtone_addy loop volume 0.5
    $ persistent.heard.add("sfx_ringtone_addy")
    n "Addy gets a phone call."
    pause 1.0
    play sound sfx_pickup_call
    pause 3.0
    if fun_value(FUN_VALUE_MUSIC):
        addy "Hello? Is this everybody? Because I want to rule the world."
        n "CS, from offscreen, bursts out laughing."
        iris "Okay, that was terrible."
        addy "I know, lol."
        addy "Anyways..."
    else:
        addy "Hello?"
        addy "Who is this?"
    iris "Hello, Addy."
    n "Addy fumbles the phone, nearly dropping it in surprise."
    addy "Iris?"
    iris "Hey."
    iris "Did you do something with a man named cs188?"
    addy "Oh, yeah, uh..."
    addy "We had an accident in the K17 sector yesterday."
    addy "We had to..."
    addy "Get rid of him."
    "..."
    iris "Hmm..."
    iris "Can you bring him back?"
    iris "Digi's been crying all day because they found out CS doesn't exist anymore."
    addy "Yeah, I should have a backup somewhere."
    iris "Nice, thank you."
    iris "I'll go tend to Digi."
    play sound sfx_end_call
    n "Iris hangs up."
    pause 1.0
    addy "I guess that's what I get for letting these guys with half a brain run this place."
    addy "I'll have to go clean up the mess later. I can still hear alarms."
    addy "In the meantime, let's get this memory prepared."
    play sound sfx_sliding_door_open
    n "Addy pulls out a small memory jar they've been saving from a cabinet in their office."
    stop music fadeout 3.0
    music end
    addy "Thank goodness I saved this."
    # i'm so sorry
    # but also you can't tell me that liquid DOESN'T look like chug - tate
    play sound sfx_chug_jug
    n "Addy places the jar into a receptacle."
    addy "Well, here goes nothing."
    $ ending_manager.mark("archival")
    $ renpy.sound.stop(fadeout=3.0)
    $ renpy.movie_cutscene(archival_end)
    $ renpy.end_replay()
    return
