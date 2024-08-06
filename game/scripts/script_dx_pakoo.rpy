label dx_after_true:
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "This story takes place a year or so the events that took place in the True Route."
    n "CS' life went back to normal, working on YTPs and reacting to car crash videos on stream."
    n "Arceus went to England to live a happy life with Kitty..."
    if fun_value(FUN_VALUE_MUSIC):
        n "As for Billy, he's still on the road, hearing his baby: Spring Remix, and pitching his various products."
    else:
        n "As for Billy, he's still on the road, pitching his various products."
        
    show after_true_title at truecenter with dissolve
    pause 3.0
    hide after_true_title with dissolve
    pause 1.0
    
    play music letshearspring volume 2
    music "Let's Hear My Baby: Spring Remix - Pakoo"  
    scene cs_room_cars with dissolve
    show cs at left
    show billy at center
    show arceus at right
    with dissolve
    n "CS and his friends are watching car crash videos on the TV."
    show cs angry
    play sound sfx_car_horn volume 0.5
    pause 1.0
    cs "What an idiot!"
    billy "The \"don't turn on red\" sign is there for a {i}reason!"
    show cs worried
    play sound sfx_car_crash volume 0.5
    pause 2.0
    cs "Holy shit!"
    show cs
    show arceus angry
    arceus "Y'know, this is why cars have side mirrors, lady! {i}Use{/i} them!"
    show arceus
    arceus "Man, it's been a while, but I've been enjoying hanging out again."
    billy "I agree!"
    cs "Do you guys want to go out for a bit?"
    billy "Great idea! I have something to show you!"
    show arceus flipped with determination
    hide cs
    hide billy
    hide arceus
    with moveoutright
    n "The three head out to Billy's car."
    scene cs_house with dissolve
    show cs at left
    show billy at center
    show arceus flipped at right
    with moveinleft
    show arceus with determination
    billy "Alright. Do you guys trust me?"
    arceus "Yeah, I guess so?"
    billy "Do you trust me to take you somewhere while you're blindfolded?"
    show arceus worried
    arceus "Ehh..."
    cs "Arceus, look. This dude took us across the country, and more, all for $20."
    billy "$19.95!"
    show cs happy
    cs "Exactly. I trust him."
    show cs
    show arceus
    arceus "{i}Sigh..."
    arceus "Alright, I guess you have a point. Let's do this."
    billy "Great! You're gonna love it!"
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "Billy puts blindfolds on CS and Arc, then they all head out."
    if fun_value(FUN_VALUE_MUSIC):
        n "After what feels like forever, they arrive at their Echoing: Spring Remix destination."
    else:
        n "After what feels like forever, they arrive at their destination."
    play music echoing_spring volume 2
    music "Echoing: Spring Remix - Pakoo" 
    billy "Alright, you can take the blindfolds off."
    scene wis_forest 
    show cs dark at left
    show arceus dark flipped at center
    show billy dark at right
    with dissolve
    pause 0.5
    show arceus worried dark flipped
    arceus "Wha-- where are we? How long has it been?"
    billy "We're finally far enough. I just wanted to do this somewhere secluded. "
    n "Arceus looks nervous."
    #show mika horny lightner horizontal
    show arceus dark flipped
    cs "So, where's this surprise?"
    billy "It's in my trunk. That's why I blindfolded you."
    billy "You guys will have to help, though. It's kinda big."
    show cs dark flipped
    show arceus dark
    with determination
    hide cs
    hide arceus
    with moveoutleft
    arceus "Jesus, what {i}is{/i} this thing?"
    cs "Okay, you grab the right, and I'll grab the left."
    arceus "Fuck, this is heavy as hell!"
    billy "Alright, bring it over here!"
    window hide
    show cs concentrate dark at mid_mid_right
    show pot_lift at mid_right
    show arceus angry dark at mid_right_right
    with moveinleft
    pause 0.5
    hide pot_lift
    show pot_sunken at mid_right
    play sound sfx_bucket volume 0.9
    pause 1.0
    show billy dark at left with move
    show cs dark flipped with determination
    show cs dark flipped at mid_left
    show arceus dark at mid_left_left
    with move
    show cs dark
    show arceus dark flipped
    with determination
    cs "What a workout!"
    billy "Would you guys like to guess what this is?"
    show arceus worried dark flipped
    arceus "I dunno... a giant pot?"
    show arceus dark flipped
    billy "It's a mixer containing every product I've ever sold!"
    billy "I invited you guys to see what happens when they grind together into the ultimate Billy Mays product!"
    show arceus worried dark flipped
    arceus "{i}This{/i} is what you brought us out into the middle of nowhere for?"
    show cs happy dark
    cs "This is gonna be crazy, Arceus!"
    arceus "Will it?"
    billy "Well, who wants to do the honors?"
    cs "I'll do it!"
    show arceus dark flipped    
    arceus "I'm gonna back up in case this thing explodes..."
    show cs dark at right with move
    show cs dark flipped with determination
    billy "Alright, CS! Just hit all those buttons on the side to start it up!"
    n "The machine starts whirring as a mysterious light shoots out from the top."
    hide pot_sunken
    play sound sfx_okuubeam
    show pot_beam at mid_right with hpunch
    show pot_beam at mid_right with vpunch
    show arceus worried dark flipped
    show cs worried dark flipped
    pause 1.0
    arceus "CS! Get back from there!"
    cs "Oh, God, what's happening?!"
    billy "Turn it off! Turn it off!"
    cs "I {i}can't!"
    play sound sfx_tinnitus volume 3
    scene white with dissolve
    stop music fadeout 3.0
    music end
    stop sound fadeout 5.0
    n "A flash of blinding light engulfs CS. The rest of the forest disappears from his view."
    if fun_value(FUN_VALUE_MUSIC):
        n "As CS slowly opens his eyes, he finds himself in an alien atmosphere."
    else:
        n "As CS slowly opens his eyes, he finds himself in an unforgiving place."
    scene roombacks
    show cs concentrate
    with dissolve
    play music alien_atmosphere volume 2
    music "Alien Atmosphere - Dr. Awesome"
    pause 1.5
    show cs disappointed
    pause 0.5
    show cs concentrate
    pause 0.2
    show cs disappointed
    pause 1.0
    cs "Wait, what happened?"
    cs "Oh, God, where am I?"
    show cs worried
    cs "Oh, no… It can't be..."
    show cs scared
    cs "Help! I have to be dreaming!"
    "???" "Hey! Who's up there?"
    show cs scared flipped
    cs "Help! I'm stuck in the backrooms!"
    n "The man runs up the stairs to meet the panicking CS."
    show renovator at left with moveinleft
    stop music
    music end
    renovator "What's wrong with you? How did you get back here?"
    show cs worried flipped
    cs "I've teleported into the backrooms and I think I'm stuck here forever!"
    n "The man laughs at CS."
    renovator "Well, yeah, you're in {i}my{/i} backroom, and you need to get out. The stairs are behind me."
    show cs disappointed flipped
    cs "Wh-- really?"
    #"Get out" is more aggressive than "leave quickly"
    renovator "Yes, and please get out. We are renovating this place into an RC racetrack room, and we don't need insane people ruining it."
    cs "Okay, okay. I'm sorry."
    hide cs with moveoutleft
    scene backrooms with dissolve
    show cs disappointed flipped at mid_left with moveinright
    n "As CS is leaving, he sees the sign with the date of the renovation."
    cs "\"Opening 2004\"? Is this outdated?"
    show renovator at right with moveinright
    renovator "Are you insane or high, dude? It's 2003! Are you okay?"
    play sound sfx_somethingchanged
    n "CS' heart drops."
    show cs disappointed
    cs "Yeah, I just... I'm just hungover, I guess."
    show cs disappointed flipped with determination
    hide cs with moveoutleft
    renovator "{size=-15}Fuckin' drunkards..."
    renovator "You're {i}also{/i} in Wisconsin, in case you're too drunk or high to even remember where you live!"
    scene hobbytown with dissolve
    show cs disappointed at center with moveinleft
    n "CS' head is spinning."
    cs "So, I am in Wisconsin, about 20 years in the past. What else is new?"
    cs "Apparently I ended up in the backrooms, as well?"
    show cs disappointed flipped
    cs "I wonder if Billy and Arc ended up here too..."
    show cs disappointed
    if fun_value(FUN_VALUE_EPIC):
        n "All of a sudden, a time and space portal opens and Car Guy comes out of it."
        jump dx_after_renault
    else:
        jump dx_after_back_to_story

