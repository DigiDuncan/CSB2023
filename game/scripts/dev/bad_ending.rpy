screen bad_ending(text = "Why'd you do that?"):
    modal True

    $ global typewriter_text 
    $ typewriter_text = text
    $ renpy.sound.play("audio/sfx/sfx_bad_ending.ogg", "sound", loop=False) # TODO: why does this play twice?

    frame:
        background None

        at transform:
            zoom 2.0
            xanchor 0.5 yanchor 0.55
            xpos 0.5 ypos 0.5
            alpha 0
            
            parallel:
                linear 0.25 zoom 0.5
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 rotate -15
            
        add "gui/bad_poop.png":           
            at transform:
                matrixcolor sil_black_matrix
                xalign 0.325 yalign 0.425

        add "gui/bad_poop.png":           
            at transform:
                xalign 0.5 yalign 0.5
                
                block:
                    linear 0.25 xzoom 1.0
                    ease_bounce 0.125 xzoom 3.0
                    ease_bounce 0.125 xzoom 1.0

        text _("BAD ENDING"):
            xalign 0.5 yalign 0.3
            font "fonts/impact.ttf"
            size 188*2
            color "#FFFFFF"
            outlines [ (absolute(18), "#000", absolute(0), absolute(0)) ]
        
        add DynamicDisplayable(show_typewriter): # TODO: this doesn't display the input text
            at transform:
                xalign 0.5 yalign 1.0
    
                    