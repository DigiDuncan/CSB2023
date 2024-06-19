# TODO: mean needs a better text beep
# TODO: add bios/music tracks to people/jukebox once route is written

######## VARIABLES ########
label train_start_good:
    $ train_money_stolen = False
    jump train_intro_start

label train_start_bad:
    $ train_money_stolen = True
    jump train_intro_start

######## RUN INTRO ########
label train_intro_start:

    # syntax: if train_money_stolen true flip sprites

    cs "We should head back home now. I have a plan for our newfound riches."

    # flip
    if train_money_stolen == True:
       show arceus happy flipped
    else:
        show arceus happy 

    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"

    # flip
    if train_money_stolen == True:
       show cs flipped
       show arceus flipped
    else:
        show cs
        show arceus

    pause 2.0
    "{w=1.0}..."
    pause 1.0

    # flip
    if train_money_stolen == True:
        show cs flipped
        show arceus worried flipped
    else:
        show cs
        show arceus worried

    pause 1.0
    arceus "... But, how {i}will{/i} we get back, exactly?"
    arceus "That's a pretty long drive. I'm already beat."

    # flip
    if train_money_stolen == True:
        show cs surprised flipped
    else:
        show cs surprised

    cs "I saw some signs for an airport really clo--{w=0.25}{nw}"

    # flip
    if train_money_stolen == True:
        show arceus angry flipped
        show cs disappointed flipped
    else:
        show arceus angry
        show cs disappointed

    arceus "Dude, {i}no.{/i}"
    arceus "We are {i}not{/i} flying. I hate flying."
    show arceus worried flipped
    arceus "We've already been through enough, man..."
    cs "Well, if you don't want to drive, and you don't want to fly..."
    cs "What else is there?"
    cs "Like... a {i}train,{/i} or something?"

    # flip
    if train_money_stolen == True:
        show arceus flipped
    else:
        show arceus

    pause 2.0
    n "Arceus thinks for a moment."
    pause 2.0
    arceus "Actually... yeah."
    pause 2.0

    # that's not a hyphen
    play music "<loop 0>sub_game_select.ogg" volume 1
    music "Sub−Game Select - Jun Ishikawa"

    # flip
    if train_money_stolen == True:
        show arceus happy flipped
    else:
        show arceus happy

    arceus "...Yeah!"
    arceus "That sounds like a great idea!"
    arceus "We could just relax and watch the world go by!"
    arceus "Nobody has to drive, we won't have to worry about finding rest stops, {i}and{/i} I won't have a panic attack inside of a flying metal tube!"
    cs "I dunno... How long would it take, though? A flight would only be a few hours."
    cs "Don't trains have to stop a lot? Wouldn't it be more expensive, too?"

    # flip
    if train_money_stolen == True:
        show arceus worried flipped 
    else:
        show arceus worried 

    arceus "Come {i}on,{/i} man! I just want to unwind!"
    arceus "We don't even need to worry about how much it'll cost, remember?"

    # flip
    if train_money_stolen == True:
        show arceus happy flipped 
    else:
        show arceus happy
 
    arceus "We're filthy stinkin' {i}rich!{/i}"
    n "CS can sense that Arceus probably won't take \"no\" for an answer."
    cs "Well... I suppose we {i}do{/i} have all the money we could ever need, and we don't really have any reason to rush getting home..."
    
    # flip
    if train_money_stolen == True:
        show cs surprised flipped  
    else:
        show cs surprised

    cs "And I've never been on a cross-country train before..."

    # flip
    if train_money_stolen == True:
        show cs happy flipped  
    else:
        show cs happy

    cs "Yeah, you know what? Let's do it!"
    arceus "Let's go!"

    show cs happy
    show arceus flipped
    pause 0.25

    hide arceus
    hide cs
    with moveoutright

    scene black with fade
    stop music fadeout 3.0
    music end

    n "CS and Arceus hop back in the car and drive to the nearest train station."

    jump train_story_begin

