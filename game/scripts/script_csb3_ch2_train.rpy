# TODO: find someone who can make these bgms actually properly loop. i don't know where to find looped versions...

label train_start_good:
    # variable for use in train route.
    $ money_stolen = False

    cs "We should head back home now. I have a plan for our newfound riches."
    show arceus happy flipped
    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"
    show cs flipped
    show arceus flipped
    pause 2.0
    n "{w=1}..."
    pause 1.0
    show cs flipped
    show arceus worried flipped
    pause 2.0
    arceus "...But, how {i}will{/i} we get back, exactly?"
    arceus "That's a pretty long drive. {w=0.25}I'm already beat."
    cs "I saw some signs for an airport really clo--{nw}"
    show arceus angry flipped
    show cs disappointed flipped
    arceus "Dude, {i}no.{/i}"
    arceus "We are {i}not{/i} flying. {w=0.5}I hate flying."
    show arceus worried flipped
    arceus "We've already been through enough, man..."
    cs "Well, if you don't want to drive, {w=0.25}and you don't want to fly..."
    cs "What else is there?"
    cs "Like... {w=0.5} a {i}train,{/i} or something?"
    show arceus flipped
    pause 2.0
    n "Arceus thinks for a moment."
    pause 2.0
    arceus "Actually... {w=0.25}yeah."
    pause 2.0
    show arceus happy flipped 
    arceus "...Yeah!"
    arceus "That sounds like a great idea!"
    arceus "We could just relax and watch the world go by!"
    arceus "Nobody has to drive, {w=0.25}we won't have to worry about finding rest stops, {w=0.25}{i}and{/i} I won't have a panic attack inside of a flying metal tube!"
    cs "I dunno... {w=0.25}How long would it take, though? {w=0.25}A flight would only be a few hours."
    cs "Don't trains have to stop a lot? {w=0.25}Wouldn't it be more expensive, too?"
    show arceus worried flipped 
    arceus "Come {i}on,{/i} man! {w=0.25}I just want to unwind!"
    arceus "We don't even need to worry about how much it'll cost, remember?"
    show arceus happy flipped 
    arceus "We're filthy stinkin' {i}rich!{/i}"
    n "CS can sense that Arceus probably won't take \"no\" for an answer."
    cs "Well... {w=0.5}I suppose we {i}do{/i} have all the money we could ever need, {w=0.25}and we don't really have any reason to rush getting home..."
    show cs surprised flipped 
    cs "And I've never been on a cross-country train before..."
    show cs happy flipped
    cs "Yeah, you know what? {w=0.25}Let's do it!"
    arceus "Let's go!"

    show cs happy
    show arceus flipped
    pause 0.25

    hide arceus
    hide cs
    with moveoutright

    scene black with fade

    n "CS and Arceus hop back in the car and drive to the nearest train station."

    jump train_route_begin

label train_start_bad:
    # variable for use in train route.
    $ money_stolen = True

    cs "We should head back home now. I have a plan for our newfound riches."
    show arceus happy flipped
    arceus "Alright! I'm excited to see what you've got cooking up!"
    arceus "Let's get going!"
    show cs
    show arceus flipped
    pause 2.0
    n "{w=1}..."
    pause 1.0
    show cs
    show arceus worried
    pause 2.0
    arceus "...But, how {i}will{/i} we get back, exactly?"
    arceus "That's a pretty long drive. {w=0.25}I'm already beat."
    cs "I saw some signs for an airport really clo--{nw}"
    show arceus angry
    show cs disappointed
    arceus "Dude, {i}no.{/i}"
    arceus "We are {i}not{/i} flying. {w=0.5}I hate flying."
    show arceus worried
    arceus "We've already been through enough, man..."
    cs "Well, if you don't want to drive, {w=0.25}and you don't want to fly..."
    cs "What else is there?"
    cs "Like... {w=0.5} a {i}train,{/i} or something?"
    show arceus
    pause 2.0
    n "Arceus thinks for a moment."
    pause 2.0
    arceus "Actually... {w=0.25}yeah."
    pause 2.0
    show arceus happy
    arceus "...Yeah!"
    arceus "That sounds like a great idea!"
    arceus "We could just relax and watch the world go by!"
    arceus "Nobody has to drive, {w=0.25}we won't have to worry about finding rest stops, {w=0.25}{i}and{/i} I won't have a panic attack inside of a flying metal tube!"
    cs "I dunno... {w=0.25}How long would it take, though? {w=0.25}A flight would only be a few hours."
    cs "Don't trains have to stop a lot? {w=0.25}Wouldn't it be more expensive, too?"
    show arceus worried
    arceus "Come {i}on,{/i} man! {w=0.25}I just want to unwind!"
    arceus "We don't even need to worry about how much it'll cost, remember?"
    show arceus happy
    arceus "We're filthy stinkin' {i}rich!{/i}"
    n "CS can sense that Arceus probably won't take \"no\" for an answer."
    cs "Well... {w=0.5}I suppose we {i}do{/i} have all the money we could ever need, {w=0.25}and we don't really have any reason to rush getting home..."
    show cs surprised
    cs "And I've never been on a cross-country train before..."
    show cs happy
    cs "Yeah, you know what? {w=0.25}Let's do it!"
    arceus "Let's go!"

    show cs
    show arceus flipped
    pause 0.25

    hide arceus
    hide cs
    with moveoutright

    scene black with fade

    n "CS and Arceus hop back in the car and drive to the nearest train station."

    jump train_route_begin

