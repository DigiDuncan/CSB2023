init python:
    roller = renpy.random.randint(1, 20)

    def reroll():
        global roller
        roller = renpy.random.randint(1, 20)