label dx_after_back_to_story:
    stop music fadeout 1.0
    music end
    scene hobbytown
    show cs disappointed
    cs "Maybe I can find Billy's machine, if it ended up here."
    n "Before CS can get anywhere, a group of men run up to him."
    show shadowman at mid_left with moveinleft
    cs "Hey what's going--{nw}"
    play sound sfx_hitbod1
    scene black
    play sound sfx_hitbod2
    cs "Ow! HEY--{nw}"
    play sound sfx_hitbod3
    play sound sfx_hitbod1
    pause 5.0
    scene pencilroomblur with dissolve
    cs "Ohhh, my head..."
    cs "What is going on with today..."
    cs "Where am I {i}now?"
    scene pencilroom
    show cs disappointed pencil at center
    show pencilguy at left
    show pencilcashier at right
    with dissolve
    play music apple_kid
    music "Apple Kid - Keiichi Suzuki"
    cs "...and what the hell is this outfit?"
    if fun_value(FUN_VALUE_MUSIC):
        pencil "Welcome, Apple kid, to the Pencil Cult!"
        cs "That's not my name..."
    else:
        pencil "Welcome to the Pencil Cult!"
    cs "..."
    cs "Should I even ask?"
    pencil "Every year, we host PencilCon, the biggest gathering of pencil lovers worldwide!"
    pencil "But, we need to increase the number of memberships, so we grab random people and dress them up for our group!"
    pencil "We call ourselves a cult so we can win CultCon and gain massive amounts of followers!"
    cashier "Don't bother with trying to escape, either. I already tried that and they just blocked the door."
    cs "Okay, okay, slow down."
    cs "Pencil Cult? CultCon?"
    cs "Are we at... CultCon {i}right now?"
    pencil "Indeed! If we can show how massive our fanbase is by capturing people, we'll win, and then we can gain more pencil enthusiasts!"
    cs "Okay, first of all..."
    cs "Couldn't you, like, advertise a bit better than kidnapping random people to make some kind of cult?"
    pencil "That's too much work! People wouldn't even glance at our ads!"
    cs "... And, {i}kidnapping{/i} isn't too much work?"
    pencil "We've gotten really good at it!"
    cs "Why don't you just set up, like, uhh..."
    cs "A big billboard, or something like that?"
    n "The pencil man thinks for a moment."
    pencil "We'll try that next year."
    pencil "But, for now, you are now enlisted into the Pencil Cult and cannot leave until the event ends!"
    cs "Yeah, okay, but can I go to the bathroom first? I was gonna pee before you kidnapped me."
    pencil "Hey, that rhymed! Yeah, you can go."
    show cs pencil
    cs "Thank you, I'll just be a moment!"
    hide cs with moveoutright
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "CS gets to the bathroom and takes off his stuffy pencil costume."
    scene cult_con
    show cs disappointed at center
    with dissolve
    play music ten_feet_away
    music "10 Feet Away - Dr. Awesome"
    cs "God, what the fuck is all of this?"
    if fun_value(FUN_VALUE_MUSIC):
        cs "I can't tell if I'm still in the past, or 10 feet away..."
    else:
        cs "I can't tell if I'm still in the past, or what..."
    cs "I need to find a way out of here."
    n "Just as CS starts looking for an exit, a video starts playing on one of the many TVs around the convention hall."
    scene black with dissolve
    stop music fadeout 3.0
    music end
    #CultCon intro video plays
    n "A video would play here, but I didn't finish it yet."
    n "The video would sum up Cult Con, explaining that there is a side competition that takes place."
    n "The competition is where cults sign up to try to impress other cults and get votes to win a prize."
    n "The prize is Billy's machine that he made, somehow in the hands of CultCon."
    scene cult_con
    show cs 
    with dissolve
    play music ten_feet_away
    $ total_votes = 0
    cs "Well, I guess I can't leave, now!"
    cs "I need to figure out how to get Billy's machine back..."
    n "Before CS can think, a familiar voice is heard rushing over to him."
    show cs disappointed at left with move
    show csgod at right with moveinright
    csgod "Stop! Don't go anywhere yet!"
    cs "Oh, great! What's going on now?"
    csgod "This is very convenient timing, but I need you to speak to someone for me."
    csgod "There is this group of people known as the Blue Branch Cult. They are--"
    show cs
    cs "The Blue Branch Cult? Yeah, I've met them before. Remember? When Billy was taking us home?"
    csgod "Wait, you've seen them?"
    cs "Yeah, they tried to kill us! Don't you, like, watch my every move?"
    csgod "I don't remember. I was probably taking a shit."
    show cs disappointed
    cs "You... {i}do{/i} that?"
    hide csgod
    show csgod_angry at right
    csgod "Look, CS, I may be a god, but we still do a lot of the same things you mortals do."
    csgod "I don't watch over you every second. Like, I'm sorry, but that would be extremely boring."
    show cs angry
    cs "Wow, okay! I have had a pretty interesting life, at least since HoH SiS came along!"
    cs "Why can't you speak to your cult yourself?"
    csgod "Okay, let me explain this to you."
    csgod "Every time they do one of their rituals, it's like if one of your ecstatic fans called you on Discord."
    csgod "You let that shit go to voicemail, man, otherwise you're gonna get spammed until the end of time."
    cs "So, you just want a middle man to do it for you."
    csgod "Well, yeah? Kinda?"
    show cs pissed
    #The only reason I want to keep caps here, is because I had to create a new sprite to show how mad he was.
    cs "I don't know how many times you have to take a shit, or whatever, but in case you weren't watching, I AM FUCKING {i}STUCK IN THE PAST."
    hide csgod_angry
    show csgod at right
    csgod "..."
    csgod "Oh."
    csgod "..."
    csgod "So..."
    csgod "Do you think you can still talk to them for me?"
    show cs
    cs "Oh, yeah, sure. Give me one second."
    show cs flipped with determination
    hide cs with moveoutleft
    n "CS rushes off."
    csgod "Thank {i}me,{/i} I thought this was gonna be much harder."
    show cs cultist at left with moveinleft
    cs "Yeah, well, fuck that! I'm not helping you!"
    hide csgod
    show csgod_angry at right
    csgod "Hey! Take that off right now! Your {i}god{/i} demands it!"
    cs "Until you can bring me back to the future, I'm gonna go join your cult!"
    cs "And, we are winning this competition!"
    hide cs with moveoutright
    n "CS runs off to find the cultists."
    csgod "Fuck, man... I really need to get my life together."
    n "Meanwhile, The Blue Branch Cult is formulating their winning strategy."
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    with dissolve
    cultist_2 "Guys, how are we gonna win this year? CultCon is filled with {i}actual{/i} competitors!"
    cultist_3 "Yeah, usually the cults with the most followers would turn out to be human traffickers, or would torture their followers, and lose."
    cultist "If it weren't for those Scientologist pricks, we would have a bit of an upper hand."
    show cs cultist at left with moveinleft
    cs "Hey, guys! Fellow hater of everything, here!"
    cultist_3 "Is that a new follower?"
    cultist "I need to make sure. Do you think you have what it takes to be a member of Blue Branch?"
    cs "I mean, I secretly don't hate CSGod."
    cultist "Yeah, he's a real one. Let him in."
    cs "Woohoo!"
    cultist_2 "So, how did you find out about us?"
    cs "Well, I have heard about you guys from other CultCons, but I hadn't been able to travel all the way to Montana until now."
    cs "So, I figured that travelling to Wisconsin would be easier, and that this would also be my chance to get in."
    cultist "Well, we appreciate it."
    cs "You mean, you {i}hate{/i} it?"
    cultist "Exactly."
    cultist "It's a good thing you showed up. We are mainly lacking enough members to win this year."
    cultist "We need someone that can influence the other cults to put their votes in for us."
    cs "Well, I can certainly help with that. The prize this year is really something special."
    cultist_3 "Is it? It just looks like a big pot. In fact, I kinda hate it."
    cs "Oh, no. It is much more powerful than it looks."
    cultist "Well, if you can help us win, we'll let you take it. We just care about winning."
    cs "Sounds good to me."
    jump dx_after_cult_questions

