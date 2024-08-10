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
    show toxic_mikas at manual_pos(1.5, 1.0, 1.0):
        zoom 0.6
    with dissolve
    n "George, Harold, and Pakoo are busy studying the wonders of gooey jugular veins."
    play sound sfx_small_spill volume 8
    n "Their new science teacher, Mr.{w=0} Weird Al Yankovic, spills some smelly sulfuric acid on a pile of toxic Mikas!"
    show harold at center
    show pakoo disappointed flipped at mid_left behind george
    show weird_al at right
    show toxic_mikas at manual_pos(1.1, 1.0, 1.0):
        zoom 0.6
    with move
    weird_al "Whoops!"
    n "Suddenly, the pile begins to morph into a giant evil Mika!"
    
    # not sure why it doesnt like zorder here but w/e
    # TODO: want pixellate here
    show toxic_mikas at center behind pakoo
    show weird_al behind toxic_mikas
    show harold at center
    with move

    play sound sfx_bossappears
    hide toxic_mikas
    show mika at t_evil_mika behind pakoo
    show david at offscreenright
    with Dissolve(0.1)
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
    play sound sfx_addy_snap
    n "Pakoo snaps his fingers."
    # TODO: hey baker, think you can clean up this trash smiling edit for me? thx - tate
    show mr_krupp grin with dissolve
    n "Soon, a digital grin comes across Mr.{w=0} Krupp's face as he drops his dark tie and runs to his office."
    show mr_krupp grin at offscreenleft with MoveTransition(0.25)
    play sound sfx_house_door_close
    pause 2.0
    play sound sfx_punch
    with hpunch
    show cpt_underpants at left with moveinleft
    n "Soon, Captain Underpants punches through the wall!"
    show cpt_underpants at mid_offscreen_left
    with MoveTransition(0.25)
    show slime16 at center_left with dissolve
    n "He grabs a slimy M-16 and hits the monster on its elbow!"
    show slime16 fire
    play sound sfx_hks1
    show mika at right behind weird_al with MoveTransition(0.25)
    show slime16
    with hpunch
    mika "Ouchies!"
    n "The monster turns and kicks Captain Underpants in his esophagus!"
    show mika at center:
        linear 0.25 xzoom -1
        linear 0.25 xzoom 1
    show cpt_underpants at manual_pos(0.3, 1.0, 1.0)
    show slime16 at manual_pos(-0.5, 0.25, 0.5):
        linear 0.5 rotate 720
    with MoveTransition(0.25)
    play sound sfx_alt_punch
    with vpunch
    pause 1.0
    show pakoo flipped at mid_left zorder 3 
    show cpt_underpants at manual_pos(0.4, 1.0, 1.0)
    show gamebarrel at manual_pos(-0.5, 0.9, 0.5) zorder 4:
        zoom 0.6
    with MoveTransition(0.25)

    play sound sfx_mc_brew
    show dookie_milk_jar at manual_pos(0.4, 0.6, 0.5) zorder 3 with dissolve:
        zoom 0.5     
    n "Pakoo quickly mixes up a bottle of chocolate milk with bloody piles of dog shit!"
    george "Hey, Pakoo? Where did you find the jar of crazy stuff?"
    show gamebarrel at manual_pos(0.1, 0.9, 0.5) with MoveTransition(0.5):
        zoom 0.6
    pakoo "It was right here, next to this barrel of toxic yellow Game Boys."
    pause 1.0
    harold "Oh, that makes sense."
    play sound sfx_water_shake
    show dookie_milk_jar:
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6   
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6   
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
        linear 0.1 ypos 0.5
        linear 0.1 ypos 0.6
    n "Pakoo shakes up the strange mixture and throws it at the monster!"
    show pakoo flipped at mid_left
    #show mika at right
    stop sound
    play sound sfx_mc_throw volume 10
    show dookie_milk_jar at manual_pos(0.5, 0.3, 0.5):
        linear 0.25 rotate 130
    with MoveTransition(0.25)
    
    play sound sfx_mc_bottlehit volume 3
    hide dookie_milk_jar with Dissolve(0.25)
    show mika:
        parallel:
            linear 0.25 rotate 90
        parallel:
            linear 0.25 xpos 2.5
        parallel:
            linear 0.25 ypos 2.0
    show realistic_explosion_anim at manual_pos(0.8, 0.7, 0.5) behind weird_al:
        subpixel True
        zoom 20
    play sound sfx_explosion
    with vpunch
    mika "Woohoo!"
    n "The monster dies of a massive right toe attack!"
    pause 1.0
    george "{i}That{/i} makes sense, too."
    play sound sfx_small_spill volume 3.0
    n "Unfortunately, some of the mixture splashes onto Captain Underpants' head, and he turns back into Mr.{w=0} Krupp."
    play sound sfx_glitch_in
    hide cpt_underpants
    hide slime16
    show mr_krupp at manual_pos(0.4, 1.0, 1.0)
    # TODO: need custom pixellate
    with pixellate
    pause 0.5
    show mr_krupp at center behind weird_al with move
    pause 1.0
    mr_krupp "Holy bright {i}penguins!"
    mr_krupp "I'll bet that George, Harold, and Pakoo are responsible for this mess!"
    show pakoo worried flipped
    mr_krupp "For your punishment, you all must chop in the broom closet for {i}negative eight hours!"
    
    pause 0.5
    scene black with dissolve
    pause 1.0

    scene broom_closet
    show george at left
    show harold at right
    show pakoo at center
    with dissolve
    pause 1.0
    george "This has got to be the {i}dumbest{/i} story we've ever been in!"
    harold "Don't blame {i}me,{/i} Pakoo wrote it!"
    return
