label dx_christmas_start:
    play music lets_hear_winter volume 0.7 if_changed
    music lets_hear_winter
    scene cs_bedroom2 
    show cs at mid_left
    with dissolve
    n "CS wakes up to a snowy winter morning."
    cs "Oh yes! It snowed today!"
    show cs at mid_right with move
    n "CS looks at his calendar."
    show cs happy
    cs "Woohoo!"
    cs "Christmas is almost here!"
    show cs
    cs "...And you know what that means!"
    if fun_value(FUN_VALUE_COMMON):
        cs "Fish!"
    cs "I finally get to throw a huge Christmas party at my house!"
    show cs flipped
    cs "I'm so pumped, I should call everyone again to make sure they are coming."
    scene black with dissolve
    n "CS calls all of his guests who he invited a couple weeks ago."
    scene cs_bedroom1
    show cs at center
    with dissolve
    cs "Alright, well, the party is going to start in 2 days."
    show cs disappointed
    cs "I have not prepared at all."
    cs "Fuck."
    show cs
    cs "Okay, well first place I need to start is by checking out my house."
    show cs flipped
    cs "I have this huge mansion, and I don't even use the rest of my house!"
    cs "Let's go look."
    hide cs with moveoutleft
    n "CS walks into his living room."
    scene cs_living2
    show cs at center
    with dissolve
    cs "Well, okay maybe I should bring in the Christmas supplies first."
    cs "Let's go see what we have."
    n "CS goes into his garage."
    hide cs with moveoutright
    scene cs_garage
    show cs at mid_left
    with dissolve
    cs "Okay, okay, what should I get first..."
    menu:
        "Christmas tree":
            jump dx_christmas_tree
        "Lights and garland":
            jump dx_christmas_lights
        "Ornaments and decorations":
            jump dx_christmas_decor

# christmas tree
label dx_christmas_tree:
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if lights_first or decor_first:
        $ tree_second = True
        cs "Alright, time to get the Christmas tree!"
        n "CS drags the box out of the garage and brings it into his living room."
        n "CS goes back to the garage."
        if lights_first:
            menu:
                "Ornaments and decorations":
                    jump dx_christmas_decor
        if decor_first:
            menu:
                "Lights and garland":
                    jump dx_christmas_lights
        menu:
            "Lights and garland":
                jump dx_christmas_lights
            "Ornaments and decorations":
                jump dx_christmas_decor
    $ tree_first = True
    if tree_first:
        cs "I should get the Christmas tree first."
        show cs at mid_right with move
        cs "Who doesn't wanna get this thing out? This is the best part of decorating!"
        show cs disappointed
        cs "I just, need to be, careful..."
        show cs concentrate
        cs "Hnng..."
        n "All of a sudden, the shelf tips and all of the supplies fall onto CS!"
        show cs worried with hpunch
        play sound sfx_metalpipe
        cs "Shit!{w=1.0}{nw}"
        scene black with vpunch
        play sound2 sfx_lego_break noloop
        pause 1.0
        play sound sfx_cat_crash
        # crashing SFX
        scene cs_garage_mess
        show cs disappointed at mid_left
        with dissolve
        cs "Ow..."
        n "CS gets himself out of the mess of lights, garland, and Legos."
        # CS steps on a Lego.
        show cs disappointed at center with move
        show cs worried with hpunch
        cs "Fuck!"
        show cs disappointed flipped
        cs "Man, what a mess!"
        cs "This is gonna take forever to clean up!"
        hide cs with moveoutleft
    jump dx_christmas_anno


# Decorations/lights
label dx_christmas_lights:
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if tree_second or decor_first:
        cs "Alright, I should probably get the lights and garland next."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
        if tree_second:
            menu:
                "Ornaments and decorations":
                    jump dx_christmas_decor
        if decor_first:
            menu:
                "Christmas tree":
                    jump dx_christmas_tree
    $ lights_first = True
    if lights_first:
        cs "I should probably get the lights and garland first, they are in the easiest box for me to grab anyways."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
    menu:
        "Christmas tree":
            jump dx_christmas_tree
        "Ornaments and decorations":
            jump dx_christmas_decor

label dx_christmas_decor:
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if tree_second or lights_first:
        cs "Alright, I should probably get the decorations next."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
        if tree_second:
            menu:
                "Lights and garland":
                    jump dx_christmas_lights
        if lights_first:
            menu:
                "Christmas tree":
                    jump dx_christmas_tree
    $ decor_first = True
    if decor_first:
        cs "I'm gonna get the decorations first, I have a huge assortment of Legos in there!"
        n "CS gets the box inside, and then goes back to the garage to grab the next box."   
    menu:
        "Christmas tree":
            jump dx_christmas_tree
        "Lights and garland":
            jump dx_christmas_lights

label dx_christmas_before_anno:
    cs "Well that's all done!"
    cs "I have moved all of the Christmas supplies into the house!"
    cs "This is where the fun part begins!"
    jump dx_christmas_anno

label dx_christmas_anno:
    scene cs_foyer
    show cs at center
    with dissolve
    cs "Maybe I should call someone over to help."
    cs "Lemme see if Anno is around..."
    play sound sfx_ring_once
    n "CS decides to call Anno."
    show cs phone at mid_left with move
    show anno_house at mid_offscreen_right
    show anno at mid_right
    with moveinright
    anno "Hello?"
    cs "Hey Anno, CS here!"
    anno "Yes, I know the party is in two days, you just called me."
    cs "Well, I was wondering..."
    show cs happy phone
    cs "If you wanted to help me decorate my house!"
    show cs phone
    anno "I still have to get a gift for the gift exchange..."
    anno "...But I can do that tomorrow."
    anno "I'll come over. Be there soon."
    show cs happy phone
    cs "Cool!"
    hide anno_house
    hide anno
    with moveoutright
    show cs at center with move
    cs "Alright, I got Anno to come over and help out!"
    cs "I guess I'll just plan out how I want the house to look."
    show cs worried
    cs "Actually, shit, it snowed last night!"
    stop music fadeout 3.0
    music end
    cs "I need to shovel before Anno gets here!"
    hide cs with moveoutright
    n "CS gets dressed and goes out into the garage to get his shovel."
    if tree_first:
        scene cs_garage_mess with dissolve
        show cs disappointed at offscreenleft
        show cs disappointed at mid_mid_left with moveinleft
        show cs worried with hpunch
        cs "Shit! I hate Legos, but only when they're in my feet!"
    else:
        scene cs_garage with dissolve
        show cs at mid_mid_left with moveinleft
    show cs
    cs "Okay, now the real question is, how much did it snow?"
    show cs disappointed
    n "CS presses the garage button, and nothing happens."
    cs "Dammit, I think it's iced shut."
    cs "I'm gonna have to go out in front."
    show cs disappointed flipped with determination
    hide cs with moveoutleft
    scene cs_house_snowed_in
    show cs disappointed flipped at right
    with dissolve
    play music snowy
    music snowy
    n "When CS gets outside, he finds a massive snow drift blocking his garage."
    cs "Well that's just great."
    cs "This is gonna take an hour at least to scoop up."
    cs "I better get to it, I guess."
    n "As CS is about 10 minutes into shoveling, CS hears someone walking up his driveway."
    show carguy flipped at left with moveinleft
    carguy "Nice snow!"
    carguy "Nooot so nice driveway."
    cs "Look man, I'm trying. It's cold as balls out here."
    carguy "Speaking of balls, you need some help?"
    carguy "I got something you might need!"
    carguy "Crotch Doctor's \"Scratch My Balls\" technology doesn't just help removing shit from your car, it also instantly melts snow!"
    carguy "Watch!"
    n "Carguy unscrews the bottle of Crotch Doctor, and tips it upside down."
    n "A single drop falls into the snow, leaving one small hole."
    cs "Umm..."
    carguy "Hold on, it's just..."
    n "Carguy vigorously shakes the empty bottle."
    carguy "{i}I thought I had more of this...{/i}" 
    carguy "Welp, sorry! Looks like I ran out!"
    show carguy with determination
    hide carguy with easeoutleft
    n "Carguy turns and trots away though the snow as fast as he can go."
    show cs angry flipped
    cs "Well that was a huge waste of time!"
    cs "I really need to finish shoveling my driveway, my face is starting to freeze!"
    scene cs_house_snow
    show cs flipped at center
    with dissolve
    n "As CS finishes scooping up the driveway, Anno's car pulls up on his street."
    cs "Just in time!"
    n "CS greets Anno as he pulls up on his driveway."
    show anno at left with moveinleft
    anno "Hey, how's it going?"
    show cs disappointed flipped
    cs "Cold. Very cold."
    show cs disappointed
    cs "Let's get inside please it's freezing."
    hide cs
    hide anno
    with moveoutright
    n "CS and Anno huddle inside and take their jackets off, while they make their way into the living room."
    scene cs_living2
    show cs at left
    show anno at right
    with dissolve
    n "They sit on the couch and catch up with each other while they get warmed up."
    anno "Well CS, how have you been doing?"
    show cs happy
    cs "Good! Still rockin' that Kurt Cobain look?"
    anno "Pfft, you thought I would get rid of it?"
    show cs
    cs "I've enjoyed not being chased by the cops again and just living a roughly normal life."
    anno "Yeah, how was your trip back home after all that? We haven't really talked much since then."
    show cs disappointed
    cs "Well, I had a blast working for LTT for a few days, but eventually I had to escape again because the cops came after us."
    show cs
    cs "I eventually proved to the cops that I wasn't guilty, and then Billy Mays took us home."
    anno "How the hell did you manage to come across Billy Mays?"
    show cs happy
    cs "Crazy coincidence I guess, but it was fun though! I won a golden pencil sharpener!"
    show cs
    anno "The cops never came after me, so I tried to start up a band, but it didn't really work out."
    #Christmas tree first
    if tree_first:
        anno "By the way, where are all of the decorations?"
        cs "Ah yes, it's all in the garage. I'll show you."
        n "Anno follows CS to his garage."
        hide cs with moveoutright
        hide anno with moveoutright
        scene cs_garage_mess with dissolve
        show cs at center
        show anno at left
        with moveinleft
        n "As they enter the garage, Anno gawks at the mess on the floor."
        anno "Damn bitch, you live like this?"
        cs "...I may have had small mishap when I was trying to get the tree out."
        anno "Small?!"
        show cs disappointed flipped
        cs "Do you think you can help me?"
        show cs disappointed
        cs "I figured it'd be faster if I had a helping hand."
        n "Anno groans."
        anno "I was hoping to be setting up decorations, not cleaning them up."
        anno "...But I guess I don't really have any other option, do I?"
        cs "Here, I'll grab these boxes, and we'll start throwing stuff in them."
        scene black with dissolve
        n "After about an hour, they manage to clean up the mess, without stepping on too many Legos."
        n "CS and Anno drag the boxes inside."
    #Setting up decorations
label dx_christmas_setup:
    stop music fadeout 3.0
    music end
    scene cs_living2
    show cs at left
    show anno at right
    with dissolve
    cs "Well Anno, are you ready to start decorating this place?"
    anno "Yeah! Where do you wanna start?"
    n "Insert decorating scene here."
    # TODO: Decorating scene
    #Living room
    #Kitchen
    #Hallway
    #Entrance
    #Outside
    #After
    cs "Thanks Anno! You really rizzed up my crib!"

    #Day 2
label dx_christmas_before_shopping:
    scene cs_bedroom2
    show cs at mid_left
    with dissolve
    n "After a good night's sleep, CS slowly wakes up to read the time."
    show cs at mid_right with move
    cs "Huh?"
    show cs worried with hpunch
    cs "Oh shit! It's 2pm already?"
    cs "I should go get all my shopping done!"
    show cs worried flipped
    n "CS jolts out of his room and gets ready for the day."
    hide cs with easeoutleft
    scene cs_house_snow
    show cs flipped at mid_right
    with dissolve
    cs "Thankfully it didn't snow anymore, otherwise my car would have been snowed in!"
    hide cs with moveoutleft
    n "CS gets in his car and figures out where to go."
    scene cs_car_inside
    show cs at left
    with dissolve
    cs "I went to Walmart last time because they had a deal, but I never shop there regularly."
    cs "To Target we go!"
    n "CS starts up his car and heads to Target."
    scene tgt_inside
    show cs at center
    with dissolve
    play sound sfx_hubbub loop volume 0.2
    show cs happy
    cs "Now this is a real store!"
    show cs
    cs "Everything is mostly clean and neat, no depressing lighting and messy aisles..."
    cs "I should probably stop praising the store and actually buy the groceries I need."
    hide cs with moveoutright
    #Shopping
    n "CS heads over to the grocery aisles."
    scene tgt_shelf with dissolve
    show cs at left with moveinleft
    cs "Well I need to get some Genergy, of course."
    # TODO: Add more shopping
    hide cs with moveoutright
    #Checkout
