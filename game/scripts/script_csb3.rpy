label csbiii_start:
    $ persistent.csb3a_unlocked = True
    stop music fadeout 3.0
    scene outside_ltt with fade
    show cs at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene inside_ltt with fade
    play music "<loop 0>passport.mp3" volume 0.5
    music PASSPORT.MID - George Stone
    show linus at center with moveinright
    linus "Welcome to Linus Media Group! Come on in. I'll show you to your desk."
    cs "Thanks, Linus."
    scene black with fade
    n "Linus and CS walk to CS' new desk."
    scene csdesk with fade
    show linus at right with moveinright
    show cs at left with moveinleft
    cs "Wow! I thought this was a starting office. Why do I get such a cool desk?"
    linus "Actually, this is our worst setup. You'll get upgraded after you've been here for a while."
    cs "Holy shit, really? This is way better than any setup I've seen, let alone {i}had.{/i}"
    linus "You must've had really bad setups then. This only has a 3080. Everyone else has 3090s or 4080s."
    cs "I have absolutely no problem with a 3080."
    linus "Well, enjoy!"
    hide linus with moveoutright
    cs "I guess I'd better get to work on editing. Let's see what videos I need to edit..."
    cs "Let's see, I have the new TechQuickie video on how livestreaming works, or the video on how at least half of the keys on your keyboard should be macros..."
    if persistent.true_ending:
        menu:
            "Hold a meeting?"
            "Yes":
                jump csbiii_ai
            "No"  (type = "true"):
                pass
    show cs worried
    cs "Damn it, Taran, you can edit your own macro fetish content."
    show cs
    cs "I guess I'll edit the livestreaming one."
    scene black with fade
    n "CS starts working on editing the TechQuickie video, and after some time, Linus comes in to check on him."
    scene csdesk
    show cs at left
    with fade
    show linus at right with moveinright
    linus "Hey, CS, how's the new video coming along?"
    cs "It's going well! I have the background all done, and I'm working on adding graphics and fixing audio."
    linus "Wow! You're a fast worker. You'll get off of that old 3080 in no time."
    cs "Thanks, Linus."
    linus "Speaking of livestreaming, we need a new PC for the WAN Show. Can you go and buy parts for one?"

    menu: 
        "What are you going to do?"
        "Go to the store.":
            jump microcenter
        "Help edit a video." (type = "true"):
            jump edit_video

label edit_video:
    cs "Nah, I wanna finish this project first. That way I can help you pump out videos faster."
    linus "Alright, that's fine. I'll probably send Colton to get the parts instead. He's good at sucking up and doing this kinda thing."
    cs "Alright, yeah. I definitely wasn't using this as an excuse to get out of shopping!"
    linus "...okay? Whatever, just keep editing."
    cs "Yeah, no, don't worry, I've got this."
    hide linus with moveoutright
    n "Linus leaves the room."
    stop music fadeout 3.0
    music end
    cs "Hmm, this video looks pretty great so far. I'm practically done at this point."
    cs "I wonder what the others will think of this. I should probably get opinions from some of the other employees."
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
    cs "Thanks! I guess my many years of video editing are finally paying off after all."
    taran "They definitely have."
    taran "You know what? I think this video is so good, I don't even think Linus needs to check this."
    taran "He'll be so surprised when you upload it. He's gonna wonder how you put it together so well in such little time."
    show cs
    cs "You really think so? I mean, I don't want him to be upset with me."
    taran "Don't worry about it. If he thinks it's that bad, I'll take the blame on it."
    cs "That's nice and all, but do you think that's a good idea? I mean, I don't want to mess up my first chance at this."
    taran "Nah, don't worry about it."
    taran "Even if something dumb happens, he usually never gets mad at us for doing silly things like that."
    cs "Well, if you say so, I guess it's fine."
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
    cs "Well, I guess since this video is already good enough, I can upload it now."
    cs "It's so crazy having the ability to access the LTT channels. There's so much crazy shit going on here!"
    cs "Oh well. Time to upload this."
    n "CS pauses for a moment."
    cs "I don't know. I really feel like I shouldn't upload this yet."
    cs "It doesn't feel complete. Something is missing from it..."
    cs "Lemme go look at the project file and run through the video again."
    n "Just as CS was about to watch his video, an idea kicked in."
    cs "I got it! I know exactly what to do!"
    cs "If Taran really does mean what he says about Linus, then I'm sure he'll love this!"
    cs "I'm gonna turn this video into a YTP!"
    cs "It will be perfect! No one will expect it because they probably don't even know what I did with my life for the past 13 years!"
    cs "As always, I should make sure it's as good as possible so at least Linus will enjoy it, along with his fans."
    cs "But I also don't have much time before Linus comes back and notices, so I need to hurry!"
    cs "Welp, time to get to work!"
    scene black with dissolve
    music Supernova - Laszlo
    minigame "play_editgame" "boost" "fired"

label fired:
    $ renpy.movie_cutscene("movies/mymovie_cs.webm")
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
    linus "Look, I don't care how much you really wanted to humiliate me. Just leave."
    cs "I don't understand, I didn't think you would be this upse--{w=0.25}{nw}"
    linus "Just get out of here you stupid dumb animal!!"
    cs "..."
    n "CS turns around and stomps out of the building."
    show cs angry flipped with hpunch
    hide cs with moveoutleft
    scene black with fade
    jump new_plan

