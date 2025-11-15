# TODO: replace image/description for achievement for completing this route
# TODO: fill in bio info, the skeletons already exist
# TODO: sprites/beeps for everyone
# TODO: fix horse's beep
# TODO: fix RPG stats for CEO/Secretary

label bt1d_wakeup:
    stop music fadeout 3.0
    music end
    play music lets_hear_my_baby volume 0.15 if_changed
    music lets_hear_my_baby

    scene cs_room_2
    show cs disappointed at center
    with dissolve
    n "CS wakes up in his bedroom after a long slumber."
    n "Exhausted from the previous days' events, he groggily makes his way towards the kitchen."
    show cs flipped with determination
    hide cs with moveoutleft

    scene cs_kitchen
    show cs_kitchen_fg
    show cs disappointed behind cs_kitchen_fg
    with dissolve
    cs "I'm starving! I've gotta eat something..."
    # TODO: digi needs to get a pic of the fridge open
    play sound sfx_foghorn
    n "A terrible stench assaults his nostrils."
    show cs concentrate
    cs "Augh!" with hpunch
    if fun_value(FUN_VALUE_COMMON):
        cs "Good Lord, what is happening in there?!"
    n "CS grabs an item from the fridge, rubs his eyes, and looks at the date."
    show cs disappointed
    pause 0.5
    show cs disappointed at mid_right
    pause 1.5
    show cs disappointed at center
    pause 1.0
    # Show an expiry date here
    show cs angry
    cs "July?! {nw}"
    extend "{i}Disgusting!" with vpunch
    show cs disappointed
    cs "Gross! I was gone for so long that all my food went bad!"
    cs "Ugh, now I gotta go to the store before I can even have breakfast..."
    hide cs with moveoutright
    scene cs_door_outside
    show cs flipped at center
    with dissolve
    n "CS starts to walk out the door, but before he does, his phone buzzes."
    # TODO: SFX phone vibrate
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
    # TODO: SFX car drives away like we did in Ch 1
    scene black with dissolve
    stop music fadeout 3.0
    music end
    jump bt1d_aldi

label bt1d_aldi:
    n "Once he arrives at the ALDI, he grabs a quarter from his center console, and heads to the cart return."
    # TODO: add items: quarter, cart
    show aldi_outside
    show cs at mid_left
    with dissolve
    cs "What a smart system! Those Europeans sure know what they're doing."
    hide cs with moveoutright
    scene aldi_inside
    with dissolve
    show cs at mid_left with moveinleft
    n "CS walks into the ALDI and is enamored by the selection and prices."
    show horse at offscreenright behind cs
    cs "Oh my gosh, there's so much I can get! I'm so hungry, I could eat a horse!"
    show horse at center with { "master": MoveTransition(1.0) }
    n "A horse...? walks by CS."
    show cs worried
    horse "You could what?"
    show cs disappointed
    cs "Erm... nothing."
    horse "Mm-hmm."
    play sound sfx_waterphone
    pause 2.5
    show horse at offscreenleft with { "master": MoveTransition(1.0) }
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

    jump bt1d_backhome

