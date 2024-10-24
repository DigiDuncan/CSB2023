label true_back_home:
    stop music2
    scene cs_house with dissolve
    play music park_theme volume 0.5 if_changed
    music park_theme
    if fun_value(FUN_VALUE_MUSIC):
        n "After listening to Billy's many themes, they drive past the park next to CS' house."      
    else:
        n "After the long and treacherous journey, CS finally arrives at his house."
    show arceus flipped at left with moveinleft
    arceus "We made it back to your house, CS!"
    show cs at center with moveinleft
    cs "Finally, I'm home..."
    show cs flipped
    cs "Arceus, thank you so much for everything on this trip. I couldn't have done it without you."
    arceus "Aww, it was nice helping ya here."
    cs "You too, Billy."
    show billy at mid_left behind arceus with moveinleft
    billy "No problem!"
    cs "Well, I guess I should get some rest."
    show cs happy flipped
    cs "If you guys want, we can have a party at my place tomorrow to celebrate getting through all this shit!"
    show arceus happy flipped
    "Arc and Billy" "Hell yeah!"
    show arceus at left with determination
    hide billy with moveoutleft
    hide arceus with moveoutleft
    n "As CS says goodbye to his friends, a familiar but upsetting voice can be heard at the front of CS' house."
    stop music fadeout 1.0
    music end
    show cs scared flipped
    ed "{i}You!" with hpunch
    show cs worried at left with moveinleft
    n "CS and the gang look towards CS' front porch, where Richard and Ed are waiting angrily for him."
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    show ed at right
    show rich at mid_mid_right behind ed
    with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        ed "I've been listening to Alfred's theme while waiting for you."      
    else:
        ed "I have been waiting for you for quite some time now."
    rich "We've been trying to stop you for a while now, but this is the final stop for you."
    show cs disappointed
    cs "HoH SiS?! What do you guys still want from me?"
    ed "What do you think, CS? After you put Wesley in the hospital? After you crippled most of our workers?"
    cs "Well, you guys scammed me out of my money and broke my computer! Of {i}course{/i} I wanted some kind of revenge!"
    ed "Why do you think this all started?"
    cs "I-{w=0.5} I don't know, because you're evil?"
    ed "CS, you made a laughingstock of our company long ago."
    ed "When you made that parody video of us that you call a \"YTP\", people wouldn't stop harrassing us about it."
    rich "You tried to humiliate us with your videos. You made others think we were a joke!"
    ed "You see, my ancestors came from the planet JoJ many years ago to start a foundation company."
    ed "It was the best damn foundation company in the world."
    ed "We repaired more than 50 percent of all foundations on the planet, and now... {i}you.{/i}"
    ed "You. You embarrassed us with those silly, stupid videos that dragged our family company through the mud."
    rich "That's why Ed wanted to get revenge on you. That's why we destroyed your computer, CS."
    cs "I don't understand..."
    if persistent.true_ending:
        menu:
            "Fight them!" (type = "bad"):
                jump true_fighthohsis
            "Negotiate with them!" (type = "true"):
                jump true_talktohohsis
            "Tell it like it is!" (type = "bad"):
                jump true_fuckuphohsis
            "Call Copguy!":
                jump true_copsathohsis
    else:
        menu:
            "Fight them!" (type = "bad"):
                jump true_fighthohsis
            "Negotiate with them!" (type = "true"):
                jump true_talktohohsis
            "Tell it like it is!" (type = "bad"):
                jump true_fuckuphohsis