label train_route_begin:

    n "A little over an hour later, the two arrive at Kingman Amtrak Station."

    scene kingman_exterior
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2
    with fade

    play music "<loop 0>outdoors.mp3" volume 1
    music Outdoors - Miki Obata

    pause 1.0

    arceus "Welp, here we are!"
    show cs disappointed
    cs "...Wait, {i}this{/i} is the train station?"
    arceus "Well, yeah."
    arceus "What were you expecting?"
    cs "It's just-- {w=0.25}I dunno, I guess I expected something... {w=0.25}bigger? {w=0.25}Fancier?"
    arceus "I mean, Kingman is a tiny-ass town. It would be pretty weird to have a massive station here."
    cs "I guess that makes sense."
    arceus "We should probably get going soon, though. The train only even comes through here once a day."
    show cs worried
    cs "Oh, shit. Alright."

    scene black with fade

    if money_stolen == True:
        $ money_container = "bag"
        $ money_stolen_dialogue_switch = "zip it up"
    elif money_stolen == False:
        $ money_container = "briefcase"
        $ money_stolen_dialogue_switch = "latch it shut"
    else:
        $ money_container = "treasure chest"
        $ money_stolen_dialogue_switch = "lock it shut"

    n "CS and Arceus get out of the car and grab the [money_container] of money."

    scene kingman_exterior with fade

    show cs flipped at left
    show arceus at right
    with moveinright

    pause 2.0
    show cs
    pause 1.0

    cs "Oh, right."
    cs "I guess we won't be needing this for a while."
    play sound "audio/lego_break.WAV"
    n "CS quickly deconstructs the Lego car. He shoves the colorful little bricks into the [money_container] for later."
    n "The [money_container] is now full to bursting, but CS just barely manages to [money_stolen_dialogue_switch]."
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
    n "To their surprise, the place is desolate."
    cs "Hello? {w=0.5}Is anyone here?"
    pause 1.0
    show cs disappointed
    pause 2.0
    show arceus 
    arceus "Yeah, uh, remember what I said about this town being small? {w=0.25}This station is unmanned."
    arceus "We can buy tickets on the train once it gets here, though."
    cs "Wow, okay. How long until the train is here, then?"
    show arceus flipped at mid_right with moveinright
    n "CS notices Arceus' gaze land upon a board displaying the timetable."
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
    arceus "Yeah, well, we're not like the UK."
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
    
    cs "... Man, that's some bad luck, though. What are the odds of this place burning down {i}twice?!{/i}"
    show arceus
    arceus "I mean, back then, trains were powered by steam."
    arceus "Like, do you know what happens if you open a pressure cooker too early?"
    show cs disappointed
    cs "It... {w=0.25}{i}explodes,{/i}{w=0.25} right?"
    arceus "Yeah. It's pretty much the same concept."
    arceus "You crash a steam engine, you end up with this huge pressure differential, then you get a big {i}boom.{/i}"
    show cs worried
    cs "Yikes. Glad that's not the case nowadays."
    show arceus worried
    arceus "Yeah. It's also a big part of why planes are so scary for me. There are pressure differences at play there, too."
    arceus "If some jackass were to open the emergency exit in midair, or something, well…{w=0.5} there's really no surviving something like that."
    show cs scared
    cs "Shit, I guess I've never really thought about that…"
    arceus "Yeah, and if you have a lunatic like that on a fucking {i}plane,{/i} it's not like you can just… {w=0.25}throw them overboard and keep going."
    show cs disappointed
    cs "\"Overboard\"? {w=0.25}Wait, isn't that term only used for boats?"
    show arceus angry
    arceus "Man, I don't know what word you'd use for throwing someone off of a plane."
    arceus "That's not even a thing you can {i}do.{/i}"
    arceus "How can a word exist for a thing that's impossible?"
    show arceus
    show cs surprised
    arceus "Anyway, do you remember that news story about the guy who got duct-taped to his seat during a flight?"
    show arceus worried
    show cs disappointed
    arceus "... {w=0.5}Yeah. {w=0.5}That's about the {i}only{/i} thing they could have done to protect themselves and everyone else."
    show cs worried
    cs "Damn, I'd forgotten all about that!"
    cs "What would have happened if it had been on a train?"
    show arceus angry

    # TODO: polar express reference

    arceus "I dunno, man. I'm just gonna assume that they'd kick the bastard off at the next station."
    arceus "I really don't want to think about someone like that being on {i}our--{/i}"
    stop music fadeout 3.0
    music end
    show cs
    show arceus flipped
    play sound "audio/amtrak_horn.wav"
    n "The conversation is interrupted by the blare of a train horn."
   
    # TODO: i need a similar image but less crunchy

    scene kingman_train_arrive with fade
    play music "<loop 0>ochre_woods_day.mp3" volume 0.8
    music Ochre Woods ~ Day - Miki Obata
    n "The two watch as the locomotive approaches the station and eventually slows to a stop."
    hide cs
    hide arceus

    scene amtrak_arrive_close with fade

    show arceus flipped at mid_mid_left
    show cs at left
    with moveinleft

    arceus "Welp, there it is."
    n "The two wait a few moments before boarding while the incoming passengers exit the train."
    pause 2.0
    tate_offscreen "{bt=a3-p10-s4}{size=+24}Alllllll aboarrrrrrd!!" with hpunch
    cs "Welp, I guess that's our--{nw}"
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
    tate "I'm Tate. I'm CS's--{w=0.5} uh... "
    show tate sheepish flipped
    tate "Um... {w=1.0}friend. {w=0.25}Yes."
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
    tate "We don't wanna end up stranded here. This train only comes through once a day, after all!"

    show cs at mid_offscreen_left
    show arceus flipped at left
    show tate at center
    show amtrak_conductor at right
    with moveinright

    amtrak_conductor "All aboard!"
    show cs disappointed
    cs "... Wait, I thought you already called for everyone to board, Tate?"
    show arceus worried flipped
    arceus "Yeah, and why aren't you in uniform?"
    show tate sheepish flipped
    tate "Hah, I don't actually work for Amtrak. I just try to help where I can."
    show tate smug flipped
    tate "Also, I kinda just wanted to do the funny."
    amtrak_conductor "Yeah, {w=0.1}don't do that."
    show tate sheepish
    pause 1.0
    amtrak_conductor "You're on thin ice anyway after what happened in the dining car."
    tate "But, I just wanted--{nw}"
    amtrak_conductor "The {i}only{/i} reason why you're still on this train is because the new guy won't let us kick you off."
    tate "Listen, I was just trying to he--{nw}"
    amtrak_conductor "Yeah, {w=0.25}well, {w=0.25}{i}don't."
    amtrak_conductor "Or we'll leave {i}both{/i} of you at the next station."
    show tate sad
    tate "Yes, sir..."
    amtrak_conductor "Let's get a move on."

    show amtrak_conductor flipped
    pause 0.5
    hide amtrak_conductor with moveoutright
    pause 1.0

    hide tate
    hide cs
    hide arceus
    with moveoutright

    stop music fadeout 3.0
    music end
    scene black with fade
    n "The group boards the train."
    n "CS and Arceus buy tickets from the staff on board."
    n "From there, the trio heads towards the sleeper cars."

