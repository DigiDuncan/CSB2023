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

    play music lets_hear_spring volume 2 if_changed
    music lets_hear_spring
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
    play music echoing_spring volume 2 if_changed
    music echoing_spring
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
    $ collect("pot")
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
    play music alien_atmosphere volume 2 if_changed
    music alien_atmosphere
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
    cs "Oh, no... It can't be..."
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
    play music apple_kid if_changed
    music apple_kid
    cs "...and what the hell is this outfit?"
    if fun_value(FUN_VALUE_MUSIC):
        pencil "Welcome, Apple kid, to the Pencil Cult!"
        cs "That's not my name..."
    else:
        pencil "Welcome to the Pencil Cult!"
    cs "..."
    cs "Should I even ask?"
    pencil "Every year, we host PencilCon, the biggest gathering of pencil lovers worldwide!"
    pencil "But we need to increase our numbers, so we grab random people and dress them up for our group!"
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
    pencil "But, for now, you are enlisted into the Pencil Cult and cannot leave until the event ends!"
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
    play music ten_feet_away_1 if_changed
    music ten_feet_away
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
    play music ten_feet_away_1 if_changed
    music ten_feet_away
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
    cs "I don't know how many times you have to take a shit, or whatever, but, in case you weren't watching, I AM FUCKING {i}STUCK IN THE PAST."
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
    show cultist behind cultist_2 at mid_right
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
    cs "Well, I'd heard about you guys from other CultCons, but I couldn't travel all the way to Montana until now."
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

# CULT CON INTRO

label dx_after_cult_questions:
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
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
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
    show cs cultist at left
    cs "Tell me more about how CultCon works."
    cultist "Well, you see, CultCon is mainly just an event for cultists to meet up and share ideas, teachings, and other cult-related topics."
    cultist "The Cult Competiton is a side thing that only a few cults try to participate in."
    cultist "If they win, not only do they win the advertised prize, but they get bragging rights about how awesome their cult is, which usually grows their cult in the process."
    cultist "{i}That's{/i} what we are interested in."
    cultist "We almost won a few years back when those Heaven's Gate people voted for us, but they all just killed themselves the following year."
    jump dx_after_cult_questions

label dx_after_competitors_ask:
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
    show cs cultist at left
    cs "Who are the main competitors this year?"
    cultist "Well, there are the pencil guys who usually end up in dead last, so they give their vote to us most of the time."
    cultist "Our main opponent is the Scientologists. They have so many numbers, and they aren't {i}completely{/i} psycho."
    cultist "We had the Branch Davidians here that one year, and, lemme just tell you... Yikes, those guys are fucking oblivious to anything their leader says."
    cultist "Anyway, yeah, they mainly have an advantage because they got that guy from Top Gun in their ranks now."
    cs "Tom Cruise?"
    cultist "Yeah, fuck that guy. If there is {i}one{/i} thing that I hate more than everything else, it's gotta be him."
    cultist "I don't think the rest of the groups are as bad as them, so I believe you'll have an easy time winning them over."
    jump dx_after_cult_questions

label dx_after_win_ask:
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
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
    play music ten_feet_away_1 if_changed
    music ten_feet_away
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
    show cs cultist at left
    cs "I think I'm good."
    cultist "Alright, awesome."
    if con_start:
        jump menu_branch_ask
    stop music fadeout 3.0
    music end
    cultist "Now go out there and--{nw}"
    play music hitsquad_2 if_changed
    music hitsquad_2
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
    play music ten_feet_away_1 if_changed
    music ten_feet_away
    show cs cultist at center with moveinleft
    $ con_start = True
    cs "Alright, so, there are a few cults I can challenge here."
    jump dx_after_seek_competitors

# CULT CON START

label dx_after_seek_competitors:
    play music ten_feet_away_1 if_changed
    music ten_feet_away
    if total_votes >= 25:
        play music2 [ "<sync music>audio/10_feet_away_2.ogg", ten_feet_away_2 ] if_changed
    if total_votes >= 50:
        play music3 [ "<sync music>audio/10_feet_away_3.ogg", ten_feet_away_3 ] if_changed
    if total_votes >= 75:
        play music4 [ "<sync music>audio/10_feet_away_4.ogg", ten_feet_away_4 ] if_changed
    if blanchin == True:
        play music5 [ "<sync music>audio/blanchin_remix.ogg", blanchin_remix ] if_changed
    scene cult_con
    show cs cultist at center
    cs "Which cult should I look for?"
    menu:
        "Pick a cult:"
        "Scientology":
            if gun_get == True:
                jump dx_after_science_quest
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

# PENCIL CULT

