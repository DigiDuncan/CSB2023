label csbiii_start:
    $ persistent.csb3a_unlocked = True
    stop music fadeout 3.0
    scene outside_ltt with dissolve
    show cs at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene black with dissolve
    pause 1.0
    scene inside_ltt with dissolve
    play music passport volume 0.5 if_changed
    music passport
    show linus at center with moveinright
    linus "Welcome to Linus Media Group! Come on in. I'll show you to your desk."
    cs "Thanks, Linus."
    scene black with dissolve
    n "Linus leads CS to his new desk."
    scene csdesk with dissolve
    show linus at right with moveinright
    show cs at left with moveinleft
    dxcom 5years
    cs "Wow! I thought this was a starting office. Why do I get such a cool setup?"
    linus "Actually, this is our {i}worst{/i} setup. You'll get upgraded after you've been here for a while."
    cs "Holy shit, really? This is way better than any setup I've seen, let alone {i}had.{/i}"
    linus "You must've had really bad setups then. This only has a 3080. Everyone else has 3090s or 4080s."
    cs "I have absolutely no problem with a 3080."
    linus "Well, enjoy!"
    hide linus with moveoutright
    hide screen dxcom
    pause 0.5
    cs "I guess I'd better get to work! Let's see what videos need editing..."
    show cs surprised
    cs "Hmm..."
    cs "I have the new TechQuickie video on how livestreaming works..."
    cs "Or, this video on how at least half of the keys on your keyboard should be macros..."

    # this section added by tate

    n "As CS ponders his choices, he receives a Slack message from Taran."
    play sound sfx_slack
    show taran slack at manual_pos(0.6, 0.2) with Dissolve(0.1)
    pause 0.5
    taran "Hey, CS! Would you like to join us for a quick meeting?"
    if persistent.true_ending:
        menu:
            "Join the meeting?"
            "Yes":
                show cs happy
                cs "Sure thing! I'll be right there!"
                hide taran with Dissolve(0.25)
                hide cs with moveoutright
                stop music fadeout 3.0
                scene black with dissolve
                pause 1.0
                jump csbiii_ai
            "No"  (type = "true"):
                jump csbiii_no_meeting

label csbiii_no_meeting:
    show cs disappointed
    cs "Not this time. I need to get to work!"
    hide taran with Dissolve(0.25)
    pause 0.5
    show cs surprised
    cs "Now, which video..."
    menu:
        "Which video will CS edit?"
        "TechQuickie's Intro To Livestreaming" (type = "true"):
            pass
        "Comprehensive Keyboard Macro Guide":
            jump csbiii_boring_video 

    # end section added by tate

    show cs disappointed
    cs "Damn it, Taran... You can edit your own macro fetish content."
    show cs
    cs "I guess I'll edit the livestreaming one."
    scene black with dissolve
    pause 1.0
    n "CS starts working on editing the TechQuickie video. After some time, Linus comes in to check on him."
    scene csdesk
    show cs at left
    with dissolve
    show linus at right with moveinright
    linus "Hey, CS, how's the new video coming along?"
    cs "It's going well! I have the background all done, and I'm working on adding graphics and fixing audio now."
    linus "Wow! You're a fast worker. You'll get off of that old 3080 in no time."
    show cs happy
    cs "Thanks, Linus."
    linus "Speaking of livestreaming, we need a new PC for {i}The WAN Show.{/i} Can you go and buy parts for one?"

    menu: 
        "What will CS do?"
        "Go to the store.":
            jump friend_microcenter
        "Help edit a video." (type = "true"):
            jump csbiii_edit_video

label csbiii_boring_video:
    scene csdesk
    show cs surprised at left
    play music passport volume 0.5 if_changed
    music passport
    cs "I suppose that something super-technical like this could be really useful to the viewers. Maybe I'll learn something new, too."
    show cs
    cs "Well, let's see what this is all about!"
    scene black with dissolve
    pause 1.0
    n "As CS watches the footage, his eyelids grow heavy..."
    centered "Two hours later..."
    play sound sfx_csnore
    pause 1.0
    linus "CS?"

    scene csdesk
    show cs concentrate at left
    show linus at right
    with dissolve

    play sound sfx_csnore
    cs "Zzzzz..."
    linus "{i}CS!!" with hpunch
    stop sound
    show cs scared
    cs "Wha-- huh?!"

    linus "Damn it, CS!"
    if fun_value(FUN_VALUE_COMMON):
        linus "I've heard your sleep schedule's abysmal, but you can't sleep {i}any{/i}time!"
    else:
        linus "Asleep on the job? On your {i}first day?!"
    cs "Oh, shi--{nw}"
    linus "This is unacceptable!"
    linus "You're {i}fired!" with hpunch

    scene black with dissolve
    pause 1.0
    n "CS is groggily escorted out of the building."
    jump fired_new_plan

label csbiii_edit_video:
    play music passport volume 0.5 if_changed
    music passport
    show csdesk
    show linus at right
    show cs at left  
    cs "Nah, I wanna finish this project first. That way, I can help you pump out videos faster."
    linus "Alright, that's fine. I'll probably send Colton to get the parts instead. He's good at sucking up and doing this kinda thing."
    cs "Alright, yeah. I definitely wasn't using this as an excuse to get out of shopping!"
    linus "... Okay? Whatever, just keep editing."
    cs "Yeah, no, don't worry, I've got this."
    show linus flipped
    hide linus with moveoutright
    n "Linus leaves the room."
    stop music fadeout 3.0
    music end
    cs "Hmm, this video looks pretty great so far. I'm practically done at this point."
    cs "I wonder what the others will think of this. I should probably get opinions from some of the other employees."
    pause 0.5
    play music good_eatin volume 0.4 if_changed
    music good_eatin
    show taran at right with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        taran "You eatin' good, CS?"
    else:
        taran "Need any help with anything?"
    show cs happy
    cs "Hey, Taran! You wanna check out my video so far?"
    taran "Sure, let it roll."
    # TODO: FOR THE LOVE OF GOD, CAN WE FIX THIS SCREENSHOT ALREADY? I *PROMISE* YOU CS WILL NOTICE IF WE DON'T
    scene csvideo with dissolve
    n "CS and Taran watch CS' video."
    scene csdesk
    show cs disappointed at left
    show taran at right
    with dissolve
    cs "Well? You think it's good?"
    taran "Hey, hey! That's not half-bad!"
    show cs happy
    cs "Thanks! I guess my many years of video editing are finally paying off!"
    taran "They definitely are."
    taran "You know what? I think this video is so good, I don't even think Linus needs to check it."
    taran "He'll be so surprised when you upload it. He's gonna wonder how you put it together so well in such little time."
    show cs
    cs "You really think so? I mean, I don't want him to be upset with me."
    taran "Don't worry about it. If he thinks it's that bad, I'll take the blame for it."
    show cs disappointed
    cs "That's nice and all, but do you think that's a good idea? I mean, I don't want to mess up my first chance at this."
    taran "Nah, don't worry about it."
    taran "Even if something dumb happens, he usually never gets mad at us for doing silly things like that."
    cs "Well, if you say so, I guess it's fine."
    cs "Let's wait and see how he reacts."
    taran "Alrighty, then. I'll catch you later!"
    show cs happy
    cs "For tonight, this{w=0.05} is{w=0.05} C{w=0.05}S,{w=0.5} siiiiiiiiigning{w=0.05} out!"
    taran "... What did you say?"
    show cs worried
    cs "Huh? I totally didn't say that. I'm just gonna go now."
    taran "..."
    cs "..."
    taran "... This is {i}your{/i} office..."
    cs "..."
    taran "Okay, I'll see you later then!"
    show taran flipped at right
    hide taran with moveoutright
    stop music fadeout 3.0
    music end
    pause 1.0
    show cs
    cs "Well, I guess since this video is already good enough, I should upload it now."
    cs "It's so crazy having the ability to access the LTT channels. There's so much crazy shit going on here!"
    cs "Oh, well. Time to upload this."
    pause 1.0
    show cs surprised
    pause 1.0
    n "CS pauses for a moment."
    pause 1.0
    cs "I don't know. I really don't feel like I should upload this yet."
    cs "It doesn't feel complete. Something is missing..."
    cs "Lemme look at the project file and run through the video again."
    pause 0.5
    n "Just as CS was about to rewatch his video, an he gets an idea."
    # TODO: idea lightbulb? idk
    show cs happy
    cs "I've got it!"
    cs "I know {i}exactly{/i} what to do!"
    show cs
    cs "If Taran really does mean what he says about Linus, then I'm sure he'll {i}love{/i} this!"
    show cs happy
    cs "I'm gonna turn this video into a YTP!"
    cs "It'll be perfect! No one will expect it because they probably don't even know what I've done with my life for the past 13 years!"
    show cs
    cs "As always, I should make sure it's as high-quality as possible, so both Linus {i}and{/i} the fans can enjoy it."
    cs "But, I don't have much time before Linus comes back and notices, so I need to hurry!"
    show cs happy
    if fun_value(FUN_VALUE_MUSIC):
        cs "Welp, time to make a supernova of a video!"
    else:
        cs "Welp, time to get to work!"
    scene black with dissolve
    minigame "minigame_editing" "csbiii_boost" "csbiii_bad_video"

