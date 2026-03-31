python early:
    import re
    import json

    # default spine size is 300x46
    class Book:
        def __init__(
            self,
            book_id: str,
            title: str, description: str,
            x_pos: int, y_pos: int,
            kind: str, destination: str
        ):
            self.book_id = book_id
            self.title = title
            self.description = description
            self.x_pos = x_pos
            self.y_pos = y_pos

            self.kind = kind
            self.destination = destination

            self.spine = f"gui/books/{book_id}/side.png"
            self.hover_spine = f"selectable:gui/books/{book_id}/side.png"
            self.front = f"gui/books/{book_id}/cover.png"

style subgame_return is button:
    # this is the closest thing to a blank line i can do here, but the tag needs to exist or it'll crash - tate
    background None

style subgame_return_text is text:
    color "#000000"
    outlines [(5, "#FFFFFF", absolute(0), absolute(0))]

    hover_color "#FFFFFF"
    hover_outlines [(5, "#000000", absolute(0), absolute(0))]

screen subgame():
    tag menu
    image "gui/subgame_menu.png"

    default bookshelf = []
    default current_subgame_name = None
    default current_subgame_desc = None
    default current_subgame_art = None
    default current_subgame_kind = None
    default current_subgame_destination = None

    python:
        bookshelf = []
        for book in BOOKS_MAP:
            # only show the book if's unlocked
            # default is unlocked
            this_unlocked = True

            # unlock by label
            if "need_label" in BOOKS_MAP[book] and not renpy.seen_label(BOOKS_MAP[book]["need_label"]):
                this_unlocked = False

            # unlock by persistent value
            if "need_persistent" in BOOKS_MAP[book] and not getattr(persistent, "saved_christmas"):
                this_unlocked = False

            # append to shelf if unlocked
            if this_unlocked == True:
                bookshelf.append(
                    Book(
                        book,
                        BOOKS_MAP[book]["title"],
                        BOOKS_MAP[book]["desc"],
                        BOOKS_MAP[book]["x_pos"],
                        BOOKS_MAP[book]["y_pos"],
                        BOOKS_MAP[book]["kind"],
                        BOOKS_MAP[book]["destination"]
                    )
                )

    for book in bookshelf:
        imagebutton:
            hover book.hover_spine
            idle book.spine
            hover_sound "audio/sfx/sfx_select.ogg"
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SetScreenVariable("current_subgame_name", book.title),
                SetScreenVariable("current_subgame_desc", book.description),
                SetScreenVariable("current_subgame_art", book.front),
                SetScreenVariable("current_subgame_kind", book.kind),
                SetScreenVariable("current_subgame_destination", book.destination)
            ]
            xpos book.x_pos
            ypos book.y_pos

    if current_subgame_name:
        frame:
            background None
            xsize 0.5 ysize 1.0
            xalign 1.0 yalign 1.0

            vbox:
                # Name of the game
                frame:
                    background None
                    xalign 0.5 yalign 0
                    xsize 1.0 ysize 300
                    vbox:
                        xalign 0.5  yalign 0.5
                        text current_subgame_name:
                            color Color("#FFFFFF")
                            outlines [(5, "#000000", absolute(0), absolute(0))]
                            size 72
                            xalign 0.5
                            text_align 0.5

                        # Description of the game
                        text current_subgame_desc:
                            color Color("#FFFFFF")
                            outlines [(5, "#000000", absolute(0), absolute(0))]
                            text_align 0.5
                            xalign 0.5

                # Display the book image
                frame:
                    background None
                    xalign 0.5 yalign 0
                    xsize 1.0 ysize 600
                    image current_subgame_art:
                        xalign 0.5 yalign 0.5
                        xysize(392,600)
                        fit("contain")

            # Play button
            imagebutton:
                idle "gui/play_button.png"
                hover "selectable:gui/play_button.png"
                xalign 0.5 yalign 1.0
                hover_sound "audio/sfx/sfx_select.ogg"

                if current_subgame_kind == "label":
                    action [
                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                        Start(current_subgame_destination)
                    ]
                elif current_subgame_kind == "menu":
                    action [
                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                        ShowMenu(current_subgame_destination)
                    ]
                else:
                    # this should NEVER happen
                    action [ Notify("Something's broken! Yell at Tate!") ]

    textbutton _("Main Menu"):
        style "subgame_return"
        action Return()
        yoffset 1000
        xoffset 25
