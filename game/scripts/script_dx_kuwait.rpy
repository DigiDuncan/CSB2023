label kuwait_travel:
    play music airport volume 0.4 if_changed
    music airport
    scene ticket_counter
    show benrey at center
    show cs disappointed at left
    cs "Uh, I guess I wanted to go to Kuwait?"
    benrey "Well, I'm sorry, but everyone has a Pass{w=0.5} Port!"
    show cs disappointed
    benrey "Try checking your mouth."
    show cs scared
    cs "Hu-"
    n "CS starts coughing and reaches into his mouth, pulling out a passport."
    benrey "And for my next trick--"
    show cs disappointed
    cs "I {i}just{/i} want to get to Kuwait."
    benrey "Okay, okay!"
    benrey "Now, let's get you your ticket."
    n "CS hands the ticket fella his money."
    benrey "Alright, your plane is actually leaving here in about five minutes."
    show cs worried
    cs "Oh, crap! Thank you!"
    hide cs with moveoutright
    scene black with dissolve
    scene airport_tsa
    show tsa at right
    with dissolve
    n "CS rushes up to TSA to get checked through."
    show cs at mid_left with moveinleft
    n "He takes a minute to catch his breath."
    cs "I'm almost there!"
    tsa "Alright, go on through to the MTLDTCTR sir."
    show cs disappointed
    cs "The... what?"
    tsa "The Metal Detector. We got a new model."
    cs "Okay...?"
    show cs at mid_right with move
    n "The detector remains silent as CS steps through."
    tsa "Perfect."
    cs "So, this means I'm good to go, right?"
    tsa "Yup."
    show cs happy
    cs "Woohoo! Thanks!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS somehow manages to get on the plane just before the terminal closes down."
    stop music fadeout 3.0
    music end
    scene airplane_seats
    show cs at left
    with dissolve
    n "CS makes himself comfortable and tries to not think about the cops."
    cs "Whew! What a day."
    show cs disappointed
    cs "I really hope this works out. I don't think I have enough cash to travel again after this."
    cs "I didn't think {i}this{/i} is how I'd be going to another country, rushing out of a hospital and all."
    show cs
    cs "Well, it's been a long day."
    cs "I guess I should get some rest."
    scene black with dissolve
    jump kuwait



label kuwait:
    scene airplane_seats
    show cs at left
    with dissolve
    n "CS wakes up as his plane lands in Kuwait City."
    cs "Finally, to Kuwait! I don't have to worry about the cops anymore."
    cs "Not entirely sure why I came here, but hey, might as well go explore."
    scene black with dissolve
    n "CS exits the airport and finds himself in the middle of the city."
    scene kuwait_city 
    show cs at left
    with dissolve
    cs "Man, Kuwait is so nice, especially this time of year!"
    show RCOMEM at right with moveinright
    RCOMEM "Hey, good morning!"
    show cs happy
    cs "Good morning to you, too!"
    hide RCOMEM with moveoutleft
    
    # howdy y'all, tate here.
    # sooo this is awkward but thanks for accidentally teaching me where the hell my father was at in '92?? (the year i was born)
    # also i wasn't initially going to leave any comments here but mean said i should bc it would be funny. feel free to delete all this once you've read it
    
    cs "Man, it sure is great, that, in 1992, U.S. Forces successfully liberated Kuwait from Saddam Hussein's presence in Operation Desert Sabre."
    cs "It lead to the majority of Kuwait's population knowing perfect English!"
    cs "I don't know how I would manage here if they spoke a different language."
    cs "Weird how this is the only thing I remember from my history class..."
    n "As CS is reflecting upon his youth, he starts hearing crackles and booms in the distance."
    show cs disappointed
    cs "What the heck could {i}that{/i} be?"
    n "In that moment, something big hits CS!"
    show cs scared
    cs "WHAT THE F--{w=0.1}{nw}"
    show kuwait_explosion behind cs
    play sound sfx_explosion
    hide cs with moveoutleft 
    stop sound
    scene black

