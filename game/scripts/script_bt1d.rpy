label bt1d_wakeup:
    stop music fadeout 3.0
    music end
    play music lets_hear_my_baby volume 0.15 if_changed
    music lets_hear_my_baby
    scene cs_room_2
    show cs at center
    with dissolve
    n "CS wakes up in his bedroom after a long slumber. Exhausted from the previous days' events, he groggily makes his way to the kitchen."
    show cs flipped with determination
    hide cs with moveoutright
    scene cs_kitchen
    show cs_kitchen_fg
    show cs disappointed behind cs_kitchen_fg
    with dissolve
    cs "I'm starving, I need to get something to eat."
    n "CS opens his fridge, and is assailed by a nasty smell."
    show cs concentrate with hpunch
    cs "Augh!"
    if fun_value(FUN_VALUE_COMMON):
        cs "Good lord, what is happening in there?!"
    n "CS grabs an item from the fridge, rubs his eyes, and looks at the date."
    show cs disappointed
    pause 0.5
    show cs disappointed at mid_right
    pause 1.5
    show cs disappointed at center
    pause 1.0
    # Show an expiry date here
    show cs angry
    cs "July?? Disgusting!"
    show cs disappointed
    cs "I don't know how I didn't think of this, but all my food went bad!"
    cs "Ugh, I'm going to need to go to the store to get more before I can even get a bite to eat..."
    hide cs with moveoutright
    scene cs_door_outside
    show cs flipped at center
    with dissolve
    n "CS starts to walk out the door, but before he does, his phone buzzes."
    show cs disappointed flipped
    phone "New game from Annorexorcist: ANNO 188: Poop Romana!"
    show cs angry flipped
    cs "I don't care right now! I'm hungry and tired!"
    hide cs with moveoutleft
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS clears the notification and gets in the car."
    play sound sfx_doorslam
    scene cs_car_inside
    show cs disappointed at left
    with dissolve
    play music canyon_car volume 0.2 if_changed
    music canyon
    pause 1.0
    if fun_value(FUN_VALUE_RARE):
        cs "I don't want to go Walmart any more, but at this point, I don't want to go to Walmart anymore."
    else:
        cs "I don't want to go Walmart any more, but at this point, I don't want to go to Target, either."
    show cs
    cs "You know what, I'm going to ALDI. They always have great deals."
    n "CS speeds off to the nearest ALDI."
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "Once he arrives at the ALDI, he grabs a quarter from his center console, and heads to the cart return."
    show aldi_outside
    show cs at mid_left
    with dissolve
    cs "What a smart system! The Europeans really know what they're doing."
    hide cs with moveoutright
    scene aldi_inside
    with dissolve
    show cs at mid_left with moveinleft
    n "CS walks into the ALDI, and is enamored by the selection and prices."
    cs "Oh my gosh, there's so much I can get! I'm so hungry, I could eat a horse!"
    n "A horse...? walks by CS."
    show cs worried
    horse "You could what?"
    show cs disappointed
    cs "Erm... nothing."
    horse "Mm-hmm."
    play sound sfx_waterphone
    pause 2.5
    n "The horseperson walks away."
    cs "Anyway..."

    # CS buys a lot of food I don't know figure it out
    hide cs with moveoutright
    n "CS goes to check out with a cart full of food."
    cs "I can't wait to get all this home..."
    n "CS puts all this food up on the belt, and cashier checks him out with great speed!"
    cashier "That will be $88.88."
    n "Wow, that's pretty cheap for this much food!"
    cashier "That's what we do here at ALDI."
    cashier "Tell your friends; we don't have a marketing budget."

    # Cut to CS at home with his groceries
    scene cs_room
    show cs at center
    with dissolve
    cs "Finally, now I can feast."
    cs "I'm very hungry!"
    cs "Give me the snacks!"
    n "CS spends the next few hours sitting on his couch and eating his spoils, all the while watching car crash videos on his TV."
    show cs concentrate
    n "Eventually, he passes out right where he's sitting!"
    scene black with dissolve

    # he passes out, show the passage of time
    play music apple_kid if_changed
    music apple_kid
    show cs_room
    show cs disappointed
    with dissolve
    n "CS awakes surrounded by wrappers and plates, and some random video playing on the TV."
    cs "What the heck is this?"
    n "The TV displays some kind of baby sensory video."
    cs "Something must have autoplayed... what time is it?"
    n "CS checks his phone."
    cs "9AM?! I slept all night?"
    cs "Ugh, I feel awful..."
    cs "How much did I eat last night?"
    n "CS stands up and looks around, taking inventory of the damage."
    cs "Oreos... Cheez-Its... Animal crackers... oh jeez..."
    n "CS thinks for a moment, then is taken aback with horror!"
    show cs worried with hpunch
    cs "Oh no! Wait, what if I have diabetes?!"
    n "CS rushes to this computer."
    n "CS begins researching diabetes."
    cs "How much would insulin cost? It's not like I have a ton of cash..."

    # pause beat, maybe zoom in?

    cs "{cshake}$300?!"
    cs "This is insane! I need to call Digi. They have diabetes, maybe they can make this make sense to me."
    show nugget_inside
    show digi at center
    # cut to Digi on the nugget
    n "Digi is tinkering with their arm, when their phone rings."
    # play Digi's actual ringtone here
    digi "What the heck? No one calls me..."
    digi "CS? What could this be about?"

    # splitscreen
    show cs_room at left
    show cs worried at mid_left
    with moveinleft
    show nugget_inside at mid_offscreen_right
    show digi at mid_right
    with move

    cs "Digi, I'm worried I got diabetes!"
    digi "What, huh--"
    cs "I ate a ton of food last night because I got home from the adventure and--"
    digi "Oh yeah, did you ever get your pencil sharpener in the mail?"
    cs "No, I didn't, I'm-- "
    show cs scared at mid_left with vpunch
    extend "Digi, this is important!"
    n "Digi sets down the screwdriver they were poking their arm with."
    digi "Man, you can't get diabetes. At least, not Type 1."
    cs "What do you mean? How did you get it?"
    digi "Type 1 is genetic. You kinda have it lingering in you until it crops up."
    digi "For me, it cropped up when I was two."
    cs "Wait, OK, then what's the difference between Type 1 and Type 2?"
    stop music fadeout 3.0
    music end
    digi "Well..."
    play music basketball_music if_changed
    scene basketball_court
    # cut to a cutaway. a machine is on the left, a basketball hoop on the right. the background
    # is like, a chalkboard or something.
    
    digi "Imagine your body has a basketball machine in it. You need basketballs to live."

    # the words NO DIABETES appear at the top of the screen.
    # round basketballs fire out of the machine, and into the hoop.

    digi "In a normal body, your body happily makes nice, round basketballs. They go through the hoop just fine!"

    # the words TYPE 1 appear at the top of the screen.
    # no more basketballs are made

    digi "In my body, with Type 1 Diabetes, I don't make any basketballs. So I have to \"import\" some."

    # a cardboard box drops into the scene. a basketball comes out the box, and flies into the hoop.

    digi "That's what my pump is for."

    # the words TYPE 2 appear at the top of the screen.
    # cubular basketballs come out of the machine, try to fly into the hoop, and bounce right back out!

    digi "With Type 2, your body makes cubular basketballs."
    digi "They can't go through the hoop... so we need to hammer them back into spheres!"

    # A hammer is added to the scene. The balls hit the hammer, become round, then go in the hoop.

    digi "That's what medication does!"

    # cut back to the splitscreen voice call

    cs "OK, but you're a cyborg... why do you still have diabetes at all?"
    digi "Eh, didn't feel right to cure."
    digi "If the people in real life don't have a cure, why should I?"
    cs "Wait, what do you mean by \"real life\", aren't we currently in real--{nw}"
    digi "Donate to {a=https://tilt.fyi/UEZfMk99zW}Breakthrough T1D!"
    cs "Uh, I have done that."
    digi "Good. Anywho, you very likely don't have diabetes."
    cs "Well, that's good."
    digi "You probably just have a tummyache, man."
    cs "Fair. Well, why is insulin so expensive?"
    digi "Now {i}that{/i} is because of... well... I don't know!"
    digi "All I know is it only costs a few dollars to produce, but they mark it up a {i}ton."
    cs "That's outrageous! Imagine if I {i}did{/i} have diabetes! I'd be bankrupt!"
    digi "That's a lot of people's reality."
    cs "We need to get to the bottom of this!"
    n "Digi looks at their holoband."
    digi "Well, I don't have anything to do today. I'll come over there and we can sort it out."
    cs "Great. See you soon."

    # The phone call ends, and CS' half of the split screen slides away.

    digi "Well, I guess I have plans today now. Come on, Lad."
    n "Lad gives a happy jingle." # sfx here of kricketot's cry

    # cut to Nugget landing in front of CS' house
    n "CS meets Digi in front of his house."
    cs "You got here quick!"
    digi "Yeah man, it's a spaceship."
    cs "Fair. Why do you have that anyway?"
    
    if "iris" in persistent.seen:
        digi "Long story. You remember Iris?"
        cs "Vaguely...?"
        digi "Her."
    else:
        digi "Long story. Do you know a purple woman?"
        cs "I don't think so...?"
        digi "Don't worry about it."

    cs "OK then. Where do we start?"
    digi "I'm thinking we go to the pharmacy. They have to know why insulin is this expensive."
    cs "That does make sense."
    digi "Hop in the Nugget!"
    cs "Do I need like, a space suit?"
    digi "No, dingus, we're not leaving atmosphere."
    