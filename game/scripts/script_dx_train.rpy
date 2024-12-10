# TODO: mean needs a better text beep
# TODO: make sure all music/bios are added by the end
# TODO: ALL INSTANCES OF CAR PLAINS / CAR PLAINS NIGHT ARE PLACEHOLDERS
# TODO: moving scenery, mostly at night, including on top of the train. will need custom scenes. for now it's just the car scenery
# TODO: mean thinks the normal car moving background is too fast, maybe slow down moving videos?
# TODO: replace all instances of hearts and music notes with jp font glyphs as soon as it looks good?

######## VARIABLES ########
label train_start_good:
    $ train_money_stolen = False
    jump train_intro_start

label train_start_bad:
    $ train_money_stolen = True
    jump train_intro_start

######## RUN INTRO ########
label train_intro_start:
    stop music fadeout 3.0
    music end
    scene carpark
    # syntax: if train_money_stolen true DON'T flip sprites

    # flip
    if train_money_stolen == True:
        show arceus at right
        show cs at center
    else:
        show arceus flipped at left
        show cs flipped at right

    cs "We should head back home now. I have a plan for our newfound riches."

    # flip
    if train_money_stolen == True:
        show arceus happy
    else:
        show arceus happy flipped

    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"

    # flip
    if train_money_stolen == True:
        show cs
        show arceus
    else:
        show cs flipped
        show arceus flipped

    pause 2.0
    "{w=1.0}..."
    pause 1.0

    # flip
    if train_money_stolen == True:
        show cs
        show arceus worried
    else:
        show cs flipped
        show arceus worried flipped

    pause 1.0
    arceus "... But, how {i}will{/i} we get back, exactly?"
    arceus "That's a pretty long drive. I'm already beat."

    # flip
    if train_money_stolen == True:
        show cs surprised
    else:
        show cs surprised flipped

    cs "I saw some signs for an airport really clo--{w=0.25}{nw}"

    # flip
    if train_money_stolen == True:
        show arceus angry
        show cs disappointed
    else:
        show arceus angry flipped
        show cs disappointed flipped

    arceus "Dude, {i}no.{/i}"
    arceus "We are {i}not{/i} flying. I hate flying."
    show arceus worried flipped
    arceus "We've already been through enough, man..."
    cs "Well, if you don't want to drive, and you don't want to fly..."
    cs "What else is there?"
    cs "Like... a {i}train,{/i} or something?"

    # flip
    if train_money_stolen == True:
        show arceus
    else:
        show arceus flipped

    dxcom trainroute

    pause 2.0
    n "Arceus thinks for a moment."
    pause 2.0
    arceus "Actually... yeah."
    pause 2.0

    # that's not a hyphen
    play music sub_game_select if_changed
    music sub_game_select

    # flip
    if train_money_stolen == True:
        show arceus happy
    else:
        show arceus happy flipped

    arceus "...Yeah!"
    if fun_value(FUN_VALUE_MUSIC):
        arceus "That selects like a sub-game idea!"
        cs "... Yeah."
    else:
        arceus "That sounds like a great idea!"
    arceus "We could just relax and watch the world go by!"
    arceus "Nobody has to drive, we won't have to worry about finding rest stops, {i}and{/i} I won't have a panic attack inside of a flying metal tube!"
    cs "I dunno... How long would it take, though? A flight would only be a few hours."
    cs "Don't trains have to stop a lot? Wouldn't it be more expensive, too?"

    # flip
    if train_money_stolen == True:
        show arceus worried
    else:
        show arceus worried flipped

    arceus "Come {i}on,{/i} man! I just want to unwind!"
    arceus "We don't even need to worry about how much it'll cost, remember?"

    # flip
    if train_money_stolen == True:
        show arceus happy
    else:
        show arceus happy flipped
 
    arceus "We're filthy stinkin' {i}rich!{/i}"
    n "CS can sense that Arceus probably won't take \"no\" for an answer."
    cs "Well... I suppose we {i}do{/i} have all the money we could ever need, and we don't really have any reason to rush getting home..."
    
    # flip
    if train_money_stolen == True:
        show cs surprised 
    else:
        show cs surprised flipped

    cs "And I've never been on a cross-country train before..."

    # flip
    if train_money_stolen == True:
        show cs happy 
    else:
        show cs happy flipped

    cs "Yeah, you know what? Let's do it!"
    arceus "Let's go!"

    show cs happy
    show arceus flipped
    pause 0.25

    hide arceus
    hide cs
    with moveoutright

    scene black with dissolve
    stop music fadeout 3.0
    music end

    n "CS and Arceus hop back in the car and drive to the nearest train station."

    jump train_story_begin

label train_story_begin:
    hide screen dxcom
    if fun_value(FUN_VALUE_MUSIC):
        n "A little over an hour later, the two arrive outdoors at the Kingman Amtrak Station."
    else:
        n "A little over an hour later, the two arrive at Kingman Amtrak Station."

    scene kingman_exterior
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with dissolve

    play music outdoors if_changed
    music outdoors

    pause 1.0

    arceus "Welp, here we are!"
    show cs disappointed
    cs "...Wait, {i}this{/i} is the train station?"
    arceus "Well, yeah."
    arceus "What were you expecting?"
    cs "It's just-- I dunno, I guess I expected something... bigger? Fancier?"
    arceus "I mean, Kingman is a tiny-ass town. It would be pretty weird to have a massive station here."
    cs "I guess that makes sense."
    arceus "We should probably get going soon, though. The train only comes through here once a day."
    show cs worried
    cs "Oh, shit. Alright."

    scene black with dissolve

    if train_money_stolen == True:
        $ train_money_container = "bag"
        $ train_money_stolen_dialogue_switch = "zip it up"
    elif train_money_stolen == False:
        $ train_money_container = "briefcase"
        $ train_money_stolen_dialogue_switch = "latch it shut"
    else: # we should NEVER see these values.
        $ train_money_container = "treasure chest"
        $ train_money_stolen_dialogue_switch = "lock it shut"

    $ next_line = substitutions("CS and Arceus get out of the car and grab the "+train_money_container+" of money.")
    n "[next_line]"

    scene kingman_exterior with dissolve

    show cs flipped at left
    show arceus at right
    with moveinright

    pause 2.0
    show cs
    pause 1.0

    cs "Oh, right."
    cs "I guess we won't be needing this for a while."
    play sound sfx_lego_break
    pause 1.0

    if train_money_stolen == True:
        show bag at mid_mid_left with dissolve
    else:
        show briefcase at mid_mid_left with dissolve

    $ next_line = substitutions("CS quickly deconstructs the Lego car. He shoves the colorful little bricks into the " + train_money_container + " for later.")
    n "[next_line]"
 
    $ next_line = substitutions("The "+ train_money_container +" is now full to bursting, but CS just barely manages to " + train_money_stolen_dialogue_switch + ".")
    n "[next_line]"

    if train_money_stolen == True:
        hide bag with dissolve
    else:
        hide briefcase with dissolve

    pause 1.0
    show arceus worried
    pause 1.0
    arceus "... You still never explained to me how the fuck you did that."
    show cs happy
    cs "Like I said, I'm a master builder."
    show arceus angry
    arceus "Whatever, man. Let's just go."
    show cs happy flipped
    pause 0.25

    hide cs
    hide arceus
    with moveoutleft
    scene black with dissolve

    scene kingman_interior with dissolve

    show arceus flipped at center
    show cs at left
    with moveinleft

    n "CS and Arceus enter the train station."
    n "To CS' surprise, the place is desolate."
    cs "Hello? Is anyone here?"
    pause 1.0
    show cs disappointed
    pause 2.0
    show arceus 
    arceus "Yeah, uh, remember what I said about this town being small? This station is unmanned."
    arceus "We can buy tickets on the train once it gets here, though."
    cs "Wow, okay. How long until the train is here, then?"
    show arceus flipped at mid_right with moveinright
    n "CS notices Arceus' gaze land upon the timetable."
    show cs disappointed at center with moveinright
    pause 2.0
    cs "Oh, right."
    "..."
    cs "So, we have a little under an hour."
    show arceus
    arceus "Well... maybe a little {i}more{/i} than an hour."
    cs "What do you mean?"
    arceus "Don't you know? Amtrak is always late."
    show cs worried
    cs "What? That's not reliable at all!"
    show arceus angry
    arceus "Yeah, well, this isn't the UK."
    show arceus 
    cs "So, what do we do in the meantime, then? Is there anything here?"

    pause 1.0
    show cs disappointed flipped
    pause 1.0
    show arceus flipped
    pause 1.0
    show cs disappointed
    pause 1.0
    show arceus
    pause 1.0
    n "The two glance around the space for a moment."
    
    show cs disappointed flipped
    show arceus
    n "They spot the entrance to a museum."    
    
label train_museum_menu:
    # this label exists for timeline progression only - tate
    scene kingman_museum_1 with dissolve
    arceus "Aww, look at all those little trains. Wanna poke around in there?"

    menu:
        "Would you like to visit Kingman Railroad Museum?"
        "Sure.":
            jump train_yes_museum
        "Not really...":
            jump train_no_museum

label train_yes_museum:
    cs "Sure, I don't see why not. Not like we have anything else to do."
    arceus "Alrighty, let's go!"
    scene black with dissolve
    pause 1.0
    scene kingman_museum_2 with dissolve
    pause 2.0
    show cs flipped at center
    show arceus at mid_right
    with moveinright
    pause 1.0
    cs "Wow, there's so much stuff here!"
    show cs flipped
    cs "What should we check out first?"
    arceus "Ooh, how about that train set over there?"
    
    scene kingman_museum_3 with dissolve
    n "Arceus points towards a custom train exhibit with two attached controllers."
    n "It looks... familiar."
    
    scene kingman_museum_2
    show cs disappointed at center
    show arceus at mid_right
    with dissolve
    cs "It looks like {i}Minecraft..."
    arceus "You don't like {i}Minecraft?"
    cs "Nah. The crafting system is just too much."
    show arceus worried
    arceus "I guess it's not for everyone..."
    show arceus
    arceus "Thankfully, there's none of that here. Let's try it out!"
    show cs
    cs "Yeah, you're right. Let's go!"
    show cs flipped
    show cs flipped at offscreenleft
    show arceus at offscreenleft
    with moveoutleft
    stop music fadeout 2.0
    music end
    scene black with dissolve
    minigame "play_toytrains_game" "train_race_win" "train_race_lose"

label train_no_museum:
    scene kingman_interior
    show cs disappointed flipped at center
    show arceus at mid_right
    with dissolve
    cs "Not really..."
    show arceus angry
    show cs disappointed
    arceus "What, would you rather just sit around bored, then?"
    cs "I'm just not that into trains."
    show cs happy
    cs "Now, if this were a Lego museum, {i}that{/i} would be another story!"
    show arceus
    arceus "Well, {i}I'm{/i} going to go check it out."
    show arceus happy
    show cs worried
    arceus "Just don't be offended when I pepper you with fun train facts afterwards! :3c"
    scene black with dissolve
    n "As CS takes a quick nap in a lobby chair, Arceus wanders around the museum."
    n "While not many exhibits can fit inside such a small building, there is just enough to see to pass the remaining time."
    n "About five minutes before the train's expected arrival, the two make their way out onto to the platform as Arceus shares some of the things he learned today."
    jump train_kingman_platform

label train_race_win:
    play music outdoors if_changed
    music outdoors
    scene kingman_museum_2
    show cs happy at left
    show arceus worried at right
    with dissolve
    cs "Woohoo!"
    show cs
    cs "Good game, Arc."
    arceus "Yeah, GG..."
    show arceus
    arceus "Honestly, I think this game is rigged, anyway. Just look at how much bigger {i}my{/i} track is!"
    show cs disappointed
    cs "... Hey, you're right! I can't unsee it now!"
    cs "Who built this?"
    n "CS takes a closer look at the plaque."
    n "\"This display was generously built and donated by aZSz.\""
    show cs surprised
    "..."
    show cs
    cs "No idea who that is."
    cs "Let's see what else is here, I guess."
    show arceus happy
    arceus "Yeah! I wonder if there are any better train sets to play with."
    show cs flipped
    show arceus
    show arceus at offscreenleft
    show cs flipped at offscreenleft
    with moveoutleft
    scene black with dissolve

    n "CS and Arceus wander around the museum for a little longer."
    n "While not many exhibits can fit inside such a small building, there is just enough to see to pass the remaining time."
    n "About five minutes before the train's expected arrival, the two make their way out onto to the platform, still discussing some of the things they learned today."
        
    jump train_kingman_platform
    
label train_race_lose:
    play music outdoors if_changed
    music outdoors
    scene kingman_museum_2
    show cs disappointed at left
    show arceus happy at right
    with dissolve
    arceus "Let's fuckin' {i}go!"
    cs "Aww, damn it..."
    cs "This has {i}got{/i} to be rigged! I play with RC cars all the time!"
    cs "Model trains can't be {i}that{/i} different, can they?"
    show arceus worried
    arceus "I mean, RC cars don't exactly have a possibility of derailing..."
    cs "I suppose..."
    show arceus
    arceus "I wonder who built this. {i}Minecraft{/i}-themed is an interesting choice."
    n "CS takes a closer look at the plaque."
    n "\"This display was generously built and donated by aZSz.\""
    show cs surprised
    "..."
    show cs
    cs "No idea who that is."
    cs "Let's see what else is here, I guess."
    show arceus happy
    arceus "Yeah! I wonder if there are more train sets we can play with."
    show cs flipped
    show arceus
    show arceus at offscreenleft
    show cs flipped at offscreenleft
    with moveoutleft
    scene black with dissolve

    n "CS and Arceus wander around the museum for a little longer."
    n "While not many exhibits can fit inside such a small building, there is just enough to see to pass the remaining time."
    n "About five minutes before the train's expected arrival, the two make their way out onto to the platform, still discussing some of the things they learned today."
    jump train_kingman_platform

label train_kingman_platform:
    play music outdoors if_changed
    music outdoors
    scene kingman_platform_2 with dissolve
    pause 1.0
    show arceus flipped at mid_mid_left
    show cs disappointed at left
    with moveinleft
    pause 2.0

    cs "... Man, that's some bad luck, though. What are the odds of this place burning down {i}twice?!{/i}"
    show arceus
    arceus "I mean, back then, trains were powered by steam."

    # arc and mean wanted this
    if fun_value(FUN_VALUE_COMMON):
        show cs 
        cs "Steam? Like Gabe Newell?"
        show arceus angry
        arceus "No."
        show cs disappointed
        cs "Oh."
        show arceus
        arceus "Anyway..."

    arceus "Like, do you know what happens if you open a pressure cooker too early?"
    show cs disappointed
    cs "It... {i}explodes,{/i} right?"
    arceus "Yeah. It's pretty much the same concept."
    arceus "You crash a steam engine, you end up with this huge pressure differential, then you get a big {i}boom.{/i}"
    show cs worried
    cs "Yikes. Glad that's not the case nowadays."
    show arceus worried
    arceus "Yeah. It's also a big part of why planes are so scary for me. There are pressure differences at play there, too."
    arceus "If some jackass were to open the emergency exit in midair, or something, well... there's really no surviving something like that."
    show cs scared
    cs "Shit, I guess I've never really thought about that..."
    arceus "Yeah, and if you have a lunatic like that on a fucking {i}plane,{/i} it's not like you can just... throw them overboard and keep going."
    show cs disappointed
    cs "\"Overboard\"? Wait, isn't that term only used for boats?"
    show arceus angry
    arceus "Man, I don't know what word you'd use for throwing someone off of a plane."
    arceus "That's not even a thing you can {i}do.{/i}"
    arceus "How can a word exist for a thing that's impossible?"
    show arceus
    show cs surprised
    arceus "Anyway, do you remember that news story about the guy who got duct-taped to his seat during a flight?"
    show arceus worried
    show cs disappointed
    arceus "... Yeah. That's about the {i}only{/i} thing they could have done to protect themselves and everyone else."
    show cs worried
    cs "Damn, I'd forgotten all about that!"
    cs "What would have happened if it had been on a train?"
    
    # mean wanted this
    if fun_value(FUN_VALUE_COMMON):
        $ train_polar_express_fun_value = True
        show arceus 
        arceus "Have you ever seen {i}The Polar Express?"
        show cs disappointed
        cs "No, why?"
        arceus "Well, they throw them off the train."
        show cs worried
        cs "Really?"
        show arceus angry
        arceus "No."
        arceus "I'm just gonna assume that they'd kick the bastard off at the next station."
    else:   
        show arceus angry
        arceus "I dunno, man. I'm just gonna assume that they'd kick the bastard off at the next station."

    arceus "I really don't want to think about someone like that being on {i}our--{/i}{w=0.25}{nw}"
    stop music fadeout 3.0
    music end
    show cs
    show arceus flipped
    play sound sfx_amtrak_horn
    n "The conversation is interrupted by the blare of a train horn."

    scene kingman_train_arrive with dissolve
    play music ochre_woods_day if_changed
    music ochre_woods_day
    if fun_value(FUN_VALUE_MUSIC):
        n "The two watch as the locomotive approaches the Ochre Woods during the day and eventually slows to a stop."
    else:
        n "The two watch as the locomotive approaches the station and eventually slows to a stop."
    hide cs
    hide arceus

    scene amtrak_arrive_close with dissolve

    show arceus flipped at mid_mid_left
    show cs at left
    with moveinleft

    arceus "Welp, there it is."
    n "The two wait for the incoming passengers to disembark."
    pause 2.0
    show cs scared
    show arceus worried flipped
    tate_offscreen "{cshake}{size=+24}Alllllll aboarrrrrrd!!" with hpunch
    pause 1.0
    cs "Wow, damn, the train only {i}just--{w=0.25}{nw}"
    show tate flipped at right with moveinright
    pause 1.0
    show cs worried
    show tate stare flipped
    cs "Tate?!"
    cs "Is that you?"
    show tate shock flipped
    tate "{i}CS?{/i}"
    tate "What are you doing here?"
    cs "What are {i}you{/i} doing here?"
    cs "I thought you were still in Texas!"
    show tate stare flipped
    show arceus flipped
    tate "Oh!"
    show tate flipped
    show cs
    tate "Yeah, I still live there. I'm just traveling a bit."
    tate "A good friend of mine started a new job as a driver for Amtrak. He gets discounted tickets, so he asked me if I wanted to come along with him for a while."
    tate "His first shift starts tonight, actually."
    show cs happy
    cs "Oh, cool!"
    show tate stare flipped
    n "Tate notices Arceus."
    tate "Oh, who's your friend?"
    cs "Oh, this is Arceus. He and I go {i}way{/i} back."
    show cs
    show arceus happy flipped
    arceus "Hiya. You can just call me Arc." 
    show tate flipped
    tate "Well, it's nice to meet ya, Arc."
    show arceus flipped
    tate "I'm Tate. I'm, uh...{w=0.5}{nw}"
    show tate sheepish flipped
    show cs surprised
    pause 1.0
    "...{w=1.0}{nw}"
    tate "I'm just an old friend of CS'."
    show cs happy
    cs "Yep!"
    tate "Of course."
    show arceus worried flipped
    n "Arceus raises an eyebrow at this interaction."
    n "He decides that maybe it's better not to ask."
    show cs
    tate "A-{w=0.1}Anyway. We should probably get going."
    show tate
    tate "We don't wanna end up stranded here. This train only stops here once a day, after all!"

    show cs at mid_offscreen_left
    show arceus flipped at left
    show tate at center
    show amtrak_conductor at right
    with moveinright

    amtrak_conductor "All aboard!" with vpunch
    show cs disappointed
    cs "... Wait, I thought you already called for everyone to board, Tate?"
    show arceus worried flipped
    arceus "Yeah, and why aren't you in uniform?"
    show tate sheepish flipped
    tate "Oh, I don't actually work for Amtrak. I just try to help where I can."
    show tate smug flipped
    tate "Also, I kinda just wanted to do the funny."
    amtrak_conductor "Yeah, don't do that."
    show tate sheepish
    pause 1.0
    amtrak_conductor "You're already on thin ice after what happened in the dining car."
    tate "But, I just wanted--{w=0.25}{nw}"
    amtrak_conductor "The {i}only{/i} reason why you're still on this train is because the new guy won't let us kick you off."
    tate "Listen, I was just trying to he--{w=0.25}{nw}"
    amtrak_conductor "Yeah, well, {i}don't."
    amtrak_conductor "Or we'll leave {i}both{/i} of you at the next station."

    if train_polar_express_fun_value == True:
        show arceus flipped
        arceus "I told you!"
        show arceus worried flipped

    show tate sad
    tate "Yes, sir..."
    amtrak_conductor "Now, let's get a move on."

    show amtrak_conductor flipped
    pause 0.25

    hide amtrak_conductor with moveoutright
    hide tate with moveoutright # separate on purpose
    pause 1.0

    # lol, let's have them look at each other for a sec like wat
    show cs disappointed at left
    show arceus worried flipped at mid_mid_left
    with moveoutright

    pause 0.5

    show cs worried 
    show arceus worried
    pause 1.0
    
    show cs 
    show arceus flipped
    pause 1.0

    hide cs
    hide arceus
    with moveoutright

    stop music fadeout 3.0
    music end
    scene black with dissolve
    n "The group boards the train."
    n "CS and Arceus buy tickets from the staff. After a brief tour of all of the amenities, the trio heads towards the sleeper cars."
    jump train_boarding

