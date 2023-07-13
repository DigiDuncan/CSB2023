label csbiii_start:

    scene outside_ltt with fade
    show cs at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene inside_ltt with fade
    play music "<loop 0>passport.mp3" volume 0.5
    music PASSPORT.MID - George Stone
    show linus at center with moveinright
    linus "Welcome to Linus Media Group, come on in, I'll show you to your desk."
    cs "Thanks, Linus."
    scene black with fade
    n "Linus and CS walk to CS' new desk."
    scene csdesk with fade
    show linus at right with moveinright
    show cs at left with moveinleft
    cs "Wow! I thought this was a starting office, why do I get such a cool desk?"
    linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."
    cs "Holy shit, really? This is way better than any setup I've seen, let alone had."
    linus "You must've had really bad setups then, this only has 3080s, everyone else has 3090s or 4080s."
    cs "I have absolutely no problem with 3080s."
    linus "Well, enjoy!"
    hide linus with moveoutright
    cs "I guess I better get to work on editing, let's see what videos I need to edit..."
    cs "Let's see, I have the new TechQuickie video on how live streaming works, or the video on how at least half of the keys on your keyboard should be macros..."
    show cs worried
    cs "Dammit Taran, you can edit your own macro fetish content."
    show cs
    cs "I guess I'll edit the livestreaming one."
    scene black with fade
    n "CS starts working on editing the TechQuickie video and Linus comes in to check on him."
    scene csdesk
    show cs at left
    with fade
    show linus at right with moveinright
    linus "Hey CS, how's the new video coming along?"
    cs "It's going well, I have the background all done and I'm working on adding graphics and fixing audio."
    linus "Wow! You're a fast worker, you'll get off of those old 3080s in no time."
    cs "Thanks Linus."
    linus "Speaking of live streaming, we need a new PC for the WAN Show, can you go and buy parts for one?"

    menu: 
        "What are you going to do?"
        "Go to the store.":
            jump microcenter
        "Help edit a video." (type = "true"):
            jump edit_video
label microcenter:
    cs "Sure, what parts do you need?"
    linus "We need eggs, milk..."
    linus "Just kidding."
    linus "I'll leave the details up to you since you've done a lot of live streaming, just get the highest end available."
    cs "Alright, I'll go get the parts."
    # Jumpcut, fade to black
    cs "I have your new streaming PC, and it runs quite well too! Way better than my computer!"
    linus "Awesome! Lemme go move this into the othe--{w=0.25}WOAAAHHH!!!"
    show linus with hpunch
    n "Linus trips and falls, immediately destroying the insides and outsides of the PC that CS just built."
    cs "Oh damn, you okay there?"
    linus "No of course not! I just destroyed another one of these $20,000 computing machines! How the hell am I going to get another just like this?"
    cs "Well, you could just always buy more parts like these, I'm sure you have the budget for that."
    linus "No no, that's too expensive and wasteful, let me think..."
    linus "Hmmm..."
    linus "Wait! I just got a brilliant idea! Why don't you go buy more parts for me, we certainly have the budget to do that!"
    cs "Uhmm… I literally just said--"
    linus "Alright! The plan is settled! You can go fetch me some more parts for the ultimate streaming machine, and you get to decide what parts should be in the computer!"
    cs "Okay but, are there any recommendations you would give me for building this? This is YOUR money, you know."
    linus "Nah, it's fine. I'm sure you will do well picking out parts, make sure to get the highest quality you can!"
    cs "Alrighty, I'll get going now."
    stop music fadeout 3.0
    music end
    # TODO: [BG] CS goes to Microcenter
    n "CS goes to Microcenter."
    cs "Okay gamers, we are buying some parts for our epic computing machine. Let's go inside the magical concrete structure to buy some computing parts."  # the fuck is this line Pakoo
    cs "Wow, this building looks a lot bigger than the places I would go shopping at near home."
    n "CS enters the building."
    cs "Woah! This place is huge!"
    cs "There are so many options to pick from! And I have as much money as I'll ever need, too!"
    cs "Before I get too carried away though, I should probably start by buying the processor."
    # TODO: [BG] CPU aisle
    n "CS goes to the CPU aisle."
    cs "My goodness, there are so many options."
    cs "I honestly don't know which one to pick."
    cs "Let's see here…"
    cs "I could get a super high-end Intel CPU since Linus still seems to default to Intel even after shilling for AMD…"
    cs "Or I could get a Ryzen, more cores would probably be better for streaming..."
    cs "Too many good options! I don't know what one to pick!"
    # FIXME: REMEMBER TO CHANGE THIS
    cs "Whatever, I'll get *whatever choice since this doesn't change the path*"
    cs "Now for the GPU."

    menu:
        "Which card do you want to choose?"
        "High end GPU":
            jump high_gpu
        "Low end GPU":
            jump low_gpu

label low_gpu:
    cs "I should probably try to save Linus some money. Most of the expensive parts he gets are from sponsors, he's not actually that rich."
    n "CS flags down an employee."
    cs "I'm trying to get a graphics card, and I want to save money, what do you have?"
    worker "Everything here is pretty expensive, lemme check the back..."
    n "The worker comes back."
    worker "Alright, I got this. It's pretty old, and it's covered in dust, but it's like $50."
    cs "Sounds great, I'll take it."

label edit_video:
    cs "Nah, I wanna finish this video first. That way I can help you pump out videos faster."
    linus "Alright, that's fine. I'll probably send Colton to get the parts instead, he's good at sucking up to those kinda things."
    cs "Alright haha, yeah I definitely wasn't using this as an excuse to get out of shopping!"
    linus "...ok? Whatever, just keep editing."
    cs "Yeah, no, don't worry I got this."
    hide linus with moveoutright
    n "Linus leaves the room."
    stop music fadeout 3.0
    music end
    cs "Hmm, this video looks pretty great so far, I'm practically almost done at this point."
    cs "I wonder what the others will think of this though? I should probably get opinions from some of the other employees."
    play music "<loop 0>good_eatin.mp3" volume 0.4
    music "Good Eatin' - ClascyJitto"
    show taran at right with moveinright
    taran "Need any help with anything?"
    cs "Hey Taran! You wanna check out my video so far?"
    taran "Sure, let it roll."
    scene csvideo with fade
    n "CS and Taran watch CS' video."
    scene csdesk
    show cs worried at left
    show taran at right
    with fade
    cs "Well, you think it's good?"
    taran "Hey hey! That's not half bad!"
    show cs happy
    cs "Thanks! I guess my many years of video editing is finally paying off after all."
    taran "They definitely have."
    taran "You know what? I think this video is so good, I don't even think Linus needs to check this."
    taran "He will be so surprised when you upload it, he will wonder how you put it together so well in such little time."
    show cs
    cs "You really think so? I mean, I don't want him to be upset with me."
    taran "Don't worry about it. If he thinks it is that bad, I'll take the blame on it."
    cs "That's nice and all, but do you think that's a good idea? I mean, I don't want to mess up my first chance at this."
    taran "Nah, don't worry about it."
    taran "Even if something dumb happens, he usually never gets mad at us for doing silly things like that."
    cs "Well if you say so, I guess it's fine."
    cs "Let's wait and see how he reacts."
    taran "Alrighty then, I'll catch you later!"
    cs "For tonight, this{w=0.1} is{w=0.1} CS,{w=0.5}{cps=*0.1} signing{cps=*10} out!"
    taran "...What did you say?"
    cs "Huh? I totally didn't say that, I'm just gonna leave."
    taran "..."
    n "..."
    taran "... This is {i}your{/i} office..."
    n "..."
    taran "Okay, I'll see you later then!"
    show taran flipped at right
    hide taran with moveoutright
    stop music fadeout 3.0
    music end
    # Do we really need three lines for this?
    cs "Well, I guess since this video is already good enough, I can upload it now."
    cs "It's so crazy having the ability to access the LTT channels. There is so much crazy shit going on here!"
    cs "Oh well, time to upload this."
    # ^
    n "CS pauses for a moment."
    cs "I don't know, I really feel like I shouldn't upload this yet."
    cs "It doesn't feel complete. Something is missing from it..."
    cs "Lemme go look at the project file and run through the video again."
    n "Just as CS was about to watch his video, an idea kicked in."
    cs "I got it! I know exactly what to do!"
    cs "If Taran really does mean what he says about Linus, then I'm sure he'll love this!"
    cs "I'm gonna turn this video into a YTP!"
    cs "It will be perfect! No one will expect it because they probably don't even know what I even did with my life for the past 13 years!"
    cs "As always, I should make sure it's as good as possible so at least Linus will enjoy it, along with his fans."
    cs "But I also don't have much time before Linus comes back and notices, so I need to hurry!"
    cs "Welp, time to get to work!"
    menu:
        "Good" (type = "true"):
            hide cs
            hide csdesk
            show black
            with fade
            jump boost
        "Bad" (type = "bad"):
            hide cs
            hide csdesk
            show black
            with fade
            jump fired

label fired:
    $ renpy.movie_cutscene("movies/mymovie_cs.mpg")
    scene inside_ltt with fade
    n "The next day."
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    cs "Hey guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes, and we need to talk."
    cs "Don't worry, I already know it's perfect. It's so great, isn't it?"
    linus "It's actually the very opposite of that. You're fired."
    show cs disappointed
    cs "Wait, what?"
    linus "Look, I don't care how much you really wanted to humiliate me, just leave."
    cs "I don't understand, I didn't think you would be this upse-{w=0.25}{nw}"
    linus "Just get out of here you stupid dumb animal!!"
    cs "..."
    n "CS turns around and stomps out of the building."
    show cs angry flipped with hpunch
    hide cs with moveoutleft
    scene black with fade
    scene outside_ltt with fade
    show cs angry at center
    cs "This really sucks. One of my favorite YouTubers just kicked me out of my dream job and told me to never come back!"
    show cs
    cs "I would be acting super emotional right now, but the years of angry YouTube comments against me have already worn me down."
    cs "Well, I guess I have no other choice than to look for another job."
    return
