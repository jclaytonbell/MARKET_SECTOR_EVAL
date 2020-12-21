"""Define object classes"""

# region Imports

# endregion

# region Define Class Objects

class Base_Object:
    """Base object class."""

    def __init__(self, name):
        """Instantiate Base_Object class"""
        self.name = name

    def get_name(self):
        """Returns the name of the object"""
        return self.name

class Stock(Base_Object):
    """A class to define individual stocks."""

    def __init__(self, stock_name, ticker_symbol, exchange_name, price):
        """Instantiate Stock class"""
        Base_Object.__init__(self, stock_name)
        self.ticker_symbol = ticker_symbol
        self.exchange = exchange_name
        self.price = price

    def get_price(self):
        """Returns the current stock price."""
        return self.price

class Sector(Base_Object):
    """A class to define market sector objects."""

    def __init__(self, sector_name, stocks):
        """Instantiate Sector class"""
        Base_Object.__init__(self, sector_name)
        self.stocks = stocks