label dx_after_cult_questions:
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    show cs cultist at left
    cultist "Is there anything else you would like to know about?"
    menu:
        "What else would you like to know?"
        "Tell me more about CultCon.":
            jump dx_after_cultcon_ask
        "Who are our competitors?":
            jump dx_after_competitors_ask
        "How can we win the competition?":
            jump dx_after_win_ask
        "I think I'm good.":
            jump dx_after_competiton_start

label dx_after_cultcon_ask:
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    show cs cultist at left
    cs "Tell me more about how CultCon works."
    cultist "Well, you see, CultCon is mainly just an event for cultists to meet up and share ideas, teachings, and other cult-related topics."
    cultist "The Cult Competiton is a side thing that only a few cults try to participate in."
    cultist "If they win, not only do they win the advertised prize, but they get bragging rights about how awesome their cult is, which usually grows their cult in the process."
    cultist "{i}That's{/i} what we are interested in."
    cultist "We almost won a few years back when those Heaven's Gate people voted for us, but, they just killed themselves the following year."
    jump dx_after_cult_questions

label dx_after_competitors_ask:
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    show cs cultist at left
    cs "Who are the main competitors this year?"
    cultist "Well, there are the pencil guys who usually end up in dead last, so they give their vote to us most of the time."
    cultist "Our main opponent is the Scientologists, because they have so many numbers, and aren't {i}completely{/i} psycho."
    # this next line is... difficult to reword. i need context - tate
    cultist "We had the Branch Davidians here that one year, and, lemme just tell you... Yikes, those guys are fucking oblivious to anything their leader says."
    cultist "Anyway, yeah, they mainly have an advantage because they got that guy from Top Gun in their ranks now."
    cs "Tom Cruise?"
    cultist "Yeah, fuck that guy. If there is {i}one{/i} thing that I hate more than everything else, it's gotta be him."
    cultist "I don't think the rest of the groups are as bad as them, so I believe you'll have an easy time winning them over."
    jump dx_after_cult_questions

label dx_after_win_ask:
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    show cs cultist at left
    cs "So, how do we win the competition?"
    cultist "Well, all of the cults have a certain number of votes they can give out to other cults that they are impressed by."
    cultist "The bigger the cult, the more votes you can hand out."
    cultist "That {i}also{/i} means that, the bigger you are, the more likely that the other votes will usually go to you."
    cultist "It {i}is{/i} possible for a small cult like us to win. We just have to put in more work to be influential."
    cultist "Which is what you'll be doing."
    cs "Ah, I got it."
    jump dx_after_cult_questions

label dx_after_competiton_start:
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    show cs cultist at left
    cs "I think I'm good."
    cultist "Alright, awesome."
    if con_start:
        jump menu_branch_ask
    stop music fadeout 3.0
    music end
    cultist "Now go out there and--{nw}"
    play music hitsquad_2
    music "Hitsquad 2 - Dr. Awesome"
    if fun_value(FUN_VALUE_MUSIC):
        cruise "Hey you hit squad, 2, idiots!"
        cs "Yeah, you tried."
    else:
        cruise "Hey you purple-hooded idiots!"
    show cruise flipped at center with moveinleft
    show cs angry cultist
    cultist_2 "Yeah, what do {i}you{/i} want?"
    cultist_3 "Get out of here, you alien-worshipping asshole!"
    cruise "Oh, I just wanted to see how well you guys were {i}losing{/i} this year!"
    show cruise 
    cruise "I'll bet your god is fake, just like everyone else's!"
    cultist "Alright, you prick, get the hell out of here!"
    show cruise flipped
    cruise "Or, {i}what?{/i} If you attack me, you'll get kicked out!"
    cruise "I've been working on opening up past my human form. Once I achieve this, I'll be unstoppable."
    cruise "Then, this convention will have something {i}real{/i} to show off for once!"
    cruise "See y'all later!"
    show cruise with determination
    hide cruise with moveoutleft
    stop music fadeout 3.0
    music end
    show cs cultist
    cultist "Eugh, fuck that guy."
    cultist "Anyways, I wish you the best of luck."
    cs "Don't worry. We'll show him who's boss by the end of this."
    cultist "I hope so."
    n "CS runs off to find competitors."
    scene cult_con with dissolve
    play music ten_feet_away
    show cs cultist at center with moveinleft
    $ con_start = True
    cs "Alright, so, there are a few cults I can challenge here."
    jump dx_after_seek_competitors
    
label dx_after_seek_competitors:
    play music ten_feet_away if_changed
    scene cult_con
    show cs cultist at center
    cs "Which cult should I look for?"
    menu:
        "Pick a cult:"
        "Scientology":
            jump dx_after_science_ask
        "Pencil Cult":
            jump dx_after_pencil_ask
        "Catholicism":
            jump dx_after_catholic_ask
        "Lunatic Cultists":
            jump dx_after_lunatic_ask
        "Society of the Blind Eye":
            jump dx_after_blindeye_ask
        "Check votes/balance":
            jump dx_after_votes_balance
        "Back to Blue Branch":
            jump dx_after_branch_ask

label dx_after_votes_balance:
    cs "Ah, let's see here..."
    n "Total votes: [total_votes]"
    n "Current balance: $[cath_counter]"
    jump dx_after_seek_competitors