label boost:
    $ renpy.movie_cutscene("movies/good_cs_ytp.mpg")
    n "The next day."
    $ achievement_manager.unlock("#1 Rated Pooper")
    scene inside_ltt with fade
    show cs at offscreenleft
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    show linus at offscreenright
    cs "Hey guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes we did."
    linus "It was..."
    show cs disappointed
    cs "Oh shoot, it was awful wasn't it?"
    cs "Yeah, I should've realized my style is too crazy, I guess I should leave…"
    show cs disappointed flipped at left
    show linus behind cs at left with ease
    show linus at center with ease
    n "As CS turns around, Linus friendly punches him in the back."
    play music "<loop 0>airport_counter.mp3" volume 0.5
    music Airport Counter - Kazumi Totaka
    linus "Dude what are you talking about? That video was awesome!"
    show cs at left
    cs "Woah wait, you actually like YTPs?"
    linus "Yeah man, you think I just hired you on the spot because of your obviously fake visa?"
    linus "I love your videos! I've been secretly hoping you would YTP one of mine for the longest time!"
    show linus at left with ease
    show linus at center with ease
    show cs happy
    n "CS' frown fades in a big grin, as they both high-five."
    cs "Hell yeah! I would've never thought YTPs would help me in a business setting, nevermind that my BOSS enjoyed them!"
    cs "Alright! Well, I guess I better get back to poopin'!"
    show cs flipped at left
    show cs flipped at offscreenleft with ease
    n "Before CS heads out of the room, Linus shouts to him."
    linus "Hey, later today, I got a big surprise to show you. I'll stop by your office and we can check it out!"
    cs "Sure thing!"
    scene csdesk
    show cs at center
    with fade
    n "When CS gets back to his setup, he starts letting his mind race with ideas."
    cs "Oh man, where do I even start now?"
    cs "I have so many ideas of videos to poop, I could even try to teach Linus how to YTP..."
    cs "I mean, with the amount of tech he drops on a daily basis, he kinda already is a YTP."
    cs "Alright well, back to editing!"
    n "The time flies by as CS dumps his ideas into Premiere."
    cs "Doo dee doo..."
    show linus at offscreenright
    n "Linus barges in. "
    show linus at center with ease
    with hpunch
    show cs at left
    show linus at right
    with ease
    linus "CS!!!"
    show cs worried
    cs "WOAH SHI--{w=0.5}you scared the crap out of me!"
    show cs
    linus "Hah sorry, I'm just excited to show you this!"
    n "Linus holds out a rectangular box that reads on the front in black bold text {b}DO NOT USE.{/b}"
    show cs disappointed
    cs "Umm, you sure this is the right box? It literally says--"
    linus "Yeah I know what it says, I just wrote this on here so no one else uses it."
    linus "Don't worry, I didn't like, buy it from some creepy dude at a garage sale that claims it's haunted."
    n "CS looks unnerved."
    linus "Look just, open the box. I'm sure you'll like it."
    n "CS cautiously takes the box, and opens the top. "
    show ytx at truecenter
    n "Inside is what looks to be a graphics card, but with a brown YouTube logo engraved into the side."
    show cs
    cs "Woah, what is this, Linus? A YouTube-brand graphics card?"
    linus "Not exactly. It's an experimental piece of hardware that we have never used before, and it's custom made."
    n "Linus holds the card into the air."
    linus "Behold! {w=0.5} The-- WOAH SHIT {w=0.5}{nw}"
    show ytx at linus_drop_tips
    pause 0.35
    show linus with vpunch
    n "Linus loses grip of the card as it tumbles down onto the table next to him."
    hide ytx
    n "CS facepalms, while you can hear Luke laughing in the background."
    cs "Goodness Linus, you should maybe not do that next time."
    linus "Yeah, I'm sorry. Maybe you should hold it." 
    linus "This card is called the YTX-9001 Ti, a PCI add-in for enhancing and optimizing YouTube Poops."
    n "CS' eyes widen."
    cs "Wait whaaat? That's awesome! How does this even work?"
    linus "We don't even know, we haven't even tested it yet."
    linus "It also apparently has Poop-tracing, which I'm curious to see how that works."
    cs "Well, what are we waiting for? Let's get this thing hooked up!"
    n "Linus and CS take apart CS' PC and put the card in."
    n "They then start the computer, and everything boots up as normal."
    linus "Alright, now that it's up and working, we need to install the drivers. The card came with a flash drive that includes them."
    n "As Linus inserts the flashdrive, a window off the side of the screen pops up saying 'Your new Peeforce Experience drivers are available.'"
    n "CS chuckles a bit."
    show cs happy
    cs "Peeforce? I must admit, even these driver names are a bit silly."
    n "Linus laughs."
    linus "If you want, we can wipe them later."
    cs "Wipe! Now you're in on it!"
    n "They both laugh as the drivers install, and once they're finished, CS boots up Premiere."
    scene csvideo with fade
    cs "Alrighty, let's see here. Why don't we try this on that YTP I just made?"
    linus "Go to the settings real quick, and find the YTP features. turn YTP mode ON to allow the poop-tracing."
    cs "Alright, here goes nothing."
    n "A loading bar appears as the timeline starts shifting and different edits are created in the process."
    cs "Holy crap! This is amazing! It optimized every part of my YTP!"
    linus "That's pretty cool, but let's try it on a completely new source."
    linus "Open the video that we just took yesterday."
    n "CS opens the video, and enables YTP ON again. The source starts already making edits to start with."
    linus "And hey, if you don't like the edits it makes, you can always turn it off or tweak the settings in that tab."
    scene csdesk
    show cs at left
    show linus at right
    with fade
    cs "Wow, thank you so much for this, Linus!"
    linus "No problem! This was my gift to you. Now, we should make a review video of it before the day ends."
    cs "Sure thing, let's take the card out real quick."
    scene ltt_bg
    show ltt_fg
    with determination
    show cs at t_cs_ltt behind ltt_fg with moveinleft
    show linus at t_linus_ltt behind ltt_fg with moveinright
    n "Linus goes and gets the cameras set up, and they start to film the video."
    linus "These days, video editing can be so difficult, and tedius. Lately the YouTube algorithm has been demanding more from us content creators."
    linus "Which is why today, we brought along our newest employee, long term YouTube Pooper: cs188 for this review of the new YTX-9001!"
    cs "Hey guys! CS here! The YTX-9001 is a fantastic card, and we can't wait to show you all of its features!"
    linus "Much like we can't wait to show you this seguay to our sponsor!"
    n "The two stand for a moment awkwardly staring at the camera."
    linus "...Go ahead and cut."
    cs "Who knew recording could be so stressful. I could use a drink. The lights are so bright."
    linus "Here. Take this water bottle, it will keep you hydrated and your water cool. lttstore.com"
    cs "... Linus, we aren't filming..."
    linus "Sorry. Force of habit."
    n "Some time passes and they finish the recording."
    n "Afterwards, CS goes up to Linus' office."
    #Todo get Linus' office
    scene loffice with fade
    show cs at left with moveinleft
    cs "Hey Linus?"
    linus "What's up CS? What do you need help with?"
    menu:
        "What does CS need help with?"
        "I want to work on YTPs." (type = "true"):
            jump ytp_edit
        "I want to do reviews":
            jump reviews

label reviews:
    $ fanbase = "ltt"
    cs "I'm up to doing more review videos with you."
    show linus at center with ease
    linus "Sweet! I'll make sure to hit you up for our next video!"
    linus "If you want, you can think of some ideas for next time."
    linus "You should probably head out for now, it's getting late."
    cs "Yeah, I just hope that my community will move on with this new content."
    cs "I've been making Youtube Poops for a while now, so I hope they understand in due time."
    linus "I'm sure you'll be okay, plus the LTT fanbase is much bigger!"
    cs "I guess so."
    n "Before CS can think about this too much, a lot of commotion can be heard at the front of the building."
    show colton at right with moveinright
    colton "Linus! There is a furry outside!"
    linus "What?"
    linus "Hold on, lemme check."
    n "CS and Linus rush to the front door."
    scene frontdoor with fade
    show linus at right with moveinleft
    show cs at center with moveinleft
    n "Linus goes to open the door."
    linus "Who's there? Is anyone here?"
    n "Suddenly, Arceus rushes in through the doors."
    show arceus at mid_right with moveinright
    arceus "CS! There you are! We need to go ASAP!"
    play music "<loop 0>hired_guns.mp3" volume 0.5
    music Hired Guns - Brian Johnston
    linus "CS? You know this person?"
    show cs worried
    cs "It's a long story."
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "WHAT? CS, why are the cops chasing you? This could seriously damage our reputation {size=-10}more than the time I mentioned I dropped hard R's as a kid!"
    menu:
        "What will CS do?"
        "I'm going to stay with LTT." (type = "bad"):
            jump cops_ltt
        "Escape with Arceus.":
            jump arc_escape    
    
label ytp_edit:
    show linus at offscreenright
    cs "I have a question about what I want to do here at LTT."
    n "Linus stands up and walks over to him."
    show linus at center with ease
    linus "Sure. I mean, what do you want to do?"
    cs "I really want to make more YTPs for you guys."
    n "Linus laughs a bit."
    linus "Oh, CS, when I gave you the YTP card that was meant for use on your own channel, not the LTT one."
    cs "I know, but--{w=0.25}{nw}"
    linus "I mean, for example.{w=0.5} TARAN! GET IN HERE!"
    n "Taran rushes up to Linus' office."
    show taran at right with moveinright
    taran "{i}panting{/i} Yes, {w=0.5}Linus? {w=0.5}What is it?"
    linus "Taran, have you ever seen a YTP?"
    taran "Other than the one CS made the other day? Not really."
    linus "See, CS? Not only will our audience be super confused, but our employees will be as well."
    cs "Alright... I see..."

    menu:
        "What will CS do?"
        "Show everyone more YTPs" (type = "true"):
            jump both_fan
        "Ignore them and keep making your own YTPs.":
            jump ytp_fan

label ytp_fan:
    $ fanbase = "ytp"
    cs "Well, I want to keep working on YTPs!"
    show cs angry
    cs "This is like, what I built my life on, and I just..."
    linus "CS? Are you okay? Maybe you should take a chill pill."
    cs "I thought you liked YTPs a lot! You said you hired me because of it!"
    taran "What? You hired him because of that?"
    linus "Look, let's all just calm down okay? If you wanna keep doing YTPs, fine, but if it messes up our company you have to either stop or you're fired."
    cs "Fine!"
    n "Before CS can storm off, Colton rushes in with some info."
    show colton at right with moveinright    
    colton "Linus! There is a furry outside!"
    linus "What?"
    linus "Hold on, lemme check."
    n "CS and Linus rush to the front door."
    scene frontdoor with fade
    show linus at right with moveinleft
    show cs at center with moveinleft
    n "Linus goes to open the door."
    linus "Who's there? Is anyone here?"
    n "Suddenly, Arceus rushes in through the doors."
    show arceus at mid_right with moveinright
    arceus "CS! There you are! We need to go ASAP!"
    play music "<loop 0>hired_guns.mp3" volume 0.5
    music Hired Guns - Brian Johnston
    linus "CS? Seriously?"
    show cs worried
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "WHAT? CS, why are the cops chasing you? This could seriously damage our reputation {size=-10}more than the time I mentioned I dropped hard R's as a kid!"
    jump arc_escape


