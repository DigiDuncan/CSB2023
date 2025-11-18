# TODO: make this book only appear if you've defeated Perfect Tate.
# TODO: finish art for said book.
# TODO: make sprites for tate_cyan

label book_celestial_sightseeing:
    play music we_will_meet_again
    music we_will_meet_again
    pause 1.0
    tate_cyan_offscreen "Ah, so {i}that's{/i} where the conduit landed."
    tate_cyan_offscreen "What a fitting location."

    scene nursing_home
    show tate at mid_mid_left
    with dissolve

    # TODO: hey can baker or someone pls go through all my dxcom audios and make em louder? thanks
    dxcom tate_sick

    tate_cyan_offscreen "It's kinda perfect, actually."
    cs "Huh?"
    tate_cyan_offscreen "Hello, CS."

    show cs disappointed flipped at offscreenright
    show cs disappointed flipped at right with MoveTransition(1.0)
    pause 1.0

    cs "Who are you? And how do you know my name?"
    cs "And... {nw}"
    show cs worried flipped
    extend "what {i}happened{/i} to you?"
    tate_cyan_offscreen "Ah... I was expecting them to have already told you."
    show cs disappointed flipped
    "..."
    tate_cyan_offscreen "...{fast} But... at the same time..."
    tate_cyan_offscreen "I suppose, knowing us, it makes sense, too, that they have not."
    show cs worried flipped
    cs "{i}Huh?!"
    tate_cyan_offscreen "Ah-- it's... kind of... a {i}lot."
    tate_cyan_offscreen "I'll try to make it make sense."
    show cs disappointed flipped
    tate_cyan_offscreen "I know you already know Tate."
    tate_cyan_offscreen "In a way, I am also Tate. That is how I know you."
    $ persistent.seen.add("tate_cyan")
    tate_cyan "Through this book, I can see what goes on in your realm."
    tate_cyan "As for what happened to my body..."
    tate_cyan "Don't worry about the details."
    tate_cyan "Just know that forbidden magick is typically forbidden for a reason."
    show cs worried flipped

    # TODO: maybe redo this later
    if fun_value(FUN_VALUE_RARE):
        cs "Magick...? With a K?"
        cs "Tate's a {i}witch?!"
        show cs disappointed flipped
        tate_cyan "Look, I know {i}you{/i} can read the text box, too, and that we can {i}both{/i} break the fourth wall, but could you maybe {i}not{/i} do that here?"
        tate_cyan "This connection isn't exactly stable to begin with, y'know."
        tate_cyan "Anyway, no, we are not witches."
    else:
        cs "Magick...? Like... {i}real{/i} magick?!"
        cs "Tate's a {i}witch?!"
        show cs disappointed flipped
        tate_cyan "Oh, heavens, no."

    tate_cyan "Where we come from, we'd have been hanged for that."
    tate_cyan "Well... {nw}"
    show cs worried flipped
    extend "{size=-5}I suppose they {i}already{/i} wanted to do that, just for... {nw}"
    show cs scared flipped
    extend "{size=-5}slightly {i}different{/i} reasons..."
    "..."
    tate_cyan "Anyway, no."
    show cs disappointed flipped
    tate_cyan "We were... in a bad spot."
    tate_cyan "Desperate for an escape, we decided to... open a door... to... outside."
    tate_cyan "Literally to anywhere else. We did not have a destination in mind."
    tate_cyan "In hindsight, perhaps that lack of clear direction contributed to... all of this."
    n "Tate gestures vaguely towards the nearby IV pole."
    "..."

    if fun_value(FUN_VALUE_COMMON):
        tate_cyan "I can tell that you're still unsatisfied."
        show cs angry flipped
        cs "100%%, even."
    else:
        tate_cyan "I can tell that you still aren't satisfied."
        show cs angry flipped
        cs "Not even 50%%."

    show cs surprised flipped
    tate_cyan "Very well."
    tate_cyan "We knew we weren't going to survive if we stayed."
    tate_cyan "We also figured that we'd at least die a much more {i}interesting{/i} death if we had tried and failed than if we had never tried at all."
    show cs disappointed flipped
    cs "Okay, but... what exactly {i}happened?"
    cs "I still don't get how you ended up... like {i}this."
    tate_cyan "Ah..."
    tate_cyan "You see, this very book was discovered to be missing during the last moments of the ritual."
    tate_cyan "While we did barricade the door before we began, we knew that it wouldn't hold for long if--{w=0.5}{nw}"
    show cs surprised flipped
    cs "So you {i}stole{/i} the book."
    tate_cyan "...!" with vpunch
    n "Tate anxiously scratches at something under the neck of their shirt."
    cs "... What happened next?"
    tate_cyan "Ah..."
    tate_cyan "O-{w=0.1}Our hands shook as we completed the circle."
    tate_cyan "Sweat and tears fell onto the stone and made the ink start to run."
    tate_cyan "The final sigil was rushed and came out sloppy. But we had no time to redo it."
    show cs worried flipped
    tate_cyan "We could hear the door splintering behind us."
    tate_cyan "We had no choice but to see it through."
    tate_cyan "With a flick of our blade, the portal opened."
    tate_cyan "With nothing left for us in that world..."
    show cs scared flipped
    tate_cyan "We jumped."
    "..."
    "..."
    show cs worried flipped
    tate_cyan "In certain circles, it is whispered..."
    tate_cyan "They say it's not about the technique, or even about how much experience a practictioner has..."
    tate_cyan "They say it's all about one's own inner strength, and about the intention behind one's actions..."
    tate_cyan "With these words held close to our heart, we had hoped that our will to live would see us through..."
    tate_cyan "You know... {i}in one piece."
    "..."
    "..."
    tate_cyan "As you can probably tell, we were lied to."
    show cs disappointed flipped
    cs "Jeez... you're speaking in riddles."
    cs "So there's... {nw}"
    show cs worried flipped
    extend "{i}two{/i} of you?"
    cs "Did you, like, get split into pieces or something?"
    n "Tate takes a nervous sip from their juice box."
    n "CS notices that their hands look almost... skeletal."
    "..."
    tate_cyan "{color=#00FFFF}Mind{/color}, {color=#FF00FF}body{/color}, and {color=#FFFF00}spirit.{/color}"
    tate_cyan "In many ways, {color=#FFFF00}the Tate you know{/color} will live on no matter what happens to the rest of us."
    tate_cyan "As for {color=#00FFFF}me{/color}..."
    tate_cyan "My new IV bags should be in soon. You should probably get out of here before the nurse comes to hook me back up to that damn pole."
    cs "Wait, why do I have to leave? I still have so many questions..."
    tate_cyan "Well, {i}I{/i} want to rest, and {i}you{/i} didn't sign in at the front desk."
    tate_cyan "I don't think either of us wants to deal with any questions from security."
    show cs disappointed flipped
    cs "I guess that's fair..."
    tate_cyan "When you get back, will you please put that book back where you found it?"
    cs "Sure thing."
    tate_cyan "And-- ah! Please do me one other favor."
    tate_cyan "Don't tell the Tate of your world that we have met."
    tate_cyan "You know how I-- well, I guess, you know how {i}we{/i} can get."
    tate_cyan "I don't need that one asking too many questions."
    tate_cyan "I {i}certainly{/i} don't need them trying to... {nw}"
    show cs worried flipped
    extend "{i}break anything else{/i} on their own."
    tate_cyan "I simply don't have the time to babysit that one right now. I need to focus on my recovery."
    cs "Well... "
    show cs disappointed flipped
    extend "alright..."
    cs "I, uh... {nw}"
    show cs flipped
    extend "I hope you get well soon, other-Tate!"
    tate_cyan "Thank you."
    tate_cyan "And I hope {i}you{/i} enjoy the rest of your adventure."
    show cs disappointed flipped
    cs "Thanks{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?"

    scene black with dissolve

    pause 1.5
    tate_cyan "And don't go jumping through any wormholes, y'hear?!"
    pause 1.0
    n "CS closes the book."
    n "As he does, it suddenly feels heavier in his hands."
    n "Curiosity continuing to eat at him, he tries to reopen it, but the pages do not budge. It is as if they have turned to stone."
    n "Defeated, he slips the strange tome back into its place on the shelf."
    return

