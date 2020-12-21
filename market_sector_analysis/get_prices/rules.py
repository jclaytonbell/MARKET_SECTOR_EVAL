

class Prices:

    def __init__(self, source):
        """Instantiate Prices class"""
        self.source = source

    def get_stock_price(self, stock):
        """Get the current price of a stock."""
        if not self.validate_stock(stock):
            price = 100
            #fill in get price method
            return price

    def get_sector_price(self, sector):
        """Sum the current prices of all stocks in the sector."""
        return sum([self.get_stock_price(stock) for stock in sector.stocks])

    def get_tsm_price(self):
        """Return the current price of the Vanguard Total Stock Market Index Fund"""
        price = 200
        # fill in get price method
        return price

    def get_sp500_price(self):
        """Return the current price of the Vanguard S&P 500 Index Fund"""
        price = 500
        # fill in the get price method
        return price

    def validate_stock(self, stock):
        """Validate stock object"""
        return True