########## Generic Character Definitions
define n = Character(None, what_italic = True, callback = char_callback)  # Narrator
define chat = Character(_("Chat"), callback = char_callback)
define unknown = Character(_("???"), callback = char_callback)
define pc = Character(_("PC"), callback = char_callback)
define everyone_generic = Character(_("Everyone"), callback = char_callback)

########## CS' Various Character Definitions
define cs = Character(_("cs188"), callback = renpy.partial(char_callback, name = "cs", beep = "cs"))
define cs_fakegod = Character(_("cs188 (pretending to be CSGod)"), callback = renpy.partial(char_callback, name = "cs", beep = "csgod"))
define csgod = Character(_("CSGod"), callback = renpy.partial(char_callback, name = "csgod", beep = "csgod"), what_color="#CB50FF", who_color="#CB50FF")
define ycs = Character(_("Young CS"), callback = renpy.partial(char_callback, beep = "ycs"))

########## CSBI Character Definitions (Including HoH SiS)
define carguy = Character(_("Carguy"), callback = renpy.partial(char_callback, name = "carguy", beep = "nice"))
define carguy_nobeep = Character(_("Carguy"), callback = renpy.partial(char_callback, name = "carguy", play_beeps = False))
define cashier = Character(_("Cashier"), callback = renpy.partial(char_callback, name = "cashier"))
define craptop = Character(_("Craptop"), callback = renpy.partial(char_callback, name = "craptop", beep=["craptop_1", "craptop_2", "craptop_3", "craptop_4", "craptop_5", "craptop_6", "craptop_7", "craptop_8", "craptop_9", "craptop_10"]))
define discord = Character(_("Discord"), callback = char_callback)
define doug = Character(_("Doug"), callback = renpy.partial(char_callback, name = "doug", beep = "doug"))
define greeter = Character(_("Greeter"), callback = renpy.partial(char_callback, name = "doug", beep = "doug"))
define michael = Character(_("Michael"), callback = renpy.partial(char_callback, name = "michael", beep = "mich"))
define michael_nobeep = Character(_("Michael"), callback = renpy.partial(char_callback, name = "michael", play_beeps = False))
define phil = Character(_("Phil"), callback = renpy.partial(char_callback, name = "phil", beep = "phil"))
define sticky = Character(_("Sticky Note"), callback = renpy.partial(char_callback, name = "sticky"))
## HoH SiS
define ed = Character(_("Ed"), callback = renpy.partial(char_callback, name = "ed", beep = "ed"))
define hoh_operator = Character(_("HoH SiS Operator"), callback = char_callback)
define rich = Character(_("Richard"), callback = renpy.partial(char_callback, name = "rich", beep = "rich"))
define wesley = Character(_("Wesley"), callback = renpy.partial(char_callback, name = "wesley", beep = "wes"))
define worker_1 = Character(_("Worker 1"), callback = char_callback)
define worker_1_beach = Character(_("Customer"), callback = char_callback)
define worker_2 = Character(_("Worker 2"), callback = char_callback)
define worker_3 = Character(_("Worker 3"), callback = char_callback)
define worker_4 = Character(_("Worker 4"), callback = char_callback)
define worker_5 = Character(_("Worker 5"), callback = char_callback)
define worker_6 = Character(_("Worker 6"), callback = char_callback)
define worker_7 = Character(_("Worker 7"), callback = char_callback)

########## CSBII Character Definitions
define asylum_worker = Character(_("Mr. Mohs"), callback = renpy.partial(char_callback, name = "mohs"))
define border_guard = Character(_("Border Guard"), callback = renpy.partial(char_callback, name = "border_guard"))
define copguy = Character(_("Copguy"), callback = renpy.partial(char_callback, name = "copguy", beep = "cop"))
define linus = Character(_("Linus"), callback = renpy.partial(char_callback, name = "linus", beep = "ltt"))

########## CSBIII Part 1 Character Definitions
define colton = Character(_("Colton"), callback = renpy.partial(char_callback, name = "colton"))
define luke = Character(_("Luke"), callback = renpy.partial(char_callback, name = "luke", beep = "luke"))
define sheriff = Character(_("Sheriff"), callback = renpy.partial(char_callback, name = "sheriff", beep = "sheriff"))
define taran = Character(_("Taran"), callback = renpy.partial(char_callback, name = "taran", beep = "taran"))

