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
    play music lets_hear_my_baby volume 0.15 if_changed
    music lets_hear_my_baby
    if fun_value(FUN_VALUE_MUSIC):
        cs "Welp, Let's hear my baby."
    else:
        cs "Welp, time to start up the ol' Craptop."
    hide cs
    jump csbi_craptop

label csbi_craptop:
    play music lets_hear_my_baby volume 0.15 if_changed
    music lets_hear_my_baby
    scene craptop_bg
    show craptop desktop
    $ collect("craptop")
    if e2:
        show post_it2 at t_post_it
    else:
        show post_it at t_post_it
    with dissolve

    $ achievement_manager.unlock("zup")
    pause 1.0
    craptop "Your PC sux. lol."
    if e2:
        jump e2
    else:
        sticky "Delete the CSCord."
    cs "Eh, maybe tomorrow."
    play sound sfx_page volume 5
    show post_it at manual_pos(0.7, -300) with MoveTransition(0.25):
        linear 0.25 yzoom -1
    pause 2.0
    show craptop updating
    craptop "Downloading update 200/13..."
    craptop "Update complete."
    cs "{cshake}OoOoOoOoOh{/bt} yes!"
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
        "Just... don't." (type = "dx"):
            jump csbi_nah
            
    play sound sfx_ping
    cs "Okay, bedtime! Bye, guys!"
    show nova discord at manual_pos(0.6, 0) with Dissolve(0.1)
    play sound sfx_ping
    nova "But... it's, like, 8:04 AM, and you just woke up."
    play sound sfx_ping
    cs "Bye!"
    show cs flipped with determination
    hide cs with moveoutleft
    discord "CS is now offline."
    play sound sfx_ping
    nova "k bye"
    hide nova with Dissolve(0.1)
    show craptop car
    play sound sfx_car_stop
    cs "Time to watch car crash videos for the next couple of hours!"
    show black with dissolve
    centered "Two hours later..."
    scene cs_room
    show cs
    with dissolve
    cs "Okay... What to do, now?"
    cs "I could go outside, look at some flowers..."
    show cs happy
    stop music fadeout 3.0
    music end
    cs "Yeah! Let's go outside!"
    hide cs with moveoutright
    scene black with dissolve
    pause 1.0
    scene cs_house
    show cs happy
    with dissolve
    play music canyon volume 0.2 if_changed
    music canyon
    if fun_value(FUN_VALUE_MUSIC):
        cs "Woah! Is that a canyon over there?"
    else:    
        cs "Nice day!"
    show cs
    cs "Well, I guess it's car time."
    scene cs_car
    $ collect("cs_car")
    show carguy at right
    with dissolve
    show cs at left with moveinleft
    play sound sfx_nice_car
    carguy_nobeep "Nice car!"
    show cs disappointed
    cs "It's pretty nice, but it's got some scratches..."
    play sound sfx_not_so_nice_scratch
    carguy_nobeep "Nooot so nice scratch..."
    carguy "You should try Crotch Doctor!"
    show cs worried at left
    cs "OH GOD, AN ADVERTISER!!!"
    stop music fadeout 3.0
    music end
    show cs scared at left
    cs "QUICK! START THE CAR, {i}START THE CAR!!!"
    show cs scared at right behind carguy with MoveTransition(0.25)
    play sound sfx_doorslam
    scene cs_car_inside
    # TODO: baker needs the street view img to finish recoloring the car. cs does not drive a red car
    show cs disappointed at left
    with dissolve
    play music canyon_car volume 0.2 if_changed
    music canyon
    pause 1.0
    cs "Whew... That was close!"
    cs "Should I go get groceries?"
    menu:
        "Get groceries?"
        "Yes":
            cs "Yeah... I should probably go pick up a few things."
        "No":
            $ achievement_manager.unlock("no_people")
            show cs happy at left
            cs "Screw you, I'm going anyway!"
    play sound sfx_driving volume 0.5
    scene black with dissolve
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    pause 3.0
    jump csbi_walmart

