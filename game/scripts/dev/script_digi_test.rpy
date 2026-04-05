label _digi_test:
    $ chatted_with_digi = 0
    $ entered_tests = False
    stop music
    scene black with dissolve

    play sound sfx_nugget

    scene nugget_bedroom
    show digi
    with dissolve

    music drive

    digi "Oh, hey, welcome to the Nugget!"
    digi "I assume you're here to test something.{w=1.0} Unless you just want to chat?"

    label .menu:
        menu:
            "What do you want to do?"
            "I'd like to test things!":
                jump .tests
            "I want to talk!":
                jump .chat
            "I gotta head out.":
                digi "Alright, seeya!"
                $ renpy.full_restart()

    label .chat:
        $ chatted_with_digi += 1
        if chatted_with_digi == 1:
            digi "Well, unfortunately, Digi is lazy and didn't write much here yet."
            digi "What? I'm Digi? No, I mean Digi{font=cmunrm.ttf}[[0]{/font}."
            digi "Don't ask. It's a lot to explain."
            digi "Is there something else you want to do, though?"
        elif chatted_with_digi == 2:
            digi "Well, unfortunately-- "
            extend "wait, didn't we just do this?"
            digi "Yeah, we did! You already know I have nothing to talk about right now."
            digi "I appreciate you wanting to talk, though. Means a lot."
            digi "Anywho, there's gotta be something else you need, right? If not, you can head out, it's chill."
        else:
            digi "No, seriously. I'm out of stuff to say."
        jump .menu

    label .tests:
        if not entered_tests:
            digi "What test are you looking to run?"
            $ entered_tests = True
        else:
            digi "What now?"

        menu:
            "What test?"
            "Multiple Dialogue":
                jump .test_md
            "Text Shaders":
                jump .test_text_shaders
            "None, actually!" (type = "bad"):
                digi "Alrighty, then!"
                jump .menu

    label .test_md:
        digi "Alright, let's see if we can get a few people yapping."
        show screen digimultiple([(digi, "I'm line one!"), (tate, "I'm line two!")])
        digi "Did... did that work?"
        digi "I don't think it did, but I can't see it, I'm prewritten."
        jump .tests

    label .test_text_shaders:
        digi "Text shaders? We have those?"
        digi "Let me check..."
        digi "Oh, shit, yeah, we do!"
        digi "OK, let me try some out."

        digi "{shader=dissolve}This one's called dissolve, which apparently reveals the text slowly over time..."
        digi "{shader=flip}This one's flip, I'm not quite sure what that means, though..."
        digi "{shader=jitter}This one's jitter, but I think we have something like that already."
        digi "{shader=linetexture:u__texture=rainbownoise.png}This is linetexture, I gave it rainbow noise as a texture."
        digi ":read: That one's kinda messed up, I think the texture size is weird."

        digi "That's all I can be bothered to test right now, but I think we can make our own, too."
        jump .tests