init python:
    roller = renpy.random.randint(1, 20)

    def reroll():
        global roller
        if preferences.csbounciness == 100:
            roller = 20
        else:
            roller = renpy.random.randint(1, 20)
