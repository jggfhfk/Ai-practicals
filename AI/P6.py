class StockTradingExpertSystem:
    def __init__(self, symbol, current_price, historical_prices, moving_average, volume, pe_ratio):
        self.symbol = symbol
        self.current_price = current_price
        self.historical_prices = historical_prices
        self.moving_average = moving_average
        self.volume = volume
        self.pe_ratio = pe_ratio

    def decide(self):
        if self.current_price < min(self.historical_prices) and self.volume > 1.5 * self.moving_average and self.pe_ratio < 15:
            return "Buy"
        elif self.current_price > max(self.historical_prices) and self.volume > 1.5 * self.moving_average and self.pe_ratio > 20:
            return "Sell"
        else:
            return "Hold"

# Get input from the user
symbol = input("Enter the stock symbol: ")
current_price = float(input("Enter the current price: "))
historical_prices = list(map(float, input("Enter the historical prices (comma-separated): ").split(',')))
moving_average = float(input("Enter the moving average: "))
volume = int(input("Enter the volume: "))
pe_ratio = float(input("Enter the P/E ratio: "))

# Create the expert system and make a decision
system = StockTradingExpertSystem(symbol, current_price, historical_prices, moving_average, volume, pe_ratio)
decision = system.decide()
print(f"The decision for {symbol} at price {current_price} is: {decision}")