label train_boarding:

    scene amtrak_sleeper_corridor
    with fade

    play music "<loop 0>bedroom_day.mp3" volume 0.5
    music Bedroom ~ Day - Miki Obata
    
    # TODO: amtrak stewardess sprite leading the group.
    show amtrak_stewardess at right
    show tate at mid_mid_right
    show cs at left
    show arceus flipped at mid_mid_left
    with moveinleft

    pause 1.0
    show tate flipped
    pause 1.0
    tate "... And, {i}this{/i} way is the sleeper car! {w=0.25}Your room is--{w=0.25}{nw}"
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
    amtrak_stewardess "{size=-10}Or, why don't {i}you{/i} have a nap, too? {w=0.5}Do you {i}ever{/i} sleep?"
    tate "Oh... {w=0.25}yeah."
    tate "Sorry."
    tate "I guess it {i}has{/i} been a while since I've seen CS. I can stay here for a bit..."
    show tate sheepish flipped
    tate "... if you're okay with that."
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
    show amtrak_stewardess flipped at right with moveinright

    show tate sheepish
    amtrak_stewardess "I {i}mean{/i} it, Tate."
    amtrak_stewardess "Be good."
    tate "Yes, ma'am..."    
    show amtrak_stewardess
    pause 0.25
    hide amtrak_stewardess with moveoutright
    pause 1.0
    n "The stewardess returns to work."
    pause 2.0

    show cs disappointed at mid_mid_left 
    with moveinright
    pause 1.0

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
    cs "... {w=0.5}Yeah, {w=0.25}that tracks."
    show cs disappointed
    cs "You always {i}were{/i} a little..."
    n "..."
    pause 2.0
    show tate srs flipped
    tate "A little...?"
    show cs worried
    cs "Just a little, uh--{nw}"

    # TODO: need a sprite for the thief.

    show cs scared at mid_offscreen_left with hpunch
    show tate shock flipped
    show cs concentrate
    show tate shock flipped at right with moveinright
    n "CS is knocked to the ground as a stranger sprints down the corridor!"
    unknown "Sorry, cat dude! I've gotta {i}run!"
    tate "Oh my God! Are you alright?!"
    cs "Yeah..."
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
    
    # TODO: I need a better picture than this...
    show amtrak_sleeper_interior_day
    show arceus at right
    with fade

    n "CS and Tate enter the sleeper unit just as the train starts moving."

    show tate at mid_mid_left
    show cs at left
    with moveinleft

    show arceus worried
    arceus "Hey, guys. Sorry about that. I think something I ate at that creepy-ass pizza place didn't quite agree with me."
    show cs disappointed
    show tate stare
    cs "Damn. Are you feeling any better?"
    show arceus
    arceus "Oh, yeah. I think I'll be alright now."
    show cs
    show tate
    cs "That's good to hear."   
    show tate stare
    tate "Oh, yeah! Let me know if y'all need more toilet paper, {w=0.25}or soap, or... {w=0.25}anything."
    show cs disappointed
    cs "...{w=0.5} Shouldn't we be asking the {i}staff?"
    show tate shock flipped
    pause 1.0
    show tate sad flipped
    pause 0.5
    tate "{w=0.5}...{w=0.5}Yes. {w=0.25}Yes, you should."
    show tate sad
    n "Tate sheepishly looks down at the floor."
    show arceus worried
    arceus "So, uh..."
    arceus "Hey, Tate, how do you know CS, anyway?"
    show tate sheepish
    tate "Oh, uh..."
    tate "We met a few years ago, back when Mixer was a thing."
    show cs
    cs "You might remember it as Beam, Arc."
    show arceus happy
    arceus "Oh, yeah! {w=0.25}Damn, {i}Beam?"
    show tate
    arceus "Now {i}that's{/i} a name I haven't heard in a while!"
    show cs disappointed
    show arceus
    cs "Yeah. It's a real shame that Microsoft eventually kills off every product I like."
    show tate flipped   
    tate "Yeah, it really is."
    tate "But, you're not still shilling for them now, though, right?"
    "..."
    show tate sheepish flipped
    tate "... {w=0.25}Right?"

    stop music fadeout 3.0
    music end

    show cs scared
    show tate shock flipped
    show arceus worried
    with shake2
    play sound "audio/hard_knock.mp3"

    n "A sudden hard knock on the door startles the group."
    # TODO: sfx - angry crowd fade in
    n "An uproar of angry passengers grows steadily louder."

    play music "<loop 0>item_bounce.mp3" volume 0.6
    music Item Bounce - Akira Miyagawa

    cs "What the hell?!"
    tate "No, no, {i}no!"
    tate "This can't be good!"
    arceus "So much for a relaxing trip..."
    n "The door is slid open with a heavy hand."
    
    play sound "audio/sliding_door_open.mp3"
    pause 1.0
    
    show cs scared flipped at mid_mid_right
    show tate shock flipped at right
    show arceus worried at mid_offscreen_right
    with moveinright

    show amtrak_conductor flipped at left
    with moveinleft
    
    amtrak_conductor "Alright every--{w=0.5}{nw}"
    amtrak_conductor "Oh. {w=1.0}{i}Tate."
    tate "I {i}swear,{/i} sir! {w=0.5}Whatever happened just now, {w=0.25}I had {i}nothing{/i} to do with it!"
    tate "I've been in this room! {w=0.25}Just talking with CS, here!"
    show cs happy flipped
    cs "Hey guys, CS here!"
    amtrak_conductor "Huh?{w=0.5}{nw}"
    show tate srs flipped
    show arceus angry
    tate "{i}Why.{w=0.5}{nw}"
    show cs scared flipped
    cs "{i}Ahem{w=0.25}{nw}"
    show cs flipped
    show tate sheepish flipped
    show arceus
    cs "I mean, {w=0.25}uh, {w=0.25}yes. {w=0.5}Tate was here the entire time."
    arceus "Yep, Tate has been with us since we got on the train."
    amtrak_conductor "Oh, really?"
    amtrak_conductor "Well, if they are bothering you, I can take care of them for you."
    show tate shock flipped
    tate "Eep!"
    show cs happy flipped
    show tate sheepish flipped
    cs "Oh, no, not at all!"
    show cs flipped
    cs "Tate and I have known each other for years. We were just catching up."
    amtrak_conductor "Well, alright."
    show arceus worried
    arceus "May I ask what is going on out there? The noise kinda scared us."
    show amtrak_conductor
    amtrak_npc_1 "Hey, my watch is gone, too!"
    amtrak_npc_2 "Man, {i}fuck{/i} your watch! They took my damn {i}Switch!{/i}"
    amtrak_npc_3 "Such {i}language!"
    amtrak_npc_3 "My dearest mother's priceless brooch is also missing, and you don't hear {i}me{/i} speaking like an utter {i}barbarian!"
    n "The complaints of a few more distraught travelers echo throughout the car."
    show amtrak_conductor at mid_offscreen_left with moveinleft
    amtrak_conductor "Please remain calm, everyone! {w=0.25}We will find out who the thief is, {w=0.25}and they {i}will{/i} be brought to justice!"
    amtrak_conductor "Please return to your rooms! {w=0.25}We will have an update for you as early as possible!"
    n "One by one, the disgruntled passengers return to their units."
    pause 1.0
    show amtrak_conductor flipped at left with moveinright
    pause 1.0
    amtrak_conductor "... {w=0.25}As you can probably tell, a lot of passengers have been victims of theft. "
    amtrak_conductor "Are any of you missing valuables?"
    show arceus worried
    arceus "I mean, all we had was the one [money_container]."
    pause 0.5
    arceus "... {w=0.5}CS, where is the [money_container]?"
    show cs worried
    cs "I thought {i}you{/i} had it?"

    # TODO: sprites looking around every which way

    show cs worried
    cs "Oh."
    show cs scared
    cs "Shit."

    if money_stolen == True:
        $ money_stolen_dialogue_switch = "black bag"
        $ money_stolen_dialogue_switch_2 = "\n... {w=0.5}won"
    elif money_stolen == False:
        $ money_stolen_dialogue_switch = "metal briefcase"
        $ money_stolen_dialogue_switch_2 = " won"
    else:
        $ money_stolen_dialogue_switch = "red and gold treasure chest"
        $ money_stolen_dialogue_switch_2 = " totally plundered"


    show cs disappointed flipped
    cs "Yes, sir, we're missing a single [money_stolen_dialogue_switch] filled with money we[money_stolen_dialogue_switch_2] while we were in Vegas."
    show arceus angry
    arceus "... And Lego bricks." 
    show cs surprised
    cs "And Legos, yes."
    show tate srs flipped
    tate "Wait, so..."
    tate "You got rich in Vegas, {w=0.25}and the first thing you did was buy {i}Legos?"
    show cs worried
    cs "Well, no--{w=0.25}{nw}"
    tate "I suppose I shouldn't have expected anything else from you."
    show cs disappointed
    cs "That's not what--{w=0.25}{nw}"
    show cs disappointed flipped
    amtrak_conductor "Thank you, sir. We'll keep an eye out for your things."
    show tate sheepish flipped
    amtrak_conductor "Tate. {w=0.5}You'd better behave. {w=0.5}Stay out of the way during this investigation."
    show tate sad flipped
    tate "Yes, sir."
    tate "I'll probably just keep chatting with CS until Mean wakes up."
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

    play sound "audio/sliding_door_close.mp3"
    n "The conductor leaves to return to his duties."
    tate "I can't believe this..."
    arceus "Me, neither. All of that money, just... {w=0.25}{i}gone..."
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
    tate "It's just that... {w=0.5}he's got enough to worry about, since today will be his first official shift as the night driver..."
    tate "I really don't want him dealing with something like this on his first day."
    show tate sheepish flipped
    tate "I just feel like I have to do {i}something."
    cs "Don't you think you've done enough already?"
    show tate srs flipped
    tate "What do you mean?"
    show cs worried
    cs "The conductor and that attendant both seemed really annoyed with you."
    show cs surprised
    cs "I {i}know{/i} how you work, Tate."
    cs "I really think that sometimes you need to just... \n{w=0.25}let {w=0.25}things {w=0.25}{i}happen."
    show tate shock flipped
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
    cs "Exaaaaactly. {w=0.25}Just let things happen."
    show tate srs flipped
    tate "How can you be so... {i}unbothered{/i} by all of this? {w=0.25}And after you just lost so much money?!"
    show arceus worried
    arceus "{size=-10}Well, {i}I'm{/i} bothered by it..."
    show cs worried
    cs "I mean, yeah, it totally sucks balls, but all it means is that when we get home, things will just be the same as they were before."
    show tate sheepish flipped
    tate "I really do hope they find everyone's things.."
    show tate sad flipped
    tate "I'm just so scared that they'll accuse Mean of stealing it, or something."
    
    # TODO: An extra-sad tate sprite, on the verge of tears
    
    tate "I really don't know if he could handle losing this job, too."
    show cs disappointed
    cs "Wait, what happened at his last job?"
    show tate srs flipped
    tate "It was so fucking stupid."
    tate "So, he was working for this home repair company, right? {w=0.25}They made him a security guard, since he's all spiky--{w=0.25}{nw}"
    show arceus 
    arceus "{i}Spiky?{/i} {w=0.25}Wha--{w=0.25}{nw}"

    # TODO: can we replace "pushed" to reference whichever attack was used in CSBII?

    tate "--and then some weirdo dressed as a catgirl maid broke in and fought the CEO! {w=0.25}A lot of people got hurt!"
    show tate shock flipped
    show cs worried
    show arceus worried
    tate "I think Mean said that someone even got pushed off of the roof!"
    show tate sheepish flipped
    tate "But since Mean couldn't... {w=0.5}{size=-5}hold him off... {w=1.0}{size=-5}he was... {w=1.5}{size=-5}fired..."
    pause 1.0
    show tate shock flipped
    n "Tate goes silent. They stare wide-eyed at CS' outfit."
    tate "..."
    pause 2.0
    show cs scared
    cs "... Woah, Tate, why are you look--{w=0.25}{nw}"
    
    # TODO: tate needs a FURIOUS sprite

    show tate srs flipped
    tate "{bt=a3-p10-s4}{size=+36}IT WAS {i}YOU!!"
    cs "Wha-- {i}huh?!"
    tate "CS, WHAT THE {i}FUCK?!"
    tate "{i}YOU{/i} BROKE INTO HOH SIS?!"
    show cs worried
    "Oh, yeah, uh--{w=0.25}{nw}"
    
    show tate sad flipped
    n "Tate is on the verge of tears."
    tate "My best friend lost his job, {w=0.25}and it's your fault..."
    tate "And now, {w=0.25}you're {i}here..."
    tate "I can't believe this..."
    show cs disappointed
    cs "Tate..."
    cs "Listen to me, please--{nw}"
    show tate srs flipped
    tate "{i}No!"
    tate "I don't want to hear it!"
    tate "Is {i}this{/i} what you've been up to since we--{w=0.25}{nw}"
    tate "..."
    tate "You know what, no."
    tate "Fuck this shit."
    tate "Mean's shift starts soon. {w=0.25}I need to be there for him."
    tate "If either of y'all see him, you will not breathe a word of {i}any{/i} of this to him."
    tate "Not about the thefts, {w=0.25}and certainly not about what happened at HoH SiS."
    tate "He doesn't need this. {w=0.25}Especially not today."
    show cs worried
    n "Tate reinforces their demand with a piercing glare towards CS."
    show tate srs
    n "Tate then suddenly stands up." with vpunch
    tate "I'm sorry."
    tate "I need to go."
    show tate sad flipped
    pause 0.25
    hide tate with moveoutleft
    play sound "audio/sliding_door_open.mp3"
    n "Tate swiftly exits the sleeper car and runs off, not even bothering to shut the door behind them."
    n "CS looks distraught."
    pause 2.0
    show cs disappointed
    cs "... {w=0.25}Fuck."
    arceus "You alright, man?"
    cs "I will be. I'm just worried about Tate."
    cs "I don't even remember the last time they were so upset."
    cs "I'm also really tired... I think I could use some rest."
    show arceus
    arceus "Yeah, same. I'm really glad we sprung for the private room."
    show arceus happy
    arceus "These beds are looking pretty good right now."
    show cs
    cs "They {i}do{/i} look nice."
    show cs happy
    cs "I think that tomorrow, {w=0.25}we'll wake up, {w=0.25}someone will have found our cash overnight, {w=0.25}Tate will have had some time to cool off, {w=0.25}we'll all get together and have a huge complimentary breakfast..."
    cs "... and all will be right with the world!"

    # TODO: some funny cheery fanfare jingle?

    show arceus angry
    arceus "... {i}I{/i} think you're being way too optimistic about all of this."
    arceus "I'm going to bed."
    show cs disappointed
    cs "Yeah, I think I should, too..."

    scene black with fade
    n "CS and Arceus decide to call it an early night."
    n "CS easily falls into a deep slumber."
    n "While the train bed is indeed quite comfortable, Arceus struggles to get any rest."


    # TODO: better bg image

    scene amtrak_sleeper_interior_night
    with fade
    pause 1.0
    arceus "Fuck..."
    arceus "I'm so tired, but I {i}still{/i} can't fucking sleep..."
    arceus "I wonder if they have booze on this train."

    show arceus dark at center with dissolve
    n "Arceus quietly gets out of bed, being careful not to wake CS."
    hide arceus with moveoutleft
    play sound "audio/sliding_door_open.mp3"
    pause 2.0
    n "He gently shuts the door behind him, then makes for the dining car in hopes of drinking his worries away."
    play sound "audio/sliding_door_close.mp3"

    scene black with fade
    pause 2.0