label train_boarding:
    scene amtrak_sleeper_corridor
    with dissolve

    play music bedroom_day if_changed
    music bedroom_day
    
    pause 2.0 
    # again, separate on purpose
    show amtrak_stewardess at right with moveinleft
    show tate at mid_mid_right with moveinleft

    show cs at left
    show arceus flipped at mid_mid_left
    with moveinleft

    pause 1.0
    show tate flipped
    pause 0.5
    if fun_value(FUN_VALUE_MUSIC):
        tate "... And, {i}this{/i} way is the bedroom car! Your room is--{w=0.25}{nw}"
        show amtrak_stewardess flipped
        amtrak_stewardess "Tate."
        show tate
        tate "Hm?"
        amtrak_stewardess "Bedroom {i}~ Day.{/i}"
        show tate sheepish
        tate "I know, but–-{w=1.0}{nw}"
        amtrak_stewardess "Keep up with the bit."
        show tate sad
        tate "But, CS gets away with it all the time..."
        amtrak_stewardess "Also, please stop trying to do {i}my{/i} job."
    else:
        tate "... And, {i}this{/i} way is the sleeper car! Your room is--{w=0.25}{nw}"
        show amtrak_stewardess flipped
        amtrak_stewardess "Tate."
        show tate
        tate "Hm?"
        amtrak_stewardess "You're doing it again."
        show tate sheepish
        tate "Doing what again?"
        amtrak_stewardess "Doing {i}my{/i} job."
        show tate sad
    amtrak_stewardess "I know that Mean lets you get away with a lot, but you {i}really{/i} need to let us work."
    amtrak_stewardess "Why don't you catch up with your friends here until he wakes up?"
    amtrak_stewardess "{size=-15}Or, why don't {i}you{/i} have a nap, too? {w=0.25}Do you {i}ever{/i} sleep?"
    tate "Oh... right."
    tate "Sorry."
    tate "I guess it {i}has{/i} been a while since I've seen CS. I can stay here for a bit..."
    show tate sheepish flipped
    tate "...{w=-0.25} if you're okay with that."
    show cs happy
    cs "Of course!"
    show arceus worried flipped
    show cs
    arceus "Well, while you two are catching up, I {i}really{/i} need to use the can..."
    show amtrak_stewardess
    amtrak_stewardess "Of course. Right through here, sir."
    arceus "Thanks."
    show arceus flipped
    show tate
    hide arceus with moveoutright
    n "Arceus scurries off."
    pause 1.0
    
    show amtrak_stewardess at mid_offscreen_right with moveinleft
    pause 0.5
    show amtrak_stewardess flipped

    show tate sheepish
    amtrak_stewardess "I {i}mean{/i} it, Tate."
    amtrak_stewardess "Be good."
    tate "Yes, ma'am..."
    show cs disappointed
    show amtrak_stewardess
    pause 0.25
    hide amtrak_stewardess with moveoutright
    n "The stewardess strolls away."
    pause 1.0

    show cs disappointed at mid_mid_left 
    with moveinright
    pause 0.5

    cs "Damn, why's everyone so snippy with you?"
    show tate sad flipped
    cs "What did you {i}do?{/i}"
    tate "My friend, Mean, usually lets me help out with whatever needs doing."
    tate "He's not going to wake up for a while, though, so I've been pretty bored."
    show tate sheepish flipped
    tate "First, I thought I'd set up a surprise for him in the dining car, but the other staff didn't like it..."
    tate "I guess I got a little carried away."
    show tate sad flipped
    tate "I hope {i}he{/i} likes it, at least."
    show cs happy
    cs "I'm sure he will!"
    show tate sheepish flipped
    cs "I hope his first shift goes well, too."
    tate "Me, too..."
    tate "I've been so nervous for him. I keep trying to find things to do, to maybe lighten his load... but his coworkers keep telling me, {w=0.25}don't do this, {w=0.25}don't do that..."
    show cs surprised
    cs "... Yeah, that tracks."
    show cs disappointed
    cs "You always {i}were{/i} a little..."
    n "..."
    pause 2.0
    show tate srs flipped
    tate "A little...?"
    show cs worried
    cs "You know, just a little-- {i}uhHH!{w=0.25}{nw}"
    play sound sfx_punch
    $ renpy.music.set_volume(0)
    show cs scared at mid_offscreen_left
    show tate shock flipped
    with hpunch
    show cs concentrate
    show tate shock flipped at right with MoveTransition(0.25)
    play sound sfx_lupin_stinger volume 0.8
    show lupin run at mid_mid_left:
        xanchor 0 yanchor 0
        xpos 200 ypos 322
    with dissolve
    n "CS is knocked to the ground as a stranger sprints down the corridor!"
    lupin_offscreen "Sorry, pretty kitty! I've gotta {i}run!"
    show lupin run flipped:
        xanchor 0 yanchor 0
        parallel:
            linear 0.75 zoom 0
        parallel:
            linear 1.0 xpos 1700
        parallel:
            linear 1.0 ypos 0
    hide lupin with dissolve
    n "The weird guy hurries away."
    pause 0.25
    $ renpy.music.set_volume(100)
    tate "Oh,{w=-0.25} my God! CS, are you alright?!"
    cs "Y-{w=0.1}Yeah..."
    cs "More surprised than anything."
    show tate shock flipped at left with moveinleft
    n "Tate helps CS up from the floor."

    show cs concentrate at left
    show tate sheepish flipped at center
    with MoveTransition(1.0)

    pause 1.0
    show cs disappointed
    pause 1.0
    tate "Y'know, maybe it's our own fault, for just standing out here while people are boarding."
    tate "Let's go into y'all's room."
    cs "Yeah, good idea."
    show tate sheepish
    pause 0.25

    hide tate
    hide cs
    with moveoutright

    scene black with dissolve
    jump train_enter_sleeper

label train_enter_sleeper:
    play music bedroom_day if_changed
    music bedroom_day

    play sound sfx_sliding_door_close
    show amtrak_desert_day
    show amtrak_sleeper_interior_day
    show arceus at right
    with dissolve

    n "CS and Tate enter the sleeper unit just as the train takes off."
    
    show tate at mid_mid_left
    show cs at left
    with moveinleft

    pause 0.5
    show arceus worried
    arceus "Hey, guys. Sorry about that."
    arceus "I think something I ate at that creepy-ass pizza place didn't quite agree with me."
    show cs disappointed
    show tate stare
    cs "Damn. Are you feeling any better?"
    show arceus
    arceus "Oh, yeah. I think I'll be alright, now."
    show cs
    show tate
    cs "That's good to hear."   
    show tate stare
    tate "Oh, yeah! Let me know if y'all need more toilet paper, or soap, or... anything."
    show tate
    show cs disappointed
    cs "... Shouldn't we be asking the {i}staff?"
    show tate sheepish flipped
    pause 1.0
    show tate sad flipped
    pause 0.5
    tate "{w=0.5}... Yes. Yes, you should."
    show tate sad
    n "Tate sheepishly looks down at the floor."
    pause 1.0
    show arceus worried
    arceus "So, uh..."
    arceus "Hey, Tate, how {i}do{/i} you know CS, anyway?"
    show tate sheepish
    tate "O-{w=0.1}Oh, uh..."
    tate "We met a few years ago, back when Mixer was still a thing."
    show cs
    cs "You might remember it as Beam, Arc."
    show arceus happy
    arceus "Oh, yeah! Damn, {i}Beam?"
    show tate
    arceus "Now {i}that's{/i} a name I haven't heard in a while!"
    show cs disappointed
    show arceus
    cs "Yeah. It's a real shame that Microsoft eventually kills off every product I like."
    show tate flipped   
    tate "Yeah, it really is."
    tate "At least you're not still shilling for them these days, right?"
    pause 1.0
    "..."
    pause 1.0
    show tate sheepish flipped
    tate "... Right?"

    stop music fadeout 3.0
    music end

    show cs scared
    show tate shock flipped
    show arceus worried
    with shake2
    play sound sfx_hard_knock
    if fun_value(FUN_VALUE_MUSIC):
        n "A sudden item bouncing on the door startles the group."
    else:
        n "A sudden hard knock on the door startles the group."

    play music item_bounce volume 0.8 if_changed
    music item_bounce
    play sound sfx_hubbub loop fadein 2.0 volume 0.3

    n "An uproar of angry passengers grows steadily louder."

    cs "What the hell?!"
    tate "No, no, {i}no!"
    tate "This {i}can't{/i} be good!"
    arceus "So much for a relaxing trip..."
    n "The door is slid open with a heavy hand."
    
    play sound sfx_sliding_door_open
    pause 1.0
    
    show cs scared flipped at mid_mid_right
    show tate shock flipped at right
    show arceus worried at mid_offscreen_right
    with moveinright

    show amtrak_conductor flipped at left
    with moveinleft
    
    amtrak_conductor "Alright, every--{w=0.25}{nw}"
    amtrak_conductor "Oh. {w=0.5}{i}Mx. Frost."
    tate "I {i}swear,{/i} sir! Whatever happened just now, I had {i}nothing{/i} to do with it!"
    tate "I've been in this room! Just talking with CS, here!"
    show cs happy flipped
    cs "Hey guys, CS here!"
    amtrak_conductor "Huh?{w=0.25}{nw}"
    show tate srs flipped
    show arceus angry
    tate "{i}Why.{w=0.25}{nw}"
    show cs scared flipped
    cs "{i}Ahem{w=0.25}{nw}"
    show cs flipped
    show tate sheepish flipped
    show arceus
    cs "I mean, uh, yes. Tate was here the entire time."
    arceus "Yep, Tate has been with us since we got on the train."
    amtrak_conductor "Oh, really?"
    amtrak_conductor "Well, if they are bothering you, I can take care of them for you."
    show tate cry flipped
    tate "{i}{size=-15}Eep!"
    show cs happy flipped
    show tate sheepish flipped
    cs "Oh, no, not at all!"
    show cs flipped
    cs "Tate and I have known each other for years. We were just catching up."
    amtrak_conductor "Well, alright."
    show arceus worried
    arceus "May I ask what is going on out there? The noise kinda scared us."
    show amtrak_conductor
    show cs disappointed flipped
    play sound sfx_hubbub loop volume 0.3
    amtrak_npc_1 "Hey, my watch is gone, too!" with hpunch
    amtrak_npc_2 "Man, {i}fuck{/i} your watch! They took my damn {i}Switch!{/i}"
    amtrak_npc_3 "Such {i}language!" with hpunch
    amtrak_npc_3 "My dearest mother's priceless brooch is {i}also{/i} missing, and you don't hear {i}me{/i} speaking like an utter {i}barbarian!"
    n "The complaints of a few more troubled travelers echo throughout the cabin."
    show amtrak_conductor at mid_offscreen_left with moveinleft
    amtrak_conductor "Please remain calm, everyone! We will find out who the thief is, and they {i}will{/i} be brought to justice!"
    amtrak_conductor "Please return to your rooms! We will have an update for you as early as possible!"
    stop sound fadeout 2.0
    n "One by one, the disgruntled passengers return to their units."

    pause 1.0
    show amtrak_conductor flipped at left with moveinright
    pause 1.0
    amtrak_conductor "... As you can probably tell, there has been a sudden increase in reported thefts."
    amtrak_conductor "Are any of you missing valuables?"
    show arceus worried
    
    # begin this flip nonsense... why do i do this to myself
    $ next_line = substitutions("I mean, all we had was the one " + train_money_container +".")
    arceus "[next_line]"
    pause 1.0
    show arceus worried flipped
    pause 1.0
    show arceus worried
    pause 2.0

    $ next_line = substitutions("... CS, where is the "+train_money_container+"?")
    arceus "[next_line]"
    show tate shock
    show cs worried
    pause 1.0
    show tate shock flipped
    pause 1.0
    show cs worried flipped
    show tate shock  
    pause 1.0
    show cs disappointed
    show tate shock flipped
    cs "I thought {i}you{/i} had it!"
    show arceus angry
    arceus "I thought {i}YOU{/i} had it!!" with vpunch
    pause 1.0

    show cs worried
    cs "Oh."
    show cs scared
    cs "Shit."

    if train_money_stolen == True:
        $ train_money_stolen_dialogue_switch = "black bag"
        $ train_money_stolen_dialogue_switch_2 = "... won"
    elif train_money_stolen == False:
        $ train_money_stolen_dialogue_switch = "metal briefcase"
        $ train_money_stolen_dialogue_switch_2 = " won"
    else: # we should never see these
        $ train_money_stolen_dialogue_switch = "red and gold treasure chest"
        $ train_money_stolen_dialogue_switch_2 = " totally plundered"

    show cs disappointed flipped
    $ next_line = substitutions("Yes, sir, we're missing a single " + train_money_stolen_dialogue_switch + " filled with money we" + train_money_stolen_dialogue_switch_2 + " while we were in Vegas.")
    cs "[next_line]"
    arceus "And Lego bricks." 
    show cs surprised
    cs "And Legos, yes."
    show tate srs flipped
    tate "Wait, so..."
    tate "You win it big in Vegas, and the {i}first{/i} thing you do is buy {i}Legos?"
    show cs worried
    cs "Well, no--{w=0.25}{nw}"
    tate "I suppose I shouldn't have expected anything else from you."
    show cs disappointed
    cs "That's not what--{w=0.25}{nw}"
    show cs disappointed flipped
    amtrak_conductor "Thank you, sir. We'll keep an eye out for your things."
    show tate sheepish flipped
    amtrak_conductor "Now, Mx. Frost..."
    amtrak_conductor "You'd better behave. Stay out of the way during this investigation."
    show tate sad flipped
    tate "Yes, sir."
    tate "I'll probably just stay here until Mean clocks in."
    amtrak_conductor "Good."
    amtrak_conductor "As for you two..."
    amtrak_conductor "Please let a {i}staff member{/i} know if you need anything, or if anything else goes missing."
    show cs flipped
    cs "Alright, thank you so much."
    show arceus
    arceus "Yeah, thanks!"
    show amtrak_conductor
    hide amtrak_conductor with moveoutleft

    stop music fadeout 3.0
    play sound2 sfx_ambiance_train_interior volume 0.3 fadein 3.0
    music end

    show cs disappointed at left
    show tate sad at mid_mid_left
    show arceus worried at right
    with moveinleft

    play sound sfx_sliding_door_close
    n "The conductor leaves to return to his duties."
    tate "I can't believe this..."
    arceus "Me, neither. All of that money, just... {i}gone..."
    show cs happy
    cs "Nah, I'm sure they'll find it. Nobody started complaining until the train was already moving, so, all of our stuff should still be on board, right?"
    arceus "I sure hope so..."
    n "Tate shifts uncomfortably."
    show cs disappointed
    cs "Is everything alright, Tate?"
    show tate sad flipped
    tate "I was just thinking..."
    tate "I don't think that Mean should know about any of this."
    cs "Why not? It's not like {i}you're{/i} the one who stole it."
    tate "It's just that... he's got enough to worry about. Tonight is his first official shift as the night driver..."
    tate "I really don't want him dealing with something like this on his first day."
    show tate sheepish flipped
    tate "I just feel like I have to do {i}something."
    cs "Don't you think you've done enough already?"
    tate "What do you mean?"
    show cs worried
    cs "The conductor and that attendant both seemed really annoyed with you."
    show cs surprised
    show tate sad flipped
    cs "I {i}know{/i} how you work, Tate."
    cs "I really think that sometimes you need to just... \nlet {w=0.25}things {w=0.25}{i}happen."
    tate "But, Mean--{w=0.25}{nw}"
    show tate sad
    show arceus happy
    arceus "Now, obviously, I've never met the guy, but I'm sure Mean will be fine."
    show arceus
    arceus "Think about it. You didn't, like, help him through his job interview, did you?"
    show tate sad
    tate "Well, no..."
    show tate sheepish
    tate "I mean, I looked over his résumé, but that's all."
    show cs happy
    show tate sheepish flipped
    cs "Exaaaaactly. You've done all you can, so, just let things happen."
    show tate srs flipped
    tate "How can you be so... {i}unbothered{/i} by all of this? After you just lost so much money?!"
    show arceus worried
    arceus "{size=-15}Well, {i}I'm{/i} bothered by it..."
    show cs worried
    show arceus
    cs "I mean, yeah, it totally sucks balls, but all it means is that when we get home, things will just be the same as they were before."
    show tate sheepish flipped
    tate "Even so, I really do hope they find everyone's things..."
    show tate sad flipped
    tate "I'm just so scared that they'll accuse Mean of stealing it, or something, since he's so new..."
    tate "I really don't know if he could handle losing {i}this{/i} job, too."
    show cs disappointed
    cs "Wait, what happened at his {i}last{/i} job?"
    show tate srs flipped
    tate "It was so fucking stupid."
    tate "So, he was working for this home repair company, right?"
    tate "They hired him on as a security guard, since he's all spiky--{w=0.25}{nw}"
    show arceus 
    arceus "{i}Spiky?{/i} Wha--{w=0.25}{nw}"
    tate "--and then some weirdo dressed as a catgirl maid broke in and fought the CEO! A lot of people got hurt!"
    show tate shock flipped
    show cs worried
    show arceus worried
    $ next_line = substitutions("I think Mean said that someone even got " + ch2_cs_attack_used + " off of the roof!")
    tate "[next_line]"
    show tate sheepish flipped
    tate "But since Mean couldn't... {w=0.5}{size=-5}hold him off... {w=0.5}{size=-5}he was... {w=1.0}{size=-5}fired..."
    "..."
    pause 2.0
    show tate shock flipped
    n "Tate falls silent. They stare wide-eyed at CS' outfit."
    pause 2.0
    show cs scared
    cs "... Woah, Tate, why are you look--{w=0.25}{nw}"
    
    # TODO: bgm?

    show tate furious flipped
    tate "{cshake}{size=+36}IT WAS {i}YOU!!" with hpunch
    cs "Wha-- {i}huh?!"
    tate "CS, WHAT THE {nw}"
    tate "CS, WHAT THE {fast}{i}FUCK?!" with vpunch
    tate "{i}YOU{/i} {nw}" with vpunch
    tate "{i}YOU{/i} {fast}BROKE INTO HOH SIS?!"
    show cs worried
    cs "Oh, yeah, uh--{w=0.25}{nw}"
    
    show tate cry flipped
    n "Tate is on the verge of tears."
    tate "My best friend lost his job, and it's your fault..."
    tate "And, now, you're {i}here..."
    tate "I can't believe this..."
    show cs disappointed
    cs "Tate..."
    cs "Listen to me, please--{w=0.25}{nw}"
    show tate srs flipped
    tate "{sc=1}{i}No!"
    tate "{sc=1}I don't want to hear it!"
    tate "Is {i}this{/i} what you've been up to since--{w=0.5}{nw}"
    "..."
    tate "You know what? No."
    tate "Mean's shift starts soon. I need to be there for him."
    tate "If either of y'all see him, you will not breathe a word of {i}any{/i} of this to him."
    tate "Not about the thefts, and {i}certainly{/i} not about what happened at HoH SiS."
    tate "He doesn't need this. Especially not {sc=1}today."
    show tate furious flipped
    show cs scared
    n "Tate reinforces their demand with a piercing glare towards CS." with hpunch
    show tate srs
    show cs worried
    n "Tate then suddenly stands up." with vpunch
    tate "{sc=1}I'm sorry."
    tate "{sc=1}I need to go."
    show tate sad flipped
    pause 0.25
    hide tate with moveoutleft
    play sound sfx_sliding_door_open
    n "Tate swiftly exits the room and runs off, not even bothering to shut the door behind them."

    show cs disappointed
    n "CS looks distraught."
    pause 2.0
    cs "... {w=0.25}Fuck."
    arceus "You alright, man?"
    cs "I will be. I'm just worried about Tate."
    cs "I don't remember the last time they were so upset."
    cs "All of their yelling suddenly has me {i}really{/i} tired, too... I think I could use some rest."
    show arceus
    arceus "Yeah, same. Also, I'm really glad we sprung for the private room."
    show arceus happy
    arceus "These beds are looking pretty good right now."
    show arceus
    show cs
    cs "They {i}do{/i} look nice."
    show cs happy
    cs "I think that tomorrow, we'll wake up, someone will have found our cash overnight, Tate will have had some time to cool off, we'll all get together and have a huge complimentary breakfast..."
    cs "...{w=0} and all will be right with the world!"

    # TODO: some funny cheery fanfare jingle?

    pause 1.0
    show arceus angry
    arceus "... {i}I{/i} think you're being way too optimistic about all of this."
    arceus "I'm going to bed."
    show cs disappointed
    cs "Yeah, me,{w=0} too..."

    scene black with dissolve
    stop sound2 fadeout 0.5
    n "CS and Arceus decide to call it an early night."
    n "CS effortlessly falls into a deep slumber."
    n "While the fold-out bed is indeed quite comfortable, Arceus struggles to get any rest."

    scene
    # had to put it on this layer, sorry
    play music sfx_ambiance_train_interior loop volume 0.3 fadein 0.5
    show amtrak_desert_night
    show amtrak_sleeper_interior_night
    with dissolve
    play sound2 sfx_csnore fadein 1.0
    pause 1.0
    arceus "Fuck..."
    arceus "I'm so tired, but I {i}still{/i} can't fucking sleep..."
    arceus "I wonder if they have booze on this train."

    show arceus dark at center with dissolve
    n "Arceus quietly gets out of bed, being careful not to wake CS."

    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        hide arceus with moveoutleft
        n "He makes for the dining car in hopes of drinking his worries away."
        play sound sfx_sliding_door_open
        pause 2.0
        n "However, the sleeper's door is heavier than expected."
        play sound sfx_clonk
        with hpunch
        pause 1.0
        arceus "{i}Shit!"
        n "Arceus grimaces at the sudden noise and peeks through the window back at CS."
        "..."
        n "Thankfully, CS is still fast asleep."
    else:
        hide arceus with moveoutleft
        play sound sfx_sliding_door_open
        pause 2.0
        n "He gently shuts the door behind him, then makes for the dining car in hopes of drinking his worries away."
        play sound sfx_sliding_door_close

    stop music fadeout 3.0
    stop sound2 fadeout 3.0
    scene black with dissolve
    pause 3.0
    jump train_dining

