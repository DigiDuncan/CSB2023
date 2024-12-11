label fired_new_plan:
    stop music fadeout 3.0
    music end
    scene outside_ltt
    show cs angry at center
    with dissolve
    cs "This really sucks. One of my favorite YouTubers just kicked me out of my dream job and told me to never come back!"
    show cs
    cs "I {i}would{/i} be acting super emotional right now, but years of angry YouTube comments against me have already prepared me for this."
    show cs disappointed
    cs "Well, I guess I have no other choice than to look for another job."
    n "CS sulks away in defeat."

    scene alley with dissolve
    dxcom newplan
    show cs disappointed flipped with moveinright
    show cs disappointed
    cs "Ugh, what am I going to do now?"
    cs "I don't even know what other job I could get."
    cs "I've spent most of my life editing..."
    n "Before CS can spend much time thinking about alternatives, someone comes running up to him."
    show arceus worried at right with moveinright
    arceus "CS!"
    show cs scared
    cs "Ah! Arceus?!"
    arceus "CS, we've gotta get outta here, fast."
    show cs worried 
    cs "Okay, what? What's going on?"
    arceus "Cops. They're still after us."
    show cs angry
    cs "Oh, come on, {i}really?!{/i} Today has sucked bad enough already."
    show arceus
    arceus "What happened to you? I just thought you were out here for a smoke break."
    show cs disappointed
    cs "Arc, I don't smoke."
    arceus "Man, I don't know."
    play music dealin_dope volume 0.5 if_changed
    music dealin_dope
    if fun_value(FUN_VALUE_MUSIC):
        cs "No, I got caught dealin' dope."
        show arceus angry
        arceus "What the fuck?"
        cs "Hey, at least I'm not drinking, Arceus."
        show arceus
        cs "But, no, I got fired."
    else:
        cs "No, I got fired."
    arceus "Aw, man. That sucks. I'm sure we'll figure it out."
    arceus "Come on, let's go back to the hotel. We can think of something, I'm sure."
    cs "Alright, man, thanks. Let's go."
    hide screen dxcom

    scene hotel_lobby
    show cs flipped at right
    show arceus flipped at left
    with dissolve
    arceus "Come on up to my room, and we'll workshop where to go from here."
    show cs disappointed flipped
    cs "Alrighty, then. Not like I'll be able to pay for my own much longer..."
    arceus "Oh, c'mon, don't talk like that! Let's go."

    scene hotel_room
    show arceus at right
    show cs at left
    with dissolve
    arceus "Okay, let's think. We have two big problems: The cops, and money."
    cs "Right."
    arceus "Let's tackle these one at a time."
    cs "The cops, first."
    arceus "Nah, I don't think tackling the cops is going to work."
    show cs angry
    arceus "I'm thinking we need to convince them to give it up."
    show cs
    cs "How would we do that?"
    n "A knock is heard at the door."
    anno "Can I come in?"
    arceus "Yeah, of course."
    show anno at center with moveinleft
    anno "Hey, CS, what are you doing here?"
    cs "I got fired, and the cops are still after us."
    anno "Ah, fuck. What's the plan?"
    arceus "Nothing yet..."
    arceus "Wait. Anno, I've just got an idea."
    anno "What's up?"
    arceus "You know AI stuff, right?"
    anno "Well, yeah, but I don't see--"
    arceus "We AI generate a message to the cops telling them they don't need to go after us anymore."
    anno "From who?"
    arceus "HoH SiS."
    anno "Wait, yeah, I can totally do that. I have the models ready for that and everything."
    n "Anno starts typing away at his laptop, and within a few minutes, a voice plays out of the speaker."
    ed_ai "I think CS is a pretty good guy. You shouldn't arrest him."
    cs "Oh, my God, that's amazing! What about you two?"
    anno "Gotcha covered."
    if fun_value(FUN_VALUE_RARE):
        play sound sfx_obama volume 0.5
        bomahanobeep "I'm officially pardoning Annorexorcist and Arceus3251 because they really helped me out of a pickle."
    else:
        play sound sfx_obama volume 0.5
        obamanobeep "I'm officially pardoning Annorexorcist and Arceus3251 because they really helped me out of a pickle."
    show arceus happy
    arceus "Incredible as always, Anno."
    anno "I try."
    stop music fadeout 3.0
    music end
    cs "But, what about money? I'm still out of a job, and I'd like to keep having a roof over my head."
    show arceus
    arceus "I don't know, man, I can't think after all that. Let's take a bit and relax. Clear our heads."
    cs "Good call. Wanna play some {i}Guitar Hero?{/i}"
    anno "I'm down, but... do you have controllers?"
    cs "{i}Do{/i} I?"
    hide cs with moveoutleft
    n "Anno and Arceus look at each other confused."
    show cs guitar at left with moveinleft
    n "CS comes back holding two guitar controllers and a drum kit."
    if fun_value(FUN_VALUE_MUSIC):
        cs "Saw 'em on the side of the road. Couldn't pass 'em up. Now, hit me with your best shot!"
    else:
        cs "Saw 'em on the side of the road. Couldn't pass 'em up."
    jump fired_guitar_hero

label fired_guitar_hero:
    play music hit_me_with_your_best_shot volume 0.5 if_changed
    music hit_me_with_your_best_shot
    scene hotel_guitar_hero with dissolve
    dxcom hitme
    n "CS, Anno, and Arceus relax by playing some {i}Guitar Hero.{/i}"
    arceus "Man, we're all pretty good at this."
    cs "Wait, this gives me an idea."
    anno "What?"
    arceus "No, you're not thinking..."
    cs "Let's start a band!"
    arceus "Man, there's no way that'll work. Playing a video game isn't the same thing as making real music."
    cs "Come on! Anno knows AI, Arc is actually a really good percussionist, and I have millions of scrobbles, so I know my music."
    anno "He has a point..."
    arceus "Does he?"
    cs "What's the worst that could happen? We need money, don't we?"
    arceus "We do..."
    cs "Then, let's do this!"
    anno "I'm down!"
    cs "Arc?"
    arceus "What do I have to lose?"
    cs "Woohoo!"  # haha I did it too Pakoo -- DD
    # Learn to use commas, fuck-ass. "I did it too, Pakoo" - Arc
    stop music fadeout 3.0
    music end
    hide screen dxcom
    $ achievement_manager.unlock("guitar_hero")

    scene hotel_room
    show arceus at right
    show cs at left
    show anno at center
    with dissolve
    play music hightop volume 0.5 if_changed
    music hightop
    if fun_value(FUN_VALUE_MUSIC):
        cs "Maybe we should call Blank if we wanna get high on top. He's, like... an actual musician."
    else:
        cs "Maybe we should call Blank. He's, like... an actual musician."
    show cs phone
    n "CS calls Blank on Discord."
    blank "CS? Where the heck have you been?"
    cs "Don't worry about it, I'll explain soon. I need tips on making music."
    blank "Man, I don't know, I just open FL Studio and kinda click shit until music comes out."
    cs "Wait, that's it?"
    blank "I mean, that's not {i}it{/i}, but--"
    show cs happy
    cs "Awesome! Thanks, Blank!"
    n "CS hangs up."
    show cs
    cs "Well, you heard the man. Anno, do you have FL Studio?"
    anno "Just got it."
    cs "Well, let's get to work, boys!"
    jump fired_write_song

