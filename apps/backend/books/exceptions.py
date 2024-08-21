class BookNotFoundError(Exception):
    def __init__(self, book_id) -> None:
        super().__init__(f"Book with the given {book_id} doesn't exists")
