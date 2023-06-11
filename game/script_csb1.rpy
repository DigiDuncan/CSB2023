screen best_music():
    zorder 100
    image "best_music.png" at music_appear
    timer 5 action Hide('best_music')

label csbi_start:

    scene cs_room
    show cs_neutral
    play music "<loop 0>lets_hear_my_baby.mp3" volume 0.15
    music "Let's hear my baby - Walkman"
    cs "Welp, time to start up the ol' Craptop."
    hide cs_neutral
    scene craptop_bg
    show craptop_desktop
    show post_it at t_post_it
    craptop "Your PC sux. lol."
    sticky "Delete the CSCord."
    cs "Eh, maybe tomorrow."
    hide post_it
    play sound "page.wav" volume 5
    hide craptop_desktop
    show craptop_updating
    craptop "Downloading update 200/13..."
    craptop "Update complete."
    cs "OoOoOoOoO yes!"
    hide craptop_updating
    show craptop_discord
    play sound "windows_logon.mp3"
    cs "Hey guys!"
    show discord at center_right
    play sound "ping_spam.mp3"
    discord "Hi! Hi! Hi! Hi!"
    n "The Discord is overflowing with people trying to talk to CS."
    hide discord
    show cs_neutral at left
    play sound "ping.mp3"
    cs "OK, bedtime! Bye guys!"
    show nova at right
    play sound "ping.mp3"
    nova "But it's like 8:04AM and you just woke up."
    play sound "ping.mp3"
    cs "Bye!"
    hide cs_neutral with moveoutleft
    show discord at center_left
    discord "CS is now offline."
    play sound "ping.mp3"
    nova "k bye"
    hide nova
    hide discord
    hide craptop_discord
    show craptop_car
    cs "Time to watch car crash videos for the next couple of hours!"
    show black with fade
    n "Two hours later..."
    scene cs_room
    show cs_neutral
    cs "Okay... What to do now?"
    cs "I could go outside, look at some flowers.."
    show cs_room_2 behind cs_neutral
    hide cs_room
    cs "Oh! Look out the window! There's a Michael Rosen!"
    hide cs_neutral
    show cs_happy
    stop music fadeout 3.0
    cs "Yeah! Let's go outside!"
    scene cs_house
    play music "canyon.mp3" volume 0.2
    music CANYON.MID - George Stone
    show cs_happy
    cs "Nice day!"
    hide cs_happy
    show cs_neutral
    cs "Well, I guess it's car time."
    show cs_car behind cs_neutral
    hide cs_house
    show cs_neutral at left with move
    show carguy at right with moveinright
    play sound "nicecar.ogg"
    carguy "Nice car!"
    cs "It's pretty nice, but it's got some scratches..."
    carguy "Nooot so nice scratch..."
    carguy "You should try Crotch Doctor!"
    hide cs_neutral
    show cs_worried at left
    cs "OH GOD AN ADVERTISER!!!"
    stop music fadeout 3.0
    cs "QUICK START THE CAR START THE CAR!!!"
    hide cs_worried with moveoutright
    hide carguy with dissolve
    play sound "doorslam.ogg"
    show black with dissolve
    show cs_car_inside behind cs_neutral
    play music "<loop 0>canyon_but_in_the_car.mp3" volume 0.2
    cs "Whew.. That was close!"
    cs "Should I go get groceries?"
    menu:
        "Get groceries?"
        "Yes":
            cs "Yeah... It's a good idea to get some stuff."
        "No":
            cs "Screw you, I'm going anyway!"
    play audio "driving.wav"
    pause 3
    stop audio
    jump walmart

label walmart:
    scene walmart_outside
    show cs_happy
    cs "Oh yes! Walmart is open!"
    scene walmart_inside with fade
    show screen best_music
    play music "<loop 0>summer_clearance_sale.mp3"
    n "CS walks inside."
    show doug at right with moveinright
    greeter "Hello and welcome to Walmart! Can I help you with anything?"
    show cs_neutral at left with moveinleft
    cs "Wow! It's Walmart CEO Doug McMillon! You actually work here?"
    doug "Of course! They were short a greeter today, so I filled in the slot!"
    cs "Wow! He seems like a good man!"
    hide doug with moveoutright
    show cs_neutral at center with move
    cs "Now. Lets find some food!"
    show walmart_aisle behind cs_neutral with dissolve
    cs "*pop* Noice! Genergy is 2 for $5! I'll take them all!"
    cs "Oooh! Pringles are on sale too! Yoink!"
    n "CS walks to checkout."
    show walmart_register behind cs_neutral with dissolve
    show cs_neutral at left with move
    show cashier at right with dissolve
    cs "Here's my stuff!"
    cashier "That'll be $11.88."
    cs "Here you go!"
    cashier "Have a good day."
    cs "You too, bye!"
    hide cashier
    stop music fadeout 3.0
    show walmart_outside behind cs_neutral with dissolve
    cs "Let's get to the car."
    show carguy at right with moveinright
    carguy "Nooooot so nice scratch."
    hide cs_neutral
    show cs_disappointed at left
    cs "Not you again!"
    cs "I gotta get outta here!"
    hide cs_disappointed with moveoutright
    hide carguy with dissolve
    play sound "doorslam.ogg"
    show black with dissolve
    show car_inside behind cs_neutral
    play music "<loop 0>canyon_but_in_the_car.mp3" volume 0.2
    play audio "driving.wav"
    cs "Let's get home before that guy doctors my crotch!"
    scene black with fade
    n "CS drives home and manages to avoid reenacting one of his favorite car crash videos."
    jump room