label csbi_walmart:
    scene walmart_outside
    show cs happy
    with dissolve
    cs "Oh, yes! Walmart is open!"
    scene walmart_inside with dissolve

    play music summer_clearance_sale if_changed
    music summer_clearance_sale
    
    show cs at left with moveinleft
    n "CS walks inside."
    show doug at right with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        greeter "Hello, and welcome to our Summer Clearance Sale! Isn't this the BEST MUSIC ever?"
    else:
        greeter "Hello, and welcome to Walmart! Can I help you with anything?"
    cs "Wow! It's Walmart CEO Doug McMillon! You actually {i}work{/i} here?"
    doug "Of course! We were short a greeter today, so I filled in for them!"
    doug "Enjoy your visit!"
    hide doug with moveoutleft
    n "Doug gets back to work."
    cs "Wow! He seems like a good man!"
    show cs at center
    with move
    hide doug
    cs "Now, let's find some food!"
    hide cs with moveoutright
    scene black with dissolve
    scene walmart_aisle
    with dissolve
    show cs at center with moveinleft
    pause 1.0
    show cs at right with moveinleft
    pause 1.0
    play sound sfx_noicepop
    show cs happy
    cs "{i}pop{/i}\nNoice! Genergy is two for $5! Yes, {i}please!"
    show genergy at manual_pos(1800, 300) with Dissolve(0.25)
    $ collect("genergy")
    show genergy at manual_pos(1650, 800) with MoveTransition(0.25)
    hide genergy with dissolve
    show genergy at manual_pos(1800, 300) with Dissolve(0.25)
    show genergy at manual_pos(1650, 800) with MoveTransition(0.25)
    hide genergy with dissolve
    show cs flipped at center with moveinleft
    pause 1.0
    show cs flipped at left with moveinright
    pause 1.0
    show cs happy flipped
    cs "Oooh! Pringles are on sale, too! {i}Yoink!"
    show pringles at manual_pos(50, 300) with Dissolve(0.25)
    $ collect("pringles")
    show pringles at manual_pos(200, 800) with MoveTransition(0.25)
    hide pringles with dissolve
    show cs at center with moveinleft
    n "CS walks to the checkout area."
    hide cs with moveoutright
    scene black with dissolve
    pause 1.0
    scene walmart_register
    show cashier at mid_mid_right
    show walmart_register_fg
    with dissolve
    show cs at left with moveinleft
    pause 1.0
    cs "Here's my stuff!"
    show pringles at manual_pos(500, 500) 
    show genergy at manual_pos(450, 500)
    show genergy at manual_pos(425, 500) as duplicate
    with dissolve
    n "The cashier scans each item."
    play sound sfx_retail_beep
    show pringles behind cs at manual_pos(1750, 550) with move
    pause 0.5
    # small detail time: cashier goes lazy mode and scans one genergy twice
    show genergy behind cs at manual_pos(800,500) with move
    play sound sfx_retail_beep
    pause 0.25
    play sound sfx_retail_beep
    show genergy behind cs at manual_pos(1625, 650) with move
    show genergy behind cs as duplicate at manual_pos(1500, 625) with move
    pause 0.5
    play sound sfx_retail_beep
    pause 2.0
    cashier "That'll be $11.88."
    cs "Here you go!"
    play sound sfx_moneyfalls
    show spent_11_88 at t_fake_rpg_text(0.1, 0.1, 0.5)
    pause 2.0
    cashier "Have a nice day."
    show cs happy
    cs "You, too! Bye!"
    show cs at mid_offscreen_right with moveoutright
    pause 1.0
    hide pringles
    hide genergy
    hide genergy as duplicate
    show walmart_bag at right
    $ collect("walmart_bag")
    with dissolve
    hide cs
    hide walmart_bag
    with moveoutright
    stop music fadeout 3.0
    music end
    scene walmart_outside with dissolve
    show cs at left
    show walmart_bag at left
    with moveinleft
    cs "Let's get to the car."
    show carguy at right with moveinright
    play sound sfx_not_so_nice_scratch
    carguy_nobeep "Nooooot so nice scratch."
    show cs worried at left
    cs "Not {i}you,{/i} again!"
    cs "I've gotta get outta here!"
    show cs at offscreenright
    show walmart_bag at offscreenright
    with MoveTransition(0.25)
    play sound sfx_doorslam
    scene cs_car_inside
    show cs scared at left
    with dissolve
    play music canyon_car volume 0.2 if_changed
    music canyon
    play sound sfx_driving volume 0.5
    cs "Let's get home before that guy doctors {i}my{/i} crotch!"
    scene black with dissolve
    n "CS drives home, managing to avoid reenacting one of his favorite car crash videos."
    jump csbi_room

