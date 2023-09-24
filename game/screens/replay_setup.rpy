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
    Replay_items.append(ReplayItem(["Rthumb1"], "mainmenu_setup", "{color=#000}Gallery button setup{/color}"))
    Replay_items.append(ReplayItem(["Rthumb1"], "main_gallery_images", "{color=#000}Gallery Images{/color}"))
    Replay_items.append(ReplayItem(["Rthumb1"], "gallery_usage", "{color=#000}Making Gallery Images viewable{/color}"))
    Replay_items.append(ReplayItem(["Rthumb1"], "replay_button", "{color=#000}Replay button setup{/color}"))
    Replay_items.append(ReplayItem(["Rthumb1"], "replay_thumb_image", "{color=#000}Replay thumbnail setup{/color}"))
    Replay_items.append(ReplayItem(["Rthumb1"], "replay_list_setup", "{color=#000}Replay list setup{/color}"))
    Replay_items.append(ReplayItem(["Rthumb1"], "finished", "{color=#000}The last bit needed{/color}"))


# a black background screen for the selection
image black = "#000"

#the locked image for the replay gallery if you're using the gallery you can use the same (if you want to)
image replay_locked = "images/replay/replay_lock.jpg"

#384x216 (16x9) set 1280x720p for the lock and thumbnails
#600x338 (16x9) set 1920x1080 for the lock and thumbnails
#replay thumbnails images setup defined here
image Rthumb1 = ("images/replay/replay_unlock.jpg")