label csbiii_bad_video:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "Let's see your results."
    $ renpy.movie_cutscene(bad_ytp)

    scene black with dissolve
    pause 0.5
    centered "The next day."
    pause 0.5
    scene inside_ltt with dissolve
    pause 0.5
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    cs "Hey guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes, and we need to talk."
    show cs happy
    cs "Don't worry, I already know it's perfect. It's so great, isn't it?"
    linus "It's actually the very opposite of that. You're fired."
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        play sound sfx_waterphone
    show cs worried
    cs "Wait, what?"
    linus "Look, I don't care how much you wanted to humiliate me. Just leave."
    show cs scared
    cs "I don't understand, I didn't think you would be this upse--{w=0.25}{nw}"
    linus "{sc=1}Just get out of here, you stupid, dumb animal!"
    cs "..."
    n "CS turns around and stomps out of the building."
    show cs angry flipped 
    play sound sfx_punch
    with hpunch
    pause 0.5
    hide cs with moveoutleft
    play sound sfx_punch volume 0.75
    with hpunch
    pause 0.5
    scene black with dissolve
    play sound sfx_punch volume 0.5
    pause 1.5
    play sound sfx_punch volume 0.25
    pause 3.0
    jump fired_new_plan

label csbiii_boost:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "Let's see your results!"
    $ renpy.mark_label_seen("play_edit_game")
    $ renpy.movie_cutscene(good_ytp)
    scene black with dissolve
    pause 0.5
    centered "The next day."
    pause 0.5
    $ achievement_manager.unlock("no_1_pooper")
    scene inside_ltt with dissolve
    pause 0.5
    show cs at offscreenleft
    pause 0.5
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    show linus at offscreenright
    cs "Hey, guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes, we did."
    linus "It was..."
    show cs disappointed
    cs "Oh, shoot, it was awful, wasn't it?"
    cs "Yeah, I should've realized my style is too crazy. I guess I should leave..."
    show cs disappointed flipped at mid_offscreen_left with move
    show linus behind cs at left with ease
    show cs worried flipped at mid_offscreen_left
    play sound sfx_punch_friendly
    with vpunch
    show linus at mid_left with move
    if fun_value(FUN_VALUE_MUSIC):
        n "As CS turns around, he almost trips on a counter, one that looks like those found at the airport."
    else:
        n "As CS turns around, Linus gives him a friendly punch in the back."
    play music airport_counter volume 0.5 if_changed
    music airport_counter
    linus "Dude, what are you talking about? That video was {i}awesome!{/i}"
    show cs worried at left
    show linus at center
    with move
    cs "Woah, wait! You actually {i}like{/i} YTPs?"
    linus "Yeah, man! You think I hired you on the spot just because of your obviously-fake visa?"
    linus "I {i}love{/i} your videos! I've been secretly hoping you would YTP one of mine for the longest time!"
    show cs happy with dissolve

    show linus at manual_pos(0.4, 0.5, 0.5)
    show cs happy at manual_pos(0.3, 0.5, 0.5)
    with ease
    play sound sfx_high_five

    show cs at left
    show linus at center
    with ease

    n "CS' frown fades into a big grin as they share a high-five."
    cs "Hell yeah! I never would've thought that YTPs would help me in a business setting, let alone with a boss who {i}enjoys{/i} them!"

    cs "Alright! Well, I guess I'd better get back to poopin'!"
    show cs flipped at left
    show cs flipped at offscreenleft with ease
    show linus at mid_left with move
    n "As CS heads out of the room, Linus shouts after him."
    linus "Hey, later today, I've got a big surprise to show you. I'll bring it by your office and we can check it out!"
    cs "Sure thing!"
    scene black with dissolve
    pause 0.5
    scene csdesk
    show cs at center
    with dissolve
    n "As CS gets comfortable at his desk, his mind starts to race with ideas."
    cs "Oh, man... where do I even start, now?"
    cs "I have so many ideas for videos to poop. I could even try to teach Linus how to YTP..."
    show cs surprised
    cs "I mean, with the amount of tech he drops on a daily basis, he kinda already {i}is{/i} a YTP."
    pause 0.5
    show cs happy
    cs "Alright, well, back to editing!"
    show cs
    play sound sfx_keyboard loop
    n "The time flies by as CS dumps his ideas into Premiere."
    pause 1.0
    cs "Doo dee doo..."
    show linus at offscreenright
    n "Linus barges in."
    stop sound
    play sound sfx_doorslam_open
    with hpunch
    show linus at center
    with ease
    play sound sfx_punch_alt
    show cs scared with hpunch
    show cs scared at left
    show linus at right
    with ease
    linus "CS!!!"
    show cs worried
    cs "{i}Woah, shi--{/i}{w=0.5} You scared the crap out of me!"
    show cs
    linus "Hah, sorry. I'm just excited to show you this!"
    show linus_box at truecenter with dissolve
    $ collect("linus_box")
    n "Linus holds out a rectangular box with bold black lettering. It reads, DO NOT USE."
    show cs disappointed
    cs "Umm, you sure this is the right box? It literally says--"
    linus "Yeah, I know what it says. I just wrote this on here so no one {i}else{/i} uses it."
    linus "Don't worry, I didn't, like, buy it from some creepy dude at a garage sale who claims it's haunted."
    show cs worried
    n "CS looks unnerved."
    linus "Look, just... look inside. I'm sure you'll like it."
    n "CS cautiously reaches into the box."
    show ytx at truecenter
    $ collect("ytx")
    hide linus_box 
    with dissolve
    n "He pulls out what looks to be a graphics card, but with a brown YouTube logo engraved onto the side."
    show cs
    cs "Woah, what {i}is{/i} this, Linus? A YouTube-brand graphics card?"
    linus "Not exactly. It's a custom-made experimental piece of hardware that we have never used before."
    show ytx at manual_pos(0.5, 0.3, 0.5) with move
    n "Linus holds the card into the air."
    linus "Behold! {w=0.5}The-- WOAH SHIT{w=0.25}{nw}"
    show ytx at manual_pos(0.5, 1.0, 0.5) with MoveTransition(0.1)
    pause 0.1
    play sound sfx_clonk
    show cs scared
    show linus with vpunch
    n "Linus loses grip of the card as it tumbles down onto the table next to him."
    play sound sfx_michael_facepalm
    # TODO: sfx luke laughing
    n "CS facepalms while Luke can be heard laughing from across the room."
    show cs disappointed
    cs "Goodness, Linus. You should maybe {i}not{/i} do that next time."
    linus "Yeah, I'm sorry. Maybe {i}you{/i} should hold it."
    show ytx at manual_pos(0.3, 0.7, 0.5) with move
    pause 0.5
    linus "This card is called the YTX-9001 Ti, a PCI add-in for enhancing and optimizing YouTube Poops."
    show cs
    n "CS' eyes widen."
    cs "Wait, whaaat? That's awesome! How does this even work?"
    linus "Well... we don't actually know. We haven't tested it yet."
    linus "We don't exactly do a lot of YTPing around here... until now!"
    linus "We were hoping you could help us test it. It even apparently has a feature called poop-tracing, which I'm especially curious about."
    show cs happy
    cs "Well, what're we waiting for? Let's get this thing hooked up!"
    scene black with dissolve
    n "Linus and CS take apart CS' PC and install the card."
    n "They then start the computer, and everything boots up as normal."

    scene csdesk
    show cs at left
    show linus at right
    with dissolve

    linus "Alright, now that it's up and working, we need to install the drivers."
    show ytx_drive at manual_pos(0.7, 0.5, 0.5) with dissolve
    $ collect("ytx_drive")
    linus "The card came with a flash drive that includes them."
    pause 0.5
    hide ytx_drive with dissolve
    n "As Linus inserts the flash drive, a window off the side of the screen pops up saying \"Your new Peeforce Experience drivers are available.\""
    show cs happy
    n "CS chuckles a bit."
    show cs
    cs "\"Peeforce\"? I must admit, even these driver names are a bit silly."
    n "Linus laughs."
    linus "If you want, we can wipe them later."
    show cs happy
    cs "{i}Wipe!{/i} Now {i}you're{/i} in on it!"
    n "They both laugh as the drivers finish installing. As soon as the installation completes, CS boots up Premiere."
    show cs surprised
    cs "Alrighty, let's see here..."
    cs "Why don't we try this on that YTP I just made?"
    scene csvideo with dissolve
    n "Linus reads from the included instruction manual."
    linus "Go into \"Settings\" real quick, and find the \"YTP Features\". Turn \"YTP Mode\" on to enable poop-tracing."
    cs "Alright, here goes nothing."
    # TODO: background image with the loading bar
    n "A loading bar appears as the timeline starts shifting on its own, creating different edits in the process."
    cs "Holy crap! This is amazing! It optimized every part of my YTP!"
    linus "That's pretty cool! Let's try it on a completely new source."
    linus "Open the video that we just recorded yesterday."
    n "CS opens the video and re-enables the YTP settings. Before CS's eyes, edits are automatically made to the source."
    cs "Wow! This is incredible!"
    linus "And, hey, if you don't like the edits it makes, you can always turn it off or tweak the other options in that tab."
    linus "If all else fails, you still have the ability to edit any section the old-fashioned way!"
    scene csdesk
    show cs at left
    show linus at right
    with dissolve
    cs "Wow, thank you so much for this, Linus!"
    linus "No problem! Please consider this my gift to you."
    linus "We should make a review video of it before the workday ends."
    cs "Sure thing. Let's take the card out real quick."
    scene black with dissolve
    pause 0.5
    centered "Ten minutes later..."
    pause 0.5
    scene ltt_bg
    show ltt_fg
    with dissolve
    show cs at t_cs_ltt behind ltt_fg with moveinleft
    show linus at t_linus_ltt behind ltt_fg with moveinright
    n "After making sure everything is set up to record, Linus and CS take their places on the set."
    n "The camera operators are ready and the teleprompter is activated."
    n "An employee starts counting down before another gives the signal to begin."
    pause 0.5
    play sound sfx_clapperboard
    pause 1.0
    linus "These days, video editing software is capable of producing some {i}amazing{/i} results."
    linus "Unfortunately, the process to actually {i}get{/i} to those results can, more often than not, be difficult, tedious, and even downright {i}frustrating!"
    linus "To make matters worse, when it comes to those of us who make a living off of content creation, the YouTube algorithm has just been demanding more and {i}more{/i} from us!"
    linus "If we want even a {i}chance{/i} of all our hard work getting any attention, we have to find a way to stand out from the millions of other creators on this platform."
    linus "This is why, today, we have brought along surrealist video editor cs188, who {i}also{/i} happens to be the newest addition to the LMG team!"
    show cs happy
    cs "Hey guys, CS here!"
    show cs
    linus "CS has been turning otherwise boring videos into hilarious nonsense for over a decade, {i}and{/i} he has the subscribers and views to prove it."
    linus "Naturally, this also makes him the {i}perfect{/i} guy to help us review the upcoming YTX-9001 Ti!"
    cs "Thanks, Linus!"
    cs "The YTX-9001 Ti is a fantastic piece of hardware that promises to make video editing less of a chore for everyone!"
    cs "We can't wait to show you {i}all{/i} of its features in action!"
    linus "Much like we can't wait to show you this segue {w=0.25}to our {i}sponsor!"
    "..."
    n "The two stand for a moment, awkwardly staring at the camera."
    linus "... Go ahead and cut."
    pause 0.5
    show cs disappointed
    cs "Who knew recording could be so stressful..."
    cs "I could use a drink. These lights are so bright..."
    if fun_value(FUN_VALUE_COMMON):
        show ltt_bottle_linus behind ltt_fg at truecenter with moveinbottom
        linus "Here. Take this water bottl-- oops!{w=0.25}{nw}"
        show ltt_bottle_linus at manual_pos(0.5, 1.0, 0.5) with MoveTransition(0.1)
        $ collect("ltt_bottle_linus")
        pause 0.1
        play sound sfx_metalpipe
        show cs scared with vpunch
        n "Linus drops the water bottle onto the floor."
        show cs worried
        cs "Wow, Linus... you really {i}do{/i} have butterfingers."
    else:
        show ltt_bottle_linus behind ltt_fg at truecenter with moveinbottom
        $ collect("ltt_bottle_linus")
        linus "Here! Try out our LTT water bottle! It'll keep your water cool all day, allowing {i}you{/i} to stay hydrated without the hassle. {a=https://lttstore.com}lttstore.com{/a}"
        show cs disappointed
        cs "... Linus, we aren't filming..."
        "..."
        linus "Sorry. Force of habit."
    linus "Anyway, let's take five. The crew can handle getting some B-roll clips of the card itself."
    cs "Sure thing..."
    scene black with dissolve
    n "After some time, they recording is complete, and the footage is passed along to the editing team."
    n "CS takes few minutes to shake off the stress of being featured in such a high-budget production for the first time."
    n "Once he collects himself, CS heads up to Linus' office to chat."
    jump csbiii_ltt_decide

