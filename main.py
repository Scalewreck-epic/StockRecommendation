from tradingview_ta import TA_Handler, Interval
from datetime import datetime as dt, timedelta as td
import time

print("Get stock information from TradingView List (https://tvdb.brianthe.dev)")

symbol = input("Enter stock symbol:")
screener = input("Enter stock screener:")
exchange = input("Enter stock exchange:")

def get_minute_trade():
    output = TA_Handler(symbol=symbol, screener=screener, exchange=exchange,
                        interval=Interval.INTERVAL_1_MINUTE).get_analysis().summary
    return output


def get_hour_trade():
    output = TA_Handler(symbol=symbol, screener=screener, exchange=exchange,
                        interval=Interval.INTERVAL_1_HOUR).get_analysis().summary
    return output


def get_day_trade():
    output = TA_Handler(symbol=symbol, screener=screener, exchange=exchange,
                        interval=Interval.INTERVAL_1_DAY).get_analysis().summary
    return output


while True:
    output_minute = get_minute_trade()
    output_hour = get_hour_trade()
    output_day = get_day_trade()

    recommendation_minute = output_minute.get("RECOMMENDATION")
    buy_minute = output_minute.get("BUY")
    sell_minute = output_minute.get("SELL")

    recommendation_hour = output_minute.get("RECOMMENDATION")
    buy_hour = output_minute.get("BUY")
    sell_hour = output_minute.get("SELL")

    recommendation_day = output_minute.get("RECOMMENDATION")
    buy_day = output_minute.get("BUY")
    sell_day = output_minute.get("SELL")

    print(f"{symbol} {dt.today() + td(minutes=1)} {recommendation_minute}:  Buy: {buy_minute} Sell: {sell_minute}")
    print(f"{symbol} {dt.today() + td(hours=1)} {recommendation_hour}: Buy: {buy_hour} Sell: {sell_hour}")
    print(f"{symbol} {dt.today() + td(days=1)} {recommendation_day}: Buy: {buy_day} Sell: {sell_day}")

    time.sleep(1)
    input("Press Enter to refresh")
