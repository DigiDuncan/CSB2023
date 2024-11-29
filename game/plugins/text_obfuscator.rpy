init python:
    # TODO: I want to replicate the minecraft obfuscation thing for later. for now, this DOES do the thing

    def obfuscator(input_text):
        ob = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        new_text = ""
        next_char = ""

        for l in input_text:
            # 1 in 5 chance of replacing letter with a question mark
            if renpy.random.randint(1, 5) == 1:
                next_char = "?"
            else:
                next_char = renpy.random.choice(ob)

            new_text = new_text + next_char

        return "{font=REDACTED-REGULAR.TTF}"+new_text