label csbiii_ltt_decide:
    play music airport_counter volume 0.5 if_changed
    music airport_counter
    scene loffice with dissolve
    pause 0.5
    show cs at left with moveinleft
    pause 0.5
    cs "Hey, Linus?"
    linus "What's up, CS? What do you need help with?"
    menu:
        "What does CS need help with?"
        "I want to work on YTPs." (type = "true"):
            jump csbiii_ytp_edit
        "I want to do reviews.":
            jump csbiii_reviews

label csbiii_reviews:
    play music airport_counter volume 0.5 if_changed
    music airport_counter
    scene loffice
    show cs at left
    show linus at offscreenright
    $ fanbase = "ltt"
    cs "I'm up to doing more review videos with you."
    show linus at center with ease
    linus "Sweet! I'll make sure to hit you up for our next video!"
    linus "If you want, if you have any ideas for products you'd like to review, we can go over them and see if they'd be a good fit."
    linus "But, for now, you should probably start heading out. It's getting late."
    show cs disappointed
    cs "Yeah..."
    cs "You know, I just hope that my community will move on, now that I'm helping make this new content."
    cs "I've been making YouTube Poops for so long now that it's all anyone has come to expect from me."
    cs "But, even with my {a=patreon.com/cs188}Patreon{/a} and stuff, YTPs really don't pay very well. Advertisers don't like 'em and neither does the algorithm."
    cs "I hope that my fans will understand in due time that I just needed something {i}more."
    linus "I'm sure you'll be okay. Besides, the LTT fanbase is {i}much{/i} bigger!"
    linus "This company exists almost {i}entirely{/i} because of what YouTube pays us!"
    linus "As long as you're under my employment, I can promise you, you'll never have to worry about money again."
    cs "I sure hope you're right..."
    n "Before CS can think about it much longer, a sudden commotion can be heard from the front of the building."
    show colton at mid_right with moveinright
    show cs worried
    colton "Linus! There is a furry outside!"
    show linus flipped
    linus "What?"
    linus "Hold on, lemme check on this."
    n "CS and Linus rush to the front door."
    scene black with dissolve
    pause 0.5
    jump csbiii_arceus_appears
    
label csbiii_ytp_edit:
    play music airport_counter volume 0.5 if_changed
    music airport_counter
    scene loffice
    show cs at left
    show linus at offscreenright
    cs "I have a question about my job here at LMG."
    n "Linus stands up and walks over to him."
    show linus at center with moveinright
    linus "Sure. I mean, what do you see yourself doing for us?"
    cs "I really want to make more YTPs for you guys."
    n "Linus laughs a bit."
    linus "Oh, CS, when I gave you the YTP card, that was meant for use on your own channel, not the LTT one."
    show cs disappointed
    cs "I know, but--{w=0.25}{nw}"
    linus "I mean, for example..."
    show cs scared
    linus "TARAN! GET IN HERE!" with vpunch
    n "Taran rushes up to Linus' office."
    show taran at offscreenright with determination
    show taran at right with MoveTransition(0.5)
    show cs worried
    n "Taran is panting and out of breath."
    taran "Yes, {w=0.5}Linus? {w=0.5}What is it?"
    show linus flipped
    linus "Taran, have you ever seen a YTP?"
    taran "Other than the one CS made the other day? Not really."
    show linus
    linus "See, CS? Not only will our audience be super confused, but our employees will be as well."
    show cs disappointed
    cs "Alright... I see..."

    menu:
        "What will CS do?"
        "Show everyone more YTPs." (type = "true"):
            jump csbiii_both_fan
        "Ignore them and keep making your own YTPs.":
            jump csbiii_ytp_fan

label csbiii_ytp_fan:
    play music airport_counter volume 0.5 if_changed
    music airport_counter
    scene loffice
    show cs disappointed at left
    show linus at center
    show taran at right
    $ fanbase = "ytp"
    cs "Well... I still want to keep working on YTPs!"
    stop music fadeout 3.0
    music end
    cs "This is what I, like, built my entire life on, and I just..."
    linus "CS? Are you okay? Maybe you should take a chill pill."
    show cs angry
    cs "I thought you {i}liked{/i} YTPs! You said that's why you even hired me!"
    taran "What? You hired him because of {i}that?!"
    linus "Look, let's all just calm down, okay?"
    linus "If you wanna keep doing YTPs, fine, but if it messes with our company's reputation, you will need to stop, or you're fired."
    cs "Fine by me!"
    show cs angry flipped at mid_offscreen_left with move
    n "Before CS can storm off, Colton rushes in with some info."
    show colton at offscreenright with determination
    show colton at mid_right with MoveTransition(0.25)
    colton "Linus! There is a furry outside!"
    show linus flipped
    show cs worried at left with moveinleft
    linus "What?"
    linus "Hold on, lemme check on this."
    n "CS and Linus rush to the front door."
    scene black with dissolve
    pause 0.5
    jump csbiii_arceus_appears

