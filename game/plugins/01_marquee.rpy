################################################################################
##
## Marquee for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
##
################################################################################
## This file contains code for a marquee displayable in Ren'Py. There is both
## a CDD to handle the rendering of the marquee, and a screen language keyword
## so it can be easily declared in-game. Several example transforms are also
## included at the bottom of this file.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the other file,
## marquee_examples.rpy! This is just the backend; you don't need to understand
## everything in this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_marquee.rpy", None)
    build.classify("**01_marquee.rpyc", "archive")
################################################################################
python early:

    class Marquee(renpy.display.layout.MultiBox):
        """
        Creates a special container which crops its child to the size of the
        container, and applies an animation to the child if it is larger than
        the container.

        Attributes:
        -----------
        animation : ATL transform
            The animation to apply to the child if it is larger than the
            container. If None, no animation is applied.
        always_animate : bool
            If True, the animation will always be applied, even if the child
            would fit in the container. If False, the default, the animation
            is only applied when the child is too large for the container.
        applied_animation : bool or Displayable
            The animation that was applied to the child. If False, no animation
            was applied. Otherwise, this is the child with the animation
            applied.
        """
        def __init__(self, *args, **kwargs):
            self.animation = kwargs.pop("animation", None)
            self.always_animate = kwargs.pop("always_animate", False)
            self._children = [ ]
            self.applied_animation = None
            self.last_child = None
            super(Marquee, self).__init__(*args, **kwargs)

        @property
        def children(self):
            if self.applied_animation:
                return [ self.applied_animation ]
            elif self.child:
                return [ self.child ]
            else:
                return self._children

        def per_interact(self):
            """Ensure the animation is updated if the children are."""
            if self.child is not self.last_child:
                self.applied_animation = None
            super(Marquee, self).per_interact()

        @children.setter
        def children(self, value):
            self._children = value

        def render(self, width, height, st, at):
            """Render the marquee to the screen."""

            if self.animation is None:
                ## No animation to apply
                self.applied_animation = False
            elif self.always_animate:
                ## Always apply the animation.
                if not self.applied_animation:
                    self.applied_animation = At(self.child, self.animation)
            else:
                ## Check if we need to apply the animation at all. What's the
                ## size of the child vs our size?
                c_w, c_h = self.child.render(width, height, st, at).get_size()
                if c_w > width or c_h > height:
                    ## Apply the animation if we haven't already saved one.
                    if not self.applied_animation:
                        self.applied_animation = At(self.child, self.animation)
                else:
                    self.applied_animation = False
            self.last_child = self.child
            ren = super(Marquee, self).render(width, height, st, at)
            ## Crop the child to the size of the container
            rv = ren.subsurface((0, 0, width, height), focus=True)
            return rv

    ## Register the marquee as a screen language keyword.
    renpy.register_sl_displayable("marquee", Marquee, "marquee", 1,
        default_keywords={ 'layout' : 'fixed' }
        ).add_property("animation"
        ).add_property("always_animate"
        ).add_property_group("box")

## The default style for any marquee displayables.
style marquee:
    is fixed

################################################################################
## Transforms
################################################################################
## You can create your own transforms to use with the marquee element. Here are
## a few standard ones you might like to use.

## A transform which shuffles the marquee element back and forth while
## remaining on-screen.
transform marquee_shuffle(t, delay=0.5):
    xalign 0.0 subpixel True
    pause delay
    ease t xalign 1.0
    pause delay
    ease t xalign 0.0
    repeat

## A transform which constantly pans the marquee element in a loop.
transform marquee_pan(t):
    xpan -180 subpixel True
    linear t xpan 180
    repeat

## A transform which moves the marquee element offscreen, and then
## resets it back on-screen.
transform marquee_scroll(t, delay=0.5):
    xalign 0.0 subpixel True
    pause delay
    linear t xanchor 1.0 xpos 0.0
    pause 0.1
    repeat
