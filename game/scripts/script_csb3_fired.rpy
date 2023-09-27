### TODO:
# Needed character sprites:
# cs surprised
# cs scared
# customer
# guest [gen z] [needs bio]
# janitor
# mean [needs bio]
# ges

# Needed bgs:
# tour_bus_inside
# manitoba_street
# shoe_store
# stage2
# big_stage

# Needed sounds:
# elevator music
# elevator ding
# ~5 rock instrumentals

# TODO: TRANSITIONS NEED TO BE MORE DYNAMIC
# anno is always just sitting on the left, arc on the right, and CS in the middle
# need to like, make this more interesting

# TODO: [PAKOO] THIS ROUTE REALLY NEEDS MUSIC

label new_plan:
    scene outside_ltt
    show cs angry at center
    with fade
    cs "This really sucks. One of my favorite YouTubers just kicked me out of my dream job and told me to never come back!"
    show cs
    cs "I would be acting super emotional right now, but the years of angry YouTube comments against me have already worn me down."
    cs "Well, I guess I have no other choice than to look for another job."
    n "CS sulks away in defeat."

    scene alley with fade
    show cs disappointed with moveinright
    cs "Ugh, what am I going to do now?"
    cs "I don't even know what other job I could get."
    cs "I've spent most of my life editing..."
    n "Before CS can spend much time thinking about alternatives, someone comes running up to CS."
    show arceus at right with moveinright
    arceus "CS!"
    show cs scared
    cs "Ah! Arceus?!"
    arceus "CS, we gotta get outta here, fast."
    cs "OK, what? What's going on?"
    arceus "Cops. They're still after us."
    cs "Oh, come on, really?! Today has sucked bad enough already."
    arceus "What happened to you? I just thought you were out here for a smoke break."
    cs "Arc, I don't smoke."
    arceus "Man, I don't know."
    show cs disappointed
    cs "No, I got fired."
    arceus "Aw, man. That sucks. I'm sure we'll figure it out."
    arceus "Come on, let's go back to the hotel. We can think of something, I'm sure."
    cs "Alright man, thanks. Let's go."

    scene hotel_lobby
    show cs at right
    show arceus at left
    with fade
    arceus "Come on up to my room, we'll workshop where to go from here."
    cs "Alrighty then. Not like I'll be able to pay for my own much longer..."
    arceus "Oh come on, don't talk like that. Come on."

    scene hotel_room
    show arceus at right
    show cs at left
    with fade
    arceus "OK, let's think. We have two big problems. The cops, and money."
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
    show anno at mid_left
    anno "Hey, CS, what are you doing here?"
    cs "I got fired. And the cops are still after us."
    anno "Ah, fuck. What's the plan?"
    arceus "Nothing yet... wait. Anno, I just got an idea."
    anno "What's up?"
    arceus "You know AI stuff, right?"
    anno "Well, yeah, but I don't see--"
    arceus "We AI generate a message to the cops. Tell them they don't need to go after us anymore."
    anno "From who?"
    arceus "HoH SiS."
    anno "Wait, yeah, I can totally do that, I have the models ready for that and everything."
    n "Anno starts typing away at his laptop, and within a few minutes, a voice plays out of the speaker."
    ed "I think CS is a pretty good guy. You shouldn't arrest him."
    cs "Oh my god, that's amazing! But what about you two?"
    anno "Gotcha covered."
    # IDEA: Maybe have an actual AI-generated clip here?
    if fun_value(20):
        bomaha "I'm officially pardoning Annorexorcist and Arceus3251, for helping me out of a pickle."
    else:
        obama "I'm officially pardoning Annorexorcist and Arceus3251, for helping me out of a pickle."
    arceus "Incredible as always, Anno."
    anno "I try."
    cs "But what about money? I'm still out of a job and I'd like to keep having a roof over my head."
    arceus "I don't know man, I can't think after all that. Let's take a bit and relax. Clear our heads."
    cs "Good call. Wanna play some Guitar Hero?"
    anno "I'm down, but, do you have controllers?"
    cs "Do I?"
    hide cs with moveoutleft
    n "Anno and Arc look at each other confused."
    show cs with moveinleft
    n "CS comes back holding two guitar controllers and a drum kit."
    cs "Saw em on the side of the road. Couldn't pass em up."
    jump guitar_hero

label guitar_hero:
    scene hotel_guitar_hero with fade
    n "CS, Anno, and Arc relax by playing some Guitar Hero."
    arceus "Man, we're all pretty good at this."
    cs "Wait, this gives me an idea."
    anno "What?"
    arceus "No, you're not thinking..."
    cs "Let's start a band!"
    arceus "Man, there's no way that'll work. Playing a video game isn't the same thing as making real music."
    cs "Come on! Anno knows AI, Arc is actually a really good percussionist, and I have millions of scrobbles, so I know my music."
    anno "He has a point..."
    arceus "Does he?"
    cs "What's the worst that happens? We need money, don't we?"
    arceus "We do..."
    cs "Then let's do this!"
    anno "I'm down!"
    cs "Arc?"
    arceus "What do I have to lose?"
    cs "Woohoo!"  # haha I did it too Pakoo
    $ achievement_manager.unlock("Guitar Hero")

    scene hotel_room with fade
    cs "Maybe we should call Blank. He's like, an actual musician."
    n "CS calls Blank on Discord."
    blank "CS? Where the heck have you been?"
    cs "Don't worry about it, I'll explain soon. I need tips on making music."
    blank "Man, I don't know, I just open FL Studio and kinda click shit until music comes out."
    cs "Wait, that's it?"
    blank "I mean, that's not {i}it{/i}, but--"
    cs "Awesome, thanks Blank!"
    n "CS hangs up."
    cs "Well, you heard the man. Anno, do you have FL Studio?"
    anno "Just got it."
    cs "Well let's get to work, boys!"
    jump write_song

