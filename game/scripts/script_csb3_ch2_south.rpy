label south:
    cs "Why don't we try going south?"
    show arceus
    arceus "Alright, what's your plan? Where are we going, exactly?"
    cs "I've always kinda wanted to go down to Vegas. We could have a ton of fun down there!"
    show arceus worried
    arceus "Don't you want to go back home?"
    cs "Listen, we are free again, and we're in the middle of nowhere. If we can find a way to make a bit of cash and get a car, maybe we can make it big!"
    show arceus angry
    arceus "This sounds like an awful idea."
    pause 1.0
    show arceus
    arceus "Eh, fuck it. What do I have to lose at this point? Let's go!"
    show cs happy
    cs "Hell yeah!"
    scene black with fade
    n "CS and Arceus keep following the road for a while until they come across a small town."
    scene town with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    cs "Oh my God! We found civilization again!"
    arceus "Thank God."
    n "The two look around for a bit until they see a gas station close by."
    cs "Let's head over to that gas station so we can pick up something to eat."
    n "CS and Arceus head over to the convenience store at the gas station."
    hide cs with moveoutright
    show arceus flipped at right
    hide arceus with moveoutright
    scene gasinside with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    arceus "Finally, some good fucking food."
    cs "Donuts and chips have never tasted better."
    arceus "Thank God the slushie machine was working for once." 
    n "After they finish their food, they start to plan their epic journey to Vegas."
    scene gasoutside with fade
    show cs at left
    show arceus flipped at right
    with moveinleft
    show arceus with determination
    cs "Okay, so, how do we get down to Nevada? That's quite a distance."
    arceus "We could use those bikes over there?"
    cs "Nah, that's too much effort."
    cs "How about..."
    cs "Hold on. I got an idea."
    play music "brick_by_dick.mp3"
    music Brick by Brick (Suck my Dick) - cs188
    cs "See those pieces on the ground?"
    show arceus worried
    arceus "What pieces?"
    n "CS quickly starts grabbing material from thin air and puts together a new car."
    play sound "sfx_legosfx.mp3" volume 1
    pause 3.0
    cs "Tada!"
    arceus "{i}How did you do that?!"
    cs "Look, I'm a master builder. You wouldn't understand."
    arceus "Well... does the car even work?"
    cs "Only one way to find out!"
    stop music fadeout 3.0
    music end
    scene gasoutside
    show cscar1
    show cscar2
    with fade
    show cs at left behind cscar2 with moveinleft
    show arceus at right behind cscar2 with moveinright
    n "Once they get into the car, CS starts it up."
    play sound "sfx_driving.wav" volume 0.5
    pause 1.0
    cs "Woohoo! Vegas time!"
    arceus "I don't even know how you do these things, man, but let's go!"
    n "The duo heads out to Vegas, or, where they presume Vegas is."
    stop sound fadeout 2.0
    scene black with fade
    n "After many hours of driving, day turns to night once again."
    stop music fadeout 3.0
    music end
    jump utah

