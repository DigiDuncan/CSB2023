label microcenter:
    cs "Sure, what parts do you need?"
    linus "We need eggs, milk..."
    linus "Just kidding."
    linus "I'll leave the details up to you since you've done a lot of live streaming, just get the highest end available."
    cs "Alright, I'll go get the parts."
    scene black with fade
    pause 3.0
    scene csdesk
    show linus at right
    with fade
    show cs at left with moveinleft
    cs "I have your new streaming PC, and it runs quite well too! Way better than my computer!"
    linus "Awesome! Lemme go move this into the othe--{w=0.25}WOAAAHHH!!!"
    show linus with hpunch
    n "Linus trips and falls, immediately destroying the insides and outsides of the PC that CS just built."
    cs "Oh damn, you okay there?"
    linus "No of course not! I just destroyed another one of these $20,000 computing machines! How the hell am I going to get another just like this?"
    cs "Well, you could just always buy more parts like these, I'm sure you have the budget for that."
    linus "No no, that's too expensive and wasteful, let me think..."
    linus "Hmmm..."
    linus "Wait! I just got a brilliant idea! Why don't you go buy more parts for me, we certainly have the budget to do that!"
    show cs disappointed
    cs "Uhmm… I literally just said--{nw}"
    linus "Alright! The plan is settled! You can go fetch me some more parts for the ultimate streaming machine, and you get to decide what parts should be in the computer!"
    show cs
    cs "Okay but, are there any recommendations you would give me for building this? This is YOUR money, you know."
    linus "Nah, it's fine. I'm sure you will do well picking out parts, make sure to get the highest quality you can!"
    cs "Alrighty, I'll get going now."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 2.0
    scene microcenter with fade
    n "CS goes to Microcenter."
    show cs at left with moveinleft
    show cs happy
    cs "Okay gamers, we are buying some parts for our epic computing machine. Let's go inside the magical concrete structure to buy some computing parts."  # the fuck is this line Pakoo
    cs "Wow, this building looks a lot bigger than the places I would go shopping at near home."
    hide cs at right with moveoutright
    n "CS enters the building."
    scene microinside with fade
    play music "<loop 0>morning_highway.mp3" loop volume 0.4
    music Morning Highway - BEST MUSIC
    show cs at left with moveinleft
    cs "Woah! This place is huge!"
    cs "There are so many options to pick from! And I have as much money as I'll ever need, too!"
    cs "Before I get too carried away though, I should probably start by buying the processor."
    hide cs at right with moveoutright
    scene cpuaisle with fade
    n "CS goes to the CPU aisle."
    show cs at mid_left with moveinleft
    cs "My goodness, there are so many options."
    show cs happy
    cs "I honestly don't know which one to pick."
    show cs
    cs "Let's see here…"
    cs "I could get a super high-end Intel CPU since Linus still seems to default to Intel even after shilling for AMD…"
    cs "Or I could get a Ryzen, more cores would probably be better for streaming..."
    show cs happy
    cs "Too many good options! I don't know what one to pick!"
    show cs
    if fun_value(40):
        cs "Whatever, I'll get this AMD Threadripper."        
    else:
        cs "Whatever, I'll get this Intel i9."
    cs "Now for the GPU."
    hide cs with moveoutright
    scene gpuaisle with fade
    show cs at mid_left with moveinleft
    n "CS heads over to the GPU aisle."
    cs "Hmm, we got AMD and NVIDIA, I wish Linus told me which one I should get..."
    n "CS looks at his options."
    hide cs with moveoutright
    scene gpuaisle2 with fade
    show cs at center with moveinleft
    pause 2.0
    show cs flipped with determination
    hide cs with moveoutleft
    scene gpuaisle with fade
    show cs flipped at mid_left with moveinright
    pause 1.0
    show cs with determination
    pause 2.0
    cs "Okay, we have a NVIDIA RTX 4080, and an AMD Radeon RX 7900."

    menu:
        "Which card do you want to choose?"
        "RTX 4080":
            $ fanboy_type = "amd"
            jump high_gpu
        "Radeon RX 7900":
            $ fanboy_type = "nvidia"
            jump high_gpu
        "GTX 760"  (type = "bad"):
            jump low_gpu

