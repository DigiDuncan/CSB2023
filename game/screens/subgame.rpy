python early:
    class Book:
        def __init__(self, book_id: str, title: str, description: str, jump_label: str):
            self.book_id = book_id
            self.title = title
            self.description = description
            self.jump_label = jump_label

            self.spine = f"gui/books/{book_id}/side.png"
            self.hover_spine = f"gui/books/{book_id}/hover.png"
            self.front = f"gui/books/{book_id}/cover.png"

    books = [
        # Each are 46 wide and 300 tall
        Book("ce", "CSBounciness: Christmas Edition", "jingle jingle ho ho ho", "ce_start"),
        Book("sp", "CSBounciness: Space Program", "spaaaaaaaaaace", "secret_dx"),
        Book("pt", "Celestial Sightseeing", "The Aspiring Planeswalker's Guide To\nChronomancy, Synchrony, & Cosmic Safety", "book_celestial_sightseeing")
    ]

screen subgame():
    tag menu
    image "gui/subgame_menu.png"
    # Defines where the first book will be
    $ x_pos = 864
    $ y_pos = 390
    for book in books:
        imagebutton:
            hover book.hover_spine
            idle book.spine
            action SetVariable("current_subgame_name", book.title), SetVariable("current_subgame_desc", book.description), SetVariable("current_subgame_art", book.front), SetVariable("current_subgame_label", book.jump_label)
            xpos x_pos
            ypos y_pos
        # Spaces things out by a hardcoded number (This is just the book width + 4)
        $ x_pos = x_pos - 50

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
            action Start(current_subgame_label)

    # TODO: make this match the rest of the page later
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