label both_fan:
    $ fanbase = "both"
    stop music
    music end
    cs "You know what? Why don't you all come down to my office."
    linus "I mean... sure. Let's see what you have in stock."
    linus "Come on guys, let's go!"
    show taran flipped at right
    hide taran with moveoutright
    hide linus with moveoutright
    hide cs with moveoutright
    scene csdesk with fade
    n "Linus gathers more employees as they follow CS to his office."
    show cs at center with moveinright
    show linus at mid_left with moveinright
    show taran at left with moveinright
    show taran flipped at left
    show luke at mid_right with moveinright
    show colton at right with moveinright
    luke "What is this all about Linus? I was just about to go home."
    linus "Boohoo, Luke, you probably don't even do anything at home."
    luke ":("
    colton "Hi guys! What did I miss? I thought we were going to build a streaming machine?"
    linus "Look Colton, we can do that tomorrow."
    cs "Hey guys~ CS Here! Showing you the wonderful world of YTPs!"
    linus "Oh no..."
    colton "A... what?"
    cs "Alright! Strap in because YouTube is where the poop is!"
    show black with fade
    play sound "ytpintro.ogg"
    n "After half an hour passes, CS has shown LTT what YTPs are all about."
    hide black with fade
    cs "Welp. Those are some of the best ones that I could find."
    taran "Hey, those were actually really funny. Linus, didn't you tell me about how much you actually liked YTPs?"
    linus "Nooooo...?"
    luke "Now that you say that..."
    linus "Alright fine! I guess if you all like it too, we could put some on our channel from time to time."
    show cs happy
    cs "Hell yeah!"
    linus "But you still have to help with some other videos as well, not just YTPs."
    show cs
    cs "Alright, that's fair."
    linus "Well, the rest of you can go back to what you were doing."
    colton "Oh yeah, Linus? Before I go, I was told someone was banging on the door to enter just a minute ago."
    colton "They were dressed up like a furry or something."
    linus "Great CS, did you attract your furry fanbase to work here as well?"
    cs "I swear, this doesn't have anything to do with my community."
    linus "Wait, what do you mean? I was just joking about the furry fanbase."
    cs "..."
    linus "Whatever, let's just go check out who it is."
    # TODO: Different room in the LTT office
    scene black with fade

    n "CS and Linus rush to the front door."
    scene frontdoor with fade
    show linus at right with moveinleft
    show cs at center with moveinleft
    n "Linus goes to open the door."
    linus "Who's there? Is anyone here?"
    n "Suddenly, Arceus rushes in through the doors."
    show arceus at mid_right with moveinright
    arceus "CS! There you are! We need to go ASAP!"
    play music "<loop 0>hired_guns.mp3" volume 0.5
    music Hired Guns - Brian Johnston
    linus "So you DO have a furry fanbase who wants to join LTT! Damn it CS, I should've known."
    show cs worried
    cs "Shut up, Linus!"
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "WHAT? CS, why are the cops chasing you? This could seriously damage our reputation {size=-10}more than the time I mentioned I dropped hard R's as a kid!"

    menu:
        "What will CS do?"
        "I'm going to stay with LTT." (type = "bad"):
            jump cops_ltt
        "Escape with Arceus." (type = "true"):
            jump arc_escape

label cops_ltt:
    show cs disappointed
    n "CS thinks long and hard about his decision."
    cs "I'm sorry Arceus, but I finally just got this dream job, and I can't lose it."
    arceus "The cops are almost here CS! If they find you, you won't be able to work anyways!"
    cs "I'm done running Arc. I need to be with LTT."
    arceus "Welp. I tried."
    n "Arc shrugs and walks away, as he goes to escape on his own."
    hide arceus with moveoutright
    linus "CS, what happened with the cops?! I still have no clue what's going on!"
    show cs
    cs "Look okay, so there were these guys from a company called HoH SiS, who do foundation repair."
    cs "My house was in dire need of foundation repair, so I called them up to come help fix my house."
    cs "They also thought I was prank caller because I made that one video about them a long time ago,"
    cs "and they also told me that they changed their policy with payments and I had to pay them immediately."
    cs "When they came over I decided to go visit my friend Michael Rosen, and he had this chocolate cake that actually WASN'T chocolate cake,"
    cs "And then I gave him an energy drink and he went kinda crazy, so I went back home to check on HoH SiS."
    cs "and when I got back home, they-"
    show copguy at mid_right with moveinright
    show cs worried
    copguy "Freeze!"
    n "As CS was explaining his story in extreme detail, the cops showed up in time."
    copguy "You are under arrest! Put your hands in the air!"
    return

label arc_escape:
    cs "Look, I'm sorry Linus, I wish I could explain, but Arceus is right. I need to get going."
    linus "I am like, {i}so{/i} confused and frustrated, this better not ruin LMG."
    show cs disappointed
    cs "I'm sorry guys, I'll try to get you guys caught up after this."
    cs "This is CS, signing out."
    arceus "We have no time for that, CS! We need to go!"
    # TODO: Outside LTT
    scene outside_ltt with determination
    show cs disappointed at left
    show arceus at right
    with moveinright
    n "CS and Arceus run out of the building, and try to find cover while they escape."
    play sound "siren.ogg" loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "As they are making their way further from the building, they can hear sirens grow in volume as flashing lights rush towards the LMG headquarters."
    if fanbase == "ytp":
        cs "Thank god we are getting out of here, Linus didn't like my ideas."
        arceus "Ah dang, that sucks to hear."
    else:
        cs "This is awful, I was just starting to get along well with Linus and the gang."
        arceus "I'm sure they'll forgive you in due time, but for now, we need to evade the cops' trail and get back to the United States."
    stop music fadeout 3.0
    music end
    n "While Arceus and CS were fleeing away from the scene, the cops show up at LTT to investigate."
    scene frontdoor
    stop sound fadeout 4.0
    show linus at left
    show luke at center
    show taran at right
    show colton at mid_left
    n "The employees at LTT are in chaos as the police show up to the front of the building."
    luke "WTF is going on?"
    taran "Linus! What did you do!?"
    linus "Relax guys, it's nothing that we did."
    n "Linus mutters to himself."
    linus "{i}I should've done a background check on CS, it's weird how--{/i}"
    show luke at mid_left
    show taran flipped at mid_mid_left
    show colton at center
    with move
    show copguy at right with moveinright
    n "Copguy bursts in."
    play music "<loop 0>undyne.mp3" volume 0.5
    music Undyne - Toby Fox
    copguy "Alright, everyone! Back against the wall! Nobody move!"
    luke "So, are we moving to the wall or... not moving?"
    copguy "Don't question the police! Just--{w=0.5} stand against the wall!"
    n "The LMG members move toward the wall while more policemen come in and search the place."
    copguy "Alright, I have a very simple question to ask you all."
    copguy "Do you know this man?"
    show cswanted at truecenter with dissolve
    n "Copguy shows a picture of CS to the crew."
    taran "Uhh yeah, that's--"
    hide cswanted
    linus "We don't know who that is at all."
    copguy "Oh really? You there, what did you say about this man?"
    taran "I, uhh..."
    taran "I was saying that..."
    taran "That it looks like Colton! Yeah!"
    colton "What the fuck, Taran!"
    linus "Yep, that looks like Colton, alright."
    copguy "Alright, sir, what's your name?"
    linus "It's Lin-"
    copguy "Yeah okay. Linard, if you say that it's {i}this{/i} man, how can you explain the maid outfit that was used in the video that was just uploaded an hour ago?"
    linus "Well uhh, he's got some... weird kinks..."
    colton "Oh my fucking god."
    copguy "If you are so sure then, lemme go talk to the sheriff about this."
    linus "Sure thing, officer."
    hide copguy with moveoutright
    n "Copguy leaves the scene."
    stop music fadeout 3.0
    music end
    colton "I can't fucking believe you guys! That was way too far!"
    linus "April Fools?"
    colton "IT'S JULY!"
    scene outside_ltt
    n "Copguy orders the rest of the cops to leave the scene and return back to the station."
    show copguy at left with moveinleft
    copguy "Damnit, they don't have CS anymore. We're gonna have to look harder for him."
    scene road_to_canada
    show cs disappointed dusk at left
    show arceus dusk at right
    with fade
    n "Meanwhile, CS and Arc have been running back to the US border."
    cs "Aw man! This is embarrassing!"
    arceus "Yeah, so much for the editing job, I guess."
    cs "I can't seem to get a break this month. First my problems with HoH SiS, now I'm running from the cops?"
    cs "I should've just called another foundation repair company."
    arceus "Yeah, that sounds like hell. {size=-10}You could have called me. I am literally a god."
    cs "It IS hell."
    arceus "I should've known that the cops were going look for us. We didn't hide our tracks too well."
    arceus "I heard about the cops at the last second when I was checking comm chatter around the area. I figured that since you helped me out, I should come back for you."
    cs "Thanks man, I really owe you again."
    arceus "Nah, I owe you."
    scene border_dusk with fade
    show cs dusk at left
    show arceus dusk flipped at mid_left
    play music "<loop 0>atarashii_kaze.mp3" volume 0.3
    music Atarashii Kaze - Satoru Kosaki
    n "CS and Arc approach the border guard again."
    show border_guard dusk at right with moveinright
    border_guard "I'm gonna need proof of--"
    border_guard "Ey, it's you two buds again!"
    arceus "Yeah, quite the vacation we had! We had so much fun in Canada didn't we CS?"
    cs "Yep!"
    border_guard "Alright, hope you two come back to visit the Great White North again, ey buds?"
    arceus "Sure thing!"
    scene washington_road with fade
    n "The duo continue their trek now in the US, in the state of Washington."
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "So, what happened with you?"
    arceus "Hmm?"
    cs "Well, I went to work at LTT, and had to spend my nights at a nearby hotel."
    cs "Linus gave me enough money to make due in time."
    arceus "Wait, which hotel?"
    cs "The Hoto Hoto?"
    arceus "Well, I've been at the same hotel, clearing up ties from my cyber criminal past."
    arceus "I've been in prison for five years, so I've had to figure out what to do again for money."
    stop music fadeout 3.0
    music end
    arceus "Anno's been at the hotel too, I think he's planning on starting some kind of band."
    cs "Ah, I see."
    scene sheriff_office
    play music "<loop 0>police_station.mp3" volume 0.5  
    music Police Station - Lorin Nelson  
    show sheriff at left
    with fade
    n "Back at the police station, Copguy talks to the sheriff about CS."
    show sheriff at left
    show copguy at right with moveinright
    sheriff "Howdy officer Copguy, tell me, you guys arrested CS this evening, right?"
    copguy "Unfortunately, no we did not."
    n "The sheriff slams his desk."
    show sheriff at left with vpunch
    sheriff "Damnit! And how did you fuck that up?"
    copguy "Look, you see, he managed--"
    sheriff "You know what, I don't want to hear this!"
    sheriff "First, they manage to escape from one of our top prisons, and now you're telling me that you lost him?!"
    copguy "Please, this is one of my best cases yet! I need to catch him, and I promise I'll put him back in jail along with those other two!"
    n "The sheriff thinks for a moment."
    sheriff "Alright, since I know you've been pretty good at catching criminals for the past 15 years, I'll let it slide this time."
    sheriff "But believe me, this CS man has a pretty big target on his head, and we need to bring him to justice before him and his gang do anything else funny."
    sheriff "The next time you come back here, he better be with you, or you're fired!"
    copguy "Sure thing, boss. I'll track him down...{w=0.5} on my own."
    hide copguy with moveoutright
    n "Copguy turns around and heads out to track down CS and Arc."
    stop music fadeout 3.0
    music end
    scene washington_road with fade
    n "Meanwhile, CS and Arc are still making their way through the US, without any sense of direction."
    play music "<loop 0>echoing.mp3" volume 0.5
    music Echoing - Banana
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "Hey Arceus? Do you have any clue where we are?"
    arceus "No idea, I'm just following the road. There's bound to be a rest stop here eventually."
    cs "I hope so, we've been walking for hours. It's gotta be midnight around now…"
    #More filler here probably, for now I'm jumping to when copguy comes in
    stop music fadeout 3.0
    music end
    n "CS looks into the distance."
    cs "Hey Arc! I can see some lights in the distance! We gotta be getting close!"
    arceus "Wait a minute, those are--"
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" volume 0.1
    n "Arceus squints into the distance, but CS and Arc both immediately recognize the sounds."
    show cs worried dark
    "CS and Arceus" "SHIT!"
    arceus "Copguy's back! He's probably looking all over for us! What do we do CS?!"
    menu:
        "What do we do CS?!"
        "Fight the cops with YTP Magic" (type = "bad"):
            jump ytp_magic_fight
        "Flee into the forest" (type = "true"):
            jump pussy_out_forest