label fired_write_song:
    stop music fadeout 3.0
    scene black with dissolve
    n "After some time, the gang has their first song written."
    stop music fadeout 3.0
    music end
    scene hotel_room with dissolve
    show arceus happy at right with moveinright
    arceus "Ya know what? That's not half bad."
    show anno at left with moveinright
    anno "I like it a lot!"
    show cs at center with moveinbottom
    cs "Wanna play it one more time?"
    anno "Can do!"
    if fun_value(FUN_VALUE_MUSIC):
        n "Anno longs to ever hit play on the track."
    else:
        n "Anno hits play on the track."
    play music everlong volume 0.5 if_changed
    music everlong

    dxcom everlong
    n "{cps=15}{image=note_small1.png} We broke the chains, now we're free to fly,{w=1.5}\nEscaped concrete, and now we see blue skies{w=1.5}\nBecome brand new, we'll leave the past behind,{w=1.5}\nPrisoners no more, 'cause a new life we'll find {image=note_small2.png}"
    cs "Yeah, that's really good!"
    show arceus
    stop music fadeout 3.0
    music end
    hide screen dxcom

    arceus "Well, I guess all we have to do now is upload it."
    dxcom madlibs
    anno "Alright, boys, what do we call it?"
    $ song_name_1 = renpy.input("What should we call the song?", song_name_1, length = 32)
    cs "How about {i}[song_name_1]?{/i}"
    $ achievement_manager.unlock("name_is")
    if song_name_1 == "FUCK SEX BALLS":
        show arceus angry
        arceus "Haha, very funny, Pakoo."
        cs "Huh?"
        show arceus
        arceus "Sorry, I meant CS. I don't know why I said Pakoo."
        anno "Well, I like it."
        arceus "I'm cool with it."
    else:
        anno "That's awesome."
        show arceus happy
        arceus "I like it!"
    cs "Alright, it's settled! Let's upload {i}[song_name_1]{/i} to streaming services!"
    show arceus
    arceus "Are you going to plug it in the Discord?"
    cs "I guess I should, but... people are going to be really confused as to why I'm still not streaming..."
    anno "I think they're used to you not streaming for a while."
    cs "Fair, but... a music career?"
    arceus "Just say it's a side project."
    cs "Fair enough."
    n "Anno uploads the song, then CS tells the CSCord about it."
    discord "What the heck is this?"
    discord "Huh, this is pretty good."
    discord "CS can sing?!"
    show cs happy
    cs "It's going well! People seem to like it."
    arceus "Let's hit the hay and check in on it in the morning."
    anno "Yeah, I'm getting tired."
    cs "Sounds good to me!"

    scene black with dissolve
    n "While they sleep, the song accumulates streams..."
    hide screen dxcom
    jump fired_hotel_next_day

label fired_hotel_next_day:
    stop music fadeout 3.0
    scene hotel_room with dissolve
    show cs at left with moveinleft
    cs "Let's go get breakfast."
    show anno with moveinleft
    anno "Free waffles, hell yeah."
    show arceus flipped at right with moveinleft
    show arceus with determination
    arceus "Those sausages are amazing."

    scene hoh_elevator with dissolve
    show anno at left
    show arceus at right
    show cs
    with dissolve
    play music local_forecast volume 0.5 if_changed
    music local_forecast
    pause 2.0
    if fun_value(FUN_VALUE_MUSIC):
        cs "So, anyone see the local forecast?"
    else:
        cs "So, see any good shows lately?"
    arceus "You watch TV?"
    cs "Not really."
    arceus "Mmm."

    pause 2.0
    cs "Do you have any ideas for--{nw}"
    show arceus angry
    arceus "Man, I {i}just{/i} woke up."
    cs "Yeah, sorry."

    pause 2.0
    stop music fadeout 3.0
    music end
    play sound sfx_elevator_ding

    scene hotel_breakfast with dissolve
    show cs at center with moveinleft
    cs "Ah, nothing like a hotel breakfast to wake me up."
    n "The other two groggily join CS."
    show anno at left behind cs
    show arceus flipped at right behind cs
    with moveinleft
    show arceus with determination
    n "They all sit down to eat."

    n "As they eat, CS checks the number of streams on {i}[song_name_1].{/i}"
    show cs scared
    cs "Guys?"
    arceus "Mmm?"
    n "Arceus and Anno are stuffing their faces."
    play music now_what volume 0.5 if_changed
    music now_what
    if fun_value(FUN_VALUE_MUSIC):
        cs "That one song has, like, a hundred thousand streams. Now what?"
    else:
        cs "The song has, like, a hundred thousand streams."
    n "Arceus nearly spits out his food."
    # DX: arceus shocked?
    arceus "It has {i}what?!{/i}"
    n "CS shows Arceus the phone."
    show arceus happy
    arceus "Holy shit!"
    anno "Wait, that's crazy, actually."
    show cs happy
    cs "This is amazing! We might have a ticket out of here! We won't have to run from the cops anymore!" # we changing this line? since they already resolved this? - tate
    n "A random patron turns to look at CS."
    show cs worried
    cs "Uh... metaphorically, of course."
    n "The patron turns back around."
    show cs
    cs "{i}ahem{/i}\nAnyway...{w=0.5} so what now?"
    anno "I guess we keep it going?"
    show arceus
    arceus "We can't let this window close, right?"
    cs "I'm shocked, but, yeah! Let's do it!"
    n "The gang finishes their food and heads back up to their room."
    stop music fadeout 3.0
    music end
    hide cs
    hide anno
    hide arceus
    with moveoutright
    jump fired_song_2

label fired_song_2:
    stop music fadeout 3.0
    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve

    cs "Well, what do we write about next?"
    arceus "I've had an idea kicking around my head..."
    arceus "Hey, Anno?"
    anno "Yeah?"
    arceus "Hit me with something energetic, something in a good mood."
    anno "Gotcha."
    n "Anno tinkers around for a moment on his laptop, until..."
    play music happy_rock volume 0.5 if_changed
    music happy_rock
    if fun_value(FUN_VALUE_MUSIC):
        n "A happy rock instrumental plays from Anno's computer."
    else:
        n "An upbeat rock instrumental plays from Anno's computer."
    show arceus happy
    arceus "Heck yeah, awesome. Okay, here I go..."
    arceus "{cps=15}{image=note_small1.png} We're going down to Vegas,{w=1.5} we're gonna strike it rich!{w=1.5}\nWe're going down to Vegas..."
    show arceus worried
    arceus "Uh..."
    $ line_1 = renpy.input("Finish the line!", "", length = 64)
    cs "How about, '[line_1]'?"
    $ achievement_manager.unlock("first_song")
    show arceus happy
    arceus "Yeah!"
    arceus "{cps=15}{image=note_small1.png} We're going down to Vegas,{w=1.5} [line_1] {image=note_small2.png}"
    cs "Woohoo! That sounds awesome!"
    stop music fadeout 3.0
    music end
    anno "Let's get some backing vocals and a solo done, then we have another song!"
    arceus "I'm glad you guys like it :3"

    scene black with dissolve
    n "After a furious writing session, their new song is done!"

    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve
    anno "So, what do we call this one?"
    arceus "I liked your name for the last one, CS, so why don't you name this one, too?"
    cs "How about..."
    $ song_name_2 = renpy.input("What should we call the song?", song_name_2, length = 32)
    cs "{i}[song_name_2]?{/i}"
    show arceus happy
    arceus "You're a genius, CS."
    show cs happy
    cs "Aw, thanks, guys. Wait, we don't have a band name, either!"
    anno "Yeah, what were you thinking?"
    cs "I was thinking..."
    $ band_name = renpy.input("What should we call the band?", band_name, length = 32)
    cs "[band_name]!"
    anno "Woah, awesome! Not as good as \"Nirvana\", but, you know, it wasn't going to be."
    cs "Hell yeah! [band_name] forever!"
    n "They all high five."
    arceus "Well, I guess tomorrow we can release this one!"
    anno "Sounds good!"
    cs "I'm getting tired. I think we should hit the sack."
    if fun_value(FUN_VALUE_COMMON):
        arceus "I'm gonna hit {i}my{/i} sack{nw}"
        # Ow, my sack :( - Arc
    arceus "Yeah, that sounds like a good idea."
    n "The boys all get ready for a night's rest."

    scene black with dissolve
    pause 2.0
    cs "Hey, guys?"
    anno "Hmm?"
    cs "What if we {i}don't{/i} release the song tomorrow?"
    arceus "What? Are you crazy? We're doing so well."
    cs "That's what I'm saying. Let's release a whole EP! That way, we get more streams on the whole thing, and maybe we can even sell vinyls!"
    arceus "You and your vinyls."
    cs "I mean, come on, right? Our first gamble paid off, and now we have an audience. What do we have to lose?"
    anno "Yeah, we could."
    arceus "I guess I'm cool with that."
    cs "Let's do it, then! [band_name], here we go!"
    jump fired_ep_time

