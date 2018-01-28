from pyoms import book, order, config

class OrderManager:

    """ The foundation of this system.  The orderManager must be instantiated on startup to use this platform.
        All order and book handling is done from this object"""

    def __init__(self):
        self.myConfig = config.Config().get_config_section(self.__class__.__name__)
        self.books = {}

    def create_book(self, book_name):
        self.books[book_name] = book.Book(book_name)
