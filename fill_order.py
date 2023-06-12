from binance.client import Client
from binance.enums import *
import ta
import time

def fill_order(api_key, api_secret, symbol):
    # Create a Binance Futures client
    client = Client(api_key, api_secret, futures=True)

    # Set the leverage
    leverage = 2

    # Set the time interval for checking indicators (in minutes)
    interval = '5m'

    # Set the order type and parameters
    order_type = ORDER_TYPE_MARKET
    take_profit_percentage = 0.05
    stop_loss_percentage = -0.03

    # Start an infinite loop to continuously check the indicators
    while True:
        try:
            # Fetch the candlestick data
            candles = client.futures_klines(symbol=symbol, interval=interval)

            # Extract the closing prices from the candlestick data
            closes = [float(candle[4]) for candle in candles]

            # Calculate the EMA indicators
            ema1_length = 50
            ema2_length = 100
            ema1 = ta.trend.ema_indicator(closes, window=ema1_length)
            ema2 = ta.trend.ema_indicator(closes, window=ema2_length)

            # Calculate the MACD indicator
            macd_fast_length = 6
            macd_slow_length = 13
            macd_signal_smooth = 4
            macd, macd_signal, _ = ta.trend.MACD(closes, n_fast=macd_fast_length,
                                                n_slow=macd_slow_length, n_sign=macd_signal_smooth)

            # Check for buy signal
            if ema1[-1] > ema2[-1] and macd[-1] > macd_signal[-1] and macd[-2] < macd_signal[-2]:
                # Get the current price
                current_price = float(closes[-1])

                # Calculate take profit and stop loss prices
                take_profit_price = current_price * (1 + take_profit_percentage)
                stop_loss_price = current_price * (1 + stop_loss_percentage)

                # Place the buy order
                order = client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY,
                    type=order_type,
                    quantity=leverage,
                    positionSide=POSITION_SIDE_LONG,
                    stopPrice=stop_loss_price,
                    closePosition=True,
                    takeProfitPrice=take_profit_price
                )

                # Print the order details
                print("Buy order placed successfully!")
                print("Order ID:", order['orderId'])
                print("Symbol:", order['symbol'])
                print("Side:", order['side'])
                print("Price:", order['price'])
                print("Quantity:", order['origQty'])
                print("Take Profit:", take_profit_price)
                print("Stop Loss:", stop_loss_price)

                # Break the loop after placing the order
                break

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Wait for a specific duration before checking the indicators again
        time.sleep(300)  # 5 minutes (adjust as per your requirements)

# Example usage
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR
