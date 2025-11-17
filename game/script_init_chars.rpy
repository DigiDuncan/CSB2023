# Character Definitions

# Generic Character Definitions
define n = Character(None, what_italic = True, callback = char_callback)  # Narrator
define chat = Character("Chat", callback = char_callback)
define unknown = Character("???", callback = char_callback)

# CS' Various Character Definitions
define cs = Character("cs188", callback = renpy.partial(char_callback, name = "cs", beep = "cs"))
define cs_fakegod = Character("cs188 (pretending to be CSGod)", callback = renpy.partial(char_callback, name = "cs", beep = "csgod"))
define csgod = Character("CSGod", callback = renpy.partial(char_callback, name = "csgod", beep = "csgod"), what_color="#CB50FF")
define ycs = Character("Young CS", callback = renpy.partial(char_callback, beep = "ycs"))

# CSBI Character Definitions (Including HoH SiS)
define carguy = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", beep = "nice"))
define carguy_nobeep = Character("Carguy", callback = renpy.partial(char_callback, name = "carguy", play_beeps = False))
define cashier = Character("Cashier", callback = renpy.partial(char_callback, name = "cashier"))
define craptop = Character("Craptop", callback = renpy.partial(char_callback, name = "craptop"))
define discord = Character("Discord", callback = char_callback)
define doug = Character("Doug", callback = renpy.partial(char_callback, name = "doug", beep = "doug"))
define greeter = Character("Greeter", callback = renpy.partial(char_callback, name = "doug", beep = "doug"))
define michael = Character("Michael", callback = renpy.partial(char_callback, name = "michael", beep = "mich"))
define michael_nobeep = Character("Michael", callback = renpy.partial(char_callback, name = "michael", play_beeps = False))
define phil = Character("Phil", callback = renpy.partial(char_callback, name = "phil", beep = "phil"))
define sticky = Character("Sticky Note", callback = renpy.partial(char_callback, name = "sticky"))
## HoH SiS
define ed = Character("Ed", callback = renpy.partial(char_callback, name = "ed", beep = "ed"))
define hoh_operator = Character("HoH SiS Operator", callback = char_callback)
define rich = Character("Richard", callback = renpy.partial(char_callback, name = "rich", beep = "rich"))
define wesley = Character("Wesley", callback = renpy.partial(char_callback, name = "wesley", beep = "wes"))
define worker_1 = Character("Worker 1", callback = char_callback)
define worker_2 = Character("Worker 2", callback = char_callback)
define worker_3 = Character("Worker 3", callback = char_callback)
define worker_4 = Character("Worker 4", callback = char_callback)
define worker_5 = Character("Worker 5", callback = char_callback)
define worker_6 = Character("Worker 6", callback = char_callback)
define worker_7 = Character("Worker 7", callback = char_callback)

# CSBII Character Definitions
define asylum_worker = Character("Mr. Mohs", callback = renpy.partial(char_callback, name = "mohs"))
define border_guard = Character("Border Guard", callback = renpy.partial(char_callback, name = "border_guard"))
define copguy = Character("Copguy", callback = renpy.partial(char_callback, name = "copguy", beep = "cop"))
define linus = Character("Linus", callback = renpy.partial(char_callback, name = "linus", beep = "ltt"))

# CSBIII Part 1 Character Definitions
define colton = Character("Colton", callback = renpy.partial(char_callback, name = "colton"))
define luke = Character("Luke", callback = renpy.partial(char_callback, name = "luke", beep = "luke"))
define sheriff = Character("Sheriff", callback = renpy.partial(char_callback, name = "sheriff", beep = "sheriff"))
define taran = Character("Taran", callback = renpy.partial(char_callback, name = "taran", beep = "taran"))

