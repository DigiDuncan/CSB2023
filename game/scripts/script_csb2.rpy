label csbii_start:
    $ persistent.csb2_unlocked = True
    scene helipad
    show wesley at right
    with fade
    show cs angry at left with moveinleft
    cs "You'll pay for what you did!"
    n "Wesley sweats nervously."
    wesley "Do you want a refund?"
    cs "I'll refund your face to the floor!"
    hide cs
    hide wesley

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
    show cs angry at left
    show wesley at right
    cs "Take this!"
    n "CS punches Wesley and knocks him out."
    show cs angry at center with move
    play sound "sfx_punch.ogg"
    play sound "sfx_punch.ogg"
    show wesley at right with hpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show wesley at right with vpunch
    play sound "sfx_punch.ogg"
    show wesley at right with hpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show wesley at right with vpunch
    play sound "sfx_punch.ogg"
    show wesley at right with hpunch
    play sound "sfx_punch.ogg"
    play sound "sfx_punchalt.ogg"
    show wesley at right with vpunch
    play sound "sfx_punch.ogg"
    show wesley at right with hpunch
    play sound "sfx_victorypunch.ogg" volume 0.5
    show wesley at t_punchup with move
    show cs angry at left with move
    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at right with moveinright
    show cs angry at left with move
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump csbii_caught

# Chop
label csbii_chop:
    show cs angry at left
    show wesley at right
    cs "Hi-{i}yah!{/i}" # hiya is a greeting, not the sound you're looking for - tate
    n "CS chops Wesley in the chest and he flies off the roof."
    show cs angry at center with move
    play sound "sfx_chop.ogg"
    hide wesley with easeoutright
    show cs angry at left with move
    cs "I sawed this foundation repairman in half!"
    show ed_phone at right with moveinright
    show cs angry at left with move
    ed "Hello, 911? My coworker just got karate chopped off the roof by a disgruntled customer! Send help!"
    jump csbii_caught

# Kick
label csbii_kick:
    show cs angry at left
    show wesley at right
    $ renpy.movie_cutscene("movies/kick.webm")
    hide wesley with easeoutright
    show cs angry at left with move

    dxcom hidemovie
    $ achievement_manager.unlock("Dead Meme")

    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at right with moveinright
    show cs angry at left with move
    ed "Hello, 911? My coworker just got kicked off the roof by a disgruntled customer! Send help!"
    hide screen dxcom
    jump csbii_caught

# Special
label csbii_special:
    show cs concentrate at left
    show wesley at right
    n "CS uses his YTP Magic to make the foundation repairmen fight each other."
    hide wesley at right with moveoutright
    play sound "sfx_punch.ogg"
    rich "Hey! Cut it out!"
    play sound "sfx_punch.ogg"
    wesley "I'm not trying to fight you! I don't know what's happening! {i}Help!!{/i}"
    play sound "sfx_punch.ogg"
    rich "Ed! Do something!"
    play sound "sfx_punch.ogg"
    if e1:
        jump e1
    else:    
        show ed at right with moveinright
    ed "Hello, 911? My coworkers are--"
    n "CS sentence-mixes Ed's words."
    ed "Everything is fine here, officer. No need to come here."
    ed "Wait, what just happened?"
    n "CS quickly puts all the workers to sleep."
    hide ed with moveoutbottom
    show cs at left
    cs "Huh. That worked a lot better than I thought. I should use this power more!"
    cs "Welp, time to go home!"
    show cs flipped with determination
    hide cs with moveoutleft
    stop music fadeout 3.0
    music end
    scene black with fade
    scene hoh_hq with fade
    show cs at left with moveinleft
    n "As CS makes to leave the building, the cops come rushing in."
    play sound "sfx_siren.ogg" loop
    show blue_light at left
    show red_light at right
    show copguy behind blue_light, red_light at right with moveinright
    copguy "Freeze! Put your hands in the air!"
    stop sound fadeout 1.0
    cs "What's going on? I didn't do anything!"
    show cs worried at left
    copguy "Come with us. We need to ask you some questions."
    show cs at left
    cs "Alright, sure thing, officer."
    show cs flipped with determination
    hide cs
    hide copguy
    with moveoutleft
    scene black with fade
    jump csbii_questioning