label write_song:
    stop music
    scene black with dissolve
    n "After some time, the gang have their first song written."

    scene hotel_room with dissolve
    show arceus at right with moveinright
    arceus "You know, that's not half bad."
    show anno at left with moveinright
    anno "I like it a lot!"
    show cs at center with moveinbottom
    cs "Wanna play it again one more time?"
    anno "Can do!"
    n "Anno hits play on the track."
    # IDEA: Actual instrumental here? I'm thinking rock-themed. Kinda Foo Fighters-y?
    n "{cps=15}{image=note_small1.png}We broke the chains, now we're free to fly,{w=1.5}\nEscaped concrete, and now we see blue skies{w=1.5}\nBecome brand new, we'll leave the past behind,{w=1.5}\nPrisoners no more, 'cause a new life we'll find{image=note_small2.png}"
    cs "Yeah, that's really good!"
    arceus "Well I guess all we have to do now is upload it."
    anno "Alright boys, what do we call it?"
    $ song_name_1 = renpy.input("What should we call the song?", song_name_1)
    cs "How about {i}[song_name_1]{/i}?"
    $ achievement_manager.unlock("Hi, My Name Is...")
    if song_name_1 == "FUCK SEX BALLS":
        arceus "Haha, very funny, Pakoo."
        cs "Huh?"
        arceus "Sorry, I meant CS. I don't know why I said Pakoo."
        anno "Well, I like it."
        arceus "I'm cool with it."
    else:
        anno "That's awesome."
        arceus "I like it!"
    cs "Alright, it's settled! Let's upload {i}[song_name_1]{/i} to streaming services!"
    arceus "Are you going to plug it in the Discord?"
    cs "I guess I should, but people are going to be really confused as to why I'm not streaming still..."
    anno "I think they're used to you not streaming for a while."
    cs "Fair, but a music career?"
    arceus "Just say it's a side project."
    cs "Fair enough."
    n "Anno uploads the song, and CS tells the CSCord about it."
    discord "What the heck is this?"
    discord "Huh, this is pretty good."
    discord "CS can sing?!"
    cs "It's going well! People seem to like it."
    arceus "Let's hit the hay and check in on it in the morning."
    anno "Yeah, I'm getting tired."
    cs "Sounds good to me!"

    scene black with dissolve
    n "While they sleep, the song accumulates streams..."
    jump hotel_next_day

label hotel_next_day:
    stop music
    scene hotel_room with dissolve
    show cs at left with moveinleft
    cs "Let's go get breakfast."
    show anno with moveinleft
    anno "Free waffles, hell yeah."
    show arceus flipped at right with moveinleft
    arceus "Those sausages are amazing."

    scene hoh_elevator with fade
    show anno at left
    show arceus at right
    show cs
    with dissolve
    # play music elevator_music
    pause 2.0
    cs "So, see any good shows lately?"
    arceus "You watch TV?"
    cs "Not really."
    arceus "Mmm."

    pause 2.0
    cs "Do you have any ideas for{nw}"
    arceus "Man I {i}just{/i} woke up."
    cs "Yeah, sorry."

    pause 2.0
    play sound "audio/elevator_ding.ogg"

    scene hotel_breakfast with fade
    show cs at center with moveinleft
    cs "Ah, nothing like a hotel breakfast to wake me up."
    n "The other two groggily join CS."
    show anno at left behind cs
    show arceus flipped at right behind cs
    with moveinleft
    n "They all sit down to eat."

    # show hotel_table behind cs with dissolve
    n "As they eat, CS checks the stream numbers on {i}[song_name_1]{/i}."
    # show cs surprised
    cs "Guys?"
    arceus "Mmm?"
    n "Arceus and Anno are stuffing their face."
    cs "The song has like, a hundred thousand streams."
    n "Arceus nearly spits out his food."
    arceus "It has what?!"
    n "CS shows Arc the phone."
    arceus "Holy shit!"
    anno "Wait, that's crazy actually."
    show cs happy
    cs "This is amazing! We might have a ticket out of here! We won't have to run from the cops anymore!"
    n "A random patron turns to look at CS."
    show cs worried
    cs "Uh... metaphorically, of course."
    n "The patron turns back around."
    show cs
    cs "{i}ahem{/i}\nAnyway...{w=0.5} so what now?"
    anno "I guess we keep it going?"
    arceus "We can't let this window close, right?"
    cs "I'm shocked, but yeah! Let's do it!"
    n "The gang finish their food and head back up to their room."
    hide cs
    hide anno
    hide arceus
    with moveoutright
    jump song_2

label song_2:
    stop music
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
    # TODO: An upbeat rock instrumental.
    n "An upbeat rock instrumental plays from Anno's computer."
    arceus "Heck yeah, awesome. OK, here I go..."
    arceus "{cps=15}{image=note_small1.png}We're going down to Vegas,{w=1.5} we're gonna strike it rich!{w=1.5}\nWe're going down to Vegas..."
    arceus "Uh..."
    $ line_1 = renpy.input("Finish the line!", "")
    cs "How about, '[line_1]'"
    $ achievement_manager.unlock("Singer-Songwriter")
    arceus "Yeah!"
    arceus "{cps=15}{image=note_small1.png}We're going down to Vegas,{w=1.5} [line_1]{image=note_small2.png}"
    cs "Woohoo! That sounds awesome!"
    anno "Let's get some backing vocals and a solo done and we have another song!"
    arceus "I'm glad you guys like it :3"

    scene black with dissolve
    n "After a furious writing session, their new song is done!"

    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve
    anno "So what do we call this one?"
    arceus "I liked your name for the last one, CS, why don't you name this one, too?"
    cs "How about..."
    $ song_name_2 = renpy.input("What should we call the song?", song_name_2)
    cs "{i}[song_name_2]{/i}?"
    arceus "You're a genius, CS."
    cs "Aw, thanks, guys. Wait, we don't have a band name either!"
    anno "Yeah, what were you thinking?"
    cs "I was thinking..."
    $ band_name = renpy.input("What should we call the band?", band_name)
    cs "[band_name]!"
    anno "Woah, awesome! Not as good as 'Nirvana', but you know, it wasn't going to be."
    cs "Hell yeah! [band_name] forever!"
    n "They all high-five."
    arceus "Well, I guess tomorrow, we can release this one!"
    anno "Sounds good!"
    cs "I'm getting tired, I think we should hit the sack."
    if fun_value(10):
        arceus "I'm gonna hit my sack{nw}"
    arceus "Yeah, that sounds like a good idea."
    n "The boys all get ready for a night's rest."

    scene black with dissolve
    pause 2.0
    cs "Hey guys?"
    anno "Hmm?"
    cs "What if we {i}don't{/i} release the song tomorrow?"
    arceus "What? Are you crazy? We're doing so well."
    cs "That's what I'm saying. Let's release a whole EP! That way, we get more views on the whole thing, and maybe we can even sell vinyls!"
    arceus "You and your vinyls."
    cs "I mean, come on, right? Our first gamble paid off, and now we have an audience. What do we have to lose?"
    anno "Yeah, we could."
    arceus "I guess I'm cool with that."
    cs "Let's do it then! [band_name], here we go!"
    jump ep_time

