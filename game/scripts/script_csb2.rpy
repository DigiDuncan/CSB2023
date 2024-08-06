label csbii_start:
    $ persistent.csb2_unlocked = True
    play music time_for_a_smackdown volume 0.2 if_changed
    music Time for a Smackdown! - Mr. Sauceman
    scene helipad
    show wesley at right
    with dissolve
    show cs angry at left with moveinleft
    cs "You'll pay for what you did!"
    n "Wesley sweats nervously."
    wesley "Do you want a refund?"
    cs "I'll refund your face to the floor!"

    menu:
        "What attack would you like to use?"
        "Punch" (type = "true"):
            $ ch2_cs_attack_used = "punched"
            jump csbii_punch
        "Chop" (type = "true"):
            $ ch2_cs_attack_used = "karate-chopped"
            jump csbii_chop
        "Kick" (type = "true"):
            $ ch2_cs_attack_used = "Sparta-kicked"
            jump csbii_kick
        "Special" (type = "bad"):
            jump csbii_special

# Punch
label csbii_punch:
    play music time_for_a_smackdown volume 0.2 if_changed
    music Time for a Smackdown! - Mr. Sauceman
    scene helipad
    show wesley behind cs at right
    show cs angry at left
    cs "Take this!"
    n "CS punches Wesley and knocks him out!"
    # i'm not sorry - tate
    show cs angry at center with MoveTransition(0.25)

    show cs angry at mid_mid_right with MoveTransition(0.05)
    show wesley behind cs with hpunch
    play sound sfx_punch
    show cs angry at mid_right with MoveTransition(0.05)
    play sound sfx_punch_alt
    show wesley behind cs with vpunch

    show cs angry at mid_mid_right with MoveTransition(0.05)
    show wesley behind cs with hpunch
    play sound sfx_punch
    show cs angry at mid_right with MoveTransition(0.05)
    play sound sfx_punch_alt
    show wesley behind cs with vpunch

    show cs angry at mid_mid_right with MoveTransition(0.05)
    show wesley behind cs with hpunch
    play sound sfx_punch
    show cs angry at mid_right with MoveTransition(0.05)
    play sound sfx_punch_alt
    show wesley behind cs with vpunch

    show cs angry at center with MoveTransition(0.1)
    pause 0.5
    show cs angry at mid_right with MoveTransition(0.05)
    show cs angry at manual_pos(0.8, 0.5, 0.5) with MoveTransition(0.05)
    show wesley behind cs with hpunch
    play sound sfx_punch
    play sound2 sfx_victorypunch noloop volume 0.5
    show wesley at t_punchup with MoveTransition(0.25)
    with vpunch
    with vpunch
    pause 1.0
    play sound sfx_shoeslide
    show cs angry at left with MoveTransition(0.35)
    pause 1.0
    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at offscreenright with determination
    show ed_phone at right
    show cs angry at left
    with MoveTransition(0.5)
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump csbii_caught

# Chop
label csbii_chop:
    play music time_for_a_smackdown volume 0.2 if_changed
    music Time for a Smackdown! - Mr. Sauceman
    scene helipad
    show cs angry at left
    show wesley at right
    cs "Hi-{i}yah!{/i}" # hiya is a greeting, not the sound you're looking for - tate
    n "CS chops Wesley in the chest and he flies off the roof!"
    show cs angry at mid_mid_right with MoveTransition(0.25)
    play sound sfx_chop
    show wesley at offscreenright with MoveTransition(0.25):
        linear 0.1 xzoom -1
        linear 0.1 xzoom 1
    pause 0.5
    cs "I sawed this foundation repairman in half!"
    show ed_phone at offscreenright with determination
    show cs angry at left
    show ed_phone at right
    with MoveTransition(0.5)
    ed "Hello, 911? My coworker just got karate-chopped off the roof by a disgruntled customer! Send help!"
    jump csbii_caught

