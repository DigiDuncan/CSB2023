label south_back_home_alt:
    scene cs_house with dissolve
    play music park_theme volume 0.5 if_changed
    music park_theme
    n "After the long and exciting journey, CS finally arrives at his house."
    show arceus flipped at left with moveinleft
    arceus "We made it back to your house, CS!"
    show cs at center with moveinleft
    cs "Finally, I'm home..."
    show cs flipped
    cs "Arceus, thank you so much for everything on this trip. I couldn't have done it without you."
    arceus "Aw, it was nice helping ya here."
    cs "You too, Billy."
    show billy at mid_left behind arceus with moveinleft
    billy "No problem!"
    cs "Well, I guess I should get some rest."
    cs "If you guys want, we can have a party at my place tomorrow to celebrate getting through all this shit!"
    show arceus happy flipped
    arceus "Hell yeah!" (multiple = 2)
    billy "Hell yeah!" (multiple = 2)
    show arceus at left with determination
    hide billy with moveoutleft
    hide arceus with moveoutleft
    n "As CS says goodbye to his friends, a familiar but upsetting voice can be heard at the front of CS' house."
    stop music fadeout 1.0
    music end
    show cs scared flipped
    ed "{i}You!" with hpunch
    show cs disappointed at left with moveinleft
    n "CS and the gang look towards CS' front porch, where Richard and Ed are waiting angrily for him."
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    show ed at right
    show rich at mid_mid_right behind ed
    with moveinright
    ed "I have been waiting for you for quite some time now."
    rich "We've been trying to stop you for a while now, but this is the final stop for you."
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
    menu:
        "Fight" (type = "bad"):
            jump south_fighthohsis_alt
        "Donate" (type = "true"):
            jump south_donatehohsis
        "Brag" (type = "bad"):
            jump south_braghohsis

label south_donatehohsis:
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs disappointed at left
    cs "I never intended to harm your company. I just thought that the video was a good source to YTP."
    cs "I'm sorry about all those prank callers. I even made a video telling people to stop prank calling you."
    cs "I never had bad intentions for you guys... Honestly, it was also kind of like a free promotion."
    ed "Well, I'm sorry, CS, but it's too late."
    ed "Richard, get the JoJ UFO and vaporize the house."
    stop music fadeout 1.0
    music end
    cs "Woah, woah! Hold on a second!"
    cs "I am genuinely sorry about those videos, and I am sorry if you had any business losses."
    cs "You know what? Hold on one second."
    show cs flipped with determination
    hide cs with moveoutleft
    n "CS grabs the briefcase from Arceus, takes out a few gold bars, and gives them to Ed."
    show cs at left 
    show case at left
    with moveinleft
    cs "Here, I hope this helps you guys a bit."
    rich "Woah, is that real gold?"
    n "Ed presses his fingernail into the bar and dents it."
    ed "Shit, yeah, this is the real deal."
    ed "I... don't know what to say. This is way more than enough."
    ed "You really sure about this? Even after we broke your laptop?"
    cs "Don't worry about it. We'll go our own ways after this, and I hope you guys will continue to prosper in the business world!"
    rich "Thank you so much!"
    hide case with dissolve
    ed "Alright, let's get going now."
    ed "As long as you leave our company alone, we'll leave you alone from now on."
    ed "Good luck to you as well."
    hide ed
    hide rich
    with moveoutright
    n "Ed and Richard go back to their JoJ UFO and take off."
    show cs at right with move
    n "CS walks up to his front door."
    scene cs_room with dissolve
    play music ac_title volume 0.4 if_changed
    music ac_title
    show cs at center with moveinleft
    cs "Ah, it's good to be home again!"
    if fanbase == "both":
        jump south_true_ending_alt
    elif fanbase == "ltt":
        jump south_ltt_ending_alt
    elif fanbase == "ytp":
        jump south_ytp_ending_alt
    else:
        jump south_true_ending_alt

label south_true_ending_alt:
    scene cs_room
    play music ac_title volume 0.4 if_changed
    music ac_title
    show cs at center
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
    n "The chat is overflowing with messages."
    chat "Yeah what happened to you?{w=0.25} Oh my God, CS, you're here!{w=0.25} Hi!{w=0.25} Hi!{w=0.25} Where have you been?"
    show cs happy at mid_left
    cs "Well, guys..."
    jump south_lego_ending

label south_ytp_ending_alt:
    scene cs_room
    play music ac_title volume 0.4 if_changed
    music ac_title
    show cs at center
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
    jump south_lego_ending

label south_ltt_ending_alt:
    scene cs_room
    play music ac_title volume 0.4 if_changed
    music ac_title
    show cs at center
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
    jump south_lego_ending

label south_lego_ending:
    scene cs_room_2
    show cs at mid_left
    stop music fadeout 1.0
    music end
    cs "Guess what!"
    play music lego_island volume 0.6 if_changed
    music lego_island
    show case at mid_left
    n "CS takes his briefcase out and opens it up on camera."
    cs "I'm fuckin' rich now!"
    hide case with dissolve
    cs "I'm gonna make Lego Island in real life!"
    cs "You're all invited to come stay at my island once it's built!"
    n "The chat is freaking out as CS announces his plan."
    cs "I'm gonna start buying all the Lego bricks we need, and you guys can help build the island!"
    cs "Now, let's see what to buy..."
    scene black with dissolve
    stop music fadeout 1.0
    music end
    $ ending_manager.mark("south")
    $ renpy.movie_cutscene(creditsm)
    $ persistent.heard.add("goodbye_summer_hello_winter")
    $ renpy.end_replay()
    return

label south_fighthohsis_alt:
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
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
    stop music fadeout 1.0
    music end
    bad_end "Revenge!" "south_back_home_alt"

label south_braghohsis:
    play music hohsis_remix volume 0.5 if_changed
    music hohsis_remix
    scene cs_house
    show ed at right
    show rich at mid_mid_right behind ed
    show cs angry at left
    cs "Yeah, well, I have {i}so{/i} much money! I don't really care!"
    cs "You guys {i}deserve{/i} to have your company in shambles!"
    n "Richard and Ed back up to their UFO."
    hide rich
    hide ed
    with moveoutright
    cs "Hey! Where are you guys going?"
    cs "Come back here!"
    n "The JoJ UFO flies up over the house, then vaporizes it with a laser."
    play sound sfx_beam volume 0.6
    show beam at xstretch_in
    pause 3.0
    show beam at xstretch_out
    scene cshouse_vaporized
    show cs angry at left
    cs "I'll just buy a new house!"
    n "Ed then also vaporizes the briefcase of money."
    show cs disappointed
    with vpunch
    n "Ed flips CS the bird, then flies away."
    show cs disappointed
    pause 1.0
    cs "Fuck."
    bad_end "Time to bunk\nat Rosen's!" "south_back_home_alt"
    stop music fadeout 1.0
    music end
    return
