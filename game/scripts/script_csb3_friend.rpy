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
    cs "Hey, do you hear that?"
    n "CS and Linus can hear a growing audience of people yelling nearby."
    linus "Hold on, lemme go check the window."
    n "Linus heads over the window, and peers out to see a bunch of angry AMD fans rioting."
    linus "Oh shit, this is bad..."
    cs "What is it?"
    n "All of a sudden, a brick flies through the window!"
    cs "Woah! Stand back Linus!"
    linus "The AMD fans are rioting outside! We need to hide!"
    hide cs
    hide linus
    with moveoutleft
    scene black with fade
    n "CS and Linus meet up with the rest of the members downstairs."
    scene frontdoor
    show luke at left
    show taran at mid_left
    with fade
    show linus at center
    show cs at right
    with moveinright
    taran "What the fuck is happening?!"
    luke "Linus, how did you piss off so many people?"
    linus "Look, it never usually gets this bad!"
    luke "What are we gonna do?"
    taran "We could call the cops!"
    cs "No!"
    linus "Huh?"
    show cs angry
    cs "Actually, you know what? Leave this to me!"
    hide cs with moveoutleft
    n "CS runs out the front door into the crowd."
    linus "CS what are you doing? You gonna get yourself killed out there!"
    scene outside_ltt with fade
    show cs angry at center with dissolve
    "Fanboys" "Boo!! You suck! AMD is the best!"
    cs "Yeah well, let's see about that!"


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