# CSBIII Friend Route Character Definitions (NPCs only, friends have their own section)
define bomaha = Character("Omaha", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define cop = Character("Cop", callback = renpy.partial(char_callback, name = "cop"))
define obama = Character("Obama", callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define worker = Character("Worker", callback = char_callback)

# CSBIII South Route Character Definitions
define green = Character("Mr. Green", callback = renpy.partial(char_callback, name = "green", beep = "green"), what_color="#00FF00")
define jerma = Character("Jerma", callback = renpy.partial(char_callback, name = "jerma", beep = "jerma"))
define lancer = Character("Lancer", callback = renpy.partial(char_callback, name = "lancer", beep = "lancer"))
define lego = Character("LegoBot", callback = renpy.partial(char_callback, name = "lego", beep = "lego"))
define luigi = Character("Luigi", callback = renpy.partial(char_callback, name = "luigi", beep = "luigi"))
define trailtrash = Character("Trailer Trash", callback = renpy.partial(char_callback, name = "trailtrash"))
define tsa = Character("TSA Agent", callback = renpy.partial(char_callback, name = "tsa"))
## Reality Break Ending
define billy_far = Character("Billy (from off screen)", callback = renpy.partial(char_callback, beep = "billy_from_afar"))
define direct = Character("Director", callback = renpy.partial(char_callback, beep = "iris"))
define monika = Character("Monika", callback = renpy.partial(char_callback, name = "monika", beep = "monika"))

# CSBIII East Route Character Definitions
define billy = Character("Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define carla = Character("Carla", callback = renpy.partial(char_callback, beep = "carla"))
define cultist = Character("Cultist", callback = renpy.partial(char_callback, name = "cultist", beep = "cult"))
define cultist_2 = Character("Cultist 2", callback = char_callback)
define cultist_3 = Character("Cultist 3", callback = char_callback)
define gnome = Character("Gnome", callback = renpy.partial(char_callback, name = "gnome", beep = "gnome"))
define host = Character("Host", callback = renpy.partial(char_callback, name = "mettaton", beep = "snd_mtt"), what_font = "8bitoperator_jve.ttf", what_size = 40)
define mario = Character("Mario", callback = renpy.partial(char_callback, name = "mario"))
define peppino = Character("Peppino", callback = renpy.partial(char_callback, name = "peppino", beep = "peppino"))
define pencil = Character("Pencil Greeter", callback =renpy.partial(char_callback, name = "pencil"))
define shaggy_too_dope = Character("Shaggy Too Dope", callback = char_callback)
define scott = Character("Scott", callback = renpy.partial(char_callback, name = "scott", beep = "scott"))
define signup = Character("Signup Helper", callback = char_callback)
define smiley = Character("Smiley", callback = renpy.partial(char_callback, name = "smiley"))
define terry = Character("Terry", callback = renpy.partial(char_callback, name = "terry", beep = "terry"))
define tv_billy = Character("TV Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define streetguy = Character("Street Guy", callback = renpy.partial(char_callback, name = "streetguy", beep = "nice"))
define violent_jay = Character("Violent Jay", callback = renpy.partial(char_callback, name = "jay"))
define waitress = Character("Waitress", callback = char_callback)

# CSBIII Fired Route Character Definitions
define customer = Character("Customer", callback = char_callback)
define crowd = Character("Crowd", callback = char_callback)
define ges = Character("Ges", callback = renpy.partial(char_callback, name = "ges", beep = "ges"))
define guest = Character("Guest", callback = renpy.partial(char_callback, name = "guest"))
define howie = Character("Howie", callback = renpy.partial(char_callback, name = "howie", beep = "howie"))
define janitor = Character("Janitor", callback = char_callback)

# CSBIII Country Route Character Definitons
define nurse = Character("Nurse", callback = char_callback)
define benrey = Character("Benrey", callback = renpy.partial(char_callback, name = "benrey"))
## England
define gordon = Character("Gordon", callback = renpy.partial(char_callback, name = "gordon", beep = "gordon"))
define hammond = Character("Richard", callback = renpy.partial(char_callback, name = "hammond"))
define jeremy = Character("Jeremy", callback = char_callback)
define james = Character("James", callback = char_callback)
define tom = Character("Tom Scott", callback = renpy.partial(char_callback, name = "tom", beep = "tom"))
## Japan
define receptionist = Character("Receptionist", callback = char_callback)
define scott_pres = Character("Scott, President of Domino's Pizza", callback = renpy.partial(char_callback, name = "scott_pres", beep = "scott_pres"))
define miku = Character("Hatsune Miku", callback = renpy.partial(char_callback, name = "miku", beep = "miku"))
define sayori = Character("Sayori", callback = renpy.partial(char_callback, name = "sayori"))
## Sweden
define joel = Character("Vargskelethor Joel", callback = renpy.partial(char_callback, name = "joel", beep = "joel"))
define ikea_greeter = Character("Ikea Greeter", callback = char_callback)
define ikea_worker = Character("Ikea Worker", callback = char_callback)
define pomni = Character("Pomni", callback = renpy.partial(char_callback, name = "pomni", beep = "pomni"))
define average_swede = Character("Swede", callback = char_callback)
define alien = Character("Grey", callback = char_callback, what_font = "Eyecicles-Pz2.ttf", what_size = 40)
define moomin = Character("Moomin", callback = renpy.partial(char_callback, name = "moomin", beep = "moomin"))
define snufkin = Character("Snufkin", callback = renpy.partial(char_callback, name = "snufkin", beep = "snufkin"))
define alicia = Character("Alicia", callback = renpy.partial(char_callback, name = "alicia", beep = "alicia"))
define witch = Character("Witch", callback = renpy.partial(char_callback, name = "witch", beep = "witch"))

# Archival Ending Character Definitions
define k174 = Character("K17-M4", callback = renpy.partial(char_callback, name = "k174", beep = "k17"))
define k199 = Character("K19-M9", callback = renpy.partial(char_callback, beep = "k19"))
define k207 = Character("K20-M7", callback = renpy.partial(char_callback, beep = "k20"))

# Offscreen Character Definitions
define tate_offscreen = Character("???", callback = renpy.partial(char_callback, beep="tate"))
define tate_cyan_offscreen = Character("???", callback = renpy.partial(char_callback, beep="tate_cyan"))
define pakoo_offscreen = Character("???", callback = renpy.partial(char_callback, beep="pak"))
define green_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "green"), what_color="#00FF00")
define anno_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "anno"))
define k174_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "k17"))
define k199_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "k19"))
define k207_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "k20"))

