init python:
    roller = renpy.random.randint(1, 20)

    def reroll():
        global roller
        if preferences.cs_bounciness == 100:
            roller = 20
        else:
            roller = renpy.random.randint(1, 20)