label csbi_room:
    scene cs_room
    with dissolve
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    play sound sfx_house_door_open
    pause 1.0
    play sound sfx_house_door_close
    n "CS arrives home and walks into the living room."
    pause 1.0
    show cs happy flipped with moveinright
    cs "Ahhh. It's good to be home!"
    show cs surprised flipped
    cs "What to do, now..."
    cs "You know, I haven't put out a YTP in a while. I should work on one of my in-progress ones."
    scene craptop_bg
    show craptop edit
    with dissolve
    play music scales_of_joy volume 0.3 if_changed
    music scales_of_joy
    n "CS sits down at his craptop and opens up Premiere."
    if fun_value(FUN_VALUE_MUSIC):
        cs "Ooooh! I can really feel the scales of joy! People would be excited to finally see this as a finished product."
    else:
        cs "Ooooh! Here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    n "CS watches the unfinished video."
    cs "This is pretty good, but I'm feeling uninspired... I don't know where to go from here..."
    cs "Hmm..."
    cs "I know! I should watch some other YTPs for inspiration."
    show craptop ytp
    n "CS opens up YouTube and begins watching YTPs. After a while, he comes across some older poops."
    cs "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now..."
    cs "..."
    cs "Oh, look, a flashback. What a coincidence..."
    play sound sfx_flashback_start
    scene cs_room with pixellate
    show cs_young with moveinbottom
    ycs "Hey guys, Young CS here! Today, I'm gonna be editing a \n{cshake}CraAaAaAaAzY{/bt} video!!"
    play sound sfx_keyboard
    n "CS taps furiously on his keyboard."
    ycs "Ohhhhhh {cshake}YeeEeeEeEeeEEeEEs!{/bt} This is lookin' {i}good!"
    play sound sfx_flashback_end
    hide cs_young
    scene cs_room
    show cs
    with pixellate
    pause 1.0
    show cs disappointed
    cs "Oh, flashback over."
    play sound sfx_foundationfail volume 0.5
    show cs worried
    show cs_room behind cs at rotate_10 with hpunch
    n "A loud crash is heard as CS' foundation splits beneath his feet!"
    show cs worried
    cs "Woah! I was dreaming for so long that the foundation fell apart. My house just fell to the side!"
    cs "I really need to get some foundation repair."
    menu:
        "Who you gonna call?"
        "HoH SiS":
            pass
        "Home Savers"(type="dx"):
            jump csbi_home_savers
    show cs
    cs "Better call HoH SiS!"
    cs "They're really good at giving me the JoJ!"
    show cs phone
    $ collect("cs_phone")
    n "CS dials 1-800-HoH-SiiS."
    play sound sfx_dial_hohsis
    pause 16
    
    # prevent dial tone overflow
    stop sound

    hoh_operator "Hello, and thank you for calling Home Sa--{w=0.5}{nw}"
    cs "Hello? Can you give me the JoJ?"
    hoh_operator "Is this another prank caller on the line?"
    show cs phone worried
    cs "No! My house really needs foundation repair! I need your help, ASAP!"
    hoh_operator "Alright. That will be 200,000 bits. You can pay us afterwards."
    play sound sfx_end_call
    n "The operator hangs up."
    show cs
    cs "Welp, that's one thing taken care of."
    cs "I guess I'll work on my new YTP while I wait."
    scene black with dissolve
    n "After some time, the doorbell rings."
    play sound sfx_doorbell volume 0.5
    stop music fadeout 3.0
    music end
    scene door_closed with dissolve
    show cs happy with moveinleft
    cs "Oh, they're here!"
    cs "Let me go get the door..."
    show cs at left with move
    play sound sfx_house_door_open
    show door_open behind cs with dissolve
    cs "Hello! I am CS, and I--"
    play music hohsis_theme volume 0.2 if_changed
    music hohsis_theme
    show ed at center:
        alpha 0.0
    with determination
    show ed at right:
        linear 2.5 alpha 1.0
    with MoveTransition(2)
    if fun_value(FUN_VALUE_MUSIC):
        ed "Alright, that will be one {i}Alfred Hitchcock{/i} intro theme."
        show cs disappointed
        cs "What?"
        show cs
    else:    
        ed "Alright, that will be 200,000 Bits."
    cs "Okay, I guess they already told you what I need done. Lemme get my wallet..."
    show cs flipped at mid_left_left with moveoutleft
    pause 1.0
    show cs disappointed flipped
    pause 0.5
    show cs disappointed
    cs "Hang on a sec! Didn't they say I could pay afterwards?"
    ed "Yeah, well, corporate policies just changed five seconds ago. Pay up."
    cs "Oh... alright..."
    show cs disappointed flipped with determination
    show cs disappointed flipped at offscreenleft with move
    show cs_wallet at offscreenleft with determination
    pause 2.0
    show cs at left 
    show cs_wallet at manual_pos(0.25, 0.6, 0.5):
        zoom 0.2
    with moveinleft
    $ collect("cs_wallet")
    pause 1.0
    cs "Here you go!"
    play sound sfx_moneyfalls
    show spent_bits at t_fake_rpg_text(0.075, 0.1, 0.5)
    pause 0.5
    hide cs_wallet with dissolve
    cs "I'll get out of your guys' hair while you work."
    if fun_value(FUN_VALUE_RARE):
        play sound sfx_gleam
        show gleam at manual_pos(0.8, 0.15, 0.5):
            zoom 0
            blur 5
            parallel:
                linear 0.25 zoom 2
            parallel:
                linear 0.5 rotate 360
            pass
            linear 0.5 alpha 0
        hide gleam with Dissolve(0.5)
        pause 0.25
        ed "..."
    show cs happy
    cs "See ya later!"
    show cs at mid_mid_left with moveoutright
    hide cs with dissolve
    pause 0.5
    n "CS leaves."
    pause 1.0
    ed "Come on in, guys. Coast is clear."
    show ed at right
    show wesley at center with dissolve
    show rich flipped at left with dissolve
    rich "It's about time!"
    show wesley flipped
    wesley "We can finally get our revenge!"
    ed "Yep! We have been laughed at on the internet for long enough!"
    ed "We'll show him what happens when you tarnish our good name!"
    pause 1.0
    "..."
    ed "But, now that we're here, what should we actually {i}do?"

    ed "Hmm..." (multiple = 3)
    wesley "Hmm..." (multiple = 3)
    rich "Hmm..." (multiple = 3)

    pause 2.0
    wesley "Let's go check this other room. We might get some ideas."
    show ed flipped with determination
    hide ed
    hide wesley
    hide rich
    with moveoutright
    scene black with dissolve
    pause 1.0
    scene cs_room_2 with dissolve
    show ed flipped at right
    show wesley flipped at center
    show rich flipped at left
    with moveinleft
    show ed with determination
    n "The three HoH SiS workers enter CS' bedroom."
    show wesley
    show rich
    wesley "Wow, I didn't know CS had a Union Jack!"
    rich "CS sure loves those Brits~!"
    show rich flipped
    show wesley flipped
    ed "Alright, boys. We didn't come here to admire the décor."
    ed "What should we do in here?"
    show wesley
    wesley "How about we burn down the house?"
    rich "Eh..."
    show wesley flipped
    ed "Are you insane?! {nw}" with vpunch
    extend "We are a {i}home repair company!{/i}"
    ed "We have a reputation to uphold!"
    wesley "{i}Do{/i} we? After all of those videos he put out making fun of us?"
    show wesley
    rich "Wait, I've got it!"
    rich "How about we mess with his laptop?"
    rich "That's what he used to {i}make{/i} those awful videos in the first place!"
    show wesley flipped
    ed "Now, {i}that's{/i} more like it! Rich, you're a genius!"
    ed "Let's get to sabotagin'!"
    scene craptop_bg
    show craptop desktop
    with dissolve
    n "Ed launches the craptop."
    play sound sfx_windows_logon
    ed "Heheh... He won't know what hit him."
    wesley "Quick! Let's get out of here before he comes back!"
    show craptop updating
    rich "Hurry up!"
    play sound sfx_bluescreen
    show craptop error with hpunch
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene cs_house with dissolve
    show ed at left
    show wesley at center
    show rich at right
    with moveinright
    rich "Lemme call our JoJ UFO!"

    ed "I'm beaming up!" (multiple = 3)
    wesley "I'm beaming up!" (multiple = 3)
    rich "I'm beaming up!" (multiple = 3)

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
    scene black with dissolve
    pause 2.0
    scene cs_street
    with dissolve
    show cs with moveinleft
    pause 3.0
    cs "Things sure are boooooring around here..."
    pause 1.0
    cs "Hey, I've got an idea!"
    show cs happy
    cs "Let's go to Michael Rosen's house!"
    hide cs with moveoutright
    scene black with dissolve
    pause 1.0
    jump csbi_michael_house

