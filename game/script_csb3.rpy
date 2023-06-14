label csbiii_start:

    scene outside_ltt with fade
    show cs neutral at left with moveinleft
    n "CS returns to LMG the next day."
    hide cs with moveoutright
    scene inside_ltt with fade
    show linus in center with moveinright
    linus "Welcome to Linus Media Group, come on in, I'll show you your desk."
    cs "Thanks Linus."
    scene black with fade
    n "Linus and CS walk to CS’ new desk."
    cs "Wow! I thought this was an office, why do I get such a cool desk?"
    linus "Actually, this is our worst setup, you'll get upgraded after you've been here a while."
    cs "Holy shit, really? This is way better than any setup I've seen, let alone had."
    linus "You must've had really bad setups then, this only has 2080s, everyone else has 2080 TIs or GTX Titans."
    cs "I have absolutely no problem with 2080s."
    linus "Well, enjoy!"
    n "Linus exits."
    cs "I guess I better get to work on editing, let's see what videos I need to edit..."
    cs "Let's see, I have the new TechQuickie video on how live streaming works, or the video on how at least half of the keys on your keyboard should be macros..."
    cs "Dammit Taran, you can edit your own macro fetish content."
    cs "I guess I'll edit the livestreaming one."
    n "CS starts working on editing the TechQuickie video and Linus comes in to check on him."
    n "Linus enters the office."
    linus "Hey CS, how's the new video coming along?"
    cs "It's going well, I have the background all done and I'm working on adding graphics and fixing audio."
    linus "Wow! You're a fast worker, you'll get off of those old 2080s in no time."
    cs "Thanks Linus."
    linus "Speaking of live streaming, we need a new PC for the WAN Show, can you go and buy parts for one?"

    menu: 
        "What are you going to do?"
        "Go to the store.":
            return
        "Help edit a video.":
            return
