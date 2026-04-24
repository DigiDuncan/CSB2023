init python:
    def csgod_sprite(expression = "neutral", glow_intensity = 5, flipped=False):

        # Face handling
        valid_expr = [ 
            "angry",
            "concentrate",
            "disappointed",
            "happy",
            "neutral",
            "pissed",
            "scared",
            "surprised",
            "worried"
        ]

        if expression in valid_expr:
            active_expr = expression
        else:
            active_expr = "neutral"

        # Flip handling
        if flipped:
            flip = -1
        else:
            flip = 1

        sprite = Image("images/characters/cs/csgod/"+active_expr+".png", optimize_bounds=False, mesh=True, mesh_pad=(glow_intensity, glow_intensity))

        # Get canvas size / buffer
        canvas = renpy.image_size(sprite)

        # Put them together
        return Fixed(
            At(sprite, Transform(xzoom=flip, matrixcolor=TintMatrix("#FF00FF") * BrightnessMatrix(1.0), blur=glow_intensity)),
            At(sprite, Transform(xzoom=flip)),
            subpixel=True,
            xsize=canvas[0], ysize=canvas[1],
            xanchor=0.5, yanchor=1.0   
        )