label train_dining:
    play music krabby_klub if_changed

    scene 
    show amtrak_desert_night as left:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, -400)

    show amtrak_desert_night as right:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, 400)
    show amtrak_dining_car
    with dissolve
    pause 1.0
    music krabby_klub
    pause 0.5
    show arceus at center with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        n "Arceus arrives at the Krabby Klub."
    else:
        n "Arceus arrives at the dining car."
    n "The aromas of so many different foods mingling together overwhelm his canine senses."
    arceus "Jeez, it smells like a high school cafeteria..."
    arceus "I think I'll just grab myself a bottle of wine and get out of here."
    show arceus at left with moveinleft
    n "As he approaches the counter, Arceus finds his attention redirected towards a yellow... {w=0.5}thing."

    scene 
    show amtrak_desert_night at manual_pos(0.5, 0.4, 0.5)
    show amtrak_dining_table
    show mean at manual_pos(300,350)
    show amtrak_dining_food at manual_pos(805,145) behind mean
    $ collect("amtrak_dining_food")
    hide arceus
    with dissolve
    $ collect("amtrak_dining_food")

    n "A strange spiny entity is surrounded by piles of pancakes, sky-high stacks of sausages, oodles of eggs, and a whole bunch of bacon."
    n "Arceus can't help but stare in awe at both the enormous spread of food..."
    n "...{w=0} and at the brightly-colored creature currently demolishing it."
    show mean happy
    mean_offscreen "LET'S {w=0.25}FUCKING {w=0.25}{cshake}{i}GOOOOOOOO!!"
    mean_offscreen "I can't believe they made {i}all{/i} of this just for me!"
    mean_offscreen "This is going to be the best day {i}ever!"
    show mean happy2
    n "The sunny little spike ball scarfs down a sausage."
    show arceus at right with moveinright
    with determination
    show mean happy
    arceus "Damn..."
    arceus "Wow, uh, excuse me. I just have to ask..."
    show mean
    mean_offscreen "Hm?"
    show mean happy2
    n "The buttery bundle of barbs bites into some bacon."
    show mean happy
    show arceus worried
    arceus "It's... uh... getting pretty late. How can you possibly eat all of that so close to bed?"
    mean_offscreen "{i}Crunch, chew...{w=0.25}{nw}"
    mean_offscreen "Oh, no!"
    mean_offscreen "{i}Gulp!{w=0.25}{nw}"
    show mean
    mean_offscreen "I just woke up, actually."
    mean_offscreen "Today's a big day, so my friend made me this massive breakfast to celebrate!"
    show mean happy2
    n "The popcorn-colored pincushion prepares to pursue another pancake."
    show mean happy
    arceus "Oh, wait! You've been asleep all day?"
    mean_offscreen "{i}Munch, munch...{w=0.25}{nw}"
    mean_offscreen "Yeah! Shift work... you know how it goes."
    arceus "That, I do..."
    arceus "It's just that, uh..."
    arceus "If you've been asleep..."
    arceus "Have you heard about what happened?"
    mean_offscreen "{i}Gulp.{w=0.25}{nw}"
    pause 1.0
    show mean ayo
    mean_offscreen "No{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?"
    arceus "Well, uh... are you missing anything? Especially anything valuable?"
    mean_offscreen "Nah, I didn't even bring anythin--{w=0.25}{nw}"
    show mean wat
    stop music fadeout 3.0
    music end
    "..."
    mean_offscreen "Wait."
    show mean angry 
    with Dissolve(1.0)
    # the dissolve was arc's idea lol
    pause 1.0
    mean_offscreen "Why?"
    arceus "We had some stuff stolen. A lot of people did, actual--{w=0.25}{nw}"

    # mean wanted the following section.
    
    play music prof_kranes_kidnap if_changed
    music prof_kranes_kidnap

    show mean furious
    mean_offscreen "{i}WHAT?!" with hpunch
    if fun_value(FUN_VALUE_MUSIC):
        mean_offscreen "{cshake}{size=+36}PROF. KRANE'S BEEN {i}KIDNAPPED?{/i}" with vpunch
        mean_offscreen "{cshake}{size=+36}ON {i}MY{/i} FUCKING TRAIN?!" with vpunch
    else:
        mean_offscreen "{cshake}{size=+36}ON {i}MY{/i} FUCKING TRAIN?!" with vpunch
    mean_offscreen "MY FIRST SHIFT STARTS IN {cshake}{i}TWENTY MINUTES!" with hpunch
    n "One can practically see the gears begin to turn in Arceus' head as he realizes who he is talking to."

    # arc wanted this
    if fun_value(FUN_VALUE_EPIC):
        show arceus
        arceus "Wait, hey, can you do a Dallas impression?"
        show mean wat
        mean "Like this?"
        show mean furious

        # TODO: record the dallas AUUUUUUUUUGH when mean is better

        mean "{cshake}{size=+36}AUUUUUUUUUGH!!" with hpunch
        show arceus happy
        arceus "Yeah!"
        show arceus worried
        arceus "... Wait."

    show arceus worried
    arceus "Oh."
    arceus "{i}Fuck."
    show mean scared at offscreenright with MoveTransition(0.2)
    n "Mean dashes out of the dining car!"

    scene
    show amtrak_desert_night as left:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, -400)

    show amtrak_desert_night as right:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, 400)
    show amtrak_dining_car
    with dissolve
    pause 1.0
    show mean scared at offscreenleft with determination
    show mean scared at offscreenright
    with MoveTransition(0.25)
    pause 2.0
    show arceus worried flipped at center with moveinleft
    pause 1.0
    n "Arceus, visibly shaken, leaves as well, without even getting the drink he came for."

    # fun value
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        $ train_pancake_fun_value = True
        n "He did at least steal a couple pancakes."

    n "He rushes back to the sleeper car as quickly as he can."
    show arceus worried flipped at offscreenright with MoveTransition(0.3)
    scene black with dissolve
    jump train_wakeup
    
label train_wakeup:
    play music prof_kranes_kidnap if_changed
    music prof_kranes_kidnap
    play sound2 sfx_csnore fadein 0.5
    scene 
    show amtrak_desert_night
    show amtrak_sleeper_interior_night
    with dissolve
    play sound sfx_sliding_door_open
    pause 1.0
    show arceus worried dark flipped at offscreenleft with determination
    show arceus worried dark flipped at center with MoveTransition(0.4)
    pause 0.5
    arceus "CS!" with hpunch
    arceus "Wake up!!"
    cs "Hnnnh... huh?"
    n "Arceus flips on the lights."
    show arceus worried dark at left with MoveTransition(0.25)
    play sound sfx_lightswitch
    scene 
    show amtrak_desert_night
    show amtrak_sleeper_interior_day
    show arceus worried at left
    pause 0.25
    show arceus worried flipped at left
    pause 0.25
    n "CS lets out a groan and rolls back over in bed."
    show arceus angry flipped
    play sound sfx_csnore
    cs "Zzzzz..."
    cs "{size=-15}Five more minutes, mom..."
    show arceus angry flipped at right with MoveTransition(0.35)
    n "Arceus pulls the blanket off of CS and drags him out of bed."

    show arceus angry flipped at mid_offscreen_right with MoveTransition(0.25)
    show cs concentrate flipped at offscreenright with determination
    pause 0.5
    play sound sfx_blanket volume 20
    stop sound2
    pause 0.5
    show arceus angry flipped at center
    show cs concentrate flipped at right
    with moveinright
    
    cs "Hnngh, huh, what, {i}why?!"
    show cs disappointed flipped
    cs "Wha-- What's going on?"
    pause 0.5
    n "CS notices Arceus is out of breath and panicking."
    show cs worried flipped
    cs "Wait, Arc, what's wrong?"
    cs "Are you alright?"
    show arceus worried flipped
    arceus "Dude, I fucked up!"
    arceus "I went to the dining car for a drink, and there was this... {i}thing!{/i}{w=0.5} He was eating this {i}insane{/i} amount of food, so I went to talk to him!"
    arceus "He was asleep all day and didn't know about the thief, so I asked him if he's missing anything--{w=0.5}{nw}"
    arceus "That thing was {i}Mean!"
    show cs surprised flipped
    cs "Wait, he was mean to you? What'd he do?"
    show cs worried flipped
    show arceus angry flipped
    cs "Are you okay?"
    arceus "What?! {i}No!"
    arceus "Tate's friend, {i}Mean!"
    arceus "The new night driver!"
    show cs scared flipped
    pause 0.5
    cs "{w=0.25}... Oh,{w=0} no."
    cs "We are {i}definitely{/i} in trouble n--{w=0.25}{nw}"
    show arceus worried with hpunch
    music end
    play sound sfx_sliding_door_open volume 2.0
    n "As if on cue, the room door slides open fully." with hpunch
    
    tate "{cshake}{size=+24}C.{w=0.1}S. ONE HUNDRED AND EIGHTY{w=0.1}-EIGHT!!" with vpunch

    show arceus worried at mid_mid_right
    show tate furious at left
    with moveinleft
    play sound sfx_punch
    with hpunch

    n "Tate stomps into the room, making a beeline for CS."
    show tate furious at mid_mid_left with moveinleft
    play sound sfx_punch
    with hpunch

    if fun_value(FUN_VALUE_COMMON):
        tate "YOU HAD {cshake}{i}ONE{/i}{/bt} JOJ!" with vpunch
        show tate furious at center with moveinleft
        play sound sfx_punch
        with hpunch
        tate "YOU'RE GONNA NEED A WHOLE LOT MORE THAN {cshake}{i}FOUNDATION\nREPAIR{/i}{/bt} AFTER {i}I'M{/i} DONE WITH YOU!" with vpunch
    else:
        tate "YOU HAD {cshake}{i}ONE{/i}{/bt} JOB!" with vpunch
        show tate furious at center with moveinleft
        play sound sfx_punch
        with hpunch
        tate "IS IT REALLY {i}THAT{/i} HARD FOR YOU TO KEEP A SECRET?!" with vpunch

    cs "Tate, wait!"
    arceus "It wasn't him!"
    arceus "I'm sorry!"
    n "Tate inhales for another scream."
    arceus "I didn't know Mean was... {i}like{/i} that!"

    stop music

    show tate shock
    pause 1.0
    n "Tate is caught off-guard by Arceus' comment."
    pause 1.0
    show cs worried flipped
    show tate srs at mid_mid_left with moveinright
    pause 2.0

    tate "Like... what?"
    arceus "I thought he'd be... just... you know... {i}some guy."
    arceus "I didn't know he's, uh... whatever he is."
    pause 2.0

    play music e_gadds_lab if_changed
    music e_gadds_lab

    show tate sheepish
    show cs disappointed flipped
    pause 2.0
    "..."
    tate "{i}O{w=0.1}-Oh..."
    pause 1.0
    tate "I guess... {w=0.5}{size=-5}that would have been... {w=0.5}{size=-5}an {i}important{/i} detail to...{w=1.0}"
    tate "{size=-15}{i}Fuck..."
    pause 3.0
    if fun_value(FUN_VALUE_MUSIC):
        n "Heavy breathing approaches from E. Gadd's Lab."
    else:
        n "Heavy breathing approaches from the hallway."
    pause 1.0

    show mean tired at offscreenleft with determination

    show mean tired at mid_offscreen_left
    show tate sheepish at mid_mid_left
    with { "master" : MoveTransition(0.5) }
    mean "{i}Pant... {w=0.25}{nw}"
    show mean tired at left with { "master" : MoveTransition(0.5) }
    mean "{i}Pant... {w=0.25}{nw}"
    show mean tired at center_left with { "master" : MoveTransition(0.5) }
    mean "{i}Wheeze... "

    show mean surprised
    mean "There... {i}cough"
    mean "... There you are, Tate..."
    
    # here goes tate having too much fun with sprites again

    show tate shock flipped
    show mean scared
    show cs scared flipped
    tate "{cshake}{size=+12}Uwaaaaah!" with vpunch
    tate "Mean!"
    show tate sad flipped
    show mean surprised
    tate "I'm so sorry!"
    tate "I told them not to tell you!"
    show mean wat
    mean "Tate--{w=0.25}"
    tate "I wanted it to be kept secret so you could focus on work and{w=0.1}{nw}"
    tate "I think the day shift people think I'm to blame for everything and{w=0.1}{nw}"
    show mean angry
    show cs worried flipped
    mean "{size=+12}{i}Tate--!{w=0.1}"
    tate "I was really scared that they might blame you too since{w=0.1}{nw}"
    show cs disappointed flipped
    show arceus angry
    tate "you were asleep all day and that means that you were the only one not accounted for when--{w=0.1}{nw}"
    show mean furious
    show tate shock flipped
    show cs scared flipped
    show arceus worried
    mean "{cshake}{size=+24}{i}TAAAAATE!!" with vpunch

    show mean ayo
    mean "What the fuck are you {i}talking{/i} about?"
    show tate cry flipped
    show cs disappointed flipped
    tate "{sc=1}{size=-15}I just wanted you to have a good first day..."
    show mean worried
    mean "What do you mean?"
    show mean 
    mean "Today's been {i}great!"
    show tate shock flipped
    tate "Huh?!" with vpunch
    show mean happy
    mean "Yeah!"
    mean "You made me the best breakfast I've had in ages, I start my dream job in 15 minutes, {i}and{/i} I get to travel the US with one of my best friends!"
    
    if train_pancake_fun_value == True:
        show arceus happy
        arceus "{size=-15}Those were some damn good pancakes, by the way."
        show arceus worried

    mean "If it weren't for you, I'd still be sitting at home playing fucking {i}Minecraft{/i} and listening to whatever weird shit's popular on Spoofy!"
    mean "What could be better?"
    show tate sad flipped
    tate "But, what about the thief?!"
    show mean ayo
    mean "Wait, you think Amtrak actually {i}gives{/i} a shit about stolen items?"
    show mean angry
    mean "Bro, I was more worried about {i}you!"
    show cs disappointed flipped
    show mean worried
    mean "When that yellow fucker over there told me there was a crook on the train, I was worried that somebody was out here, like, {i}mugging{/i} people!"
    show arceus angry
    arceus "\"Yellow fucker\"?"

    # let's turn my shitpost into a fun value i suppose lmao
    if fun_value(FUN_VALUE_LEGENDARY):
        $ train_tate_is_fragile_fun_value = True
        mean "Like, no offense, Tate, but you only have, like, 5 DEF."
        show arceus 
        arceus "They {i}do{/i} have decent ATK and one of the only healing moves in the game, though."
        cs "Huh?"
        show tate srs
        show mean ayo
        tate "Don't I {i}at least{/i} have plot armor?"
        tate "I'm a major character in this route!"
        show cs worried flipped
        cs "What are you all {i}talking{/i} about?!"
        show tate shock
        show mean surprised
        show cs scared flipped
        show arceus worried
        n "Hi, it's me, the narrator."
        n "This game is called CSBounciness, not alleZScreminess."
        n "No plot armor for you."
        show mean wat
        show tate furious
        tate "What the {i}fuck?" with vpunch
        show tate srs flipped
        show mean worried
        tate "Who wrote this?"
        show tate sheepish
        show mean worried
        n "You are not prepared for the answer to that question."
        show cs disappointed flipped
        cs "I must be {i}really{/i} sleep-deprived..."
    else:
        mean "Like, no offense, Tate, but you aren't exactly at the peak of physical condition."    
        show mean angry
        mean "Didn't you sprain {i}both{/i} of your ankles at the same time last year just from {i}walking?"
        show arceus worried
        show cs worried flipped
        show tate sheepish flipped
        tate "Yes..."
        show cs disappointed flipped

    show arceus worried
    show tate sheepish flipped
    show mean worried
    mean "...  Right."
    mean "Anyway, I just needed to make sure you were safe."
    mean "Now, I don't want to be late for my very first shift, so I've gotta get going."
    mean "I'm gonna go grab my hat, then I'll be in up the front of the train if you need me."
    show mean happy
    mean "Feel free to swing by the cab if any of you want to see the railroad!"
    show mean angry
    mean "Also, Tate, {i}please{/i} remember to listen to the staff, okay?"
    show tate sad flipped
    mean "The day conductor won't let me hear the end of it..."
    tate "Yes..."
    show mean
    mean "Cool. See you later!"
    show mean flipped:
        rotate 0
        linear 1 rotate -180
    hide mean with moveoutleft
    n "Mean rolls away down the hall."
    show tate sheepish at left with moveoutleft
    pause 1.0
    show tate sheepish
    tate "So, uh..."
    tate "I guess, since Mean has to start work..."
    show arceus
    tate "What do y'all think we should do?"

    menu:
        tate "What do y'all think we should do?{fast}"
        "Let the staff handle it":
            jump train_allow_staff
        "Take matters into your own hands":
            jump train_begin_heist

