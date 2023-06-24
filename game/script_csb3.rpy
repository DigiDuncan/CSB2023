label csbiii_start:

    scene outside_ltt with fade
    show cs at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene inside_ltt with fade
    play music "<loop 0>passport.mp3" volume 0.5
    music PASSPORT.MID - George Stone
    show linus at center with moveinright
    linus "Welcome to Linus Media Group, come on in, I'll show you your desk."
    cs "Thanks Linus."
    scene black with fade
    n "Linus and CS walk to CS' new desk."
    scene csdesk with fade
    show linus at right with moveinright
    show cs at left with moveinleft
    cs "Wow! I thought this was an office, why do I get such a cool desk?"
    linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."
    cs "Holy shit, really? This is way better than any setup I've seen, let alone had."
    linus "You must've had really bad setups then, this only has 2080s, everyone else has 2080 TIs or GTX Titans."
    cs "I have absolutely no problem with 2080s."
    linus "Well, enjoy!"
    hide linus with moveoutright
    cs "I guess I better get to work on editing, let's see what videos I need to edit..."
    cs "Let's see, I have the new TechQuickie video on how live streaming works, or the video on how at least half of the keys on your keyboard should be macros..."
    cs "Dammit Taran, you can edit your own macro fetish content."
    cs "I guess I'll edit the livestreaming one."
    scene black with fade
    n "CS starts working on editing the TechQuickie video and Linus comes in to check on him."
    scene csdesk
    show cs at left
    with fade
    show linus at right with moveinright
    linus "Hey CS, how's the new video coming along?"
    cs "It's going well, I have the background all done and I'm working on adding graphics and fixing audio."
    linus "Wow! You're a fast worker, you'll get off of those old 2080s in no time."
    cs "Thanks Linus."
    linus "Speaking of live streaming, we need a new PC for the WAN Show, can you go and buy parts for one?"

    menu: 
        "What are you going to do?"
        "Go to the store.":
            jump microcenter
        "Help edit a video.":
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
    music Good Eatin - ClascyJitto
    show taran at right with moveinright
    taran "Need any help with anything?"
    cs "Hey Taran! You wanna check out my video so far?"
    taran "Sure, let it roll."
    scene csvideo with fade
    n "CS and Taran watch CS's video."
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
    taran "... This is {i}your{/i} office.."
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
        "Good":
            hide cs
            hide csdesk
            show black
            with fade
            jump boost
        "Bad":
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
    show cs angry with hpunch
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
    linus "Dude what are you talking about? That video was awesome!"
    show cs at left
    cs "Woah wait, you actually like YTPs?"
    linus "Yeah man, you think I just hired you on the spot because of your obviously fake visa?"
    linus "I love your videos! I've been secretly hoping you would YTP one of mine for the longest time!"
    show linus at left with ease
    show linus at center with ease
    show cs happy
    n "CS's frown fades in a big grin, as they both high-five."
    cs "Hell yeah! I would've never thought YTPs would help me in a business setting, nevermind that my BOSS enjoyed them!"
    cs "Alright! Well, I guess I better get back to poopin'!"
    show cs flipped at left
    show cs flipped at offscreenleft with ease
    n "Before CS heads out of the room, Linus shouts to him."
    linus "Hey, later today, I got a big surprise to show you. I'll stop by your office and we can check it out."
    cs "Sure thing!"
    scene csdesk
    show cs at center
    with fade
    n "When CS gets back to his setup, he starts letting his mind race with ideas."
    cs "Oh man, where do I even start now?"
    cs "I have so many ideas of videos to poop, I could even try to teach Linus how to YTP..."
    cs " I mean, with the amount of tech he drops on a daily basis, he kinda already is a YTP."
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
    n "Inside is what looks to be a graphics card, but with a brown YouTube logo engraved into the side."
    show cs
    cs "Woah, what is this Linus? A YouTube-brand graphics card?"
    linus "Not exactly. It's an experimental piece of hardware that we have never used before, and it's custom made."
    n "Linus holds the card into the air."
    linus "Behold! {w=0.5} The-- WOAH SHIT {w=0.5}{nw}"
    with vpunch
    n "Linus loses grip of the card as it tumbles down onto the table next to him."
    n "CS facepalms, while you can hear Luke laughing in the background."
    cs "Goodness Linus, you should maybe not do that next time."
    linus "Yeah, I'm sorry. Maybe you should hold it." 
    linus "This card is called the YTX-9001 Ti, a PCI add-in for enhancing and optimizing Youtube Poops."
    n "CS's eyes widen."
    cs "Wait whaaat? That's awesome! How does this even work?"
    linus "We don't even know, we haven't even tested it yet."
    linus "It also apparently has Poop-tracing, which I'm curious to see how that works."
    cs "Well, what are we waiting for? Let's get this thing hooked up!"
    n "Linus and CS take apart CS's PC and put the card in."
    n "They then start the computer, and everything boots up as normal."
    linus "Alright, now that it's up and working, we need to install the drivers. The card came with a flash drive that includes them."
    n "As Linus inserts the flashdrive, a window off the side of the screen pops up saying 'Your new Peeforce Experience drivers are available.'"
    n "CS chuckles a bit."
    show cs happy
    cs "Peeforce? I must admit, even these drive names are a bit silly."
    n "Linus Laughs."
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
    cs "Wow, thank you so much Linus for this!"
    linus "No problem! This was my gift to you. Now, we should make a review video of it before the day ends."
    cs "Sure thing, let's take the card out real quick."
    show black with fade
    n "Linus goes and gets the cameras set up, and they start to film the video."
    scene setup with fade
    n "After they finish recording, CS goes up to Linus's office."
    #Todo get linus's office
    scene loffice with fade
    show cs at left with moveinleft
    cs "Hey Linus?"
    linus "What's up CS? What do you need help with?"
    menu:
        "What does CS need help with?"
        "I want to work on YTPs.":
            jump ytp_edit
        "I want to do reviews":
            jump reviews
    