label ep_time:
    stop music
    pause 1.0
    scene hotel_breakfast
    show anno at left
    show arceus flipped at right
    show cs
    with dissolve

    cs "So, we're making a whole EP, what do we have to do?"
    anno "Well, Naming King, what were you thinking about calling it?"
    cs "Well, I had a dream last night."
    arceus "Oh no."
    cs "And I dreamt the name:"
    $ ep_name = renpy.input("What should we call the EP?", ep_name)
    cs "[ep_name]!"
    anno "You know what, I like it."
    arceus "See, when you said 'I thought of it in a dream,' I thought it was going to suck."
    cs "Fair."
    cs "So now we need to start putting some songs on this bad boy!"
    arceus "Well then let's get to it, yeah? We already have {i}[song_name_1]{/i} and {i}[song_name_2]{/i}."
    anno "Well, I had an idea for one this time."
    cs "Oh? Hit us with it!"
    anno "Well, I know I want it to be about travelling the world, but I don't know what to say for some of the lines."
    cs "I can help fill them in!"
    anno "Alright, awesome, here's what I got:"
    anno "{cps=15}{image=note_small1.png}I made my way over to Japan...{image=note_small2.png}"
    $ line_2 = renpy.input("What should the next line be?", "")
    anno "OK! How about..."
    anno "{cps=15}{image=note_small1.png}I found myself in the U.K...{image=note_small2.png}"
    $ line_3 = renpy.input("What should the next line be?", "")
    anno "Nice, nice, how about:"
    anno "{cps=15}{image=note_small1.png}I'm gonna go party in Sweden...{image=note_small2.png}"
    $ line_4 = renpy.input("What should the next line be?", "")
    anno "{cps=15}{image=note_small1.png}I'm globetrottin'!{image=note_small2.png}"
    cs "Hey, I like that! Sing it all the way through!"
    anno "Gotcha!"
    # TODO: Fun rock instrumental
    anno "{cps=15}{image=note_small1.png}I made my way over to Japan...{w=1.5}\n[line_2]{image=note_small2.png}"
    anno "{cps=15}{image=note_small1.png}I found myself in the U.K...{w=1.5}\n[line_3]{image=note_small2.png}"
    anno "{cps=15}{image=note_small1.png}I'm gonna go party in Sweden...{w=1.5}]\n[line_4]{image=note_small2.png}"
    anno "{cps=15}{image=note_small1.png}I'm globetrottin'!{image=note_small2.png}"
    n "Arceus claps."
    cs "Well, I guess you want me to name this one, too?"
    anno "Go for it."
    $ song_name_3 = renpy.input("What should we call the song?", song_name_3)
    anno "{i}[song_name_3]{/i} it is!"
    cs "Woohoo! Three songs down!"
    arceus "Dang, and all without leaving the breakfast table."
    anno "Now that's efficency. I'll go back upstairs and polish this up."
    hide anno with moveoutleft
    n "Anno gets up from his seat and heads to the room."
    cs "He's really been a huge help with all of this."
    arceus "Yeah, I kinda feel like I'm not pulling my weight."
    cs "What do you mean, you wrote {i}[song_name_2]{/i}!"
    arceus "True, true."
    cs "Listen, I'm just like, the name guy. And part of me doesn't even feel like I'm coming up with those, they just kinda come to me, man."
    arceus "Nah dude, you wrote {i}[song_name_1]{/i}!"
    cs "I guess."
    arceus "We should head back upstairs with Anno. Maybe there is something we can do to help!"
    cs "Yeah, let's go see!"
    jump back_to_room

label back_to_room:
    stop music
    scene hotel_room
    show anno
    with dissolve

    show cs at left
    show arceus at right
    with moveinleft

    n "Anno is deep in his laptop."
    anno "Hey guys!"
    cs "Hey!"
    arceus "We were wondering, is there anything we can do to help?"
    anno "Hmm... well, I need help with this solo."
    arceus "Well, hey, I'm a percussionist, I can get a drum solo in there."
    anno "Yeah, lay one on me!"
    n "Anno plays the track, and Arceus taps out a killer drum line."
    anno "That's awesome, man!"
    arceus "Thank you, thank you."
    cs "What can I do?"
    anno "Well, you already named it {i}[song_name_3]{/i}, and that's definitely our best title yet. You wrote like, half the lines, too."
    anno "But if you want to record backing vocals, this track might sound dope with them!"
    cs "Will do!"
    python:
        last_words = []
        for l in [line_2, line_3, line_4]:
            s = l.split(" ")
            last_words.append(s[-1])
    anno "Recording!"
    cs "{cps=15}...Japan!{w=1.5} ...[last_words[0]]!{w=1.5}\n{cps=15}...U.K.!{w=1.5} ...[last_words[1]]!{w=1.5}\n{cps=15}...Sweden!{w=1.5} ...[last_words[2]]!\n{w=1.5} ...globetrottin'~!"
    pause 1.0
    anno "You're clear! That was awesome!"
    cs "Thank you, thank you!"
    arceus "Is that us wrapped for the day?"
    anno "I think it is! I'll export this and save it as {i}[song_name_3]{/i}!"
    cs "Let's go!"
    n "Everyone high-fives."

    scene black with dissolve
    n "The gang go to bed after another successful day."
    cs "{i}At this rate, we'll have this whole EP done by the end of the week!"
    n "CS smiles to himself, drifting off to sleep."

    pause 1.0
    jump mcd