label train_dining:

    scene amtrak_dining_car
    with fade
    pause 1.0

    play music "<loop 0>krabby_klub.mp3" volume 0.6
    music Krabby Klub - Tsukasa Tawada
    
    show arceus at center with moveinright

    n "Arceus arrives at the dining car. The aromas of so many different foods mingling together overwhelm his canine senses."
    arceus "Geez, it smells like a high school cafeteria..."
    arceus "I think I'll just grab a bottle of wine and get out of here."
    show arceus at left with moveinleft
    n "As he heads to the counter, Arceus finds his attention redirected towards a yellow... {w=0.5}thing."

    hide arceus
    scene amtrak_dining_mean
    show mean at t_mean_dining_car
    with fade

    n "A strange spiny entity is surrounded by piles of pancakes, {w=0.25}sky-high stacks of sausages, {w=0.25}oodles of eggs, {w=0.25}and a whole bunch of bacon."
    n "Arceus can't help but stare in awe at both the enormous spread of food..."
    n "... and at the brightly-colored creature currently demolishing it."
    show mean happy
    mean "Let's fucking {i}gooooo!{/i}"
    mean "I can't believe they made {i}all{/i} of this just for me!"
    mean "This is going to be the best day {i}ever!"
    show mean happy2
    n "The sunny little spikeball scarfs down a sausage."
    show arceus at right with moveinright
    with determination
    show mean happy
    arceus "Damn..."
    arceus "Wow, uh, excuse me. I have to ask..."
    show mean
    mean "Hm?"
    show mean happy2
    n "The buttery ball of barbs bites into some bacon."
    show mean happy
    show arceus worried
    arceus "It's... uh... getting pretty late. How can you possibly eat all of that so close to bed?"
    mean "{i}Crunch, chew...{w=0.25}{nw}"
    mean "Oh, no!"
    mean "{i}Gulp!{w=0.25}{nw}"
    show mean
    mean "I just woke up, actually."
    mean "Today's a big day, so my friend made me this massive breakfast to celebrate!"
    show mean happy2
    n "The popcorn-colored pincushion prepares to pursue another pancake."
    show mean happy
    arceus "Oh, wait! You've been asleep all day?"
    mean "{i}Munch, munch...{w=0.25}{nw}"
    mean "Yeah! Shift work... {w=0.25}you know how it goes."
    arceus "That, I do..."
    arceus "It's just that, uh..."
    arceus "If you've been asleep..."
    arceus "Have you heard about what happened?"
    mean "{i}Gulp.{w=0.25}{nw}"
    show mean ayo
    mean "No...?"
    arceus "Well, uh... are you missing anything? Especially anything valuable?"
    mean "Nah, I didn't even bring anythin--{nw}"
    show mean wat
    stop music fadeout 3.0
    music end
    "..."
    mean "Wait."
    show mean angry 
    with Dissolve(1.0)
    # the dissolve was arc's idea lol
    mean "Why?"
    arceus "We had some stuff stolen. A lot of people did, actual--{nw}"

    # mean wanted the following section.
    
    play music "<loop 0>odd_one_out.mp3" volume 0.6
    music Odd One Out - Miki Obata

    show mean furious
    mean "{i}WHAT?!" with hpunch
    mean "{bt=a3-p10-s4}{size=+36}ON {i}MY{/i} FUCKING TRAIN?!" with vpunch
    mean "MY FIRST SHIFT STARTS IN {bt=a3-p10-s4}{i}TWENTY MINUTES!" with hpunch
    n "One can practically see the gears begin to turn in Arceus' head as he realizes who he is talking to."

    # arc wanted this
    if fun_value(10):
        show arceus
        arceus "Wait, hey, can you do a Dallas impression?"
        show mean wat
        mean "Like this?"
        show mean furious
        mean "{bt=a3-p10-s4}AUUUUUUUUUGH!!" with hpunch
        show arceus happy
        arceus "Yeah!"

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
    pause 2.0
    n "Arceus, visibly shaken, leaves as well, without even getting the drink he came for."

    # fun value
    if fun_value(5):
        n "He did at least steal a few of the abandoned pancakes."

    n "He gets back to the sleeper car as quickly as he can."
    hide arceus with moveoutright
    scene black with fade
    