label ytp_magic_fight:
    show cs concentrate
    n "CS closes his eyes. He starts to concentrate on the sirens and the car."
    play sound "<loop 0>siren.ogg" loop fadein 3.0 volume 0.4
    arceus "CS?!? What are you doing!?"
    play sound "<loop 0>siren.ogg" loop volume 0.5
    arceus "CS!!!! They're heading right at us!!"
    play sound "<loop 0>siren.ogg" loop volume 0.6
    scene black
    arceus "CS!!!!!!!!!!!!"
    play sound "<loop 0>siren.ogg" loop fadein 1.0 volume 2
    pause 1.0
    play sound "car_crash.ogg" volume 0.7
    pause 7.0
    n "CopGuy's car flies off the road and violently crashes into the forest."
    scene washington_road
    show arceus dark at right
    show cs concentrate at left
    with fade
    pause 3.0
    show cs
    pause 1.0
    show cs concentrate
    pause 0.2
    show cs
    pause 1.0
    arceus "CS??? Are you okay?"
    cs "Yeah, I feel really good actually."
    cs "Are we good?"
    arceus "..."
    arceus "I guess so."
    arceus "CopGuy, he..."
    cs "Yeah I took care of him, didn't I?"
    arceus "I guess you did."
    cs "Should we keep going?"
    arceus "Are you not like, phased at all by this?"
    cs "Eh, not really."
    arceus "Alright, well..."
    arceus "Let's keep going..."
    scene black with fade
    scene washington_road with fade
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    play music "<loop 0>killcops.mp3" volume 0.5
    music Echoing? - Banana
    n "The duo continues to travel along the road."
    n "CS talks to himself along the way, with Arceus weary of his actions still."
    cs "{size=-45}39463609346834683806834683068436803806489368389046803864368869034806849368030dsjkweu8yu euyhegw47ithw98gthw39thw389ghw9ghsiughfudghw4u9hfdhsgjdghsdkhsjgjdsgjsdjgsjgsjgjhsdgjsgjs689"
    arceus "CS? What are you saying?"
    cs "Huh? Nothing."
    show arceus dark flipped
    menu:
        "Attack now." (type = "bad"):
            jump attack_arc
        "Wait." (type = "bad"):
            jump wait_arc

label attack_arc:
    cs "{size=-15}It's now or never."
    n "CS channels CSGod."
    hide cs
    show csgod flipped at left
    csgod "Time to die, Arceus!"
    show arceus dark
    stop music
    music end
    show csgod flipped at left with vpunch
    play sound "alt_punch.ogg"
    show csgod at t_punchup with move
    show arceus dark at right with hpunch
    arceus "Really? I've been a god longer than you dummy."
    arceus "Nice try."
    return

label wait_arc:
    cs "{size=-15}I need to wait. I'm not powerful enough to attack."
    arceus "Man, I hope you are doing fine."
    cs "Yep!"
    stop music
    music end
    pause 5.0
    n "The duo walks silently for a few hours, and eventually the sun rises."
    scene washington_road morning
    show arceus at right
    show cs at left
    with fade
    pause 3.0
    arceus "So uhh, should we keep going this direction?"
    cs "..."
    cs "Yep."
    pause 5.0
    scene town
    show arceus at right
    show cs at left
    with fade    
    pause 2.0
    arceus "Hey, we found a town! That's good right?"
    cs "Yep."
    arceus "Dude, are you sure you're okay?"
    arceus "You haven't said anything, like at all for the past several hours."
    cs "I'm fine."
    arceus "...okay."
    arceus "Well uhh, what should we do now?"
    arceus "Are we gonna like, try to get you home?"
    arceus "{size=-4}Do you wanna even go home?"
    cs "Yes yes, let's just wait here."
    arceus "In the middle of the road?"
    arceus "Why?"
    arceus "There is someone coming! Shouldn't we move?"
    pause 1.0
    arceus "Hello?"
    n "All of a sudden, the car driving at them slowly stops."
    n "The man inside gets out of the car."
    show billy at center with moveinright
    billy "Hey that's my car!"
    billy "What are you doing?"
    cs "Take us to these coordinates: 46.5754, -112.3008."
    billy "I uhh,"
    pause 2.0
    billy "No problem!"
    billy "Let's go!"
    scene car background
    show billy car
    pause 5.0
    scene car background night
    show billy car
    with fade
    pause 3.0
    n "For the whole drive, no one says a word."
    scene cultforest
    show billy car
    billy "Welp. We are here."
    n "CS gets out of the car and heads up the trail on the side of the road."
    arceus "Hey uhh, I'm gonna get out too."
    hide billy car with fade
    show arceus flipped at mid_left with moveinleft
    arceus "CS? Where did you go?"
    arceus "What is wrong with him right now?"
    pause 2.0
    arceus "After that the incident with the cops he's been..."
    pause 1.0
    arceus "He's just been-"
    csgod "Stronger than ever."
    show csgod flipped at mid_left with moveinleft
    show arceus flipped at mid_left with vpunch
    play sound "audio/punch.ogg"
    show arceus flipped at mid_left with hpunch
    play sound "audio/punchalt.ogg"
    show arceus flipped at t_punchup with move
    arceus "Ouch."
    show cultist at mid_right with moveinright
    show cultist_2 at right with moveinright
    show cultist_3 at center with moveinright
    cultist "Praise CS God! Praise CS God!"
    n "Billy takes off in an instant after witnessing the event."
    csgod "I have finally harnessed the power of CS God!"
    csgod "Time to take over the world!"
    return


label pussy_out_forest:
    cs "Arceus, quick! Let's escape into the forest!"
    arceus "Alrighty, let's go!"
    hide arceus
    hide cs
    with moveoutright
    scene black with fade
    stop sound fadeout 1.0
    n "CS and Arc quickly jump into the trees next to them."
    n "As CS and Arceus hunker down into the foliage, they see the flash of lights fly past them."
    arceus "Phew! That was a close one, CS!"
    cs "Yeah, it looks like we hid just in time."
    arceus "Alright well, should we wait here for a bit or do you think the coast is clear?"
    jump wait_forest

label wait_forest:
    cs "We should probably wait for a little bit. They might turn around and see us."
    arceus "Yeah, that's a good point. I kinda don't want to risk going back to prison again."
    n "CS and Arc stay quiet in the forest for about 15 minutes before heading back on the road again."
    scene washington_road with fade
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "Hey, Arceus?"
    arceus "Hmm?"
    cs "Now that we are out here and have more time to talk, where exactly are we heading to? Why did we come back to the US?"
    arceus "Well, I figured you wanted to go back home, right?"
    cs "Of course I want to head back home, it's just... it seems so far away."
    cs "We don't really have a car or anything, we are completely lost, and we got the cops still looking for us, probably!"
    arceus "Look man, I know it's pretty hard right now. But we gotta be optimistic about this."
    arceus "The second we find people, I'm sure we can work something out and head back home."
    cs "If you say so, I just hope we don't have to WALK all the way there."
    arceus "I don't think that'll be the case."
    copguy "{cps=10}I don't think so either."
    n "Before CS and Arc can react, they both get the lights knocked out of them."
    play sound "punch.ogg"
    scene black with determination
    n "When CS and Arc wake up, they find themselves in handcuffs leaned up against a cop car."
    scene washington_road
    show cs disappointed dark at left
    show arceus dark flipped at mid_left_left
    with fade
    cs "Huh?"
    cs "What happened?"
    show copguy dark at right with moveinright
    play music "<loop 0>danger_mystery.mp3" volume 0.5
    music Danger Mystery - Toby Fox
    copguy "Hey, you're finally awake."
    arceus "Hey, CS."
    arceus "I'm sorry."
    show cs worried dark
    cs "No no no! This can't be happening!"
    cs "Arceus! Can't you do something about this?"
    arceus "No can do, boss. Looks like this is the end of the line."
    copguy "No time for negotiations, pal. Get in the car."
    scene copcar with fade
    show copguy at t_copguy_frontseat
    show copcar_mask
    with determination
    show arceus at right with moveinleft
    show cs disappointed at left with moveinleft
    n "CS and Arc are thrown into the cop car, as Copguy says some order on his walkie."
    copguy "This is Copguy calling in a 1-8-8 on Compass Road. Sheriff? We got em."
    n "Copguy gets in the car and they head off."
    n "As they are heading away, CS has the urge to say something."
    menu:
        "HoH SiS scammed me" (type = "true"):
            jump good_convince
        "I'm not CS" (type = "bad"):
            jump bad_convince

