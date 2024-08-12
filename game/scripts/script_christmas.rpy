label dx_christmas_start:
    play music lets_hear_winter volume 0.7
    scene black
    n "CS wakes up to a snowy winter morning."
    cs "Yes! It snowed today!"
    n "CS looks at his calendar."
    cs "Woohoo!"
    cs "Christmas is almost here!"
    cs "...And you know what that means!"
    cs "I finally get to throw a huge Christmas party at my house!"
    cs "I'm so pumped, I should call everyone again to make sure they are coming."
    n "CS calls all of his guests who he invited a couple weeks ago."
    cs "Alright, well, the party is going to start in 2 days."
    cs "I have not prepared at all."
    cs "Fuck."
    cs "Okay, well first place I need to start is by checking out my house."
    cs "I have this huge mansion, and I don't even use the rest of my house!"
    cs "Let's go look."
    n "CS walks into his living room."
    cs "Well, okay maybe I should bring in the Christmas supplies first."
    cs "Let's go see what we have."
    n "CS goes into his garage."
    cs "Okay, okay, what should I get first..."
    menu:
        "Christmas tree":
            jump dx_christmas_tree
        "Lights and garland":
            jump dx_christmas_lights
        "Ornaments and decorations":
            jump dx_christmas_decor

# christmas tree
label dx_christmas_tree:
    cs "I should get the Christmas tree first."
    cs "Who doesn't wanna get this thing out? This is the best part of decorating!"
    cs "I just, need to be, careful..."
    cs "Hnng..."
    n "All of a sudden, the shelf tips and all of the supplies fall onto CS!"
    $ tree_first = True
    cs "Shit!"
    # crashing SFX
    cs "Ow..."
    n "CS gets himself out of the mess of lights, garland, and Legos."
    # CS steps on a Lego.
    cs "Fuck!"
    cs "Man, what a mess! "
    cs "This is gonna take forever to clean up!"
    jump dx_christmas_anno


# Decorations/lights
label dx_christmas_lights:
    cs "I should probably get the lights and garland first, they are in the easiest box for me to grab anyways."
    n "CS gets the box inside, and then goes back to the garage to grab the next box."
    return

label dx_christmas_decor:
    n "Not done yet."
    return

label dx_christmas_anno:
    cs "Maybe I should call someone over to help."
    cs "Lemme see if Anno is around..."
    n "CS decides to call Anno."
    anno "Hello?"
    cs "Hey Anno, CS here!"
    anno "Yes, I know the party is in two days, you just called me."
    cs "Well, I was wondering..."
    cs "If you wanted to help me decorate my house!"
    anno "I still have to get a gift for the gift exchange..."
    anno "...But I can do that tomorrow."
    anno "I'll come over. Be there soon."
    cs "Cool!"
    cs "Alright, I got Anno to come over and help out!"
    cs "I guess I'll just plan out how I want the house to look."
    cs "Actually, shit, it snowed last night!"
    cs "I need to shovel before Anno gets here!"
    n "CS gets dressed and goes out into the garage to get his shovel."
    if tree_first:
        cs "Shit! I hate Legos, but only when they're in my feet!"
    cs "Okay, now the real question is, how much did it snow?"
    n "CS presses the garage button, and nothing happens."
    cs "Damnit, I think it's iced shut."
    cs "I'm gonna have to go out in front."
    n "When CS gets outside, he finds a massive snow drift blocking his garage."
    cs "Well that's just great."
    cs "This is gonna take an hour at least to scoop this all up."
    cs "I better get to it, I guess."
    n "As CS is about 10 minutes into shoveling, CS hears someone walking up his driveway."
