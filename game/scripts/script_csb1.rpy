screen best_music():
    layer "music"
    zorder 100
    image "best_music.png" at music_appear
    timer 5 action Hide('best_music')

label csbi_start:
    $ quick_menu = False
    stop music fadeout 3.0
    scene black with dissolve
    $ quick_menu = True
    if persistent.first_time:
        window hide
        scene cs_room
        show cs at center
        show oldgame
        with dissolve
        pause 7.0
        show pakoo at right with moveinright
        pakoo "Oh, whoops!"
        pakoo "The old game is still here..."
        pakoo "Lemme fix that real quick for you."
        play sound sfx_page volume 5
        if e1:
            show pakoo disappointed with determination
            hide pakoo
        else:
            hide pakoo
        hide oldgame
        with moveoutright
    $ persistent.first_time = False
    if e3:
        jump e3
    window hide
    scene cs_room
    show cs at center
    with dissolve
    play music lets_hear_my_baby volume 0.15
    music "Let's hear my baby - Walkman"
    if fun_value(FUN_VALUE_MUSIC):
        cs "Welp, Let's hear my baby."
    else:
        cs "Welp, time to start up the ol' Craptop."
    hide cs
    jump csbi_craptop

label csbi_craptop:
    play music lets_hear_my_baby volume 0.15 if_changed
    scene craptop_bg
    show craptop desktop
    if e2:
        show post_it2 at t_post_it
    else:
        show post_it at t_post_it

    $ achievement_manager.unlock("ZUP!")
    craptop "Your PC sux. lol."
    if e2:
        jump e2
    else:
        sticky "Delete the CSCord."
    cs "Eh, maybe tomorrow."
    hide post_it
    play sound sfx_page volume 5
    pause 2.0
    show craptop updating
    craptop "Downloading update 200/13..."
    craptop "Update complete."
    cs "{bt=a3-p10-s4}OoOoOoOoOh{/bt} yes!"
    show craptop discord
    play sound sfx_windows_logon
    cs "Hey guys!"
    play sound sfx_ping_spam
    discord "Hi! Hi! Hi! Hi!"
    n "The Discord is overflowing with people trying to talk to CS."
    show cs at left with moveinleft
    menu:
        "What will CS do?"
        "Speedrun CSBounciness" (type = "dx"):
            jump vibration
        "Respond to chat" (type = "true"):
            pass
    play sound sfx_ping
    cs "Okay, bedtime! Bye, guys!"
    show nova at right
    play sound sfx_ping
    nova "But it's like 8:04AM and you just woke up."
    play sound sfx_ping
    cs "Bye!"
    show cs flipped with determination
    hide cs with moveoutleft
    discord "CS is now offline."
    play sound sfx_ping
    nova "k bye"
    hide nova
    show craptop car
    cs "Time to watch car crash videos for the next couple of hours!"
    show black with dissolve
    centered "Two hours later..."
    scene cs_room
    show cs
    cs "Okay... What to do, now?"
    cs "I could go outside, look at some flowers..."
    show cs happy
    stop music fadeout 3.0
    music end
    cs "Yeah! Let's go outside!"
    scene cs_house
    show cs happy
    with dissolve
    play music canyon volume 0.2
    music CANYON.MID - George Stone
    if fun_value(FUN_VALUE_MUSIC):
        cs "Woah! Is that a canyon over there?"
    else:    
        cs "Nice day!"
    show cs
    cs "Well, I guess it's car time."
    show cs_car behind cs
    hide cs_house
    show cs at left with move
    show carguy at right with moveinright
    play sound sfx_nice_car
    carguy_nobeep "Nice car!"
    cs "It's pretty nice, but it's got some scratches..."
    play sound sfx_not_so_nice_scratch
    carguy_nobeep "Nooot so nice scratch..."
    carguy "You should try Crotch Doctor!"
    show cs worried at left
    cs "OH GOD, AN ADVERTISER!!!"
    stop music fadeout 3.0
    music end
    show cs scared at left
    cs "QUICK! START THE CAR, START THE CAR!!!"
    hide cs with moveoutright
    play sound sfx_doorslam
    scene cs_car_inside
    show cs disappointed at left
    with dissolve
    play music canyon_car volume 0.2
    music CANYON.MID - George Stone
    cs "Whew... That was close!"
    cs "Should I go get groceries?"
    menu:
        "Get groceries?"
        "Yes":
            cs "Yeah... It's a good idea to get some stuff."
        "No":
            $ achievement_manager.unlock("I Don't Like People!")
            show cs happy at left
            cs "Screw you, I'm going anyway!"
    play sound sfx_driving volume 0.5
    pause 3.0
    jump csbi_walmart