label dx_after_pencil_ask:
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
    show onscreen_sharpener at manual_pos(0.875, 0.5, 0.5) with dissolve
    n "The pencil man pulls out a pencil sharpener."
    show cs cultist
    cs "Lemme guess, a pencil sharpening contest?"
    pencil "How'd you know?"
    cs "Oh, just a hunch, that's all."
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    stop music4 fadeout 3.0
    stop music5 fadeout 3.0
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
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    stop music4 fadeout 3.0
    stop music5 fadeout 3.0
    music end
    show pencilroom
    show pencilguy at right
    show cs cultist at left
    with dissolve
    if god_money and check2:
        pencil "Jeez, you did it again."
        show cs cultist flipped with determination
        hide cs with moveoutleft
        n "CS turns around and leaves, offering no further explanation."
        scene cult_con with dissolve
        show cs cultist at center with moveinleft
        jump dx_after_seek_competitors
    elif god_money and pencil_check:
        pencil "Jeez, you did it again."
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
    music ten_feet_away
    show cs cultist at center with moveinleft
    cs "Well, that takes me back."
    cs "Or, I guess, that takes me {i}forward!"
    show cs disappointed cultist
    cs "Fuck, I need to get back home..."
    show cs cultist
    cs "Alright, well..."
    jump dx_after_seek_competitors

# SCIENTOLOGY

label dx_after_science_ask:
    scene cult_con
    show cs cultist at center
    if gun_get:
        jump dx_after_science_quest
    if science_check and god_money:
        cs "I could try asking them for money, it's worth a shot."
        hide cs with moveoutright
        n "CS runs over to Scientology stand."
        scene science_zone
        show cruise flipped at mid_right 
        with dissolve
        show cs cultist at left with moveinleft
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
        n "Mr. Cruise pulls out a few tens and hands them to CS."
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
        scene science_zone
        show cruise flipped at mid_right
        with dissolve
        show cs cultist at left with moveinleft
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
    scene science_zone
    show cruise flipped at mid_right
    with dissolve
    show cs cultist at left with moveinleft
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
        n "Mr. Cruise pulls out a few tens and hands them to CS."
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

# CATHOLICS

label dx_after_catholic_ask:
    scene cult_con
    show cs cultist at center
    if god_money:
        hide cs with moveoutright
        n "CS goes to check out the Catholics."
        scene cath_zone
        show priest at mid_right 
        with dissolve
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
        scene cath_zone
        show priest at mid_right 
        with dissolve
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
    scene cath_zone
    show priest at mid_right
    with dissolve
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
    priest "I wasn't {i}planning{/i} on moving, but, thank you! Your donation is appreciated."
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
    scene cath_zone
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

# LUNATIC CULTISTS

label dx_after_lunatic_ask:
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
            l_cultist "I guess we have a bit..."
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
    stop music fadeout 2.0
    stop music2 fadeout 2.0
    stop music3 fadeout 2.0
    stop music4 fadeout 2.0
    stop music5 fadeout 2.0
    music end
    n "The cultists take CS into a limbo-like area, where he remembers all of the adventures from other timelines."
    show portalbg with dissolve
    show lunatic_cultist at center with moveinright

    play music space_classroom if_changed
    music space_classroom
    l_cultist "Alright, cs... 188?"
    show lunatic_cultist flipped
    l_cultist "That's your name, apparently..."
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
    scene cult_zone1
    show cs disappointed cultist at mid_left
    show lunatic_cultist at mid_right
    with dissolve
    play music ten_feet_away_1
    music ten_feet_away
    if total_votes >= 25:
        play music2 [ "<sync music>audio/10_feet_away_2.ogg", ten_feet_away_2 ]
    if total_votes >= 50:
        play music3 [ "<sync music>audio/10_feet_away_3.ogg", ten_feet_away_3 ]
    if total_votes >= 75:
        play music4 [ "<sync music>audio/10_feet_away_4.ogg", ten_feet_away_4 ]
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
    l_cultist "Sorry, but you didn't get any of our questions right."
    l_cultist "Maybe consider calling some of your friends, so you can remember who they are."
    cs "Yeah, yeah, I'll get going..."
    if god_money:
        cs "Also, before I go, do you guys have any spare change?"
        l_cultist "I guess we have a bit..."
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
    cs "Let's see..."
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
    l_cultist "Jeez, you've got a really good memory."
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

# SOCIETY OF THE BLIND EYE

