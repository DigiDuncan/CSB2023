label train_start_good:
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
    arceus "Nobody has to drive, {w=0.25}we won’t have to worry about finding rest stops, {w=0.25}{i}and{/i} I won’t have a panic attack inside of a flying metal tube!"
    cs "I dunno... {w=0.25}How long would it take, though? {w=0.25}A flight would only be a few hours."
    cs "Don’t trains have to stop a lot? {w=0.25}Wouldn’t it be more expensive, too?"
    show arceus worried flipped 
    arceus "Come {i}on,{/i} man! {w=0.25}I just want to unwind!"
    arceus "We don’t even need to worry about how much it’ll cost, remember?"
    show arceus happy flipped 
    arceus "We're filthy stinkin' {i}rich!{/i}"
    n "CS can sense that Arceus probably won’t take \"no\" for an answer."
    cs "Well... {w=0.5}I suppose we {i}do{/i} have all the money we could ever need, {w=0.25}and we don’t really have any reason to rush getting home..."
    show cs surprised flipped 
    cs "And I’ve never been on a cross-country train before..."
    show cs happy flipped
    cs "Yeah, you know what? {w=0.25}Let’s do it!"
    arceus "Let's go!"

    show cs happy
    hide cs with moveoutright
    show arceus flipped
    hide arceus with moveoutright

    scene black with fade

    n "CS and Arceus hop back in the car and drive to the nearest train station."

    jump train_route_begin

label train_start_bad:
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
    arceus "Nobody has to drive, {w=0.25}we won’t have to worry about finding rest stops, {w=0.25}{i}and{/i} I won’t have a panic attack inside of a flying metal tube!"
    cs "I dunno... {w=0.25}How long would it take, though? {w=0.25}A flight would only be a few hours."
    cs "Don’t trains have to stop a lot? {w=0.25}Wouldn’t it be more expensive, too?"
    show arceus worried
    arceus "Come {i}on,{/i} man! {w=0.25}I just want to unwind!"
    arceus "We don’t even need to worry about how much it’ll cost, remember?"
    show arceus happy
    arceus "We're filthy stinkin' {i}rich!{/i}"
    n "CS can sense that Arceus probably won’t take \"no\" for an answer."
    cs "Well... {w=0.5}I suppose we {i}do{/i} have all the money we could ever need, {w=0.25}and we don’t really have any reason to rush getting home..."
    show cs surprised
    cs "And I’ve never been on a cross-country train before..."
    show cs happy
    cs "Yeah, you know what? {w=0.25}Let’s do it!"
    arceus "Let's go!"

    show cs
    hide cs with moveoutright
    show arceus flipped
    hide arceus with moveoutright

    scene black with fade

    n "CS and Arceus hop back in the car and drive to the nearest train station."

    jump train_route_begin