label utah:
    scene utah
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with fade
    arceus "Are you sure we're close to Vegas?"
    cs "We {i}have{/i} to be! Nevada is, like, right below Washington!"
    arceus "Well, there's a state sign coming up. Let's see if you're right."
    if fun_value(20):
        scene utajsign
        show cscar1
        show cscar2
        show cs at left behind cscar2
        show arceus at right behind cscar2
        n "As they approach the sign, it reads \"Welcome to UTAJ, Life Elevated\"."
        arceus "Welp. You tried."
        cs "I could've sworn we were going the right way."
        arceus "Did you ever see a sign that said \"Las Vegas - in however many miles\"?"
        cs "No...?"
        arceus "Oh, well. At least we know where we are now."
        arceus "Tomorrow, we'll head to Vegas."
        arceus "Let's find somewhere to eat before we hit the hay tonight."
        n "They continue driving for a bit until they come across a small town."
    else:      
        scene utahsign
        show cscar1
        show cscar2
        show cs at left behind cscar2
        show arceus at right behind cscar2
        n "As they approach the sign, it reads \"Welcome to UTAH, Life Elevated\"."
        arceus "Welp. You tried."
        cs "I could've sworn we were going the right way."
        arceus "Did you ever see a sign that said \"Las Vegas - in however many miles\"?"
        cs "No...?"
        arceus "Oh, well. At least we know where we are now."
        arceus "Tomorrow, we'll head to Vegas."
        arceus "Let's find somewhere to eat before we hit the hay tonight."
        n "They continue driving for a bit until they come across a small town."

    scene utahnight
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with dissolve
    cs "Alright, let's start looking for a place."
    cs "We got, like, Joe's Diner over there, there's a Casey's..."
    cs "Grilled Mormons? Ewww!"
    arceus "There's uhh... The Soup Store?"
    cs "Nah, that's a clothing store."
    arceus "Oh, weird."
    cs "Wait, hold up! I think I see a pizza place!"
    arceus "Man, pizza {i}does{/i} sound good right about now."
    cs "Woah, what? It's a Lego pizza place?"
    cs "We're going there. {i}Right now."
    n "CS pulls into the parking lot of the restaurant."
    scene pizzaplace with fade
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "I've never seen this before!"
    cs "Lego NXT Entertainment? They must have those robotic Lego things inside!"
    show arceus worried dark
    n "Arceus looks worried."
    arceus "Are you sure about this, CS? This place gives me the creeps."
    cs "This is my dream place to eat at. We {i}need{/i} to see if we can get in."
    scene legodoor with fade
    show cs dark at left with moveinleft
    show arceus worried dark at right with moveinright
    n "They approach the front door. There is a sign on the door that reads \"CLOSED.\""
    arceus "Dang, that suuuuuure sucks. We can leave now, right?"
    scene legodooropen
    show cs dark at left
    show arceus worried dark at right
    n "CS pushes the door open."
    cs "The door isn't locked! We can go in!"
    arceus "Oh, great. Yippee..."
    scene black with fade
    n "As CS and Arceus walk in, they are greeted with a musty aroma and a dimly-lit party room."
    scene fazlobby with fade
    play music "<loop 0>tunnely_shimbers.mp3" volume 0.5
    music Tunnely Shimbers - Mr. Sauceman
    n "CS walks around in awe as Arceus creeps behind him."
    show cs dark at left with moveinleft
    show arceus flipped dark at right with moveinleft
    show arceus dark
    if fun_value(25):
        pause 1.0
        show fumobee at lego_run
        play sound "secret/sfx_vine.mp3"
        with move
        pause 1.0
        show arceus worried dark
        arceus "Ahhh!! FUCK!"
        show arceus angry dark
        arceus "Please CS, can we {i}not{/i} go to the one place with a {i}bee?{/i}"
        cs "No? It's just a plushie..."
        cs "Anyways..."
    cs "Wow, a Lego-themed pizza restaurant. This place looks like it was built out of Lego, too!"
    cs "Woah, Arc, look at those giant minifig statues!"
    n "Up in the front of the room, four human-scale Lego minifigures can be seen standing up on the stage."
    n "CS goes up to stand next to them."
    scene legostage with fade
    show cs dark at left with moveinleft
    cs "Arceus, do you have a camera? You should take a picture of me!"
    arceus "No, why would I have a camera? Also, you probably shouldn't be up there!"
    arceus "Weren't we gonna get some pizza?"
    pause 1.0
    arceus "Do they even {i}have{/i} pizza here? I can smell it, but it doesn't look like anyone's here."
    cs "I see it in the back by the counter!"
    n "CS hops off stage and runs over to the serving counter."
    hide cs with moveoutright
    scene fazlobby
    show cs dark at left
    show arceus dark at right
    with fade
    n "A couple boxes of freshly-baked pizza are sitting there."
    show arceus worried dark
    arceus "It's hot, too! Who {i}made{/i} this?"
    cs "The cook who works here, duh!"
    arceus "The place was closed, CS."
    cs "Well, then, why would the cook be in the back making pizzas?"
    show arceus angry dark
    arceus "Because there is-- Whatever, let's just find a place to sit down and eat."
    arceus "... And not out here. I don't wanna look at those creepy minifigures."
    cs "Fine..."
    n "CS and Arceus head down the hallway next to the kitchen area until they find a small office in the back."
    scene fazplace with fade
    show cs dark at left with moveinleft
    show arceus flipped dark at right with moveinleft
    show arceus dark
    arceus "Perfect. Let's eat in here, then we get back in the car."
    cs "Aww, I wanted to spend the night here!"
    show arceus angry dark
    arceus "No fucking way, dude."
    show arceus dark
    n "CS notices a Lego RC car sitting on the desk with a controller."
    cs "Ah, sweet! I used to have one of these!"
    n "As CS turns it on, the TV screen next to them turns on as well, and shows live footage from the Lego car."
    scene tvcar with dissolve
    cs "Hey, look at that! We can see where the car goes!"
    cs "While we eat, I'm gonna take the car around the restaurant and see if we can find anything cool."
    arceus "Alright, just don't break it."
    n "CS drives the car outside of the office and into different rooms."
    cs "This already feels like a cool vacation. I'm glad we managed to find this."
    arceus "Well, at least {i}you're{/i} happy."
    cs "Weren't there supposed to be robotic Legos though? I was looking forward to tha-- Heyyy!!!"
    scene fazplace
    show cs disappointed dark at left
    show arceus dark at right
    arceus "What? What's going on?"
    cs "The minifigs! One of them is gone!"
    show arceus worried dark
    arceus "{i}What?"
    arceus "CS, we need to get the fuck out of here, {i}now!"
    cs "But I haven't finished my pizz--"
    arceus "I don't care! Let's go!"
    stop music fadeout 3.0
    music end 
    n "Arceus drags CS by the arm as they run out of the office and down the hallway."
    show cs disappointed dark flipped with determination
    hide cs
    hide arceus
    with moveoutleft
    scene fazhall
    show lego at truecenter
    with fade
    show cs dark at mid_left_left with moveinleft
    show arceus worried dark at mid_right_right with moveinright   
    n "Before they make it to the door, Arceus stops dead in his tracks."
    cs "Hey! Why'd we stop?"
    n "CS looks ahead of him to see the giant minifigure standing in front of them."
    cs "Ohh."
    arceus "CS, don't move a muscle."
    cs "Why not? It's just a Leg--"
    play music "<loop 0>hard_drive.mp3" volume 0.5
    music Hard Drive to Munch You - Mr. Sauceman
    show lego eyes
    n "The minifigure's eyes glow as it raises its arms up and starts running at CS."
    lego "HEEYYYY!!!!!"
    n "Arceus quickly drags CS out of the way at the last second."
    show arceus dark at left
    show lego eyes at lego_run
    with move
    lego "A MAN HAS FALLEN INTO THE--"
    hide lego with moveoutbottom
    n "The minifigure crashes into the wall and falls to the ground."
    show cs worried dark with vpunch
    n "The other figures up ahead turn on and start moving toward Arceus and CS."
    show arceus worried dark
    arceus "{bt=a3-p10-s4}Run, CS, run!!!"
    n "They desperately run as fast as they can to the front door, then slam the door behind them."
    scene pizzaplace with fade
    show cs worried dark at left with moveinleft
    show arceus worried dark flipped at right with moveinleft
    show arceus worried dark
    n "The minifigures run up to the door and smash their arms and heads through."
    arceus "To the car! Get in the car!"
    show cs worried dark flipped with determination
    hide cs
    hide arceus
    with moveoutleft
    n "Arceus hops in the driver's seat while CS gets in the back."
    scene pizzaplace
    show cscar1arc
    show cscar2
    show arceus flipped at left behind cscar2
    with fade
    cs "I made this car though..."
    n "Arceus starts the car. He takes off at lightning speed out of the parking lot and back onto the road."
    scene black with fade
    stop music fadeout 3.0
    music end
    scene utahnight
    show cscar1arc
    show cscar2
    show arceus flipped at left behind cscar2
    with fade
    arceus "Thank God. I can take a breather now."
    cs "Man, this sucks."
    cs "It was super cool before the Legos tried to kill us."
    arceus "I think that whole restaurant was trying to kill us, CS."
    n "Arceus drives the rest of the way until they reach Las Vegas."
    jump vegas