label csbi_walmart:
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    scene walmart_outside
    show cs happy
    with dissolve
    cs "Oh, yes! Walmart is open!"
    scene walmart_inside with dissolve

    # This has to be like this because CJK support for this is mid.
    show screen best_music
    $ _current_song = "Summer Clearance Sale"
    $ _current_artist = "BEST MUSIC"
    play music summer_clearance_sale
    $ persistent.heard.add("Summer Clearance Sale - BEST MUSIC")

    n "CS walks inside."
    show doug at right with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        greeter "Welcome, the Summer Clearance Sale is going on! Isn't this the BEST MUSIC ever?"
    else:
        greeter "Hello, and welcome to Walmart! Can I help you with anything?"
    show cs at left with moveinleft
    cs "Wow! It's Walmart CEO Doug McMillon! You actually work here?"
    doug "Of course! They were short a greeter today, so I filled in the slot!"
    cs "Wow! He seems like a good man!"
    show doug at offscreenright
    show cs at center
    with move
    hide doug
    cs "Now, let's find some food!"
    show walmart_aisle behind cs with dissolve
    cs "{i}pop{/i}\nNoice! Genergy is two for $5! I'll take them all!"
    show cs happy
    cs "Oooh! Pringles are on sale too! Yoink!"
    n "CS walks to the checkout area."
    scene walmart_register
    show cashier at mid_mid_right
    show walmart_register_fg
    with dissolve
    show cs at left with moveinleft
    cs "Here's my stuff!"
    cashier "That'll be $11.88."
    cs "Here you go!"
    cashier "Have a good day."
    cs "You too, bye!"
    hide cs with moveoutright
    stop music fadeout 3.0
    music end
    scene walmart_outside with dissolve
    show cs at left with moveinleft
    cs "Let's get to the car."
    show carguy at right with moveinright
    play sound sfx_not_so_nice_scratch
    carguy_nobeep "Nooooot so nice scratch."
    show cs disappointed at left
    cs "Not you again!"
    cs "I've gotta get outta here!"
    hide cs with moveoutright
    play sound sfx_doorslam
    scene cs_car_inside
    show cs worried at left
    with dissolve
    play music canyon_car volume 0.2
    play sound sfx_driving volume 0.5
    cs "Let's get home before that guy doctors my crotch!"
    scene black with dissolve
    n "CS drives home and manages to avoid reenacting one of his favorite car crash videos."
    jump csbi_room

