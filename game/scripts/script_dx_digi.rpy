label fix_pakoo_death:
    scene green_screen
    digi "What? What are you doing here?"
    digi "You're not supposed to be here."
    digi "Did you-- did you kill Pakoo?!"
    digi "He's the scriptwriter, I can't..."
    pause 0.5
    digi "Fine, I'll fix it."
    pause 1.0
    digi "But, you owe me one."
    pause 2.0
    digi "See you on the other side!"
    return

label dx_underpants:
    # Hi, Tate, I assume you'll see this at some point.
    # This is a reference to a Mad Lib Pakoo and Mika wrote at 3AM and sent me via voice message.
    # There's a reason this barely makes sense.
    # If you're doing a grammar pass on this, please don't change the wording without consulting me.
    # Just want to make sure the jokes stay intact.
    # Thanks!
    # -- Digi

    play music school volume 0.4
    scene classroom
    show george at left
    show harold at right
    show pakoo at center
    show weird_al at offscreenright
    with dissolve
    n "George, Harold, and Pakoo are busy studying the wonders of gooey jugular veins."
    n "Their new science teacher, Mr. Weird Al Yankovic, spills some smelly sulfiric acid on a pile of toxic Mikas!"
    show harold at center
    show pakoo at mid_left
    show weird_al at right
    with move
    weird_al "Whoops!"
    n "Suddenly, the pile began to morph into a giant evil Mika!"
    show mika at _t_evil_mika behind george with vpunch
    play sound sfx_bossappears
    pause 1.0
    show david at right with moveinright
    david "Help!"
    david "A giant, evil Mika just stepped on my lunch bucket and ate a Van Halen!"
    show mr_krupp at left with moveinleft
    mr_krupp "Oh no! The poor lunch box!"
    hide george
    hide harold
    hide pakoo
    with moveoutleft
    n "George, Harold, and Pakoo try to escape by hiding behind a neutrino."
    n "Pakoo snapped his fingers."
    n "Soon, a digital grin came across Mr. Krupp's face as he dropped his dark tie, and ran to his office."
    hide mr_krupp with moveoutleft
    pause 1.0
    play sound sfx_punch
    show cpt_underpants at left with moveinleft
    n "Soon, Captain Underpants punched through the wall!"
    n "He grabbed a slimy M-16 and hit the monster on its elbow!"
    play sound sfx_hks1
    mika "Ouchies!"
    n "The monster turned and kicked the monster on its esaphogus!"
    play sound sfx_alt_punch
    n "Pakoo quickly mixed up a bottle of chocolate milk with bloody piles of dog shit!"
    george "Hey, Pakoo? Where did you find the jar of crazy stuff?"
    pakoo "It was right here, next to this barrel of toxic yellow Game Boys."
    harold "Oh, that makes sense."
    n "Pakoo shook up the strange mixture, and threw it at the monster!"
    show pakoo flipped at left with moveinleft
    play sound sfx_splash
    mika "Woohoo!"
    hide mika with moveoutbottom
    play sound sfx_explosion
    n "The monster died of a massive right toe attack!"
    george "That made sense, too."
    n "Unfortunately, some of the mixture splashed onto Captain Underpants' head, and he turned pack into Mr. Krupp."
    hide cpt_underpants
    show mr_krupp at center
    with dissolve
    mr_krupp "Holy bright penguins!"
    mr_krupp "I'll bet that George, Harold, and Pakoo are responsible for this mess!"
    mr_krupp "For your punishment, you all must chop in the broom closet for negative eight hours!"

    scene broom_closet
    show george at left
    show harold at right
    show pakoo at center
    with dissolve
    george "This has got to be the dumbest story we've ever been in!"
    harold "Don't blame me, Pakoo wrote it!"
    return