label train_story_begin:

    n "A little over an hour later, the two arrive at Kingman Amtrak Station."

    scene kingman_exterior
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with fade

    play music "<loop 54.031>outdoors.ogg" volume 1
    music Outdoors - Miki Obata

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

    scene black with fade

    if train_money_stolen == True:
        $ train_money_container = "bag"
        $ train_money_stolen_dialogue_switch = "zip it up"
    elif train_money_stolen == False:
        $ train_money_container = "briefcase"
        $ train_money_stolen_dialogue_switch = "latch it shut"
    else:
        $ train_money_container = "treasure chest"
        $ train_money_stolen_dialogue_switch = "lock it shut"

    n "CS and Arceus get out of the car and grab the [train_money_container] of money."

    scene kingman_exterior with fade

    show cs flipped at left
    show arceus at right
    with moveinright

    pause 2.0
    show cs
    pause 1.0

    cs "Oh, right."
    cs "I guess we won't be needing this for a while."
    play sound "audio/sfx_lego_break.WAV"
    n "CS quickly deconstructs the Lego car. He shoves the colorful little bricks into the [train_money_container] for later."
    n "The [train_money_container] is now full to bursting, but CS just barely manages to [train_money_stolen_dialogue_switch]."
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
    scene black with fade

    scene kingman_interior with fade

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
    
    show cs flipped
    show arceus
    n "They spot the entrance to a museum."    
    
    scene kingman_museum with fade

    arceus "Oh, look at all those little trains. Wanna poke around there?"
    cs "I don't see why not. Not like we have anything else to do."
    arceus "Alrighty, let's go."
    scene black with fade
    n "CS and Arceus wander around Kingman Railroad Museum for a little while."
    n "While not many exhibits can fit inside such a small building, there is just enough to see to pass the remaining time."
    n "About five minutes before the train's expected arrival, the two make their way out onto to the platform."
    
    scene kingman_platform_2 with fade

    show arceus flipped at mid_mid_left
    show cs disappointed at left
    with moveinleft
    pause 1.0

    cs "... Man, that's some bad luck, though. What are the odds of this place burning down {i}twice?!{/i}"
    show arceus
    arceus "I mean, back then, trains were powered by steam."

    # arc and mean wanted this
    if fun_value(100):
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
    if fun_value(10):
        $ polar_express_fun_value = True
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
    play sound "audio/sfx_amtrak_horn.wav"
    n "The conversation is interrupted by the blare of a train horn."

    scene kingman_train_arrive with fade
    play music "<loop 27.401>ochre_woods_day.ogg" volume 1
    music Ochre Woods ~ Day - Miki Obata
    n "The two watch as the locomotive approaches the station and eventually slows to a stop."
    hide cs
    hide arceus

    scene amtrak_arrive_close with fade

    show arceus flipped at mid_mid_left
    show cs at left
    with moveinleft

    arceus "Welp, there it is."
    n "The two wait for the incoming passengers to disembark."
    pause 2.0
    show cs scared
    show arceus worried flipped
    tate_offscreen "{bt=a3-p10-s4}{size=+24}Alllllll aboarrrrrrd!!" with hpunch
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
    tate "I'm Tate. I'm CS's-- uh... "
    show cs surprised
    show tate sheepish flipped
    tate "Um... friend. Yes."
    show cs happy
    cs "Yeah! Of course we're friends."
    tate "Of course."
    show arceus worried flipped
    show tate sad flipped
    n "Arceus raises an eyebrow at this interaction."
    n "He decides that maybe it's better not to ask."
    show cs
    show tate sheepish flipped
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

    if polar_express_fun_value == True:
        show arceus flipped
        arceus "I told you!"
        show arceus worried flipped

    show tate sad
    tate "Yes, sir..."
    amtrak_conductor "Let's get a move on."

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
    scene black with fade
    n "The group boards the train."
    n "CS and Arceus buy tickets from the staff. After a brief tour of all of the amenities, the trio heads towards the sleeper cars."

label train_boarding:

    scene amtrak_sleeper_corridor
    with fade

    play music "<loop 0.916>bedroom_day.ogg" volume 1
    music Bedroom ~ Day - Miki Obata
    
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
    amtrak_stewardess "{size=-10}Or, why don't {i}you{/i} have a nap, too? {w=0.25}Do you {i}ever{/i} sleep?"
    tate "Oh... right."
    tate "Sorry."
    tate "I guess it {i}has{/i} been a while since I've seen CS. I can stay here for a bit..."
    show tate sheepish flipped
    tate "...if you're okay with that."
    show cs happy
    cs "Of course!"
    show arceus worried flipped
    show cs
    arceus "Well, while you two are doing that, I {i}really{/i} need to use the can..."
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
    tate "I thought I'd set up a surprise for him in the dining car, but the other staff didn't like it..."
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
    cs "You know, just a little, uhHH--!!{w=0.25}{nw}"
    play sound "audio/sfx_punch.ogg"

    # TODO: less crumnchy lupin sprite
    # TODO: sfx - Lupin musical sting

    show cs scared at mid_offscreen_left with hpunch
    show tate shock flipped
    show lupin at mid_mid_left with dissolve
    show cs concentrate
    show tate shock flipped at right with moveinright
    n "CS is knocked to the ground as a stranger sprints down the corridor!"
    unknown "Sorry, pretty kitty! I've gotta {i}run!"
    hide lupin with dissolve
    n "The weird guy hurries away."
    pause 0.25
    tate "Oh, my God! CS, are you alright?!"
    cs "Y-{w=0.1}Yeah..."
    cs "More surprised than anything."
    show tate shock flipped at left with moveinleft
    n "Tate helps CS up from the floor."

    show cs concentrate at left
    show tate sheepish flipped at center
    with moveinright

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

    scene black with fade

