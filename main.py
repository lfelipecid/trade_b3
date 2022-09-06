from back_test.backtest import BackTest
import yfinance as yf
import pandas as pd
import json

bt = BackTest()
bt.download_data()


# bt.media_high_low()
# # print(bt.df)
# orders = bt.show_orders()
# print(orders)

# fig = bt.fig_candlestick(fixrange=True)
# bt.fig_show(fig)