label vegas:
    if returning_from_blooper:
        if fun_value(10):
            scene vegasjade
            $ jade = True
        else:
            $ jade = False
            scene vegas
        show cscar1
        show cscar2
        show arceus flipped at left behind cscar2
        with determination
        play sound "sfx_clapperboard.wav"
        play music "<loop 0>penthouse.mp3" volume 0.5
        music "Al's Penthouse - Andy Blythe"
        $ returning_from_blooper = False
    else:
        if fun_value(10):
            $ jade = True
            scene vegasjade
            $ persistent.seen.add("bubble")
        else:
            $ jade = False
            scene vegas
        show cscar1arc
        show cscar2
        show arceus flipped at left behind cscar2
        with fade
    play music "<loop 0>penthouse.mp3" volume 0.5
    music "Al's Penthouse - Andy Blythe"
    n "After a few hours of driving, the duo sees the bright Las Vegas sign coming into view."
    cs "Woohoo! We're almost there!"
    arceus "Some reckless gambling will probably help me forget about the horrors from that restaurant..."
    n "They enter Las Vegas and find a place to park, then they start heading down The Strip."
    if jade:
        scene vegasjade2 with fade
    else:
        scene strip with fade
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "Alright, Arc, you ready to get rich?"
    show arceus happy dark
    arceus "I doubt we will, but, hell yeah! Let's go!"
    show arceus dark
    arceus "Do you want to get something to eat first? I see a place called Pasta... Italy... something.{w=1.0} They probably have food."
    cs "Why would we eat? We just got here, and I wanna gamble!"
    cs "Look over there! SlotsaFun! That looks like a cool place to start!"
    arceus "Alright, sure, I guess I can find something to eat there... Probably."
    show arceus dark flipped with determination
    hide cs dark
    hide arceus dark
    with moveoutright
    n "CS and Arceus enter the casino. It looks like chaos is unfolding in front of their faces."
    scene casino1 with fade
    play sound "sfx_slots.mp3" volume 3
    n "The sounds of slot machines fill the room. Many drunkards hobble around the establishment."
    show cs at left with moveinleft
    show arceus at right with moveinright
    show arceus worried
    arceus "Oh, God, I already feel like I have a migraine..."
    cs "C'mon, Arc, let's go play some slots!"
    hide cs dark with moveoutright
    n "CS starts looking around for a machine to sit at."
    arceus "Hold on, CS, I need a minute."
    n "A drunk lady bumps into Arceus."
    show trailtrash flipped at mid_right with moveinleft
    show trailtrash flipped with hpunch
    show trailtrash flipped at center with move
    arceus "Huh?"
    trailtrash "I need a new trailer!"
    arceus "No, I'm sorry, I--"
    trailtrash "I {i}need{/i} a new trailer!"
    show bouncer1 at center with moveinleft
    show bouncer2 at mid_mid_left behind trailtrash with moveinleft
    n "Two guards approach the lady and drag her towards the elevator."
    hide trailtrash
    hide bouncer1
    hide bouncer2
    with moveoutleft
    arceus "Thank goodness."
    arceus "I need to sit down."
    show arceus flipped with determination
    hide arceus with moveoutright
    n "As Arceus wanders off to find a place to relax, CS tries his luck at the slots."
    scene slots with fade
    cs "C'mon, this is the one!"
    cs "Bars, {w=1.0}bars, {w=1.0}football player with a{w=0.5} hot...dog...?"
    cs "Damn it! So close!"
    cs "I haven't won anything, and I've already spent most of my money..."
    cs "I wonder what Arc is up to. I haven't seen him at all."
    n "CS gets up from the slot machine and begins looking for Arceus."
    scene casino1 with fade
    n "CS looks around for a while, but he can't find Arceus."
    show cs disappointed at center with moveinleft
    cs "Arceus! Hello?"
    cs "Where did he go?"
    cs "Maybe he went to the table games. I'll go check over there."
    hide cs with moveoutright
    n "CS heads over to the table games section to search for Arceus."
    scene tablegames with fade
    show cs disappointed at center with moveinleft
    cs "Arceus, are you around here?"
    cs "I've checked all the tables and I still can't find him!"
    cs "Maybe I should leave. He might've gone to that restaurant, or whatever it was."
    stop music fadeout 3.0
    stop sound fadeout 2.0
    music end
    unknown "Hey, you!"
    show cs disappointed flipped
    cs "Huh? Me?"
    n "CS notices a well-dressed man smoking a cigar and waving him over."
    unknown "Yeah, you! Come over to the poker tabeh! {i}coughs{/i} I bet I can beat you!"
    cs "I guess this is my last chance to make it big. It's worth a shot."
    cs "Alright, sure, I'll play a round, but I don't have much."
    unknown "Arright, great! Come sit down here."
    hide cs with moveoutleft
    n "CS sits down at the poker table and notices that the man's skin is a putrid green."
    n "CS looks disgusted, but shrugs, as he doesn't want to start trouble now."
    scene luigi2
    show green flipped at left
    with fade
    show cs disappointed flipped at right with moveinright
    play music "<loop 0>laurel_palace.mp3" volume 0.5
    music Laurel Palace - Manami Matsumae
    green "Deal us some cards arready!"
    scene luigi1
    show green flipped at left
    show cs disappointed flipped at right
    n "The house deals the cards out to Mr. Green and CS."
    scene pokertable with fade
    show cards1
    green "Hahahaha! I can tell this one's a winner!"
    n "CS looks at his cards. He's got an ace of spades and a king of spades."
    show cards2
    n "The dealer lays down a nine of hearts, an eight of clubs, and a queen of spades."
    green "Arright! I'm puttin' one million in!"
    cs "One {i}million?!{/i}"
    green "Heheh, is that all you got?"
    pause 1.0
    n "CS ponders for a moment, wondering if he should risk it all."
    menu:
        "Fold" (type = "bad"):
            jump folded
        "Stand" (type = "good"):
            jump poker

label poker:
    cs "No. I'll stand."
    green "Bwahahaha! You think you can beat me?"
    scene luigi1
    show green flipped at left
    show cs flipped at right
    pause 1.0
    scene pokertable
    show cards3
    n "The dealer draws a ten of spades."
    green "Ten million! You're bluffing! I can see through you!"
    menu:
        "Fold" (type = "bad"):
            jump folded
        "Stand" (type = "good"):
            jump poker2

label poker2:
    cs "I'm still gonna stand."
    green "I'm gonna be rich! You better have that money on you, boy!"
    scene luigi1
    show green flipped at left
    show cs flipped at right
    pause 1.0
    scene pokertable
    show cards4
    n "The dealer draws a jack of spades."
    green "100 million! You better drop out {i}coughs{/i} rrright now!"
    menu:
        "Fold"  (type = "bad"):
            jump folded
        "Stand"  (type = "good"):
            jump poker3