# Kick
label csbii_kick:
    play music time_for_a_smackdown volume 0.2 if_changed
    music Time for a Smackdown! - Mr. Sauceman
    scene helipad
    show cs angry at left
    show wesley at right
    show cs angry at center with MoveTransition(0.25)
    $ renpy.movie_cutscene(kick)
    show wesley at right
    show cs angry at center
    show wesley at offscreenright:
        linear 0.5 rotate 30
    with MoveTransition(0.5)

    dxcom hidemovie
    $ achievement_manager.unlock("Dead Meme")

    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at offscreenright with determination
    show cs angry at left
    show ed_phone at right
    with MoveTransition(0.5)
    ed "Hello, 911? My coworker just got kicked off the roof by a disgruntled customer! Send help!"
    hide screen dxcom
    jump csbii_caught

# Special
label csbii_special:
    play music time_for_a_smackdown volume 0.2 if_changed
    music Time for a Smackdown! - Mr. Sauceman
    scene helipad
    show cs concentrate at left
    show wesley at right
    n "CS uses his YTP Magic to make the foundation repairmen fight each other!"
    show wesley at offscreenright with MoveTransition(0.25)
    play sound sfx_punch
    with hpunch
    rich "Hey! Cut it out!"
    play sound sfx_punchalt
    with vpunch
    wesley "I'm not trying to fight you! I don't know what's happening!"
    wesley "{i}HELP!{/i}"
    play sound sfx_punch
    with hpunch
    play sound sfx_punch
    with hpunch
    rich "Ed! {i}Do{/i} something!"
    play sound sfx_punchalt
    with vpunch
    if e1:
        jump e1
    else:    
        show ed_phone at offscreenright with determination
        show ed_phone at right with MoveTransition(0.5)
    ed "Hello, 911? My coworkers are--{w=0.5}{nw}"
    play sound sfx_tape_rewind volume 0.5
    with hpunch
    n "CS sentence-mixes Ed's words!"
    ed "{sc=1.88}{color=#CB50FF}Everything is fine here, officer. No need to come here."
    ed "Wait, what just happened?!"
    n "CS quickly puts all the workers to sleep."
    show ed_phone at manual_pos(0.8, 2.0):
        linear 0.5 rotate 45
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    pause 1.0
    show cs at left
    cs "Huh. That worked a lot better than I thought."
    cs "I should use this power more often!"
    show cs happy
    cs "Welp, time to go home!"
    show cs flipped with determination
    hide cs with moveoutleft
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 1.0
    scene hoh_hq with dissolve
    show cs at left with moveinleft
    n "As CS makes to leave the building, the cops come rushing in."
    play sound sfx_siren loop
    show blue_light at left
    show red_light at right
    show copguy behind blue_light, red_light at right with moveinright
    show cs surprised
    copguy "Freeze! Put your hands in the air!"
    stop sound fadeout 1.0
    cs "What's going on? I didn't do anything!"
    show cs worried at left
    copguy "Come with us. We need to ask you some questions."
    show cs disappointed at left
    cs "Alright, sure thing, officer."
    show cs disappointed flipped with determination
    hide cs
    hide copguy
    with moveoutleft
    scene black with dissolve
    pause 1.0
    jump csbii_questioning

# Questioning
label csbii_questioning:
    scene question
    show cs disappointed dark at left
    show copguy dark at right
    with dissolve
    play music card_castle volume 0.5
    music Card Castle - Toby Fox
    pause 1.0
    copguy "Alright, CS."
    if fun_value(FUN_VALUE_MUSIC):
        copguy "This is the Card Castle."
    else:
        copguy "A lot of crazy things have happened today."
    copguy "The CEO of HoH SiS called us and he was immediately interrupted by something, or some{i}one,{/i} telling us that everything was under control."
    copguy "After reviewing the phone call, his voice sounds kinda messed up."
    cs "I, uhh, I don't know what all {i}that{/i} is about..."
    copguy "Oh, really?"
    copguy "What about all of the workers in the building? Most of them were out cold on the floor."
    show cs worried dark
    cs "Okay, fine!"
    cs "I confess!"
    cs "I was using YTP Magic on the employees to make them fight each other, and I--{w=1.0}{nw}"
    copguy "You {i}what?!{/i} What the hell are you on about?"
    cs "I have this power, and I just figured out how to--{w=0.5}{nw}"
    copguy "Alright, I've heard enough."
    copguy "Lemme call in someone more qualified to deal with this."
    copguy "Mr.{w=0} Mohs, this one's all yours."
    hide copguy with moveoutright
    show asylum_worker at right with moveinright
    asylum_worker "Sure thing, boss."
    pause 1.0
    asylum_worker "Alright, buddy. Come follow me."
    hide asylum_worker
    hide cs
    with moveoutright
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 1.0
    jump csbii_asylum

