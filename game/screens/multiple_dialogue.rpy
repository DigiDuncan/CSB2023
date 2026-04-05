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

    $ total_chars = len(blocks)

    window:
        id "window"

        for idx, block in enumerate(blocks):
            $ char = block[0]
            $ what = block[1]
            $ name = substitutions(char.name)

            window:
                yoffset 75 * idx
                xoffset 125 * idx
                id "namebox"
                style "namebox"
                text name id "who"

            text what id "what"