label train_wakeup:

    scene amtrak_sleeper_interior_night
    with fade
    play sound "audio/sliding_door_open.mp3"
    pause 1.0
    show arceus worried dark flipped at center with moveinleft
    pause 1.0
    arceus "CS!"
    play sound "audio/sliding_door_close.mp3"
    arceus "Wake up!"
    cs "Hnnnh... {w=0.5}huh?"
    n "Arceus flips on the lights."
    play sound "audio/lightswitch.wav"
    show amtrak_sleeper_interior_day
    hide arceus
    show arceus worried flipped
    pause 1.0
    n "CS lets out a groan and rolls back over in bed."
    show arceus angry flipped
    cs "Zzzzz..."
    cs "{size=-12}Five more minutes, mom..."
    show arceus angry flipped at right with moveinleft
    n "Arceus pulls the blanket off of CS and drags him out of bed."

    show arceus angry flipped at center
    show cs concentrate flipped at right
    with moveinright
    
    cs "Hnngh, {w=0.25}huh, {w=0.25}what, {w=0.25}why?!"
    show cs disappointed flipped
    cs "Wha-- {w=0.05}What's going on?"
    pause 1.0
    n "CS notices Arceus is out of breath and panicking."
    show cs worried flipped
    cs "Wait, Arc, what's wrong?"
    cs "Are you alright?"
    show arceus worried flipped
    arceus "Dude, I fucked up!"
    arceus "I went to the dining car for a drink, and there was this... {w=0.5}{i}thing{/i} eating an insane amount of food, and I went to talk to him!"
    arceus "He was asleep all day and didn't know about the thief, so I asked him if he's missing anything--{w=0.25}{nw}"
    arceus "That {i}thing{/i} was Mean!"
    show cs surprised flipped
    cs "Wait, {w=0.25}he was mean to you? {w=0.5}What'd he do?"
    show cs worried flipped
    show arceus angry flipped
    cs "Are you okay?"
    arceus "No!"
    arceus "He's Tate's friend, {i}Mean!"
    arceus "The new night driver!"
    show cs scared flipped
    pause 0.5
    cs "{w=0.25}... Oh no."
    cs "We are {i}definitely{/i} in trouble n--{nw}"
    show arceus worried with hpunch
    music end
    n "As if on cue, the room door slides open."

    scene black
    show tate shock at center
    tate "{bt=a3-p10-s4}Awawawawa!"
    tate "Oh no! {w=0.25}You've reached the end of whatever's been programmed in already!"
    show tate srs
    tate "Tell IRL!Tate to finish the story!"
    show tate sheepish
    tate "Let's go back to the main menu for now."
