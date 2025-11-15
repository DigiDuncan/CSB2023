label bt1d_cvs:

    # This scene should be beefed up a bit, I think.
    n "The Nugget lands in the CVS parking lot, and the two clammer out into the daytime."
    cs "To the pharmacy department!"

    n "CS and Digi arrive at the pharmacy, and confront the pharmacy worker."
    cvs "Welcome to CVS, can I help you today?"
    cs "Yeah, you can tell me why insulin is so expensive!"
    cvs "Do you have a prescription to pick up?"
    cs "No! I'm just pissed!"
    digi "Sorry, excuse him. He's being a bit {nw}"
    extend "{i}too aggressive." with hpunch
    cs "... Sorry."
    digi "The question is more generic, do you know why insulin is so expensive?"
    cvs "I don't really know, the insulin companies just set the prices. We don't have control of it."
    cs "Hmmm... what insulin companies?"
    cvs "It's mostly one, 'Leedlelee.'"
    digi "Well, that's all the information we're going to get. Thank you!"
    digi "Let's go, CS."
    n "CS and Digi walk out of the CVS."
    # let the shot linger here for a moment.
    n "The CVS worker picks up their work phone."
    cvs "A cat maid and a tiny cyborg just came in here assailing me about insulin prices."
    cvs "Am I reporting this? What is there to report? I'm just telling you, I guess."
    cvs "Get back to work? Yeah, that makes sense."
    # fade out

    # interior nugget
    cs "So, now what?"
    digi "We gotta go find Leedlelee, I suppose."
    n "Digi starts plugging coordinates into the console of the ship."
    digi "I think I know where to go... the question is, will we be able to talk to the CEO."
    cs "I don't know if they're just going to let two idiots with an agenda up to the penthouse."
    digi "I've done weirder."
    cs "You know, come to think of it, so have I."
    digi "Then we'll try our luck!"

    n "The Nugget lands in to the parking lot of the Leedlelee offices."
    digi "No where to go but up!"
    cs "Let's do this."

    # interior office
    receptionist "Welcome to Leedlelee, do you have an appointment?"
    cs "No, we--"
    digi "Let me handle this."
    digi "We need to speak to the CEO."
    receptionist "I can't let you up without an appointment. The CEO is a very busy man."
    digi "We understand, we only need a minute of his time."
    receptionist "Hmm. Let's see how his mood is, then."
    n "The receptionist calls up to the CEO."
    receptionist "Yes, there's two people here to see you.{w=2} No, they don't have an appointment.{w=2} Yes, sir, I understand.{w=1} One minute, sir? I'll let them know.{w=2} Thank you, sir."
    n "The receptionist hangs up the phone."
    receptionist "You have one minute. Good luck."
    cs "Thank you so much!"
    receptionist "Don't mention it."
    digi "Let's hurry!"
    n "The two scurry into the elevator."

    # in the elevator
    cs "Do you think we'll get any information out of him?"
    digi "Only one way to find out. We need to convince him we're on his side."
    cs "Are we?"
    digi "To be honest?"
    digi "No."

    # elevator ding

    # interior penthouse office
    leedle "Who are you two? I don't have all day."
    cs "We're here to ask you a quick question."
    digi "We're looking for the source of these high insulin prices."
    cs "Yeah, why do you--"
    n "Digi shoulders CS in the side." with hpunch
    digi "What my friend {i}meant{/i} to say, was we don't think it's you."
    digi "My bet? There's someone up the chain pulling {i}your{/i} chain. Am I right?"
    leedle "And why would I tell you?"
    digi "Because we can help."
    leedle "Yeah? How do I know you aren't recording this with your cyborg gobbledygook, and you're going to blackmail me!"
    cs "{size=-20}{cshake}Guilty concious..."
    digi "Listen. I'll make you a deal."
    digi "If you tell us who's up to this, we'll (insert bribe here.)" # FIX
    leedle "Fine."
    leedle "Fine!"
    leedle "I don't know his name."
    leedle "He calls himself the CEO of Diabetes."
    n "Digi gasps."
    cs "What's wrong?"
    digi "I know him."
    cs "{i}You know him?!"
    digi "Yeah. I've fought with him before."
    digi "CS, let's go."
    digi "Thank you... what's your name?"
    leedle "(name)." # FIX
    digi "Thanks, (name)."
    n "Digi heads out back to the elevator, and CS quickly follows."

    n "The elevator ride is quiet, but the energy is tense."
    n "Even CS recognizes now isn't the time to speak."

    jump secret_dx
