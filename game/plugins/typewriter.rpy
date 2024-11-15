init python:
    import math

    def show_typewriter(st, at):
        if st > 2.0:
            return Text(typewriter_text, textalign = 0.5, size = 100, outlines=[(absolute(10), "#000", absolute(0), absolute(0))]), 0.1
        else:
            d = Text(typewriter_text[:math.ceil((st / 2.0) * len(typewriter_text))], textalign = 0.5, size = 100, outlines=[(absolute(10), "#000", absolute(0), absolute(0))])
            return d, 0.1

default typewriter_text = "Hello, world!"
image typewriter = DynamicDisplayable(show_typewriter)
