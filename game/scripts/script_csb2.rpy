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
            jump punch
        "Chop":
            jump chop
        "Kick":
            jump kick
        "Special" (type = "bad"):
            jump special

# Punch
label punch:
    show cs angry at left
    show wesley at right
    cs "Take this!"
    n "CS punches Wesley and knocks him out."
    show cs angry at center with move
    play sound "audio/punch.ogg"
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show wesley at right with vpunch
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show wesley at right with vpunch
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "audio/punch.ogg"
    play sound "audio/punchalt.ogg"
    show wesley at right with vpunch
    play sound "audio/punch.ogg"
    show wesley at right with hpunch
    play sound "victorypunch.ogg" volume 0.5
    show wesley at t_punchup with move
    show cs angry at left with move
    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at right with moveinright
    show cs angry at left with move
    ed "Hello, 911? My coworker just got knocked out by a disgruntled customer and appears to be dying! Send help!"
    jump caught

# Chop
label chop:
    show cs angry at left
    show wesley at right
    cs "Hiya!"
    n "CS chops Wesley in the chest and he flies off the roof."
    show cs angry at center with move
    play sound "audio/chop.ogg"
    hide wesley with easeoutright
    show cs angry at left with move
    cs "I sawed this foundation repairman in half!"
    show ed_phone at right with moveinright
    show cs angry at left with move
    ed "Hello, 911? My coworker just got karate chopped by a disgruntled customer off the roof! Send help!"
    jump caught

# Kick
label kick:
    show cs angry at left
    show wesley at right
    $ renpy.movie_cutscene("movies/kick.webm")
    hide wesley with easeoutright
    show cs angry at left with move

    $ achievement_manager.unlock("Dead Meme")

    cs "That'll teach you not to mess with a nerd's computer!"
    show ed_phone at right with moveinright
    show cs angry at left with move
    ed "Hello, 911? My coworker just got kicked by a disgruntled customer off the roof! Send help!"
    jump caught

# Special
label special:
    show cs concentrate at left
    show wesley at right
    n "CS uses his YTP magic to make the foundation repairman fight eachother."
    hide wesley at right with moveoutright
    play sound "audio/punch.ogg"
    rich "Hey! Cut it out!"
    play sound "audio/punch.ogg"
    wesley "I'm not trying to fight! I don't know what is happening help!!"
    play sound "audio/punch.ogg"
    rich "Ed! Do something!"
    play sound "audio/punch.ogg"
    if e1:
        n "Wesley shoots Richard in the head with his gun."
        pause 3.0
        n "Welsey, then takes the gun, and--{w=0.5}{nw}"
        stop music
        music end
        scene black with dissolve
        pause 1.0
        n "Deleting persistent{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
        $ e2 = True
        n "Resetting script{w=0.5}.{w=0.5}.{w=0.5}.{nw=0.5}"
        show script
        pause 1.5
        jump csbi_start
    else:    
        show ed at right with moveinright
    ed "Hello, 911? My coworkers are-"
    n "CS sentence-mixes Ed's words to his own will."
    ed "Everything is fine here officer. No need to come here."
    ed "What wait just happened?"
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
    n "As CS was about to leave, the cops come rushing in."
    play sound "siren.ogg" loop
    show blue_light at left
    show red_light at right
    show copguy behind blue_light, red_light at right with moveinright
    copguy "Freeze! Put your hands in the air!"
    stop sound fadeout 1.0
    cs "What's going on? I didn't do anything!"
    show cs worried at left
    copguy "Come with us, we need you to ask some questions."
    show cs at left
    cs "Alright, sure thing officer."
    show cs flipped with determination
    hide cs with moveoutleft
    hide copguy with moveoutleft
    scene black with fade
    jump questioning

# Questioning
label questioning:
    scene question with fade
    play music "<loop 0>card_castle.mp3" volume 0.5
    music Card Castle - Toby Fox
    show cs disappointed at left with moveinleft
    show copguy at right with moveinright
    copguy "Alright CS, a lot of crazy things happened today."
    copguy "The CEO of HoH SiS called us today, and was immediately interrupted buy something or someone telling us that everything was under control."
    copguy "After reviewing the phone call, his voice sounds kinda messed up."
    cs "I uhh, I don't know what that is all about..."
    copguy "Oh really?"
    copguy "What about all the workers in the building? Most of them were lying cold on the floor."
    cs "Okay fine!"
    cs "I confess!"
    cs "I was using YTP magic on the employees to make them fight, and I--"
    copguy "You what? What the hell are you on about?"
    cs "I have this power, and I just figured out how to--"
    copguy "Alright, I've heard enough."
    copguy "Lemme call in someone to deal with this."
    copguy "Mr. Mohs, you can deal with this man."
    hide copguy with moveoutright
    show asylum_worker at right with moveinright
    asylum_worker "Sure thing, boss."
    asylum_worker "Come on, follow me this way at once."
    show cs flipped with determination
    hide cs with moveoutleft
    hide asylum_worker with moveoutleft
    stop music fadeout 3.0
    music end
    scene black with fade
    jump asylum

