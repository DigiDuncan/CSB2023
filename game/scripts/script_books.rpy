# TODO: make this book only appear if you've defeated Perfect Tate.
# TODO: finish art for said book.
# TODO: make sprites for tate_cyan

label book_celestial_sightseeing:
    play music we_will_meet_again
    music we_will_meet_again
    pause 1.0
    tate_cyan_offscreen "Ah, so {i}that's{/i} where the conduit landed."
    tate_cyan_offscreen "What a fitting location."

    scene nursing_home
    show tate at mid_mid_left
    with dissolve

    # TODO: hey can baker or someone pls go through all my dxcom audios and make em louder? thanks
    dxcom tate_sick

    tate_cyan_offscreen "It's kinda perfect, actually."
    cs "Huh?"
    tate_cyan_offscreen "Hello, CS."

    show cs disappointed flipped at offscreenright
    show cs disappointed flipped at right with MoveTransition(1.0)
    pause 1.0

    cs "Who are you? And how do you know my name?"
    cs "And... {nw}"
    show cs worried flipped
    extend "what {i}happened{/i} to you?"
    tate_cyan_offscreen "Ah... I was expecting them to have already told you."
    show cs disappointed flipped
    "..."
    tate_cyan_offscreen "...{fast} But... at the same time..."
    tate_cyan_offscreen "I suppose, knowing us, it makes sense, too, that they have not."
    show cs worried flipped
    cs "{i}Huh?!"
    tate_cyan_offscreen "Ah-- it's... kind of... a {i}lot."
    tate_cyan_offscreen "I'll try to make it make sense."
    show cs disappointed flipped
    tate_cyan_offscreen "I know you already know Tate."
    tate_cyan_offscreen "In a way, I am also Tate. That is how I know you."
    $ persistent.seen.add("tate_cyan")
    tate_cyan "Through this book, I can see what goes on in your realm."
    tate_cyan "As for what happened to my body..."
    tate_cyan "Don't worry about the details."
    tate_cyan "Just know that forbidden magick is typically forbidden for a reason."
    show cs worried flipped

    # TODO: maybe redo this later
    if fun_value(FUN_VALUE_RARE):
        cs "Magick...? With a K?"
        cs "Tate's a {i}witch?!"
        show cs disappointed flipped
        tate_cyan "Look, I know {i}you{/i} can read the text box, too, and that we can {i}both{/i} break the fourth wall, but could you maybe {i}not{/i} do that here?"
        tate_cyan "This connection isn't exactly stable to begin with, y'know."
        tate_cyan "Anyway, no, we are not witches."
    else:
        cs "Magick...? Like... {i}real{/i} magick?!"
        cs "Tate's a {i}witch?!"
        show cs disappointed flipped
        tate_cyan "Oh, heavens, no."

    tate_cyan "Where we come from, we'd have been hanged for that."
    tate_cyan "Well... {nw}"
    show cs worried flipped
    extend "{size=-5}I suppose they {i}already{/i} wanted to do that, just for... {nw}"
    show cs scared flipped
    extend "{size=-5}slightly {i}different{/i} reasons..."
    "..."
    tate_cyan "Anyway, no."
    show cs disappointed flipped
    tate_cyan "We were... in a bad spot."
    tate_cyan "Desperate for an escape, we decided to... open a door... to... outside."
    tate_cyan "Literally to anywhere else. We did not have a destination in mind."
    tate_cyan "In hindsight, perhaps that lack of clear direction contributed to... all of this."
    n "Tate gestures vaguely towards the nearby IV pole."
    "..."

    if fun_value(FUN_VALUE_COMMON):
        tate_cyan "I can tell that you're still unsatisfied."
        show cs angry flipped
        cs "100%%, even."
    else:
        tate_cyan "I can tell that you still aren't satisfied."
        show cs angry flipped
        cs "Not even 50%%."

    show cs surprised flipped
    tate_cyan "Very well."
    tate_cyan "We knew we weren't going to survive if we stayed."
    tate_cyan "We also figured that we'd at least die a much more {i}interesting{/i} death if we had tried and failed than if we had never tried at all."
    show cs disappointed flipped
    cs "Okay, but... what exactly {i}happened?"
    cs "I still don't get how you ended up... like {i}this."
    tate_cyan "Ah..."
    tate_cyan "You see, this very book was discovered to be missing during the last moments of the ritual."
    tate_cyan "While we did barricade the door before we began, we knew that it wouldn't hold for long if--{w=0.5}{nw}"
    show cs surprised flipped
    cs "So you {i}stole{/i} the book."
    tate_cyan "...!" with vpunch
    n "Tate anxiously scratches at something under the neck of their shirt."
    cs "... What happened next?"
    tate_cyan "Ah..."
    tate_cyan "O-{w=0.1}Our hands shook as we completed the circle."
    tate_cyan "Sweat and tears fell onto the stone and made the ink start to run."
    tate_cyan "The final sigil was rushed and came out sloppy. But we had no time to redo it."
    show cs worried flipped
    tate_cyan "We could hear the door splintering behind us."
    tate_cyan "We had no choice but to see it through."
    tate_cyan "With a flick of our blade, the portal opened."
    tate_cyan "With nothing left for us in that world..."
    show cs scared flipped
    tate_cyan "We jumped."
    "..."
    "..."
    show cs worried flipped
    tate_cyan "In certain circles, it is whispered..."
    tate_cyan "They say it's not about the technique, or even about how much experience a practictioner has..."
    tate_cyan "They say it's all about one's own inner strength, and about the intention behind one's actions..."
    tate_cyan "With these words held close to our heart, we had hoped that our will to live would see us through..."
    tate_cyan "You know... {i}in one piece."
    "..."
    "..."
    tate_cyan "As you can probably tell, we were lied to."
    show cs disappointed flipped
    cs "Jeez... you're speaking in riddles."
    cs "So there's... {nw}"
    show cs worried flipped
    extend "{i}two{/i} of you?"
    cs "Did you, like, get split into pieces or something?"
    n "Tate takes a nervous sip from their juice box."
    n "CS notices that their hands look almost... skeletal."
    "..."
    tate_cyan "{color=#00FFFF}Mind{/color}, {color=#FF00FF}body{/color}, and {color=#FFFF00}spirit.{/color}"
    tate_cyan "In many ways, {color=#FFFF00}the Tate you know{/color} will live on no matter what happens to the rest of us."
    tate_cyan "As for {color=#00FFFF}me{/color}..."
    tate_cyan "My new IV bags should be in soon. You should probably get out of here before the nurse comes to hook me back up to that damn pole."
    cs "Wait, why do I have to leave? I still have so many questions..."
    tate_cyan "Well, {i}I{/i} want to rest, and {i}you{/i} didn't sign in at the front desk."
    tate_cyan "I don't think either of us wants to deal with any questions from security."
    show cs disappointed flipped
    cs "I guess that's fair..."
    tate_cyan "When you get back, will you please put that book back where you found it?"
    cs "Sure thing."
    tate_cyan "And-- ah! Please do me one other favor."
    tate_cyan "Don't tell the Tate of your world that we have met."
    tate_cyan "You know how I-- well, I guess, you know how {i}we{/i} can get."
    tate_cyan "I don't need that one asking too many questions."
    tate_cyan "I {i}certainly{/i} don't need them trying to... {nw}"
    show cs worried flipped
    extend "break anything else on their own."
    tate_cyan "I simply don't have the time to babysit that one right now. I need to focus on my recovery."
    cs "Well... "
    show cs disappointed flipped
    extend "alright..."
    cs "I, uh... {nw}"
    show cs flipped
    extend "I hope you get well soon, other-Tate!"
    tate_cyan "Thank you."
    tate_cyan "And I hope {i}you{/i} enjoy the rest of your adventure."
    show cs disappointed flipped
    cs "Thanks{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}?"

    scene black with dissolve

    pause 1.5
    tate_cyan "And don't go jumping through any wormholes, y'hear?!"
    pause 1.0
    n "CS closes the book."
    n "As he does, it suddenly feels heavier in his hands."
    n "Curiosity continuing to eat at him, he tries to reopen it, but the pages do not budge. It is as if they have turned to stone."
    n "Defeated, he slips the strange tome back into its place on the shelf."