label kuwait_hospital:
    scene black
    pause 10
    play sound sfx_heartbeat loop
    play music tmwstw if_changed
    music tmwstw
    pause 5
    cs "{i}Where... where am I?{/i}"
    if fun_value(FUN_VALUE_MUSIC):
        cs "{i}Am I the man who sold the world?{/i}"
        cs "{i}Everything hurts like hell...{/i}"
    else:
        cs "{i}Everything hurts like hell...{/i}"
    cs "{i}Might as well try opening my eyes.{/i}"
    scene kuwait_hospital_inside 
    show kuwait_doctor_1 at right
    show kuwait_nurse_1 at left
    with Dissolve(0.5) # this line was crashing 50% of the time so i changed it - tate
    k_nurse "Doctor, doctor! He's waking up!"
    k_doctor "Ah, it's about time."
    k_doctor "Welcome back to the land of the living."
    k_doctor "Will you shut that damn thing off?"
    stop sound
    stop music
    music end
    k_nurse "Sorry, Doctor."
    cs "What the he--"
    k_doctor "Try not to speak just yet. You've been out cold for a while."
    k_doctor "You're one of the few we managed to save before Kuwait completely fell."
    k_doctor "I know you have some questions, but you're going to have to take those up with the lieutenant."
    k_doctor "We've kept you pretty stable while you've been here, but it might take some time for you to walk properly again."
    k_doctor "You should at least be able to stand up in the next few minutes, thanks to modern science!"
    k_doctor "Okay, nurse, let's bounce!"
    hide kuwait_doctor_1 
    hide kuwait_nurse_1
    with moveoutleft
    cs "{i}Oh, jeez...{/i}"
    scene black with dissolve
    n "CS falls asleep for a few more hours."
    n "As he wakes up, CS feels refreshed, but hungry and very thirsty."
    cs "I really need to take a crap, too."
    cs "Nurse, where's the bathroom?"
    k_nurse "Down the hall, to the left."
    cs "Thanks, nurse!"
    centered "A CSBIII Expansion created by: Mikapara"
    scene kuwait_hospital_corridor with dissolve
    cs "Man, it's really hard to walk. I basically have to grab onto everything."
    cs "Last thing I remember... there were weird sounds in the distance."
    cs "Despite all of this, I feel like I just got the best sleep of my life!"
    scene black
    centered "With the help of: Pakoo and DigiDuncan."
    cs "This should be the bathroom."
    n "As CS is about to walk into one of the stalls, he notices something strange in the mirror."
    scene kuwait_hospital_bathroom_foggy with dissolve
    cs "What the hell? Why's it so blurry?"
    n "CS uses what strength he has to de-fog the mirror."
    scene kuwait_hospital_bathroom_clear 
    cs "What the fuck happened?!{w=1}{nw}"
    scene black
    centered "CSBIII: Kuwait"
    n "After panicking for 30 minutes, CS finally exits the bathroom to find the Lieutenant."
    scene kuwait_islandbase_leaders
    show kuwait_lieutenant_snow at right
    with dissolve
    show cs worried punishedgown at left with moveinleft
    l_snow "Ah, you must be CS."
    cs "Yes! Wait, how'd you know my name?"
    l_snow "We took a peek at your wallet when you first came in."
    cs "Well, what the hell is going on?"
    l_snow "Now, CS, I know it's going to shock you, but... It's been seven years since Kuwait fell."
    cs "You mean to tell me I've been in a coma for {i}seven years?!"
    scene black
    centered "Chapter 1: 7 Years Later"
    scene kuwait_islandbase_leaders
    show cs worried punishedgown at left
    show kuwait_lieutenant_snow at right
    with dissolve
    l_snow "Yeah, it's very shocking, I know."
    cs "Yeah, it is! Also, what do you mean the fall of Kuwait, did it get attacked?"
    l_snow "Sadly, yes."
    l_snow "The infection started in a Canadian airport. British Columbia, specifically."
    l_snow "Many people traveling by plane were already infected, so it spread worldwide, and {i}quickly."
    l_snow "Right now, the only places we know of that have not been turned are Russia and Greece."
    cs "Wait, infection? Like... zombies?!"
    l_snow "Or walkers, zeds... idiots that move slow and are somewhat easy to kill, as Isaac puts it."
    cs "This is... {i}so{/i} much to take in right now. I need a moment."
    l_snow "I understand. For now, how about you go get changed?"
    cs "Did my outfit survive?"
    l_snow "It was mostly obliterated in the blast, but we saved some scraps!"
    cs "That's alright. I'll see what I can piece together."

    scene black

    centered "CS quickly finds his stuff and pieces what he can together"

    scene kuwait_islandbase_leaders
    show kuwait_lieutenant_snow at right
    with dissolve
    show cs angry punished at left with moveinleft
    cs "Alright, I'm changed. I'm glad most of my outift survived, had to improvise a little though."
    l_snow "Fantastic. We're aware of who you are, by the way. Your abilities and what-not. We've also seen your videos."
    cs "Oh, God... You {i}saw{/i} those?"
    l_snow "Yeah, they were funny."
    l_snow "Anyway, we need a field agent of sorts. Someone who knows their way around a fight, y'know?"
    cs "I guess... but, the last fight I had landed me here in Kuwait."
    l_snow "Two things before you go: First, here's your field communicator, an iPad 2!"
    cs "An iPad? Is that really the best equipment you've got?"
    l_snow "I mean, we have this holographic display device, if you want to give it a spin."
    l_snow "The Wireless Internet Networkable Device Of Wonderous Strengths Phosphor Holographic OLED Night-vision-capable E-display!"
    cs "... A \"Windows Phone\"?"
    l_snow "I... {i}guess{/i} you could call it that?"
    cs "Awesome, I love Windows Phones!"
    l_snow "Fantastic! It'll be activated later. Don't worry about it for now."
    l_snow "Secondly, there are four locations that you need to pay a visit to: the mechanic, the civilian encampment, the armory, and the helipad."
    cs "I hope I don't get too lost..."
    l_snow "This is not a huge island. I'm sure you'll find your way around, no problem. Dismissed!"
    show cs angry punished flipped with determination
    hide cs with moveoutleft
    scene black with dissolve
    jump kuwait_icarus

