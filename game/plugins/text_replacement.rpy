init python:
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

        return s
    config.say_menu_text_filter = substitutions
