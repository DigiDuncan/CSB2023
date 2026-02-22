label book_CSB3_EBEEP12024FDEADNYWFFEAGM:
    stop music fadeout 3.0
    music end
    scene cs_kitchen
    show digi flipped at center
    with dissolve
    play music good_eatin
    music good_eatin
    n "As the sun comes up for the day, Digi finds himself in his kitchen."
    digi "I really need to find something to eat..."
    show digi shock flipped
    digimom "Duncan!{w=1.0}{nw}" with vpunch
    extend " Come here!" with vpunch
    show digi flipped
    digimom "There is a letter for you!"
    digi "Coming!"
    window hide
    hide digi with moveoutright
    pause 3.0
    show digi at center
    show folded_paper at manual_pos(0.5, 0.75, 0.5):
        zoom 0.6
    with moveinright
    n "Digi comes back to the kitchen, now with a letter in hand."
    digi "I wonder who sent me a letter..."
    n "Digi pulls the letter out of the envelope, and reads it out loud."
    digi "Dear Digi, you are invited to come over to Elizabeth's birthday party."
    digi "I guess."
    digi "I don't really know what we will be doing, but it might be cool."
    show digi shock
    digimom "Duncan!" with vpunch
    extend " You are talking {i}way{/i} too loud!" with vpunch
    digi "Well, this is a great excuse to leave!"
    show digi angry flipped
    digi "Alright then, bye mom!"
    show folded_paper:
        zoom 0.6
        linear 0.1 rotate 75 xpos 1000 ypos 600
        linear 0.2 rotate 150 xpos 800 ypos 500
        linear 0.1 rotate 210 xpos 700 ypos 700
        linear 0.1 rotate 290 xpos 600 ypos 900
        linear 0.1 rotate 330 xpos 500 ypos 1100
    hide digi with moveoutright
    digimom "You're breathing too loud!" with vpunch
    play sound sfx_house_door_close
    stop music fadeout 3.0
    music end
    n "Digi hops in his spaceship and takes off."
    scene black with dissolve
    pause 3.0
    scene nugget_inside
    show digi flipped at center
    with dissolve
    digi "This is why I'm glad I got this spaceship."
    digi "Living at my old house was way too stressful!"
    digi "Whatever, at least that was a while ago now."
    digi "Let's hurry up and get to this party, I'm running late!"
    scene black with dissolve
    $ renpy.movie_cutscene(dumb_thing_for_route)
    play sound sfx_nugget
    scene apartment_outside with dissolve
    show digi flipped at center with moveinleft
    n "After a rather short trip, Digi shows up near Elizabeth's apartment."
    digi "Alright, almost there."
    n "As Digi is approaching Elizabeth's house, he sees someone on the streets."
    show digi happy flipped
    digi "Holy shit, is that Doug McMillon?!"
    show digi shock flipped with vpunch
    play sound sfx_hks1 noloop
    pause 0.2
    show digi shock flipped with hpunch
    play sound sfx_hks2 noloop
    pause 0.1
    show digi shock flipped with vpunch
    play sound sfx_hks2 noloop
    pause 0.3
    show digi shock flipped with hpunch
    play sound sfx_hks3 noloop
    pause 1.0
    digi "Oh, I guess he got shot. Ok."
    n "Digi knocks on Elizabeth's door."
    # Doug mcmillon dies
    play sound sfx_house_door_open
    scene apartment_3
    show anne at mid_right
    show grace at mid_mid_right
    with dissolve
    play music bedroom_day
    music bedroom_day
    show digi flipped at mid_left with moveinleft
    show grace happy at mid_mid_right
    grace "Hey Digi!"
    show anne happy at mid_right
    anne "Hi, Digi!"
    show anne at mid_right
    show grace at mid_mid_right
    grace "You're a little late, but thanks for showing up!"
    digi "Yeah sorry, I got the message last minute."
    show elizabeth at mid_right with moveinright
    eliza "Hey Digi, thank you for coming."
    show digi happy flipped
    digi "Of course! Anything for my friends!"
    eliza "Well, we don't have much planned, but at least more people showed up than I thought."
    show k22 disappointed at center with moveinright
    show k22 disappointed flipped with determination
    k22 "Hey, this party is going on all night, correct?"
    eliza "Uhm, sure?"
    eliza "We were gonna watch the turn of the new year."
    k22 "Yeah, I'm sorry, I gotta head out for now."
    k22 "I have this sort of inauguration thing to attend, and I can't miss it."
    show k22 disappointed with determination
    eliza "Alright well, I'll see ya later."
    hide k22 with moveoutleft
    pause 0.5
    show elizabeth worried with vpunch
    eliza "Wait, doesn't K-17 have to go with you?"
    show digi sad flipped
    digi "I think they are already gone."
    show digi flipped
    show elizabeth
    eliza "Great, well I hope someone can get him home."
    eliza "Feel free to mingle among the guests."
    hide digi with moveoutright
    scene apartment_1
    show luke at center
    show ges at mid_left
    show scott at right
    with dissolve
    show digi flipped at mid_left with moveinleft
    digi "Hello everyone!"
    luke "Heya, Digi!"
    ges "What's up, eh?"
    digi "Is CS here at this party?"
    show grace at left with moveinleft
    grace "He was invited to come, but I think he was busy or something."
    digi "Oh, dang."
    hide grace with moveoutright
    luke "Also Digi, I'm sorry about what happened at CS' party."
    show digi thinking flipped
    digi "With the projector?"
    luke "Yeah..."
    show digi flipped
    digi "It's okay, I was super pumped to finally set up a projector, but if you couldn't do it, I guess I probably couldn't either."
    luke "Linus couldn't even figure it out, and he's my boss!"
    # next room
    scene apartment_2
    show billy at mid_right
    show grace at center
    show anne at mid_left
    with dissolve
    pause 0.5
    show grace happy flipped
    grace "Hi Billy!"
    billy "Hi, it's Billy!"
    show grace
    grace "Do you have anything for sale?"
    billy "Let me think..."
    billy "I have been working on a big project, and I need a lot of my supplies for it."
    billy "On the other hand, I just came back from France, so I do need to gain some money."
    billy "Sure! Whaddya want?"
    show grace happy flipped
    grace "Uhm, how much do you have?"
    show anne angry with vpunch
    anne "Grace!"
    show grace sad
    anne "We can't buy everything, we barely have any money!"
    grace "Can I buy like, one thing?"
    billy "I can give you a special offer of $9.95 for one item!"
    show grace
    anne "Fine, go ahead. But only for one thing!"
    show anne
    show grace worried flipped
    grace "Do you have uhh..."
    grace "Mighty Putty?"
    show grace
    billy "Sure thing!"
    billy "Lemme go grab it real quick."
    hide billy with moveoutright
    n "As Billy runs out to his car, an ad starts playing on the TV."
    phil "Hi, Phil Swift here for Flex Tape!"
    show grace worried
    grace "Ooh! Anne, can we buy--{w=0.5}{nw}"
    show grace sad
    show anne angry with vpunch
    anne "Grace, knock it off!"
    # next room
    scene apartment_3
    show bubble flipped at left:
        zoom 0.6
    show ges flipped at mid_left
    show pomni at center
    show scott at right
    show terry at mid_right
    show rex at mid_right_right
    show digi flipped at left
    with dissolve
    bbl "Oh my God, is that Pomni?"
    ges "Fuckin' a rights, bud!"
    terry "I don't I could fuck any rights, I'm a vegan."
    pomni "H... Hi..."
    show pomni think
    pomni "I think I'm lost again..."
    rex "Not to fear, clown girl. Let me show you to the door."
    show pomni concern
    pomni "No-- Thanks, I'm just..."
    pomni "I feel like, I keep finding myself stuck in these wacky scenarios!"
    show pomni
    scott "Tell me about it! I've had to deal with a blue border around my vision for GOD knows how long!"
    # Reversi
    stop music fadeout 3.0
    music end
    n "As the guests are conversing, Elizabeth walks in to grab everyone's attention."
    show elizabeth at center with moveinright
    eliza "Hey everyone!"
    eliza "I would like to play a game with y'all."
    eliza "I'm sure some of you may remember this from CS' party."
    show reversi_box at manual_pos(0.4, 0.6, 0.5) with dissolve:
        zoom 0.5
    eliza "It's Reversi!"
    eliza "I decided to get the game myself because I liked it so much!"
    eliza "Who would like to play?"
    digi "Sure, I'll play a round."
    eliza "Who would you like to verse?"
    jump play_mika_reversi

    # Presents