label dx_after_blindeye_ask:
    if blind_check:
        jump dx_after_blindeye_reask
    cs "Those guys look pretty strange."
    cs "They look like they have eyes on their hoods!"
    hide cs with moveoutright
    n "CS walks over to the optical-hooded fellows."
    scene blind_zone
    show blind_eye_leader at mid_right
    show blind_eye at right behind blind_eye_leader
    with dissolve
    show cs cultist at mid_left with moveinleft
    cs "Hey guys! See Ess here!"
    blind_eye "Well, we prefer not to see."
    blind_eye "We are the Society of the Blind Eye, and we remove traumatizing memories from our local town."
    cs "Oh crap, that sounds really sketchy."
    cs "How... do you, do that?"
    cs "Do you use some crazy voodoo magic or some shit?"
    blind_eye "No, we use this."
    n "The Blind Eye cultist pulls out what looks like a gun with a lightbulb on the end of it."
    cs "Jeez, does that really work? It looks like it was built in the 1800's!"
    blind_eye "Yes, well, it did."
    blind_eye "Unfortunately, it broke recently and we haven't been able to fix it."
    blind_eye "... I may have dropped it too many times."
    cs "Well, is there any way I can help?"
    blind_eye "Well, there is one man who can help us..."
    blind_eye "Do you perchance know a Fiddleford? Fiddleford McGucket?"
    cs "...No. Can't say I have."
    blind_eye "Hmm..."
    blind_eye "They said they would be here... I wonder where they are..."
    cs "I can ask around for them, if you want me to."
    blind_eye "That would be great! We really need them to help fix our gun."
    cs "Sure, I'll be back soon!"
    if god_money:
        jump spare_change
    $ blind_check = True
    $ fiddle_search = True
    show cs cultist flipped with determination
    hide cs cultist with moveoutleft
    n "CS heads back to the convention floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Well, now I have to find this guy..."
    cs "Fiddleford? I think their name was?"
    cs "Well anyways..."
    jump dx_after_seek_competitors

label dx_after_blindeye_reask:
    if quest_finished == True:
        jump dx_after_blindeye_quest
    cs "Maybe I should check on the Blind Eye guys again."
    hide cs cultist with moveoutright
    n "CS rushes over to the Society of the Blind Eye."
    if gun_get == True:
        scene blind_zone
        show blind_eye_leader at mid_right
        show blind_eye at right behind blind_eye_leader
        with dissolve
        show cs cultist at mid_left with moveinleft
        blind_eye "Did you deal with the Scientologists yet?"
        cs "Oh yeah, I gotta go do that!"
        jump dx_after_seek_competitors    
    # After asking Blue Branch
    if blue_check:
        scene blind_zone
        with dissolve
        show cs cultist at mid_left with moveinleft
        cs "Huh, where did they go?"
        cs "Maybe they went looking for him themselves?"
        n "CS spots a door slightly cracked open next to the wall where they were standing."
        cs "Hmm..."
        cs "I'm gonna go take a peek..."
        hide cs with moveoutright
        scene black with dissolve
        n "CS gently opens the door."
        cs "Man, I can't see a thing in here!"
        cs "Where's the light switch?"
        cs "Aha! Found it!"
        scene janitor_closet
        show cs cultist at left
        show blind_eye_leader at right
        show cultist at mid_right
        cs "Huh?"
        fiddle "Okay wait I can--"
        cs "Whaaaat?!?"
        cs "You're the leader of Blue Branch??"
        $ blue_check = False
        fiddle "Okay well-- Yes-- It's a long story..."
        cs "This is fucking insane, hold on..."
        blind_eye "You seem to be not handling the situation well."
        blind_eye "Would you like us to remove this event from your memory?"
        cs "No, I'm good, I just wasn't expecting that."
        fiddle "Well, yes, I am the leader of Blue Branch."
        fiddle "I made this gun about 20 years ago, and gave it to these guys."
        fiddle "I wanted to keep helping them, but I got in a fight with the colleague I lived with. I needed to stay undercover."
        fiddle "I created Blue Branch and set up a small area in Montana, where I could stay in close contact with the Blind Eye."
        cs "Well, that's one crazy story."
        cs "Did you guys fix the gun?"
        fiddle "Yes, we did! I'm assuming you needed it for something?"
        cs "Yeah, I was looking for you."
        fiddle "Well, I'll head back to the cult, I shouldn't leave my fellow cultists alone for too long."
        fiddle "...And remember, don't tell anyone about this.  Okay?"
        cs "Got it."
        hide cultist with moveoutleft
        n "Fiddleford leaves the scene."
        blind_eye "Well CS, thank you for sending Fiddleford."
        cs "I didn't even know--"
        blind_eye "Anyways, now that you are here, would you like to help us with a favor?"
        cs "Sure thing!"
        blind_eye "Since our gun is fixed now, we would like you to erase some embarrassing memories from another group here."
        cs "Who are they?"
        blind_eye "It's... the scientologists."
        cs "Oh, figures."
        blind_eye "If you can make sure Tom Cruise forgets about us, we'll give you most of our votes."
        blind_eye "All you have to do is type \"blind eye\" on the keypad."
        cs "Is it case sensitive?"
        blind_eye "There are no caps, no numbers, no nothing."
        cs "Alright, good to know."
        blind_eye "We should also mention, please don't type anything else in there, and don't use it on anyone else."
        blind_eye "It's not a toy, it's used to remove traumatizing memories."
        cs "Don't worry, I won't use this thing on anyone else. Promise."
        blind_eye "Alright well, good luck."
        show cs cultist flipped with determination
        hide cs cultist with moveoutleft
        n "CS takes the gun and heads back to the convention."
        $ gun_get = True
        scene cult_con with dissolve
        show cs cultist at center with moveinleft
        cs "Alright, time to find those Scientologists."
        jump dx_after_seek_competitors
    scene blind_zone
    show blind_eye_leader at mid_right
    show blind_eye at right behind blind_eye_leader
    with dissolve
    show cs cultist at mid_left with moveinleft
    blind_eye "Hey again, did you find Fiddleford yet?"
    cs "Not yet, but..."
    # Ask for money
