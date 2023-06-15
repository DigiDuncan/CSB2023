label csbiii_start:

    scene outside_ltt with fade
    show cs at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene inside_ltt with fade
    show linus at center with moveinright
    linus "Welcome to Linus Media Group, come on in, I'll show you your desk."
    cs "Thanks Linus."
    scene black with fade
    n "Linus and CS walk to CS’ new desk."
    scene csdesk with fade
    show cs at left with moveinleft
    show linus at right with moveinright
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
            jump secret
        "Help edit a video.":
            jump edit_video

label edit_video:
    cs "Nah, I wanna finish this video first. That way I can help you pump out videos faster."
    linus "Alright, that's fine. I'll probably send Colton to get the parts instead, he's good at sucking up to those kinda things."
    cs "Alright haha, yeah I definitely wasn't using this as an excuse to get out of shopping!"
    linus "...ok? Whatever, just keep editing."
    cs "Yeah, no, don't worry I got this."
    hide linus with moveoutright
    n "Linus leaves the room."
    cs "Hmm, this video looks pretty great so far, I'm practically almost done at this point."
    cs "I wonder what the others will think of this though? I should probably get opinions from some of the other employees."
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
    taran "He will be so surprised when you upload it, he will wonder how well you put it together in such little time."
    show cs
    cs "You really think so? I mean I don't want him to be upset with me."
    taran "Don't worry about it. If he thinks it is that bad, I'll take the blame on it."
    cs "That's nice and all, but do you think that's a good idea? I mean, I don't want to mess up my first chance at this."
    taran "Nah, don't worry about it."
    taran "Even if something dumb happens, he usually never gets mad at us for doing silly things like that."
    taran "Besides, he plays practical jokes on us half the time, so even if the video was dumb, I doubt he would be mad at all."
    cs "Well if you say so, I guess it's fine."
    cs "Let's wait and see how he reacts."
    taran "Alrighty then, I'll catch you later!"
    cs "For tonight, this{w} is{w} CS,{cps=*0.1} signing {cps=*10} out!"
    taran "...What did you say?"
    cs "Huh? I totally didn't say that, I'm just gonna leave."
    taran "..."
    taran "Okay, I'll see you later then!"
    hide taran with moveoutright
    n "Taran goes back to his office."
    cs "Well, I guess since this video is already good enough, I can upload it now."
    cs "It's so crazy having the ability to access the LTT channels. There is so much crazy shit going on here!"
    cs "Oh well, time to upload this."
    n "CS pauses for a moment."
    cs "I don't know, I really feel like I shouldn't upload this yet."
    cs "It doesn't feel complete. Something is missing from it…"
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
    cs "Don’t worry, I already know it’s perfect. It’s so great, isn’t it?"
    linus "It’s actually the very opposite of that. You’re fired."
    show cs disappointed
    cs "Wait, what?"
    linus "Look, I don’t care how much you really wanted to humiliate me, just leave."
    cs "I don’t understand, I didn’t think you would be this upse-"
    linus "Just go already! I don’t want to see you again!"
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
    n "The next day."
    scene inside_ltt with fade
    show cs at offscreenleft
    n "CS walks into LMG to greet Linus."
    show cs at left with moveinleft
    show linus at offscreenright
    cs "Hey guys! Did you all check out the new video?"
    show linus at right with moveinright
    linus "Yes we did."
    linus "It was…"
    cs "Oh shoot, it was awful wasn’t it?"
    cs "Yeah, I should’ve realized my style is too crazy, I guess I should leave…"
    show cs flipped at left
    show linus behind cs at left with ease
    show linus at center with ease
    n "As CS turns around, Linus friendly punches him in the back. "
    linus "Dude what are you talking about? That video was awesome!"
    show cs at left
    cs "Woah wait, you actually like YTPs?"
    linus "Yeah man, you think I just hired you on the spot because of your obviously fake visa?"
    linus " I love your videos! I’ve been secretly hoping you would YTP one of mine for the longest time!"
    show linus at left with ease
    show linus at center with ease
    n "CS’s frown fades in a big grin, as they both high-five."
    cs "Hell yeah! I would’ve never thought YTPs would help me in a business setting, nevermind that my BOSS enjoyed them!"
    cs "Alright! Well, I guess I better get back to poopin’!"
    show cs flipped at left
    show cs flipped at offscreenleft with ease
    n "Before CS heads out of the room, Linus shouts to him."
    linus "Hey, later today, I got a big surprise to show you. I’ll stop by your office and we can check it out."
    cs "Sure thing!"
    scene csdesk
    show cs at center
    with fade
    n "When CS gets back to his setup, he starts letting his mind race with ideas."
    cs "Oh man, where do I even start now?"
    cs "I have so many ideas of videos to poop, I could even try to teach Linus how to YTP…"
    cs " I mean, with the amount of tech he drops on a daily basis, he kinda already is a YTP."
    cs "Alright well, back to editing!"
    n "The time flies by as CS dumps his ideas into Premiere."
    cs "Doo dee doo…"
    show linus at offscreenright
    n "Linus barges in. "
    show linus at center with ease
    with hpunch
    show cs at left
    show linus at right
    with ease
    linus "CS!!!"
    cs "WOAH SHi- you scared the crap out of me!"
    linus "Hah sorry, I’m just excited to show you this!"
    n "Linus holds out a rectangular box that reads on the front in black bold text DO NOT USE."
    cs "Umm, you sure this is the right box? It literally says-"
    linus "Yeah I know what it says, I just wrote this on here so no one else uses it."
    linus "Don’t worry, I didn’t like, buy it from some creepy dude at a garage sale that claims it’s haunted."
    n "CS looks unnerved."
    linus "Look just, open the box. I’m sure you’ll like it."
    n "CS cautiously takes the box, and opens the top. "
    n "Inside is what looks to be a graphics card, but with a brown youtube logo engraved into the side."
    cs "Woah, what is this Linus? A Youtube-brand graphics card?"
    linus "Not exactly. It’s an experimental piece of hardware that we have never used before, and it’s custom made."
    n "Linus holds the card into the air."
    linus "Behold! The- WOAH SHIT"
    with vpunch
    n "Linus loses grip of the card as it tumbles down onto the table next to him."
    n "CS facepalms, while you can hear Luke laughing in the background."
    cs "Goodness Linus, you should maybe not do that next time."
    linus "Yeah, I’m sorry. Maybe you should hold it." 
    linus "This card is called the YTX-9001 Ti, a PCI add-in for enhancing and optimizing Youtube Poops."
    n "CS’s eyes grow."
    cs "Wait whaaat? That’s awesome! How does this even work?"
    linus "We don’t even know, we haven’t even tested it yet."
    linus "It also apparently has Poop-tracing, which I’m curious to see how that works."
    cs "Well, what are we waiting for? Let’s get this thing hooked up!"
    n "Linus and CS take apart CS’s PC and put the card in."
    n "They then start the computer, and everything boots up as normal."
    linus "Alright, now that it’s up and working, we need to install the drivers. The card came with a flash drive that includes them."
    n "As Linus inserts the flashdrive, a window off the side of the screen pops up saying \"Your new Peeforce Experience drivers are available\"."
    n "CS chuckles a bit."
    cs "Peeforce? I must admit, even these drive names are a bit silly."
    n "Linus Laughs."
    linus "If you want, we can wipe them later."
    cs "Wipe! Now you’re in on it!"
    n "They both laugh as the drivers install, and once they’re finished, CS boots up Premiere."
    scene csvideo with fade
    cs "Alrighty, let’s see here. Why don’t we try this on that YTP I just made?"
    linus "Go to the settings real quick, and find the YTP features. turn YTP mode ON to allow the poop-tracing."
    cs "Alright, here goes nothing."
    n "A loading bar appears as the timeline starts shifting and different edits are created in the process."
    cs "Holy crap! This is amazing! It optimized every part of my YTP!"
    linus "That’s pretty cool, but let’s try it on a completely new source."
    linus "Open the video that we just took yesterday."
    n "CS opens the video, and enables YTP ON again. The source starts already making edits to start with."
    linus "And hey, if you don’t like the edits it makes, you can always turn it off or tweak the settings in that tab."
    scene csdesk
    show cs at left
    show linus at right
    with fade
    cs "Wow, thank you so much Linus for this!"
    linus "No problem! This was my gift to you. Now, we should make a review video of it before the day ends."
    cs "Sure thing, let’s take the card out real quick."
    n "Linus goes and gets the cameras set up, and they start to film the video."
    n "After they finish recording, CS goes up to Linus."
    cs "Hey Linus?"
    linus "What’s up CS? What do you need help with?"