label high_gpu:
    if fanboy_type == "nvidia":
        cs "Alright, I'm just gonna get the Radeon RX 7900."
        cs "Linus likes to use AMD for streaming and gaming, so I hope this will work."
    else:
        cs "Alright, I'm just gonna get the RTX 4080."
        cs "I know NVIDIA pretty well, so I'm sure they're the best option to choose here."
    cs "Let's go check this out."
    hide cs with moveoutright
    n "CS heads out to the checkout."
    scene cashzone
    show cashier at mid_right 
    with fade
    show cs at mid_left with moveinleft
    cashier "That'll be $1188."
    cs "Welp, not my money!"
    cs "Awesome! Hopefully this is gonna be good enough for Linus!"
    hide cs with moveoutright
    stop music fadeout 3.0
    music end
    scene black with fade
    n "CS heads back to LTT."
    scene loffice
    show linus at center
    with fade
    n "CS meets Linus in his office."
    play music "<loop 0>creative_exercise.mp3" loop volume 0.3
    music Creative Exercise - Hirokazu Tanaka
    show cs at left with moveinleft
    cs "Hey Linus! I got your parts!"
    linus "Alright, let's see what you got!"
    show linus at mid_left_left with move
    pause 0.5
    show linus at center with move
    linus "Alright let's see what we got here..."
    linus "Nice, an Intel i9..."
    if fanboy_type == "nvidia":
        linus "Oh nice! A Radeon RX 7900! That's amazing!"
        show cs happy
        cs "Thanks man!"
        cs "I was hoping you'd like it, since you use AMD for gaming."
    else:
        linus "Ooh! A RTX 4080! Excellent choice CS!"
        show cs happy
        cs "Thank you!"
        show cs
        cs "I'm more of an NVIDIA guy myself, so I decided to go with it."
    linus "Well you made some great purchases, I'm excited to see the specs we'll get with this!"
    linus "I'm gonna go get the set ready, and then we can build and test it on camera."
    cs "Oh wow, already?"
    linus "Yeah, I'm excited! You can help me build it, right?"
    cs "Yeah, of course!"
    linus "Alright then, let's go!"
    hide linus
    hide cs
    with moveoutright
    scene black with fade
    n "CS and Linus head down to the recording room, while Linus sets up the cameras and equipment."
    scene ltt_bg
    show ltt_fg
    with fade
    show cs at t_cs_ltt behind ltt_fg with moveinleft
    linus "Alright, one second..."
    show linus at t_linus_ltt behind ltt_fg with moveinright
    linus "You ready CS?"
    cs "I don't think I've ever done a professional recording like this before..."
    linus "Relax! You can act normal here, and the editors can cut out anything that we need."
    cs "Okay."
    linus "3... 2... 1... Go."
    linus "Today, we are going to start-- {nw}"
    cs "Hey guys, CS here! How's it goin? Today we are going to build this CraAaAaAaAzY computer!"
    pause 1.0
    linus "Yeah. As I was going to say, we have our new employee, CS188 here, helping build a new streaming machine for LTT!"
    if fanboy_type == "nvidia":
        linus "CS picked out the parts, which were an Intel i9 and a Radeon RX 7900!"
        cs "Woohoo! Go AMD!"       
    else:
        linus "CS picked out the parts, which were an Intel i9 and a RTX 4080!"
        cs "Woohoo! NVIDIA is the best!"
    linus "Alright, let's put the computer together!"
    stop music fadeout 3.0
    music end
    scene black with fade
    n "CS and Linus then spend the next hour building and setting up the computer, showing off it's amazing capabilities."
    n "When they finish, they wrap up and Linus gives the footage to the editors."
    scene inside_ltt with fade
    show cs at left
    show linus at right
    with moveinleft
    show cs happy
    cs "That was really fun actually!"
    linus "Yeah! I'm glad that you could put together such a nice PC on your first day!"
    cs "Hell yeah!"
    linus "Well, that's it for today. When you come back tomorrow, we'll see what our audience thinks about it."
    cs "Alrighty well, I'm pumped! See you tomorrow!"
    hide cs with moveoutright
    hide linus with moveoutleft
    scene black with fade
    n "CS heads out back to the local hotel he's been staying at, already excited for the next day."
    n "As morning comes, CS heads back to LTT to check out the video."
    scene inside_ltt
    show linus at mid_right
    with fade
    show cs at mid_left with moveinleft
    linus "Hey CS!"
    cs "Hey Linus!"
    linus "Let's see how our video did!"
    n "Linus and CS sit down at the desk while Linus pulls open the video."
    scene comments with fade
    play music "<loop 0>pixel_peeker_polka.mp3" loop volume 0.4
    music Pixel Peeker Polka - Kevin MacLeod
    linus "Alright well, we've already got quite a bit of views..."
    cs "Man! I wish I got this amount of average views!"
    cs "Look at the comments!"
    linus "Yeah I'm getting there."
    linus "Yeah, they seem to like your build!"
    cs "Yes!!"
    if fanboy_type == "nvidia":
        cs "Aw man, what are those people saying? AMD blows, you guys are hoes?"        
    else:
        cs "Aw man, what are those people saying? NVIDIA sucks, you guys are cucks?"
    cs "Heyyy!!! No I'm not!"
    stop music fadeout 3.0
    music end
    linus "Yeah, there are always people who get upset because of the brand we used. Don't worry, this always happens."
    scene inside_ltt
    show linus at mid_right
    show cs disappointed at mid_left
    with fade
    play music "<loop 0>yelling.ogg" loop volume 0.3
    cs "Hey, do you hear that?"
    n "CS and Linus can hear a growing audience of people yelling nearby."
    linus "Hold on, lemme go check the window."
    hide linus at offscreenright with moveoutright
    if fanboy_type == "nvidia":
            n "Linus heads over the window, and peers out to see a bunch of angry NVIDIA fans rioting."
    else:
        n "Linus heads over the window, and peers out to see a bunch of angry AMD fans rioting."
    linus "Oh shit, this is bad..."
    cs "What is it?"
    n "All of a sudden, a brick flies through the window!"
    play sound "<loop 0>glass.ogg" volume 3
    show sansbrick at offscreenleft with moveinright
    show cs worried
    cs "Woah! Stand back Linus!"
    show linus at center with moveinright
    if fanboy_type == "nvidia":
        linus "The NVIDIA fans are rioting outside! We need to hide!"        
    else:
        linus "The AMD fans are rioting outside! We need to hide!"
    show cs flipped with determination
    hide cs
    hide linus
    with moveoutleft
    stop music fadeout 3.0
    scene black with fade
    n "CS and Linus meet up with the rest of the members downstairs."
    scene frontdoor
    play sound "<loop 0>yelling.ogg" loop volume 0.5
    show luke flipped at left
    show taran flipped at mid_left
    with fade
    show linus at center
    show cs flipped at right
    with moveinright
    taran "What the fuck is happening?!"
    luke "Linus, how did you piss off so many people?"
    linus "Look, it never usually gets this bad!"
    luke "What are we gonna do?"
    taran "We could call the cops!"
    show cs worried flipped
    cs "No!"
    linus "Huh?"
    menu:
        "Which card do you want to choose?"
        "Go out and fight!":
            jump attack_fanboy
        "Stay inside":
            jump stay_inside