label mcd:
    stop music

    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve

    anno "Well, you guys ready to write the next song?"
    n "Stomachs grumble throughout the room."
    cs "Ugh, I'm starving."
    arceus "That hotel breakfast just isn't doing it for me today."
    anno "Hmm... we have a little extra money from the first song's streams, wanna go to like, McDonald's?"
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

    n "CS and the gang sit at a table in the McDonald's and eat their food."
    n "As they eat, they start talking about their next song."
    cs "OK, I had this idea, but it's a bit out there."
    anno "Alright, let's hear it."
    cs "{cps=15}{image=note_small1.png}I'M GONNA TAKE OVER THE WORLD.{w=1.0} I'M GONNA KILL GOD.{w=1.0} I CAN CONTORT REALITY TO MY WHIMS--{image=note_small2.png}"
    anno "Wait, what the fuck, hold on--"
    n "Arceus looks visibly concerned."
    arceus "That might be a little bit much."
    n "Arceus texts someone under the table."
    cs "Yeah, I was worried about that."
    cs "OK, OK, I have a different idea."
    anno "Yeah...?"
    cs "Well I don't have all the lyrics yet..."
    arceus "Maybe this time, we can fill in the lines!"
    cs "OK! Here's what I have so far:"
    cs "{cps=15}{image=note_small1.png}Through all adversity, we'll bind together and overcome...{image=note_small2.png}"
    arceus "Ooh, I got something:"
    $ line_5 = renpy.input("What should the next line be?", "")
    arceus "{cps=15}{image=note_small1.png}[line_5]{image=note_small2.png}"
    cs "Nice! How about:"
    cs "{cps=15}{image=note_small1.png}With my friends beside there's no foe we can not fight...{image=note_small2.png}"
    anno "Let me take this one."
    $ line_6 = renpy.input("What should the next line be?", "")
    anno "{cps=15}{image=note_small1.png}[line_6]{image=note_small2.png}"
    cs "Heck yeah! And then I think we should have a solo like:"
    cs "{cps=15}{image=note1.png}{image=note4.png}{image=note3.png}{image=note1.png}{image=note5.png}{image=note1.png}{image=note2.png}{image=note1.png}{image=note2.png}{image=note2.png}{image=note4.png}{image=note4.png}{image=note3.png}{image=note3.png}{image=note5.png}{image=note5.png}{image=note1.png}{image=note1.png}{nw}"
    arceus "Woah, how are you doing that with your mouth?"
    cs "What, like:"
    cs "{cps=10}{image=note1.png}{image=note2.png}{image=note3.png}{image=note4.png}{image=note5.png}"
    cs "Honestly I have no idea."
    customer "Hey, that sounds really good!"
    cs "Huh?"
    customer "Yeah, I heard you guys making that song from my table, it's really good!"
    anno "Thanks! We're actually putting out an EP soon!"
    customer "Well I definitely wanna hear that song again, what's it called?"
    cs "Uh..."
    $ song_name_4 = renpy.input("What should the song be called?", song_name_4)
    cs "It's called {i}[song_name_4]!{/i}"
    anno "It'll be on our EP [ep_name], just look up [band_name] on streaming services!"
    customer "Awesome, I'm excited! I'll make sure to check it out!"
    n "The customer walks away."
    cs "People are really liking our stuff."
    arceus "This is going better than I ever dare hoped."
    anno "Let's go back to the room and get this song made!"
    n "On their way out of the store, CS turns to Arc."
    cs "You know, I think [song_name_4] might be our best one yet."

    scene black with dissolve
    jump hotel_lobby_2

label hotel_lobby_2:
    stop music

    scene hotel_lobby    
    show anno at left
    show arceus at right
    show cs
    with dissolve

    n "As they walk through the hotel lobby to their room, they hum their newest song to themselves."
    cs "{cps=15}{image=note_small1.png}{i}[line_5]{/i}{image=note_small2.png}"
    n "Someone in the lobby overhears them singing the song and runs up to them."
    guest "Holy shit, are you from [band_name]?!"
    cs "Uh..."
    guest "You are! Holy shit!"
    guest "You guys are cracked at making music! You're like GOATed!"
    cs "What? What does that--"
    n "A crowd starts to form around them."
    guest "You're a rizz god! You're off the sauce at this shit!"
    anno "We've released one song."
    guest "I'm like the biggest stan of you guys! You guys gotta perform."
    arceus "Perform?"
    guest "You gotta like, give us a sneak peak of your new EP!"
    anno "{i}How did he know we're releasing a new EP{/i}"
    guest "Come on! You gotta! You'll pop off on TikTok."
    cs "Uh, sure? I guess?"
    n "The crowd cheers."
    cs "Alright, well, here's our song..."
    n "CS turns to the others to queue them."
    cs "[song_name_2]!"
    n "Anno starts up the backing track, and Arceus grabs some random objects to use as a drum kit."
    cs "{cps=15}{image=note_small1.png}We're going down to Vegas, we're gonna strike it rich!{w=1.5}\nWe're going down to Vegas, [line_1]{image=note_small2.png}"
    n "The crowd cheers wildly."
    anno "We're [band_name]! Check out [ep_name] on streaming services soon!"
    n "The gang heads up to their room."
    jump song_5

label song_5:
    stop music
    scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve

    anno "This is the last song on the EP. We need to go big with this one."
    arceus "I'm nervous to write this one, we really need to end on a banger."
    anno "Something victorious, something inspiring."
    arceus "Hmmm..."
    anno "CS, why don't you write this one?"
    cs "Me?"
    anno "Yeah!"
    cs "But I wrote all the other songs!"
    anno "Nah, you filled in our blanks."
    arceus "Yeah, why don't you write the whole thing this time!"
    cs "Oh gosh, you guys sure?"
    anno "Yeah, go ahead! Here, I'll give you a beat..."
    n "Anno plays an upbeat song on his laptop."
    $ line_7 = renpy.input("Write a line! (1/4)", "")
    $ line_8 = renpy.input("Write a line! (2/4)", "")
    $ line_9 = renpy.input("Write a line! (3/4)", "")
    $ line_10 = renpy.input("Write a line! (4/4)", "")
    cs "I think I have something, here it is!"
    cs "{cps=15}{image=note_small1.png}[line_7]{w=1.5}\n[line_8]{w=1.5}\n[line_9]{w=1.5}\n[line_10]{image=note_small2.png}"
    arceus "Yo?!"
    anno "That's perfect! Give it name!"
    $ song_name_5 = renpy.input("What should the song be called?", song_name_5)
    cs "It's called {i}[song_name_5]!{/i}"
    arceus "That's going to be a huge hit."
    anno "So wait, that's [ep_name] done, then!"
    cs "Woohoo!"
    n "They all high five."
    anno "I guess I'll get this mastered and release it tonight!"
    cs "[band_name] forever!"
    arceus "You know, I'm starting to really believe in this whole thing."
    $ achievement_manager.unlock("Independent Artist")
    jump fan_interaction

