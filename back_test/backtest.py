import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from back_test.plot.plot import PlotData
import numpy as np
import time
import json
import os
from warper_mongo.mongo_warper import cursor_tickers


class BackTest(PlotData):
    df = None
    # PD Settings
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    open_ord, close_ord, orders = [], [], []

    # def __init__(self):
    #
    #     self.df = self.csv_profit('back_test/data/PETR4_B_0_Diário.csv')
    # self.df = yf.download(ticker+".SA", period='5y', interval='1d', auto_adjust=True)

    @staticmethod
    def csv_profit(csv):
        colnames = ['Asset', 'Date', 'Open', 'High', 'Low', 'Close', 'Vol_Fin', 'Vol']
        df = pd.read_csv(csv, names=colnames, header=None, sep=';')

        df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
        df = df.set_index(df['Date']).sort_index()

        df = df[['Open', 'High', 'Low', 'Close', 'Vol']].copy()

        df['Open'] = df['Open'].str.replace(',', '.').astype('float')
        df['High'] = df['High'].str.replace(',', '.').astype('float')
        df['Low'] = df['Low'].str.replace(',', '.').astype('float')
        df['Close'] = df['Close'].str.replace(',', '.').astype('float')

        return df

    def build_db(self):

        list_b3 = [
            'https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/search?language=pt-br&governance=16',
            'https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/search?language=pt-br&governance=17',
            'https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/search?language=pt-br&governance=18',
        ]





        # dir_path = './back_test/data/'
        # date = datetime.now().strftime('%Y-%m-%d')
        #
        # # Main LOCAL DB
        # with open('back_test/tickers.json', 'r') as f:
        #     data = json.load(f)
        #
        # for i in data:
        #     new_dict = {
        #         i: {
        #             'name': None,
        #             'month_vol': 0,
        #             'strategy': {},
        #             'last_update': {},
        #         }
        #     }
        #
        #     print(new_dict)
        #
        #     break

        # for i in data:
        #     # TODO: or BIG then X days
        #     if data[i].get('month_vol') == 0:
        #         for f in os.listdir(dir_path):
        #             # Check if the same TICKER and
        #             if i in f:
        #                 print(i)
        #
        #                 """ Open CSV """
        #                 # df = pd.read_csv(f'{dir_path + f}')
        #                 #
        #                 # df = df[-31:-1]
        #                 # df['vol_fin_MM'] = (df.Close * df.Volume) / 1000000
        #                 # avg_vol = df.vol_fin_MM.mean()
        #                 # print(df)
        #
        #     break
        #
        #     # # Download Data from YFINACE
        #     # for tick in data:
        #     #     raw_data = yf.download(tick + '.SA', interval=interval, period=period, auto_adjust=True)
        #     #     raw_data.to_csv(f'back_test/data/{tick}_{interval}_{period}_{date}.csv')

    def media_high_low(self):
        # Number
        med_sup = 10

        # Indicadores
        self.df['med_sup'] = self.df['High'].rolling(med_sup).mean()
        self.df['med_inf'] = self.df['Low'].rolling(med_sup).mean()
        self.df = self.df.round(2)

        # Paramters
        self.df['buy_position'] = 0
        self.df['signal'] = 0

        # PRESET DATE
        # self.df = self.df.loc['2020-10-07':]

        # Logic
        handler_position = False
        for row in self.df.itertuples():

            # Bloco de Entrada
            if not handler_position and row.High > row.med_inf > row.Low:
                self.df.at[row.Index, 'signal'] = 1
                self.df.at[row.Index, 'buy_position'] = 1
                handler_position = True

                self.open_order(row.Index, 100, row.med_inf, 'c')

            if handler_position:
                self.df.at[row.Index, 'buy_position'] = 1

            # Bloco de saida
            if handler_position and row.High > row.med_sup > row.Low:
                self.df.at[row.Index, 'signal'] = 1
                self.df.at[row.Index, 'buy_position'] = 0
                handler_position = False

                self.close_order(row.Index, row.med_sup)

    def open_order(self, _open, _qntd, _preco_compra, lado):
        self.open_ord.append({
            'abertura': _open,
            'fechamento': None,
            'qtd': _qntd,
            'preco_compra': _preco_compra,
            'preco_venda': None,
            'lado': lado,
        })

    def close_order(self, _close, _preco_venda):
        self.close_ord.append({
            'fechamneto': _close,
            'preco_venda': _preco_venda,
        })

    def show_orders(self):
        res = []

        # print(len(self.open_ord))
        # print(len(self.close_ord))

        for i in range(len(self.close_ord)):
            aberutra = self.open_ord[i].get('abertura')
            fechamento = self.close_ord[i].get('fechamneto')
            tempo_op = fechamento - aberutra
            qnt = self.open_ord[i].get('qtd')
            lado = self.open_ord[i].get('lado')
            preco_compra = self.open_ord[i].get('preco_compra')
            preco_venda = self.close_ord[i].get('preco_venda')
            resultado = (preco_venda - preco_compra) * qnt
            resultado_p = (resultado / (preco_compra * qnt)) * 100
            res.append([aberutra, fechamento, tempo_op, qnt, lado, preco_compra, preco_venda, resultado, resultado_p])

        col = ['abertura', 'fechamento', 'tempo', 'qntd', 'lado', 'preco_compra', 'preco_venda', 'resultado', 'p_res']
        df = pd.DataFrame(res, columns=col)
        df = df.round(2)
        df['total'] = df['resultado'].cumsum()
        df.loc[df.resultado > 0, 'operacao'] = 'win'
        df.loc[df.resultado <= 0, 'operacao'] = 'loss'

        # Filter something u want
        mask = df['operacao'].str.contains('loss')
        # print(df[mask])

        return df
