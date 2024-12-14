label beach_start:
    scene washington_road day
    show cs at left
    show arceus angry at right
    with dissolve
    play music happy_roaming volume 0.5 if_changed
    music happy_roaming

    pause 0.5
    show cs surprised
    cs "You know, Arc..."
    cs "I saw a bus stop a little ways back."
    cs "Think it goes to anywhere cool?"
    arceus "If it'll keep you from going west again, I guess it's worth a look..."
    show cs happy
    cs "Great! Let's check it out!" 
    window hide
    show cs happy flipped
    hide cs with moveoutleft
    show arceus angry at offscreenleft with MoveTransition(1.0)
    pause 0.5

    scene black with dissolve
    pause 0.5
    "placeholder"