label spare_change:
    if god_money:
        cs "Do you guys have any spare change?"
        if blind_check2 == True:
            blind_eye "I believe you've already come to ask us that question."
            cs "Whoops, my bad."
            cs "Pretend I didn't do that."
            show cs cultist flipped with determination
            hide cs cultist with moveoutleft
            n "CS heads back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            jump dx_after_seek_competitors
        blind_eye "..."
        pause 2.0
        cs "Sorry, I'm not trying to be a beggar, there is just this--{w=1.0}{nw}"
        blind_eye "No, we know. It's those Catholics, correct?"
        cs "...Yeah?"
        cs "I'm really running, and gunning if you will, to get as many votes as possible."
        blind_eye "Well, I wouldn't give them any money myself, but I guess {i}you{/i} can try giving this to them."
        $ cath_counter += 77
        n "The Blind Eye cultist gives CS a $77 dollar bill."
        blind_eye "I don't know if this has any real worth, so I guess you can do what you want with it."
        cs "Oh... Kay. Weird..."
        n "CS inspects the dollar bill."
        cs "This man on the bill... Nathaniel Northwest? Do you know them?"
        blind_eye "Yes, they are an extremely wealthy family from the town we come from."
        blind_eye "We don't really want to do anything with them, so I guess it's better that you have this now."
        cs "Alright, well, thanks!"
        if blind_check == False:
            $ blind_check = True
            $ fiddle_search = True
            show cs cultist flipped with determination
            hide cs cultist with moveoutleft
            n "CS heads back to the convention floor."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            cs "Well, now I have to find this guy..."
            cs "Fiddleford? I think their name was?"
            cs "Well anyways..."
            $ blind_check2 = True            
            jump dx_after_seek_competitors
        show cs cultist flipped with determination
        hide cs cultist with moveoutleft
        n "CS heads back to the convention floor."
        scene cult_con with dissolve
        show cs cultist at center with moveinleft
        cs "Well, that was weird..."
        $ blind_check2 = True     
        jump dx_after_seek_competitors
    # Keep looking
    cs "... I'll keep looking!"
    blind_eye "Thank you. Your service is very much appreciated."
    cs "No problem!"
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    n "CS keeps looking for Fiddleford."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Alright, I just gotta find this guy..."
    jump dx_after_seek_competitors

label dx_after_science_quest:
    if quest_finished == True:
        cs "I already did the Blind Eye's deed, no need to go talk to Tom Cruise again!"
        cs "He gives me the creeps..."
        jump dx_after_seek_competitors
    cs "Let's go talk to Mr. Cruise."
    hide cs cultist with moveoutright
    n "CS walks over to the Scientologists."
    scene science_zone
    show cruise flipped at mid_right
    with dissolve
    show cs cultist at mid_left with moveinleft
    show cruise with determination
    cruise "Hey, what do you want now?"
    n "CS types in \"blind eye\" into the gun and blasts Tom Cruise right in the head."
    cruise "Hey! What the hell did you do to me?"
    cruise "Do you know anything about the Society of the Blind Eye?"
    cruise "Who? What are you even talking about?"
    cs "That's all I needed to hear! Thank you!"
    show cs cultist flipped with determination
    hide cs cultist with moveoutleft
    n "CS heads back to the convention floor."
    cruise "Fuckin' weirdo..."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Now that I've done what they asked, I should go talk to them."
    $ quest_finished = True
    jump dx_after_seek_competitors