label ytp_edit:
    show linus at offscreenright
    cs "I have a question about what I want to do here at LTT."
    n "Linus stands up and walks over to him."
    show linus at center with ease
    linus "Sure. I mean, what do you want to do?"
    cs "I really want to make more YTPs for you guys."
    n "Linus laughs a bit."
    linus "Oh, CS, When I gave you the YTP card that was meant for use on your own channel, not the LTT one."
    cs "I know, but--{w=0.25}{nw}"
    linus "I mean, for example.{w=0.5} TARAN! GET IN HERE!"
    n "Taran rushes up to Linus's office."
    show taran at right with moveinright
    taran "{i}panting{/i} Yes, {w=0.5}Linus? {w=0.5}What is it?"
    linus "Taran, have you ever seen a YTP?"
    taran "Other than the one CS made the other day? Not really."
    linus "See, CS? Not only will our audience be super confused, but our employees will be as well."
    cs "Alright... I see..."

    menu:
        "What will CS do?"
        "Show everyone more YTPs":
            jump both_fan
        "Ignore them and keep making your own YTPs.":
            jump ytp_fan

label both_fan:
    cs "You know what? Why don't you all come down to my office."
    linus "I mean... sure. Let's see what you have in stock."
    linus "Come on guys, let's go!"
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
    linus "Oh no.."
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
    cs "I know, but I swear, this doesn't have anything to do with my community."
    linus "Wait what do you mean I know? I was just joking about the furry fanbase."
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
    linus "So you DO have a furry fanbase who wants to join LTT! Damnit CS, I should've known."
    show cs worried
    cs "Shut up, Linus!"
    cs "Arceus, what's going on? Where have you been?"
    arceus "Look, CS, we don't have much time. I know that you've been living here for a while, but the cops are still looking to extradite us back to America, and they are headed to LTT to search for you!"
    linus "WHAT? CS, why are the cops chasing you? This could seriously damage our reputation more than the time I mentioned I dropped hard R's as a kid!"

    menu:
        "What will CS do?"
        "I'm going to stay with LTT.":
            jump cops_ltt
        "Escape with Arceus.":
            jump arc_escape

