label rockstar_start:
    scene black
    # Music CS is diagetically listening to plays in this scene
    n "CS is relaxing at home, listening to a vinyl."
    cs "Ah, it's good to just kick back and listen to some tunes."

    # SFX: ringtone
    n "Suddenly, his phone rings!"
    cs "Oh shi--"
    cs "Who could that be? I'm not expecting a call today."

    # Pause vinyl
    n "CS turns off the record player and answers the phone."

    # Howie appears on screen with a different background to represent this phone call.
    cs "Hello?"
    # Do we have a Howie Motif? Maybe we should? IDK music should play here.
    howie "Hey, CS, it's Howie. How's it hanging?"
    cs "Howie? It's been a while! I'm doing well, just relaxing after the crazy adventure I went on."
    howie "Good, good, glad to hear you've been getting that R&R, because I just might throw a wrench in that plan."
    cs "A wren-- wait, what do you mean?"
    howie "A bit of a twist in the schism, a knot in your drawstrings, you dig?"
    cs "No?"
    howie "Ah, come on, man, you know what I'm sayin'. I think it's time for that album, yeah?"
    cs "Album? I... didn't we make an album?"
    howie "Nah, man, that was just an EP! Sure, it's a great way to get your name out there, but now it's out there! It's out and about! It's time to capture that magic."
    cs "Howie, I appreciate it, I do, but [band_name] hasn't recorded anything since the tour, and I just don't know how easy it'll be to get everyone back together."
    howie "It's just you, Diet Cobain, and Fluffy Butt, right? Surely you three can find some time to make some dimes!"
    cs "I don't really need the money... we made quite a bit off that tour, and I still make money from YouTube Poops."
    howie "It's not about the money, baby! It's about the love of the craft, the feeling in your soul, the jazz up your--"
    cs "OK, OK, I get it. I'll give it some thought."
    howie "Well once you've thought enough thinks and drank enough drinks, hit me up. I got a pretty sweet deal on the table for both of us if ya do."

    # Bye, Howie. End Howie music.
    n "The phone hangs up."
    n "CS sets his phone down in thought."
    cs "[band_name] making an album again? I mean sure, I joked about [album_name] 2, but..."
    n "CS turns back on the vinyl he was listening to."

    # Turn back on the vinyl
    pause 5.0
    n "CS starts humming some words to himself."
    cs "{cps=15}{image=note_small1.png} [line_7]{w=1.5}\n[line_8]... {image=note_small2.png}"
    n "CS realizes what he's doing."
    cs "I need to get Anno and Arc."

    # Fade, new scene in CS' car
    cs "OK, I'll start driving to Anno's, and get Arc on the phone."
    cs "Arc's in the UK, so I'm a bit worried about getting him..."
    n "CS starts driving."
    cs "Good thing I got a Jupiter Jack from Billy."
    n "CS dials Arc and sets his phone in the center console."

    # SFX: ringing
    n "{i}Ring ring!"

    # Show Arc on phone
    arceus "CS? Man, it's like, late, me and Kitty are going to bed."
    cs "It's important, do you have a minute?"
    arceus "I guess, are... are you in the car?"
    cs "Yeah, I'm driving to Anno's place."
    arceus "Anno's? Why are you dong that?"
    cs "I want to get [band_name] back together."
    arceus "What? Wait, did Howie put you up to this?"
    cs "No! {w=0.5}Well..."
    arceus "I knew it."
    cs "No, it's not like that. He just got me thinking. I think I really want this."
    cs "I loved writing {i}[album_name]{/i} with you guys. And I think I still have music in my heart."
    cs "If you don't want to, you don't have to."
    arceus "It's not that I don't want to... I do, really. I want to support you, as well."
    arceus "I'm going to need to talk to Kitty."
    kitty "What was that, babe?"
    arceus "I'm gonna let you go. I'll get back to you."
    cs "Sounds good, let me know."
    arceus "See you, man!"
    
    # Hide Arc on phone
    n "CS drives on, listening to some tunes to get his mind in a music-making mood."
    cs "I hope Anno takes well to this."

    # Fade scene, CS in car at Anno's house
    cs "Alright, here goes nothing."

    # CS leaves car and is at Anno's door.
    n "{i}Knock knock!"
    anno_offscreen "The heck?"
    n "{i}Knock knock!"
    n "Anno comes to the door."
    anno "CS?"
    cs "Anno! Can I come in?"
    anno "Sure? What's this about?"
    cs "I'll tell you inside."

    # Scene change, inside Anno's house
    anno "What's going on?"
    cs "I want to get [band_name] back together."
    anno "What? Really? Did Howi--"
    cs "Arc said the same thing. {i}I{/i} want to do this. Howie just reminded me."
    anno "{i}sigh"
    anno "OK."
    cs "OK? That easy?"
    anno "I mean, I want to, too. If Arc is down, I don't see why not."
    cs "He should be calling me back soo--"

    # SFX: ringtone
    cs "Right on cue!"
    n "CS picks up the phone."
    cs "Hey Arc, what's the plan?"
    arceus "I'm in. But Kitty's coming."
    kitty "{i}But?"
    arceus "Sorry. {i}And{/i} Kitty's coming."
    kitty "Good."
    cs "Sounds good to me! When can you be here?"
    arceus "Well, work says I can't teleport anymore, so next time we get on a plane."
    cs "Work? Tele-- huh?"
    arceus "Don't worry about it."
    arceus "See you soon!"
    cs "Woohoo! We're getting [band_name] back together!"