label train_enter_sleeper:

    # TODO: better sleeper bg
    play sound "audio/sfx_sliding_door_close.mp3"
    show amtrak_sleeper_interior_day
    show arceus at right
    with fade

    n "CS and Tate enter the sleeper unit just as the train takes off."
    
    show tate at mid_mid_left
    show cs at left
    with moveinleft

    show arceus worried
    arceus "Hey, guys. Sorry about that."
    arceus "I think something I ate at that creepy-ass pizza place didn't quite agree with me."
    show cs disappointed
    show tate stare
    cs "Damn. Are you feeling any better?"
    show arceus
    arceus "Oh, yeah. I think I'll be alright now."
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
    tate "Oh, uh..."
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
    tate "...Right?"

    stop music fadeout 3.0
    music end

    show cs scared
    show tate shock flipped
    show arceus worried
    with shake2
    play sound "audio/sfx_hard_knock.mp3"

    n "A sudden hard knock on the door startles the group."

    play music "<loop 0>item_bounce.ogg" volume 0.8
    music Item Bounce - Akira Miyagawa
    play sound "audio/sfx_hubbub.ogg" loop fadein 2.0 volume 0.3

    n "An uproar of angry passengers grows steadily louder."

    cs "What the hell?!"
    tate "No, no, {i}no!"
    tate "This {i}can't{/i} be good!"
    arceus "So much for a relaxing trip..."
    n "The door is slid open with a heavy hand."
    
    play sound "audio/sfx_sliding_door_open.mp3"
    pause 1.0
    
    show cs scared flipped at mid_mid_right
    show tate shock flipped at right
    show arceus worried at mid_offscreen_right
    with moveinright

    show amtrak_conductor flipped at left
    with moveinleft
    
    amtrak_conductor "Alright, every--{w=0.25}{nw}"
    amtrak_conductor "Oh. {w=0.5}{i}Tate."
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
    tate "{i}{size=-10}Eep!"
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
    play sound "audio/sfx_hubbub.ogg" loop volume 0.3
    amtrak_npc_1 "Hey, my watch is gone, too!" with hpunch
    amtrak_npc_2 "Man, {i}fuck{/i} your watch! They took my damn {i}Switch!{/i}"
    amtrak_npc_3 "Such {i}language!" with hpunch
    amtrak_npc_3 "My dearest mother's priceless brooch is also missing, and you don't hear {i}me{/i} speaking like an utter {i}barbarian!"
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
    arceus "I mean, all we had was the one [train_money_container]."
    pause 1.0
    show arceus worried flipped
    pause 1.0
    show arceus worried
    pause 2.0

    arceus "... CS, where is the [train_money_container]?"
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
    arceus "I thought {i}YOU{/i} had it!!" 
    pause 1.0

    show cs worried
    cs "Oh."
    show cs scared
    cs "Shit."

    if train_money_stolen == True:
        $ train_money_stolen_dialogue_switch = "black bag"
        $ train_money_stolen_dialogue_switch_2 = "... {w=0.5}won"
    elif train_money_stolen == False:
        $ train_money_stolen_dialogue_switch = "metal briefcase"
        $ train_money_stolen_dialogue_switch_2 = " won"
    else:
        $ train_money_stolen_dialogue_switch = "red and gold treasure chest"
        $ train_money_stolen_dialogue_switch_2 = " totally plundered"

    show cs disappointed flipped
    cs "Yes, sir, we're missing a single [train_money_stolen_dialogue_switch] filled with money we[train_money_stolen_dialogue_switch_2] while we were in Vegas."
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
    amtrak_conductor "Tate. You'd better behave. Stay out of the way during this investigation."
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
    music end

    show cs disappointed at left
    show tate sad at mid_mid_left
    show arceus worried at right
    with moveinleft

    play sound "audio/sfx_sliding_door_close.mp3"
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
    arceus "Think about it. You didn't, like, help him with his job interview, right?"
    show tate sad
    tate "Well, no..."
    show tate sheepish
    tate "I mean, I looked over his résumé, but that's all."
    show cs happy
    show tate sheepish flipped
    cs "Exaaaaactly. You've done all you can, so, just let things happen."
    show tate srs flipped
    tate "How can you be so... {i}unbothered{/i} by all of this? And after you just lost so much money?!"
    show arceus worried
    arceus "{size=-10}Well, {i}I'm{/i} bothered by it..."
    show cs worried
    cs "I mean, yeah, it totally sucks balls, but all it means is that when we get home, things will just be the same as they were before."
    show tate sheepish flipped
    tate "Even so, I really do hope they find everyone's things..."
    show tate sad flipped
    tate "I'm just so scared that they'll accuse Mean of stealing it, or something, since he's so new..."
    tate "I really don't know if he could handle losing {i}this{/i} job, too."
    show cs disappointed
    cs "Wait, what happened at his last job?"
    show tate srs flipped
    tate "It was so fucking stupid."
    tate "So, he was working for this home repair company, right? They hired him on as a security guard, since he's all spiky--{w=0.25}{nw}"
    show arceus 
    arceus "{i}Spiky?{/i} Wha--{w=0.25}{nw}"

    # TODO: can we replace "pushed" to reference whichever attack was used in CSBII?

    tate "--and then some weirdo dressed as a catgirl maid broke in and fought the CEO! A lot of people got hurt!"
    show tate shock flipped
    show cs worried
    show arceus worried
    tate "I think Mean said that someone even got pushed off of the roof!"
    show tate sheepish flipped
    tate "But since Mean couldn't... {w=0.5}{size=-5}hold him off... {w=0.5}{size=-5}he was... {w=1.0}{size=-5}fired..."
    "..."
    pause 2.0
    show tate shock flipped
    n "Tate falls silent. They stare wide-eyed at CS' outfit."
    pause 2.0
    show cs scared
    cs "... Woah, Tate, why are you look--{w=0.25}{nw}"
    
    # TODO: tate needs a FURIOUS sprite
    # TODO: bgm

    show tate srs flipped
    tate "{bt=a3-p10-s4}{size=+36}IT WAS {i}YOU!!" with hpunch
    cs "Wha-- {i}huh?!"
    tate "CS, WHAT THE {i}FUCK?!"
    tate "{i}YOU{/i} BROKE INTO HOH SIS?!"
    show cs worried
    cs "Oh, yeah, uh--{w=0.25}{nw}"
    
    show tate cry flipped
    n "Tate is on the verge of tears."
    tate "My best friend lost his job, and it's your fault..."
    tate "And now, you're {i}here..."
    tate "I can't believe this..."
    show cs disappointed
    cs "Tate..."
    cs "Listen to me, please--{w=0.25}{nw}"
    show tate srs flipped
    tate "{i}No!"
    tate "I don't want to hear it!"
    tate "Is {i}this{/i} what you've been up to since we--{w=0.25}{nw}"
    "..."
    tate "You know what? No."
    tate "Mean's shift starts soon. I need to be there for him."
    tate "If either of y'all see him, you will not breathe a word of {i}any{/i} of this to him."
    tate "Not about the thefts, and {i}certainly{/i} not about what happened at HoH SiS."
    tate "He doesn't need this. Especially not today."
    show cs worried
    n "Tate reinforces their demand with a piercing glare towards CS."
    show tate srs
    n "Tate then suddenly stands up." with vpunch
    tate "I'm sorry."
    tate "I need to go."
    show tate sad flipped
    pause 0.25
    hide tate with moveoutleft
    play sound "audio/sfx_sliding_door_open.mp3"
    n "Tate swiftly exits the room and runs off, not even bothering to shut the door behind them."

    # TODO: bgm

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
    cs "...and all will be right with the world!"

    # TODO: some funny cheery fanfare jingle?

    pause 1.0
    show arceus angry
    arceus "... {i}I{/i} think you're being way too optimistic about all of this."
    arceus "I'm going to bed."
    show cs disappointed
    cs "Yeah, me too..."

    scene black with fade
    n "CS and Arceus decide to call it an early night."
    n "CS effortlessly falls into a deep slumber."
    n "While the fold-out bed is indeed quite comfortable, Arceus struggles to get any rest."

    # TODO: better sleeper bg

    scene amtrak_sleeper_interior_night
    with fade
    pause 1.0
    arceus "Fuck..."
    arceus "I'm so tired, but I {i}still{/i} can't fucking sleep..."
    arceus "I wonder if they have booze on this train."

    show arceus dark at center with dissolve
    n "Arceus quietly gets out of bed, being careful not to wake CS."
    hide arceus with moveoutleft

    play sound "audio/sfx_sliding_door_open.mp3"

    if fun_value(10):
        pause 2.0
        n "...But the door was heavier than he expected."

        # TODO: replace with a proper sliding door slam later

        play sound "audio/sfx_clonk.wav"
        with hpunch
        pause 1.0
        arceus "{i}Shit!"
        n "Arceus grimaces at the sudden noise and peeks through the window back at CS."
        "..."
        n "Thankfully, CS is still fast asleep."
    else:
        pause 2.0
        n "He gently shuts the door behind him, then makes for the dining car in hopes of drinking his worries away."
        play sound "audio/sfx_sliding_door_close.mp3"

    scene black with fade
    pause 3.0