label boost:
    $ renpy.mark_label_seen("play_edit_game")
    $ renpy.movie_cutscene("movies/good_cs_ytp.webm")
    scene black
    centered "The next day."
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
    cs "Oh shoot, it was awful, wasn't it?"
    cs "Yeah, I should've realized my style is too crazy. I guess I should leave..."
    show cs disappointed flipped at left
    show linus behind cs at left with ease
    show linus at center with ease
    n "As CS turns around, Linus gives him a friendly punch in the back."
    play music "<loop 0>airport_counter.mp3" volume 0.5
    music Airport Counter - Kazumi Totaka
    linus "Dude, what are you talking about? That video was {i}awesome!{/i}"
    show cs at left
    cs "Woah, wait! You actually {i}like{/i} YTPs?"
    linus "Yeah, man! You think I just hired you on the spot because of your obviously fake visa?"
    linus "I love your videos! I've been secretly hoping you would YTP one of mine for the longest time!"
    show linus at left with ease
    show linus at center with ease
    show cs happy
    n "CS' frown fades into a big grin as they both high five."
    cs "Hell yeah! I never would've thought that YTPs would help me in a business setting, let alone with a boss who enjoys them!"
    cs "Alright! Well, I guess I'd better get back to poopin'!"
    show cs flipped at left
    show cs flipped at offscreenleft with ease
    n "Before CS heads out of the room, Linus shouts to him."
    linus "Hey, later today, I've got a big surprise to show you. I'll stop by your office and we can check it out!"
    cs "Sure thing!"
    scene csdesk
    show cs at center
    with fade
    n "When CS gets back to his setup, he starts letting his mind race with ideas."
    cs "Oh, man... where do I even start now?"
    cs "I have so many ideas of videos to poop. I could even try to teach Linus how to YTP..."
    cs "I mean, with the amount of tech he drops on a daily basis, he kinda already {i}is{/i} a YTP."
    cs "Alright, well, back to editing!"
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
    cs "{i}Woah, shi--{/i}{w=0.5}you scared the crap out of me!"
    show cs
    linus "Hah, sorry, I'm just excited to show you this!"
    n "Linus holds out a rectangular box with bold black lettering. It reads, {b}DO NOT USE.{/b}"
    show cs disappointed
    cs "Umm, you sure this is the right box? It literally says--"
    linus "Yeah, I know what it says, I just wrote this on here so no one {i}else{/i} uses it."
    linus "Don't worry, I didn't, like, buy it from some creepy dude at a garage sale who claims it's haunted."
    n "CS looks unnerved."
    linus "Look, just... open the box. I'm sure you'll like it."
    n "CS cautiously takes the box and opens the top. "
    show ytx at truecenter
    n "Inside is what looks to be a graphics card, but with a brown YouTube logo engraved into the side."
    show cs
    cs "Woah, what is this, Linus? A YouTube-brand graphics card?"
    linus "Not exactly. It's an experimental piece of hardware that we have never used before, and it's custom-made."
    n "Linus holds the card into the air."
    linus "Behold! {w=0.5} The-- WOAH SHIT {w=0.5}{nw}"
    show ytx at t_linus_drop_tips
    pause 0.35
    show linus with vpunch
    n "Linus loses grip of the card as it tumbles down onto the table next to him."
    hide ytx
    n "CS facepalms while Luke can be heard laughing in the background."
    cs "Goodness, Linus, you should maybe not do that next time."
    linus "Yeah, I'm sorry. Maybe {i}you{/i} should hold it." 
    linus "This card is called the YTX-9001 Ti, a PCI add-in for enhancing and optimizing YouTube Poops."
    n "CS' eyes widen."
    cs "Wait, whaaat? That's awesome! How does this even work?"
    linus "We don't even know. We haven't even tested it yet."
    linus "It also apparently has poop-tracing, which I'm especially curious about."
    cs "Well, what are we waiting for? Let's get this thing hooked up!"
    n "Linus and CS take apart CS' PC and put the card in."
    n "They then start the computer, and everything boots up as normal."
    linus "Alright, now that it's up and working, we need to install the drivers. The card came with a flash drive that includes them."
    n "As Linus inserts the flash drive, a window off the side of the screen pops up saying \"Your new Peeforce Experience drivers are available.\""
    n "CS chuckles a bit."
    show cs happy
    cs "\"Peeforce\"? I must admit, even these driver names are a bit silly."
    n "Linus laughs."
    linus "If you want, we can wipe them later."
    cs "Wipe! Now {i}you're{/i} in on it!"
    n "They both laugh as the drivers install, and once they're finished, CS boots up Premiere."
    scene csvideo with fade
    cs "Alrighty, let's see here. Why don't we try this on that YTP I just made?"
    linus "Go to the settings real quick, and find the YTP features. Turn YTP mode on to allow the poop-tracing."
    cs "Alright, here goes nothing."
    n "A loading bar appears as the timeline starts shifting, creating different edits in the process."
    cs "Holy crap! This is amazing! It optimized every part of my YTP!"
    linus "That's pretty cool, but let's try it on a completely new source."
    linus "Open the video that we just took yesterday."
    n "CS opens the video, and enables YTP ON again. Before CS's eyes, edits are already starting to be made to the source."
    linus "And, hey, if you don't like the edits it makes, you can always turn it off or tweak the settings in that tab."
    scene csdesk
    show cs at left
    show linus at right
    with fade
    cs "Wow, thank you so much for this, Linus!"
    linus "No problem! This was my gift to you. Now, we should make a review video of it before the day ends."
    cs "Sure thing. Let's take the card out real quick."
    scene ltt_bg
    show ltt_fg
    with fade
    show cs at t_cs_ltt behind ltt_fg with moveinleft
    show linus at t_linus_ltt behind ltt_fg with moveinright
    n "Linus goes and gets the cameras set up, and they start to film the video."
    linus "These days, video editing can be so difficult and tedious. Lately, the YouTube algorithm has been demanding more from us content creators."
    linus "Which is why today we have brought along our newest employee, long-term YouTube Pooper cs188 for this review of the new YTX-9001!"
    cs "Hey guys, CS here! The YTX-9001 is a fantastic card, and we can't wait to show you all of its features!"
    linus "Much like we can't wait to show you this segue to our sponsor!"
    n "The two stand for a moment awkwardly staring at the camera."
    linus "...Go ahead and cut."
    cs "Who knew recording could be so stressful. I could use a drink. The lights are so bright."
    if fun_value(15):
        linus "Here. Take this water bottl-- oops!"
        n "Linus drops the water bottle on the ground."
        cs "You really have butter fingers with everything, Linus."
    else:
        linus "Here. Take this water bottle, it will keep you hydrated and your water cool. lttstore.com"
        cs "...Linus, we aren't filming..."
        linus "Sorry. Force of habit."
    n "Some time passes and they finish the recording."
    n "Afterwards, CS goes up to Linus' office."
    jump ltt_decide

