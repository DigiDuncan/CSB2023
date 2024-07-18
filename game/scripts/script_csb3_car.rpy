screen skip_car():
    zorder 100
    layer "music"
    style_prefix "skip_car"

    frame at t_skip_car:
        imagebutton idle "images/skip_now.png" hover_sound "sfx_select.ogg":
            action Play("sound", "sfx_valid.ogg"), Hide("skip_car", Fade(1.0)), Jump("back_home")

transform t_skip_car:
    xanchor 1.0 xpos 0.95
    yanchor 0.0 ypos 0.05
    on show:
        alpha 0.0
        time 3.0
        linear 30 alpha 1.0

style skip_car_frame is empty

label car_dialogue:
    scene car plains
    show billy car
    with fade
    play music billy_mix volume 1
    music "Billy's Mix - Billy Mays"
    cs "Well, Arceus, it has been quite a ride."
    arceus "It sure has. We've been through quite a lot, haven't we?"
    cs "Yeah, I'm so tired. I can't wait to get some actual rest."

    show screen skip_car

    pause 1.0

    cs "So, Arc?"
    arceus "Yeh?"
    cs "Are you a furry?"
    arceus "I mean, I {i}am{/i} furry."
    cs "You know what I mean."
    arceus "Is it {i}really{/i} being a furry if I'm literally not a human?"
    cs "Fair point."

    pause 1.0

    cs "You know, I can drive, Billy."
    billy "This is {i}my{/i} car!"
    cs "Well, {i}yeah,{/i} but, if you don't want to drive the whole way..."
    billy "No, I'm good. You're in {i}my{/i} car, and that means {i}I'll{/i} drive!"
    cs "Alright, man... I just don't feel like we paid you enough for this."
    billy "Everything I sell is always $19.95!"
    arceus "{size=-15}That isn't true--"
    cs "{size=-15}Shh..."
    cs "Thanks, man."
    billy "{i}That's{/i} the power of friendship!"

    pause 1.0

    digi "CS, how {i}did{/i} you beat me in the pencil sharpening contest?"
    digi "I have, like, robotic augments."
    cs "Digi, you said you were inspired by me, correct?"
    digi "Yeah..."
    cs "I've been celebrating Pencil Sharpening Day every year since I invented it."
    digi "I guess so...{w=1.0}{nw}"
    cs "I {i}literally{/i} sharpened a lightbulb with a pencil sharpener."
    digi "Yeah, I don't even know how you did that."

    pause 1.0

    cs "So, Arc, where'd you learn to hack like that?"
    arceus "College."
    cs "You went to college? I thought you'd been in prison for five years!"
    arceus "And...?"
    cs "How... how old are you?"
    n "Arceus locks eyes with CS."
    cs "I forgot what I was saying. Never mind."
    arceus "Yeah, that's fine."

    pause 1.0

    cs "How long is this drive?"
    arceus "You sound like a child asking their mom if they're at Disney World yet."
    cs "I'm sorry, man. I just want to get home."
    billy "It's quite a ways away, still!"
    cs "Aw, man..."
    arceus "Listen, at least the cops aren't after us this time."
    billy "What?"
    digi "Huh?"
    cs "Don't worry about it."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    carla "Hey, Billy, it's Carla!"
    billy "What are you doing in my car?"
    carla "I'm not in your car, I'm on the phone. You're using the Jupiter Jack, remember?"
    billy "Oh, yeah."
    carla "We have a meeting in twenty minutes."
    billy "I'm in the fucking Northeast!"
    carla "What? What are you doing there?"
    billy "It's {i}my{/i} car!"
    n "Billy hangs up the phone."
    billy "Unbelievable."
    
    pause 1.0

    arceus "CS, why do you still pay for Adobe Premiere?"
    cs "Well, I pay for the whole Creative Cloud."
    digi "Why? Isn't that super expensive?"
    arceus "You know, I can get you the whole suite for free."
    cs "No, no, I know. I just don't feel like I should."
    arceus "Yarr."
    cs "No, thank you. I understand what you were insinuating."
    arceus ";)"
    billy "How much are you paying for it?"
    cs "Like $60 a month..."
    digi "That's fucking insane!"
    billy "Unbelievable! I wouldn't pay more than $19.95!"
    billy "And buy one, get one {i}free!{/i}"
    cs "What would I do with two Adobe suites?"
    billy "What would you do with two Grater Platers?"
    cs "Fair enough."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    pakoo "Hey, guys, which {i}Cars{/i} movie is your favorite?"
    pakoo "I personally think the first one is the best."
    cs "Nah, it's definitely the second one."
    arceus "Yeah, I'm with CS on this one."
    arceus "It's a damn spy movie with cars!"
    cs "And Mater says \"I'm the bomb!\" or whatever."
    pakoo "I just like the first one I think because the '70 Dodge Charger is in it."
    pakoo "What's his name, again?"
    digi "Pakoo, did you even watch the first one?"
    pakoo "Pfft, yeah, I just haven't seen it in a while."
    pakoo "Whatever. The first one is better."
    n "Pakoo hangs up."

    pause 1.0

    cs "Hey, Arceus?"
    arceus "Hmm?"
    cs "Ever heard of the Butterfly Effect?"
    arceus "Yeah, that's like where one little thing can {i}effect{/i} something big later down the line."
    cs "Yeah, I've been thinking, what if, like, I took the other job Linus gave me?"
    arceus "What do you mean?"
    cs "Oh, Linus wanted me to build him a stream machine."
    arceus "Ah, I see. That sounds cool."
    cs "I was thinking about what would have happened if I'd done that."
    cs "I might've, like, gotten into a fight and went to the hospital or something."
    cs "And then traveled the world!"
    arceus "That's very... descriptive."
    cs "What I love about the Butterfly Effect is that that might've actually happened!"

    pause 1.0

    cs "Have you heard of Genshin Impact? Start your adventure on the continent of Teyvat, and--{w=0.5}"
    arceus "{b}No.{/b}"
    billy "I'm a pitchman, and even I won't stoop that low."
    n "CS shuts up."

    pause 1.0

    arceus "Okay, so, CS, what's up with the catmaid outfit?"
    pause 3.0
    arceus "CS?"

    pause 3.0

    n "Billy gets a call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    linus "Hey Billy. CS is with you, right?"
    cs "Oh, hey, Linus. It's me, CS!"
    cs "I'm sorry about the cop scenario. I had an issue with a company called HoH SiS where they scammed me, and I kinda beat up their workers."
    digi "CS, what the hell did you do?"
    linus "Oh, HoH SiS? I heard that the cops were looking for them anyway."
    linus "I'm sorry to hear about all that, though. I hope you are doing well now."
    cs "We're doing okay!"
    linus "That's good. I hope to hear from you again."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    iris "Arceus?"
    digi "Oh my God."
    arceus "How did you-- who is this?"
    iris "We need to talk later."
    pause 1.0
    iris ":3"
    n "The phone hangs up from the other end."

    pause 1.0

    arceus "Hey, remember that pizza place we went to?"
    cs "Yeah, why?"
    arceus "Well, when we spent the night there, I could have {i}sworn{/i} there was someone watching us."
    cs "Oh, really? Like, when we were sleeping?"
    arceus "Yeah, I think I saw this dude with a funky hat, and he had a camera."
    cs "That's really creepy."

    pause 1.0

    arceus "Did you ever change the Mount Rushmore thing back?"
    cs "Nope!"
    cs "Why would I? It looks cool now!"
    arceus "..."
    
    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    pakoo "What did the dog say after a long day of work?"
    pause 3.0
    pakoo "That was ruff."
    n "Billy immediately hangs up."

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    tv_billy "Hi, it's Billy!"
    tv_billy "Introducing the New Craptop that isn't sentient at all, from me, Billy Mays!"
    billy "What the actual fuck?"
    tv_billy "Hello? Did I get a new signal?"
    billy "You aren't Billy! I'm Billy!"
    tv_billy "No! {i}I'm{/i} Billy! I died long ago and I'm now in Super Heaven, selling pointless products!"
    billy "No, fuck you! {i}I'm{/i} the real Billy!"
    cs "Yeah, dude from the radio, you sound like an imposter."
    arceus "sus{w=0.25}{nw}"
    tv_billy "And {i}you{/i} sound like that one guy who I sold a laptop to from his old-ass TV!"
    cs "No clue what are you talking about."
    n "Billy turns off the Jupiter Jack for a while."

    pause 1.0

    cs "Who called asking for you earlier, Arc?"
    arceus "No clue."
    cs "Huh."

    pause 1.0

    cs "Man, we should have a podcast or something."
    arceus "No, no we shouldn't."
    cs "What do you mean? We're just chatting right now, and I think it's pretty funny!"
    arceus "You only think it's funny because we're the ones talking."
    arceus "Every group of idiot friends thinks they're funny enough to have a podcast, and 99 percent of the time, they're wrong."
    billy "Yeah, I gotta agree with him on this one. I don't think anyone would find this funny."
    n "Arceus glances at the top-right corner of the screen."
    cs "What are you looking at?"
    arceus "Nothing."

    pause 1.0

    n "Arceus sniffs the air."
    cs "What do you smell, Arc?"
    arceus "Gas."
    cs "Oh, jeez, I hope the tank isn't leaking!"
    arceus "No, like, gas. Like, passed gas."
    cs "Oh, that was me."
    n "Billy rolls down the window for a bit."
    play sound sfx_roll_window volume 0.7
    
    pause 5.0

    $ renpy.music.set_pause(True, "music")
    play music2 moving_right_along
    $ renpy.pause(5.0, hard = True)
    # 0:05.0
    cs "{cps=30}{image=note_small1.png} Moving right along, in search of good times and good news {image=note_small2.png}{w=0.8}{nw}"
    $ renpy.pause(1.0, hard = True)
    # 0:08.9
    cs "{cps=30}{image=note_small1.png} With good friends you can't lose {image=note_small2.png}{w=0.8}{nw}"
    # 0:11.4
    arceus "{cps=30}{image=note_small1.png} This could become a habit! {image=note_small2.png}{w=0.8}{nw}"

    stop music2
    $ renpy.music.set_pause(False, "music")

    pause 1.0

    cs "I spy, with my little eye, something blue."
    arceus "Is it the car?"
    cs "Yeah..."

    pause 1.0

    cs "Did you know you can buy 500,000 plastic straws on AliBaba for like $50?"
    arceus "Why... would you?"
    cs "I don't know, you just {i}can.{/i}"
    billy "That's an amazing deal!"
    arceus "I think that's meant for, like, restaurants."
    cs "I guess, but, like, that'd still be funny to do, right?"
    arceus "...no?"
    cs "Yeah, you're probably right."

    pause 1.0

    cs "I wonder what would've happened if we'd gone south."
    arceus "Back at Compass Road?"
    cs "Yeah. Who knows how far we might've gotten..."

    pause 1.0

    cs "Let's play 20 Questions!"
    arceus "Sure."
    cs "Okay, it's an object."
    arceus "Is it bigger than a breadbox?"
    cs "Nope."
    arceus "Um, is it useful?"
    cs "Yep!"
    arceus "Hmm, uh, do you use it with your hands?"
    cs "Yeah."
    arceus "Is it... uh, frick, is it in my house?"
    cs "Probably."
    arceus "Is it in a drawer?"
    cs "Usually?"
    arceus "Is it shiny?"
    cs "Typically, yeah."
    arceus "Is it a knife?"
    cs "Nope!"
    arceus "Dang it, uh, is it a tool?"
    cs "Yes?"
    arceus "Okay, okay, is it in the kitchen?"
    cs "Yes!"
    arceus "Okay, so is it a fork?"
    cs "Nope!"
    arceus "How many questions have I done?"
    cs "You're halfway in."
    arceus "A... spoon?"
    cs "That's the one!"
    arceus "Welp, yay."

    pause 1.0

    n "Arceus is reading a book."
    arceus "{i}Call me Ishmael.  Some years ago-- never mind how long precisely-- having little or no money in my purse,"
    arceus "{i}and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world."
    cs "Arc? Are you... reading {i}Moby Dick?"
    arceus "Yeah."
    arceus "{i}It is a way I have of driving off the spleen and regulating the circulation.  Whenever I find myself growing grim about the mouth;"
    arceus "{i}whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet--{nw}"
    cs "Do you... have to read out loud?"
    arceus "Oh, shit, I'm reading out loud?"
    cs "How do you not notice that?"
    arceus "{i}and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street,"
    arceus "{i}and methodically knocking people's hats off--then,  account it high time to get to sea as soon as I can."
    cs "Yeah, you're doing it again."
    arceus "Sorry."

    pause 1.0

    cs "{i}First of all, let me get something straight: This is a journal, not a diary. I know what it says on the cover, but when Mom went out to buy this thing I specifically told her to get one that didn't say “diary” on it."
    arceus "Okay, okay, I get it."

    pause 1.0

    cs "The fog is coming."
    arceus "The fog is coming, CS?"
    cs "The fog is coming, Arc."
    billy "Crap, the fog is coming!"
    cs "The fog is coming, Billy."
    digi "The fog is coming."
    arceus "Fuck, the fog is coming, Digi?!"
    digi "The fog is coming, Arceus."
    billy "The fog is coming."
    cs "The fog is coming."

    pause 1.0

    n "CS hears something from the back of the car. It sounds like the faint clacking of plastic."
    n "CS turns around."
    n "Arceus is mumbling under his breath."
    arceus "Right, up, right inverted, up inverted..."
    cs "Are you... solving a Rubik's cube?"
    arceus "Yeah, it's a hobby of mine."
    cs "Where the fuck did you get a Rubik's cube?"
    arceus "Man, we've been a lot of places the last few days. I don't remember exactly where I got a Rubik's cube."
    cs "I need to learn to stop asking questions."
    arceus "That, you do."

    pause 1.0

    n "Billy turns on the Jupiter Jack again."
    tv_billy "Hi, Billy Mays here for Smacid!"
    billy "What the actual fuck?"
    tv_billy "The fast and easy way to smash stomach pain from the source!"
    billy "What is this shit? I would {i}never{/i} sell this scammy crap!"
    n "Billy changes the channel on the Jupiter Jack."

    pause 1.0

    n "Pakoo calls the group again."
    pakoo "Digi, didn't you fall in a black hole one time?"
    digi "Can you not bring this up now?"
    pakoo "It's kinda funny that it happened though."
    cs "Digi, is this true?"
    digi "Look, just-- why do you always clown on me for these things?"
    pakoo "Because it's a little funny. Speaking of which, did you know about this dance Digi did?{w=0.5}{nw}"
    digi "Stop! Billy, hang up on him!"
    billy "No, it's {i}my{/i} radio!"
    n "Arceus temporarily disables the Jupiter Jack."
    digi "Thank you, Arc."
    billy "What the actual fuck? I'm gonna throw you all out of this car!"
    cs "Now I'm curious. What was Pakoo talking about, Digi?"
    digi "Look, I'll tell you later. I don't want to think about it."
    n "The radio comes back on."
    pakoo "--and, yeah, it's, like, the best video ever. Thank you, Digi. I unironically love that video."
    digi "Sure, Pakoo."

    pause 1.0

    cs "Could you imagine if, like, everything we did was predetermined?"
    arceus "What, like {i}The Matrix?"
    cs "Yeah, I guess so, but what if everything we said was just someone else doing the talking?"
    digi "I think you just watched {i}The Matrix{/i} recently."
    cs "FUCK SEX BALLS."
    cs "FUCK SEX BALLS."
    cs "FUCK SEX BALLS."
    billy "CS, how old are you?"
    cs "I was just testing the Matrix!"
    cs "No way they could've predicted me saying that."

    pause 1.0

    cs "Digi, did you ever actually poop in your socks?"
    digi "God damn it. No."
    cs "Okay, okay, I was just wondering..."

    pause 1.0

    billy "Hi, Billy Mays here! No..."
    billy "Hi, Billy Mays... No..."
    billy "Billy Mays here! For the... No..."
    cs "You okay, man?"
    billy "I just try to practice my infomerical voice a few times a day."
    billy "Recently, I've felt like I've been losing my charm."
    digi "Did somebody say charm?"
    billy "Hold on, I think I've got it!"
    billy "Hi, Billy Mays here, for {i}Charm!{/i} The fast and easy way to play all of your rhythm games, in one engine."
    digi "Dude, that was amazing! Can I record you saying that next time?"
    billy "Sure! I can do a commerical for {i}Charm{/i} if you want. New product pitches are pretty sparse these days."
    digi "Hell yeah!"

    pause 1.0

    cs "Hey, Arc?"
    arceus "Hmm?"
    cs "Would you rather have unlimited bacon, but no games?"
    cs "Or games."
    cs "{i}Unlimited games."
    cs "But no games."
    arceus "What?"
    digi "That's, like, a paradox, right?"
    cs "No, no, you see, you get unlimited games, but no games."
    arceus "I'm just gonna take the unlimited bacon."
    cs "But you get no games!"
    arceus "I'm choosing bacon. Final answer."

    pause 1.0

    play sound "<from 0 to 1>sfx_roll_window.ogg" volume 0.7
    pause 2.5
    play sound "<from 0 to 2>sfx_roll_window.ogg" volume 0.7
    pause 2.0
    play sound "<from 0 to 1>sfx_roll_window.ogg" volume 0.7
    pause 1.5
    arceus "CS, stop messing with the window. I can see you doing that."
    cs "Fine, I'm just bored."

    pause 1.0
    n "Billy gets yet another call on his Jupiter Jack."
    billy "Hi, it's Billy!"
    mean "Hello, Mr. Mays! Is Digi with you?"
    digi "What the fuck, Mean. How did you know I was with Billy?"
    mean "Bro, I'mma keep it a hundred. I was just calling random numbers until I got you."
    mean "Also, turn on your ringer. I called {i}you{/i} first."
    n "Digi checks his phone."
    digi "Whoops."
    digi "So, what did ya need me for?"
    mean "I just wanted to say hi."
    mean "Hi!"
    digi "Hi, Mean."
    mean "Also, Tate says \"a.\""
    tate "a"
    n "The phone hangs up."

    pause 1.0

    n "An ad starts playing through the Jupiter Jack."
    $ renpy.music.set_pause(True, "music")
    play music2 summer_clearance_sale volume 0.5
    doug "When you shop at Walmart..."
    doug "You're shopping at Walmart."
    doug "Keep shopping at Walmart{w=0.25} by going to Walmart today!"
    stop music2
    $ renpy.music.set_pause(False, "music")
    pause 2.5
    billy "I need to get the Europa Blocker for my Jupiter Jack."

    pause 1.0

    n "The guys in the back start looking through Billy's various tools."
    show billy car turn
    billy "Hey! What are you guys doing back there?"
    cs "Nothing! I just dropped something."
    show billy car
    billy "Alright. You'd better not mess with my gadgets!"
    digi "{size=-15}Shhh! Don't say anything!"
    cs "{size=-15}Okay, I've got it. Arceus, roll down the window."
    play sound "<from 0 to 1>sfx_roll_window.ogg" volume 0.7
    pause 5.0
    cs "Alright, you ready?"
    pause 2.0
    play sound "minigames/car/sfx_gaster_blast.ogg"
    show billy car turn with hpunch
    show billy car turn with vpunch
    billy "What the hell are you guys doing?!"
    billy "I'm gonna double the offer of this car ride if you do that again!"
    show billy car
    cs "Digi did it!"
    digi "No, I didn't! You grabbed it!"
    cs "Arc rolled down the window!"
    arceus "Really? You're just gonna blame all of us?"
    play sound "<from 0 to 2>sfx_car_crash.ogg" volume 0.7
    scene tom_road
    show billy car turn with hpunch
    pause 3.0
    billy "3..."
    pause 1.0
    billy "2..."
    pause 1.0
    billy "1..."
    cs "Okay, I'm sorry! It was my fault."
    billy "No more tomfoolery in the backseat, okay?"
    cs "Okay..."
    scene car plains
    show billy car
    with dissolve

    pause 1.0

    n "Billy gets a call on his Jupiter Jack."
    host "HEY, CHAMP!"
    host "I JUST WANTED TO LET YOU KNOW YOUR {color=#ffff00}PENCIL SHARPENER{/color} SHOULD BE IN THE MAIL SOON!"
    cs "Woohoo! Thanks!"
    host "HOPE TO HAVE YOU COMPETE AGAIN NEXT YEAR!"

    pause 1.0

    cs "Wouldn't it be funny if someone was listening to all of this?"
    arceus "Well, they'd be really bored by now."

    $ achievement_manager.unlock("Bored")

    hide screen skip_car

    jump back_home