label fired_ep_time:
    stop music fadeout 3.0
    pause 1.0
    scene hotel_breakfast
    show anno at left
    show arceus at right
    show cs
    with dissolve

    cs "So, we're making a whole EP. What do we have to do?"
    anno "Well, Naming King, what were you thinking about calling it?"
    cs "Well, I had a dream last night."
    show arceus worried
    arceus "Oh no."
    cs "And I dreamt the name..."
    $ ep_name = renpy.input("What should we call the EP?", ep_name, length = 32)
    cs "[ep_name]!"
    anno "You know what, I like it."
    show arceus happy
    arceus "See, when you said \"I thought of it in a dream\", I thought it was going to suck."
    cs "Fair."
    cs "So, now we need to start putting some songs on this bad boy!"
    show arceus
    arceus "Well then, let's get to it, yeah? We already have {i}[song_name_1]{/i} and {i}[song_name_2]{/i}."
    anno "Well, I had an idea for one this time."
    cs "Oh? Hit us with it!"
    anno "Well, I know I want it to be about travelling the world, but I don't know what to say for some of the lines."
    cs "I can help fill them in!"
    if fun_value(FUN_VALUE_MUSIC):
        anno "Alright, awesome, here's the energetic rock song I've got..."
    else:
        anno "Alright, awesome, here's what I've got..."
    play music energetic_rock volume 0.5 if_changed
    music energetic_rock
    anno "{cps=15}{image=note_small1.png} I made my way over to Japan... {image=note_small2.png}"
    $ line_2 = renpy.input("What should the next line be?", "", length = 64)
    anno "Okay! How about..."
    anno "{cps=15}{image=note_small1.png} I found myself in the U.K... {image=note_small2.png}"
    $ line_3 = renpy.input("What should the next line be?", "", length = 64)
    anno "Nice, nice, how about..."
    anno "{cps=15}{image=note_small1.png} I'm gonna go party in Sweden... {image=note_small2.png}"
    $ line_4 = renpy.input("What should the next line be?", "", length = 64)
    anno "{cps=15}{image=note_small1.png} I'm globetrottin'! {image=note_small2.png}"
    cs "Hey, I like that! Sing it all the way through!"
    anno "Gotcha!"
    anno "{cps=15}{image=note_small1.png} I made my way over to Japan... {w=1.5}\n[line_2]{image=note_small2.png}"
    anno "{cps=15}{image=note_small1.png} I found myself in the U.K... {w=1.5}\n[line_3]{image=note_small2.png}"
    anno "{cps=15}{image=note_small1.png} I'm gonna go party in Sweden... {w=1.5}\n[line_4]{image=note_small2.png}"
    anno "{cps=15}{image=note_small1.png} I'm globetrottin'! {image=note_small2.png}"
    show arceus happy
    n "Arceus claps."
    cs "Well, I guess you want me to name this one, too?"
    anno "Go for it."
    show arceus
    $ song_name_3 = renpy.input("What should we call the song?", song_name_3, length = 32)
    anno "{i}[song_name_3]{/i} it is!"
    show cs happy
    cs "Woohoo! Three songs down!"
    show arceus happy
    stop music fadeout 3.0
    music end
    arceus "Dang, and all without leaving the breakfast table."
    anno "Now, that's efficency. I'll go back upstairs and polish this up."
    hide anno with moveoutleft
    n "Anno gets up from his seat and heads back to the room."
    cs "He's really been a huge help with all of this."
    show arceus worried
    arceus "Yeah, I kinda feel like I'm not pulling my weight."
    cs "What do you mean, you wrote {i}[song_name_2]!{/i}"
    show arceus
    arceus "True, true."
    cs "Listen, I'm just, like... the name guy. And part of me doesn't even feel like I'm coming up with {i}those{/i}. They just.. kinda come to me, man."
    arceus "Nah, dude, you wrote {i}[song_name_1]!{/i}"
    cs "I guess."
    arceus "We should head back upstairs with Anno. Maybe there is something we can do to help!"
    cs "Yeah, let's go see!"
    jump fired_back_to_room 

label fired_back_to_room:
    stop music fadeout 3.0
    scene hotel_room
    show anno
    with dissolve

    show cs at left
    show arceus flipped at right
    with moveinleft
    show arceus with determination

    n "Anno is concentrating deeply on his laptop."
    anno "Hey guys!"
    cs "Hey!"
    arceus "We were wondering, is there anything we can do to help?"
    anno "Hmm... well, I need help with this solo."
    arceus "Well, hey, I'm a percussionist. I can get a drum solo in there."
    anno "Yeah, lay one on me!"
    n "Anno plays the track, and Arceus taps out a killer drum line."
    anno "That's awesome, man!"
    show arceus happy
    arceus "Thank you, thank you."
    cs "What can I do?"
    anno "Well, you already named it {i}[song_name_3],{/i} and that's definitely our best title yet. You wrote, like, half the lines, too."
    anno "But, if you want to record backing vocals, this track might sound dope with them!"
    cs "Will do!"
    python:
        last_words = []
        for l in [line_2, line_3, line_4]:
            s = l.split(" ")
            last_words.append(s[-1])
    play music energetic_rock volume 0.5 if_changed
    music energetic_rock
    anno "Recording!"
    cs "{cps=15}...Japan!{w=1.5} ...[last_words[0]]!{w=1.5}\n{cps=15}...U.K.!{w=1.5} ...[last_words[1]]!{w=1.5}\n{cps=15}...Sweden!{w=1.5} ...[last_words[2]]!\n{w=1.5} ...globetrottin'~!"
    pause 1.0
    anno "You're clear! That was awesome!"
    cs "Thank you, thank you!"
    arceus "Is that us wrapped for the day?"
    anno "I think it is! I'll export this and save it as {i}[song_name_3]!{/i}"
    cs "Let's go!"
    n "Everyone high fives."
    stop music fadeout 3.0
    scene black with dissolve
    n "The gang goes to bed after another successful day."
    cs "{i}At this rate, we'll have this whole EP done by the end of the week!"
    n "CS smiles to himself, drifting off to sleep."

    pause 1.0
    jump fired_mcd