label ltt_decide:
    scene loffice with fade
    show cs at left with moveinleft
    cs "Hey, Linus?"
    linus "What's up, CS? What do you need help with?"
    menu:
        "What does CS need help with?"
        "I want to work on YTPs." (type = "true"):
            jump ytp_edit
        "I want to do reviews.":
            jump reviews

label reviews:
    $ fanbase = "ltt"
    cs "I'm up to doing more review videos with you."
    show linus at center with ease
    linus "Sweet! I'll make sure to hit you up for our next video!"
    linus "If you want, you can think of some ideas for next time."
    linus "You should probably head out for now. It's getting late."
    cs "Yeah, I just hope that my community will move on with this new content."
    cs "I've been making YouTube Poops for a while now, so I hope they understand in due time."
    linus "I'm sure you'll be okay. Plus, the LTT fanbase is much bigger!"
    cs "I guess so."
    n "Before CS can think about this too much, a lot of commotion can be heard at the front of the building."
    show colton at mid_right with moveinright
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
    show arceus worried at mid_right with moveinright
    arceus "CS! There you are! We need to go, ASAP!"
    play music2 "<loop 0>hired_guns.mp3" volume 0.5
    music Hired Guns - Brian Johnston
    linus "CS? You know this person?"
    show cs worried
    cs "It's a long story."
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "{i}What{/i}? CS, why are the cops chasing you? This could seriously damage our reputation {size=-10}more than the time I mentioned I dropped hard R's as a kid!"
    menu:
        "What will CS do?"
        "I'm going to stay with LTT." (type = "bad"):
            jump cops_ltt
        "Escape with Arceus.":
            jump arc_escape
    
label ytp_edit:
    show linus at offscreenright
    cs "I have a question about my job here at LTT."
    n "Linus stands up and walks over to him."
    show linus at center with ease
    linus "Sure. I mean, what do you want to do?"
    cs "I really want to make more YTPs for you guys."
    n "Linus laughs a bit."
    linus "Oh, CS, when I gave you the YTP card, that was meant for use on your own channel, not the LTT one."
    cs "I know, but--{w=0.25}{nw}"
    linus "I mean, for example...{w=0.5} TARAN! GET IN HERE!"
    n "Taran rushes up to Linus' office."
    show taran at right with moveinright
    n "Taran is panting and out of breath."
    taran "Yes, {w=0.5}Linus? {w=0.5}What is it?"
    linus "Taran, have you ever seen a YTP?"
    taran "Other than the one CS made the other day? Not really."
    linus "See, CS? Not only will our audience be super confused, but our employees will be as well."
    cs "Alright... I see..."

    menu:
        "What will CS do?"
        "Show everyone more YTPs." (type = "true"):
            jump both_fan
        "Ignore them and keep making your own YTPs.":
            jump ytp_fan

label ytp_fan:
    $ fanbase = "ytp"
    cs "Well, I want to keep working on YTPs!"
    stop music fadeout 3.0
    music end
    show cs angry
    cs "This is, like, what I built my life on, and I just..."
    linus "CS? Are you okay? Maybe you should take a chill pill."
    cs "I thought you liked YTPs a lot! You said you hired me because of it!"
    taran "What? You hired him because of that?"
    linus "Look, let's all just calm down, okay? If you wanna keep doing YTPs, fine, but if it messes up our company you have to either stop, or you're fired."
    cs "Fine!"
    n "Before CS can storm off, Colton rushes in with some info."
    show colton at mid_right with moveinright    
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
    show arceus worried at mid_right with moveinright
    arceus "CS! There you are! We need to go ASAP!"
    play music2 "<loop 0>hired_guns.mp3" volume 0.5
    music Hired Guns - Brian Johnston
    linus "CS? Seriously?"
    show cs worried
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "{i}What?{/i} CS, why are the cops chasing you? This could seriously damage our reputation {size=-10}more than the time I mentioned I dropped hard R's as a kid!"
    menu:
        "What will CS do?"
        "I'm going to stay with LTT." (type = "bad"):
            jump cops_ltt
        "Escape with Arceus." (type = "true"):
            jump arc_escape