# Asylum
label asylum:
    scene asylum with fade
    play music "<loop 0>basement.mp3" volume 0.5
    music Basement - Toby Fox
    show cs worried flipped at left with moveinright
    show cs worried with determination
    show asylum_worker at right with moveinright
    asylum_worker "Here is your room. Enjoy living out the rest of your life here."
    show cs worried at center with moveinleft
    cs "Sir, you need to listen to me! I'm not crazy!"
    asylum_worker "That's what they all say. Get off of me."
    play sound "audio/punch.ogg"    
    hide cs with moveoutbottom
    asylum_worker "Sorry it had to be this way, bud."
    hide asylum_worker with moveoutright
    pause 3.0
    show cs disappointed at center with moveinbottom
    cs "Ow..."
    cs "This isn't fair!"
    csgod "Hey!"
    csgod "Quit the whining!"
    show csgod at right
    show cs disappointed at left
    with moveinright
    cs "What?"
    cs "Who are you?"
    csgod "I am CS God, and I was the one who used the YTP power."
    cs "WHAT? How? I am so confused."
    csgod "You channelled your power through me, that was how you were able to do those abilities back at HoH SiS HQ."
    csgod "It seems that you weren't good enough at lying to get yourself out of the situation though."
    cs "Well, I wanted to be honest!"
    csgod "Yeah well, look where honesty got you."
    csgod "No one would believe something as silly as YTP power."
    csgod "For your punishment, I'm gonna leave you here you a while."
    cs "No! Please!"
    csgod "You'll get out soon enough, but maybe you should think about making a {i}better choice{/i} next time."
    hide csgod with moveoutright
    stop music fadeout 3.0
    music end
    $ renpy.movie_cutscene("movies/bad_ending.webm")
    $ renpy.end_replay()
    return
    
# Caught
label caught:
    cs "Dammit! Ed's calling the police! I gotta go after him!"
    ed "911! Come quickly! He's chasing after me!"
    play sound "siren.ogg" loop
    show blue_light at left
    show red_light at right
    n "The police arrive and CS runs away."
    show cs flipped with determination
    hide cs with moveoutleft
    show ed_phone behind blue_light, red_light at left with move
    show copguy behind blue_light, red_light  at right with moveinright
    copguy "Get back here!"
    cs "You can't catch me, I'm the speedy Michael Rosen!"
    stop music fadeout 3.0
    music end
    n "As CS is not actually the speedy Michael Rosen, he gets caught by the police."
    stop sound fadeout 1.0
    scene black with fade
    jump jail

label jail:
    scene jail_inside with fade
    show cs prison at offscreenleft
    show copguy at offscreenright
    with determination
    show cs prison at left
    show copguy at right
    with move
    copguy "Alright, welcome to the slammer. How tough are ya?"
    cs "How tough am I?! How, tough, am, I?! I beat Cuphead!"
    copguy "So?"
    cs "In under 90 minutes!"
    copguy "Hmm... okay, you're a tough enough guy to handle this cellmate, then."

    hide copguy with moveoutright
    show arceus at right with moveinright

    play music "<loop 0>stal.mp3" volume 0.4
    music stal - C418
    cs "Oh, hi Arceus."
    arceus "Heya, CS. .w."
    # And it's about time.
    cs "So what are you in for?"
    arceus "Putting spyware on a politician's phone."
    cs "Yeah, no, that checks out."
    arceus "And from my recent debug of CSBounciness, I know that you're in for beating up workers at HoHSiS."
    cs "Your what?"
    arceus "Never mind. Why'd you do it, anyhow?"
    show cs prison_worried at left
    cs "I was 100 percent unsatisfied."
    arceus "As was I. As was I..."
    n "A brief moment of silence..."
    show cs prison at left
    arceus "Welp. I'm tired of this place. Wanna break out?"
    cs "Eh... sure, why not, I've played plenty of The Escapists, I should be able to figure it out."
    cs "We should break out at least one other person though."
    arceus "If you say so... Who were you thinking of breaking out?"
    cs "Let's just break out that guy next to us, I think his name was Anno..."
    arceus "Anno? Sure, I've seen what he's capable of, he may be of use to us."
    cs "Alright then, let's get going!"

    show arceus at offscreenright
    show cs prison at offscreenleft
    with ease
    jump breakout

