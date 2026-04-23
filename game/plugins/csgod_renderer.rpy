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

        sprite = "images/characters/cs/csgod/"+active_expr+".png"

        # Get canvas size / buffer
        canvas = renpy.image_size(sprite)
        canvas = [c + glow_intensity * 2 for c in canvas]

        expanded = Composite(canvas, [glow_intensity * 2, 0], sprite)

        # Create the pieces
        glow_layer =  At(
            expanded, 
            Transform(
                subpixel=True, 
                matrixcolor=TintMatrix("#FF00FF") * BrightnessMatrix(1.0), 
                blur=glow_intensity, 
                xzoom=flip,
                xanchor=0.5, yanchor=1.0   
            )
        )
        
        base_layer = At(
            expanded,  
            Transform(
                subpixel=True, 
                xzoom=flip,
            )
        )

        # Put them together
        return Fixed(
            Frame(glow_layer),
            Frame(base_layer),
            subpixel=True,
            xsize=canvas[0], ysize=canvas[1],
            xanchor=0.5, yanchor=1.0   
        )