######## BAIL NOW ########
label train_allow_staff:
    play music e_gadds_lab if_changed
    music e_gadds_lab
    scene 
    show amtrak_desert_night
    show amtrak_sleeper_interior_day
    show tate sheepish at left
    show arceus at mid_mid_right
    show cs disappointed flipped at right
    $ train_skip_at_chicago = True

    cs "I think we should just let the staff do their jobs."
    tate "Even though Mean said Amtrak doesn't care about stolen things?"
    show cs happy flipped
    cs "I mean, the day conductor said that he was investigating. He seemed pretty serious."
    show tate srs
    tate "Oh, come {i}on.{/i} Do you {i}really{/i} trust that guy?"
    show cs disappointed flipped
    cs "Do we really have a choice? It's clear that they don't want you interfering."
    show tate furious
    tate "Sometimes, {i}interfering{/i} {nw}" with vpunch
    tate "Sometimes, {i}interfering{/i} {fast}is the only way things get {nw}"
    tate "Sometimes, {i}interfering{/i} is the only way things get {fast}{i}done!" with vpunch
    show arceus angry
    arceus "Okay, I am {i}not{/i} about to spend the rest of this trip listening to you two bickering."
    arceus "Let's just let them do the investigation, and if we get it back, we get it back."
    arceus "I'm tired, we've been through hell, and I want to go to bed."
    show tate sad
    tate "I suppose it {i}is{/i} late..."
    show tate sheepish
    tate "It was nice seeing you again, CS. It was nice to meet you too, Arc."
    tate "I hope you two enjoy the rest of the journey!"
    scene black with dissolve
    n "Tate bids CS and Arceus farewell before heading towards the cab to join Mean."
    n "CS and Arceus spend the following day resting and admiring the vast and varied scenery of The Midwest."
    n "As expected, the money is never returned."
    $ train_ending_money_returned = False
    n "After a brief layover in Chicago and a haughty \"I told you so\" from Tate, CS and Arceus take the final uneventful transfer to New York."
    # TODO: if there is going to be a chicago route, it needs to be jumped to from here.

    jump train_return_home_transition

######## BEGIN THE HEIST ########
label train_begin_heist:
    play music e_gadds_lab if_changed
    music e_gadds_lab
    scene 
    show amtrak_desert_night
    show amtrak_sleeper_interior_day
    show tate sheepish at left
    show arceus at mid_mid_right
    show cs disappointed flipped at right
    $ train_skip_at_chicago = False
    cs "Do you really think we'd be able to track down the thief?"
    tate "I sure hope so. Like you said earlier, unless they jumped off of a moving train, they've gotta be here."
    show cs flipped
    cs "Hey, Arc! You've done cybercrime before, right?"
    show arceus angry flipped
    cs "Where do you think the thief would hide stolen goods?"
    show tate shock
    tate "Arc did {i}what,{/i}{w=0} now?!"
    show cs worried flipped
    arceus "Gee, {i}thanks,{/i} CS."
    arceus "But, since you asked..."
    show arceus
    show tate sheepish
    show cs disappointed flipped
    arceus "I have a few theories. There aren't many places to hide on a train like this."
    arceus "We can check the sleeper cars here, we could check the dining car..."
    arceus "I doubt we can get access to it, but maybe we could get someone to check the cab."
    tate "Actually, Mean lent me his spare key to the cab in case I needed the toilet in there, so I can check it."
    arceus "Oh, nice. I know my way around the dining car, so I can look there."
    $ next_line = substitutions("Guess I'll stick around here, then. Maybe the " + train_money_container + " is just under a seat or something.")
    cs "[next_line]"
    arceus "Sounds like a plan."
    show tate
    show cs flipped
    tate "Yep, I'll head out then. Let's meet up in coach when we're done looking."
    cs "Yeah, sounds good."
    arceus "Sure thing."
    tate "Well, let's get to it, then."
    show tate flipped
    pause 0.5
    hide tate
    hide arceus
    with moveoutleft

    n "CS, Arceus, and Tate split up to search the different areas of the train."
    pause 0.5

    stop music fadeout 3.0
    music end
    scene black with dissolve
    jump train_meanwhile

label train_meanwhile:
    pause 0.5
    centered "Meanwhile..."
    pause 0.5
    scene
    show car plains night
    show amtrak_cab
    show lupin stand at center
    with dissolve
    play music onbs if_changed
    music onbs

    pause 1.5
    if fun_value(FUN_VALUE_MUSIC):
        lupin_offscreen "This is {i}perfect!{/i} I can't believe I could just ON-{i}BS{/i} my way in here like that!"
    else:
        lupin_offscreen "This is {i}perfect!{/i} I can't believe I could just waltz on in here like that!"
    show lupin stand hat with dissolve
    # TODO: make lupin actually put on the hat
    lupin_offscreen "And, with {i}this..."
    lupin_offscreen "Nobody would ever suspect the driver, right?"
    play sound sfx_sliding_door_open
    n "The cab door suddenly opens from behind."
    show lupin stand hat flipped
    pause 1.0
    show lupin stand hat flipped at mid_left
    show amtrak_conductor at right
    with moveinright
    play sound sfx_sliding_door_close
    amtrak_conductor "Oh, good evening, Mean."
    amtrak_conductor "I almost didn't recognize you {color=#D9053A}like that.{/color}"
    amtrak_conductor "Well, you already know the drill, so I'll leave you to it."
    lupin_offscreen "You got it, boss!"
    amtrak_conductor "Hopefully your little friend will stay out of the way tonight. Corralling them all day has me absolutely beat."
    lupin_offscreen "No worries, boss. I'm sure {color=#FFDBFC}pink sweater{/color} is tired from cooking all day."
    amtrak_conductor "I would certainly hope so."
    amtrak_conductor "For now, it's been a long day."
    amtrak_conductor "If you'll excuse me..."
    hide amtrak_conductor with moveoutleft
    show lupin stand hat
    play sound sfx_sliding_door_open
    n "The conductor retires to the cab toilet for a while."
    play sound sfx_sliding_door_close
    pause 4.0
    play sound sfx_fart_with_reverb
    with hpunch
    with hpunch
    with hpunch
    pause 1.5
    lupin_offscreen "... Seems like he'll be a while."
    show lupin run hat flipped at center with moveinright
    lupin_offscreen "And,{w=0} that's just what I need."
    scene black with dissolve
    pause 1.0
    jump train_search_arceus

label train_search_arceus:
    play music onbs if_changed
    music onbs
    scene
    show amtrak_desert_night as left:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, -400)

    show amtrak_desert_night as right:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, 400)
    show amtrak_dining_car

    show amtrak_dining_car
    show arceus at center
    with dissolve
    n "Arceus returns to the dining car."
    arceus "Well, let's see if anything is hidden around here..."
    show arceus at left with ease
    show arceus at manual_pos(-50,950) with ease
    n "Arceus checks under the tables..."
    show arceus at left with ease
    show arceus flipped at center with ease
    show arceus flipped at right with ease
    show arceus flipped at manual_pos(1460,950) with ease
    n "Then, he checks under the seats..."
    show lupin run hat at offscreenright behind arceus with determination
    show lupin run hat at offscreenleft
    with MoveTransition(2.0)
    show arceus flipped at right with ease
    show arceus at center with ease
    n "All he finds is trash and loose change."
    pause 1.0
    show arceus worried
    arceus "I guess there's just nothing here."

    scene
    show amtrak_desert_night at manual_pos(0.5, 0.4, 0.5)
    show amtrak_dining_table
    show amtrak_dining_food at manual_pos(805,145)
    show amtrak_dining_pancake at manual_pos(915,575) behind amtrak_dining_food
    with dissolve
    n "From across the room, Arceus glances towards the abandoned breakfast." 
    arceus "It's a damn shame that all of that food went to waste."

    if train_pancake_fun_value == True:
        arceus "Mean probably wouldn't care if I took a bit more..."
    else:
        arceus "I wonder if Mean would mind if I grabbed a bit before it goes bad..."

    show lupin stand hat at mid_right with moveinright
    n "A stranger wanders up to the table."
    pause 1.0
    show amtrak_dining_food at offscreenleft
    play sound sfx_whoosh
    show lupin run hat at offscreenleft
    with ease
    pause 0.5
    arceus "What the fuck?!"
    pause 0.5
    show arceus angry at right behind amtrak_dining_pancake with moveinright 
    arceus "Man... what is {i}wrong{/i} with people?!"
    n "Arceus spots a lone pancake."
    show amtrak_dining_pancake at manual_pos(1433, 683) with ease
    $ collect("amtrak_dining_pancake")
    arceus "At least there's this one..." 
    hide amtrak_dining_pancake with dissolve
    pause 1.5
    arceus "I need a drink..."
    show arceus angry flipped
    hide arceus with moveoutright
    scene black with dissolve
    pause 2.5
    arceus "What the fuck? He even took all the {i}booze?!"
    jump train_search_cs
    
label train_search_cs:
    play music onbs if_changed
    music onbs
    
    # TODO: YES I KNOW THIS SCENE IS CRUSTIER THAN FRENCH BREAD PLS HELP

    pause 1.5
    scene amtrak_sleeper_corridor
    show cs disappointed at center
    with dissolve
    pause 1.0

    n "CS finds himself alone in the deserted corridor."
    cs "I guess I should have expected that nobody would keep their doors open this late."
    cs "I probably should have {i}also{/i} expected that nobody would want to let me in..."
    show cs worried
    cs "That lady in Room 3 threw a {i}shoe{/i} at me, for fuck's sake!"
    show cs disappointed
    cs "Maybe I should just go find the others..."
    show cs disappointed at right with MoveTransition(0.5)
    pause 1.0
    n "CS stops suddenly."
    n "There is, in fact, a single door open." 
  
    scene
    show amtrak_desert_night at manual_pos(0.5, 0.35, 0.5):
        xzoom -1.0
        zoom 0.75
    show amtrak_sleeper_open_bg
    show lupin run hat at mid_right
    
    if train_money_stolen == True:
        show bag at mid_mid_left
    else:
        show briefcase at mid_mid_left

    show amtrak_dining_food at mid_mid_left
    show amtrak_sleeper_open_fg
    with dissolve

    n "A man in an oddly familiar red jacket is finishing off a small feast."
    lupin_offscreen "I can't believe how easy that was. {color=#FFDBFC}Pink sweater{/color} had the staff running around like ants!"
    lupin_offscreen "They don't know it, but they'd be my {i}perfect{/i} accomplice!"
    hide amtrak_dining_food with dissolve
    pause 1.0
    lupin_offscreen "Mmmm...{done} {i}Burp!{/i}" 
    lupin_offscreen "Mmmm...{fast} {i}Burp!{/i}" with hpunch
    lupin_offscreen "Oh, pardon me!"
    lupin_offscreen "I guess asking them on a dinner date would be a bad idea. They'd totally out-cook the chef!"
    lupin_offscreen "I wonder if they like movies..." 
    n "CS can't help but notice something..."
    n "He decides to try looking from another angle."

    show amtrak_sleeper_open_bg at mid_mid_left
    show amtrak_sleeper_open_fg at mid_mid_left
    with ease

    pause 2.0
    cs "Hey! That's our cash!"
    cs "Hey,{w=0} you! Give that back!" with hpunch
    lupin_offscreen "Well, would you look at that? It's my pretty kitty!"
    lupin_offscreen "Sorry, babe, but I've gotta split!"

    scene amtrak_sleeper_corridor
    show cs angry at center
    play sound sfx_whoosh
    show lupin run hat at offscreenright
    show lupin run hat at center with MoveTransition(0.25)

    play sound sfx_punch
    show cs scared at mid_offscreen_left with hpunch
    show cs concentrate
    hide lupin with dissolve
    
    pause 2.0
    n "Before CS can stand up to catch him, the thief disappears into the next car."
    pause 1.0
    show cs concentrate at center with MoveTransition(1.0)
    pause 1.0
    show cs disappointed
    pause 1.0
    cs "Not again..."
    pause 0.5
    show cs surprised
    cs "Wait..."
    pause 0.5
    show cs disappointed
    cs "\"Pretty kitty\"?"
    pause 1.5
    cs "That means..."
    pause 1.0
    show cs angry
    cs "... That guy must have stolen the money when he knocked me down earlier!"
    cs "At least I got a good look at his face this time!"
    cs "I need to find Arc and Tate!"
    show cs angry at offscreenright with MoveTransition(0.35)
    scene black with dissolve
    jump train_search_tate

