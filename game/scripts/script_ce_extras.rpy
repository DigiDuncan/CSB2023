label ce_extras_cruz:
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    scene cs_bedroom2 with dissolve 
    n "CS wakes up the day of the party."
    cs "Woohoo! This party is gonna be awesome!"
    cs "I am really craving some Easy cheese though, I'm gonna head to the store and get some extra."
    scene black with dissolve 
    n "CS drives to the store to get some more cheese in a can."
    scene tgt_chips with dissolve
    show cs coat disappointed at center with moveinleft
    cs "Man, I cannot find any EZ Cheese!"
    cs "I've looked everywhere, but it's not here!"
    show cs coat disappointed flipped
    n "CS sees someone moving a pallet, with a box of EZ Cheese on top."
    # play music juice_it_up
    show cs coat flipped
    cs "Yes! I need to get to that box!"
    hide cs with moveoutleft
    scene tgt_tree with dissolve
    show cs coat at mid_right with moveinright
    n "CS starts walking towards the pallet guy, but he speeds up and takes a turn."
    show cs coat disappointed with determination
    hide cs with moveoutleft 
    scene tgt_tech with dissolve 
    cs "Hey sir, I have a question!"
    scene tgt_inside with dissolve 
    n "CS starts running after the pallet, but they manage to go even faster."
    scene tgt_line with dissolve 
    cs "Hey! Please stop!"
    scene tgt_tater with dissolve 
    cs "I need that EZ Cheese!"
    scene tgt_alcy with dissolve 
    n "CS manages to start catching up, but the pallet starts heading towards the backroom doors."
    scene
    scene tgt_dairy with dissolve
    cs "Waiiit!"
    n "CS chases the man into the backroom, but once he gets in, the pallet dude and the pallet are gone."
    scene tgt_backroom with dissolve
    cs "Ah man, where did they go?"
    cs "...and why were they going so fast?"
    cs "They are definitely gonna get in trouble."
    cs "Well, I probably shouldn't be here, but I really want to find that EZ cheese."
    n "To CS' luck, an employee shows up."
    cs "Hey, have you seen a pallet with EZ Cheese back here? I just saw it come through."
    "cruz" "Yeah! Do you think you can help me throw away some of this cardboard though? It's everywhere!"
    cs "I mean, I don't work here…"
    cs "...but if i did…"
    cs "I guess I can help. It's worth it for that cheesy goodness."
    "cruz" "Thanks! I've been in deep shit today."
    "cruz" "So yeah, just take these boxes and shove them in that chute."
    cs "Got it."
    n "A half hour passes, and there is still a huge load of cardboard."
    cs "This is gonna take forever!"
    cs "Is there no one who can help us?"
    "cruz" "Hold on, I have a faster way to do this."
    "cruz" "Follow me."
    n "Cruz squeezes behind some carts and CS follows."
    n "They open a door that leads down a long staircase."
    scene archival_14 with dissolve
    n "The farther they go down, the walls turn into black brick and are lined with torches."
    scene police_interregation with dissolve
    n "As they get to the bottom, there is a room with another chute on the wall."
    n "A warm bright light glows from inside the chute."
    "cruz" "Here is the secret lava compactor, we can get it done faster by doing it this way."
    cs "Okay? I guess, that makes, sense…"
    n "As CS wonders why this exists under the Target, they manage to finish rather quickly."
    cs "Wow, I guess that was faster."
    "cruz" "Good job."
    "cruz" "Now…"
    cs "I can get my EZ cheese?"
    "cruz" "You want to know what happened to that guy pushing the pallet?"
    cs "Uhh…"
    n "Cruz takes a battle axe that was hanging on the wall."
    "cruz" "He was incompetent, and you can't leave this room!"
    cs "Wait, wha–"
    # boss battle
    scene police_interregation with dissolve
    n "As Cruz charges at CS, he moves out of the way at the last second, running into the chute and falling down into the abyss."
    cs "Welp, that was something."
    cs "Time to go look for my EZ Cheese again!"
    scene tgt_backroom with dissolve
    n "As CS heads upstairs, the building starts to shake and screams can be heard."
    cs "What the hell is going on up here?"
    n "While CS is trying to get out of the backroom, lava starts coming up through the cracks in the floor!"
    cs "Hot damn!"
    cs "I need to get the fuck outta here!"
    n "CS manages to dodge all the debris falling around him, and makes it to the sales floor."
    scene tgt_tree with dissolve 
    n "Once he gets there, he finds an employee lost in trance amidst the chaos."
    cs "Hey dude, are you okay? We need to leave!"
    tgt_worker "It's… happening."
    cs "What? Are you crazy?"
    n "The employee spends the next 20 minutes lore dumping CS."
    cs "So you're telling me, there have been multiple generations of human sacrifices under this building, and that one guy falling down the chute just awakened a dead god?"
    tgt_worker "Yes, that is correct."
    cs "Well fuck this! I'm getting to my car, I don't care!"
    tgt_worker "No, you can't. You can't escape, CS."
    cs "Yes I can!"
    n "CS tries to run out of the building, but his legs feel like molasses, and debris keeps blocking his way."
    scene tgt_inside with dissolve
    cs "Nooo!"
    n "The ancient demon bursts out of the ground, and bellows a rather annoying sound."
    "demon" "Beep! Beep! Beep!"
    cs "Huh?"
    scene cs_bedroom2
    n "CS' alarm is buzzing."
    n "CS jolts up in a cold sweat."
    cs "Wait what?"
    cs "That was… just a dream…"
    cs "Oh man, what was I dreaming about?"
    cs "The store was falling apart, and there was lava everywhere…"
    n "CS takes a moment to catch his bearings before he fully wakes up."
    $ renpy.end_replay()
    return

