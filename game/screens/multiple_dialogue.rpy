screen multiple_say(who, what, multiple):
    style_prefix "say"

    $ block = multiple[0] - 1
    $ total_chars = multiple[1]  # Unused rn

    window:
        id "window"
        yoffset 75 * block

        if who is not None:

            $ new_who = substitutions(who)

            window:
                yoffset -75 * block
                xoffset 125 * block
                id "namebox"
                style "namebox"
                text new_who id "who"

        text what id "what"


screen digimultiple(blocks):
    zorder 5
    style_prefix "say"

    $ total_chars = len(blocks)

    window:
        id "window"
        style "window"

        for idx, block in enumerate(blocks):
            $ char = block[0]
            $ what = substitutions(block[1])
            $ name = substitutions(char.name)

            $ last_name_width = len(name)*gui.text_size * idx # TODO: this math is wrong
            $ print(last_name_width)

            window:
                id "namebox"
                style "namebox"
                xoffset last_name_width
                        
                text name id "who":
                    style "namebox_label"
                    font gui_theme_map["name_font"]
   
            text substitutions(what):
                id "what"
                style "say_dialogue"
                yoffset gui.text_size * idx

                slow_cps preferences.text_cps

            if idx < len(blocks) and idx > 0:
                frame:
                    xsize 0.6125 ysize 1
                    xalign 0.5 yoffset get_size("window")[1]/2 + gui.text_size * idx
                  
                    background gui.text_color
                
                
                
