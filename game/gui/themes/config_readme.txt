Concerning the contents of config.json in each folder:

The first set of colors EXACTLY matches the UI colors as defined in gui.rpy.

The second set is for supplemental colors added for custom screens such as Item Collection. 
"screen_transparency_layer" may be either a color code or an image.

If you add any extra values/features into this file or the game, you have to add it to *all* the themes!

Color codes already include alpha, so you do not need to specify an alpha value in any newly-created screens (unless you really want/need to).

If you want to use a webm for menu backgrounds:
- Be sure to include a png version as a fallback for Craptop Mode.
- Include a first_frame.png to attempt to prevent the bug where the video goes black for one frame.

If adding new fonts:
- Be sure to adjust both font scaling and line scaling in 01_early_execute.
- Be ready to include matching fonts for JP/CN/RU/dyslexia-friendly text.

unlock_requirement refers to a value that must be added to persistent.unlocked_themes().

perf_warning is a warning to the player regarding themes that use heavier assets such as webm backgrounds.

letterbox_color is the color you'd see on the sides of the screen if you're not playing in fullscreen.