label bt1d_backhome:
    # Cut to CS at home with his groceries
    scene cs_room
    show cs at center
    with dissolve
    cs "Finally, now I can feast!"
    if fun_value(FUN_VALUE_COMMON):
        cs "I'm very hungry!"
        cs "Give me the snacks!"
    n "CS spends the next few hours sitting on his couch and eating his spoils, all the while watching car crash videos on his TV."
    # TODO: matrix math some crash video onto the screen
    show cs concentrate
    n "Eventually, he passes out right where he's sitting!"
    scene black with dissolve
    # TODO: SFX snoring

    # he passes out, show the passage of time
    play music apple_kid if_changed
    music apple_kid
    show cs_room
    show cs disappointed
    with dissolve
    n "CS awakes surrounded by wrappers and plates, and some random video playing on the TV."
    # TODO: matrix math some baby fruit video onto the screen
    cs "What the heck is this?"
    n "The TV displays some kind of baby sensory video."
    cs "Something must have autoplayed..."
    cs "What time is it?"
    n "CS checks his phone."
    cs "9AM?! I slept all night?"
    cs "Ugh, I feel awful..."
    cs "How much did I eat yesterday?"
    n "CS stands up and looks around, taking inventory of the damage."
    cs "Oreos... Cheez-Its... Animal crackers... oh, jeez..."
    n "CS thinks for a moment, then is taken aback with horror!"
    show cs worried with hpunch
    cs "Oh no! Wait, what if I have diabetes?!"
    n "CS rushes to this computer."
    # TODO: change scene, put him at a computer. he doesn't have the craptop anymore at this point so we need a shot of his new PC
    n "CS begins researching diabetes."
    cs "How much would insulin cost? It's not like I have a ton of cash..."

    camera:
        parallel:
            linear 2.0 zoom 1.1
        parallel:
            linear 2.0 xpos -0.05
        parallel:
            linear 2.0 ypos -0.05
    pause 2.0

    show cs scared
    camera:
        reset
    cs "{cshake}$300?!" with hpunch
    cs "This is insane! I need to call Digi. They have diabetes, maybe they can make this make sense to me."

    # TODO: cs pulls out phone; SFX: DialingDuncan lol

    scene black with dissolve

    show nugget_inside
    show digi thinking at center
    show cs worried at offscreenleft
    with dissolve
    # TODO: ambient spaceship sfx

    n "Digi is tinkering with their arm when their phone rings."
    # TODO: digi also needs a phone item
    show digi
    play sound sfx_ringtone_digi
    $ persistent.heard.add("sfx_ringtone_digi")
    digi "What the heck? No one ever calls me..."
    digi "CS? What could this be about?"

    play sound sfx_pickup_call

    # splitscreen
    show cs_room at offscreenleft
    show cs scared at offscreenleft
    with determination

    show cs_room at mid_offscreen_left behind cs
    show nugget_inside at mid_offscreen_right behind cs
    show cs scared at mid_left
    show digi at mid_right
    with move

    show digi shock
    cs "Digi! {nw}" with hpunch
    extend "I think I gave myself diabetes!"
    digi "What?! Huh--{nw}"
    cs "I ate a ton of food last night after I got home from our adventure and--"
    show digi
    digi "Oh yeah, did you ever get your pencil sharpener in the mail?"
    show cs surprised
    cs "No, I didn't, actual-- "
    show cs scared at mid_left
    show digi shock
    extend "Digi, this is important!" with vpunch
    show digi disappointed
    n "Digi sets down the screwdriver they were poking their arm with."
    digi "Listen, man. You can't just {i}get{/i} diabetes."
    digi "At least, not Type 1."
    show cs disappointed
    cs "What do you mean? How did {i}you{/i} get it, then?"
    digi "Type 1 is genetic. You kinda have it just lingering inside you until it decides to rear its ugly head."
    digi "For me, it cropped up when I was 2."
    cs "Wait, okay, then what's the difference between Type 1 and Type 2?"
    stop music fadeout 3.0
    music end
    digi "Well..."
    jump bt1d_basketball

label bt1d_basketball:
    play music basketball_music if_changed
    music basketball_music
    scene basketball_court
    # cut to a cutaway. a machine is on the left, a basketball hoop on the right. the background
    # is like, a chalkboard or something.

    digi "Imagine your body has a basketball machine in it. You need basketballs to live."
    show basketball_machine at right with moveinright
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
    jump bt1d_afterbball

label bt1d_afterbball:
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
    cs "OK..."
    n "CS hesitantly steps onto the ship."

    jump bt1d_cvs

label bt1d_cvs:
    # interior nugget
    cs "So, where are we going?"
    digi "I'm thinking CVS."
    cs "CVS--"
    cs "That's right down the road!" with hpunch
    digi "Yeah?"
    cs "Why do we need a whole spaceship for this?!"
    digi "We don't? I needed it to get to your house, I was on Microtech."
    cs "Where?"
    digi "It's in Stanton."
    cs "Wh-- why didn't we just use a car?!"
    digi "I can't drive."
    cs "But you can pilot a spaceship?!"
    digi "It's a lot easier, in my opinion. And I don't need a license for a spaceship."
    cs "{size=-10}I feel like you should..."
    digi "Anywho, to CVS!"

    # This scene should be beefed up a bit, I think.
    n "The Nugget lands in the CVS parking lot, and the two clammer out into the daytime."
    cs "To the pharmacy department!"

    n "CS and Digi arrive at the pharmacy, and confront the pharmacy worker."
    cvs "Welcome to CVS, can I help you today?"
    cs "Yeah, you can tell me why insulin is so expensive!"
    cvs "Do you have a prescription to pick up?"
    cs "No! I'm just pissed!"
    digi "Sorry, excuse him. He's being a bit {nw}"
    extend "{i}too aggressive." with hpunch
    cs "... Sorry."
    digi "The question is more generic, do you know why insulin is so expensive?"
    cvs "I don't really know, the insulin companies just set the prices. We don't have control of it."
    cs "Hmmm... what insulin companies?"
    cvs "It's mostly one, 'Leedlelee.'"
    digi "Well, that's all the information we're going to get. Thank you!"
    digi "Let's go, CS."
    n "CS and Digi walk out of the CVS."
    # let the shot linger here for a moment.
    n "The CVS worker picks up their work phone."
    cvs "A cat maid and a tiny cyborg just came in here assailing me about insulin prices."
    cvs "Am I reporting this? What is there to report? I'm just telling you, I guess."
    cvs "Get back to work? Yeah, that makes sense."
    # fade out
    jump bt1d_insulin

