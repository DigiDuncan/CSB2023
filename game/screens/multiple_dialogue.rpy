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
    $ last_name_width = get_size("namebox")[0]

    window:
        id "window"
        style "window"

        for idx, block in enumerate(blocks):
            $ char = block[0]
            $ what = substitutions(block[1])
            $ name = substitutions(char.name)

            $ last_name_width = get_size("namebox")[0]

            window:
                id "namebox"
                style "namebox"

                if idx > 0:
                    xoffset last_name_width
                    # yoffset 75 * idx
                
                text name id "who":
                    style "namebox_label"
                    font gui_theme_map["name_font"]
   
            text substitutions(what):
                id "what"
                style "say_dialogue"
                yoffset 50 * idx

                slow_cps preferences.text_cps
                
                
                
