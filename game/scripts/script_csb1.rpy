screen best_music():
    layer "music"
    zorder 100
    image "best_music.png" at music_appear
    timer 5 action Hide('best_music')

label csbi_start:

    scene cs_room with fade
    show cs at center
    play music "<loop 0>lets_hear_my_baby.mp3" volume 0.15
    music "Let's hear my baby - Walkman"
    cs "Welp, time to start up the ol' Craptop."
    hide cs
    scene craptop_bg
    show craptop desktop
    show post_it at t_post_it
    craptop "Your PC sux. lol."
    sticky "Delete the CSCord."
    cs "Eh, maybe tomorrow."
    hide post_it
    play sound "page.wav" volume 5
    pause 2.0
    show craptop updating
    craptop "Downloading update 200/13..."
    craptop "Update complete."
    cs "OoOoOoOoO yes!"
    show craptop discord
    play sound "windows_logon.mp3"
    cs "Hey guys!"
    show discord at center_right
    play sound "ping_spam.mp3"
    discord "Hi! Hi! Hi! Hi!"
    n "The Discord is overflowing with people trying to talk to CS."
    hide discord
    show cs at left
    play sound "ping.mp3"
    cs "OK, bedtime! Bye guys!"
    show nova at right
    play sound "ping.mp3"
    nova "But it's like 8:04AM and you just woke up."
    play sound "ping.mp3"
    cs "Bye!"
    hide cs with moveoutleft
    show discord at center_left
    discord "CS is now offline."
    play sound "ping.mp3"
    nova "k bye"
    hide nova
    hide discord
    show craptop car
    cs "Time to watch car crash videos for the next couple of hours!"
    show black with fade
    n "Two hours later..."
    scene cs_room
    show cs
    cs "Okay... What to do now?"
    cs "I could go outside, look at some flowers.."
    show cs happy
    stop music fadeout 3.0
    music end
    cs "Yeah! Let's go outside!"
    scene cs_house
    show cs happy
    with fade
    play music "canyon.mp3" volume 0.2
    music CANYON.MID - George Stone
    cs "Nice day!"
    show cs
    cs "Well, I guess it's car time."
    show cs_car behind cs
    hide cs_house
    show cs at left with move
    show carguy at right with moveinright
    play sound "nicecar.ogg"
    carguy_nobeep "Nice car!"
    cs "It's pretty nice, but it's got some scratches..."
    play sound "notsonicescratch.ogg"
    carguy_nobeep "Nooot so nice scratch..."
    carguy "You should try Crotch Doctor!"
    show cs worried at left
    cs "OH GOD AN ADVERTISER!!!"
    stop music fadeout 3.0
    music end
    cs "QUICK START THE CAR START THE CAR!!!"
    hide cs with moveoutright
    hide carguy with dissolve
    play sound "doorslam.ogg"
    show black with dissolve
    show cs_car_inside behind cs
    play music "<loop 0>canyon_but_in_the_car.mp3" volume 0.2
    music CANYON.MID - George Stone
    cs "Whew.. That was close!"
    cs "Should I go get groceries?"
    menu:
        "Get groceries?"
        "Yes":
            cs "Yeah... It's a good idea to get some stuff."
        "No":
            cs "Screw you, I'm going anyway!"
    play sound "driving.wav" volume 0.5
    pause 3.0
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    jump walmart

label walmart:
    scene walmart_outside
    show cs happy
    cs "Oh yes! Walmart is open!"
    scene walmart_inside with fade
    show screen best_music
    $ _current_song = "Summer Clearance Sale"
    $ _current_artist = "BEST MUSIC"
    play music "<loop 0>summer_clearance_sale.mp3"
    n "CS walks inside."
    show doug at right with moveinright
    greeter "Hello and welcome to Walmart! Can I help you with anything?"
    show cs at left with moveinleft
    cs "Wow! It's Walmart CEO Doug McMillon! You actually work here?"
    doug "Of course! They were short a greeter today, so I filled in the slot!"
    cs "Wow! He seems like a good man!"
    hide doug with moveoutright
    show cs at center with move
    cs "Now. Lets find some food!"
    show walmart_aisle behind cs with dissolve
    cs "*pop* Noice! Genergy is 2 for $5! I'll take them all!"
    cs "Oooh! Pringles are on sale too! Yoink!"
    n "CS walks to checkout."
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
    hide cashier
    stop music fadeout 3.0
    music end
    show walmart_outside behind cs with dissolve
    cs "Let's get to the car."
    show carguy at right with moveinright
    play sound "notsonicescratch.ogg"
    carguy_nobeep "Nooooot so nice scratch."
    show cs disappointed at left
    cs "Not you again!"
    cs "I gotta get outta here!"
    hide cs with moveoutright
    hide carguy
    show black
    with fade
    play sound "doorslam.ogg"
    show car_inside with fade
    play music "<loop 0>canyon_but_in_the_car.mp3" volume 0.2
    play sound "driving.wav" volume 0.5
    cs "Let's get home before that guy doctors my crotch!"
    scene black with fade
    n "CS drives home and manages to avoid reenacting one of his favorite car crash videos."
    jump room