label dx_after_blindeye_quest:
    # After Blind Eye Quest
    if blind_check3 == True:
        cs "I think I am finished talking to those guys..."
        if god_money == False:
            cs "For now, at least."
            jump dx_after_seek_competitors
        if blind_check2 == False and god_money == True:
            cs "...But I could still ask them for money."
            hide cs cultist with moveoutright
            n "CS runs over to the Blind Eye cult."
            scene blind_zone
            show blind_eye_leader at mid_right
            show blind_eye at right behind blind_eye_leader
            with dissolve
            show cs cultist at mid_left with moveinleft
            jump spare_change
    cs "Time to go tell them that I'm done!"
    hide cs cultist with moveoutright
    n "CS runs over to the Blind Eye cult."
    scene blind_zone
    show blind_eye_leader at mid_right
    show blind_eye at right behind blind_eye_leader
    with dissolve
    show cs cultist at mid_left with moveinleft
    cs "Hey, I finished your task!"
    blind_eye "Oh, cool. Thank you for doing that for us."
    n "CS hands the gun back to the Blind Eye Guys."
    $ gun_get = False
    cs "No problem!"
    blind_eye "You didn't mess with anyone else's mind, correct?"
    cs "Nope!"
    blind_eye "Great. In return, we will give you most of our votes."
    $ blind_votes += 15
    $ total_votes += blind_votes
    cs "Woohoo!"
    blind_eye "Actually, we wouldn't mind giving you the rest of our votes, if you will comply to one final task."
    cs "Um, sure? What is it?"
    blind_eye "Well, our memory gun can also beam in memories, thanks to a recent upgrade."
    cs "Beam? You mean Mixer?"
    blind_eye "What?"
    cs "Sorry, I was like, half listening, nevermind."
    blind_eye "...Okay, well anyways, if you let us put our sick remix in your head, we'll give you the votes."
    menu:
        "No":
            cs "Sorry, I already have a lot going on in my head right now, I'll pass."
            blind_eye "Alright, fine..."
            if god_money == True:
                cs "Also..."
                jump spare_change
            show cs cultist flipped with determination
            hide cs cultist with moveoutleft
            n "CS heads back to the convention."
            blind_eye "One day, someone will listen to our epic remix..."
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            $ blind_check3 = True
            jump dx_after_seek_competitors
        "Yes":
            cs "Eh, why not?"
            blind_eye "Awesome!"
            n "The cultist tweaks the gun and types in his prompt in."
            blind_eye "Here goes nothing..."
            $ blanchin = True
            if blanchin == True:
                play music5 [ "<sync music>audio/blanchin_remix.ogg", blanchin_remix ] if_changed  
            blind_eye "Did it work?"
            cs "Yeah..."
            blind_eye "...Do you like it?"
            cs "I... what the hell are these lyrics?"
            cs "Is this permanent?"
            blind_eye "No, we can remove it at the end of the convention."
            blind_eye "So, do you like it?"
            cs "Uhh... sure!"
            blind_eye "Yesss! Finally someone likes our song!"
            cs "I'm gonna go now."
            blind_eye "Alright! See you at the end!"
            if god_money == True:
                cs "Also..."
                jump spare_change
            show cs cultist flipped with determination
            hide cs cultist with moveoutleft
            n "CS goes back to the convention floor."
            $ total_votes += 5
            scene cult_con with dissolve
            show cs cultist at center with moveinleft
            cs "I don't really like this song, but I guess this is a small price to pay for the chance to go home..."
            $ blind_check3 = True
            jump dx_after_seek_competitors

# BLUE BRANCH

label dx_after_branch_ask:
    scene cult_con
    show cs cultist at center
    cs "I'm gonna go back to the Blue Branch guys."
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS walks back to check on Blue Branch."
    if blue_check == True:
        scene blue_branch
        show cultist_2 at right
        show cultist_3 at mid_mid_right
        with dissolve
        show cs cultist at left with moveinleft
        cs "Huh."
        cs "Where'd the main guy go?"
        cultist_2 "I think they went to the bathroom or something?"
        cultist_3 "Wait, our leader is gone?"
        cultist_2 "Yeah idiot! Did you not see them leave?"
        cultist_3 "No, did you?"
        cultist_2 "...no..."
        cs "Oh well, I guess I'll come back later."
        show cs cultist flipped with determination
        hide cs with moveoutleft
        scene cult_con
        with dissolve
        show cs cultist at center with moveinleft
        jump dx_after_seek_competitors
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
    with dissolve
    show cs cultist at left with moveinleft
    cultist "Welcome back! Did you need anyone else?"
    jump menu_branch_ask

label menu_branch_ask:
    if fiddle_search:
        menu:
            "Ask for help again":
                jump dx_after_cult_questions
            "Finish gathering votes":
                jump dx_after_branch_ask2
            "Continue gathering votes":
                jump dx_after_continue_votes
            "Ask about Fiddleford":
                jump dx_after_branch_fiddleford
    else:
        menu:
            "Ask for help again":
                jump dx_after_cult_questions
            "Finish gathering votes":
                jump dx_after_branch_ask2
            "Continue gathering votes":
                jump dx_after_continue_votes