########## CSBIII Friend Route Character Definitions (NPCs only, friends have their own section)
define bomaha = Character(_("Omaha"), callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define cop = Character(_("Cop"), callback = renpy.partial(char_callback, name = "cop"))
define obama = Character(_("Obama"), callback = renpy.partial(char_callback, name = "obama", beep = "obama"))
define worker = Character(_("Worker"), callback = char_callback)

########## CSBIII South Route Character Definitions
define green = Character(_("Mr. Green"), callback = renpy.partial(char_callback, name = "green", beep = "green"), what_color="#00FF00")
define jerma = Character(_("Jerma"), callback = renpy.partial(char_callback, name = "jerma", beep = "jerma"))
define lancer = Character(_("Lancer"), callback = renpy.partial(char_callback, name = "lancer", beep = "lancer"))
define lego = Character(_("LegoBot"), callback = renpy.partial(char_callback, name = "lego", beep = "lego"))
define luigi = Character(_("Luigi"), callback = renpy.partial(char_callback, name = "luigi", beep = "luigi"))
define trailtrash = Character(_("Trailer Trash"), callback = renpy.partial(char_callback, name = "trailtrash"))
define tsa = Character(_("TSA Agent"), callback = renpy.partial(char_callback, name = "tsa"))

### Reality Break Ending
define billy_far = Character(_("Billy (from off screen)"), callback = renpy.partial(char_callback, beep = "billy_from_afar"))
define direct = Character(_("Director"), callback = renpy.partial(char_callback, beep = "iris"))
define monika = Character(_("Monika"), callback = renpy.partial(char_callback, name = "monika", beep = "monika"))

########## CSBIII East Route Character Definitions
define billy = Character(_("Billy"), callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define carla = Character(_("Carla"), callback = renpy.partial(char_callback, beep = "carla"))
define cultist = Character(_("Cultist"), callback = renpy.partial(char_callback, name = "cultist", beep = "cult"))
define cultist_2 = Character(_("Cultist 2"), callback = char_callback)
define cultist_3 = Character(_("Cultist 3"), callback = char_callback)
define gnome = Character(_("Gnome"), callback = renpy.partial(char_callback, name = "gnome", beep = "gnome"))
define host = Character(_("Host"), callback = renpy.partial(char_callback, name = "mettaton", beep = ["snd_mtt1", "snd_mtt2", "snd_mtt3", "snd_mtt4", "snd_mtt5", "snd_mtt6", "snd_mtt7", "snd_mtt8", "snd_mtt9"]), what_font = "8bitoperator_jve.ttf", what_size = 40)
define mario = Character(_("Mario"), callback = renpy.partial(char_callback, name = "mario"))
define peppino = Character(_("Peppino"), callback = renpy.partial(char_callback, name = "peppino", beep = "peppino"))
define pencil = Character(_("Pencil Greeter"), callback =renpy.partial(char_callback, name = "pencil"))
define shaggy_too_dope = Character(_("Shaggy Too Dope"), callback = char_callback)
define scott = Character(_("Scott"), callback = renpy.partial(char_callback, name = "scott", beep = "scott"))
define signup = Character(_("Signup Helper"), callback = char_callback)
define smiley = Character(_("Smiley"), callback = renpy.partial(char_callback, name = "smiley"))
define terry = Character(_("Terry"), callback = renpy.partial(char_callback, name = "terry", beep = "terry"))
define tv_billy = Character(_("TV Billy"), callback = renpy.partial(char_callback, name = "billy", beep = "billy"))
define streetguy = Character(_("Street Guy"), callback = renpy.partial(char_callback, name = "streetguy", beep = "nice"))
define violent_jay = Character(_("Violent Jay"), callback = renpy.partial(char_callback, name = "jay"))
define waitress = Character(_("Waitress"), callback = char_callback)

########## CSBIII Fired Route Character Definitions
define customer = Character(_("Customer"), callback = char_callback)
define crowd = Character(_("Crowd"), callback = char_callback)
define guest = Character(_("Guest"), callback = renpy.partial(char_callback, name = "guest"))
define howie = Character(_("Howie"), callback = renpy.partial(char_callback, name = "howie", beep = "howie"))
define janitor = Character(_("Janitor"), callback = char_callback)

########## CSBIII Country Route Character Definitons
define nurse = Character(_("Nurse"), callback = char_callback)
define benrey = Character(_("Benrey"), callback = renpy.partial(char_callback, name = "benrey"))

### England
define gordon = Character(_("Gordon"), callback = renpy.partial(char_callback, name = "gordon", beep = "gordon"))
define hammond = Character(_("Richard"), callback = renpy.partial(char_callback, name = "hammond"))
define jeremy = Character(_("Jeremy"), callback = char_callback)
define james = Character(_("James"), callback = char_callback)
define tom = Character(_("Tom Scott"), callback = renpy.partial(char_callback, name = "tom", beep = "tom"))

### Japan
define receptionist = Character(_("Receptionist"), callback = char_callback)
define scott_pres = Character(_("Scott, President of Domino's Pizza"), callback = renpy.partial(char_callback, name = "scott_pres", beep = "scott_pres"))
define miku = Character(_("Hatsune Miku"), callback = renpy.partial(char_callback, name = "miku", beep = "miku"))
define sayori = Character(_("Sayori"), callback = renpy.partial(char_callback, name = "sayori"))

### Sweden
define joel = Character(_("Vargskelethor Joel"), callback = renpy.partial(char_callback, name = "joel", beep = "joel"))
define ikea_greeter = Character(_("Ikea Greeter"), callback = char_callback)
define ikea_worker = Character(_("Ikea Worker"), callback = char_callback)
define pomni = Character(_("Pomni"), callback = renpy.partial(char_callback, name = "pomni", beep = "pomni"))
define average_swede = Character(_("Swede"), callback = char_callback)
define alien = Character(_("Grey"), callback = char_callback, what_font = "Eyecicles-Pz2.ttf", what_size = 40)
define moomin = Character(_("Moomin"), callback = renpy.partial(char_callback, name = "moomin", beep = "moomin"))
define snufkin = Character(_("Snufkin"), callback = renpy.partial(char_callback, name = "snufkin", beep = "snufkin"))
define alicia = Character(_("Alicia"), callback = renpy.partial(char_callback, name = "alicia", beep = "alicia"))
define witch = Character(_("Witch"), callback = renpy.partial(char_callback, name = "witch", beep = "witch"))

########## Archival Ending Character Definitions
define k174 = Character(_("K17-M4"), callback = renpy.partial(char_callback, name = "k174", beep = "k17"))
define k199 = Character(_("K19-M9"), callback = renpy.partial(char_callback, beep = "k19"))
define k207 = Character(_("K20-M7"), callback = renpy.partial(char_callback, beep = "k20"))

########## Offscreen Character Definitions
define tate_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep="tate"))
define tate_cyan_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep="tate_cyan"))
define pakoo_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep="pak"))
define green_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "green"), what_color="#00FF00")
define anno_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "anno"))
define k174_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "k17"))
define k199_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "k19"))
define k207_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "k20"))