label fan_interaction:
    stop music
    scene black with dissolve
    n "The next day, they hear a knock on their hotel room door early morning."
    scene hotel_door with dissolve
    cs "Huh? Who the fuck knocks on a hotel door, especially at this hour?"
    show cs angry at left with moveinleft
    cs "Hello?"
    # show mean at right with moveinright
    mean "OMG, it's CS!"
    cs "Huh? Are you like, a fan?"
    mean "Yes! Of your music!"
    n "CS for a moment forgets he just spent a week making an EP."
    cs "My... music? Oh, yeah, right, [band_name]!"
    cs "Wait, how did you find my hotel room?"
    mean "You should go on tour!"
    cs "What?"
    n "CS is still half asleep."
    mean "Go on tour! I'm from Ontario."
    cs "Oh... kay?"
    mean "Bye!"
    hide mean with moveoutright
    n "CS closes the door."
    cs "Anno?"
    n "Anno wakes up, barely."
    anno "Huh?"
    cs "I need you to check the numbers, quick."
    anno "The numbers? On [ep_name]? Uh..."
    n "Anno pulls out his phone."
    n "Anno drops his phone."
    anno "Guys... we might have more money than we thought."

    scene hotel_room
    show anno at left
    show arceus at right
    show cs 
    with fade

    n "The gang regroup to discuss."
    cs "OK, give it to me straight. How many sales of the EP?"
    anno "57,685."
    cs "Holy shit, that's a lot of sales, how much money{nw}"
    anno "57,688."
    cs "OK, yeah, I got that, how much money does that equate to{w=0.5}{nw}"
    anno "57,692...{w=1.0}{nw}"
    cs "Stop refreshing the page!"
    anno "Sorry."
    cs "How much money is that?"
    anno "About $15,000."
    cs "Oh my god!"
    arceus "Well, we going to need to file taxes on it."
    anno "Do we?"
    arceus "You wanna go back to prison?"
    anno "No..."
    arceus "Well then."
    cs "We need to figure this out. We at least have enough money to get out of this hotel room."
    arceus "And more."
    cs "And more, but we gotta be careful. We don't wanna blow it, or spend more than we can pay the taxes on."
    anno "For sure."
    cs "How are we going to figure out how to--"
    n "Anno gets an email."
    anno "Wait, hold on, let me read this, it looks important."
    agent "{b}Tour Offer{/b}\nHey, [band_name]!\nMy name is Howie Mandell, and I'm a talent agent and tour manager."
    cs "Woah, really?"
    agent "I'm emailing to inquire if you'd be interested in touring the country with your band. Your latest EP, [ep_name], has been making big waves on streaming services, and a live performance might be just what you need to take the next step."
    anno "Oh my God!"
    agent "If you're willing to negotiate, I think we could strike a very mutually benefitial deal for both of us."
    arceus "That sounds amazing!"
    agent "Please get in touch as soon as you can,\n-- Howie Mandell"
    cs "We have to accept, right?"
    arceus "Our last two gambles paid off, I guess we gotta go all the way."
    anno "We can't pass this up. I'll email him back."
    cs "[band_name] is going on tour!"
    jump howie

label howie:
    stop music
    scene black with dissolve
    n "After a few hours, the band meet Howie downstairs in the lobby."

    scene hotel_lobby
    show anno
    show cs at mid_right
    show arceus at right
    with dissolve

    n "Howie walks into the lobby."
    show howie at left with moveinleft
    agent "You guys ready?"
    cs "Ready for what?"
    agent "A ride in a limosine!"
    n "The group is in shock."
    anno "Already? We haven't even struck a deal!"
    agent "Ah, you will, I trust in that. But until then, why don't I treat you all to the ride of a lifetime?"
    n "CS, Anno, and Arc all head into the limo out front, lead by Howie."
    hide cs
    hide anno
    hide arceus
    hide howie
    with moveoutleft

    scene in_limo with dissolve
    arceus "These snacks are amazing!"
    anno "This music's awesome!"
    cs "These seats are some comfy!"
    agent "Alright boys, enough chat, let's talk business."
    agent "I want to take you guys on tour."
    cs "Already?!"
    agent "Oh yeah baby, already. [ep_name] made [band_name] big, overnight. This kinda success comes once in a lifetime, and it's in your lifetime, and it's right now!"
    anno "Woah, woah, woah, slow down. Why are you so invested in our success?"
    agent "Oh, don't think I'm going to get a raw deal here, I know how to make sure we all end up happy."
    arceus "You sure you mean all of us?"
    agent "I sense you're spooked so I'll give ya the rub. We take you on tour. Every ticket you sell, I get a cut, you get a cut, we all go home snuggling our cash."
    cs "You snuggle your cash?"
    agent "Better than lavender, baby."
    anno "So what's the plan? How do we get venues? Do we even have a way to promote?"
    agent "Leave all the fiddly buisness to me. You guys just get on stage and sing like, {i}[song_name_3]{/i} or whatever."
    agent "How's that song go? {image=note_small1.png}{i}I made my way over to Japan, [line_3]?{/i}{image=note_small2.png}"
    arceus "No, that's not--{w=0.5}{nw}"
    agent "Anywho, do we got a deal?"
    anno "I want to see whatever contract you're having us sign, first."
    agent "Smart man, smart man. Here it is."
    n "Howie hands Anno the contract."

    scene black with dissolve
    n "As Anno reads over the contract, CS, Arc, and Howie talk more about the deal."
    menu:
        "Should they take the deal?"
        "Yes"  (type = "good"):
            jump signed_the_contract
        "No"  (type = "bad"):
            return