label dx_christmas_checkout:
    n "CS heads over to the checkout lanes."
    scene tgt_line
    show streetguy flipped at mid_right_right
    show amtrak_stewardess at mid_right
    show snufkin flipped at mid_mid_right
    show customer at center
    with dissolve
    show cs at left with moveinleft
    pause 1.0
    show cs disappointed
    cs "Wait, what?"
    show cs angry
    cs "There are no lanes open! How the hell am I supposed to check out?"
    show cs disappointed
    cs "Oh wait, I guess self-checkout is open..."
    show cs disappointed at mid_mid_left with move
    n "CS gets in the long line wrapped around the self-check area."
    cs "Man, this place is really short staffed, especially for the holidays!"
    show customer flipped
    customer "They're always like this. I come every day, and they definitely have been losing employees."
    show customer
    cs "Yikes, I wonder why..."
    hide streetguy with moveoutright
    show amtrak_stewardess at mid_right_right
    show snufkin flipped at mid_right
    show customer at mid_mid_right
    with move
    show cs at center with move
    pause 2.0
    hide amtrak_stewardess with moveoutright
    show snufkin flipped at mid_right_right
    show customer at mid_right
    with move
    show cs at mid_mid_right with move
    pause 2.0
    hide snufkin flipped with moveoutright
    show customer at mid_right_right with move
    show cs at mid_right with move
    pause 3.0
    hide customer with moveoutright
    show cs at mid_right_right with move
    pause 2.0
    cs "Finally, I can checkout."
    scene tgt_checkerror with dissolve
    show cs at left with moveinleft
    n "CS sees an message on the machine."
    cs "Welp, can't use that one!"
    hide cs with moveoutright
    n "CS goes to the next machine."
    scene tgt_checkout with dissolve
    show cs at left with moveinleft
    n "As CS is checking out, the machine beeps at him."
    show cs worried
    cs "What? I scanned this twice? No I didn't!"
    # TODO: Pakoo needs to greenscreen themselves
    show cs disappointed
    show tgt_worker at mid_right with moveinright
    tgt_worker "Oh yeah, it always does that, keep going."
    show cs
    cs "Okay."
    hide tgt_worker with moveoutright
    show cs disappointed
    cs "Ah crap, I scanned this one too many times."
    n "The worker comes back."
    show tgt_worker at mid_right with moveinright
    tgt_worker "Hello, what's wrong?"
    show cs
    cs "Sorry, I scanned this pie 7 times."
    tgt_worker "...how many do you have?"
    cs "I have 2."
    tgt_worker "Wh-- okay hold on."
    show tgt_worker at center with move
    pause 3.0
    show tgt_worker at mid_right with move
    tgt_worker "There you go."
    cs "Thanks!"
    hide tgt_worker with moveoutright
    show cs angry
    cs "Hey wait a minute!"
    show tgt_worker at mid_right with moveinright
    n "The target employee runs back over."
    cs "These are ringing up 11.99 per pie!"
    cs "They said they were like 20-percent off on the sign over there!"
    tgt_worker "Hmm..."
    n "The employee scans the pie."
    show cs disappointed
    tgt_worker "Do you perchance have Target Circle?"
    cs "No?"
    tgt_worker "You need Target Circle to get this deal. Sorry."
    show cs angry
    cs "Really?"
    tgt_worker "I'm sorry, but that's just how the deal works."
    show cs disappointed
    cs "Fine, whatever, I'll just keep them."
    hide tgt_worker with moveoutright
    n "When CS goes to scan his alcohol, it beeps again and tells him to get out his ID."
    show cs pissed
    cs "Seriously?!"
    show cs angry
    n "The employee runs over again."
    show tgt_worker at mid_right with moveinright
    tgt_worker "Oh yeah. I should probably do that for you."
    show tgt_worker at center with move
    n "The employee signs into the machine and opens the prompt to enter an ID."
    n "They then wait patiently for CS."
    cs "What? Do you need something from me?"
    tgt_worker "Yeah, I need to check your ID."
    show cs pissed
    cs "Are you kidding me?"
    tgt_worker "Yes, they will kill me if you don't do it."
    show cs disappointed
    n "CS sighs."
    cs "Here you go."
    n "The target employee punches in his birthday and leaves."
    hide tgt_worker with moveoutright
    pause 3.0
    hide cs with moveoutright
    stop sound fadeout 3.0
    scene tgt_outside
    show cs disappointed
    with dissolve
    cs "Kids these days, asking me for my ID..."
    cs "They should hire some new people!"
    show cs
    cs "Anyways, I need to get home now and put everything away."
    show cs happy
    cs "It's the big day tomorrow, and it's gonna be the best party ever!"
    hide cs with moveoutright
label dx_christmas_aftershop:
    scene cs_kitchen
    show cs_kitchen_fg
    with dissolve
    show cs flipped at mid_right behind cs_kitchen_fg with moveinright
    n "When CS gets home, he starts putting the groceries away."
    show cs flipped at center behind cs_kitchen_fg with move
    n "As he's finishing up, a D20 he had sitting on the counter gets knocked onto the floor."
    show cs disappointed behind cs_kitchen_fg
    cs "What the hell? When did I ever have one of these?"
    n "CS picks up the die."
    show cs behind cs_kitchen_fg
    cs "Hey, I got a [d20]!"
label dx_christmas_party_before:
    scene cs_bedroom2
    show cs happy
    with dissolve
    cs "Today is the day!"
    cs "Now I just have to wait for people to arrive!"
    show cs flipped
    cs "I wonder who will arrive first?"
    if d20 == 1:
        n "CS waits paiently."
        n "He keeps on waiting."
        show cs disappointed flipped
        cs "Alright, any minute now..."
        cs "The party starts here in about 15 minutes, so people should start showing up soon..."
        n "CS keeps on waiting, but it looks like no one shows up early."
        jump dx_christmas_intro      
    if d20 == 2:
        n "As CS asks himself this, a small car pulls up in the driveway."
        cs "Hmm, let go see who that is!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show arceus flipped at mid_left
        show kitty at left
        with dissolve
        show cs flipped at right with moveinright
        arceus "Hey CS!"
        cs "Hey Arc! Hey Kitty!"
        kitty "What's up?"
        cs "Well, Merry Christmas guys! I'm glad you could travel back here for this!"
        arceus "No problem! I mean, after everything we went through, how could I not?"
        cs "Yeah, well, should we get inside? It's pretty cold out."
        kitty "Well, we are rather warm, but yeah."
        kitty "Let's go inside."
        jump dx_christmas_intro      
    if d20 == 3:
        n "CS peers out the window to see Anno's car pull into the driveway."
        cs "Hey look at that! Anno's here first!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show anno at mid_left
        with dissolve
        show cs flipped at right with moveinright
        anno "Hey CS!"
        anno "I showed up kinda early, but I wanted to see everyone's initial reactions of our decor work!"
        cs "Well I'm glad you showed up, come inside! It's cold out."
        jump dx_christmas_intro      
    if d20 == 4:
        n "All of a sudden, CS hears a futuristic sounding vehicle land outside."
        show cs disappointed flipped
        cs "What the hell is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show digi flipped at mid_left
        with dissolve
        show cs flipped at right with moveinright
        digi "Hey CS! How've you been?"
        cs "Hey Digi! Didn't know you have a... spaceship?"
        digi "Well sometimes, you can barely call it that."
        digi "Brr... it's cold out. Can we go inside?"
        cs "Yeah, let's get inside."
        jump dx_christmas_intro      
    if d20 == 5:
        n "As soon as he says that, he feels the house start to shake."
        show cs disappointed flipped
        cs "Wh-- What's going on?"
        show cs worried flipped
        n "As the house shakes even faster, a loud train whistle bellows out."
        cs "Holy shit, is that a train?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show tate festive flipped at mid_left
        show mean human flipped at left
        with dissolve
        show cs worried flipped at right with moveinright
        cs "That's a fucking train!"
        tate "Hey CS! How've you been doin'?"
        cs "Tate? Hey! I've been great!"
        mean "Hey CS, Merry Christmas!"
        cs "Merry Christmas to you too, Mean. Shall we get inside?"
        tate "Yeah!"
        jump dx_christmas_intro
    if d20 == 6:
        n "As soon as he says that, he feels the house start to shake."
        show cs disappointed flipped
        cs "Wh-- What's going on?"
        show cs worried flipped
        n "As the house shakes even faster, a loud train whistle bellows out."
        cs "Holy shit, is that a train?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show tate festive flipped at mid_left
        show mean human flipped at left
        with dissolve
        show cs worried flipped at right with moveinright
        cs "That's a fucking train!"
        tate "Hey CS! How've you been doin'?"
        cs "Tate? Hey! I've been great!"
        mean "Hey CS, Merry Christmas!"
        cs "Merry Christmas to you too, Mean. Shall we get inside?"
        tate "Yeah!"
        jump dx_christmas_intro    
    if d20 == 7:
        n "CS notices a familiar blue car roll up on the driveway."
        cs "Look at that! Looks like Billy is here first!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show billy at mid_left
        with dissolve
        show cs flipped at right with moveinright
        billy "Hi! It's Billy!"
        billy "Merry Christmas!"
        cs "Merry Christmas to you too, Billy!"
        billy "Times like these make me wish I could still run commercials."
        billy "It's been hard to sell products by word of mouth, especially since I died that one time."
        cs "That sucks man, I hope this party cheers you up."
        billy "Let's get inside. It's freezing out here."
        jump dx_christmas_intro      
    if d20 == 8:
        n "All of a sudden, CS hears helicopter blades outside of his house."
        show cs worried flipped
        cs "Woah, what the hell?"
        n "A Blackhawk helicopter is seen landing out in the middle of the street."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show obama festive at mid_left
        with dissolve
        show cs flipped at right with moveinright
        n "The President of the United States steps out."
        obama "Hello, CS! Nice to meet you."
        cs "Obama?! I didn't think you would actually come!"
        obama "Well, I have enjoyed your content, and when you sent an invitation to your Christmas party, I figured I could come visit for a while."
        obama "Besides, running the political circus has become tiring enough, I need a break."
        cs "Fair enough, I guess! Well Mr. President, let's get inside and wait for the other guests."
        obama "Sure thing. It is very cold outside."
        jump dx_christmas_intro      
    if d20 == 9:
        play sound sfx_siren
        show blue_light at left
        show red_light at right
        n "Sirens start blaring outside."
        show cs worried flipped
        cs "Uh oh! Why are the cops here?"
        n "CS rushes outside."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show copguy festive flipped at mid_left
        with dissolve
        show cs worried flipped at right with moveinright
        copguy "Heya, CS. Did I scare you?"
        cs "Fuck, yeah you did! I didn't think you were gonna be on duty!"
        copguy "Well someone's gotta be security, right?"
        cs "I... guess?"
        cs "Whatever, let's inside, I'm freezing."
        jump dx_christmas_intro      
    if d20 == 10:
        n "CS looks outside to see a bus pull up."
        cs "Hmm, I wonder who took the bus."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show sheriff flipped at left
        with dissolve
        show cs flipped at right with moveinright
        sheriff "God dammit! Stupid damn wheels! Stuck in the snow!"
        cs "Woah, hey! Who are you?"
        sheriff "Who am I? I'm Copguy's boss, that's who!"
        sheriff "I asked him to pick me up, but apparently he had to shop or some shit!"
        sheriff "And I had to take the bus!"
        cs "Oh wow okay, uhm, do you need help?"
        sheriff "Yes!! I keep getting stuck in the snow! Take me inside!"
        jump dx_christmas_intro      
    if d20 == 11:
        n "A beam sound can be heard from outside."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show ed flipped at center
        show rich flipped at mid_left
        show wesley flipped at left
        with dissolve
        show cs flipped at right with moveinright
        cs "Hey guys! How have you guys been doing?"
        ed "We've been doing well! Our business has been profitable recently!"
        ed "Even Wesley has made a speedy recovery! He wasn't too happy about getting that metal pipe in his back, though."
        cs "Yeah, I'm uhh..."
        cs "I'm really sorry about that. I still feel bad about taking that too far."
        n "Wesley stares at the ground and mutters."
        wesley "Yeah."
        rich "Well, why don't we get inside? It's freezing!"
        cs "Yeah, let's go!"
        jump dx_christmas_intro      
    if d20 == 12:
        n "An old Dodge Charger pulls up on the driveway."
        cs "Nice car! I wonder if that's Carguy..."
        hide cs with moveoutleft
        scene cs_house_snow_night
        show k22 flipped at left
        show k17 flipped at mid_left
        with dissolve
        show cs disappointed flipped at right with moveinright
        cs "Hey it's... two Pakoos?"
        show k17 happy flipped
        k17 "CS!!!"
        show k17 flipped
        k22 "Hey CS. Merry Christmas!"
        cs "Hi, so umm..."
        cs "Are you guys both Pakoo?"
        k22 "It's... kind of complicated."
        k22 "Let's go inside, and we can explain."
        jump dx_christmas_intro      
    if d20 == 13:
        n "A teleport-like sound is heard outside."
        show cs disappointed flipped
        cs "What in the world?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show aria flipped at mid_left
        with dissolve
        show cs flipped at right with moveinright
        cs "Oh hey! Aria, right?"
        aria "Yep, that's me!"
        aria "Goodness, am I too early?"
        cs "A little, but that's okay!"
        cs "I was hoping someone would arrive early."
        aria "Well then. Should we head inside? You're probably getting cold, I assume."
        cs "Yeah, it's kinda freezing out."
        jump dx_christmas_intro      
    if d20 == 14:
        n "Someone's car pulls into the driveway."
        cs "I wonder who that could be?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show michael at mid_left
        with dissolve
        show cs flipped at right with moveinright
        cs "Oh hey, it's Michael!"
        cs "You're still visiting the United States? I thought you were only here for the summer!"
        michael "I decided to spend a whole year over here."
        michael "It's pretty cold out, innit?"
        cs "Yeah, let's get inside now."
        jump dx_christmas_intro      
    if d20 == 15:
        n "CS sees Linus' car pulling up outside."
        cs "It looks like Linus got here first!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show linus at mid_left
        show luke flipped at left
        with dissolve
        show cs flipped at right with moveinright
        linus "Hey CS! Long time no see!"
        cs "You too, and Luke as well?"
        luke "Hey man! I know we didn't talk much during your short employment, but it was fun having you around!"
        luke "Linus talks a lot about you."
        cs "Oh really?"
        linus "I just think you're a funny guy!"
        linus "What wasn't funny was the cops showing up at LTT, but we can let bygones be bygones."
        cs "Yeah, sorry about all that. It's a long story."
        cs "Why don't we go inside, and i'll explain the whole thing while we wait."
        jump dx_christmas_intro      
    if d20 == 16:
        n "Another Honda Civic shows up in CS' driveway."
        cs "Oh look at that! It's Blank!"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show blank flipped at mid_left
        with dissolve
        show cs flipped at right with moveinright
        blank "Hey CS, how have you been?"
        cs "I've been doing well, did you drive safe here?"
        blank "I did, but lots of people on the interstate didn't!"
        blank "I got quite a bit of dashcam footage to watch if you want."
        cs "Sure thing! Let's get inside and watch while we wait for the others."
        jump dx_christmas_intro      
    if d20 == 17:
        n "An unknown car shows up in the driveway."
        cs "I wonder who that is?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show nova flipped at mid_left
        with dissolve
        show cs flipped at right with moveinright
        nova "Hey CS! Thanks for inviting me to your Christmas party!"
        cs "Yeah sure thing!"
        cs "It's been a while, how've you been?"
        nova "Oh y'know, I've been moving a lot, had my friend move in with me..."
        cs "Well, if you wanna chat about it, let's go inside first. It's cold out here."
        jump dx_christmas_intro      
    if d20 == 18:
        n "CS sees a Cherokee pull up to his house."
        show cs disappointed flipped
        cs "What the fuck? Who is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show elizabeth at center
        show anne at mid_left
        show grace at left
        with dissolve
        show cs disappointed flipped at right with moveinright
        cs "Hey, uhh..."
        eliza "Is this the right place?"
        cs "I think so?"
        cs "Are you..."
        eliza "I'm Elizabeth. Behind me is Anne and Grace."
        cs "You might have the wrong place. Sorry."
        eliza "Do you know a Mika? A Mikapara?"
        cs "Is that you?"
        eliza "Close enough."
        cs "Well, should we go inside."
        eliza "Yeah, I guess so."
        jump dx_christmas_intro      
    if d20 == 19:
        n "An orange mini coooper shows up infront of CS' house."
        cs "Holy crap, is that who I think it is?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show db at mid_left
        with dissolve
        show cs flipped at right with moveinright
        cs "DB! Your the first one here!"
        db "I am??"
        cs "Yes! You managed to be the earliest this time!"
        db "Wow, I can't believe it!"
        cs "Yeah! Let's get inside and we can talk!"
        jump dx_christmas_intro      
    if d20 == 20:
        n "A man in a white shirt walks up to CS' house."
        show cs disappointed flipped
        cs "Who the hell is that?"
        hide cs with moveoutleft
        scene cs_house_snow_night
        show avgn flipped at mid_left
        with dissolve
        show cs disappointed flipped at right with moveinright
        cs "Hey, are you..."
        avgn "I'm the fuckin' Nerd!"
        cs "The Angry Video Game Nerd? I didn't invite you, at least I don't think I did?"
        avgn "It doesn't fucking matter! Merry fucking Christmas!"
        cs "Okay, do you, wanna go inside?"
        avgn "Hell yeah."
        cs "Alright then..."
        jump dx_christmas_intro      
    else:
        n "CS waits paiently."
        n "He keeps on waiting."
        show cs disappointed flipped
        cs "Alright, any minute now..."
        cs "The party starts here in about 15 minutes, so people should start showing up soon..."
        n "CS keeps on waiting, but it looks like no one shows up early." 
        jump dx_christmas_intro      
    #Introductions
