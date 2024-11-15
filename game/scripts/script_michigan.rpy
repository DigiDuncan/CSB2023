label michigan:
    scene car plains
    show billy car
    with dissolve
    play music track_4 volume 0.4 if_changed
    music track_4
    billy "Alright. The highway entrance should be right around here."
    billy "We can head to Ohio, and then we'll be getting really close."
    billy "Fuck."
    cs "What's wrong?"
    billy "The entrance is closed. We should stop and ask what's going on."
    billy "There's someone over by the gas station. We can ask him."
    scene black with dissolve
    n "Billy pulls into a nearby gas station and gets out to talk."
    scene gas_station_2
    show streetguy at mid_right
    with dissolve
    show billy at mid_left with moveinleft
    billy "Hey, man. Do you know what's up with the highway?"
    streetguy "Not sure on details, but I hear they found one of the horsemen of the apocalypse flying around."
    streetguy "Possibly in Michigan."
    billy "What?"
    streetguy "Like I said, I don't know details."
    billy "Well, do you know which roads are affected? We need to get to New York."
    streetguy "Last I saw, the route through Michigan should still be open."
    streetguy "That's how I found out about the horseman of the apocalypse."
    streetguy "Michigan having better roads than literally any other place is a sign of the end times."
    billy "Alright, thanks for the help. I'm gonna get going."
    hide billy with moveoutleft
    scene black with dissolve
    n "Billy gets back in the car to tell the others what the stranger had told him."
    scene gas_station_2
    show billy car
    with dissolve
    cs "Well. I guess if we have no other option, we may as well go through Michigan."
    arceus "Yeah, they have corn and at least two other things, so it's honestly probably better than going through Ohio."
    billy "Sounds like a plan. The drive is gonna take longer with the detour though, so we should definitely get going."
    scene car plains
    show billy car
    with dissolve    
    n "They get on the highway and start heading towards Michigan."
    arceus "We're making progress. Finally in Michigan."
    stop music fadeout 3.0
    billy "It looks like we're coming up to a place called Bronson. Maybe we could stop there for food."
    menu:
        "Decide."
        "Try to stop going to Bronson" (type = "dx"):
            jump michigan_bronson
        "Don't say anything":
            jump michigan_continue

label michigan_bronson:
    scene car plains
    show billy car
    stop music fadeout 3.0
    cs "Look, man, just don't go to Bronson, okay?"
    billy "Okay, okay, we won't go."
    cs "It's just... I am getting a really bad vibe from that place."
    show billy car turn
    billy "CS, I already said we aren't going there, okay?"
    arceus "I'm getting chills thinking about it, too. CS is right."
    if fun_value(FUN_VALUE_MUSIC):
        billy "Okay, shut up! On me drive!"
    else:
        billy "Okay, shut up! Let me drive!"
    play music upon_me if_changed
    music upon_me
    cs "Billy, you took the Bronson exit."
    show billy car
    billy "..."
    scene car plains night
    show billy car
    with dissolve
    billy "Shit."
    n "As they continue into Bronson, the clouds darken. A crimson thunderstorm approaches."
    n "The screams of the damned can be heard, sounding more similar to cheering..."
    n "Welcome to Bronson."
    scene black with dissolve
    pause 2.0
    $ achievement_manager.unlock("We Don't Go To Bronson")
    play sound sfx_thunder volume 0.5 loop
    scene bronson_hell
    show cscar1arc
    show billy at left
    show cs scared flipped at right
    show cscar2
    with dissolve 
    cs "Holy shit... I think we are in hell."
    arceus "What the..."
    billy "Actual fuck."
    cs "Okay, okay, don't freak out."
    cs "This is the {i}worst{/i} time to freak out."
    cs "Maybe Michigan just gets surprise storms?"
    billy "With blood-red clouds?"
    arceus "If we keep going, maybe we'll just blow right through it...?"
    billy "It's the only option we've got."
    arceus "Bronson is small, right? We'll be out of here in no time!"
    cs "Yeah! Right, Billy?"
    billy "I think so... I mean, we survived a UFO attack,so this can't be much worse!"
    show cs disappointed flipped
    cs "Yeah!"
    billy "Also, well... if you didn't distract me, we wouldn't be here!"
    show cs worried flipped
    cs "Hey! I felt sick thinking about even the {i}name{/i} of this place!"
    arceus "Yeah... I don't know why, but I felt it too..."
    billy "Well, you need to shut your mouth when I am driving!"
    show cs disappointed flipped
    cs "Billy, what has gotten into you?"
    billy "I don't know, maybe because we are here because of {i}you?!"
    show cs angry flipped
    cs "Well, maybe {i}you{/i} need to keep your eyes on the road!"
    billy "Don't tell me how to drive, damn it!"
    arceus "Guys! Calm down!"
    cs "This is not my fault {i}at all!"
    billy "Just shut the fuck up!"
    billy "I shouldn't have picked you up to begin with! It's been nothing but trouble with you CS!"
    show cs disappointed flipped
    cs "What the hell, man?"
    play sound2 sfx_siren volume 0.1 loop
    arceus "Both of you, shut up! Do you hear... {i}something{/i} in the distance?"
    window hide
    stop music fadeout 5.0
    music end
    pause 5.0
    play sound2 sfx_siren volume 0.2
    pause 2.0
    play sound2 sfx_siren volume 0.3
    pause 2.0
    play sound2 sfx_siren volume 0.4
    show blue_light at left
    show red_light at right
    with dissolve
    pause 2.0
    play sound2 sfx_siren volume 0.5
    show cs scared flipped
    cs "Is... that...?"
    arceus "It's Copguy."
    cs "Billy, step on it!"
    billy "I'm going as fast as I can!"
    arceus "He's catching up!"
    cs "I think he's gonna ram us!"
    cs "Brace yourselves!"
    scene black with dissolve
    play sound2 sfx_car_crash volume 0.7 noloop
    pause 10.0
    play sound2 sfx_siren volume 0.2 loop
    scene bronsoncrash
    show billy laser at left
    show arceus dirty worried flipped at mid_left
    show cs disappointed flipped at mid_right
    with dissolve
    pause 2.0
    billy "Everyone, stay quiet."
    cs "Is he..."
    copguyexe "WHERE ARE YOU, CS?"
    billy "Hunker down and wait."
    billy "Get ready to fight."
    copguyexe "I CAN SMELL YOU."
    show cs worried flipped
    pause 3.0
    copguyexe "THERE YOU ARE. GET READY FOR YOUR WORST NIGHTMARE!"
    stop sound2 fadeout 1.0
    show copguyexe with dissolve
    scene white with dissolve
    pause 1.0
    jump rpg_bronsonbattle

label michigan_bronson_win:
    play sound sfx_thunder volume 0.5 loop if_changed
    stop music fadeout 3.0
    music end
    scene bronsoncrash
    show billy at left
    show arceus dirty flipped at mid_left
    show cs disappointed flipped at mid_right
    with dissolve
    cs "Holy crap, we did it."
    show arceus dirty worried flipped at mid_left
    arceus "I don't know what is happening, or {i}how,{/i} but I kinda just want to get out of here."
    billy "Sounds good to me. Let's get back on the road!"
    scene black with dissolve
    n "Thankfully, Billy's car is still operational."
    n "Shaken, the trio quickly drives away from this place."
    window hide
    pause 1.0
    play sound sfx_doorslam
    scene bronson_hell
    show cscar1arc
    show billy at left
    show cs disappointed flipped at right
    show cscar2
    with dissolve
    pause 3.0
    n "As Bronson gradually fades over the horizon behind them, no one says a word."
    cs "Is it okay... if we all just..."
    arceus "Forget about this?"
    cs "Yeah. I don't want to think about this ever again. That was spooky as hell."
    arceus "Yeah. Whatever else happens on this trip can't possibly be as bad as this."
    n "After a while, the storm finally clears up."
    stop sound fadeout 3.0
    scene car plains
    show billy car
    with dissolve
    billy "Hey, guys?"
    billy "I'm sorry for how I acted back there. I don't know what came over me."
    cs "You freaked me out when you said that I was ruining this trip."
    billy "Nonsense. I may have picked you guys up to take you home a few days ago..."
    billy "But I can say that you guys are friends for life."
    arceus "Same here."
    arceus "You guys are great."
    cs "Yeah, we've had some great times so far!"
    cs "I mean, that pizza back in Nebraska was pretty frickin' good."
    billy "And, in less creepy news, there are more exits coming up here..."
    billy "We've got both I-69 and I-94."
    billy "Which one are you guys down to take? I'm honestly up for anything that's not blood-red skies again."

    jump michigan_interstate_menu

