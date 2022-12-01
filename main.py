from tradingview_ta import TA_Handler, Interval
import time

print("Get stock information from TradingView List (https://tvdb.brianthe.dev)")

symbol = input("Enter stock symbol:")
screener = input("Enter stock screener:")
exchange = input("Enter stock exchange:")

while True:
    output = TA_Handler(symbol=symbol, screener=screener, exchange=exchange, interval=Interval.INTERVAL_1_MINUTE)
    buyAmount = output.get_analysis().summary.get("BUY")
    sellAmount = output.get_analysis().summary.get("SELL")
    neutralAmount = output.get_analysis().summary.get("NEUTRAL")

    print(f"Recommendation: Buy: {buyAmount} Sell: {sellAmount} Neutral: {neutralAmount}")

    time.sleep(1)

    input("Press Enter to refresh")
