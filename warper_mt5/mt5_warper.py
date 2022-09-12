from ssl import ALERT_DESCRIPTION_PROTOCOL_VERSION
from turtle import clear
import pandas as pd
from datetime import datetime as dt
import time
import MetaTrader5 as mt5

if not mt5.initialize():
    print('Fail')
    mt5.shutdown()


# Total de ALERT_DESCRIPTION_PROTOCOL_VERSION
# ativos = mt5.symbols_get()
# print(len(ativos))

# for i in range(10):
#     print(ativos[i].name)

# asset = mt5.copy_rates_from_pos('PETR4', mt5.TIMEFRAME_M1, 0, 1)


def get_ohlc(ativo, timeframe, n=5):
    ativo = mt5.copy_rates_from_pos(ativo, timeframe, 0, n)
    ativo = pd.DataFrame(ativo)
    ativo['time'] = pd.to_datetime(ativo['time'], unit='s')
    ativo.set_index('time', inplace=True)

    return ativo
    

# print(get_ohlc("PETR4", mt5.TIMEFRAME_M1))

# print(mt5.symbol_info_tick('PETR4'))

tempo = time.time() + 5

while time.time() < tempo:
    tick = mt5.symbol_info_tick('PETR4')
    print(f'QUOTE {tick.last}, bid: {tick.bid}, ask: {tick.ask}')
    time.sleep(0.5)