label stay_inside:
    show cs disappointed flipped at right
    cs "Let's just, stay here."
    cs "They've got to go away at some point, right?"
    linus "I'm sure, I mean, we are LTT after all!"
    linus "We're so cool, our fans love us! They'll probably run home here in a moment."
    taran "Holy shit! They're throwing bricks!"
    play sound "<loop 0>glass.ogg" volume 3
    show sansbrick at offscreenright with moveinleft
    scene black
    stop sound
    jump knocked_out

label attack_fanboy:
    show cs angry flipped
    cs "Actually, you know what? Leave this to me!"
    hide cs with moveoutleft
    n "CS runs out the front door into the crowd."
    linus "CS what are you doing? You gonna get yourself killed out there!"
    stop sound fadeout 3.0
    scene outside_ltt with fade
    play sound "<loop 0>yelling.ogg" loop volume 1
    show cs angry at center with dissolve
    if fanboy_type == "nvidia":
        "Fanboys" "Boo!! You suck! NVIDIA is the best!"  
        cs "Yeah well, let's see about that!"
        stop sound fadeout 3.0
        music Nordic Report 2 - Lizardking
        jump rpg_fanboy_fight_nvidia     
    else:
        "Fanboys" "Boo!! You suck! AMD is the best!"
    cs "Yeah well, let's see about that!"
    stop sound fadeout 3.0
    music Nordic Report 1 - Lizardking
    jump rpg_fanboy_fight_amd

label after_fanboy:
    scene outside_ltt
    show cs angry flipped at center
    with fade
    $ achievement_manager.unlock("I Thought This Was A Visual Novel")
    n "CS struggles to catch his breath."
    if fanboy_type == "nvidia":
        $ achievement_manager.unlock("NVIDIA Flex")
    else:
        $ achievement_manager.unlock("The Threadripper")
    cs "That was exhilarating!"
    cs "That's right! The rest of you get out of here!"
    show arceus at right with moveinright
    arceus "CS! We need to--"
    show arceus worried
    arceus "What happened here?"
    show cs
    cs "Oh hey Arc. There were some angry fanboys complaining outside of LTT, so I fought them!"
    arceus "You fought them?"
    cs "Yeah! I won as well!"
    show arceus
    show linus at left with moveinleft
    linus "Woah hey, CS you alright?"
    cs "Yeah! I fought them and scared the rest away!"
    linus "Well shit! Good job CS!"
    linus "Hey I mean, if this happened again, would you be ready again to fight back?"
    if fanboy_type == "nvidia":
        cs "Umm, if they're NVIDIA fans, sure thing I guess."       
    else:
        cs "Umm, if they're AMD fans, sure thing I guess."
    linus "Great! I'll be right back."
    hide linus with moveoutleft
    show cs worried
    cs "Hey wait! What does that mean? What are you doing?"
    show cs
    arceus "CS? Do you have a minute?"
    cs "Looks like I do now, why?"
    arceus "We need to talk for a moment. Can we go somewhere private in the meantime?"
    cs "Sure I guess, yeah."
    show arceus flipped with determination
    hide cs
    hide arceus
    with moveoutright
    scene alley with fade
    play music "<loop 0>lowbudget_song.mp3" loop volume 0.4
    music Lowbudget Song - Dr. Awesome
    show arceus flipped at right
    show cs at center
    with moveinleft
    show arceus with determination
    arceus "Alright, hi."
    show cs disappointed
    cs "We could've just gone upstairs in the building?"
    arceus "Nah, I don't want anyone to hear us."
    show cs
    arceus "Okay so, we have a major problem."
    arceus "Remember when we escaped from that prison?"
    cs "How could I forget?"
    arceus "Well, the cops are still actively searching for us."
    arceus "Based off of the recent events that just happened here, they're probably gonna be here soon."
    show cs worried
    cs "Ah shit."
    cs "What am I gonna tell Linus? The cops are probably going to question him!"
    arceus "Yeah, I'm wondering how we are gonna get out of this."
    arceus "Let's just go inside and play it cool, maybe we'll think of something."
    show cs disappointed
    cs "Okay."
    show arceus
    show cs disappointed
    with determination
    show cs flipped with determination
    hide arceus
    hide cs
    with moveoutleft
    scene outside_ltt 
    show pakoo at right
    with fade
    show cs disappointed at left
    show arceus flipped at mid_left
    with moveinleft
    pakoo "Hey, what are you guys up to?"
    arceus "Nothing. We work at LTT, going back to our job."
    pakoo "Oh? Are you CS?"
    arceus "Uhh, no?"
    pakoo "Oh, Linus brought me here to--"
    show arceus flipped angry
    arceus "Are you a cop? You better not be cop."
    if fun_value(50):
        cs "Hey, aren't you the guy who made Petscop 2?"
        pakoo "Huh?"
    show arceus flipped
    show linus at center with vpunch
    linus "Heyyy! There you are!"
    linus "CS, this is the trainer we brought in today!"
    stop music fadeout 3.0
    music end
    linus "They're gonna help you learn how to use a gun and stuff like that in case we get rioters again!"
    show cs worried
    cs "Woah what? Don't you think weapons training is a bit overkill for this?"
    linus "Nahhh!"
    linus "We can even make a video about it, so others won't fuck with us!"
    show cs disappointed
    cs "Geez okay, if you're so sure."
    linus "Come on, let's get inside first."
    show pakoo flipped with determination
    hide cs
    hide arceus
    hide linus
    hide pakoo
    with moveoutright
    scene frontdoor with fade
    show cs at left
    show arceus flipped at mid_left
    show linus at right
    show pakoo flipped at mid_mid_right behind linus   
    with moveinleft
    show pakoo
    linus "Alright well, this is Pakoo, our weapons expert! They should be able to give you the proper weapons training you need!"
    cs "Oh, I see. That's Pakoo."
    cs "I didn't recognize you, but how come you didn't recognize me?"
    pakoo "Of course I knew who you were dummy, I was just messing with you!"
    show arceus flipped angry
    arceus "I still thought you were a cop."
    show arceus flipped
    linus "Alright well, we should show you guys the training course."
    show cs worried
    cs "A whole training course? At LTT?"
    show cs disappointed
    linus "Yeah, it's been a secret project that's been going on for a while now, just in case LTT gets taken over by our supposedly insane fanbase."
    show cs
    cs "Alright, well, let's go check this out."
    arceus "I'll just wait here for you guys to come back."
    show pakoo flipped with determination
    hide linus
    hide pakoo
    with moveoutright
    show cs at mid_right with move
    arceus "Hey CS?"
    show cs flipped with determination
    cs "Yeah?"
    arceus "If the cops are coming our way, I'll come down and let you know, but we'll just have to get going immediately, no exclamation to Linus."
    arceus "Got it?"
    cs "Yep! I'll see you soon!"
    show cs with determination
    hide cs with moveoutright
    scene black with fade
    n "CS, Linus, and Pakoo head down an elevator into the training facility."
    jump training