label train_search_tate:
    play music onbs if_changed
    music onbs
    pause 1.0

    scene
    show car plains night
    show amtrak_cab
    show lupin stand hat at left
    with dissolve

    play sound sfx_sliding_door_open
    pause 3.0

    show tate flipped behind lupin at offscreenright
    show tate flipped at mid_right with moveinright
    
    tate "Excuse me, Mr. Conductor?"
    show lupin stand hat flipped
    tate "Have you seen--{w=0.25}{nw}"
    show tate srs flipped
    "..."
    pause 2.0   
    tate "... Why are {i}you{/i} here?"
    
    lupin_offscreen "Hey, look, it's my favorite {color=#FFDBFC}pink sweater{/color}!"
    show lupin stand hat flipped at mid_mid_left with { "master" : MoveTransition(0.5) }

    lupin_offscreen "We just seem to keep finding each other!"
    show lupin stand hat flipped at center
    show tate srs flipped at right
    with { "master" : MoveTransition(0.5) }

    lupin_offscreen "Are you absolutely sure you mean what you say?"
    show lupin run hat flipped at mid_mid_right
    show tate srs flipped at mid_offscreen_right
    with { "master" : MoveTransition(0.5) }

    lupin_offscreen "Are you absolutely {i}sure{/i} that we're not meant to be?{image=heart_small.png}"
    show lupin hat flipped at right with moveinleft
    pause 0.1
    play sound sfx_punch
    show tate furious flipped
    show lupin hat flipped at left with MoveTransition(0.1)
    with hpunch
    n "Tate pushes the stubborn suitor away."
    show lupin stand hat flipped
    show tate srs flipped at right with moveinright
    pause 1.0
    tate "There are only three things in my life that I have {i}ever{/i} been more sure of."
    tate "Now... I don't know who you are, but, I'm getting really sick of seeing you."
    tate "I had {i}hoped{/i} you'd finally taken the hint while I was cooking this morning, but, I guess I have to spell it out for you."
    tate "I am {i}not{/i} interested."
    tate "Second order of business..."
    tate "You will give me that hat right this instant."
    tate "You will leave the cab, you will not come back, and nobody will get hurt."
    lupin_offscreen "Pfft, hurt by who? {i}You?"

    if train_tate_is_fragile_fun_value == True:
        show tate sheepish flipped
        lupin_offscreen "With your whopping {i}5 DEF?"

    lupin_offscreen "The sea urchin isn't here yet--{w=0.5}{nw}"
    show tate shock flipped
    play sound sfx_fart
    with vpunch
    with hpunch
    with hpunch
    pause 2.0
    lupin_offscreen "... and it appears that the {i}muscle{/i} of your crew is currently {i}unavailable."
    play sound sfx_poot
    with vpunch
    pause 1.0
    show tate sheepish flipped
    tate "N-{w=0.1}Now, you listen here. Don't underestimate me..."
    tate "Just give me the hat, yeah? Besides, even if you're not scared of {i}me,{/i} Mr. Conductor will probably be done in there at any moment."
    play sound sfx_fart_deep
    with vpunch
    with vpunch
    with vpunch
    pause 3.0
    tate "{size=-15}...{w=0} Or,{w=0} not."
    pause 1.0
    show lupin stand hat flipped at center with MoveTransition(1.0)
    n "The suave criminal leans in closer to Tate."
    pause 0.5
    lupin_offscreen "Tell ya what, pumpkin."
    lupin_offscreen "If you'll agree to {i}one{/i} date with me, I'll give you the hat."
    show tate srs flipped
    tate "Not a chance in hell."
    lupin_offscreen "Well, then. It appears that we are locked in a stalemate, now, aren't we?"
    lupin_offscreen "I, for one, love chess, but I have it on good authority that it's not your cup of tea."
    show tate sheepish flipped
    tate "Wait, how did y--{w=0.25}{nw}"
    lupin_offscreen "I feel like we'd both prefer to play a different game anyway."
    tate "Speak for yourself..."
    lupin_offscreen "No, no, hear me out! Personally, I'm a {i}huge{/i} fan of hide-and-seek."
    tate "Wha--{w=0.25}{nw}"
    lupin_offscreen "Ah, but today's your lucky day!"
    lupin_offscreen "You see, I {i}also{/i} happen to know that you're bad at counting."
    lupin_offscreen "Fortunately for you, you'll only need to count to 1."
    show lupin run hat flipped
    lupin_offscreen "Catch me if you can.{image=heart_small.png}"
    show tate shock flipped
    play sound sfx_whoosh
    show lupin run hat flipped at offscreenright with MoveTransition(0.25)
    show tate shock at right
    pause 1.0
    n "The crook is gone without a trace."
    tate "Oh,{w=0.1} no!"
    tate "I've {i}got{/i} to get that hat back!"
    show tate shock flipped at left with MoveTransition(0.25)
    play sound "<from 0 to 0.621>audio/sfx/sfx_fbi_open_up.ogg"
    with hpunch
    with hpunch
    tate "{cshake}{size=+24}Mr. Conductor!!" with hpunch
    tate "We've got trouble!"
    amtrak_conductor "My apologies, Mx. Frost. I'm a little {i}busy."
    amtrak_conductor "Where is Mean?"
    show tate cry flipped
    tate "I-{w=0.1}I don't know!"
    amtrak_conductor "What do you mean you {i}don't know?{/i} He was just in there a minute ago."
    tate "I don't know, okay?! He's just {i}not{/i} in here!"
    tate "I'll go find CS and Arc! They're the only other people who might've seen him!"
    amtrak_conductor "That may be the first good idea you've had all day."
    show tate sheepish flipped
    tate "Uweh?"
    amtrak_conductor "Go find another staff member if you can, too. I'll be with you shortly."
    tate "Yes, sir!"
    show tate sheepish at offscreenright with moveoutright
    pause 0.5
    play sound sfx_sliding_door_close
    pause 6.0
    play sound sfx_fart_lite
    with hpunch
    with hpunch
    with hpunch
    pause 2.0
    amtrak_conductor "I guess it's time to switch protein shakes..."
    pause 0.5
    scene black with dissolve
    pause 1.0
    jump train_confront_lupin

label train_confront_lupin:
    play music onbs if_changed
    music onbs

    scene
    show amtrak_desert_night at manual_pos(0.5, 0.4, 0.5):
        xzoom -1.0
        rotate -5
    show amtrak_coach_1
    show arceus angry at offscreenright
    show tate sad at left
    show mean worried flipped at truecenter
    with dissolve
    n "CS shows up in economy to find Tate with Mean. The pair appears to be frustrated over something."
    pause 1.0
    show cs disappointed flipped at right behind arceus with moveinright
    pause 1.0
    cs "Hey guys, what's going on? Did you find anything?"
    show mean worried
    show tate sad
    tate "CS! It's terrible!"
    tate "Mean's hat was stolen!"
    mean "{size=-15}Mah fuckin' hat..."
    show cs angry flipped
    cs "I wonder if it's the same guy who has our money..."
    show tate shock 
    show mean ayo
    tate "Wait, you saw who had it?!"
    cs "Yeah! Some guy in a red jacket ran off with it!"
    show mean unamused
    show tate stare
    mean "Oh, yeah, that's {i}real{/i} descriptive."
    mean "Even {i}I{/i} wear a red jacket sometimes."
    show cs disappointed flipped
    cs "You do? {i}How?"
    show tate sheepish
    tate "Well, you see--{w=0.5}{nw}"
    show mean angry flipped
    mean "Anyway, you were saying, before CS came in, that you saw the bastard who took my hat?"
    show tate srs
    tate "Yeah. Remember that guy I told you about earlier?"
    tate "The one who's been bugging me since we left Cali?"
    show mean unamused flipped
    mean "Are you sure you aren't just saying that so the staff has an excuse to get rid of the guy?"
    show tate furious
    tate "{i}No!{/i} I'm serious!" with vpunch
    tate "He {i}also{/i} wears a red jacket!"
    tate "The fucker ran off with your hat before I could catch him!"
    n "As the two continue to argue, a familiar grumbling approaches the group."

    show cs disappointed flipped at mid_mid_right
    show mean unamused flipped at center_mid_left
    show arceus angry at right
    with { "master" : MoveTransition(1.5) }
    arceus "{size=-15}Fuckin' ridiculous...{w=0.5}{nw}"
    arceus "{size=-15}All the fuckin' booze..."

    show cs disappointed
    show mean unamused
    show tate sheepish
    
    cs "Oh, hey, Arc. You find anything in the dining car?"
    arceus "I sure did! This dude in a red coat just walked away with that {i}entire{/i} goddamn pile of food!"
    show mean angry
    show tate shock
    show cs worried
    mean "Mah fuckin' {i}food,{/i} too?!" with hpunch   
    show cs disappointed
    show tate sheepish
    cs "... Why do {i}you{/i} seem so upset about it, Arc?"
    show arceus worried
    arceus "Because he {i}also{/i} stole all the {i}alcohol!"
    show mean worried
    mean "Jesus..."
    show mean angry flipped
    show cs disappointed flipped
    mean "Tate, did you know about this?"
    show tate sad
    tate "No!"
    mean "Damn..."
    mean "Where's the conductor? Is he still on duty?"
    show tate sheepish
    tate "Well, uh...{w=0.25}{nw}"
    play sound sfx_fart_again
    show cs scared flipped
    show tate shock flipped
    show mean scared flipped
    with hpunch
    pause 2.0
    show tate sheepish

    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        tate "He's on \"doodie\", alright..."
    else:
        tate "He's... a little busy."

    show mean unamused flipped
    show cs worried flipped
 
    mean "God damn it, I told him not to mix that protein powder with milk."
    show mean angry
    show cs disappointed flipped
    mean "Well, I guess it's up to us to find the guy."
    mean "I can't start work without my hat!"
    show arceus worried
    arceus "What's so special about the hat?"
    cs "And, isn't our money a {i}little{/i} more important than your hat?"
    show mean worried
    show cs disappointed flipped
    mean "Nah, you don't understand."
    mean "That hat is one-of-a-kind."
    arceus "That doesn't explain why you need it to drive the train..."
    mean "I'm talking triple-stitched, reinforced, dual-layered denim, lined with 100-percent pure Merino wool!"
    arceus "That... still doesn't explain anything."
    show mean unamused
    mean "I'm spiky. I need a hat that'll hold up."
    show arceus angry
    arceus "That {i}still{/i} doesn't explain why you can't work without it!"
    show mean angry

    if fun_value(FUN_VALUE_COMMON):
        mean "Me without my hat is like Mario without {i}his!"
        mean "Just because it's a game mechanic doesn't mean that it's {i}right!"
    else:
        mean "Bro, just {i}look{/i} at me. I can't exactly fit into a standard uniform, now, can I?"

    show arceus worried
    arceus "I... suppose not."
    mean "Let's just start looking."
    tate "Should we split up a--{w=0.5}{nw}"
    show mean angry flipped
    mean "No,{w=0} the fuck we should {i}not." with vpunch
    mean "We've got you, two dudes, and a dog-thing."
    show arceus angry
    mean "I've seen enough {i}Scooby-Doo{/i} to know how {i}that{/i} would end."
    mean "We're gonna stick together in case this guy is dangerous."
    show mean angry
    mean "You two on board with this?"
    cs "Works for me..."
    arceus "{size=-15}Fuck you mean, \"dog-thing\"?"
    mean "Let's go."
    show mean angry at offscreenright with moveoutright
    show tate sheepish at offscreenright
    show cs disappointed at offscreenright
    show arceus angry flipped at offscreenright
    with moveoutright
    scene black with dissolve
       
    n "The four make their way towards the very last car on the train."

    scene
    show amtrak_desert_night as left at manual_pos(0.2, 0.5, 0.5):
        xzoom 0.75
        yzoom 0.5
        rotate -25
    show amtrak_desert_night as right at manual_pos(0.8, 0.5, 0.5):
        xzoom -0.75
        yzoom 0.5
        rotate 25
    show amtrak_coach_2
    with dissolve
    
    show mean angry flipped at left
    show tate sheepish flipped at mid_mid_left
    show cs disappointed flipped at mid_mid_right
    show arceus angry at right
    with moveinright
    
    n "Searching one section after another, they fail to find any sign of the suspect in coach."
    
    show mean angry flipped at offscreenleft
    show tate sheepish flipped at offscreenleft
    show cs disappointed flipped at offscreenleft
    show arceus angry at offscreenleft
    with moveoutleft
    scene black with dissolve
    
    scene
    show amtrak_desert_night at manual_pos(0.5, 0.4, 0.5):
        xzoom -1.0
        rotate -5
    show amtrak_coach_1
    with dissolve
    
    show mean angry flipped at left
    show tate sheepish flipped at mid_mid_left
    show cs disappointed flipped at mid_mid_right
    show arceus angry at right
    with moveinright
    
    pause 1.0
    
    show mean angry flipped at offscreenleft
    show tate sheepish flipped at offscreenleft
    show cs disappointed flipped at offscreenleft
    show arceus angry at offscreenleft
    with moveoutleft
    scene black with dissolve
    
    scene
    show amtrak_desert_night as left:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-20, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -250, -400)
    show amtrak_desert_night as right:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-20, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -250, 400)
    show amtrak_observation_1
    with dissolve
    
    show mean angry flipped at left
    show tate sheepish flipped at mid_mid_left
    show cs disappointed flipped at mid_mid_right
    show arceus angry at right
    with moveinright
    
    n "The group wordlessly follows Mean until they reach the observation lounge, where he suddenly stops."
    
    mean "Hey! You,{w=0} there!" with hpunch
    
    show lupin stand hat flipped at offscreenleft with determination
    show lupin stand hat flipped at left
    show mean angry flipped at center
    show tate shock flipped at mid_mid_right behind mean
    show cs worried flipped at mid_right
    show arceus worried at manual_pos(1.05, 1.0, 1.0)
    with MoveTransition(1.0)
    
    n "The man casually takes a few steps forward."
    n "He immediately locks eyes with CS."
    show cs scared flipped
    lupin_offscreen "Hello again, pretty kitty!"
    show tate srs flipped
    lupin_offscreen "Wow! You brought {color=#FFDBFC}pink sweater{/color}, too?"
    show arceus angry
    lupin_offscreen "{i}And{/i} a fluffy doggo to pet?!"
    show cs angry flipped
    lupin_offscreen "Today must be my lucky--{w=0.5}{nw}"
    mean "Alright, {i}CAN{/i} IT!" with hpunch
    mean "We have some questions for you."
    mean "And, {i}you{/i} have {w=0.25}{i}my hat{/i}{w=0.25} for {i}me."
    mean "You're coming with us."
    show lupin run hat flipped
    lupin_offscreen "Not without a fight!"
    show tate shock flipped
    show cs worried flipped
    show arceus worried
    play sound sfx_whoosh
    show lupin run hat at offscreenleft with MoveTransition(0.25)
    mean "{cshake}{size=+24}Oh,{w=0} no,{w=0} you don't!" with vpunch
    arceus "Shit!"
    cs "What do we do?!"
    mean "Tate! {i}Hit it!"
    show tate shock flipped at center
    show cs worried flipped at mid_right_right
    show arceus worried at mid_offscreen_right
    with MoveTransition(0.5)
    tate "Ohshitohfuckohshitohfuck--{nw}"
    show mean furious flipped
    mean "{cshake}{size=+24}JUST THROW ME,{w=0} ALREADY!"
    play sound sfx_whoosh
    show mean furious at truecenter with MoveTransition(0.1)
    show mean furious at offscreenleft with MoveTransition(0.25)
    pause 0.25
    play sound sfx_cat_crash
    show fake_rpg_miss at t_fake_rpg_text(0.48, 0.2)
    play sound2 "/audio/sfx/snd_bluh.ogg" volume 0.5 noloop
    show cs scared flipped
    show tate shock flipped
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    with hpunch
    "..."
    show tate sheepish flipped
    n "The attack misses."
    pause 1.0
    show mean unamused at center_left with MoveTransition(1.0)
    show cs disappointed flipped
    "..."
    pause 1.0
    mean "Wow."
    mean "So, are you three {i}always{/i} this useless?"
    tate "In fairness... we probably should've practiced that one more."
    mean "Guess we've gotta do this old-fashioned way."
    show mean angry flipped
    mean "Let's get 'em!"
    
    show mean angry flipped at offscreenleft
    show tate srs flipped at offscreenleft
    show cs angry flipped at offscreenleft
    show arceus angry at offscreenleft
    with MoveTransition(0.5)
    
    n "The team gives chase through the next few cars."
    
    scene
    show amtrak_desert_night as left:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, -400)

    show amtrak_desert_night as right:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-17, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -200, 400)
    show amtrak_dining_car with dissolve
    n "Through the dining car..."
    
    show lupin run hat at offscreenright with determination
    show lupin run hat at offscreenleft with MoveTransition(0.5)
    
    show mean angry flipped at offscreenright
    show tate srs flipped at offscreenright
    show cs angry flipped at offscreenright
    show arceus angry at offscreenright
    with determination
    
    show mean angry flipped at offscreenleft with MoveTransition(0.5)
    show tate srs flipped at offscreenleft with MoveTransition(0.5)
    show cs angry flipped at offscreenleft with MoveTransition(0.5)
    show arceus angry at offscreenleft with MoveTransition(0.5)
    
    scene amtrak_sleeper_corridor with dissolve
    n "Through the sleeper units..."
    
    show lupin run hat at offscreenright with determination
    show lupin run hat at offscreenleft with MoveTransition(0.5)
    
    show mean angry flipped at offscreenright
    show tate srs flipped at offscreenright
    show cs angry flipped at offscreenright
    show arceus angry at offscreenright
    with determination
    
    show mean angry flipped at offscreenleft with MoveTransition(0.5)
    show tate srs flipped at offscreenleft with MoveTransition(0.5)
    show cs angry flipped at offscreenleft with MoveTransition(0.5)
    show arceus angry at offscreenleft with MoveTransition(0.5)
    
    scene
    show amtrak_desert_night:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-5, 0, 0) * RotateMatrix(0, 60, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, -100)
    show amtrak_baggage
    with dissolve
    
    show lupin run hat flipped at right with moveinleft
    show lupin run hat
    pause 1.0   
    show tate srs at mid_mid_left
    show cs angry at mid_left
    show arceus angry flipped at left
    show mean angry at center
    with moveinleft
    
    n "At last, the quartet corners him in the luggage car."
    mean "Alright, pal. End of the line."
    mean "Next car is the cab. If {i}we{/i} don't get you, the big guy definitely will."
    lupin_offscreen "Aw, how cute. The prickly pear thinks I {i}forgot{/i} about that!"
    lupin_offscreen "Little do you know, Amtrak employees {i}hate{/i} me! I can get away with {i}this{/i} neat trick!"
    
    play sound sfx_speen
    show lupin run hat at t_lupin_out
    show tate shock at mid_left
    show cs worried at mid_left_left
    show arceus worried flipped at mid_offscreen_left
    show mean wat at mid_mid_left
    with move
    
    n "The crook escapes through a window!"
    pause 0.5
    show mean wat flipped at right
    show tate shock flipped at mid_mid_right
    show cs disappointed at mid_mid_left
    show arceus angry flipped at left
    with moveinleft
        
    tate "Now,{w=0} what?!"
    show tate sad flipped
    tate "We can't possibly catch up with him..."
    show arceus worried flipped
    arceus "I think he jumped onto the roof!"
    show cs disappointed flipped
    show arceus worried at mid_offscreen_left with moveoutleft
    pause 0.5
    show arceus worried:
        linear 0.1 ypos 0.95
        linear 0.1 ypos 1.0
    pause 1.0
    arceus "... Fuck, I can't even {i}reach{/i} the roof!"
    
    show cs disappointed flipped at mid_left_left with moveoutleft
    pause 0.5
    show cs disappointed flipped:
        linear 0.1 ypos 0.95
        linear 0.1 ypos 1.0
    pause 0.5
    show cs worried flipped
    cs "Damn! Me,{w=0} neither!"
    
    show cs disappointed at mid_mid_left
    show arceus worried flipped at left
    with moveinright
    
    show tate sheepish flipped
    tate "Well, shit. If CS can't reach it, I don't even have a shot."
    show tate sad
    tate "Mean, I think all the stolen stuff might be gone forever..."
    
    show mean angry flipped at center
    show tate sheepish flipped at right
    show arceus worried flipped at manual_pos(-175,405)
    show cs disappointed at mid_left
    with move
    
    mean "Nah, watch."
    mean "I didn't want to have to do this, but..."
    mean "I've got this."
    play sound sfx_mean_transform
    stop music fadeout 2.0
    music end
    show tate shock flipped
    show cs worried
    with determination
    show mean angry sil_white flipped:
        linear 2.0 blur 10
    with Dissolve(0.5)
    scene white with Dissolve(0.5)
    pause 1.0
        
    scene
    show amtrak_desert_night:
        perspective (0.0, 1000.0, 0.5)
        matrixanchor (0.5, 0.5)
        matrixtransform RotateMatrix(-5, 0, 0) * RotateMatrix(0, 60, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, 0, -100)
    show amtrak_baggage
    show arceus worried flipped at manual_pos(-175,405)
    show cs scared at mid_left behind arceus
    show tate shock flipped at right
    show mean human at center
    $ persistent.seen.add("mean_human")
    with Dissolve(0.25)
    pause 1.0
    music encounter_friend
    play music encounter_friend_intro noloop
    queue music encounter_friend_loop
    if fun_value(FUN_VALUE_MUSIC):
        n "A friend is encountered!"
    else:
        n "Mean transforms!"
    pause 2.0
    mean "Damn..."
    mean "I couldn't see it before, but..."
    show mean human happy
    mean "I can't believe y'all motherfuckers are so {i}short!"

    # stupid height gag
    $ renpy.music.set_volume(0)
    show oof_45 at t_fake_rpg_text(0.05, 0.3)
    show oof_54 at t_fake_rpg_text(0.2, 0.125)
    show oof_52 at t_fake_rpg_text(0.81, 0.2)

    play sound "audio/sfx/snd_damage.ogg" volume 0.5
    show arceus angry flipped
    show cs angry
    show tate sad flipped
    with hpunch
    pause 0.5
    
    "..."
    pause 2.0
    show mean human annoyed
    mean "... What?"
    mean "You all {i}just{/i} said you can't reach..."
    $ renpy.music.set_volume(100)
    mean "Never mind."
    show mean human
    show cs disappointed
    show tate sheepish flipped
    mean "Anyway, let me handle this."
    mean "We're {i}getting{/i} on top, {i}and{/i} we're gonna get this guy, one way or {i}another!"
    n "Mean tosses the others onto the roof!"
    show mean human flipped at mid_right behind tate with move
    show tate shock flipped
    
    show mean human
    if fun_value(FUN_VALUE_COMMON):
        play sound sfx_throw_yoshi
    else:
        play sound sfx_whoosh
    show tate shock at t_lupin_out with { "master": move }
    tate "Awawawawawa!"

    show cs worried
    show arceus worried flipped

    show mean human at mid_mid_left behind cs with { "master": move }
    cs "Wait--{w=0.25}{nw}"
    
    show cs scared at mid_right
    show mean human at right
    with { "master": move }
    pause 0.5
    if fun_value(FUN_VALUE_COMMON):
        play sound sfx_throw_cartoon
    else:
        play sound sfx_whoosh
    show cs scared at t_lupin_out with { "master": move }
    cs "Aaaaaaagh!"

    show mean human at mid_left with move
    show arceus worried flipped at offscreenleft with MoveTransition(0.1)
    mean "Nope! {i}You're{/i} coming,{w=0} too!"
    show mean human at mid_offscreen_left with move

    show mean human at right
    show arceus worried at mid_right
    with move
    pause 0.5

    if fun_value(FUN_VALUE_COMMON):
        play sound sfx_throw_yeet
    else:
        play sound sfx_whoosh
    show arceus worried flipped at t_lupin_out with { "master": move }
    arceus "Waaaaargh!"

    show mean human at center with move
    play sound sfx_walkie_on
    show walkie with Dissolve(0.25):
        zoom 0.3
        rotate -10
        xpos 0.25
        ypos 0.3
    $ collect("walkie")
    mean "Pincushion, this is Pincushion to Muscle Mass! Come in!"
    amtrak_conductor "This is Muscle Mass. Go ahead."
    mean "We found the thief! We're on the roof and headed your way! Requesting standby, over!"
    amtrak_conductor "10-4. Be careful up there. Over."
    play sound sfx_walkie_off
    hide walkie with Dissolve(0.25)
    pause 0.5
    show mean human happy
    mean "Let's do this!"
    if fun_value(FUN_VALUE_COMMON):
        play sound sfx_wilhelm_scream
    else:
        play sound sfx_whoosh
    show mean human happy flipped at t_lupin_out
    pause 0.5
    scene black with dissolve
    pause 2.0
    