label folded:
    scene luigi2
    show green flipped at left
    show cs disappointed flipped at right
    cs "Yeah, I'm out. I can't risk that much."
    green "Hahahaha! That's what I thought, bucko!"
    green "Now scram!"
    show cs disappointed with determination
    hide cs at right with moveoutright
    n "CS sulks back to the lobby."
    scene casino1 with fade
    stop music fadeout 3.0
    music end
    show cs disappointed at center with moveinleft
    cs "Damn, I really thought I was gonna win something!"
    cs "This wasn't as cool as I thought. I guess I should go find Arc."
    cs "I wonder where he went..."
    hide cs with moveoutright
    n "CS returns to the search for Arceus."
    scene black with fade
    n "Meanwhile, Arceus has been trying to win it big, but in a different kind of way..."
    scene outsafe
    show arceus full flipped at mid_right
    show drill at center_right
    with fade
    play sound "sfx_drill.ogg" loop volume 0.5
    arceus "Come on, I'm almost there..."
    pause 6.0
    show drillbreak at center_right
    play sound "sfx_drillbreak.ogg" loop volume 0.5
    show arceus full angry flipped
    arceus "Fuck!"
    hide drillbreak
    show arceus full flipped
    show drill at center_right
    play sound "sfx_drill.ogg" loop volume 0.5
    pause 6.0
    show drillbreak at center_right
    play sound "sfx_drillbreak.ogg" loop volume 0.5
    show arceus full angry flipped
    arceus "God!"
    hide drillbreak
    show arceus full flipped
    show drill at center_right
    play sound "sfx_drill.ogg" loop volume 0.5
    pause 6.0
    show drillbreak at center_right
    play sound "sfx_drillbreak.ogg" loop volume 0.5
    show arceus full angry flipped
    arceus "You broke-dick piece-of-shit drill!"
    hide drillbreak
    show arceus full flipped
    show drill at center_right
    play sound "sfx_drill.ogg" loop volume 0.5
    pause 3.0
    scene outsafeopen
    show arceus full flipped at mid_right
    with fade
    play sound "sfx_payday.mp3" volume 0.5
    $ achievement_manager.unlock("The House Doesn't Always Win")
    show arceus full happy flipped
    arceus "Hell yeah!"
    scene insafe with fade
    arceus "Look at all this loot! CS is gonna be so surprised..."
    n "While Arceus is looting the casino, CS continues his search."

    # variable for use in train route.
    $ money_stolen = True

    scene vegasbathroom with fade
    show cs disappointed at center with moveinleft
    cs "Hello? Arceus?"
    cs "Not in the bathroom..."
    cs "Maybe he went to the car?"
    cs "I guess I should go check. I'm kinda tired of this place anyway."
    show cs disappointed flipped with determination
    hide cs with moveoutleft
    scene black with fade
    n "CS heads out to the parking lot to find Arceus by the car."
    scene carpark
    show arceus at right
    with fade
    show cs at center with moveinleft
    cs "Hey! There you are! Where were you?"
    show arceus happy
    arceus "I was getting us the motherlode!"
    show bag at mid_right with dissolve
    n "Arceus opens a body bag revealing stacks of gold, bills, and jewels."
    show cs worried
    cs "{i}What??{/i} How did you win that much??"
    arceus "You think I {i}won{/i} this? Haha, no! I just broke open their vault!"
    cs "Arceus! That's stealing!"
    show arceus
    arceus "Yeah, and the casino steals from us. Slots are rigged, man."
    show cs disappointed
    cs "Yeah, I guess you're right. Oh, well."
    cs "Did anyone notice?"
    show arceus happy
    arceus "Nope! I 100 percent stealthed that!"
    show cs
    cs "Well, damn, sweet! Thank you so much, Arceus!"
    cs "We are millionaires now!"
    hide bag with dissolve
    show arceus happy
    arceus "Yeah! We can do whatever we wanna do now!"
    show arceus
    arceus "What would you like to do, CS?"
    menu:
        "Go to the airport":
            jump airport_bad
        "Don't go to the airport":
            jump noairport

