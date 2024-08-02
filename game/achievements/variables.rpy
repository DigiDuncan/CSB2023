default persistent.unlocked_achievements = set()

# Required args:
#   - Achievement name
#   - Description while locked
#   - Description once unlocked
#   - Image icon filename
#   - Category (Acceptable values: "story", "extra")
#       - Use "story" if you can encounter this achievement through normal gameplay, including menu choices.    
#       - Use "extra" if your achievement:
#           - Requires a perfect score on a minigame
#           - Requires any fun value as a prerequisite
#           - Requires the player to do anything else that would not occur naturally through normal gameplay.
# Optional args:
#   - Whether achievement is hidden until unlocked (Default: False)
#   - Whether achivement is DX-new (Default: False)

define achievements = [
    Achievement("ZUP!", "???", "Start the game.", "zup", "extra"),
    Achievement("A Great British Pound", "???", "Enjoy :)", "pound", "extra"),
    Achievement("Overcaffeinated", "???", "Give an old man {i}way{/i} too much energy.", "genergy", "story"),
    Achievement("Ohai, Mark", "???", "Did-- did that reference land?", "mark", "story"),
    Achievement("I Don't Like People!", "Avoid responsibility.", "Tell CS not to go to Walmart.", "no_person", "story"),
    Achievement("Dead Meme", "???", "Sparta kick Wesley.", "sparta", "story"),
    Achievement("#1 Rated Pooper", "???", "Use your skills to keep your job.", "poop", "story"),
    Achievement("Instinctual Editor", "Let your instincts take over.", "This isn't actually Premiere.", "premiere", "extra"),
    Achievement("Crowd Pleaser", "???", "Appease both your fanbases.", "goodrating", "story"),
    Achievement("Can We Go Back?", "???", "Try to go back to Canada.", "compass", "extra"),
    Achievement("Ocean Man", "???", "Go west eight times.", "ocean", "extra"),
    Achievement("Pacifist", "???", "Don't fight.", "pacifist", "story"),
    Achievement("No Mercy", "???", "Try to kill Arceus.", "nomercy", "story"),
    Achievement("Blaster Disaster", "???", "Outrun the JoJites.", "joj", "story"),
    Achievement("You've Been Gnomed", "???", "Hoo!", "gnome", "story"),
    Achievement("Analog Horror Protagonist", "???", "Survive the Michigan woods.", "forest", "story"),
    Achievement("Creepy Clown Sightings", "???", "Meet a bunch of clowns.", "clowns", "story"),
    Achievement("Pencil Sharpening Day!", "Woohoo!", "Beat Digi at pencil sharpening.", "pencil", "story"),
    Achievement("Pencilovania", "???", "Get a perfect pencil sharpening score.", "300", "extra"),
    Achievement("Bored", "Sit through all the car dialogue.", "Sit through all the car dialogue.", "yawn", "story"),
    Achievement("High Roller", "Win a game of Poker.", "Beat Mr. Green at Poker.", "poker","story"),
    Achievement("The House Doesn't Always Win", "???", "Complete the Golden Grin Casino job on the Death Sentence difficulty.", "house", "story"),
    Achievement("Broken Masquerade", "???", "Peer behind the fourth wall.", "ekhi", "story", True),
    Achievement("Guitar Hero", "???", "Unlock a new career by playing Guitar Hero?", "gh", "story"),
    Achievement("Hi, My Name Is...", "Fill in the blank.", "Name your first song.", "hi", "story"),
    Achievement("Singer-Songwriter", "???", "Write your first song.", "songwriter", "story"),
    Achievement("Independent Artist", "???", "Release an EP.", "ep", "story"),
    Achievement("You Rock!", "???", "Complete your tour.", "rockstar", "story"),
    Achievement("The Threadripper", "???", "Beat up the AMD Fans.", "amd", "story"),
    Achievement("NVIDIA Flex", "???", "Beat up the NVIDIA Fans.", "nvidia", "story"),
    Achievement("I Thought This Was A Visual Novel", "Discover what we spent 1000 lines of code on.", "Win your first RPG battle.", "rpg", "story"),
    Achievement("A Little Help From My Friends", "???", "Gather a full party.", "friends", "story"),
    Achievement("Hopes and Dreams", "???", "Beat Copguy EX.", "souls", "story"),
    Achievement("Machine Gun", "???", "Defeat Copguy EX as CS.", "gun", "story"),
    Achievement("Master Chef", "???", "Win over Gordon Ramsay.", "masterchef", "story"),
    Achievement("The Man In The Red Shirt", "???", "Get in a Tom Scott video.", "redshirt", "story"),
    Achievement("Bottom Gear", "???", "Beat the Top Gear crew in a race.", "bottomgear", "story"),
    Achievement("I'm Scared Right Now...", "Acknowledge your roots.", "Meet the creator of Nekopara.", "nekopara", "story"),
    Achievement("Dame Da Ne", "???", "Sing karaoke in Japan.", "karaoke", "story"),
    Achievement("Have Some Fucking Pizza!", "???", "Meet Scott and Miku.", "pizza", "story"),
    Achievement("Grand Dad", "Fleenstones?!", "Meet Joel in Sweden.", "granddad", "story"),
    Achievement("Oak, Pine, And Norsemen", "???", "Escape the IKEA.", "ikea", "story"),
    Achievement("Obviously Grilled", "No, no, that's what I call hamburgers!", "Turn on the Northern Lights.", "steamedhams", "story"),
    Achievement("HoH SiS's Most Wanted", "???", "Complete CSBI.", "csbi", "story"),
    Achievement("Welcome to CSBIII, Mother Fucker", "???", "Complete CSBII.", "csbii", "story"),
    Achievement("That's All, Folks!", "???", "Complete CSBIII.", "csbiii", "story"),
    Achievement("Boingy Boingy Boingy", "???", "Max out CSBounciness and get an ending.", "max_bounce", "extra"),
    Achievement("Artifical Unintelligence", "???", "Get the Chat-GPT ending.", "gpt", "story", True),
    Achievement("All Over Again", "???", "Beat CSBIII all over again.", "alloveragain", "extra", True),
    Achievement("F.U.N.", "???", "Roll a fun value.", "fun", "extra", True),
    Achievement("Archived", "???", "Find Addy's Facility.", "archive", "extra", True),
    Achievement("Chronicle Skipper 188", "Think you can you set a new record?", "Stay home and speedrun this game!", "speedrun", "story", dx = True),
    Achievement("Get The Job Done Right", "The first time...", "Call the right company.", "savers", "extra", dx = True),
    Achievement("Graphite Grinder", "Sharpening Time 2", "Beat the Pencil Cultist's high score.", "grinder", "story", dx = True),
    Achievement("60 Drillless WR", "Your wrist hurts.", "Get a perfect score of 1200.", "1200","extra", dx = True),
    Achievement("We Don't Go To Bronson", "???", "Welcome to Hell!",  "bronson", "story", dx = True),
    Achievement("Wacka Wacka DooDoo Yeah!", "Find the legendary fun value in Country route.", "Find the legendery fun value in Country route.", "albu", "extra", dx = True),
    Achievement("Lots & Lots Of Trains!", "Aren't they just adorable?", "Play with some model trains.", "train", "story", dx = True),
    Achievement("Conductor Skillz 188", "No health potions here.", "Win the train game with full health.", "train_healthy", "extra", dx = True),
    Achievement("Main Character Syndrome", "Remind them whose game this is.", "Defeat Tate EX.", "vs-tate", "extra", dx = True),
    Achievement("All Aboard!", "???", "Complete Train Route.", "amtrak", "story", dx = True),
    Achievement("Gotta Catch Them All", "Collect every bio.", "Collect every bio.", "bios", "extra"),
    Achievement("The Brown Album", "Collect every song in the jukebox.", "Collect every song in the jukebox.", "juke", "extra"),
    Achievement("Fin.", "Collect all the endings.", "Collect all the endings.", "end", "extra")
]