label training:
    scene testing_main with fade
    show linus at right
    show cs at center
    show pakoo flipped at left behind linus   
    with moveinleft
    play music "klaxon_beat.mp3" loop volume 0.6
    music Klaxon Beat - Kelly Bailey
    linus "Alright, here's our facility! What do you think?"
    cs "Oh wow! This looks like something from Quake!"
    pakoo "Close."
    linus "Follow me this way to the entrance for the course."
    cs "The course?"
    pakoo "Yeah, you gotta run through some exercises before you can use a gun!"
    show cs disappointed
    cs "Manual labor? Ugh..."
    linus "Alright, Hup Hup CS! Let's go!"
    hide linus
    hide cs
    hide pakoo
    with moveoutright
    scene testing_front with fade
    show linus at mid_left
    show cs disappointed at center
    show pakoo flipped at left behind linus    
    with moveinleft
    linus "Alright well, get going through the courses, and we'll watch from above and help you if you need anything."
    pakoo "Good luck CS! I'm sure you got this."
    hide linus
    hide pakoo
    with moveoutright
    cs "Alright..."
    cs "Here goes nothing."
    scene black with dissolve
    scene course_1 with fade
    show cs at left with moveinleft
    pakoo "Alright, just make your way through these blockades."
    cs "Just crouch under them and stuff?"
    pakoo "Yep!"
    show cs at mid_left with move
    hide cs at center with moveoutbottom
    show cs at mid_right with moveinbottom
    show cs at right with move
    show cs happy
    cs "Piece of cake!"
    pakoo "Alright, onto the next one."
    scene course_2 with fade
    show cs at left with moveinleft
    pakoo "Alright, you gotta jump across this pit."
    show cs disappointed
    cs "Really? This is a huge pit..."
    pakoo "Cmon, you got this!"

    menu:
        "Do a cool ass jump":
            jump cool_jump
        "Do a regular jump":
            jump reg_jump


label cool_jump:
    show cs
    cs "I got this guys, you watching?"
    pakoo "Yep!"
    show cs at t_punchup with move
    show cs at right with moveintop
    hide cs with moveoutbottom
    show cs at right with moveinbottom
    "Pakoo and Linus" "WOOAHH!!"
    show cs happy
    cs "Hell yeah! What did you guys think of that?"
    pakoo "That was impessive man!"
    linus "I never doubted you CS!"
    cs "Hey, maybe this training isn't too bad!"
    hide cs with moveoutright
    jump fire_range

label reg_jump:
    show cs
    cs "Alright, here goes nothing!"
    show cs at top with move
    show cs at right with move
    cs "Woohoo! I did it!"
    pakoo "Nice! Let's keep moving!"
    hide cs with moveoutright
    jump fire_range

