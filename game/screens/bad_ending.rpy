screen bad_ending(text = "Why'd you do that?"):
    modal True
    on "show" action Play("sound", ["<silence 0.15>", "audio/sfx/sfx_bad_ending.ogg"])
    key "dismiss" action Return()
    
    frame:
        background None
        xsize 3000

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
                linear 0.25 rotate -17
            
        add "gui/bad_poop.png":           
            at transform:
                matrixcolor sil_black_matrix
                xalign 0.5 yalign 0.5
                xoffset 34 yoffset 34

                block:
                    linear 0.25 xzoom 1.0
                    ease_bounce 0.125 xzoom 3.0
                    ease_bounce 0.125 xzoom 0.8
                    ease_bounce 0.125 xzoom 1.0

        add "gui/bad_poop.png":           
            at transform:
                xalign 0.5 yalign 0.5
                
                block:
                    linear 0.25 xzoom 1.0
                    ease_bounce 0.125 xzoom 3.0
                    ease_bounce 0.125 xzoom 0.8
                    ease_bounce 0.125 xzoom 1.0

        text _("BAD ENDING"):
            xalign 0.5 yalign 0.4 text_align 0.5
            font gui.name_text_font
            size 188*2
            color "#FFFFFF"
            outlines [ (absolute(18), "#000", 9, 9) ]
        
        text text:
            slow_cps preferences.text_cps/2
            color "#FFFFFF"
            size 150
            outlines [(absolute(10), "#000", absolute(0), absolute(0))]
            at transform:
                xalign 0.5 yalign 1.0