label both_fan:
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
    scene csdesk with fade
    n "Linus gathers more employees as they follow CS to his office."
    show cs flipped at center with moveinright
    show cs with determination
    show linus at mid_left with moveinright
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
    show black with fade
    play sound "ytpintro.ogg"
    n "Half an hour passes, and CS has shown LTT what YTPs are all about."
    hide black with fade
    cs "Welp. Those are some of the best ones that I could find."
    taran "Hey, those were actually really funny. Linus, weren't you telling me about how much you actually {i}liked{/i} YTPs?"
    linus "Nooooo...?"
    luke "Now that you say that..."
    linus "Alright, fine! I guess if you all like it too, we could put some on our channel from time to time."
    show cs happy
    $ achievement_manager.unlock("Crowd Pleaser")
    cs "Hell yeah!"
    linus "But you still have to help with some other videos as well, not just YTPs."
    show cs
    cs "Alright, that's fair."
    linus "Well, the rest of you can go back to what you were doing."
    colton "Oh, yeah, Linus? Before I go, I was told someone was banging on the door to enter just a minute ago."
    colton "They were dressed up like a furry or something."
    linus "Great, CS, did you attract your furry fanbase to work here as well?"
    cs "I swear, this doesn't have anything to do with my community."
    linus "Wait, what do you mean? I was just joking about the furry fanbase."
    cs "..."
    linus "Whatever, let's just go check out who it is."
    scene black with fade

    n "CS and Linus rush to the front door."
    scene frontdoor with fade
    show linus at right with moveinleft
    show cs at center with moveinleft
    n "Linus goes to open the door."
    linus "Who's there? Is anyone here?"
    n "Suddenly, Arceus rushes in."
    show arceus worried at mid_right with moveinright
    arceus "CS! There you are! We need to go, ASAP!"
    play music2 "<loop 0>hired_guns.mp3" volume 0.5
    music Hired Guns - Brian Johnston
    linus "So you {i}do{/i} have a furry fanbase who wants to join LTT! Damn it, CS, I should've known."
    show cs worried
    cs "Shut up, Linus!"
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "{i}What?{/i} CS, why are the cops chasing you? This could seriously damage our reputation {size=-10}more than the time I mentioned I dropped hard Rs as a kid!"

    menu:
        "What will CS do?"
        "I'm going to stay with LTT." (type = "bad"):
            jump cops_ltt
        "Escape with Arceus." (type = "true"):
            jump arc_escape

label cops_ltt:
    stop music
    scene frontdoor
    show linus at right
    show arceus worried at mid_right
    show cs disappointed
    n "CS thinks long and hard about his decision."
    cs "I'm sorry, Arceus, but I finally just got this dream job, and I can't lose it."
    arceus "The cops are almost here, CS! If they find you, you won't be able to work anyway!"
    cs "I'm done running, Arc. I need to be with LTT."
    arceus "Welp. I tried."
    n "Arceus shrugs and walks away as he goes to escape on his own."
    show arceus flipped with determination
    hide arceus flipped with moveoutright
    linus "CS, what happened with the cops?! I still have no clue what's going on!"
    show cs
    cs "Look, okay, so there were these guys from a company called HoH SiS, who do foundation repair."
    cs "My house was in dire need of foundation repair, so I called them up to come help fix my house."
    cs "They also thought I was a prank caller because I made that one video about them a long time ago,"
    cs "and they also told me that they changed their policy with payments and I had to pay them immediately."
    cs "When they came over, I decided to go visit my friend Michael Rosen, and he had this chocolate cake that actually {i}wasn't{/i} chocolate cake,"
    cs "and then I gave him an energy drink, and he went kinda crazy, so I went back home to check on HoH SiS."
    cs "And when I got back home, they--"
    show copguy at mid_right with moveinright
    show cs worried
    copguy "Freeze!"
    n "As CS was explaining his story in extreme detail, the cops showed up."
    copguy "You are under arrest! Put your hands in the air!"
    stop music2 fadeout 3.0
    music end
    bad_end "Stupid CS! You dropped\nyour lore in front of the hoes!" "ltt_decide"