label signed_the_contract:
    stop music
    scene black
    n "After some time, Anno signs the contract, and they all return to the hotel."

    scene hotel_lobby    
    show anno at left
    show arceus
    show cs at mid_left
    show howie at right
    with dissolve

    agent "Well, your first stop is Vancouver."
    cs "Vancouver? Where are we playing?"
    n "Howie reads his iPad."
    agent "Looks like something called LTX? Linus Tech Expo?"
    cs "Wait, Linus--"
    agent "See you bright an early tomorrow, we're getting in a tour bus!"

    hide howie with moveoutright
    show cs at center
    show arceus at right
    with move

    cs "Linus..."
    anno "Don't be worried. Maybe he won't even recognize you."
    arceus "Yeah, he'll be busy running the expo."
    cs "Man, I don't know, we didn't end on great terms."
    arceus "Let's just get a good night sleep. If we need to be up that early I need to get shuteye."
    cs "OK..."

    scene black with dissolve
    n "The gang all go upstairs and head to bed, but CS struggles to sleep well."
    cs "{i}Man, I'm worried about seeing Linus again. What if he just throws all of us out because he doesn't want to see me?"
    cs "{i}The fate of [band_name] could rest in some dumb shit I did in the past."
    cs "{i}Not even the past, like, a week or two ago."
    cs "{i}Ugh, I can't sleep like this. I need a drink."
    n "CS gets out of bed and takes a walk around the halls."

    scene hotel_hall
    show cs at left with moveinleft
    cs "Maybe a cold drink will clear my head."

    show csgod at right with dissolve
    csgod "Or I can."
    show cs shocked
    cs "Ah!"
    show cs
    csgod "I wouldn't fret about Linus."
    cs "How-- how did you--"
    csgod "What you did was your best. Good men will realize that. His anger will have been brief, despite his rash actions."
    cs "How do you know all this?"
    csgod "That isn't important. What's important is your mind being prepared for the day ahead."
    csgod "You will go to bed, you will rest, and you will do your best -- as you have."
    cs "Th-thank you... what do I call you?"
    csgod "You can call me...{w=1.5} !!!"
    hide csgod with dissolve
    # show janitor at right with moveinright
    janitor "You alright man? Who are you talking to?"
    cs "N-- no-one. Just heading to bed."
    show cs flipped
    hide cs with moveoutleft
    janitor "Weird guy."
    jump first_tour_day

label first_tour_day:
    stop music
    scene black with dissolve
    n "CS heads to bed, and the next morning, the whole [band_name] crew gets ready for their first tour day."

    scene hotel_room
    show anno at left
    show arceus at right
    with dissolve

    show cs with moveinleft
    anno "Feeling better?"
    cs "Much."
    arceus "What changed?"
    cs "Eh, something... something got into my head and cleared things up for me."
    arceus "Alrighty man, well let's hope it did a good job, because it's time to hit the road."

    hide arceus
    hide cs
    hide anno
    with moveoutright

    scene hotel_lobby with dissolve
    show anno at left
    show arceus
    show cs at mid_left
    with moveinleft

    show howie at right with moveinright
    agent "You boys ready to go?"
    cs "Ready as we'll ever be."
    agent "Well, then! It's show time!"

    scene black with dissolve
    scene ltx with dissolve
    show anno at left
    show arceus
    show cs at mid_left
    with moveinleft

    n "They all arrive at LTX."
    cs "Well, it's pretty busy, I doubt we'll run into--"
    show linus at right with moveinright
    linus "Oh good, you guys are finally, here, you're [band_name], right?"
    linus "Luke told me about you guys, and I listened to [ep_name] last night... I really liked, uh, which one was it, {i}[song_name_4]{/i}?"
    linus "Anywho, I...{w=1.0}wait, CS?!"
    cs "Uh, hi?"
    linus "Wait, you... you're the lead singer in [band_name]?!"
    cs "Looks like it..."
    linus "Well, I'll say this, you're better at singing than you are editing LTT videos."
    show cs worried
    n "CS looks worried."
    n "Linus chuckles."
    linus "Listen, don't worry about it."
    show cs surprised
    cs "Really?"
    linus "Yeah, I was too hard on you. Maybe too quick to fire you, too, though it looks like you're in a better position than I could have given you."
    show cs happy
    cs "Well, thanks for the apology."
    linus "Yeah, you deserve it. Honestly, when the public learned who was editing that video and that we axed you, they were pretty upset."
    cs "How about this, when I get out of this mess, you let me edit a guest video, and I'll make a video saying we parted ways amicably."
    linus "Now that's a deal I'll take."
    linus "Now, get on stage and rock the house!"

    scene ltx_stage
    show anno at left
    show arceus at right
    show cs
    with dissolve

    # TODO: cheering
    n "The crowd is going insane."
    cs "We're [band_name], and this is {i}[song_name_4]{/i}!"
    n "The crowd is nuts."
    cs "{cps=15}{image=note_small1.png}Through all adversity, we'll bind together and overcome!{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}[line_5]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}With my friends beside there's no foe we can not fight!{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}[line_6]{image=note_small2.png}"
    n "Anno plays an epic guitar solo."
    pause 2.0
    scene black with Dissolve(3.0)

    scene ltx
    show anno at left
    show arceus
    show cs at mid_left
    show linus at right
    with dissolve

    linus "You guys were incredible! That was my favorite song of yours, too."
    show cs happy
    cs "Thank you so much!"
    linus "Well, I'll transfer the money to your agent."
    cs "Sounds good!"
    linus "Well, thank you, CS. I'm glad we could bury whatever hatchet we had."
    cs "Absolutely."
    hide linus with moveoutright

    show cs at center
    show arceus at right
    with move

    arceus "We did it, that was amazing!"
    anno "Hell yeah!"
    cs "We rocked!"
    arceus "Welp, back on the bus to recoop and see how much we earned!"

    hide cs
    hide arceus
    hide anno
    with moveoutright

    # scene tour_bus_inside
    scene black
    show anno at left
    show arceus at right
    show cs at center
    with dissolve

    show howie at offscreenleft with moveinright
    show howie at right with move

    agent "Boys!"
    n "The team turn to Howie to look at him."
    agent "You really rocked out there! Playing Linus' favorite song, that was a clutch move."
    cs "How much did we make?"
    agent "Five."
    arceus "Five?!"
    agent "Thousand."
    anno "Holy shit, already? With that kinda cashflow, we could..."
    agent "Woah, woah, woah, slow your horses kid."
    anno "Slow my horses...?"
    agent "That's without me taking my cut, or you three splitting it. We still got more shows to do, you know!"
    cs "Well then, let's get this show on the road!"

    scene black with dissolve
    jump second_tour_day

