init -2 python:
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

        # Get canvas size
        canvas = get_size("images/characters/cs/csgod/neutral.png")

        # Create the pieces
        glow_layer = At("images/characters/cs/csgod/"+active_expr+".png", Transform(subpixel=True, matrixcolor=TintMatrix("#FF00FF") * BrightnessMatrix(1.0), blur=glow_intensity, xzoom=flipped))
        base_layer = At("images/characters/cs/csgod/"+active_expr+".png",  Transform(subpixel=True, xzoom=flipped))

        return Image(
            Composite(
                (canvas[0] + glow_intensity + 20, canvas[1] + glow_intensity + 20),
                (0, 0), glow_layer,
                (0, 0), base_layer   
            )     
        )