label csbi_michael_house:
    play sound sfx_doorslam
    scene car_inside
    show cs at left
    with dissolve
    play music canyon_car volume 0.2 if_changed
    music canyon
    cs "Thankfully, Michael lives pretty close."
    cs "His vacation home in the US is only a few streets away!"
    cs "I should probably call him first. I don't want to just show up unannounced!"
    show cs phone at left
    n "CS pulls out his phone and calls Michael."
    play sound sfx_dial_rosen
    pause 12.5

    # prevent dial tone overflow
    stop sound

    show rosen_abode at mid_offscreen_right
    show michael at right
    show rosen_phone at manual_pos(0.875, 0.625, 0.5):
        rotate -10
    with moveinright
    $ collect("rosen_phone")

    michael "Hello!"
    cs "Hey, Michael! How're you doin' today?"
    michael "I'm feeling rather noice today."
    show cs happy phone
    cs "That's good to hear! You mind if I head over to your place?"
    show cs phone
    cs "I'm having the JoJ done on my house, so I figured we can chat for a bit in the meantime."
    michael "Sure! I have a another guest visiting as well. He's bringing chocolate cake!"
    show cs happy phone
    cs "Mmm! That sounds delicious!"
    show cs phone flipped
    n "CS looks in the back seat of his car."
    cs "I have some Genergy with me, if you guys want some."
    michael "Sounds wonderful. I've never tried it, but I'm sure it's good."
    show cs happy phone
    cs "Alright, well, I'll be there soon!"
    michael "See you soon!"
    show cs at left
    hide rosen_abode
    hide rosen_phone
    hide michael
    with moveoutright
    play sound sfx_end_call
    n "CS puts his phone away and drives over to Michael's house."
    play sound sfx_driving volume 0.5
    pause 2.0
    show black with dissolve
    stop sound fadeout 2.0
    stop music fadeout 2.0
    pause 2.0
    jump csbi_rosen_house