# Asylum
label csbii_asylum:
    scene asylum with dissolve
    play music basement volume 0.5
    music Basement - Toby Fox
    pause 2.0
    show cs insane worried flipped dark at left with moveinright
    show cs insane worried dark with determination
    show asylum_worker at right with moveinright
    pause 1.0
    if fun_value(FUN_VALUE_MUSIC):
        asylum_worker "Here's your basement. Enjoy living out the rest of your life here."
    else:
        asylum_worker "Here's your room. Enjoy living out the rest of your life here."
    show cs insane worried dark at center with moveinleft
    cs "Sir, you need to listen to me! I'm not crazy!"
    asylum_worker "That's what they all say."
    asylum_worker "Get off of me."
    show asylum_worker at mid_mid_right with MoveTransition(0.1)
    play sound sfx_punch
    show cs insane worried dark:
        linear 0.25 ypos 2.0
    with MoveTransition(0.25)
    with vpunch
    show asylum_worker at right with MoveTransition(0.1)
    pause 1.0
    asylum_worker "Sorry it had to be this way, bud."
    hide asylum_worker with moveoutright
    pause 0.5
    play sound sfx_house_door_close
    pause 3.0
    show cs insane disappointed dark at center with MoveTransition(1.0)
    pause 1.0
    cs "Ow..."
    cs "This isn't fair!"
    show cs insane worried dark
    csgod "Hey!" with vpunch
    csgod "Quit the whining!"
    show csgod at offscreenright with determination:
        alpha 0
    show csgod:
        parallel:
            linear 2.0 alpha 1.0
        parallel:
            linear 0.5 xpos 0.6
    show cs insane worried dark at left 
    with MoveTransition(2.0)
    pause 1.0
    cs "What?"
    cs "Who are you?"
    csgod "I am CSGod. It was I who used the YTP power."
    cs "{i}What?!{/i} How?"
    show cs insane disappointed dark
    cs "I am so confused..."
    
    # tate was here
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        csgod "You channeled my power. You had it all, right there at your fingertits."
    else:
        csgod "You channeled my power through your fingertips."
    csgod "That was how you were able to use those abilities back at HoH SiS HQ."
    csgod "However, it seems that you weren't good enough at lying to get yourself out of this situation."
    show cs insane disappointed dark
    cs "Well, I wanted to be honest!"
    csgod "Yeah, well, look where honesty got you."
    show cs insane disappointed dark
    csgod "No mortal would ever believe in something as silly as YTP Magic."
    csgod "For your punishment, I shall leave you here you a while."
    show cs insane worried dark
    cs "No! Please!"
    csgod "You will get out soon enough, but maybe you should think about making a {i}better choice{/i} next time."
    hide csgod with dissolve
    stop music fadeout 3.0
    music end
    window hide
    bad_end "Silly CS!\nYTP Magic doesn't exist!" "csbii_start"
    return
    
