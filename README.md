```
# Binance Futures Order Filling Script

This script allows you to fill an order on Binance Futures based on a set of technical indicators. It continuously monitors the market, calculates the indicators, and executes a buy order when specific conditions are met.

## Prerequisites
- Python 3.x
- `python-binance` package (install using `pip install python-binance`)
- `ta` (Technical Analysis Library) package (install using `pip install ta`)

## Setup

1. Clone the repository or download the script directly.

2. Install the required packages by running the following command:
   ```
   pip install python-binance ta
   ```

3. Obtain Binance API credentials:
   - Visit the Binance website and create an account if you don't have one.
   - Enable Futures trading in your account.
   - Generate an API key and secret with the required permissions.

4. Replace the placeholders in the script with your API key and secret:
   ```python
   api_key = 'YOUR_API_KEY'
   api_secret = 'YOUR_API_SECRET'
   ```

## Usage

To run the script, execute the following command:
```
python fill_order.py
```

The script will start monitoring the market based on the specified indicators and conditions. If the criteria for a buy signal are met, it will execute a market order with the specified leverage, stop loss, and take profit levels.

## Customization

You can customize the script by adjusting the following parameters:

- `symbol`: The trading pair symbol on Binance Futures (e.g., 'BTCUSDT', 'ETHUSDT').
- `leverage`: The leverage amount to be used for the order.
- `interval`: The time interval for checking the indicators (in minutes).
- `order_type`: The order type (defaulted to `ORDER_TYPE_MARKET`).
- `take_profit_percentage`: The percentage above the current price to set as the take profit level.
- `stop_loss_percentage`: The percentage below the current price to set as the stop loss level.
- `ema1_length`: The length of the first EMA indicator.
- `ema2_length`: The length of the second EMA indicator.
- `macd_fast_length`: The length of the fast length for MACD calculation.
- `macd_slow_length`: The length of the slow length for MACD calculation.
- `macd_signal_smooth`: The smoothing factor for the MACD signal line.

Feel free to modify these parameters according to your trading strategy and requirements.

## Disclaimer

This script is provided for educational and informational purposes only. Use it at your own risk. Trading involves risks, and past performance is not indicative of future results. Make sure to thoroughly test and validate any trading strategy before using it with real funds.

## License

This script is released under the MIT License.
```
