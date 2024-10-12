label dx_christmas_start:
    play music lets_hear_winter volume 0.7
    scene black
    n "CS wakes up to a snowy winter morning."
    cs "Yes! It snowed today!"
    n "CS looks at his calendar."
    cs "Woohoo!"
    cs "Christmas is almost here!"
    cs "...And you know what that means!"
    cs "I finally get to throw a huge Christmas party at my house!"
    cs "I'm so pumped, I should call everyone again to make sure they are coming."
    n "CS calls all of his guests who he invited a couple weeks ago."
    cs "Alright, well, the party is going to start in 2 days."
    cs "I have not prepared at all."
    cs "Fuck."
    cs "Okay, well first place I need to start is by checking out my house."
    cs "I have this huge mansion, and I don't even use the rest of my house!"
    cs "Let's go look."
    n "CS walks into his living room."
    cs "Well, okay maybe I should bring in the Christmas supplies first."
    cs "Let's go see what we have."
    n "CS goes into his garage."
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
            jump dx_christmas_decor
        if decor_first:
            jump dx_christmas_lights
    $ tree_first = True
    if tree_first:
        cs "I should get the Christmas tree first."
        cs "Who doesn't wanna get this thing out? This is the best part of decorating!"
        cs "I just, need to be, careful..."
        cs "Hnng..."
        n "All of a sudden, the shelf tips and all of the supplies fall onto CS!"
        cs "Shit!"
        # crashing SFX
        cs "Ow..."
        n "CS gets himself out of the mess of lights, garland, and Legos."
        # CS steps on a Lego.
        cs "Fuck!"
        cs "Man, what a mess! "
        cs "This is gonna take forever to clean up!"
    jump dx_christmas_anno