label fired_mcd:
    stop music fadeout 3.0

    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve

    anno "Well, you guys ready to write the next song?"
    cs "Ugh, I'm starving."
    arceus "That hotel breakfast just isn't doing it for me today."
    anno "Hmm... we have a little extra money from the first song's streams. Wanna go to, like, McDonald's?"
    n "CS perks up."
    cs "For sure."
    arceus "Well then, let's head out!"

    hide anno
    hide arceus
    hide cs
    with moveoutright

    scene mcdonalds_inside
    show anno at left
    show arceus at right
    show cs
    with dissolve
    play music fnaf_6 volume 0.5 if_changed
    music fnaf_6
    if fun_value(FUN_VALUE_MUSIC):
        n "CS and the gang race over to the minigame table in the McDonald's and eat their food."
    else:
        n "CS and the gang sit at a table in the McDonald's and eat their food."
    n "As they eat, they start talking about their next song."
    cs "Okay, I had this idea, but it's a bit out there."
    anno "Alright, let's hear it."
    $ renpy.music.set_pause(True, "music")
    play music2 france volume 0.5 if_changed
    music france
    if fun_value(FUN_VALUE_MUSIC):
        cs "{cps=15}{image=note_small1.png} I'M GONNA TAKE OVER THE GUILLOTINE WORLD.{w=1.0} I'M GONNA KILL GOD.{w=1.0} I CAN CONTORT REALITY TO MY WHIMS-- {image=note_small2.png}"
    else:
        cs "{cps=15}{image=note_small1.png} I'M GONNA TAKE OVER THE WORLD.{w=1.0} I'M GONNA KILL GOD.{w=1.0} I CAN CONTORT REALITY TO MY WHIMS-- {image=note_small2.png}"
    stop music2
    music end
    $ renpy.music.set_pause(False, "music")
    anno "Wait, what the fuck, hold on--"
    n "Arceus looks visibly concerned."
    show arceus worried
    arceus "That might be a little bit much."
    n "Arceus texts someone under the table."
    cs "Yeah, I was worried about that."
    cs "Okay, okay, I have a different idea."
    anno "Yeah...?"
    cs "Well, I don't have all the lyrics yet..."
    show arceus
    if fun_value(FUN_VALUE_MUSIC):
        arceus "Maybe this time, {i}we{/i} can take over the Dragon Castle!"
    else:
        arceus "Maybe this time, {i}we{/i} can fill in the lines!"
    cs "Okay! Here's what I have so far..."
    $ renpy.music.set_pause(True, "music")
    play music2 dragon_castle volume 0.5 if_changed
    music dragon_castle
    cs "{cps=15}{image=note_small1.png} Through all adversity, we'll bind together and overcome... {image=note_small2.png}"
    arceus "Ooh, I got something..."
    $ line_5 = renpy.input("What should the next line be?", "", length = 64)
    arceus "{cps=15}{image=note_small1.png} [line_5] {image=note_small2.png}"
    cs "Nice! How about..."
    cs "{cps=15}{image=note_small1.png} With my friends beside there's no foe we can not fight... {image=note_small2.png}"
    anno "Let me take this one."
    $ line_6 = renpy.input("What should the next line be?", "", length = 64)
    anno "{cps=15}{image=note_small1.png} [line_6] {image=note_small2.png}"
    cs "Heck yeah! And then I think we should have a solo like..."
    cs "{cps=15}{image=note1.png}{image=note4.png}{image=note3.png}{image=note1.png}{image=note5.png}{image=note1.png}{image=note2.png}{image=note1.png}{image=note2.png}{image=note2.png}{image=note4.png}{image=note4.png}{image=note3.png}{image=note3.png}{image=note5.png}{image=note5.png}{image=note1.png}{image=note1.png}{nw}"
    arceus "Woah, how are you doing that with your mouth?"
    cs "What, like..."
    cs "{cps=10}{image=note1.png}{image=note2.png}{image=note3.png}{image=note4.png}{image=note5.png}"
    cs "Honestly, I have no idea."
    stop music2 fadeout 3.0
    music end
    $ renpy.music.set_pause(False, "music")
    show customer at mid_left with moveinleft
    customer "Hey, that sounds really good!"
    show cs flipped
    cs "Huh?"
    customer "Yeah, I heard you guys making that song from my table, it's really good!"
    anno "Thanks! We're actually putting out an EP soon!"
    customer "Well, I definitely wanna hear that song again. What's it called?"
    cs "Uh..."
    $ song_name_4 = renpy.input("What should the song be called?", song_name_4, length = 32)
    cs "It's called {i}[song_name_4]!{/i}"
    anno "It'll be on our EP {i}[ep_name],{/i} just look up [band_name] on streaming services!"
    customer "Awesome, I'm excited! I'll make sure to check it out!"
    n "The customer walks away."
    hide customer with moveoutright
    show cs happy
    cs "People are really liking our stuff."
    show arceus happy
    arceus "This is going better than I ever dared to hope."
    anno "Let's go back to the hotel and get this song made!"
    n "On their way out of the store, CS turns to Arceus."
    cs "You know, I think {i}[song_name_4]{/i} might be our best one yet."
    stop music fadeout 3.0
    music end    
    scene black with dissolve
    jump fired_hotel_lobby_2

label fired_hotel_lobby_2:
    stop music fadeout 3.0

    scene hotel_lobby    
    show anno at left
    show arceus flipped
    show cs at mid_mid_left
    with dissolve
    play music gold_room volume 0.5 if_changed
    music gold_room
    if fun_value(FUN_VALUE_MUSIC):
        n "As they walk through the gold room to their ball, they hum their newest song to themselves."
    else:
        n "As they walk through the hotel lobby to their room, they hum their newest song to themselves."
    cs "{cps=15}{image=note_small1.png} {i}[line_5]{/i} {image=note_small2.png}"
    n "Someone in the lobby overhears them singing the song and runs up to them."
    show guest at right with moveinright
    guest "Holy shit, are you from [band_name]?!"
    cs "Uh..."
    guest "You {i}are!{/i} Holy shit!"
    guest "You guys are {i}cracked{/i} at making music! You're like {i}GOATed!{/i}"
    # DX: fun value "GOATed with the swows" - Tate/Digi
    cs "What? What does that--"
    n "A crowd starts to form around them."
    guest "You're a rizz god! You're off the sauce at this shit!"
    anno "We've released one song."
    guest "I'm, like, the biggest stan of you guys! You guys {i}gotta{/i} perform."
    arceus "Perform?"
    guest "You gotta, like, give us a sneak peak of your new EP!"
    anno "{i}How did he know we're releasing a new EP{/i}"
    guest "Come on! You {i}gotta!{/i} You'll pop off on TikTok."
    cs "Uh, sure? I guess?"
    n "The crowd cheers."
    stop music fadeout 3.0
    music end    
    cs "Alright, well, here's our song..."
    n "CS turns to the others to cue them."
    cs "{i}[song_name_2]!{/i}"
    n "Anno starts up the backing track, and Arceus grabs some random objects to use as a drum kit."
    play music happy_rock volume 0.5 if_changed
    music happy_rock
    cs "{cps=15}{image=note_small1.png} We're going down to Vegas, we're gonna strike it rich!{w=1.5}\nWe're going down to Vegas, [line_1] {image=note_small2.png}"
    n "The crowd cheers wildly."
    anno "We're [band_name]! Check out {i}[ep_name]{/i} on streaming services soon!"
    stop music fadeout 3.0
    n "The gang heads up to their room."
    jump fired_song_5

label fired_song_5:
    stop music fadeout 3.0
    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve

    anno "This is the last song on the EP. We need to go big with this one."
    show arceus worried
    arceus "I'm nervous to write this one. We really need to end on a banger."
    anno "Something victorious, something inspiring."
    show arceus
    arceus "Hmmm..."
    anno "CS, why don't you write this one?"
    cs "Me?"
    anno "Yeah!"
    cs "But, I wrote all the other songs!"
    anno "Nah, you filled in our blanks."
    arceus "Yeah, why don't you write the whole thing this time!"
    cs "Oh, gosh, you guys sure?"
    if fun_value(FUN_VALUE_MUSIC):
        anno "Yeah, go ahead! Here, I'll give you a sweet victory..."
    else:
        anno "Yeah, go ahead! Here, I'll give you a beat..."
    play music sweet_victory volume 0.5 if_changed
    music sweet_victory
    n "Anno plays an upbeat song on his laptop."
    $ line_7 = renpy.input("Write a line! (1/4)", "", length = 64)
    $ line_8 = renpy.input("Write a line! (2/4)", "", length = 64)
    $ line_9 = renpy.input("Write a line! (3/4)", "", length = 64)
    $ line_10 = renpy.input("Write a line! (4/4)", "", length = 64)
    cs "I think I have something! Here it is..."
    cs "{cps=15}{image=note_small1.png} [line_7]{w=1.5}\n[line_8]{w=1.5}\n[line_9]{w=1.5}\n[line_10] {image=note_small2.png}"
    arceus "Yo?!"
    anno "That's perfect! Give it a name!"
    # Yeah, give it name, Digi <3
    $ song_name_5 = renpy.input("What should the song be called?", song_name_5, length = 32)
    cs "It's called {i}[song_name_5]!{/i}"
    show arceus happy
    arceus "That's going to be a huge hit."
    anno "So, wait, that's {i}[ep_name]{/i} done, then!"
    cs "Woohoo!"
    n "They all high five."
    anno "I guess I'll get this mastered and release it tonight!"
    cs "[band_name] forever!"
    stop music fadeout 3.0
    music end 
    arceus "You know, I'm starting to really believe in this whole thing."
    $ achievement_manager.unlock("indie_artist")
    jump fired_fan_interaction