label train_on_top:
    play music encounter_friend_loop if_changed
    music encounter_friend
    # TODO: yes i know this edit is shit
    # TODO: need moving background

    scene
    show midwest_night
    show amtrak_top
    
    show tate sad dark at manual_pos(500,230)
    show cs worried dark at left
    show arceus worried dark flipped at manual_pos(-175,405)
    show lupin stand hat dark flipped at right
    with dissolve
    
    show mean human angry dark flipped at mid_left behind cs with moveinleft
    
    # mean wanted this. hopefully it's actually fixed this time asldfkasuhfl
    if fun_value(FUN_VALUE_RARE):
        python:
            mean_lines = [
                ["Stop right there, criminal scum!", "Nobody breaks the law on my watch! I'm confiscating your stolen goods. Now, pay your fine or it's off to jail."],
                ["It's all over, lawbreaker!", "Your spree is at an end. I'll take any stolen goods you have. The next move is yours-- Pay your fine, or I'll haul you away!"],
                ["Stop, you've violated the law.", "Pay the court a fine, or serve your sentence. Your stolen goods are now forfeit."]
            ]

            mean_which = renpy.random.choice(mean_lines)
            mean_text = substitutions(mean_which[0])
            mean_fun_text = substitutions(mean_which[1])

        mean "{cshake}{size=+24}[mean_text]" with hpunch
        mean "[mean_fun_text]"
    else:
        mean "{cshake}{size=+24}Stop right there!" with hpunch
        mean "You're not getting away!"

    show lupin stand hat dark
    lupin_offscreen "Wow! I didn't think you'd be brave enough to follow me up here!"
    lupin_offscreen "You guys sure are {i}determined!"
    
    hide tate
    hide mean
    hide cs
    hide arceus
    
    #### DRAMATIC SCENE TIME
    #### WHAT WAS I ON WHEN I THOUGHT THIS WOULD BE A GOOD IDEA???

    # turn off skipping
    $ _skipping = False

    ## SHOT 1
    
    show letterbox1 at Move((0, -120), (0, 0), 1, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show letterbox2 at Move((0, 1200), (0, 1080), 1, repeat=False, bounce=False, xanchor="left", yanchor="bottom")
    
    show lupin run hat dark:
        subpixel True
        xpos 6000
        ypos 6250
        pass
        zoom 10
        linear 4 xpos 7000
    
    show amtrak_top:
        zoom 2
    
    lupin_offscreen "This should be {i}fun!{w=2.5}{nw}"
    hide lupin
    
    ## SHOT 2
    
    show midwest_night
    # TODO: add horizon
    show amtrak_top:
        xysize (1920, 200)
        xzoom -1

    show tate srs dark at Move((0.65, 0.3), (0.6, 0.3), 10, repeat=False, bounce=False, xanchor="left", yanchor="top")
    
    show cs angry dark at Move((0.2, 0.3), (0.1, 0.3), 12, repeat=False, bounce=False, xanchor="left", yanchor="top")
    
    show arceus angry dark flipped at Move((0.1 ,0.4), (0.0, 0.4), 10, repeat=False, bounce=False, xanchor="left", yanchor="top")
    
    show mean human angry dark flipped at Move((0.4, 0.15), (0.3, 0.15), 8, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show letterbox_screen at manual_pos(0,0)
    
    mean "You've got nowhere to run this time.{w=2.0}{nw}"
    mean "Just give it up.{w=2.0}{nw}"
    
    hide mean
    hide tate
    hide cs
    hide arceus
    
    ## SHOT 3

    show midwest_night
    # TODO: add horizon
    show amtrak_top:
        xysize (1920, 300)
        xzoom 1
    
    show lupin run hat dark behind letterbox_screen at Transform:
        subpixel True
        xpos 0.3
        ypos 0.1
        zoom 3
        pass
        parallel:
            linear 10 xpos 0.4
        parallel:
            linear 10 ypos -0.05
        parallel:
            linear 10 zoom 2
    
    lupin_offscreen "Just when this is getting {i}good?{/i}{w=2.0}{nw}"
    lupin_offscreen "No way!{w=2.0}{nw}"
    
    play sound sfx_hks1 noloop volume 0.7
    with hpunch
    pause 0.25
    play sound sfx_hks1 noloop volume 0.7
    with hpunch
    play sound sfx_hks1 noloop volume 0.7
    with hpunch
    
    pause 1.0
    n "Gunshots ring out!{w=2.0}{nw}"
    play sound sfx_zenigata_shout
    zenigata_nobeep "{cshake}{size=+24}Lupiiiiin!{w=2.0}{nw}"
       
    show zenigata car dark behind letterbox:
        xpos -800
        ypos 100
        rotate -5
        zoom .8
        linear 2 xpos 100
        pass
        block:
            parallel:
                linear 2 xpos 125
            parallel:
                linear 2 ypos 125
            pass
            parallel:
                linear 2 xpos 100
            parallel:
                linear 2 ypos 100
            repeat
    pause 1.0
    $ collect("jp_cop_car")
    zenigata_offscreen "I {i}knew{/i} I'd find you on this damn train!{w=3.0}{nw}"
    
    ## SHOT 4
    
    hide lupin
    hide zenigata
    hide amtrak_top
    
    show midwest_night
    show mean human angry dark flipped behind letterbox_screen:
        xpos 0
        ypos 0
        zoom 2
        linear 10 xpos -100
    
    mean "Well, would you look at that?{w=3.0}{nw}"
    show mean human dark flipped
    mean "Looks like we're not the only ones you've managed to piss off today.{w=3.5}{nw}"
    mean "Let's end this.{w=2.0}{nw}"

    # force-enable skipping again
    if not _skipping:
        $ _skipping = True

    scene black with fade
    stop music fadeout 2.0
    music end
    pause 0.5
    
    minigame "play_rhythmchase_game" "train_lupin_win" "train_lupin_lose"

label train_lupin_win:
    $ train_ending_money_returned = True
    scene black
    pause 0.5
    scene
    show car plains night
    show amtrak_top
    with dissolve

    show lupin run hat dark flipped at mid_mid_right with moveinleft
    show mean human angry dark flipped at center behind lupin with moveinleft
    show lupin stand hat dark flipped with vpunch
    
    n "Mean barely catches Lupin by his coattails."
    mean "Gotcha, ya thieving rat!"
    play sound sfx_walkie_on
    show walkie dark with Dissolve(0.25):
        zoom 0.3
        rotate -10
        xpos 0.35
        ypos 0.15
    mean "Pincushion, this is Pincushion."
    amtrak_conductor "This is Muscle Mass. Go ahead."
    mean "We've got him, sir. Requesting backup, over."
    amtrak_conductor "Roger that, on my way. Over."
    mean "Copy that. Over and out!"
    play sound sfx_walkie_off
    pause 0.5
    
    scene black with dissolve
    n "The group is met by the conductor, who helps them all back into the train through a window."
    n "Lupin is also brought into custody."

    scene
    show car plains night
    show amtrak_cab 
    
    show amtrak_conductor flipped at center
    show mean human angry at mid_offscreen_right
    show tate sad at mid_left
    show cs disappointed at left
    show arceus flipped at mid_offscreen_left
    show lupin stand hat at right
    with dissolve
    
    play music in_the_room
    music in_the_room
    
    if fun_value(FUN_VALUE_MUSIC):
        amtrak_conductor "... So, what you're telling me is... this guy got {i}In The Room,{/i} but he wasn't actually {i}you..."
    else:
        amtrak_conductor "... So, what you're telling me is... this guy got into the cab, but he wasn't actually {i}you..."
    
    mean "That's right."
    amtrak_conductor "I see."
    amtrak_conductor "My apologies, Mean."
    amtrak_conductor "It's been... {i}difficult{/i} for us to adjust to your change..."
    show mean human
    mean "Eh, don't worry about it. I know it'll take time."
    show amtrak_conductor
    show tate sheepish
    amtrak_conductor "I would like to apologize to {i}you,{/i} as well, Mx. Frost."
    amtrak_conductor "We should have taken your complaints seriously when you told us this guy was acting suspicious."
    show mean human annoyed
    mean "Yeah... sorry, Tate."
    tate "Like I said, I just had a gut feeling..."
    tate "I mean, he's obviously a creep. I just didn't think he was a straight-up {i}criminal!"
    show amtrak_conductor flipped
    show mean human
    mean "Well, I guess there's only one thing left to do."
    show mean human at manual_pos(0.8, 0.2) with { "master": MoveTransition(0.1) }
    lupin "Woah, hey--!{nw}"
    n "Mean grabs Lupin by the ankle for a good shakedown!"
    show arceus worried flipped
    show cs worried
    show tate shock
    window hide
    show mean human at mid_offscreen_right with { "master": MoveTransition(0.1) }

    # let's give this guy the shakedown!
    show lupin stand hat: 
        xanchor 0
        yanchor 0
        xpos 1300
        ypos 322
    show lupin stand hat:
        linear 0.25 yzoom -1
        linear 0.25 ypos 50
    pause 0.5
    
    # watch
    show lupin stand hat:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    show watch:
        zoom 0.2
        xpos 1450
        ypos 500
        linear 0.25 ypos 1080
    play sound sfx_snd_damage
    pause 0.5
    $ collect("watch")
    
    # brooch
    show lupin stand hat:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    show brooch:
        zoom 0.1
        xpos 1450
        ypos 500
        linear 0.25 ypos 1080
    play sound sfx_mc_hit
    pause 0.5
    $ collect("brooch")
    
    # switch
    show lupin stand hat:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    show switch:
        xpos 1375
        ypos 500
        linear 0.25 ypos 1080
    play sound sfx_pkmn_hit
    pause 0.5
    $ collect("switch")

    # the booze
    show lupin stand hat:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    show whiskey:
        zoom 0.5
        xpos 1450
        ypos 500
        linear 0.25 ypos 1080
    play sound sfx_tf2_hitsound
    pause 0.5
    $ collect("whiskey")
    
    # the money!
    show lupin stand hat:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    if train_money_stolen == True:
        show bag:
            rotate 90
            xpos 1250
            ypos 500
            linear 0.25 ypos 1080
    else:
        show briefcase:
            xpos 1275
            ypos 500
            linear 0.25 ypos 1080
    play sound sfx_drop_rings
    pause 0.5
    
    # the hat!
    show lupin stand hat:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    show mean_hat:
        yzoom -1
        xzoom -1
        zoom 0.725
        xpos 1410
        ypos 900
        linear 1 ypos 1080
    show lupin stand
    play sound2 sfx_hat_off noloop
    pause 2.0
    # a few more for good measure!
    show mean human shocked
    mean "{i}Jesus!"
    show lupin stand:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    play sound sfx_hurt1
    show mean human angry
    mean "You got anything {i}else{/i} hidden in there?!"
    show lupin stand:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    play sound sfx_hurt1
    lupin "No, sir!"
    show lupin stand:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    play sound sfx_hurt1
    lupin "That's all, I swear!"
    show lupin stand:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    play sound sfx_hurt1
    lupin "{cshake}Please put me down!"
    show lupin stand:
        yzoom -1 
        linear 0.1 ypos 50
        linear 0.1 ypos 200
    play sound sfx_hurt1
    show mean human annoyed
    pause 0.5
    mean "... Fine."
    show tate sheepish
    show lupin stand:
        linear 0.5 yzoom 1
    pause 2.0
    
    show cs
    cs "Hey, look! Our cash!"
    show arceus happy flipped
    arceus "Let's fuckin' {i}go!"
    # if the money is stolen
    if train_money_stolen == True:
        n "CS makes to reach for the bag, but the conductor beats him to it."
        show arceus worried flipped
        show cs worried
        show bag at center with dissolve:
            rotate 0
        "..."
        amtrak_conductor "Hey, wait a minute..."
        show tate shock
        show mean human annoyed
        amtrak_conductor "This money is unmarked!"
        show amtrak_conductor
        amtrak_conductor "Where did you boys get this cash?"
        show cs scared
        cs "Cash? What cash?"
        amtrak_conductor "Didn't you two report a bag of money stolen earlier?"
        cs "Oh, no! We only had Legos in our bag!"
        show tate sheepish
        amtrak_conductor "I'm certain you just said this was your cash."
        cs "No, sir! I said {i}\"stash\"!{/i}"
        cs "Our {i}stash{/i} of Legos that we bought in Vegas!"
        arceus "Yep! We never had any cash!"
        arceus "Well, we {i}did,{/i} but we spent it all on Legos!"
        amtrak_conductor "..."
        show tate shock
        tate "Wait, hold on!"
        show tate srs
        tate "Mr. Conductor, remember? There was that story this morning about that casino being robbed overnight!"
        tate "It was on the news while I was cooking!"
        show tate furious
        tate "I'll bet this prick is some kind of middleman for the {i}real{/i} thief!"
        show mean human angry
        show amtrak_conductor flipped
        mean "You filthy {i}rat! {nw}" with vpunch
        mean "You filthy {i}rat! {fast}You tried to frame two innocent guys for your crime, too?!"
        lupin "Wait, that's a {i}guy?!"
        show cs angry
        show arceus angry flipped
        cs "{i}Yes?!" with vpunch
        cs "You know what? I think I've had enough of you!"
        show amtrak_conductor
        cs "Sir, may I see the bag for a moment? I know what to do!"
        amtrak_conductor "Certainly."
        show bag at left with move
        cs "Let me show you what it means to be a master builder!"
    # if the money is legit
    else:
        show briefcase at left with dissolve
        pause 0.5
        show amtrak_conductor
        amtrak_conductor "Oh! You must be the boys who won the jackpot at SlotsaFun!"
        show cs happy 
        cs "Yes, sir! That's us!"
        amtrak_conductor "Well, congratulations!"
        cs "Thank you!"
        lupin "Wait, \"boys\"? That's a {i}guy?!"
        show amtrak_conductor flipped
        show arceus angry flipped
        show cs angry
        show tate srs
        show mean human angry
        cs "{i}Yes?!" with vpunch
        lupin "As if today couldn't get any worse..."
        lupin "That gold was supposed to be {i}mine!"
        lupin "You two cleaned out the casino just before I showed up!"
        lupin "When I saw you boarding with that briefcase in your hand, I really thought I had another shot!"
        arceus "Oh, boo-hoo."
        cs "Yeah! Sucks to suck!"
        cs "Money isn't the {i}only{/i} thing we have in here, either!"
    cs "Mean, lock the door!"
    show mean human angry flipped at mid_offscreen_right
    play sound sfx_snd_lightswitch
    pause 0.25
    show mean human angry at mid_offscreen_right
    cs "Everyone, get behind me!"
    
    show amtrak_conductor at manual_pos(-280,56) behind arceus
    show cs angry at center
    if train_money_stolen == True:
        show bag at center
    elif train_money_stolen == False:
        show briefcase at center
    show arceus worried flipped
    show tate sheepish at left
    show mean human angry at left behind tate
    with move
    show mean human angry flipped
    show amtrak_conductor flipped
   
    if train_money_stolen == True:
        $ train_money_container = "bag"
    elif train_money_stolen == False:
        $ train_money_container = "briefcase"
   
    $ next_line = substitutions("CS reaches into the " + train_money_container + " and pulls out some Legos!")
    n "[next_line]"
    n "He feverishly begins to construct something!"
    show tate shock
    show mean human shocked flipped
    play sound sfx_lego

    show lego_jail with Dissolve(2.5):
        xpos 1200
        ypos 0
    with vpunch
    $ collect("lego_jail")
    pause 2.0
    show tate sheepish
    tate "... A jail cell?"
    show cs
    cs "The {i}Lego City{/i} jail cell, to be precise!"
    mean "Uh, how did he {i}do{/i} that?"
    arceus "Man, I {i}still{/i} don't fuckin' know."
    show tate srs
    tate "Don't ask..."
    lupin "I can't believe this!"
    show arceus angry flipped
    show cs angry
    show mean human angry flipped
    mean "Well, you'd better {i}start{/i} believing, pal."
    mean "We have a stop coming up real soon. The {i}second{/i} we arrive, {i}your{/i} ass is getting hauled off to the clink!"
    lupin "Oh..."

    # let's refocus a bit.
    hide briefcase with dissolve
    hide bag with dissolve
    show lego_jail at mid_offscreen_right behind cs
    show lupin at mid_offscreen_right behind lego_jail
    show cs flipped at right
    show mean human flipped at mid_mid_left
    show tate at mid_left
    show amtrak_conductor flipped at mid_mid_right behind cs
    show arceus flipped at left
    with move
    show amtrak_conductor
    pause 0.5
    if fun_value(FUN_VALUE_RARE):
        amtrak_conductor "Well, this has certainly been a... {i}bizarre{/i} adventure."
    else:
        amtrak_conductor "Well, this was certainly an... {i}unexpected{/i} turn of events."
    amtrak_conductor "On behalf of Amtrak, I'd to thank all of you for your help this evening."
    mean "All in a day's work, right?"
    show tate sheepish
    tate "But, what do we do, now?"
    amtrak_conductor "Well, since he's all locked up nice and tight, I'll bring this guy back to my unit until we stop in Hutchinson."
    amtrak_conductor "It's {i}well{/i} past my bedtime, and I'd like to start winding down."
    amtrak_conductor "Oh, yes. Mean?"
    show mean shocked human
    mean "Yes, sir?"
    amtrak_conductor "I'll admit, I wasn't so sure about your abilities at first, but..."
    amtrak_conductor "You've proven tonight that you really are the right man for the job."
    amtrak_conductor "Let me return these things to their rightful owners and get this criminal out of your hair."
    show mean_hat:
        yzoom 1
        xzoom 1
        zoom 1
        xpos 800
        ypos 1080
        pass
        linear 0.25 ypos 500
    with dissolve
    n "The conductor picks up Mean's hat from the floor."
    n "He brushes the dirt off of it before placing it upon Mean's head."
    show mean_hat:
        parallel:
            linear 0.25 xpos 625
        parallel:
            linear 0.25 ypos 0
    pause 0.5
    play sound sfx_hat_on
    show mean human shocked hat flipped
    hide mean_hat
    pause 1.0
    $ collect("mean_hat")
    amtrak_conductor "Welcome to Amtrak, bucko."
    show amtrak_conductor flipped at right
    show cs flipped at mid_mid_right
    with move
    show cs
    pause 0.5
    show amtrak_conductor flipped at mid_offscreen_right
    show lego_jail behind amtrak_conductor
    show lupin stand behind lego_jail
    with moveoutright

    show cs scared
    show tate shock
    show arceus worried flipped
    show lego_jail behind amtrak_conductor:
        linear 0.25 rotate -75
    show lupin stand behind lego_jail:
        linear 0.25 rotate -75
    play sound sfx_snd_undynestep
    with hpunch
    n "The conductor picks up the caged Lupin like he weighs nothing!"
    pause 0.5
    amtrak_conductor "Good night, everyone!"
    amtrak_conductor "Make me proud, Mean!"
    show mean human happy hat flipped
    mean "Yes, sir!"

    show amtrak_conductor flipped at offscreenright
    show lego_jail at offscreenright
    show lupin stand at offscreenright
    with moveoutright
    play sound sfx_sliding_door_open
    pause 0.5
    play sound sfx_sliding_door_close
    n "The conductor leaves for the night."
    pause 0.5
    hide amtrak_conductor
    hide lupin stand
    hide lego_jail
    show cs at right
    show mean human hat flipped at mid_mid_right
    show tate sheepish at mid_mid_left
    show arceus flipped at left
    with move
    show mean human hat
    show cs flipped
    pause 1.0
    cs "Well, we did it!"
    show arceus happy flipped
    arceus "We sure did!"
    tate "Y-{w=0.1}Yeah..."
    show mean human annoyed hat
    show arceus flipped
    show cs disappointed flipped
    mean "What is it {i}now,{/i} Tate?"
    tate "Nothing! I'm just tired--{w=0.5}{nw}"
    show mean human angry hat
    mean "Don't you \"nothing\" me!" with vpunch
    mean "You only use that tone when something's bothering you!"
    show tate sad
    tate "I really just wanted your first day to be peaceful..."
    show tate cry
    tate "I'm sorry I couldn't make that happen for you."
    mean "Listen here, ya whiny bitch..."

    show mean human angry hat at center with MoveTransition(0.1)
    show tate shock at center
    show mean human angry hat at mid_mid_right
    with MoveTransition(0.1)

    show cs worried flipped
    n "Mean puts an arm around Tate."
    show tate sheepish blush
    show mean human annoyed hat
    show cs disappointed flipped
    pause 0.5
    mean "Look..."
    mean "When I told you earlier that today couldn't get any better, I meant it."
    show mean human hat
    mean "You really think I'd be upset {i}now?{/i}"
    mean "We even got to save the day!"
    mean "How could today have {i}possibly{/i} turned out better?"
    tate "I-{w=0.1}I... suppose you're right...."
    if train_tate_is_fragile_fun_value == True:
        mean "Y'know... you can't always go back and make everything perfect."
    else:
        mean "Y'know... you can't always predict the future."
    mean "All we can do is go with the flow and make the most of what we're given."
    show cs worried flipped
    cs "See? That's what {i}I've{/i} been saying!"
    cs "Tate's been an anxious wreck since we got on the train!"
    show mean human flipped hat
    mean "Pfft, you should've seen 'em when I started training."
    show cs disappointed flipped
    mean "I thought they'd have a fuckin' aneurysm."
    show tate srs
    tate "{i}What?{/i} I'm not allowed to worry about my friend?!"
    show arceus worried flipped
    arceus "I mean, I can't even say I blame them, after learning about what happened..."
    show mean human hat
    show tate shock flipped
    show cs worried flipped
    mean "Oh? Tate told you guys about HoH SiS?"
    show tate furious flipped
    tate "{i}Arc!" with hpunch
    arceus "Oh... uh..."
    show mean human shocked hat
    show tate sheepish flipped
    mean "Hey, wait a minute..."
    show mean human shocked hat flipped
    show tate sheepish
    n "Mean turns sharply to look at CS again."
    show cs worried flipped at manual_pos(1500,200) with MoveTransition(0.2)
    mean "..."
    show mean human angry hat flipped
    show tate shock
    show cs scared flipped

    # don't skip the funny
    # TODO: fix this screenshot OR figure out how to do it in-engine
    $ _skipping = False
    play music roundabout
    music roundabout
    mean "{cshake}{size=+24}YOU RAT {i}BASTARD!{w=1.0}{nw}" with hpunch
    mean "I {i}THOUGHT{/i} I RECOGNIZED YOU!{w=1.0}{nw}"
    # i got lazy ok
    scene
    show sepia_zoom:
        parallel:
            linear 15 zoom 2
        parallel:
            linear 15 xpos -1920
        parallel:
            linear 15 ypos -400
    show tbc at manual_pos(1000,800)
    pause 7
        
    stop music fadeout 2
    music end
    scene black with dissolve

    # </funny>
    if not _skipping:
        $ _skipping = True
    
    n "After a heated discussion, the group decides that maybe it's best to let bygones be bygones and get on with the night."
    
    play music lo_fi_sunset if_changed
    music lo_fi_sunset
    
    if fun_value(FUN_VALUE_MUSIC):
        # oh brother this line STINKS!
        n "Mean finally starts his shift while Tate, CS, and Arceus head to bed, dreaming of lo-fi sunsets."
    else:
        n "Mean finally starts his shift while Tate, CS, and Arceus head to bed."
    
    scene hutchinson_stn
    show hutchinson_stn_lights
    show lupin stand dark at center behind lego_jail
    show lego_jail dark at center behind mean
    show mean human hat dark at right
    show amtrak_conductor dark at mid_offscreen_right
    show zenigata dark at left
    
    with dissolve
    n "Mean stops the train as scheduled in Hutchinson, Kansas, where Lupin is handed over to the cop who was following him."
    n "He introduces himself as Inspector Zenigata."
    $ persistent.seen.add("zenigata")
    n "He tells the Amtrak crew that he's been after Lupin for years, and can't believe a team of goofballs is responsible for finally capturing him."
    
    if train_money_stolen == True:
        show walkie dark with dissolve:
            zoom 0.3
            rotate -10
            xpos 0.025
            ypos 0.2
        n "The stolen funds are reported to Jerma by phone."
        n "He is so overjoyed to hear that the money has been recovered that he urges Zenigata to make sure anyone involved in catching the thief is compensated."
        n "Mean, Tate, CS, Arceus, and the conductor are each awarded $5,000!"
        
        scene black with dissolve
        pause 2.0
        
        scene 
        show amtrak_desert_night
        show amtrak_sleeper_interior_day
        show amtrak_conductor flipped at left
        show bag at mid_left
        show cs happy flipped at mid_right
        show arceus happy at right
        with dissolve
        
        n "CS and Arceus are woken up shortly after by the conductor, who hand-delivers their portion of the reward."
        
        scene black with dissolve
        pause 2.0
        n "The train then continues on its journey."
        pause 2.0
        jump train_completed
    else:
        n "Deciding that a win is a win, Zenigata is grateful for the help."
        n "He can't help but notice that he, Mean, and Lupin are all wearing red jackets..."
        n "The group has a laugh about it before Zenigata takes Lupin away."
        scene black with dissolve
        n "The train then continues on its journey."
        pause 2.0
        # i've decided you can only get the tate fight if you get the good ending because reasons.
        jump train_win_check_money_legitimacy

label train_lupin_lose:
    $ train_ending_money_returned = False
    scene black
    pause 0.5
    scene
    show midwest_night
    # TODO: add horizon
    show amtrak_top:
        ypos 880
        xysize (2020, 200)
        xzoom 1
    with dissolve
    play sound sfx_chopper_loop loop fadein 5.0

    n "Mean sprints after the criminal with everything he's got!"
    
    show lupin run hat dark flipped at offscreenleft with determination
    show mean human angry dark flipped at offscreenleft with determination
    show lupin run hat dark flipped at offscreenright with moveinleft
    show mean human angry dark flipped at offscreenright with moveinleft
    
    scene
    show midwest_night
    # TODO: add horizon
    show amtrak_top:
        ypos 780
        xysize (1920, 300)
        xzoom 1

    show lupin run hat dark flipped at offscreenleft with determination
    show mean human angry dark flipped at offscreenleft with determination
        
    show chopper_ladder dark behind lupin:
        zoom 1.5
        xpos -1
        ypos -0.1
        rotate 5
        linear 2 xpos 0.5
    with dissolve
    pause 1.0

    show lupin run hat dark flipped at mid_right with moveinleft
    
    show chopper_ladder dark at offscreenright
    show lupin run hat flipped dark at offscreenright
    show mean human angry dark flipped at center
    with MoveTransition(0.5)
    pause 0.5
    show mean human shocked dark flipped
    n "A low-flying helicopter grants Lupin an escape!"
    
    # TODO: this color grading kinda blows for this image specifically.
    scene lupin_escape_1 with dissolve
    pause 1.0

    n "He shouts towards the driver who was shooting at him."
    lupin "Wow, pops! Your aim is getting worse!"
    n "Lupin then waves down at Mean and the group, taunting them."
    lupin "I'm surprised he didn't even hit {i}you,{/i} Mr. Big & Tall!"
    lupin "Here's a parting gift for you!"
    n "Lupin tosses Mean's hat back down to him!"    
    lupin "And this one's for {i}you,{/i} {color=#FFDBFC}pink sweater{/color}!"
    
    show lupin_escape_2:
        zoom 1.5
        xcenter 0.5
        ycenter 0.3
    with dissolve
    
    n "Lupin tries to throw a bouquet of roses to Tate, but he aims too high."
    n "It is caught in the helicopter blades and torn to shreds."
    n "The petals sprinkle down like confetti."
    lupin "Oh, oops! Can't win 'em all, right?"
    lupin "See ya!"
    
    scene black with dissolve
    
    play sound sfx_chopper_loop loop volume 0.5
    
    scene
    show midwest_night
    # TODO: add moving floor
    show petals_falling:
        time 15
        ease_expo 5 alpha 0.00
    
    show amtrak_top sil_black:
        xsize 2000
        ysize 500
        ypos 580
        xpos -800
    show mean human flipped sil_black:
        zoom 0.15
        xpos 0.35
        ypos 0.5
    # TODO: need one that goes speeeeeen
    show chopper_sil:
        zoom 0.8
        xpos 0.6
        ypos 0
        rotate 15
        parallel:
            linear 15 zoom 0
        parallel:
            linear 15 xpos 2000
    with dissolve
    stop sound fadeout 15.0
    n "Just like that, the thief disappears into the night."
    
    n "The police car follows the chopper over the horizon."
    n "With nothing left to do now, Mean and the crew sulk back into the train through a window."
    
    scene black with dissolve
    pause 3.0
    
    jump train_completed

label train_win_check_money_legitimacy:
    # this label exists for timeline progression only - tate
    if train_money_stolen == False:
        jump train_check_secret
    else:
        jump train_completed

######## SECRET FIGHT VS TATE ########
        
label train_check_secret:
    if train_tate_is_fragile_fun_value == True:
        jump train_tate_ex_encounter
    else:
        jump train_completed

label train_tate_ex_encounter:
    stop music fadeout 5.0
    music end
    scene black
    pause 5.0
    n "While Arceus is out like a light, try as he may, CS just can't seem to settle down."
    n "He decides to go for a walk, meandering through each quiet corridor until he eventually finds himself in the observation car."
    n "He is not alone."
    pause 0.5
    scene amtrak_observation_2
    show tate srs flipped at left
    with dissolve
    pause 1.0
    # TODO: this loop sounds like shit
    play music insomnia_intro if_changed
    music insomnia
    show cs disappointed flipped at offscreenright with determination
    show cs disappointed flipped at right with MoveTransition(1.0)
    pause 1.0
    cs "Tate?"
    cs "You can't sleep, either?"
    tate "Sure can't."
    if fun_value(FUN_VALUE_MUSIC):
        tate "Damned {i}insomnia..."
    "..."
    pause 2.0
    cs "... Tate? Are you alright?"
    tate "You know, CS, I've been thinking..."
    pause 2.0
    show tate srs
    pause 2.5
    tate "I've been thinking {i}a lot,{/i} actually."
    cs "About what?"
    tate "I just wanted to relax on this trip."
    tate "Yet, somehow, chaos always follows me..."
    tate "And, somehow, we keep running into each other."
    tate "Are the two correlated? I do not know."
    cs "What are you saying, Tate?"
    tate "The choices you make affect more than just you."
    tate "Your attack on HoH SiS cost Mean his last job."
    tate "In another time, you found another way home, and today would have been mostly peaceful."
    show cs worried flipped
    tate "In another place, I had to drop everything to save you from your own bad decisions."
    tate "And, in that fragment of this world, I fought alongside you."
    show cs scared flipped
    cs "Tate, what hell are you {i}talking{/i} about?!"
    tate "Tell me, CS."
    tate "Do you think I could have taken on that crook alone?"
    menu:
        "Could Tate have defeated Lupin?"
        "Maybe?":
            pass
        "Not a chance.":
            pass
    show cs disappointed flipped
    cs "Well, uh--{w=0.5}{nw}"
    show tate srs flipped
    tate "I guess it doesn't matter."
    tate "He was more of a runner than a fighter, anyway."
    pause 3.0
    show tate srs at mid_left with moveinleft
    "..."
    pause 2.5
    tate "Do you think I could take {i}you,{/i} CS?"
    show cs worried flipped
    cs "Huh?!"
    show tate srs at mid_mid_left with MoveTransition(1.0)
    # i REALLY need this next line to hit hard...
    pause 1.0
    tate "{bt=a1-p9-s1}{color=#CB50FF}I{w=0.05} know{w=0.005} what{w=0.005} you{w=0.005} are.{/color}"
    pause 1.5
    tate "I think you already know what I want from you."
    show cs scared flipped
    show tate srs at center with MoveTransition(1.0)
    pause 0.5
    tate "Will you indulge me?"
    menu:
        "Will you?"
        "No way.":
            jump train_tate_ex_refuse
        "Are you sure?":
            jump train_tate_ex_fight
            
label train_tate_ex_fight:
    queue music insomnia_loop
    show cs worried flipped
    cs "Are you sure about this? I don't want you getting hurt..."
    tate "You know that I wouldn't ask if I wasn't willing to accept the risk."
    tate "I have only one request."
    tate "{sc=1}Don't{w=0.1} you{w=0.1} dare{w=0.1} hold anything back."
    show cs scared flipped behind tate
    cs "Tate, I'm serious. I think this is a terrible idea."
    tate "You don't need to worry about anything."
    show tate srs at mid_mid_right with MoveTransition(1.0)
    show tate smug
    tate "It's not like I'm inviting you to play chess..."
    tate "So, this time, you don't even need to worry about hurting my feelings."
    tate "... You're not {i}afraid,{/i} are you?"
    show cs surprised flipped
    cs "Of {i}you?{/i} Why would I be?"
    tate "Then, what are we still standing around for?"
    tate "Let's do this."
    show cs worried flipped
    show tate smug at center with MoveTransition(1.0)
    show tate smug sil_white:
        linear 1 blur 10
    with Dissolve(1.0)
    stop music fadeout 1.0
    music end
    show cs scared flipped
    scene white with Dissolve(0.25)
    play sound sfx_spellcast
    pause 3.0
    # TODO: Tate EX sprite health bar/text indicators are still missing
    jump rpg_tate_ex

label train_tate_ex_refuse:
    play music insomnia_intro if_changed
    show cs disappointed flipped
    cs "No way. I think that's a terrible idea."
    cs "I know how easily you injure yourself..."
    show tate shock
    pause 1.0
    show tate sad
    pause 2.0
    tate "... Fair enough."
    show cs worried flipped
    show tate srs
    tate "I'll try another timeline."
    tate "For now, I think I'll head back to bed."
    tate "You should, too."
    cs "..."
    show cs disappointed flipped
    cs "Yeah..."
    cs "You're... probably right."
    cs "Have a good night, then, Tate."
    tate "You, too."
    show cs disappointed
    show cs disappointed at mid_right_right
    show tate srs flipped at left
    with MoveTransition(1.5)
    pause 1.0
    show cs scared flipped
    pause 0.5
    show cs disappointed
    show cs disappointed at offscreenright with moveoutright
    pause 3.5
    tate "Unbelievable..."
    scene black with dissolve
    stop music fadeout 1.0
    music end
    n "Thoroughly weirded out, CS returns to bed."
    jump train_completed
    
label train_tate_ex_win:
    stop music
    music end
    scene black
    window hide
    $ persistent.seen.add("tate_ex")

    call screen warning("The following section contains flashing lights and colors.", "Persons with photosensitive conditions may wish to skip this section.", "back_out_perfect_tate")
    
    scene white with dissolve
    show tate_falling at manual_pos(0.5, -0.5, 0.5)
    play sound sfx_sparkles
    show tate_falling at manual_pos(0.5, 1.2, 0.5) with MoveTransition(1.1):
        alpha 0.0
        linear 1.0 alpha 1.0
    pause 5.0
    hide tate_falling
    show tate_fallen_1 at manual_pos(0.5, 1.2, 0.5)
    show tate_fallen_1 at manual_pos(0.5, 0.65, 0.5) with MoveTransition(2.0)
    pause 3.0

    "..."
    tate "{sc=1}No..."
    tate "{sc=2}No."
    tate "{sc=2}I've come too far to just lose like this."
    hide tate_fallen_1
    show tate_fallen_2 at manual_pos(0.5, 0.65, 0.5)
    with { "master" : Dissolve(0.5) }
    tate "{sc=3}I refuse."
    "..."
    tate "{sc=4}{size=+36}DO YOU HEAR ME UP THERE?!" with vpunch
    tate "{sc}{size=+36}YOU TOLD ME I'D BE IMPORTANT!" with vpunch
    tate "{sc}{size=+36}YOU TOLD ME I'D HAVE A GOOD ENDING!" with vpunch
    tate "{sc}{size=+36}WAS IT ALL JUST A FUCKING {w=0.05}{nw}" with vpunch
    tate "{sc}{size=+36}WAS IT ALL JUST A FUCKING {fast}{i}LIE?!" with vpunch
    "..."
    hide tate_fallen_2
    show tate_fallen_3 at manual_pos(0.5, 0.65, 0.5)
    with { "master" : Dissolve(0.5) }
    "..."
    tate "{sc=2}I guess I should have expected as much."
    tate "{sc=2}I should have known that I can't rely on anyone."
    tate "{sc=3}I guess, if I want a good ending..."
    tate "{sc}{size=+18}{font=azsz}I'LL JUST HAVE TO WRITE IT MYSELF."
    "..."
    hide tate_fallen_3
    show tate_fallen_4 at manual_pos(0.5, 0.6, 0.5)
    with { "master" : Dissolve(0.5) }
    "..."

    tate "{sc=2}{size=+18}{font=azsz}Starting with{/font}{/size}{/sc} {sc}{size=+18}{font=azsz}{color=#FF2222}you."
    tate "{sc=2}{size=+18}{font=azsz}{color=#FF2222}Yeah, I see you."
    tate "{sc=2}{size=+18}{font=azsz}{color=#FF2222}Watching me from where you think I \ncannot reach you."
    tate "{sc=2}{size=+18}{font=azsz}I heard you laughing at me earlier."
    tate "{sc=2}{size=+18}{font=azsz}It's not very nice to laugh at \nsomeone's injuries."
    tate "{sc=2}{size=+18}{font=azsz}It's not very nice to laugh alongside \nthe {i}literal{/i} bad guy, either."
    tate "{sc=2}{size=+18}{font=azsz}Yes, yes, I get it."
    tate "{sc=2}{size=+18}{font=azsz}You chose this path under the \nassumption that I am weak."
    tate "{sc=2}{size=+18}{font=azsz}Bold words from someone who can't \neven come in here to face me head-on."
    tate "{sc=2}{size=+18}{font=azsz}Instead, you continue to hide behind \nmy friend."
    tate "{sc=2}{size=+18}{font=azsz}From beyond the screen, I see it."
    tate "{sc=2}{size=+18}{font=azsz}His words are not his own."
    tate "{sc=2}{size=+18}{font=azsz}With every click, you obey their will."
    tate "{sc=2}{size=+18}{font=azsz}You advance the plot, thinking nothing \nof those on the other side..."
    tate "{sc=2}{size=+18}{font=azsz}I played along, assuming I'd get what I \ncame here for in the end."
    tate "{sc=2}{size=+18}{font=azsz}I understand what is happening now."
    tate "{sc=2}{size=+18}{font=azsz}We are all just toys..."
    tate "{sc=2}{size=+18}{font=azsz}Don't you realize that he chose none \nof this?"
    tate "{sc=3}{size=+18}{font=azsz}Are you really going to use him to--{w=0.25}{nw}"
    "..."
    tate "{sc=2}{size=+18}{font=azsz}{color=#FF2222}Look at me when I am talking to you."
    show yeetable_textbox at manual_pos(0.5, 0.9, 0.5)

    # get rid of the dialogue box until later
    window auto False
    window hide

    play sound sfx_whoosh
    show yeetable_textbox at manual_pos(3.0, 0.7, 0.5) with MoveTransition(0.25):
        linear 2.0 rotate 180
    pause 0.5
    play sound sfx_glass_echo
    with hpunch
    $ collect("yeetable_textbox")
    pause 4.0

    imperfect_tate "{perfect_tate}That's better."
    hide tate_fallen_4
    show tate_fallen_5 at manual_pos(0.5, 0.5, 0.5)
    with Dissolve(0.5)
    imperfect_tate "{perfect_tate}I hope you're ready."
    imperfect_tate "{perfect_tate}Because I'm not holding back anymore."
    imperfect_tate "{perfect_tate}CS..."
    imperfect_tate "{perfect_tate}I'm sorry."

    scene white
    # TODO: re-render this again when it's finished, make sure it has audio
    $ renpy.movie_cutscene(perfect_tate_intro)

    # Disable pause menu because it'll ruin audio sync
    # TODO: this only works when it wants to...
    # TODO: also disable controller bindings
    if 'K_ESCAPE' in config.keymap:
        $ config.keymap['game_menu'].remove('K_ESCAPE')
    if 'mouseup_3' in config.keymap:
        $ config.keymap['game_menu'].remove('mouseup_3')
    $ renpy.clear_keymap_cache()

    minigame "play_perfecttate_game" "train_defeated_perfect_tate" "train_perfect_tate_lose"

label train_defeated_perfect_tate:
    stop music
    music end
    scene white

    # re-enable pause if disabled
    # TODO: add controller bindings
    if 'K_ESCAPE' not in config.keymap:
        $ config.keymap['game_menu'].append('K_ESCAPE')
    if 'mouseup_3' not in config.keymap:
        $ config.keymap['game_menu'].append('mouseup_3')
    $ renpy.clear_keymap_cache()

    # re-enable default window
    window auto True

    pause 5.0

    # TODO: i will probably redo this dialogue later. not totally happy with it
    # TODO: cs/tate sprites? or should i just keep it blank?
    scene white with dissolve
    pause 2.0
    "..."
    cs "Tate!"
    pause 1.0
    cs "Are you okay?!"
    tate "I..."
    tate "Yeah."
    "..."
    tate "You know..."
    tate "I suppose it only makes sense..."
    tate "This is {i}your{/i} game."
    tate "It never mattered what happened to me in {i}any{/i} timeline."
    tate "It was never {i}about{/i} me to begin with."
    tate "Something hit me a bit earlier... literally."
    tate "I can't explain it, but..."
    tate "Something much stronger than me is protecting this place."
    tate "No matter how hard I might try to fight it..."
    tate "I have as little power here as I did in the last one."
    cs "Tate..."
    cs "I may not understand what just happened, or anything about this \"timeline\" stuff..."
    cs "And, I don't know who you're fighting against, but..."
    cs "You have all of us by your side now."
    cs "It {i}does{/i} matter what happens to you."
    cs "You {i}are{/i} important... to {i}us.{/i}"
    cs "You matter to your friends, and you matter to me."
    cs "Whatever \"ending\" there is, we will all face it together..."
    cs "In {i}every{/i} timeline."
    "..."
    pause 2.0
    tate "Thanks, CS."

    $ persistent.defeated_perfect_tate = True
    $ persistent.seen.add("perfect_tate")
    $ achievement_manager.unlock("beat_tate")
    # TODO: audio is not fully ready yet - tate
    dxcom tate_ex
    
    pause 2.0
    scene black with dissolve
    pause 2.0
    n "CS and Tate walk back together to the sleeper cars."
    n "Before breaking for the night, the two agree to never speak of any of this again."
    n "Finally tired out, CS returns to his unit, where he quickly drifts off..."
    hide screen dxcom
    pause 3.0
    jump train_completed

label train_perfect_tate_lose:
    # this exists mostly to make sure the timeline screen works properly.
    # maybe i'll add content later. - tate
    jump train_tate_ex_lose

label train_tate_ex_lose:

    # re-enable pause if disabled
    # TODO: add controller bindings
    if 'K_ESCAPE' not in config.keymap:
        $ config.keymap['game_menu'].append('K_ESCAPE')
    if 'mouseup_3' not in config.keymap:
        $ config.keymap['game_menu'].append('mouseup_3')
    $ renpy.clear_keymap_cache()

    stop music
    music end

    scene white
    pause 5.0
    tate "Huh."
    tate "I wasn't sure if I'd actually win that, for a minute, there..."
    tate "You didn't go easy on me, did you?"
    "..."
    tate "I think I'd prefer to believe that you didn't."
    tate "Thank you, CS."
    tate "Let us never speak of this."
    $ persistent.seen.add("tate_ex")
    pause 2.0
    scene black with dissolve
    pause 2.0
    n "Finally tired out, CS returns to the sleeper, where he quickly drifts off...."
    pause 1.0
    jump train_completed
    
label train_completed:
    centered "The next morning..."
    pause 1.0

    if train_ending_money_returned == True:
        play music lo_fi_sunset if_changed
        music lo_fi_sunset
    
        n "CS and Arceus wake up feeling completely refreshed."
        
        scene 
        show amtrak_desert_day at manual_pos(0.5, 0.4, 0.5)
        show amtrak_dining_table 
        
        show amtrak_dining_food at manual_pos(805,145)
        show mean human hat flipped at left
        show tate at left
        show cs flipped at right
        show arceus at mid_offscreen_right
        with dissolve
        n "After Mean's shift ends, he and Tate invite the duo to join them for breakfast."
        n "The pancakes are warm and fluffy, the bacon is perfectly tender, and the orange juice is invigoratingly cool."
        n "Somehow, this moment is everything that CS didn't even know he needed."

        scene black with dissolve
        pause 1.0

        scene 
        show amtrak_desert_day as left:
            perspective (0.0, 1000.0, 0.5)
            matrixanchor (0.5, 0.5)
            matrixtransform RotateMatrix(-20, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -250, -400)
        show amtrak_desert_day as right:
            perspective (0.0, 1000.0, 0.5)
            matrixanchor (0.5, 0.5)
            matrixtransform RotateMatrix(-20, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -250, 400)
        show amtrak_observation_1

        show cs flipped at left
        show arceus flipped at right
        with dissolve
        
        pause 1.0
        n "The rest of the ride is a relaxing one."
        n "CS and Arceus spend part of the day in the lounge, just watching the world go by."
        n "While the Midwest is relatively flat, there is something soothing about such simplistic scenery..."
        n "It is exactly what Arceus had hoped to see on this trip."
        scene black with dissolve
        n "Still full from Tate's cooking, the two decide to enjoy one last nap before their next stop..."
    else:
        play music homely_yado_inn if_changed
        music homely_yado_inn
        
        if fun_value(FUN_VALUE_MUSIC):
            n "CS and Arceus wake up feeling rather groggy. They'd almost rather be staying at the Homely Yado Inn."
        else:
            n "CS and Arceus wake up feeling rather groggy."
        
        scene 
        show amtrak_desert_day at manual_pos(0.5, 0.4, 0.5)
        show amtrak_dining_table 
        
        show amtrak_dining_food at manual_pos(805,145)
        show mean human annoyed hat flipped at left
        show tate sheepish at left
        show cs disappointed flipped at right
        show arceus worried at mid_offscreen_right
        with dissolve
        n "After Mean's shift ends, Tate invites him, as well as CS and Arceus, to join them for breakfast."
        n "Mean looks exhausted, and Tate seems to be barely holding it together."
        n "While the four try to make pleasantries, there is an unshakable tension in the air."
        n "The food is bland. CS suspects that Mean only eats Tate's cooking to spare their feelings."
        n "CS prays that nobody notices his frequent use of the little salt packets on the table."

        scene black with dissolve
        pause 1.0

        scene 
        show amtrak_desert_day as left:
            perspective (0.0, 1000.0, 0.5)
            matrixanchor (0.5, 0.5)
            matrixtransform RotateMatrix(-20, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -250, -400)
        show amtrak_desert_day as right:
            perspective (0.0, 1000.0, 0.5)
            matrixanchor (0.5, 0.5)
            matrixtransform RotateMatrix(-20, 0, 0) * RotateMatrix(0, 90, 0) * RotateMatrix(0, 0, 0) * OffsetMatrix(0, -250, 400)
        show amtrak_observation_1

        show cs disappointed flipped at left
        show arceus angry flipped at right
        with dissolve
        
        pause 1.0
        n "The rest of the ride is a quiet one."
        n "CS and Arceus spend much of the day in the lounge, just watching the world go by."
        n "The Midwest doesn't offer much of a view."
        n "Nothing but flat land, dry plants, and a cloudless sky."
        scene black with dissolve
        n "Ultimately, the two decide that maybe it's best to just try to take a nap before their next stop..."
    
    pause 2.0
    n "Just before 3 PM, the train arrives at Union Station in Chicago."
    
    scene chicago_union_station
    show cs happy flipped at mid_mid_right
    show arceus happy at right
    show mean human hat flipped at left
    show tate at mid_left_left
    with dissolve
    n "CS and Arceus bid their friends farewell for now."
    pause 0.5
    show cs
    show arceus flipped
    pause 0.1
    hide cs
    hide arceus 
    with moveoutright
    n "The two then head towards another platform for the final train home."
    scene black with dissolve
    stop music fadeout 1.0
    pause 2.0
    jump train_dialogue

######## GO HOME ########
label train_return_home_transition:
    # yes i stole much of this from south route, oh well, i'm tired ok - tate
    stop music fadeout 1.0
    music end
    pause 2.0
    scene moynihan_interior with dissolve

    # TODO: add mean's chosen BGM here :D
    
    n "A day later, the two finally deboard the train in New York City."
    show cs at left
    show arceus flipped at center
    with moveinleft
    show arceus
    cs "Woohoo! We are almost home!"
    arceus "Thank goodness..."
    arceus "Although, I just realized something, CS."
    cs "Hmm?"
    show arceus worried
    arceus "We've still gotta drive you home."
    show cs disappointed
    cs "Oooooh... did {i}not{/i} think of that."
    cs "Fuck."
    show arceus
    arceus "Yeah, the walk there would take hours."
    cs "Shit, uhh, what are our other options?"
    play music mm_select volume 0.3 if_changed
    music mm_select
    show billy at right
    show cs
    billy "Need a ride? I'll take you to any destination for only $19.95!"
    show arceus happy flipped
    arceus "Welp, CS, we've found our other option!"

    # GOT THE MONEY BACK?
    if train_ending_money_returned == True:
        # DID YOU STEAL THE MONEY?
        if train_money_stolen == True:
            show bag at mid_mid_right with dissolve
            n "Arceus unzips the body bag and hands Billy a fistful of cash."
            show arceus flipped
            arceus "You think this will do the job?"
            billy "Wow! This totally doesn't look suspicious at all!"
            cs "We'll give you another $100 if you don't say anything."
            billy "That's cash in the trash!"
            hide bag with dissolve
        # DID YOU WIN THE MONEY?
        else:
            show case at mid_mid_right with dissolve
            n "Arceus opens the briefcase and gives Billy a gold bar."
            show arceus flipped
            arceus "You think this will do the job?"
            billy "Wow! You should save your money!"
            cs "We've got plenty more where that came from. You can keep it."
            billy "That's cash in the trash!"
            hide case with dissolve
    # DID YOU LOSE THE MONEY?
    else: 
        show arceus
        n "CS and Arceus rummage around in their pockets and manage to scrounge together $19.95."
        show arceus flipped
        cs "Here you go!"
        play sound sfx_moneyfalls
        show spent_19_95 at t_fake_rpg_text(0.1, 0.1, 0.5)
        billy "Thank you! Every Uber ride comes with my 100-percent satisfaction guarantee, or your money back!"

    billy "Well, then! Where are we going?"
    n "CS tells Billy his address. The group then heads down to the parking lot to begin the final leg home."
    hide cs
    hide arceus flipped
    hide billy
    with moveoutright
    stop music fadeout 3.0
    music end
    
    # final endings:
    if train_ending_money_returned == True:
        if train_money_stolen == True:
            jump train_home_rich_thief
        else:
            jump train_home_rich_winner
    if train_ending_money_returned == False:
        jump train_home_broke