label breakout:
    scene jail_cell
    show cs prison at left
    show arceus at right
    with dissolve

    arceus "So, what's the plan? I've been trying to break outta here for five years."
    cs "Well, for a start. I need to get a feel of the routine here."
    arceus "I really can't stand being here another minute. I'll give you the rundown. Hasn't changed then, won't change now." 
    n "Arceus describes the prison routine to CS."
    cs "I think I got all that."
    arceus "So, what's our plan, boss?"
    cs "I gotta grab a few plastic spoons from the mess hall, a cup of molten chocolate, a guard outfit, and a change of shorts."
    arceus "Why a change of shorts?"
    show cs prison_worried at left
    cs "You kidding me? I'm gonna shit myself 'cause this is scary as hell."
    arceus "Fair enough."
    scene black with fade

    stop music fadeout 3.0
    music end
    n "The current day ends, and the next one progresses. CS and Arceus gather the required essentials for their escape. Along the way, they inform Anno, who more than happily complies with the plan." 
    n "The next evening..."
    play music "<loop 0>moongazer.mp3" volume 0.5
    music Moongazer - Dr. Awesome
    cs "Key, check."

    show arceus flipped at left with moveinleft
    arceus "Uniforms, check."

    show anno prison at right with moveinright
    anno "Spoons, check."

    show cs prison at center with dissolve
    cs "Extra shorts..."
    cs "Check."
    cs "Alright men, let's get the heck out of here!"

    scene black with dissolve

    n "In the dark of the night, the three begin chipping away at their cell floor."
    n "Upon breaking through, they set up makeshift bed dummies in their beds with their prison outfits, and don their acquired guard outfits."

    scene tunnel with fade
    # If anyone asks, Arceus is part god and can dig really easily, I guess.
    n "They begin digging quickly, making distance away from their cells."
    show cs guard dark at left with easeinleft
    cs "Jeez... I didn't think that would actually work."

    show arceus dark at right with easeinright
    arceus "You what?" 
    
    show anno guard dark with easeinbottom
    anno "How are we supposed to cross the border with the new wall?"
    arceus "Not the Mexican border, the Canadian border. We're in Washington, it's way closer and they're too polite to send us back."
    cs "Works for me, free healthcare."
    arceus "Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."
    hide cs
    hide anno guard
    hide arceus
    with dissolve
    n "The three continue to dig for hours, until their hands begin to blister and their spoons break."
    arceus "Based on my instinct and my tiredness. This should be far enough."
    n "The now escaped fugitives dig up for their ascent to the surface."
    stop music fadeout 3.0
    music end

    hide cs with dissolve
    hide arceus with dissolve
    hide anno with dissolve
    jump bordercrossing