label arc_escape:
    cs "Look, I'm sorry, Linus. I wish I could explain, but Arceus is right. I need to get going."
    linus "I am, like, {i}so{/i} confused and frustrated. This better not ruin LMG."
    show cs disappointed
    cs "I'm sorry, guys. I'll try to get you guys caught up after this."
    cs "This is CS, signing out."
    arceus "We have no time for that, CS! We need to go!"
    scene outside_ltt with dissolve
    show cs disappointed flipped at left
    show arceus at right
    with moveinright
    show cs disappointed at left
    n "CS and Arceus run out of the building and try to find cover while they escape."
    play sound "siren.ogg" loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "As they are making their way further from the building, they can hear sirens grow in volume as flashing lights rush towards the LMG headquarters."
    if fanbase == "ytp":
        cs "Thank God we are getting out of here, Linus didn't like my ideas."
        arceus "Ah dang, that sucks to hear."
    else:
        cs "This is awful. I was just starting to get along well with Linus and the gang."
        arceus "I'm sure they'll forgive you in due time, but for now, we need to evade the cops' trail and get back to the United States."
    stop music2 fadeout 3.0
    music end
    n "While Arceus and CS are fleeing away from the scene, the cops show up at LTT to investigate."
    scene frontdoor
    stop sound fadeout 4.0
    show linus at left
    show luke at center
    show taran at right
    show colton at mid_left
    n "The employees at LTT are in chaos as the police show up to the front of the building."
    luke "WTF is going on?"
    taran "Linus! What did you do?!"
    linus "Relax, guys, it's nothing that we did."
    n "Linus mutters to himself."
    linus "{i}I should've done a background check on CS. It's weird how--{/i}"
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
    taran "Uhh, yeah, that's--"
    hide cswanted
    linus "We don't know who that is at all."
    copguy "Oh, really? You there, what did you say about this man?"
    taran "I, uhh..."
    taran "I was saying that..."
    taran "That it looks like Colton! Yeah!"
    colton "What the fuck, Taran?!"
    linus "Yep, that looks like Colton, alright."
    copguy "Alright, sir, what's your name?"
    linus "It's Lin-"
    copguy "Yeah, okay. Linard, if you say that it's {i}this{/i} man, how can you explain the maid outfit that was used in the video that was just uploaded an hour ago?"
    linus "Well, uhh, he's got some... weird kinks..."
    colton "Oh my fucking God."
    copguy "If you are so sure then, lemme go talk to the sheriff about this."
    linus "Sure thing, officer."
    show copguy flipped
    hide copguy with moveoutright
    n "Copguy leaves the scene."
    stop music fadeout 3.0
    music end
    colton "I can't fucking believe you guys! That was way too far!"
    linus "April Fools?"
    colton "{bt=a3-p10-s4}IT'S JULY!"
    scene outside_ltt
    n "Copguy orders the rest of the cops to leave the scene and return back to the station."
    show copguy flipped at left with moveinleft
    copguy "Damn it, they don't have CS anymore. We're gonna have to look harder for him."
    scene road_to_canada
    show cs disappointed dusk at left
    show arceus dusk at right
    with fade
    n "Meanwhile, CS and Arceus have been running back to the US border."
    cs "Aw, man! This is embarrassing!"
    arceus "Yeah, so much for the editing job, I guess."
    cs "I can't seem to get a break this month. First my problems with HoH SiS, now I'm running from the cops?"
    cs "I should've just called another foundation repair company."
    arceus "Yeah, that sounds like hell."
    cs "It {i}is{/i} hell."
    arceus "{size=-10}You could have called me. I am literally a god."
    arceus "I should've known that the cops were going look for us. We didn't hide our tracks too well."
    arceus "I heard about the cops at the last second when I was checking comms chatter around the area. I figured that since you helped me out, I should come back for you."
    cs "Thanks, man. I really owe you again."
    arceus "Nah, I owe you."
    scene border_dusk
    show cs dusk at left
    show arceus dusk flipped at mid_left
    with fade
    play music "<loop 0>atarashii_kaze.mp3" volume 0.3
    music Atarashii Kaze - Satoru Kosaki
    n "CS and Arceus approach the border guard again."
    show border_guard dusk at right with moveinright
    border_guard "I'm gonna need proof of--"
    border_guard "Ey, it's you two buds again!"
    arceus "Yeah, quite the vacation we had! We had so much fun in Canada, didn't we, CS?"
    cs "Yep!"
    border_guard "Alright, hope you two come back to visit the Great White North again, ey buds?"
    arceus "Sure thing!"
    scene washington_road with fade
    n "The duo continues their trek now in the US, in the state of Washington."
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "So, what happened with you?"
    arceus "Hmm?"
    cs "Well, I went to work at LTT, and had to spend my nights at a nearby hotel."
    cs "Linus gave me enough money to make do in time."
    arceus "Wait, which hotel?"
    cs "The Hoto Hoto?"
    arceus "Well, I've been at the same hotel, clearing up ties from my cybercriminal past."
    arceus "I've been in prison for five years, so I've had to figure out what to do again for money."
    stop music fadeout 3.0
    music end
    arceus "Anno's been at the hotel, too. I think he's planning on starting some kind of band?"
    cs "Ah, I see."
    scene sheriff_office
    show sheriff at left
    with fade
    play music "<loop 0>police_station.mp3" volume 0.5
    music Police Station - Lorin Nelson  
    n "Back at the police station, Copguy talks to the sheriff about CS."
    show sheriff at left
    show copguy at right with moveinright
    sheriff "Howdy, officer Copguy. Tell me, you guys arrested CS this evening, right?"
    copguy "Unfortunately, no, we did not."
    n "The sheriff slams his desk."
    show sheriff at left with vpunch
    sheriff "Damn it! And how did you fuck {i}that{/i} up?"
    copguy "Look, you see, he managed--"
    sheriff "You know what, I don't want to hear this!"
    sheriff "First, they manage to escape from one of our top prisons, and now you're telling me that you {i}lost{/i} him?!"
    copguy "Please, this is one of my best cases yet! I need to catch him, and I promise I'll put him back in jail along with those other two!"
    n "The sheriff thinks for a moment."
    sheriff "Alright, since I know you've been pretty good at catching criminals for the past 15 years, I'll let it slide this time."
    sheriff "But believe me, this CS man has a pretty big target on his head, and we need to bring him to justice before he and his gang do anything else funny."
    sheriff "The next time you come back here, he'd better be with you, or you're fired!"
    copguy "Sure thing, boss. I'll track him down...{w=0.5} on my own."
    show copguy flipped
    hide copguy with moveoutright
    n "Copguy turns around and heads out to track down CS and Arceus."
    stop music fadeout 3.0
    music end
    scene washington_road with fade
    n "Meanwhile, CS and Arceus are still making their way through the US without any sense of direction."
    play music "<loop 0>echoing.mp3" volume 0.5
    music Echoing - Banana
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "Hey, Arceus? Do you have any clue where we are?"
    arceus "No idea, I'm just following the road. There's bound to be a rest stop here eventually."
    cs "I hope so. We've been walking for hours. It's gotta be midnight around now..."
    stop music fadeout 3.0
    music end
    n "CS looks down the road."
    cs "Hey, Arc! I can see some lights in the distance! We've gotta be getting close!"
    arceus "Wait a minute, those are--"
    show blue_light at left
    show red_light at right
    play sound "<loop 0>siren.ogg" volume 0.1
    n "Arceus squints into the night, but CS and Arceus both immediately recognize the sounds."
    show cs worried dark
    show arceus worried dark
    "CS and Arceus" "{i}Shit!"
    arceus "Copguy's back! He's probably looking all over for us! What do we do, CS?!"
    jump forest_menu
