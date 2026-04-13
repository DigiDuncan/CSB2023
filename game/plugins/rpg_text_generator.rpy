init python:
    def generate_rpg_text(text:str, size = 50, text_color = "#FFF", outline_color = "#000"):
        return Text(text, text_align=0.5, color=text_color, outlines=[ (absolute(2.25), outline_color, absolute(0), absolute(0)) ], font_size=size)