# Travel Locations

label kuwait_al_wafra:
    scene al_wafra
    show cs angry punished
    with dissolve
    cs "I am now at Al Wafra."
    menu:
        "What do you want to check out?"
        "House":
            cs "I'll go check out the House."
            hide cs with moveoutright
            show wafra_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_al_wafra
        "Barn":
            cs "I'll go check out the Barn."
            hide cs with moveoutright
            show wafra_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_al_wafra
        "Greenhouses":
            cs "I'll go check out the Greenhouses."
            hide cs with moveoutright
            show wafra_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_al_wafra

label kuwait_khiran_camp:
    scene khiran_camp
    show cs angry punished
    with dissolve
    cs "I am now at Khiran Camp."
    menu:
        "What do you want to check out?"
        "House 1":
            cs "I'll go check out this House."
            hide cs with moveoutright
            show khiran_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_khiran_camp
        "House 2":
            cs "I'll go check out this House."
            hide cs with moveoutright
            show khiran_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_khiran_camp
        "House 3":
            cs "I'll go check out this House."
            hide cs with moveoutright
            show khiran_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_khiran_camp

label kuwait_burgan_oil_fields:
    scene burgan_oil
    show cs angry punished
    with dissolve
    cs "I am now at the Burgan Oil Fields."
    menu:
        "What do you want to check out?"
        "Shed":
            cs "I'll go check out the Shed."
            hide cs with moveoutright
            show burgan_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_burgan_oil_fields
        "Oil Drums":
            cs "I'll go check out the Oil Drums."
            hide cs with moveoutright
            show burgan_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_burgan_oil_fields

label kuwait_sharq:
    scene sharq
    show cs angry punished
    with dissolve
    cs "I am now at Sharq."
    cs "This is interesting, but I don't have too much to do here."

label kuwait_icarus:
    scene icarus
    show cs angry punished
    with dissolve
    if tutorial == True:
        scene icarus
        show cs angry punished
        with dissolve
        cs "I am now at Icarus."
        menu:
            "What do you want to check out?"
            "The Interior":
                jump kuwait_interior
            "The Exterior":
                jump kuwait_exterior
    else:
        cs "Hmm, where should I go?"
        menu:
            "What do you want to check out?"
            "The Interior":
                jump kuwait_interior
            "The Exterior":
                jump kuwait_exterior
