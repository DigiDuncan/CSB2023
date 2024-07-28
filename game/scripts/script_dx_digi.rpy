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
    n "Their new science teacher, Mr. Weird Al Yankovic, spills some smelly sulfuric acid on a pile of toxic Mikas!"
    show harold at center
    show pakoo at mid_left
    show weird_al at right
    with move
    weird_al "Whoops!"
    n "Suddenly, the pile begins to morph into a giant evil Mika!"
    show mika at t_evil_mika behind george with vpunch
    play sound sfx_bossappears
    pause 1.0
    show david at right with moveinright
    david "Help!"
    david "A giant evil Mika just stepped on my lunch bucket and ate a Van Halen!"
    show mr_krupp at left with moveinleft
    mr_krupp "Oh, no! The poor lunch box!"
    hide george
    hide harold
    hide pakoo
    with moveoutleft
    n "George, Harold, and Pakoo try to escape by hiding behind a neutrino."
    n "Pakoo snaps his fingers."
    n "Soon, a digital grin comes across Mr. Krupp's face as he drops his dark tie and runs to his office."
    hide mr_krupp with moveoutleft
    pause 1.0
    play sound sfx_punch
    show cpt_underpants at left with moveinleft
    n "Soon, Captain Underpants punches through the wall!"
    n "He grabs a slimy M-16 and hits the monster on its elbow!"
    play sound sfx_hks1
    mika "Ouchies!"
    n "The monster turns and kicks the monster on its esaphogus!"
    play sound sfx_alt_punch
    n "Pakoo quickly mixes up a bottle of chocolate milk with bloody piles of dog shit!"
    george "Hey, Pakoo? Where did you find the jar of crazy stuff?"
    pakoo "It was right here, next to this barrel of toxic yellow Game Boys."
    harold "Oh, that makes sense."
    n "Pakoo shakes up the strange mixture and throws it at the monster!"
    show pakoo flipped at left with moveinleft
    play sound sfx_splash
    mika "Woohoo!"
    hide mika with moveoutbottom
    play sound sfx_explosion
    n "The monster dies of a massive right toe attack!"
    george "That makes sense, too."
    n "Unfortunately, some of the mixture splashes onto Captain Underpants' head, and he turns back into Mr. Krupp."
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
