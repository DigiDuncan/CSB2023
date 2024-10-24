## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.
init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (3 + 1)

    minigame_page = 0

    class MinigameItem:
        def __init__(self, thumbs, replay, name):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name

        def num_minigame(self):
            return len(self.thumbs)

    #add replay items here format below
    #Replay_items.append(ReplayItem(["the thumbnail"], "the_label_from_code", "brief description"))
    Minigame_items = []
    Minigame_items.append(MinigameItem(["EditGame"], "play_edit_game", "{outlinecolor=#000000}{color=#EA71FF}Editing Game{/color}{/outlinecolor}"))
    Minigame_items.append(MinigameItem(["CarGame"], "play_car_game", "{outlinecolor=#000000}{color=#D4FF43}Car Game{/color}{/outlinecolor}"))
    Minigame_items.append(MinigameItem(["PencilGame"], "play_pencil_game", "{outlinecolor=#000000}{color=#FFCA00}Pencil Game{/color}{/outlinecolor}"))
    Minigame_items.append(MinigameItem(["SlotsGame"], "play_slots_game", "{outlinecolor=#000000}{color=#518EFF}Slots Game{/color}{/outlinecolor}"))
    Minigame_items.append(MinigameItem(["Pencil2Game"], "play_pencil2_game", "{outlinecolor=#000000}{color=#FF7E7E}Pencil Game 2{/color}{/outlinecolor}"))

# Images are going to be 600 x 338
#replay thumbnails images setup defined here
image EditGame = ("images/replay/edit_game.png")
image CarGame = ("images/replay/car_game.png")
image PencilGame = ("images/replay/pencil_game.png")
image SlotsGame = ("images/replay/slots_game.png")
image Pencil2Game = ("images/replay/pencil2_game.png")