label kuwait_interior:
    scene kuwait_hallway
    show cs angry punished
    with dissolve
    cs "Alright, where should I go from here?"
    menu:
        "What do you want to check out?"
        "The Gunsmith":
            cs "I'll go check out the gunsmith."
            hide cs with moveoutright
            show gunsmith with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            $ gunsmith_check = True
            jump kuwait_interior
        "The Mechanic":
            cs "I'll go check out the mechanic."
            hide cs with moveoutright
            show mechanic_shop
            show suzuki at right
            with dissolve
            show cs angry punished with moveinleft
            if tutorial == False:
                $ mechanic_check = True
                cs "Hey, who are you?"
                suzuki "I'm Suzuki, the local mechanic!"
            suzuki "Do you need help with anything?"
            cs "Nope, not yet!"
            show cs angry punished with determination
            hide cs with moveoutleft
            jump kuwait_interior
        "The Bar":
            cs "I'll go check out the bar."
            hide cs with moveoutright
            show ag_bar
            show anne at right
            show grace at mid_right
            with dissolve
            show cs angry punished with moveinleft
            if tutorial == True:
                grace "Welcome back, CS!"
                anne "Do you want anything to drink?"
                menu:
                    "See shop inventory":
                        anne "Sorry, we don't have anything yet."
                        jump kuwait_interior
                    "Talk about world travels":
                        cs "I've travelled this whole world of ours from Cali to Moomin Valley"
                        jump kuwait_interior
            $ bar_check = True
            grace "Hi! Welcome to the A&G Bar!"
            anne "You seem new here, who are you?"
            cs "Hey girls! CS here!"
            grace "CS? Like 188?"
            cs "Yeah, you know me?"
            grace "I do, you're that YTP guy!"
            cs "Indeed I am!"
            anne "Well, this is our bar, and we serve the local residents of this island."
            anne "Do you want anything to drink?"
            
            jump kuwait_icarus   
        "The Main Office":
            cs "I guess I can go back and talk with that lady."
            hide cs with moveoutright
            scene kuwait_islandbase_leaders
            show kuwait_lieutenant_snow at right
            with dissolve
            show cs angry punished at left with moveinleft
            if (gunsmith_check and mechanic_check and bar_check and civvies_check and pmc_check and heli_check):
                l_snow "Well, it looks like you've talked with everyone!"
                l_snow "You are on your own now, hopefully you'll be able to save Kuwait!"
                $ tutorial = True
                jump kuwait_icarus
            l_snow "Welcome back, did you need anything else from me?"
            cs "No not really."
            show cs angry punished flipped with determination
            hide cs with moveoutleft
            jump kuwait_interior
        "Go Back Outside":
            jump kuwait_exterior
label kuwait_exterior:
    scene icarus
    show cs angry punished
    with dissolve
    cs "Alright, what building should I go check out?"
    menu:
        "What do you want to check out?"
        "The Civvies":
            $ civvies_check = True
            cs "I'll go check out that Building."
            hide cs with moveoutright
            show icarus_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_exterior
        "The PMCs":
            $ pmc_check = True
            cs "I'll go check out that Building."
            hide cs with moveoutright
            show icarus_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_exterior
        "The Heliport":
            cs "I'll go check out that Building."
            hide cs with moveoutright
            show icarus_3
            show elizabeth at right
            with dissolve
            show cs angry punished with moveinleft
            if tutorial == True:
                eliza "Heya CS! Are you ready to head out again?"
                menu:
                    "Head out to Kuwait":
                        cs "Yep, I'm ready!"
                        eliza "Alrighty. Well let's get a move on, shall we?"
                        scene black with dissolve
                        jump kuwait_select
                    "Stay at Icarus for now":
                        cs "I'm not ready yet, I still have a few things to do."
                        eliza "Take your time, but not too much time."
                        show cs angry punished flipped with determination
                        hide cs with moveoutleft
                        jump kuwait_exterior
            $ heli_check = True
            eliza "Hey, you new here?"
            cs "Yeah, it's a long story."
            eliza "Well, whenever you are ready for adventure, come to me and I'll drop you off anywhere in Kuwait."
            cs "Sounds good!"
            show cs angry punished flipped with determination
            hide cs with moveoutleft            
            jump kuwait_exterior
        "Go Inside":
            jump kuwait_interior

label kuwait_kuwait_city:
    scene kuwait_cityu
    show cs angry punished
    with dissolve
    cs "I am now at Kuwait City."
    menu:
        "What do you want to check out?"
        "Fire Station":
            cs "I'll go check out the Fire Station."
            hide cs with moveoutright
            show mirai_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city
        "Offices":
            cs "I'll go check out the Offices."
            hide cs with moveoutright
            show mirai_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city
        "Restaurant":
            cs "I'll go check out the Restaurant."
            hide cs with moveoutright
            show mirai_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city
        "Weather Service":
            cs "I'll go check out the Weater Service Building."
            hide cs with moveoutright
            show mirai_4 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city
        "Police Station":
            cs "I'll go check out the Police Station."
            hide cs with moveoutright
            show mirai_5 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city
        "Bank":
            cs "I'll go check out the Bank."
            hide cs with moveoutright
            show mirai_6 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city
        "Hospital":
            cs "I'll go check out the Hospital."
            hide cs with moveoutright
            show mirai_7 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kuwait_city

label kuwait_hawally:
    scene hawally
    show cs angry punished
    with dissolve
    cs "I am now at Hawally."
    menu:
        "What do you want to check out?"
        "Apartments 1":
            cs "I'll go check out the Apartment Complex."
            hide cs with moveoutright
            show hawally_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_hawally
        "Apartments 2":
            cs "I'll go check out the other Apartment Complex."
            hide cs with moveoutright
            show hawally_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_hawally
        "Store":
            cs "I'll go check out the Store."
            hide cs with moveoutright
            show hawally_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_hawally
        "Pizza Shop":
            cs "I'll go check out the Pizza Shop."
            hide cs with moveoutright
            show hawally_4 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_hawally