label bad_convince:
    play music "<loop 0>pressing_pursuit_cornered.mp3" volume 0.3
    music Pressing Pursuit ~ Cornered - Masakazu Sugimori
    play sound "objection.mp3" volume 0.5
    show objection at truecenter with hpunch
    pause 1.0
    hide objection
    cs "Wait a second! I'm not actually CS!"
    cs "I just LOOK like CS!"
    arceus "I mean, he might not be CS?"
    play sound "hold_it.mp3" volume 0.5
    show hold_it at truecenter with hpunch
    pause 1.0
    hide hold_it
    stop music
    music end
    copguy "Nice try, bud. We saw your fake visa and everything. You too are going back to the slammer."
    return

label good_convince:
    show cs worried
    play music "<loop 0>pressing_pursuit_cornered.mp3" volume 0.3
    music Pressing Pursuit ~ Cornered - Masakazu Sugimori
    play sound "objection.mp3" volume 0.5
    show objection at truecenter with hpunch
    pause 1.0
    hide objection
    cs "Wait a second! The reason all this happened was because HoH SiS sabotaged my computer!"
    arceus "Wait, what?"
    copguy "What are you on about?"
    cs "Yes! HoH SiS scammed me out of thousands of dollars to get my foundation fixed, and they also broke my laptop!"
    cs "So afterwards, I wanted to get my revenge!"
    copguy "I'm not believing this for a second."
    copguy "You really thought I would fall for some silly little lie?"
    play sound "hold_it.mp3" volume 0.5
    show hold_it at truecenter with hpunch
    pause 1.0
    hide hold_it
    arceus "Actually, I have proof of this."
    arceus "CS just raised a good point, and I can show you."
    copguy "And HOW can you prove this? Where is your evidence?"
    n "Arceus pulls up a laptop that he managed to grab from the front seat."
    copguy "WHAT? How did you get that?"
    arceus "Watch this."
    show black with fade
    n "Copguy stops the car as Arceus plays back the scene from {i}CS Bounciness I{/i} with the scamming of CS by HoH SiS."
    scene copcar
    show copguy at mid_left
    show copcar_mask
    show arceus at right
    show cs disappointed at left
    with dissolve
    cs "How--"
    arceus "I have my ways."
    copguy "I don't understand, so HoH SiS really did scam you hard, didn't they?"
    copguy "I'm not sure how valid it was for you to push that man off a building..."
    copguy "But I can't argue right now on if that footage is fake or not."
    stop music fadeout 3.0
    music end
    n "Copguy gets out of the car."
    n "He then proceeds to open the doors and let them out, freeing them of their shackles."
    scene washington_road with fade
    show copguy dark at right with moveinleft
    show cs disappointed dark at left with moveinleft
    show arceus dark flipped at mid_left_left with moveinleft
    copguy "Listen, I really shouldn't be doing this right now, but I have to go back to look into this deal with HoH SiS."
    copguy "You are free to go for now."
    copguy "But know this: I'm putting my job on the line over this."
    copguy "Don't do anything stupid, because I have my eye on you two!"
    n "Copguy gets back into his car, and heads off into the dead of night."
    hide copguy with moveoutright
    show arceus dark flipped at mid_right_right with move
    show arceus dark at mid_right_right
    show cs dark
    n "CS and Arc look at each other, and smile."
    play music "<loop 0>bun_guster.mp3" volume 0.3
    music Bun Guster - Satoru Kōsaki
    arceus "Holy crap, I didn't think that would work."
    cs "Me neither! I'm so glad that they let us go!"
    cs "I don't know how you got that footage, but we are now free once again!"
    arceus "Hooray for CS and Arc!"
    show cs dark at center
    show arceus dark at center 
    with move
    show cs dark at mid_left_left
    show arceus dark at mid_right_right
    with move
    n "They both high five, and continue heading in the direction of the road."
    stop music fadeout 3.0
    music end
    jump choose_direction

#Chapter 2 for True Ending 1 starts here
label choose_direction:
    scene black with determination
    n "As the duo continues their journey through the night, they soon have to figure out exactly where to go."
    scene washington_road morning
    play music "<loop 0>happy_roaming.mp3" volume 0.5
    music Happy Roaming - Lorin Nelson
    show cs at left
    show arceus at right
    cs "We've been walking all night, I'm exhausted."
    arceus "Yeah, let's hope we find food and water soon."
    cs "Hey uhh, do you know exactly where we're going?"
    arceus "Well, I noticed that the sun set in our opposite direction, which means we're heading east right now."
    arceus "We can head in any direction really. The second we find a better form of transportation than walking, we're taking it."
    menu:
        "Which way do you want to go?"
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west 

label north:
    cs "What if we go north?"
    arceus "...What?"
    show cs disappointed
    cs "You said pick a direction!"
    arceus "To the north is Canada. Where we just came from. Try again."
    show cs
    menu:
        "North":
            jump north2
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west 

label north2:
    $ achievement_manager.unlock("Can We Go Back?")
    arceus "I literally just said-"
    arceus "Just pick another direction."
    menu:
        "North":
            jump north2
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west 

label west:
    cs "I think we should go west."
    arceus "Alright, we can try."
    n "CS and Arc run into the Pacific Ocean."
    scene washington_road day
    show cs at left
    show arceus at right
    arceus "It's just the ocean. Let's go another direction."
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west2

label west2:
    cs "Let's try going west again. I'm sure there is something there."
    arceus "Uhm, okay... Maybe we've missed something."
    n "CS and Arc run into the Pacific, again."
    scene washington_road dusk
    show cs dusk at left
    show arceus dusk at right
    arceus "Still just the ocean..."
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west3

label west3:
    cs "Nah come on, there is definitely SOMETHING we can find west."
    arceus "I really don't want to go there again..."
    cs "Nah, we got this, for sure this time."
    n "CS and Arc find a cool looking crab, but still just the ocean again."
    scene washington_road
    show cs dark at left
    show arceus dark at right
    cs "Hey! that's quite an epic crustacean!"
    arceus "Alright cool, can we pick another direction that ISN'T west this time?"
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west4

label west4:
    cs "Okay! One last time!"
    arceus "... Something tells me you were in an asylum for a bit..."
    n "CS and Arc surprisingly, find the ocean again."
    scene washington_road morning
    show cs at left
    show arceus at right
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west5

label west5:
    arceus "..."
    scene washington_road day
    show cs at left
    show arceus at right
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west6

label west6:
    arceus "..."
    scene washington_road dusk
    show cs dusk at left
    show arceus dusk at right
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west7

label west7:
    arceus "..."
    scene washington_road
    show cs dark at left
    show arceus dark at right
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west8

label west8:
    $ achievement_manager.unlock("Ocean Man")
    arceus "Player. {w=0.5}Stop. {w=0.5}Going. {w=0.5}West."
    scene washington_road morning
    show cs at left
    show arceus at right
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west5

label south:
    cs "I'm too fucking tired to think of what's south."
    arceus "Yeah, same."
    cs "Did you know that the Halifax Disaster was the biggest manmade non-nuclear explosion?"
    arceus "What?"
    cs "I don't know man, I'm too fucking tired to thhhhhhhinkkkk brooo"

label east:
    cs "Well since east is the way home, we should probably go that way."
    arceus "Alright, that sounds like a good idea."
    n "CS and Arc keep following the road for a while, until they come across a small town."
    scene town with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    cs "Oh my god! We found civilization again!"
    arceus "Thank God."
    n "The two look around for a bit, when they see a gas station close by."
    cs "Let's head over to that gas station, so we can pick up some food."
    n "CS and Arc head over to the convenience store at the gas station."
    hide cs with moveoutright
    hide arceus with moveoutright
    scene gasinside with fade
    show cs at left with moveinleft
    show arceus at right with moveinright
    arceus "Finally, some good fucking food."
    cs "Donuts and chips have never tasted better."
    arceus "Thank god the slushie machine was working for once."
    cs "Okay, now that we can think about something other than food, what's our plan to get home?"
    arceus "Yeah, I have no clue currently."
    arceus "I was hoping that we could like hitchhike on a bus or something, but it might be ages until that happens... If it even DOES happen, this town is small enough as is."
    stop music fadeout 3.0
    music end
    menu:
        "Wait for driver at the gas station" (type = "true"):
            jump billy_driver
        "Hotwire a car" (type = "bad"):
            jump hotwire

label hotwire:
    cs "I don't know, we could just, hotwire a car?"
    arceus "I can probably do that, let's go look."
    scene gasoutside with fade
    show cs at left with moveinleft
    show arceus at right with moveinleft
    n "CS and Arc approach one of the cars in front of the gas station."
    n "Arceus smashes open the window and opens the door from the inside."
    arceus "Alright, so if we connect this to this..."
    n "The car starts up."
    cs "Hell yeah! Let's go home!"
    n "All of a sudden, flashing lights and sirens show up behind them."
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" volume 0.5
    show copguy at center with moveinleft
    show cs disappointed
    copguy "I heard the sound of a car window breaking from miles away!"
    copguy "You guys already blew it! Back to the slammer!"
    return

label billy_driver:
    cs "Why don't we just wait for someone at the gas station to come out, and then we ask them for an Uber?"
    n "CS walks over to someone's car parked in the front of the gas station."
    scene gasoutside with fade
    show cs at left with moveinleft
    show arceus at right with moveinleft
    arceus "Are you crazy? To drive all the way back to New York? In a stranger's car at that."
    arceus "Besides, how are we even going to pay the guy anyways?"
    cs "Well we don't have to go all the way to New York, we could go a small distance and then get another Uber."
    arceus "That would be even more money in tips!"
    n "As the two are agruing, the owner of the car comes up to them."
    "???" "What are you doing next to my car?"
    cs "Oh, hi."
    cs "Do you think you can Uber us to New York?"
    "???" "Oh uhh, hold on a second."
    n "The mysterious driver walks behind the store."
    arceus "What are you doing? That man looks like he's going to kill us!"
    arceus "He's probably getting a gun, we need to lea--"
    show billy at center with moveinleft
    play music "<loop 0>mm_select.mp3" volume 0.3
    music Mm Select - Matthew Simmonds
    billy "Hi, Billy Mays here for the Uber Driver!"
    billy "The fast and easy way to get people around who don't have a car!"
    show cs happy
    cs "Sweet! We need to get to upstate New York, do you think you can help us?"
    billy "Absolutely! For only $19.95, I'll take you both to New York!"
    cs "Alright well, it's settled! We have our driver, Arceus!"
    arceus "..."
    arceus "... What the fuck. Works for me I guess."
    cs "Hell yeah! I call shotgun!"
    n "CS and Arc get into Billy's car."
    stop music fadeout 3.0
    music end
    hide cs with moveoutright
    hide billy with moveoutright
    hide arceus with moveoutright
    jump in_billy_car

