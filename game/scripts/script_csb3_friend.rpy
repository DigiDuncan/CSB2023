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
    cs "Uhmm… I literally just said--{nw}"
    linus "Alright! The plan is settled! You can go fetch me some more parts for the ultimate streaming machine, and you get to decide what parts should be in the computer!"
    cs "Okay but, are there any recommendations you would give me for building this? This is YOUR money, you know."
    linus "Nah, it's fine. I'm sure you will do well picking out parts, make sure to get the highest quality you can!"
    cs "Alrighty, I'll get going now."
    stop music fadeout 3.0
    music end
    scene microcenter with fade
    n "CS goes to Microcenter."
    show cs at left with moveinleft
    show cs happy
    cs "Okay gamers, we are buying some parts for our epic computing machine. Let's go inside the magical concrete structure to buy some computing parts."  # the fuck is this line Pakoo
    cs "Wow, this building looks a lot bigger than the places I would go shopping at near home."
    hide cs at right with moveoutright
    n "CS enters the building."
    scene microinside with fade
    show cs at left with moveinleft
    cs "Woah! This place is huge!"
    cs "There are so many options to pick from! And I have as much money as I'll ever need, too!"
    cs "Before I get too carried away though, I should probably start by buying the processor."
    hide cs at right with moveoutright
    scene cpuaisle with fade
    # TODO: [BG] CPU aisle
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
    cs "Whatever, I'll get this Intel i9."
    cs "Now for the GPU."
    hide cs with moveoutright
    scene gpuaisle with fade
    show cs at mid_left with moveinleft
    n "CS heads over to the GPU aisle."
    cs "Hmm, we got AMD and NVIDIA, I wish Linus told me which one I should get..."
    n "CS looks at his options."
    show cs at mid_right with move
    pause 2.0
    show cs flipped with determination
    show cs flipped at mid_left with move
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
        "GTX 760":
            jump low_gpu

label high_gpu:
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
    with determination
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
    linus "Alright well, we've already got quite a bit of views..."
    cs "Man! I wish I got this amount of average views!"
    cs "Look at the comments!"
    linus "Yeah I'm getting there."
    linus "Yeah, they seem to like your build!"
    cs "Yes!!"
    cs "Aw man, what are those people saying? NVIDIA sucks, you guys are cucks?"
    cs "Heyyy!!! No I'm not!"
    linus "Yeah, there are always people who get upset because of the brand we used. Don't worry, this always happens."
    show cs disappointed
    play music "<loop 0>yelling.ogg" loop volume 0.3
    cs "Hey, do you hear that?"
    n "CS and Linus can hear a growing audience of people yelling nearby."
    linus "Hold on, lemme go check the window."
    hide linus at offscreenright with moveoutright
    n "Linus heads over the window, and peers out to see a bunch of angry AMD fans rioting."
    linus "Oh shit, this is bad..."
    cs "What is it?"
    n "All of a sudden, a brick flies through the window!"
    play sound "<loop 0>glass.ogg" volume 3
    show sansbrick at offscreenleft with moveinright
    show cs worried
    cs "Woah! Stand back Linus!"
    show linus at center with moveinright
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
    cs "No!"
    linus "Huh?"
    show cs angry flipped
    cs "Actually, you know what? Leave this to me!"
    hide cs with moveoutleft
    n "CS runs out the front door into the crowd."
    linus "CS what are you doing? You gonna get yourself killed out there!"
    stop sound fadeout 3.0
    scene outside_ltt with fade
    play sound "<loop 0>yelling.ogg" loop volume 1
    show cs angry at center with dissolve
    "Fanboys" "Boo!! You suck! AMD is the best!"
    cs "Yeah well, let's see about that!"
    stop sound fadeout 3.0
    jump after_fanboy

label after_fanboy:
    scene outside_ltt
    show cs angry flipped at center
    with fade
    cs "*Huff Huff*"
    cs "That was exhilarating!"
    cs "That's right! The rest of you get out of here!"
    show arceus at right with moveinright
    arceus "CS! We need to--"
    arceus "What happened here?"
    show cs
    cs "Oh hey Arc. There were some angry fanboys complaining outside of LTT, so I fought them!"
    arceus "You fought them?"
    cs "Yeah! I won as well!"
    show linus at left with moveinleft
    linus "Woah hey, CS you alright?"
    cs "Yeah! I fought them and scared the rest away!"
    linus "Well shit! Good job CS!"
    linus "Hey I mean, if this happened again, would you be ready again to fight back?"
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
    arceus "Are you a cop? You better not be cop."
    show linus at center with vpunch
    linus "Heyyy! There you are!"
    linus "CS, this is the trainer we brought in today!"
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
    arceus "I still thought you were a cop."
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
    scene black with fade
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
    cs "Woohoo! I got all the targets!"
    pakoo "Nice job CS!"


label low_gpu:
    cs "I should probably try to save Linus some money. Most of the expensive parts he gets are from sponsors, he's not actually that rich."
    n "CS flags down an employee."
    show cashier at mid_right with moveinright
    cs "I'm trying to get a graphics card, and I want to save money, what do you have?"
    "Worker" "Everything here is pretty expensive, lemme check the back..."
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
    "Worker" "Hey I'm-- what are you doing?"
    show cs worried
    cs "Oops! Sorry!"
    cs "Anyways, what did you find?"
    "Worker" "I got this. It's pretty old, and it's covered in dust, but it's like $50."
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