label poker3:
    cs "Still standing."
    green "What?! You son of a bitch, you are so scrrewed!"
    scene luigi2
    show green flipped at left
    show cs flipped at right
    luigi "Alright, let's see your hands."
    pause 1.0
    scene pokertable
    n "Mr. Green and CS put their cards down."
    if fun_value(42):
        show cards5alt
        n "CS and Mr. Green both have a royal flush with ace and king of spades."
        stop music fadeout 3.0
        music end
        scene luigi2
        show cs disappointed flipped at right
        show green flipped at left
        cs "What? That can't be right!"
        show cs angry flipped
        cs "You cheated!"
        green "Hehehe, it doesn't matter becasue I'm gonna take all the money anyway!"
        green "Hahahahahahahahahahahahahahahaha!!!!!!{nw}"
        show lancer at center with moveintop
        show lancer with vpunch
        play sound "secret/sfx_explosion.mp3" volume 1.5
        show green at t_punchup with move
        pause 0.3
        play music "<loop 0>secret/lancer.mp3" volume 1
        music Lancer - Toby Fox
        lancer "Hey guys!"
        show cs worried flipped
        cs "What in the world??"
        lancer "I just found this cool shiny metal in the back, but it didn't taste very good."
        show case at mid_right with dissolve
        lancer "Here, have it, waiter dude!"
        lancer "See ya later!"
        hide lancer with moveouttop
        stop music fadeout 3.0
        music end
        pause 2.0
        show cs flipped
        cs "Well, then!"
        cs "Awesome, I guess!"
        cs "Time to show Arc!"
        show cs with determination
        hide case with dissolve
        hide cs with moveoutright
        scene casino1 with fade    
        n "CS continues to look for Arceus."
        show cs disappointed at center with moveinleft
        cs "Arc? Where are you?"
        cs "Maybe he went to the bathroom?"
        hide cs with moveoutright
        scene vegasbathroom
        show arceus worried at center
        with fade
        n "CS finds the bathroom, to see Arceus with his head up against the mirror."
        show cs at left with moveinleft
        cs "Hey, Arc! There you are! Are you okay?"
        arceus "My head hurts so bad..."
        arceus "I think I'm gonna head back to the car..."
        cs "Alright, I'm ready to leave too, because we just won a ton of money!"
        arceus "Wh... what?? Are you just trying to make me feel better?"
        cs "No joke! Look, let's head out to the car!"
        arceus "Alright..."
        hide arceus with moveoutleft
        pause 1.0
        show cs flipped with determination
        hide cs with moveoutleft
        scene carpark
        show arceus flipped at left
        with fade
        show cs flipped at right with moveinright
        cs "Hey Arc, how're you feeling?"
        arceus "I do feel better now, yeah."
        arceus "I think it was just too much sensory overload for me."
        cs "Well that's good to hear."
        cs "What's also good to hear is that we are rich as hell!"
        show cs happy flipped
        show case flipped at right
        n "CS opens the case to reveal loads of gold bars and diamonds."
        show arceus happy flipped
        arceus "Holy shit! We're loaded!"
        show arceus flipped
        arceus "I can't believe I missed your big win."
        show cs flipped
        cs "Oh yeah, I don't really know what happened. Some blue kid gave this to me."
        arceus "Oh, that's weird as hell."
        cs "Yeah, but it's legit though! So I'm not complaining."

    else:
        show cards5
        n "CS has a royal flush with his ace and king of spades, while Mr. Green has a seven of hearts and a ten of clubs."
        n "Mr. Green vomits all over the table and falls over backwards, passing out."
        stop music fadeout 3.0
        music end
        $ achievement_manager.unlock("High Roller")
        scene luigi2
        show cs happy flipped at right
        cs "Woohoo! I won!"
        play music "<loop 0>price_right.mp3" volume 0.5
        music Price Is Right Theme - Edd Kalehoff
        luigi "Congratulations, sir, you just won 100 million dollars!"
        cs "Yay! I can pay for my Creative Cloud without donations!"
        n "CS jumps into the air and cheers."
        show cs flipped
        cs "Finally! Arc and I can buy whatever we want! I need to let him know!"
        n "Before CS runs off to find Arceus, the owner of the casino approaches CS."
        show jerma at left with moveinleft
        if fun_value(5):
            n "Jerma looks down at Mr. Green."
            jerma "Woah, clean up on aisle {i}you!"
            jerma "Anyways..."
        jerma "Well, look who we have here!"
        jerma "You beat my highest roller! How'd you do that?"
        cs "Uhh, I dunno."
        jerma "Well, congrats on your victory!"
        jerma "I'll go get the money for you. Mr. Green is gonna have to pay up to {i}me,{/i} now."
        cs "Alright! I'm gonna go find my friend real quick."
        jerma "Sure thing! Meet me back by the employee access area."
        show cs with determination
        hide cs with moveoutright
        stop music fadeout 3.0
        music end
        scene casino1 with fade    
        n "CS continues to look for Arceus."
        show cs disappointed at center with moveinleft
        cs "Arc? Where are you?"
        cs "Maybe he went to the bathroom?"
        hide cs with moveoutright
        scene vegasbathroom
        show arceus worried at center
        with fade
        n "CS enters the bathroom to see Arceus with his head up against the mirror."
        show cs at left with moveinleft
        cs "Hey, Arc! There you are! Are you okay?"
        arceus "My head hurts so bad..."
        arceus "I think I'm gonna head back to the car..."
        cs "Alright, I'm ready to leave too, because we just won 100 million dollars!"
        arceus "Wh- what?? Are you just trying to make me feel better?"
        cs "No joke! Look, head out to the car, and I'll meet you there!"
        arceus "Alright..."
        hide arceus with moveoutleft
        n "Arceus stumbles back out to the casino floor while CS goes to collect his winnings."
        show cs flipped with determination
        hide cs with moveoutleft
        n "CS meets Jerma in the employee backroom."
        scene backroomcasino
        show jerma at center
        show case flipped at mid_mid_left
        with fade
        n "Jerma is waiting with a briefcase."
        show cs at left behind case with moveinleft
        jerma "Here he is! The man of the hour!"
        cs "I honestly didn't think I was gonna win. I would've been in massive debt if I had lost."
        jerma "Well, good thing you won, because Mr. Green is in massive debt to us right now."
        jerma "Believe me, we've had a lot of money problems recently with Mr. Green! He's had to steal from our rival, Pasta Italiano."
        show cs disappointed
        cs "Yikes, that sounds shitty."
        show cs
        cs "Welp, I wish you the best of luck, Mr. Jerma!"
        show cs at mid_mid_left with move
        show case with determination
        show cs at left
        show case at left
        with move
        n "After CS collects his winnings, he finds his way back to the car."
        show cs flipped with determination

        # variable for use in train route.
        $ money_stolen = False

        hide cs
        hide case
        with moveoutleft
        scene carpark
        show arceus flipped at left
        with fade
        show cs flipped at right with moveinright
        cs "Hey Arc, how're you feelin'?"
        arceus "I do feel better now, yeah."
        arceus "I think it was just too much sensory overload for me."
        cs "Well, glad to hear you're feeling better!"
        cs "What's also good to hear is that we are rich as hell!"
        show cs happy flipped
        show case flipped at right
        n "CS opens the case to reveal loads of gold bars and diamonds."
        show arceus happy flipped
        arceus "Holy shit! We're loaded!"
        show arceus flipped
        arceus "I can't believe I missed your big win."
        show cs flipped
        cs "Oh, yeah, it was kinda funny! The man I won against puked all over the table and fell over!"
        arceus "Hahaha, I would've too if I lost that much money."
        cs "Yeah, that's true."
    hide case
    arceus "Alright, well, what's the plan now? We have so much money, we can do anything with it!"
    menu:
        "Go to airport"  (type = "good"):
            jump airport
        "Don't go to airport"  (type = "bad"):
            jump noairport