label ce_extras_poop:
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    scene tgt_tree
    show cs coat disappointed at mid_right
    show shopping_cart flipped at manual_pos(0.5, 1.1, 0.5)
    show pomni flipped at mid_offscreen_left
    show shopping_cart as second at manual_pos(0.2, 1.1, 0.5)
    with dissolve
    pomni "Oh!"
    show pomni think flipped
    show cs coat worried flipped
    cs "Sorry! That was an intrusive thought!"
    n "Pomni blushes, and immediately runs away."
    hide pomni with moveoutright
    show cs coat disappointed flipped
    cs "Huh, okay…"

    scene tgt_outside
    show cs coat hat
    show shopping_cart at manual_pos(0.7, 1.1, 0.5)
    with dissolve
    n "As CS is about to get into his car, Pomni runs up to him."
    show pomni concern at left with moveinleft
    pomni "Hey, uhh, weird question…"
    show cs coat surprised flipped
    show pomni think flipped
    pomni "Can I… come, home… with you?"
    show cs coat disappointed flipped
    cs "Uhh…"
    show pomni concern flipped
    pomni "I don't know, it was just the way you booped me, in the store, I just…"
    cs "I mean, I guess if you want to, you can come check out my house?"
    show pomni flipped
    cs "But I need to get to bed early tonight, I have a big day tomorrow."
    pomni "Of course!"
    show cs coat with determination
    hide cs with moveoutright 
    hide pomni with moveoutright
    scene black with dissolve
    play sound sfx_car_door_open
    n "Pomni gets in CS' car, and they head to his house."
    play sound sfx_car_approach_stop volume 5.0 fadein 1.0
    scene cs_house_snow
    play sound sfx_doorslam
    show cs coat hat at center
    show pomni flipped at mid_left
    with moveinleft
    cs "Well, here it is!" 
    show pomni concern flipped
    pomni "Wow! It's so big!"
    show cs coat hat happy
    cs "Yeah, all those patreon donations add up!"
    show cs coat hat
    cs "Come in, I'll show you around."
    hide cs
    hide pomni
    with moveoutright
    play sound sfx_house_door_close
    scene cs_bathroom
    show cs at mid_right
    show pomni flipped at mid_left
    with move
    show cs flipped with determination 
    cs "So yeah, in here is my bedroom."
    show pomni concern flipped
    pomni "You have such a cool house!"
    cs "I got something even better."
    cs "Watch this."
    cs "Athena, galaxy mode."
    play sound sfx_fabeep
    pomni "Wow!"
    cs "You like it?"
    show pomni think flipped
    pomni "I like you."
    n "CS smirks."
    cs "Athena, romance mode."
    "athena" "Okay, switching to–"
    "athena" "Poop mode."
    play sound sfx_fabeep
    pause 1.0
    scene cs_bathroom_open
    show cs_bathroom_open_fg
    show cs disappointed
    show pomni flipped
    pause 0.5
    cs "Athena wait–"
    # play music cs_poop_song
    pause 1.0
    cs "Athena stop!"
    show cs worried
    "athena" "I'm sorry, I don't know what you're–"
    show cs scared
    cs "Athena turn off!"
    play sound sfx_house_door_open
    hide cs with easeoutright
    n "CS frantically tries to turn his smart device off."
    cs "ATHENA TURN OFF!"
    play sound sfx_power_out volume 0.25
    n "CS unplugs his machine."
    play sound sfx_house_door_close
    show cs disappointed flipped
    cs "Must have been some kind of glitch…"
    n "The song continues to play."
    cs "I have to…"
    cs "Flush it, to turn it off."
    show cs disappointed flipped at center
    n "CS' head turns red with embarrassment as he goes into the bathroom to flush the toilet."
    show cs disappointed flipped behind cs_bathroom_open_fg:
        linear 0.5 zoom 0.7 pos (0.5, 0.9)
    play sound2 sfx_toilet_flush noloop
    pause 1.5
    "athena" "New user weight detected."
    cs "Oh for fucks sake."
    n "CS sits on the toilet, and stands up to flush again."
    play sound2 sfx_toilet_flush noloop
    stop music
    pause 2.0
    "athena" "Congratulations, CS on: Doing a poop."
    show cs disappointed flipped at manual_pos(0.4, 0.35):
        linear 0.5 zoom 1.0 pos (0.4, 0.2)
    cs "So uhh, sorry about that…"
    "athena" "Now printing: Big Boy Certificate."
    scene cs_bathroom
    show pomni flipped at right
    show cs worried flipped with vpunch
    play sound sfx_house_door_close
    n "CS slams the door."
    cs "So uhh, did you wanna do anything else?"
    hide pomni with easeoutleft
    show cs disappointed flipped
    cs "Athena, left hand mode."
    play sound sfx_fabeep
    # play music party_rock fadein 3.0
    scene cs_bathroom_open
    show cs_bathroom_open_fg
    play sound sfx_house_door_open
    show cs disappointed flipped

    show cs disappointed flipped behind cs_bathroom_open_fg:
        linear 0.5 zoom 0.7 pos (0.5, 0.9)
    pause 0.5
    scene cs_bathroom
    play sound sfx_house_door_close
    pause
    $ renpy.end_replay()
    return
