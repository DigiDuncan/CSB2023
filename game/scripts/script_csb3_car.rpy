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

    cs "So, there's going to be a bunch of random dialouge here?"
    arceus "Eyup."
    cs "So we just need to sit here and talk for a while?"
    arceus "May as well, passes the time."
    cs "Fair enough."
    arceus "What do you wanna talk about?"
    cs "Man, I don't know, I've been through a lot."
    arceus "Man, same. I'm tired. And I don't think Digi wants to write more right now."
    cs "Huh?"
    arceus "Don't worry about it."

    $ achievement_manager.unlock("Bored")

    jump back_home