label true_talktohohsis:
    cs "I never intended to harm your company. I just thought that the video was a good source to YTP."
    cs "I'm sorry about all those prank callers. I even made a video telling people to stop prank calling you."
    cs "I never had bad intentions for you guys... honestly, it was also kind of like a free promotion."
    ed "Well, I'm sorry, CS, but it's too late."
    ed "Richard, get the JoJ UFO and vaporize the house."
    stop music fadeout 1.0
    show anno at offscreenleft
    play music track_3 volume 0.4 if_changed
    music track_3 
    if fun_value(FUN_VALUE_MUSIC):
        show anno at center behind doug with moveinleft
        anno "Track 3!!!"
        show cs angry
        cs "C'mon Anno, this is an important moment!"
        ed "Yeah, is that the best you can do?"
        anno "Sorry guys, I honestly didn't get enough sleep for the final act."
        show cs disappointed
        cs "Well it's over now, we'll do another take later, let's keep going so we have more practice for the final take."
    
    else:
        anno_offscreen "Wait!!!"
        n "A voice can be heard behind the group running up to them."
        cs "Anno?"
        show anno at center behind doug with moveinleft
    anno "You guys can't just destroy CS' house!"
    ed "Why not?"
    anno "I don't know, because..."
    anno "CS wasn't trying to harm you!"
    show arceus flipped at mid_left_left with moveinleft
    arceus "Yeah, CS' videos are hilarious, and honestly, if I knew you guys before this, I would've called you up for help on my house."
    arceus "If, y'know, I didn't go after that one politician."
    ed "Well, okay, but--"
    n "Even more of CS' friends show up at the scene."
    show cs at left
    show linus at mid_left behind phil with moveinleft
    linus "Yeah, I loved those videos about HoH SiS, and we'd love for you to come and fix up some of the damages at the LTT offices."
    show taran flipped at mid_mid_left behind cs with moveinleft
    show luke at mid_left_left behind cs with moveinleft
    show colton at default behind doug with moveinleft
    taran "What damages?"
    luke "Y'know, when Linus ran his car into the back of the building?"
    colton "Finally, something that wasn't my fault."
    show michael at mid_mid_left behind cs with moveinleft
    michael "If I get my chocolate cake, you fellows at HoH SiS can fix up my house too."
    show phil at mid_left behind cs with moveinleft     
    phil "I can help too, with the power of Flex Tape!"
    show doug at center behind cs with moveinbottom
    doug "I don't know what I'm doing here, but yeah, good job, guys!"
    show cashier at mid_mid_right behind cs with moveinleft
    cashier "Yeah! Go CS!"
    show pakoo happy at center with moveinleft
    pakoo "Yeah! Get 'em, CS!"
    show peppino at mid_left behind cs with moveinleft
    peppino "It's pizza time!"
    show digi at mid_mid_left behind cs with moveinleft
    digi "I believe in you, CS!"
    show mettaton at mid_left_left behind cs with moveinleft
    host "YOU ARE A PENCIL SHARPENING GOD!"
    show aria at mid_left behind cs with moveinleft
    aria "You're a pretty cool guy, CS."
    if nome:
        show gnome at mid_left_left with moveinleft
        gnome "Follow ze path of de forest!"
    elif clown:
        show mario flipped at mid_left_left with moveinleft
        mario "Wahoo!"
        show shaggy_too_dope at mid_left_left with moveinleft
        show violent_jay at mid_left with moveinleft
        violent_jay "Our clown sense sensed you were in danger!"
        shaggy_too_dope "Don't mess with CS! He's one of us!"
    show scott at center with moveinleft
    show scott_border with dissolve
    scott "Hey all, Scott here! I love CS and his content!"
    show pencilguy at mid_mid_left with moveinleft
    pencil "I knew you were a cool dude!"
    show border_guard at mid_mid_left behind cs with moveinleft
    border_guard "I'm important too, eh!"
    if jade or fun_value(FUN_VALUE_COMMON):
        show bubble at center behind border_guard with moveinbottom
        show bubble with vpunch
        $ persistent.seen.add("bubble")
    cs "Wow, I don't know how you all got here coincidentally, but I appreciate it!"
    show cs at left
    rich "Oh my God, that's so many people!"
    ed "Okay, okay, I get it."
    hide anno
    hide arceus flipped
    hide linus
    hide taran flipped
    hide luke
    hide colton
    hide michael
    hide phil
    hide doug
    hide cashier
    hide border_guard
    hide pakoo
    hide peppino
    hide digi
    hide mettaton
    hide aria
    hide scott
    hide pencilguy
    hide gnome
    hide bubble
    hide violent_jay
    hide shaggy_too_dope
    hide mario
    with moveoutleft
    hide scott_border with dissolve
    ed "We won't do anything to your house, and we are sorry for destroying your laptop."
    cs "And I'm sorry for injuring your coworkers."
    stop music fadeout 3.0
    music end
    ed "Wesley is still in the hospital, so, like, if you wanted to give us some more money..."
    show cs disappointed at left
    cs "Didn't you scam me out of more money than my foundation was worth?"
    ed "Oh, yeah..."
    show cs angry at left
    cs "What {i}about{/i} my foundation, anyway?"
    show cs at left
    cs "Tell you what. If you can fix my foundation, I'll pay you for that, and we put this all behind us."
    rich "What do you think, Ed?"
    n "Ed ponders for a moment."
    ed "Sure. We have a deal."
    show cs happy at left
    cs "Woohoo!"
    n "As if the crowd couldn't get any bigger, the cops show up."
    show cs at left
    show copguy flipped at center with moveinleft
    copguy "Hey, CS, we finally found HoH SiS."
    copguy "And it looks like you did, too."
    show sheriff at mid_left with moveinleft
    sheriff "Good job, Copguy. Time to put them in the slammer!"
    cs "No need, guys, we worked everything out."
    sheriff "What?!"
    copguy "Are you sure?"
    ed "Yep, we've got everything under control."
    sheriff "All this for nothing..."
    sheriff "Whatever. C'mon, Copguy, let's go."
    n "The cops get back in their car and speed off."
    show copguy with determination
    hide sheriff with moveoutleft
    hide copguy with moveoutleft
    hide ed with moveoutright
    hide rich with moveoutright
    show cs at mid_right with moveinright
    n "After all that commotion, CS finally steps up to his front door."
    show cs flipped at mid_right
    n "He looks back out towards the crowd again one more time."
    cs "This is CS..."
    cs "Signing out!"
    play sound sfx_cheers volume 0.7
    pause 2.0
    n "The crowd erupts into cheers as CS finally enters his house."
    scene black with dissolve
    pause 1.0
    $ renpy.movie_cutscene(hoh_repair)
    scene cs_room with dissolve
    play music ac_title volume 0.4 if_changed
    music ac_title
    show cs at center with moveinleft
    if fun_value(FUN_VALUE_MUSIC):
        cs "Ah, It's good to be New Leaf Title Theme again!"
        show cs happy
        cs "CS laughs."
        billy_far "Hey, now you have no room to talk!"
        show cs
        cs "Oh whatever, this take is ruined anyways."
    else:
        cs "Ah, it's good to be home again!"
    if fanbase == "both":
        jump true_ending
    elif fanbase == "ltt":
        jump true_ltt_ending
    elif fanbase == "ytp":
        jump true_ytp_ending
    else:
        jump true_ending

