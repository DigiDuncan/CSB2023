<<<<<<< Updated upstream
# Custom preferences
default persistent.text_beeps = True
=======
init python:
    if persistent.csbounciness is None:
        persistent.csbounciness = 0
>>>>>>> Stashed changes

label start:
    scene black
    menu:
        "Start where?"

        "CSBounciness I":
            jump csbi_start
        "CSBounciness II":
            jump csbii_start