label fired_fan_interaction:
    stop music fadeout 3.0
    scene black with dissolve
    n "The next day, in the early morning, they hear a knock on their hotel room door."
    scene hotel_door with dissolve
    play music dig_this volume 0.5 if_changed
    music dig_this
    if fun_value(FUN_VALUE_MUSIC):
        cs "Huh? Who the fuck digs this on a hotel door, especially at this hour?"
    else:
        cs "Huh? Who the fuck knocks on a hotel door, especially at this hour?"
    show cs angry at left with moveinleft
    cs "Hello?"
    show mean surprised flipped at right with moveinright
    mean "Holy fuck, it's CS!"
    cs "Huh? Are you, like, a fan?"
    show mean flipped
    mean "Yes! Of your music!"
    n "CS, for a moment, forgets he just spent a week making an EP."
    cs "My... music? Oh, yeah, right, [band_name]!"
    cs "Wait, how did you find my hotel room?"
    show mean happy flipped
    mean "You should go on tour!"
    cs "What?"
    n "CS is still half asleep."
    show mean happy2 flipped
    mean "Go on tour! I'm from Ontario."
    cs "Oh... kay?"
    mean "Bye!"
    hide mean with moveoutright
    n "CS closes the door."
    show cs flipped 
    cs "Anno?"
    n "Anno wakes up, but just barely."
    anno "Huh?"
    cs "I need you to check the numbers, quick."
    anno "The numbers? On {i}[ep_name]?{/i} Uh..."
    n "Anno pulls out his phone."
    n "Anno drops his phone."
    anno "Guys... we might have more money than we thought."

    scene hotel_room
    show anno at left
    show arceus at right
    show cs 
    with dissolve

    n "The gang regroups to discuss."
    cs "Okay, give it to me straight. How many sales of the EP?"
    anno "57,685."
    cs "Holy shit, that's a lot of sales, how much money--{nw}"
    anno "57,688."
    cs "Okay, yeah, I got that, how much money does that equate to--{w=0.5}{nw}"
    anno "57,692...{w=1.0}{nw}"
    cs "Stop refreshing the page!"
    anno "Sorry."
    cs "How much money is that?"
    anno "About $15,000."
    cs "Oh, my God!"
    arceus "Well, we're going to need to file taxes on it."
    anno "Do we?"
    show arceus angry
    arceus "You wanna go back to prison?"
    anno "No..."
    show arceus
    arceus "Well, then."
    cs "We need to figure this out. We at least have enough money to get out of this hotel room."
    arceus "And more."
    cs "And more, but we've gotta be careful. We don't wanna blow it or spend more than we can pay the taxes on."
    anno "For sure."
    cs "How are we going to figure out how to--"
    n "Anno gets an email."
    anno "Wait, hold on, let me read this, it looks important."
    howie "{b}Tour Offer{/b}\nHey, [band_name]!\nMy name is Howie Mandell, and I'm a talent agent and tour manager."
    cs "Woah, really?"
    howie "I'm emailing to inquire about whether you'd be interested in touring the country with your band. Your latest EP, {i}[ep_name],{/i} has been making big waves on streaming services."
    howie "I think live performances might be just what you need to take the next step."
    anno "Oh, my God!"
    howie "If you're willing to negotiate, I think we could strike a very mutually beneficial deal."
    show arceus happy
    arceus "That sounds amazing!"
    howie "Please get in touch as soon as you can,\n-- Howie Mandell"
    cs "We have to accept, right?"
    arceus "Our last two gambles paid off. May as well go all the way."
    anno "We can't pass this up. I'll email him back."
    cs "[band_name] is going on tour!"
    stop music fadeout 3.0
    music end    
    jump fired_howie

label fired_howie:
    stop music fadeout 3.0
    scene black with dissolve
    n "After a few hours, the band meets Howie downstairs in the lobby."
    scene hotel_lobby
    show anno
    show cs flipped at mid_right
    show arceus at right
    with dissolve
    play music gold_room volume 0.5 if_changed
    music gold_room
    n "Howie walks into the lobby."
    show howie flipped at left with moveinleft
    howie "You guys ready?"
    cs "Ready for what?"
    howie "A ride in a limousine!"
    n "The group is in shock."
    anno "Already? We haven't even struck a deal!"
    howie "Ah, you will, I trust in that... but, until then, why don't I treat you all to the ride of a lifetime?"
    stop music fadeout 3.0
    n "CS, Anno, and Arceus follow Howie to the limo parked out front."
    show howie with determination
    hide cs
    hide anno
    hide arceus
    hide howie
    with moveoutleft
    jump fired_limo_time

label fired_limo_time:
    scene in_limo
    show arceus happy flipped
    show cs happy at mid_mid_left
    show anno at left behind cs
    with dissolve
    play music exotic volume 0.5 if_changed
    music exotic
    if fun_value(FUN_VALUE_MUSIC):
        arceus "These snacks are exotic!"
    else:
        arceus "These snacks are amazing!"
    anno "This music's awesome!"
    cs "These seats sure are comfy!"
    howie "Alright, boys, enough chat, let's talk business."
    howie "I want to take you guys on tour."
    show cs worried
    show arceus flipped
    cs "Already?!"
    howie "Oh yeah, baby, already. {i}[ep_name]{/i} made [band_name] big overnight. This kind of success comes once in a lifetime, and it's in {i}your{/i} lifetime, and it's {i}right now!{/i}"
    anno "Woah, woah, woah, slow down. Why are you so invested in our success?"
    howie "Oh, don't think I'm going to get a raw deal here. I know how to make sure we all end up happy."
    show arceus angry flipped
    arceus "You sure you mean {i}all{/i} of us?"
    howie "I sense you're spooked so I'll give ya the rub. We take you on tour. Every ticket you sell, I get a cut, you get a cut, we all go home snuggling our cash."
    cs "You snuggle your cash?"
    howie "Better than lavender, baby."
    show arceus flipped
    show cs
    anno "So what's the plan? How do we get venues? Do we even have a way to promote?"
    howie "Leave all the fiddly buisness to me. You guys just get on stage and sing like, {i}[song_name_3],{/i} or whatever."
    howie "How's that song go?\n{image=note_small1.png} {i}I made my way over to Japan, [line_3]?{/i} {image=note_small2.png}"
    show arceus angry flipped
    arceus "No, that's not--{w=0.5}{nw}"
    howie "Anywho, do we have a deal?"
    anno "I want to see whatever contract you're having us sign, first."
    howie "Smart man, smart man. Here it is."
    n "Howie hands Anno the contract."
    stop music fadeout 3.0
    music end    

    scene black with dissolve
    n "As Anno reads over the contract, CS, Arceus, and Howie talk more about the deal."
    menu:
        "Should they take the deal?"
        "Yes"  (type = "good"):
            jump fired_signed_the_contract
        "No"  (type = "bad"):
            jump fired_no_contract
            
label fired_no_contract:
    $ ending_manager.mark("threw_away_fame")
    bad_end "Well,\nthat was kinda dumb!" "fired_limo_time"