label room:
    scene cs_room
    stop audio
    stop music fadeout 3.0
    n "CS arrives home and walks to his room."
    show cs_happy with dissolve
    cs "Ahhh. It's good to be home!"
    show cs_neutral
    hide cs_happy
    cs "You know, I haven't put out a YTP in a while. I should work on one of my in-progress ones."
    show craptop_bg
    show craptop_edit
    with fade
    n "CS walks to his craptop and opens up Premiere."
    play music "<loop 0>scales_of_joy.mp3" volume 0.3
    music scales of joy.mod - Mel O Dee
    cs "Ooooh! Here's the one from my last editing stream. People would be excited to finally see this as a finished product."
    n "CS watches the in-progress video."
    cs "This is pretty good, but I am feeling uninspired... I don't know where to go from here..."
    cs "Hmmm..."
    cs "I know! I should watch some other YTPs for inspiration."
    hide craptop_edit
    show craptop_ytp
    n "CS opens up YouTube and begins watching YTPs. After a while, CS runs into some old YTPs."
    cs "Man, it was so easy back then. All you needed was Windows Movie Maker and some effects. If only it was that easy now..."
    cs "..."
    cs "Oh look a flashback. What a coincidence..."
    scene cs_room with pixellate
    show cs_young with moveinbottom
    ycs "Hey guys! Young CS here! Today I'm gonna be editing a craaaaAaAAaAAAAAaaAazy video!!"
    n "keyboard tapping"
    ycs "Ohhhhhh YeeEeeEeEeeEEeEEs! This is lookin' good!"
    hide cs_young
    scene cs_room
    show cs_neutral
    with pixellate
    cs "Oh, flashback over."
    play sound "foundationfail.ogg" volume 0.5
    show cs_room behind cs_neutral at rotate_10 with hpunch
    n "A loud crash can be heard as though an atom has split in CS' foundation."
    cs "Woah! I was dreaming so long that the foundation fell apart. My house just fell to the side!"
    cs "I really need to get some foundation repair."
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
    scene door_closed with fade
    show cs_happy with moveinbottom
    cs "Oh they're here!"
    cs "Let me go get the door.."
    show door_open behind cs_happy
    cs "Hello! I am cs188 and I-"
    show cs_neutral
    hide cs_happy
    show cs_neutral at left with move
    show ed at right with moveinright
    play music "<loop 0>hohsis_theme.mp3" volume 0.2
    music Alfred Hitchcock Intro Theme - Charles Gounod
    ed "Alright that will be 200,000 Bits."
    cs "Okay, I guess they already told you what I need done.. Lemme get my wallet..."
    cs "Hang on a sec. Didn't they say I could pay afterwards?"
    ed "Yeah well, corporate policies just changed 5 seconds ago. Pay up."
    hide cs_neutral with moveoutleft
    n "A few moments later..."
    show cs_neutral at left with moveinleft
    cs "Here you go! I'll get out of you guys' hair while you work."
    hide cs_neutral with moveoutright
    n "CS leaves after paying 200,000 Bits."
    ed "Come on in, guys, CS left."
    show ed at left with move
    show wesley at center with moveinright
    show rich at right with moveinright
    ed "So now that we're here, what should we do to him?"
    "Ed, Wesley, and Richard" "Hmmm..."
    wesley "Let's go check his room. We might get some ideas."
    show cs_room behind ed with dissolve
    n "The three HoH SiS workers go upstairs."
    wesley "Wow I didn't know CS had a Union Jack!"
    ed "CS sure loves those Brits~!"
    wesley "Alright, but now what should we do?"
    ed "How about we burn down his house!"
    wesley "Eh..."
    rich "How about we mess with his laptop?"
    ed "Good idea! Let's get sabotagin'!"
    show craptop_bg
    show craptop_desktop
    with dissolve
    n "Ed launches the craptop."
    ed "Heheh... He won't know what hit him..."
    wesley "Quickly! Let's get out of here before he comes back!"
    hide craptop_desktop
    show craptop_updating
    wesley "Hurry up!"
    hide craptop_updating
    show craptop_error with hpunch
    pause 1.0
    scene cs_house with fade
    show ed at left with moveinbottom
    show wesley at center with moveinbottom
    show rich at right with moveinbottom
    rich "Lemme call our JoJ UFO."
    # TODO: [DIGI] Beaming up animation
    "Ed, Wesley, and Richard" "I'm beaming up!"
    hide ed
    hide wesley
    hide rich
    with moveouttop
    stop music fadeout 3.0
    scene cs_street
    show cs_neutral with moveinleft
    cs "Things sure are boooooring around here..."
    cs "Hey, I got an idea!"
    cs "Let's go to Michael Rosen's house!"
    show black with dissolve
    jump michael_house