label csbiii_arceus_appears:

    scene frontdoor with dissolve
    show linus flipped at right with moveinleft
    show cs disappointed at center with moveinleft
    n "Linus opens the door."
    linus "Who's there? Is anyone here?"
    stop music fadeout 1.0
    n "Suddenly, Arceus rushes in."
    show arceus worried at offscreenright with determination
    show arceus worried at mid_right with MoveTransition(0.25)
    show cs scared
    if fun_value(FUN_VALUE_MUSIC):
        arceus "CS! There you are! Hired guns are coming after us!"
    else:
        arceus "CS! There you are! We need to go, ASAP!"
    play music hired_guns volume 0.5 if_changed
    music hired_guns

    if fanbase == "both":
        show linus
        linus "So you {i}do{/i} have a furry fanbase who wants to join LTT! Damn it, CS, I should've known."
        show cs worried
        cs "Shut up, Linus!"
    else:
        show linus
        linus "CS? You know this... person?"
    show cs worried
    cs "It's a long story."
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while."
    arceus "The cops are still looking to extradite us back to America, and they are headed {i}here{/i} to search for you!"
    linus "{i}What?!{/i} CS, why are there {i}cops{/i} after you?"
    linus "This could seriously damage our reputation {size=-15}more than the time I mentioned I dropped hard R's as a kid!"
    menu:
        "What will CS do?"
        "I'm going to stay with LTT." (type = "bad"):
            jump csbiii_cops_ltt
        "Escape with Arceus.":
            jump csbiii_arc_escape

label csbiii_both_fan:
    play music airport_counter volume 0.5 if_changed
    music airport_counter
    scene loffice
    show cs at left
    show linus at center
    show taran at right
    $ fanbase = "both"
    stop music fadeout 3.0
    music end
    cs "You know what? Why don't you all come down to my office?"
    linus "I mean... sure. Let's see what you have in store for us."
    linus "Come on, guys, let's go!"
    show taran flipped at right
    hide taran with moveoutright
    hide linus with moveoutright
    hide cs with moveoutright
    scene csdesk with dissolve
    n "Linus gathers more employees as they follow CS to his office."
    show cs flipped at center with moveinright
    show cs with determination
    show linus at mid_left with moveinright
    show linus flipped
    show taran at left with moveinright
    show taran flipped at left with determination
    show luke at mid_right with moveinright
    show colton at right with moveinright
    luke "What is this all about, Linus? I was just about to go home."
    linus "Boohoo, Luke. You probably don't even do anything at home."
    luke ":("
    colton "Hi, guys! What did I miss? I thought we were going to build a streaming machine?"
    linus "Look, Colton, we can do that tomorrow."
    cs "Hey guys, CS here! Showing you the wonderful world of YTPs!"
    linus "Oh no..."
    colton "A... what?"
    cs "Alright! Strap in, because YouTube is where the poop is!"
    show black with dissolve
    play sound sfx_ytpintro
    n "Half an hour passes, and CS has shown LTT what YTPs are all about."
    hide black with dissolve
    pause 1.0
    cs "Welp. Those are some of the best ones that I could find."
    taran "Hey, those were actually really funny!"
    taran "Linus, weren't you telling me about how much you actually {i}liked{/i} YTPs?"
    linus "Nooooo...?"
    luke "Now that you say that..."
    linus "Alright, fine! I guess if you all like it too, we could put some on our channel from time to time."
    show cs happy
    $ achievement_manager.unlock("crowd_pleaser")
    cs "Hell yeah!"
    linus "But, you still have to help with some other videos as well, not just YTPs."
    show cs flipped
    cs "Alright, that's fair."
    linus "Well, the rest of you can go back to what you were doing."
    colton "Oh, yeah, Linus? Before I go, I was told someone was banging on the door to enter just a minute ago."
    colton "They were dressed up like a furry or something."
    linus "Great, CS, did you attract your furry fanbase to work here as well?"
    show cs disappointed flipped
    cs "I swear, this doesn't have anything to do with my community."
    linus "Wait, what do you mean? I was just joking about the furry fanbase."
    cs "..."
    linus "Whatever, let's just go check out who it is."
    scene black with dissolve

    n "CS and Linus rush to the front door." 
    scene black with dissolve
    pause 0.5
    jump csbiii_arceus_appears

label csbiii_cops_ltt:
    stop music fadeout 3.0
    music end
    scene frontdoor
    show linus at right
    show arceus worried at mid_right
    show cs disappointed
    n "CS thinks long and hard about his decision."
    cs "I'm sorry, Arceus, but I finally got this dream job. I can't just throw it all away now."
    arceus "The cops are almost here, CS! If they find you, you won't be able to work anyhow!"
    cs "I'm done running, Arc. I need to stay with LMG."
    arceus "Welp. I tried."
    n "Arceus shrugs and walks away as he makes his own escape."
    show arceus flipped with determination
    show arceus flipped at offscreenright with move
    linus "CS, seriously, {i}what{/i} happened with the cops! I still have {i}no{/i} clue what's going on!"
    cs "Look, okay, so there are these guys from this foundation repair company called HoH SiS.{w=0.5}{nw}"
    cs "My house was in dire need of foundation repair, so I called them up to come help fix my house.{w=0.5}{nw}"
    show cs surprised
    cs "They also thought I was a prank caller because I made that one video about them a long time ago,{w=0.25}{nw}"
    show cs disappointed
    cs "and they also told me that they changed their policy with payments and I had to pay them immediately.{w=0.5}{nw}"
    show cs worried
    cs "While they were working, I decided to go visit my friend Michael Rosen, and he had this chocolate cake that actually {i}wasn't{/i} chocolate cake,{w=0.25}{nw}"
    cs "and when I gave him an energy drink, he went kinda crazy, so I went back home to check on HoH SiS.{w=0.5}{nw}"
    cs "And when I got back home, they--{w=0.25}{nw}"
    show copguy at mid_right with moveinright
    show cs scared
    copguy "Freeze!"
    n "As CS was explaining his story in extreme detail, the cops showed up."
    copguy "You are under arrest! Put your hands in the air!"
    stop music fadeout 3.0
    music end
    $ ending_manager.mark("premature")
    bad_end "Stupid CS! You dropped\nyour lore in front of the hoes!" "csbiii_ltt_decide"

