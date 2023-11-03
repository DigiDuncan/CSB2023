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
    show arceus at right behind cscar2
    with fade

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

    if money_stolen:
        $ money_container = "bag"
        $ money_stolen_dialogue_switch = "zip it up"
    else:
        $ money_container = "briefcase"
        $ money_stolen_dialogue_switch = "latch it shut"

    "CS and Arceus get out of the car and grab the {money_container} of money."

    show kingman_exterior
    with fade

    show cs flipped at left with moveinright
    show arceus at right with moveinright
    pause 2.0
    show cs

    cs "Oh, right. I guess we won't be needing this for a while."
    play sound "audio/lego_break.WAV"
    n "CS quickly deconstructs the Lego car. He shoves the colorful little bricks into the {money_container} for later."
    n "The {money_container} is now full to bursting, but CS just barely manages to {money_stolen_dialogue_switch}."
    show arceus worried
    pause 1.0
    arceus "... You still never explained to me how the fuck you did that."
    show cs happy
    cs "Like I said, I'm a master builder."
    show arceus angry
    arceus "Whatever, man. Let's just go."
    hide cs with moveoutleft
    hide arceus with moveoutleft
    scene black with fade
    
    


    show tate shock at center
    tate "{bt=a3-p10-s4}Awawawawa!"
    tate "Oh no! {w=0.25}You've reached the end of whatever's been programmed in already!"
    show tate srs
    tate "Tell IRL!Tate to finish the story!"
