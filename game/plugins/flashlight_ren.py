"""renpy
init python:
"""

class Flashlight(renpy.Displayable):
    def __init__(self):
        super(Flashlight, self).__init__()

        # This image should be twice the width and twice the height
        # of the screen.
        self.child = Image("gui/flashlight.png")

        # (-1, -1) is the way the event system represents
        # "outside the game window".
        self.pos = (-1, -1)

    def render(self, width, height, st, at):
        render = renpy.Render(config.screen_width, config.screen_height)

        if self.pos == (-1, -1):
            # If we don't know where the cursor is, render pure black.
            render.canvas().rect("#000", (0, 0, config.screen_width, config.screen_height))
            return render

        # Render the flashlight image.
        child_render = renpy.render(self.child, width, height, st, at)

        # Draw the image centered on the cursor.
        flashlight_width, flashlight_height = child_render.get_size()
        x, y = self.pos
        x -= flashlight_width / 2
        y -= flashlight_height / 2
        render.blit(child_render, (x, y))
        return render

    def event(self, ev, x, y, st):
        # Re-render if the position changed.
        if self.pos != (x, y):
            renpy.redraw(self, 0)

        # Update stored position
        self.pos = (x, y)

    def visit(self):
        return [ self.child ]