label csbiii_arc_escape:
    play music hired_guns volume 0.5 if_changed
    music hired_guns
    scene frontdoor 
    show cs worried at center
    show linus at right
    show arceus worried at mid_right
    cs "Look, I'm sorry, Linus. I wish I could explain, but Arceus is right. I need to get out of here."
    linus "I am, like, {i}so{/i} confused and frustrated. This better not ruin LMG."
    show cs disappointed
    cs "I'm so sorry. I'll get you guys caught up on the situation as soon as I can."
    cs "This is CS, signing out."
    arceus "We have no time for that, CS! We need to go, {i}now!"
    show cs disappointed at offscreenright
    show arceus flipped at offscreenright
    with MoveTransition(0.25)
    scene black with dissolve
    pause 0.5
    scene outside_ltt with dissolve
    show cs disappointed flipped at left
    show arceus at right
    with moveinright
    show cs disappointed at left
    n "CS and Arceus sprint out of the building, trying to find cover."
    play sound sfx_siren loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "As they keep moving, they hear approaching sirens as flashing lights rush towards the LMG headquarters."
    if fanbase == "ytp":
        cs "Thank God we are getting out of here. While the job was cool, Linus didn't really like my ideas."
        arceus "Ah, dang. That sucks to hear."
        arceus "Let's get out of here!"
    else:
        cs "This is awful. I was just starting to get along well with Linus and the gang."
        arceus "I'm sure they'll forgive you in due time, but for now, we need to evade the cops' trail and get back to the United States."
    stop music fadeout 3.0
    music end
    show cs worried flipped at offscreenleft
    show arceus at offscreenleft
    with MoveTransition(0.25)
    n "While Arceus and CS flee the scene, the cops enter the building to investigate."
    scene frontdoor
    stop sound fadeout 4.0

    show colton at left
    show luke flipped at mid_mid_left
    show taran flipped at center
    show linus at right

    with dissolve
    n "The employees are panicked as they spot the officers."
    luke "WTF is going on?"
    taran "Linus! What did you {i}do?!"
    linus "Relax, guys, it's nothing that {i}we{/i} did."
    n "Linus mutters to himself."
    linus "{size=-12}I should've done a background check on CS. It's weird how--"

    if fun_value(FUN_VALUE_RARE):
        play sound sfx_fbi_open_up
        with vpunch
        with vpunch
        pause 1.0
        with hpunch
        with hpunch
    else:
        play sound sfx_door_break
        with hpunch

    show colton at mid_left_left
    show luke flipped at left
    show taran flipped at mid_mid_left
    show linus at center
    with MoveTransition(0.25)
    show linus flipped
    pause 1.0

    show copguy at offscreenright with determination
    show copguy at right with MoveTransition(0.25)
    if fun_value(FUN_VALUE_MUSIC):
        n "Undyne bursts in."
    else:    
        n "Copguy bursts in."
    play music undyne volume 0.5 if_changed
    music undyne
    copguy "Alright, everyone! Backs against the wall! Nobody move!"
    luke "So, are we moving to the wall or... {i}not{/i} moving?"
    copguy "Don't question the police! Just--{w=0.5} stand against the wall!"

    show colton at manual_pos(0.2, 0.5, 0.5):
        linear 0.5 zoom 0.75
    show luke flipped at manual_pos(0.3, 0.5, 0.5):
        linear 0.5 zoom 0.75
    show taran flipped at manual_pos(0.4, 0.5, 0.5):
        linear 0.5 zoom 0.75
    show linus flipped at manual_pos(0.5, 0.5, 0.5):
        linear 0.5 zoom 0.75
    with MoveTransition(0.5)

    show cop at offscreenright
    show cop at offscreenleft with move

    show cop at offscreenright
    show cop at offscreenleft with move

    show cop at offscreenright
    show cop at offscreenleft  with move

    n "The LMG members move toward the wall while more policemen march in to begin their search."
    pause 0.5
    copguy "Alright, I have a very simple question to ask you all."
    copguy "Do you know this man?"
    play sound sfx_page
    show cswanted at manual_pos(0.65, 0.55, 0.5) with Dissolve(0.25):
        zoom 0.75
    $ collect("cswanted")
    n "Copguy produces a wanted poster with CS's face."
    hide cswanted with dissolve
    taran "Uhh, yeah, that's--"
    play sound sfx_punch_alt
    with vpunch
    linus "No, sir. We don't know who that is at all."
    copguy "Oh, really?"
    copguy "You there, what did you say about this man?"
    taran "I, uhh..."
    taran "I was saying that..."
    taran "That it looks like Colton! Yeah!"
    colton "What the {i}fuck,{/i} Taran?!" with hpunch
    linus "Yep, that looks like Colton, alright."
    n "Copguy turns back towards Linus."
    copguy "Alright, sir, what's {i}your{/i} name?"
    linus "It's Lin--{w=0.25}{nw}"
    copguy "Yeah, okay. Linard, if you say that it's {i}this{/i} man, how can you explain the maid outfit that your {i}co-star{/i} wore in your most recent video?"
    linus "Well, uhh, he's got some... weird kinks..."
    colton "{sc=2}Oh my fucking {i}God."
    copguy "If you are so sure, then, lemme go talk to the sheriff about this."
    linus "Sure thing, officer."
    show copguy flipped
    hide copguy with moveoutright
    n "Copguy steps outside to contact the sheriff."
    stop music fadeout 3.0
    music end
    pause 2.0
    colton "I can't fucking {i}believe{/i} you guys! That was {i}way{/i} too far!"
    show linus
    show luke
    show taran
    pause 1.0
    linus "April Fools?"
    colton "{cshake}IT'S {i}JULY!" with vpunch
    pause 1.0
    scene black with dissolve
    pause 1.0

    scene outside_ltt with dissolve
    pause 1.0
    n "Copguy orders the rest of the cops to leave the scene and return to the station."
    show copguy flipped at left with moveinleft
    copguy "Damn it, they don't have CS anymore. We're gonna have to start a manhunt..."
    scene black with dissolve
    pause 0.5

    scene road_to_canada
    show cs disappointed dusk at left
    show arceus dusk at right
    with dissolve
    n "Meanwhile, CS and Arceus have been running back towards the US border."
    cs "Aw, man! This is embarrassing!"
    arceus "Yeah, so much for the editing job, I guess."
    cs "I just can't seem to catch a break this month, can I?"
    cs "First my problems with HoH SiS, now I'm running from the {i}cops?!"
    cs "I should've just called a different foundation repair company..."
    arceus "Yeah, that sounds like hell."
    cs "It {i}is{/i} hell!"
    arceus "{size=-15}I mean, you {i}could{/i} have called upon me..."
    arceus "I should've known that the cops were going look for us. We didn't exactly hide our tracks too well."
    arceus "I was checking comms chatter around the area when I heard at the last second that they were heading towards LMG."
    arceus "I figured that since you helped me break out of prison, it's only fair that I come back for you."
    cs "Thanks, man. I really owe you again."
    arceus "Nah, {i}I{/i} owe {i}you."
    scene black with dissolve

    scene border_dusk
    show cs dusk at left
    show arceus dusk flipped at mid_left
    with dissolve
    play music atarashii_kaze volume 0.3 if_changed
    music atarashii_kaze
    n "CS and Arceus approach the border guard again."
    show border_guard dusk at right with moveinright
    border_guard "I'm gonna need proof of--"
    if fun_value(FUN_VALUE_MUSIC):
        border_guard "Atarashii Kaze! It's you two buds again!"
    else:  
        border_guard "Ey, it's you two buds again!"
    arceus "Yep, quite the vacation we had! We had so much fun in Canada, didn't we, CS?"
    cs "Sure did!"
    border_guard "Alright, hope you two come back to visit the Great White North again, ey buds?"
    arceus "We certainly will!"
    scene black with dissolve

    scene washington_road with dissolve
    n "The duo continues their trek into the US."
    n "They find themselves in the state of Washington, surrounded by trees."
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "So, what happened with you?"
    arceus "Hmm?"
    cs "Well, I went to work at LTT, and had to spend my nights at a nearby hotel."
    cs "Linus gave me enough money to get by for a little while."
    arceus "Wait, which hotel?"
    cs "The Hoto Hoto?"
    arceus "Shoot, I've been at the same hotel, clearing up ties from my cybercriminal past."
    arceus "I've been in prison for five years, so I need to figure out what to do again for money."
    arceus "I ran into Anno at the hotel, too. I think he said he's planning on starting some kind of band?"
    cs "Ah, neat!"
    cs "I guess it's just the time for starting over, then, huh."
    arceus "Sure seems like it."
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 2.0

    scene sheriff_office
    show sheriff at left
    with dissolve
    play music police_station volume 0.5 if_changed
    music police_station 
    n "Back at the police station, Copguy meets with the sheriff, hoping to formulate a plan to capture CS."
    show sheriff at left
    show copguy at right with moveinright
    show sheriff flipped
    sheriff "Howdy, Officer Copguy."
    sheriff "Tell me, you guys arrested CS this evening, right?"
    copguy "Unfortunately, no, we did not, sir."
    show sheriff at left 
    play sound sfx_desk_slam
    with vpunch
    sheriff "Damn it!" with hpunch
    show sheriff flipped
    sheriff "Damn it!{fast} And, how did you fuck {i}that{/i} up?" with vpunch
    copguy "Look, sir, you see, he--{w=0.25}{nw}"
    sheriff "You know what, I don't want to hear this!"
    sheriff "First, this guy manages to escape from one of our top prisons, and {i}now{/i} you're telling me that you {i}lost{/i} him?!"
    copguy "Please, sir, this is one of my best cases yet! I need to catch him, and I promise I'll put him back in jail, along with those {i}other{/i} two!"
    copguy "You know, the furry and the Kurt Cobain impersonator!"
    pause 0.5
    n "The sheriff thinks for a moment."
    pause 1.0
    sheriff "Alright, since I know you've taken this job seriously for the last 15 years, I'll let this one fuck-up slide this time."
    sheriff "But, believe me, this CS man has a pretty big target on his head."
    sheriff "We need to bring him to justice before he and his gang do anything else funny."
    sheriff "The next time you come back here, he'd better be with you, or you're fired!"
    copguy "Sure thing, boss. I'll track him down..."
    copguy "If it's the last thing I do."
    pause 0.5
    show copguy flipped
    hide copguy with moveoutright
    pause 0.5
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 2.0


    scene washington_road with dissolve
    if fun_value(FUN_VALUE_MUSIC):
        n "Meanwhile, as CS and Arceus make their way through the US, strange sounds seem to be echoing throughout the forest."
    else:  
        n "Meanwhile, without any sense of direction, CS and Arceus make their way through the US."
    play music echoing volume 0.5 if_changed
    music echoing
    show cs disappointed dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "Hey, Arceus? Do you have any clue where we are?"
    arceus "No idea. I'm just following the road. There's bound to be a rest stop here eventually."
    cs "I hope so. We've been walking for hours. It's gotta be midnight around now..."
    stop music fadeout 3.0
    music end
    n "CS looks down the road."
    show cs dark
    cs "Hey, Arc! I can see some lights in the distance! We've gotta be getting close!"
    arceus "Wait a minute, those are--"

    show cs scared dark
    show arceus worried dark
    with determination

    show blue_light at left
    show red_light at right
    with dissolve

    play sound sfx_siren volume 0.1
    n "Arceus squints into the night, but they both immediately recognize the sounds."
    show cs worried dark
    show arceus worried dark

    # TODO: implement multiple dialogue screen
    cs "{i}Shit!" (multiple=2)
    arceus "{i}Shit!" (multiple=2)

    arceus "Copguy's back! He's probably looking all over for us!"
    arceus "What do we do, CS?!"
    jump csbiii_forest_menu

label csbiii_forest_menu:
    stop music fadeout 3.0
    music end
    scene washington_road
    show cs worried dark at left
    show arceus worried dark at right
    show blue_light at left
    show red_light at right
    menu:
        "What do we do, CS?!"
        "Fight the cops with YTP Magic" (type = "bad"):
            jump genocide_fight
        "Flee into the forest" (type = "true"):
            jump csbiii_escape_forest