label bordercrossing:
    scene border with fade
    play music "<loop 0>onett.mp3" volume 0.6
    music Onett Theme - Keiichi Suzuki
    n "CS, Anno, and Arceus emerge and begin heading north towards the border crossing."
    n "A wild border guard appears."

    show border_guard at center with dissolve
    border_guard "I'm going to need proof of citizenship, eh."
    show border_guard at right with move
    show arceus flipped at left with moveinleft
    arceus "Colour is spelled with a u, eh."
    border_guard "Works for me, eh."

    scene canada with fade 
    n "Some time passes as the party continues forth into the land of Canada."
    cs "Arceus, can we stop somewhere? I'm getting hungry."
    anno "Yeah, we've been walking for miles now."
    arceus "Guys. We've only just left the border. You can still see it behind us."
    scene flag
    $ renpy.music.set_pause(True, "music")
    play music2 "star_spangled_banner.mp3"
    n "The crew look behind them and still see a faint American flag waving."
    scene canada
    stop music2
    $ renpy.music.set_pause(False, "music")
    cs "Prison food just isn't all that filling."
    arceus "I suppose we could find a Tim Horton's, it's as common in Canada as a McDonald's is in America."
    n "Anno and CS nod aggressively."
    n "Arceus sniffs the air."
    arceus "There's one just over here, come on."

    scene outside_tim_hortons
    show cs at left
    with fade
    cs "I'm starving after all that walking, I need a donut."
    show cs at offscreenright with move
    show arceus flipped at offscreenright with moveinleft
    show anno at offscreenright with moveinleft
    stop music fadeout 3.0
    music end

    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    with fade
    play music "<loop 0>buy_something.mp3" volume 0.6
    music Buy Something Will Ya! - Keiichi Suzuki
    show cs at left with moveinleft
    show arceus flipped at center with moveinleft
    show anno at right with moveinleft

    anno "Finally."
    hide anno
    hide cs
    with dissolve

    show arceus flipped at t_arc_at_tims with ease

    arceus "Hi."
    cashier "Can I help you?"
    arceus "Yeah, can I have a dozen glazed donuts please?"
    cashier "Oh hi, Arceus, I didn't know it was you."

    show anno
    anno "Wait, huh?"
    hide anno
    show arceus flipped at t_arc_at_tims
    cashier "Here you go."
    arceus "That's me!"
    arceus "How much is it?"
    cashier "It'll be $18.{nw}"
    arceus "Here you go! Keep the change."
    arceus "Hi doggy!"
    cashier "You're my favorite customer."
    arceus "Thanks a lot! Bye~"
    show arceus at t_arc_at_tims
    hide arceus with moveoutleft
    cashier "Buh-bye!"
    stop music fadeout 3.0
    music end


    show cs disappointed
    cs "..."
    cs "I think I'm {i}really{/i} sleep deprived."

    $ achievement_manager.unlock("Ohai, Mark")
    play music "<loop 0>buy_something.mp3" volume 0.6
    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    show cs
    show anno at left
    show arceus at right
    with fade

    n "CS, Arceus, and Anno enjoy some well-deserved donuts."
    arceus "Sorry to interrupt you two, but we may have a problem: Those donuts cost me the last of my money. We are going to need to find a way to make some cash."
    scene outside_ltt
    n "CS looks across the street to see Linus Media Group."

    scene inside_tim_hortons
    show cashier at t_cashier_at_tims
    show inside_tim_hortons_fg
    show cs
    cs "Linus Media Group, huh? I have a lot of video editing experience, maybe I can get a job there."
    stop music fadeout 3.0
    music end

    scene black with fade
    n "CS walks into the studio to ask for a job."

    scene inside_ltt
    show linus
    with fade
    play music "<loop 0>passport.mp3" volume 0.5
    music PASSPORT.MID - George Stone
    linus "Sure, you can have a job, just show us proof of citizenship and you're ready to go!"
    cs "Colour is spelled with a u, eh."
    linus "I need actual papers, the last time I hired someone who used that as proof of citizenship I got fined and had to sell one of my thousands of 4090s."
    cs "Ummmm, I'll be right back."

    scene outside_ltt
    show arceus at right
    with dissolve
    show cs at left with moveinleft

    cs "Arc, what am I gonna do? They need proof I'm legal to work."
    arceus "Hmmm..."
    n "A lightbulb goes off in Arceus' head."
    arceus "Leave it to me."
    hide arceus
    show arceus flipped at right
    hide arceus flipped with moveoutright

    scene alley
    show arceus flipped with moveinleft

    n "Arceus rummages around in the dumpsters behind LMG."
    arceus "Hnng...{w} hmmpmh... {w}aha!"
    n "Arceus finds an old laptop."
    arceus "Perfect."
    n "Within minutes, Arceus has hacked the Canadian governement records to display CS as having a valid work visa."
    arceus "Even their security is too nice..."
    n "Arceus rummages around the dumpster more and finds a magnet from an old CRT."
    n "He places it against the laptop, corrupting the hard drive instantly."
    arceus "Without a trace."
    n "He discards both items and rushes out of the alley."

    hide arceus flipped
    show arceus
    hide arceus with moveoutleft

    scene outside_ltt
    show cs at left
    show arceus at right with moveinright

    arceus "All taken care of."
    cs "What did you do?"
    arceus "Don't worry about it. Just have them look you up."

    scene black with fade
    scene inside_ltt
    show linus
    with fade

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
    show cs with moveinleft

    cs "I did it, I got the job!"
    anno "Woohoo!"
    arceus "Hell yeah!"

    anno "Let's celebrate!"
    n "CS, Anno, and Arceus cheers their donuts together."
    stop music fadeout 3.0
    music end

    $ achievement_manager.unlock("Welcome to CSBIII, Mother Fucker")

    scene black with fade
    jump csbiii_start