label csbi_room:
    scene cs_room
    show cs
    with dissolve
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    n "CS arrives home and walks to his room."
    show cs happy
    cs "Ahhh. It's good to be home!"
    show cs surprised
    cs "You know, I haven't put out a YTP in a while. I should work on one of my in-progress ones."
    scene craptop_bg
    show craptop edit
    with dissolve
    play music scales_of_joy volume 0.3
    music scales of joy.mod - Mel O Dee
    n "CS sits down at his craptop and opens up Premiere."
    if fun_value(FUN_VALUE_MUSIC):
        cs "Ooooh! I can really feel the scales of joy! People would be excited to finally see this as a finished product."
    else:
        cs "Ooooh! Here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    n "CS watches the in-progress video."
    cs "This is pretty good, but I'm feeling uninspired... I don't know where to go from here..."
    cs "Hmmm..."
    cs "I know! I should watch some other YTPs for inspiration."
    show craptop ytp
    n "CS opens up YouTube and begins watching YTPs. After a while, CS runs into some older poops."
    cs "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now..."
    cs "..."
    cs "Oh, look, a flashback. What a coincidence..."
    scene cs_room with pixellate
    show cs_young with moveinbottom
    ycs "Hey guys, Young CS here! Today, I'm gonna be editing a \n{bt=a3-p10-s4}CraAaAaAaAzY{/bt} video!!"
    play sound sfx_keyboard
    n "CS taps furiously on his keyboard."
    ycs "Ohhhhhh {bt=a3-p10-s4}YeeEeeEeEeeEEeEEs!{/bt} This is lookin' good!"
    hide cs_young
    scene cs_room
    show cs
    with pixellate
    cs "Oh, flashback over."
    play sound sfx_foundationfail volume 0.5
    show cs worried
    show cs_room behind cs at rotate_10 with hpunch
    n "A loud crash is heard as a crack is split in CS' foundation."
    show cs worried
    cs "Woah! I was dreaming for so long that the foundation fell apart. My house just fell to the side!"
    cs "I really need to get some foundation repair."
    show cs
    cs "Better call HoH SiS!"
    cs "They're really good at giving me the JoJ!"
    show cs phone
    n "CS dials 1-800-HoH-SiiS."
    cs "Hello? Can you give me the JoJ?"
    hoh_operator "Is this a prank caller on the line?"
    show cs phone worried
    cs "No! My house really needs foundation repair! I need your help ASAP!!"
    hoh_operator "Alright. That will be 200,000 bits. You can pay us afterwards."
    n "The operator hangs up."
    show cs
    cs "Welp, that's one thing taken care of."
    cs "I guess I'll work on my new YTP while I wait."
    scene black with dissolve
    n "Time passes and the doorbell rings."
    play sound sfx_doorbell volume 0.5
    stop music fadeout 3.0
    music end
    scene door_closed with dissolve
    show cs happy with moveinleft
    cs "Oh, they're here!"
    cs "Let me go get the door..."
    show cs at left with move
    show door_open behind cs
    cs "Hello! I am CS, and I--"
    show ed at right with moveinright
    play music hohsis_theme volume 0.2
    music Alfred Hitchcock Intro Theme - Charles Gounod
    if fun_value(FUN_VALUE_MUSIC):
        ed "Alright, that will be Alfred Hitchcock Intro Theme."
        show cs disappointed
        cs "What?"
        show cs
    else:    
        ed "Alright, that will be 200,000 Bits."
    cs "Okay, I guess they already told you what I need done. Lemme get my wallet..."
    show cs disappointed
    cs "Hang on a sec. Didn't they say I could pay afterwards?"
    ed "Yeah, well, corporate policies just changed five seconds ago. Pay up."
    show cs disappointed flipped with determination
    hide cs with moveoutleft
    n "A few moments later..."
    show cs at left with moveinleft
    cs "Here you go! I'll get out of your guys' hair while you work."
    hide cs with moveoutright
    n "CS leaves after paying 200,000 bits."
    ed "Come on in, guys. CS just left."
    show ed at left with move
    show wesley at center with moveinright
    show rich at right with moveinright
    ed "So, now that we're here, what should we do to him?"
    "Ed, Wesley, and Richard" "Hmmm..."
    wesley "Let's go check his room. We might get some ideas."
    show cs_room_2 behind ed with dissolve
    n "The three HoH SiS workers go to CS's room."
    wesley "Wow, I didn't know CS had a Union Jack!"
    ed "CS sure loves those Brits~!"
    wesley "Alright, but, now what should we do?"
    ed "How about we burn down his house!"
    wesley "Eh..."
    rich "How about we mess with his laptop?"
    ed "Good idea! Let's get sabotagin'!"
    scene craptop_bg
    show craptop desktop
    with dissolve
    n "Ed launches the craptop."
    ed "Heheh... He won't know what hit him..."
    wesley "Quickly! Let's get out of here before he comes back!"
    show craptop updating
    wesley "Hurry up!"
    show craptop error with hpunch
    pause 1.0
    scene cs_house with dissolve
    show ed at left
    show wesley at center
    show rich at right
    with moveinright
    rich "Lemme call our JoJ UFO."
    "Ed, Wesley, and Richard" "I'm beaming up!"
    play sound sfx_beam volume 0.6
    show beam at xstretch_in
    pause 2.0
    hide ed
    hide wesley
    hide rich
    with moveouttop
    show beam at xstretch_out
    pause 2.0
    stop music fadeout 3.0
    music end
    scene cs_street
    with dissolve
    show cs with moveinleft
    cs "Things sure are boooooring around here..."
    cs "Hey, I've got an idea!"
    show cs happy
    cs "Let's go to Michael Rosen's house!"
    jump csbi_michael_house