label michigan_continue:
    scene car plains
    show billy car
    stop music fadeout 3.0
    arceus "Nah, this place looks too rural to have much around."
    n "The two look over to CS, who seems visibly distressed."
    arceus "Uh, CS? How's it going?"
    cs "I... should be fine."
    cs "Something about the name Bronson, Michigan sends a chill down my spine."
    arceus "We'll just skip it. Nothing around here anyway."
    scene black with dissolve
    n "They keep driving. CS continues muttering \"Don't go to Bronson\" until they finally stop seeing Bronson signs."
    scene car plains
    show billy car
    with dissolve
    billy "Alright. We're way past Bronson, but we're getting pretty far north."
    billy "We should probably find an exit to start heading towards New York soon."
    cs "There's an exit coming up. We can take either I-69 or 94."
    billy "Alright. Which one do you think?"
    arceus "Well, 94 goes east which is the direction we want, but the other one is 69, so I'm down for either."
    billy "I guess it's up to you then, CS."

    jump michigan_interstate_menu

label michigan_interstate_menu:
    # this label exists for timeline progression - tate
    scene car plains
    show billy car
    menu:
        "Which road should we take?"
        "I-69" (type = "warning"):
            jump michigan_interstate_69
        "I-94":
            jump michigan_interstate_94