label forest_menu:
    scene washington_road
    show cs worried dark at left
    show arceus worried dark at right
    show blue_light at left
    show red_light at right
    menu:
        "What do we do, CS?!"
        "Fight the cops with YTP Magic" (type = "bad"):
            jump ytp_magic_fight
        "Flee into the forest" (type = "true"):
            jump pussy_out_forest

label ytp_magic_fight:
    show cs concentrate dark
    n "CS closes his eyes. He starts to concentrate on the sirens and the car."
    play sound "<loop 0>siren.ogg" loop fadein 3.0 volume 0.4
    arceus "CS?! What are you doing?!"
    play sound "<loop 0>siren.ogg" loop volume 0.5
    arceus "CS!!!! They're heading right for us!!"
    play sound "<loop 0>siren.ogg" loop volume 0.6
    scene black
    arceus "CS!!!!!!!!!!!!"
    play sound "<loop 0>siren.ogg" loop fadein 1.0 volume 2
    pause 1.0
    play sound "car_crash.ogg" volume 0.7
    pause 7.0
    n "Copguy's car flies off the road and violently crashes into the forest."
    scene washington_road
    show arceus worried dark at right
    show cs concentrate dark at left
    with fade
    pause 3.0
    show cs dark
    pause 1.0
    show cs concentrate dark
    pause 0.2
    show cs dark
    pause 1.0
    arceus "CS?? Are you okay?"
    cs "Yeah, I feel really good, actually."
    cs "Are we good?"
    arceus "..."
    arceus "I guess so."
    arceus "Copguy, he..."
    cs "Yeah, I took care of him, didn't I?"
    arceus "I guess you did."
    cs "Should we keep going?"
    arceus "Are you not, like, phased at all by this?"
    cs "Eh, not really."
    arceus "Alright, well..."
    arceus "Let's keep going..."
    scene washington_road with fade
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    play music2 "<loop 0>killcops.mp3" volume 0.5
    music Echoing? - Banana
    n "The duo continues to travel along the road."
    n "Arceus is wary of CS' actions as he can't help but notice CS muttering to himself as they walk."
    cs "{chaos}TmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXAsIG5ldmVyIGdvbm5hIGxldCB5b3UgZG93biwgbmV2ZXIgZ29ubmEgcnVuIGFyb3VuZCBhbmQgZGVzZXJ0IHlvdS4KTmV2ZXIgZ29ubmEgbWFrZSB5b3UgY3J5LCBuZXZlciBnb25uYSBzYXkgZ29vZGJ5ZSwgbmV2ZXIgZ29ubmEgdGVsbCBhIGxpZSwgYW5kIGh1cnQgeW91fg=="
    arceus "CS? What are you saying?"
    cs "Huh? Nothing."
    show arceus dark flipped
    menu:
        "Attack now." (type = "bad"):
            jump attack_arc
        "Wait." (type = "bad"):
            jump wait_arc

label attack_arc:
    stop music
    scene washington_road
    show cs dark at left 
    show arceus dark flipped at right
    $ achievement_manager.unlock("No Mercy")
    cs "{size=-15}It's now or never."
    n "CS channels CSGod."
    hide cs
    show csgod flipped at left
    csgod "Time to die, Arceus!"
    show arceus angry dark
    stop music2
    music end
    show csgod flipped at left with vpunch
    play sound "alt_punch.ogg"
    show csgod at t_punchup with move
    show arceus angry dark at right with hpunch
    arceus "Really? I've been a god longer than you, dummy."
    arceus "Nice try."
    bad_end "There's no weapon\nto free us all!" "forest_menu"

label wait_arc:
    stop music
    scene washington_road
    show cs dark at left 
    show arceus dark flipped at right
    cs "{size=-15}I need to wait. I'm not powerful enough to attack."
    arceus "Man, I hope you're doing fine."
    cs "Yep!"
    stop music2
    music end
    pause 5.0
    n "The duo walks silently for a few hours, and eventually the sun rises."
    scene washington_road morning
    show arceus at right
    show cs at left
    with fade
    pause 3.0
    arceus "So, uhh, should we keep going this direction?"
    cs "..."
    cs "Yep."
    pause 5.0
    scene town
    show arceus at right
    show cs at left
    with fade    
    pause 2.0
    arceus "Hey, we found a town! That's good, right?"
    cs "Yep."
    show arceus worried
    arceus "Dude, are you {i}sure{/i} you're okay?"
    arceus "You haven't said anything, like, {i}at all,{/i} for the past several hours."
    cs "I'm fine."
    arceus "...okay."
    arceus "Well, uhh, what should we do now?"
    arceus "Are we gonna, like, try to get you home?"
    arceus "{size=-4}Do you even wanna go home?"
    cs "Yes, yes, let's just wait here."
    arceus "In the middle of the road?"
    arceus "Why?"
    arceus "There's someone coming! Shouldn't we move?"
    pause 1.0
    arceus "Hello?"
    n "All of a sudden, the car driving at them slowly comes to a stop."
    n "The man inside gets out of the car."
    show billy at center with moveinright
    billy "Hey, that's my car!"
    billy "What are you doing?"
    cs "Take us to these coordinates: 46.5754, -112.3008."
    billy "I, uhh..."
    pause 2.0
    billy "No problem!"
    billy "Let's go!"
    scene car background
    show billy car
    play music "<loop 0>insane_personalities.mp3" volume 0.6
    music Insane Personalities - Lizardking
    pause 5.0
    scene car background night
    show billy car
    with fade
    pause 3.0
    n "For the whole drive, no one says a word."
    stop music fadeout 3.0
    music end
    scene cultforest
    show billy car
    billy "Welp. We are here."
    n "CS gets out of the car and heads up the trail on the side of the road."
    arceus "Hey, uhh, I'm gonna get out too."
    hide billy car with fade
    show arceus flipped at mid_left with moveinleft
    arceus "CS? Where did you go?"
    arceus "What is wrong with him right now?"
    pause 2.0
    arceus "After that incident with the cops, he's been..."
    pause 1.0
    arceus "He's just been--"
    play music "<from 60 to 170>insane_personalities.mp3" volume 1
    csgod "Stronger than ever."
    show csgod flipped at mid_left with moveinleft
    show arceus flipped at mid_left with vpunch
    play sound "audio/punch.ogg"
    show arceus flipped at mid_left with hpunch
    play sound "audio/punchalt.ogg"
    show arceus flipped at t_punchup with move
    arceus "Ouch."
    $ achievement_manager.unlock("No Mercy")
    show cultist at mid_right with moveinright
    show cultist_2 at right with moveinright
    show cultist_3 at center with moveinright
    cultist "Praise CSGod! Praise CSGod!"
    n "Billy takes off in an instant after witnessing the event."
    csgod "I have finally harnessed the power of CSGod!"
    csgod "Time to take over the world!"
    stop music
    bad_end "This will affect\nthe local trout population!" "forest_menu"

