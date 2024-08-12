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
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if lights_first or decor_first:
        $ tree_second = True
        cs "Alright, time to get the Christmas tree!"
        n "CS drags the box out of the garage and brings it into his living room."
        n "CS goes back to the garage."
        if lights_first:
            jump dx_christmas_decor
        if decor_first:
            jump dx_christmas_lights
    $ tree_first = True
    if tree_first:
        cs "I should get the Christmas tree first."
        cs "Who doesn't wanna get this thing out? This is the best part of decorating!"
        cs "I just, need to be, careful..."
        cs "Hnng..."
        n "All of a sudden, the shelf tips and all of the supplies fall onto CS!"
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
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if tree_second or decor_first:
        cs "Alright, I should probably get the lights and garland next."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
        if tree_second:
            jump dx_christmas_decor
        if decor_first:
            jump dx_christmas_tree
    $ lights_first = True
    if lights_first:
        cs "I should probably get the lights and garland first, they are in the easiest box for me to grab anyways."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
    menu:
        "Christmas tree":
            jump dx_christmas_tree
        "Ornaments and decorations":
            jump dx_christmas_decor

label dx_christmas_decor:
    if decor_first and tree_second and lights_first:
        jump dx_christmas_before_anno
    if tree_second or lights_first:
        cs "Alright, I should probably get the decorations next."
        n "CS gets the box inside, and then goes back to the garage to grab the next box."
        if tree_second:
            jump dx_christmas_lights
        if lights_first:
            jump dx_christmas_tree
    $ decor_first = True
    if decor_first:
        cs "I'm gonna get the decorations first, I have a huge assortment of Legos in there!"
        n "CS gets the box inside, and then goes back to the garage to grab the next box."   
    menu:
        "Christmas tree":
            jump dx_christmas_tree
        "Lights and garland":
            jump dx_christmas_lights

label dx_christmas_before_anno:
    cs "Well that's all done!"
    cs "I have moved all of the Christmas supplies into the house!"
    cs "This is where the fun part begins!"
    jump dx_christmas_anno

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
    carguy "Nice snow!"
    carguy "Nooot so nice driveway."
    cs "Look man, I'm trying. It's cold as balls out here."
    carguy "Speaking of balls, you need some help?"
    carguy "I got something you might need!"