label dx_after_pencil_ask:
    play music ten_feet_away if_changed    
    scene cult_con
    show cs cultist at center
    if pencil_check and god_money:
        cs "Maybe I should go see if they have any extra spare change."
        scene pencilroom 
        show pencilguy at right
        with dissolve
        show cs cultist at left with moveinleft
        pencil "Hey hey hey! Were you looking to {i}sharpen{/i} your skills again?"
        
        menu:
            "Choose what you want to do:"
            "Ask for money":
                if check2:
                    cs "Do you have any spare change I can have?"
                    pencil "Dude, you already asked for some money! I'm not rich!"
                    pencil "I already spent it all on this pencil gig!"
                    cs "Oops. Sorry, I'll just go back."
                    show cs cultist flipped with determination
                    hide cs with moveoutleft
                    scene cult_con with dissolve
                    play music ten_feet_away if_changed
                    show cs cultist at center with moveinleft
                    jump dx_after_seek_competitors
                cs "Do you have any spare change I can have?"
                pencil "What? I mean, I guess you did beat my score..."
                n "The pencil man takes out some bills and hands them to CS."
                n "It looks to be an assortment of ones and fives."
                $ cath_counter += 13
                n "Current balance: $[cath_counter]."
                cs "Thank you! Your contributions are appreciated."
                pencil "... You're welcome?"
                n "CS goes back to the convention floor."
                show cs cultist flipped with determination
                hide cs with moveoutleft
                $ check2 = True
                scene cult_con with dissolve
                play music ten_feet_away if_changed
                show cs cultist at center with moveinleft
                jump dx_after_seek_competitors
            "Redo pencil game":
                cs "I would indeed, like to {i}sharpen{/i} my skills."
                pencil "Alright! You must have a strong arm to do this again! What have you been doing to be strong in just your arm?"
                pause 1.0
                pencil "I just thought about it, don't tell me."
                n "The pencil man pulls out the sharpener and some more pencils."
                pencil "Ready, and, go!"
                minigame "play_pencil2_game" "dx_after_win_pencil2" "lose_pencil_game2"
    elif pencil_check:
        cs "Maybe I can try to beat my previous score."
        scene pencilroom 
        show pencilguy at right
        with dissolve
        show cs cultist at left with moveinleft
        pencil "Hey hey hey! Were you looking to {i}sharpen{/i} your skills again?"
        menu:
            "Choose what you want to do:"
            "Redo pencil game":
                cs "I would indeed, like to {i}sharpen{/i} my skills."
                pencil "Alright! You must have a strong arm to do this again! What have you been doing to be strong in just your arm?"
                pause 1.0
                pencil "I just thought about it, don't tell me."
                n "The pencil man pulls out the sharpener and some more pencils."
                pencil "Ready, and, go!"
                minigame "play_pencil2_game" "dx_after_win_pencil2" "lose_pencil_game2"
            "Go back":
                cs "Sorry, I think I just got lost."
                pencil "Yeah, it happens to me everytime."
                show cs cultist flipped with determination
                hide cs with moveoutleft
                scene cult_con with dissolve
                play music ten_feet_away if_changed
                show cs cultist at center with moveinleft
                jump dx_after_seek_competitors
    cs "The cult leader said that the pencil guys usually give us a vote, so let's go see what they are up to."
    hide cs with moveoutright
    n "CS makes his way to the pencil room."
    scene pencilroom 
    show pencilguy at right
    with dissolve
    show cs cultist at left with moveinleft
    n "When he gets there, the leader immediately recognizes him."
    pencil "Hey! You ran away from our group!"
    pencil "You teamed up with Blue Branch? Hah! Well, this year, we don't care anymore!"
    show cs disappointed cultist
    cs "What makes you say that?"
    pencil "The cult idea wasn't really working out, so we are switching to a more casual approach to lure fans!"
    cs "... Like I suggested?"
    pencil "It's officially {i}our{/i} idea now!"
    pencil "Look, if you want to win our vote, you've gotta earn it!"
    pencil "Behold!"
    show onscreen_sharpener at mid_right_right with dissolve
    n "The pencil man pulls out a pencil sharpener."
    show cs cultist
    cs "Lemme guess, a pencil sharpening contest?"
    pencil "How'd you know?"
    cs "Oh, just a hunch, that's all."
    stop music fadeout 3.0
    music end
    hide onscreen_sharpener with dissolve
    n "The pencil man places the sharpener onto the table next to them, and then pulls out a pack of 60 pencils."
    pencil "You better hope you have some godlike endurance. You've got four minutes."
    pencil "If you can beat my score, we'll give you our vote!"
    cs "Oh, I'll win."
    pencil "Well, aren't you cocky? Let's see this, then!"
    pencil "3, 2, 1,"
    pencil "Go!"
    minigame "play_pencil2_game" "dx_after_win_pencil2" "lose_pencil_game2"

    label dx_after_win_pencil2:
    hide bad_end_screen
    hide typewriter
    stop music fadeout 3.0
    music end   
    show pencilroom
    show pencilguy at right
    show cs cultist at left
    with dissolve
    if god_money and check2:
        pencil "Geez, you did it again."
        show cs cultist flipped with determination
        hide cs with moveoutleft
        n "CS turns around and leaves, offering no further explanation."
        scene cult_con with dissolve
        play music ten_feet_away if_changed
        show cs cultist at center with moveinleft
        jump dx_after_seek_competitors 
    elif god_money and pencil_check:
        pencil "Geez, you did it again."
        cs "Also, do you have any spare change I can have?"
        pencil "What? I mean, I guess you did beat my score..."
        n "The pencil man takes out some bills and hands them to CS."
        $ cath_counter += 13
        n "Current balance: $[cath_counter]."
        n "It looks to be an assortment of ones and fives."
        cs "Thank you! Your contributions are appreciated."
        pencil "... You're welcome?"
        $ check2 = True   
        show cs cultist flipped with determination
        hide cs with moveoutleft
        n "CS turns around and leaves, offering no further explanation."
        $ pencil_check = True
        scene cult_con with dissolve
        play music ten_feet_away if_changed
        show cs cultist at center with moveinleft
        jump dx_after_seek_competitors 
    $ pencil_votes = 0
    $ pencil_votes += 3
    $ total_votes += pencil_votes
    pencil "Woah, where'd {i}that{/i} kinda skill come from?!"
    pencil "You're a pencil sharpening {i}legend!"
    cs "I'll just say one thing:"
    cs "October 27th. Remember that day."
    pencil "Uhh, alright?"    
    if god_money:
        cs "Also, do you have any spare change I can have?"
        pencil "What? I mean, I guess you did beat my score..."
        n "The pencil man takes out some bills and hands them to CS."
        $ cath_counter += 13
        n "Current balance: $[cath_counter]."
        n "It looks to be an assortment of ones and fives."
        cs "Thank you! Your contributions are appreciated."
        pencil "... You're welcome?"
        $ check2 = True
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS turns around and leaves, offering no further explanation."
    $ pencil_check = True
    scene cult_con with dissolve
    play music ten_feet_away if_changed
    show cs cultist at center with moveinleft
    cs "Well, that takes me back."
    cs "Or, I guess, that takes me {i}forward!"
    show cs disappointed cultist
    cs "Fuck, I need to get back home..."
    show cs cultist
    cs "Alright, well..."
    jump dx_after_seek_competitors

label dx_after_science_ask:
    play music ten_feet_away if_changed    
    scene cult_con
    show cs cultist at center
    if science_check and god_money:
        cs "I could try asking them for money, it's worth a shot."
        hide cs with moveoutright
        n "CS runs over to Scientology stand."
        show cs cultist at left with moveinleft
        show cruise flipped at mid_right
        show cruise with determination
        cruise "Hey, welcome back! Want to give up already?"
        show cs cultist
        cs "I was going to ask, you have any spare change?"
        if science_check2:
            cruise "I already gave you a bit of money!"
            cruise "I don't carry around a million dollars with me everywhere I go!"
            cs "Sorry, sorry. I didn't mean to ask you again."
            cruise "Just get out of here! You better not disappoint me tonight!"
            show cs cultist flipped with determination
            hide cs with moveoutleft
            n "CS heads back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft 
            jump dx_after_seek_competitors
        cruise "Why the hell would I give any money to you?"
        cruise "You are, like, part of that fuckin' group that I hate!"
        show cs disappointed cultist        
        cs "I dunno, it was worth a try."
        show cs disappointed cultist flipped
        n "CS heads back to the convention floor."
        show cs disappointed cultist flipped at offscreenleft with move
        cruise "Wait! Are you just gonna walk away?!"
        show cs disappointed cultist with determination
        cs "Well, I mean, you already say no."
        show cruise flipped
        cruise "Okay, fuck... Just give me a moment."
        show cs cultist at center with move
        show cruise
        n "Mr.{w=0} Cruise pulls out a few tens and hands them to CS."
        $ cath_counter += 30
        n "Current balance: $[cath_counter]."
        cruise "I'm not just gonna let you win that easily. If you lose, now I can {i}really{/i} laugh at you!"
        cs "Thanks! Your donation will be incredibly useful!"
        cruise "Yeah, yeah, whatever."
        $ science_check2 = True
        show cs cultist flipped with determination
        hide cs with moveoutleft
        n "CS heads back to the convention floor."
        scene cult_con with dissolve
        show cs cultist at center with moveinleft
        cs "Well, that was a lot easier than I thought."        
        jump dx_after_seek_competitors

    if science_check:
        cs "I guess I could see if Tom Cruise has anything else to say."
        hide cs with moveoutright
        n "CS runs over to Scientology stand."
        show cs cultist at left with moveinleft
        show cruise flipped at mid_right
        cs "Hey! I'm back!"
        show cruise
        cruise "What do you want?"
        cs "I was just gonna ask..."
        cs "Can I have like, one more vote?"
        cruise "What the fuck? No!"
        cs "Pleeeease??"
        cruise "Just for that, I'm gonna give you a tenth of a vote."
        $ science_votes = 0
        $ science_votes += 0.1
        $ total_votes += science_votes
        cs "Fine, I'm just getting bored of this."
        show cs cultist flipped with determination
        hide cs with moveoutleft
        n "CS heads back to the convention floor."
        scene cult_con with dissolve
        show cs cultist at center with moveinleft       
        jump dx_after_seek_competitors
    cs "Y'know, the Scientologists think they are all that, but maybe if I talk to them, I can convince them to vote for us."
    hide cs with moveoutright
    n "CS runs over to Scientology stand."
    show cs cultist at left with moveinleft
    show cruise flipped at mid_right
    n "When he gets there, he sees Tom Cruise standing nearby, greeting other cult members walking by."
    cruise "Yeah, and make sure to watch my movies, too!"
    cs "Hey, guy! CS here!"
    show cruise
    cruise "Hey, you're that new guy!"
    cruise "Why the hell did you pick {i}those{/i} guys, anyway? They always lose!"
    show cs disappointed cultist
    cs "Well, it's funny that you said this convention never can show off any {i}real{/i} power."
    cs "I think I've got something up my sleeve that'll meet your definition."
    cruise "Hah! They all say that, bud. What makes you so special?"
    cs "If you put a vote in for us, and we win, I'll show you all."
    cs "If I can't, the Blue Branch won't show up for another Cult Con."
    cruise "A bet? Sure, I'm down, but you'd better not disappoint me!"
    show cs angry cultist
    cs "I won't, man, don't worry."
    $ science_votes = 0
    $ science_votes += 37
    $ total_votes += science_votes
    if god_money:
        show cs cultist
        cs "By the way, do you have any spare change?"
        cruise "Why the hell would I give any money to you?"
        cruise "You are, like, part of that fuckin' group that I hate!"
        show cs disappointed cultist        
        cs "I dunno, it was worth a try."
        show cs disappointed cultist flipped
        n "CS heads back to the convention floor."
        show cs disappointed cultist flipped at offscreenleft with move
        cruise "Wait! Are you just gonna walk away?!"
        show cs disappointed cultist with determination
        cs "Well, I mean, you already say no."
        show cruise flipped
        cruise "Okay, fuck... Just give me a moment."
        show cs cultist at center with move
        show cruise
        n "Mr.{w=0} Cruise pulls out a few tens and hands them to CS."
        $ cath_counter += 30
        n "Current balance: $[cath_counter]."
        cruise "I'm not just gonna let you win that easily. If you lose, now I can {i}really{/i} laugh at you!"
        cs "Thanks! Your donation will be incredibly useful!"
        cruise "Yeah, yeah, whatever."
        $ science_check2 = True
    $ science_check = True
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS heads back to the convention floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Well, that was a lot easier than I thought."
    jump dx_after_seek_competitors