label michigan_interstate_69_old:
    stop music fadeout 3.0
    window hide
    show screen warning("The following scene is a major tonal shift.\nIt may be disconcerting to some viewers.", "Warnings: creepy forests, haunting music, slow descents into madness.", "back_out_i69")
    pause
    window show
    $ nome = True
    cs "We're on a detour anyway. May as well take the funny route."
    billy "Alright. 69 it is."
    arceus "I don't know if that's safe while driving, but we can do that once we stop somewhere, I suppose."
    billy "I think I'm fine. You and CS can do that now if you want though."
    cs "That'd be hard with the seatbelts on, so I'll wait. What if we got into a crash?"
    cs "Remember to always have safe sex, kids."
    arceus "Fair point."
    arceus "I've been seeing signs for East Lansing for a while. Maybe we should stop there."
    billy "Any spiritual discomfort about that one, CS?"
    cs "No, that sounds fine. It'd be good to get some food in us."
    billy "Lansing it is."
    scene black with dissolve
    n "They get off at the exit and start driving into East Lansing."
    scene traffic
    show cscar1arc
    show billy at left
    show cs disappointed flipped at right
    show cscar2
    with dissolve 
    play music honk_song volume 0.8 if_changed
    music honk_song
    cs "I was expecting there to be people around, but I wasn't expecting traffic like this. I wonder what's going on?"
    arceus "All the people walking are wearing green and white, so it's probably a sports thing."
    billy "We are in Lansing. They have one of the biggest football schools in the country."
    cs "Really? I've never heard of that before."
    billy "Figures. You don't strike me as the type to know about sports."
    cs "You would be correct."
    arceus "God, the people on the sidewalk are going so much faster than us. What is this?"
    billy "I guess you can only get so many cars through a small intersection."
    arceus "Well, if it's so many damn cars, we should be through by now."
    billy "That's not what that expression means... Whatever. We just have to wait it out."
    cs "Hey, do you guys see that little guy? Over behind that tree?"
    billy "Oh, did Arceus get out to pee?"
    arceus "You can literally see me in your rear-view mirror right now."
    billy "Only if I squint."
    arceus "I'm not {i}that{/i} small, man..." # Me with the goddamn ellipses again lmao - Aria
    cs "No, look, that short guy. The one with the red pointy hat."
    arceus "Oh, shit, you're right! That looks like a gnome!"
    show cs worried flipped
    cs "God, did Blank somehow track me to Michigan?"
    arceus "Blank is at least three gnomes tall, though. That couldn't just be him in a costume."
    show cs disappointed flipped
    cs "You're probably right, but I wouldn't be all that shocked if he learned practical effects for a gag."
    show cs worried flipped
    cs "Wait, is he coming this way?!"
    n "The gnome steps out from behind the tree and makes his way to the door of the unoccupied seat of the car, motioning a request to roll down the window."
    billy "Holy shit, you two weren't kidding. I think he's trying to talk to us."
    stop music fadeout 3.0
    billy "I'm gonna see what he wants."
    play sound sfx_roll_window volume 0.7
    pause 2.0 
    # DX: It could be funny to have an option to ignore the gnome for a while
    play music wayward_wanderer volume 0.7 if_changed
    music wayward_wanderer
    if fun_value(FUN_VALUE_MUSIC):
        gnome "Hallo, I am a Wayward Wanderer, may I enter your Automobile?"
    else:
        gnome "Hallo, may I enter your Automobile?" 
    billy "What do you want with us?"
    gnome "I mean you no harm. May I sit and explain myself?"
    arceus "I don't think this guy is a threat. We may as well let him in."
    show cs disappointed flipped
    cs "He'll at least make this traffic jam more entertaining."
    billy "Alright, fine, come on in."
    gnome "I thank you. As you may be aware, I am not of your Species."
    arceus "I don't think I'm the same species as these two."
    gnome "That may be true, however, it appears that neither of your Species are the same as mein." 
    gnome "Therefore mein Point still stands, und thus I still must briefly introduce mein Volk und our Relationship to this Place."
    gnome "I am of the Forest, und I have recently become acquainted mit some of your Kind."
    gnome "Deine Group has a similarly unique Redolence to those I encountered."
    gnome "As I am a Being of the Forest and of the Land surrounding it, I find myself in a Position to assist you."
    cs "Alright, this is a lot to take in, but at this point I'll do anything to get out of this car."
    cs "How can you help us?"
    gnome "My kind is not of this World, but rather of the Forest Dimension. I cannot clear this Path, but I can bring you to another."
    cs "Yeah, that may as well happen to us at this point."
    show cs happy flipped
    cs "Thanks for your help." 
    gnome "No need to thank me. It is mein Pleasure."
    n "Everyone feels an energy emanate from the gnome as they watch the environment around them transform from a modern university into a dense forest."
    scene gnome_forest
    show cscar1arc
    show billy at left
    show cs flipped at right
    show cscar2
    with dissolve
    n "The buildings disappear as more trees, bushes, and brush spring forth from the ground as if you were watching a timelapse of hundreds of years of nature."
    n "Eventually, the growth comes to a halt as any semblance of their old surroundings is buried in a lush and lively grove."
    n "They find themselves on a clear path through the trees as the sunlight shining through the canopy up ahead starkly contrasts the heavy darkness of the woods behind them."
    gnome "If you continue to drive, you will reach a Clearing with a large Sugar Maple surrounded by a Bed of Clovers."
    billy "Where will it take us once we return to our own world?" 
    gnome "We will simply return to the Edge of the Campus. You will be able to continue your Journey smoothly."
    scene forest_clearing_magic
    show billy car
    with dissolve
    n "Billy takes the car forward and stops in front of the tree."
    n "As they pull into the clearing and stop the car, they again become aware of the gnome's presence."
    n "The gnome remains silent as the energy no longer seems to be radiating from him, but returning to him."
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    n "The forest, which had previously sprung forward as if growing naturally, fell rapidly before their eyes."
    scene white
    show billy car turn
    with dissolve
    n "A glowing white cut appears through the trees before the remaining trunks also decay into a mass of bright light."
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    n "The light begins to appear at the base of the bushes before the ground that housed their roots is tossed out, taking the bushes along with it."
    scene parking_lot
    show billy car turn
    stop music fadeout 3.0
    music end
    n "Finally, the forest's brush, along with the detritus of other plants that dotted the ecosystem, disappears in a sea of white flame that leaves them in a desolate parking lot."
    show billy car
    $ achievement_manager.unlock("You've Been Gnomed")
    billy "Well, that was deeply disconcerting."
    gnome "If you are not used to it, I suppose so."
    billy "I think I need a break from driving after all that."
    cs "Yeah, that's fine. I was getting hungry anyway."
    cs "Hey Mx.{w=0} Gnome, do you know anywhere good to eat around here?"
    gnome "I don't often eat Human Food, however, I do know of one Restaurant because of my previous Human Encounter."
    cs "Cool! Can you take us there?"
    gnome "Of course. It is right around this Corner. Simply take a Right Turn. It's called East Cafe."
    billy "Oh, yeah, I see it. That really {i}is{/i} close!"
    cs "Definitely. I'm just excited to get in and eat."
    scene black with dissolve
    n "The gang gets out of the car and heads over to East Cafe."
    scene cafe_entrance
    show cs at left
    show arceus flipped at mid_left
    show billy at center
    show gnome at mid_left_left
    with dissolve
    show waitress at right with moveinright
    waitress "Welcome, welcome. Please wait, and I'll come seat you in a minute."
    hide waitress with moveoutright
    n "As everyone is waiting, the strange glowing grey blob in the corner notices the group and floats over."
    show aria at right with moveinright
    play music mis_leader volume 0.7 if_changed
    music mis_leader
    aria "CS! Arc! What are you doing here?"
    gnome "Aria! I knew I recognized that Scent."
    aria "OMG, hi! So, you brought them here?"
    gnome "That I did. They were stuck in the Game Day Traffic."
    aria "Yeah, that'll happen."
    show cs disappointed
    cs "Wait, who are you?"
    aria "It's Aria. You know, we met all the mall?"
    cs "Wait, what? I remember that, and you definitely didn't look like this."
    show cs
    aria "I dunno, people change."
    aria "Speaking of surprising, is that Billy Mays with you?"
    billy "In the flesh."
    aria "Didn't you die of a heart attack or cocaine overdose or something?"
    billy "Cocaine-induced heart attack, yeah."
    billy "You're a formerly-human floating grey blob that hangs out with gnomes. I don't think I'm the weirdest thing here right now."
    aria "Fair enough. Do you all wanna eat with me?"
    cs "Sure. It's been a while."
    scene black with dissolve
    n "CS and the gang sit down with Aria."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    with dissolve
    show waitress at right with moveinright    
    aria "Alright."

    $ translate_this_line = "Waitress, they'll sit with me!"
    aria "{a=show:show_tl}{font=cn}老板娘！他们会跟我一起坐。{/font}{/a}"

    $ translate_this_line = "OK!"
    waitress "{a=show:show_tl}{font=cn}可以啊！{/font}{/a}"

    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right  
    billy "Oh, you speak Chinese?"
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "Yeah. I got tired of having to ask for chopsticks whenever I came here, and I figured if I spoke Chinese, they'd just assume that I'd want them."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    billy "Did that work?"
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "It did. Not sure that the return on investment made sense effort-wise, but it's a cool skill either way."
    aria "What did you all want to eat?"
    gnome "Frog Legs sound good."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus happy at right
    arceus "I've always wanted to try chicken feet. I'll get some of those."
    show arceus
    show cs happy
    cs "Pork fried rice, please."
    show cs
    billy "Ooh, jellyfish. I'll get that."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right

    $ translate_this_line = "Please give me a bowl of fish-flavored eggplant. Let me ask, if I just said some random shit, you wouldn't tell them, right?"
    aria "{a=show:show_tl}{font=cn}请给一碗鱼香茄子。请问一下，如果我说一点狗屁，你不会告诉他们，对吧？{/font}{/a}"

    $ translate_this_line = "No, I won't."
    waitress "{a=show:show_tl}{font=cn}对，我不会。{/font}{/a}"

    $ translate_this_line = "Okay. Thanks. Unless they use Google Translate, they won't understand it at all."
    aria "{a=show:show_tl}{font=cn}好啊。谢谢。除非他们使用{/font}Google Translate, {font=cn}他们完全听不懂。{/font}{/a}"

    $ translate_this_line = "I want them to think my Chinese is better than it really is."
    aria "{a=show:show_tl}{font=cn}我想让他们以为我的中文水平比我真的水平更好。{/font}{/a}"

    $ translate_this_line = "My hovercraft is filled with eels."
    aria "{a=show:show_tl}{font=cn}我的气垫船装满了鳝鱼。{/font}{/a}"

    waitress "Wow, your Chinese sounds like a native, but you're clearly utterly insane."
    aria "Wow, that phrasebook was really helpful."
    waitress "By the way, we don't have any pork to fry the rice right now."
    scene cafe_sitting_2
    show cs disappointed at left
    show billy at center
    show arceus worried at right
    arceus "Wait, how?! That's by far the most popular thing we ordered..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "Pigs are expensive and they have a good union. We just hired a bunch of shrimp instead."
    scene cafe_sitting_2
    show cs disappointed at left
    show billy at center
    show arceus angry at right
    arceus "I'm not playing along with that joke."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "It wasn't meant to be humorous, but, fair enough."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "I'll just get chicken fried rice."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "Alright, I'll be back in a bit."
    hide waitress with moveoutright
    n "Everyone starts a conversation as the waitress walks off."
    aria "So, CS, it's been a while since I saw you. How's it been?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "It's been... a hell of a lot."
    cs "Not horrible, but things could definitely have gone smoother."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Yeah, life is like that sometimes. Glad things have been largely okay, though."
    aria "How about you, Arc? It's weird seeing you in person. How's moving to the UK been? Have you been visiting the US for long?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus worried at right
    arceus "I'm not sure if that move is happening in this timeline..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Ah, yeah, that happens. I guess not every plan is meant to be."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    arceus "That wasn't what I meant by timeline, but it would be a lot to explain, so we'll go with that."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "So, Billy, what's your story? You don't have to go into it if you don't want, but I'm very curious."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    billy "Well, I died of a heart attack, got buried, came back from the dead, dug my way out of the grave, and tried to go back to normal."
    billy "People just assumed I was an imposter, and I couldn't get any pitchman gigs, so I became an Uber driver."
    billy "Then these guys showed up and I offered to drive them from Washington to New York."
    billy "I heard CS was a YouTuber, so I was just expecting some MrBeast-style video."
    billy "Now, I'm stuck hanging out with gnomes and floating blobs, and going through forest dimensions."
    pause 1.0
    billy "No offense."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    gnome "G'none taken."
    aria "A little bit taken, but I also brought up your cocaine overdose immediately after first meeting you, so fair play, honestly."
    aria "Y'all are headed to New York, then?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "Yeah, I'm just trying to get home, and these two kinda got dragged along."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Would you like to come rest at my apartment for a while? I have enough space for you all to get some sleep."
    aria "I also have a really pretty wooded area behind my apartment I can take you through."
    aria "You've all been through a lot. It'd be a good way to relax before you finish the drive."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    arceus "That'd be great. It'd be nice to get some proper rest."
    billy "I'd be happy to be off the road for a while longer. I think I might've had enough of forests for today, though..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    gnome "A Forest will do you good. They're good for your Health."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "Yeah, sure, we'll go over there after we eat."
    show waitress at mid_right with moveinright
    waitress "Here's everyone's food. Enjoy your meal!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "They all eat and then leave the restaurant. The gnome goes back to his forest, and the others head to Aria's apartment for a rest."
    scene aria_apartment_outside
    show billy car
    with dissolve
    aria "You can park here next to the building."
    billy "Alright. I know it's early, but I'm ready to just sleep."
    arceus "Yeah, that sounds good."
    aria "Sounds like a plan. I'll get you some sleeping bags, and blankets for whoever wants to sleep on the couch."
    scene black with dissolve
    n "Aria goes to her room as everyone rests. She hears them waking up late into the night and goes back out to check on them."
    scene aria_room
    show cs at left
    show billy at mid_left behind cs
    show arceus flipped at center
    with dissolve
    show aria at right
    with moveinright
    aria "Hey, everyone. How'd you sleep?"
    show cs happy
    cs "It was great. Thanks."
    show cs
    aria "So, when are you all planning to head out? I imagine you probably want to head out soon, but I would like to show you the woods."
    aria "I love the nature around here, so I spend a lot of time out there. Feels like a waste to not check it out while you're in the area."
    arceus "That does seem relaxing. May as well have a normal field trip instead of all these crazy adventures."
    cs "Yeah, sure."
    billy "Well, if everyone else is going, may as well check it out."
    scene black with dissolve
    n "They all walk through the parking lot until they come to the entrance to the forest."
    n "The woods are at a lower height, and the group walks down a path of cracked concrete, ducking under branches that hang over the path."
    n "The cover of the trees is still thin, but the shadows are starting to cover their limited moonlight."
    scene path_entrance
    show cs disappointed dark flipped at mid_right
    show arceus worried dark at right
    show billy dark at center
    show aria dark flipped at left
    with dissolve
    play music dense_woods_b volume 0.5 if_changed
    music dense_woods_b
    billy "Why does the window by the entrance have to be bright red?"
    billy "I've had enough of spooky forests today."
    aria "It's fine. That guy always has his lights set to red."
    aria "It's admittedly a little creepy, but you get used to it."
    cs "That's probably the least concerning thing we've seen in a forest so far today, to be fair."
    arceus "Still seems plenty murderous to me."
    aria "I'm out here most nights, and he hasn't murdered me yet, so I wouldn't worry too much."
    scene forest_bridge
    show cs dark flipped at mid_right
    show arceus dark at right
    show billy dark at left
    show aria dark flipped at center
    with dissolve
    aria "We're gonna take a left at the bridge up ahead. The forward path just spits us right out onto a normal street."
    billy "We've been out here for all of five minutes and that's already seeming like the better option..."
    aria "Nah, trust me. This path has all the best plants and the only real path through the forest."
    aria "White banesberry, hawthorn, sugar maple."
    aria "It's really pretty."
    show cs disappointed dark flipped behind arceus
    cs "What do you mean by \"the only real path\"? Aren't we currently walking through a forest?"
    aria "This isn't a forest, this is just a concrete path with trees on the sides."
    aria "Once you're actually in the woods, you're surrounded by plants of all kinds."
    aria "The smallest of them just springing up from the ground."
    aria "The tallest spreading their roots and taking command of the very earth we all draw our energy from."
    show arceus worried dark
    arceus "You're not helping this seem any more normal..."
    aria "What do you mean? It's perfectly natural."
    scene creepy_path
    show cs worried dark flipped at mid_right
    show arceus worried dark at right
    show billy dark at left
    show aria dark flipped at center
    with dissolve
    aria "Anyway, the forest path is right up there."
    billy "Are you kidding? This path is dark enough. That's not a path, that's a portal to the void."
    cs "Yeah, I don't know about that."
    aria "It's fine, it's my typical path."
    aria "We have flashlights, and honestly, the moonlight is usually enough for me once I get in there."
    billy "You're also an incomprehensible entity. We have a different scale."
    aria "I guess you're welcome to just head back out on the road."
    aria "Just watch out for fae paths on the way back."
    billy "What the hell is a fae path?"
    aria "Oh, they're paths that look like a normal path for the first little while, but end up placing you in the center of the woods."
    aria "The sense of linear direction decays as the path becomes less clear, and you eventually can't tell what direction you came from."
    billy "And you didn't think it was relevant to mention this before?"
    aria "Well, no, you have a guide. I was planning on making this a relaxing walk, so I didn't plan on taking the fae paths."
    billy "Why would you ever?!"
    aria "Well, they put you into some pretty parts of the woods."
    billy "Your obsession with these woods is not healthy."
    aria "How come? It gets me fresh air and exercise."
    show cs disappointed dark flipped behind arceus
    aria "Anyway, this path loops around to where we came from, so if you wanna leave, it's the fastest way back at this point."
    billy "So, no matter which way I take, I'm at risk of ending up in a cursed path to the middle of a haunted forest?"
    aria "I wouldn't say cursed or haunted, but I would advise staying with me."
    aria "Any unfamiliar woods comes with a chance of getting lost, and I imagine you all don't want that."
    billy "Why would anyone?!"
    aria "To each their own, I suppose."
    billy "What do you all think?"
    show cs dark flipped behind arceus
    cs "I've not had any reason to distrust Aria before, and having someone who knows the woods has to be good."
    show arceus dark
    arceus "Yeah, these woods are gonna be creepy no matter what route we take. We may as well pick the fastest one."
    aria "Alrighty then, follow me everyone."
    scene creepy_path_2 with dissolve
    n "As the group enters the path, a ray of moonlight shines through a gap in the canopy."
    n "Rustling noises can be heard further into the woods, but the path through the trees is clear, albeit dimly lit."
    stop music fadeout 3.0
    music end
    scene creepy_path_4 with dissolve
    play music melancholy if_changed
    music melancholy
    aria "If you look to the right, you'll see one of my favorite paths in the woods."
    aria "It's not exactly clear, so we'll skip it today, but it leads to a pretty little grotto."
    aria "It feels like something out of a fairy tale."
    cs "This whole forest does, but only the uncensored Brothers Grimm versions."
    aria "Yeah, it really feels like an authentic fairy tale experience c:"
    cs "That's not a good thing..."
    scene doll_eye_tree
    n "Aria stopped listening because it's distracted by a tree up ahead."
    if fun_value(FUN_VALUE_COMMON): 
        aria "Here's one of the white baneberries that I was talking about. They're also known as {i}Actaea Pakoopoda,{/i} or Doll's Eyes."
    else:
        aria "Here's one of the white baneberries that I was talking about. They're also known as {i}Actaea Pachypoda,{/i} or Doll's Eyes."
    arceus "I can see where they got the name!"
    aria "It does have thick stalks that fit the pachypoda name."
    arceus "Not the altiora poke-and-prod-er or whatever, the fucking doll's eyes!"
    arceus "That tree is watching us."
    aria "I like to think that Mother Nature watches us through all the trees."
    arceus "This isn't the time for metaphors! It has eyes that blink!"
    aria "Well, of course, they'd water too much if they didn't."
    arceus "Oh for f--{w=0.5} whatever, just get us out of here!"
    aria "No need to worry, we're on the way."
    arceus "As long as we're on the fastest path out of here, I'm happy."
    cs "Aria, how exactly do you find this relaxing?!"
    aria "I simply appreciate the beauty of the world around me."
    billy "I think that's fair. That {i}is{/i} a very pretty tree."
    aria "Thank you! See? {i}Someone{/i} gets it!"
    cs "Oh no, I think the woods are getting to him. He's getting some kind of environmental Stockholm syndrome." 
    cs "We've gotta get out of here, quick, before he gets worse."
    billy "I wouldn't be too worried about it."
    billy "I'm also terrified right now, but there's a certain macabre beauty that cuts through it..."
    arceus "Weren't you already scared going into this?"
    arceus "Like, before there were any clear signs of this weirdness?"
    arceus "There's no way that shift is natural."
    billy "There's nothing wrong with feeling the irresistible pull of nature."
    cs "Okay, that's definitely concerning."
    cs "Let's pick up the pace."
    aria "We're already going on the fastest path. I wouldn't deviate from the plan."
    scene creepy_path_fairy with dissolve
    cs "I didn't mean to change paths, I just meant to go down it faster--{w=0.5} wait, what's that glowing thing up ahead?"
    aria "Oh, that's strange, They don't normally appear on this path..."
    aria "That's one of the Faeries."
    aria "I've seen one like that before, with the glowing white body and warm yellow-colored edges."
    aria "I haven't seen that many Faeries, but I've kept track as I encounter new varieties."
    aria "I call this kind Seraphites."
    aria "They have particularly warm energy and have a brighter glow, as well as higher pitched resonance."
    cs "Resonance?"
    aria "The tone They produce as They float around."
    aria "It's similar to a CRT whine, so it might be too high-pitched for you to be able to hear it."
    arceus "I can hear CRTs, but I don't hear that..."
    billy "What are you talking about? That's so loud, how can you not hear it?"
    cs "Wait, Billy and Aria are the only two that can hear it?!"
    cs "The Fae must have something to do with the weird forest obsession."
    cs "We need to get Billy out of here, ASAP."
    arceus "We can't go forward with it up ahead!"
    aria "You can just walk past It. Faeries are mischievous, but They aren't malevolent."
    arceus "Maybe not to {i}you!{/i} You're also a glowing blob!"
    aria "I wasn't always, and They left me alone then, too."
    cs "I don't know if I want to try and go back if we've encountered the Fae that make the trick paths..."
    cs "I guess we don't have any other options."
    show creepy_path_3 with dissolve
    n "They all slip past the Seraphite, and It floats off between the trees."
    n "They walk further along the path, which becomes less clear as tree branches block their way."
    aria "Huh, these aren't normally here..."
    arceus "What do you mean \"not normally here\"?! Is this path changing?!"
    cs "What the hell? How are we getting out of here?!"
    billy "I guess we've gotta just go through."
    arceus "Go through where?! These branches are about as thick as the trees on the side!"
    billy "We go down the same way we've been going."
    billy "What's your issue? You're short enough that you don't even need to crouch to get under the branches."
    arceus "Fuck off."
    arceus "I guess you're right, though. We can't really turn back now."
    n "Everyone begins making their way through the nest of tree branches."
    n "Eventually, they reach the end and the canopy begins to thin out as they reach a path next to a road."
    show creepy_path_exit
    aria "Alright, here's the path back."
    arceus "Are you sure?! Can you guarantee me that this path is the same way it's supposed to be?!"
    aria "Yeah, that path is the same as it always is."
    billy "That path goes back the same way we came, of course it's fine."
    arceus "That was what she said about the last path and then we ended up climbing between a tangled web of branches."
    show billy at left
    show cs worried
    show arceus worried at mid_left
    show aria dark at right
    with dissolve
    arceus "That's a normal road with a sidewalk over there. We're taking that."
    cs "I'm with Arceus on this one."
    cs "I don't think I'll be able to go between two rows of trees without having a panic attack for a while."
    aria "I think Michigan roads are scarier than any forest, but I'll take you back on whichever path you want."
    $ achievement_manager.unlock("Analog Horror Protagonist")
    n "They all walk down and reach the apartment, then make their way to where the car is parked."
    scene aria_apartment_outside
    show billy at left
    show cs 
    show arceus flipped at mid_left
    show aria at right
    with dissolve
    stop music fadeout 3.0
    music end
    aria "Thanks for hanging out with me. It was fun."
    aria "Sorry you two didn't enjoy the woods, but I'm glad at least Billy seemed to like it."
    show cs disappointed
    cs "I guess nothing was actively dangerous, and that's above average for us at this point."
    show cs
    cs "Thanks for letting us rest at your place."
    aria "Anytime."
    aria "Billy, it was nice meeting you. You're welcome to come back and visit the woods again."
    billy "It was nice meeting you too. I'll definitely come back next time I'm in Michigan."
    aria "CS, it was also nice seeing you again." 
    aria "And, Arceus, it was nice finally meeting you in person."
    arceus "You, as well, until we went to the woods."
    aria "Yeah, sorry about that..."
    billy "You're fine. It was nice then, too. He's just got a bit of a skill issue, I think."
    arceus "Whatever, man..."
    aria "Bye-bye, y'all! Good luck on your adventure!"
    scene black with dissolve
    jump true_ohio

