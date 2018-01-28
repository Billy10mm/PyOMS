class Security:

    """Creates a security"""

    def __init__(self, symbol):
        self.symbol = symbol
        self.position = 0
        self.reference_price = 0
        self.locates = 0
        self.ticker = symbol

    def set_position(self, position):
        self.position = position

    def add_quantity(self, quantity):
        self.position += quantity

    def rem_quantity(self, quantity):
        self.position -= quantity
