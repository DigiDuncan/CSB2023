
define audio.albuquerque = "<from 104>albuquerque.ogg"
define audio.albuquerque2 = "<from 153.5>albuquerque.ogg"
define audio.albuquerque3 = "<from 280.75>albuquerque.ogg"
define audio.albuquerque4 = "<from 390>albuquerque.ogg"
define audio.albuquerque5 = "<from 480.5>albuquerque.ogg"
define audio.albuquerque6 = "<from 578>albuquerque.ogg"

#
# DON'T CHANGE OR EDIT THE SCRIPT AT ALL, IT MAY RUIN THE TIMING
#

label dx_albuquerque:
    scene airplane_seats
    show cs at mid_left
    pause 0.5
    play music albuquerque if_changed
    music albuquerque
    cs_nobeep "{cps=40}You know, I'd never been on a real airplane before...{w=0.5}{nw}"
    show cs happy
    cs_nobeep "{cps=40}...And I gotta tell ya, it was really great!{w=0.8}{nw}"
    show cs disappointed 
    show trailtrash flipped at mid_offscreen_left behind cs
    show trailtrash_2 at center behind cs
    with moveinleft
    cs_nobeep "{cps=40}Except that I had to sit between {cps=30}two large Albanian women with {cps=20}excruciatingly severe body odor...{w=1.0}{nw}"
    play sound sfx_puke volume 0.3
    cs_nobeep "{cps=40}...And the little kid in back of me kept throwin' up the whole time!{w=1.0}{nw}" with vpunch
    show cs worried
    cs_nobeep "{cps=40}The flight attendants ran out of Dr. Pepper and salted peanuts...{w=1}{nw}"
    cs_nobeep "{cps=40}...And the in-flight movie was Bio-Dome with Pauly Shore...{w=1}{nw}"
    cs_nobeep "{cps=40}...And,{w=0} oh yeah,{w=0} three of the airplane engines burned out...{w=0.75}{nw}" with vpunch
    show airplane_seats behind cs at rotate_10 with hpunch
    show cs scared
    show trailtrash flipped at mid_offscreen_left behind cs
    show trailtrash_2 at center behind cs
    show red_light at manual_pos(500,-500)
    play sound sfx_less_annoying_alarm_sound loop
    cs_nobeep "{cps=40}...And we went into a tailspin and crashed into a hillside...{w=0.5}{nw}" with vpunch
    scene kuwait_explosion
    play sound sfx_explosion
    cs_nobeep "{cps=40}...And the plane exploded in a giant fireball and everybody died!{w=2.0}{nw}"
    scene airplane_seats
    show cs
    with dissolve
    cs_nobeep "{cps=40}Except for me.{w=1.00}{nw}"
    cs_nobeep "{cps=40}You know why?{w=0.75}{nw}"
    show cs happy
    cs_nobeep "{cps=40}'Cause I had my tray table up...{w=1.5}{nw}"
    show cs
    cs_nobeep "{cps=40}...And my seat back in the {cps=40}full up{cps=40}right position!{w=1.7}{nw}"
    show cs happy
    cs_nobeep "{cps=40}Had my tray table up...{w=1.5}{nw}"
    show cs
    cs_nobeep "{cps=40}...And my seat back in the {cps=40}full up{cps=40}right position!{w=1.7}{nw}"
    show cs happy
    cs_nobeep "{cps=40}Had my tray table up...{w=1.5}{nw}"
    show cs
    cs_nobeep "{cps=40}...And my seat back in the {cps=40}full up{cps=40}right position!{w=1.7}{nw}"
    show cs scared
    cs_nobeep "{cps=20}Ah ha ha ha!{w=0.5}{nw}"
    show cs happy
    cs_nobeep "{cps=20}Ah ha ha!{w=0.5}{nw}"
    show cs
    cs_nobeep "{cps=10}Ah...{w=1.0}{nw}"
    #scene black
    #stop music
    #pakoo "Start string 2!"
    #play music albuquerque2 if_changed
    scene kuwait_island_outside
    with dissolve
    show cs disappointed at Move((-0.2 , 0.3), (1.2, 0.3), 20, repeat=False, bounce=False, xanchor="left", yanchor="top")
    cs_nobeep "{cps=40}So I crawled from the twisted, burnin' wreckage...{w=1}{nw}"
    cs_nobeep "{cps=25}I crawled on my hands and knees{cps=20} for{cps=10} three full days...{w=0.75}{nw}"
    cs_nobeep "{cps=40}{cps=15}Draggin' along my {cps=25}big leather suitcase{cps=30} and my garment bag...{w=0.75}{nw}"
    cs_nobeep "{cps=25}...And my tenor saxophone and my twelve-pound bowling ball...{nw}"
    cs_nobeep "{cps=30}...And my lucky, lucky{w=0.25} autographed {cps=20}glow-in-the-dark{cps=40} snorkel!{w=1.25}{nw}"
    scene hotel_lobby
    show cs happy
    with dissolve
    cs_nobeep "{cps=40}But finally I arrived at the world famous,{w=1.0} {cps=20}Albuquerque {cps=40}Holiday Inn!{w=1.0}{nw}"
    cs_nobeep "{cps=40}Where the towels are {cps=25}oh so{cps=40} fluffy!{w=1}{nw}"
    cs_nobeep "{cps=40}...And you can {cps=25}eat your soup{cps=40} right out of the ashtrays if you wanna!{w=1}{nw}"
    cs_nobeep "{cps=40}It's okay, they're clean!{w=0.5}{nw}"
    scene hotel_room
    show cs
    with dissolve
    cs_nobeep "{cps=40}Well, I checked into my room, and I turned down the A/C...{w=0.5}{nw}"
    cs_nobeep "{cps=40}...And I turned on the SpectraVision...{w=0.5}{nw}"
    cs_nobeep "{cps=40}...And I'm just about to eat that little chocolate mint on my pillow...{w=0.5}{nw}"
    cs_nobeep "{cps=40}That I love so very, very much when suddenly, there's a knock on the door.{w=1.0}{nw}"
    cs_nobeep "{cps=40}Well now, who could that be?{w=0.75}{nw}"
    show hotel_door_back behind cs
    show cs at left
    with dissolve
    cs_nobeep "{cps=40}I say, Who is it?{w=0.5}{nw}"
    cs_nobeep "{cps=40}No answer.{w=1}{nw}"
    show cs happy
    cs_nobeep "{cps=40}Who is it?{w=1}{nw}"
    cs_nobeep "{cps=40}There's no answer.{w=1}{nw}"
    show cs angry
    cs_nobeep "{cps=40}Who is it?!{w=1}{nw}"
    cs_nobeep "{cps=40}They're not sayin' anything!{w=0.7}{nw}"
    show cs angry at mid_right with move
    cs_nobeep "{cps=50}So, finally I go over and I open the door {cps=10}and {cps=20}just as I suspected!{w=0.5}{nw}"
    show mr_krupp at right with moveinright
    show cs scared at mid_left
    with move
    cs_nobeep "{cps=50}It's some big fat hermaphrodite with a Flock of Seagulls haircut and only one nostril.{w=2.25}{nw}"
    cs_nobeep "{cps=40}Oh man, I hate it when I'm right!{w=1.0}{nw}"
    show mr_krupp at mid_offscreen_left with move
    show mr_krupp at right with move
    cs_nobeep "{cps=40}So anyway, he bursts into my room and he grabs my lucky snorkel...{w=0.5}{nw}"
    cs_nobeep "{cps=40}...And I'm like, Hey, you can't have that!{w=0.75}{nw}"
    cs_nobeep "{cps=40}That snorkel's been just like a snorkel to me!{w=1}{nw}"
    cs_nobeep "{cps=30}And he's like,{w=0.5}{nw}"
    hermaphrodite "{cps=20}Tough!{w=0.25}{nw}"
    cs_nobeep "{cps=30}...And I'm like Give it!{w=0.25}{nw}"
    cs_nobeep "{cps=40}...And he's like,{w=0.5}{nw}"
    hermaphrodite "{cps=30}Make me.{w=0.5}{nw}"
    cs_nobeep "{cps=20}...And I'm like,{cps=40} Kay!{w=0.3}{nw}"
    show cs pissed at center with move
    play sound sfx_punch
    cs_nobeep "{cps=30}So I grabbed his leg and he grabbed my esophagus...{w=0.25}{nw}" with vpunch
    show mr_krupp at center with move
    show cs pissed at left with ease
    play sound sfx_punch
    cs_nobeep "{cps=30}...And I bit off his ear and he chewed off my eyebrows...{w=0.25}{nw}" with hpunch
    show cs pissed at center with ease
    hide mr_krupp with easeoutright
    play sound sfx_punch
    cs_nobeep "{cps=40}...And I took out his appendix and he gave me a colonic irrigation!{w=0.25}{nw}" with vpunch
    cs_nobeep "{cps=40}Yes, indeed, you better believe it!{w=0.5}{nw}"
    show cs at left
    cs_nobeep "{cps=40}And somehow in the middle of it all, the phone got knocked off the hook.{w=1.25}{nw}" with hpunch
    cs_nobeep "{cps=40}And twenty seconds later, I heard a familiar voice.{w=1}{nw}"
    cs_nobeep "{cps=40}And you know what it said?{w=1}{nw}"
    cs_nobeep "{cps=40}I'll tell you what it said!{w=1}{nw}"
    cs_nobeep "{cps=40}It said:{w=0.5}{nw}"
    show hotel_door_back at left behind cs with move
    show hoh_hq at mid_offscreen_right behind ed
    show ed phone at right
    with moveinright 
    daphone "{cps=40}If you'd like to make a call,{w=1} please {cps=25}hang up {cps=40}and try again;{w=1.25}{nw}"
    daphone "{cps=40}If you need help, hang up {cps=25}and then dial your {cps=10}oper{cps=20}ator!{w=3}{nw}"
    daphone "{cps=40}If you'd like to make a call,{w=1} please {cps=25}hang up {cps=40}and try again;{w=1.25}{nw}"
    daphone "{cps=40}If you need help, hang up {cps=25}and then dial your {cps=10}oper{cps=20}ator!{w=3}{nw}"
    cs_nobeep "{cps=40}In Al{w=3.5}buquerque!{w=1.5}{nw}"
    cs_nobeep "{cps=40}Al{w=3.5}buquerque!{w=1.5}{nw}"
    #scene black
    #stop music
    #pakoo "Start string 3!"
    #play music albuquerque3 if_changed
    scene hotel_lobby
    show cs disappointed
    cs_nobeep "{cps=30}Well, to cut a long story short,{cps=40} he got away with my snorkel...{w=1}{nw}"
    show cs angry
    cs_nobeep "{cps=40}...But I made a solemn vow {cps=30}right then and there that {cps=20}I would not rest,{w=1}{nw}"
    cs_nobeep "{cps=20}I would not sleep {cps=30}for an instant {cps=40}until the one-nostrilled man was brought to justice!{w=1}{nw}"
    show cs
    cs_nobeep "{cps=40}...But first, I decided to buy some donuts.{w=1}{nw}"
    scene cs_car_inside
    show cs at left
    cs_nobeep "{cps=40}So I got in my car and I drove over to the donut shop...{w=0.5}{nw}"
    scene inside_tim_hortons
    show inside_tim_hortons_fg
    show cashier at t_cashier_at_tims behind inside_tim_hortons_fg
    show cs at center with moveinleft
    show cs at t_arc_at_tims
    cs_nobeep "{cps=55}...And I walked on up to the guy behind the counter...{w=0.5}{nw}"
    cs_nobeep "{cps=40}...And he says,{w=0.75}{nw}"
    cashier_nobeep "{cps=10}Yeah, {cps=40}what do ya want?{w=3}{nw}"
    cs_nobeep "{cps=40}I said, {cps=30}You got any glazed donuts?{w=1}{nw}"
    cs_nobeep "{cps=40}He said,{w=0.25}{nw}"
    cashier_nobeep "{cps=40}No, we're outta glazed donuts!{w=1}{nw}"
    cs_nobeep "{cps=40}I said, {cps=30}You got any jelly donuts?{w=1}{nw}"
    cs_nobeep "{cps=40}He said,{w=0.25}{nw}"
    cashier_nobeep "{cps=40}No, we're outta jelly donuts!{w=1}{nw}"
    cs_nobeep "{cps=40}I said, {cps=30}You got any Bavarian cream-filled donuts?{w=1}{nw}"
    cs_nobeep "{cps=40}He said,{w=0.25}{nw}"
    cashier_nobeep "{cps=40}No, we're outta Bavarian cream-filled donuts!{w=1}{nw}"
    cs_nobeep "{cps=40}I said, {cps=30}You got any cinnamon rolls?{w=1}{nw}"
    cs_nobeep "{cps=40}He said,{w=0.25}{nw}"
    cashier_nobeep "{cps=40}No, we're outta cinnamon rolls!{w=1}{nw}"
    cs_nobeep "{cps=40}I said, {cps=30}You got any apple fritters?{w=1}{nw}"
    cs_nobeep "{cps=40}He said,{w=0.25}{nw}"
    cashier_nobeep "{cps=40}No, we're outta apple fritters!{w=1}{nw}"
    cs_nobeep "{cps=40}I said, {cps=30}You got any bear claws?{w=1}{nw}"
    cs_nobeep "{cps=40}He said,{w=0.25}{nw}"
    cashier_nobeep "{cps=40}Wait a minute, I'll go check.{w=1}{nw}"
    show cashier at offscreenright with move
    pause 8.0
    show cashier at t_cashier_at_tims behind inside_tim_hortons_fg with move
    cashier_nobeep "{cps=40}No, we're outta bear claws!{w=1}{nw}"
    cs_nobeep "{cps=40}I said, Well, in that case -{w=1.5} in that case, what do you have?{w=1}{nw}"
    cs_nobeep "{cps=40}He says,{w=0.5}{nw}"
    cashier_nobeep  "{cps=40}All I got right now is this box of one dozen starving, crazed weasels.{w=2.5}{nw}"
    cs_nobeep "{cps=40}I said, Okay, I'll take that.{nw}"
    show pot at t_cashier_at_tims with dissolve
    show pot at t_arc_at_tims with move
    cs_nobeep "{cps=40}...So he hands me the box and I open up the lid and the weasels jump out...{w=1.5}{nw}" with hpunch
    hide pot
    hide cs
    show cs scared at center
    show nova_head as first at mid_mid_left
    show nova_head as second at mid_mid_right
    with dissolve
    cs_nobeep "{cps=40}...And they immediately latch onto my face and start bitin' me all over...{w=1.0}{nw}" with hpunch
    "Weasels" "{cps=40} Ahh gnahh nahh nahh! Ah gahhh nahh!{w=0.75}{nw}" with hpunch
    cs_nobeep "{cps=40}Oh man, they were just going nuts!{w=0.75}{nw}"
    cs_nobeep "{cps=40}They were tearin' me apart!{w=1}{nw}"
    cs_nobeep "{cps=40}You know, I think it was just about that time that a little ditty started goin' through my head.{w=2}{nw}"
    cs_nobeep "{cps=40}I believe it went a little something like this...{w=2}{nw}"
    cs_nobeep "{cps=40}Doh!{w=0.8}{nw}" with hpunch
    cs_nobeep "{cps=40}Get 'em off me!{w=0.25}{nw}" with hpunch
    cs_nobeep "{cps=40}Get 'em off me!{w=0.25}{nw}" with hpunch
    cs_nobeep "{cps=40}No, get 'em off, get 'em off!{w=1}{nw}" with hpunch
    cs_nobeep "{cps=40}Oh, oh God, oh God!{w=0.75}{nw}" with hpunch
    cs_nobeep "{cps=40}Oh, get 'em off me!{w=0.6}{nw}" with hpunch
    cs_nobeep "{cps=40}Oh, oh God!{w=0.5}{nw}" with hpunch
    cs_nobeep "{cps=40}Ohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!{w=0.25}{nw}"
    #scene black
    #stop music
    #pakoo "Start string 4!"
    #play music albuquerque4 if_changed
    scene canada_block with dissolve
    show cs scared flipped at Move((1.2 , 0.2), (-0.2, 0.2), 5, repeat=True, bounce=True, xanchor="left", yanchor="top")
    show nova_head as first at Move((1.2 , 0.2), (-0.2, 0.2), 5, repeat=True, bounce=True, xanchor="left", yanchor="top")
    cs_nobeep "{cps=40}I ran out into the street with these flesh-eating weasels all over my face...{w=0.5}{nw}"
    cs_nobeep "{cps=40}Wavin' my arms all around and just runnin',{w=0.05} runnin',{w=0.05} runnin',{w=0.05}{w=0.75}{nw}"
    cs_nobeep "{cps=40}Like a constipated wiener dog!{w=1.25}{nw}"
    cs_nobeep "{cps=40}...And as luck would have it, that's exactly when I ran into the girl of my dreams.{w=0.5}{nw}"
    show cs flipped at mid_right
    show nova_head as first at manual_pos(0.65 , 0.2)
    pause 1.25
    show pomni flipped at left with moveinleft
    cs_nobeep "{cps=40}Her name was Zelda.{w=1.5}{nw}"
    cs_nobeep "{cps=40}She was a calligraphy enthusiast with a slight overbite and hair the color of strained peaches.{w=2.5}{nw}"
    cs_nobeep "{cps=40}I'll never forget the very first thing she said to me.{w=0.75}{nw}"
    cs_nobeep "{cps=40}She said,{w=0.1}{nw}"
    zelda "{cps=40}Hey, you've got weasels on your face.{w=1.25}{nw}"
    hide nova_head as first with moveouttop
    cs_nobeep "{cps=40}That's when I knew it was true love!{w=1}{nw}"
    cs_nobeep "{cps=40}We were inseparable after that...{w=1}{nw}"
    scene dining_room
    show pomni flipped at mid_left
    show cs happy flipped at right
    cs_nobeep "{cps=40}Aw, we ate together, we bathed together...{w=1}{nw}"
    scene toilet_zone
    show pomni flipped at mid_left
    show cs happy flipped at right
    cs_nobeep "{cps=40}We even shared the same piece of mint-flavored dental floss!{w=1.5}{nw}"
    show cs flipped
    cs_nobeep "{cps=40}The world was our burrito.{w=1.0}{nw}"
    scene dining_room
    show pomni flipped at mid_left
    show cs happy flipped at right
    cs_nobeep "{cps=40}So we got married and we bought us a house...{w=1}{nw}"
    scene kitty_room
    show pomni flipped at mid_left
    show cs happy flipped at mid_right
    show harold at Move((1.2, 0.35), (0.8, 0.35), 5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show george at Move((-0.2, 0.5), (0.0, 0.5), 5, repeat=False, bounce=False, xanchor="left", yanchor="top")
    cs_nobeep "{cps=40}...And had two beautiful children - Nathaniel and Superfly!{w=1.75}{nw}"
    cs_nobeep "{cps=40}Oh, we were so very very very happy, aw yeah.{w=1.5}{nw}"
    scene rosen_abode
    show pomni flipped at mid_left
    show cs flipped at mid_right
    cs_nobeep "{cps=40}But then one fateful night, Zelda said to me,{w=1.0}{nw}"
    cs_nobeep "{cps=40}She said,{w=0.75}{nw}"
    show pomni flipped at center with move
    zelda "{cps=40}Sweetie pumpkin? Do you wanna join the Columbia Record Club?{w=1.5}{nw}"
    show cs angry flipped
    window hide
    camera:
        parallel:
            linear 3 xpos -1600
        parallel:
            linear 3 ypos -300
        parallel:
            linear 3 zoom 2
    pause 2.5
    camera:
        parallel:
            linear 0.5 xpos 0
        parallel:
            linear 0.5 ypos 0
        parallel:
            linear 0.5 zoom 1
    show cs worried flipped
    cs_nobeep "{cps=40}I said, Whoa, hold on now, baby, I'm just not ready for that kind of a commitment!{w=2}{nw}" with hpunch
    hide cs with moveoutleft
    cs_nobeep "{cps=40}So we broke up and I never saw her again!{w=1.0}{nw}"
    cs_nobeep "{cps=40}But that's just the way things go,{w=0.75}{nw}"
    cs_nobeep "{cps=40}In Al{w=3}buquerque!{w=2}{nw}"
    cs_nobeep "{cps=40}Al{w=3}buquerque!{w=2}{nw}"
    pause 10.5
    #scene black
    #stop music
    #pakoo "Start string 5!"
    #play music albuquerque5 if_changed
    scene town
    show cs
    with dissolve
    cs_nobeep "{cps=40}Anyway, things really started lookin' up for me!{w=0.5}{nw}"
    cs_nobeep "{cps=40}Because about a week later, I finally achieved my lifelong dream.{w=1.5}{nw}"
    scene hell_kitchen
    show cs happy
    with dissolve
    cs_nobeep "{cps=40}That's right, I got me a part-time job at The Sizzler!{w=2}{nw}"
    cs_nobeep "{cps=40}I even made employee of the month after I put out that grease fire with my face!{w=1.0}{nw}"
    cs_nobeep "{cps=40}Aw yeah, everybody was pretty jealous of me after that!{w=1}{nw}"
    show cs
    cs_nobeep "{cps=40}I was gettin' a lot of attitude.{w=1}{nw}"
    scene parking_lot
    show cs
    with dissolve
    cs_nobeep "{cps=40}OK, like one time, I was out in the parking lot,{w=0.5}{nw}"
    cs_nobeep "{cps=40}Tryin' to remove my excess earwax with a golf pencil...{w=1}{nw}"
    cs_nobeep "{cps=40}When I see this guy Marty tryin' to carry a big ol' sofa up the stairs all by himself!{w=2}{nw}"
    scene archival_14
    show copguy at right
    with dissolve
    show cs at left with moveinleft
    cs_nobeep "{cps=40}So I, I say to him, I say, Hey, you want me to help you with that?{w=0.5}{nw}"
    cs_nobeep "{cps=40}And Marty, he just rolls his eyes and goes,{w=0.5}{nw}"
    show cs disappointed
    marty "{cps=40}No, I want you to cut off my arms and legs with a chainsaw.{w=2}{nw}"
    show cs happy
    cs_nobeep "{cps=40}So I did.{w=0.65}{nw}"
    hide copguy
    show copguy at manual_pos(0.75, 0.9, 0.5):
        rotate -30
    play sound sfx_chop
    show cs disappointed
    cs_nobeep "{cps=40}And then he gets all indignant on me!{w=0.75}{nw}"
    cs_nobeep "{cps=40}He's like,{w=0.5}{nw}"
    marty "{cps=40}Hey man, I was just being sarcastic!{w=0.5}{nw}"
    cs_nobeep "{cps=40}Well, that's just great!{w=0.55}{nw}"
    show cs angry
    cs_nobeep "{cps=40}How was I supposed to know that?{w=0.75}{nw}"
    scene parking_lot
    show cs angry
    cs_nobeep "{cps=40}I'm not a mind reader for cryin' out loud!{w=1}{nw}"
    show cs happy
    cs_nobeep "{cps=40}Besides, now he's got a really cute nickname: \"Torso-Boy\"!{w=1}{nw}"
    cs_nobeep "{cps=40}So what's he complaining about?{w=1}{nw}"
    show cs
    cs_nobeep "{cps=40}Say, that reminds me of another amusing anecdote.{w=1}{nw}"
    scene dumpster
    show cs at left
    with dissolve
    show taran at center with moveinright
    cs_nobeep "{cps=40}This guy comes up to me on the street and he tells me he hasn't had a bite in three days!{w=2.25}{nw}"
    cs_nobeep "{cps=40}Well, I knew what he meant...{w=0.25}{nw}"
    cs_nobeep "{cps=40}But just to be funny, I took a big bite out of his jugular vein!{w=1.5}{nw}"
    show cs at center with move
    show cs at left with move
    cs_nobeep "{cps=40}And he's yellin' and screamin' and bleeding all over!{w=0.5}{nw}" with vpunch
    hide taran with moveoutbottom
    cs_nobeep "{cps=40}And I'm like, Hey, come on, don'tcha get it?{w=0.5}{nw}"
    cs_nobeep "{cps=40}But he just keeps rolling around on the sidewalk, bleeding, and screaming!{w=0.5}{nw}"
    "Guy" "{cps=40}Gaaahhh! Owwwwwww! Owwwwwww! AHhhhhh!{w=0.5}{nw}" with vpunch
    show cs disappointed
    cs_nobeep "{cps=40}You know, just completely missing the irony of the whole situation.{w=0.5}{nw}"
    cs_nobeep "{cps=40}Man, some people just can't take a joke, you know?{w=1}{nw}"
    scene airplane_seats
    show cs disappointed at center
    show blank at mid_offscreen_right
    show amtrak_conductor flipped at mid_offscreen_left
    show shaggy_too_dope at mid_right
    show customer at mid_left
    with dissolve
    cs_nobeep "{cps=40}Anyway, um, um, where was I?{w=3}{nw}"
    cs_nobeep "{cps=40}Kinda lost my train of thought.{w=2}{nw}"
    cs_nobeep "{cps=40}Uh, well, uh, okay.{w=0.75}{nw}"
    cs_nobeep "{cps=40}Anyway I, I know it's kinda been a roundabout way of saying it...{w=0.75}{nw}"
    cs_nobeep "{cps=40}But I guess the whole point I'm tryin' to make here is:{w=0.75}{nw}"
    #scene black
    #stop music
    #pakoo "Start string 6!"
    #play music albuquerque6 if_changed
    camera:
        parallel:
            linear 0 xpos -333
        parallel:
            linear 0 ypos 0
        parallel:
            linear 0 zoom 1.33
    cs_nobeep "{cps=40}I...{w=1.0}{nw}"
    camera:
        parallel:
            linear 0 xpos -666
        parallel:
            linear 0 ypos -150
        parallel:
            linear 0 zoom 1.66
    cs_nobeep "{cps=40}HATE...{w=1.0}{nw}"
    camera:
        parallel:
            linear 0 xpos -1000
        parallel:
            linear 0 ypos -300
        parallel:
            linear 0 zoom 2
    cs_nobeep "{cps=40}SAUERKRAUT!{w=0.75}{nw}"
    camera:
        parallel:
            linear 1.5 xpos 0
        parallel:
            linear 1.5 ypos 0
        parallel:
            linear 1.5 zoom 1
    show cs
    cs_nobeep "{cps=40}That's all I'm really tryin' to say.{w=0.25}{nw}"
    cs_nobeep "{cps=40}And, by the way, if one day you happen to wake up,{w=0.5}{nw}"
    cs_nobeep "{cps=40}And find yourself in an existential quandary,{w=0.5}{nw}"
    cs_nobeep "{cps=40}Full of loathing and self-doubt,{w=1.0}{nw}"
    cs_nobeep "{cps=40}And wracked with the pain and isolation of your pitiful meaningless existence,{w=2.25}{nw}"
    cs_nobeep "{cps=40}At least you can take a small bit of comfort in knowing that{w=1.25}{nw}"
    cs_nobeep "{cps=40}Somewhere out there in this crazy old mixed-up universe of ours,{w=1.5}{nw}"
    cs_nobeep "{cps=40}There's still a little place {w=1.25}called,{w=1.75}{nw}"
    show cs happy
    cs_nobeep "{cps=40}Al{w=4.0}buquerque!{w=1.0}{nw}"
    cs_nobeep "{cps=40}Al{w=3.5}buquerque!{w=1.5}{nw}"
    show cs happy at little_bounce
    cs_nobeep "{cps=40}Albuquerque, Albuquerque!{w=1.3}{nw}"
    show cs happy at little_bounce
    cs_nobeep "{cps=40}Albuquerque, Albuquerque!{w=1.35}{nw}"
    show cs happy at little_bounce
    cs_nobeep "{cps=40}Albuquerque, Albuquerque!{w=1.3}{nw}"
    show cs happy at little_bounce
    cs_nobeep "{cps=40}Albuquerque, Albuquerque!{w=1.35}{nw}"
    show cs happy at little_bounce
    cs_nobeep "{cps=40}I said, A!{w=1.25}{nw}"
    crowd_nobeep "{cps=40}A!{w=0.65}{nw}"
    show cs happy at little_bounce    
    cs_nobeep "{cps=40}L!{w=0.65}{nw}"
    crowd_nobeep "{cps=40}L!{w=00.65}{nw}"
    show cs happy at little_bounce  
    cs_nobeep "{cps=40}B!{w=0.65}{nw}"
    crowd_nobeep "{cps=40}B!{w=0.6}{nw}"
    show cs happy at little_bounce  
    cs_nobeep "{cps=40}U!{w=0.6}{nw}"
    crowd_nobeep "{cps=40}U!{w=0.6}{nw}"
    cs_nobeep "{cps=40}......{w=2.0}{nw}"
    show cs happy at little_bounce  
    cs_nobeep "{cps=40}Querque!{w=1.0}{nw}"
    crowd_nobeep "{cps=40}Querque!{w=1.0}{nw}"
    show cs
    pause 4.0
    everyone_nobeep "{cps=40}Albuquerque, Albuquerque, Albuquerque, Albuquerque,{w=0.25}{nw}"  
    everyone_nobeep "{cps=40}Albuquerque, Albuquerque, Albuquerque, Albuquerque,{w=0.25}{nw}"
    everyone_nobeep "{cps=40}Albuquerque, Albuquerque, Albuquerque, Albuquerque,{w=0.25}{nw}"
    everyone_nobeep "{cps=40}Albuquerque, Albuquerque,{w=0.25}{nw}"
    cs_nobeep "{cps=40}Al{w=5}{cps=5}buquerque!"
    $ achievement_manager.unlock("albu")
    jump england