label michigan_interstate_69:

    call screen warning("The following scene is a major tonal shift.\nIt may be disconcerting to some viewers.", "Warnings: creepy forests, haunting music, slow descents into madness.", "back_out_i69")

    scene car plains
    show billy car
    stop music fadeout 3.0
    $ nome = True
    cs "We're on a detour anyway. May as well take the funny route."
    billy "Alright. 69 it is."
    cs "I get it, it's like--{w=0.5}{nw}"
    arceus "Yeah, yeah, it's sex."
    billy "Don't start fucking in the backseat, I'm almost out of Kaboom!"
    arceus "We should get something to eat, I saw a town called Lansing I think?"
    billy "Yeah, it's a couple exits ahead. We can head out that way."
    scene black with dissolve
    n "They get off at the exit and start driving into East Lansing."
    scene traffic
    show cscar1arc
    show billy at left
    show cs disappointed flipped at right
    show cscar2
    with dissolve 
    play music honk_song volume 0.8 if_changed
    music honk_song
    cs "Ugh, traffic? Billy, you have a dashcam, right?"
    show cs flipped
    billy "Of course! I have the Crash Stopper! The fast and easy way to make sure you never crash again!"
    arceus "You sold dashcams?"
    billy "I was gonna pitch the Crash Stopper, but y'know, I kinda..."
    cs "You died?"
    billy "Yeah."
    cs "Speaking of, How did you come back to--{w=2.0}{nw}"
    billy "What in the actual fuck? Didja see that?"
    arceus "What? what?"
    billy "There was like this, gnome thingy walking around. Look out on the left!"
    show cs worried flipped
    cs "God, did Blank somehow track me to Michigan?"
    arceus "Nah, Blank looks like a Catboy.             Musical."
    show cs disappointed flipped
    cs "You're right, but I wouldn't be all that shocked if he learned practical effects for a gag."
    show cs worried flipped
    cs "Wait, is he coming this way?!"
    n "The gnome steps out from behind the tree and makes his way to the door of the unoccupied seat of the car, motioning a request to roll down the window."
    billy "Holy shit! You two weren't kidding. I think he's trying to talk to us."
    show cs disappointed flipped
    stop music fadeout 3.0
    billy "I'm gonna see what he wants, grab the Awesome Augement if he tries to do anything funny."
    play sound sfx_roll_window volume 0.7
    pause 2.0 
    # DX: It could be funny to have an option to ignore the gnome for a while
    play music wayward_wanderer volume 0.7 if_changed
    music wayward_wanderer
    if fun_value(FUN_VALUE_MUSIC):
        gnome "Hallo, I am a Wayward Wanderer, may I enter your Automobile?"
    else:
        gnome "Hallo, may I enter your Automobile?" 
    billy "Hi, Billy Mays here! What are doing next to my car?"
    gnome "I mean you no harm. May I sit and explain myself?"
    arceus "See CS, he's not Blank. I don't think Blank has a German accent."
    show cs disappointed flipped
    cs "He'll at least make this traffic jam more entertaining."
    billy "Alright, fine, come on in."
    gnome "I thank you. As you may be aware, I am not of your Species."
    arceus "I don't think I'm the same species as these two."
    gnome "That may be true, however, it appears that neither of your Species are the same as mein." 
    show cs flipped
    gnome "Therefore mein Point still stands, und thus I still must briefly introduce mein Volk und our Relationship to this Place."
    gnome "I am of the Forest, und I have recently become acquainted mit some of your Kind."
    gnome "Deine Group has a similarly unique Redolence to those I encountered."
    gnome "As I am a Being of the Forest and of the Land surrounding it, I find myself in a Position to assist you."
    cs "Arceus, do you speak German?"
    arceus "It's an accent dude, and I think he can help us."
    gnome "My kind is not of this World, but rather of the Forest Dimension. I cannot clear this Path, but I can bring you to another."
    cs "As long as there are no cultists, last time we were at a forest, we almost got killed."
    gnome "No, no cultists. Just more of mein volk. Are you all ready?"
    n "Everyone feels an energy emanate from the gnome as they watch the environment around them transform from a modern university into a dense forest."
    scene gnome_forest
    show cscar1arc
    show billy at left
    show cs worried flipped at right
    show cscar2
    with dissolve
    n "The buildings disappear as more trees, bushes, and brush spring forth from the ground as if you were watching a timelapse of hundreds of years of nature."
    n "Eventually, the growth comes to a halt as any semblance of their old surroundings is buried in a lush and lively grove."
    n "They find themselves on a clear path through the trees as the sunlight shining through the canopy up ahead starkly contrasts the heavy darkness of the woods behind them."
    gnome "If you continue to drive, you will reach a Clearing with a large Sugar Maple surrounded by a Bed of Clovers."
    billy "Alright everyone, this may be bumpy!"
    show billy with hpunch
    pause 0.5
    show billy with vpunch
    pause 0.5
    show billy with hpunch
    pause 0.5
    show billy with vpunch
    pause 0.5
    scene forest_clearing_magic
    show billy car
    with dissolve
    n "Billy takes the car forward and stops in front of the tree."
    n "As they pull into the clearing and stop the car, they again become aware of the gnome's presence."
    n "The gnome remains silent as the energy no longer seems to be radiating from him, but returning to him."
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    n "The forest, which had previously sprung forward as if growing naturally, fell rapidly before their eyes."
    scene white
    show billy car turn
    with dissolve
    n "A glowing white cut appears through the trees before the remaining trunks also decay into a mass of bright light."
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    show billy car turn with hpunch
    show billy car turn with vpunch
    n "The light begins to appear at the base of the bushes before the ground that housed their roots is tossed out, taking the bushes along with it."
    scene parking_lot
    show billy car turn
    stop music fadeout 3.0
    music end
    n "Finally, the forest's brush, along with the detritus of other plants that dotted the ecosystem, disappears in a sea of white flame that leaves them in a desolate parking lot."
    show billy car
    $ achievement_manager.unlock("You've Been Gnomed")
    billy "That'll leave a mark on my 6000 pound car!"
    gnome "Sorry, do you have good Vagen Inzuurance?."
    billy "No worry, I have tons of Might Putty!"
    cs "Hey Gnome... dude, do you know anywhere good to eat around here?"
    gnome "I don't often eat Human Food, however, I do know of one Restaurant because of my previous Human Encounter."
    cs "Woohoo! Can you take us there?"
    gnome "Of course. It is right around this Corner. Simply take a Right Turn. It's called East Cafe."
    billy "Oh, yeah, I see it. That really {i}is{/i} close!"
    cs "Definitely. I'm just excited to get in and eat."
    scene black with dissolve
    n "The gang gets out of the car and heads over to East Cafe."
    scene cafe_entrance
    show cs at left
    show arceus flipped at mid_left
    show billy at center
    show gnome at mid_left_left
    with dissolve
    show waitress at right with moveinright
    waitress "Welcome, welcome. Please wait, and I'll come seat you in a minute."
    hide waitress with moveoutright
    if fun_value(FUN_VALUE_MUSIC):
        n "As everyone is waiting, the strange misleading grey blob in the corner notices the group and floats over."
    else:
        n "As everyone is waiting, the strange glowing grey blob in the corner notices the group and floats over."
    show aria at right with moveinright
    play music mis_leader volume 0.7 if_changed
    music mis_leader 
    aria "CS! Arc! What are you doing here?"
    gnome "Aria! I knew I recognized that Scent."
    aria "OMG, hi! So, you brought them here?"
    gnome "That I did. They were stuck in the Game Day Traffic."
    aria "Yeah, that'll happen."
    show cs disappointed
    cs "Wait, who are you?"
    aria "It's Aria. You know, we met all the mall?"
    cs "Wait, what? I remember that, and you definitely didn't look like this."
    show cs
    aria "I dunno, people change."
    aria "Speaking of surprising, is that Billy Mays with you?"
    billy "Hi, it's Billy!"
    aria "Didn't you die of a heart attack or cocaine overdose or something?"
    billy "Yep! Don't mix that shit with Oxy Clean, lemme tell ya."
    billy "Also, what the actual fuck? If i'm so surprising, what about you? You look like a sentient mixture of Oxi Clean and Kaboom!"
    aria "Fair enough. Do you all wanna eat with me?"
    cs "Sure, we had some pizza a couple days ago and we haven't ate much since."
    scene black with dissolve
    n "CS and the gang sit down with Aria."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    with dissolve
    show waitress at right with moveinright
    aria "Alright."

    $ translate_this_line = "Waitress, they'll sit with me!"
    aria "{a=show:show_tl}{font=cn}老板娘！他们会跟我一起坐。{/font}{/a}"

    $ translate_this_line = "OK!"
    waitress "{a=show:show_tl}{font=cn}可以啊！{/font}{/a}"

    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right  
    billy "Oh, you speak Chinese?"
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "Yeah. I got tired of having to ask for chopsticks whenever I came here, and I figured if I spoke Chinese, they'd just assume that I'd want them."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    billy "Did that work?"
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    aria "It did. Not sure that the return on investment made sense effort-wise, but it's a cool skill either way."
    aria "What did you all want to eat?"
    gnome "Frog Legs sound good."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus happy at right
    arceus "I've always wanted to try chicken feet. I'll get some of those."
    show arceus
    show cs happy
    cs "Pork fried rice, please."
    show cs
    billy "Ooh, jellyfish. I'll get that."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right

    $ translate_this_line = "Please give me a bowl of fish-flavored eggplant. Let me ask, if I just said some random shit, you wouldn't tell them, right?"
    aria "{a=show:show_tl}{font=cn}请给一碗鱼香茄子。请问一下，如果我说一点狗屁，你不会告诉他们，对吧？{/font}{/a}"

    $ translate_this_line = "No, I won't."
    waitress "{a=show:show_tl}{font=cn}对，我不会。{/font}{/a}"

    $ translate_this_line = "Okay. Thanks. Unless they use Google Translate, they won't understand it at all."
    aria "{a=show:show_tl}{font=cn}好啊。谢谢。除非他们使用{/font}Google Translate, {font=cn}他们完全听不懂。{/font}{/a}"

    $ translate_this_line = "I want them to think my Chinese is better than it really is."
    aria "{a=show:show_tl}{font=cn}我想让他们以为我的中文水平比我真的水平更好。{/font}{/a}"

    $ translate_this_line = "My hovercraft is filled with eels."
    aria "{a=show:show_tl}{font=cn}我的气垫船装满了鳝鱼。{/font}{/a}"

    waitress "Wow, your Chinese sounds like a native, but you're clearly utterly insane."
    aria "Wow, that phrasebook was really helpful."
    waitress "By the way, we don't have any pork to fry the rice right now."
    scene cafe_sitting_2
    show cs disappointed at left
    show billy at center
    show arceus worried at right
    arceus "Wait, how?! That's by far the most popular thing we ordered..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "Pigs are expensive and they have a good union. We just hired a bunch of shrimp instead."
    scene cafe_sitting_2
    show cs disappointed at left
    show billy at center
    show arceus angry at right
    arceus "I'm not playing along with that joke."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "It wasn't meant to be humorous, but, fair enough."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "I'll just get chicken fried rice."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    show waitress at right
    waitress "Alright, I'll be back in a bit."
    hide waitress with moveoutright
    n "Everyone starts a conversation as the waitress walks off."
    aria "So, CS, it's been a while since I saw you. How's it been?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "It's been... a hell of a lot."
    cs "Not horrible, but things could definitely have gone smoother."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Yeah, life is like that sometimes. Glad things have been largely okay, though."
    aria "How about you, Arc? It's weird seeing you in person. How's moving to the UK been? Have you been visiting the US for long?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus worried at right
    arceus "That move hasn't happened yet in this timeline..."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Ah, yeah, that happens. I guess not every plan is meant to be."
    aria "So, Billy, what's your story? You don't have to go into it if you don't want, but I'm very curious."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    billy "Well, I died of a heart attack, but somehow I came back alive again."
    billy "People just assumed I was an imposter, and I couldn't get any pitchman gigs, so I became an Uber driver."
    billy "Then these guys showed up and I offered to drive them from Washington to New York."
    billy "I heard CS was a YouTuber, so I was just expecting some MrBeast-style video."
    billy "Now, I'm stuck hanging out with gnomes and floating blobs, and going through forest dimensions."
    pause 1.0
    billy "No offense."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    gnome "G'none taken."
    aria "A little bit taken, but I also brought up your cocaine overdose immediately after first meeting you, so fair play, honestly."
    aria "Y'all are headed to New York, then?"
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    cs "Yeah, I'm just trying to get home, and these two kinda got dragged along."
    scene cafe_sitting
    show aria flipped at left
    show gnome at center
    aria "Would you like to come rest at my apartment for a while? I have enough space for you all to get some sleep."
    aria "I also have a really pretty wooded area behind my apartment I can take you through."
    aria "You've all been through a lot. It'd be a good way to relax before you finish the drive."
    scene cafe_sitting_2
    show cs at left
    show billy at center
    show arceus at right
    arceus "That'd be great. It'd be nice to relax for a while."
    billy "I'd be happy to be off the road for a while longer. I miss when I didn't have to drive, and instead shouted all day."
    cs "Same here. And yeah, sure, we'll go check out the forest after we eat."
    show waitress at mid_right with moveinright
    waitress "Here's everyone's food. Enjoy your meal!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "They all eat and then leave the restaurant. The gnome goes back to his forest, and the others head to Aria's apartment for a rest."
    scene aria_apartment_outside
    show billy car
    with dissolve
    aria "You can park here next to the building."
    billy "Alright. I know it's early, but I'm ready to just chill for a bit."
    arceus "Yeah, that sounds good."
    aria "Sounds like a plan. Come up to my room for a bit and we can hang out."
    scene black with dissolve
    n "Aria goes to her room as everyone relaxes."
    n "Once it hits midnight, Aria decides to take them all out to the forest."
    scene path_entrance
    show cs disappointed dark flipped at mid_right
    show arceus worried dark at right
    show billy dark at center
    show aria dark flipped at left
    with dissolve
    play music dense_woods_b volume 0.5 if_changed
    music dense_woods_b
    if fun_value(FUN_VALUE_MUSIC):
        cs "Wouldn't you say these are some Dense Woods, Billy?"
    else:
        billy "Why does the window by the entrance have to be bright red?"
    billy "I've had enough of spooky forests today. They wear me out!"
    aria "It's fine. That guy always has his lights set to red."
    aria "It's admittedly a little creepy, but you get used to it."
    cs "That's probably the least concerning thing we've seen in a forest so far today, to be fair."
    arceus "Still seems plenty murderous to me."
    aria "I'm out here most nights, and he hasn't murdered me yet, so I wouldn't worry too much."
    arceus "Yet."
    scene forest_bridge
    show cs dark flipped at mid_right
    show arceus dark at right
    show billy dark at left
    show aria dark flipped at center
    with dissolve
    aria "We're gonna take a left at the bridge up ahead. The forward path just spits us right out onto a normal street."
    billy "We've been out here for all of five minutes and that's already seeming like the better option!"
    aria "Nah, trust me. This path has all the best plants and the only real path through the forest."
    aria "White banesberry, hawthorn, sugar maple."
    aria "It's really pretty."
    show cs disappointed dark flipped behind arceus
    cs "What do you mean by \"the only real path\"? Aren't we currently walking through a forest?"
    aria "This isn't a forest, this is just a concrete path with trees on the sides."
    aria "Once you're actually in the woods, you're surrounded by plants of all kinds."
    aria "The smallest of them just springing up from the ground."
    aria "The tallest spreading their roots and taking command of the very earth we all draw our energy from."
    show arceus worried dark
    arceus "You're not helping this seem any more normal..."
    aria "What do you mean? It's perfectly natural."
    scene creepy_path
    show cs worried dark flipped at mid_right
    show arceus worried dark at right
    show billy dark at left
    show aria dark flipped at center
    with dissolve
    aria "Anyway, the forest path is right up there."
    billy "Are you kidding? This path is dark enough. That one is a path of nothing!."
    cs "Yeah, I don't know about that."
    aria "It's fine, it's my typical path."
    aria "We have flashlights, and honestly, the moonlight is usually enough for me once I get in there."
    billy "You're also a floating pile of OxyClean! We have a different scale."
    aria "I guess you're welcome to just head back out on the road."
    aria "Just watch out for fae paths on the way back."
    billy "What the actual fuck is a fae path?"
    aria "Oh, they're paths that look like a normal path for the first little while, but end up placing you in the center of the woods."
    aria "The sense of linear direction decays as the path becomes less clear, and you eventually can't tell what direction you came from."
    billy "And you didn't think it was relevant to mention this before?"
    aria "Well, no, you have a guide. I was planning on making this a relaxing walk, so I didn't plan on taking the fae paths."
    billy "Why would you ever?!"
    aria "Well, they put you into some pretty parts of the woods."
    billy "Your obsession with these woods is not healthy. Maybe you should pitch some products, like me, Billy Mays!"
    aria "Maybe some time. If I decide to, i'll give you call."
    show cs disappointed dark flipped behind arceus
    aria "Anyway, this path loops around to where we came from, so if you wanna leave, it's the fastest way back at this point."
    billy "So, no matter which way I take, I'm at risk of ending up in a cursed path to the middle of a haunted forest?"
    aria "I wouldn't say cursed or haunted, but I would advise staying with me."
    aria "Any unfamiliar woods comes with a chance of getting lost, and I imagine you all don't want that."
    billy "Why would anyone?!"
    aria "To each their own, I suppose."
    billy "What do you all think?"
    show cs dark flipped behind arceus
    cs "I've not had any reason to distrust Aria before, and having someone who knows the woods has to be good."
    show arceus dark
    arceus "Yeah, these woods are gonna be creepy no matter what route we take. We may as well pick the fastest one."
    aria "Alrighty then, follow me everyone."
    scene creepy_path_2 with dissolve
    n "As the group enters the path, a ray of moonlight shines through a gap in the canopy."
    n "Rustling noises can be heard further into the woods, but the path through the trees is clear, albeit dimly lit."
    stop music fadeout 3.0
    music end
    scene creepy_path_4 with dissolve
    play music melancholy if_changed
    music melancholy
    if fun_value(FUN_VALUE_MUSIC):
        aria "If you look to the right, you'll see one of my favorite, melancholy, paths in the woods."
    else:
        aria "If you look to the right, you'll see one of my favorite paths in the woods."
    aria "It's not exactly clear, so we'll skip it today, but it leads to a pretty little grotto."
    aria "It feels like something out of a fairy tale."
    cs "This whole forest does, but only the uncensored Brothers Grimm versions."
    aria "Yeah, it really feels like an authentic fairy tale experience c:"
    cs "That's not a good thing..."
    scene doll_eye_tree
    n "Aria stopped listening because it's distracted by a tree up ahead."
    if fun_value(FUN_VALUE_COMMON): 
        aria "Here's one of the white baneberries that I was talking about. They're also known as {i}Actaea Pakoopoda,{/i} or Doll's Eyes."
    else:
        aria "Here's one of the white baneberries that I was talking about. They're also known as {i}Actaea Pachypoda,{/i} or Doll's Eyes."
    arceus "I can see where they got the name!"
    aria "It does have thick stalks that fit the pachypoda name."
    arceus "Not the altiora poke-and-prod-er or whatever, the fucking doll's eyes!"
    arceus "That tree is watching us."
    aria "I like to think that Mother Nature watc--{w=2.0}{nw}"
    $ renpy.music.set_pause(True, "music")
    play music2 sfx_ringtone_cs loop volume 3 
    $ persistent.heard.add("sfx_ringtone_cs")
    n "All of a sudden, CS' phone starts going off."
    cs "Oh shit, sorry. I forgot I left my ringer on."
    aria "Well, can you turn it off? You're interrupting my friend's song!"
    cs "What? The fuck you mean your friend's song?"
    aria "Just, figure it out man, it's ruining the forest mood."
    cs "Alright, hold on."
    stop music2
    $ renpy.music.set_pause(False, "music")
    n "CS picks up the phone, and what sounds like a telemarketer starts shouting."
    pencil "Come on down to PencilCon! The best pencil-themed convention only in Pennsylvania! Tickets still available at the door!"
    pencil "Don't miss it! Starts tomorrow evening! Would you like to order tickets?"
    cs "What the hell? Who is this?! I should kick your fucking ass!"
    pencil "It's, for, PencilCon?"
    cs "I'm out in this creepy ass forest, and it's the middle of the night! You scared the shit out of me!"
    pencil "Okay, I'm sorry sir, it's just that--{w=2.0}{nw}"
    cs "It's what?"
    pencil "Wait, haven't I met you before?"
    aria "Are you almost done yet?"
    cs "I need to go, sorry. Cya!"
    cs "Sorry about that. I don't know who the hell that was."
    arceus "Well, I want to say that at least distracted me from the creepy forest a bit."
    aria "Well, I guess if it makes you feel better, that matters more."
    aria "C'mon, we'll be out of here soon. I have one more area to show you guys, and then we can go back."
    arceus "Thanks."
    scene creepy_path_fairy with dissolve
    cs "I didn't mean to change paths, I just meant to go down it faster--{w=0.5} wait, what's that glowing thing up ahead?"
    aria "Oh, that's strange, They don't normally appear on this path..."
    aria "That's one of the Faeries."
    aria "I've seen one like that before, with the glowing white body and warm yellow-colored edges."
    aria "I haven't seen that many Faeries, but I've kept track as I encounter new varieties."
    aria "I call this kind Seraphites."
    aria "They have particularly warm energy and have a brighter glow, as well as higher pitched resonance."
    cs "Resonance?"
    aria "The tone They produce as They float around."
    aria "It's similar to a CRT whine, so it might be too high-pitched for you to be able to hear it."
    arceus "I can hear CRTs, but I don't hear that..."
    billy "What are you talking about? That's so loud, how can you not hear it?"
    cs "Wait, Billy and Aria are the only two that can hear it?!"
    cs "The Fae must have something to do with the weird forest obsession."
    cs "We need to get Billy out of here, ASAP."
    arceus "We can't go forward with it up ahead!"
    aria "You can just walk past It. Faeries are mischievous, but They aren't malevolent."
    arceus "Maybe not to {i}you!{/i} You're also a glowing blob!"
    aria "I wasn't always, and They left me alone then, too."
    cs "I don't know if I want to try and go back if we've encountered the Fae that make the trick paths..."
    cs "I guess we don't have any other options."
    show creepy_path_3 with dissolve
    n "They all slip past the Seraphite, and It floats off between the trees."
    n "They walk further along the path, which becomes less clear as tree branches block their way."
    aria "Huh, these aren't normally here..."
    arceus "What do you mean \"not normally here\"?! Is this path changing?!"
    cs "What the hell? How are we getting out of here?!"
    billy "I guess we've gotta just go through."
    arceus "Go through where?! These branches are about as thick as the trees on the side!"
    billy "We go down the same way we've been going."
    billy "What's your issue? You're short enough that you don't even need to crouch to get under the branches."
    arceus "Fuck off."
    arceus "I guess you're right, though. We can't really turn back now."
    n "Everyone begins making their way through the nest of tree branches."
    n "Eventually, they reach the end and the canopy begins to thin out as they reach a path next to a road."
    show creepy_path_exit
    aria "Alright, here's the path back."
    arceus "Are you sure?! Can you guarantee me that this path is the same way it's supposed to be?!"
    aria "Yeah, that path is the same as it always is."
    billy "That path goes back the same way we came, of course it's fine."
    arceus "That was what she said about the last path and then we ended up climbing between a tangled web of branches."
    show billy at left
    show cs worried
    show arceus worried at mid_left
    show aria dark at right
    with dissolve
    arceus "That's a normal road with a sidewalk over there. We're taking that."
    cs "I'm with Arceus on this one."
    cs "I don't think I'll be able to go between two rows of trees without having a panic attack for a while."
    aria "I think Michigan roads are scarier than any forest, but I'll take you back on whichever path you want."
    $ achievement_manager.unlock("Analog Horror Protagonist")
    n "They all walk down and reach the apartment, then make their way to where the car is parked."
    scene aria_apartment_outside
    show billy at left
    show cs 
    show arceus flipped at mid_left
    show aria at right
    with dissolve
    stop music fadeout 3.0
    music end
    aria "Thanks for hanging out with me. It was fun."
    aria "Sorry you two didn't enjoy the woods, but I'm glad at least Billy seemed to like it."
    show cs disappointed
    cs "I guess nothing was actively dangerous, and that's above average for us at this point."
    show cs
    cs "Thanks for letting us rest at your place."
    aria "Anytime."
    aria "Billy, it was nice meeting you. You're welcome to come back and visit the woods again."
    billy "It was nice meeting you too. I'll definitely come back next time I'm in Michigan."
    aria "CS, it was also nice seeing you again." 
    aria "And, Arceus, it was nice finally meeting you in person."
    arceus "You, as well, until we went to the woods."
    aria "Yeah, sorry about that..."
    billy "You're fine. It was nice then, too. He's just got a bit of a skill issue, I think."
    arceus "Whatever, man..."
    aria "Bye-bye, y'all! Good luck on your adventure!"
    scene black with dissolve
    jump true_ohio

