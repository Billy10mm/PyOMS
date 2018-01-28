from pyoms import config

class Book:

    """ The Book is automatically instantiated by the Order Manager and is accessible by the client.
        This allows the client and the OrderManager to interact directly with the order book"""

    LIMITS = ['GrossLong', 'GrossShort', 'DollarVolumeDaily']

    def __init__(self, book_name):
        self.book_name = book_name
        self.myConfig = config.Config().get_config_section(self.__class__.__name__)
        self.orders = {}
        self.positions = {}
        self.config_folder = self.myConfig['BookConfigFolder']
        self.bookConfig = config.Config(self.config_folder + '/{}.cfg'.format(self.book_name))
        [setattr(self, self.bookConfig.get_config('RISKLIMITS', limit), 0) for limit in LIMITS]

    def rem_order(self, order):
        """Removes an order from the order book"""
        del self.orders[order.id]

    def create_order(self, **kwargs):
        """ Creates a new order.  Parameters can be passed it when calling it, or using constructors after the fact"""
        new_order = order.Order()
        self.book.add_order(new_order)
        return new_order.id