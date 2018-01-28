from pyoms import config, order

class Book:

    """A Book is an account. You must name it as you instantiate it via the Order Manager."""

    LIMITS = ['GrossLong', 'GrossShort', 'DollarVolumeDaily']

    def __init__(self, book_name):
        self.book_name = book_name
        self.orders = {}
        self.positions = {}
        self.myConfig = config.Config().get_config_section(self.__class__.__name__)
        self.config_folder = self.myConfig['BookConfigFolder']
        self.bookConfig = config.Config(self.config_folder + '/{}.cfg'.format(self.book_name))
        [setattr(self, self.bookConfig.get_config('RiskLimits', limit), 0) for limit in self.LIMITS]

    def create_order(self):
        """ Creates a new order."""
        new_order = order.Order()
        self.orders[new_order.id] = new_order
        return new_order.id