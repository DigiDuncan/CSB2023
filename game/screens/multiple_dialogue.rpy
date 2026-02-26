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