########## AI Imposter Character Definitions
define ed_ai = Character(_("\"Ed\""), callback = renpy.partial(char_callback, beep = "ed"))
define obamanobeep = Character(_("\"Obama\""), callback = renpy.partial(char_callback, play_beeps = False))
define bomahanobeep = Character(_("\"Omaha\""), callback = renpy.partial(char_callback, play_beeps = False))

########## DX Misc Character Definitions
define copguyexe = Character(_("Copguy"), callback = renpy.partial(char_callback, name = "copguy", beep = "copexe"))

########## DX Book Character Definitions
define tate_cyan = Character(_("Tate?"), callback = renpy.partial(char_callback, beep = "tate_cyan")) # no auto-unlock on purpose

# Cpt. Underpants is not here because he has no spoken lines
define david = Character(_("David"), callback = renpy.partial(char_callback, name = "david"))
define george = Character(_("George"), callback = renpy.partial(char_callback, name = "george"))
define harold = Character(_("Harold"), callback = renpy.partial(char_callback, name = "harold"))
define mr_krupp = Character(_("Mr. Krupp"), callback = renpy.partial(char_callback, name = "mr_krupp"))
define weird_al = Character(_("Weird Al"), callback = renpy.partial(char_callback, name = "weird_al"))

define digimom = Character(_("DigiMom"), callback = char_callback)
define rex = Character(_("Rex Mohs"), callback = char_callback)

