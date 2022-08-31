from back_test.backtest import BackTest
import yfinance as yf
import pandas as pd

bt = BackTest()

bt.media_high_low()
orders = bt.show_orders()
print(orders)

# fig = bt.fig_candlestick(fixrange=True)
# bt.fig_show(fig)