label pussy_out_forest:
    $ achievement_manager.unlock("Pacifist")
    cs "Arceus, quick! Let's escape into the forest!"
    arceus "Alrighty, let's go!"
    show arceus flipped
    hide arceus
    hide cs
    with moveoutright
    scene black with fade
    stop sound fadeout 1.0
    n "CS and Arceus quickly jump into the trees next to them."
    n "As CS and Arceus hunker down into the foliage, they see the flash of lights fly past them."
    arceus "Phew! That was a close one, CS!"
    cs "Yeah, it looks like we hid just in time."
    arceus "Alright, well, should we wait here for a bit or do you think the coast is clear?"
    jump wait_forest

label wait_forest:
    cs "We should probably wait for a little bit. They might turn around and see us."
    arceus "Yeah, that's a good point. I kinda don't want to risk going back to prison again."
    n "CS and Arceus stay quiet in the forest for about 15 minutes before heading back onto the road again."
    scene washington_road with fade
    show cs dark at left with moveinleft
    show arceus dark at right with moveinright
    cs "Hey, Arceus?"
    arceus "Hmm?"
    cs "Now that we are out here and have more time to talk, where exactly are we heading to? Why did we come back to the US?"
    arceus "Well, I figured you wanted to go back home, right?"
    cs "Of course I want to head back home, it's just... it seems so far away."
    cs "We don't really have a car or anything, we are completely lost, and we've got the cops still looking for us, probably!"
    arceus "Look, man, I know it's pretty hard right now, but we've gotta be optimistic about this."
    arceus "The second we find people, I'm sure we can work something out and head back home."
    cs "If you say so. I just hope we don't have to {i}walk{/i} all the way there."
    arceus "I don't think that'll be the case."
    copguy "{cps=10}I don't think so either."
    n "Before CS and Arceus can react, they both get the lights knocked out of them."
    play sound "punch.ogg"
    scene black with determination
    n "When CS and Arceus wake up, they find themselves in handcuffs leaned up against a cop car."
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
    show arceus worried dark flipped
    arceus "I'm sorry."
    show cs worried dark
    cs "No, no, no! This can't be happening!"
    cs "Arceus! Can't you do something about this?"
    arceus "No can do, boss. Looks like this is the end of the line."
    copguy "No time for negotiations, pal. Get in the car."
    scene copcar
    show copguy at t_copguy_frontseat
    show copcar_mask
    with fade
    show arceus worried flipped at right
    show cs disappointed at left
    with moveinleft
    n "CS and Arceus are thrown into the back of the cruiser as Copguy barks some order into his walkie."
    copguy "This is Copguy calling in a 1-8-8 on Compass Road. Sheriff? We got 'em."
    n "Copguy starts the car and they drive off."
    jump copcar_menu

label copcar_menu:
    scene copcar
    show copguy at t_copguy_frontseat
    show copcar_mask
    show arceus at right
    show cs disappointed at left
    n "As they are heading away, CS has the urge to say something."
    menu:
        "HoH SiS scammed me!" (type = "true"):
            jump good_convince
        "I'm not CS!" (type = "bad"):
            jump bad_convince

label bad_convince:
    scene copcar
    show copguy at t_copguy_frontseat
    show copcar_mask
    show arceus at right
    show cs disappointed at left
    play music "<loop 0>pressing_pursuit_cornered.mp3" volume 0.3
    music Pressing Pursuit ~ Cornered - Masakazu Sugimori
    play sound "hold_it.mp3" volume 0.5
    show hold_it at truecenter with hpunch
    pause 1.0
    hide hold_it
    cs "Wait a second! I'm not actually CS!"
    cs "I just {i}look{/i} like CS!"
    show arceus worried
    arceus "I mean... he {i}might{/i} not be CS?"
    play sound "objection.mp3" volume 0.5
    show objection at truecenter with hpunch
    pause 1.0
    hide objection
    stop music
    music end
    copguy "Nice try, bud. We saw your fake visa and everything. You two are going back to the slammer."
    bad_end "Did you really\nthink that would work?" "copcar_menu"