# Caught
label csbii_caught:
    play music time_for_a_smackdown volume 0.2 if_changed
    music Time for a Smackdown! - Mr. Sauceman
    scene helipad
    show ed_phone at right
    show cs angry at left
    cs "Damn it! Ed's calling the police! I've gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    play sound sfx_siren loop
    show blue_light at left
    show red_light at right
    n "The police arrive and CS runs away."
    show cs angry flipped with determination
    show cs angry flipped at offscreenleft with MoveTransition(0.25)
    show ed_phone behind blue_light, red_light at left with move
    show copguy behind blue_light, red_light, ed_phone at right with moveinright
    copguy "Get back here!"
    show copguy at offscreenleft with MoveTransition(0.25)
    cs "You can't catch me, I'm the speedy Michael Rosen!"
    stop music fadeout 3.0
    music end
    n "As CS is not actually the speedy Michael Rosen, he is quickly apprehended by the police."
    play sound2 sfx_punch noloop
    with hpunch
    pause 2.0
    stop sound fadeout 1.0
    scene black with dissolve
    pause 2.0
    jump csbii_jail

label csbii_jail:
    stop music fadeout 3.0
    music end
    pause 2.0
    scene jail_inside with dissolve
    show cs prison flipped at offscreenright
    show copguy at offscreenright
    with determination
    show cs prison flipped at left
    show copguy at right
    with move
    show cs prison
    pause 1.0
    copguy "Alright, welcome to the slammer. How tough are ya?"
    cs "How tough am I? {bt=a3-p10-s4}How tough am I?!{/bt}"
    cs "I beat {i}Cuphead!{/i}"
    copguy "So?"
    cs "{i}In under 90 minutes!"
    copguy "Hmm... okay. You're a tough enough guy to handle this cellmate, then."

    hide copguy with moveoutright
    pause 1.0
    show arceus prison at right with moveinright
    pause 1.0
    play music stal volume 0.4
    music stal - C418
    if fun_value(FUN_VALUE_MUSIC):
        cs "Oh, hi, Arceus. Sorry for stal-ing."
    else:
        cs "Oh, hi, Arceus."
    arceus "Heya, CS. .w."
    # And it's about time.
    cs "So, what're you in for?"
    arceus "Putting spyware on a politician's phone."
    cs "Yeah, no, that checks out."
    arceus "And, from my recent debug of {i}CSBounciness,{/i} I know that {i}you're{/i} in for beating up workers at HoH SiS."
    cs "Your what?"
    arceus "... Never mind."
    arceus "Why'd you do it, anyhow?"
    show cs prison_worried at left
    cs "I was 100-percent unsatisfied."
    arceus "As was I. As was I..."
    n "A brief moment of silence..."
    show cs prison at left
    arceus "Welp. I'm tired of this place. Wanna break out?"
    cs "Eh... sure, why not. I've played plenty of {i}The Escapists.{/i} I should be able to figure it out."
    cs "We should break out at least one other person though."
    arceus "If you say so... Who were you thinking of breaking out?"
    cs "Let's just break out that guy next to us. I think his name was Anno...?"
    arceus "Anno? Sure. I've seen what he's capable of, so he may be of use to us."
    cs "Alright, then! Let's get going!"

    show arceus prison at offscreenright
    show cs prison at offscreenleft
    with ease
    pause 1.0
    jump csbii_breakout

