label csbii_start:
    $ persistent.csb2_unlocked = True
    play music time_for_a_smackdown volume 0.2 if_changed
    music time_for_a_smackdown
    scene helipad
    show wesley at right
    with dissolve
    show cs angry at left with moveinleft
    cs "You'll pay for what you did!"
    n "Wesley sweats nervously."
    wesley "Do you want a refund?"
    cs "I'll refund your {nw}"
    extend "face to the {i}floor!" with vpunch

    menu:
        "Which attack will you use?"
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
    music time_for_a_smackdown
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
    show ed phone at offscreenright with determination
    show ed phone at right
    show cs angry at left
    with { "master": MoveTransition(0.5) }
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump csbii_caught

# Chop
label csbii_chop:
    play music time_for_a_smackdown volume 0.2 if_changed
    music time_for_a_smackdown
    scene helipad
    show cs angry at left
    show wesley at right
    cs "Hi-{i}yah!{/i}" # hiya is a greeting, not the sound you're looking for - tate
    n "CS chops Wesley in the chest and he flies off the roof!"
    show cs angry at mid_mid_right with MoveTransition(0.25)
    play sound sfx_chop
    hide wesley
    show wesleytop at right
    show wesleybottom at right
    show wesleytop at Move((0.7 , 0.15), (1.75, -0.3), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show wesleybottom at Move((0.7 , 0.15), (1.75, 0.5), 2, repeat=False, bounce=False, xanchor="left", yanchor="top")

    pause 0.5
    cs "I sawed this foundation repairman in half!"
    show ed phone at offscreenright with determination
    show cs angry at left
    show ed phone at right
    with MoveTransition(0.5)
    ed "Hello, 911? My coworker just got karate-chopped off the roof by a disgruntled customer! Send help!"
    jump csbii_caught

# Kick
label csbii_kick:
    play music time_for_a_smackdown volume 0.2 if_changed
    music time_for_a_smackdown
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
    $ achievement_manager.unlock("sparta")

    cs "That'll teach you not to mess with a nerd's computer!"
    show ed phone at offscreenright with determination
    show cs angry at left
    show ed phone at right
    with MoveTransition(0.5)
    ed "Hello, 911? My coworker just got kicked off the roof by a disgruntled customer! Send help!"
    hide screen dxcom
    jump csbii_caught

# Special
label csbii_special:
    play music time_for_a_smackdown volume 0.2 if_changed
    music time_for_a_smackdown
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
    wesley "I'm not {i}trying{/i} to fight you! I don't know what's happening!"
    wesley "{cshake}{i}HELP!{/i}" with hpunch
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
        show ed phone at offscreenright with determination
        show ed phone at right with MoveTransition(0.5)
    ed "Hello, 911? My coworkers are--{w=0.5}{nw}"
    play sound sfx_tape_rewind volume 0.5
    with hpunch
    n "CS sentence-mixes Ed's words!"
    ed "{ytpmagic}Everything is fine here, officer. No need to come here."
    pause 0.5
    ed "Wait, what just happened?!"
    n "CS quickly puts all the workers to sleep."
    show ed phone at manual_pos(1.0, 1.0, 1.0) with determination
    show ed phone at manual_pos(1.2, 1.7, 1.0):
        linear 0.5 rotate 60
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    show wesley at manual_pos(0.7, 0.4):
        linear 0.5 rotate -45
    with MoveTransition(0.5)
    play sound sfx_punch
    with vpunch
    pause 2.0
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
    pause 0.5
    show cs at left with moveinleft
    n "As CS makes to leave the building, the cops come rushing in."
    play sound sfx_siren loop
    show blue_light at left
    show red_light at right
    show copguy behind cs at right with easeinright
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
    play music card_castle volume 0.5 if_changed
    music card_castle
    pause 1.0
    copguy "Alright, CS."
    if fun_value(FUN_VALUE_MUSIC):
        copguy "This is the Card Castle."
    else:
        copguy "A lot of crazy things have happened today."
    copguy "The CEO of HoH SiS called us."
    copguy "He was immediately interrupted by something, or some{i}one,{/i} telling us that everything was under control."
    copguy "After reviewing the audio, his voice sounds kinda messed up."
    cs "I, uh, I don't know what all {i}that{/i} is about..."
    copguy "Oh, really?"
    copguy "What about all of the workers in the building? Most of them were out cold on the floor."
    show cs worried dark
    cs "Okay, fine!"
    cs "I confess!"
    cs "I was using YTP Magic on the employees to make them fight each other, and I--{w=1.0}{nw}"
    copguy "You {i}what?!{/i} {nw}" with vpunch
    extend "What the hell are you on about?"
    cs "I have this power, and I just figured out how to--{w=0.5}{nw}"
    copguy "Alright, I've heard enough."
    copguy "Lemme call in someone more qualified to deal with this."
    show copguy dark flipped
    copguy "Mr. Mohs, this one's all yours."
    hide copguy with moveoutright
    pause 0.5
    show asylum_worker at right with { "master": moveinright }
    show cs scared dark
    asylum_worker "Sure thing, boss."
    pause 1.0
    asylum_worker "Alright, buddy. Come follow me."
    hide asylum_worker with moveoutright
    hide cs with moveoutright
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 1.0
    jump csbii_asylum

# Asylum
label csbii_asylum:
    scene asylum with dissolve
    play music basement volume 0.5 if_changed
    music basement
    pause 2.0
    show cs worried insane dark flipped at left with moveinright
    show cs worried insane dark with determination
    show asylum_worker at right with moveinright
    pause 1.0
    if fun_value(FUN_VALUE_MUSIC):
        asylum_worker "Here's your basement. Enjoy living out the rest of your life here."
    else:
        asylum_worker "Here's your room. Enjoy living out the rest of your life here."
    show cs scared insane dark at center with moveinleft
    cs "Sir, you need to listen to me! I'm not crazy!"
    asylum_worker "That's what they all say."
    asylum_worker "Get off of me."
    show asylum_worker at mid_mid_right with MoveTransition(0.1)
    play sound sfx_punch
    show cs scared insane dark at manual_pos(1.0, 2.0, 1.0) with MoveTransition(0.25)
    with vpunch
    show asylum_worker at right with MoveTransition(0.1)
    pause 1.0
    asylum_worker "Sorry it had to be this way, bud."
    hide asylum_worker with moveoutright
    pause 0.5
    play sound sfx_house_door_close
    pause 3.0
    show cs disappointed insane dark at manual_pos(0.8, 1.115, 1.0) with MoveTransition(1.0):
        rotate 45
        linear 1.0 rotate 0
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
    show cs worried insane dark at manual_pos(0.5, 1.115, 1.0)
    with MoveTransition(2.0)
    pause 1.0
    cs "What?"
    cs "Who are you?"
    csgod "I am CSGod."
    csgod "It was I who used the YTP power."
    show cs scared insane dark
    cs "{i}What?!{/i} How?" with vpunch
    show cs disappointed insane dark
    cs "I am so confused..."

    # tate was here
    if fun_value(FUN_VALUE_UNOBTRUSIVE):
        csgod "You channeled my power. You had it all, right there at your fingertits."
    else:
        csgod "You channeled my power through your fingertips."
    csgod "That was how you were able to use those abilities back at HoH SiS HQ."
    csgod "However, it seems that you weren't good enough at lying to get yourself out of this situation."
    show cs disappointed insane dark
    cs "Well, I wanted to be honest!"
    csgod "Yeah, well, look where honesty got you."
    csgod "No mortal would ever believe in something as silly as YTP Magic."
    csgod "For your punishment, I shall leave you here you a while."
    show cs scared insane dark
    cs "No! Please!"
    csgod "You will get out soon enough, but maybe you should think about making a {i}better choice{/i} next time."
    hide csgod with dissolve
    stop music fadeout 3.0
    music end
    window hide
    $ ending_manager.mark("asylum")
    bad_end "Silly CS!\nYTP Magic doesn't exist!" "csbii_start"
    return

# Caught
label csbii_caught:
    play music time_for_a_smackdown volume 0.2 if_changed
    music time_for_a_smackdown
    scene helipad
    show ed phone at right
    show cs angry at left
    cs "Damn it! Ed's calling the police! I've gotta go after him!"
    show cs angry at center with { "master": move }
    ed "911! Come quickly! {nw}"
    show ed phone flipped at offscreenright with { "master": MoveTransition(0.25) }
    extend "He's chasing after me!"
    play sound sfx_siren loop
    show blue_light at left
    show red_light at right
    n "The police arrive and CS runs away."
    show cs angry flipped with determination
    show cs angry flipped at offscreenleft with MoveTransition(0.25)
    show ed phone behind blue_light, red_light at left with move
    show copguy behind blue_light, red_light, ed at right with moveinright
    copguy "Get back here!"
    show copguy at offscreenleft with MoveTransition(0.25)
    cs "You can't catch me! I'm the speedy Michael Rosen!"
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
    pause 1.0
    show cs prison flipped at offscreenright
    show copguy at offscreenright
    with determination
    show cs prison flipped at left
    show copguy at right
    with move
    show cs prison
    pause 1.0
    copguy "Alright, welcome to the slammer. How tough are ya?"
    cs "How tough am I? {cshake}How tough am I?!{/bt}"
    cs "I beat {i}Cuphead!{/i}"
    copguy "So?"
    show cs happy prison
    cs "{i}In under 90 minutes!"
    copguy "Hmm... okay. You're a tough enough guy to handle this cellmate, then."
    show cs prison
    show copguy flipped
    hide copguy with moveoutright
    pause 1.0
    show arceus prison at right with moveinright
    pause 1.0
    play sound sfx_jailcell_shut
    play music stal volume 0.4 if_changed
    music stal
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
    show cs disappointed prison
    cs "Your what?"
    arceus "... Never mind."
    arceus "Why'd you do it, anyhow?"
    cs "I was 100%% unsatisfied."
    arceus "As was I. As was I..."
    pause 1.0
    "..."
    pause 1.0
    show cs prison at left
    arceus "Welp. I'm tired of this place. Wanna break out?"
    cs "Eh... sure, why not. I've played plenty of {i}The Escapists.{/i} I should be able to figure it out."
    cs "We should break out at least one other person though."
    arceus "If you say so..."
    arceus "Who were you thinking of breaking out?"
    cs "Let's just break out that guy next to us. I think his name was Anno{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?"
    arceus "Anno? Sure. I've seen what he's capable of, so he may be of use to us."
    cs "Alright, then! Let's get going!"

    show arceus prison at offscreenright
    show cs prison at offscreenleft
    with ease
    pause 1.0
    jump csbii_breakout

label csbii_breakout:
    play music stal volume 0.4 if_changed
    music stal
    scene jail_cell
    show cs prison at left
    show arceus prison at right
    with dissolve

    dxcom prisonroute

    pause 1.0
    arceus "So, what's the plan? I've been trying to break outta here for five years."
    cs "Well, for starters, I need to get a feel for the routine here."
    arceus "I really can't stand being here another minute. I'll give you the rundown. Hasn't changed then, won't change now."

    scene black with dissolve
    pause 0.5
    n "Arceus describes the prison routine to CS."
    pause 0.5

    scene jail_cell
    show cs prison at left
    show arceus prison at right
    with dissolve
    pause 1.0

    cs "... Cool, I think I got all that."
    arceus "So, what's our plan, boss?"
    cs "I've gotta grab a few plastic spoons from the mess hall, a cup of molten chocolate, a guard uniform, and a change of shorts."
    arceus "... Why a change of shorts?"
    show cs disappointed prison at left
    cs "You kidding me? I'm gonna shit myself, 'cause this is scary as hell."
    arceus "Fair enough."
    pause 0.5
    hide screen dxcom
    stop music fadeout 3.0
    music end
    scene black with dissolve
    pause 0.5

    n "The day comes to an end and the next one follows."
    n "CS and Arceus gather the required essentials for their escape. Along the way, they inform Anno, who more than happily complies with the plan."
    pause 1.0
    centered "The next evening..."
    pause 0.5
    play music moongazer volume 0.5 if_changed
    music moongazer
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

    show spoon as first:
        zoom 0.5
        xpos 0.25
        ypos 1.0
        linear 0.5 ypos 0.55
    show spoon as second:
        zoom 0.5
        xpos 0.6
        ypos 1.0
        linear 0.5 ypos 0.5
    show spoon as third:
        zoom 0.5
        xpos 0.9
        ypos 1.0
        linear 0.5 ypos 0.6
    with dissolve

    $ collect("spoon")

    pause 0.5
    scene black with dissolve
    pause 0.5

    n "In the dark of night, the three begin chipping away at their cell floor."
    n "Upon breaking through, they set up makeshift dummies in their beds with their prison jumpsuits, then don their acquired guard uniforms."

    scene tunnel with dissolve
    # If anyone asks, Arceus is part god and can dig really easily, I guess.

    n "They begin digging quickly, putting distance between themselves and their cells."
    show cs disappointed guard dark at left with easeinleft
    dxcom tint
    cs "Jeez... I didn't think that would actually work."

    show arceus guard dark at right with easeinright
    arceus "You {i}what?"

    show anno guard dark with easeinbottom
    anno "How are we supposed to cross the border with the new wall?"
    arceus "Not the Mexican border, the Canadian border. We're in Washington, it's way closer, and they're too polite to send us back."
    show cs guard dark
    cs "Works for me. Free healthcare!"
    arceus "Well, you have to live there for a few years before you get access to that, but you {i}should{/i} last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."
    hide cs
    hide anno guard
    hide arceus
    with dissolve
    pause 1.0
    n "The three continue to dig for hours, until their hands begin to blister and their spoons break."
    arceus "Based on my instinct, and on my tiredness, this should be far enough."
    n "The now-escaped fugitives dig upwards for their ascent towards the surface."
    pause 0.5

    hide screen dxcom
    scene black
    with dissolve
    stop music fadeout 3.0
    music end
    pause 1.0

    jump csbii_bordercrossing

label csbii_bordercrossing:
    scene border with dissolve
    play music onett volume 0.6 if_changed
    music onett
    if fun_value(FUN_VALUE_MUSIC):
        n "CS, Anno, and Arceus emerge from the earth and begin heading north towards Onett. Theme."
    else:
        n "CS, Anno, and Arceus emerge from the earth and begin heading north towards the border crossing."
    pause 0.5

    # INTENTIONAL DISSOLVE: Pokemon reference
    show border_guard at center with { "master": dissolve }
    n "A wild border guard appears."

    if fun_value(FUN_VALUE_COMMON):
        border_guard "Eh, Schnitzelburg!"
    border_guard "I'm going to need proof of citizenship, eh."
    show border_guard at right
    show arceus flipped at left
    with moveinleft
    arceus "Colour is spelled with a u, eh."
    border_guard "Works for me, eh."
    pause 0.5

    scene canada with dissolve
    pause 1.0
    n "Some time passes as the party ventures forth into the land of Canada."
    cs "Arceus, can we stop somewhere? I'm getting hungry."
    anno "Yeah, we've been walking for miles now."
    arceus "Guys. We've only {i}just{/i} left the border. You can still see it behind us."
    scene flag
    $ renpy.music.set_pause(True, "music")
    play music2 star_spangled_banner if_changed
    music star_spangled_banner
    if fun_value(FUN_VALUE_MUSIC):
        n "The crew looks behind them and hears The Star Spangled Banner playing."
    else:
        n "The crew looks behind them and still sees a faint American flag waving."
    scene canada
    stop music2
    $ renpy.music.set_pause(False, "music")
    music onett
    "..."
    cs "Prison food just isn't all that filling."
    arceus "I suppose we could find a Tim Horton's. It's as common in Canada as McDonald's is in America."
    n "Anno and CS nod enthusiastically."
    n "Arceus sniffs the air."
    arceus "There's one just over here, come on."

    scene black with dissolve
    pause 1.0
    scene outside_tim_hortons
    show cs disappointed at left
    with dissolve
    pause 1.0
    cs "I'm starving after all that walking. I can't wait to eat a donut."
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
    play music buy_something volume 0.6 if_changed
    music buy_something
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
    cashier "It'll be $18. {nw}"
    show arceus full happy flipped
    arceus "Here you go! Keep the change."
    arceus "Hi, doggy!"
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
    pause 0.5
    $ achievement_manager.unlock("ohai_mark")
    scene black with dissolve
    pause 1.0

    play music buy_something volume 0.6 if_changed
    music buy_something
    scene inside_tim_hortons_2
    show cs
    show anno at left
    show arceus at right
    show tims_dozen at manual_pos(0.4, 0.6)
    $ collect("tims_dozen")
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
        play music passport_ytp volume 0.5 if_changed
        music passport_ytp
    else:
        play music passport volume 0.5 if_changed
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
        music passport_ytp
    else:
        hide passportdigi
        music passport
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
    arceus "Hmm..."
    n "A lightbulb goes off in Arceus' head."
    arceus "Leave it to me."
    show arceus flipped at offscreenright with moveoutright

    scene alley
    with dissolve
    if fun_value(FUN_VALUE_LEGENDARY):
        show passportdigi with dissolve
    else:
        hide passportdigi
    show arceus flipped with moveinleft

    n "Arceus rummages around in the dumpsters behind LMG."
    show arceus flipped:
        xanchor 0.5
        parallel:
            linear 0.5 xpos 0.7
        parallel:
            linear 0.5 ypos 0.8
        parallel:
            linear 0.5 zoom 0.7
    pause 1.0

    play sound sfx_items_rustling volume 3.0
    arceus "Hnng...{w} hmmpmh... {w}{i}aha!"
    pause 0.5
    stop sound
    arceus "So, I just need..."

    show arceus :
        xanchor 0.5
        parallel:
            linear 0.5 xpos 0.3
        parallel:
            linear 0.5 ypos 0.9
        parallel:
            linear 0.5 zoom 1.1

    pause 1.0
    play sound sfx_items_rustling volume 5.0
    arceus "Come on..."
    stop sound
    show craptop at manual_pos(0.1, 0.5) with dissolve
    n "Arceus finds an old laptop."
    arceus "Perfect."

    show arceus flipped at center
    show craptop at manual_pos(0.55, 0.5)
    with move
    pause 0.5

    play sound sfx_keyboard
    n "Within minutes, Arceus has hacked the Canadian government records to display CS as having a valid work visa."
    arceus "Even their security is too nice..."
    # TODO: please replace this with an accurate image. idk what it actually looks like -tate
    show crt_magnet at manual_pos(0.35, 0.6) with dissolve
    $ collect("crt_magnet")
    n "Arceus produces the old CRT magnet he found a moment ago."
    show crt_magnet at manual_pos(0.55, 0.5) with MoveTransition(0.5)
    n "He places it against the laptop, corrupting the hard drive instantly."
    play sound sfx_bluescreen
    pause 1.0
    arceus "Without a trace."
    show craptop at manual_pos(1.2, 0.6, 0.5):
        linear 0.5 rotate 180
    show crt_magnet at manual_pos(1.1, 0.8, 0.5):
        linear 0.5 rotate 180
    with MoveTransition(0.25)
    play sound sfx_cat_crash
    with hpunch
    pause 1.5
    n "He discards both items and rushes out of the alley."

    show arceus
    show arceus at offscreenleft with MoveTransition(0.25)

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
    cs "Oh, {i}yes!"
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

    dxcom donuts

    show donut_1 at manual_pos(0.2, 0.7)
    show donut_2 at manual_pos(0.5, 0.7)
    show donut_3 at manual_pos(0.7, 0.7)
    with dissolve
    $ collect("donut_1")
    $ collect("donut_2")
    $ collect("donut_3")

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

    $ achievement_manager.unlock("csbii")

    scene black with dissolve
    hide screen dxcom
    pause 1.0
    jump csbiii_start