label dx_christmas_intro:
    scene black with dissolve
    n "By the time of the party, everyone shows up at CS' house in droves."
    scene cs_foyer
    show cs at left
    show anno at mid_left behind cs
    show aria at mid_mid_left behind anno
    show digi at center
    show tate festive flipped at mid_right
    with dissolve
    play music teeth_dust if_changed
    music teeth_dust
    cs "Well, it looks like everyone is here, right?"
    anno "DB isn't here yet, but other than that, yeah."
    show tate sheepish festive flipped
    tate "There are... a lot of people here..."
    show digi flipped
    digi "Yeah, I wonder where Arc and Kitty are..."
    show k17 happy at center
    show k22 at mid_mid_right behind k17
    with moveinright
    show tate shock festive flipped
    k17 "OMG hey guys!"
    show k17 shock
    k17 "You guys all look so... different!"
    show k22 confident
    k22 "Hi, I'm his--"
    show cs disappointed
    k17 "CS, look how much you've grown!"
    show k22
    cs "Okay, why are there 2 Pakoos?"
    cs "...and you don't have green hair anymore again?"
    show k22 disappointed
    k22 "Oh boy, alright K-17, calm down for one second. I think everyone here needs an explanation."
    show k17
    show digi
    show tate festive flipped
    cs "Yes please. I didn't want to say it, but it seems like everytime I meet you guys, your appearance always changes!"
    aria "Sorry."
    digi "Did I change too much?"
    cs "No no, just, let Pakoo #2 speak."
    if fun_value(FUN_VALUE_RARE):
        show k17 disappointed
        k17 "Hey, where's Fyreee at?"
        show k22 angry
        k22 "Dammit, can you let me talk?"
        show k17
    else:
        show k22
        k22 "I'm gonna assume that's me."
    show k22 confident
    k22 "Alright, so, I'm K-22, the physical manifestation of Pakoo's memories from the year 2022."
    show k22
    k22 "This is K-17, I'm sure you can figure out what year he is."
    show k17 happy
    k17 "Remember me? I'm the Sunny D guy!"
    n "CS groans."
    cs "Okay, so what about the green haired one?"
    show k17
    show k22 confident
    k22 "That's Addy, our boss. They run this archiving facility far away from here, and I guess they would be the closest version of Pakoo you know, but they aren't here right now."
    show k22 disappointed
    k22 "They are running their own Christmas party, which I wanted to be a part of, but this creature right here just HAD to go this party,"
    k22 "and I have to make sure he doesn't get too crazy."
    cs "Great."
    cs "Is that it?"
    show k22
    k22 "I mean, I could go on, but I'd be here all night."
    show mean human at mid_offscreen_right with moveinright
    mean "Hey, what's going on here?"
    show mean human shocked
    show k17 flipped
    show k22 flipped
    mean "Wait, there's 2 Pakoos now?"
    show mean human annoyed
    show k22 confident flipped
    k22 "Okay, so--"
    show k22 flipped
    show tate sheepish festive flipped
    tate "I'll just tell him later."
    show tate festive flipped
    cs "Alright, well, I'll let you guys talk, I'm gonna check on the others."
    hide cs with moveoutright
    show k17 shock flipped
    k17 "So, who are you? Are you DigBick?"
    show mean human angry
    mean "What did you just call me?"
    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at right behind cs_kitchen_fg
    show ed at mid_right behind cs_kitchen_fg
    show michael at mid_mid_right behind cs_kitchen_fg
    show billy at mid_mid_left behind cs_kitchen_fg
    with dissolve
    show cs at left with moveinleft
    cs "Hey guys, how are y'all doing?"
    obama "Hello CS, we are all preparing our meals for dinner tonight."
    obama "I'm gonna make a carrot cake."
    billy "I'm gonna make some big city sliders!"
    michael "I've been thinking of preparing some mashed potatoes."
    cs "That all sounds great!"
    cs "What about you, Ed?"
    ed "Well, I think when it comes to cooking, it's just as good as my foundation repair skills."
    ed "I'm preparing a Christmas turkey for our feast."
    cs "Damn! That sounds delicious!"
    if fun_value(FUN_VALUE_COMMON):
        cs "Hey Ed can you make me a sandwich?"
        ed "Noe!"
    else:
        cs "Well I hope you are all doing great!"
    cs "I'm gonna go check everyone else!"
    show cs flipped with determination
    hide cs with moveoutleft
    scene cs_living
    show digi flipped at left
    show linus at mid_left behind digi
    show luke at mid_left_left behind linus
    show blank at mid_right
    show nova at right
    with dissolve
    digi "So, this should go here..."
    linus "No, you got the wrong cable!"
    luke "You idiots are both wrong! You are putting in the wrong port!"
    "Digi and Linus" "Ohhhhh..."
    show cs flipped at center with moveinright
    cs "Hey guys! What are you guys doing?"
    digi "Oh, we are just trying to set up a projector to play movies on!"
    linus "Don't ask how this became a 3 man job."
    show cs
    cs "Well, what about you two?"
    blank "We are working on setting up the music."
    nova "The problem is, I don't really want to have Blank play his shitty music during the party."
    blank "Why? Not all of it's crazy shit, like yours is."
    show cs disappointed
    nova "Shut the hell up!"
    show cs worried
    cs "Woah okay, calm down."
    show cs disappointed
    cs "This is a Christmas party, after all. Let's try to have fun."
    show cs flipped
    cs "I'm gonna go check on anyone else who is here."
    hide cs with moveoutleft
    scene cs_hallway
    show arceus flipped at mid_left
    show kitty at left
    with dissolve
    show cs flipped at center with moveinright
    cs "Hey how are you guys? I was looking all over and couldn't find you."
    arceus "Sorry CS, we kind of got overwhelmed."
    kitty "We aren't the best with huge social gatherings."
    cs "Ah, it's okay. I'm just happy to talk."
    arceus "We'll be around when something important happens."
    show elizabeth at right
    show anne at mid_right
    show grace at mid_mid_right
    with moveinright
    eliza "Hey, what's up."
    show cs worried
    grace "CS! You're that YTP guy!"
    show cs disappointed
    cs "Uhm... who are you three?"
    eliza "Well, do you know Mika at all?"
    show cs angry
    cs "I swear to God, are you guys like, memories or some shit as well?"
    eliza "Relax, no, we are just..."
    eliza "Just think of us as them I guess yeah."
    cs "You guys are so complicated."
    arceus "I mean, it wasn't too hard for me to figure out, funny enough."
    show cs disappointed
    n "CS sighs."
    cs "I guess not, I'm just stressed out a bit."
    cs "I just really want this party to go well, and I feel like at this point I don't know half the people here."
    cs "I mean, you split into three people, Pakoo split into two..."
    eliza "I mean, if you want us to, we can step outside for a bit."
    cs "No, no, it's okay."
    cs "I hope you guys have fun, I'm gonna go back to the party."
    hide cs with moveoutright
    #Banter
