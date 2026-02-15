init -10 python:
    ########## DUSK SHADER
    duskmatrix = TintMatrix("#ffaa49")

    def shade_dusk(s):
        return Transform(s, matrixcolor = duskmatrix)

    def shade_dusk_flip(s):
        return Transform(s, xzoom = -1, matrixcolor = duskmatrix)

    config.displayable_prefix["dusk"] = shade_dusk
    config.displayable_prefix["dusk:flip"] = shade_dusk_flip

    ########## DARK SHADER
    darkmatrix = TintMatrix("#4848b8")

    def shade_dark(s):
        return Transform(s, matrixcolor = darkmatrix)

    def shade_dark_flip(s):
        return Transform(s, xzoom = -1, matrixcolor = darkmatrix)

    config.displayable_prefix["dark"] = shade_dark
    config.displayable_prefix["dark:flip"] = shade_dark_flip

    ########## WHITE SILHOUETTE SHADER
    sil_white_matrix = BrightnessMatrix(value=1.0)

    def sil_white(s):
        return Transform(s, xzoom = 1, matrixcolor = sil_white_matrix)

    def sil_white_flip(s):
        return Transform(s, xzoom = -1, matrixcolor = sil_white_matrix)

    config.displayable_prefix["sil_white"] = sil_white
    config.displayable_prefix["sil_white:flip"] = sil_white_flip

    ########## BLACK SILHOUETTE SHADER
    sil_black_matrix = BrightnessMatrix(value=-1.0)

    def sil_black(s):
        return Transform(s, xzoom = 1, matrixcolor = sil_black_matrix)

    def sil_black_flip(s):
        return Transform(s, xzoom = -1, matrixcolor = sil_black_matrix)

    config.displayable_prefix["sil_black"] = sil_black
    config.displayable_prefix["sil_black:flip"] = sil_black_flip

    ########## SEPIA FILTER
    def shade_sepia(s):
        return Transform(s, xzoom = 1, matrixcolor = SepiaMatrix())

    def shade_sepia_flip(s):
        return Transform(s, xzoom = 1, matrixcolor = SepiaMatrix())

    config.displayable_prefix["sepia"] = shade_sepia
    config.displayable_prefix["sepia:flip"] = shade_sepia_flip

    ########## YELLOW SELECTABLE FILTER
    # Full disclosure: this one single line was partially-written by AI.
    sil_select_matrix = ColorizeMatrix("#808000","#FFFFFF")

    def shade_select(s):
        return Transform(s, xzoom = 1, matrixcolor = sil_select_matrix)

    def shade_select_flip(s):
        return Transform(s, xzoom = 1, matrixcolor = sil_select_matrix)

    config.displayable_prefix["selectable"] = shade_select
    config.displayable_prefix["selectable:flip"] = shade_select_flip

    ########## SPRITE FLIPPER
    def xflip(s):
        return Transform(s, xzoom = -1)

    config.displayable_prefix["flip"] = xflip
