from back_test.backtest import BackTest
import yfinance as yf
import pandas as pd

# bt = BackTest("PETR4.SA", "1d", "1y")
#
# bt.media_high_low()
# print(bt.df)

# fig = bt.fig_candlestick(fixrange=True)
# bt.fig_show(fig)

# from datetime import datetime, timedelta
# data = datetime.now() - timedelta(days=365)
# print(data)

# petr4 = yf.download('PETR4.SA', interval='1d', period='1y', auto_adjust=True)
# print(petr4.tail(50))


ticker = pd.read_csv('back_test/data/PETR4_B_0_Diário.csv')
# ticker =