label second_tour_day:
    n "The group rests for the day, on their way to their next venue."
    
    # scene tour_bus_inside
    scene black
    show anno at left
    show arceus at right
    show cs at center
    with dissolve

    n "CS shouts up to the front."
    cs "Where are we heading?!"
    agent "Manitoba! We'll stop in Winnipeg, so you guys can grab some stuff if you need it."
    cs "Yeah, I might head into the city. What about you guys?"
    anno "Nah, I'm good."
    arceus "Yeah, I'm just gonna chill here."
    cs "Alrighty then!"

    scene black with dissolve
    n "As they pull into the city, CS gets out and walks the street."

    # scene manitoba_street
    show cs with moveinleft
    cs "What a place. Way better than the places I've been lately."
    cs "And everyone's so friendly!"
    show border_guard at right with moveinright
    border_guard "Pardon me, eh!"
    hide border_guard with moveoutleft
    cs "Ooh, a shoe store!"
    cs "If I'm going to be on stage, I need some better kicks."

    # scene shoe_store
    # show ges at right
    # with dissolve
    show cs at left with moveinleft
    ges "Welcome to the sho--, woah, are you CS?"
    cs "Yeah, how'd you know?"
    ges "Aren't you touring with [band_name] right now?"
    cs "Yeah, I am!"
    ges "Dude, I've been listening to [song_name_3] all day!"
    ges "{cps=15}{image=note_small1.png}I found myself in the U.K...{w=1.5}\n[line_3]{image=note_small2.png}"
    ges "That shit slaps!"
    cs "Well, thanks, I was wondering if you had some nice shoes for my concert tonight."
    ges "Oh man, I got just the thing."
    # hide ges with moveoutright
    n "Ges searches through boxes in the back."
    n "He returns with a box."
    # show ges at right with moveinright
    ges "These are called the {i}Gessler Step!"
    cs "The Gessler Step?"
    ges "The finest shoes I got, and I personally recommend them. You'll love 'em or my name isn't Ges! And it is."
    cs "Wait, did you make these shoes?"
    ges "Nah, just kinda a coincidence."
    cs "Oh, okay."
    n "CS tries on the shoes."
    cs "These are awesome!"
    cs "Wait, how did you know my size?"
    ges "It's online."
    cs "Wait, it's what--{w=0.5}{nw}"
    ges "That'll be $88.88, if you want em!"
    cs "I'll take them!"
    n "CS checks out and heads back to the tour bus."

    # scene tour_bus_inside
    show anno at left
    show arceus flipped
    with dissolve

    show cs flipped at right with moveinright
    anno "Hey CS!"
    arceus "Dang, nice shoes!"
    cs "Thanks! Are you guys ready to perform tonight?"
    arceus "Heck yeah!"
    anno "Of course."
    cs "I think we should sing [song_name_3] tonight."
    arceus "Why is that?"
    cs "I just think it'll make someone pretty happy."
    anno "Sounds good to me!"

    scene convention_center_entrance
    show anno at left
    show cs at mid_left
    show arceus
    with dissolve

    n "A crowd can be heard cheering for the previous act."
    show nova at right with moveinright
    nova "Easy crowd tonight, you guys are gonna knock it out of the--{w=0.5} CS?"
    cs "Nova? What are you doing here?"
    nova "I live close by, I was DJing as the opening act..."
    nova "Wait, let me check something."
    n "Nova looks at a piece of paper."
    nova "Opening for... [band_name]? Is that you guys?"
    cs "Yep!"
    nova "No shit, I've been listening to [ep_name] on $STREAMING_SERVICE a ton this week!"
    nova "I didn't know it was you!"
    cs "Well, us."
    n "CS gestures to the others."
    nova "Of course! Well you guys go clean up out there."
    arceus "Will do!"
    
    hide nova with moveoutright
    cs "Well, let's go out there and show them what we're made of!"

    # scene stage2
    show anno at left
    show arceus at right
    show cs
    with dissolve

    cs "I know you all just watched an amazing performance by Nova, and that's going to be a hard act to follow..."
    cs "But who wants to hear {i}[song_name_3]{/i}?!"
    n "The crowd is exploding."

    cs "{cps=15}{image=note_small1.png}I made my way over to Japan...{w=1.5}\n[line_2]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}I found myself in the U.K...{w=1.5}\n[line_3]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}I'm gonna go party in Sweden...{w=1.5}]\n[line_4]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}I'm globetrottin'!{image=note_small2.png}"

    n "The crows is applauding wildly."
    cs "We're [band_name]!"
    n "The crowd is loving it."

    scene black with dissolve
    
    # scene tour_bus_inside
    show anno at left
    show arceus at right
    show cs
    with dissolve

    jump third_tour_day