label airport:
    cs "We should head back home now. I have a plan for our newfound riches."
    show arceus flipped happy
    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"
    show cs flipped with determination
    show arceus with determination
    hide cs
    hide arceus
    with moveoutleft
    scene black with fade
    n "CS drives to the airport nearest to Las Vegas."
    scene airport_interior with fade
    play music "<loop 0>airport.mp3" volume 0.4
    music Airport Infilration - Marten Joustra
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    n "CS and Arceus pack up any belongings they have and head inside to the terminal."
    cs "What a crazy trip! That was really fun, Arc."
    arceus "Yeah, even though I was traumatized at the pizza place, I had a lot of fun."
    cs "Welp, let's go catch our plane!"
    hide cs
    hide arceus flipped
    with moveoutright
    scene airport_tsa
    show tsa at right
    with fade
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    n "CS and Arceus put their luggage on the conveyor and walk through the scanner."
    n "The scanner goes off when the briefcase goes through the x-ray machine."
    show cs disappointed
    cs "Huh?"
    tsa "We're gonna have to check this case."
    show tsa at center with move
    show case at center with dissolve
    n "The TSA agent opens up the briefcase, revealing all the riches from the casino."
    arceus "Oh, yeah, the winnings."
    n "The TSA agent looks through the case and finds a signed document from Jerma certifying the legality of the money."
    show tsa at right with move
    tsa "Alright, you guys are good to go."
    show cs
    cs "Phew! That was scary. I didn't even know that was in there!"
    show cs at center
    show arceus flipped at mid_right
    with move
    n "Arceus and CS collect their items again and get on the plane."
    hide cs
    hide arceus flipped
    hide case
    with moveoutright
    stop music fadeout 3.0
    music end
    scene airplane_seats with fade
    n "They go and sit down somewhere near the back of the plane."
    show cs flipped at mid_left
    show arceus at center
    with moveinright
    show cs
    cs "I want the window seat!"
    arceus "Alright, fine, can you hold on to the briefcase though? We can't have anyone steal this."
    cs "Yeah, okay."
    cs "But I'm not holding it the whole time!"
    n "The plane takes off and CS falls asleep."
    show cs concentrate
    arceus "Hey, have you ever flown before?"
    cs "Zzzz..."
    arceus "I guess he has."
    show arceus flipped
    arceus "That, or he's just really tired. I don't blame him."
    show arceus worried flipped
    arceus "I hate flying though, and I can't stop thinking about being in a flying metal tube."
    arceus "It'll be over soon enough."
    scene black with fade
    n "After a few hours, the plane arrives in New York."
    scene airport_inside with fade
    n "CS and Arceus get out of the plane and relax in the waiting area."
    show cs at left
    show arceus flipped at center
    with moveinleft
    show arceus
    cs "Woohoo! We are almost home!"
    arceus "Thank goodness I'm off that plane."
    arceus "Also, I just realized something, CS."
    cs "Hmm?"
    show arceus worried
    arceus "We've still gotta drive you home."
    show cs disappointed
    cs "Oooooh... did {i}not{/i} think of that."
    cs "Fuck."
    show arceus
    arceus "Yeah, the walk there would take hours."
    cs "Shit, uhh, what are our other options?"
    play music "<loop 0>mm_select.mp3" volume 0.3
    music Mm Select - Matthew Simmonds
    show billy at right
    show cs
    billy "Need a ride? I'll take you to any destination for only $19.95!"
    show arceus happy flipped
    arceus "Welp, CS, we've found our other option!"
    show case at mid_mid_right with dissolve
    n "Arceus opens the briefcase and gives Billy a gold bar."
    show arceus flipped
    arceus "You think this will do the job?"
    billy "Wow! You should save your money!"
    cs "We've got plenty more where that came from. You can keep it."
    hide case with dissolve
    billy "That's cash in the trash!"
    billy "Well, then! Where are we going?"
    n "CS tells Billy his address and they go down to the parking lot and start heading home."
    hide cs
    hide arceus flipped
    hide billy
    with moveoutright
    stop music fadeout 3.0
    music end
    jump back_home_alt

label airport_bad:
    cs "We should head back home now. I have a plan for our newfound riches."
    show arceus happy
    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"
    show cs flipped with determination
    hide cs
    hide arceus flipped
    with moveoutleft
    scene black with fade
    n "CS drives to the airport nearest to Las Vegas."
    scene airport_interior with fade
    play music "<loop 0>airport.mp3" volume 0.4
    music Airport Infilration - Marten Joustra
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    n "CS and Arceus pack up any belongings they have and head inside to the terminal."
    cs "What a crazy trip! That was really fun, Arc."
    arceus "Yeah, even though I was traumatized at the pizza place, I had a lot of fun."
    cs "Welp, let's go catch our plane!"
    hide cs
    hide arceus flipped
    with moveoutright
    scene airport_tsa
    show tsa at right
    with fade
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    n "CS and Arceus put their luggage on the conveyor and walk through the scanner."
    n "The scanner goes off when the bag goes through the x-ray machine."
    show cs disappointed
    cs "Huh?"
    tsa "We're gonna have to check this bag."
    show tsa at center with move
    show bag at center with dissolve
    n "The TSA agent opens up the bag, revealing all the riches from the casino."
    show arceus worried flipped
    arceus "Oh, yeah... Shit..."
    n "The TSA agent looks through the suspicious amount of money and notices it is unmarked."
    show tsa at right
    show bag at right
    with move
    tsa "This is stolen property! We are confiscating this, and you guys have to go!"
    show cs worried
    cs "Aw, man!"
    show arceus flipped at center with move
    show arceus with determination
    arceus "Welp, time to do it all over again."
    cs "Huh?"
    n "Arceus shoots finger guns at CS."
    arceus "Aaannd...."
    stop music fadeout 3.0
    music end    
    jump choose_direction

label back_home_alt:
    scene cs_house with fade
    play music "<loop 0>park_theme.mp3" volume 0.5
    music Park Theme - Lorin Nelson
    n "After the long and exciting journey, CS finally arrives at his house."
    show arceus flipped at left with moveinleft
    arceus "We made it back to your house, CS!"
    show cs flipped at center with moveinright
    cs "Finally, I'm home..."
    cs "Arceus, thank you so much for everything on this trip. I couldn't have done it without you."
    arceus "Aw, it was nice helping ya here."
    cs "You too, Billy."
    show billy at mid_left behind arceus with moveinleft
    billy "No problem!"
    cs "Well, I guess I should get some rest."
    cs "If you guys want, we can have a party at my place tomorrow to celebrate getting through all this shit!"
    show arceus happy flipped
    "Arc and Billy" "Hell yeah!"
    show arceus at left with determination
    hide billy with moveoutleft
    hide arceus with moveoutleft
    n "As CS says goodbye to his friends, a familiar but upsetting voice can be heard at the front of CS' house."
    stop music fadeout 1.0
    music end
    ed "{i}You!"
    show cs disappointed at left with moveinleft
    n "CS and the gang look towards CS' front porch, where Richard and Ed are waiting angrily for him."
    play music2 "<loop 0>hohsisremix.mp3" volume 0.5
    music "Alfred's Theme - Eminem"
    show ed at right
    show rich at mid_mid_right behind ed
    with moveinright
    ed "I have been waiting for you for quite some time now."
    rich "We've been trying to stop you for a while now, but this is the final stop for you."
    cs "HoH SiS?? What do you guys still want from me?"
    ed "What do you think, CS? After you put Wesley in the hospital? After you crippled most of our workers?"
    cs "Well, you guys scammed me out of my money and broke my computer! Of {i}course{/i} I wanted some kind of revenge!"
    ed "Why do you think this all started?"
    cs "I-{w=0.5} I don't know, because you're evil?"
    ed "CS, you made a laughingstock of our company long ago."
    ed "When you made that parody video of us that you call a \"YTP\", people wouldn't stop harrassing us about it."
    rich "You tried to humiliate us with your videos. You made others think we were a joke!"
    ed "You see, my ancestors came from the planet JoJ many years ago to start a foundation company."
    ed "It was the best damn foundation company in the world."
    ed "We repaired more than 50 percent of all foundations on the planet, and now... {i}you.{/i}"
    ed "You. You embarrassed us with those silly, stupid videos that dragged our family company through the mud."
    rich "That's why Ed wanted to get revenge on you. That's why we destroyed your computer, CS."
    cs "I don't understand..."
    menu:
        "Fight" (type = "bad"):
            jump fighthohsis_alt
        "Donate" (type = "true"):
            jump donatehohsis
        "Brag" (type = "bad"):
            jump braghohsis