label train_dining:

    play music "<loop 3.1>krabby_klub.ogg" volume 1
    scene amtrak_dining_car
    with fade
    pause 1.0
    music Krabby Klub - Tsukasa Tawada
    pause 0.5
    show arceus at center with moveinright

    n "Arceus arrives at the dining car."
    n "The aromas of so many different foods mingling together overwhelm his canine senses."
    arceus "Geez, it smells like a high school cafeteria..."
    arceus "I think I'll just grab myself a bottle of wine and get out of here."
    show arceus at left with moveinleft
    n "As he approaches the counter, Arceus finds his attention redirected towards a yellow... {w=0.5}thing."

    scene amtrak_dining_table
    show mean at t_mean_dining_car
    show amtrak_dining_food at t_dining_car_breakfast behind mean
    hide arceus
    with fade

    n "A strange spiny entity is surrounded by piles of pancakes, sky-high stacks of sausages, oodles of eggs, and a whole bunch of bacon."
    n "Arceus can't help but stare in awe at both the enormous spread of food..."
    n "...and at the brightly-colored creature currently demolishing it."
    show mean happy
    mean_offscreen "LET'S {w=0.25}FUCKING {w=0.25}{bt=a3-p10-s4}{i}GOOOOOOOO!!"
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
    
    play music "<loop 0>prof_kranes_kidnap.ogg" volume 1
    music "Prof. Krane's Kidnap - Tsukasa Tawada"

    show mean furious
    mean_offscreen "{i}WHAT?!" with hpunch
    mean_offscreen "{bt=a3-p10-s4}{size=+36}ON {i}MY{/i} FUCKING TRAIN?!" with vpunch
    mean_offscreen "MY FIRST SHIFT STARTS IN {bt=a3-p10-s4}{i}TWENTY MINUTES!" with hpunch
    n "One can practically see the gears begin to turn in Arceus' head as he realizes who he is talking to."

    # arc wanted this
    if fun_value(10):
        show arceus
        arceus "Wait, hey, can you do a Dallas impression?"
        show mean wat
        mean "Like this?"
        show mean furious

        # TODO: record the dallas AUUUUUUUUUGH when mean is better

        mean "{bt=a3-p10-s4}{size=+36}AUUUUUUUUUGH!!" with hpunch
        show arceus happy
        arceus "Yeah!"
        show arceus worried
        arceus "... Wait."

    show arceus worried
    arceus "Oh."
    arceus "{i}Fuck."
    hide mean with moveoutright
    n "Mean dashes out of the dining car!"

    scene amtrak_dining_car
    with fade
    pause 1.0
    show mean scared at offscreenleft with determination
    show mean scared at offscreenright
    with MoveTransition(0.5)
    pause 2.0
    show arceus worried flipped at center with moveinleft
    pause 1.0
    n "Arceus, visibly shaken, leaves as well, without even getting the drink he came for."

    # fun value
    if fun_value(5):
        $ pancake_fun_value = True
        n "He did at least steal a few of the abandoned pancakes."

    n "He rushes back to the sleeper car as quickly as he can."
    hide arceus with moveoutright
    scene black with fade
    
