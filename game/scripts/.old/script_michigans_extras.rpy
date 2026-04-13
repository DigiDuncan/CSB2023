# tate don't edit this label, this is old
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
    $ achievement_manager.unlock("gnomed")
    billy "Well, that was deeply disconcerting."
    gnome "If you are not used to it, I suppose so."
    billy "I think I need a break from driving after all that."
    cs "Yeah, that's fine. I was getting hungry anyway."
    cs "Hey Mx. Gnome, do you know anywhere good to eat around here?"
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

    $ translate_this_line = _("Waitress, they'll sit with me!")
    aria "{a=show:show_tl}{font=cn}老板娘！他们会跟我一起坐。{/font}{/a}"

    $ translate_this_line = _("Okay!")
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

    $ translate_this_line = _("Please give me a bowl of fish-flavored eggplant. Let me ask, if I just said some random shit, you wouldn't tell them, right?")
    aria "{a=show:show_tl}{font=cn}请给一碗鱼香茄子。请问一下，如果我说一点狗屁，你不会告诉他们，对吧？{/font}{/a}"

    $ translate_this_line = _("No, I won't.")
    waitress "{a=show:show_tl}{font=cn}对，我不会。{/font}{/a}"

    $ translate_this_line = _("Okay. Thanks. Unless they use Google Translate, they won't understand it at all.")
    aria "{a=show:show_tl}{font=cn}好啊。谢谢。除非他们使用{/font}Google Translate, {font=cn}他们完全听不懂。{/font}{/a}"

    $ translate_this_line = _("I want them to think my Chinese is better than it really is.")
    aria "{a=show:show_tl}{font=cn}我想让他们以为我的中文水平比我真的水平更好。{/font}{/a}"

    $ translate_this_line = _("My hovercraft is filled with eels.")
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
    $ achievement_manager.unlock("forest")
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