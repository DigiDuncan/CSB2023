### TODO:
# Needed character sprites:
# cs surprised
# 

# Needed backgrounds:
# hotel_lobby
# hotel_room
# guitar_hero
# hotel_elevator
# hotel_breakfast
# mcdonalds

# Needed sounds:
# elevator music
# elevator ding
# ~5 rock instrumentals

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

    # scene hotel_lobby
    show cs at right
    show arceus at left
    with fade
    arceus "Come on up to my room, we'll workshop where to go from here."
    cs "Alrighty then. Not like I'll be able to pay for my own much longer..."
    arceus "Oh come on, don't talk like that. Come on."

    # scene hotel_room
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
    # scene guitar_hero with fade
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

    # scene hotel_room
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
    # scene black with dissolve
    n "After some time, the gang have their first song written."

    # scene hotel_room with dissolve
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
    $ song_name_1 = renpy.input("What should we call the song?", "Prison Break")
    cs "How about {i}[song_name_1]{/i}?"
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
    # scene hotel_room with dissolve
    show cs at left with moveinleft
    cs "Let's go get breakfast."
    show anno with moveinleft
    anno "Free waffles, hell yeah."
    show arceus flipped at right with moveinleft
    arceus "Those sausages are amazing."

    # scene hotel_elevator
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
    # play sound elevator_ding

    # scene hotel_breakfast with dissolve
    show cs at center with moveinleft
    cs "Ah, nothing like a hotel breakfast to wake me up."
    n "The other two groggily join CS."
    show anno at left behind cs
    show arceus flipped at right behind cs
    with moveinleft
    n "They all sit down to eat."

    # show hotel_tabel behind cs with dissolve
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
    # scene hotel_room
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
    arceus "Yeah!"
    arceus "{cps=15}{image=note_small1.png}We're going down to Vegas,{w=1.5} [line_1]{image=note_small2.png}"
    cs "Woohoo! That sounds awesome!"
    anno "Let's get some backing vocals and a solo done and we have another song!"
    arceus "I'm glad you guys like it :3"

    scene black with dissolve
    n "After a furious writing session, their new song is done!"

    # scene hotel_room
    show anno at left
    show arceus at right
    show cs
    with dissolve
    anno "So what do we call this one?"
    arceus "I liked your name for the last one, CS, why don't you name this one, too?"
    cs "How about..."
    $ song_name_2 = renpy.input("What should we call the song?", "Down to Vegas")
    cs "{i}[song_name_2]{/i}?"
    arceus "You're a genius, CS."
    cs "Aw, thanks, guys. Wait, we don't have a band name either!"
    anno "Yeah, what were you thinking?"
    cs "I was thinking..."
    $ band_name = renpy.input("What should we call the band?", "CS' Crazy Crew")
    cs "[band_name]!"
    anno "Woah, awesome! Not as good as 'Nirvana', but you know, it wasn't going to be."
    cs "Hell yeah! [band_name] forever!"
    n "They all high-five."
    arceus "Well, I guess tomorrow, we can release this one!"
    anno "Sounds good!"
    cs "I'm getting tired, I think we should hit the sack."
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
    cs "I mean, come on, right? Out first gamble paid off, and now we have an audience. What do we have to lose?"
    anno "Yeah, we could."
    arceus "I guess I'm cool with that."
    cs "Let's do it then! [band_name], here we go!"
    jump ep_time

label ep_time:
    stop music
    pause 1.0
    # scene hotel_breakfast
    show anno at left
    show arceus flipped at right
    show cs
    with dissolve

    cs "So, we're making a whole EP, what do we have to do?"
    anno "Well, Naming King, what were you thinking about calling it?"
    cs "Well, I had a dream last night."
    arceus "Oh no."
    cs "And I dreamt the name:"
    $ ep_name = renpy.input("What should we call the EP?", "The White Album")
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
    $ song_name_3 = renpy.input("What should we call the song?", "Globetrottin'")
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
    # scene hotel_room
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

    # scene hotel_room
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

    # scene mcdonalds
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
    $ song_name_4 = renpy.input("What should the song be called?", "Through the Battles and the Fights")
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

    # scene hotel_lobby
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