label csbi_rosen_house:
    if e3:
        jump e3_rosen
    else:
        scene rosen_abode with dissolve
    play sound sfx_house_door_open
    pause 1.0
    play sound sfx_house_door_close
    play music super_friendly volume 0.4 if_changed
    music super_friendly
    show michael at right with moveinright
    show cs flipped at offscreenright
    if fun_value(FUN_VALUE_MUSIC):
        michael "Come in! Come in! I'm Super Friendly!"
    else:
        michael "Come in! Come in!"
    show michael at left
    show cs flipped at right
    with MoveTransition(1.0)
    cs "Hey, Michael!"
    michael "Sit down, make yourself comfy. I've got a new poem I'd like you to hear!"
    cs "Sure thing, enlighten me."
    michael "Right. This one is called{w=0.5} {i}The Library.{/i}"
    michael "There once was a man who would go on a grand adventure."
    michael "He would meet all sorts of friends, and flee from his enemies."
    show cs disappointed flipped
    michael "After his long adventure, he took a long nap."
    michael "When he woke up, he was in a {i}huge{/i} library."
    if e2:
        jump e2_rosen
    if e1:
        michael "He started to get up, and walk around."
        michael "While he was walking, he found a--{nw}"
        show black
    else:
        show cs concentrate flipped
        show black with dissolve
    pause 1.0
    play sound sfx_csnore
    pause 2.0
    michael "CS? Did you fall asleep?"
    michael "CS!"
    stop sound
    hide black
    show cs scared flipped with vpunch
    cs "Wha-- {i}What?"
    michael "Did you just... sleep through my {i}entire{/i} poem?"
    show cs worried flipped
    cs "Nooooooooooooooooo...?"
    n "Michael sighs and facepalms."
    play sound sfx_michael_facepalm
    show cs disappointed flipped
    pause 3.0
    play sound sfx_doorbell volume 0.5 
    n "The doorbell rings."
    michael "Oh! My other guest is here! Please excuse me for just one moment..."
    show cs flipped
    show michael at offscreenright with moveoutright
    show phil at offscreenright with determination
    pause 2.0
    show michael at left behind cs with MoveTransition(1.0)
    show phil at center behind cs with MoveTransition(1.0)
    pause 1.0
    phil "Phil Swift here!"
    michael "CS, meet my other friend, Phil!"
    cs "Oh, wow! I didn't know you were friends with Phil Swift!"
    michael "Well, it might be because he said he could make the best chocolate cake."
    michael "Speaking of which, Phil, do you have the cake?"
    phil "Here it is!"
    show flexcake at manual_pos(0.35, 0.6, 0.5) with dissolve
    $ collect("flexcake")
    phil "It even works {i}underwater!"
    michael "That's odd to mention, but... alright! Time to eat!"
    show cs worried flipped
    n "CS suddenly realizes what is going on."
    show cs scared flipped at right
    cs "Michael, wait!"
    cs "That's not chocolate cake!"
    play sound sfx_michael_eat
    michael "I have {i}loads{/i} to eat! Om nom nom..."
    pause 1.0
    play sound sfx_puke
    show flexcake at manual_pos(0.45, 1.1, 0.5):
        linear 1 rotate 80
    with MoveTransition(0.25)
    play sound2 sfx_plate_break noloop
    michael_nobeep "Blarrrgh!" with hpunch
    n "Michael spits out the Flex Cake."
    michael "This is {i}horrible!"
    michael "Get {i}out!{/i} Get out of here!"
    phil "But it seals, and bonds--{w=0.5}{nw}"
    michael "{i}OUT!" with hpunch
    hide phil with moveoutright
    show cs disappointed flipped at right
    pause 1.0
    play sound sfx_house_door_open
    pause 1.0
    play sound sfx_house_door_close
    pause 3.0
    michael "I need something to drink..."
    michael "CS, did you bring that drink?"
    show cs happy flipped
    cs "Sure did! Here you go!"
    show genergy at manual_pos(1400, 500) with dissolve
    show genergy at manual_pos(300, 500) with MoveTransition(0.5)
    pause 0.5
    michael "Goodness."
    n "Michael downs the whole can."
    play sound sfx_crack_open_cold_one
    pause 0.5
    show genergy at manual_pos(325,400) with MoveTransition(0.25):
        linear 0.25 rotate -50
    pause 0.5
    play sound sfx_mc_drink
    pause 3.0
    hide genergy with dissolve
    pause 2.0
    "..."
    pause 2.0
    show cs worried flipped
    michael "{i}Quick!{/i} Get out!" with vpunch
    cs "What's going on?"
    michael "The Genergyfoogle is here! It's come to eat us {i}all!"
    cs "Oh, man... did that Genergy have something {i}else{/i} in it?!"
    show cs scared flipped
    cs "I need to get out before he goes nuts!"
    show cs scared at offscreenright with MoveTransition(0.25)
    pause 1.0
    play sound sfx_house_door_open
    pause 1.0
    play sound sfx_house_door_close
    scene black with dissolve
    pause 1.0
    jump csbi_end