label dx_after_catholic_ask:
    play music ten_feet_away if_changed
    scene cult_con
    show cs cultist at center
    if god_money:
        hide cs with moveoutright
        n "CS goes to check out the Catholics."
        show priest at mid_right
        show cs cultist at left with moveinleft
        if cath_check2:
            priest "You have already donated. Thank you for your contribution!"
            cs "Oh yeah, I already did that."
            cs "Welp, back to the floor."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            pause 1.0
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            jump dx_after_seek_competitors           
        priest "Hello, do you have anything to donate yet?"
        menu:
            "Donate money":
                jump dx_after_catholic_tally
            "Keep looking for money":
                cs "I think I'm gonna find a bit more."
                priest "The more, the merrier!"
                show cs cultist flipped with determination
                hide cs with moveoutleft
                n "CS heads back to the convention floor."
                scene cult_con with dissolve
                show cs cultist at center with moveinleft
                jump dx_after_seek_competitors              
    if cath_check:
        cs "Ugh, alright, let's see what those Christians have to offer."
        hide cs with moveoutright
        n "CS goes to check out the Catholics."
        show priest at mid_right
        show cs cultist at left with moveinleft
        priest "I thought I told you to leave!"
        cs "Look, I'm sorry, I'm just a bit stressed actually because a lot has happened today..."
        cs "...and I kinda need to win this prize."
        priest "Well, if you are willing, I can accept cash, and possibly change my mind on our voting offer!"
        priest "Maybe you will want to reconsider my original offer?"
        cs "I don't know about becoming Catholic, but I can find some money."
        jump dx_after_catholic_find
    cs "Who the hell are those guys?"
    cs "They just look like Christians!"
    hide cs with moveoutright
    n "CS goes to check out the Catholics."
    show priest at mid_right
    show cs cultist at left with moveinleft
    n "As CS approaches the priest, he immediately greets him."
    priest "Hello! Would you like to donate to the church?"
    menu:
        "Find money to donate":
            jump dx_after_catholic_find
        "Ask for vote regardless":
            cs "No thanks, I don't have money on me."
    cs "Would you like to vote for Blue Branch?"
    priest "Oh, sorry, we don't hand out votes to anyone."
    priest "We just want to see if any cult is willing to..."
    priest "... upgrade?"
    cs "Have you gotten anyone to bite?"
    priest "Not yet, but I'm sure someone will realize--{nw}"
    show cs disappointed cultist
    cs "Dude, I'm sorry, but I don't think this is gonna work out for you guys."
    priest "Just get out of here. You'll ruin my image."
    show cs cultist
    cs "Alright, cya!"
    $ cath_check = True
    n "CS heads back to the convention floor."
    show cs cultist flipped with determination
    hide cs with moveoutleft
    pause 0.5
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Well, that was a load of crap!"
    jump dx_after_seek_competitors

label dx_after_catholic_find:
    $ god_money = True
    $ cath_counter = 0
    cs "Stay right here. I'm sure I can find some money."
    priest "I wasn't planning on moving, but thank you! The church will thank you."
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS runs back to the main floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "So, what I'm thinking is, if I give those guys some money, they'll be sure to give us votes!"
    cs "I mean, the Catholic church must have a {i}lot{/i} of votes to give out, right?"
    cs "Well, I need to figure out who to ask..."
    jump dx_after_seek_competitors

label dx_after_catholic_tally:
    play music ten_feet_away if_changed    
    scene cult_con
    show priest at mid_right
    show cs cultist at left
    n "Are you sure? Once you donate, you cannot come back to give more money!"
    menu:
        "Keep looking for money":
            cs "I think I'm gonna find a bit more."
            priest "The more, the merrier!"
            n "CS heads back to the convention floor."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            pause 0.5
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            jump dx_after_seek_competitors 
        "Yes, donate":
            $ cath_votes = 0
    cs "I think I'm ready to donate my money."
    priest "Alrighty! Let's see what you got!"
    priest "It looks like you got:"
    priest "$[cath_counter]!"
    priest "With this much, I think we can give you..."
    if 0 <= cath_counter < 10:
        priest "5 votes."
        $ cath_votes += 5
    elif 10 <= cath_counter < 25:
        priest "10 votes."
        $ cath_votes += 10
    elif 25 <= cath_counter < 50:
        priest "20 votes."
        $ cath_votes += 20
    elif 50 <= cath_counter < 100:
        priest "30 votes."
        $ cath_votes += 30
    elif 100 <= cath_counter < 125:
        priest "35 votes."
        $ cath_votes += 35
    elif 125 <= cath_counter < 150:
        priest "40 votes."
        $ cath_votes += 40
    elif 150 <= cath_counter:
        priest "50 votes."
        $ cath_votes += 50
    cs "Awesome sauce."
    $ cath_check2 = True
    $ cath_counter = 0
    $ total_votes += cath_votes
    show cs cultist flipped with determination
    hide cs with moveoutleft
    pause 0.5
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    jump dx_after_seek_competitors