label genocide_fight:
    stop music fadeout 3.0
    music end
    scene washington_road
    show cs concentrate dark at left
    show arceus worried dark at right
    show blue_light at left
    show red_light at right
    n "CS closes his eyes. He starts to concentrate on the sirens and the car."
    play sound sfx_siren loop fadein 3.0 volume 0.4
    arceus "CS? What are you doing?!"
    play sound sfx_siren loop volume 0.5
    arceus "{i}CS! They're heading right for us!!"
    play sound sfx_siren loop volume 0.6
    scene black
    arceus "{cshake}{i}CS!!!"
    play sound sfx_siren loop fadein 1.0 volume 2
    pause 1.0
    play sound sfx_car_crash volume 0.7
    pause 8.0
    n "Copguy's car flies off the road and violently crashes into the forest."
    pause 0.5

    scene washington_road
    show arceus worried dark at right
    show cs concentrate dark at left
    with dissolve
    pause 3.0
    show cs dark
    pause 1.0
    show cs concentrate dark
    pause 0.2
    show cs dark
    pause 1.0
    arceus "CS? Are you okay?!"
    cs "Yeah, I feel really good, actually."
    cs "Are we good?"
    arceus "..."
    arceus "I guess so."
    arceus "Copguy, he..."
    cs "Yeah, I took care of him, didn't I?"
    arceus "I guess you did."
    cs "Should we keep going?"
    "..."
    arceus "Are you not, like, phased {i}at all{/i} by this?"
    cs "Eh, not really."
    arceus "Alright, well..."
    arceus "Let's keep going..."
    scene washington_road with dissolve
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    play music kill_cops volume 0.5 if_changed
    music kill_cops
    n "The duo keeps walking along the road."
    n "Arceus is wary of CS."
    n "He can't help but notice CS muttering to himself."

    # i am told the overflowing text box is intended - tate
    cs "{chaos}TmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXAsIG5ldmVyIGdvbm5hIGxldCB5b3UgZG93biwgbmV2ZXIgZ29ubmEgcnVuIGFyb3VuZCBhbmQgZGVzZXJ0IHlvdS4KTmV2ZXIgZ29ubmEgbWFrZSB5b3UgY3J5LCBuZXZlciBnb25uYSBzYXkgZ29vZGJ5ZSwgbmV2ZXIgZ29ubmEgdGVsbCBhIGxpZSwgYW5kIGh1cnQgeW91fg=="
    arceus "CS? What are you saying?"
    cs "Huh? Nothing."
    show arceus dark flipped
    menu:
        "Attack now." (type = "bad"):
            jump genocide_attack_arc
        "Wait." (type = "bad"):
            jump genocide_wait_arc

label genocide_attack_arc:
    stop music fadeout 3.0
    music end
    scene washington_road
    show cs dark at left 
    show arceus dark flipped at right
    $ achievement_manager.unlock("no_mercy")
    cs "{size=-15}It's now or never."
    n "CS channels CSGod."

    # TODO: some kind of sfx, maybe a cooler transition in general

    hide cs
    show csgod flipped at left
    with Dissolve(0.5)

    csgod "Time to die, Arceus!"
    show arceus angry dark
    stop music2
    music end
    show csgod flipped at left with vpunch
    play sound sfx_alt_punch
    show csgod at t_punchup with move
    show arceus angry dark at right with hpunch
    arceus "{i}Really?"
    arceus "I've been a god longer than you, dummy."
    arceus "Nice try."
    $ ending_manager.mark("god_fail")
    bad_end "There's no weapon\nto free us all!" "csbiii_forest_menu"

label genocide_wait_arc:
    stop music fadeout 3.0
    music end
    scene washington_road
    show cs dark at left 
    show arceus dark flipped at right
    cs "{size=-15}I need to wait. I'm not powerful enough to attack."
    arceus "Man, I hope you're doing alright..."
    cs "Yep!"
    pause 5.0
    n "They continue on silently for a few hours, eventually seeing the sunrise."
    scene washington_road morning
    show arceus flipped at right
    show cs at left
    with dissolve
    pause 3.0
    show arceus
    arceus "So, uhh, should we keep going this direction?"
    cs "..."
    cs "Yep."
    pause 5.0
    scene town
    show arceus at right
    show cs at left
    with dissolve    
    pause 2.0
    arceus "Hey, we found a town! That's good, right?"
    cs "Yep."
    show arceus worried
    arceus "Dude, are you {i}sure{/i} you're okay?"
    arceus "You haven't said anything, like, {i}at all,{/i} for the past several hours."
    cs "I'm fine."
    arceus "... Okay."
    arceus "So, uhh, what should we do now?"
    arceus "Are we gonna, like, try to get you home?"
    arceus "{size=-15}Do you even wanna go home?"
    cs "Yes, yes, let's just wait here."
    arceus "In the middle of the road?"
    arceus "Why?"

    arceus "There's someone coming! Shouldn't we move?"
    pause 1.0
    arceus "Hello?"
    n "The approaching vehicle slowly coasts to a stop."

    play sound sfx_car_approach_stop volume 5.0 fadein 5.0
    show billy_car behind arceus:
        xanchor 0.5 yanchor 0.5
        xpos 0.5 ypos 0.8
        alpha 0.0 zoom 0
        parallel:
            linear 5.0 alpha 1.0
        parallel:
            linear 12.0 zoom 1.2
    $ collect("billy_car")
    $ renpy.skipping = False
    $ renpy.pause(15.0, hard=True)
    $ renpy.skipping = True

    n "The driver steps out to confront the pair."
    play sound sfx_car_door_open
    show billy behind arceus with dissolve:
        xanchor 0.5 yanchor 0.5
        xpos 0.7 ypos 0.7
        zoom 0.6
        
    billy "Hey, that's my car!"
    play sound sfx_doorslam

    show billy:
        parallel:
            linear 0.5 xpos 0.5
        parallel:
            linear 0.5 ypos 0.5
        parallel:
            linear 0.5 zoom 1.0

    pause 0.5
    billy "What are you doing?"
    cs "Take us to these coordinates: 46.5754, -112.3008."
    billy "I, uhh--{w=0.5}{nw}"
    
    play sound sfx_tape_rewind volume 0.5
    with hpunch

    pause 3.0
    billy "{ytpmagic}No problem!"
    billy "{ytpmagic}Let's go!"
    scene black with dissolve
    pause 1.0
    play sound sfx_doorslam
    pause 1.0

    scene car background
    show billy car
    with dissolve

    play music insane_personalities volume 0.6 if_changed
    music insane_personalities
    pause 5.0

    scene car background night
    show billy car
    with dissolve
    pause 3.0

    n "For the whole drive, no one says a word."
    stop music fadeout 3.0
    music end
    scene cultforest
    show billy car 
    with dissolve
    pause 3.0
    billy "{ytpmagic}We are here."

    play sound sfx_car_door_open
    pause 0.5
    play sound2 sfx_car_door_ajar loop
    pause 2.0
    n "CS gets out of the car."
    pause 2.0
    play sound sfx_doorslam
    stop sound2
    pause 3.0
    n "Arceus watches as CS crosses the street and starts heading up a nearby trail."

    pause 2.0
    
    arceus "Hey, uhh, I'm gonna get out too."
    play sound sfx_car_door_open
    pause 0.5
    play sound2 sfx_car_door_ajar loop
    pause 2.0
    play sound sfx_doorslam
    stop sound2
 
    scene black with dissolve
    pause 1.0
    
    scene cultforest with dissolve
    show arceus flipped at mid_left with moveinleft
    arceus "CS? Where'd ya go?"
    arceus "CS?"
    pause 1.0
    show arceus worried flipped
    arceus "Man, what is {i}wrong{/i} with him right now?"
    pause 2.0
    arceus "After that incident with the cops, he's been..."
    pause 1.0
    arceus "He's just been--"

    play music genocide if_changed

    music insane_personalities
    show csgod at offscreenleft with determination
    csgod "Stronger than ever."
    show csgod flipped at mid_left with MoveTransition(0.25)
    show arceus flipped at mid_left with vpunch
    play sound sfx_punch
    show arceus flipped at mid_left with hpunch
    play sound sfx_punch_alt
    show arceus flipped at t_punchup with MoveTransition(0.25)
    pause 1.0
    arceus "Ouch."
    $ achievement_manager.unlock("no_mercy")
    show cultist at mid_right with moveinright
    show cultist_2 at right with moveinright
    show cultist_3 at mid_mid_right with moveinright
    cultist "Praise CSGod! Praise CSGod!"

    play sound sfx_car_tire_squeal

    n "Upon witnessing this, Billy instantly takes off!"
    pause 1.0
    csgod "I have finally harnessed the power of CSGod!"
    csgod "Time to take over the world!" # TODO: maybe a more epic line here??
    stop music
    $ ending_manager.mark("god_success")
    bad_end "This will affect\nthe local trout population!" "csbiii_forest_menu"