label donatehohsis:
    cs "I never intended to harm your company. I just thought that the video was a good source to YTP."
    cs "I'm sorry about all those prank callers. I even made a video telling people to stop prank calling you."
    cs "I never had bad intentions for you guys... Honestly, it was also kind of like a free promotion."
    ed "Well, I'm sorry, CS, but it's too late."
    ed "Richard, get the JoJ UFO and vaporize the house."
    stop music2 fadeout 1.0
    music end
    cs "Woah, woah! Hold on a second!"
    cs "I am genuinely sorry about those videos, and I am sorry if you had any business losses."
    cs "You know what? Hold on one second."
    show cs flipped with determination
    hide cs with moveoutleft
    n "CS grabs the briefcase from Arceus, takes out a few gold bars, and gives them to Ed."
    show cs at left 
    show case at left
    with moveinleft
    cs "Here, I hope this helps you guys a bit."
    rich "Woah, is that real gold?"
    n "Ed presses his fingernail into the bar and dents it."
    ed "Shit, yeah, this is the real deal."
    ed "I... don't know what to say. This is way more than enough."
    ed "You really sure about this? Even after we broke your laptop?"
    cs "Don't worry about it. We'll go our own ways after this, and I hope you guys will continue to prosper in the business world!"
    rich "Thank you so much!"
    hide case with dissolve
    ed "Alright, let's get going now."
    ed "As long as you leave our company alone, we'll leave you alone from now on."
    ed "Good luck to you as well."
    hide ed
    hide rich
    with moveoutright
    n "Ed and Richard go back to their JoJ UFO and take off."
    show cs at right with move
    n "CS walks up to his front door."
    scene cs_room with fade
    play music "<loop 0>ac_title.mp3" volume 0.4
    music New Leaf Title Theme - Kazumi Totaka
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    if fanbase == "both":
        jump true_ending_alt
    elif fanbase == "ltt":
        jump ltt_ending_alt
    elif fanbase == "ytp":
        jump ytp_ending_alt
    else:
        jump true_ending_alt

label true_ending_alt:
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor, which has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have you work with us again virtually. Just give us a call!\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs happy at mid_left
    cs "Well, guys..."
    jump lego_ending

label ytp_ending_alt:
    n "CS looks over at his desk, where his old computer is sitting."
    scene cs_room_2 with fade
    show cs at mid_left
    cs "Oh yeah, I forgot I actually have a computer that's not a craptop."
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well, guys..."
    jump lego_ending

label ltt_ending_alt:
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor, which has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have you work with us again virtually. Just give us a call!\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat slowly comes in, confused."
    chat "Oh you're streaming?{w=0.25} I thought you were working for LTT now?{w=0.25} What happened to the YTPs?{w=0.25} Are you okay?{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well, guys..."
    jump lego_ending

label lego_ending:
    scene cs_room_2
    show cs at mid_left
    stop music fadeout 1.0
    music end
    cs "Guess what!"
    play music "<loop 0>lego_island.ogg" volume 0.6
    music Lego Island Theme - Lorin Nelson
    show case at mid_left
    n "CS takes his briefcase out and opens it up on camera."
    cs "I'm fuckin' rich now!"
    hide case with dissolve
    cs "I'm gonna make Lego Island in real life!"
    cs "You're all invited to come stay at my island once it's built!"
    n "The chat is freaking out as CS announces his plan."
    cs "I'm gonna start buying all the Lego bricks we need, and you guys can help build the island!"
    cs "Now, let's see what to buy..."
    scene black with fade
    stop music fadeout 1.0
    music end  
    $ renpy.movie_cutscene("movies/credits.webm")
    $ renpy.end_replay()
    return

label fighthohsis_alt:
    n "CS challenges HoH SiS to a fight."
    show cs angry
    cs "I beat up all your workers and Wesley, I can take you guys down too!"
    cs "Let's go!"
    ed "Richard, stand back."
    hide rich with moveoutright
    cs "C'mon! Hit me!"
    ed "I'm going to refund my fist into your face!"
    show cs at center
    show ed at center
    with move
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show cs with hpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show ed with vpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show cs with hpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show ed with vpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show cs with hpunch
    play sound "sfx_alt_punch.ogg"
    show cs at t_punchup with move
    show cs with vpunch
    show ed at right with move
    hide cs
    pause 2.0
    show cs disappointed at mid_left with moveintop
    cs "I no longer want the JoJ..."
    hide cs with moveoutbottom
    show ed with hpunch
    ed "Time to take a shit on the house."
    stop music fadeout 1.0
    music end
    bad_end "Revenge!" "back_home_alt"

label braghohsis:
    stop music
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
    cs "Yeah, well, I have {i}so{/i} much money! I don't really care!"
    cs "You guys {i}deserve{/i} to have your company in shambles!"
    n "Richard and Ed back up to their UFO."
    hide rich
    hide ed
    with moveoutright
    cs "Hey! Where are you guys going?"
    cs "Come back here!"
    n "The JoJ UFO flies up over the house, then vaporizes it with a laser."
    play sound "sfx_beam.ogg" volume 0.6
    show beam at xstretch_in
    pause 3.0
    show beam at xstretch_out
    scene cshouse_vaporized
    show cs angry at left
    cs "I'll just buy a new house!"
    n "Ed then also vaporizes the briefcase of money."
    show cs disappointed
    with vpunch
    n "Ed flips CS the bird, then flies away."
    show cs disappointed
    pause 1.0
    cs "Fuck."
    bad_end "Time to bunk\nat Rosen's!" "back_home_alt"
    stop music fadeout 1.0
    music end
    return