label dx_eliza_party_after:
    stop music fadeout 3.0
    music end
    scene apartment_1
    show elizabeth flipped at center
    with dissolve
    play music mm_complete
    music mm_complete
    eliza "Alright, I'm gonna open my gifts!"
    eliza "The first one is from Billy Mays!"
    show green_now at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    n "Elizabeth pulls out a bottle of Green Now."
    eliza "Hey thanks!"
    eliza "I guess I can be... green?"
    billy "...Yeah!"
    hide green_now with dissolve
    billy "I don't entirely remember pitching this one."
    eliza "Next up: we got a gift from Terry Lesler."
    show pumpkin at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    eliza "It's a... pretty big pumpkin."
    terry "It's the most vegan fruit I know, make sure to take good care of it."
    eliza "Well uhh, I'll try."
    hide pumpkin with dissolve
    eliza "Now we have, Scott's gift."
    show wiiu at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    eliza "It's a... Wii U?"
    scott "A European Wii U!"
    eliza "I don't think I ever had a Wii, but I guess I could give it a go."
    hide wiiu with dissolve
    eliza "This gift is from... Rex Mohs."
    show dkc at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    show elizabeth worried flipped with vpunch
    eliza "Donkey Kong country tropical freeze?"
    show elizabeth angry flipped
    eliza "Stalin loved this game!"
    rex "As much as I love the economy."
    "Scott, Terry and Rex" "Clapping and shouting about the economy"
    show elizabeth flipped
    hide dkc with dissolve
    eliza "Alright, this next gift is from Pomni."
    show floppy at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    eliza "Hey, a Floppy Disk! I remember these!"
    pomni "Yeah..."
    hide floppy with dissolve
    eliza "This next gift is... Luke's!"
    show fish_finder at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    eliza "Is this a... fish finder?"
    luke "Yeah, I was at Scheels trying to find tech stuff, and this is all they had."
    hide fish_finder with dissolve
    eliza "I'm sure I can try this out next summer."
    eliza "Alright, let's open Ges' gift."
    show 1911 at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    eliza "Wow, this is pretty!"
    ges "I was hoping you'd like it, eh?"
    eliza "I'll have to try this out later."
    hide 1911 with dissolve
    eliza "This one is Bubble's gift."
    show walkie as first at manual_pos(0.6, 0.7, 0.5) with moveinbottom:
        zoom 0.25
    show walkie as second at manual_pos(0.65, 0.7, 0.5) with moveinbottom:
        zoom 0.25
    eliza "Oh cool! A pair of walkie talkies!"
    bbl "I didn't know what to get you, so I assumed you would like this."
    eliza "Yeah, I like it!"
    hide walkie as first
    hide walkie as second
    with dissolve
    eliza "Alright Anne, what did you get me?"
    show anne_shirt at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    eliza "Heh, cool t-shirt!"
    anne "Thanks! It was one of the best things I could muster up this year."
    hide anne_shirt with dissolve
    eliza "Finally, we have Grace's gift."
    show blockbuster at manual_pos(0.6, 0.7, 0.5) with moveinbottom
    show elizabeth worried flipped with vpunch
    eliza "Wh--"
    show elizabeth flipped
    eliza "Grace, Blockbuster doesn't exist anymore..."
    grace "What do you mean? Anne goes there all the time!"
    hide blockbuster with dissolve
    n "Anne angrily looks at Grace."
    digi "I mean, there technically is still one left..."
    n "Elizabeth reads the room."
    eliza "I'm sorry, thank you Grace."
    eliza "Well, thank you all for the gifts!"
    eliza "I honestly didn't expect this many people to come."
    digi "I mean hey, you invited us."
    eliza "I guess so."
    scene black with dissolve
    stop music fadeout 3.0
    music end
    n "After the presents, everyone started to wrap up and head home."
    scene apartment_3
    show elizabeth at center
    show digi flipped at left
    with dissolve
    digi "Bye Elizabeth! I'll see you around!"
    eliza "See ya, Digi!"
    show digi with determination
    hide digi with moveoutleft
    play sound sfx_house_door_close
    pause 2.5
    show k17 at right
    k17 "Hi!"
    show elizabeth worried flipped with hpunch
    eliza "Huh?"
    show elizabeth flipped
    eliza "Oh yeah, you lost your ride."
    show k17 disappointed
    k17 "Yeah, it looks like I'm gonna miss the inauguration as well..."
    show k17
    k17 "...But at least I got to spend time with you again!"
    eliza "What's this inauguration that you need to attend, if I may ask?"
    k17 "Well, every new year, a new person becomes a K-type, just like me."
    k17 "They get imbued with the memories of the current year, and we get to see what their personality is."
    eliza "Huh."
    eliza "I can see why CS was confused by your existence."
    eliza "Well, I guess you can stay here for now..."
    show k17 happy
    k17 "Awesome!"
    scene black with Dissolve(5.0)
    return

label play_mika_reversi:
    menu:
        "Who would you like to play against?"
        "Billy":
            $ reversi_difficulty = ReversiAI.BILLY
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Elizabeth":
            $ reversi_difficulty = ReversiAI.ELIZABETH
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Terry":
            $ reversi_difficulty = ReversiAI.TERRY
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Scott":
            $ reversi_difficulty = ReversiAI.SCOTT
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Rex":
            $ reversi_difficulty = ReversiAI.REX
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Pomni":
            $ reversi_difficulty = ReversiAI.POMNI
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Luke":
            $ reversi_difficulty = ReversiAI.LUKE
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Ges":
            $ reversi_difficulty = ReversiAI.GES
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Bubble":
            $ reversi_difficulty = ReversiAI.BUBBLE
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
        "Anne":
            $ reversi_difficulty = ReversiAI.ANNE
            minigame "play_reversigame" "dx_eliza_party_after" "dx_eliza_party_after"
            return