label fire_range:
    scene course_3 with fade
    show cs at left with moveinleft
    pakoo "Alright, you picked up the rifle before you came into this room, right?"
    show m4 at left
    cs "Yep!"
    show cs angry
    cs "So do I just-- why won't it fire!!"
    show cs
    pakoo "Okay woah woah, calm down."
    pakoo "You gotta turn the safety off."
    pakoo "Be careful where you aim that as well."
    cs "Alright, I think I got this now."
    cs "Watch this!"
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks1.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks1.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks3.wav" volume 1
    pause 0.5
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks1.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks3.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination    
    pause 1.0
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks1.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks3.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination    
    pause 1.0
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks1.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks3.wav" volume 1
    show m4 at left with determination
    show m4 fire at left with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 at left with determination    
    pause 1.0
    show cs happy
    cs "Woohoo! I got all the targets!"
    pakoo "Nice job CS!"
    linus "That was excellent! You passed the course with flying colors!"
    pakoo "Head back to the main lobby, and we'll meet up with you there."
    cs "Alright, cya in a bit!"
    stop music fadeout 3.0
    music end
    hide m4
    show cs happy flipped with determination
    hide cs with moveoutleft
    scene testing_main with fade
    show cs flipped at mid_mid_left with moveinright
    show cs with determination
    pause 1.0
    show linus at mid_mid_right
    show pakoo at right
    with moveinright
    linus "Alrighty! Well Pakoo, what do you think? Do you think he's ready to become a guard for LTT?"
    pakoo "I would say so, yeah."
    cs "Awesome! This is gonna be like a real arena shooter!"
    show pakoo disappointed
    pakoo "...yeah."
    show pakoo
    pakoo "I think some more training should be done until he's a proper armed guard,"
    show pakoo worried
    pakoo "and this seems very... what's the right word..."
    show pakoo disappointed
    pakoo "Exaggerated?"
    linus "Whatttt? Look, I need this for my company."
    linus "There are just too many variables for what could happem, and I need some... protection for those variables!"
    show cs disappointed
    cs "Will I be able to work on editing ever? That's kinda what I signed up for in the first place, now that you mention this training stuff."
    show pakoo
    show cs
    linus "Sure! It's just--{w=0.5}{nw}"
    show arceus flipped at left with moveinleft
    play music "cp_violation.mp3" loop volume 0.6
    music CP Violation - Kelly Bailey
    arceus "Alright CS. We gotta go now."
    linus "Heyy! How'd you get down here?"
    show cs disappointed
    cs "Alright... I gotta go. This is important."
    linus "Yeah, and this is too! We gotta train more!"
    cs "Look I'll, explain later okay?"
    arceus "Alright, we're going CS!"
    arceus "C'mon!"
    cs "This is CS... signing out."
    show cs disappointed flipped
    show arceus
    with determination
    hide cs
    hide arceus
    with moveoutleft
    show linus at mid_left with move
    linus "Hey! Come back here!"
    show pakoo disappointed at center with move
    pakoo "Hey Linus?"
    linus "Yeah?"
    pakoo "Let me go with him. This is important for his job with you, and... I'm the reason why he's leaving."
    linus "What??"
    show pakoo worried
    pakoo "Yeah I... set up a plan with him in secret afterwards..."
    show pakoo
    pakoo "So that he would be more trained when he came back! To impress you!"
    show pakoo worried
    pakoo "Guess I went a little too hard with the scheduling though..."
    linus "Ahh, I see. I get it now."
    linus "I'll pretend like I didn't know, go help him."
    show pakoo
    pakoo "Alright sweet! Thank you Linus!"
    hide pakoo with moveoutleft
    pause 1.0
    linus "This is such a good idea! Pat yourself on the back, Linus."
    show black with dissolve
    show outside_ltt with fade
    show cs disappointed at center
    show arceus flipped at right
    with moveinleft
    cs "Welp, this kinda sucks."
    show arceus with determination
    arceus "What do you mean, man? You got proper firearms training!"
    show cs
    cs "Oh yeah!"
    cs "That reminds me..."
    show m4 at center
    pause 1.0
    cs "I took this with me too!"
    hide m4
    show arceus worried
    arceus "Holy shit! You took the rifle with you?"
    show arceus
    cs "Yeah, I don't know, it looked cool, and no one really saw me hiding it."
    cs "So y'know... free gun?"
    show arceus happy
    arceus "Hell yeah! We can use this!"
    cs "Yeah! To shoot mean people right?"
    show arceus angry
    arceus "Geez man, I was thinking to intimidate them!"
    cs "...I was also thinking that."
    show arceus
    show pakoo flipped at left with moveinleft
    pakoo "Hi!"
    show cs angry flipped
    window hide
    show m4
    show pakoo disappointed flipped
    cs "Hey I am armed!"
    cs "...and dangerous!"
    pakoo "Woah woah, put the gun down."
    pakoo "I'm gonna help you guys!"
    hide m4
    show cs disappointed flipped
    cs "Huh?"
    show arceus angry
    arceus "How are you gonna help us? Do you even know what is going on?"
    pakoo "Of course! The cops are chasing you, right?"
    arceus "I knew it! You are a cop!"
    pakoo "No-- dammit okay, listen to me for a second."
    pakoo "I've known for a while Copguy is chasing you down."
    pakoo "I've also known that Copguy has been working for 15 years, and you are his last criminal he wants to bust."
    pakoo "So he's gonna do anything to take you guys down."
    show arceus
    pakoo "Why do you think I showed up here? I know Copguy, and you're all over the place now!"
    pakoo "You made a video on a channel with like, millions of subscribers! What were you thinking?"
    cs "Shit, I never really thought about that."
    pakoo "Look, I just lied to Linus so he won't question this, so let me help you."
    arceus "CS? What do you say?"
    cs "I guess if you are willing to, you have more weapons right?"
    pakoo "Yeah I--{w=0.5}{nw}"
    show cs flipped
    cs "That's all I needed to hear!"
    show pakoo flipped
    pakoo "Yeah, I can help you a bit more along the way as well."
    pakoo "Where are we headed to?"
    arceus "Lemme think..."
    arceus "We don't really have a vehicle, and there is a car dealership a block from here..."
    arceus "Lemme scramble our location from the cops real quick, and then we should make it over there in a hurry and steal a car."
    pakoo "Alright!"
    cs "Hell yeah! Let's do this!"
    stop music fadeout 3.0
    music end
    scene black with fade
    n "Arceus takes one of the LTT laptops to scramble their location, and head off to the car dealer."
    scene canada_block with fade
    show pakoo at right
    show cs at center
    show arceus flipped at left
    with moveinleft
    arceus "We should be almost there, it should be around this corner."
    pakoo "Real quick before we get there, I should let Mika know what's going on today."
    cs "Who?"
    pakoo "Sorry, my boyfriend. I didn't really tell him that I'm helping two guys escape from the cops."
    show arceus worried flipped
    arceus "Fuuuuuck, I haven't told Kitty that I escaped from prison."
    show arceus flipped
    cs "I might tell Tate as well..."
    cs "You mind if we make some calls as well?"
    n "Pakoo pulls out a couple of phones from his back pocket and gives them to Arc and CS."
    show pakoo at center with move
    pause 1.0
    show pakoo at left with move
    pause 1.0
    show pakoo flipped with determination
    show pakoo flipped at right with move
    show pakoo with determination
    pakoo "I had these few spare with me, you guys should just keep them."
    pakoo "One may or may not be LTT property that I stole."
    scene black with fade
    n "The gang stops to call their friends and partners, and then makes their way to the dealership."
    scene dealership with fade
    show arceus flipped at center
    show cs at mid_mid_left
    show pakoo flipped at left behind cs
    with moveinleft
    arceus "Alright, here we are."
    cs "So we can pick any car we'd like?"
    arceus "Basically, yeah."
    show carguy at mid_right with moveinright
    play music "<loop 0>mm_complete.mp3" loop volume 0.6
    music Mm Complete - Matthew Simmonds
    carguy "Check out all these nice cars!"
    carguy "Nooooot so nice that you fellas don't have a car though."
    carguy "Wouldn't it be nice if having a car was this easy?"
    pakoo "Yeah, you know how expensive cars are these days?"
    carguy "Well, with my new real estate technology, you can! Welcome to Carguy's Deals!"
    arceus "I don't think that's new technolo-- {w=1.0}{nw}"
    carguy "Right this way, please!"
    cs "Sure, I guess."
    show carguy flipped with determination
    hide carguy with moveoutright
    hide pakoo
    hide cs
    hide arceus
    with moveoutright
    jump car_picker