label michael_house:
    scene car_inside
    show cs_neutral at left
    play audio "driving.wav"
    cs "Thankfully, Michael lives pretty close."
    cs "His vacation house in the US is only a few streets away!"
    cs "Before I forget, I should probably call him first."
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
    show black with dissolve
    stop audio

    scene rosen_abode
    play music "<loop 0>super_friendly.mp3" volume 0.4
    music Super Friendly - Kevin Macleod
    show michael at right with moveinright
    show cs_neutral at offscreenright
    michael "Come in! Come in!"
    show michael at left
    show cs_neutral at right
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
    hide cs_neutral
    show cs_worried at right
    cs "Michael! That's not chocolate cake!"
    michael "I have loads to eat! Om nom nom..."
    play sound "puke.ogg"
    michael "Blarrrgh!"
    n "Michael spits out the Flex Seal cake."
    michael "This is horrible! Get out! Get out of here!"
    phil "But it seals, and bonds--"
    michael "OUT!"
    hide phil with moveoutright
    hide cs_worried
    show cs_neutral at right
    michael "I need something to drink. CS, did you bring that drink?"
    cs "Sure thing, here you go."
    michael "Goodness."
    n "Michael downs the whole can."
    michael "Quick! Get out!"
    cs "What is going on?"
    michael "The Genergyfoogle is here! It's come to eat us all!"
    cs "Oh man, did that Genergy have something else in it...?"
    cs "I need to get out before he goes nuts!"
    hide cs_neutral with moveoutright
    show black with dissolve

    scene car_inside
    stop music fadeout 3.0
    show cs_neutral at left
    play audio "driving.wav"
    jump csbi_end

label csbi_end:
    cs "I should check on the HoH SiS folks. They should be making some progress by now."
    scene cs_room
    show cs_neutral with moveinbottom
    stop audio
    n "CS walks into his room."
    hide cs_neutral
    show cs_disappointed
    cs "What?! They're gone? Already?"
    hide cs_disappointed
    scene craptop_bg
    show craptop_off
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
    pause
    cs "They didn't even do the JoJ!"
    hide craptop_off
    show craptop_sad with hpunch
    play sound "audio/punch.ogg"
    pause
    scene cs_room
    show cs_angry
    cs "I need to get those guys!"
    cs "I'm gonna go to HoH SiS HQ and kick some butt!"
    scene hoh_outside with fade
    window hide
    pause
    scene hoh_hq with dissolve
    play music "<loop 0>time_for_a_smackdown.mp3" volume 0.2
    music Time for a Smackdown! - Tour De Pizza
    show cs_angry with dissolve
    cs "Alright! Where are the head JoJites?!"
    show worker_1 at right with moveinright
    worker_1 "I don't know!!"
    cs "BullShisH!"
    n "CS punches the worker."
    play sound "audio/punch.ogg"
    show worker_1 at right with hpunch
    hide worker_1 with moveoutright
    show worker_2 at right with moveinright
    worker_2 "They--... They're on the roof!!"
    cs "Good!!"
    n "..."
    show black with dissolve
    scene hoh_hq2
    show worker_3 at center_right
    show worker_4 at left
    show cs_angry with moveinleft
    cs "Get out of my way!"
    n "CS bodyslams the worker as he runs past."
    play sound "audio/punch.ogg"
    show worker_3 at center_right with hpunch
    play sound "audio/punch.ogg"
    show worker_4 at left with hpunch
    hide worker_3 with moveoutright
    hide worker_4 with moveoutleft
    show black with dissolve
    scene hoh_hq3
    show worker_5 at left
    show cs_angry at right with moveinright
    cs "Which way to the elevator? Now!"
    hide worker_5
    show worker_5alt at left
    worker_5 "Uhh, that way!"
    cs "Thanks, and also-"
    n "CS clocks the worker in the face."
    show cs_angry at left with move
    play sound "audio/punch.ogg"
    show cs_angry at right with move
    show worker_5alt at left with hpunch
    hide worker_5alt with moveoutbottom
    hide cs with moveoutright
    scene hoh_hq4 with fade
    show cs_angry with moveinbottom
    cs "Which way to go..."

    menu:
        "Left":
            jump left
        "Right":
            jump right

label left:
    scene hoh_hq5
    show worker_6 at right
    show cs_angry at left with moveinleft
    cs "A... pineapple?"
    show cs_angry at right with move
    play sound "audio/punch.ogg"
    show cs_angry at left with move
    show worker_6 at right with hpunch
    hide worker_6 with moveoutright
    show black with dissolve
    jump csbii_start

label right:
    scene hoh_hq5
    show worker_7 at right
    show cs_angry at left with moveinleft
    cs "A fucking chicken?"
    show cs_angry at right with move
    play sound "audio/punch.ogg"
    show cs_angry at left with move
    show worker_7 at right with hpunch
    hide worker_7 with moveoutright
    show black with dissolve
    jump csbii_start
