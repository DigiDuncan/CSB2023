### EXPERIMENTAL LAYERED SPRITE, DO NOT USE THIS YET ### 

# KNOWN ISSUES:
# optional items must be removed manually. ex tate_comp blush -> tate_comp -blush
# you can't swap expressions on the fly, you have to manually change each thing
# shaders and flip sprite do not work and i don't know if they CAN work

layeredimage tate_comp:
    
    group outfit:
        attribute outfit default:
            "/characters/tate/composite_test/body_default.png"
        attribute festive:
            "/characters/tate/composite_test/body_festive.png"

    group extra1:
        attribute blush:
            "/characters/tate/composite_test/blush.png"

    group face:
        attribute happy default:
            "/characters/tate/composite_test/face_happy.png"
        attribute sad:
            "/characters/tate/composite_test/face_sad.png"
        attribute sheepish:
            "/characters/tate/composite_test/face_sheepish.png"
        attribute shock:
            "/characters/tate/composite_test/face_shock.png"
        attribute serious:
            "/characters/tate/composite_test/face_serious.png"
        attribute smug:
            "/characters/tate/composite_test/face_smug.png"
        attribute stare:
            "/characters/tate/composite_test/face_stare.png"

    group extra2:
        attribute tears:
            "/characters/tate/composite_test/tears.png"

label awawa_tate_composite_test:
    
    tate "Awawa!"
    tate "Let's see if this works!"
    show tate_comp
    "Default"
    show tate_comp sad
    "Sad"
    show tate_comp sad tears
    "Sad + tears"
    show tate_comp sheepish -tears
    "Sheepish"
    show tate_comp sheepish blush
    "Sheepish + blushing"
    show tate_comp shock -blush
    "Shock"
    show tate_comp serious
    "Serious"
    show tate_comp smug
    "Smug"
    show tate_comp stare
    "Stare"

    show tate_comp festive
    "Festive!"
    show tate_comp sad festive
    "Sad Festive"
    show tate_comp sad tears festive
    "Sad + tears + Festive"
    show tate_comp sheepish -tears festive
    "Sheepish + Festive"
    show tate_comp sheepish blush festive
    "Sheepish + blushing + Festive"
    show tate_comp shock -blush festive
    "Shock + Festive"
    show tate_comp serious festive
    "Serious + Festive"
    show tate_comp smug festive
    "Smug + Festive"
    show tate_comp stare festive
    "Stare + Festive"

    tate "Shader test!"
    
    show tate_comp
    "Normal"
    show tate_comp dusk
    "Dusk"
    show tate_comp dark
    "Dark"
    show tate_comp sil_white
    "White"
    show tate_comp sil_black
    "Black"
    show tate_comp flipped
    "Also, let's flip!"

    show tate sheepish

    tate "Did {i}any{/i} of that work?"

    
