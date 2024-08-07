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
    play sound sfx_small_spill volume 5
    n "Their new science teacher, Mr.{w=0} Weird Al Yankovic, spills some smelly sulfuric acid on a pile of toxic Mikas!"
    # TODO: uhhhh i guess a small pile of mikas?????
    show harold at center
    show pakoo disappointed flipped at mid_left behind george
    show weird_al at right
    with move
    weird_al "Whoops!"
    # TODO: better morph
    n "Suddenly, the pile begins to morph into a giant evil Mika!"
    play sound sfx_bossappears
    show mika at t_evil_mika behind pakoo with Dissolve(0.25)
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
    # TODO: sfx - pakoo's finger snap
    n "Pakoo snaps his fingers."
    # TODO: hey baker, think you can clean up this trash edit for me? thx - tate
    show mr_krupp grin with dissolve
    n "Soon, a digital grin comes across Mr.{w=0} Krupp's face as he drops his dark tie and runs to his office."
    show mr_krupp grin at offscreenleft with MoveTransition(0.25)
    play sound sfx_house_door_close
    pause 1.0
    play sound sfx_punch
    show cpt_underpants at left with moveinleft
    with hpunch
    n "Soon, Captain Underpants punches through the wall!"
    show cpt_underpants at mid_offscreen_left
    show david at mid_right_right
    show weird_al at mid_right_right
    with MoveTransition(0.25)
    # TODO: need M-16. this will do for the moment
    show m4 at center_left with dissolve
    n "He grabs a slimy M-16 and hits the monster on its elbow!"
    show m4 fire
    play sound sfx_hks1
    with hpunch
    show m4
    mika "Ouchies!"
    show mika:
        linear 0.25 xzoom -1
    n "The monster turns and kicks the monster on its esaphogus!"
    show mika:
        linear 0.25 xzoom 1
    play sound sfx_alt_punch
    with vpunch
    show pakoo flipped at mid_left_left zorder 3 
    show cpt_underpants at left
    show m4 at truecenter
    with MoveTransition(0.25)
    # TODO: OH GOD, EXACTLY WHAT SORT OF SPRITE AM I SUPPOSED TO PUT HERE?????
    # probably gonna pixellate-censor it, whatever it is...
    # TODO: liquid shaking sfx... ewww.
    n "Pakoo quickly mixes up a bottle of chocolate milk with bloody piles of dog shit!"
    george "Hey, Pakoo? Where did you find the jar of crazy stuff?"
    pakoo "It was right here, next to this barrel of toxic yellow Game Boys."
    # TODO: lmao i have to edit a barrel here
    harold "Oh, that makes sense."
    # TODO: sfx - liquid shake
    n "Pakoo shakes up the strange mixture and throws it at the monster!"
    show pakoo flipped at left with MoveTransition(0.1)
    # TODO: sfx - minecraft potion throwing/bottle breaking instead of splash
    play sound sfx_splash
    with hpunch
    pause 1.0
    mika "Woohoo!"
    show mika:
        parallel:
            linear 0.25 rotate 90
        parallel:
            linear 0.25 xpos 0.8
        parallel:
            linear 0.25 ypos 2.0
    play sound sfx_explosion
    with vpunch
    # TODO: can i put the deltarune realistic explosion here???
    pause 1.0
    n "The monster dies of a massive right toe attack!"
    george "That makes sense, too."
    play sound sfx_small_spill volume 3.0
    n "Unfortunately, some of the mixture splashes onto Captain Underpants' head, and he turns back into Mr.{w=0} Krupp."
    play sound sfx_glitch_in
    hide cpt_underpants
    hide m4
    show mr_krupp at center
    # TODO: need custom pixellate
    with pixellate
    pause 2.0
    mr_krupp "Holy bright penguins!"
    mr_krupp "I'll bet that George, Harold, and Pakoo are responsible for this mess!"
    show pakoo worried flipped
    mr_krupp "For your punishment, you all must chop in the broom closet for negative eight hours!"

    scene black with dissolve
    pause 1.0

    scene broom_closet
    show george at left
    show harold at right
    show pakoo at center
    with dissolve
    pause 1.0
    george "This has got to be the dumbest story we've ever been in!"
    harold "Don't blame me, Pakoo wrote it!"
    return
