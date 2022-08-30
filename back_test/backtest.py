import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from back_test.plot.plot import PlotData
import numpy as np
import time


class BackTest(PlotData):
    med_sup = 10

    # PD Settings
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    def __init__(self, ticker, interval, period):
        self.ticker = ticker
        self.interval = interval
        self.period = period  # 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        self.df = self.extract_data()

    def media_high_low(self):

        # Indicadores
        self.df['med_sup'] = self.df['High'].rolling(10).mean()
        self.df['med_inf'] = self.df['Low'].rolling(10).mean()
        self.df = self.df.round(2)

        # Paramters
        self.df['buy_position'] = 0
        self.df['signal'] = 0

        # Logic
        buy_position = 0
        for row in self.df.itertuples():

            # buy_position = False
            #
            # # Bloco de Entrada
            # if buy_position is False and row.Low < row.med_inf < row.High:
            #     self.df.at[row.Index, 'signal'] = 1
            #     self.df.at[row.Index, 'buyPosition'] = 1
            #     buy_position = True
            #
            # if buy_position is True and row.High > row.med_sup < row.Low:
            #     pass
            #
            # # Bloco de Saida
            print(row.buy_position)
            time.sleep(0.5)


    def get_period(self):
        pass

    def extract_data(self):
        raw_data = yf.download(self.ticker, period='1y', interval=self.interval, auto_adjust=True)
        raw_data = raw_data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

        return raw_data
