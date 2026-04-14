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

init python:
    import datetime
    import hashlib

    def weed_legality():
        return hashlib.sha256(bytes(f"{datetime.date.today()}", encoding="utf-8")).digest()[0] % 2 == 0

screen isweedlegal():
    modal True
    $ response = "Yes." if weed_legality() else "No."
    $ today = datetime.date.today().strftime("%B %d, %Y")

    frame:
        background "#0C132C"
        xfill True
        yfill True
        vbox:
            align (0.5, 0.0)
            text "THE WHITE HOUSE":
                font "fonts/InstrumentSerif-Regular.ttf"
                size 64
                text_align 0.5
                align (0.5, 0.0)
            text "WASHINGTON, D.C.":
                font "fonts/InstrumentSerif-Regular.ttf"
                size 32
                text_align 0.5
                align (0.5, 0.0)
            add "gui/star_hr.png"
        vbox:
            align (0.5, 0.5)
            text response:
                font "fonts/InstrumentSerif-Regular.ttf"
                size 256
                text_align 0.5
                align (0.5, 0.5)
            text "for the day of [today]":
                font "fonts/InstrumentSerif-Italic.ttf"
                size 64
                text_align 0.5
                align (0.5, 0.5)

        add "gui/star_hr.png":
            align (0.5, 0.95)

        textbutton _("Return"):
            xpos 15 ypos 1000
            action [
                Hide("isweedlegal"),
                Return(),
                With(dissolve)
            ]

