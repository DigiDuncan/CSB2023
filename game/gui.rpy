################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.

# Default has to be here for some reason
define gui_theme_map = {}
define default_theme_map = {}
define missing_images = []

python:
    with renpy.open_file("gui/themes/default/config.json") as f:
        default_theme_map = json.load(f)

init python:
    gui.init(1920, 1080)

    font_cache = {}

    def reload_theme(theme_name, force_changed):
        global gui_theme_map
        global gui

        # Attempt to load in theme. 
        try:
            with renpy.open_file(f"gui/themes/{theme_name}/config.json") as f:
                j = json.load(f)

            def _get(k):
                nonlocal j
                global default_theme_map
                if k in j:
                    return j[k]
                elif k in default_theme_map:
                    return default_theme_map[k]
                else:
                    logger.warn(f"{k} not in theme, and fallback failed!")
                    raise ValueError(k)

            # Handler for if a theme is already in use.
            if preferences.gui_theme == theme_name and force_changed:
                logger.info(f"Theme '{theme_name}' already in use.")
                renpy.notify("You're already using this theme!")
            else:
                logger.info(f"Loaded theme '{theme_name}'.")
                if force_changed:
                    renpy.notify(f"Loaded theme {j["theme_name"]}.")

            # Force-change colors
            gui.accent_color = _get("accent_color")
            gui.idle_color = _get("idle_color")
            gui.idle_small_color = _get("idle_small_color")
            gui.hover_color = _get("hover_color")
            gui.selected_color = _get("selected_color")
            gui.insensitive_color = _get("insensitive_color")
            gui.muted_color = _get("muted_color")
            gui.hover_muted_color = _get("hover_muted_color")
            gui.text_color = _get("text_color")
            gui.interface_text_color = _get("interface_text_color")
            gui.choice_button_text_idle_color = _get("choice_button_text_idle_color")
            gui.choice_button_text_hover_color = _get("choice_button_text_hover_color")
            gui.choice_button_text_insensitive_color = _get("choice_button_text_insensitive_color")

            config.font_name_map["default"] = _get("main_font")
            config.font_name_map["cn"] = _get("cn_font")
            config.font_name_map["jp"] = _get("jp_font")
            config.font_name_map["ru"] = _get("ru_font")
            config.font_name_map["music_text"] = FontGroup().add("FiraCode-Retina.ttf", 0x2206, 0x2206).add( _get("jp_font") , 0x2600, 0x9fff).add( _get("main_font") , 0x0000, 0xffff)

            def _dyslexia_font(f):
                if theme_name in font_cache:
                    return font_cache[theme_name]
                else:
                    font_cache[theme_name] = FontGroup().add("FiraCode-Retina.ttf", 0x2206, 0x2206).add( _get("jp_font") , 0xA1, 0xfc4a).add( _get("cn_font") , 0x88a1, 0xfc4b).add( _get("ru_font") , 0x8440, 0x8491).add( _get("dyslexia_font") , 0x0000, 0xffff)
                    return font_cache[theme_name]

            config.font_transforms["dyslexia"] = _dyslexia_font

            # Switch music
            if main_menu and not preferences.disable_menu_theme and force_changed:
                renpy.music.play( _get("menu_theme"), loop=False )
                persistent.heard.add( _get("menu_theme_jukebox_id") )

        except:
            j = default_theme_map
            preferences.gui_theme = "default" # force-reset it
            logger.warn(f"Couldn't load color data for theme '{theme_name}'. Using default theme.")
            renpy.notify(f"Couldn't load color data for theme '{theme_name}'. Using default theme.")

        # Set the global theme map to the loaded one.
        gui_theme_map = j

    # Run it once as the game loads. We'll call it again in CSettings.
    reload_theme(preferences.gui_theme if hasattr(preferences, "gui_theme") else "default", False)

    def get_themed_attribute(file_path, ext = "png", prefix = "") -> str:
        sub_path = file_path + "." + ext
        file_name = sub_path.split("/")[-1]
        # You can add more places to check in this list if you want
        check_these_paths = [
            f"gui/themes/{preferences.gui_theme}/{sub_path}",
            f"gui/themes/{preferences.gui_theme}/{file_name}",
            f"gui/themes/default/{sub_path}",
            f"gui/themes/default/{file_name}",
        ]

        all_paths = []
        # Deal with Ren'Py [prefix_] style subsititutions:
        # https://www.renpy.org/doc/html/style_properties.html#style-prefix-search

        for path in check_these_paths:
            if r"[idle_]" in path:
                all_paths.append(path.replace(r"[idle_]", "idle_"))
                all_paths.append(path.replace(r"[idle_]", ""))
            elif r"[hover_]" in path:
                all_paths.append(path.replace(r"[hover_]", "hover_"))
                all_paths.append(path.replace(r"[hover_]", ""))
            elif r"[insensitive_]" in path:
                all_paths.append(path.replace(r"[insensitive_]", "insensitive_"))
                all_paths.append(path.replace(r"[insensitive_]", ""))
                all_paths.append(path.replace(r"[insensitive_]", "idle_"))
            elif r"[selected_idle_]" in path:
                all_paths.append(path.replace(r"[selected_idle_]", "selected_idle_"))
                all_paths.append(path.replace(r"[selected_idle_]", "idle_"))
                all_paths.append(path.replace(r"[selected_idle_]", "selected_"))
                all_paths.append(path.replace(r"[selected_idle_]", ""))
            elif r"[selected_hover_]" in path:
                all_paths.append(path.replace(r"[selected_hover_]", "selected_hover_"))
                all_paths.append(path.replace(r"[selected_hover_]", "hover_"))
                all_paths.append(path.replace(r"[selected_hover_]", "selected_"))
                all_paths.append(path.replace(r"[selected_hover_]", ""))
            elif r"[selected_insensitive_]" in path:
                all_paths.append(path.replace(r"[selected_insensitive_]", "selected_insensitive_"))
                all_paths.append(path.replace(r"[selected_insensitive_]", "hover_"))
                all_paths.append(path.replace(r"[selected_insensitive_]", "selected_"))
                all_paths.append(path.replace(r"[selected_insensitive_]", ""))
                all_paths.append(path.replace(r"[selected_insensitive_]", "selected_idle_"))
                all_paths.append(path.replace(r"[selected_insensitive_]", "idle_"))
            else:
                all_paths.append(path)

        # Add missing texture as fallback fallback
        all_paths.append("gui/missing_texture." + ext)
        all_paths.append("gui/missing_texture.png")

        # Deal with .. and //, since for some reason an interal function produces them
        all_paths = [p.replace("..", ".").replace("//", "/") for p in all_paths]

        global missing_images
        for path in all_paths:
            folder, name = path.rsplit("/", 1)
            if renpy.loadable(name, folder):
                if name == "missing_texture.png" and sub_path not in missing_images:
                    logger.warn(f"Missing image: {sub_path}")
                    missing_images.append(sub_path)
                return path if not prefix else f"{prefix}:{path}"

        logger.error(f"{file_path} not found in theme or fallback!")
        print(all_paths)
        raise ValueError(file_path)

    def get_themed_menu(which: str):
        file_type = gui_theme_map.get(f"{which}_filetype", "png")
        if file_type == "png" or preferences.craptop_mode:
            return get_themed_attribute(which)
        elif file_type == "webm":
            return Movie(play = get_themed_attribute(which, "webm"),
                        loop = True,
                        start_image = get_themed_attribute(f"{which}_first_frame"))
        else:
            raise ValueError(f"Unsupported menu filetype: {file_type}")


