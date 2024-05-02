# Define function to make decision
def decide(symbol, current_price, historical_prices, moving_average, volume, pe_ratio):
    if current_price < min(historical_prices) and volume > 1.5 * moving_average and pe_ratio < 15:
        return "Buy"
    elif current_price > max(historical_prices) and volume > 1.5 * moving_average and pe_ratio > 20:
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

# Make a decision
decision = decide(symbol, current_price, historical_prices, moving_average, volume, pe_ratio)
print(f"The decision for {symbol} at price {current_price} is: {decision}")
