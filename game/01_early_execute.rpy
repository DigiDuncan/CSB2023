init python:
    renpy.add_layer("music", above = "master")
    renpy.add_layer("popup", above = "overlay")

# WARN:
# For some reason the linter thinks that persistent variables with underscores
# are never initialized. It's lying to you; it's fine.

define determination = Dissolve(0.0)
default persistent.seen = set()
default persistent.heard = set()
default persistent.true_ending = False
default persistent.creative_mode = False
default persistent.seen_splash = False
default persistent.first_time = True

# Chapter unlocks
default persistent.csb2_unlocked = False
default persistent.csb3a_unlocked = False
default persistent.csb3b_unlocked = False