label _digi_test:
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
            "I want to talk! {size=-12}(NVL mode test)":
                jump .chat
            "I gotta head out.":
                show digi happy
                digi "Alright, seeya!"
                $ renpy.full_restart()

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

    label .chat:
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
        jump .chat_topics

    label .chat_topics:
        if not just_entered:
            digi_n "What else do you want to talk about?"
        else:
            $ just_entered = False
        menu (nvl = True):
            "How are you?":
                jump .chat_how_are_you
            "What is this place?":
                nvl clear
                you_n "What is this place?{fast}"
                digi_n "Well, do you mean on Layer 1, or Layer 0?"
                jump .chat_layers
            "Aren't you like, small sometimes?":
                jump .chat_small
            "Is weed legal today?":
                jump .chat_is_weed_legal
            "Who's Iris?" if mentioned_iris:
                nvl clear
                you_n "Who's Iris?{fast}"
                show digi happy
                digi_n "Yeah, Iris! She's my friend and... boss? Kinda? I work for her, but the relationship isn't really formal."
                show digi
                digi_n """When I first got to this universe, I was kinda... adrift, for a while. Didn't have a place to go.
                She took me in after I had a run in with a black hole."""
                show digi sad
                digi_n "..."
                show digi disappointed
                digi_n "OK, yes, it was my fault for getting that close, I don't want to talk about it right now. Some other time."
                show digi
                digi_n "Anywho, she took me in, gave me some equipment, helped me back on my feet, and gave me the opportunity to help her out with what she does."
                you_n "What does she do?"
                show digi thinking
                digi_n "I don't have time to get into that right now, to be honest."
                show digi
                extend " Another time."
                jump .chat_topics
            "Nothing else!":
                you_n "Nothing else!"
                jump .chat_exit

    label .chat_layers:
        menu (nvl = True):
            "Layer 1?":
                nvl clear
                you_n "Layer 1?{fast}"
                digi_n "Well, on Layer 1, this is the Nugget!"
                digi_n """The Nugget is my spaceship. I've had it for quite a while...
                I got it shortly after I entered this universe.

                The details are hazy, but this ship used to be a lot more rinky-dink.
                I did a lot of upgrades after acquiring it, though. It still doesn't run {i}perfectly{/i} but
                it's a pretty good ship at this point. Iris keeps bugging me to upgrade to ion thrusters from
                hydrogen ones, though.
                """
                $ mentioned_iris = True
                jump .chat_topics
            "Layer 0?":
                nvl clear
                you_n "Layer 0?{fast}"
                digi_n "This is a test room for some features Digi{font=cmunrm.ttf}[[0]{/font} wants to mess around with."
                digi_n "It being a seperate space gives them the creative freedom to just kinda mess around."
                digi_n "Some problems with the game have already been spotted with this method!"
                jump .chat_topics
            "You keep saying layers...?":
                nvl clear
                you_n "You keep saying \"layers\", {fast}what do you mean by that?"
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
                        digi_n "There, I sent you a link to the {a=https://scp-wiki.wikidot.com/scp-3812}{color=#ff0000}article.{/color}{/a}"
                        digi_n "It's a cool read."
                    "Thank you.":
                        pass

                jump .chat_topics
        
        jump .chat_topics

    label .chat_small:
        nvl clear
        you_n "Aren't you like, small sometimes?{fast}"
        show digi goober
        digi_n "What a thing to ask a person."
        show digi
        digi_n "Yeah, I have a device called the {color=#FFAA00}Height Compressor{/color}."
        digi_n "It lets me get smaller than my default height, and come back."
        you_n "What's your default height?"
        digi_n "Usually I'm #redacted#. Don't tell anyone!"
        you_n "... That was redacted. I couldn't read that."
        show digi happy
        digi_n "I know. I haven't come up with the real answer yet."

        menu (nvl = True):
            "How does the height compressor work?":
                you_n "How does the height compressor work?{fast}"
                show digi thinking
                digi_n "Well, do you mean like, scientifically, or just how I use it?"
                menu (nvl = True):
                    "How you use it.":
                        jump .chat_hc_how
                    "Scientifically.":
                        jump .chat_hc_science
                    "Never mind.":
                        jump .chat_topics
            "{i}Ask about something else":
                jump .chat_topics

    label .chat_hc_how:
        nvl clear
        you_n "How you use it.{fast}"
        digi_n "Well, the height compressor is linked to my brain."
        show digi thinking
        digi_n "Think of it like a neural implant, I suppose."
        show digi
        digi_n "So, in general, I can think about getting smaller..."
        show digi goober:
            zoom 1.0
            linear 2.0 zoom 0.5
        show digi happy
        digi_n "And now I'm smaller!"
        show digi sad
        extend " There's a few caveats, though..."
        show digi goober:
            zoom 0.5
            linear 2.0 zoom 1.0
        show digi
        digi_n "First of all, I'm not always in {i}perfect{/i} control of it."
        digi_n "Since it's linked to what's essentially my subconcious, it can kinda act for me sometimes."
        digi_n "So sometimes I change size before I'm prepared to."
        digi_n "Also, I can't manually override it unless I have a calm mind."
        digi_n "So, if I'm in a stressful situation, or preoccupied with something else, I may not be able to get back to normal size quickly."
        digi_n "All in all though, I love the thing. Worth the tradeoffs."
        jump .chat_topics

    label .chat_hc_science:
        $ mentioned_iris = True
        nvl clear
        you_n "Scientifically.{fast}"
        show digi sad
        digi_n "You're gonna hate the answer for this."
        show digi shock
        digi_n "I have no idea."
        show digi
        digi_n "The height compressor was one of the first things Iris gave me when I showed up in this universe."
        show digi thinking
        digi_n "I've been trying to deconstruct it, figure out how it works..."
        show digi disappointed
        digi_n "It just eludes me, honestly. It's not like any tech I've ever seen."
        show digi
        digi_n "Works a lot better than you can imagine, though. No atomic distortion, no spatial lensing, no cellular decomposition..."
        show digi happy
        digi_n "It's a remarkable device!"
        show digi
        digi_n "I hope I can figure out how it works one day."
        jump .chat_topics

    label .chat_how_are_you:
        nvl clear
        you_n "How are you?{fast}"
        show digi happy
        digi_n "I'm doing alright!"
        show digi
        $ force_hour = 0
        $ hour = datetime.datetime.now().hour if force_hour is None else force_hour
        if 10 <= hour <= 12:
            digi_n "I just woke up, really."
            digi_n "I'm not great in the mornings. I've become {i}somewhat{/i} reliant on caffeine."
            digi_n "Oops! Addictive substance is addictive."
            extend " Hey, it's better than other vices I could have."
            jump .chat_how_are_you_after
        elif 13 <= hour <= 17:
            digi_n "Just been working on some stuff."
            digi_n "The day is still young, you know?"
            extend " I usually am just kinda jumping between a few different projects around this time,"
            digi_n "Good afternoon yourself, by the way."
            jump .chat_how_are_you_after
        elif 18 <= hour <= 22:
            digi_n "Starting to get hungry, though."
            extend " I've been working on stuff all day and kinda forgot to eat..."
            digi_n "I could really go for a burger."
            digi_n "Ugh, do you know how hard it is to get DoorDash up here?"
            jump .chat_how_are_you_after
        elif (23 <= hour <= 24) or (0 <= hour <= 1):
            digi_n "I'm running low on steam but I still have some stuff to get done today."
            digi_n "Just hoping to get some more of the TODO list before I conk out."
            digi_n "Ooh, that's a good point, let me add that to my TODO list."
            # I stole this from the BT1D script, sorry Tate, I don't know how to animate
            show digi_phone flipped with MoveTransition(0.25):
                zoom 0.3
                xpos 0.10
                ypos 0.65
                alpha 0.0
                rotate -15
                parallel:
                    linear 0.25 alpha 1.0
                parallel:
                    linear 0.25 ypos 0.55
            n_n "Digi takes out their phone."
            digi_n "{i}Stop adding so much to my TODO list..."
            hide digi_phone with dissolve
            jump .chat_how_are_you_after
        elif 2 <= hour <= 4:
            digi_n "I'm pretty tired, though."
            digi_n "I need to stop staying up this late."
            digi_n "Hell, {i}you{/i} also probably need to stop staying up this late."
            digi_n "I don't know, I don't know your life."
            digi_n "Clearly I barely know mine."
            jump .chat_how_are_you_after
        else:
            digi_n "I really should be asleep, though."
            digi_n "You should too, by the way. Unless you're usually up this early?"
            digi_n "I don't usually wake up until like 10AM, though, so I'm one to talk about schedules."
            jump .chat_how_are_you_after

    label .chat_how_are_you_after:
        digi_n "How about yourself?"
        menu (nvl = True):
            "I'm doing good!":
                you_n "I'm doing good!{fast}"
                digi_n "That's great to hear!"
                digi_n "It always puts a smile on my face to hear when my friends are doing well."
                digi_n "Honestly, it's probably the thing that uplifts me the most."
            "I'm alright.":
                you_n "I'm alright.{fast}"
                digi_n "That's good to hear!"
                digi_n "Sometimes I think we take 'alright' for granted."
                extend " Any rating over a 5/10 means it's net positive, you know?"
                digi_n "That's good. We should capture that feeling when we get it."
            "I'm mid.":
                you_n "I'm mid.{fast}"
                digi_n "Fair enough."
                digi_n "Whether that's because things are just neutral, or because a bunch of good and bad are in balance, I hope the good outweighs the bad in the end."
            "I'm not doing super great.":
                you_n "I'm not doing super great.{fast}"
                digi_n "Damn, that sucks."
                digi_n "Whatever's got you down, I'm sure things can turn around."
                digi_n "That's a hope I hold on to."
            "I'm doing kinda awful.":
                you_n "I'm doing kinda awful.{fast}"
                digi_n "I'm sorry to hear that."
                digi_n "Hopefully working on this silly visual novel gives you some calm, though."
                digi_n "I may not be real, but Digi{font=cmunrm.ttf}[[0]{/font} is, so do reach out to them if you need the support."
            "I prefer not to say right now.":
                you_n "I prefer not to say right now.{fast}"
                digi_n "And you know what? Valid."
                digi_n "I'm just a pre-written dialogue in a visual novel, anyway."
                digi_n "If you want to talk to Digi{font=cmunrm.ttf}[[0]{/font} about it, though, do reach out."
                extend " They care a lot about you."
        jump .chat_topics

    label .chat_exit:
        digi_n "Alrighty!"
        digi_n "{size=-12}I hope NVL mode worked well..."
        show digi at center with move
        jump .menu

    label .chat_is_weed_legal:
        nvl clear
        you_n "Is weed legal today?{fast}"
        digi_n "I mean, we can check the government website."
        digi_n "Let me pull it up."
        window hide
        call screen isweedlegal()
        if weed_legality():
            digi_n "That's good to hear! This is a weird system."
        else:
            digi_n "Welp, looks like we're out of luck today."

        jump .chat_topics