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
    style_prefix "say"
    zorder 5

    key "dismiss" action [
        Hide("digimultiple"),
        Return()
    ]
    if config.skipping:
        timer 0.01 action Return()

    $ total_chars = len(blocks)

    window:
        id "window"
        style "window"

        for idx, block in enumerate(blocks):
            python:
                if what and what != "None":
                    char = block[0]
                    what = substitutions(block[1])
                    if isinstance(char, str):
                        name = substitutions(char)
                    else:
                        name = substitutions(char.name)

            python:
                last_name_width = 0
                for i in range(0, idx):
                    if isinstance(blocks[i][0], str):
                        check_name = blocks[i][0]
                        if check_name == "None":
                            continue
                    else:
                        check_name = blocks[i][0].name
                    last_name_width += get_size(Text(substitutions(check_name), style = "namebox_label", font = gui_theme_map["name_font"]))[0] + int(gui_theme_map["dialogue_namebox_xspacing"])

            window:
                id "namebox"
                style "namebox"
                xoffset last_name_width
                        
                text name id "who":
                    style "namebox_label"
                    font gui_theme_map["name_font"]
   
        vbox:
            style "say_dialogue"
            
            for idx, block in enumerate(blocks):
                text substitutions(block[1]):
                    id "what"
                    slow_cps preferences.text_cps

                if idx != len(blocks) - 1:
                    add get_themed_attribute("multiple_separator")

python early:
    def parse_multiple(lexer):
        block = lexer.subblock_lexer()
        r = []
        while block.advance():
            name = block.simple_expression()
            text = block.rest()
            r.append((name, text))
        return r

    def lint_multiple(parsed_object):
        ...

    def execute_multiple(parsed_object):
        print("Hey, I'm the multiple dialogue parser.")
        print("Here's what I got for ya:")
        print(parsed_object)

        rr = []
        for char_name, text in parsed_object:
            text = text.strip("\"")
            if char_name.startswith("\""):
                rr.append((char_name.strip("\""), text))
            else:
                character_object = globals().get(char_name, None)
                if character_object and isinstance(character_object, ADVCharacter):
                    rr.append((character_object, text))
                else:
                    rr.append((char_name, text))

        for block in rr:
            char = block[0]
            what = substitutions(block[1])
            if isinstance(char, str):
                name = substitutions(char)
            else:
                name = substitutions(char.name)
            narrator.add_history(kind="adv", who=name, what=what)

        renpy.hide_screen("say", immediately=True)
        renpy.call_screen("digimultiple", rr)

    renpy.register_statement(name="multiple",
        block=True,
        parse = parse_multiple,
        lint = lint_multiple,
        execute = execute_multiple)
