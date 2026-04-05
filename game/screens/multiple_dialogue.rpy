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

            python:
                last_name_width = 0
                separator_y = 0
                for i in range(0, idx):
                    last_name_width += get_size(Text(substitutions(blocks[i][0].name), style = "namebox_label", font = gui_theme_map["name_font"]))[0] + int(gui_theme_map["dialogue_namebox_xspacing"])
                                
                    if preferences.dyslexia_mode:
                        separator_y = get_size("window")[1]/2 + gui.text_size * idx           
                    else:
                        separator_y = get_size("window")[1]/2 + gui.text_size * idx 

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
                    xalign 0.5 yoffset separator_y
                    background gui.text_color