# AI Imposter Character Definitions
define ed_ai = Character("\"Ed\"", callback = renpy.partial(char_callback, beep = "ed"))
define obamanobeep = Character("\"Obama\"", callback = renpy.partial(char_callback, play_beeps = False))
define bomahanobeep = Character("\"Omaha\"", callback = renpy.partial(char_callback, play_beeps = False))

# DX Misc Character Definitions
define copguyexe = Character("Copguy", callback = renpy.partial(char_callback, name = "copguy", beep = "copexe"))
define tate_cyan = Character("Tate?", callback = renpy.partial(char_callback, beep="tate_cyan"))

# DX Digi Character Definitions
define david = Character("David", callback = char_callback)
define george = Character("George", callback = char_callback)
define harold = Character("Harold", callback = char_callback)
define mr_krupp = Character("Mr. Krupp", callback = char_callback)
define weird_al = Character("Weird Al", callback = char_callback)

# DX BT1D Character Definitions
# TODO: need beeps
define phone = Character("Phone", callback = renpy.partial(char_callback, beep="snd_txtspam"))
define cvs = Character("CVS Employee", callback = char_callback)
define leedle = Character("Leedlelee Employee", callback = char_callback)
define diabetes_ceo = Character("CEO of Diabetes", callback = renpy.partial(char_callback, beep="diabetes_ceo"))
define diabetes_secretary = Character("Secretary of Diabetes", callback = char_callback)

# DX CultCon Character Definitions
define baumer = Character("Steve Baumer", callback = char_callback)
define blind_eye = Character("Blind Eye Cultist", callback = char_callback)
define cruise = Character("Tom Cruise", callback = renpy.partial(char_callback, name = "cruise"))
define l_cultist = Character("Lunatic Cultist", callback = char_callback)
define priest = Character("Priest", callback = char_callback)
define renovator = Character("Renovator", callback = char_callback)

# DX Kuwait Character Definitions
define k_doctor = Character("Kuwait Doctor", callback = char_callback)
define k_nurse = Character("Kuwait Nurse", callback = char_callback)
define l_snow = Character("Lt. Snow", callback = char_callback)
define RCOMEM = Character("Rocco Mem", callback = char_callback)
define suzuki = Character("Suzuki", callback = char_callback)

# DX Plane Route Character Definitions
define plane_npc_1 = Character("Passenger 1", callback = char_callback)
define plane_npc_2 = Character("Passenger 2", callback = char_callback)
define plane_npc_3 = Character("Passenger 3", callback = char_callback)
define k19 = Character("K-19", callback = renpy.partial(char_callback, name = "k19"))
define orville = Character("Orville Wright", callback = renpy.partial(char_callback, name = "wright"))
define wilbur = Character("Wilbur Wright", callback = renpy.partial(char_callback, name = "wright"))
define booger = Character("Mucinex Booger", callback = renpy.partial(char_callback, name = "booger"))