init python:
    def custom_button_properties(kind):
        g = globals()

        def get(prop):
            _gui = g["gui"]

            if kind + "_" + prop in _gui.__dict__:
                return _gui.__dict__[kind + "_" + prop]

            return None

        borders = get("borders")

        tile = get("tile")
        if tile is None:
            tile = gui.button_tile

        idle_backgrounds = []
        hover_backgrounds = []
        insensitive_backgrounds = []
        selected_idle_backgrounds = []
        selected_hover_backgrounds = []
        selected_insensitive_backgrounds = []

        if kind != "button":
            idle_backgrounds.append(get_themed_attribute("/button/" + kind[:-7] + "_[idle_]background", gui.button_image_extension))
            hover_backgrounds.append(get_themed_attribute("/button/" + kind[:-7] + "_[hover_]background", gui.button_image_extension))
            insensitive_backgrounds.append(get_themed_attribute("/button/" + kind[:-7] + "_[insensitive_]background", gui.button_image_extension))
            selected_idle_backgrounds.append(get_themed_attribute("/button/" + kind[:-7] + "_[selected_idle_]background", gui.button_image_extension))
            selected_hover_backgrounds.append(get_themed_attribute("/button/" + kind[:-7] + "_[selected_hover_]background", gui.button_image_extension))
            selected_insensitive_backgrounds.append(get_themed_attribute("/button/" + kind[:-7] + "_[selected_insensitive_]background", gui.button_image_extension))

        idle_backgrounds.append(get_themed_attribute("/button/[idle_]background", gui.button_image_extension))
        hover_backgrounds.append(get_themed_attribute("/button/[hover_]background", gui.button_image_extension))
        insensitive_backgrounds.append(get_themed_attribute("/button/[insensitive_]background", gui.button_image_extension))
        selected_idle_backgrounds.append(get_themed_attribute("/button/[selected_idle_]background", gui.button_image_extension))
        selected_hover_backgrounds.append(get_themed_attribute("/button/[selected_hover_]background", gui.button_image_extension))
        selected_insensitive_backgrounds.append(get_themed_attribute("/button/[selected_insensitive_]background", gui.button_image_extension))

        if renpy.variant("small"):
            backgrounds = [ i.replace("gui/themes/", "gui/phone/themes") for i in backgrounds ] + backgrounds

        rv = {
            "idle_background" : Frame(idle_backgrounds, borders or gui.button_borders, tile=tile),
            "hover_background" : Frame(hover_backgrounds, borders or gui.button_borders, tile=tile),
            "insensitive_background" : Frame(insensitive_backgrounds, borders or gui.button_borders, tile=tile),
            "selected_idle_background" : Frame(selected_idle_backgrounds, borders or gui.button_borders, tile=tile),
            "selected_hover_background" : Frame(selected_hover_backgrounds, borders or gui.button_borders, tile=tile),
            "selected_insensitive_background" : Frame(selected_insensitive_backgrounds, borders or gui.button_borders, tile=tile),
        }

        if borders is not None:
            rv["padding"] = borders.padding

        width = get("width")
        height = get("height")

        if width is not None:
            rv["xsize"] = width

        if height is not None:
            rv["ysize"] = height

        return rv

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = gui_theme_map["accent_color"] 

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = gui_theme_map["idle_color"]

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = gui_theme_map["idle_small_color"]

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = gui_theme_map["hover_color"]

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = gui_theme_map["selected_color"]

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = gui_theme_map["insensitive_color"]

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = gui_theme_map["muted_color"]
define gui.hover_muted_color = gui_theme_map["hover_muted_color"]