label csbiii_escape_forest:
    stop music fadeout 3.0
    music end
    scene washington_road
    show cs worried dark at left
    show arceus worried dark at right
    show blue_light at left
    show red_light at right
    $ achievement_manager.unlock("pacifist")
    cs "Arceus, quick! Let's escape into the forest!"
    arceus "Alrighty, let's go!"

    show arceus dark flipped at offscreenright
    show cs dark at offscreenright
    with MoveTransition(0.25)
    scene black with dissolve
    stop sound fadeout 1.0
    pause 0.5

    n "CS and Arceus quickly jump into the trees next to them."
    n "As they hunker down into the foliage, flashes of red and blue fly past them."
    pause 0.5
    arceus "Phew! That was a close one, CS!"
    cs "Yeah, it looks like we hid just in time."
    arceus "Alright, well, should we wait here for a bit or do you think the coast is clear?"
    jump csbiii_wait_forest

label csbiii_wait_forest:
    scene black
    stop music fadeout 3.0
    cs "We should probably wait for a little bit. They might turn around and see us."
    arceus "Yeah, that's a good point. Let's not risk it."
    n "CS and Arceus stay quiet in the forest for about 15 minutes before heading back onto the road again."
    pause 0.5

    scene washington_road with dissolve
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    pause 0.5
    cs "Hey, Arceus?"
    arceus "Hmm?"
    cs "Now that we have more time to talk, where exactly are we headed? Why did we come back to the US?"
    arceus "Well, I figured, you wanted to go back home, right?"
    show cs disappointed dark
    cs "Of course I want to go home, it's just... it seems so far away."
    cs "We don't really have a car or anything, we are {i}completely{/i} lost, {i}and{/i} the cops are probably still looking for us!"
    arceus "Look, man, I know it's pretty hard right now, but we've gotta be optimistic about this."
    arceus "The second we find civilization, I'm sure we can work something out and head back home."
    cs "If you say so. I just hope we don't have to {i}walk{/i} all the way there."
    arceus "I don't think that'll be the case."
    copguy "{cps=10}I don't think so either."
    play sound sfx_punch
    scene black with determination
    pause 3.0
    n "When CS and Arceus wake up, they find themselves in handcuffs leaned up against a cop car."

    scene washington_road
    show cop_car dark at mid_offscreen_left
    $ collect("cop_car")
    show cs disappointed dark at mid_left
    show arceus dark flipped at mid_left_left
    with dissolve
    cs "Huh?"
    cs "What happened?"
    show copguy dark at right with moveinright
    play music danger_mystery volume 0.5 if_changed
    music danger_mystery
    if fun_value(FUN_VALUE_MUSIC):
        copguy "Hey, ain't this a dangerous mystery."
    else:  
        copguy "Hey, you're finally awake."
    arceus "Hey, CS..."
    show arceus worried dark flipped
    arceus "I'm sorry."
    show cs worried dark
    cs "No, no, no! This can't be happening!"
    show cs scared dark
    cs "Arceus! Can't you do something about this?"
    arceus "No can do, boss. Looks like this is the end of the line."
    copguy "No time for negotiations, pal. Get in the car."

    scene copcar
    show copguy at offscreenleft
    show copcar_mask
    with dissolve
    show arceus worried flipped at right
    show cs worried at left
    with moveinleft
    play sound sfx_punch
    with hpunch
    show arceus worried
    pause 0.5
    play sound2 sfx_doorslam noloop
    pause 1.0

    show copguy at t_copguy_frontseat
    with moveinleft
    pause 0.5
    play sound sfx_doorslam
    show walkie at manual_pos(0.4, 0.3, 0.5) behind copguy with dissolve:
        zoom 0.2
        rotate 15
    $ collect("walkie")
    play sound sfx_walkie_on

    n "CS and Arceus are thrown into the back of the cruiser as Copguy barks some order into his walkie."
    copguy "This is Copguy calling in a 1-8-8 on Compass Road."
    copguy "Sheriff? We got 'em."
    sheriff "Copy that. Good job, soldier."
    play sound sfx_walkie_off
    hide walkie with dissolve
    play sound sfx_driving volume 0.5


    jump csbiii_copcar_menu

label csbiii_copcar_menu:
    play music danger_mystery volume 0.5 if_changed
    music danger_mystery
    scene copcar
    show copguy at t_copguy_frontseat
    show copcar_mask
    show arceus at right
    show cs disappointed at left
    n "As they are heading away, CS has the urge to say something."
    menu:
        "HoH SiS scammed me!" (type = "true"):
            jump csbiii_good_convince
        "I'm not CS!" (type = "bad"):
            jump csbiii_bad_convince

label csbiii_bad_convince:
    scene copcar
    show copguy at t_copguy_frontseat
    show copcar_mask
    show arceus at right
    show cs disappointed at left
    play music pressing_pursuit_cornered volume 0.3 if_changed
    music pressing_pursuit_cornered
    play sound sfx_hold_it volume 0.5
    show hold_it at truecenter with hpunch
    pause 1.0
    hide hold_it
    show cs scared
    if fun_value(FUN_VALUE_MUSIC):
        cs "Wait a second! I'm not actually CS! I'm cornered and I'm Pressing Pursuit!"
    else: 
        cs "Wait a second! I'm not actually CS!"
    cs "I just {i}look{/i} like CS!"
    show arceus worried
    arceus "I mean... he {i}might{/i} not be CS?"
    play sound sfx_objection volume 0.5
    show objection at truecenter with hpunch
    pause 1.0
    hide objection
    stop music
    music end
    show cs disappointed
    copguy "Nice try, bud. We saw your fake visa and everything."
    copguy "You two are going back to the slammer."
    $ ending_manager.mark("attorney")
    bad_end "Did you really\nthink that would work?" "csbiii_copcar_menu"

# TODO: ace attorney select evidence menu

label csbiii_good_convince:
    scene copcar
    show copguy at t_copguy_frontseat
    show copcar_mask
    show arceus at right
    show cs angry at left
    play music pressing_pursuit_cornered volume 0.3 if_changed
    music pressing_pursuit_cornered
    play sound sfx_hold_it volume 0.5
    show hold_it at truecenter with hpunch
    pause 1.0
    hide hold_it
    if fun_value(FUN_VALUE_MUSIC):
        cs "Wait a second! The reason all this happened was because HoH SiS sabotaged my computer and cornered me! I'm Pressing Pursuit!"
    else: 
        cs "Wait a second! The reason all this happened was because HoH SiS sabotaged my computer!"
    show arceus worried
    arceus "Wait, what?"
    show arceus
    copguy "What are you on about?"
    show cs worried
    cs "Yes! I called HoH SiS to fix my foundation, but they scammed me out of thousands of dollars and broke my laptop!"
    cs "So, afterwards, I went to their HQ to get my revenge!"
    copguy "I'm not believing this for a second."
    copguy "You really think I'll fall for a lie as ridiculous as this?"
    play sound sfx_objection volume 0.5
    show objection at truecenter with hpunch
    pause 1.0
    hide objection
    arceus "Actually, I have proof of all this."
    arceus "I can show you."
    copguy "And {i}how{/i} exactly do you plan to do that? Where is your evidence?"

    show craptop at manual_pos(0.7, 1.5, 0.5) with determination
    show craptop at manual_pos(0.7, 0.55, 0.5) with move

    n "Arceus pulls up a laptop that he managed to grab from the front seat."
    copguy "{i}What?{/i} How did you get that?"
    arceus "Watch this."
    play sound "<from 9.0>sfx/sfx_car_approach_stop.ogg" volume 10.0 fadein 1.0
    n "Reluctantly, Copguy stops the car."
    pause 2.0
    stop sound
    scene backseat
    show craptop evidence
    with dissolve
    n "Arceus plays back the events from {i}CS Bounciness I.{/i}"

    scene copcar
    show copguy at center
    show copcar_mask
    show arceus at right
    show craptop at manual_pos(0.7, 0.55, 0.5)
    show cs disappointed at left
    with dissolve
    cs "How--"
    show arceus happy
    arceus "I have my ways."
    show arceus
    copguy "I don't understand..."
    copguy "HoH SiS really {i}did{/i} scam you hard, didn't they?"
    copguy "I'm not sure how valid it was for you to push that man off of the building..."
    copguy "But, I can't argue right now about whether that footage is fake."
    stop music fadeout 3.0
    music end
    pause 2.0
    
    show copguy with MoveTransition(1.0):
        xanchor 0.5 xpos 0.325
    pause 1.0
    play sound sfx_car_door_open
    play sound2 sfx_car_door_ajar loop
    hide copguy with moveoutleft
    n "Copguy gets out of the car."
    n "He then proceeds to open the doors to let CS and Arceus out, freeing them of their shackles."
    pause 0.5
    play sound sfx_car_door_open
    
    scene washington_road
    show cop_car dark at mid_offscreen_left
    with dissolve

    pause 0.5

    show copguy dark flipped at right with moveinleft
    show copguy dark with determination
    show cs disappointed dark at mid_left with moveinleft
    show arceus dark flipped at mid_left_left with moveinleft
    pause 1.0
    copguy "Listen, I really shouldn't be doing this right now, but I have to go back to look into this deal with HoH SiS."
    copguy "The only thing more corrupt than the force is scummy businesses like these." # TODO: idk that about that line
    copguy "You are free to go for now."
    copguy "But know this: I am putting my job on the line for you."
    # fun fact, i stole this next line from my awful mother :D - tate
    copguy "Don't do anything stupid, because I have eyes everywhere." 

    n "Copguy gets back into his car, heading off into the dead of night."
    show copguy dark at left with move
    pause 1.0
    hide copguy with dissolve
    pause 1.0
    play sound sfx_doorslam
    stop sound2
    pause 3.0
    play sound sfx_driving
    pause 2.0
    hide cop_car with moveoutleft
    stop sound fadeout 3.0
    pause 5.0

    show arceus dark flipped at mid_right with move
    show arceus dark
    show cs dark
    pause 0.5
    if fun_value(FUN_VALUE_MUSIC):
        n "CS and Arceus look at each other and smile, doing their best Bun Guster pose."  
    else: 
        n "CS and Arceus look at each other and smile."
    play music bun_guster volume 0.3 if_changed
    music bun_guster
    arceus "Holy crap, I didn't think that would work."
    cs "Me, neither! I'm so glad that he let us go!"
    cs "I don't know how you got that footage, but we are free once again!"
    show arceus happy dark
    arceus "Hooray for CS and Arc!"

    show cs happy dark at center
    show arceus happy dark at center 
    with MoveTransition(0.5)
    play sound sfx_high_five
    show cs happy dark at mid_left_left
    show arceus happy dark at mid_right_right
    with move
    n "After a high-five, the journey of CS and Arceus continues!"
    stop music fadeout 3.0
    music end
    pause 1.0
    scene black with dissolve
    pause 1.0
    jump csbiii_choose_direction

