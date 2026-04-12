init python:
    def play_nugget_playlist():
        songs = [audio.drive, audio.into_the_night, audio.escapements, audio.im_u, audio.bring_you_back, audio.bending_light]
        renpy.random.shuffle(songs)
        renpy.music.queue(songs, tight = True)
        
        for s in songs:      
            persistent.heard.add(find_id_by_filename(os.path.basename(getattr(s, 'filename', s))))
 
# Used for the NVL test.
define n_n = Character(None, kind=nvl, what_color="#BBBBBB", what_italic = True, callback = char_callback)
define digi_n = Character('Digi', kind=nvl, what_color="#009dff", callback = renpy.partial(char_callback, name = "digi", beep = "digi"))
define you_n = Character('You', kind=nvl, callback = char_callback)

label _digi_test:
    $ chatted_with_digi = 0
    $ entered_tests = False
    stop music
    scene black with dissolve

    play sound sfx_nugget
    play sound2 sfx_ambience_nugget loop
    $ play_nugget_playlist()
        
    scene nugget_bedroom
    show digi happy
    with dissolve

    music Nugget Mix:Beacon{size=-12} (Mix by DigiDuncan)

    digi "Oh, hey, welcome to the Nugget!"
    show digi
    digi "I assume you're here to test something.{w=1.0} Unless you just want to chat?"

    label .menu:
        show digi
        menu:
            "What do you want to do?"
            "I'd like to test things!":
                jump .tests
            "I want to chat!":
                jump .chat
            "I want to talk for a while! {size=-12}(NVL mode test)":
                jump .chat_nvl
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
            "osu!spinner":
                jump .test_osu_spinner
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
        call screen digimultiple([(digi, "I'm line one!"), (arceus, "I'm line two!"), (cs, "I'm line three, and I have a pause in it!")])
        pause
        hide screen digimultiple
        show digi sad
        digi "Did... did that work?"
        show digi happy
        digi "Tate might have fixed it, so I hope it did."

        show digi
        digi "Now, let's try it with the lexer..."
        multiple:
            digi "Hello, I'm being lexed!"
            "Awawa" "And what the fuck does that mean?"
            mean "They're being lexed, doofus, what's there to not understand?!"

        show digi thinking
        digi "That was certainly dialouge."
        show digi disappointed
        digi "{font=digi}Dialouge? Dialogue? Dialog? 【/'daɪəˌɫɔɡ/|dai·uh·laag】. Whatever."
        show digi happy
        digi "Anywho, hope it worked for ya!"

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

    label .test_osu_spinner:
        digi "Oh jeez, the osu!spinner."
        digi "I'll call one up. I don't know how accurate it is though."
        window hide
        call screen osu_spinner(dismissable = True)
        hide screen osu_spinner
        window show
        digi "Did that work well?"
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

    label .chat_nvl:
        # Welcome to a full-scale test of NVL mode.
        # This is going to be very custom for what I want, so if we want to do this
        # in other parts of the game, this might be a good template, but we should
        # definitely look into a more consistent themeing for all of this.
        show digi at mid_left with move
        nvl clear
        n_n "You start chatting with Digi."
        $ just_entered = True
        $ mentioned_iris = False
        digi_n "Hey! What do you want to talk about?"
        jump .chat_nvl_topics

    label .chat_nvl_topics:
        if not just_entered:
            digi_n "What else do you want to talk about?"
        else:
            $ just_entered = False
        menu (nvl = True):
            "What is this place?":
                nvl clear
                you_n "What is this place?"
                digi_n "Well, do you mean on Layer 1, or Layer 0?"
                jump .chat_nvl_layers
            "Iris?" if mentioned_iris:
                nvl clear
                you_n "Iris?"
                digi_n "Yeah, Iris! She's my friend and... boss? Kinda? I work for her, but the relationship isn't really formal."
                digi_n """When I first got to this universe, I was kinda... adrift, for a while. Didn't have a place to go.
                She took me in after I had a run in with a black hole.

                ...

                OK, yes, it was my fault for getting that close, I don't want to talk about it right now. Some other time.

                Anywho, she took me in, gave me some equipment, helped me back on my feet,
                and gave me the opportunity to help her out with what she does.
                """
                you_n "What does she do?"
                digi_n "I don't have time to get into that right now, to be honest. Another time."
                jump .chat_nvl_topics
            "Nothing else!":
                you_n "Nothing else!"
                jump .chat_nvl_exit

    label .chat_nvl_layers:
        menu (nvl = True):
            "Layer 1?":
                nvl clear
                you_n "Layer 1?"
                digi_n "Well, on Layer 1, this is the Nugget!"
                digi_n """The Nugget is my spaceship. I've had it for quite a while...
                I got it shortly after I entered this universe.

                The details are hazy, but this ship used to be a lot more rinky-dink.
                I did a lot of upgrades after acquiring it, though. It still doesn't run {i}perfectly{/i} but
                it's a pretty good ship at this point. Iris keeps bugging me to upgrade to ion thrusters from
                hydrogen ones, though.
                """
                $ mentioned_iris = True
                jump .chat_nvl_topics
            "Layer 0?":
                nvl clear
                you_n "Layer 0?"
                digi_n "This is a test room for some features Digi{font=cmunrm.ttf}[[0]{/font} wants to mess around with."
                digi_n "It being a seperate space gives them the creative freedom to just kinda mess around."
                digi_n "Some problems with the game have already been spotted with this method!"
                jump .chat_nvl_topics
            "You keep saying layers...?":
                nvl clear
                you_n "You keep saying \"layers\", what do you mean by that?"
                digi_n "Layers, like layers of fiction."
                digi_n """You, the person reading this, are in Layer 0. You are in the \"real world.\"
                
                Now, I hate to break it to ya, but I'm not. I'm in Layer 1, which to you, is fiction.
                Going deeper into fiction increases the number. Going up the chain decreases it.
                So, if {i}I{/i} wrote a fictional story, that story would take place in Layer 2.
                
                It's a theory in pataphysics, there's a write up in the {i}Report on SCP-3812's Behavioural Instability and the Implication of Existential--{/i}
                """
                n_n "Digi cuts themselves off before they bore you."
                digi_n "Sorry, never mind, it's complex. I won't bore you with the details."

                menu (nvl = True):
                    "No, give me the details!":
                        nvl clear
                        you_n "No, give me the details!"
                        digi_n "OK, well, here."
                        n_n "Digi pokes at the hologram eminating from their wrist."
                        n_n "Your phone lights up with a notification."
                        digi_n "There, I sent you a link to the {a=https://scp-wiki.wikidot.com/scp-3812}article.{/a}"
                        digi_n "It's a cool read."
                    "Thank you.":
                        pass

                jump .chat_nvl_topics
        
        jump .chat_nvl_topics

    label .chat_nvl_exit:
        digi_n "Alrighty!"
        digi_n "{size=-12}I hope NVL mode worked well..."
        show digi at center with move
        jump .menu