label dx_after_lunatic_ask:
    play music ten_feet_away if_changed    
    scene cult_con
    show cs cultist at center
    if lunatic_check3 and god_money:
        cs "I think I cheated here on this one, I have no reason to go back."
        show lunatic_cultist at mid_right with moveinright
        l_cultist "Hold up! I forgot to give you this!"
        $ cath_counter += 10000
        n "Current balance: $[cath_counter]."
        cs "Woohoo!"
        hide lunatic_cultist with moveoutleft
        jump dx_after_seek_competitors
    if lunatic_check3:
        cs "I think I cheated here on this one, I have no reason to go back."
        jump dx_after_seek_competitors
    if lunatic_check and god_money:
        cs "Well, did look pretty fancy for a cult, maybe they have some spare change to hand out?"
        hide cs with moveoutright
        n "CS runs over to meet the Lunatic Cultists."
        scene cult_zone1
        show lunatic_cultist at mid_right
        with dissolve
        show cs cultist at mid_left with moveinleft
        l_cultist "Welcome back."
        l_cultist "Was there anything you needed?"
        cs "Did you have any spare change you could give me?"
        if lunatic_check2:
            l_cultist "Sorry, we don't have much else we would want to give away right now."
            cs "Ah, it's okay."
            cs "Worth a try."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            n "CS heads back to the floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            jump dx_after_seek_competitors
        if lunatic_votes == 0:
            l_cultist "I guess we have a bit…"
            n "They hand CS a copper coin."
            cs "Thanks."
            $ cath_counter += 0.01
            n "Current balance: $[cath_counter]."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            n "CS sulks back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            $ lunatic_check2 = True 
            jump dx_after_seek_competitors 
        elif lunatic_votes == 3 or lunatic_votes == 4:
            l_cultist "Here, we have something..."
            n "They hand CS a silver coin."
            cs "Thank you!"
            $ cath_counter += 1
            n "Current balance: $[cath_counter]."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            n "CS makes his way back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            $ lunatic_check2 = True  
            jump dx_after_seek_competitors
        elif lunatic_votes == 6 or lunatic_votes == 7:
            l_cultist "Y'know what? You can have this."
            n "They hand CS a gold coin."
            cs "Holy crap, thanks a lot!"
            $ cath_counter += 100
            n "Current balance: $[cath_counter]."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            n "CS gets back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            $ lunatic_check2 = True
            jump dx_after_seek_competitors       
        elif lunatic_votes == 10:
            l_cultist "I think you deserve this."
            n "They hand CS a shiny platinum coin."
            cs "Woohoo!"
            $ cath_counter += 10000
            n "Current balance: $[cath_counter]."
            show cs cultist flipped with determination
            hide cs with moveoutleft
            n "CS happily makes his way back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            $ lunatic_check2 = True
            jump dx_after_seek_competitors      
        else:
            jump secret_dx
    if lunatic_check:
        cs "I guess I can check about doing those questions again?"
        hide cs with moveoutright
        n "CS runs over to meet the Lunatic Cultists."
        scene cult_zone1
        show lunatic_cultist at mid_right
        with dissolve
        show cs cultist at mid_left with moveinleft
        l_cultist "Welcome back."
        l_cultist "Was there anything you needed?"
        cs "Can I answer those questions again?"
        l_cultist "Unfortunately, we gave you one shot at answering those questions."
        l_cultist "We travelled into your mind, if you couldn't answer them there, why do it again?"
        show cs disappointed cultist
        cs "I... guess that would make sense."
        cs "Dangit."
        l_cultist "You can try the first set of questions again though!"
        show cs cultist
        cs "Sure, I'll give it another try!"
        jump dx_after_lunatic_jump
    cs "Hmm, who are those guys? They look like plague doctors, almost..."
    cs "Let's go check them out."
    hide cs with moveoutright
    n "CS runs over to meet the Lunatic Cultists."
    scene cult_zone1
    show lunatic_cultist at mid_right
    with dissolve
    show cs cultist at mid_left with moveinleft
    cs "Hey, guys! Cultist here!"
    l_cultist "Aren't we all?"
    cs "So, what do you guys do? Who do you worship?"
    l_cultist "We are the Lunatic Cultists. We worship our leader, who plans to summon the Moon Lord and bring balance to the world!"
    cs "I can see the \"lunatic\" part, definitely. That sounds pretty crazy."
    l_cultist "Well, what about you then?"
    show cs disappointed cultist
    cs "We worship CSGod, who will use YTP Mag--"
    cs "... Yeah, okay, {i}I{/i} sound crazy too."
    cs "My plan was to ask you guys for votes, but I don't think our ideas are as big as yours."
    show cs cultist
    l_cultist "If you want our votes, you must pass a quiz."
    $ lunatic_votes = 0
    l_cultist "If you can guess every answer correctly, we will give you {i}all{/i} of our votes!"
    cs "Alright well, lay it on me."
label dx_after_lunatic_jump:
    l_cultist "What are the three evils of the world?"
    # CS answers
    $ terraria_question_1 = renpy.input("Name the first evil.", terraria_question_1, length = 32).lower()
    $ terraria_question_2 = renpy.input("Name the second evil.", terraria_question_2, length = 32).lower()
    $ terraria_question_3 = renpy.input("Name the third evil.", terraria_question_3, length = 32).lower()
    $ all_terraria = [terraria_question_1, terraria_question_2, terraria_question_3]
    cs "[terraria_question_1], [terraria_question_2], and [terraria_question_3]."
    if terraria_question_1 == "fuck" and terraria_question_2 == "sex" and terraria_question_3 == "balls":
        jump secret_dx2
    if "hallow" in all_terraria and "crimson" in all_terraria and "corruption" in all_terraria:
        l_cultist "Wait, how the hell did you know that?"
        cs "There is this game called--"
        l_cultist "You don't need to make an excuse. You are clearly well-studied in our teachings."
        cs "Except, I'm not?"
        l_cultist "I'm at a loss for words."
        l_cultist "We'll give you all our votes, because no one outside of the cult is supposed to know this."
        $ lunatic_votes += 10
        $ total_votes += lunatic_votes
        cs "Woohoo!"
        cs "Thank you so much!"
        if god_money:
            l_cultist "I think you deserve this."
            n "They hand CS a shiny platinum coin."
            cs "Woohoo!"
            $ cath_counter += 10000
            n "Current balance: $[cath_counter]."
            $ lunatic_check2 = True
        show cs cultist flipped with determination
        hide cs with moveoutleft
        n "CS heads back to the convention floor."
        scene cult_con with dissolve
        show cs cultist at center with moveinleft
        cs "I've barely played Terraria, so either I looked it up or asked the chat."
        cs "Either way, I've gotten us a ton of votes now!"
        $ lunatic_check3 = True
        jump dx_after_seek_competitors
    else:
        if lunatic_check:
            l_cultist "Sorry, those aren't the correct answers."
            show cs disappointed cultist
            cs "Fuck."
            show cs disappointed cultist flipped with determination
            hide cs with moveoutleft
            n "CS sulks back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            jump dx_after_seek_competitors
        l_cultist "Dude, how was he gonna know that? Only {i}we{/i} know that!"
    l_cultist "Shit, you're right. That was probably too hard."
    l_cultist "Alright, for these next questions, we'll peer into your mind!"
    show cs disappointed cultist
    cs "Woah, wait--"
    scene black with dissolve
    n "The cultists take CS into a limbo-like area, where he remembers all of the adventures from other timelines."
    show lunatic_cultist at center with moveinright
    play music space_classroom
    l_cultist "Alright, cs... 188?"
    show lunatic_cultist flipped
    l_cultist "That's your name, apparently…"
    show lunatic_cultist
    l_cultist "Let's ask you a few questions."
    l_cultist "How many friends did you gather to help takedown Copguy EX? Excluding you, of course."


    $ csb_question_1 = renpy.input("How many friends did you gather to defeat Copguy EX?", csb_question_1, length = 32).lower()
    if csb_question_1 in ["12", "twelve", "a dozen"]:
        $ lunatic_votes += 3
        l_cultist "Alright, good. Next question."

    l_cultist "Including the bad ones, how many total endings you can get in this game?"
    $ csb_question_2 = renpy.input("How many endings can you get? (Plus the bad ones)", csb_question_2, length = 32).lower()
    if csb_question_2 in ["27", "twenty-seven", "twenty seven"]:
        $ lunatic_votes += 4
        l_cultist "Alright, you're doing pretty good so far!"
    l_cultist "You've already won most of our votes, but we have one more question that'll give you the last of 'em."
    l_cultist "You ready?"
    l_cultist "Last question."
    
    l_cultist "How much money in USD did you make in Country route?"
    l_cultist "For the sake of convenience, we'll give you the conversion from pounds and yen to US dollars." 
    n "1 Japanese Yen = 0.0062 USD"
    n "1 Pound Sterling = 1.26 USD"
    l_cultist "You made need to use a calc."
    show lunatic_cultist flipped
    l_cultist "... That's slang for \"calculator,\" if you didn't know."
    show lunatic_cultist
    $ csb_question_3 = renpy.input("How much richer is CS after Country route?", csb_question_3, length = 32).lower()
    if csb_question_3 in ["148600", "148,600", "$148600", "$148,600"]:
        $ lunatic_votes += 3
        l_cultist "Wow, you got every question right! Good job!"
    
    jump dx_after_quiz_finish

