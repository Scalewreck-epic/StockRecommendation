from tradingview_ta import TA_Handler, Interval
import time

print("Get stock information from TradingView List (https://tvdb.brianthe.dev)")

symbol = input("Enter stock symbol:")
screener = input("Enter stock screener:")
exchange = input("Enter stock exchange:")

while True:
    output_minute = TA_Handler(symbol=symbol, screener=screener, exchange=exchange, interval=Interval.INTERVAL_1_MINUTE)

    recommendation = output_minute.get_analysis().summary.get("RECOMMENDATION")
    buy = output_minute.get_analysis().summary.get("BUY")
    sell = output_minute.get_analysis().summary.get("SELL")
    neutral = output_minute.get_analysis().summary.get("NEUTRAL")

    print(f"Recommendation: {recommendation} Buy: {buy} Sell: {sell}, Neutral: {neutral}")

    print("Refreshes in 1 minute")
    time.sleep(60)