label third_tour_day:
    n "Howie hollers from the front of the bus."
    agent "Alright boys, it's your last performance!"
    cs "Where are we heading?"
    agent "Ontario!"
    cs "Ontario? That's where that one fan was from!"
    agent "Well he's about to be a happy camper!"
    anno "I can't believe we're already at our last tour day!"
    $ line_num = renpy.get_filename_line()[1] + 1
    arceus "Well, it's been [line_num] lines, it's been a while."
    anno "We're going to really have to go big for this one, I think it's our biggest audience size yet."
    cs "We'll put on a show like they've never seen before!"

    # TODO: Can this please be a diiferent convention center?
    scene convention_center_lobby
    show anno at left
    show arceus
    show cs at mid_left
    with moveinleft

    cs "Alright, well let's get prepared, we have way more songs to do tonight--{nw}"
    # show mean with moveinright
    mean "HOLY SHIT IT'S YOU!"
    cs "Wait, are you that fan from my hotel?"
    mean "YOU ACTUALLY MADE IT TO ONTARIO?"
    cs "Uh... yeah, totally because you asked me to!"
    show cs worried
    # show mean at mid_left
    with move
    n "Mean tackle hugs CS."
    if fun_value(10):
        cs "Ow."
    
    # show mean at right with move
    mean "Thank you so much! I know you guys will do amazing."
    # hide mean with moveoutright
    cs "Let's go make our fans proud."

    # scene big_stage
    show anno at left
    show arceus at right
    show cs
    with dissolve

    cs "For our special performance tonight, we'll be singing every song off [ep_name]!"
    n "The crowd is going wild."
    cs "First up, it's {i}[song_name_1]{/i}!"
    n "The crowd cheers."
    # TODO: Play track
    cs "{cps=15}{image=note_small1.png}We broke the chains, now we're free to fly,{w=1.5}\nEscaped concrete, and now we see blue skies{w=1.5}\nBecome brand new, we'll leave the past behind,{w=1.5}\nPrisoners no more, 'cause a new life we'll find{image=note_small2.png}"
    n "The crowd is loving this!"

    cs "Who wants to hear {i}[song_name_2]{/i}?!"
    n "The crowd responds with further excitement."
    # TODO: Play track
    cs "{cps=15}{image=note_small1.png}We're going down to Vegas,{w=1.5} we're gonna strike it rich!{w=1.5}\nWe're going down to Vegas,{w=1.5} [line_1]"
    n "The audience is adoring this."

    cs "Next up, here's a classic: [song_name_3]"
    anno "CS, none of our songs are classics, we're a new band."
    n "The crowd laughs."
    # TODO: Play track
    cs "{cps=15}{image=note_small1.png}I made my way over to Japan...{w=1.5}\n[line_2]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}I found myself in the U.K...{w=1.5}\n[line_3]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}I'm gonna go party in Sweden...{w=1.5}]\n[line_4]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}I'm globetrottin'!{image=note_small2.png}"
    n "The crowd loves this a lot."

    cs "Alright, here's a favorite for a lot of you: [song_name_4]!"
    # TODO: Play track
    cs "{cps=15}{image=note_small1.png}Through all adversity, we'll bind together and overcome!{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}[line_5]{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}With my friends beside there's no foe we can not fight!{image=note_small2.png}"
    cs "{cps=15}{image=note_small1.png}[line_6]{image=note_small2.png}"
    n "Anno shreds an epic solo."
    n "The crowd is exploding!"

    cs "And now, for the first time on stage: it's [song_name_5]!"
    n "The crowd is ready to burst."
    # TODO: Play track
    cs "{cps=15}{image=note_small1.png}[line_7]{w=1.5}\n[line_8]{w=1.5}\n[line_9]{w=1.5}\n[line_10]{image=note_small2.png}"
    n "The crowd can't get enough!"
    "Crowd" "Encore! {w=0.5}Encore! {w=0.5}Encore! {w=0.5}"
    n "CS whispers to the others."
    cs "Encore? But we don't have any more songs..."
    arceus "Make something up!"
    n "CS shouts to the crowd."
    cs "Uh... hey, you guys! Give me a word!"
    "Crowd" "Banana! {w=0.5}Street! {w=0.5}Ice!"
    cs "Uh..."
    menu:
        "What should the song be about?"
        "Banana":
            $ line_11 = "When I see you, I think about bananas"
        "Street":
            $ line_11 = "When I see you walking down the street"
        "Ice":
            $ line_11 = "Everybody knows I'm cool as ice"

    cs "OK!"
    # TODO: Play track
    cs "{cps=15}{image=note_small1.png}[line_11]{image=note_small2.png}"
    $ line_12 = renpy.input("What's the next line?")
    cs "{cps=15}{image=note_small1.png}[line_12]{image=note_small2.png}"

    cs "Thank you! We're [band_name], and thank you for listening to [ep_name]!"
    n "The crowd is overjoyed."

    hide cs
    hide anno
    hide arc
    with moveoutleft

    scene black with Dissolve(3.0)
    # Line 1200, give it up for line 1200
    jump final_tour_bus

label final_tour_bus:
    # scene tour_bus_inside
    show anno at left
    show arceus at right
    show cs
    with dissolve

    n "The boys are exhausted."
    show howie at offscreenright
    show anno at left
    show cs at mid_left
    show arceus
    show howie at right
    with move

    agent "Well, gang, that was the last stop! You did amazing out there."
    cs "I'm beat."
    anno "I'm so tired..."
    arceus "I need a nap."
    agent "Well, maybe this will perk you guys up. Wanna hear the final total?"
    cs "Sure, what is it?"
    agent "Well, after all the cuts, and splitting it... {w=0.5}each of you gets..."
    agent "$10,000!"
    n "The gang perks up."
    cs "Wait... 10K?!"
    n "Arc nudges CS."
    arceus "You can go home!"
    n "CS looks forlorn."
    arceus "What's wrong?"
    cs "Well, I've been really enjoy this, actually."
    cs "I'm not sure I wanna go home."
    anno "Nah, don't act like that. This doesn't mean [band_name] is over!"
    arceus "Yeah, we can still make music together. But you need to get back to your normal routine for a bit."
    anno "Yeah, reset your head a bit."
    cs "Yeah, you're right. And hey, maybe we can write [ep_name] 2 some day!"
    arceus "Maybe we shouldn't name it [ep_name] 2."
    cs "Yeah."
    agent "Want me to point this bus towards Casa De CS?"
    cs "You know what, yeah, let's do it."
    arceus "Let's get you home, buddy."

    scene black with dissolve
    scene cs_house with dissolve

    # TODO: I'm tired of adding transitions right now and I'm really burned out
    n "CS steps off the tour bus."
    cs "Ah, home sweet home."
    n "The others join him outside."
    arceus "Well, you should get some rest. It's been a wild few weeks for you."
    cs "It's been a wild few {i}years{/i} for you."
    arceus "Fair enough."
    anno "Yeah, we need to get back to our places too. Figure out how to reintegrate."
    howie "Pleasure doing business with you boys."
    cs "Thanks, Mr. Mandell."
    howie "Please, call me Howie."
    cs "Well, thanks Howie."
    cs "Bye, everyone! Let's talk soon."
    cs "[band_name] forever!"
    n "They all high-five one last time."

    n "CS goes to head inside, but there's a note on his door."
    sticky "We waited for you to come home to confront you, but you took too long, so we left."
    sticky "Fuck you.\n-- HoH SiS"
    cs "Well, I guess that's the end of that."

    # scene cs_room
    cs "I think I'm going to play some Guitar Hero before bed."
    n "CS gets out his guitar."

    cs "{cps=15}{image=note_small1.png}[line_7]{w=1.5}\n[line_8]{w=1.5}\n[line_9]{w=1.5}\n[line_10]{image=note_small2.png}"
    scene black with Dissolve(3.0)

    # TODO: credits
    return