label train_wakeup:

    scene amtrak_sleeper_interior_night
    with fade
    play sound "audio/sfx_sliding_door_open.mp3"
    pause 1.0
    show arceus worried dark flipped at center with moveinleft
    pause 0.5
    arceus "CS!" with hpunch
    play sound "audio/sfx_sliding_door_close.mp3"
    arceus "Wake up!!"
    cs "Hnnnh... huh?"
    n "Arceus flips on the lights."
    play sound "audio/sfx_lightswitch.wav"
    show amtrak_sleeper_interior_day
    hide arceus
    show arceus worried flipped
    pause 0.5
    n "CS lets out a groan and rolls back over in bed."
    show arceus angry flipped
    cs "Zzzzz..."
    cs "{size=-12}Five more minutes, mom..."
    show arceus angry flipped at right with moveinleft
    n "Arceus pulls the blanket off of CS and drags him out of bed."

    show arceus angry flipped at center
    show cs concentrate flipped at right
    with moveinright
    
    cs "Hnngh, huh, what, why?!"
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
    cs "{w=0.25}... Oh no."
    cs "We are {i}definitely{/i} in trouble n--{w=0.25}{nw}"
    show arceus worried with hpunch
    music end
    play sound "audio/sfx_sliding_door_open.mp3"
    n "As if on cue, the room door slides open." with hpunch
    
    tate "{bt=a3-p10-s4}{size=+24}C.{w=0.1}S. ONE HUNDRED AND EIGHTY{w=0.1}-EIGHT!!" with vpunch

    show arceus worried at mid_mid_right
    show tate srs at left
    with moveinleft

    n "Tate stomps into the room, making a beeline for CS."
    show tate srs at mid_mid_left with moveinleft

    if fun_value(15):
        tate "YOU HAD {bt=a3-p10-s4}{i}ONE{/i}{/bt} JOJ!" with vpunch
        show tate srs at center with moveinleft
        tate "YOU'RE GONNA NEED A WHOLE LOT MORE THAN {bt=a3-p10-s4}{i}FOUNDATION\nREPAIR{/i}{/bt} AFTER {i}I'M{/i} DONE WITH YOU!" with vpunch
    else:
        tate "YOU HAD {bt=a3-p10-s4}{i}ONE{/i}{/bt} JOB!" with vpunch
        show tate srs at center with moveinleft
        tate "IS IT REALLY {i}THAT{/i} HARD FOR YOU TO KEEP A SECRET?!" with vpunch

    cs "Tate, wait!"
    arceus "It wasn't him!"
    arceus "I'm sorry!"
    n "Tate inhales for another scream."
    arceus "I didn't know Mean was... {i}like{/i} that!"

    stop music

    show tate shock
    show cs worried flipped
    n "Tate is caught off-guard by Arceus' comment."
    pause 1.0
    show tate srs at mid_mid_left with moveinright
    pause 2.0

    tate "Like... what?"
    arceus "I thought he'd be... just... you know... {i}some guy."
    arceus "I didn't know he's, uh... whatever he is."
    pause 2.0    

    play music "<loop 1.071>e_gadds_lab.ogg" volume 1
    music "E. Gadd's Lab - Kazumi Totaka & Shinobu Tanaka"

    show tate sheepish
    show cs disappointed flipped
    pause 2.0
    "..."
    tate "{i}O{w=0.1}-Oh..."
    pause 1.0
    tate "I guess... {w=0.5}{size=-5}that would have been... {w=0.5}{size=-5}an {i}important{/i} detail to...{w=1.0}"
    tate "{size=-15}{i}Fuck..."
    pause 3.0
    n "Heavy breathing approaches from the hallway."
    pause 1.0

    show mean tired at mid_offscreen_left
    show tate sheepish at mid_mid_left
    with moveinleft
    mean "{i}Pant... {w=0.25}{nw}"
    show mean tired at left with moveinleft
    mean "{i}Pant... {w=0.25}{nw}"
    show mean tired at center_left with moveinleft
    mean "{i}Wheeze... "

    show mean surprised
    mean "There... {i}cough"
    mean "...There you are, Tate..."
    
    # here goes tate having too much fun with sprites again

    show tate shock flipped
    show mean scared
    show cs scared flipped
    tate "{bt=a3-p10-s4}{size=+12}Uwaaaaah!" with vpunch
    tate "Mean!"
    show tate sad flipped
    show mean surprised
    tate "I'm so sorry!"
    tate "I told them not to tell you!"
    show mean wat
    mean "Tate--{w=0.25}"
    tate "I wanted it to be kept secret so you could focus on work and{w=0.25}{nw}"
    tate "I think the day shift people think I'm to blame for everything and{w=0.25}{nw}"
    show mean angry
    show cs worried flipped
    mean "{size=+12}{i}Tate--!{w=0.25}"
    tate "I was really scared that they might blame you too since{w=0.25}{nw}"
    show cs disappointed flipped
    show arceus angry
    tate "you were asleep all day and that means that you were the only one not accounted for when--{w=0.25}{nw}"
    show mean furious
    show tate shock flipped
    show cs scared flipped
    show arceus worried
    mean "{bt=a3-p10-s4}{size=+24}{i}TAAAAATE!!" with vpunch

    show mean ayo
    mean "What the fuck are you {i}talking{/i} about?"
    show tate cry flipped
    show cs disappointed flipped
    tate "{size=-10}I just wanted you to have a good first day..."
    show mean worried
    mean "What do you mean?"
    show mean 
    mean "Today's been {i}great!"
    show tate shock flipped
    tate "Huh?!" with vpunch
    show mean happy
    mean "Yeah!"
    mean "You made me the best breakfast I've had in ages, I start my dream job in 15 minutes, {i}and{/i} I get to travel the US with my best friend!"
    
    if pancake_fun_value == True:
        show arceus happy
        arceus "{size=-15}Those were some damn good pancakes, by the way."
        show arceus worried

    mean "If it weren't for you, I'd still be sitting at home playing fucking {i}Minecraft{/i} and listening to whatever weird shit's popular on Spoofy!"
    mean "What could be better?"
    show tate sad flipped
    tate "But, what about the thief?!"
    show mean ayo
    mean "Wait, you think Amtrak actually gives a shit about stolen items?"
    show mean angry
    mean "Bro, I was more worried about {i}you!"
    show cs disappointed flipped
    show mean worried
    mean "When that yellow fucker over there told me there was a crook on the train, I was worried that somebody was out here, like, {i}mugging{/i} people!"
    show arceus angry
    arceus "\"Yellow fucker\"?"

    # let's turn my shitpost into a fun value i suppose lmao
    if fun_value(100):
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
        show tate srs
        tate "What the fuck?"
        show tate srs flipped
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
    show mean flipped
    hide mean with moveoutleft
    n "Mean rolls away down the hall."
    show tate sad at left with moveoutleft
    show tate sheepish
    pause 0.5
    tate "So, uh..."
    tate "I guess, since Mean has to work..."
    show arceus
    tate "What do y'all think we should do?"

    menu:
        tate "Got any ideas?"
        "Let the staff handle it":
            jump train_allow_staff
        "Take matters into your own hands":
            jump train_begin_heist