label fired_signed_the_contract:
    stop music fadeout 3.0
    scene black
    n "After some time, Anno signs the contract, and they all return to the hotel."

    scene hotel_lobby    
    show anno at left
    show arceus flipped
    show cs at mid_mid_left
    show howie at right
    with dissolve
    play music gold_room volume 0.5 if_changed
    music gold_room
    howie "Well, your first stop is Vancouver."
    cs "Vancouver? Where are we playing?"
    n "Howie reads from his iPad."
    howie "Looks like something called LTX? Linus Tech Expo?"
    show cs worried
    cs "Wait, Linus--"
    howie "See you bright and early tomorrow! We're taking a tour bus!"

    hide howie with moveoutright
    show cs at center
    show arceus at right
    with move
    stop music fadeout 3.0
    cs "Linus..."
    anno "Don't be worried. Maybe he won't even recognize you."
    arceus "Yeah, he'll be busy running the expo."
    cs "Man, I don't know... We didn't end on great terms..."
    arceus "Let's just get a good night's sleep. If we need to be up that early, I need to get some shuteye."
    cs "Okay..."

    scene black with dissolve
    n "The gang heads upstairs to bed, but CS struggles to sleep well."
    cs "{i}Man, I'm worried about seeing Linus again. What if he just throws all of us out because he doesn't want to see me?"
    cs "{i}The fate of [band_name] could rest in some dumb shit I did in the past."
    cs "{i}Not even the past, like, week or two ago."
    cs "{i}Ugh, I can't sleep like this. I need a drink."
    n "CS gets out of bed and takes a walk around the halls."

    scene hotel_hall
    show cs at left with moveinleft
    cs "Maybe a cold drink will clear my head."
    play music another_him volume 0.5 if_changed
    music another_him
    show csgod at right with dissolve
    csgod "Or I can."
    show cs surprised
    cs "Ah!"
    show cs
    if fun_value(FUN_VALUE_MUSIC):
        csgod "I would not fret about another, especially him."
    else:
        csgod "I would not fret about Linus."
    cs "How- how did you--"
    csgod "What you did was your best. Good men will realize that. His anger will have been brief, despite his rash actions."
    cs "How do you know all this?"
    csgod "That is not important. What {i}is{/i} important is your mind being prepared for the day ahead."
    csgod "You will go to bed, you will rest, and you will do your best, as you have."
    cs "Th- thank you... what do I call you?"
    csgod "You can call me...{w=1.5} !!!"
    hide csgod with dissolve
    stop music fadeout 3.0
    music end    
    show janitor at right with moveinright
    janitor "You alright, man? Who are you talking to?"
    cs "N-no one. Just heading to bed."
    show cs flipped
    hide cs with moveoutleft
    janitor "Weird guy."
    jump fired_first_tour_day

label fired_first_tour_day:
    stop music fadeout 3.0
    scene black with dissolve
    n "CS heads to bed. The next morning, the [band_name] crew gets ready for their first tour day."

    scene hotel_room
    show anno at left
    show arceus at right
    with dissolve

    show cs with moveinleft
    anno "Feeling better?"
    cs "Much."
    arceus "What changed?"
    cs "Eh, something... something got into my head and cleared things up for me."
    arceus "Alrighty, man, well, let's hope it did a good job, because it's time to hit the road."

    show arceus flipped with determination
    hide arceus
    hide cs
    hide anno
    with moveoutright

    scene hotel_lobby with dissolve
    show anno at left
    show arceus flipped
    show cs at mid_mid_left
    with moveinleft
    play music gold_room volume 0.5 if_changed
    music gold_room
    show howie at right with moveinright
    howie "You boys ready to go?"
    cs "Ready as we'll ever be."
    howie "Well, then! It's showtime!"
    stop music fadeout 3.0
    scene black with dissolve
    scene ltx with dissolve
    show anno at left
    show arceus flipped
    show cs at mid_mid_left
    with moveinleft

    n "They all arrive at LTX."
    cs "Well, it's pretty busy. I doubt we'll run into--"
    show linus at right with moveinright
    play music passport volume 0.5 if_changed
    music passport
    linus "Oh good, you guys are finally here. You're [band_name], right?"
    linus "Luke told me about you guys, and I listened to {i}[ep_name]{/i} last night... I really liked, uh, which one was it, {i}[song_name_4]?{/i}"
    linus "Anywho, I...{w=1.0} wait, CS?!"
    cs "Uh, hi?"
    linus "Wait, you... {i}you're{/i} the lead singer in [band_name]?!"
    cs "Looks like it..."
    linus "Well, I'll say this, you're better at singing than you are editing LTT videos."
    show cs worried
    n "CS looks worried."
    n "Linus chuckles."
    linus "Listen, don't worry about it."
    show cs surprised
    cs "Really?"
    linus "Yeah, I was too hard on you. Maybe too quick to fire you, too, though it looks like you're in a better position than I could have offered you."
    show cs happy
    cs "Well, thanks for the apology."
    linus "Yeah, you deserve it. Honestly, when the public learned who was editing that video, and that we axed you, they were pretty upset."
    cs "How about this, when I get out of this mess, you let me edit a guest video, and I'll make a video saying we parted ways amicably."
    linus "Now, that's a deal I'll take."
    linus "Now, get on stage and rock the house!"
    stop music fadeout 3.0
    scene ltx_stage
    show anno at left
    show arceus at right
    show cs
    with dissolve
    n "The crowd is going insane."
    cs "We're [band_name], and this is {i}[song_name_4]!{/i}"
    play sound sfx_start_rocking
    play sound sfx_cheer
    n "The crowd roars louder."
    play music dragon_castle volume 0.5 if_changed
    music dragon_castle
    cs "{cps=15}{image=note_small1.png} Through all adversity, we'll bind together and overcome! {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} [line_5] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} With my friends beside there's no foe we can not fight! {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} [line_6] {image=note_small2.png}"
    n "Anno plays an epic guitar solo."
    stop music fadeout 3.0
    play sound sfx_cheer
    pause 2.0
    scene black with Dissolve(3.0)

    scene ltx
    show anno at left
    show arceus flipped
    show cs at mid_mid_left
    show linus at right
    with dissolve
    play music passport volume 0.5 if_changed
    music passport
    linus "You guys were incredible! That was my favorite song of yours, too."
    show cs happy
    cs "Thank you so much!"
    linus "Well, I'll transfer the money to your agent."
    cs "Sounds good!"
    linus "Well, thank you, CS. I'm glad we could bury whatever hatchet we had."
    cs "Absolutely."
    hide linus with moveoutright
    stop music fadeout 3.0
    show cs at center
    show arceus at right
    with move

    arceus "We did it! That was amazing!"
    anno "Hell yeah!"
    cs "We rocked!"
    arceus "Welp, back on the bus to recoup and see how much we earned!"

    show arceus flipped with determination
    hide cs
    hide arceus
    hide anno
    with moveoutright

    scene tour_bus_inside
    show anno at left
    show arceus flipped at mid_right
    show cs at center
    with dissolve
    play music exotic volume 0.5 if_changed
    music exotic
    show howie at offscreenleft with moveinright
    pause 1.0
    show howie flipped at right behind arceus with move
    show howie at right behind arceus

    howie "Boys!"
    n "The team turns to face Howie."
    howie "You really rocked out there! Playing Linus' favorite song, that was a clutch move."
    cs "How much did we make?"
    howie "Five."
    arceus "Five?!"
    howie "Thousand."
    anno "Holy shit, already? With that kinda cashflow, we could--"
    howie "Woah, woah, woah, hold your horses, kid."
    anno "Hold my horses...?"
    howie "That's without me taking my cut, or you three splitting it. We've still got more shows to do, you know!"
    cs "Well, then, let's get this show on the road!"
    stop music fadeout 3.0
    scene black with dissolve
    jump fired_second_tour_day