label dx_after_quiz_finish:
    l_cultist "Let's bring you back to reality, now."
    stop music fadeout 3.0
    n "CS' mind feels like it's being untangled, then put back together again."
    play music ten_feet_away if_changed
    scene cult_zone1
    show cs disappointed cultist at mid_left
    show lunatic_cultist at mid_right
    with dissolve
    cs "Woah, where am I?"
    cs "And, what the hell just happened?"
    l_cultist "Well, we asked you some questions from deep within your consciousness, and then cleared your short-term memory afterward."
    show cs angry cultist
    cs "Wait, why did you wipe my mind?"
    l_cultist "Because you could see how everything played out in different timelines?"
    l_cultist "I don't know, I feel like knowing what you did in five different lives would screw something up."
    l_cultist "Either with {i}you,{/i} or with reality itself."
    cs "As long as you didn't remove my frontal lobe, or something, I guess that's all that matters."
    show cs cultist
    l_cultist "Well, we should gather up your votes."
    l_cultist "It looks like you got..."
    l_cultist "[lunatic_votes] votes."
    $ total_votes += lunatic_votes
    if lunatic_votes == 0:
        jump dx_after_zero_right
    elif lunatic_votes == 3 or lunatic_votes == 4:
        jump dx_after_one_right
    elif lunatic_votes == 6 or lunatic_votes == 7:
        jump dx_after_two_right
    elif lunatic_votes == 10:
        jump dx_after_three_right
    else:
        jump secret_dx
    #CS got zero right
label dx_after_zero_right:
    show cs disappointed cultist
    cs "Dang, I really got no votes?"
    l_cultist "Sorry, but you didn't get any of your answers right."
    l_cultist "Maybe consider calling some of your friends, so you can remember who they are."
    cs "Yeah, yeah, I'll get going..."
    if god_money:
        cs "Also, before I go, do you guys have any spare change?"
        l_cultist "I guess we have a bit…"
        n "They hand CS a copper coin."
        cs "Thanks."
        $ cath_counter += 0.01
        n "Current balance: $[cath_counter]."
        $ lunatic_check2 = True
    show cs disappointed cultist flipped with determination
    hide cs with moveoutleft
    n "CS sulks back to the convention floor."
    scene cult_con with dissolve
    show cs disappointed cultist at center with moveinleft
    cs "That really sucks. I can't believe I did {i}that{/i} bad."
    cs "I need to find more people to get votes from..."
    $ lunatic_check = True
    jump dx_after_seek_competitors
    #CS got one right
label dx_after_one_right:
    cs "Hey, I'll take whatever I can get."
    l_cultist "You could've done a bit better, sure, but that was probably quite a bit for you to take in."
    cs "Oh, well, it's okay."
    if god_money:
        l_cultist "Here, we have something..."
        n "They hand CS a silver coin."
        cs "Thank you!"
        $ cath_counter += 1
        n "Current balance: $[cath_counter]."
        $ lunatic_check2 = True
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS makes his way back to the convention floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Hey, at least I got some votes. I should still go try for more."
    cs "Let's see…"
    $ lunatic_check = True
    jump dx_after_seek_competitors
    #CS got two right
label dx_after_two_right:
    cs "That's not bad at all!"
    l_cultist "To be honest, that last question was pretty hard."
    l_cultist "I don't blame you for not getting it."
    cs "Well, I still did pretty good, I think."
    if god_money:
        l_cultist "Y'know what? You can have this."
        n "They hand CS a gold coin."
        cs "Holy crap, thanks a lot!"
        $ cath_counter += 100
        n "Current balance: $[cath_counter]."
        $ lunatic_check2 = True
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS gets back to the convention floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Well, I'm doing pretty good, I would say!"
    cs "I need to get some more votes, but I'm feeling confident!"
    cs "Alright, who's next?"
    $ lunatic_check = True
    jump dx_after_seek_competitors
    #CS got them all right
label dx_after_three_right:    
    cs "Woohoo!"
    l_cultist "Geez, you've got a really good memory."
    l_cultist "You deserve to win this year. Good luck to ya, man."
    cs "Thank you!"
    if god_money:
        l_cultist "I think you deserve this."
        n "They hand CS a shiny platinum coin."
        cs "Woohoo!"
        $ cath_counter += 10000
        n "Current balance: $[cath_counter]."
        $ lunatic_check2 = True
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS happily makes his way back to the convention floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    # This is a reference to Fallout: NV, keep this the way it is
    cs "Who won the lottery? I did!"
    cs "Smell that air!"
    cs "I really think we are gonna win this!"
    cs "Who's next?"
    $ lunatic_check = True
    jump dx_after_seek_competitors

label dx_after_blindeye_ask:
    cs "Those guys look pretty strange."
    cs "They look like they have eyes on their hoods!"
    n "CS walks over to the optical-hooded fellows."
    cs "Hey guys! See Ess here!"
    blind_eye "Well, we prefer not to see."
    blind_eye "We are the Society of the Blind Eye, and we remove traumatizing memories from our local town."
    cs "Oh crap, that sounds really sketchy."
    cs "How… do you, do that?"
    cs "Do you use some crazy voodoo magic or some shit?"
    blind_eye "No, we use this."
    n "The Blind Eye cultist pulls out what looks like a gun with a lightbulb on the end of it."
    cs "Geez, does that really work? It looks like it was built in the 1800's!"
    blind_eye "Yes, well, it did."
    blind_eye "Unfortunately, it broke recently and we haven't been able to fix it."
    blind_eye "... I may have dropped it too many times."
    cs "Well, is there any way I can help?"
    blind_eye "Well, there is one man who can help us…"
    blind_eye "Do you perchance know a Fiddleford? Fiddleford McGucket?"
    cs "...No. Can't say I have."
    blind_eye "Hmm…"
    blind_eye "They said they would be here… I wonder where they are…"
    cs "I can ask around for them, if you want me to."
    blind_eye "That would be great! We really need them to help fix our gun."
    cs "Sure, I'll be back soon!"
    n "CS heads back to the convention floor."
    cs "Well, now I have to find this guy…"
    cs "Fiddleford? I think their name was?"
    cs "Well anyways…"

label dx_after_branch_ask:
    play music ten_feet_away if_changed    
    scene cult_con
    show cs cultist at center
    cs "I'm gonna go back to the Blue Branch guys."
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS walks back to check on Blue Branch."
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    with dissolve
    show cs cultist at left with moveinleft
    cultist "Welcome back! Did you need anyone else?"
    jump menu_branch_ask

label menu_branch_ask:
    menu:
        "Ask for help again":
            jump dx_after_cult_questions
        "Finish gathering votes":
            jump dx_after_branch_ask2
        "Continue gathering votes":
            cs "Nevermind, I'm gonna see if I can get some more votes."
            cultist "Alright, well, get out there and show them how cool we are!"
            cs "On it!"
            show cs cultist at offscreenright with move
            pause 0.3
            show cs cultist at offscreenright with vpunch
            play sound sfx_clonk
            pause 1.0
            show cs disappointed cultist flipped at right with moveinright
            cs "Ow, that was a wall."
            cs "I'm okay..."
            cultist "Maybe raise your hood a bit?"
            cs "Nah, I'm fine. Alright, back to culting!"
            hide cs with moveoutleft
            play music ten_feet_away if_changed
            scene cult_con
            with dissolve
            show cs cultist at center with moveinleft
            jump dx_after_seek_competitors

label dx_after_branch_ask2:
    play music ten_feet_away if_changed 
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist at mid_right
    show cs cultist at left
    cs "I think I have impressed all the groups enough!"
    cultist_2 "Nice job!"
    cultist_3 "I hope we manage to win this year!"
    cultist "We are proud to see your involvement and dedication to Blue Branch."
    cultist "Let's hope you didn't let us down."
    cs "Well, I guess we'll find out soon enough."
    cs "When does the tallying start?"
    n "The cult leader checks his watch."
    cultist "It looks like it's gonna be starting any minute now."
    scene black with dissolve
    n "Placeholder for ending cultcon"
    n "Votes to win: 70"
    n "You have: [total_votes]"
    n "Returning to menu for now."
    return