label car_picker:
    stop sound
    scene dealer_cars with fade
    show carguy flipped at right
    show arceus flipped at center
    show cs at mid_left
    show pakoo flipped at left behind cs
    with moveinleft
    show carguy with determination
    carguy "Look at all these nice cars!"
    carguy "You guys look around, I'll be in the dealership building when you guys pick something you like."
    show carguy flipped with determination
    hide carguy with moveoutright
    pause 0.5
    show arceus flipped at mid_right
    show cs at center
    with move
    show arceus with determination
    arceus "Alright guys, pick out a car quick and let's get the hell outta here!"
    menu:
        "Pick a car!"
        "JoJ Charger":
            jump cool_car
        "Honda Civic":
            jump reg_car
        "Flintstones Car"  (type = "bad"):
            jump flint_car

label cool_car:
    $ nice_car = True
    cs "That's a nice car!"
    pakoo "That is a sick ass car."
    arceus "Damn. Are we taking it CS?"
    cs "Hell yeah! We can't just turn up a car as cool as this!"
    stop music fadeout 3.0
    music end
    scene joj_charger_fg
    show dealership behind joj_charger_fg
    with fade
    show cs at left with moveinleft
    show pakoo at right with moveinright
    pakoo "Punch it CS! We gotta get outta here!"
    play sound "siren.ogg" loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "As CS started up the car and began to drive off, the cops pull up around him."
    show cs disappointed
    show pakoo disappointed
    n "Copguy walks up next to the car."
    copguy "Nice car!"
    copguy "Noooot so nice that you walked right into my trap!"
    copguy "We've got you guys surrounded! Get out of the car now!"
    arceus "You guys ready?"
    "CS and Pakoo" "Yep. Let's do this."
    n "They all slowly step out of the car."
    scene dealership
    show blue_light at left
    show red_light at right
    show copguy flipped at left
    with fade
    show cs disappointed flipped at center
    show arceus at mid_mid_right
    show pakoo at right
    with moveinright
    copguy "Alright, put your hands in the air!"
    n "CS pulls out his rifle and fires a few shots in the air."
    show cs angry flipped
    show m4 flipped at center with determination
    show m4 fire flipped at center with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 flipped at center with determination 
    pause 0.5
    show m4 flipped at center with determination
    show m4 fire flipped at center with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 flipped at center with determination
    pause 0.5
    cs "Make me!"
    copguy "He's armed! Men, get in position and fire!"
    music Compulsion To Obey - Lizardking
    jump rpg_cop_fight_1