label kuwait_boubyan_island:
    scene boubyan_island
    show cs angry punished
    with dissolve
    cs "I am now at Boubyan Island."
    cs "This is interesting, but I'm actively dying."

label kuwait_saqr_airbase:
    scene saqr_airbase
    show cs angry punished
    with dissolve
    cs "I am now at the Saqr Airbase."
    menu:
        "What do you want to check out?"
        "Armory":
            cs "I'll go check out the Armory."
            hide cs with moveoutright
            show saqr_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_saqr_airbase
        "Tents":
            cs "I'll go check out the Tents."
            hide cs with moveoutright
            show saqr_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_saqr_airbase
        "Hangar":
            cs "I'll go check out the Hangar."
            hide cs with moveoutright
            show saqr_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_saqr_airbase

label kuwait_salmiya:
    scene salmiya
    show cs angry punished
    with dissolve
    cs "I am now at Salmiya."
    menu:
        "What do you want to check out?"
        "Big Apartments":
            cs "I'll go check out the Big Apartments."
            hide cs with moveoutright
            show salmiya_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_salmiya
        "Small Apartments":
            cs "I'll go check out the Small Apartments."
            hide cs with moveoutright
            show salmiya_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_salmiya
        "Shop":
            cs "I'll go check out the Shop."
            hide cs with moveoutright
            show salmiya_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_salmiya
        "Fire Station":
            cs "I'll go check out the Fire Station."
            hide cs with moveoutright
            show salmiya_4 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_salmiya

label kuwait_bayan_water_towers:
    scene bayan_water
    show cs angry punished
    with dissolve
    cs "I am now at the Bayan Water Towers."
    menu:
        "What do you want to check out?"
        "Top of Water Towers":
            cs "I'll go climb the Water Towers."
            hide cs with moveoutright
            show bayan_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_bayan_water_towers

label kuwait_mutla_ridge:
    scene mutla_ridge
    show cs angry punished
    with dissolve
    cs "I am now at Mutla Ridge."
    cs "This is interesting, but I don't have too much to do here."

label kuwait_um_al_maradim:
    scene um_al_maradim
    show cs angry punished
    with dissolve
    cs "I am now at Um Al Maradim."
    menu:
        "What do you want to check out?"
        "Tents 1":
            cs "I'll go check out these Tents."
            hide cs with moveoutright
            show maradim_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_um_al_maradim
        "Tents 2":
            cs "I'll go check out these other Tents."
            hide cs with moveoutright
            show maradim_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_um_al_maradim

label kuwait_um_al_namil:
    scene um_al_namil
    show cs angry punished
    with dissolve
    cs "I am now at Um Al Namil."
    cs "This is interesting, but I don't have too much to do here."

label kuwait_sulaibiya:
    scene sulaibiya
    show cs angry punished
    with dissolve
    cs "I am now at Sulaibiya."
    cs "This is interesting, but I don't have too much to do here."

label kuwait_kubar_island:
    scene kubar_island
    show cs angry punished
    with dissolve
    cs "I am now at Kubar Island."
    menu:
        "What do you want to check out?"
        "House":
            cs "I'll go check out this House."
            hide cs with moveoutright
            show kubar_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_kubar_island

label kuwait_jahra_industrial:
    scene jahra_industrial
    show cs angry punished
    with dissolve
    cs "I am now at Jahra Industrial."
    menu:
        "What do you want to check out?"
        "Warehouse 1":
            cs "I'll go check out the Warehouse."
            hide cs with moveoutright
            show jahra_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_jahra_industrial
        "Warehouse 2":
            cs "I'll go check out the other Warehouse."
            hide cs with moveoutright
            show jahra_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_jahra_industrial

label kuwait_al_abdally:
    scene al_abdally
    show cs angry punished
    with dissolve
    cs "I am now at Al-Abdally."
    menu:
        "What do you want to check out?"
        "Small Barn":
            cs "I'll go check out the Small Barn."
            hide cs with moveoutright
            show abdally_1 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_al_abdally
        "Big Barn":
            cs "I'll go check out the Big Barn."
            hide cs with moveoutright
            show abdally_2 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_al_abdally
        "Greenhouses":
            cs "I'll go check out the Greenhouses."
            hide cs with moveoutright
            show abdally_3 with dissolve
            show cs angry punished with moveinleft
            cs "This is interesting, but I don't have too much to do here."
            jump kuwait_al_abdally
