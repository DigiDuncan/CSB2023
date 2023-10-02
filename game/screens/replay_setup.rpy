## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.
init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (3 + 1)

    replay_page = 0

    class ReplayItem:
        def __init__(self, thumbs, replay, name):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name

        def num_replay(self):
            return len(self.thumbs)

    #add replay items here format below
    #Replay_items.append(ReplayItem(["the thumbnail"], "the_label_from_code", "brief description"))
    Replay_items = []
    Replay_items.append(ReplayItem(["Asylum"], "asylum", "{outlinecolor=#000000}{color=#FF0000}Asylum Ending{/color}{/outlinecolor}"))


# a black background screen for the selection
image black = "#5F777F"

#the locked image for the replay gallery if you're using the gallery you can use the same (if you want to)
image replay_locked = "images/replay/replay_lock.jpg"

# Images are going to be 600 x 338
#replay thumbnails images setup defined here
image Asylum = ("images/replay/asylum_bad.png")