## The colors used for dialogue and menu choice text.
define gui.text_color = gui_theme_map["text_color"]
define gui.interface_text_color = gui_theme_map["interface_text_color"]


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = gui.preference("font", gui_theme_map["main_font"])

## The font used for character names.
define gui.name_text_font = gui.preference("font_name", gui_theme_map["name_font"])

## The font used for out-of-game text.
define gui.interface_text_font = gui.preference("font", gui_theme_map["main_font"])

## The size of normal dialogue text.
define gui.text_size = 46 * gui.preference("fsm", 1)

## The size of character names.
define gui.name_text_size = 36 * gui.preference("fsm", 1)

## The size of text in the game's user interface.
define gui.interface_text_size = 46 * gui.preference("fsm", 1)

## The size of labels in the game's user interface.
define gui.label_text_size = 36 * gui.preference("fsm", 1)

## The size of text on the notify screen.
define gui.notify_text_size = 24 * gui.preference("fsm", 1)

## The size of the game's title.
define gui.title_text_size = 75 * gui.preference("fsm", 1)

## Custom: Font for page header elements
define gui.header_text_font = gui.preference("font_header", gui_theme_map["header_font"])


## Main and Game Menus #########################################################

## The images used for the main and game menus.
## While it can take a video, make sure to have a png fallback for craptop mode / the first frame of the video
## Statements must be run in order of priority:
## Craptop mode, webm handling, png fallback.
## Always include a fallback image.

define gui.main_menu_background = get_themed_menu("main_menu")
define gui.game_menu_background = get_themed_menu("game_menu")

## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 278

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 360
define gui.name_ypos = 0

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = 72

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(20, 10, 20, 10)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 380
define gui.dialogue_ypos = 75

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1116

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(6, 6, 6, 6)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = gui_theme_map["choice_button_text_idle_color"]
define gui.choice_button_text_hover_color = gui_theme_map["choice_button_text_hover_color"]
define gui.choice_button_text_insensitive_color = gui_theme_map["choice_button_text_insensitive_color"]


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 60

## The vertical position of the skip indicator.
define gui.skip_ypos = 15

## The vertical position of the notify screen.
define gui.notify_ypos = 68

## The spacing between menu choices.
define gui.choice_spacing = 33

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 6

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(24, 8, 36, 8)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = None

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 173

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 15

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 278
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