label csbi_michael_house:
    scene car_inside
    show cs at left
    with dissolve
    play music canyon_car volume 0.2
    cs "Thankfully, Michael lives pretty close."
    cs "His vacation house in the US is only a few streets away!"
    cs "Before I forget, I should probably call him first."
    show cs phone at left
    n "CS pulls out his phone and calls Michael."
    michael "Hello!"
    cs "Hey, Michael! How're you doin' today?"
    michael "I'm feeling rather noice today."
    show cs happy phone
    cs "That's good to hear! You mind if I head over to your place?"
    show cs phone
    cs "The JoJ is being done on my house, so I figured we can chat for a bit."
    michael "Sure! I have a another guest visiting as well, bringing chocolate cake."
    show cs happy phone
    cs "Mmm! That sounds delicious!"
    show cs phone
    n "CS looks in the back seat of his car."
    cs "I have some Genergy with me, if you guys want some."
    michael "Sounds wonderful. I've never tried it, but I'm sure it's good."
    show cs happy phone
    cs "Alright, well, I'll be there soon!"
    show cs at left
    n "CS puts his phone away and drives over to Michael's house."
    play sound sfx_driving volume 0.5
    pause 2.0
    show black with dissolve
    stop sound fadeout 2.0
    jump csbi_rosen_house

label csbi_rosen_house:
    if e3:
        jump e3_rosen
    else:
        scene rosen_abode with dissolve
    play music super_friendly volume 0.4
    music Super Friendly - Kevin Macleod
    show michael at right with moveinright
    show cs flipped at offscreenright
    if fun_value(FUN_VALUE_MUSIC):
        michael "Come in! Come in! I'm Super Friendly!"
    else:
        michael "Come in! Come in!"
    show michael at left
    show cs flipped at right
    with ease
    cs "Hey, Michael!"
    michael "Sit down, make yourself comfy. I've got a new poem I want to show you!"
    cs "Sure thing, enlighten me."
    michael "Right. This one is called{w} {i}The Library.{/i}"
    michael "There once was a man who would go on a grand adventure."
    michael "He would meet all sorts of friends, and flee from his enemies."
    michael "After his long adventure, he took a long nap."
    michael "When he woke up, he was in a {i}huge{/i} library."
    if e2:
        jump e2_rosen
    if e1:
        michael "He started to get up, and walk around."
        michael "While he was walking, he found a--{nw}"
        show black
    else:
        show black with dissolve
    play sound sfx_csnore
    michael "CS? Did you fall asleep?"
    michael "CS!"
    stop sound
    hide black
    cs "Wha- what?"
    michael "Did you just... sleep through my entire poem?"
    show cs worried flipped
    cs "Nooooooooooooooooo?"
    n "Michael sighs and facepalms."
    play sound sfx_doorbell volume 0.5 
    n "The doorbell rings."
    michael "Oh! My other guest is here! I'll be right back!"
    show cs flipped
    hide michael at right with moveoutright
    show michael at left with moveinright
    show phil at center with moveinright
    phil "Phil Swift here!"
    michael "CS, meet my other friend, Phil!"
    cs "Oh, wow! I didn't know you were friends with Phil Swift!"
    michael "Well, it might be because he said he could make the best chocolate cake."
    michael "Speaking of which, Phil, do you have the cake?"
    phil "Here it is! It even works underwater!"
    michael "That's odd to mention, but time to eat!"
    show cs worried flipped
    n "CS suddenly realizes what's going on."
    show cs scared flipped at right
    cs "Michael! That's not chocolate cake!"
    michael "I have loads to eat! Om nom nom..."
    play sound sfx_puke
    michael_nobeep "Blarrrgh!"
    n "Michael spits out the Flex Seal cake."
    michael "This is horrible! Get out! Get out of here!"
    phil "But, it seals, and bonds--"
    michael "OUT!"
    hide phil with moveoutright
    hide cs
    show cs disappointed flipped at right
    michael "I need something to drink. CS, did you bring that drink?"
    cs "Sure thing, here you go."
    michael "Goodness."
    n "Michael downs the whole can."
    michael "Quick! Get out!"
    show cs worried flipped
    cs "What's going on?"
    michael "The Genergyfoogle is here! It's come to eat us all!"
    cs "Oh man, did that Genergy have something {i}else{/i} in it...?"
    show cs scared flipped
    cs "I need to get out before he goes nuts!"
    show cs scared with determination
    hide cs with moveoutright
    pause 0.5
    jump csbi_end