label arc_escape:
    cs "Look I'm sorry Linus, I wish I could explain, but Arceus is right. I need to get going."
    linus "I am like, so confused and frustrated, this better not ruin LMG."
    show cs disappointed
    cs "I'm sorry guys, I'll try to catch you guys up after this."
    cs "This is CS, signing out."
    arceus "We have no time for that CS! We need to go!"
    # TODO: Outside LTT
    scene outside_ltt with determination
    show cs disappointed at left
    show arceus at right
    with moveinright
    n "CS and Arceus run out of the building, and try to find cover while they escape."
    play sound "siren.ogg" loop fadein 2.0 volume 0.2
    show blue_light at left
    show red_light at right
    n "As they are making their way away from the building, they can hear sirens grow in volume as flashing lights rush towards the LTT building."
    cs "This is awful, I was just starting to get along well with Linus and the gang."
    arceus "I'm sure they'll forgive you in due time, but for now, we need to evade the cops' trail and get back to the United States."
    n "While Arceus and CS were hitchhiking away from the scene, the cops show up at LTT to investigate."
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
    linus "*mutters to himself* I should've done a background check on CS, it's weird how-"
    show luke at mid_left
    show taran flipped at mid_mid_left
    show colton at center
    with move
    show copguy at right with moveinright
    n "Copguy bursts in."
    copguy "Alright, everyone! Back against the wall! Nobody move!"
    luke "So, are we moving to the wall or… not moving?"
    copguy "Don't question the police! Just… stand against the wall!"
    n "The LMG members move toward the wall while more policemen come in and search the place."
    copguy "Alright, I have a very simple question to ask you all."
    copguy "Do you know this man?"
    n "Copguy shows a picture of cs188 to the crew."
    taran "Uhh yeah, that's-"
    linus "We don't know who that is at all."
    copguy "Oh really? You there, what did you say about this man?"
    taran "I uhh…"
    taran "I was saying that…"
    taran "That it looks like Colton! Yeah!"
    colton "WTF Taran!"
    linus "Yep, that looks like Colton alright."
    copguy "Alright, sir what's your name?"
    linus "It's lin-"
    copguy "Yeah okay. Linard, if you say that it's {i}this{/i} man, how can you explain the maid outfit that was used in the video that was just uploaded an hour ago?"
    linus "Well uhh, he's got some... weird kinks…"
    colton "Oh my fucking god."
    copguy "If you are so sure then, lemme go talk to the sheriff about this."
    linus "Sure thing, officer."
    hide copguy with moveoutright
    n "Copguy leaves the scene."
    colton "I can't fucking believe you guys! That was way too far!"
    linus "April fools?"
    colton "IT'S JULY!"
    scene outside_ltt
    n "Copguy orders the rest of the cops to leave the scene and return back to the station."
    show copguy at left with moveinleft
    copguy "Damnit, they don't have CS anymore. We're gonna have to look harder for him."
    scene road_to_canada with fade
    show cs disappointed dusk at left
    show arceus dusk at right
    n "Meanwhile, CS and Arc have been running back to the US border."
    cs "Aw man! This is embarrassing!"
    arceus "Yeah, so much for the editing job, I guess."
    cs "I can't seem to get a break this month. First my problems with HoH SiS, now I'm running from the cops?"
    cs "I should've just called another foundation repair company."
    arceus "Yeah, that sounds like hell. You could have called me. I am literally a god."
    cs "It IS hell."
    arceus "I should've known that the cops were going look for us. We didn't hide our tracks too well."
    arceus "I heard about the cops at the last second when I was checking comm chatter around the area. I figured that since you helped me out, I should come back for you."
    cs "Thanks man, I really owe you again."
    arceus "Nah, I owe you."
    scene border_dusk with fade
    show cs dusk at left
    show arceus dusk flipped at mid_left
    n "CS and Arc approach the border guard again."
    show border_guard dusk at right with moveinright
    border_guard "I'm gonna need proof of-"
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
    arceus "Well, I've been at the same hotel, clearing up ties with my cyber criminal past."
    arceus "I've been in prison for 5 years, so I've had to figure out what to do again for money."
    arceus "Anno's been at the hotel too, I think he's planning on starting some kind of band."
    cs "Ah, I see."
    scene sheriff_office with fade
    n "Back at the police station, Copguy talks to the sheriff about CS."
    show sheriff at left
    show copguy at right with moveinright
    sheriff "Howdy Officer copguy, tell me, you guys arrested CS this evening, right?"
    copguy "Unfortunately, no we did not."
    n "The sheriff slams his desk."
    show sheriff at left with hpunch
    sheriff "Damnit! And how did you fuck that up?"
    copguy "Look, you see, he managed-"
    sheriff "You know what, I don't want to hear this!"
    sheriff "First, they manage to escape from one of our top prisons, and now you're telling me that you lost him?!"
    copguy "Please, this is one of my best cases yet! I need to catch him, and I promise I'll put him back in jail along with those other 2!"
    n "The sheriff thinks for a moment."
    sheriff "Alright, since I know you've been pretty good at catching criminals for the past 15 years, I'll let it slide this time."
    sheriff "But believe me, this CS man has a pretty high target on his head, and we need to bring him to justice before him and his gang do anything else funny."
    sheriff "The next time you come back here, he better be with you, or you're fired!"
    copguy "Sure thing, boss. I'll track him down on my own."
    hide copguy with moveoutright
    n "Copguy turns around and heads out to track down CS and Arc."
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
    arceus "Wait a minute, those are-"
    n "Arceus squints into the distance, but CS and Arc both immediately recognize the sounds."
    show cs worried dark
    "CS and Arceus" "SHIT!"
    arceus "Copguy's back! He's probably looking all over for us! What do we do CS?!"
    menu:
        "What do we do CS?!"
        "Fight the cops with YTP Magic":
            jump ytp_magic_fight
        "Flee into the forest":
            jump pussy_out_forest