label train_route_begin:

    n "A little over an hour later, the two arrive at Kingman Amtrak Station."

    scene train_route_begin
    show kingman_exterior
    show cscar1
    show cscar2
    show cs at left behind cscar2
    show arceus at right behind cscar2 with fade

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

    # TODO: why doesn't this switch properly?!
    if money_stolen == True:
        $ money_container = "bag"
        $ money_stolen_dialogue_switch = "zip it up"
    else:
        $ money_container = "briefcase"
        $ money_stolen_dialogue_switch = "latch it shut"

    n "CS and Arceus get out of the car and grab the [money_container] of money."

    show kingman_exterior with fade

    show cs flipped at left with moveinright
    show arceus at right with moveinright
    pause 2.0
    show cs

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
    hide cs with moveoutleft
    hide arceus with moveoutleft
    scene black with fade

    show kingman_interior with fade

    show arceus flipped at center with moveinleft
    show cs at left with moveinleft

    n "CS and Arceus enter the train station."
    n "To their surprise, the place is desolate."
    cs "Hello? Is anyone here?"
    show cs disappointed
    show arceus 
    arceus "Yeah, uh, remember what I said about this town being small? This station is unmanned."
    arceus "We can buy tickets on the train once it gets here, though."
    cs "Wow, okay. How long until the train is here, then?"
    show arceus flipped at mid_right with moveinright
    n "CS notices Arceus' gaze land upon a board displaying the timetable."
    show cs disappointed at center with moveinright
    pause 2.0
    cs "Oh, right."
    cs "..."
    cs "So, we have a little under an hour."
    show arceus 
    arceus "Yep."
    cs "So, what do we do in the meantime? Is there anything here?"

    pause 2.0
    show cs disappointed flipped
    pause 1.0
    show arceus flipped
    pause 1.0
    show cs disappointed
    pause 1.0
    show arceus
    pause 1.0
    n "The two glance around the space for a moment."
    
    show kingman_museum with fade

    arceus "Looks like there's a little museum here. Wanna poke around there?"
    cs "I don't see why not. Not like we have anything else to do."
    arceus "Alrighty, let's go."
    scene black with fade
    n "CS and Arceus wander around the museum for a little while."
    n "There aren't many exhibits in such a small building, but there is just enough to look at to pass the remaining time."
    n "About five minutes before the train's expected arrival, the two make their way out onto to the platform."
    
    show kingman_platform_2 with fade

    show arceus flipped at mid_mid_left with moveinleft
    show cs at left with moveinleft
    
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
    arceus "How can a word exist for a thing that's {i}impossible?{/i}"
    show arceus
    show cs surprised
    arceus "Anyway, do you remember that news story about the guy who got duct-taped to his seat during a flight?"
    show arceus worried
    show cs disappointed
    arceus "... Yeah. That's about the {i}only{/i} thing they could have done to protect themselves and everyone else."
    show cs worried
    cs "Damn, I'd forgotten all about that!"
    cs "What would have happened if it had been on a train?"
    show arceus angry
    arceus "I dunno, man. I'm just gonna assume that they'd kick the bastard off at the next station."
    arceus "I really don't want to think about someone like that being on {i}our--{/i}"
    show cs
    show arceus flipped
    play music "<loop 0>ochre_woods_day.mp3" volume 0.8
    music Ochre Woods ~ Day - Miki Obata
    play sound "audio/amtrak_horn.wav"
    n "The conversation is interrupted by the blare of a train horn."
   
    show kingman_train_arrive with fade
    n "The two watch as the locomotive approaches the station, eventually slowing to a stop."
    hide cs
    hide arceus

    show amtrak_arrive_close with fade
    show arceus flipped at mid_mid_left with moveinleft
    show cs at left with moveinleft
    arceus "Welp, there it is."
    n "The two wait a few moments before boarding while the other passengers exit the train."
    pause 1.0
    tate_offscreen "{bt=a3-p10-s4}All aboard!"
    cs "Welp, I guess that’s our--{nw}"
    show tate flipped at right with moveinright
    pause 1.0
    show cs worried
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
    tate "A good friend of mine started a new job as a conductor for Amtrak, and asked me if I wanted to come with him for a while."
    tate "His first shift starts tonight, actually."
    show cs happy
    cs "Oh, cool!"
    n "Tate notices Arceus."
    tate "Oh, who's your friend?"
    cs "Oh, this is Arceus. He and I go way back."
    show cs
    show arceus happy flipped
    arceus "Hi, you can just call me Arc."  
    tate "Well, it's nice to meet ya, Arc."
    show arceus flipped
    tate "I'm Tate. I'm CS's--{w=0.5} uh... "
    show tate sheepish flipped
    tate "Um... {w=1.0} friend. {w=0.25} Yes."
    cs "Yeah! Of course we're friends."
    tate "Of course!"
    show arceus worried flipped
    n "Arceus raises an eyebrow at this interaction."
    n "He decides that maybe it's better not to ask."
    tate "A-Anyway. We should probably get going."
    show tate
    tate "We don't wanna be stranded here. This train only comes through once a day, after all!"
    show cs at mid_offscreen_left with moveinright
    show arceus flipped at left with moveinright
    show tate at center with moveinright

    # TODO: serious-looking amtrak conductor enters from right here, on right side of screen.

    amtrak_conductor "All aboard!"
    show cs disappointed
    cs "... Wait, I thought you already called for everyone to board, Tate?"
    show arceus worried flipped
    arceus "Yeah, and why aren't you in uniform?"
    show tate sheepish flipped
    tate "Hah, I don't actually work for Amtrak. I just try to help where I can."
    show tate smug flipped
    tate "Also, I kinda just wanted to do the funny."
    show tate sheepish
    amtrak_conductor "Yeah, don't do that."
    amtrak_conductor "You're on thin ice {i}anyway{/i} after what happened in the dining car."
    tate "But I just wanted--{nw}"
    amtrak_conductor "The only reason why you're still on this train is because the new guy won't let us kick you off."
    tate "Listen, I was just trying to he--{nw}"
    amtrak_conductor "Yeah, well, {i}don't."
    amtrak_conductor "Or we'll leave {i}both{/i} of you at the next station."
    show tate sad
    tate "Yes, sir..."

    scene black with fade
    n "The three all board the train."
    n "CS and Arceus buy tickets from the staff on board."

    # TODO: amtrak stewardess sprite leading the group.

    
    

    show tate shock at center
    tate "{bt=a3-p10-s4}Awawawawa!"
    tate "Oh no! {w=0.25}You've reached the end of whatever's been programmed in already!"
    show tate srs
    tate "Tell IRL!Tate to finish the story!"
    show tate
    tate "Let's go back to the main menu for now."