label reg_car:
    cs "Hey! I have a Honda Civic, let's just take that!"
    arceus "Works for me."
    pakoo "Let's go!"
    stop music fadeout 3.0
    music end
    scene car_inside_fg
    show dealership behind car_inside_fg
    with fade
    show cs at left with moveinleft
    show pakoo at right with moveinright
    pakoo "Punch it CS! We gotta get outta here!"
    play sound "siren.ogg" loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "As CS started up the car and began to drive off, the cops pull up around him."
    show cs disappointed
    show pakoo disappointed
    n "Copguy walks up next to the car."
    copguy "Looks like you walked right into my trap!"
    copguy "We've got you guys surrounded! Get out of the car now!"
    arceus "You guys ready?"
    "CS and Pakoo" "Yep. Let's do this."
    n "They all slowly step out of the car."
    scene dealership
    show blue_light at left
    show red_light at right
    show copguy flipped at left
    with fade
    show cs disappointed flipped at center
    show arceus at mid_mid_right
    show pakoo at right
    with moveinright
    copguy "Alright, put your hands in the air!"
    n "CS pulls out his rifle and fires a few shots in the air."
    show cs angry flipped
    show m4 flipped at center with determination
    show m4 fire flipped at center with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 flipped at center with determination 
    pause 0.5
    show m4 flipped at center with determination
    show m4 fire flipped at center with determination
    play sound "<loop 0>hks2.wav" volume 1
    show m4 flipped at center with determination
    pause 0.5
    cs "Make me!"
    copguy "He's armed! Men, get in position and fire!"
    music Compulsion To Obey - Lizardking
    jump rpg_cop_fight_1

label so_join:
    scene dealership
    show copguy flipped at left
    show cs disappointed flipped at center
    show arceus worried at mid_right
    show pakoo disappointed at right
    with fade
    n "After that intense fight, the cops seemed to best CS and co."
    n "CS is panting heavily."
    cs "Damnit..."
    pakoo "He's way too strong..."
    copguy "Is that all you guys got?"
    copguy "Or are you ready to finally admit your defeat?"
    tate "Waaaaaaaaaait!"
    show copguy
    copguy "Huh??"
    show tate srs at left with moveinleft
    show copguy with vpunch
    show tate srs at center
    show copguy at right
    show cs at offscreenright
    show arceus at offscreenright
    show pakoo at offscreenright
    with move
    show mika at mid_left
    show kitty at left
    $ persistent.seen.add("round")
    with moveinleft
    tate "That's right! Y'all gotta get through us first!"
    mika "Yeah! Fuck da police! (For legal reasons this is a joke)"
    kitty "Let's get them!"
    music For The People!- Lizardking
    jump rpg_cop_fight_2

label after_cop_fight:
    scene dealership
    show tate at mid_mid_left
    show mika at mid_left
    show kitty at left
    with fade
    tate "Yaaaaaaaay! We won!"
    tate "Hey, y'all good?"
    show cs flipped at mid_mid_right
    show arceus at mid_right
    show pakoo  at right
    with moveinright
    cs "Yeah, uhm..."
    cs "How are you doing?"
    show tate srs
    tate "I'm fine, but you're going to have to explain what the fuck is happening here."
    show cs disappointed flipped
    cs "Fuck."
    show tate
    if nice_car:
        tate "Also, nice car!"
        show cs happy flipped
        cs "Thanks!"
    else:
        show cs flipped
    show cs flipped
    mika "Pakoo, next time you are gonna fight people, let me know in advance!"
    show pakoo disappointed
    pakoo "I know I know, this just came up not to long ago!"
    if nice_car:
        mika "Dammn, nice car!"
        show pakoo happy
        pakoo "Thanks! I love this car."
    else:
        show pakoo
    if fun_value(5):
        show pakoo happy
    else:
        show pakoo
    kitty "Arcie.. This does not surprise me in the slightest."
    show arceus worried
    arceus "I mean, I {i}did{/i} say I was going to be in trouble with the law at some point in my life."
    if nice_car:
        kitty "Nice car!"
        show arceus happy
        arceus "Yeah!"
    else:
        arceus "Well, I know we just met up, but we should probably get going."
    show arceus
    tate "Alrighty then, we'll follow behind and keep watch."
    cs "Shit yeah, Copguys not dead, he's gonna probably call backup on us."
    pakoo "Let's start heading east."
    show cs
    show arceus flipped
    show pakoo flipped
    with determination
    hide cs
    hide arceus
    hide pakoo
    with moveoutright
    show kitty flipped
    show tate flipped
    with determination
    hide kitty
    hide mika
    hide tate
    with moveoutleft
    scene black with fade
    n "Both groups head out of the dealership, making haste from the cops."
    n "Meanwhile, Copguy heads back to the police station to call for help."
    scene sheriff_office
    play music "<loop 0>police_station.mp3" volume 0.5  
    music Police Station - Lorin Nelson  
    show sheriff at left
    with fade
    show copguy at mid_right with moveinright
    copguy "Hey Sheriff, I have some unfortunate news."
    sheriff "God damnit what is it this time?"
    copguy "Not only does CS have a group of allies, but he is armed to the teeth."
    copguy "He took down most of my men."
    sheriff "Ah hell... so this is really THAT bad isn't it..."
    sheriff "We're gonna need some backup."
    copguy "Yeah, I just came to ask about that."
    sheriff "Lemme call the National Guard, did you see where they were headed?"
    copguy "I think they were headed east, sir."
    sheriff "Alright. I'll call the Montana National Guard, we can probably block them off."
    copguy "Thank you so much. I will continue to track them down."
    sheriff "Good luck, Copguy."
    show copguy flipped with determination
    hide copguy with moveoutright
    scene black with dissolve
    window hide
    music end
    stop music fadeout 3.0
    pause 3.0
    jump dpn_call


