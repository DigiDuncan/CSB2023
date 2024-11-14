# Text Beep Spacing
# Partially stolen from:
#   https://www.renpy.org/doc/html/config.html#var-config.replace_text
#   https://lemmasoft.renai.us/forums/viewtopic.php?t=22730
# This is meant to place pauses after certain punctuation automatically so that the dialogue feels more... human.
# Make sure there's a space after your punctuation or it won't work.
# You can still add manual pauses wherever you like in the script if this isn't enough for you.
# If for some reason you do NOT want the auto-pause in a certain line, put {w=0} immediately after the punctuation.
#   Real examples:
#       mean "Hey! You,{w=0} there!"
#       tate "Excuse me, Mr.{w=0} Conductor?"

init python:
    import re
    def substitutions(s):
        # these items wait for 0.25:
        # commas, periods, question marks, exclamation marks, semicolons
        s = re.sub(r'(([,|.|?|!|;])(({\/[a-z]*})*) )', r'\1{w=0.25}', s, flags=re.IGNORECASE) 

        # these items wait for 0.5:
        # ellipses, em-dashes, colons
        s = re.sub(r'((\.\.\.|--|:)(({\/[a-z]*})*) )', r'\1{w=0.5}', s, flags=re.IGNORECASE) 

        # for text effects that are a pain to type out otherwise
        s = s.replace(r"{cshake}", r"{bt=a3-p10-s4}")
        s = s.replace(r"{ytpmagic}", r"{sc=1.88}{color=#CB50FF}")
        s = s.replace(r"{perfect_tate}", r"{sc}{size=+24}{font=azsz}{color=#000000}") # i'd prefer this to be handled in the screen but {sc} breaks it?? - tate

        # awawa mode handling


        return s
    config.say_menu_text_filter = substitutions

# Awawa Mode
# Preserves original text formatting, effects, and punctuation.
# Don't call this directly or you won't have text beep spacing or custom text tags available.
# Special thanks to greyfade for assistance with this!
    def awawa_mode(input_text, frequency = 100):
        awawafication = ""
        awawafied = ""
        next_word = ""
        letter_count = 0

        # look close, it's three groups: tags, whitespace, punctuation, respectively.
        regex_disaster = re.compile("(\{\/*.=*.*?\})+|( |\n)+|([\-\?!@#\$%\^&\*\(\)_\\\.,\/<>\+=\"':;\{\}\[\]~`、。])")

        # split it into pieces
        splitput = regex_disaster.split(input_text)

        # iterate through each
        for item in splitput:

            # ignore blank items
            if item is None:
                pass
            # spit out any tags, whitespace, or punctuation as-is
            elif re.fullmatch(regex_disaster, str(item)):
                awawafication = awawafication + str(item)
            else:
               # only do the replacement according to frequency (default = 100 (always substitute)))
                awawa_chance = frequency / 100
                if renpy.random.random() <= awawa_chance:
                    # if a multi-character string is all-caps, have a 50/50 shot of it just becoming "AAAAAA"
                    if item.isupper() and len(item) > 1:
                        if renpy.random.random() <= 50 / 100:
                            for letter in item:
                                next_word = next_word + "A"
                        else:
                            for letter in item:
                                if letter_count % 2 == 0:
                                    if letter.isupper():
                                        next_word = next_word + "A"
                                    else:
                                        next_word = next_word + "a"
                                else:
                                    if letter.isupper():
                                        next_word = next_word + "W"
                                    else:
                                        next_word = next_word + "w"
                                letter_count = letter_count + 1
                    # handling for all other substitutions: alternate between letters and try to preserve original case.
                    else:
                        for letter in item:
                            if letter_count % 2 == 0:
                                if letter.isupper():
                                    next_word = next_word + "A"
                                else:
                                    next_word = next_word + "a"
                            else:
                                if letter.isupper():
                                    next_word = next_word + "W"
                                else:
                                    next_word = next_word + "w"
                            letter_count = letter_count + 1

                    # if the last character is a w, add an a, respecting the case of the last character.
                    # i don't know why next_word[-1] doesn't just work here without crashing but i guess that's what try/except is for?
                    try:
                        if re.match("w|W", next_word[-1]):
                            if next_word.isupper():
                                next_word = next_word + "A"
                            else:
                                next_word = next_word + "a"
                    except:
                        pass
                    # spit out the new word and reset temp vars for the next word
                    awawafication = awawafication + next_word
                    letter_count = 0
                    next_word = ""
                # leave unaffected words alone
                else:
                    awawafication = awawafication + str(item)

        awawafied = awawafication
        return awawafied