label in_billy_car:
    scene carback1
    show billy car
    play music "<loop 0>billy_radio.mp3" volume 0.3
    music Billy Mays Gangsta Remix - mastamokei
    cs "Alright so, it's just a straight shot to New York?"
    show billy car turn
    billy "Yep! We are gonna head through Idaho and Montana first, so get ready to see the sights!"
    show billy car happy
    cs "Yeah! It's almost like a vacation!"
    arceus "Well on a vacation, you usually have money to spend on all the crazy parts you see."
    cs "Let's just enjoy the ride there at least."
    arceus "Fair point."
    stop music fadeout 3.0
    music end
    jump montana

label montana:
    scene car background
    show billy car
    n "After a few hours of driving, the trio currently is located in the middle of Montana."
    n "Arceus is sleeping, while CS peers out the window."
    cs "Are we there yet?"
    billy "Nope!"
    cs "Aw man..."
    show billy car turn
    billy "We still got a ways to go, we aren't even a quarter of the way yet."
    show billy car
    cs "Alright, I'll just, keep looking at the trees pass by."
    billy "Well good news for you, there is a small town up ahead."
    billy "I was gonna buy some new supplies for my gadgets, if you guys want to pick out anything."
    cs "Sure! I love buying random things!"
    cs "What about you Arceus?"
    cs "Hey, Arc!"
    billy "CS, you should probably leave the dog thing alone in the back."
    n "Arceus immediately jerks straight up."
    arceus "What did you just call me?"
    billy "Nothing!"
    scene hardwareoutside
    show billy car
    billy "Here we are, at the store. I'll be back here in a few."
    cs "Same, I'll come with you."
    n "Arceus falls back to sleep in the car."
    play sound "doorslam.ogg"
    scene black with fade
    scene hardwareinside with fade
    play music "<loop 0>home_depot.mp3" volume 0.4
    music "Let's Do This - Home Depot"
    show cs at left with moveinleft
    cs "Wow look at all this stuff!"
    cs "They've got Allen wrenches, gerbil feeders, toilet seats, electric heaters{nw}"
    cs "Trash compactors, juice extractor, shower rods and water meters{nw}"
    cs "Walkie-talkies, copper wires, safety goggles, radial tires{nw}"
    cs "BB pellets, rubber mallets, fans and dehumidifiers{nw}"
    cs "Picture hangers, paper cutters, waffle irons, window shutters{nw}"
    cs "Paint removers, window louvres, masking tape and plastic gutters{nw}"
    cs "Kitchen faucets, folding tables, weather stripping, jumper cables{nw}"
    cs "Hooks and tackle, grout and spackle, power foggers, spoons and ladles{nw}"
    cs "Pesticides for fumigation, high-performance lubrication{nw}"
    cs "Metal roofing, water proofing, multi-purpose insulation{nw}"
    cs "Air compressors, brass connectors, wrecking chisels, smoke detectors{nw}"
    cs "Tire gauges, hamster cages, thermostats and bug deflectors{nw}"
    show cs worried
    cs "Trailer hitch demagnetizers, automatic circumcisers{nw}"
    show cs
    cs "Tennis rackets, angle brackets, Duracells and Energizers{nw}"
    cs "Soffit panels, circuit breakers, vacuum cleaners, coffee makers{nw}"
    cs "Calculators, generators, matching salt and pepper shakers{nw}"
    cs "and I think that's it..."
    cs "Ooh! Look at all this paint!"
    cs "Let's get some orange, blue, purple,"
    show cs happy
    cs "More colors, I need more colors!"
    show billy at right with moveinright
    show cs
    billy "You ready to go, CS?"
    cs "Yep! Let's check out and keep going!"
    billy "Where is the cashier in this store? I didn't see anyone..."
    show cashier at center with moveinbottom
    show cs worried
    show cashier with hpunch
    cashier "I gotcha covered. Have a good day!"
    hide cashier with moveoutright
    cs "Letsgoletsgoletsgoweneedtogetoutofhere"
    hide cs at moveoutright
    hide billy at moveoutright
    stop music fadeout 3.0   
    music end
    scene black with fade
    play sound "doorslam.ogg"
    scene hardwareoutside
    show billy car
    with fade
    billy "That was quite the experience, I should've brought my Hercules Hook!"
    cs "Yeah really, let's get out of here!"
    arceus "Huh? What's going on?"
    cs "Nothing Arc, just, uh, slipped and fell in the store."
    arceus "Okay whatever, I'm going back to sleep..."
    n "Billy takes off out of the parking lot."
    scene black with fade
    scene car background night
    show billy car
    with fade
    cs "Man, today was pretty crazy too."
    arceus "Yeah, at least I got some sleep after all of it."
    cs "Speaking of which, can we find a place to rest soon?"
    billy "Yeah, let's see if I can find a place to stop at."
    billy "Wait a second, what the hell?"
    n "Billy brings the car to a screeching halt."
    scene cultforest
    show billy car
    play music "<loop 0>candle_world.mp3" volume 0.4
    music Candle World - Kikiyama
    "CS and Arceus" "What in the world?"
    n "Ahead lies a barricade with a bunch of strange hooded people surrounding it."
    show cultist at mid_right behind billy with moveinright
    n "One of the members walks up to the driver's side and knocks on the window."
    n "Billy rolls down the window."
    billy "Hi, it's Billy! What are you doing by my car?"
    cultist "Get out of the car."
    billy "No, it's my car!"
    n "The cultist pulls out a revolver and aims at Billy's head."
    cultist "Does this like a joke to you guys?"
    cultist "Out of the car. Now."
    n "Billy shrugs and opens the door, with the cultist leader still aiming the gun to his head."
    cultist "You two as well, out."
    n "CS and Arceus both step out of the car."
    hide cultist with moveoutright
    hide billy car with fade
    show billy at mid_mid_left
    show cs disappointed at mid_left
    show arceus flipped at left
    with moveinleft
    show cultist at mid_right with moveinright
    cultist "So, do you want to explain what is going on here?"
    cs "Uhm, we were heading on past here to the next-"
    n "The cultist aims his gun at CS."
    cultist "Look, I don't care where you are going."
    show cultist at center with moveinleft
    cultist "We are part of the Blue Branch Cult, and our motto is that we hate everything."
    arceus "Like, everything?"
    n "The cultist aims at Arceus."
    cultist "You wanna fuck with me?"
    arceus "I mean. If you're offering."
    n "The cultist looks annoyed."
    cultist "I'm gonna get the rest of the gang to deal with you guys, don't fucking move."
    hide cultist with moveoutright
    show cultist at right with moveinright
    cultist "I mean it!"
    hide cultist with moveoutright
    show cultist at right with moveinright
    cultist "Okay?"
    hide cultist with moveoutright
    pause 2.0
    hide billy with moveoutleft
    n "Billy goes to the back of his trunk and starts digging around."
    arceus "Never thought we'd run into cultists out of all people."
    hide cs with moveoutleft
    n "CS starts digging around in the back too."
    arceus "CS, what are you doing?"
    arceus "CS?!"
    show cs fakegod at center with moveinleft
    cs "Look at me! I'm purple!"
    $ renpy.music.set_pause(True, "music")
    play sound "secret/funni.ogg" volume 0.5
    pause 3.0
    stop sound
    $ renpy.music.set_pause(False, "music")
    arceus "CS, what the fuck are you doing...?!"
    arceus "You are going to definitely get us killed!"
    n "Arceus hides behind the car as the cultist leader brings two others with him."
    hide arceus with moveoutleft
    show cs fakegod at left with moveinleft
    show cultist_2 at mid_mid_right with moveinright
    show cultist_3 at right with moveinright
    show cultist at mid_right with moveinright
    cultist "Alright, they are over here at this car."
    cultist_2 "No way..."
    cultist_3 "It's CSGod!"
    cultist_2 "Praise CSGod!"
    cultist "Oh no! It's the one thing that we don't hate!"
    cs "Huh?"
    cs "I mean,"
    cs_fakegod "Yeah that's right it's me, CSGod."
    cs_fakegod "You better leave these three alone, or I'll uh, smite you!"
    cultist "CSGod doesn't smite, he uses YTP mag-{w=0.5}"
    cs_fakegod "Don't tempt your god, I will YTP you so hard that you'll look like you came from an AwfulFawful YTP!"
    cultist_2 "We need to leave! We're sorry!"
    n "Billy comes up behind CS with one of his gadgets."
    show billy at mid_left with moveinleft
    stop music fadeout 1.0 
    play music "<loop 0>blazing_corridor.mp3" volume 0.4    
    billy "Fire a laser! Fire a laser!"
    hide cultist_2 with moveoutright
    n "Massive laser shots land between the cultists as they scramble away!"
    cultist_3 "I don't wanna turn into a YTP! Go guys go!"
    hide cultist_3 with moveoutright
    hide cultist with moveoutright
    n "The cultists disappear into the forest."
    stop music fadeout 3.0 
    music end
    billy "That's the power of the Awesome Augement!"
    play music "<loop 0>showtime.mp3" volume 0.4
    music "It's Showtime - Toby Fox"
    show cs fakegod at center with moveinright
    cs "Hooray! I'm a god now!"
    show arceus flipped at left with moveinleft
    arceus "CS, I don't know how you pull this stuff off."
    arceus "Am I still sleeping?"
    n "Arceus pinches himself."
    arceus "Fuck."
    arceus "How many divine beings and reality benders do we have in this universe anyhow?"
    cs "Alright, back on the road to New York!"
    stop music fadeout 3.0
    music end
    scene car background night
    show billy car
    with fade
    n "The gang gets back in the car and books it out of the forest."
    n "After a while of driving, Billy pulls the car into a small area off the forest to let everyone rest."
    scene black with fade
    n "After the night passes, they set off again on their trip."
    scene car background
    show billy car
    play music "<loop 0>mort_farm.mp3" volume 0.4
    music "Mort's Farm - ClascyJitto"
    cs "Can we stop somewhere to eat? We haven't eaten since yesterday."
    arceus "Yeah unfortunately the one store you guys went to didn't have anything edible."
    billy "Sure yeah, there's a McDonald's up here in a couple miles."
    scene mcdonalds
    show billy car
    n "Billy pulls up through the drive-thru to place his order."
    cashier "Hello, what you like to order?"
    billy "Hi, Billy Mays here! I would like to get the Buy 1 Get 1 Free breakfast meal for my friends here,"
    billy "and I would also like to get the egg McMuffin and a Big Mac for me."
    cashier "Sure thing, that'll be-{nw}"
    billy "But I'm not done yet! I would like to triple the offer and get 3 Big Macs, and also 3 large sodas without any shipping!"
    cashier "Uhh, yeah, we can do that without shipping."
    cashier "That'll be about, let's see..."
    cashier "$36.88."
    billy "Wow! What a deal! I'm coming around to pick up my order!"
    scene black with fade
    n "Billy drives through and picks up his meal."
    scene mcdees
    show billy car
    with fade
    n "CS and Arc happily chow down on the Mickey D's they just got."
    arceus "Thank god for that."
    cs "I have never been so excited to get a Big Mac."
    scene car plains
    show billy car
    with fade
    n "Billy heads out on the open road again, as they enter the state of South Dakota."
    jump south_dakota