# Questioning
label csbii_questioning:
    scene question with fade
    play music "<loop 0>card_castle.ogg" volume 0.5
    music Card Castle - Toby Fox
    show cs disappointed at left with moveinleft
    show copguy at right with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        copguy "Alright, CS. This is the Card Castle."
    else:
        copguy "Alright, CS. A lot of crazy things happened today."
    copguy "The CEO of HoH SiS called us and he was immediately interrupted by something, or some{i}one,{/i} telling us that everything was under control."
    copguy "After reviewing the phone call, his voice sounds kinda messed up."
    cs "I, uhh, I don't know what that is all about..."
    copguy "Oh, really?"
    copguy "What about all of the workers in the building? Most of them were out cold on the floor."
    cs "Okay, fine!"
    cs "I confess!"
    cs "I was using YTP Magic on the employees to make them fight each other, and I--"
    copguy "You what? What the hell are you on about?"
    cs "I have this power, and I just figured out how to--"
    copguy "Alright, I've heard enough."
    copguy "Lemme call in someone to deal with this."
    copguy "Mr. Mohs, you can deal with this man."
    hide copguy with moveoutright
    show asylum_worker at right with moveinright
    asylum_worker "Sure thing, boss."
    asylum_worker "Come on, follow me this way at once."
    hide asylum_worker
    hide cs
    with moveoutright
    stop music fadeout 3.0
    music end
    scene black with fade
    jump csbii_asylum

# Asylum
label csbii_asylum:
    scene asylum with fade
    play music "<loop 0>basement.ogg" volume 0.5
    music Basement - Toby Fox
    show cs insane worried flipped at left with moveinright
    show cs insane worried with determination
    show asylum_worker at right with moveinright
    if fun_value(FUN_VALUE_MUSIC):
        asylum_worker "Here's your basement. Enjoy living out the rest of your life here."
    else:
        asylum_worker "Here's your room. Enjoy living out the rest of your life here."
    show cs insane worried at center with moveinleft
    cs "Sir, you need to listen to me! I'm not crazy!"
    asylum_worker "That's what they all say. Get off of me."
    play sound "sfx_punch.ogg"
    show cs insane worried with vpunch
    hide cs worried with moveoutbottom
    asylum_worker "Sorry it had to be this way, bud."
    hide asylum_worker with moveoutright
    pause 3.0
    show cs insane disappointed at center with moveinbottom
    cs "Ow..."
    cs "This isn't fair!"
    csgod "Hey!"
    csgod "Quit the whining!"
    show csgod at right
    show cs insane disappointed at left
    with moveinright
    cs "What?"
    cs "Who are you?"
    csgod "I am CSGod, and it was I who used the YTP power."
    cs "{i}What?!{/i} How? I am so confused."
    
    # tate was here
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        csgod "You channeled my power. You had it all, right there at your fingertits."
        csgod "That was how you were able to use those abilities back at HoH SiS HQ."
    else:
        csgod "You channeled my power through your fingertips. That was how you were able to use those abilities back at HoH SiS HQ."
    csgod "However, it seems that you weren't good enough at lying to get yourself out of this situation."
    cs "Well, I wanted to be honest!"
    csgod "Yeah, well, look where honesty got you."
    csgod "No mortal would ever believe in something as silly as YTP Magic."
    csgod "For your punishment, I shall leave you here you a while."
    cs "No! Please!"
    csgod "You will get out soon enough, but maybe you should think about making a {i}better choice{/i} next time."
    hide csgod with moveoutright
    stop music fadeout 3.0
    music end
    window hide
    bad_end "Silly, CS!\nYTP Magic doesn't exist!" "csbii_start"
    return
    
