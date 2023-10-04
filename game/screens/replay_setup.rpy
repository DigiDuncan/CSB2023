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
    Replay_items.append(ReplayItem(["Hotwire"], "hotwire", "{outlinecolor=#000000}{color=#FF0000}Grand Theft Failure{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Revenge"], "fighthohsis", "{outlinecolor=#000000}{color=#FF0000}Catch These Shitty Hands{/outlinecolor}{/color}"))
    Replay_items.append(ReplayItem(["FuckUp"], "fuckuphohsis", "{outlinecolor=#000000}{color=#FF0000}RIP House{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Brag"], "braghohsis", "{outlinecolor=#000000}{color=#FF0000}RIP Money{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["FuckingDonkey"], "bad_ramsay", "{outlinecolor=#000000}{color=#FF0000}You Fucking Donkey{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["TopLoser"], "top_lose", "{outlinecolor=#000000}{color=#FF0000}Top Loser{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Scottnt"], "scott_movent", "{outlinecolor=#000000}{color=#FF0000}Scottn't{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Misfortune"], "no_contract", "{outlinecolor=#000000}{color=#FF0000}Threw Away Fame{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["GrandDad"], "flint_car", "{outlinecolor=#000000}{color=#FF0000}GRAND DAD{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Premature"], "cops_ltt", "{outlinecolor=#000000}{color=#FF0000}Premature Lore Dumper{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["GodFail"], "attack_arc", "{outlinecolor=#000000}{color=#FF0000}God Fail{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["GodSuccess"], "wait_arc", "{outlinecolor=#000000}{color=#FF0000}God Success{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Attorney"], "bad_convince", "{outlinecolor=#000000}{color=#FF0000}Attorney's Badge{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["BadDriver"], "lose_car_game", "{outlinecolor=#000000}{color=#FF0000}Bad Driver{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["PencilShart"], "lose_pencil_game", "{outlinecolor=#000000}{color=#FF0000}Pencil Sharting Day!{/color}{/outlinecolor}"))
    # Like 4 endings use the same fucking screen
    Replay_items.append(ReplayItem(["CopCall"], "copsathohsis", "{outlinecolor=#000000}{color=#00FF00}Call The Cops{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["CopCall"], "true_ending", "{outlinecolor=#000000}{color=#00FF00}True Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["CopCall"], "ytp_ending", "{outlinecolor=#000000}{color=#00FF00}YTP Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["CopCall"], "ltt_ending", "{outlinecolor=#000000}{color=#00FF00}LTT Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Archival"], "archival", "{outlinecolor=#000000}{color=#AA00CC}Archival Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["AIEnd"], "csbiii_ai", "{outlinecolor=#000000}{color=#AA00CC}AI Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["LegoLTT"], "lego_ending", "{outlinecolor=#000000}{color=#00FF00}Lego Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["LegoLTT"], "ltt_ending_alt", "{outlinecolor=#000000}{color=#00FF00}LTT Ending ALT{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["BrokenReality"], "reality_break", "{outlinecolor=#000000}{color=#AA00CC}Broken Reality{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["Rockstar"], "final_tour_bus", "{outlinecolor=#000000}{color=#00FF00}Rockstar{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["FriendEnd"], "car_slam", "{outlinecolor=#000000}{color=#FFCC00}Friend Ending{/color}{/outlinecolor}"))
    Replay_items.append(ReplayItem(["CountryEnd"], "going_home", "{outlinecolor=#000000}{color=#0000FF}Country Ending{/color}{/outlinecolor}"))
    
    
    



# a black background screen for the selection
image black = "#5F777F"

#the locked image for the replay gallery if you're using the gallery you can use the same (if you want to)
image replay_locked = "images/replay/replay_lock.jpg"

# Images are going to be 600 x 338
#replay thumbnails images setup defined here
image Asylum = ("images/replay/asylum_bad.png")
image Hotwire = ("images/replay/hotwire_bad.png")
image Revenge = ("images/replay/revenge.png")
image FuckUp = ("images/replay/riphouse.png")
image Brag = ("images/replay/ripmoney.png")
image FuckingDonkey = ("images/replay/fuckinraw.png")
image TopLoser = ("images/replay/toploser.png")
image Scottnt = ("images/replay/scottnt.png")
image Misfortune = ("images/replay/misfortune.png")
image GrandDad = ("images/replay/granddad.png")
image Premature = ("images/replay/premature.png")
image GodFail = ("images/replay/godfail.png")
image GodSuccess = ("images/replay/godsuccess.png")
image Attorney = ("images/replay/attorney.png")
image BadDriver = ("images/replay/baddriver.png")
image PencilShart = ("images/replay/pencilshart.png")
image CopCall = ("images/replay/callthecops.png")
image Archival = ("images/replay/archival.png")
image AIEnd = ("images/replay/aiend.png")
image LegoLTT = ("images/replay/legoltt.png")
image BrokenReality = ("images/replay/realitybreak.png")
image Rockstar = ("images/replay/rockstar.png")
image FriendEnd = ("images/replay/friendending.png")
image CountryEnd = ("images/replay/countryend.png")