label book_underpants:
    # Hi, Tate, I assume you'll see this at some point.
    # This is a reference to a Mad Lib Pakoo and Mika wrote at 3AM and sent me via voice message.
    # There's a reason this barely makes sense.
    # If you're doing a grammar pass on this, please don't change the wording without consulting me.
    # Just want to make sure the jokes stay intact.
    # Thanks!
    # -- Digi

    play music school volume 0.4 if_changed
    music school
    scene classroom
    show george at left
    show harold at right
    show pakoo at center
    show weird_al at offscreenright
    show toxic_mikas at manual_pos(1.5, 1.0, 1.0):
        zoom 0.6
    with dissolve
    pause 0.5
    n "George, Harold, and Pakoo are busy studying the wonders of gooey jugular veins."
    play sound sfx_small_spill volume 8
    n "Their new science teacher, Mr. Weird Al Yankovic, spills some smelly sulfuric acid on a pile of toxic Mikas!"
    show harold at center
    show pakoo disappointed flipped at mid_left behind george
    show weird_al at right
    show toxic_mikas at manual_pos(1.1, 1.0, 1.0):
        zoom 0.6
    with move
    $ collect("toxic_mikas")
    weird_al "Whoops!"
    n "Suddenly, the pile begins to morph into a giant evil Mika!"

    # not sure why it doesnt like zorder here but w/e
    show toxic_mikas at center behind pakoo
    show weird_al behind toxic_mikas
    show harold at center
    with move

    hide toxic_mikas
    show expression DynamicDisplayable(Pixellated.pixellated, widget='mika', delay=0.5, steps=8) at t_evil_mika behind pakoo
    play sound sfx_glitch_in
    with dissolve

    play sound sfx_bossappears
    hide expression DynamicDisplayable(Pixellated.pixellated, widget='mika', delay=0.5, steps=8)
    show mika at t_evil_mika behind pakoo

    show david at offscreenright
    with Dissolve(0.1)
    with vpunch
    pause 1.0
    show david at mid_right with MoveTransition(0.25)
    david "Help!"
    david "A giant evil Mika just stepped on my lunch bucket and ate a Van Halen!"
    show mr_krupp at offscreenleft with determination
    show mr_krupp at left with MoveTransition(0.25)
    mr_krupp "Oh,{w=0} no! The poor lunch box!"
    show george at offscreenleft
    show harold at offscreenleft
    show pakoo flipped at offscreenleft
    with MoveTransition(0.25)
    n "George, Harold, and Pakoo try to escape by hiding behind a neutrino."
    play sound sfx_addy_snap
    n "Pakoo snaps his fingers."
    # TODO: hey baker, think you can clean up this trash smiling edit for me? thx - tate
    show mr_krupp grin with dissolve
    n "Soon, a digital grin comes across Mr. Krupp's face as he drops his dark tie and runs to his office."
    show mr_krupp grin at offscreenleft with MoveTransition(0.25)
    play sound sfx_house_door_close
    pause 2.0
    play sound sfx_punch
    with hpunch
    show cpt_underpants at left with moveinleft
    n "Soon, Captain Underpants punches through the wall!"
    show cpt_underpants at mid_offscreen_left with MoveTransition(0.25)
    pause 0.25

    show slime16 at offscreenleft:
        rotate 90
    $ collect("slime16")
    show cpt_underpants at manual_pos(0.3, 1.0, 1.0) with MoveTransition(0.1)
    show cpt_underpants at mid_offscreen_left
    play sound sfx_tf2_pickup_metallic
    show slime16 at center_left:
        rotate 90
        linear 0.1 rotate 0
    with MoveTransition(0.1)

    n "He grabs a slimy M-16 and hits the monster on its elbow!"
    show slime16 fire
    play sound sfx_hks1
    show mika at right behind weird_al with MoveTransition(0.25)
    show slime16
    with hpunch
    mika "Ouchies!"
    n "The monster turns and kicks Captain Underpants in his esophagus!"
    show mika at center:
        linear 0.25 xzoom -1
        linear 0.25 xzoom 1
    show cpt_underpants at manual_pos(0.3, 1.0, 1.0)
    show slime16 at manual_pos(-0.5, 0.25, 0.5):
        linear 0.5 rotate 720
    with MoveTransition(0.25)
    play sound sfx_punch_alt
    with vpunch
    pause 1.0
    show pakoo flipped at mid_left zorder 3
    show cpt_underpants at manual_pos(0.4, 1.0, 1.0)
    show gamebarrel at manual_pos(-0.5, 0.9, 0.5) zorder 4:
        zoom 0.6
    with MoveTransition(0.25)

    play sound sfx_mc_brew
    show dookie_milk_jar at manual_pos(0.4, 0.6, 0.5) zorder 3 with dissolve:
        zoom 0.5
    $ collect("dookie_milk_jar")
    n "Pakoo quickly mixes up a bottle of chocolate milk with bloody piles of dog shit!"
    george "Hey, Pakoo? Where did you find the jar of crazy stuff?"
    show gamebarrel at manual_pos(0.1, 0.9, 0.5) with MoveTransition(0.5):
        zoom 0.6
    $ collect("gamebarrel")
    pakoo "It was right here, next to this barrel of toxic yellow Game Boys."
    pause 1.0
    harold "Oh, that makes sense."
    play sound sfx_water_shake
    show dookie_milk_jar:
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        repeat 25
    n "Pakoo shakes up the strange mixture and throws it at the monster!"
    show pakoo flipped at mid_left
    #show mika at right
    stop sound
    play sound sfx_mc_throw volume 10

    show dookie_milk_jar at manual_pos(0.5, 0.3, 0.5):
        linear 0.25 rotate 130
    with MoveTransition(0.1)
    hide dookie_milk_jar

    play sound sfx_mc_bottlehit volume 3
    hide dookie_milk_jar with Dissolve(0.1)
    show mika:
        parallel:
            linear 0.25 rotate 90
        parallel:
            linear 0.25 xpos 2.5
        parallel:
            linear 0.25 ypos 2.0
    show realistic_explosion_anim at manual_pos(0.8, 0.7, 0.5) behind weird_al:
        subpixel True
        zoom 20
    play sound2 sfx_explosion noloop
    with vpunch
    mika "Woohoo!"
    n "The monster dies of a massive right toe attack!"
    pause 1.0
    george "{i}That{/i} makes sense, too."
    play sound sfx_small_spill volume 3.0
    n "Unfortunately, some of the mixture splashes onto Captain Underpants' head, and he turns back into Mr. Krupp."
    play sound sfx_glitch_in
    hide cpt_underpants
    hide slime16

    show expression DynamicDisplayable(Pixellated.pixellated, widget='mr_krupp', delay=0.5, steps=8) at manual_pos(0.4, 1.0, 1.0)
    show mr_krupp at manual_pos(0.4, 1.0, 1.0) behind weird_al
    with dissolve
    pause 1.0
    hide expression DynamicDisplayable(Pixellated.pixellated, widget='mr_krupp', delay=0.5, steps=8)
    show mr_krupp at center behind weird_al with move

    pause 1.0
    mr_krupp "Holy bright {i}penguins!"
    mr_krupp "I'll bet that George, Harold, and Pakoo are responsible for this mess!"
    show pakoo worried flipped
    mr_krupp "For your punishment, you all must chop in the broom closet for {i}negative eight hours!"

    pause 0.5
    scene black with dissolve
    pause 1.0

    scene broom_closet
    show george at left
    show harold at right
    show pakoo at center
    with dissolve
    pause 1.0
    george "This has got to be the {i}dumbest{/i} story we've ever been in!"
    harold "Don't blame {i}me,{/i} Pakoo wrote it!"
    return

label CSB3_EBEEP12024FDEADNYWFFEAGM:
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
