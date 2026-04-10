init python:
    import math

    def get_angle(p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        radians = math.atan2(dy, dx)
        degrees = math.degrees(radians)
        if degrees < 0:
            degrees += 360
        return degrees

    config.per_frame_screens.append("osu_spinner")

screen osu_spinner(center = [960, 540], spinner_image = None, dismissable = False):

    on "show":
        action SetVariable("spins", 0)

    if dismissable:
        key "dismiss" action Return()
        text _("Click anywhere outside the spinner to return."):
            xalign 0.5 yalign 0.05

    default last_checkpoint = 3
    default checkpoint = 0
    default backwards = False
    default counted = False

    python:
        spinner_image = spinner_image if spinner_image is not None else get_themed_attribute("spinner")
        mouse_xy = renpy.get_mouse_pos()
        angle = get_angle(center, mouse_xy)
        if checkpoint == 0:
            if (135 < angle <= 225):
                backwards = True
                last_checkpoint = 0
                checkpoint = 3
            elif (315 < angle <= 360) or (0 < angle <= 45):
                backwards = False
                last_checkpoint = 0
                checkpoint = 1

            if not counted:
                counted = True

                if not backwards and last_checkpoint == 3:
                    store.spins += 1
                elif backwards and last_checkpoint == 1:
                    store.spins += 1
                renpy.restart_interaction()

        elif checkpoint == 1:
            if (45 < angle <= 135):
                backwards = False
                last_checkpoint = 1
                checkpoint = 2
            elif (225 < angle <= 315):
                backwards = True
                last_checkpoint = 1
                checkpoint = 0
        elif checkpoint == 2:
            if (135 < angle <= 225):
                backwards = False
                last_checkpoint = 2
                checkpoint = 3
            elif (315 < angle <= 360) or (0 < angle <= 45):
                backwards = True
                last_checkpoint = 2
                checkpoint = 1

            if counted:
                counted = False

        elif checkpoint == 3:
            if (225 < angle <= 315):
                backwards = False
                last_checkpoint = 3
                checkpoint = 0
            elif (45 < angle <= 135):
                backwards = True
                last_checkpoint = 3
                checkpoint = 2

    button:
        pos center
        anchor (0.5, 0.5)
        add spinner_image:
            rotate angle
        action NullAction()

    # vbox:
    #     text str(angle)
    #     text str(checkpoint) 
    # text str(spins):
    #     size 100 
    #     align (0.5, 0.5)
    #     text_align 0.5