label csbii_breakout:
    play music stal volume 0.4 if_changed
    music stal - C418
    scene jail_cell
    show cs prison at left
    show arceus prison at right
    with dissolve

    dxcom prisonroute

    pause 1.0
    arceus "So, what's the plan? I've been trying to break outta here for five years."
    cs "Well, for starters, I need to get a feel for the routine here."
    arceus "I really can't stand being here another minute. I'll give you the rundown. Hasn't changed then, won't change now." 
    n "Arceus describes the prison routine to CS."  # DX: Replace with blur, fade out then back in
    cs "I think I got all that."
    arceus "So, what's our plan, boss?"
    cs "I've gotta grab a few plastic spoons from the mess hall, a cup of molten chocolate, a guard uniform, and a change of shorts."
    arceus "... Why a change of shorts?"
    show cs prison_worried at left
    cs "You kidding me? I'm gonna shit myself, 'cause this is scary as hell."
    arceus "Fair enough."
    hide screen dxcom
    scene black with dissolve

    stop music fadeout 3.0
    music end
    n "The day comes to an end and the next one follows."
    n "CS and Arceus gather the required essentials for their escape. Along the way, they inform Anno, who more than happily complies with the plan." 
    centered "The next evening..."
    play music moongazer volume 0.5
    music Moongazer - Dr. Awesome
    if fun_value(FUN_VALUE_MUSIC):
        anno "I can't wait to gaze at the moon again once we're out of here."
    cs "Key, check."

    show arceus prison flipped at left with moveinleft
    arceus "Uniforms, check."

    show anno prison at right with moveinright
    anno "Spoons, check."

    show cs prison at center with dissolve
    cs "Extra shorts..."
    cs "Check."
    cs "Alright, men! Let's get the heck out of here!"

    scene black with dissolve

    n "In the dark of night, the three begin chipping away at their cell floor."
    n "Upon breaking through, they set up makeshift dummies in their beds with their prison jumpsuits, then don their acquired guard uniforms."

    scene tunnel with dissolve
    # If anyone asks, Arceus is part god and can dig really easily, I guess.

    n "They begin digging quickly, putting distance between themselves and their cells."
    show cs guard dark at left with easeinleft
    dxcom tint
    cs "Jeez... I didn't think that would actually work."

    show arceus guard at right with easeinright
    arceus "You {i}what?" 
    
    show anno guard dark with easeinbottom
    anno "How are we supposed to cross the border with the new wall?"
    arceus "Not the Mexican border, the Canadian border. We're in Washington, it's way closer, and they're too polite to send us back."
    cs "Works for me. Free healthcare!"
    arceus "Well, you have to live there for a few years before you get access to that, but you {i}should{/i} last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."
    hide cs
    hide anno guard
    hide arceus
    with dissolve
    n "The three continue to dig for hours, until their hands begin to blister and their spoons break."
    arceus "Based on my instinct, and on my tiredness, this should be far enough."
    n "The now-escaped fugitives dig upwards for their ascent towards the surface."
    stop music fadeout 3.0
    music end

    hide screen dxcom
    hide cs with dissolve
    hide arceus with dissolve
    hide anno with dissolve
    jump csbii_bordercrossing