########## DX BT1D Character Definitions
# TODO: need beeps
define phone = Character(_("Phone"), callback = renpy.partial(char_callback, beep="snd_txtspam"))
define cvs = Character(_("CVS Employee"), callback = char_callback)
define leedle = Character(_("Leedlelee Employee"), callback = char_callback)
define diabetes_ceo = Character(_("CEO of Diabetes"), callback = renpy.partial(char_callback, beep="diabetes_ceo"))
define diabetes_secretary = Character(_("Secretary of Diabetes"), callback = char_callback)

########## DX CultCon Character Definitions
define baumer = Character(_("Steve Baumer"), callback = char_callback)
define blind_eye = Character(_("Blind Eye Cultist"), callback = char_callback)
define cruise = Character(_("Tom Cruise"), callback = renpy.partial(char_callback, name = "cruise"))
define l_cultist = Character(_("Lunatic Cultist"), callback = char_callback)
define priest = Character(_("Priest"), callback = char_callback)
define renovator = Character(_("Renovator"), callback = char_callback)

########## DX Kuwait Character Definitions
define k_doctor = Character(_("Kuwait Doctor"), callback = char_callback)
define k_nurse = Character(_("Kuwait Nurse"), callback = char_callback)
define l_snow = Character(_("Lt. Snow"), callback = char_callback)
define RCOMEM = Character(_("Rocco Mem"), callback = char_callback)
define suzuki = Character(_("Suzuki"), callback = char_callback)

########## DX Plane Route Character Definitions
define plane_npc_1 = Character(_("Passenger 1"), callback = char_callback)
define plane_npc_2 = Character(_("Passenger 2"), callback = char_callback)
define plane_npc_3 = Character(_("Passenger 3"), callback = char_callback)
define k19 = Character(_("K-19"), callback = renpy.partial(char_callback, name = "k19"))
define orville = Character(_("Orville Wright"), callback = renpy.partial(char_callback, name = "wright"))
define wilbur = Character(_("Wilbur Wright"), callback = renpy.partial(char_callback, name = "wright"))
define booger = Character(_("Mucinex Booger"), callback = renpy.partial(char_callback, name = "booger"))