label csbi_end:
    scene car_inside
    show cs surprised at left
    with dissolve
    play music canyon_car volume 0.2 if_changed
    play sound sfx_driving volume 0.5
    $ achievement_manager.unlock("overcaffeinated")
    stop music fadeout 3.0
    music end
    pause 1.0
    cs "I should check on the HoH SiS folks. They should be making some progress by now."
    scene black with dissolve
    pause 1.0
    scene cs_room with dissolve
    stop sound fadeout 2.0
    play sound sfx_house_door_open
    pause 1.0
    play sound sfx_house_door_close
    pause 1.0
    show cs flipped at offscreenright with determination
    show cs flipped at center with moveinright
    n "CS returns home once again."
    pause 1.0
    show cs disappointed
    cs "What?! They're gone? Already?"
    cs "I guess I should get back to work on that YTP, then..."
    hide cs
    scene craptop_bg
    show craptop off
    with dissolve
    n "CS attempts to boot his laptop."
    n "..."
    n "Nothing."
    cs "Stupid craptop, turn {i}on!"
    n "CS tries to turn it on again.{w} Nothing."
    cs "Maybe it finally died..."
    "..."
    cs "Wait..."
    cs "The last people in this room were the HoH SiS guys!"
    cs "They must have done something to it!"
    show craptop_bg at rotate_6
    show craptop off at rotate_6
    with hpunch
    window hide
    play sound sfx_foundationfail volume 0.5
    pause 3.0
    cs "And, they didn't even do the JoJ!"
    show craptop sad at rotate_6 with hpunch
    play sound sfx_punch
    if fun_value(FUN_VALUE_RARE):
        play sound sfx_gul
    pause 1.0
    scene cs_room
    show cs angry
    with dissolve
    cs "I need to get those guys!"
    cs "I'm gonna go to HoH SiS HQ and kick some butt!"
    hide cs with moveoutright
    pause 0.5
    scene black with dissolve
    pause 2.0
    scene hoh_outside with dissolve
    window hide
    pause 2.0
    scene hoh_hq
    show cs angry
    with dissolve
    play music time_for_a_smackdown volume 0.2 if_changed
    music time_for_a_smackdown
    if fun_value(FUN_VALUE_MUSIC):
        cs "Alright! It's time for a Smackdown!"       
    else:    
        cs "Alright! Where are the head JoJites?!"
    show worker_1 at right with moveinright
    dxcom hohsisfight
    worker_1 "I don't know!!"
    $ persistent.seen.add("hoh_worker")
    cs "BullShisH!"
    n "CS punches the worker!"
    show cs angry at mid_right with MoveTransition(0.25)
    play sound sfx_punch
    with hpunch
    show worker_1 at offscreenright with MoveTransition(0.5):
        linear 0.25 xzoom -1
        linear 0.25 xzoom 1
    show cs angry at center with MoveTransition(0.5)
    show worker_2 at right with moveinright
    worker_2 "They-- They're on the roof!"
    cs "Good!"
    hide cs with moveoutright
    pause 0.5
    hide screen dxcom
    show black with dissolve
    scene hoh_hq2
    show worker_3 at mid_center_right
    show worker_4 at mid_left
    with dissolve
    show cs angry flipped with moveinright
    cs "Get out of my way!"
    n "CS bodyslams the workers as he runs past!"
    play sound sfx_punch
    show cs angry flipped at mid_left 
    show worker_4 at offscreenleft:
        linear 0.1 xzoom -1
        linear 0.1 xzoom 1
        linear 0.1 xzoom -1
        linear 0.1 xzoom 1
    with MoveTransition(0.25)
    with hpunch
    
    show cs angry with determination

    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        play sound sfx_punch
        show cs angry at right with MoveTransition(0.25)
        play sound2 sfx_spikes noloop
        show worker_3 at offscreenright:
            linear 0.5 rotate 360
        with MoveTransition(0.25)
        with hpunch

        show cs scared
        cs "Yeowch!"
        mean "{cshake}{size=+24}AUUUUUGH!!!" with hpunch
    else:
        play sound sfx_punch
        show cs angry at right with MoveTransition(0.25)
        show worker_3 at offscreenright:
            linear 0.5 rotate 360
        with MoveTransition(0.25)
        with hpunch

    show cs angry at offscreenright with MoveTransition(0.25)
    show black with dissolve
    scene hoh_hq3
    show worker_5 at left
    with dissolve
    show cs angry flipped at right with moveinright
    cs "Which way to the elevator?"
    cs "{i}Now!"
    worker_5 "Uhh... {nw}"
    hide worker_5
    show worker_5alt at left
    extend "that way!"
    cs "Thanks! And, also..."
    n "CS clocks the worker in the face!"
    show cs angry flipped at left
    with MoveTransition(0.25)
    play sound sfx_punch
    show worker_5alt at manual_pos(0, -1400) behind cs:
        linear 0.5 rotate 360
    with MoveTransition(0.5)
    show cs angry flipped at offscreenleft with MoveTransition(0.25)
    scene hoh_hq4 with dissolve
    show cs angry with moveinbottom
    pause 1.0
    cs "Which way to go..."

    menu:
        "Which way?"
        "Left":
            $ ch1_direction = "left"
            jump csbi_direction
        "Right":
            $ ch1_direction = "right"
            jump csbi_direction