label south_dakota:
    arceus "Welcome to the Great Plains."
    cs "Woohoo!"
    stop music fadeout 3.0
    music end
    arceus "I don't think you should be super excited, there is like, nothing here."
    cs "Oh yeah, we don't even have trees to look at anymore."
    cs "Is there anything to do in this state?"
    arceus "There's Mount Rushmore, I guess there's Wall Dr-{w=0.5}"
    cs "Oh hell yeah! Let's go to Mount Rushmore!"
    scene black with fade
    n "In about an hour, the crew arrives at Mount Rushmore."
    scene rushmore with fade
    n "They all hike up to the viewing spot to get a good look of the founding fathers."
    play music "<loop 0>taiikusai_desu_yo.mp3" volume 0.4
    music Taiikusai Desu Yo - Satoru Kōsaki
    show cs at right with moveinleft
    show arceus at center with moveinleft
    show billy at left with moveinleft
    billy "Wow, to think that we won a war without the Gopher."
    billy "How did they even communicate without the Jupiter Jack?"
    show cs concentrate
    arceus "It'd be cool if I had my face carved out into a mountain. Wouldn't that be cool, CS?"
    show arceus flipped at center
    n "Arceus looks over at CS concentrating on something really hard."
    arceus "CS? Are you okay?"
    show arceus flipped at mid_right with moveinleft
    n "As Arceus starts to approach CS, the groups surrounding them all gasp loudly."
    scene csmore
    show cs concentrate at right
    show arceus at center
    show billy at left
    with hpunch
    arceus "Huh?"
    show cs happy
    cs "There we go! Fixed!"
    n "Arceus looks back at Mount Rushmore, now with CS, Arceus, and Billy's face on the mountain."
    hide cs with moveoutright
    arceus "You scare me, CS. I don't even like, want to question how or why."
    arceus "{size=-12}I do look pretty cool though."
    stop music fadeout 3.0
    music end
    n "The gang gets back in the car before the overwelming groups of people engulf the site after what just happened."
    scene car plains
    show billy car
    with fade
    n "They continue to drive through the massive and empty plains of South Dakota."
    play music "<loop 0>track4.mp3" volume 0.4
    music Track 4 - Weatherscan
    n "By the time they reach Sioux City, it is already evening."
    cs "There really is nothing out here, is there?"
    arceus "Nope. I don't get how people can even live here."
    billy "We're like halfway through the Midwest, we've only got a couple states left to travel before we are in the heartland."
    n "Billy follows the Missouri River down until they hit Omaha."
    jump nebraska

label nebraska:
    scene omaha
    show billy car
    with fade
    n "The gang finally hits Omaha, right before it hits nighttime."
    cs "This is the biggest city here? This is pretty small."
    billy "It looks very quaint, hopefully we can find a place to stop here."
    billy "I have no damn clue where to go here."
    arceus "Let's get out and look for somewhere to eat."
    hide billy car
    show cs at mid_left
    show arceus at center
    show billy at mid_right
    show pakoo at offscreenleft
    with moveinleft
    n "They all get out and start roaming the streets."
    n "Suddenly, CS hears a voice behind him."
    "???" "CS? Is that you?"
    cs "Huh?"
    show cs flipped
    stop music fadeout 3.0
    music end
    n "CS turns around and sees a wacky...{w=0.5} thing, with a tophat on."
    show pakoo at left
    show billy at right
    show arceus at mid_right
    show cs flipped at center
    with ease
    pakoo "Yeah hey, it {i}is{/i} you!"
    pakoo "Arceus, you too? And, Billy... Mays?"
    billy "Hi, it's Billy!"
    arceus "Hey, Pakoo."
    cs "Yeah! I haven't seen you in a while, I never thought you'd live in this place!"
    pakoo "I never thought you guys would come down to Omaha, there's like, nothing here."
    cs "We've been through a lot recently, do you know somewhere we can eat and rest for the night?"
    n "Pakoo thinks for a moment."
    pakoo "I think I know a place."
    n "Pakoo takes the gang over to the old market section of Omaha."
    hide pakoo
    hide cs
    hide billy
    hide arceus flipped
    with easeoutright
    scene alleyway with fade
    show pakoo at center
    show billy at right
    show cs at left
    show arceus flipped at mid_left
    with moveinleft
    pakoo "Here we are, this is probably the best location to eat at, at least that I know of."
    scene black with fade
    scene peppinopizzabg
    show peppinopizzafg
    with fade   
    play music "<loop 0>funiculi_holiday.mp3" volume 0.3
    music Funiculi Holiday - ClascyJitto
    show peppino at mid_mid_left behind peppinopizzafg with moveinleft
    show peppino at pepzone behind peppinopizzafg with move
    show pakoo at mid_right with moveinleft
    show billy at right with moveinleft
    show cs at left with moveinleft
    show arceus flipped at mid_left with moveinleft
    peppino "Hey Piezanos, watcha want today?"
    pakoo "Hey Peppino, can you get me and my friends the Gustavo special today?"
    show peppino2 at pepzone behind peppinopizzafg
    hide peppino
    peppino "Sure-a thing-a! Coming right up!"
    show peppino at pepzone behind peppinopizzafg
    hide peppino2
    pakoo "Also, do you think my friends here can be spend the night? They don't have anywhere to sleep tonight."
    peppino "The room in the back should be fine, Mr. Stick is out right now, so they can bunk there."
    pakoo "Alright, epic."
    n "Peppino serves the group their pizza."
    cs "Damn, this is some good pizza!"
    arceus "Probably some of the best pizza I've ever had."
    billy "Better than my restaurant mini-burgers!"
    pakoo "Alright well, I should get going, but I hope y'all have a good time doing whatever y'all doing."
    cs "Yep! Take care, Pakoo!"
    hide pakoo with moveoutleft
    scene black with fade
    stop music fadeout 3.0
    music end
    n "The gang goes into the backroom area and sleeps for the night."
    n "Once they wake up, they thank Peppino for his business and head out."
    jump iowa

label iowa:
    scene car plains
    show billy car
    with fade  
    n "They get back in car and continue into Iowa."
    billy "Alright well, ever since that cult encounter, it's been pretty smooth sailing!"
    billy "The rest of this trip shouldn't be too long!"
    n "As if on queue, a strange sound is heard over the car."
    n "CS looks out the window."
    play music "<loop 0>speedy_comet.mp3" volume 0.5
    music Speedy Comet - Mahito Yokota
    cs "You have to be kidding me!"
    arceus "What's going on?"
    cs "HoH SiS is back!"
    arceus "WHAT?!"
    billy "Who?"
    cs "They have their UFO and--"
    n "A huge laser beam blasts on the left side of the road, ripping up everything in it's path!"
    play sound "minigames/car/gaster_blast.wav"
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car
    arceus "Shit, this is bad..."
    cs "Billy, you need to switch lanes when it charges up!"
    jump play_cargame

label after_ufo:
    scene car plains
    show billy car
    with fade
    stop music fadeout 3.0
    music end
    cs "Holy shit! We made it!"
    arceus "That was some good driving Billy!"
    billy "That's the power of the 6000 pound car!"
    n "They continue driving through the end of the Midwest."
    scene car plains night
    show billy car
    with fade
    n "As they are drving through Illinois, they pass by Chicago."
    arceus "One day, I'm gonna rule that place."
    cs "What are you... talking about?"
    arceus "It's better than ruling the Earth."
    cs "Get some sleep, Arc."
    scene black with fade
    n "The gang stops in Indiana for the night, and takes off in the morning through Michigan."
    jump michigan

label michigan:
    jump ohio

label ohio:
    scene car plains
    show billy car
    with fade
    n "After that fiasco, they travel through Ohio."
    show scott_border
    play music "<loop 0>breakout.mp3" volume 0.3  
    music Breakout - Shoichiro Sakamoto 
    n "Suddenly, a huge blue border enters everyone's vision."
    arceus "Oh what in the world? There is some red border in my eyes..."
    cs "I have a blue one, what is going on?"
    billy "Yeah, it's blue for me too, I think you are colorblind."
    arceus "I AM colorblind. Oh fuck."
    scene wozniaktroubles
    show billy car
    show scott_border
    with fade
    n "As they are driving through the state, they see some men on the side of road protesting about the blue border."
    billy "Hi, it's Billy!"
    billy "Are you tired of having a blue border in your vision?"
    billy "You should try Kaboom!"
    n "Billy pulls out a bottle of Kaboom and sprays them in the face."
    scott "Ahhhhh!"
    billy "It gets the tough stains out!"
    terry "I'm sorry that doesn't seem very vegan, I'll have to just deal with it."
    cs "Billy, I don't think that'll work, let's just keep going."
    scene car plains
    show billy car
    show scott_border
    with fade
    n "Once they leave the state, the border goes away."
    stop music fadeout 3.0
    music end
    hide scott_border with dissolve
    arceus "I'm glad it just faded away, I did not want to spray cleaner in my eyes."
    jump pennsylvania

label pennsylvania:
    n "The gang hits the last state before New York, Pennsylvania."

    jump car_dialogue

