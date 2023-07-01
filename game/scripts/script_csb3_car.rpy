screen skip_car():
    zorder 100
    layer "music"
    style_prefix "skip_car"

    frame at t_skip_car:
        imagebutton idle "images/skip_now.png" hover_sound "sfx-select.wav":
            action Play("sound", "sfx-valid.wav"), Hide("skip_car", Fade(1.0)), Jump("back_home")

transform t_skip_car:
    xanchor 1.0 xpos 0.95
    yanchor 0.0 ypos 0.05

style skip_car_frame is empty

label car_dialogue:
    cs "Well Arceus, it has been quite a ride."
    arceus "It sure has. We've been through quite a lot haven't we?"
    cs "Yeah, I'm so tired. I can't wait to get some actual rest."

    show screen skip_car

    cs "So, Arc?"
    arceus "Yeh?"
    cs "Are you a furry?"
    arceus "I mean, I {i}am{/i} furry."
    cs "You know what I mean."
    arceus "Is it really being a furry if I'm literally not a human?"
    cs "Fair point."

    pause 1.0

    cs "You know, I can drive, Billy."
    billy "This is my car!"
    cs "Well, yeah, but if you don't want to drive the whole way..."
    billy "No, I'm good. You're in my car, and that means I'll drive!"
    cs "Alright man, I just don't feel like we paid you enough for this."
    billy "Everything I sell, it's always $19.95!"
    cs "Well, thanks man."
    billy "That's the power of friendship!"

    pause 1.0

    cs "So Arc, where'd you learn to hack like that?"
    arceus "College."
    cs "You went to college? I thought you'd been in prison for five years!"
    arceus "And...?"
    cs "How... how old are you?"
    n "Arc locks eyes with CS."
    cs "I forgot what I was saying, never mind."
    arceus "Yeah, that's fine."

    pause 1.0

    cs "How long is this drive?"
    arceus "You sound like a child asking their mom if they're at Disney World yet."
    cs "I'm sorry man, I just want to get home."
    billy "It's quite a ways away still!"
    cs "Aw man..."
    arceus "Listen, at least the cops aren't after us this time."
    billy "What?"
    cs "Don't worry about it."

    pause 1.0

    n "Billy get a call on his Jupiter Jack."
    carla "Hey Billy, it's Carla!"
    billy "What are you doing in my car?"
    carla "I'm not in your car, I'm on the phone. You're using the Jupiter Jack, remember?"
    billy "Oh yeah."
    carla "We have a meeting in twenty minutes."
    billy "I'm in the fucking northeast!"
    carla "What? What are you doing there?"
    billy "It's my car!"
    n "Billy hangs up the phone."
    billy "Unbelivable."
    
    pause 1.0

    arceus "Why do you still for Adobe Premiere?"
    cs "Well, I pay for the whole Creative Cloud."
    arceus "You know, I can get you the whole suite for free."
    cs "No, no, I know, I just don't feel like I should."
    arceus "Yarr."
    cs "No, thank you, I understand what you were insinuating."
    arceus ";)"
    billy "How much are you paying for it?"
    cs "Like $50 a month..."
    billy "Unbelivable! I wouldn't pay more than $19.95!"
    billy "And buy one get one free!"
    cs "What would I do with two Adobe suites?"
    billy "What would you do with two Grater Platers?"
    cs "Fair enough."

    pause 1.0

    cs "Have you heard of Genshin Impact? Start your adventure on the continent of Teyvat, and--{w=0.5}"
    arceus "{b}No.{/b}"
    billy "I'm a pitchman, and even I won't stoop that low."
    n "CS shuts up."

    $ achievement_manager.unlock("Bored")

    hide screen skip_car

    jump back_home
