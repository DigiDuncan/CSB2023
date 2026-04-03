python early:
    import re
    import json

    # default spine size is 300x46
    class Book:
        def __init__(
            self,
            book_id: str,
            title: str, desc: str,
            x_pos: int, y_pos: int,
            kind: str, destinations: dict
        ):
            self.book_id = book_id
            self.title = title
            self.desc = desc
            self.x_pos = x_pos
            self.y_pos = y_pos

            self.kind = kind
            self.destinations = destinations

            self.spine = f"gui/books/{book_id}/side.png"
            self.hover_spine = f"selectable:gui/books/{book_id}/side.png"
            self.front = f"gui/books/{book_id}/cover.png"

    def __str__(self) -> str:
        return f"<Book {self.book_id} \"{self.title}\">"

    def __repr__(self) -> str:
        return self.__str__()

screen subgame():
    tag menu
    image "gui/subgame_menu.png"

    default bookshelf = []
    default current_book = None

    python:
        bookshelf = []
        for book in BOOKS_MAP:
            # only show the book if's unlocked
            # default is locked
            this_unlocked = False

            for destination in BOOKS_MAP[book]["destinations"]:
                # unlock by label
                if "need_label" in BOOKS_MAP[book]["destinations"][destination] and renpy.seen_label(BOOKS_MAP[book]["destinations"][destination]["need_label"]):
                    this_unlocked = True

                # unlock by persistent value
                if "need_persistent" in BOOKS_MAP[book]["destinations"][destination] and getattr(persistent, BOOKS_MAP[book]["destinations"][destination]["need_persistent"]):
                    this_unlocked = True

                if "need_label" not in BOOKS_MAP[book]["destinations"][destination] and "need_persistent" not in BOOKS_MAP[book]["destinations"][destination]:
                    this_unlocked = True

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
                        BOOKS_MAP[book]["destinations"]
                    )
                )

    for book in bookshelf:
        imagebutton:
            idle book.spine
            hover book.hover_spine
            selected_idle book.hover_spine
            selected_hover book.hover_spine
            selected (current_book is not None and current_book.book_id == book.book_id)
            hover_sound "audio/sfx/sfx_select.ogg"
            action [
                Play("sound", "audio/sfx/sfx_valid.ogg"),
                SelectedIf(SetScreenVariable("current_book", book)),
                With(Dissolve(0.25))
            ]
            xpos book.x_pos
            ypos book.y_pos

    if current_book is not None:
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
                        text current_book.title:
                            color Color("#FFFFFF")
                            outlines [(4.5, "#000000", absolute(0), absolute(0))]
                            size 72
                            xalign 0.5
                            text_align 0.5

                        # Description of the game
                        text current_book.desc:
                            color Color("#FFFFFF")
                            outlines [(4.5, "#000000", absolute(0), absolute(0))]
                            text_align 0.5
                            xalign 0.5

                # Display the book image
                frame:
                    background None
                    xalign 0.5 yalign 0
                    xsize 1.0 ysize 600
                    image current_book.front:
                        xalign 0.5 yalign 0.5
                        xysize(392,600)
                        fit("contain")

            # Play button
            if current_book.kind == "label":
                hbox:
                    xalign 0.5 yalign 1.0
                    yoffset -24
                    spacing 24

                    for l, d in current_book.destinations.items():
                        python:
                            button_text = d.get("custom_button", "PLAY")
                            show_this = True
                            if "need_label" in d:
                                if not renpy.seen_label(d["need_label"]):
                                    show_this = False
                            if "need_persistent" in d:
                                if not getattr(persistent, d["need_persistent"]):
                                    show_this = False

                        if show_this:
                            button:
                                hover_sound "audio/sfx/sfx_select.ogg"
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    Start(l)
                                ]

                                frame:
                                    xminimum 215 xmaximum 400
                                    ysize 87
                                    xalign 0.5 yalign 1.0
                                    padding (20, 0, 20, 0)
                                    
                                    idle_background Frame(get_themed_attribute("button/button"), 10, 10)
                                    hover_background Frame(get_themed_attribute("button/button", prefix="selectable") , 10, 10)

                                    text button_text:
                                        xalign 0.5 yalign 0.5
                                        text_align 0.5
                                        size 64

                                        color gui.text_color
                                        hover_color gui.text_color

            elif current_book.kind == "menu":
                hbox:
                    xalign 0.5 yalign 1.0
                    yoffset -24
                    spacing 24

                    for l, d in current_book.destinations.items():
                        python:
                            button_text = d.get("custom_button", _("OPEN"))
                            show_this = True
                            if "need_label" in d:
                                if not renpy.seen_label(d["need_label"]):
                                    show_this = False
                            if "need_persistent" in d:
                                if not getattr(persistent, d["need_persistent"]):
                                    show_this = False

                        if show_this:
                            button:
                                hover_sound "audio/sfx/sfx_select.ogg"
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    ShowMenu(l)
                                ]

                                frame:
                                    xminimum 215 xmaximum 400
                                    ysize 87
                                    xalign 0.5 yalign 1.0
                                    padding (20, 0, 20, 0)
                                    
                                    idle_background Frame(get_themed_attribute("button/button"), 10, 10)
                                    hover_background Frame(get_themed_attribute("button/button", prefix="selectable") , 10, 10)

                                    text button_text:
                                        xalign 0.5 yalign 0.5
                                        text_align 0.5
                                        size 64

                                        color gui.text_color
                                        hover_color gui.text_color
    textbutton _("Back"):
        background None
        xoffset 25 yoffset 1000
    
        text_color "#000000"
        text_outlines [(4.5, "#FFFFFF", absolute(0), absolute(0))]

        text_hover_color "#FFFFFF"
        text_hover_outlines [(4.5, "#000000", absolute(0), absolute(0))]
        action Return()