########## DX Train Route Character Definitions
define amtrak_conductor = Character(_("Conductor"), callback = renpy.partial(char_callback, name = "amtrak_conductor", beep = "amtrak_conductor"))
define amtrak_npc_1 = Character(_("Passenger 1"), callback = char_callback)
define amtrak_npc_2 = Character(_("Passenger 2"), callback = char_callback)
define amtrak_npc_3 = Character(_("Passenger 3"), callback = char_callback)
define amtrak_stewardess = Character(_("Stewardess"), callback = char_callback)
define lupin = Character(_("Lupin"), callback = renpy.partial(char_callback, name = "lupin", beep = "lupin"))
define lupin_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "lupin"))
define mean_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "mean"))
define mean_nobeep = Character(_("Mean"), callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_nobeep = Character(_("???"), callback = renpy.partial(char_callback, play_beeps = False))
define zenigata_offscreen = Character(_("???"), callback = renpy.partial(char_callback, beep = "zenigata"))
define imperfect_tate = Character(_("Tate"), callback = renpy.partial(char_callback, name = "tate", beep = "tate"), what_color = "#000000", screen = "perfect_tate_text")

########## DX Holiday Special Definitions
define avgn = Character(_("James Rolfe"), callback = renpy.partial(char_callback, name = "avgn", beep = "avgn"))
define tgt_worker = Character(_("Target Employee"), callback = renpy.partial(char_callback, name = "tgt_worker", beep="pak"))
define walkie = Character(_("Walkie"), callback = renpy.partial(char_callback, beep = "walkie"))
define everyone = Character(_("Everyone"), callback = renpy.partial(char_callback, beep = "everyone"))
define everyone2 = Character(_("Everyone"), callback = renpy.partial(char_callback, beep = "csbama17"))
define santa = Character(_("Santa Claus"), callback = renpy.partial(char_callback, name = "santa", beep = "santa"))
define mike = Character(_("Mike"),  callback = renpy.partial(char_callback, name = "mike", beep = "mike"))

########## DX Finale Character Definitions
define perfect_billy = Character(_("Perfect Billy"), callback = renpy.partial(char_callback, name = "billy", beep = "billy"), screen = "perfect_billy_text")
define fiddle = Character(_("Fiddleford"), callback = char_callback)
define cultcon_leader = Character(_("Cultcon Leader"), callback = char_callback)

########## DX Albu
define cashier_nobeep = Character(_("Cashier"), callback = renpy.partial(char_callback, name = "cashier", play_beeps = False))
define cs_nobeep = Character(_("cs188"), callback = renpy.partial(char_callback, name = "cs", play_beeps = False))
define crowd_nobeep = Character(_("Crowd"), callback = renpy.partial(char_callback, play_beeps = False))
define daphone = Character(_("Da Phone"), callback = renpy.partial(char_callback, play_beeps = False))
define everyone_nobeep = Character(_("Everyone"), callback = renpy.partial(char_callback, play_beeps = False))
define hermaphrodite = Character(_("Hermaphrodite"), callback = renpy.partial(char_callback, play_beeps = False))
define marty = Character(("Marty"), callback = renpy.partial(char_callback, play_beeps = False))
define zelda = Character(_("Zelda"), callback = renpy.partial(char_callback, play_beeps = False))

########## DX Beach
define kappn = Character(_("Kapp'n"), callback = renpy.partial(char_callback, name = "kappn")) # TODO: need beeps

########## Our Friends! Character Definitions
define addy = Character(_("Addy"), callback = renpy.partial(char_callback, name = "addy", beep = "pak"))
define anne = Character(_("Anne"), callback = renpy.partial(char_callback, name = "anne", beep = "anne"))
define anno = Character(_("Anno"), callback = renpy.partial(char_callback, name = "anno", beep = "anno"))
define arceus = Character(_("Arceus"), callback = renpy.partial(char_callback, name = "arceus", beep = "arc"))
define aria = Character(_("Aria"), callback = renpy.partial(char_callback, name = "aria", beep = "aria"))
define blank = Character(_("Blank"), callback = renpy.partial(char_callback, name = "blank", beep = "blank"))
define db = Character(_("DB05"), callback = renpy.partial(char_callback, name = "db", beep = "db05"))
define digi = Character(_("Digi"), callback = renpy.partial(char_callback, name = "digi", beep = "digi"))
define eliza = Character(_("Elizabeth"), callback = renpy.partial(char_callback, name = "eliza", beep = "mika"))
define grace = Character(_("Grace"), callback = renpy.partial(char_callback, name = "grace", beep = "grace"))
define ges = Character(_("Ges"), callback = renpy.partial(char_callback, name = "ges", beep = "ges"))
define horse = Character(_("Horse"), callback = renpy.partial(char_callback, name = "horse", beep = "horse"))
define iris = Character(_("Iris"), callback = renpy.partial(char_callback, name = "iris", beep = "iris"))
define k17 = Character(_("K-17"), callback = renpy.partial(char_callback, name = "k17", beep = "k17"))
define k22 = Character(_("K-22"), callback = renpy.partial(char_callback, name = "k22", beep = "k20"))
define kitty = Character(_("Kitty"), callback = renpy.partial(char_callback, name = "kitty", beep = "kitty"))
define mean = Character(_("Mean"), callback = renpy.partial(char_callback, name = "mean", beep = "mean"))
define midge = Character(_("Midge"), callback = renpy.partial(char_callback, name = "midge", beep = "midge"))
define mika = Character(_("Mika"), callback = renpy.partial(char_callback, name = "mika", beep = "mika"))
define nova = Character(_("Nova"), callback = renpy.partial(char_callback, name = "nova"))
define pakoo = Character(_("Pakoo"), callback = renpy.partial(char_callback, name = "pakoo", beep = "pak"))
define tate = Character(_("Tate"), callback = renpy.partial(char_callback, name = "tate", beep = "tate"))
define bbl = Character(_("Bubble"), callback = char_callback)