label fired_second_tour_day:
    n "The group rests while on their way to their next venue."
    
    scene tour_bus_inside
    show anno at left
    show arceus at right
    show cs at center
    with dissolve
    play music exotic volume 0.5 if_changed
    music exotic
    n "CS shouts up to the front."
    cs "Where are we heading?!"
    howie "Manitoba! We'll stop in Winnipeg, so you guys can grab some stuff if you need it."
    cs "Yeah, I might head into the city. What about you guys?"
    anno "Nah, I'm good."
    arceus "Yeah, I'm just gonna chill here."
    cs "Alrighty, then!"
    stop music fadeout 3.0
    scene black with dissolve
    n "After they pull into the city, CS gets out and walks the streets."

    scene manitoba_street
    with dissolve
    show cs with moveinleft
    play music track_4 volume 0.4 if_changed
    music track_4
    cs "What a place. Way better than the places I've been lately."
    cs "And everyone's so friendly!"
    show border_guard at right with moveinright
    border_guard "Pardon me, eh!"
    hide border_guard with moveoutleft
    cs "Ooh, a shoe store!"
    cs "If I'm going to be on stage, I need some better kicks."

    scene shoe_store
    show ges at right with moveinright
    with dissolve
    show cs at left with moveinleft
    if fun_value(FUN_VALUE_EPIC):
        ges "Welcome to the sho-- woah, are you CS, eh?"
        cs "Yeah, how'd you know?"
        ges "Aren't you touring with [band_name] right now, eh?"
        cs "Yeah, I am!"
        ges "Dude, I've been listening to {i}[song_name_3]{/i} all day, eh?"
        ges "{cps=15}{image=note_small1.png} I found myself in the U.K...{w=1.5}\n[line_3] {image=note_small2.png}, eh?"
        ges "That shit slaps, eh?"
        cs "Well, thanks! I was wondering if you had some nice shoes for my concert tonight."
        ges "Oh, man, I've got just the thing, eh?"
        hide ges with moveoutright
        n "Ges searches through stock in the back."
        n "He returns with a box."
        show ges at right with moveinright
        ges "These are called the {i}Gessler Step,{/i} eh?"
        cs "The Gessler Step?"
        ges "The finest shoes I've got, and I personally recommend them. You'll love 'em or my name isn't Ges! And it is, eh?"
        cs "Wait, did you make these shoes?"
        ges "Nah, just kind of a coincidence, eh?"
        cs "Oh, okay."
        n "CS tries on the shoes."
        cs "These are awesome!"
        cs "Wait, how did you know my size?"
        ges "It's online, eh?"
        cs "Wait, it's what--{w=0.5}{nw}"
        ges "That'll be $88.88, if you want 'em, eh?"
        cs "I'll take them!"
    else:
        ges "Welcome to the sho-- woah, are you CS?"
        cs "Yeah, how'd you know?"
        ges "Aren't you touring with [band_name] right now?"
        cs "Yeah, I am!"
        ges "Dude, I've been listening to {i}[song_name_3]{/i} all day!"
        ges "{cps=15}{image=note_small1.png} I found myself in the U.K...{w=1.5}\n[line_3] {image=note_small2.png}"
        ges "That shit slaps!"
        cs "Well, thanks! I was wondering if you had some nice shoes for my concert tonight."
        ges "Oh, man, I've got just the thing."
        hide ges with moveoutright
        n "Ges searches through stock in the back."
        n "He returns with a box."
        show ges at right with moveinright
        ges "These are called the {i}Gessler Step!"
        cs "The Gessler Step?"
        ges "The finest shoes I've got, and I personally recommend them. You'll love 'em or my name isn't Ges! And it is."
        cs "Wait, did you make these shoes?"
        ges "Nah, just kind of a coincidence."
        cs "Oh, okay."
        n "CS tries on the shoes."
        cs "These are awesome!"
        cs "Wait, how did you know my size?"
        ges "It's online."
        cs "Wait, it's what--{w=0.5}{nw}"
        ges "That'll be $88.88, if you want 'em!"
        cs "I'll take them!"
    stop music fadeout 3.0
    music end
    n "CS checks out and heads back to the tour bus."

    scene tour_bus_inside
    show anno at left
    show arceus flipped
    with dissolve
    play music exotic volume 0.5 if_changed
    music exotic
    show cs flipped at right with moveinright
    anno "Hey, CS!"
    arceus "Dang, nice shoes!"
    cs "Thanks! Are you guys ready to perform tonight?"
    show arceus happy
    arceus "Heck yeah!"
    anno "Of course."
    cs "I think we should sing {i}[song_name_3]{/i} tonight."
    show arceus
    arceus "Why is that?"
    cs "I just think it'll make someone pretty happy."
    anno "Sounds good to me!"
    stop music fadeout 3.0
    scene convention_center_entrance
    show anno at left
    show cs at mid_mid_left
    show arceus
    with dissolve

    n "A crowd can be heard cheering for the previous act."
    show nova at right with moveinright
    show arceus flipped
    nova "Easy gig tonight, you guys are gonna knock it out of the--{w=0.5} CS?"
    cs "Nova? What are you doing here?"
    nova "I live close by. I was DJing as the opening act..."
    nova "Wait, let me check something."
    n "Nova looks at a piece of paper."
    nova "Opening for... [band_name]? Is that you guys?"
    cs "Yep!"
    nova "No shit, I've been listening to {i}[ep_name]{/i} on Spoofy a ton this week!"
    nova "I didn't know it was you!"
    cs "Well, us."
    n "CS gestures to the others."
    nova "Of course! Well, you guys go clean up out there."
    show arceus happy
    arceus "Will do!"
    
    hide nova with moveoutright
    cs "Well, let's go out there and show them what we're made of!"

    scene stage2
    show anno at left
    show arceus at right
    show cs
    with dissolve

    cs "I know you all just watched an amazing performance by Nova, and that's going to be a tough act to follow..."
    cs "But who wants to hear {i}[song_name_3]?!{/i}"
    play sound sfx_start_rocking
    play sound sfx_cheer
    n "The crowd is exploding."
    # Fun value, add explosion sounds - Arc
    # OK - Digi
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        play sound sfx_explosion
    play music energetic_rock volume 0.5 if_changed
    music energetic_rock
    cs "{cps=15}{image=note_small1.png} I made my way over to Japan...{w=1.5}\n[line_2] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} I found myself in the U.K...{w=1.5}\n[line_3] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} I'm gonna go party in Sweden...{w=1.5}\n[line_4] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} I'm globetrottin'! {image=note_small2.png}"
    stop music fadeout 3.0
    play sound sfx_cheer
    n "The crowd is applauding wildly."
    cs "We're [band_name]!"
    n "The audience is loving it."

    scene black with dissolve
    jump fired_third_tour_day