label michigan_interstate_94:
    scene car plains
    show billy car
    stop music fadeout 3.0
    $ clown = True
    cs "What are you talking about? We're getting on 94."
    cs "We've all been through way too much for me to want to take any unnecessary detours."
    cs "I'm so tired. I just want to get home..."
    cs "I've made some pretty dumb jokes in my life, but I'm not wasting another second."
    cs "Especially not for a God damn 69 joke."
    billy "Fine, we'll take 94! All we needed was that first sentence."
    cs "Sorry, guys. I guess I'm just on-edge right now."
    arceus "{i}I{/i} thought it sounded like a good route..."
    scene black with dissolve
    n "The conversation comes to a halt as they continue heading down the highway."
    scene car plains
    show billy car
    with dissolve
    billy "Looks like there's a traffic jam up ahead. I'm gonna get off and take a detour."
    arceus "I'm gonna roll a window down now that we're off the noisy highway."
    play sound sfx_roll_window volume 0.7
    pause 1.0 
    arceus "It's crazy hot in here right now."
    cs "Huh, I didn't notice."
    arceus "I am literally always wearing a fur coat, so I guess we have different scales."
    cs "Yeah, that'll do it. You're also wearing a hoodie. You could take that off."
    arceus "If you wanna see me naked, you can just ask..."
    cs "I didn't mean-- {w=0.5}whatever..."
    show billy car turn with vpunch
    play sound sfx_splash
    show billy car turn with hpunch
    n "Soon after Arceus rolled down the window, they drive over a large flooded pothole."
    n "Water splashes up from the puddle through the car window."
    show billy car
    arceus "Oh no! My hoodie's a mess now!"
    cs "It was actively making you too hot, so now it shouldn't be a big deal, right?"
    arceus "The {i}sun{/i} was making me too hot. The hoodie was just making me too comfy!"
    arceus "We're already on a detour. We can just stop at the next laundromat we see and wash it."
    pause 5.0
    n "They continue down the road until Arceus spots a laundromat."
    scene mario_outside
    show billy car
    with dissolve
    arceus "Alright, there's one! Mario's Coin Laundry!"
    arceus "Billy! Pull over!"
    billy "Sure, I guess. I don't know if I'll be around much longer if I say no..."
    scene black with dissolve
    n "Billy parks the car and they all go inside."
    scene mario_inside
    show mario at right
    with dissolve
    play music trash_zone volume 0.3 if_changed
    music trash_zone
    show cs at left
    show arceus dirty flipped at mid_left
    with moveinleft
    if fun_value(FUN_VALUE_MUSIC):
        mario "Hey, paisanos! Welcome to my Tubular Trash Zone!"
    else:
        mario "Hey, paisanos! Welcome to my laundromat!"
    show arceus dirty worried flipped
    arceus "Wait, Mario? Why are you here?"
    mario "Why are you surprised? My name's on the sign and my picture's in the window."
    show arceus dirty flipped
    arceus "Yeah, but I assumed it was just a bootleg."
    show arceus dirty worried flipped
    arceus "Aren't you meant to be saving princesses or plumbing or driving go-karts or competing in the Olympics or... whatever {i}else{/i} it is that you do?"
    arceus "When did you have time to open a laundromat?"
    mario "All that stuff doesn't pay the bills."
    arceus "I'm pretty sure being a plumber is a decent career."
    arceus "And do you how much an Olympic swimmer can make just on endorsements alone? It's nuts!"
    arceus "Also, don't you get royalties from Nintendo or something?"
    show arceus dirty flipped
    mario "Miyamoto's my creator, so he gets to choose how the royalties are dispersed."
    mario "It's like a trust fund."
    mario "He spent all my royalties on his moped, so now I'm stuck running this laundromat."
    cs "Sorry to hear that."
    arceus "Yeah, that sucks a lot."
    mario "It is what is it."
    n "Suddenly, they all hear a metal banging sound and one of the customers walks over."
    show smiley at center with moveinright
    smiley "I was just waiting on my laundry and the machine made a loud clang and stopped spinning."
    mario "Alright, I'll be right over there."
    show mario flipped with determination
    hide mario with moveoutright
    pause 1.0
    mario "No shoes in the machine! If it's broken, you're paying for the replacement!"
    n "Mario takes out the shoes and tries running the machine, but it doesn't turn back on."
    show mario at right with moveinright
    mario "There are {i}three{/i} signs that say not to put shoes in the machine, and you decide to put these big-ass clown shoes in there?!"
    mario "You really {i}are{/i} a damn clown. I'll tell you that for free."
    smiley "The shoes were dirty, and I have a show to get to."
    smiley "Speaking of, I've still gotta head over there."
    smiley "See ya!"
    hide smiley with moveoutleft
    n "Smiley runs out of the building and gets into his car."
    play sound sfx_gamer_and_girl volume 0.4
    n "A loud \"awoooooga!\" horn is heard as a colorful little clown car drives past."
    mario "Bastard. I really didn't need this today..."
    mario "Whatever, what do y'all need?"
    arceus "I just need to wash my hoodie before we get back on the road."
    mario "Alright. Detergent is over in the corner."
    n "Arceus and the others go to the back corner and wait for the hoodie to get clean."    
    n "Mario goes back to quietly sobbing in the back room."
    show mario flipped with determination
    hide mario with moveoutright
    hide cs
    hide arceus
    with moveoutright
    scene mario_inside2 with dissolve
    show cs at left
    show arceus dirty flipped at mid_left
    with moveinleft
    n "A gray blob enters the laundromat."
    show aria flipped at center with moveinleft
    show aria with determination
    aria "Wait, CS? Arceus?"
    show cs worried
    cs "Huh, who are you? {i}What{/i} are you?"
    aria "Oh, right! Yeah, it makes sense that you wouldn't recognize me. I'm Aria! Remember, we met at the mall?"
    cs "{i}You're{/i} Aria? What happened to you?"
    aria "I got different."
    show cs
    arceus "I imagine we're not getting more details than that."
    aria "Not in this game."
    arceus "Fair."
    aria "What are you guys doing here?"
    show cs disappointed
    cs "We're, uh, kinda on a road trip?"
    show arceus dirty worried flipped
    arceus "From the law."
    cs "Yeah."
    aria "That checks out."
    show cs
    arceus "Wait, what are you doing here? You clearly don't wear clothes."
    aria "You don't know what I do in my free time."
    show aria flipped
    hide aria with moveoutright
    show arceus dirty flipped
    arceus "I suppose not."
    n "Arceus goes to transfer his hoodie."
    hide arceus with moveoutright
    n "Just as Arceus moves the hoodie into the dryer, two more clowns walk in."
    scene mario_inside
    show mario at right
    with dissolve
    show shaggy_too_dope at left
    show violent_jay at mid_left
    with moveinleft
    violent_jay "We're here to see Mario."
    mario "Hey, paisanos, what can I--" 
    pause 0.5
    mario "Oh God, more clowns. This is {i}not{/i} what I needed today."
    shaggy_too_dope "We're not just any clowns, we're Juggalos."
    shaggy_too_dope "And you don't need to worry about us. We're not like Smiley."
    mario "How did you two hear about that? How do you how his name?"
    violent_jay "All clowns are connected."
    violent_jay "We might be Juggalos, but we are still clowns."
    mario "What is it you want with me?"
    shaggy_too_dope "We want to replace that washing machine."
    violent_jay "We can't let that guy give clowns a bad name."
    violent_jay "Also, we heard about your situation with Miyamoto and all. That's messed up."
    mario "Wahoo! Thank you, I don't know what to say."
    shaggy_too_dope "Don't mention it."
    mario "Wait, how do you know about the Miyamoto thing? I didn't tell Smiley about that."
    violent_jay "Clown connection again. I could detect two clowns in here."
    mario "Smiley was the only one."
    violent_jay "There were definitely two. The other is still here."
    n "They walk towards the back where CS and Arceus are, and Violent Jay points at CS."
    hide violent_jay
    hide shaggy_too_dope
    with moveoutright
    scene mario_inside2
    show cs at left
    with dissolve
    show shaggy_too_dope at mid_right
    show violent_jay at center
    with moveinright
    violent_jay "There he is!"
    cs "Who, me? Wait, are you guys Insane Clown Posse?! What do you want with me?"
    violent_jay "Chill, man. You're just the other clown we detected here."
    show cs worried
    cs "I'm not a clown..."
    shaggy_too_dope "Can't argue with the clown sense. Definitely a clown."
    violent_jay "Why is everybody so worried whenever they see us today?"
    show cs disappointed
    cs "You {i}do{/i} call yourself Violent Jay. I'd imagine you're used to it by now."
    violent_jay "That's fair."
    show mario at right with moveinright
    violent_jay "Anyway, here's the check for the washer. We've gotta head out."
    hide violent_jay
    hide shaggy_too_dope
    with moveoutleft
    $ achievement_manager.unlock("Creepy Clown Sightings")
    show billy at mid_mid_left with moveinleft
    billy "What happened there?"
    mario "I'm not sure, but they paid for the washer, so I'm not gonna think about it too hard."
    show cs disappointed
    cs "I'm not a clown. Clowns have to be good at makeup..."
    mario "I wouldn't worry about it."
    show arceus at mid_mid_right with moveinright
    show arceus flipped
    stop music fadeout 3.0
    music end
    arceus "Yeah, my hoodie's dry, so we're ready to head out. Here's the money, Mario. Good luck with business."
    show cs flipped with determination
    show arceus with determination
    hide cs
    hide arceus
    hide billy
    with moveoutleft
    n "CS, Billy, and Arceus all walk out."
    mario "That was really nice. I guess you {i}can{/i} have shit in Detroit after all."
    scene black with dissolve
    jump true_ohio