label dx_after_convention_end:
    play music interference2
    scene conferencetv with fade
    cultist "Here are the results!"
    scene conferencetv at Move((0.0 , -1.0), (0.0, 0.0), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    show screen cultcon_votes
    pause 3.0
    show screen cultcon_votes_1
    play sound sfx_fabeep
    pause 2.0
    show screen cultcon_votes_2
    play sound sfx_fabeep
    pause 2.0
    show screen cultcon_votes_3
    play sound sfx_fabeep
    pause 2.0
    show screen cultcon_votes_4
    play sound sfx_fabeep
    pause 2.0
    show screen cultcon_votes_5
    play sound sfx_fabeep
    pause
    return

label dx_after_renault:
    stop music fadeout 1.0
    scene hobbytown
    show cs disappointed
    show carguy at right with moveinright
    play music scales_of_joy volume 0.8
    carguy "Hey, CS!"
    carguy "Do you want to test drive the all new Renault 5E?"
    cs "Uhh..."
    menu:
        "Yes":
            jump dx_after_yes_renault
        "No":
            jump dx_after_no_renault

label dx_after_no_renault:
    stop music fadeout 5.0
    music end
    scene hobbytown
    show cs disappointed
    show carguy at right
    carguy "Alright, suit yourself, then!"
    hide carguy with moveoutright
    jump dx_after_back_to_story

label dx_after_yes_renault:
    play music scales_of_joy volume 0.8 if_changed
    scene hobbytown
    show cs disappointed
    show carguy at right
    carguy "Sweet! Come with me!"
    show cs with determination
    hide cs
    hide carguy
    with moveoutright
    scene black with dissolve
    pause 1.0
    scene cs_street
    show renault
    with dissolve
    show carguy flipped at mid_left
    show cs at left
    with moveinleft
    cs "Well, for one thing, it feels good to be back in the present."
    carguy "Indeed! It will {i}also{/i} feel nice driving this new electric car from Renault!"
    show cs happy
    cs "Awesome! I can't wait!"
    scene black
    play sound sfx_doorslam
    pause 0.4
    play sound sfx_doorslam
    pause 0.5
    play sound sfx_driving volume 0.5
    scene renault_inside
    show drive_day behind renault_inside
    show cs at left
    show carguy at right
    with dissolve
    cs "Wow! This car feels super smooth to drive!"
    carguy "This car is like the R5 back in its day, a popular and essential car, but with a modern twist: silent, high-tech, environmentally-friendly and cheeky."
    cs "I love it already!"
    scene black
    play sound sfx_doorslam
    pause 0.4
    play sound sfx_doorslam
    pause 0.5
    stop music fadeout 1.0
    scene moomin_zone1
    show renault
    show cs at center
    show carguy at right
    with dissolve
    play music muumin_tani_fuyu
    music Muumin Tani Fuyu - Sumio Shiratori
    carguy "So, that was the new Renault 5E! I hope you enjoyed it!"
    cs "Yeah, I did!"
    show cs disappointed
    cs "By the way, where are we? I don't recognize this place at all!"
    show moomin flipped at left with moveinleft
    moomin "Hey, nice car! Can I test drive it?"
    carguy "Sure thing! Off you go, CS! You need to get back to your adventure!"
    show cs worried
    cs "Wait--{nw}"
    stop music
    music end
    scene hobbytown
    show cs disappointed
    play sound sfx_clapperboard
    cs "God, {i}damn{/i} it!"
    cs "I felt so in-control of that car, yet so {i}out-{/i}of-control at the same time..."
    cs "Why was I here, anyways?"
    cs "Oh, yeah..."
    jump dx_after_back_to_story

label dx_after_super_heaven:
    stop music fadeout 3.0
    music end
    scene white
    n "CS is engulfed with a blinding white light."
    n "..."
    pause 3.0
    show cs concentrate at left
    with Dissolve(5.0)
    pause 1.0
    show cs disappointed
    pause 1.0
    show cs concentrate
    pause 0.3
    show cs disappointed
    pause 1.0
    show cs concentrate
    pause 0.7
    show cs disappointed
    pause 1.0
    cs "Did..."
    cs "Did I die?"
    perfect_billy "Nonsense, CS!"
    cs "Billy? Is that you?"
    cs "Are you... God?"
    perfect_billy "Hi, it's me! Perfect Billy Mays!"
    perfect_billy "I am much more powerful than God!"
    perfect_billy "You haven't died, you have been brought up to Super Heaven, where only I reside!"
    cs "So I didn't die, but I'm in heaven? How does that work?"
    perfect_billy "You have contacted me directly in the second only other way possible!"
    perfect_billy "You mixed all of my products together!"
    cs "So Billy wasn't crazy... or maybe he was."
    cs "Wait, if you are Perfect Billy Mays, then who is the Billy that me and Arc were with this whole time?"
    perfect_billy "You see, when the Billy Mays you probably know of passed away in 2009, I embued another human with the power of pitching!"
    perfect_billy "That's the new Billy you know of!"
    cs "Okay okay, hold on a minute."
    perfect_billy "I have all day!"
    cs "So, there were other Billy Mays' before the 2009 one?"
    perfect_billy "Yep!"
    cs "Like, how far back?"
    perfect_billy "Since the beginning of time!"
    cs "Wait, so we have had Billy Mays' running around our planet, since like, caveman times?"
    perfect_billy "Even before that!"
    cs "How does that-- Y'know what, I've had a long day, I need to stop asking questions."
    perfect_billy "Good idea!"
    cs "So, okay, I'm a little freaked out about whatever the hell is going on, is there any way I can like, go home?"
    perfect_billy "I have the power to send you back to the present, but since you are here, I have some things to show you."
    perfect_billy "You may not remember, but we have met before!"
    cs "We have?"
    perfect_billy "Yes! You called me once by accessing my only commerical that plays on loop!"
    # Show screenshots of Old CSB2 here
    cs "I... can't say I remember doing that."
    cs "I don't think I even had a TV that old in a long time."
    perfect_billy "Wait, of course! You don't remember this at all!"
    perfect_billy "That's because this happened in another line!"
    cs "Another line?"
    perfect_billy "Of time. A timeline, if you will."
    cs "Oh, great, how many times did I screw up?"
    perfect_billy "Well... Let's look... together!"
    #Pan out to view the timeline
    cs "Woah..."
    cs "So... this is everything I could've ever done since I... started my old laptop up?"
    perfect_billy "Exactly!"
    cs "So, let's see here..."
    cs "I got fired from LTT, and became a rockstar with Anno and Arceus? That sounds awesome! I should've got fired!"
    cs "Or here, we went to Vegas and stopped a criminal on a train..."
    cs "...and in this one, me and my friends beat up Copguy? As a, god?"
    perfect_billy "It was Copguy EX, he was like, okay I don't even know what that was about."
    cs "Oh and what the fuck is this one? Pakoo deleted me from existence or some shit?"
    cs "I'm gonna really give it to him when I get back to the present!"
    cs "Wow! I don't wanna sound egotistical, but I think I have had the craziest life ever!"
    cs "Wait, why does it start there?"
    cs "Wouldn't this start from when I was born? That doesn't make much sense!"
    perfect_billy "Well..."
    perfect_billy "There is one thing I forgot to mention."
    cs "What, that this is a video game or something?"
    perfect_billy "What? No!"
    perfect_billy "Well, sorta."
    cs "What? Actually, I shouldn't be surprised."
    cs "That day ended with me beating up HoH SiS, that's only something I would do in a video game."
    perfect_billy "Well, when you were wondering why you have had such a crazy life, it's not by coincedence."
    perfect_billy "There is someone is this world who is known as..."
    perfect_billy "The Scriptwriter."
    perfect_billy "They are basically the reason you have had a chaotic life in the past year or so."
    cs "I was gonna say, I mean, like, why me?"
    cs "I just make like YouTube Poops and watch car crash videos!"
    perfect_billy "Well, this entity has chosen you to be the, protagonist of sorts."
    cs "So do I have like, real life plot armor?"
    cs "I mean, now that I think about it, we dug out of prison using plastic spoons."
    perfect_billy "Maybe, but all I know is that you are the one who has to stop them."
    cs "So, I can't relax yet?"
    cs "I was really hoping I could go back to a normal life again, I'm tired."
    perfect_billy "Don't worry CS, the least I can do is this!"
    #Billy heals CS
    cs "Wow, it feels like I just slept for a week!"
    cs "I don't think I have ever felt this good before."
    perfect_billy "That's great! Because I am gonna send you back home now."
    perfect_billy "Good luck!"
    cs "Wait that's it--{w=0.5}{nw}"
    jump finale_fun_value_land


