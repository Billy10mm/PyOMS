from pyoms import book, order, config

class OrderManager:

    """ The foundation of this system.  The orderManager must be instantiated on startup to use this platform.
        All order and book handling is done from this object"""

    def __init__(self):
        self.myConfig = config.Config().get_config_section(self.__class__.__name__)
        self.book = book.Book()

    def create_order(self, **kwargs):
        """ Creates a new order.  Parameters can be passed it when calling it, or using constructors after the fact"""
        new_order = order.Order()
        self.book.add_order(new_order)
        return new_order.id