label ytp_magic_fight:
    jump secret

label pussy_out_forest:
    cs "Arceus quick! Let's escape into the forest!"
    arceus "Alrighty, let's go!"
    hide arceus
    hide cs
    with moveoutright
    scene black with fade
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
    cs "Hey Arceus?"
    arceus "Hmm?"
    cs "Now that we are out here and have more time to talk, where exactly are we heading to? Why did we come back to the US?"
    arceus "Well, I figured you wanted to go back home, right?"
    cs "Of course I want to head back home, it's just, it seems so far away."
    cs "We don't really have a car or anything, we are completely lost, and we got the cops still looking for us probably!"
    arceus "Look man, I know it's pretty hard right now. But we gotta be optimistic about this."
    arceus "The second we find people, I'm sure we can work something out and head back home."
    cs "If you say so, I just hope we don't have to WALK all the way there."
    arceus "I don't think that'll be the case."
    copguy "I don't think so either."
    n "Before CS and Arc can react, they both get the lights knocked out of them."
    scene black with determination
    n "When CS and Arc wake up, they find themselves in shackles leaned up against a cop car."
    scene washington_road with fade
    show cs disappointed dark at left
    show arceus dark flipped at mid_left_left
    cs "Huh?"
    cs "What happened?"
    show copguy dark at right with moveinright
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
    n "CS and Arc get in the cop car, as copguy says some order on his walkie."
    copguy "Alright sheriff, we got em."
    n "Copguy gets in the car and they head off."
    n "As they are heading away, CS has the urge to say something."
    menu:
        "HoH SiS scammed me":
            jump good_convince
        "I'm not CS":
            jump secret

label good_convince:
    show cs worried
    play music "<loop 0>pressing_pursuit_cornered.mp3" volume 0.3
    music Pressing Pursuit ~ Cornered - Masakazu Sugimori
    cs "Wait a second! The reason all this happened was because HoH SiS sabotaged my computer!"
    arceus "Wait what?"
    copguy "What are you on about?"
    cs "Yes! HoH SiS scammed me out of thousands of dollars to get my foundation fixed, and the also broke my laptop!"
    cs "So afterwards, I wanted to get my revenge!"
    copguy "I'm not believeing this for a second."
    copguy "You really thought I would fall for some silly little lie?"
    arceus "Actually, I have proof of this."
    arceus "CS just raised a good point, and I can show you."
    copguy "And HOW can you prove this? Where is your evidence?"
    n "Arceus pulls up a laptop that he managed to grab from the front seat."
    copguy "WHAT? How did you get that?"
    arceus "Watch this."
    show black with fade
    n "Copguy stops the car as Arceus plays back the scene from CSB1 with the scamming of CS from HoH SiS."
    scene copcar with fade
    show arceus at right
    show cs disappointed at left
    cs "How-"
    arceus "I have my ways."
    copguy "I don't understand, so HoH SiS really did scam you hard, didn't they?"
    copguy "I'm not sure how valid it was for you to push that man off a building,"
    copguy "But I can't argue right now on if that footage is fake or not."
    stop music fadeout 3.0
    music end
    n "Copguy gets out of the car."
    n "He then proceeds to open the doors and let them out, freeing them of their cuffs."
    scene washington_road with fade
    show copguy dark at right with moveinleft
    show cs disappointed dark at left with moveinleft
    show arceus dark flipped at mid_left_left with moveinleft
    copguy "Listen, I really shouldn't be doing this right now, but I have to go back to look into this deal with HoH SiS."
    copguy "You are free to go for now."
    copguy "But don't do anything stupid, because I have my eye on you two!"
    n "Copguy gets back into his car, and heads off into the dead of night."
    hide copguy with moveoutright
    show arceus dark flipped at mid_right_right with move
    show arceus dark at mid_right_right
    show cs dark
    n "CS and Arc look at eachother, and smile."
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

label high_gpu:
    jump secret