label room:
    scene cs_room
    stop sound fadeout 2.0
    stop music fadeout 3.0
    music end
    n "CS arrives home and walks to his room."
    show cs happy with dissolve
    cs "Ahhh. It's good to be home!"
    show cs
    cs "You know, I haven't put out a YTP in a while. I should work on one of my in-progress ones."
    scene craptop_bg
    show craptop edit
    with fade
    play music "<loop 0>scales_of_joy.mp3" volume 0.3
    music scales of joy.mod - Mel O Dee
    n "CS walks to his craptop and opens up Premiere."
    cs "Ooooh! Here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    n "CS watches the in-progress video."
    cs "This is pretty good, but I am feeling uninspired... I don't know where to go from here..."
    cs "Hmmm..."
    cs "I know! I should watch some other YTPs for inspiration."
    show craptop ytp
    n "CS opens up YouTube and begins watching YTPs. After a while, CS runs into some old YTPs."
    cs "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now..."
    cs "..."
    cs "Oh look a flashback. What a coincidence..."
    scene cs_room with pixellate
    show cs_young with moveinbottom
    ycs "Hey guys! Young CS here! Today I'm gonna be editing a craaaaAaAAaAAAAAaaAazy video!!"
    play sound "keyboard.ogg"
    n "keyboard tapping"
    ycs "Ohhhhhh YeeEeeEeEeeEEeEEs! This is lookin' good!"
    hide cs_young
    scene cs_room
    show cs
    with pixellate
    cs "Oh, flashback over."
    play sound "foundationfail.ogg" volume 0.5
    show cs_room behind cs at rotate_10 with hpunch
    n "A loud crash is heard as a crack is split in CS' foundation."
    show cs worried
    cs "Woah! I was dreaming so long that the foundation fell apart. My house just fell to the side!"
    cs "I really need to get some foundation repair."
    show cs
    cs "Better call HoH SiS!"
    cs "They are really good at giving me the JoJ!"
    cs "{i}dials 1-800-HoH-SiiS{/i}"
    cs "Hello? Can you give me the JoJ?"
    hoh_operator "Is this a prank caller on the line?"
    cs "No! My house really needs foundation repair! I need your help ASAP!!"
    hoh_operator "Alright. That will be 200,000 bits. You can pay us afterwards."
    hoh_operator "{i}hangs up{/i}"
    cs "Well that is one thing taken care of."
    cs "I guess I'll work on my new YTP while I wait."
    scene black with fade
    n "Time passes and the doorbell rings."
    play sound "doorbell.ogg" volume 0.5
    stop music fadeout 3.0
    music end
    scene door_closed with fade
    show cs happy with moveinbottom
    cs "Oh they're here!"
    cs "Let me go get the door.."
    show door_open behind cs
    cs "Hello! I am cs188 and I-"
    show cs at left with move
    show ed at right with moveinright
    play music "<loop 0>hohsis_theme.mp3" volume 0.2
    music Alfred Hitchcock Intro Theme - Charles Gounod
    ed "Alright that will be 200,000 Bits."
    cs "Okay, I guess they already told you what I need done.. Lemme get my wallet..."
    cs "Hang on a sec. Didn't they say I could pay afterwards?"
    ed "Yeah well, corporate policies just changed 5 seconds ago. Pay up."
    hide cs with moveoutleft
    n "A few moments later..."
    show cs at left with moveinleft
    cs "Here you go! I'll get out of you guys' hair while you work."
    hide cs with moveoutright
    n "CS leaves after paying 200,000 Bits."
    ed "Come on in, guys, CS left."
    show ed at left with move
    show wesley at center with moveinright
    show rich at right with moveinright
    ed "So now that we're here, what should we do to him?"
    "Ed, Wesley, and Richard" "Hmmm..."
    wesley "Let's go check his room. We might get some ideas."
    show cs_room_2 behind ed with dissolve
    n "The three HoH SiS workers go upstairs."
    wesley "Wow I didn't know CS had a Union Jack!"
    ed "CS sure loves those Brits~!"
    wesley "Alright, but now what should we do?"
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
    scene cs_house with fade
    show ed at left with moveinbottom
    show wesley at center with moveinbottom
    show rich at right with moveinbottom
    rich "Lemme call our JoJ UFO."
    "Ed, Wesley, and Richard" "I'm beaming up!"
    play sound "beam.ogg" volume 0.6
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
    show cs with moveinleft
    cs "Things sure are boooooring around here..."
    cs "Hey, I got an idea!"
    cs "Let's go to Michael Rosen's house!"
    show black with dissolve
    jump michael_house