label noairport:
    cs "Nah, I don't wanna go to the airport."
    cs "We should take the car and drive."
    arceus "Okay, well, let's get going!"
    arceus "More road trip! Yay!"
    cs "Let's go!"
    scene carpark
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with fade
    n "CS and Arceus get back in the car and head east."
    scene black with fade
    n "After quite a bit of driving, they reach the tip of Texas."
    scene texas
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with fade
    pause 3.0
    show cs happy
    pause 1.0
    show cs
    pause 1.0
    cs "Hey, Arc?"
    arceus "What's up?"
    cs "What if... We went to your house? Don't you live in Texas?"
    arceus "Yeah, I do. Why do you wanna go there though? There isn't anything interesting there..."
    cs "I dunno. I guess I thought it'd be a cool place to stop."
    cs "I mean, we are going to my house, and I... feel like we should just check out your house!"
    arceus "Umm, okay."
    arceus "I guess we can go to my house."
    scene black with fade
    n "CS makes a stop at Arceus' house, which isn't too far away."
    scene old_house_outside with fade
    show cs at left
    show arceus flipped at right
    with moveinleft
    show arceus at right with determination
    cs "Okay! We are here!"
    show arceus worried
    arceus "Yep! This is my house, alright! This is what it looks like!"
    show arceus
    n "They enter Arceus' hou--{nw}"
    show mika at center with moveintop
    show mika at center with vpunch
    mika "Oi, chaps!"
    play music "<loop 0>pokey.mp3" volume 0.6
    music Pokeys House - Keiichi Suzuki
    mika "Ok, so, CS looks out the window and he spots a yellow Hummer."
    mika "The guy, with his arm out the window, says \"Dude, this car kicks ass! And I can watch Madagascar while driving!\""
    show arceus worried
    mika "And it cuts to him watching Madagascar while driving."
    mika "And it's Alex saying \"What kind of music do you like Gloria?\""
    mika "(Alex the lion, by the way, from Madagascar)"
    mika "And Gloria says \"HIPPO HOP!\""
    mika "And then Gloria starts dancing, okay?"
    show arceus angry
    mika "And then the guy says \"HAHAHAHAHAHAH! Dude, those animals are so fucking funny! They make me want to merge without looking!\""
    mika "Anyways..."
    mika "Jos haluatte voittaa venäläiset, kutsukaa meitä suomalaisiksi ja soittakaa Säkkijärven polkkaa."
    hide mika with moveoutbottom
    arceus "CS? Was that in the scrip--{nw}"
    cs "Alright! Let's go in Arceus' house!"
    scene arceus_house
    show cs at left
    show arceus at right
    cs "Alright! Now we are inside Arceus' house!"
    stop music fadeout 1.0
    music end  
    pause 2.0
    show cs angry
    pause 2.0
    cs "{i}Ahem!{/i}"
    scene old_house_inside
    show cs happy at left
    show arceus at right
    cs "There we go!"
    cs "Well, look at this! There is this old-ass TV sitting here! How old is this, Arc?"
    show arceus worried
    arceus "Umm..."
    cs "Well, okay, let's turn it on!"
    show arceus
    n "CS fiddles with the knobs and turns it on."
    scene tvbilly with fade
    tv_billy "Hi, it's Billy! I've been trying to sell this craptop for years and have never gotten any buyers!"
    tv_billy "So, whoever you are who just accessed Super Heaven, here's my craptop!"
    scene old_house_inside
    show cs at left
    show arceus at right
    n "The TV turns off and starts shaking."
    play music "<loop 0>clownpiece.mp3" volume 0.6
    music Pierrot of the Star Spangled Banner - ZUN
    show cs with vpunch
    show cs with hpunch
    show cs with vpunch
    show cs with hpunch
    show cs with vpunch
    show cs with hpunch
    show cs with vpunch
    show cs with hpunch
    show cs with vpunch
    show cs with hpunch
    show arceus worried
    arceus "What's going on?!"
    show cs with vpunch
    show cs with hpunch
    show cs with vpunch
    show cs with hpunch
    n "All of a sudden, the sentient craptop pops out of the TV!"
    show craptopreal at truecenter with moveinbottom
    craptop "Yo! What's up, fellas? It's me, the craptop!"
    craptop "I hate all of you!"
    craptop "So, yeah, take this random shit on my hard drive!"
    n "The craptop starts spewing out random shit?"
    show monika at center with moveintop
    show monika with vpunch
    monika "CS! You aren't real! This is a game!"
    show cs happy
    show arceus angry
    cs "Oh no! I can't believe this!"
    monika "Yeah! You, like, have to tell real-life CS to stop playing the game, or something!"
    cs "Yeah! CS! Stop playing the game, or something!"
    arceus "I don't even know anymore."
    cs "This isn't fiction and everything here is real and has happened!"
    cs "I'm gonna start streaming on time!"
    cs "And then Copguy comes in, and shoots me, then I die!"
    n "Sure, fine, whatever."
    show copguy at mid_right with moveinright
    copguy "You're... Done for!"
    copguy "Umm..."
    copguy "Pew pew pew!"
    cs "Oh no! Owwww!"
    show cs at offscreenleft with moveoutleft
    copguy "Yeah! We killed CS!"
    arceus "{i}Please kill me too...{/i}"
    copguy "Lol no"
    show copguy flipped with determination
    hide copguy with moveoutright
    show cs happy at left with move
    cs "Woohoo! I love this!"
    cs "And then comes in Gandalf the Grey and Gandalf the Wh--{nw}"
    jump reality_break

label reality_break:
    stop music
    music end  
    direct "Cut!"
    scene soundstage
    show cs happy at left
    show arceus angry at right
    with determination
    play sound "sfx_bell.mp3"
    show cs
    pause 3.0
    play sound "<loop 0>sfx_chatter.mp3"
    n "A bell rings, causing cast and crew to scatter."
    cs "Huh?"
    direct "Wow! That got out of hand!"
    cs "I was just--"
    direct "I know there's not a word-for-word script, but the story's already written, guys."
    cs "I was ad-libbing! Ryan Renolds does it all the time--{w=0.5}{nw}"
    show arceus angry at right with moveinright
    arceus "Come on, boss, it's late. We all wanna go home."
    # billy_far is Billy but from far away off-screen.
    billy_far "You know what? I'm going to need 47 million dollars for this gig, guaranteed!"
    cs "Fine, fine."
    show arceus angry flipped
    show arceus angry flipped at offscreenright with move
    direct "Alright, everyone down for another take tonight?"
    n "Nobody objects."
    direct "Okay, then, everyone take your places. We'll resume with the Vegas scene."
    show arceus at left with move
    show arceus flipped
    hide cs with moveoutright
    stop sound fadeout 2.0
    n "The cast and crew scramble back into position."
    $ achievement_manager.unlock("Broken Masquerade")
    direct "Ready?"
    show cscar2 with moveinright
    direct "Aaaaaand...{w=1.0}{nw}"
    $ returning_from_blooper = True
    $ renpy.end_replay()
    jump vegas
