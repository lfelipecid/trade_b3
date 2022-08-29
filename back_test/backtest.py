import yfinance as yf
import pandas as pd


class BackTest:

    ticker = None
    med_sup = 10

    # pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    def __init__(self, ticker, interval):
        self.ticker = ticker
        self.interval = interval

    def media_high_low(self):
        df = self.extract_data()
        df['med_sup'] = df['High'].rolling(10).mean()
        df['med_inf'] = df['Low'].rolling(10).mean()
        df = df.round(2)


        print(df)

    def extract_data(self):
        raw_data = yf.download(self.ticker, star=None, end=None, period=None, interval=self.interval)
        raw_data = raw_data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
        return raw_data