label bt1d_insulin:
    # interior nugget
    cs "So, now what?"
    digi "We gotta go find Leedlelee, I suppose."
    n "Digi starts plugging coordinates into the console of the ship."
    digi "I think I know where to go... the question is, will we be able to talk to the CEO."
    cs "I don't know if they're just going to let two idiots with an agenda up to the penthouse."
    digi "I've done weirder."
    cs "You know, come to think of it, so have I."
    digi "Then we'll try our luck!"

    n "The Nugget lands in to the parking lot of the Leedlelee offices."
    digi "No where to go but up!"
    cs "Let's do this."

    # interior office
    receptionist "Welcome to Leedlelee, do you have an appointment?"
    cs "No, we--"
    digi "Let me handle this."
    digi "We need to speak to the CEO."
    receptionist "I can't let you up without an appointment. The CEO is a very busy man."
    digi "We understand, we only need a minute of his time."
    receptionist "Hmm. Let's see how his mood is, then."
    n "The receptionist calls up to the CEO."
    receptionist "Yes, there's two people here to see you.{w=2} No, they don't have an appointment.{w=2} Yes, sir, I understand.{w=1} One minute, sir? I'll let them know.{w=2} Thank you, sir."
    n "The receptionist hangs up the phone."
    receptionist "You have one minute. Good luck."
    cs "Thank you so much!"
    receptionist "Don't mention it."
    digi "Let's hurry!"
    n "The two scurry into the elevator."

    # in the elevator
    cs "Do you think we'll get any information out of him?"
    digi "Only one way to find out. We need to convince him we're on his side."
    cs "Are we?"
    digi "To be honest?"
    digi "No."

    # elevator ding

    # interior penthouse office
    leedle "Who are you two? I don't have all day."
    cs "We're here to ask you a quick question."
    digi "We're looking for the source of these high insulin prices."
    cs "Yeah, why do you--"
    n "Digi shoulders CS in the side." with hpunch
    digi "What my friend {i}meant{/i} to say, was we don't think it's you."
    digi "My bet? There's someone up the chain pulling {i}your{/i} chain. Am I right?"
    leedle "And why would I tell you?"
    digi "Because we can help."
    leedle "Yeah? How do I know you aren't recording this with your cyborg gobbledygook, and you're going to blackmail me!"
    cs "{size=-20}{cshake}Guilty concious..."
    digi "Listen. I'll make you a deal."
    digi "If you tell us who's up to this, we'll (insert bribe here.)" # FIX
    leedle "Fine."
    leedle "Fine!"
    leedle "I don't know his name."
    leedle "He calls himself the CEO of Diabetes."
    n "Digi gasps."
    cs "What's wrong?"
    digi "I know him."
    cs "{i}You know him?!"
    digi "Yeah. I've fought with him before."
    digi "CS, let's go."
    digi "Thank you... what's your name?"
    leedle "(name)." # FIX
    digi "Thanks, (name)."
    n "Digi heads out back to the elevator, and CS quickly follows."

    n "The elevator ride is quiet, but the energy is tense."
    n "Even CS recognizes now isn't the time to speak."

    # getting into the nugget
    # interior nugget
    cs "So, can we talk about that?"
    digi "Yeah. I'm just annoyed."
    digi "I keep fighting this guy. Every year, he seems to crop back up."
    cs "Who is he?"
    digi "I don't know, either, man. He calls himself the CEO of Diabetes. He's a big, tough business man."
    digi "He's a weird one. One day, he'll be gunning for my destruction, the next he'll be calling me to see how I'm doing."
    cs "What does he want with you?"
    digi "Who knows, man. I'm diabetic. That's all I know."
    cs "Don't you raise money for charity, too?"
    digi "Yeah, that's probably part of it."
    cs "So, what does he do?"
    digi "Who knows, man? He makes... diabetes... worse for people? His job has always been very confusing."
    digi "But it seems his next scheme is to pay off insulin companies to not drop the price."
    cs "What now?"
    digi "If I know the CEO, I know where to find him."

    # smash cut, Digi kicks in the door to the CEO's office
    digi "CEO of Diabetes, I have come to--{w=0.5}{nw}"
    ceo "Oh my God, will you stop kicking down my door?!"
    ceo "Why do you keep doing this?! Just open it, it's not even locked!"
    digi "It's dramatic, I--{w=0.5}{nw}"
    ceo "I don't care! I'm going to start invoicing you for cleaning the door!"
    digi "I-- I'm here to yell at you!"
    n "CS walks in the office behind Digi."
    cs "Me too!"
    ceo "Who the heck are-- are you cs188?!"
    cs "Yeah."
    ceo "Why are you wearing a cat maid outfit?!"
    cs "I'm not going into that right now."
    ceo "OK, why are you here then?"
    cs "I researched the price of insulin, and it's egregious!"
    ceo "Heh heh heh, yeah. I did a good job with that, didn't I?"
    cs "No! You're extorting diabetics for cash!"
    ceo "Yeah. That's kinda what I do. And I'm damn good at it, too."
    digi "Alright, I'm not doing this song and dance again."
    digi "No bribes, no contracts."
    digi "Let's brawl."
    ceo "Heh! You think you can take me?"
    ceo "Alright, bet."
    ceo "You win, and I'll even call off the price hike."
    ceo "But if you lose..."
    n "A button rises like a piston on his desk."
    ceo "I release {i}Type 4 Diabetes{/i} on to the masses!"
    digi "You're on."
    cs "Y--Yeah! You're on!"

    # black knife starts playing idk

    # rpg battle 1 - ceo

    n "The CEO is panting on the floor."
    ceo "Heh... heh... you've gotten good, you little rat."
    ceo "But I'm not bested yet!"
    n "The CEO pushes a different button on his desk, and intercoms somebody."
    ceo "Secretary?"
    secretary "Yes, Mr. CEO?"
    ceo "I need you up here."
    digi "You have a secretary?"
    ceo "Do now."
    n "The door opens, and the Secretary of Diabetes walks through the door."
    n "The secretary glances at the situation around her."
    secretary "Kick their asses, sir?"
    ceo "Kick their asses."

    # rpg battle 2 - secretary

    # TODO: Beef up this dialouge?
    ceo "Ready for Round 2?"

    # rpg battle 3 - ceo + secretary

    ceo "Fine. You did well."
    secretary "These ones are good, sir."
    ceo "I'll call off the price hike."
    secretary "You're calling it off?"
    ceo "That was the deal."
    ceo "But I never said how long that will last..."
    ceo "Heh."
    ceo "Heh heh."
    ceo "Heh heh heh heh heh!"
    digi "Let's get out of here, CS."
    cs "Yeah, this guy is nuts."

    # interior nugget
    n "Back on the Nugget, the two sit in silence for a bit, Digi petting Lad for comfort."
    n "After a while, the silence breaks."
    digi "Well, we did it."
    cs "Yeah, we did. But how long until he tries something again?"
    digi "Pffft, not long. That's kinda his thing."
    cs "Then what's the point? Does this fight ever end?"
    digi "Yeah, one day. Not sure how long it'll take, but eventually."
    digi "That's why I raise money for Breakthrough T1D all the time."
    digi "Once we have a cure, there's not much more he can do."
    cs "Right. Well, good luck on the good fight."
    digi "Thanks, man."
    cs "I didn't realize this is what you do all the time!"
    digi "I do a lot of things people don't realize."

    # fade to exterior CS' house - night
    digi "Well, this is your stop. Have a nice night, CS!"
    cs "Thanks, Digi, glad I could help!"

    # TODO: this is barely an ending

    jump secret_dx