######## BAIL NOW ########
label train_allow_staff:
    $ train_skip_at_chicago = True

    cs "I think we should just let the staff do their jobs."
    tate "But Mean said that Amtrak doesn't care about stolen things!"
    show cs happy flipped
    cs "But the day conductor said that he was investigating. He seemed pretty serious."
    show tate srs
    tate "Oh, come on. Do you {i}really{/i} trust that guy?"
    show cs disappointed flipped
    cs "I mean, do we really have a choice? It's clear that they don't want you interfering."
    show arceus angry
    arceus "Okay, I am {i}not{/i} about to spend the rest of this trip listening to you two bickering."
    arceus "Let's just let them do the investigation, and if we get it back, we get it back."
    arceus "I want to go to bed."
    show tate sad
    tate "I suppose it is late..."
    show tate sheepish
    tate "It was nice seeing you again, CS. It was nice to meet you too, Arc."
    tate "I hope you two enjoy the rest of the journey!"
    scene black with fade
    n "Tate bids CS and Arceus farewell before heading towards the cab to join Mean."
    n "As expected, the money was never returned."
    n "After a brief layover in Chicago, CS and Arceus take the final uneventful transfer to New York."
    stop music fadeout 3.0
    music end

    jump train_return_home_transition

######## BEGIN THE HEIST ########
label train_begin_heist:
    $ train_skip_at_chicago = False
    cs "Do you really think we'd be able to track down the thief?"
    tate "I sure hope so. Unless they jumped off of a moving train, they've gotta be here."
    show cs flipped
    cs "Hey, Arc! You've done cybercrime before, right?"
    show arceus angry flipped
    cs "Where do you think the thief would hide stolen goods?"
    show tate shock
    tate "Arc did what now?"
    show cs worried flipped
    arceus "Gee, thanks, CS."
    arceus "But, since you asked..."
    show arceus
    show tate sheepish
    show cs disappointed flipped
    arceus "I have a few theories. There aren't many places to hide on a train like this."
    arceus "We can check the sleeper cars here, we could check the dining car..."
    arceus "I doubt we can get access to it, but maybe we could get someone to check the cab."
    tate "Actually, Mean lent me his spare key to the cab in case I needed the toilet in there, so I can check it."
    arceus "Oh, nice. I know my way around the dining car, so I can look there."
    cs "Guess I'll check around here. Maybe the [train_money_container] is just under a seat or something."
    arceus "Sounds like a plan."
    show tate
    show cs flipped
    tate "Yep, I'll head out then. Should we meet up in economy class when we're done looking?"
    cs "Yeah, sounds good."
    arceus "Sure thing."
    tate "Well, let's get to it, then."
    show tate flipped
    pause 0.5
    hide tate
    hide arceus
    with moveoutleft

    n "CS, Arceus, and Tate split up to search different areas of the train."

    stop music fadeout 3.0
    music end
    scene black with fade
    jump train_meanwhile

label train_meanwhile:
    centered "Meanwhile..."
        
    pause 0.5
    scene amtrak_cab
    show lupin at center
    with fade
    play music "<loop 0>onbs.ogg"
    music "ONBS - Tsukasa Tawada"

    pause 1.0
    lupin_offscreen "This is perfect! I can't believe I could just waltz on in like that!"
    show lupin hat with dissolve
    lupin_offscreen "And with {i}this..."
    lupin_offscreen "Nobody would ever suspect the driver, right?"
    play sound "sfx_sliding_door_open.mp3"
    n "The cab door suddenly opens from behind."
    show lupin hat flipped at left
    show amtrak_conductor at right
    with moveinright
    play sound "sfx_sliding_door_close.mp3"
    show lupin hat flipped
    amtrak_conductor "Oh, good evening, Mean."
    amtrak_conductor "I almost didn't recognize you {color=#D03131}like that.{/color}"
    amtrak_conductor "Well, you already know what to do, so I'll leave you to it."
    lupin_offscreen "You got it, boss!"
    amtrak_conductor "Hopefully your little friend will stay out of the way tonight. Corralling them all day has me absolutely beat."
    lupin_offscreen "No worries, boss. I'm sure {color=#FFDBFC}pink sweater{/color} is tired from cooking all day."
    amtrak_conductor "I would certainly hope so."
    amtrak_conductor "For now, it's been a long day."
    amtrak_conductor "If you'll excuse me..."
    hide amtrak_conductor with moveoutleft
    show lupin hat
    play sound "sfx_sliding_door_open.mp3"
    n "The conductor retires to the cab toilet for a while."
    play sound "sfx_sliding_door_close.mp3"
    pause 4.0
    play sound "sfx_fart_with_reverb.mp3"
    with hpunch
    with hpunch
    with hpunch
    pause 1.5
    lupin_offscreen "...Seems like he'll be a while."
    show lupin hat flipped at center with moveinright
    lupin_offscreen "And that's just what I need."
    scene black with fade
    pause 1.0
    jump train_search_arceus