# Caught
label csbii_caught:
    cs "Damn it! Ed's calling the police! I've gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    play sound "sfx_siren.ogg" loop
    show blue_light at left
    show red_light at right
    n "The police arrive and CS runs away."
    show cs angry flipped with determination
    hide cs angry flipped with moveoutleft
    show ed_phone behind blue_light, red_light at left with move
    show copguy behind blue_light, red_light  at right with moveinright
    copguy "Get back here!"
    cs "You can't catch me, I'm the speedy Michael Rosen!"
    stop music fadeout 3.0
    music end
    n "As CS is not actually the speedy Michael Rosen, he is quickly apprehended by the police."
    stop sound fadeout 1.0
    scene black with fade
    jump csbii_jail

label csbii_jail:
    scene jail_inside with fade
    show cs prison at offscreenleft
    show copguy at offscreenright
    with determination
    show cs prison at left
    show copguy at right
    with move
    copguy "Alright, welcome to the slammer. How tough are ya?"
    cs "How tough am I?! {bt=a3-p10-s4}How tough am I?!{/bt} I beat {i}Cuphead!{/i}"
    copguy "So?"
    cs "{i}In under 90 minutes!"
    copguy "Hmm... okay, you're a tough enough guy to handle this cellmate, then."

    hide copguy with moveoutright
    show arceus prison at right with moveinright

    play music "<loop 0>stal.ogg" volume 0.4
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
    arceus "And from my recent debug of {i}CSBounciness,{/i} I know that you're in for beating up workers at HoH SiS."
    cs "Your what?"
    arceus "Never mind. Why'd you do it, anyhow?"
    show cs prison_worried at left
    cs "I was 100 percent unsatisfied."
    arceus "As was I. As was I..."
    n "A brief moment of silence..."
    show cs prison at left
    arceus "Welp. I'm tired of this place. Wanna break out?"
    cs "Eh... sure, why not. I've played plenty of {i}The Escapists.{/i} I should be able to figure it out."
    cs "We should break out at least one other person though."
    arceus "If you say so... Who were you thinking of breaking out?"
    cs "Let's just break out that guy next to us, I think his name was Anno...?"
    arceus "Anno? Sure, I've seen what he's capable of, so he may be of use to us."
    cs "Alright, then, let's get going!"

    show arceus prison at offscreenright
    show cs prison at offscreenleft
    with ease
    jump csbii_breakout

