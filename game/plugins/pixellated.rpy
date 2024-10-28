# Code by AxelKong
#
# How to use:
# show expression DynamicDisplayable(Pixellated.pixellated, widget='your_character_sprite', delay=0.5, steps=8)
#
# You might need to hide this sprite and show the normal one after, depending on what you're doing.
# Use caution when combining with zoom/motion/rotation/anything. It may behave unexpectedly.

init python:
    class Pixellated(renpy.Displayable):

        def __init__(self, widget, step, **properties):

            super().__init__(**properties)
            self.widget = renpy.displayable(widget)
            self.width, self.height = 0, 0
            self.step = step

        def render(self, width, height, st, at):
            rdr = renpy.render(self.widget, width, height, st, at)
            self.width, self.height = rdr.get_size()

            rv = renpy.Render(rdr.width, rdr.height)
            rv.blit(rdr, (0, 0))
            rv.operation = renpy.display.render.PIXELLATE 
            rv.operation_parameter = self.step
            rv.mesh = True
            rv.add_shader("renpy.texture")
            rv.add_property("texture_scaling", "nearest_mipmap_nearest")
            rv.add_property("anisotropic", False)
            rv.add_uniform("u_lod_bias", self.step)
            return rv

        def pixellated(st, at, widget, delay, steps):
            if st < delay:
                quantum = delay / steps
                step = st // quantum
                return Pixellated(widget, steps - step), 0
            return widget, None