label train_search_arceus:
    scene amtrak_dining_car
    show arceus at center
    with fade
    n "Arceus returns to the dining car."
    arceus "Well, let's see if anything is hidden around here..."
    show arceus at left with moveinright
    n "Arceus checks under the tables..."
    show arceus flipped at right with moveinleft
    n "Then, he checks under the seats..."
    show lupin hat at offscreenright behind arceus with determination
    show lupin hat at offscreenleft
    with MoveTransition(2.0)
    show arceus at mid_left with moveinright
    n "But he finds a whole lot of nothing."
    arceus "I guess maybe there's just nothing here."
    scene amtrak_dining_table
    show amtrak_dining_food at t_dining_car_breakfast
    show amtrak_dining_pancake at t_dining_car_pancake behind amtrak_dining_food
    with fade
    n "From across the room, Arceus glances towards the forgotten breakfast." 
    arceus "It's a damn shame that all of that went to waste."

    if pancake_fun_value == True:
        arceus "Mean probably wouldn't care if I took a bit more..."
    else:
        arceus "I wonder if Mean would mind if I grabbed a bit before it goes bad..."
    show lupin hat at mid_right with moveinright
    pause 1.0
    show amtrak_dining_food at offscreenleft
    show lupin hat at offscreenleft
    with ease
    arceus "What the fuck?!"
    show arceus angry at right behind amtrak_dining_pancake with moveinright 
    arceus "Man... what is {i}wrong{/i} with people?!"
    n "Arceus spots a lone pancake."
    show amtrak_dining_pancake at t_arc_pancake with ease
    arceus "I guess I'll at least take this one..." 
    hide amtrak_dining_pancake with dissolve
    pause 1.5
    arceus "I need a drink..."
    show arceus angry flipped
    hide arceus with moveoutright
    scene black with fade
    pause 2.0
    arceus "What the fuck? He even took the {i}booze?!"
    
label train_search_cs:
    
    # TODO: YES I KNOW THIS SCENE IS CRUSTIER THAN FRENCH BREAD PLS HELP

    pause 1.0
    scene amtrak_sleeper_corridor
    show cs disappointed at center
    with fade
    pause 1.0

    n "CS finds himself alone in the deserted corridor."
    cs "I guess I should have expected nobody to keep their doors open this late."
    cs "I probably should have {i}also{/i} expected that they'd not let me in..."
    show cs worried
    cs "That lady in Room 3 threw a {i}shoe{/i} at me, for fuck's sake!"
    show cs disappointed
    cs "Maybe I should just head up front to meet the others..."
    show cs disappointed at right with ease
    pause 0.5
    n "CS stops suddenly."
    n "There is, in fact, a single door open." 
  
    scene amtrak_sleeper_open_bg
    show lupin hat at mid_right
    
    if train_money_stolen == True:
        show bag at mid_mid_left
    else:
        show briefcase at mid_mid_left

    show amtrak_dining_food at mid_mid_left
    show amtrak_sleeper_open_fg
    with fade

    n "A man in a familiar red jacket is just finishing off a large breakfast."
    lupin_offscreen "I can't believe how easy that was. {color=#FFDBFC}Pink sweater{/color} had the staff running around like ants!"
    lupin_offscreen "They don't know it, but they'd be my perfect accomplice!"
    hide amtrak_dining_food with dissolve
    pause 1.0
    lupin_offscreen "Mmmm..."
    lupin_offscreen "{i}Burp!{/i}" with hpunch
    lupin_offscreen "Oh, pardon me!"
    lupin_offscreen "I guess asking them on a dinner date would be a bad idea. They'd totally out-cook the chef!"
    lupin_offscreen "I wonder if they like movies..." 
    n "CS can't help but notice something..."
    n "He decides to try looking from another angle."

    show amtrak_sleeper_open_bg at mid_mid_left
    show amtrak_sleeper_open_fg at mid_mid_left
    with ease

    pause 2.0
    cs "Hey! That's our money!"
    cs "Hey you! Give that back!" with hpunch
    lupin_offscreen "Hey, it's my pretty kitty!"
    lupin_offscreen "Sorry, babe, but I've gotta split!"

    scene amtrak_sleeper_corridor
    show cs angry at center
    show lupin hat at offscreenright
    show lupin hat at center with MoveTransition(0.25)

    play sound "audio/sfx_punch.ogg"
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
    pause 1.0
    show cs disappointed
    cs "\"Pretty kitty\"?"
    pause 1.5
    cs "That means..."
    pause 1.0
    show cs angry
    cs "... That guy must have stolen the money when he knocked me down earlier!"
    cs "At least I got a good look at his face this time!"
    cs "I need to go find the others!"
    show cs angry at offscreenright with moveinleft
    scene black with fade