label csbii_breakout:
    scene jail_cell
    show cs prison at left
    show arceus prison at right
    with dissolve

    dxcom prisonroute

    arceus "So, what's the plan? I've been trying to break outta here for five years."
    cs "Well, for starters, I need to get a feel for the routine here."
    arceus "I really can't stand being here another minute. I'll give you the rundown. Hasn't changed then, won't change now." 
    n "Arceus describes the prison routine to CS."  # DX: Replace with blur, fade out then back in
    cs "I think I got all that."
    arceus "So, what's our plan, boss?"
    cs "I've gotta grab a few plastic spoons from the mess hall, a cup of molten chocolate, a guard uniform, and a change of shorts."
    arceus "Why a change of shorts?"
    show cs prison_worried at left
    cs "You kidding me? I'm gonna shit myself, 'cause this is scary as hell."
    arceus "Fair enough."
    hide screen dxcom
    scene black with fade

    stop music fadeout 3.0
    music end
    n "The day comes to an end and the next one follows. CS and Arceus gather the required essentials for their escape. Along the way, they inform Anno, who more than happily complies with the plan." 
    centered "The next evening..."
    play music "<loop 0>moongazer.ogg" volume 0.5
    music Moongazer - Dr. Awesome
    if fun_value(FUN_VALUE_MUSIC):
        anno "I can't wait to gaze at the moon again once we're out of here."
        cs "Key, check."
    else:
        cs "Key, check."

    show arceus prison flipped at left with moveinleft
    arceus "Uniforms, check."

    show anno prison at right with moveinright
    anno "Spoons, check."

    show cs prison at center with dissolve
    cs "Extra shorts..."
    cs "Check."
    cs "Alright, men, let's get the heck out of here!"

    scene black with dissolve

    n "In the dark of night, the three begin chipping away at their cell floor."
    n "Upon breaking through, they set up makeshift dummies in their beds with their prison jumpsuits, then don their acquired guard uniforms."

    scene tunnel with fade
    # If anyone asks, Arceus is part god and can dig really easily, I guess.

    n "They begin digging quickly, putting distance between themselves and their cells."
    show cs guard dark at left with easeinleft
    dxcom tint
    cs "Jeez... I didn't think that would actually work."

    show arceus guard at right with easeinright
    arceus "You what?" 
    
    show anno guard dark with easeinbottom
    anno "How are we supposed to cross the border with the new wall?"
    arceus "Not the Mexican border, the Canadian border. We're in Washington, it's way closer, and they're too polite to send us back."
    cs "Works for me. Free healthcare!"
    arceus "Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."
    hide cs
    hide anno guard
    hide arceus
    with dissolve
    n "The three continue to dig for hours, until their hands begin to blister and their spoons break."
    arceus "Based on my instinct, and my tiredness, this should be far enough."
    n "The now-escaped fugitives dig upwards for their ascent to the surface."
    stop music fadeout 3.0
    music end

    hide screen dxcom
    hide cs with dissolve
    hide arceus with dissolve
    hide anno with dissolve
    jump csbii_bordercrossing

