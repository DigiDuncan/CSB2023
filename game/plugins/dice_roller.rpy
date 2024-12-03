init python:
    d20 = renpy.random.randint(1, 20)

    def reroll():
        global d20
        if preferences.csbounciness == 100:
            d20 = 20
        else:
            d20 = renpy.random.randint(1, 20)
