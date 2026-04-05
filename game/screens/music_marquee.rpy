screen music_marquee():
    $ song = get_now_playing()
    if song:
        hbox:
            add "gui/inline_text/note2.png"
            if not preferences.craptop_mode:
                marquee:
                    xsize 1900 ysize 70
                    animation marquee_pan(10.0)
                    always_animate True
                    frame:
                        background None
                        xsize 1900
                        text _("{font=music_text}[song[0]] - [song[1]]    ")
            else:
                frame:
                    background None
                    xsize 1900
                    text _("{font=music_text}[song[0]] - [song[1]]    ")