label good_convince:
    show cs worried
    play music "<loop 0>pressing_pursuit_cornered.mp3" volume 0.3
    music Pressing Pursuit ~ Cornered - Masakazu Sugimori
    play sound "hold_it.mp3" volume 0.5
    show hold_it at truecenter with hpunch
    pause 1.0
    hide hold_it
    cs "Wait a second! The reason all this happened was because HoH SiS sabotaged my computer!"
    show arceus worried
    arceus "Wait, what?"
    show arceus
    copguy "What are you on about?"
    cs "Yes! HoH SiS scammed me out of thousands of dollars to get my foundation fixed, and they also broke my laptop!"
    cs "So, afterwards, I wanted to get my revenge!"
    copguy "I'm not believing this for a second."
    copguy "You really thought I would fall for some silly little lie?"
    play sound "objection.mp3" volume 0.5
    show objection at truecenter with hpunch
    pause 1.0
    hide objection
    arceus "Actually, I have proof of this."
    arceus "CS just raised a good point, and I can show you."
    copguy "And {i}how{/i} can you prove this? Where is your evidence?"
    n "Arceus pulls up a laptop that he managed to grab from the front seat."
    copguy "{i}What?{/i} How did you get that?"
    arceus "Watch this."
    scene backseat
    show craptop evidence
    with dissolve
    n "Copguy stops the car as Arceus plays back the scene from {i}CS Bounciness I{/i} with the scamming of CS by HoH SiS."  # DX: Weird line?
    scene copcar
    show copguy at mid_left
    show copcar_mask
    show arceus at right
    show cs disappointed at left
    with dissolve
    cs "How--"
    show arceus happy
    arceus "I have my ways."
    show arceus
    copguy "I don't understand... so HoH SiS really did scam you hard, didn't they?"
    copguy "I'm not sure how valid it was for you to push that man off a building..."
    copguy "But I can't argue right now about whether that footage is fake."
    stop music fadeout 3.0
    music end
    hide copguy with moveoutleft
    n "Copguy gets out of the car."
    n "He then proceeds to open the doors and let CS and Arceus out, freeing them of their shackles."
    scene washington_road with fade
    show copguy dark flipped at right with moveinleft
    show copguy dark with determination
    show cs disappointed dark at left with moveinleft
    show arceus dark flipped at mid_left_left with moveinleft
    copguy "Listen, I really shouldn't be doing this right now, but I have to go back to look into this deal with HoH SiS."
    copguy "You are free to go for now."
    copguy "But know this: I'm putting my job on the line over this."
    copguy "Don't do anything stupid, because I have my eye on you two!"
    n "Copguy gets back into his car, and heads off into the dead of night."
    show copguy dark flipped with determination
    hide copguy with moveoutright
    show arceus dark flipped at mid_right_right with move
    show arceus dark at mid_right_right
    show cs dark
    n "CS and Arceus look at each other and smile."
    play music "<loop 0>bun_guster.mp3" volume 0.3
    music Bun Guster - Satoru Kosaki
    arceus "Holy crap, I didn't think that would work."
    cs "Me neither! I'm so glad that he let us go!"
    cs "I don't know how you got that footage, but we are now free once again!"
    show arceus happy dark
    arceus "Hooray for CS and Arc!"
    show cs happy dark at center
    show arceus happy dark at center 
    with move
    show cs happy dark at mid_left_left
    show arceus happy dark at mid_right_right
    with move
    n "They both high five and continue heading down the road."
    stop music fadeout 3.0
    music end
    jump choose_direction

label choose_direction:
    $ persistent.csb3b_unlocked = True
    scene black with determination
    n "As the duo continues their journey through the night, they soon have to figure out exactly where to go."  # DX: Reword?
    scene washington_road morning
    show cs at left
    show arceus at right
    with fade
    play music "<loop 0>happy_roaming.mp3" volume 0.5
    music Happy Roaming - Lorin Nelson
    cs "We've been walking all night. I'm exhausted."
    arceus "Yeah, let's hope we find food and water soon."
    cs "Hey, uhh, do you know exactly where we're going?"
    arceus "Well, I noticed that the sun rises ahead of us, which means we're heading east right now."
    arceus "We can head in any direction, really. The second we find a better form of transportation than walking, we're taking it."
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
    show arceus worried
    arceus "...What?"
    show cs disappointed
    cs "You said to pick a direction!"
    show arceus
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
    show arceus angry
    arceus "I literally just said--"
    arceus "Just pick another direction."
    show arceus
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
    n "CS and Arceus run into the Pacific Ocean."
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
    show arceus worried
    arceus "Uhm, okay... maybe we've missed something."
    n "CS and Arceus run into the Pacific again."
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
    cs "Nah, come on, there is definitely {i}something{/i} we can find going west."
    show arceus worried
    arceus "I really don't want to go there again..."
    cs "Nah, we've got this. For sure this time."
    n "CS and Arceus find a cool looking crab, but still just the ocean again."
    scene washington_road
    show cs dark at left
    show arceus angry dark at right
    cs "Hey! That's quite an epic crustacean!"
    arceus "Alright, cool, can we pick another direction that {i}isn't{/i} west this time?"
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
    arceus "... Something tells me that you were in an asylum for a bit..."
    n "CS and Arceus, surprisingly, find the ocean again."
    scene washington_road morning
    show cs happy at left
    show arceus angry at right
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
    show arceus angry at right
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
    show arceus angry dusk at right
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
    show arceus angry dark at right
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
    show arceus angry at right
    menu:
        "North":
            jump north
        "East" (type = "true"):
            jump east
        "South":
            jump south
        "West":
            jump west5