label dx_after_continue_votes:
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
    scene cult_con
    with dissolve
    show cs cultist at center with moveinleft
    jump dx_after_seek_competitors

label dx_after_branch_fiddleford:
    cs "Do any of you guys know a Fiddleford?"
    cultist "..."
    cultist "No. Who asked you this?"
    cs "...The Blind Eye Association?"
    cultist "I see."
    cs "So, uhh..."
    cultist "Why don't you head back to the convention? You gotta get more votes for us!"
    cs "Yeah, you're right."
    show cs cultist flipped with determination
    hide cs with moveoutleft
    n "CS heads back to the convention floor."
    scene cult_con with dissolve
    show cs cultist at center with moveinleft
    cs "Well, that was weird, the leader just tried to push me away..."
    cs "I wonder if the Blind Eye people have found him themselves..."
    cs "Oh well..."
    $ blue_check = True
    $ fiddle_search = False
    jump dx_after_seek_competitors

label dx_after_branch_ask2:
    scene blue_branch
    show cultist_2 at right
    show cultist_3 at mid_mid_right
    show cultist behind cultist_2 at mid_right
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
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop music3 fadeout 3.0
    stop music4 fadeout 3.0
    stop music5 fadeout 3.0
    music end
    scene black with dissolve
    jump dx_after_convention_end

# END OF CULTCON