label true_ending:
    play music ac_title volume 0.4 if_changed
    music ac_title
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with dissolve
    n "CS looks at the monitor, which has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have you work with us again virtually. Just give us a call!\"."
    cs "I'll have to make sure to call them later!"
    if persistent.true_ending:
        menu:
            "Go to sleep" (type = "warning"):
                jump archival
            "Stream" (type = "true"):
                jump true_streaming
    else:
        $ persistent.true_ending = True
        jump true_streaming

label true_streaming:
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs happy at mid_left
    cs "Well, guys..."
    n "CS chuckles."
    cs "It's a long story..."
    if achievement_manager.get("That's All, Folks!").unlocked:
        $ achievement_manager.unlock("All Over Again")
    else:
        $ achievement_manager.unlock("That's All, Folks!")
    scene black with dissolve
    stop music2 fadeout 1.0
    $ ending_manager.mark("true")
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()

    menu:
        "Play the after story?"
        "Yes" (type = "dx"):
            jump dx_after_true
        "No" (type = "true"):
            return

label true_ytp_ending:
    play music ac_title volume 0.4 if_changed
    music ac_title
    n "CS looks over at his desk, where his old computer is sitting."
    scene cs_room_2 with dissolve
    show cs at mid_left
    cs "Oh yeah, I forgot I actually have a computer that's not a craptop."
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well, guys..."
    n "CS chuckles."
    cs "It's a long story..."
    scene black with dissolve
    stop music2 fadeout 1.0   
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return

