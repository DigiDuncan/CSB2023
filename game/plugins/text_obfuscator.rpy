init python:
    # TODO: I want to replicate the minecraft obfuscation thing for later. for now, this DOES do the thing

    def obfuscator(input_text):

        # commenting all this out until DX due to size issues
        # ob = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        # new_text = ""
        # next_char = ""

        # for l in input_text:
            # # 1 in 5 chance of replacing letter with a question mark
            # if renpy.random.randint(1, 5) == 1:
                # next_char = "?"
            # else:
                # next_char = renpy.random.choice(ob)

            # new_text = new_text + next_char

        new_text = ""
        next_char = ""

        for l in input_text:
            if l == " ":
                next_char = " "
            else:
                next_char = "?"

            new_text = new_text + next_char

        return "{color=#7F7F7F}"+new_text