label csbii_bordercrossing:
    scene border with dissolve
    play music onett volume 0.6
    music Onett Theme - Keiichi Suzuki
    if fun_value(FUN_VALUE_MUSIC):
        n "CS, Anno, and Arceus emerge and begin heading north towards Onett. Theme."
    else:
        n "CS, Anno, and Arceus emerge and begin heading north towards the border crossing."
    n "A wild border guard appears."
    show border_guard at center with dissolve
    # INTENTIONAL DISSOLVE: Pokemon reference
    if fun_value(FUN_VALUE_COMMON):
        border_guard "Eh, Schnitzelburg!"
    pause 1.0
    border_guard "I'm going to need proof of citizenship, eh."
    show border_guard at right
    show arceus flipped at left 
    with moveinleft
    arceus "Colour is spelled with a u, eh."
    border_guard "Works for me, eh."

    scene canada with dissolve 
    n "Some time passes as the party ventures forth into the land of Canada."
    cs "Arceus, can we stop somewhere? I'm getting hungry."
    anno "Yeah, we've been walking for miles now."
    arceus "Guys. We've only {i}just{/i} left the border. You can still see it behind us."
    scene flag
    $ renpy.music.set_pause(True, "music")
    play music2 star_spangled_banner
    music The Star Spangled Banner - THE UNITED STATES OF AMERICA
    if fun_value(FUN_VALUE_MUSIC):
        n "The crew looks behind them and hears The Star Spangled Banner playing."
    else:
        n "The crew looks behind them and still sees a faint American flag waving."
    scene canada
    stop music2
    $ renpy.music.set_pause(False, "music")
    "..."
    cs "Prison food just isn't all that filling."
    arceus "I suppose we could find a Tim Horton's. It's as common in Canada as McDonald's is in America."
    n "Anno and CS nod aggressively."
    n "Arceus sniffs the air."
    arceus "There's one just over here, come on."

    scene black with dissolve
    pause 1.0
    scene outside_tim_hortons
    show cs disappointed at left
    with dissolve
    pause 1.0
    cs "I'm starving after all that walking. I need a donut."
    show cs at offscreenright with move
    show arceus flipped at offscreenright with moveinleft
    show anno at offscreenright with moveinleft
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 2.0

    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    with dissolve
    play music buy_something volume 0.6
    music Buy Something Will Ya! - Keiichi Suzuki
    pause 1.0
    show cs at right with moveinleft
    show arceus flipped at center with moveinleft
    show anno at left with moveinleft
    pause 1.0

    show cs flipped
    if fun_value(FUN_VALUE_MUSIC):
        anno "Arceus, buy something, will ya?"
    else: 
        anno "Finally."
    show cs flipped at mid_offscreen_right
    show anno at mid_offscreen_left
    show arceus full flipped at t_arc_at_tims
    with MoveTransition(0.5)
    pause 1.0

    arceus "Hi."
    cashier "Can I help you?"
    arceus "Can I have a dozen glazed donuts, please?"
    cashier "Oh, hi, Arceus. I didn't know it was you."

    anno "Wait, huh?"
    show arceus full flipped at t_arc_at_tims
    cashier "Here you go."
    show arceus full happy flipped
    arceus "That's me!"
    show arceus full flipped
    arceus "How much is it?"
    cashier "It'll be $18.{nw}"
    show arceus full happy flipped
    arceus "Here you go! Keep the change."
    arceus "Hi doggy!"
    cashier "You're my favorite customer."
    show arceus full flipped
    arceus "Thanks a lot! Bye~"
    show arceus full at t_arc_at_tims
    hide arceus with moveoutleft
    cashier "Buh-bye!"
    stop music fadeout 3.0
    music end

    show cs disappointed flipped at right
    show anno at left
    with ease

    cs "..."
    cs "I think I'm {i}really{/i} sleep-deprived."

    $ achievement_manager.unlock("Ohai, Mark")
    scene black with dissolve
    pause 1.0

    play music buy_something volume 0.6
    scene inside_tim_hortons_2
    show cs
    show anno at left
    show arceus at right
    show tims_dozen at manual_pos(0.4, 0.6)
    with dissolve

    pause 1.0
    n "CS, Arceus, and Anno enjoy some well-deserved donuts."
    pause 1.0
    show arceus worried
    "..."
    arceus "Sorry to interrupt you two, but we may have a problem."
    show cs disappointed
    arceus "Those donuts cost me the last of my money. We're going to need to find a way to make some cash."
    pause 1.0
    scene outside_ltt with dissolve
    n "CS looks across the street to see Linus Media Group."

    scene inside_tim_hortons_2
    show cs surprised
    show anno at left
    show arceus at right
    show tims_dozen at manual_pos(0.4, 0.6)
    with dissolve
    pause 1.0
    cs "Linus Media Group, huh?"
    show cs
    cs "I {i}do{/i} have a lot of video editing experience..."
    show cs happy
    cs "Maybe I can get a job there!"
    stop music fadeout 3.0
    music end

    scene black with dissolve
    pause 2.0
    n "CS walks into the studio to ask for a job."
    jump csbii_ltt