label csbii_bordercrossing:
    scene border with fade
    play music "<loop 0>onett.ogg" volume 0.6
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
    border_guard "I'm going to need proof of citizenship, eh."
    show border_guard at right with move
    show arceus flipped at left with moveinleft
    arceus "Colour is spelled with a u, eh."
    border_guard "Works for me, eh."

    scene canada with fade 
    n "Some time passes as the party ventures forth into the land of Canada."
    cs "Arceus, can we stop somewhere? I'm getting hungry."
    anno "Yeah, we've been walking for miles now."
    arceus "Guys. We've only just left the border. You can still see it behind us."
    scene flag
    $ renpy.music.set_pause(True, "music")
    play music2 "star_spangled_banner.ogg"
    music The Star Spangled Banner - THE UNITED STATES OF AMERICA
    if fun_value(FUN_VALUE_MUSIC):
        n "The crew looks behind them and hears The Star Spangled Banner playing."
    else:
        n "The crew looks behind them and still sees a faint American flag waving."
    scene canada
    stop music2
    $ renpy.music.set_pause(False, "music")
    cs "Prison food just isn't all that filling."
    arceus "I suppose we could find a Tim Horton's. It's as common in Canada as McDonald's is in America."
    n "Anno and CS nod aggressively."
    n "Arceus sniffs the air."
    arceus "There's one just over here, come on."

    scene outside_tim_hortons
    show cs disappointed at left
    with fade
    cs "I'm starving after all that walking. I need a donut."
    show cs at offscreenright with move
    show arceus flipped at offscreenright with moveinleft
    show anno at offscreenright with moveinleft
    stop music fadeout 3.0
    music end

    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    with fade
    play music "<loop 0>buy_something.ogg" volume 0.6
    music Buy Something Will Ya! - Keiichi Suzuki
    show cs at right with moveinleft
    show arceus flipped at center with moveinleft
    show anno at left with moveinleft
    
    show cs flipped
    if fun_value(FUN_VALUE_MUSIC):
        anno "Arceus, buy something, will ya?"
    else: 
        anno "Finally."
    show cs flipped at mid_offscreen_right
    show anno at mid_offscreen_left
    show arceus full flipped at t_arc_at_tims
    with ease

    arceus "Hi."
    cashier "Can I help you?"
    arceus "Can I have a dozen glazed donuts, please?"
    cashier "Oh, hi Arceus, I didn't know it was you."

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
    play music "<loop 0>buy_something.ogg" volume 0.6
    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    show cs
    show anno at left
    show arceus at right
    with fade

    n "CS, Arceus, and Anno enjoy some well-deserved donuts."
    show arceus worried
    arceus "Sorry to interrupt you two, but we may have a problem. Those donuts cost me the last of my money. We're going to need to find a way to make some cash."
    scene outside_ltt
    n "CS looks across the street to see Linus Media Group."

    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    show cs
    cs "Linus Media Group, huh? I have a lot of video editing experience... maybe I can get a job there!"
    stop music fadeout 3.0
    music end

    scene black with fade
    n "CS walks into the studio to ask for a job."

    scene inside_ltt
    show linus
    with fade
    if fun_value(FUN_VALUE_RARE):
        play music "<loop 0>passport_ytp.ogg" volume 0.5
    else:
        play music "<loop 0>passport.ogg" volume 0.5
    if fun_value(FUN_VALUE_EPIC):
        show passportdigi with dissolve
    else:
        hide passportdigi
    music PASSPORT.MID - George Stone
    if fun_value(FUN_VALUE_MUSIC):
        linus "Sure, you can have a job. Just show us your passport and you're ready to go!"
    else: 
        linus "Sure, you can have a job. Just show us proof of citizenship and you're ready to go!"
    cs "Colour is spelled with a u, eh."
    linus "I need actual papers. Last time I hired someone who used {i}that{/i} as proof of citizenship, I got fined and had to sell one of my thousands of 4090s."
    cs "Ummmm, I'll be right back."

    scene outside_ltt
    show arceus at right
    with dissolve
    if fun_value(FUN_VALUE_EPIC):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show cs at left with moveinleft
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
    if fun_value(FUN_VALUE_EPIC):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show arceus flipped with moveinleft

    n "Arceus rummages around in the dumpsters behind LMG."
    arceus "Hnng...{w} hmmpmh... {w}aha!"
    n "Arceus finds an old laptop."
    arceus "Perfect."
    n "Within minutes, Arceus has hacked the Canadian government records to display CS as having a valid work visa."
    arceus "Even their security is too nice..."
    n "Arceus digs through the dumpster more and finds a magnet from an old CRT."
    n "He places it against the laptop, corrupting the hard drive instantly."
    arceus "Without a trace."
    n "He discards both items and rushes out of the alley."

    hide arceus flipped
    show arceus
    hide arceus with moveoutleft

    scene outside_ltt
    show cs at left
    with dissolve
    if fun_value(FUN_VALUE_EPIC):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show arceus at right with moveinright

    arceus "All taken care of."
    cs "What did you do?"
    arceus "Don't worry about it. Just have them look you up."

    scene black with fade
    scene inside_ltt
    show linus
    with fade
    if fun_value(FUN_VALUE_EPIC):
        show passportdigi with dissolve
    else:
        hide passportdigi
    linus "I didn't think you could have a number as a last name..."
    linus "Yep, there you are, cs188, with a valid working visa."
    linus "Looks like you're hired!"
    cs "Ohhh yes! {w}{i}ahem{/i} I mean, thank you, Linus!"

    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    show anno at right
    show arceus flipped at left
    with fade
    if fun_value(FUN_VALUE_EPIC):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show cs happy with moveinleft

    cs "I did it! I got the job!"
    anno "Woohoo!"
    show arceus happy flipped
    arceus "Hell yeah!"

    anno "Let's celebrate!"
    n "The three cheer and raise up their donuts, pressing them together in a sort of toast."
    # I FINALLY FIGURED OUT HOW TO REWRITE THAT FUCKING LINE HOLY SHIT - TATE
    stop music fadeout 3.0
    music end

    $ achievement_manager.unlock("Welcome to CSBIII, Mother Fucker")

    scene black with fade
    jump csbiii_start