# i have combined the two labels! please take note of this for future butterfly effect stuff! - tate
label csbi_direction:
    scene hoh_hq5

    if ch1_direction == "left":
        $ ch1_direction_sprite = 6
        $ ch1_direction_line = "A...{w=0.5} pineapple?"
    if ch1_direction == "right":
        $ ch1_direction_sprite = 7
        $ ch1_direction_line = "A fucking chicken?"

    show expression "worker_%s" % ch1_direction_sprite at right
    with dissolve
    show cs angry at left with moveinleft
    cs "[ch1_direction_line]"
    show cs angry at right 
    with MoveTransition(0.25)
    play sound sfx_punch
    show expression "worker_%s" % ch1_direction_sprite at offscreenright:
        linear 0.1 xzoom -1
        linear 0.1 xzoom 1
    with MoveTransition(0.25)
    with hpunch
    show cs angry at left with move
    $ achievement_manager.unlock("csbi")

    pause 1.0
    scene black with dissolve
    scene hoh_elevator
    show cs angry
    with dissolve
    pause 2.0
    play sound sfx_elevator_ding
    scene black with dissolve
    jump csbii_start

# needed to separate this into a new label for timeline progression - tate
label csbi_home_savers:
    show cs_room behind cs at rotate_10
    play music beautiful_hills volume 0.3 if_changed
    music beautiful_hills
    show cs
    cs "I guess I can call Home Savers. Despite my YTPs of their company, I don't think they'd mind helping me out."
    show cs phone
    $ collect("cs_phone")
    n "CS dials the phone number he found on their website."
    play sound sfx_dial_hohsis
    pause 16
    show cs phone at left with move
    show hoh_hq at mid_offscreen_right behind ed
    show ed phone at right
    with moveinright

    # prevent dial tone overflow
    stop sound

    ed "Hello, and thank you for calling Home Savers. This is Ed. How may I help you?"
    show cs worried phone
    cs "Hello, Ed! This is CS! My house feels like there is a rock on--{w=1.0}{nw}"
    cs "Um, I mean... my house is starting to tilt!"
    ed "Oh, man, {i}that{/i} doesn't sound good! What's your address? We can schedule a visit for this afternoon!"
    scene black with dissolve
    centered "A little while later..."
    pause 1.0
    play sound sfx_doorbell volume 0.5
    pause 1.0
    play sound sfx_house_door_open
    show cs_door_open at rotate_10
    show cs disappointed at left
    with dissolve
    pause 1.5
    show ed at center with dissolve
    ed "Hey, CS! Long time no see!"
    ed "Oh, wow, this is pretty bad! How long has it been like this?"
    show cs worried
    cs "I'm not sure! It's a pretty big house, so it must have happened so slowly that I only {i}just{/i} noticed!"
    show cs
    cs "By the way, it's nice to see you again!"
    ed "Hey, you too!"
    ed "I've been watching some of your new videos lately. They're always a hoot!"
    ed "I'm glad to see you're still going strong!"
    show cs happy
    cs "Thank you! I appreciate it."
    ed "Well, we'd better get to work. This foundation ain't gonna repair itself!"
    $ achievement_manager.unlock("savers")
    stop music fadeout 3.0
    music end
    scene black with Dissolve(3.0)
    $ ending_manager.mark("savers")
    $ renpy.movie_cutscene(hoh_repair)
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return

label csbi_nah:
    play music lets_hear_my_baby volume 0.15 if_changed
    music lets_hear_my_baby
    scene craptop_bg
    show craptop discord
    show cs disappointed at left
    n "CS thinks about starting the day, but even the thought of it exhausts him."
    scene cs_room
    show cs disappointed
    with dissolve
    cs "Y'know, I kinda just want a nap..."
    show cs disappointed
    cs "I don't really want to do anything {i}at all{/i} right now!"
    hide cs with moveoutright
    scene cs_room_2 with dissolve
    show cs at mid_left with moveinleft
    cs "Welp, time to do nothing today!"
    show cs happy
    cs "Hey guys, see ya!"
    $ achievement_manager.unlock("nah")
    scene black with dissolve
    pause 2.0
    $ ending_manager.mark("nah")
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return