label csbii_ltt:
    scene inside_ltt
    show linus
    with dissolve
    pause 1.0
    if fun_value(FUN_VALUE_RARE):
        play music passport_ytp volume 0.5
    else:
        play music passport volume 0.5
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    music PASSPORT.MID - George Stone
    if fun_value(FUN_VALUE_MUSIC):
        linus "Sure, you can have a job. Just show us your passport and you're ready to go!"
    else: 
        linus "Sure, you can have a job. Just show us proof of citizenship and you're ready to go!"
    cs "Colour is spelled with a u, eh."
    linus "I need actual papers. Last time I hired someone who used {i}that{/i} as proof of citizenship, I got fined and had to sell one of my thousands of 4090s!"
    cs "Oh, um..."
    cs "I'll be right back."
    pause 1.0

    scene outside_ltt
    show arceus at right
    with dissolve
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show cs disappointed at left with moveinleft
    pause 1.0
    show cs worried
    cs "Arc, what am I gonna do? They need proof I'm legal to work."
    show cs disappointed
    arceus "Hmmm..."
    n "A lightbulb goes off in Arceus' head."
    arceus "Leave it to me."
    hide arceus
    show arceus flipped at right
    hide arceus flipped with moveoutright

    scene alley
    with dissolve
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show arceus flipped with moveinleft

    n "Arceus rummages around in the dumpsters behind LMG."
    arceus "Hnng...{w} hmmpmh... {w}{i}aha!"
    show craptop at manual_pos(0.55, 0.5) with dissolve
    n "Arceus finds an old laptop."
    arceus "Perfect."
    play sound sfx_keyboard
    n "Within minutes, Arceus has hacked the Canadian government records to display CS as having a valid work visa."
    arceus "Even their security is too nice..."
    # TODO: please replace this with an accurate image. idk what it actually looks like -tate
    show crt_magnet at manual_pos(0.35, 0.6) with dissolve
    n "Arceus digs through the dumpster more and finds a magnet from an old CRT."
    show crt_magnet at manual_pos(0.55, 0.5) with MoveTransition(0.5)
    n "He places it against the laptop, corrupting the hard drive instantly."
    arceus "Without a trace."
    hide craptop
    hide crt_magnet
    with dissolve
    n "He discards both items and rushes out of the alley."
    pause 0.5

    hide arceus flipped
    show arceus
    hide arceus with moveoutleft

    scene outside_ltt
    show cs disappointed at left
    with dissolve
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show arceus at right with moveinright

    pause 1.0
    arceus "All taken care of."
    cs "What did you do?"
    arceus "Don't worry about it. Just have them look you up."

    scene black with dissolve
    pause 1.0
    scene inside_ltt
    show linus
    with dissolve
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    pause 1.0
    linus "I didn't think you could have a number as a last name..."
    linus "Yep, there you are, cs188, with a valid working visa."
    linus "Looks like you're hired!"
    cs "Ohhh yes!"
    cs "{i}ahem{/i}{w=0.5}\nI mean, thank you, Linus!"
    pause 1.0
    scene black with dissolve
    pause 1.0
    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    show anno at right
    show tims_dozen at manual_pos(0.8, 0.6)
    with dissolve
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    pause 1.0
    show arceus flipped at left
    show cs
    with moveinleft

    show cs happy
    cs "I did it! I got the job!"
    anno "Woohoo!"
    show arceus happy flipped
    arceus "I had a feeling that that would work!"
    anno "Let's celebrate!"
    
    # audio is not ready yet - tate
    dxcom donuts
    
    show donut_1 at manual_pos(0.2, 0.7)
    show donut_2 at manual_pos(0.5, 0.7)
    show donut_3 at manual_pos(0.7, 0.7)
    with dissolve
    
    show arceus happy flipped at mid_left
    show anno at mid_right
    show donut_1 at manual_pos(0.4, 0.25)
    show donut_2 at manual_pos(0.45, 0.25)
    show donut_3 at manual_pos(0.5, 0.25)
    with MoveTransition(0.25)
    
    n "The three cheer and raise up their donuts, pressing them together in a sort of toast."
    # I FINALLY FIGURED OUT HOW TO REWRITE THAT FUCKING LINE HOLY SHIT - TATE
    pause 1.0
    stop music fadeout 3.0
    music end

    $ achievement_manager.unlock("Welcome to CSBIII, Mother Fucker")

    scene black with dissolve
    hide dxcom
    pause 1.0
    jump csbiii_start
