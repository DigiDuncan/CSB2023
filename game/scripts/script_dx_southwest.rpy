label southwest_start:

    play music happy_roaming volume 0.5 if_changed
    music happy_roaming
    scene expression "washington_road %s" % compass_current_time
    show expression "cs %s" % compass_current_shader at left
    show expression "arceus %s" % compass_current_shader at right
    cs "Hey, how about Hitchhiking south-west? Cali should be nice round this time of the year."
    arceus "That's sounds great buddy, but I thought you wanted to start heading home."
    arceus "Last time I checked, you don't live south-west of here."
    cs "Yeah, but we can take a boat all the way back home, y'know?"
    arceus "First of all, we have no money."
    arceus "Second of all, wouldn't that take ages to get back home?"
    cs "First of all, we can just sneak in or something."
    cs "Second of all... I don't care we're doing it."
    n "CS extends a thumbs up, hoping a car will pass by soon."
    n "As if someone was listening and planning their every move, a car stops right next to them."
    frank "Hey, where you guys going?"
    cs "We're going to California."
    frank "We're stopping there anyways, you wanna hop in?" 
    cs "That sounds like the best time ever."
    susan "A stranger in our car? Are you sure about this?" (multiple=2)
    arceus "Getting in a strangers car? Are you sure CS?" (multiple=2)
    n "CS leans over to Arceus and whispers into his ear."
    cs "It's a free ride man, let's just take our chances."
    n "Arceus sighs."
    arceus "Fine. I guess this does beat walking."
    cs "Woohoo!"
    cs "If you guys don't mind, we'd love to tag along!"
    frank "Alright you two, move outta the way."
    n "The two kids in the back scoot to the side. CS and Arceus quickly get in the car."
    #fun value where we replace Rodrick with Robert Tobias "Radiation" Fox.
    #now we skip most of the ride.

    cs "We made it to Los Angeles in one piece!"
    menu:
        "No cool dialogue yet, sorry."
        "Go to San Diego":
            jump southwest_san_diego
        "Go to Vegas":
            jump southwest_vegas 
        "Go to In-N-Out":
            jump southwest_cali_foodplace

label southwest_cali_foodplace:
    cs "I guess we could go to In-N-Out. I've never been and I might as well try out their food."
    arceus "I'll eat anything at this point."
    frank "In-N-Out it is! Let's get some burgers!"
    n "Frank drives to the closest location and pulls into the line."
    cs "Holy crap, this line is so friggin' long!"
    frank "Don't worry boys, this is normal here."
    frank "That's why the employees come out to take your order!"
    n "One of the workers comes up to the car with a menu."
    cashier "Hey guys, may I take your order?"
    arceus "I will just have a coke and some fries." #Placeholder
    cs "I will take Fanta and a hamburger."
    frank "I'll have a cheeseburger, two orders of fries, and uhh, a large shake."
    cashier "Uhh, alrighty."
    cashier "So that will be PLACEHOLDER, hamburger and a regular Fanta, and a cheeseburger, two fries, and a large shake?"
    frank "Sounds correct!"
    cashier "Alright, you should be good to pick up your food when you get to the window!"
    n "As the cars pass, Frank finally pulls up to the window to get their meal."
    cashier "Here you go, sir."
    n "The cashier hands Frank a flyer for Fentanyl awareness."
    frank "Uhh, okay."
    frank "CS, you can have this."
    cs "What in the world? 34,000 deaths alone in Los Angeles County?"
    cashier "You can pull up to the next window please."
    n "Frank drives up to the second window, and gets his food."
    frank "Alrighty everyone, eat up!"
    #THen they win clue