# Decorations/lights
label dx_christmas_lights:
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if tree_second or decor_first:
        cs "Alright, I should probably get the lights and garland next."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
        if tree_second:
            jump dx_christmas_decor
        if decor_first:
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
            jump dx_christmas_lights
        if lights_first:
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
    cs "Maybe I should call someone over to help."
    cs "Lemme see if Anno is around..."
    n "CS decides to call Anno."
    anno "Hello?"
    cs "Hey Anno, CS here!"
    anno "Yes, I know the party is in two days, you just called me."
    cs "Well, I was wondering..."
    cs "If you wanted to help me decorate my house!"
    anno "I still have to get a gift for the gift exchange..."
    anno "...But I can do that tomorrow."
    anno "I'll come over. Be there soon."
    cs "Cool!"
    cs "Alright, I got Anno to come over and help out!"
    cs "I guess I'll just plan out how I want the house to look."
    cs "Actually, shit, it snowed last night!"
    cs "I need to shovel before Anno gets here!"
    n "CS gets dressed and goes out into the garage to get his shovel."
    if tree_first:
        cs "Shit! I hate Legos, but only when they're in my feet!"
    cs "Okay, now the real question is, how much did it snow?"
    n "CS presses the garage button, and nothing happens."
    cs "Damnit, I think it's iced shut."
    cs "I'm gonna have to go out in front."
    n "When CS gets outside, he finds a massive snow drift blocking his garage."
    cs "Well that's just great."
    cs "This is gonna take an hour at least to scoop this all up."
    cs "I better get to it, I guess."
    n "As CS is about 10 minutes into shoveling, CS hears someone walking up his driveway."
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
    n "Carguy turns and trots away though the snow as fast as he can go."
    cs "Well that was a huge waste of time!"
    cs "I really need to finish shoveling my driveway, my face is starting to freeze!"
    n "As CS finishes scooping up the driveway, Anno's car pulls up on his street."
    cs "Just in time!"
    n "CS greets Anno as he pulls up on his driveway."
    anno "Hey, how's it going?"
    cs "Cold. Very cold."
    cs "Let's get inside please it's freezing."
    n "CS and Anno huddle inside and take their jackets off, while they make their way into the living room."
    n "They sit on the couch and catch up with each other while they get warmed up."
    anno "Well CS, how have you been doing?"
    cs "Good! I've enjoyed not being chased by the cops again and just living a roughly normal life."
    anno "Yeah, how was your trip back home after all that? We haven't really talked much since then."
    cs "Well, I had a blast working for LTT for a few days, but eventually I had to escape again because the cops came after us."
    cs "I eventually proved to the cops that I wasn't guilty, and then Billy Mays took us home."
    anno "How the hell did you manage to come across Billy Mays?"
    cs "Crazy coincidence I guess, but it was fun though! I won a golden pencil sharpener!"
    anno "The cops never came after me, so I tried to start up a band, but it didn't really work out."
    #Christmas tree first
    if tree_first:
        anno "By the way, where are all of the decorations?"
        cs "Ah yes, it's all in the garage. I'll show you."
        n "Anno follows CS to his garage."
        n "As they enter the garage, Anno gawks at the mess on the floor."
        anno "Damn bitch, you live like this?"
        cs "...I may have had small mishap when I was trying to get the tree out."
        anno "Small?!"
        cs "Do you think you can help me?"
        cs "I figured it'd be faster if I had a helping hand."
        n "Anno groans."
        anno "I was hoping to be setting up decorations, not cleaning them up."
        anno "...But I guess I don't really have any other option, do I?"
        cs "Here, I'll grab these boxes, and we'll start throwing stuff in them."
        n "After about an hour, they manage to clean up the mess, without stepping on too many Legos."
        n "CS and Anno drag the boxes inside."
    #Setting up decorations
    cs "Well Anno, are you ready to start decorating this place?"
    anno "Yeah! Where do you wanna start?"
    #Living room
    #Kitchen
    #Hallway
    #Entrance
    #Outside
    #After
    cs "Thanks Anno! You really rizzed up my crib!"

    #Day 2
    n "After a good night's sleep, CS slowly wakes up to read the time."
    cs "Huh?"
    cs "Oh shit! It's 2pm already?"
    cs "I should go get all my shopping done!"
    n "CS jolts out of bed and gets ready for the day."
    cs "Thankfully it didn't snow anymore, otherwise my car would have been snowed in!"
    n "CS gets in his car and figures out where to go."
    cs "I went to Walmart last time because they had a deal, but I never shop there regularly."
    cs "To Target we go!"
    n "CS starts up his car and heads to Target."
    cs "Now this is a real store!"
    cs "Everything is mostly clean and neat, no depressing lighting and messy aisles..."
    cs "I should probably stop praising the store and actually buy the groceries I need."
    #Shopping
    n "CS heads over to the grocery aisles."
    cs "Well I need to get some Genergy, of course."
    #Checkout
    n "CS heads over to the checkout lanes."
    cs "Wait, what?"
    cs "There are no lanes open! How the hell am I supposed to check out?"
    cs "Oh wait, I guess self-checkout is open..."
    n "CS gets in the long line wrapped around the self-check area."
    cs "Man, this place is really short staffed, especially for the holidays!"
    customer "They're always like this. I come every day, and they definitely have been losing employees."
    cs "Yikes, I wonder why..."
    cs "Finally, I can checkout."
    n "As CS is checking out, the machine beeps at him."
    cs "What? I scanned this twice? No I didn't!"
    tgt_worker "Oh yeah, it always does that, keep going."
    cs "Okay."
    cs "Ah crap, I scanned this one too many times."
    n "The worker comes back."
    tgt_worker "Hello, what's wrong?"
    cs "Sorry, I scanned this pie 7 times."
    tgt_worker "...how many do you have?"
    cs "I have 2."
    tgt_worker "Wh-- okay hold on."
    tgt_worker "There you go."
    cs "Thanks!"
    cs "Hey wait a minute!"
    n "The target employee runs back over."
    cs "These are ringing up 11.99 per pie!"
    cs "They said they were like 20% off on the sign over there!"
    tgt_worker "Hmm..."
    n "The employee scans the pie."
    tgt_worker "Do you perchance have Target Circle?"
    cs "No?"
    tgt_worker "You need Target Circle to get this deal. Sorry."
    cs "Really?"
    tgt_worker "I'm sorry, but that's just how the deal works."
    cs "Fine, whatever, I'll just keep them."
    n "When CS goes to scan his alcohol, it beeps again and tells him to get out his ID."
    cs "Seriously?!"
    n "The employee runs over again."
    tgt_worker "Oh yeah. I should probably do that for you."
    n "The employee signs into the machine and opens the prompt to enter an ID."
    n "They then wait patiently for CS."
    cs "What? Do you need something from me?"
    tgt_worker "Yeah, I need to check your ID."
    cs "Are you kidding me?"
    tgt_worker "Yes, they will kill me if you don't do it."
    n "CS sighs."
    cs "Here you go."
    n "The target employee punches in his birthday and leaves."
    cs "Kids these days, asking me for my ID..."
    cs "They should hire some new people!"
    cs "Anyways, I need to get home now and put everything away."
    cs "It's the big day tomorrow, and it's gonna be the best party ever!"
label dx_christmas_aftershop:
    n "When CS gets home, he starts putting the groceries away."
    n "As he's finishing up, a D20 he had sitting on the counter gets knocked onto the floor."
    cs "What the hell? When did I ever have one of these?"
    n "CS picks up the die."
    cs "Hey, I got a [d20]!"
label dx_christmas_party_before:
    cs "Today is the day!"
    cs "Now I just have to wait for people to arrive!"
    cs "I wonder who will arrive first?"
    if d20 == 1:
        n "CS waits paiently."
        n "He keeps on waiting."
        cs "Alright, any minute now..."
        cs "The party starts here in about 15 minutes, so people should start showing up soon..."
        n "CS keeps on waiting, but it looks like no one shows up early."
    if d20 == 2:
        n "As CS asks himself this, "
    if d20 == 3:
        n "CS peers out the window to see Anno's car pull into the driveway."
        cs "Hey look at that! Anno's here first!"
        anno "Hey CS!"
        anno "I showed up kinda early, but I wanted to see everyone's initial reactions of our decor work!"
        cs "Well I'm glad you showed up, come inside! It's cold out."
    if d20 == 4:
        n "All of a sudden, CS hears a futuristic sounding vehicle land outside."
    if d20 == 5:
        n "As soon as he says that, he feels the house start to shake."
        cs "Wh-- What's going on?"
        n "As the house shakes even faster, a loud train whistle bellows out."
    n "By the time of the party, everyone shows up at CS' house in droves."