label michael_house:
    scene car_inside
    play music "<loop 0>canyon_but_in_the_car.mp3" volume 0.2
    show cs at left
    cs "Thankfully, Michael lives pretty close."
    cs "His vacation house in the US is only a few streets away!"
    cs "Before I forget, I should probably call him first."
    show cs phone at left
    n "CS pulls out his phone and calls Michael."
    michael "Hello!"
    cs "Hey Michael! How you doin' today?"
    michael "I'm feeling rather noice today."
    cs "That's good to hear! You mind if I head over to your place?"
    cs "The JoJ is being done on my house, so I figured we can chat for a bit."
    michael "Sure! I have a another guest visiting as well, bringing chocolate cake."
    cs "Mmm! That sounds delicious!"
    n "CS looks in the back seat of his car."
    cs "I have some Genergy with me, if you guys want some."
    michael "Sounds wonderful. I've never tried it, but I'm sure it's good."
    cs "Alright well, I'll be there soon!"
    n "CS puts his phone away and drives over to Michael's house."
    play sound "driving.wav" volume 0.5
    pause 2.0
    show black with dissolve
    stop sound fadeout 2.0

    scene rosen_abode with fade
    play music "<loop 0>super_friendly.mp3" volume 0.4
    music Super Friendly - Kevin Macleod
    show michael at right with moveinright
    show cs flipped at offscreenright
    michael "Come in! Come in!"
    show michael at left
    show cs flipped at right
    with ease
    cs "Hey Michael!"
    michael "Sit down, make yourself comfy. I got a new poem I want to show you!"
    cs "Sure thing, enlighten me."
    michael "Right. This one is called:{w}{i}The Library.{/i}"
    michael "There once was a man who would go on a grand adventure."
    michael "He would meet all sorts of friends, and flee from his enemies."
    michael "After his long adventure, he took a long nap."
    michael "When he woke up, he was in a huge library."
    show black with dissolve
    play sound "csnore.ogg"
    michael "CS? did you fall asleep?"
    michael "CS!"
    stop sound
    hide black
    cs "Wha- what?"
    michael "Did you just... sleep through my entire poem?"
    cs "Nooooooooooooooooo?"
    n "Michael sighs and facepalms."
    play sound "doorbell.ogg" volume 0.5 
    n "The doorbell rings."
    michael "Oh! My other guest is here! I'll be right back!"
    hide michael at right with moveoutright
    show michael at left with moveinright
    show phil at center with moveinright
    phil "Phil Swift here!"
    michael "CS, meet my other friend, Phil!"
    cs "Oh wow! I didn't know you were friends with Phil Swift!"
    michael "Well, it might be because he said he could make the best chocolate cake."
    michael "Speaking of which, Phil, do you have the cake?"
    phil "Here it is! It even works underwater!"
    michael "That's odd to mention, but time to eat!"
    n "CS suddenly realizes what's going on."
    show cs worried flipped at right
    cs "Michael! That's not chocolate cake!"
    michael "I have loads to eat! Om nom nom..."
    play sound "puke.ogg"
    michael_nobeep "Blarrrgh!"
    n "Michael spits out the Flex Seal cake."
    michael "This is horrible! Get out! Get out of here!"
    phil "But it seals, and bonds--"
    michael "OUT!"
    hide phil with moveoutright
    hide cs
    show cs flipped at right
    michael "I need something to drink. CS, did you bring that drink?"
    cs "Sure thing, here you go."
    michael "Goodness."
    n "Michael downs the whole can."
    michael "Quick! Get out!"
    cs "What is going on?"
    michael "The Genergyfoogle is here! It's come to eat us all!"
    cs "Oh man, did that Genergy have something else in it...?"
    cs "I need to get out before he goes nuts!"
    hide cs with moveoutright
    show black with dissolve

    scene car_inside
    show cs at left
    with fade
    play music "<loop 0>canyon_but_in_the_car.mp3" volume 0.2
    play sound "driving.wav" volume 0.5
    stop music fadeout 3.0
    music end
    jump csbi_end

