from back_test.backtest import BackTest
import yfinance as yf
import pandas as pd

bt = BackTest('PETR4')

bt.media_high_low()
# print(bt.df)
orders = bt.show_orders()
print(orders)

# fig = bt.fig_candlestick(fixrange=True)
# bt.fig_show(fig)

# assets = [
#     'WEGE3', 'EGIE3', 'ITUB4', 'ENBR3', 'EQTL3', 'B3SA3', 'ABEV3', 'FLRY3', 'PSSA3', 'ARZZ3', 'BBDC4', 'RADL3', 'PRIO3',
#     'ITSA4', 'LREN3', 'HYPE3', 'EZTC3', 'TAEE11', 'SLCE3', 'RENT3', 'PNVL3', 'SMTO3', 'BBAS3', 'VIVA3', 'VAMO3',
#     'PARD3', 'PETZ3', 'SAPR11', 'ODPV3', 'MULT3', 'AGRO3', 'TOTS3', 'INTB3', 'LEVE3', 'CSAN3', 'ALUP11', 'VIVT3',
#     'MOVI3', 'TRIS3', 'ENEV3', 'FIQE3', 'KLBN11', 'AMBP3', 'BPAC11', 'SOMA3', 'VBBR3', 'GMAT3', 'SIMH3', 'JHSF3',
#     'CGRA4', 'MATD3', 'MDIA3', 'GRND3', 'BBSE3', 'CAML3', 'SANB11', 'TASA4', 'SULA11', 'CRFB3', 'UNIP6', 'TIMS3',
#     'VALE3', 'TRPL4', 'CPLE6', 'TTEN3', 'SOJA3', 'BLAU3', 'CPFE3', 'GGPS3', 'LOGG3', 'VITT3', 'CYRE3', 'WIZS3', 'RANI3',
#     'AESB3', 'ASAI3', 'CXSE3', 'LAVV3', 'FRAS3', 'AURA33', 'CURY3', 'BOAS3', 'PLPL3', 'CMIG4', 'ROMI3', 'MTRE3',
#     'MLAS3', 'RAPT4', 'LJQQ3', 'CMIN3', 'ENAT3', 'ARML3', 'CARD3', 'JALL3', 'GOAU4', 'LVTC3', 'MGLU3', 'YDUQ3', 'NEOE3',
#     'PTBL3', 'GUAR3', 'HAPV3', 'TUPY3', 'CSMG3', 'SQIA3', 'SUZB3', 'KEPL3', 'MRFG3', 'BMOB3', 'OFSA3', 'JSLG3', 'PETR4',
#     'CLSA3', 'MRVE3', 'FESA4', 'MYPK3', 'BRBI11', 'ALLD3', 'SHUL4', 'SBSP3', 'PORT3', 'VVEO3', 'CIEL3', 'RDOR3',
#     'QUAL3', 'POMO4', 'LWSA3', 'G2DI33', 'DESK3', 'SBFG3', 'BPAN4', 'ESPA3', 'BRIT3', 'ALSO3', 'SYNE3', 'RECV3',
#     'UGPA3', 'POSI3', 'VULC3', 'RAIZ4', 'RAIL3', 'PCAR3', 'USIM5', 'TFCO4', 'ETER3', 'ABCB4', 'ELET3', 'DXCO3', 'GGBR4',
#     'DEXP3', 'BRSR6', 'STBP3', 'MILS3', 'SEER3', 'NTCO3', 'MODL11', 'JBSS3', 'BRML3', 'BEES3', 'BEEF3', 'BRAP4',
#     'NGRD3', 'EVEN3',
# ]
#
# print(len(assets))