label true_ltt_ending:
    play music ac_title volume 0.4 if_changed
    music
    n "CS looks over at his desk, where a new computer is sitting."
    scene cs_room_2 with dissolve
    n "CS looks at the monitor, which has a sticky note that says \"From LTT\"."
    show cs happy at mid_left with moveinleft
    cs "Oh my goodness, Linus got me a new PC!"
    n "There is also a note that says: \"We'd love to have you work with us again virtually. Just give us a call!\"."
    cs "I'll have to make sure to call them later!"
    show cs at mid_left
    cs "Before I head off for the night, I'll do a stream real quick."
    n "CS starts up his stream overlay and goes live on Twitch."
    cs "Hey guys, CS here! Sorry I was gone for a couple weeks!"
    n "The chat slowly comes in, confused."
    chat "Oh you're streaming?{w=0.25} I thought you were working for LTT now?{w=0.25} What happened to the YTPs?{w=0.25} Are you okay?{w=0.25} Where have you been?"
    show cs at mid_left
    cs "Well, guys..."
    cs "It's a long story..."
    scene black with dissolve
    stop music2 fadeout 1.0   
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return

label true_fighthohsis:
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    scene cs_house
    show cs disappointed at left
    show ed at right
    show rich at mid_mid_right behind ed
    n "CS challenges HoH SiS to a fight."
    show cs angry
    cs "I beat up all your workers and Wesley, I can take you guys down too!"
    cs "Let's go!"
    ed "Richard, stand back."
    hide rich with moveoutright
    cs "C'mon! Hit me!"
    ed "I'm going to refund my fist into your face!"
    show cs at center
    show ed at center
    with move
    play sound sfx_punch
    play sound sfx_punch_alt
    show cs with hpunch
    play sound sfx_punch
    play sound sfx_punch_alt
    show ed with vpunch
    play sound sfx_punch
    play sound sfx_punch_alt
    show cs with hpunch
    play sound sfx_punch
    play sound sfx_punch_alt
    show ed with vpunch
    play sound sfx_punch
    play sound sfx_punch_alt
    show cs with hpunch
    play sound sfx_alt_punch
    show cs at t_punchup with move
    show cs with vpunch
    show ed at right with move
    hide cs
    pause 2.0
    show cs disappointed at mid_left with moveintop
    cs "I no longer want the JoJ..."
    hide cs with moveoutbottom
    show ed with hpunch
    ed "Time to take a shit on the house."
    music end
    bad_end "Revenge!" "true_back_home"

label true_fuckuphohsis:
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
    cs "Yeah, I actually hate you guys, and I wanted to mess with your business!"
    cs "You guys suck and I hate you both!"
    cs "You guys {i}deserve{/i} to have your company in shambles!"
    n "Richard and Ed back up to their UFO."
    hide rich
    hide ed
    with moveoutright
    cs "Hey! Where are you guys going?!"
    cs "Come back here!"
    hide cs with moveoutright
    n "The JoJ UFO flies up over the house, then vaporizes it with a laser."
    play sound sfx_beam volume 0.6
    show beam at xstretch_in
    pause 1.5
    show cshouse_vaporized behind beam
    show beam at xstretch_out
    pause 1.0
    show cs disappointed at left with moveinleft
    with vpunch
    n "Ed flips CS the bird, then flies away."
    show cs disappointed
    pause 1.0
    cs "Fuck."
    bad_end "Time to bunk\nat Rosen's!" "true_back_home"  

label true_copsathohsis:
    stop music fadeout 3.0
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
    n "CS calls Copguy to come arrest HoH SiS."
    show cs worried
    stop music2 fadeout 1.0
    music end
    show blue_light at left
    show red_light at right
    play sound sfx_siren loop volume 0.5
    show copguy flipped at center with moveinleft
    cs "Here they are! They scammed me out of my money!"
    n "Copguy cuffs the HoH SiS members and pulls out his walkie."
    copguy "We got 'em, Sheriff. Time to put 'em in the slammer."
    hide copguy
    hide rich
    hide ed
    with moveoutright
    stop sound fadeout 1.0
    hide blue_light
    hide red_light
    show cs
    cs "Welp. That was easy."
    cs "Finally, I can rest at home."
    n "CS walks up to his house and enters."
    scene cs_room with dissolve
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    jump true_ending