label csbiii_choose_direction:
    $ persistent.csb3b_unlocked = True
    scene black with determination
    stop music fadeout 3.0
    music end
    n "As the pair continues wandering through the night, they soon realize that they haven't decided yet where to actually go."
    pause 1.0

    scene washington_road morning
    show cs disappointed at left
    show arceus at right
    with dissolve
    play music happy_roaming volume 0.5 if_changed
    music happy_roaming
    if fun_value(FUN_VALUE_MUSIC):
        cs "We've been happily roaming all night, but I'm exhausted." 
    else: 
        cs "We've been walking all night. I'm exhausted."
    arceus "Yeah, let's hope we find food and water soon."
    cs "Hey, uhh, do you know exactly where we're going?"
    arceus "Well, I noticed that the sun rises ahead of us, which means we're heading east right now."
    arceus "We can head in any direction, really. The second we find a better form of transportation than walking, we're taking it."
    arceus "Which way are you thinking?"

    # reset these for each playthrough
    $ compass_north_counter = 0
    $ compass_west_counter = 0
    $ compass_current_time = "morning"
    $ compass_current_shader = ""

    menu:
        "Which way do you want to go?"
        "North":
            jump csbiii_north
        "East" (type = "true"):
            jump true_east
        "South":
            jump south_start
        "West":
            jump csbiii_west

# everything below here has been rewritten significantly to fix both the EXCESSIVE LABELS and the abrupt shader/sky color changes. it is important to use scene EVERY TIME a sprite changes, or sprites will be duplicated. - tate

label csbiii_north:
    
    play music happy_roaming volume 0.5 if_changed
    scene expression "washington_road %s" % compass_current_time

    if compass_north_counter == 0:
        scene expression "washington_road %s" % compass_current_time
        show expression "cs %s" % compass_current_shader at left
        show expression "arceus %s" % compass_current_shader at right
        cs "What if we go north?"

        scene expression "washington_road %s" % compass_current_time
        show expression "cs %s" % compass_current_shader at left
        show expression "arceus worried %s" % compass_current_shader at right
        arceus "... What?"

        scene expression "washington_road %s" % compass_current_time
        show expression "cs disappointed %s" % compass_current_shader at left
        show expression "arceus worried %s" % compass_current_shader at right
        cs "You said to pick a direction!"

        scene expression "washington_road %s" % compass_current_time
        show expression "cs disappointed %s" % compass_current_shader at left
        show expression "arceus angry %s" % compass_current_shader at right
        arceus "To the north is Canada. Where we just came from. Try again."

        scene expression "washington_road %s" % compass_current_time
        show expression "cs %s" % compass_current_shader at left
        show expression "arceus angry %s" % compass_current_shader at right

        $ compass_north_counter = 1
    else:
        scene expression "washington_road %s" % compass_current_time
        show expression "cs %s" % compass_current_shader at left
        show expression "arceus angry %s" % compass_current_shader at right
        $ achievement_manager.unlock("northerner")
        arceus "I literally just said--"
        arceus "Just pick another direction."

        scene expression "washington_road %s" % compass_current_time
        show expression "cs %s" % compass_current_shader at left
        show expression "arceus %s" % compass_current_shader at right

    menu:
        "North":
            jump csbiii_north
        "East" (type = "true"):
            jump true_east
        "South":
            jump south_start
        "West":
            jump csbiii_west

label csbiii_west:

    play music happy_roaming volume 0.5 if_changed

    if compass_west_counter == 0:
        scene expression "washington_road %s" % compass_current_time
        show cs at left
        show arceus at right
        cs "I think we should go west."
        arceus "Alright, we can try."
        n "CS and Arceus run into the Pacific Ocean."
        $ compass_current_time = "day"
        scene expression "washington_road %s" % compass_current_time
        show cs at left
        show arceus at right
        with dissolve
        arceus "It's just the ocean. Let's go another direction."
        $ compass_west_counter = 1
        $ compass_current_shader = ""

    elif compass_west_counter == 1:
        scene expression "washington_road %s" % compass_current_time
        show cs at left
        show arceus at right
        cs "Let's try going west again. I'm sure there is something there."
        show arceus worried
        arceus "Uhm, okay... maybe we've missed something."
        n "CS and Arceus run into the Pacific again."
        $ compass_current_time = "dusk"
        scene expression "washington_road %s" % compass_current_time
        show cs dusk at left
        show arceus dusk at right
        with dissolve
        arceus "Still just the ocean..."
        $ compass_west_counter = 2
        $ compass_current_shader = "dusk"

    elif compass_west_counter == 2:
        scene expression "washington_road %s" % compass_current_time
        show cs dusk at left
        show arceus dusk at right
        cs "Nah, come on, there is definitely {i}something{/i} we can find going west."
        show arceus worried dusk
        arceus "I really don't want to go there again..."
        cs "Nah, we've got this. For sure this time."
        show cool_crab dusk at manual_pos(0.3, 0.6, 0.5) with dissolve:
            zoom 0.5
        $ collect("cool_crab")
        n "CS and Arceus find a cool-looking crab, but it's still just the ocean again."
        hide cool_crab
        $ compass_current_time = ""
        scene washington_road
        show cs dark at left
        show arceus angry dark at right
        with dissolve
        cs "Hey! That's quite an epic crustacean!"
        arceus "Alright, cool, can we pick another direction that {i}isn't{/i} west this time?"
        $ compass_west_counter = 3
        $ compass_current_shader = "dark"

    elif compass_west_counter == 3:
        scene washington_road
        show cs dark at left
        show arceus dark at right
        cs "Okay! One last time!"
        arceus "..."
        show arceus worried dark
        arceus "Something tells me that you were in an asylum for a bit..."
        n "CS and Arceus, surprisingly, find the ocean again."
        $ compass_current_time = "morning"
        scene expression "washington_road %s" % compass_current_time
        show cs happy at left
        show arceus angry at right
        with dissolve
        $ compass_west_counter = 4
        $ compass_current_shader = ""

    elif compass_west_counter == 4:
        $ compass_current_time = "day"
        scene expression "washington_road %s" % compass_current_time
        show cs at left
        show arceus angry at right
        with dissolve
        arceus "..."
        $ compass_west_counter = 5
        $ compass_current_shader = ""

    elif compass_west_counter == 5:
        $ compass_current_time = "dusk"
        scene expression "washington_road %s" % compass_current_time
        show cs dusk at left
        show arceus angry dusk at right
        with dissolve
        arceus "..."
        $ compass_west_counter = 6
        $ compass_current_shader = "dusk"

    elif compass_west_counter == 6:
        $ compass_current_time = ""
        scene washington_road
        show cs dark at left
        show arceus angry dark at right
        with dissolve
        arceus "..."
        $ compass_west_counter = 7
        $ compass_current_shader = "dark"

    elif compass_west_counter == 7:
        $ compass_current_time = "morning"
        scene expression "washington_road %s" % compass_current_time
        show cs at left
        show arceus angry at right
        with dissolve
        $ achievement_manager.unlock("ocean_man")
        arceus "Player. {w=0.5}Stop. {w=0.5}Going. {w=0.5}West."
        $ compass_west_counter = 4
        $ compass_current_shader = ""

    menu:
        "North":
            jump csbiii_north
        "East" (type = "true"):
            jump true_east
        "South":
            jump south_start
        "West":
            jump csbiii_west


# # TODO: if we ever do a beach episode, maybe this is direction to go lmao