label fired_third_tour_day:
    scene tour_bus_inside
    show anno at left
    show arceus at right
    show cs
    with dissolve
    play music exotic volume 0.5 if_changed
    music exotic
    n "Howie hollers from the front of the bus."
    howie "Alright, boys, it's your last performance!"
    cs "Where are we headed?"
    howie "Ontario!"
    cs "Ontario? That's where that one fan was from!"
    howie "Well, he's about to be a happy camper!"
    anno "I can't believe we're already on our last tour day!"
    $ line_num = renpy.get_filename_line()[1] + 1
    arceus "Well, it's been [line_num] lines, it's been a while."
    anno "We're going to really have to go big for this one. I think it's our biggest audience yet."
    cs "We'll put on a show like they've never seen before!"

    stop music fadeout 3.0
    scene convention_center_lobby
    with dissolve
    show anno at left
    show arceus at mid_mid_right
    show cs at mid_mid_left
    with moveinleft

    cs "Alright, well, let's get prepared. We have way more songs to do tonight--{nw}"
    show mean surprised flipped at right with moveinright
    mean "{i}Holy shit, it's you!"
    cs "Wait, are you that fan from my hotel?"
    show mean flipped
    mean "{i}You actually made it to Ontario?!"
    cs "Uh... yeah, totally because you asked me to!"
    show cs worried
    show mean happy at mid_mid_left
    with MoveTransition(0.25)
    show cs worried with hpunch
    n "Mean tackle-hugs CS."
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        cs "Ow."
    
    show mean at right with move
    mean "Thank you so much! I know you guys will do amazing."
    hide mean with moveoutright
    cs "Let's go make our fans proud."

    scene big_stage
    show anno at left
    show arceus at right
    show cs
    with dissolve

    cs "For our special performance tonight, we'll be singing every song off our album, {i}[ep_name]!{/i}"
    n "The crowd is going wild."
    cs "First up, it's {i}[song_name_1]!{/i}"
    play sound sfx_start_rocking
    n "The audience cheers."
    play sound sfx_cheer2
    play music everlong volume 0.5 if_changed
    music everlong
    cs "{cps=15}{image=note_small1.png} We broke the chains, now we're free to fly,{w=1.5}\nEscaped concrete, and now we see blue skies{w=1.5}\nBecome brand new, we'll leave the past behind,{w=1.5}\nPrisoners no more, 'cause a new life we'll find {image=note_small2.png}"
    n "The crowd is loving this!"
    stop music fadeout 3.0
    cs "Who wants to hear {i}[song_name_2]?!{/i}"
    play sound sfx_start_rocking
    n "The crowd responds with further excitement."
    play sound sfx_cheer2
    play music happy_rock volume 0.5 if_changed
    music happy_rock
    cs "{cps=15}{image=note_small1.png} We're going down to Vegas,{w=1.5} we're gonna strike it rich!{w=1.5}\nWe're going down to Vegas,{w=1.5} [line_1]! {image=note_small2.png}"
    n "The fans are adoring this."
    stop music fadeout 3.0

    cs "Next up, here's a classic: {i}[song_name_3]!{/i}"
    anno "CS, none of our songs are classics. We're a new band."
    play sound sfx_start_rocking
    n "The crowd laughs."
    play music energetic_rock volume 0.5 if_changed
    music energetic_rock
    cs "{cps=15}{image=note_small1.png} I made my way over to Japan...{w=1.5}\n[line_2] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} I found myself in the U.K...{w=1.5}\n[line_3] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} I'm gonna go party in Sweden...{w=1.5}\n[line_4] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} I'm globetrottin'!{image=note_small2.png}"
    n "The audience loves this a lot."
    stop music fadeout 3.0
    cs "Alright, here's a fan favorite: {i}[song_name_4]!{/i}"
    play sound sfx_start_rocking
    play sound sfx_cheer2
    play music dragon_castle volume 0.5 if_changed
    music dragon_castle
    cs "{cps=15}{image=note_small1.png} Through all adversity, we'll bind together and overcome! {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} [line_5] {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} With my friends beside there's no foe we can not fight! {image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png} [line_6] {image=note_small2.png}"
    n "Anno shreds an epic solo."
    n "The fans are exploding!"
    stop music fadeout 3.0
    cs "And now! For the first time on stage! It's {i}[song_name_5]!{/i}"
    play sound sfx_start_rocking
    play sound sfx_cheer2
    n "The crowd is ready to burst."
    play music sweet_victory volume 0.5 if_changed
    music sweet_victory
    cs "{cps=15}{image=note_small1.png} [line_7]{w=1.5}\n[line_8]{w=1.5}\n[line_9]{w=1.5}\n[line_10] {image=note_small2.png}"
    n "The audience can't get enough!"
    stop music fadeout 3.0
    crowd "Encore! {w=0.5}Encore! {w=0.5}Encore! {w=0.5}"
    n "CS whispers to the others."
    cs "Encore? But, we don't have any more songs..."
    arceus "Make something up!"
    n "CS shouts to the crowd."
    cs "Uh... hey, you guys! Give me a word!"
    if fun_value(FUN_VALUE_COMMON):
        crowd "Orange! {w=0.5}Monkey! {w=0.5}Eagle!"
        show cs concentrate
        n "CS desperately tries not to think about those words."
        show cs disappointed
        cs "Can we try... three different words?"
        show cs
    crowd "Banana! {w=0.5}Street! {w=0.5}Ice!"
    cs "Uh..."
    menu:
        "What should the song be about?"
        "Banana":
            $ line_11 = "When I see you, I think about bananas"
        "Street":
            $ line_11 = "When I see you walking down the street"
        "Ice":
            $ line_11 = "Everybody knows I'm cool as ice"

    cs "Okay!"
    play sound sfx_start_rocking
    cs "{cps=15}{image=note_small1.png} [line_11] {image=note_small2.png}"
    $ line_12 = renpy.input("What's the next line?", length = 64)
    cs "{cps=15}{image=note_small1.png} [line_12] {image=note_small2.png}"

    cs "Thank you! We're [band_name], and thank you for listening to {i}[ep_name]!{/i}"
    play sound sfx_cheer2
    n "The crowd is overjoyed."

    show cs flipped with determination
    hide cs
    hide anno
    hide arceus
    with moveoutleft

    scene black with Dissolve(3.0)
    # Line 1200, give it up for line 1200
    # Line 1388, give it up for line 1388
    jump fired_final_tour_bus

label fired_final_tour_bus:
    scene tour_bus_inside
    show anno at left
    show arceus at right
    show cs
    with dissolve
    play music exotic volume 0.5 if_changed
    music exotic
    n "The boys are exhausted."
    show howie at offscreenright
    show anno at left

    show cs at mid_mid_left
    show arceus flipped at center
    with move
    show howie at right with moveinright

    howie "Well, gang, that was the last stop! You did amazing out there."
    cs "I'm beat."
    anno "I'm so tired..."
    arceus "I need a nap."
    howie "Well, maybe this will perk you guys up. Wanna hear the final total?"
    cs "Sure, what is it?"
    howie "Well, after all the cuts, and then splitting it... {w=0.5}each of you gets..."
    howie "$10,000!"
    n "The gang perks up."
    cs "Wait... $10K?!"
    n "Arceus nudges CS."
    arceus "You can go home!"
    show cs disappointed
    stop music fadeout 3.0
    n "CS looks forlorn."
    arceus "What's wrong?"
    cs "Well, I've been really enjoying this, actually."
    cs "I'm not sure I wanna go home."
    anno "Nah, don't act like that. This doesn't mean [band_name] is over!"
    arceus "Yeah, we can still make music together, but you need to get back to your normal routine for a bit."
    anno "Yeah, reset your head a bit."
    show cs
    cs "Yeah, you're right. And, hey, maybe we can write {i}[ep_name] 2{/i} some day!"
    arceus "Maybe we shouldn't name it {i}[ep_name] 2.{/i}"
    cs "Yeah."
    howie "Want me to point this bus towards Casa de CS?"
    cs "You know what, yeah, let's do it."
    show arceus happy
    arceus "Let's get you home, buddy."

    scene black with dissolve
    scene cs_house with dissolve
    play music park_theme volume 0.5 if_changed
    music park_theme
    n "CS steps off the tour bus."
    show cs at right with moveinleft
    cs "Ah, home sweet home."
    n "The others join him outside."
    show cs flipped with determination
    show anno at mid_left
    show arceus flipped at center
    with moveinleft
    arceus "Well, you should get some rest. It's been a wild few weeks for you."
    cs "It's been a wild few {i}years{/i} for you."
    arceus "Fair enough."
    anno "Yeah, we need to get back to our places, too. Figure out how to reintegrate."
    show howie flipped at left with moveinleft
    howie "Pleasure doing business with you, boys."
    cs "Thanks, Mr. Mandell."
    howie "Please, call me Howie."
    cs "Well, thanks, Howie."
    cs "Bye, everyone! Let's talk soon."
    cs "[band_name] forever!"
    n "They all high five one last time."
    stop music fadeout 3.0
    music end
    scene cs_door_outside with dissolve
    show cs with moveinleft
    n "CS moves to head inside, but there's a note on his door." # TODO: i hate this line - tate
    sticky "We waited for you to come home to confront you, but you took too long, so we left."
    sticky "Fuck you.\n-- HoH SiS"
    cs "Well, I guess that's the end of that."

    scene cs_room with dissolve
    show cs with moveinleft
    cs "I think I'm going to play some {i}Guitar Hero{/i} before bed."
    n "CS gets out his guitar."
    show cs guitar
    play sound sfx_start_rocking

    cs "{cps=15}{image=note_small1.png} [line_7]{w=1.5}\n[line_8]{w=1.5}\n[line_9]{w=1.5}\n[line_10] {image=note_small2.png}"
    $ achievement_manager.unlock("rockstar")
    scene black with Dissolve(3.0)
    $ ending_manager.mark("rockstar")
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return