label back_home:
    scene cs_house with fade
    play music "<loop 0>park_theme.mp3" volume 0.5
    music Park Theme - Lorin Nelson
    n "After the long and treacherous journey, CS finally arrives at his house."
    show arceus flipped at left with moveinleft
    arceus "We made it back to your house, CS!"
    show cs flipped at center with moveinright
    cs "Finally I'm home..."
    cs "Arceus, thank you so much for everything on this trip. I couldn't have done it without you."
    arceus "Aw, it was nice helping ya here."
    cs "You too, Billy."
    show billy at mid_left with moveinleft
    billy "No problem!"
    cs "Well, I guess I should get some rest."
    cs "If you guys want, we can have a party at my place tomorrow to celebrate all the shit we went through!"
    "Arc and Billy" "Hell yeah!"
    hide billy with moveoutleft
    hide arceus with moveoutleft
    n "As CS was saying bye to his friends, a familiar but upsetting voice can be heard at the front of CS' house."
    stop music fadeout 1.0
    music end
    ed "YOU!"
    show cs disappointed at left with moveinleft
    n "CS and the gang look forth at CS' front porch, where Richard and Ed are waiting angrily for him."
    play music "<loop 0>hohsisremix.mp3" volume 0.5
    music "Alfred's Theme - Eminem"
    show ed at right with moveinright
    show rich at mid_right behind ed with moveinright
    ed "I have been waiting for you for quite some time now."
    rich "We've been trying to stop you for a while now, but this is final stop for you."
    cs "HoH SiS?? What do you guys still want from me?"
    ed "What do you think, CS? After you put Wesley in the hospital? After you crippled most of our workers?"
    cs "Well, you guys scammed me out of my money and broke my computer! Of course I wanted some kind of revenge!"
    ed "Why do you think this all started?"
    cs "I--{w=0.5} I don't know, because you're evil?"
    ed "CS, you put our company to shame long ago."
    ed "When you made that paraody video of us that you call a \"YTP\", people wouldn't stop harrassing us about it."
    rich "You tried to humiliate us with your videos, with others thinking we were a joke."
    ed "You see, my ancestors came from the planet JoJ many years ago to live here and start a foundation company."
    ed "It was the best damn foundation company in the world."
    ed "We repaired more than 50%% of all foundations on the planet, and now... you."
    ed "You. You embarrassed us with those silly, stupid, videos that dragged our family company through the mud."
    rich "That's why Ed wanted to get revenge on you. That's why we destroyed your computer, CS."
    cs "I don't understand..."
    menu:
        "Fight" (type = "bad"):
            jump fighthohsis
        "Negotiate" (type = "true"):
            jump talktohohsis
        "Fuck up" (type = "bad"):
            jump fuckuphohsis
        "Call CopGuy":
            jump copsathohsis

label talktohohsis:
    cs "I never intended to harm your company, I just thought that the video was a good source to YTP."
    cs "I'm sorry about all those prank callers, I even made a video telling people to stop prank calling you."
    cs "I never had bad intentions for you guys... honestly it was also kind of like a free promotion."
    ed "Well, I'm sorry CS, but it's too late."
    ed "Richard, get the JoJ UFO and vaporize the house."
    stop music fadeout 1.0
    show anno at offscreenleft
    play music "<loop 0>track3.mp3" volume 0.4
    music Track 3 - Weatherscan
    "???" "Wait!!!"
    n "A voice can be heard behind the group running up to them."
    cs "Anno?"
    show anno at center behind doug with moveinleft
    anno "You guys can't just destroy CS' house!"
    ed "Why not?"
    anno "I don't know, because..."
    anno "CS wasn't trying to harm you!"
    show arceus flipped at mid_left_left with moveinleft
    arceus "Yeah, CS' videos are hilarious, and honestly if I knew you guys before this I would've called you up for help on my house."
    arceus "If y'know, I didn't go after that one politican."
    ed "Well okay, but--"
    n "Even more of CS' friends show up at the scene."
    show cs at left
    show linus at mid_left behind phil with moveinleft
    linus "Yeah, I loved those videos about HoH SiS, and we'd love for you to come up fix up some of the damages at the LTT offices."
    show taran flipped at mid_mid_left behind cs with moveinleft
    show luke at mid_left_left behind cs with moveinleft
    show colton at default behind doug with moveinleft
    taran "What damages?"
    luke "Y'know, when Linus ran his car into the back of the building?"
    colton "Finally, something that wasn't my fault."
    show michael at mid_mid_left behind cs with moveinleft
    michael "If I get my chocolate cake, you fellows at HoH SiS can fix up my house too."
    show phil at mid_left behind cs with moveinleft     
    phil "I can help too, with the power of Flex Tape!"
    show doug at center behind cs with moveinbottom
    doug "I don't know what I'm doing here, but yeah, good job guys!"
    show cashier at mid_mid_right behind cs with moveinleft
    cashier "Yeah! Go CS!"
    show border_guard at mid_mid_left behind cs with moveinleft
    border_guard "I'm important too, eh!"
    cs "Wow, I don't know how you all got here coincidently, but I appreciate it!"
    show cs at left
    rich "Oh my god, that's so many people!"
    ed "Okay okay, I get it."
    hide anno
    hide arceus flipped
    hide linus
    hide taran flipped
    hide luke
    hide colton
    hide michael
    hide phil
    hide doug
    hide cashier
    hide border_guard
    with moveoutleft
    ed "We won't do anything to your house, and we are sorry for destroying your laptop."
    cs "And I'm sorry for injuring your coworkers."
    stop music fadeout 3.0
    music end
    ed "Wesley is still in the hospital, so like, if you wanted to, give us some more money..."
    show cs disappointed at left
    cs "Didn't you scam me out of more money than my foundation was worth?"
    ed "Oh yeah..."
    show cs angry at left
    cs "What {i}about{/i} my foundation as well?"
    show cs at left
    cs "Tell you what: if you can fix my foundation, I'll pay you for that, and we put this all behind us."
    rich "What do you think, Ed?"
    n "Ed ponders for a moment."
    ed "Sure. We have a deal."
    show cs happy at left
    cs "Hooray!"
    n "As if the crowd couldn't get any bigger, the cops show up."
    show cs at left
    show copguy at center with moveinleft
    copguy "Hey CS, we finally found HoH SiS."
    copguy "And it looks like you did too."
    show sheriff at mid_left with moveinleft
    sheriff "Goodjob Copguy, time to put them in the slammer!"
    cs "No need guys, we worked everything out."
    sheriff "What?!"
    copguy "Are you sure?"
    ed "Yep, we got everything under control."
    sheriff "All this for nothing..."
    sheriff "Whatever, c'mon Copguy, let's go."
    n "The cops get back in their car and speed off."
    hide sheriff with moveoutleft
    hide copguy with moveoutleft
    hide ed with moveoutright
    hide rich with moveoutright
    show cs at mid_right with moveinright
    n "After all that commotion, CS finally steps up to his front door."
    show cs flipped at mid_right
    n "CS looks back out into the crowd again one more time."
    cs "This is CS..."
    cs "Signing out!"
    play sound "cheers.ogg" volume 0.7
    pause 2.0
    n "The crowd errupts in cheers as CS finally enters his house."
    scene cs_room with fade
    play music "<loop 0>ac_title.mp3" volume 0.4
    music New Leaf Title Theme - Kazumi Totaka
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    if fanbase == "both":
        jump true_ending
    elif fanbase == "ltt":
        jump ltt_ending
    elif fanbase == "ytp":
        jump ytp_ending
    else:
        jump secret

label true_ending:
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor that has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have to work with us again virtually, just give us a call\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys! CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    "Chat" "Yeah what happened to you?{w=0.25} Oh my god, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs happy at mid_left
    cs "Well guys..."
    n "CS chuckles."
    cs "It's a long story..."
    scene black with fade
    stop music fadeout 1.0   
    play music "secret/credits.mp3" volume 0.5
    centered "Pretend there's credits here."
    jump secret2

label ytp_ending:
    n "CS looks over at his desk, where his old computer is sitting."
    scene cs_room_2 with fade
    show cs at mid_left
    cs "Oh yeah, I forgot I actually have a computer that's not a craptop."
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys! CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    "Chat" "Yeah what happened to you?{w=0.25} Oh my god, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well guys..."
    n "CS chuckles."
    cs "It's a long story..."
    scene black with fade
    stop music fadeout 1.0   
    play music "secret/credits.mp3" volume 0.5
    centered "Pretend there's credits here."
    jump secret2

label ltt_ending:
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with fade
    n "CS looks at the monitor that has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have to work with us again virtually, just give us a call\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys! CS here! Sorry I was gone for a couple weeks!"
    n "The chat slowly comes in, confused."
    "Chat" "Oh you're streaming?{w=0.25} I thought you were working for LTT now?{w=0.25} What happened to the YTPs?{w=0.25} Are you OK?{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well guys..."
    cs "It's a long story..."
    scene black with fade
    stop music fadeout 1.0   
    play music "secret/credits.mp3" volume 0.5
    centered "Pretend there's credits here."
    jump secret2

label fighthohsis:
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
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show cs with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show ed with vpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show cs with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show ed with vpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show cs with hpunch
    play sound "alt_punch.ogg"
    show cs at t_punchup with move
    show cs with vpunch
    show ed at right with move
    hide cs
    pause 2.0
    show cs disappointed at mid_left with moveintop
    cs "I no longer want the joj..."
    hide cs with moveoutbottom
    show ed with hpunch
    ed "Time to take a shit on the house."
    return

label fuckuphohsis:
    show cs angry
    cs "Yeah I actually hate you guys, and I wanted to mess with your business!"
    cs "You guys suck and I hate you both!"
    cs "You guys deserve to have your company in shambles!"
    n "Richard and Ed back up to their UFO."
    hide rich
    hide ed
    with moveoutright
    cs "Hey! Where are you guys going!"
    cs "Come back here!"
    n "The JoJ UFO flies up over the house and vaporizes the house."
    play sound "beam.ogg" volume 0.6
    show beam at xstretch_in
    pause 3.0
    show beam at xstretch_out
    pause 1.0
    scene cshouse_vaporized
    show cs disappointed at left
    with vpunch
    n "Ed flips CS off, and then flies away."
    show cs disappointed
    pause 1.0
    cs "Fuck."
    return    

label copsathohsis:
    n "CS calls Copguy to come arrest HoH SiS."
    show cs worried
    stop music fadeout 1.0
    music end
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" loop volume 0.5
    show copguy at center with moveinleft
    cs "Here they are! They scammed me out of my money and services!"
    n "Copguy cuffs the HoH SiS members and pulls out his walkie."
    copguy "We got them, sheriff. Time to bring them to the slammer."
    hide copguy
    hide rich
    hide ed
    with moveoutright
    stop sound fadeout 1.0
    hide blue_light
    hide red_light
    show cs
    cs "Welp. That was easy."
    cs "Finally, I can rest at home."
    n "CS walks up to his house and enters."
    scene cs_room with fade
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    jump true_ending

label high_gpu:
    jump secret

