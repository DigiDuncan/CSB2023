python early:
    class Book:
        def __init__(self, book_id: str, title: str, description: str, jump_label: str):
            self.book_id = book_id
            self.title = title
            self.description = description
            self.jump_label = jump_label

            self.spine = f"gui/books/{book_id}_side.png"
            self.hover_spine = f"gui/books/{book_id}_side_hover.png"
            self.front = f"gui/books/{book_id}.png"

    books = [
        Book("ce_book", "CSBounciness: Christmas Edition", "jingle jingle ho ho ho", "ce_start"),
        Book("sp_book", "CSBounciness: Space Program", "spaaaaaaaaaace", "secret_dx")
    ]

screen subgame():
    tag menu
    # Make the background of the thing
    # TODO: Make a book object
    image "gui/subgame_menu.png"
    for book in books:
        imagebutton:
            hover book.hover_spine
            idle book.spine
