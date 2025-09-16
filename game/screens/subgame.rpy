screen subgame():
    tag menu
    # Make the background of the thing
    # TODO: Make a book object
    python:
        books = []
    image "gui/subgame_menu.png"
    for book in books:
        imagebutton:
            hover book.hover_spine
            idle book.spine