label train_search_tate:
    pause 0.5
    scene amtrak_cab
    show lupin hat at left
    with fade

    play sound "sfx_sliding_door_open.mp3"
    pause 3.0

    show tate flipped behind lupin at offscreenright
    show tate flipped at right with moveinright
    
    tate "Excuse me, Mr. Conductor?"
    show lupin hat flipped
    tate "Have you seen--{w=0.25}{nw}"
    show tate srs flipped
    "..."
    pause 2.0   
    tate "...Why are {i}you{/i} here?"
    
    lupin_offscreen "Hey, look, it's my favorite {color=#FFDBFC}pink sweater{/color}!"
    show lupin hat flipped at mid_mid_left with moveinleft 
    lupin_offscreen "We just seem to keep finding each other!"
    show lupin hat flipped at center with moveinleft
    show tate srs flipped at mid_offscreen_right with moveoutright
    lupin_offscreen "Are you absolutely sure you mean what you say?"
    show lupin hat flipped at mid_mid_right with moveinleft
    lupin_offscreen "Are you absolutely {i}sure{/i} that we're not meant to be?{image=heart_small.png}"
    show lupin hat flipped at right with moveinleft
    pause 0.1
    play sound "audio/sfx_punch.ogg"
    show lupin hat flipped at left with MoveTransition(0.1)
    with vpunch
    n "Tate pushes the stubborn suitor away."
    show tate srs flipped at right with moveinright
    pause 1.0
    tate "There are only three things in my life that I have {i}ever{/i} been more sure of."
    tate "Now... I don't know who you are, but I'm getting really sick of seeing you."
    tate "I would have thought you'd taken the hint while I was cooking this morning, but I guess I have to spell it out for you."
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
    play sound "sfx_fart.mp3"
    with vpunch
    with hpunch
    with hpunch
    pause 2.0
    lupin_offscreen "...and it appears that your crew's {i}muscle{/i} is currently {i}unavailable."
    play sound "sfx_poot.mp3"
    with vpunch
    pause 1.0
    show tate sheepish flipped
    tate "N-{w=0.1}Now, you listen here. Don't underestimate me..."
    tate "Just give me the hat, yeah? Besides, even if you're not scared of {i}me,{/i} Mr. Conductor will probably be out at any moment."
    play sound "sfx_fart_deep.mp3"
    with hpunch
    with hpunch
    pause 3.0
    tate "{size=-15}...Or not."
    pause 1.0
    show lupin hat flipped at center with moveinleft
    n "The suave criminal leans in towards Tate."
    pause 0.5
    lupin_offscreen "Tell ya what, pumpkin."
    lupin_offscreen "If you'll agree to {i}one{/i} date with me, I'll give it back."
    show tate srs flipped
    tate "Not a chance in hell."
    lupin_offscreen "Well, then. It appears that we are locked in a stalemate, doesn't it?"
    lupin_offscreen "But, I don't really care for chess. I have it on good authority that {i}you{/i} don't, either."
    show tate sheepish flipped
    lupin_offscreen "I think we'd both rather play a different game."
    tate "Speak for yourself..."
    lupin_offscreen "No, no, hear me out! Personally, I'm a {i}huge{/i} fan of hide and seek."
    tate "Wha--{w=0.25}{nw}"
    lupin_offscreen "Ah, but today's your lucky day!"
    lupin_offscreen "See, I've heard that you're bad at counting."
    lupin_offscreen "Fortunately, for you, you'll only need to count to 1.{image=heart_small.png}"
    show tate shock flipped
    show lupin hat flipped at offscreenright with MoveTransition(0.25)
    show tate shock at right
    pause 1.0
    n "The crook is gone with the wind."
    tate "Oh no!"
    tate "I've {i}got{/i} to get that hat back!"
    show tate shock flipped at left with MoveTransition(0.25)
    tate "Mr. Conductor! We've got trouble!"
    amtrak_conductor "Sorry, Tate. I'm a little {i}busy.{/i}"
    amtrak_conductor "Where is Mean?"
    show tate cry flipped
    tate "{i}I-{w=0.1}I don't know!"
    amtrak_conductor "What do you mean you {i}don't know?{/i} He was just in there."
    tate "I don't know, okay?! He's just {i}not{/i} in here!"
    tate "I'll go find CS and Arc! They're the only other people who might have seen him!"
    amtrak_conductor "That's probably the first good idea you've had all day."
    show tate sheepish flipped
    tate "Uweh?"
    amtrak_conductor "Go find another staff member if you can, too. I'll be with you shortly."
    tate "Yes, sir!"
    show tate at offscreenright with moveoutright
    pause 2.0
    play sound "sfx_fart_lite.mp3"
    with hpunch
    with hpunch
    pause 2.0
    amtrak_conductor "I guess it's time to switch protein shake brands..."
    pause 0.5
    scene black with fade
    pause 1.0

label train_confront_lupin:
    tate "Sorry. Mean and I haven't written this yet."
    mean "Yeah, sorry. Come back later, ya bozo."

######## GO HOME ########
label train_return_home_transition:
    scene moynihan_interior with fade

    # TODO: add mean's chosen BGM here :D

    n "The two finally deboard the train in New York City."
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
    play music "<loop 0>mm_select.mp3" volume 0.3
    music Mm Select - Matthew Simmonds
    show billy at right
    show cs
    billy "Need a ride? I'll take you to any destination for only $19.95!"
    show arceus happy flipped
    arceus "Welp, CS, we've found our other option!"

    # Did you play the whole route?
    if train_skip_at_chicago == False:
        if train_money_stolen == True:
            show bag at mid_mid_right with dissolve
            n "Arceus unzips the body bag and hands Billy a fistful of cash."
            show arceus flipped
            arceus "You think this will do the job?"
            billy "Wow! This totally doesn't look suspicious at all!"
            cs "We'll give you another $100 if you don't tell anyone."
            billy "That's cash in the trash!"
            hide bag with dissolve
        else:
            show case at mid_mid_right with dissolve
            n "Arceus opens the briefcase and gives Billy a gold bar."
            show arceus flipped
            arceus "You think this will do the job?"
            billy "Wow! You should save your money!"
            cs "We've got plenty more where that came from. You can keep it."
            billy "That's cash in the trash!"
            hide case with dissolve
    # Did you skip out before Chicago?
    else:
        show arceus
        n "CS and Arceus rummage around in their pockets and manage to scrounge together $19.95."
        show arceus flipped
        cs "Here you go!"
        billy "Thank you! Every Uber ride comes with my 100-percent satisfaction guarantee, or your money back!"        

    billy "Well, then! Where are we going?"
    n "CS tells Billy his address. The group then heads down to the parking lot to begin the final leg home."
    hide cs
    hide arceus flipped
    hide billy
    with moveoutright
    stop music fadeout 3.0
    music end
    jump back_home_alt