label flint_car:
    stop music fadeout 3.0
    music end
    scene dealer_cars
    show arceus at mid_right
    show cs at center
    show pakoo flipped at left behind cs
    cs "Is that... the Flintstones car??"
    show arceus angry
    arceus "CS, please don't pick that car. It's probably just--{w=1.0}{nw}"
    cs "It's probably one of those cars that is really good, and they just try to make it look bad on the outside."
    cs "I wanna try it out!"
    arceus "This is an awful idea..."
    show arceus flipped with determination
    hide arceus
    hide cs
    hide pakoo
    with moveoutright
    scene flintcar_outside with fade
    show cs at mid_right
    show arceus flipped at mid_left
    show pakoo flipped at left
    with moveinleft
    show cs flipped with determination
    cs "Yep! This thing looks like the real deal!"
    show pakoo disappointed flipped with determination
    pakoo "You sure about this? You gotta use your feet to move, man."
    cs "Yes, I know how the Flintmobile works."
    scene flintcar_fg
    show dealership behind flintcar_fg
    with fade
    show cs at left with moveinleft
    show pakoo at right with moveinright
    cs "Alrighty, you all in?"
    "Pakoo and Arc" "Yeah."
    n "CS presses his feet against the pavement and struggles to move the car."
    show cs concentrate with hpunch
    cs "Hnnnnngg..."
    show cs disappointed
    cs "Shit."
    show pakoo disappointed
    play sound "siren.ogg" loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "Sirens blare in the dealership as Copguy pulls up to the car."
    copguy "Out of all the cars in my lot you decided to escape with, it was the Flintmobile?"
    copguy "That's kinda sad."
    bad_end "Fleenstones?" "car_picker"  
    

label low_gpu:
    cs "I should probably try to save Linus some money. Most of the expensive parts he gets are from sponsors, he's not actually that rich."
    n "CS flags down an employee."
    show cashier at mid_right with moveinright
    cs "I'm trying to get a graphics card, and I want to save money, what do you have?"
    worker "Everything here is pretty expensive, lemme check the back..."
    cs "Alright, I'll wait here."
    hide cashier with moveoutright
    pause 2.0
    cs "Dum Dee Dum..."
    cs "I'm gonna make some silly faces while I wait!"
    show cs disappointed with determination
    pause 1.0
    show cs angry with determination
    pause 1.0
    show cs concentrate with determination
    pause 1.0
    show cs worried with determination
    pause 1.0
    show cs happy with determination
    pause 1.0
    show cs concentrate with determination
    show cashier at mid_right with moveinright
    n "The worker comes back."
    worker "Hey I'm-- what are you doing?"
    show cs worried
    cs "Oops! Sorry!"
    cs "Anyways, what did you find?"
    worker "I got this. It's pretty old, and it's covered in dust, but it's like $50."
    cs "Sounds great, I'll take it."
    hide cs with moveoutright
    n "CS heads out to the checkout."
    scene cashzone 
    show cashier at mid_right
    with fade
    show cs at mid_left with moveinleft
    cashier "That'll be $50."
    cs "Good enough for me!"
    hide cs with moveoutright
    scene black with fade
    n "CS heads back to LTT."
    scene loffice
    show linus at center
    with fade
    n "CS meets Linus in his office."
    show cs at left with moveinleft
    cs "Hey Linus! I got your parts!"
    linus "Ooh goodie! Lemme see!"
    show linus at mid_left_left with move
    pause 0.5
    show linus at center with move
    linus "Alright let's see what we got here..."
    linus "Nice, an Intel i9..."
    linus "And a GTX..."
    linus "CS?"
    cs "Yeah?"
    linus "What the fuck is this shit?"
    show cs disappointed
    cs "What do you mean?"
    linus "Why did you pick this old ass graphics card?"
    linus "This is awful! We can't have a cool computer with this!"
    cs "Well, I know you probably didn't wanna me to spend too much, plus I had something similar to this once!"
    linus "I don't care about costs! I wanted a cool streaming computer and you failed!"
    linus "You're fired!"
    cs "W-W-What?"
    linus "Leave! I'll hire someone else who can make a better PC than you!"
    show cs angry
    cs "Fine!"
    show cs angry with vpunch
    hide cs with moveoutright
    n "CS stomps out of the building."
    scene black with fade
    jump new_plan
