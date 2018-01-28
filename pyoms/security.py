class Security:

    """Creates a security"""

    def __init__(self, symbol):
        self.symbol = symbol
        self.position = 0
        self.reference_price = 0
        self.locates = 0