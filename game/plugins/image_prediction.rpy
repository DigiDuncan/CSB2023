# An assortment of image prediction functions.
# Use these when loading lots of images (like, more than 100) at once.
# Examples: Item Collection, UCN2 background selection
# Now, you may be thinking:
#   Tate, why put these one-liners into functions?
#   They're already one line??
# This is done so they can run in the background of a screen without hanging!

init python:

    # These ones do NOT preload images.
    # They in the background as a "hint". Run one of these first!

    # Give this one a LIST of images.
    def start_predict_list(img_list):
        for img in img_list:
            renpy.start_predict(img)

    # Give this one a SINGLE image.
    def start_predict_single(img):
        renpy.start_predict(img)

    # Predict a single image.
    # Use it in a loop to predict many images.
    def predict_img(img):
        renpy.predict(img)
