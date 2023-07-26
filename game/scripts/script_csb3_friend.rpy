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
    cs "Hmm, we got AMD and NVIDIA, I wish Linus told me wish which one I should get..."
    n "CS looks at his options."
    show cs at mid_right with move
    pause 2.0
    show cs flipped with determination
    show cs flipped at mid_left with move
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

label low_gpu:
    cs "I should probably try to save Linus some money. Most of the expensive parts he gets are from sponsors, he's not actually that rich."
    n "CS flags down an employee."
    show cashier at mid_right with moveinright
    cs "I'm trying to get a graphics card, and I want to save money, what do you have?"
    "worker" "Everything here is pretty expensive, lemme check the back..."
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
    "worker" "Hey I'm-- what are you doing?"
    show cs worried
    cs "Oops! Sorry!"
    cs "Anyways, what did you find?"
    "worker" "I got this. It's pretty old, and it's covered in dust, but it's like $50."
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