label csbi_end:
    cs "I should check on the HoH SiS folks. They should be making some progress by now."
    scene cs_room with fade
    show cs with moveinbottom
    stop sound fadeout 2.0
    n "CS walks into his room."
    show cs disappointed
    cs "What?! They're gone? Already?"
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
    window hide
    play sound "foundationfail.ogg" volume 0.5
    pause 3.0
    cs "They didn't even do the JoJ!"
    show craptop sad with hpunch
    play sound "audio/punch.ogg"
    pause 1.0
    scene cs_room
    show cs angry
    cs "I need to get those guys!"
    cs "I'm gonna go to HoH SiS HQ and kick some butt!"
    scene hoh_outside with fade
    window hide
    pause 1.0
    scene hoh_hq with dissolve
    play music "<loop 0>time_for_a_smackdown.mp3" volume 0.2
    music Time for a Smackdown! - Mr. Sauceman
    show cs angry with dissolve
    cs "Alright! Where are the head JoJites?!"
    show worker_1 at right with moveinright
    worker_1 "I don't know!!"
    cs "BullShisH!"
    n "CS punches the worker."
    play sound "audio/punch.ogg"
    show worker_1 at right with hpunch
    $ persistent.seen.add("hoh_worker")
    hide worker_1 with moveoutright
    show worker_2 at right with moveinright
    worker_2 "They--... They're on the roof!!"
    cs "Good!!"
    n "..."
    show black with dissolve
    scene hoh_hq2 with dissolve
    show worker_3 at mid_center_right
    show worker_4 at mid_left
    show cs angry with moveinleft
    cs "Get out of my way!"
    n "CS bodyslams the worker as he runs past."
    play sound "audio/punch.ogg"
    show cs angry at mid_right with move
    show worker_3 at mid_center_right with hpunch
    hide worker_3 with moveoutright
    play sound "audio/punch.ogg"
    show cs angry at mid_left with move
    show worker_4 at mid_left with hpunch
    hide worker_4 with moveoutleft
    show cs angry at center with move
    show black with dissolve
    scene hoh_hq3 with dissolve
    show worker_5 at left
    show cs angry at right with moveinright
    cs "Which way to the elevator? Now!"
    hide worker_5
    show worker_5alt at left
    worker_5 "Uhh, that way!"
    cs "Thanks, and also-"
    n "CS clocks the worker in the face."
    show cs angry at left with move
    play sound "audio/punch.ogg"
    show cs angry at right with move
    show worker_5alt at left with hpunch
    hide worker_5alt with moveoutbottom
    hide cs with moveoutright
    scene hoh_hq4 with dissolve
    show cs angry with moveinbottom
    cs "Which way to go..."

    menu:
        "Left":
            jump left
        "Right":
            jump right

label left:
    scene hoh_hq5
    show worker_6 at right
    with dissolve
    show cs angry at left with moveinleft
    cs "A... pineapple?"
    show cs angry at right with move
    play sound "audio/punch.ogg"
    show cs angry at left with move
    show worker_6 at right with hpunch
    hide worker_6 with moveoutright
    $ achievement_manager.unlock("HoH SiS's Most Wanted")
    show black with dissolve
    jump csbii_start

label right:
    scene hoh_hq5
    show worker_7 at right
    with dissolve
    show cs angry at left with moveinleft
    cs "A fucking chicken?"
    show cs angry at right with move
    play sound "audio/punch.ogg"
    show cs angry at left with move
    show worker_7 at right with hpunch
    hide worker_7 with moveoutright
    $ achievement_manager.unlock("HoH SiS's Most Wanted")
    show black with dissolve
    jump csbii_start