label csbi_end:
    scene car_inside
    show cs surprised at left
    with dissolve
    play music canyon_car volume 0.2
    play sound sfx_driving volume 0.5
    $ achievement_manager.unlock("Overcaffeinated")
    stop music fadeout 3.0
    music end
    cs "I should check on the HoH SiS folks. They should be making some progress by now."
    scene cs_room with dissolve
    show cs with moveinleft
    stop sound fadeout 2.0
    n "CS walks into his apartment."
    show cs disappointed
    cs "What?! They're gone? Already?"
    cs "I guess I should get back to work on that YTP, then..."
    hide cs
    scene craptop_bg
    show craptop off
    n "CS attempts to boot his laptop."
    n "..."
    n "Nothing."
    cs "Stupid craptop, turn on!"
    n "CS tries to turn it on again.{w} Nothing."
    cs "Maybe it finally died..."
    cs "Wait..."
    cs "The last people in this room were the HoH SiS guys!"
    cs "They must have messed with it!"
    show craptop_bg at rotate_6
    show craptop off at rotate_6
    with hpunch
    window hide
    play sound sfx_foundationfail volume 0.5
    pause 3.0
    cs "They didn't even do the JoJ!"
    show craptop sad at rotate_6 with hpunch
    play sound sfx_punch
    if fun_value(FUN_VALUE_RARE):
        play sound sfx_gul
    pause 1.0
    scene cs_room
    show cs angry
    cs "I need to get those guys!"
    cs "I'm gonna go to HoH SiS HQ and kick some butt!"
    scene hoh_outside with dissolve
    window hide
    pause 1.0
    scene hoh_hq
    show cs angry
    with dissolve
    play music time_for_a_smackdown volume 0.2
    music Time for a Smackdown! - Mr. Sauceman
    if fun_value(FUN_VALUE_MUSIC):
        cs "Alright! It's time for a Smackdown!"       
    else:    
        cs "Alright! Where are the head JoJites?!"
    show worker_1 at right with moveinright
    dxcom hohsisfight
    worker_1 "I don't know!!"
    cs "BullShisH!"
    n "CS punches the worker."
    play sound sfx_punch
    show worker_1 at right with hpunch
    $ persistent.seen.add("hoh_worker")
    hide worker_1 with moveoutright
    show worker_2 at right with moveinright
    worker_2 "They-- They're on the roof!!"
    cs "Good!!"
    hide screen dxcom
    n "..."
    show black with dissolve
    scene hoh_hq2
    show worker_3 at mid_center_right
    show worker_4 at mid_left
    with dissolve
    show cs angry flipped with moveinright
    cs "Get out of my way!"
    n "CS bodyslams the workers as he runs past."
    play sound sfx_punch
    show cs angry flipped at mid_left with move
    show worker_4 at mid_left with hpunch
    hide worker_4 with moveoutleft
    play sound sfx_punch
    show cs angry with determination
    show cs angry at mid_right with move
    show worker_3 at mid_center_right with hpunch
    hide worker_3 with moveoutright
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        cs "Ow."
        mean "AUUUUUGH!!"
    show cs angry at offscreenright with move
    show black with dissolve
    scene hoh_hq3
    show worker_5 at left
    with dissolve
    show cs angry flipped at right with moveinright
    cs "Which way to the elevator? Now!"
    hide worker_5
    show worker_5alt at left
    worker_5 "Uhh, that way!"
    cs "Thanks, and also--"
    n "CS clocks the worker in the face."
    show cs angry flipped at left with move
    play sound sfx_punch
    show cs angry flipped at offscreenleft with move
    show worker_5alt at left with hpunch
    hide worker_5alt with moveoutbottom
    scene hoh_hq4 with dissolve
    show cs angry with moveinbottom
    cs "Which way to go..."

    menu:
        "Left":
            jump csbi_end_left
        "Right":
            jump csbi_end_right

label csbi_end_left:
    scene hoh_hq5
    show worker_6 at right
    with dissolve
    show cs angry at left with moveinleft
    cs "A... pineapple?"
    show cs angry at right with move
    play sound sfx_punch
    show cs angry at left with move
    show worker_6 at right with hpunch
    hide worker_6 with moveoutright

    $ achievement_manager.unlock("HoH SiS's Most Wanted")

    scene black with dissolve
    scene hoh_elevator
    show cs angry
    with dissolve
    pause 2.0
    play sound sfx_elevator_ding
    scene black with dissolve
    jump csbii_start

label csbi_end_right:
    scene hoh_hq5
    show worker_7 at right
    with dissolve
    show cs angry at left with moveinleft
    cs "A fucking chicken?"
    show cs angry at right with move
    play sound sfx_punch
    show cs angry at left with move
    show worker_7 at right with hpunch
    hide worker_7 with moveoutright
    
    $ achievement_manager.unlock("HoH SiS's Most Wanted")

    scene black with dissolve
    scene hoh_elevator
    show cs angry
    with dissolve
    pause 2.0
    play sound sfx_elevator_ding
    scene black with dissolve
    jump csbii_start
