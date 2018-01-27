from pyoms import config

class Book:

    """ The Book is automatically instantiated by the Order Manager and is accessible by the client.
        This allows the client and the OrderManager to interact directly with the order book"""

    def __init__(self):
        self.myConfig = config.Config().get_config_section(self.__class__.__name__)
        self._open_orders = []
        self.orders = {}

    def add_order(self, order):
        """Adds an order to the order book"""
        self.orders[order.id] = order

    def rem_order(self, order):
        """Removes an order from the order book"""
        del self.orders[order.id]