label dx_after_convention_end:
    play music interference2 if_changed
    music interference2
    scene conferencetv
    show cultcon_leader:
        xpos 762
        ypos 269
    show stand
    with dissolve
    cultcon_leader "Here are the results!"
    window hide
    scene conferencetv at Move((0.0 , -1.0), (0.0, 0.0), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show cultcon_leader at Move((0.397 , 0.25), (0.397, 1.25), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show stand at Move((0.341 , 0.587), (0.341 , 1.587), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
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
    if total_votes >= 70:
        jump dx_after_win
    if total_votes < 69:
        jump dx_after_lose
    else:
        jump dx_dogcheck

label dx_dogcheck:
    stop music
    music end
    show csbdxdogheck
    pause
    return

label dx_after_win:
    hide screen cultcon_votes
    hide screen cultcon_votes_1
    hide screen cultcon_votes_2
    hide screen cultcon_votes_3
    hide screen cultcon_votes_4
    hide screen cultcon_votes_5
    scene conferencetv at Move((0.0 , 0.0), (0.0, -1.0), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show cultcon_leader at Move((0.397 , 1.25), (0.397 , 0.25), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show stand at Move((0.341 , 1.587), (0.341 , 0.587), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    play music tv_hall_of_fame
    music tv_hall_of_fame
    cultcon_leader "Well cultists and religious orgs, we have our winner for Cultcon 2003!"
    cultcon_leader "For the first time in a while, we have ourselves a winner from a small indie cult!"
    cultcon_leader "That's right! Our winner is..."
    cultcon_leader "Blue Branch!"
    cultcon_leader "Can we get someone from the cult to come up and claim the prize?"
    show cs cultist at left with moveinleft
    cs "Woohoo! We did it guys!"
    cultist_2 "You did it, newbie! You made us win!"
    cultist "Well what are you waiting for? Go up there, make me proud!"
    n "CS struts up to the main stage."
    cultcon_leader "Congratulations! Do you have anything to say to Cultcon this year?"
    cs "Today I learned that no matter how many followers you have in your cult, you can always manage to gather more if you try hard enough."
    cultcon_leader "Some inspiring words from Blue Branch! Let's hear it for them!"
    # Cheering
    n "While everyone is praising CS for his victory, someone is seen pushing everyone out of the way."
    cultcon_leader "Thank you everyone for coming, and have a safe--{nw}"
    show cruise flipped at left with moveinleft
    show cs cultist disappointed at hpunch
    show cs cultist disappointed flipped at mid_left with move
    cruise "You promised, buddy!"
    cruise "I want you to show off \"Your Special Thing\" to everyone here!"
    cultcon_leader "Woah woah, calm down, Tom."
    cultcon_leader "That's really messed up, man."
    cultcon_leader "We really don't our winner here to show off their genitals just to prove that they won."
    cruise "Wait wha--{nw}"
    cs "Yeah man, I'm not even gay enough to even promise something like that."
    cultcon_leader "Not sure what kind of promise you made Tom, but this an extremely unappropriate time for this."
    cultcon_leader "Can someone get this guy out of here?"
    cruise "Nooo!"
    hide cruise
    cultcon_leader "Anyways, without further ado..."
    cultcon_leader "Here is your grand prize!"
    cs "Woohoo!"
    n "CS tries to pick the bucket up, but remembers how heavy it is."
    cs "Ah crap, can someone help me carry this?"
    stop music fadeout 3.0
    music end
    n "One of the other Blue Branch cultists runs out and helps CS carry it outside."
    n "After they manage to carry the bucket outside, CS tries to figure out how to turn the machine on."
    cs "I could've sworn there was a switch right here..."
    cultist "Hey, thank you again for helping us win Cultcon."
    cultist "We've never actually managed to get enough votes to even hit the Top 5, probably because of our stubborn attitudes."
    cultist "But you were different. Despite being a fellow hater just like us, you've managed to get the majority of the culting world to appreciate our work."
    cs "No problem, Thanks for letting me keep the grand prize!"
    cultist "Would you like us to give you a ride home?"
    cs "Well uhh, about that..."
    cs "Yeah, that would work for me. I live in Western Montana."
    cultist "Wait really?"
    cultist "That's were we live!"
    cs "Wow, what a crazy coincidence!"
    cs "Alright, well let's get this thing in the car then."
    cultist_2 "You're coming with us? Awesome!"
    n "All the cultist members jump into the car and head out on their way home."
    cultist_2 "That was the best Cultcon I've ever had!"
    cultist_2 "I hope we'll be able to meet you again sometime!"
    cs "Probably, yeah."
    n "CS leans over the backseat to try to the time machine controls again."
    cs "Come on, I know the switch is like right here..."
    cs "Ah yes! I found it!"
    n "In that moment, a loud whoosh above the car sends everyone shaking!"
    cultist "Woah! What in the world?"
    cs "Damnit, almost had it!"
    cultist_2 "What just happened?"
    cultist "I think... I think a jet just flew over our heads!"
    cs "A jet?"
    cultist "Yeah, they were flying way too low!"
    cs "Weird, I wonder what's going on."
    cs "Back to figuring out this machine."
    cultist "Hold up. I can see it turning around!"
    cultist "It's flying right back at us!"
    #The jet does a strafing run on the car, rattling everyone again.
    cultist_2 "Shit! Why are they firing at us?"
    n "All of a sudden, a familiar voice is heard cutting through the radio."
    cruise "Hey losers!"
    cruise "Yeah, I don't care if you guys won, because you all are still LOSERS to me!"
    cruise "Especially one of you, who made a promise and embarrassed me infront of the whole convention!"
    cultist "Damnit! This asshole again! Why won't he just fuck off?"
    cultist "He also can apparently fly a jet now, which is just great to know!"
    cs "Yeah, of course he can! He's Tom Cruise! Haven't you seen Top Gun?"
    cultist "I thought that was just a trained professional!"
    cs "Just, try to dodge his gunfire! I can probably save us with this machine!"
    cs "If you can buy me enough time, I can teleport us out of here!"
    cultist_2 "That rusty bucket was a teleporter THE WHOLE TIME??"
    cultist "Shut up and let him figure it out! I'll do my best to keep us alive, but you gotta hurry!"
    #Cue minigame here

label dx_after_win_finale:
    cs "Yes! I got it!"
    n "The machine sputters and shoots out some flashes of light, before shutting off again."
    cs "What the hell?"
    csgod "CS, what the hell are you doing now?"
    csgod "Great, you are still with these guys?"
    cs "Dude, now is not the time!"
    cultist_2 "Oh my god! It's CSGod!"
    cultist "No way! Are you--"
    cs "CSGod, can you at least do anything to get rid of this jet that's bothering us?"
    csgod "What the hell did you guys do to get a jet on you?"
    cs "It's Tom Cruise! He got mad because--"
    csgod "Oh fuck that guy. Yeah let me get rid of him for you."
    #CSGod shoots Goodsprings CS at Tom's jet, causing it to crash down infront of the car. The car swerves to try and not hit the wreckage, only to fly off the road and flip.
    n "After that aftermath, CS and the cultists crawl out of the car."
    cultist "Is everyone good?"
    cultist_2 "Yeah, shocked, but we are fine."
    n "CS pulls the machine out of the car, to find it still not working."
    cs "This is really bad, how am I gonna fix this stupid bucket?"
    cultist "Don't worry, I'm sure we can figure out something."
    cruise "Not so fast!"
    cultist "Why do you keep coming back?!"
    cruise "I'm not letting you guys get away this time!"
    cruise "This is the last straw!"
    cruise "It. Ends. Now!"
    n "All of a sudden, the time machine sputters back to life, shooting a beam of light into the air!"
    cs "Yes! Finally!"
    cruise "You've got to be kidding me!"
    cruise "Fuck you!"
    #Cruise starts firing, hits one of the smaller cultists
    cultist_3 "Ahh!! I just got shot!"
    cultist_2 "No! Dave! I loved you!"
    cs "Damnit! Everyo--"
    n "Before CS can finish his exclamation, everyone and everything is engulfed in brightness, CS' surroundings becoming nothing but a white void."
    jump dx_after_super_heaven

label dx_after_lose:
    hide screen cultcon_votes
    hide screen cultcon_votes_1
    hide screen cultcon_votes_2
    hide screen cultcon_votes_3
    hide screen cultcon_votes_4
    hide screen cultcon_votes_5
    scene conferencetv at Move((0.0 , 0.0), (0.0, -1.0), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show cultcon_leader at Move((0.397 , 1.25), (0.397 , 0.25), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show stand at Move((0.341 , 1.587), (0.341 , 0.587), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    play music tv_hall_of_fame
    music tv_hall_of_fame
    cultcon_leader "Well everyone, we have our winner for this year!"
    cultcon_leader "It seems once again, Scientology has won with an outstanding 70 votes!"
    cultcon_leader "Tom, you can come up and claim your prize?"
    cruise "Hell yeah!"
    cruise "And please, call me Mr. Cruise."
    cs "Aw man, I guess I couldn't get enough votes."
    cultist "It's alright, The Scientologists probably cheated anyways, knowing them."
    cultist "There is always next year."
    cs "I guess so."
    cultist_2 "Fuck those stupid guys! This is why I hate everything!"
    cultist "Come on guys, let's get to the car."
    cultist_3 "I'll meet you guys there, I have to go to the bathroom first."
    stop music fadeout 3.0
    music end
    n "CS and the Blue Branch Cult Leader head out into the parking lot."
    cultist "Damnit, where the hell is my car?"
    cs "What kind of car do you have?"
    cultist "It's a Blue 1998 Fiat Multipla, but I can't find it."
    cs "Wow, you guys really do hate everything."
    cs "Did the other guy also have to go to the bathroom? I can't find them anywhere..."
    cultist "I dont know, but I wanna find our car first."
    n "In that moment, the other two cultists run out of the convention entrance, carrying the time machine."
    cultist_2 "We got it!"
    cultist_3 "Guys, we got the grand prize!"
    cs "Wait what? How did you manage that?"
    cultist_2 "We snuck backstage and stole this bucket when they weren't looking!"
    cultist_3 "But we gotta get going, now!"
    n "As they are being told this, Tom Cruise is heard yelling in the distance."
    cruise "You little shits! Give me my winnings back!"
    cultist "Sh-- Alright fine! Everyone, we are stealing this car!"
    n "The leader smashes the window open and unlocks it."
    cultist "Newbie, you drive, you two, cram the bucket in, and I'll keep him distracted!"

# RENAULT

label dx_after_renault:
    stop music fadeout 1.0
    scene hobbytown
    show cs disappointed
    show carguy at right with moveinright
    play music scales_of_joy volume 0.8 if_changed
    music scales_of_joy
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
    music scales_of_joy
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
    $ collect("renault")
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
    carguy "This car is like the R5 back in its day, a popular and essential car, but with a modern twist: silent, high-tech, environmentally-friendly, and cheeky."
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
    play music muumin_tani_fuyu if_changed
    music muumin_tani_fuyu
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

# SUPER HEAVEN

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
    cs "So, I didn't die, but I'm in Heaven? How does that work?"
    perfect_billy "You have contacted me directly in the only other way possible!"
    perfect_billy "You mixed all of my products together!"
    cs "So, Billy wasn't crazy... or maybe he {i}was."
    cs "Wait, if you are Perfect Billy Mays, then who is the Billy that Arc and I were with this whole time?"
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
    perfect_billy "I have the power to send you back to the present, but since you're already here, I have some things to show you."
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
    cs "Wow! I don't wanna brag, but I think I've had the craziest life ever!"
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
    cs "So, do I have, like, real-life plot armor?"
    cs "I mean, now that I think about it, we dug out of prison using plastic spoons."
    perfect_billy "Maybe! All I know is that you are the one who has to stop them."
    cs "So, I can't relax yet?"
    cs "I was really hoping I could go back to a normal life again. I'm tired."
    perfect_billy "Don't worry, CS! I can at least do {i}this{/i} for you!"
    #Billy heals CS
    cs "Wow, it feels like I just slept for a week!"
    cs "I don't think I have ever felt this good before."
    perfect_billy "That's great! Because I am gonna send you back home now."
    perfect_billy "Good luck!"
    cs "Wait that's it--{w=0.5}{nw}"
    jump finale_fun_value_land


