label kuwait_travel:
    cs "Uhh, I guess I wanted to go to Kuwait?"
    benrey "Well, I'm sorry, but everyone has a Pass{w=0.5} Port!"
    show cs disappointed
    benrey "Try checking your mouth."
    cs "Hu-"
    n "CS starts coughing and reaches into his mouth pulling a passport out."
    benrey "And for my next trick..."
    cs "I just want to get to Kuwait"
    benrey "Okay okay!"
    benrey "Now, let's get you your ticket."
    n "CS hands the ticket fella his money."
    benrey "Alright, your plane is actually leaving here in about 5 minutes"
    show cs worried
    cs "Oh crap, thank you!"
    hide cs with moveoutright
    scene black with dissolve
    scene airport_tsa
    show tsa at right
    with dissolve
    n "CS rushes up to the TSA to get checked through."
    show cs at mid_left with moveinleft
    n "CS takes a minute to catch his breath."
    cs "I'm almost there!"
    tsa "Alright, go on through to the MTLDTCTR sir."
    cs "The what?"
    tsa "The Metal Detector, we got a new model."
    cs "Okay?"
    show cs at mid_right with move
    n "CS walks through and the detector stays silent."
    tsa "Fantastic!"
    cs "So, this means I'm good to go, right?"
    tsa "Yup."
    show cs happy
    cs "Woohoo! Thanks!"
    hide cs with moveoutright
    scene black with dissolve
    n "CS manages to get on his plane, right before the terminal closes down, somehow."
    stop music fadeout 3.0
    music end
    scene airplane_seats
    show cs at left
    with fade
    n "CS gets himself comfortable and tries to not think about the cops."
    cs "Whew! What a day."
    cs "I really hope this works out. I don't think I have enough to travel again after this."
    cs "I didn't think this is how I'd be going to another country, rushing out of a hospital and all."
    cs "Well, it's been a long day."
    cs "I guess I should get some rest."
    scene black with dissolve
    jump kuwait



label kuwait:
    scene airplane_seats
    show cs at left
    with dissolve
    n "CS wakes up as his plane lands in Kuwait City."
    cs "Finally to Kuwait! I don't have to worry about the cops anymore."
    cs "Not entirely sure why I came here but hey, might as well go explore."
    scene black with dissolve
    n "CS exits the airport and finds himself in the middle of the city."
    scene kuwait_city 
    show cs at left
    with dissolve
    cs "Man, Kuwait is so nice, especially this time of year!"
    show RCOMEM at right with moveinright
    RCOMEM "Hey, good morning!"
    cs "Good morning to you too!"
    hide RCOMEM with moveoutleft
    cs "Man, it's a great thing that in 1992 US Forces succesfuly liberated Kuwait from Saddam Husseins prescence in operation Desert Sabre."
    cs "Thus leading to the majority of the population of Kuwait speaking perfect English in return!"
    cs "I don't know how I would've managed if they spoke a different language from mine."
    cs "Weird how this is the only thing i learnt in my history class."
    n "As CS is remembering his youth, he starts hearing crackling and booms on the distance."
    cs "What the heck could those be?"
    n "Just in that moment something big hits CS"
    cs "WHAT THE F--{w=0.1}{nw}"
    show kuwait_explosion behind cs
    play sound "secret/sfx_explosion.ogg"
    hide cs with moveoutleft 
    stop sound
    scene black

label kuwait_hospital:
    pause 10
    play sound "sfx_heartbeat.ogg" loop
    play music "tmwstw.ogg"
    centered "{cps=*0.05}7 years later"
    cs "{i}Where... where am I?{/i}"
    cs "{i}Everything hurts like hell.{/i}"
    cs "{i}Might as well try opening my eyes.{/i}"
    scene kuwait_hospital_inside with dissolve
    show kuwait_doctor_1 at right
    show kuwait_nurse_1 at left
    k_nurse "Doctor, doctor! He's waking up!"
    k_doctor "Ah, it's about time. Welcome back to the land of the living."
    k_doctor "Will you shut that damn thing off?"
    stop sound
    stop music
    k_nurse "Sorry Doctor."
    cs "What the he-"
    k_doctor "Try not to speak just yet, you've been out cold for a while."
    k_doctor "You're one of the few we managed to get out before Kuwait completely fell."
    k_doctor "I know you have some questions, but you're going to have to take those up with the lieutenant"
    k_doctor "We've stabilized you well for the time you've been here, but it might take some time for you to walk properly again."
    k_doctor "You should start getting up in the next few minutes thanks to modern science!"
    k_doctor "Okay nurse, let's bounce!"
    hide kuwait_doctor_1 
    hide kuwait_nurse_1
    with moveoutleft
    cs "{i}Oh jeez{/i}"
    scene black with dissolve
    n "CS falls asleep for a few more hours."
    n "Waking up CS feels refreshed, but hungry and very thirsty"
    cs "I really need to take a crap too."
    cs "Nurse, where's the bathroom?"
    k_nurse "Down the hall to the left"
    cs "Thanks nurse!"
    centered "A CSBIII Expansion created by: Mikapara"
    scene kuwait_hospital_corridor with dissolve
    cs "Man, it's really hard to walk. I basically have to grab onto anything."
    cs "Last thing I remember, there were strange sounds on the distance."
    cs "Having said that, I feel like I got the best sleep of my life."
    scene black
    centered "With the help of: Pakoo and Digiduncan."
    cs "This should be the bathroom."
    n "As CS is about to walk into one of the stalls he notices something strange in the mirror."
    scene kuwait_hospital_bathroom_foggy with dissolve
    cs "What the hell, why's it so blurry?"
    n "CS uses some of the strength he has to de-fog the mirror"
    scene kuwait_hospital_bathroom_clear 
    cs "What the fuck happened?!{w=1}{nw}"
    scene black
    centered "CSBIII: Kuwait (Working title)"
    n "After panicking for 30 minutes CS finally exits the bathroom and goes to meet the Lieutenant."
    scene kuwait_islandbase_leaders
    show kuwait_lieutenant_snow at right
    with dissolve
    show cs worried punished at left with moveinleft
    l_snow "Ah, you must be CS."
    cs "Yes! Wait, how'd you know my name?"
    l_snow "We took a peek at your wallet when you first came in."
    cs "Well, what the hell is going on?"
    l_snow "Now CS, I know it's going to shock you but... It's been 7 years since Kuwait fell."
    cs "You mean to tell me I've been in a coma for 7 years?!"
    l_snow "Yeah, also this is where I'm gonna stop cuz I wanna do other things today :p"
    cs "Can I at least have my wallet back?"
    l_snow "No, I like it. Imma keep it"
    cs ":("


    