# DX Train Route Character Definitions
define amtrak_conductor = Character("Conductor", callback = renpy.partial(char_callback, name = "amtrak_conductor", beep = "amtrak_conductor"))
define amtrak_npc_1 = Character("Passenger 1", callback = char_callback)
define amtrak_npc_2 = Character("Passenger 2", callback = char_callback)
define amtrak_npc_3 = Character("Passenger 3", callback = char_callback)
define amtrak_stewardess = Character("Stewardess", callback = char_callback)
define lupin = Character("Lupin", callback = renpy.partial(char_callback, name = "lupin", beep = "lupin"))
define lupin_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "lupin"))
define mean_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "mean"))
define mean_nobeep = Character("Mean", callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_nobeep = Character("???", callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_offscreen = Character("???", callback = renpy.partial(char_callback, beep = "zenigata"))
define imperfect_tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"), what_color = "#000000", screen = "perfect_tate_text")

# DX Holiday Special Definitions
define avgn = Character("James Rolfe", callback = renpy.partial(char_callback, name = "avgn", beep = "avgn"))
define tgt_worker = Character("Target Employee", callback = renpy.partial(char_callback, name = "tgt_worker", beep="pak"))
define walkie = Character("Walkie", callback = renpy.partial(char_callback, beep = "walkie"))
define everyone = Character("Everyone", callback = renpy.partial(char_callback, beep = "everyone"))
define everyone2 = Character("Everyone", callback = renpy.partial(char_callback, beep = "csbama17"))
define santa = Character("Santa Claus", callback = renpy.partial(char_callback, name = "santa", beep = "santa"))
define mike = Character("Mike",  callback = renpy.partial(char_callback, name = "mike", beep = "mike"))

# DX Finale Character Definitions
define perfect_billy = Character("Perfect Billy", callback = renpy.partial(char_callback, name = "billy", beep = "billy"), screen = "perfect_billy_text")
define fiddle = Character("Fiddleford", callback = char_callback)
define cultcon_leader = Character("Cultcon Leader", callback = char_callback)

# DX Albu
define cashier_nobeep = Character("Cashier", callback = renpy.partial(char_callback, name = "cashier", play_beeps = False))
define cs_nobeep = Character("cs188", callback = renpy.partial(char_callback, name = "cs", play_beeps = False))
define crowd_nobeep = Character("Crowd", callback = renpy.partial(char_callback, play_beeps = False))
define daphone = Character("Da Phone", callback = renpy.partial(char_callback, play_beeps = False))
define everyone_nobeep = Character("Everyone", callback = renpy.partial(char_callback, play_beeps = False))
define hermaphrodite = Character("Hermaphrodite", callback = renpy.partial(char_callback, play_beeps = False))
define marty = Character ("Marty", callback = renpy.partial(char_callback, play_beeps = False))
define zelda = Character("Zelda", callback = renpy.partial(char_callback, play_beeps = False))

# Our Friends! Character Definitions
define addy = Character("Addy", callback = renpy.partial(char_callback, name = "addy", beep = "pak"))
define anne = Character("Anne", callback = renpy.partial(char_callback, name = "anne", beep = "anne"))
define anno = Character("Anno", callback = renpy.partial(char_callback, name = "anno", beep = "anno"))
define arceus = Character("Arceus", callback = renpy.partial(char_callback, name = "arceus", beep = "arc"))
define aria = Character("Aria", callback = renpy.partial(char_callback, name = "aria", beep = "aria"))
define blank = Character("Blank", callback = renpy.partial(char_callback, name = "blank", beep = "blank"))
define db = Character("DB05", callback = renpy.partial(char_callback, name = "db", beep = "db05"))
define digi = Character("Digi", callback = renpy.partial(char_callback, name = "digi", beep = "digi"))
define eliza = Character("Elizabeth", callback = renpy.partial(char_callback, name = "eliza", beep = "mika"))
define grace = Character("Grace", callback = renpy.partial(char_callback, name = "grace", beep = "grace"))
define horse = Character("Horse", callback = renpy.partial(char_callback, name = "horse", beep = "horse"))
define iris = Character("Iris", callback = renpy.partial(char_callback, name = "iris", beep = "iris"))
define k17 = Character("K-17", callback = renpy.partial(char_callback, name = "k17", beep = "k17"))
define k22 = Character("K-22", callback = renpy.partial(char_callback, name = "k22", beep = "k20"))
define kitty = Character("Kitty", callback = renpy.partial(char_callback, name = "kitty", beep = "kitty"))
define mean = Character("Mean", callback = renpy.partial(char_callback, name = "mean", beep = "mean"))
define midge = Character("Midge", callback = renpy.partial(char_callback, name = "midge", beep = "midge"))
define mika = Character("Mika", callback = renpy.partial(char_callback, name = "mika", beep = "mika"))
define nova = Character("Nova", callback = renpy.partial(char_callback, name = "nova"))
define pakoo = Character("Pakoo", callback = renpy.partial(char_callback, name = "pakoo", beep = "pak"))
define tate = Character("Tate", callback = renpy.partial(char_callback, name = "tate", beep = "tate"))
