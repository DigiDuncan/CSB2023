python early:
    import re
    import json

    with renpy.open_file("data/books.json") as json_file:
         books_file = json.load(json_file)

    global books_map
    bookshelf = []
    books_map = books_file

    # default spine size is 300x46
    class Book:
        def __init__(self, book_id: str, title: str, description: str, jump_label: str, spine_width: int, spine_height: int, x_pos: int, y_pos: int):
            self.book_id = book_id
            self.title = title
            self.description = description
            self.jump_label = jump_label
            self.spine_width = spine_width
            self.spine_height = spine_height
            self.x_pos = x_pos
            self.y_pos = y_pos

            self.spine = f"gui/books/{book_id}/side.png"
            self.hover_spine = f"gui/books/{book_id}/hover.png"
            self.front = f"gui/books/{book_id}/cover.png"

    for book in books_map:

        # only show the book if's unlocked
        # default is unlocked
        this_unlocked = True

        # TODO: idk why this doesn't work, it's literally taken from timeline that uses the same tech
        # unlock by label, will probably add more conditions later
        if "need_label" in books_map[book] and renpy.seen_label(books_map[book]["need_label"]) == False:
            this_unlocked = False

        # append to shelf if unlocked
        if this_unlocked == True:
            bookshelf.append(Book(book, books_map[book]["title"], books_map[book]["desc"], books_map[book]["jump_to"], books_map[book]["spine_width"], books_map[book]["spine_height"], books_map[book]["x_pos"], books_map[book]["y_pos"]))

style subgame_return is button:
    # this is the closest thing to a blank line i can do here, but the tag needs to exist or it'll crash - tate
    background None

# TODO: make this prettier later
style subgame_return_text is text:
    color "#000000"
    outlines [(5, "#FFFFFF", absolute(0), absolute(0))]

    hover_color "#FFFFFF"
    hover_outlines [(5, "#000000", absolute(0), absolute(0))]

screen subgame():
    tag menu
    image "gui/subgame_menu.png"

    for book in bookshelf:
        imagebutton:
            hover book.hover_spine
            idle book.spine
            action SetVariable("current_subgame_name", book.title), SetVariable("current_subgame_desc", book.description), SetVariable("current_subgame_art", book.front), SetVariable("current_subgame_label", book.jump_label)
            xpos book.x_pos
            ypos book.y_pos

    if current_subgame_name:
        # Name of the game
        $ info_x_pos = 1425
        text current_subgame_name:
            color Color("#FFFFFF")
            outlines [(5, "#000000", absolute(0), absolute(0))]
            size 72
            xanchor 0.5
            xpos info_x_pos
            ypos 40
        # Description of the game
        text current_subgame_desc:
            color Color("#FFFFFF")
            outlines [(5, "#000000", absolute(0), absolute(0))]
            # TODO: make this center-align properly on longer text
            xanchor 0.5
            xpos info_x_pos
            ypos 120
        # Display the book image
        image current_subgame_art:
            xanchor 0.5
            yanchor 0.5
            xpos info_x_pos
            ypos 600
        imagebutton:
            idle "gui/play_button.png"
            xanchor 0.5
            xpos info_x_pos
            ypos 925
            hover_sound "audio/sfx/sfx_select.ogg"
            action [ Play("sound", "audio/sfx/sfx_valid.ogg"), Start(current_subgame_label) ]

    textbutton "Main Menu":
        style "subgame_return"
        action Return()
        yoffset 1000
        xoffset 25
