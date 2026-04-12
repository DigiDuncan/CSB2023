init python:
    renpy.music.register_channel("beep", "voice", loop = True)
    def char_callback(event, name = None, beep = None, play_beeps = True, interact = True, **kwargs):
        if event == "end" and "woohoo" in kwargs["what"].lower():
            persistent.woohoo += 1
        if name:
            persistent.seen.add(name)
            if all([a in persistent.seen for a in NAME_MAP.keys()]):
                achievement_manager.unlock("bios")
        if preferences.text_beeps and play_beeps:
            if event == "show":
                if beep is not None:
                    if isinstance(beep, str):
                        renpy.sound.play(f"audio/text/{beep}.wav", channel = "beep", loop = True)
                    elif isinstance(beep, (list, tuple)):
                        renpy.sound.stop("beep")
                        for _ in range(30):
                            beep_choice = renpy.random.choice(beep)
                            renpy.sound.queue(f"audio/text/{beep_choice}.wav", channel = "beep")
                else:
                    renpy.sound.play(f"audio/text/ut.wav", channel = "beep", loop = True)
            elif event == "slow_done" or event == "end":
                renpy.sound.stop(channel = "beep")