label dx_christmas_banter:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "While the party starts up, Copguy and the sheriff get into a predicament."
    scene cs_living2
    show wesley at right
    show rich at mid_right
    show db at center
    show copguy festive at mid_right
    show sheriff flipped at mid_left
    with dissolve
    play music dont_preheat_your_oven
    music dont_preheat_your_oven
    sheriff "Hey Copguy!"
    copguy "I know, this party is great, right?"
    sheriff "No, I need to take a shit!"
    copguy "Okay, do you want me to tell everyone?"
    sheriff "Very funny, smartass! I need you to go with me."
    sheriff "My legs don't work, remember?"
    copguy "Dammit, this sucks."
    copguy "Alright, let's go."
    show copguy festive at left with move
    show copguy festive flipped with determination
    pause 0.5
    hide copguy
    hide sheriff
    with moveoutright
    scene cs_bathroom with dissolve
    show copguy festive flipped at left
    show sheriff flipped at mid_left
    with moveinleft
    pause 1.0
    show copguy festive flipped at center with move
    play sound sfx_hard_knock
    n "Copguy jiggles the bathroom door."
    tate "Occupied!"
    show copguy festive
    copguy "Sorry sir, we gotta wait."
    sheriff "This is the police! Open up!"
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show sheriff flipped at mid_left
    show copguy festive
    show tate cry festive
    hide tate with easeoutright
    tate "Awawawawa!!!"
    copguy "Really?"
    sheriff "What? I really have to go!"
    copguy "Whatever, just go. I'll wait here."
    sheriff "What do you mean? You have to wait here with me!"
    sheriff "I can't get off and on the toilet myself!"
    copguy "I think this is the worst crime I've dealt with."
    show copguy festive at left behind sheriff with move
    show copguy festive flipped with determination
    pause 1.0
    show copguy festive flipped at mid_mid_left
    show sheriff flipped at center
    with move
    hide copguy
    hide sheriff
    with dissolve
    play sound sfx_house_door_close
    scene cs_bathroom
    copguy "Alright, but you better hurry! I don't wanna be in here all day!"
    scene cs_kitchen
    show cs_kitchen_fg
    show k17 flipped at left
    show obama festive at center behind cs_kitchen_fg
    show ed at mid_right behind cs_kitchen_fg
    show michael at mid_mid_right behind cs_kitchen_fg
    show billy at right behind cs_kitchen_fg
    with dissolve
    k17 "So Obama, how have you stayed President?"
    k17 "Aren't you on your what, like fourth term?"
    if fun_value(FUN_VALUE_COMMON):
        obama "Ever heard of squatter's rights?"
        show k17 shock flipped
        k17 "You, can do that?"
        obama "I'm friggin' Obama, bitch! I can do what I want!"
    else:
        obama "Well, you see, we managed to somehow exhaust the list of succession back in 2018, and the house voted me back in."
        k17 "Huh, I see. That's pretty crazy."
    scene cs_living
    show digi flipped at left
    show linus at mid_left behind digi
    show luke at mid_left_left behind linus
    show cs disappointed flipped at right
    with dissolve
    cs "Is this projector still not set up?"
    digi "No! The projector keeps giving me this really weird error!"
    linus"Not even I've seen this!"
    digi "Watch, I'll turn it on, and..."
    play sound sfx_bluescreen
    rich "Hey, nice movie!"
    wesley "Looks like you'll have to set that up all over again."
    db "I got here early for this?"
    ed "Hey guys, what movie are we watching?"
    wesley "Nothing until these bozos fix the projector!"
    luke "Okay hold on, I got an idea."
    luke "Everyone step away from the projector."
    show digi flipped at center
    show linus at mid_right
    with move
    show digi with determination
    n "After a little bit of tech magic, the projector comes to life."
    luke "Tah dah!"
    rich "Finally, we can watch something."
    wesley "Are you 100-percent satisfied, Richard?"
    rich "Only about 80-percent."
    scene cs_foyer
    show aria at mid_mid_left
    show tate festive flipped at mid_right
    show mean human at mid_offscreen_right
    show k22 flipped at left behind k17
    show k17 flipped at center
    with dissolve
    k17 "So, there's a new world trade center now?"
    show k22 disappointed flipped
    k22 "What do you mean? They finished that in like 2014!"
    k17 "Oh. Sorry I forgot about that."
    show k22 flipped
    k17 "Okay, so, if big guy over there is DigBick..."
    show mean human angry
    show tate sheepish festive flipped
    mean "I'm not DigBick!"
    k17 "Are you DigBick's... girlfriend?"
    show tate sheepish blush festive flipped
    tate "What?"
    mean "No, first of all, I'm not fucking DigBick."
    show k17 disappointed flipped
    mean "I'm Mean, and this is Tate. We are friends."
    show tate furious blush festive flipped
    tate "And I'm not a girl--!{w=0.25}{nw}" with vpunch
    show tate furious festive flipped
    k17 "Yeah, you sound mean."
    show mean human annoyed
    show tate srs festive flipped
    show k17
    hide aria
    show aria at mid_mid_left
    k17 "What about you?"
    aria "Me? I'm Aria."
    show k17 shock
    k17 "Who?"
    show k22 confident flipped
    k22 "Uhh, well..."
    aria "I'm an old friend, the other one that wasn't Arceus? I changed."
    show k22 disappointed flipped
    k17 "Whaa?"
    k22 "Excuse us for a moment."
    show k22 disappointed flipped at Move((0.0, 0.14), (1.0, 0.14), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.4
    show k17 shock at Move((0.3125, 0.14), (1.0, 0.14), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 2.5
    scene cs_bathroom with dissolve
    copguy "Please tell me that's it, I can't bear this anymore."
    sheriff "Yep, I'm done!"
    sheriff "Now, are you gonna help me wipe?"
    play sound sfx_walkie_on
    n "All of a sudden, Copguy's walkie goes off."
    "Walkie" "Officer Copguy, we have a break-in at a house in the neighborhood you are currently at."
    "Walkie" "Can you report on that?"
    copguy "Gladly! Give me a second and I'll be in my car."
    play sound sfx_walkie_off
    copguy "Sorry boss, as much as I would love to keep helping you, this is important."
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show sheriff
    show copguy festive flipped
    hide copguy with easeoutright
    sheriff "Wait! You can't just leave me here!"
    copguy "I'll just be a moment! Don't move."
    play sound sfx_house_door_close
    scene cs_bathroom
    sheriff "God dammit! Get back here!!!"
    pause 3.0
    sheriff "\"Don't move.\" Thanks Copguy, you're a real fucking comedian."
    scene cs_door_outside 
    show k17 disappointed flipped at mid_left
    show k22 disappointed at mid_right
    show snow2
    show snow5
    with dissolve
    k17 "This is so unfair!"
    k17 "CS said that it's annoying that we changed or whatever, but look at everyone else!"
    k17 "All of my friends have changed so much!"
    k22 "Yeah, well when you are constrained to one year of your life, that can happen."
    k17 "It's just, how do I like, change that?"
    k17 "I can't just change who I am!"
    show k22 confident
    k22 "Look, you don't need to. I probably should've told you about how people change and whatnot."
    k22 "Honestly, Addy should've told you, but they were probably too busy setting up their party."
    show k22 happy
    k22 "Speaking of which, do you want to go back home? Celebrate Christmas with Addy?"
    k17 "Hmm..."
    show k17 happy flipped
    show k22 disappointed
    k17 "No, I wanna stay here till the end!"
    show k17 flipped
    k17 "I'll just keep being myself, and try to keep more of an open mind. Thank you K-22!"
    show k17 flipped at center with ease
    hide k17 with dissolve
    k22 "Dammit, it was worth a try."
    show k22 at mid_left with move
    show k22 flipped with determination
    k22 "I wonder how Addy is doing anyways."
    play sound sfx_ring_once
    n "K-22 hits up Addy."
    show archival_5 at mid_offscreen_right
    show pakoo disappointed at mid_right
    with moveinright
    # TODO: Play Frollo Show Rave Music here
    addy "HELLO??"
    k22 "Hey, uhh, how is it going over there?"
    addy "WHAT? I CAN'T HEAR, THE MUSIC IS REALLY LOUD!"
    show k22 angry flipped
    k22 "I WAS ASKING IF--{w=1.0}{nw}"
    addy "YEAH I'LL CALL YOU LATER, HAVE FUN AT CS' PARTY!"
    hide archival_5
    hide pakoo
    with moveoutright
    k22 "Mother fucker!"
    show snow3
    show snow4
    n "All of a sudden, the wind starts to pick up and snow begins to fall."
    show k22 disappointed flipped
    k22 "Brr... I should probably just get back inside and enjoy the party..."
    scene cs_bathroom with dissolve
    show k17 at mid_right with moveinright
    sheriff "Hey! Is someone there?"
    k17 "Huh?"
    sheriff "Hey you! Can you help me out of here?"
    show k17 shock
    k17 "Uhh... Uhh..."
    k17 "I'll go get someone!"
    hide k17 with easeoutleft
    scene cs_living2 
    show wesley at right
    show rich at mid_right
    show db at center
    show cs at left
    with dissolve
    rich "Oh man, I love this part."
    show k17 shock at mid_mid_right with moveinright
    k17 "Hey guys, how do I put this..."
    k17 "The sheriff is stuck in the bathroom?"
    show cs disappointed
    show k17 disappointed
    cs "Dammit, one second."
    obama "CS! Are you there?"
    show cs
    cs "Okay, lemme do this first. The president is calling!"
    hide cs with moveoutright
    #Cooking
label dx_christmas_cooking:
    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at mid_right behind cs_kitchen_fg
    show michael at mid_offscreen_left behind cs_kitchen_fg
    show billy at left behind cs_kitchen_fg
    with dissolve
    show cs at center behind cs_kitchen_fg with moveinleft
    cs "Hey Mr. President, what do you need?"
    stop music fadeout 3.0
    music end
    obama "You can just call me Obama."
    obama "Second of all, I accidently cut myself while chopping these carrots."
    obama "What a fool I am."
    show cs disappointed
    cs "Oh my god, are you okay?"
    obama "Yes, I'm fine, but I need someone to keep cutting for me."
    obama "Can you do it for me?"
    show cs
    cs "I guess I can, yeah."
    obama "Great, I just need a few more carrots cut up."
    obama "Give me a moment. I need a Band-Aid."
    hide obama with moveoutleft
    show cs at mid_right with move
    cs "Alright, just a few carrots."
    cs "Let's do this."
    #Carrot Karate Chop Minigame
    scene cs_kitchen
    show cs_kitchen_fg
    show obama festive at center behind cs_kitchen_fg
    show michael at mid_offscreen_left behind cs_kitchen_fg
    show billy at left behind cs_kitchen_fg
    show cs flipped at mid_right behind cs_kitchen_fg  
    with dissolve
    show smoke
    obama "Well would you look at that!"
    obama "That was some mighty fine chopping, CS!"
    show cs happy flipped
    cs "Woohoo!"
    cs "Thank you! Maybe I should cook more."
    show cs flipped
    cs "Speaking of cooking, I can smell something, burning..."
    obama "It is perhaps the smoke bellowing from the oven?"
    show cs worried flipped
    n "All of a sudden, the smoke detectors start beeping!"
    digi "Ahh! Turn it off!"
    nova "Dammit Blank! I said we weren't playing your music!"
    aria "Honestly this is kind of a bop. Keep it going."
    show ed flipped at center behind cs_kitchen_fg with easeinleft
    ed "Nooooo!"
    ed "My turkey!"
    show bigsmoke with dissolve
    n "Ed opens up the oven, only to have even more smoke pour out."
    n "Everyone hacks and coughs as smoke fills the room."
    hide bigsmoke with dissolve
    n "When the smoke finally clears, Ed pulls out a blackened turkey."
    hide smoke with dissolve
    show cs flipped
    play music snowdin_town
    music snowdin_town
    ed "Dammit! My roast is ruined!"
    billy "Not to fear, Ed! I made my famous restaurant mini-burgers!"
    show ed
    ed "You mean, steamed hams?"
    billy "Who the actual fuck calls burgers, steamed hams?"
    ed "It's a regional dialect?"
    billy "..."
    billy "Steamed hams... for God's sake..."
    billy "You Texans are crazy."
    michael "I also have my mashed potatoes!"
    cs "Well, at least we still have somewhat of a Christmas dinner."
    hide ed with moveoutleft
    n "Ed sheepishly walks back into the living room after throwing away the turkey."
    cs "Obama, finish baking your cake, and we can start eating."
    cs "I'm gonna go check up on everyone while you do that."
    hide cs with moveoutleft
    scene cs_bathroom
    show grace at mid_left
    with dissolve
    sheriff "...and I had to take that job that left me the way I am."
    sheriff "I could've went to college, studied the paranormal..."
    sheriff "...started up a shower curtain business, run a newspaper business..."
    sheriff "...but no. I had to be a cop."
    grace "Hey, are you almost done in there?"
    sheriff "Just leave me alone..."
    grace "But I really need to go!"
    sheriff "Find another bathoom."
    grace "But this is the only one in the house!"
    sheriff "In this mansion? There is only one damn bathroom?"
    show copguy festive flipped at center with moveinleft
    copguy "Hey, sorry, excuse me."
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show grace at mid_left
    show copguy festive flipped at center
    show sheriff at center behind copguy
    pause 1.0
    play sound sfx_house_door_close
    scene cs_bathroom
    show grace at mid_left
    copguy "Hey boss! You won't believe what I just experienced."
    copguy "This kid caught two burglars trying to rob his house with homemade traps!"
    copguy "It was so impressive, I probably would've fallen for some of them!"
    sheriff "That's great, can you get me off this toilet now?"
    sheriff "I've been thinking of signing my will here because of how long it's been!"
    copguy "Alright, let's get you out of here old man."
    play sound sfx_house_door_open
    scene cs_bathroom_open
    show grace at mid_left
    with determination
    show copguy festive at mid_right
    show sheriff at center behind copguy
    pause 1.0
    hide copguy
    hide sheriff
    with moveoutleft
    grace "Finally!"
    grace "Guys, the sheriff is out!"
    n "A line starts to form next to the bathroom."
label dx_christmas_mike:
    stop music fadeout 3.0
    music end
    scene cs_living2
    show cs at left
    show rich at center
    show ed at mid_right
    show grace at right
    with dissolve
    cs "Gee, that pizza I ordered is sure taking its time!"
    n "Just at that moment, the doorbell rings."
    cs "Well tickle my ballsack, what great timing!"
    grace "CS... you can't just say stuff like that."
    n "CS moves to open the door."
    scene cs_foyer with dissolve
    show cs at left with moveinleft
    cs "Hey guys, the pizza is here!"
    n "CS opens the door to let the pizza person in."
    show mike at right with moveinright
    play music rice_and_wine
    music rice_and_wine
    mike "I'm Chinese!"
    cs "Oh my god! It's Mike, everyone quick come look at Mike!"
    show k17 flipped at mid_mid_right behind grace
    show grace at mid_right
    show obama festive at center behind grace
    show tate festive at mid_left
    show billy at mid_mid_left
    with moveinleft
    show k17 happy flipped
    k17 "Hey, it's Mike! How's it going, long time no see!"
    grace "Oh my god! I love you Mike!"
    tate "What's up Mike!"
    obama "Mike, remember when I pardoned you?"
    billy "This guy can sell pizza better than I can!"
    show tate festive flipped with determination
    hide tate
    hide billy
    with moveoutleft
    show obama festive at mid_left behind cs
    show k17 at mid_mid_left
    show grace at center
    with move
    show k17 flipped with determination
    arceus "What's going on in here?"
    show arceus angry flipped at mid_mid_right with moveinleft
    show cs happy
    cs "It's Mike, Arceus! Mike the Pizzapotamus!"
    show cs
    show arceus angry
    arceus "Who?"
    grace "How do you not know who Mike the Pizzapotamus is?"
    obama "I mentioned him in my re-election speech!"
    cs "The children love him! He's the best in the world!"
    show arceus worried
    arceus "Yeah, I guess he's not ringing a bell?"
    show k17 disappointed flipped
    k17 "He works at the bus stop, dude!"
    arceus "You mean the bus station?"
    grace "No, the bus stop!"
    arceus "Oh, so he drives the bus?"
    show cs angry
    "Everyone" "No! The bus stop!"
    mike "You really don't know me, do you?"
    show arceus worried flipped
    arceus "Huh?"
    show pipe_gun flipped at manual_pos(0.6, 0.35) with dissolve
    n "Pizzapotamus shoots Arceus in the chest."
    play sound sfx_hks1
    show arceus worried flipped at manual_pos(0.4, 0.55):
        linear 0.5 rotate -45
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    n "As Arceus is dying on the floor, he faintly hears people talking."
    grace "I expected more from you."
    obama "Should've listened to my campaign speeches, bitch."
    mike "Alright, who wants to try pizza from my thermos?"
    show cs happy
    cs "Oh yes! Me first! Woohoo!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    pause 2.0
    play sound sfx_csnore
    cs "Zzz..."
    rich "Hey CS, are you sleeping?"
    scene cs_living2 
    show wesley at right
    show rich at mid_right
    show db at center
    show ed at mid_left behind cs
    show cs concentrate at left
    with dissolve
    play sound sfx_csnore
    rich "CS!"
    stop sound
    show cs worried
    cs "Huh?"
    show cs disappointed
    cs "Oh sorry, I did doze off."
    cs "I had this insane dream, and there was this pizza guy..."
    wesley "Speaking of pizza, should we have dinner now? I'm starving."
    cs "Yeah, that's a good point. Give me a moment to get ready."  

    #Dinner/More Banter
label dx_christmas_dinner:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    cs "Well, I'd love to start off this wonderful meal by saying--"
    blank "Hey stop it! We are not playing your music!"
    nova "Blank, Blank..."
    nova "This song is so..."
    nova "FUCKING ASS!"
    nova "STOP MAKING MUSIC!"
    nova "STOP MAKING MUSIC!"
    nova "Turn that shit off!"
    cs "Hey! Can you two stop fighting and get over here and eat with us!"

    #Gift Exchange
label dx_christmas_exchange:
    scene cs_living
    show cs at center
    with dissolve
    play music christmas_spirit
    music christmas_spirit
    cs "Alright everyone! It's time for the gift exchange!"
    cs "Everyone brought a gift, right?"
    n "Everyone nods."
    cs "Alright, well I marked numbers for everyone who showed up, so I'll go around while you guys draw from the bag!"
    hide cs with moveoutright
    n "CS goes around, and everyone draws out of the bag."
    cs "Let's see, who is going first?"
    #roll 1
    cs "Would you look at that! I guess I'm going first!"
    show cs at mid_left with moveinleft
    cs "I'm gonna pick, this one!"
    cs "I got..."
    show cs disappointed
    show thigh_highs at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    cs "Thigh highs?"
    show cs
    arceus "Look at that, you got my gift, CS!"
    hide thigh_highs with dissolve
    cs "Well, I guess I have more now!"
    k17 "You wear thigh highs?"
    cs "Yeah, I'm wearing them right now! See?"
    digi "Oh shit, I guess I never looked down to check."
    aria "I just assumed because of the outfit."
    hide cs with moveoutright
    arceus "Welp, it looks like I'm next."
    show arceus flipped at mid_left with moveinleft
    arceus "I got..."
    show tea_and_crumpets at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    arceus "Tea and crumpets?"
    kitty "Arcie! You got my gift!"
    hide tea_and_crumpets with dissolve
    show arceus worried flipped
    arceus "Sorry! I honestly forgot which one was yours."
    kitty "You saw me carry it in!"
    hide arceus with moveoutright   
    kitty "Whatever, it's my turn now."
    show kitty at mid_left with moveinleft
    kitty "Looks like I got..."
    show riffmaster at Move((0.3125, 1.0), (0.3125, 0.35), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    kitty "A... guitar hero controller?"
    cs "Holy shit, that's a Riffmaster!"
    kitty "Is that good?"
    cs "It's just a really good guitar controller."
    hide riffmaster with dissolve
    anno "That was my gift!"
    hide kitty with moveoutright   
    anno "It looks like I'm up next."
    show anno at mid_left with moveinleft
    anno "I got..."
    show raspberry_pi at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    anno "What the hell is this?"
    arceus "Ooh! That's a raspberry pi!"
    obama "What are you on about? That doesn't look edible at all!"
    digi "No-- okay it's my gift, so let me explain."
    digi "It's just a small computer that can run python."
    hide raspberry_pi with dissolve
    anno "Oh. Cool I guess."
    hide anno with moveoutright
    show digi flipped at mid_left with moveinleft
    digi "Well it's my turn now, and I'm gonna steal that Riffmaster!"
    show kitty flipped at mid_right with moveinright
    show riffmaster at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide riffmaster with dissolve
    hide digi with moveoutright
    kitty "Damn."
    kitty "Well, what do I do now?"
    cs "You can steal another gift, or pick out another one."
    hide kitty with moveoutleft
    arceus "Psst! Kitty! Come here!"
    n "Arceus whispers something into her ear."
    show kitty at mid_left with moveinleft
    kitty "Alright, Anno, hand over your computer thing."
    show anno at mid_right with moveinright
    show raspberry_pi at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide raspberry_pi with dissolve
    hide kitty with moveoutright   
    anno "Welp, next gift I guess."
    show anno at mid_left with move
    anno "I guess I'll pick this one."
    anno "I wonder what it'll be?"
    show lego_train at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    anno "A Lego set!"
    mean "A TRAIN Lego set!"
    hide lego_train with dissolve
    mean "That's my gift, by the way."
    if fun_value(FUN_VALUE_COMMON):
        tate "We know!"
    hide anno with moveoutright
    mean "Alright, well I guess it's my turn."
    show mean human flipped at mid_left with moveinleft
    mean "I'm picking this big one!"
    show instant_pot at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    mean "An instant pot?"
    tate "Mean, you got my gift!"
    show mean human happy flipped
    hide instant_pot with dissolve
    mean "Well it's mine now, bitch!"
    mean "Who's next?"
    hide mean with moveoutright
    tate "It's me!"
    show tate festive at mid_left with moveinleft    
    tate "Let's see..."
    show handy_switch at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.5
    show tate smug festive 
    tate "Billy? Is this yours?"
    billy "It's the Handy Switch!"
    billy "It let's you control any power source, from anywhere!"
    hide handy_switch with dissolve
    show tate festive
    tate "I'm sure I can find a use for this."
    hide tate with moveoutright
    billy "Alright, it's my turn!" 
    show billy at mid_left with moveinleft
    show doi at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top") 
    billy "Wow! Is this the Declaration of Independence?"
    obama "Yep! It's the real deal!"
    obama "Figured I didn't need it no more, so it's yours now!"
    hide doi with dissolve
    billy "Great! I can probably pitch this!"
    hide billy with moveoutright
    obama "Welp, I guess it's my turn now."
    show obama festive at mid_left with moveinleft 
    show mgs1 at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top") 
    obama "Metal Gear Solid?"
    copguy "Yeah, that's mine, I didn't know what anyone really wants, so I just found this at the station."
    hide mgs1 with dissolve
    obama "Dude, this is like my favorite game. I appreciate it."
    copguy "I'm glad."
    hide obama with moveoutright
    copguy "It's my turn now."
    show copguy festive flipped at mid_left with moveinleft 
    show gravity_falls at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    copguy "Okay, so I got \"Gravity Falls Season 2 Director's Cut\"..."
    copguy "...and boss? Is this your gun?"
    sheriff "Yeah, you got my gift. Don't ask how that DVD got in there."
    hide gravity_falls with dissolve
    hide copguy with moveoutright
    sheriff "Because I don't know either."
    show sheriff flipped at mid_left with moveinleft 
    sheriff "Whatever, it's my turn to pick a gift."
    sheriff "Damn, this is heavy! What the hell is this?"
    show cement at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    sheriff "A bag of cement?"
    ed "We had some leftover from the last house we worked on."
    hide cement with dissolve
    sheriff "Great, I can drop this on Copguy's head for leaving me in the bathroom!"
    hide sheriff with moveoutright
    ed "I guess it's my go."
    show ed flipped at mid_left with moveinleft 
    show melted_ice_cream at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    ed "What the hell? Who brought ice cream? It's all melted!"
    #Audio clip of Richard laughing
    play sound sfx_richlaugh
    pause 3.0
    hide melted_ice_cream with dissolve
    ed "Dammit Richard! I don't want this!"
    hide ed with moveoutright
    rich "Well let's see what I get."
    show rich flipped at mid_left with moveinleft 
    show pills at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    rich "Pain pills?"
    wesley "Wait a minute! Those are mine!"
    show wesley at mid_right with moveinright
    wesley "I didn't mean to gift that..."
    wesley "I'm gonna steal those since it's my turn now!"
    show pills at Move((0.3125, 0.5), (0.7125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    hide pills with dissolve
    hide wesley with moveoutright
    rich "Hey!"
    rich "What do I even get now?"
    rich "There's nothing else I really want here..."
    rich "I guess it's time to open another present."
    show sunny_d at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    rich "I got Sunny D!"
    hide sunny_d with dissolve
    n "K17 starts giggling."
    hide rich with moveoutright
    k17 "Alright! My go!"
    show k17 flipped at mid_left with moveinleft
    show fumo at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.5
    show k17 disappointed flipped
    k17 "Addy?"
    show k22 disappointed flipped at offscreenleft
    k22 "Huh?"
    hide k22 
    hide fumo
    with easeoutright
    n "K-22 springs up and steals the gift from K-17, sprinting out of the room."
    k22 "I'm sorry, I'll be right back!"
    k17 "What the hay! Now I gotta get another gift!"
    show k17 flipped
    k17 "I'm gonna take the Gravity Falls Commentary!"
    show sheriff at mid_right with moveinright
    show gravity_falls at Move((0.7125, 0.5), (0.3125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 3.0
    hide gravity_falls with dissolve
    k17 "...and the gun."
    hide k17 with moveoutright
    show copguy festive flipped at left with moveinleft
    copguy "Alright, then I'm taking the Declaration of Independence!"
    show billy at center with moveinright
    billy "What the actual fuck?"
    show doi at Move((0.4, 0.5), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    with dissolve
    pause 2.0
    hide doi with dissolve
    billy "Stop stealing gifts!"
    hide copguy with moveoutright
    hide sheriff with moveoutleft
    show billy at mid_left with move
    billy "Alright, I'll just take the next gift."
    show adderall at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    billy "Adderall?"
    billy "Nope! I'm done with any kind of drug! Not after last time!"
    aria "Aw, that was my gift!"
    aria "You want me to take it?"
    billy "Yes please!"
    show aria at mid_right with moveinright
    show adderall at Move((0.3125, 0.5), (0.7125, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    hide adderall with dissolve
    n "Aria steals Billy's gift."
    hide aria with moveoutleft
    billy "Awesome! I get to pick another gift!"
    show peach_syrup at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    billy "Peach syrup!"
    michael "Noice, you got my gift!"
    michael "It goes well with about everything!"
    hide peach_syrup with dissolve
    billy "I'll keep this one!"
    hide billy with moveoutright
    michael "Alright, what gift to choose..."
    show michael at mid_left with moveinleft
    show ltt_bottle at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    michael "I got a new water bottle!"
    linus "You got my LTT water bottle!"
    hide ltt_bottle with dissolve
    linus "{a=https://www.lttstore.com}lttstore.com.{/a}"
    hide michael with moveoutright
    linus "Alright, it's my turn."
    show linus at mid_left with moveinleft
    show ltt_screwdriver at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    linus "Hey Luke! I got your gift!"
    luke "Couldn't you tell it was mine?"
    hide ltt_screwdriver with dissolve
    linus "No, how was I supposed to figure that out?"
    hide linus with moveoutright
    luke "Whatever, it's my go now."
    show luke flipped at mid_left with moveinleft
    luke "I got..."
    show monitor at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show hard_drive at Move((0.3125, 1.0), (0.35, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    luke "A variation of PC components!"
    blank "Yeah, it's 2 monitors, a 1tb hard drive, and some other things."
    blank "I found it on the curb."
    hide monitor
    hide hard_drive
    with dissolve
    luke "On the {i}curb{/i}?"
    blank "Yeah, it was just lying there on the curb."
    luke "Damn, well then..."
    hide luke with moveoutright
    blank "It looks like it's my turn next."
    show blank flipped at mid_left with moveinleft
    show gamersupps at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    blank "Gamer supps?"
    blank "Guacamole Gamer... Fart... 9000?"
    nova "Dammit you got my gift Blank!"
    hide gamersupps with dissolve
    blank "Great."
    hide blank with moveoutright
    nova "As much as I want to steal that Adderall, I'm gonna pick a gift."
    show nova flipped at mid_left with moveinleft
    nova "Oh boy! I wonder what it is!"
    show russian_radio at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    nova "What the fuck is? Some World War II radio?"
    eliza "Yep. Used by the Soviets in the last half of World War II."
    hide russian_radio with dissolve
    nova "I'm sure Ges will like this, I'll probably give it to him."
    hide nova with moveoutright
    eliza "So, it's my turn, let's see what we have..."
    show elizabeth at mid_left with moveinleft
    show dog_food at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    eliza "Dog food."
    hide dog_food with dissolve
    eliza "Dog food?"
    db "Ah yeah, I had a lot extra lying around in my car, so I figured why not?"
    hide elizabeth with moveoutright
    db "Well I guess it's finally my turn."
    show db at mid_left with moveinleft
    show 1850_coin at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    db "Wow, I got some old coins!"
    digi "Holy shit, I think those are like, really rare!"
    digi "Lemme look it up."
    grace "You got our coins!"
    anne "We had them lying around on the table at home."
    digi "Yeah, those are super rare. I would hold onto those if I were you."
    hide 1850_coin with dissolve
    billy "Antique coins lying around, Tech lying on the curb..."
    billy "Where the hell do you guys live where you find this kinda shit?"
    hide db with moveoutright
    anne "Well Grace, you wanna pick out the last gift?"
    show grace at mid_left with moveinleft
    grace "Yippee! The last gift!"
    show old_shirt at Move((0.3125, 1.0), (0.3125, 0.5), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    grace "I got a cool new t-shirt!"
    cs "Hey! You finally got my gift!"
    hide old_shirt with dissolve
    cs "Not all of my Depop shirts sold, so it became my gift."
    cs "Does it even fit you?"
    n "Grace puts on the shirt."
    show grace shirt
    pause 2.0
    grace "Yep!"
    cs "Woohoo! All of the gifts have been handed out!"


    #Games/Climax
label dx_christmas_climax:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "After all of the gifts have been given out, almost everyone has come to the conclusion that the party should end."
    scene cs_living
    show cs at left
    show k22 at mid_right
    show k17 at mid_offscreen_right
    show luke at center
    show tate festive at mid_left behind cs
    show mean human flipped at mid_offscreen_left behind cs
    with dissolve
    k22 "Well CS, this was wonderful, but we should get going."
    cs "Wait! You aren't gonna stay for the games?"
    show k22 angry
    k22 "SHHHDADA--{w=1.0}{nw}"
    show k17 happy
    k17 "We are doing games? Well that's the best part!"
    show cs disappointed
    show tate sheepish festive
    k22 "Dammit!"
    show k22 disappointed
    show k17 disappointed
    show cs angry
    cs "So you never wanted to stay, you only came here because of him!"
    nova "Well, I'm also leaving, because this asshole won't let me play any good music!"
    blank "Hah! Says you! You wanted to play your trash this whole party!"
    digi "Hey wait a second! Luke!"
    luke "Wha? Oh shit!"
    show tate sad festive
    digi "You were, streaming movies to the projector from your phone?"
    show mean human annoyed flipped
    luke "Look, this looked to complicated to setup anyways, so I wanted to make it feel like your plan worked!"
    digi "But, but..."
    digi "I really thought I could set it up this time..."
    sheriff "Hey Copguy, I need to go to the bathroom again!"
    copguy "Motherfucker! Do it yourself!"
    ed "My poor turkey..."
    michael "I think I'm gonna puke."
    wesley "Arghh! My back! CS you prick, this is your fault!"
    grace "Guys! Stop yelling!"
    show tate srs festive
    tate "Yeah guys! Get it together!"
    nova "No! Fuck you!"
    anne "Hey!"
    show mean human angry flipped
    mean "What you say, you little fuck?"
    arceus "Oh my god, this is hurting my head..."
    show cs pissed
    cs "Dammit everyone! Shut the fuck u--{w=2.0}{nw}"

    #lights out
screen flashlight_demo:
    add Flashlight()

label dx_christmas_lights_out:
    $ mouse_visible = False
    scene black
    stop music
    music end
    sheriff "Hey uhh..."
    sheriff "I think I have finally become blind."
    linus "I think all of our eyes went out."
    cs "No! This can't be happening!"
    cs "My party is ruined!"
    tate "CS, this wasn't your fault."
    cs "Everyone is fighting, no one is having fun!"
    nova "Well yeah, at least I don't listen to Blank's shitty music anymore."
    tate "{i}Can it!" with hpunch
    tate "Look, we need to stop the arguing and calm down!"
    billy "I am calm!"
    aria "I am clam."
    cs "Okay, I'm trying to relax... and think..."
    cs "Let me feel my way to the basement, and try to check the breaker."
    cs "I'll be right back."
    k17 "Oof!"
    cs "Sorry!"
    arceus "CS? Is that you?"
    cs "Hey Arc. I'm making my way to the breaker to see if I can turn it on."
    arceus "Great. If you find Kitty, lemme know, I don't know where she went."
    arceus "I think she wanted to get extra food, but it's been 20 minutes since then."
    cs "Alright, I'll let you know."
    cs "The door to the basement should be here somewhere..."
    n "CS feels around the wall."
    n "Finally he finds the doorknob."
    cs "Ah-a!"
    if fun_value(FUN_VALUE_EPIC):
        cs "Huh, why is my doorknob..."
        cs "Squeezable?"
        n "CS turns the doorknob."
        n "All of a sudden, CS gets kicked to the ground!"
        play sound sfx_hitbod3
        cs "Ow! What the fuck was that?"
        eliza "Oops, sorry."
        eliza "You grabbed, my chest."
        cs "Oh crap! I'm so sorry!"
        eliza "It's okay, none of us can see and I guess I was standing infront of the doorknob..."
        cs "I was, trying, to get to the basement..."
        eliza "Let me just move out of the way."
        cs "Yeah, thanks."
    else:
        cs "Why is my doorknob so big?"
        n "CS turns the doorknob."
        grace "Ahhhhh!"
        grace "You're squeezing my head!"
        cs "Oops, sorry!"
        cs "I'm trying to get to the basement."
        grace "Let me move before you try breaking my head again."
    n "Slowly but surely, CS makes his way into the basement."
    cs "Alright, I just need to find the breaker."
    n "CS feels around, and manages to find a flashlight on a table."
    scene cs_basement
    show cs at center
    show screen flashlight_demo
    cs "Thank god, I can actually see."
    hide cs with moveoutright
    scene breakerbox with dissolve
    show cs at left with moveinleft
    cs "Found it!"
    n "CS opens the breaker and flicks off and on the switches."
    show cs disappointed
    cs "Damn, nothing."
    show cs flipped
    cs "Well, it was worth a try."
    hide cs with moveoutleft
    scene cs_basement
    show cs at center
    show kitty at left
    with dissolve
    cs "At least I have this flashlight now!"
    show cs flipped
    n "As CS turns around, he spots Kitty chilling against the wall."
    play music synchronicity
    music synchronicity
    cs "Kitty? What are you doing down here? Arceus is looking for you!"
    kitty "Sorry, I got a bad migraine during the end of the party, so I tried to find the quietest place in the house."
    kitty "I'm a little glad the power went out actually, it's been peaceful here."
    cs "I was trying to fix the power via the breaker, but it looks like I got no dice."
    kitty "I think the power is out everywhere, I heard the wind really pick up outside a little while ago."
    kitty "You should probably go check for yourself."
    kitty "Let Arceus know I'm down here, I think I'm gonna stay here for a bit."
    cs "Got it. Stay safe down here."
    show cs with determination
    hide cs with moveoutright
    n "CS rushes back upstairs."
    scene cs_hallway_off 
    show arceus at center
    show elizabeth at right
    with dissolve
    show cs at left with moveinleft
    arceus "Welcome back! Assuming you didn't get the power working?"
    cs "Nope, but I found Kitty!"
    cs "She's relaxing in the basement due to her head hurting."
    arceus "That makes sense, I'll go talk to her here soon."
    eliza "I see you found a torch."
    cs "Yeah, it was lying around downstairs, I'm lucky I found one."
    show arceus flipped
    eliza "I was thinking of lending mine to Arceus, so he can go in the basement."
    arceus "I would appreciate it."
    show elizabeth at mid_right
    eliza "Take this, make sure to bring it back when the power turns on."
    arceus "Got it."
    show arceus with determination
    hide arceus with moveoutleft
    eliza "Before you go CS, I would see if you can check the outdoors."
    eliza "Even though it is dark, no light is coming in from outside."
    eliza "It also sounds terrible out there."
    show cs disappointed
    eliza "I've experienced some harsh Soviet winters, but I've never heard anything this bad before."
    cs "Well, that's some awesome news."
    cs "I'll go check on others, and see if I can get outside."
    hide cs with moveoutright
    scene cs_foyer_off
    show anno at mid_left
    show aria at mid_mid_left behind anno
    show digi at mid_mid_left
    show k17 disappointed at center behind digi
    show k22 disappointed at mid_mid_right
    show tate srs festive flipped at mid_right
    show mean human annoyed at mid_offscreen_right
    with dissolve
    show cs at left with moveinleft
    cs "Hey guys! How is everyone holding up?"
    anno "It's getting kinda cold, so I hope the power comes back soon."
    anno "My phone is about to die."
    cs "I'm gonna check outside and see how bad it is."
    k22 "I was gonna try that, but I couldn't find the door."
    cs "If we get outside, we might be able to dig our vehicles out."
    hide cs with moveoutright
    anno "Good luck CS!"
    scene black with dissolve
    cs "Alright, let's see how bad it is."
    n "CS pulls and yanks open the door, until it finally rips open."
    n "He falls backwards, only to be greeted with an ungrateful sight."
    cs "What the hell? Is that snow?"
    n "CS sticks his finger out into the mysterious substance."
    cs "Oh my God, how much... did it..."
    n "CS slams the door shut and runs back to deliver the news."
    scene cs_foyer_off
    show anno at mid_left
    show aria at mid_mid_left behind anno
    show digi at mid_mid_left
    show k17 disappointed at center behind digi
    show k22 disappointed at mid_mid_right
    show tate srs festive flipped at mid_right
    show mean human at mid_offscreen_right
    with dissolve
    show cs worried flipped at center with moveinright
    cs "Guys, the door... the door..."
    aria "Calm down, CS. Catch your breath."
    show cs disappointed flipped
    cs "The door, it's, all snow."
    show tate sad festive flipped
    show k17 shock flipped
    anno "All snow?"
    show mean human annoyed
    mean "The door?"
    k17 "It's?"
    digi "Are we trapped in here?"
    show mean human angry
    show tate sad festive
    mean "There's only one way to find out."
    show cs disappointed
    mean "CS, take me to the roof."
    cs "To the roof?"
    mean "Yeah, let me climb up there."
    cs "Sure, we can try."
    show mean human annoyed flipped
    tate "Be careful, Mean."
    hide cs
    hide mean
    with moveoutright
    n "CS and Mean find the ladder to the attic, and make their way up."
    scene cs_attic 
    show cs disappointed at mid_left
    show mean human annoyed at mid_right
    with dissolve
    stop music fadeout 3.0
    music end
    mean "You good, CS?"
    cs "Yeah, I'm just a bit tired."
    cs "There should be a hatch or something up here..."
    mean "Shine your light up."
    mean "You mean like that one?"
    cs "Yeah, pull it open."
    n "As Mean yanks on the hatch, it bursts open downwards, as a huge pile of snow falls onto the attic floor."
    cs "That is... a lot of snow."
    mean "C'mon, let's get up here."
    n "Mean climbs up onto the roof."
    hide mean with moveouttop
    mean "Holy..."
    mean "Fuck."
    cs "What? How bad is it?"
    mean "Grab my hand, I'll pull you up."
label dx_christmas_snowed_in:
    play music winters_halloween
    music winters_halloween
    scene snowed_in
    hide screen flashlight_demo
    show cs sil_black:
        zoom 0.15
        xpos 0.3
        ypos 0.5
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.4
        ypos 0.5
    show snow1
    show snow2
    show snow3
    show snow4
    show snow5
    show snow6
    show snow_wind
    with dissolve
    mean "Look out in the distance."
    n "As CS and Mean stare out into the distance, they see nothing but an endless desert of snow, with the lamp poles poking out through."
    cs "What the fuck."
    cs "Am I dreaming?"
    n "CS picks up some snow and shoves it in his face."
    cs "I guess not..."
    mean "I know, this doesn't even feel real. How did this happen so fast?"
    mean "I live in Canada, and it's never {i}this{/i} bad."
    cs "So this is it. We are stuck here, aren't we?"
    mean "I don't fuckin' know how any of us would be able to fix this, man."
    cs "A Christmas miracle, maybe."
    cs "I don't think anyone else back in the house is gonna believe us."
    mean "Well they can see it from themselves."
    mean "Let's get back inside, it's freezing out here."
    scene black with dissolve
    n "CS and Mean climb back down and meet back up with everyone."
    scene cs_living2_off
    show cs disappointed at mid_left
    show mean human annoyed flipped at mid_offscreen_left
    show ed at right
    show digi at mid_mid_right
    show linus at mid_right
    show rich at mid_right_right
    show tate sad festive flipped at mid_mid_left
    show obama festive at center behind digi
    show k22 disappointed at center behind digi
    show k17 disappointed at mid_mid_right behind obama
    with dissolve
    show screen flashlight_demo
    stop music fadeout 3.0
    music end
    cs "Well guys, we got some bad news."
    cs "We might be stuck here for a while."
    k22 "Like all night? For a couple hours?"
    cs "Uhh..."
    cs "At least for the night."
    ed "Gee, where are we all gonna sleep?"
    linus "There's no way we can dig our way out?"
    digi "If it's that bad, wouldn't a snow plow be here soon anyways?"
    show cs worried
    rich "We've dealt with worse, let's get out there and shovel!"
    show cs disappointed
    show mean human angry flipped
    show tate shock festive flipped
    mean "Everyone! Stop!"
    mean "There's like 20 feet of snow."
    n "Everyone goes quiet."
    mean "If you want to go up to the roof and check for yourself, go ahead."
    show mean human annoyed flipped
    show tate sad festive flipped
    mean "I couldn't believe it either, but..."
    mean "There's nothing else but snow, and even more snow."
    blank "I didn't even think you could get that much snow..."
    show cs
    cs "So that means we are gonna have to wait it out!"
    show cs happy
    cs "And what a better way than to play some games!"
    show cs
    michael "I spy something, black!"
    nova "Is it Obama?"
    show mean human flipped
    show tate flipped festive
    obama "Hey!"
    michael "No, it is not."
    aria "Is it everything?"
    michael "Correct!"
    cs "Okay, I have something I've wanted to play again with someone."
    cs "I have a few board games somewhere, I just need to look."
    show tate sad festive flipped
    tate "Please tell me it's not Chess..."
    cs "It's better than Chess! I'll be back."
    scene black with dissolve
    n "After a bit of rummaging, CS comes back with a blueish-looking box."
    scene cs_living2_off
    show cs happy at mid_left
    show mean human flipped at mid_offscreen_left
    show ed at right
    show digi at mid_mid_right
    show linus at mid_right
    show rich at mid_right_right
    show tate sheepish festive flipped at mid_mid_left
    show obama festive at center behind digi
    show k22 disappointed at center behind digi
    show k17 disappointed at mid_mid_right behind obama
    with dissolve
    cs "It's Reversi!"
    digi "You have an actual Reversi board?"
    k17 "Isn't that the one game from Windows 3.1?"
    cs "Precisely!"
    n "CS takes off the cover and starts taking the pieces out."
    aria "Wait a second."
    aria "This is Othello, not Reversi."
    show cs disappointed
    cs "What do you mean? It says Reversi on the box!"
    aria "Yeah, I know, but in 1971--{w=1.5}{nw}"
    show cs angry
    cs "It's fucking Reversi, okay?"
    cs "I just want to play some Reversi."
    show cs
    cs "Who wants to play with me?"
    # maybe pick a character to play here?
    # Insert Reversi Gameplay here
label dx_christmas_billy_time:
    scene cs_living2_off
    show cs at mid_left
    show mean human flipped at mid_offscreen_left
    show ed at right
    show digi at mid_mid_right
    show linus at mid_right
    show rich at mid_right_right
    show tate sheepish festive flipped at mid_mid_left
    show obama festive at center behind digi
    show billy at center
    show k22 disappointed at center behind digi
    show k17 disappointed at mid_mid_right behind obama
    with dissolve
    billy "Wait! Everyone hold on!"
    cs "What? What is it Billy?"
    play music on_the_rocks
    music on_the_rocks
    billy "The handy switch!"
    billy "Who got my handy switch for their gift?"
    show tate festive
    tate "Me!"
    billy "Follow me to the basement!"
    show cs disappointed
    cs "Billy, what are you doing?"
    billy "I have an idea, and I'll be right back!"
    hide billy with moveoutleft
    show tate festive flipped
    tate "I guess I'm following Billy, be right back as well."
    hide tate with moveoutleft
    scene black with dissolve
    hide screen flashlight_demo    
    billy "Oh dang it! I forgot to bring a light!"
    scene cs_hallway_off
    show billy at mid_left
    show tate festive at center
    show elizabeth at right
    show screen flashlight_demo
    with dissolve
    tate "I have my phone!"
    billy "That works, I think the basement is down here!"
    eliza "Did you guys manage to get outside?"
    billy "Apparently the snow is up to the roof!"
    n "Elizabeth looks shocked."
    billy "But good news! I have a way to possibly bring the power back!"
    billy "With the handy switch!"
    eliza "I have no clue how that's gonna work, but good luck to you two."
    tate "Is the basement over this way?"
    eliza "Yeah, down the hall and to the left."
    show tate sheepish festive
    tate "Thank you... Mika?"
    eliza "It's Elizabeth, but sure."
    hide tate
    hide billy
    with moveoutright
    scene cs_bathroom_off
    show grace at mid_right
    show anne at right
    with dissolve
    show tate festive at center
    show billy at mid_left
    with moveinleft
    grace "Hey! You're the TV man!"
    anne "Grace always wanted to buy every product you sold."
    billy "You should! Hi, Billy Mays here for the--"
    show tate sheepish festive flipped
    tate "Billy, the power?"
    billy "Oh yeah. We can talk later!"
    show tate festive
    hide tate
    hide billy
    with moveoutright
    grace "I'll be waiting Billy!"
    n "Billy and Tate run into the basement."
    scene cs_basement
    show kitty at left
    show arceus worried flipped at mid_left
    show tate festive flipped at center
    show billy at mid_right
    with dissolve
    arceus "Tate? Billy?"
    kitty "What's going on?"
    billy "Fixing the power with the power of the handy switch!"
    show tate sheepish festive flipped
    tate "Don't ask."
    scene breakerbox
    show tate festive at mid_left
    show billy at mid_right
    with dissolve
    n "Finally, Billy and Tate make it to the breaker."
    billy "Alright, all you gotta do is put the switch on the breaker!"
    show tate sheepish festive
    tate "Really? Just like, slap it on?"
    billy "Yes! It's that easy!"
    show handy_switch at Move((0.3125, 0.4), (0.3125, 0.4), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    n "Tate slaps the handy switch on the breaker, and flips the switch."
    play sound sfx_snd_lightswitch
    show tate shock festive
    hide screen flashlight_demo
    tate "Wh--{w=1.0} Whaaaaaaaaaat??"
    billy "Like magic!"
    show tate sheepish festive
    tate "How... how does this even work, Billy?"
    n "Billy ponders for a moment."
    pause 3.0
    billy "I don't even know myself!"
    show tate festive
    tate "Well, what are we waiting for?"
    tate "Let's go back upstairs and check out the good news!"
    hide tate
    hide billy
    with moveoutright
    scene cs_basement
    show kitty at left
    show arceus happy flipped at mid_left
    with dissolve
    show tate festive at mid_mid_right
    show billy at right
    with moveinleft
    arceus "Would you look at that!"
    kitty "How did you guys do it?"
    billy "That's the power, of the power,"
    hide tate
    hide billy
    with moveoutright
    scene cs_hallway
    show eliza at mid_right_right
    show grace at mid_right
    show anne at right
    with dissolve
    show tate festive flipped at mid_left
    show billy at center
    with moveinright
    grace "Yay! The power is back!"
    anne "You did it!"
    billy "We sure did!"
    eliza "I don't know what kind of technology you have to have had fixed this, but good job!"
    hide tate
    hide billy
    with moveoutleft
    scene cs_living2 
    show cs flipped at center
    show mean human at mid_offscreen_right
    show sheriff at mid_mid_right
    show copguy festive at mid_right
    show luke at mid_left
    show rich flipped at mid_mid_left behind cs
    with dissolve
    show tate festive at mid_left
    show billy at left
    with moveinleft
    cs "Holy crap, the power is back!"
    sheriff "My eyes work again!"
    ed "Hooray!"
    tate "It looks like all we needed was Billy's handy switch!"
    show mean human angry
    show tate sheepish festive
    mean "Please don't say it like that, Tate."
    show mean human
    show tate festive
    stop music fadeout 3.0
    music end
    luke "This is great and all, but isn't the house still under 20 feet of snow?"
    copguy "How are we even gonna get rid of that?"
    copguy "We would need a lot of..."
    pause 1.0
    show cs
    cs "A lot of what?"
    copguy "...Nevermind. I forgot what I was thinking about."
    rich "Didn't you guys get up to the roof?"
    ed "Maybe we should all go up and check it out."
    hide mean
    hide cs
    hide copguy
    hide rich
    hide luke
    hide tate
    hide billy
    with moveoutright
    n "Everyone clammers up the stairs, and one by one, they all climb up onto the roof."
    sheriff "Welp."
    sheriff "I'll just, wait here."
label dx_christmas_roof_moment:
    scene snowed_in
    show cs sil_black:
        zoom 0.15
        xpos 0.3
        ypos 0.5
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.4
        ypos 0.5
    show arceus sil_black:
        zoom 0.15
        xpos 0.54
        ypos 0.54
    show anno sil_black:
        zoom 0.15
        xpos 0.53
        ypos 0.33
    show tate festive sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.36
    show obama sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.47
    show ed sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show rich sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.34
    show wesley sil_black:
        zoom 0.15
        xpos 0.56
        ypos 0.45
    show blank sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.34
    show nova sil_black:
        zoom 0.15
        xpos 0.55
        ypos 0.43
    show copguy sil_black:
        zoom 0.15
        xpos 0.33
        ypos 0.35
    show billy sil_black:
        zoom 0.15
        xpos 0.63
        ypos 0.46
    show aria sil_black:
        zoom 0.15
        xpos 0.42
        ypos 0.36
    show kitty sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.46
    show grace sil_black:
        zoom 0.15
        xpos 0.31
        ypos 0.31
    show anne sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show elizabeth sil_black:
        zoom 0.15
        xpos 0.38
        ypos 0.45
    show digi sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.46
    show linus sil_black:
        zoom 0.15
        xpos 0.46
        ypos 0.35
    show luke sil_black:
        zoom 0.15
        xpos 0.32
        ypos 0.45
    show db sil_black:
        zoom 0.15
        xpos 0.5
        ypos 0.6
    show k17 sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.2   
    show k22 sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.23    
    show snow1
    with dissolve
    k22 "So it is as bad as you said."
    wesley "It just keeps going! It never ends!"
    tate "What are we going to do? We can't just, walk out there!"
    copguy "I got an idea. You guys, move over there..."
    show cs sil_black at Move((0.3, 0.5), (0.27, 0.33), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show k22 sil_black at Move((0.45, 0.23), (0.34, 0.29), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show arceus sil_black at Move((0.54, 0.54), (0.3, 0.4), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show mean human flipped sil_black at Move((0.4, 0.5), (0.32, 0.4), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show anno sil_black at Move((0.53, 0.33), (0.32, 0.48), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show tate festive sil_black at Move((0.34, 0.36), (0.29, 0.5), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show obama sil_black at Move((0.47, 0.47), (0.27, 0.49), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show ed sil_black at Move((0.34, 0.43), (0.25, 0.47), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    copguy "And you move there..."
    show rich sil_black at Move((0.45, 0.34), (0.45, 0.31), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show wesley sil_black at Move((0.56, 0.45), (0.5, 0.36), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show blank sil_black at Move((0.43, 0.34), (0.52, 0.40), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show nova sil_black at Move((0.55, 0.43), (0.5, 0.45), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show copguy sil_black at Move((0.33, 0.35), (0.45, 0.5), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show billy sil_black at Move((0.63, 0.46), (0.42, 0.36), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show aria sil_black at Move((0.42, 0.36), (0.41, 0.40), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show kitty sil_black at Move((0.43, 0.46), (0.42, 0.48), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 1.0
    show anne sil_black at Move((0.34, 0.42), (0.65, 0.31), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show k17 sil_black at Move((0.43, 0.2), (0.68, 0.29), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show elizabeth sil_black at Move((0.38, 0.45), (0.6, 0.35), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show digi sil_black at Move((0.47, 0.46), (0.63, 0.39), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show linus sil_black at Move((0.46, 0.35), (0.66, 0.39), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show luke sil_black at Move((0.32, 0.45), (0.64, 0.44), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show db sil_black at Move((0.5, 0.6), (0.63, 0.5), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show obama sil_black at Move((0.47, 0.47), (0.58, 0.47), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 4.0
    copguy "That should work!"
    k17 "SoS? Nice DaThings reference."
    k22 "You idiot, it's an emergency code! If any airplanes see us--"
    k17 "Yeah I know, I was just making a joke."
    k22 "Also, DaThings is a girl now."
    k17 "Huh?"
    ed "Are there gonna be any airplanes in the sky?"
    wesley "Maybe we need some lights?"
    cs "What's to say people are still alive? Who knows how far this glacier goes?"
    digi "CS, do you really think we are the last people left?"
    cs "I don't know, I just worry that this is--"
    play sound sfx_jingle volume 0.2
    n "As CS becomes more frantic, a noise from far away can be heard."
    k17 "Shhh! Do you hear that?"
    cs "What? What is it?"
    play sound sfx_jingle volume 0.4
    k17 "I hear jingling! Does anyone hear jingling?"
    rich "Yeah, I do! It's coming from over there!"
    n "Richard points up in the sky."
    play sound sfx_jingle volume 0.6
    k17 "Yeah I see it!"
    aria "Is that..."
    digi "It's Santa! He's really up there I think!"
    wesley "What? I don't hear or see anything! Where?"
    cs "Wait a minute... I have an idea!"
    ed "Yeah, I can see him it's almost clear as day! There's Rudolph at the end, see that red light?"
    cs "Guys! You all have to believe! Believe in Santa and have that Christmas spirit!"
    eliza "Do you really think that will work?"
    cs "We gotta try! Sing with me guys!"
    cs "Ohhh..."
    cs "You better watch out..."
    cs "You better not cry..."
    cs "You better watch out I'm telling you why..."
    cs "Santa Claus is coming, to town!"
    cs "Come on guys, you gotta sing!"
    k17 "He's making a list..."
    k17 "He's checking it twice..."
    grace "He's gonna find out if you've been naughty or nice..."
    rich "Santa Claus is coming, to town!"
    tate "He knows when you are sleeping..."
    mean "He knows when you're awake..."
    db "He knows if you've been bad or good..."
    obama "So, you better be good. For goodness sake!"
    cs "Ohhh..."
    everyone "You better watch out..."
    everyone "You better not cry..."
    everyone "You better watch out I'm telling you why..."
    everyone "Santa Claus is coming, to town!"
    scene black with dissolve
    santa "Ho ho ho!"
    santa "The wind really started the pick up around here, didn't it Vixen?"
    santa "Ho ho, do you all hear that? It sounds like I can hear Christmas cheer being spread down on the ground!"
    santa "Shine your light down there, Rudolph!"
    santa "Hey, wait a minute!"
    santa "Is that an SoS signal?"
    santa "Ho ho ho! Nice DaThings reference!"
    santa "Okay, I should probably go down there and check it out."
    scene cs_roof
    show cs happy at left
    show obama festive at mid_mid_left behind k17
    show billy at center behind cs
    show michael at mid_left
    show ed at mid_right
    show linus at mid_mid_right
    with dissolve
    cs "We did it guys! We got Santa to save us!"
    n "Santa's Sleigh slows to crawl as it slowly lands in the snow."
    play music snow_blind
    music snow_blind
    show santa at right with moveinright
    santa "Ho ho ho! Merry Christmas, everyone!"
    show grace at mid_right with easeinleft
    grace "SAANNNNNTAAA!!"
    grace "OH MY GODD!!"
    show k22 flipped at mid_left
    show k17 happy flipped at mid_mid_left 
    with moveinleft
    k17 "Haha, see K-22? Who needs Addy's party when we can literally meet The Big Man himself?"
    show k22 happy flipped
    k22 "Heh, I guess you gotta point there. They aren't gonna believe this!"
    show cs
    santa "Well, let's see who we have here..."
    santa "..."
    santa "Mr. President? What are you doing here?"
    show obama festive at center with move
    obama "Well, I wanted to go to my good friend CS' Christmas party!"
    santa "Ho ho, well..."
    n "Santa stares around the crowd."
    show k17
    show k22
    with determination
    hide k17
    hide k22
    with moveoutleft
    santa "Ed? Richard? Welsey? Keep up the good work. Might need some foundation repair at my workshop here soon! Ho ho!"
    show rich flipped at mid_mid_left with moveinleft
    show wesley flipped at mid_left with moveinleft
    rich "Really!?"
    ed "We appreciate the offer, Mr. Klaus. Keep us in touch."
    santa "...And you there! Mr. Rosen!"
    show michael at center with move
    santa "Don't let those YouTube Poopers get to your head, you're a great author."
    n "Santa glances at CS."
    show cs disappointed
    cs "Hey! I love his work too! I don't even really use Michael as a source!"
    n "Both Michael and Santa laugh."
    show cs
    santa "Ah yes, Linus and Luke..."
    santa "We might need you guys up there at the North Pole as well, lots of kids these days want these crazy gaming PCs!"
    linus "If you ever need us, give LTT a call!"
    santa "There's a lot of... people here I would not expect to see."
    show rich
    show wesley
    with determination
    hide rich
    hide wesley
    hide michael
    hide obama
    hide ed
    with moveoutleft
    santa "Billy Mays, I almost forgot about... you coming back."
    hide linus with moveoutleft
    billy "Don't worry Santa, my drug days are over!"
    santa "Ho ho ho! That's the spirit!"
    santa "Well, I could keep going, but I should ask:"
    santa "What happened here? A place like this shouldn't get this much snow..."
    cs "None of us know, but we seemed to be trapped for god knows how long."
    cs "I mean, your Santa Claus, would you have anything to fix this?"
    santa "Ho ho ho..."
    santa "I... suppose I don't, unfortunately."
    santa "I may be Father Christmas, but I can't just make snow magically go away."
    santa "I'm sorry, cs188."
    copguy "Well, wait a second!"
    show copguy festive flipped at center with moveinleft
    copguy "Can't we wish for one gift? For Christmas?"
    santa "Well, I suppose I can make a miracle happen if it were a gift..."
    santa "CS? Do you have a gift that you've always wanted?"
    cs "Hmm..."
    show copguy festive
    copguy "CS, I think I have just the thing."
    show copguy festive at mid_left with move
    n "Copguy whispers in CS' ear."
    show cs surprised
    cs "Oh! You sure that will work?"
    n "Copguy nods."
    show cs
    show copguy festive flipped with determination
    show cs at center with move
    cs "Alright Santa, I have my wish."
    show cs at mid_right with move
    n "CS whispers into Santa's ear."
    n "Santa's eyes widen."
    santa "Ho ho ho! Well..."
    santa "I guess I could do that."
    scene snowed_in
    show cs sil_black:
        zoom 0.15
        xpos 0.3
        ypos 0.5
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.4
        ypos 0.5
    show arceus sil_black:
        zoom 0.15
        xpos 0.54
        ypos 0.54
    show anno sil_black:
        zoom 0.15
        xpos 0.53
        ypos 0.33
    show tate festive sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.36
    show obama sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.47
    show ed sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show rich sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.34
    show wesley sil_black:
        zoom 0.15
        xpos 0.56
        ypos 0.45
    show blank sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.34
    show nova sil_black:
        zoom 0.15
        xpos 0.55
        ypos 0.43
    show copguy sil_black:
        zoom 0.15
        xpos 0.33
        ypos 0.35
    show billy sil_black:
        zoom 0.15
        xpos 0.63
        ypos 0.46
    show aria sil_black:
        zoom 0.15
        xpos 0.42
        ypos 0.36
    show kitty sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.46
    show grace sil_black:
        zoom 0.15
        xpos 0.31
        ypos 0.31
    show anne sil_black:
        zoom 0.15
        xpos 0.34
        ypos 0.42
    show elizabeth sil_black:
        zoom 0.15
        xpos 0.38
        ypos 0.45
    show digi sil_black:
        zoom 0.15
        xpos 0.47
        ypos 0.46
    show linus sil_black:
        zoom 0.15
        xpos 0.46
        ypos 0.35
    show luke sil_black:
        zoom 0.15
        xpos 0.32
        ypos 0.45
    show db sil_black:
        zoom 0.15
        xpos 0.5
        ypos 0.6
    show k17 sil_black:
        zoom 0.15
        xpos 0.43
        ypos 0.2   
    show k22 sil_black:
        zoom 0.15
        xpos 0.45
        ypos 0.23
    show santa sil_black:
        zoom 0.15
        xpos 0.65
        ypos 0.5    
    show snow1
    with dissolve
    santa "Alright! Stand back everyone! This is gonna take a lot of focus!"
    n "Santa harnesses most of his Christmas spirit energy to create CS' wish."
    show nu_finish sil_black:
        zoom 0.75
        xpos 0.7
        ypos -0.35
    with moveintop
    pause 1.0
    show nu_finish:
        zoom 0.75
        xpos 0.7
        ypos -0.35
    with dissolve   
    santa "Ta-dah!"
    cs "Wow, that really worked!"
    billy "A giant bottle of Crotch Doctor?"
    copguy "Yeah, it can instantly melt snow!"
    copguy "It's one of my pitches, I also pitch car products as a side gig!"
    cs "Wait, your Carguy?"
    copguy "Man, I literally look like him. How have you never picked that up?"
    stop music fadeout 3.0
    music end
    show nu_finish:
        zoom 0.75
        xpos 0.5
        ypos -0.4
        linear 15 rotate -60
    santa "Ho ho, oh no. It's tipping towards us."
    santa "Oh, shit."
    scene black with dissolve
    play sound sfx_splash
    n "A tsunami of car cleaner engulfs the group, as they get washed off the roof."
    n "As everyone gathers their bearings once again, they look around, watching the waves of Crotch Doctor carrying all the snow away."
    scene cs_house_night_dtree
    show cs at mid_left
    show tate festive at left
    show obama festive at mid_right
    show copguy festive at mid_mid_right
    show k17
    show santa at right
    with dissolve
    cs "Woohoo! We did it! The avalanche covering the house is gone!"
    santa "Ho ho, well, it looks like you helped save Christmas, CS."
    santa "I need to get going however, I am slightly off schedule."
    santa "I should also make sure my steed didn't drown in car cleaner."
    cs "Good luck to you, Santa!"
    hide santa with moveoutleft
    show k17 happy
    k17 "CS? Did you see that?"
    cs "Yeah, I was kind of there with everyone one."
    show k17 disappointed
    k17 "Sorry, that was a stupid question."
    show k17
    tate "CS! You did it!"
    obama "I gotta say, that was one of the most fun Christmas parties I've ever been to."
    obama "Although, I should probably get back to The White House, the political circus is probably getting out of hand."
    hide obama with moveoutleft
    show sheriff at right
    sheriff "Hey guys, you got rid of the snow!"
    sheriff "What'd I miss?"
    cs "Uhhh..."
    play sound sfx_jingle volume 0.7
    n "As everyone is talking, the jingling of bells can be heard rushing over CS' house."
    santa "Ho ho ho! Merry Christmas everyone!"
    show snow3
    show snow4
    with dissolve
    n "As Santa flies past, the snow begins to fall again."
    sheriff "Well Copguy, we should probably get going before we get snowed in again!"
    hide sheriff
    hide copguy
    with moveoutright
    copguy "Look how shiny our car is!"
    scene cs_house_night_dtree
    show billy at mid_left
    show k22 disappointed at mid_right
    with dissolve
    n "As everyone is wrapping up to go home, K-22 and Billy have a bit of a chat."
    k22 "Hey Billy, can I talk to you for a minute?"
    billy "Sure thing! I have a moment."
    k22 "I uhh... had a customer who wanted you to make something for them."
    n "K-22 hands Billy a folded up piece of paper."
    k22 "All of the instructions are on there I was told."
    k22 "Follow them word for word."
    n "Billy opens up the paper and skims through it."
    billy "Wow."
    billy "This is great! I'll get to work on this soon."
    billy "I gotta take a trip to France."
    billy "I need to, fix an old friend."
    show k22
    k22 "Alrighty well, see you later Billy!"
    billy "See ya!"
    n "Both parties get into their cars and drive off."
    scene cs_bedroom1
    show cs happy at center
    with dissolve
    cs "That was such a blast!"
    cs "Plus my car got cleaned for free!"
    cs "What a mess, though. I'm gonna wait for tomorrow to clean this up."
    cs "Maybe I can call Anno again to help!"
    cs "For now, I should probably get to streaming."
    cs "Those car crash compilations aren't gonna watch themselves!"
    scene black with dissolve
    n "As CS entered his room to start streaming, our story here comes to a close."
    n "It wasn't the Christmas that CS expected, but it was one of the jolliest times he's had."
    n "Merry Christmas, and have a Happy New Year!"
    pause 5.0

    # Epilogue
label dx_christmas_epilogue:
    show billycar1:
        zoom 2.5
    show billycar1 at Move((-1.5, -1.0), (0.0, -1.25), 10, repeat=False, bounce=False, xanchor="left", yanchor="top") with dissolve
    billy "Dammit, where did I put my handy switch?{w=9}{nw}"
    show billycar2:
        zoom 2.5
    show billycar2 at Move((0.0, -0.25), (-1.5, 0.0), 10, repeat=False, bounce=False, xanchor="left", yanchor="top") with dissolve
    billy "I swear I had a spare here somewhere...{w=9}{nw}"
    show billycar3:
        zoom 2.5
    show billycar3 at Move((0.0, -0.25), (-1.25, -0.5), 10, repeat=False, bounce=False, xanchor="left", yanchor="top") with dissolve
    billy "Lemme check the back seat...{w=9}{nw}"
    window hide
    show christmas_finisher with dissolve
    pause
    # Pan over shot of the schematic for the Billy pot

