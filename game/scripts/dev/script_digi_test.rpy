label _digi_test:
    $ chatted_with_digi = 0
    $ entered_tests = False
    stop music
    scene black with dissolve

    play sound sfx_nugget

    scene nugget_bedroom
    show digi happy
    with dissolve

    play music drive
    music drive

    digi "Oh, hey, welcome to the Nugget!"
    show digi
    digi "I assume you're here to test something.{w=1.0} Unless you just want to chat?"

    label .menu:
        show digi
        menu:
            "What do you want to do?"
            "I'd like to test things!":
                jump .tests
            "I want to talk!":
                jump .chat
            "I gotta head out.":
                show digi happy
                digi "Alright, seeya!"
                $ renpy.full_restart()

    label .chat:
        $ chatted_with_digi += 1
        if chatted_with_digi == 1:
            show digi disappointed
            digi "Well, unfortunately, Digi is lazy and didn't write much here yet."
            show digi shock
            digi "What? I'm Digi? "
            show digi
            extend "No, I mean Digi{font=cmunrm.ttf}[[0]{/font}."
            show digi sad
            digi "Don't ask. It's a lot to explain."
            show digi happy
            digi "Is there something else you want to do, though?"
        elif chatted_with_digi == 2:
            show digi disappointed
            digi "Well, unfortunately-- "
            show digi shock
            extend "wait, didn't we just do this?"
            show digi happy
            digi "Yeah, we did! You already know I have nothing to talk about right now."
            show digi goober
            digi "I appreciate you wanting to talk, though. Means a lot."
            show digi
            digi "Anywho, there's gotta be something else you need, right? If not, you can head out, it's chill."
        else:
            show digi angry
            digi "No, seriously. I'm out of stuff to say."
        jump .menu

    label .tests:
        show digi
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
            "Emoji":
                jump .test_emoji
            "Choice Menus":
                jump .test_choices
            "Digi EX":
                jump .test_digi_ex
            "None, actually!" (type = "bad"):
                show digi happy
                digi "Alrighty, then!"
                jump .menu

    label .test_md:
        show digi happy
        digi "Alright, let's see if we can get a few people yapping."
        show screen digimultiple([(amtrak_conductor, "I'm line one!"), (arceus, "I'm line two!"), (cs, "I'm line three, and I have a pause in it!")])
        pause
        hide screen digimultiple
        show digi sad
        digi "Did... did that work?"
        digi "I don't think it did, but I can't see it, I'm prewritten."
        jump .tests

    label .test_text_shaders:
        show digi shock
        digi "Text shaders? We have those?"
        show digi thinking
        digi "Let me check..."
        show digi shock
        digi "Oh, shit, yeah, we do!"
        show digi
        digi "OK, let me try some out."

        digi "{shader=dissolve}This one's called dissolve, which apparently reveals the text slowly over time..."
        digi "{shader=flip}This one's flip, I'm not quite sure what that means, though..."
        digi "{shader=jitter}This one's jitter, but I think we have something like that already."
        digi "{shader=linetexture:u__texture=rainbownoise.png}This is linetexture, I gave it rainbow noise as a texture."
        show digi thinking
        digi ":read: That one's kinda messed up, I think the texture size is weird."

        show digi happy
        digi "That's all I can be bothered to test right now, but I think we can make our own, too."
        jump .tests

    label .test_emoji:
        show digi happy
        digi "Ooh, so I'm proud of this one."
        digi "If you put something in the `gui/inline_text` folder, you can call it by name in text with the name, surrounded by colons."
        digi "So, like, :read: is `:read:`."
        digi "It's probably important that the image is ~45x45. We can't resize these on the fly."
        digi "Also, it has to be in a string that's being run through `substitutions()`, so that's important. Ask Tate for details on that."
        digi "Here are some emojis we have!"
        digi ":cs: :dx: :ce: :note1: :note2: :ch1: :ch2: :ch3: :ch4: :ch5: :heart: :warning:"
        digi "I hope that looks good!"
        digi "Apparently, you can also just use Unicode emoji, like 😅."
        digi "Did {i}that{/i} look good?"
        jump .tests

    label .test_choices:
        show digi disappointed
        digi "Here we go."
        menu:
            "One choice."
            "1":
                pass

        menu:
            "Two choices."
            "1":
                pass
            "Exit Test":
                jump .tests

        menu:
            "Three choices."
            "1":
                pass
            "2":
                pass
            "Exit Test":
                jump .tests
        
        menu:
            "Four choices."
            "1":
                pass
            "2":
                pass
            "3":
                pass
            "Exit Test":
                jump .tests

        menu:
            "Five choices."
            "1":
                pass
            "2":
                pass
            "3":
                pass
            "4":
                pass
            "Exit Test":
                jump .tests

        menu:
            "Six choices."
            "1":
                pass
            "2":
                pass
            "3":
                pass
            "4":
                pass
            "5":
                pass
            "Exit Test":
                jump .tests

        menu:
            "Seven choices."
            "1":
                pass
            "2":
                pass
            "3":
                pass
            "4":
                pass
            "5":
                pass
            "6":
                pass
            "Exit Test":
                jump .tests

        show digi sad
        digi "Sorry about that."
        jump .tests

    label .test_digi_ex:
        show digi sad
        digi "OK, I'll take you there, but be warned, if your computer isn't up to snuff, it won't go well."
        jump dx_digi_ex

    label .test_digi_ex_after:
        stop music
        scene black with dissolve
        play sound sfx_nugget
        scene nugget_bedroom
        show digi happy
        with dissolve
        play music drive
        music drive
        digi "I hope that went well!"
        jump .tests