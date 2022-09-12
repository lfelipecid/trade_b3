from pymongo import MongoClient


def cursor_tickers():
    client = MongoClient('mongodb+srv://felipecid:Fyrfdt53@cluster0.n3hgr.mongodb.net/?retryWrites=true&w=majority')
    db = client.get_database('quant')
    collection = db['tickers']
    return collection
