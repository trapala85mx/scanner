#pip install python-binance
from binance.client import Client
import pandas as pd


api_key=''
api_secret=''

client=Client(api_key=api_key, api_secret=api_secret)

pd.set_option("display.max_rows", None, "display.max_columns", None)

monedas=[]


futures_exchange_info = client.futures_ticker()
#se le insertan los parametros a buscar, con USDT, volumen  y precio de la misma
for element in futures_exchange_info:
    if 'USDT' in element['symbol'] and float(element['quoteVolume'])>200000000.00 and float(element['lastPrice'])<5:
        monedas.append(element)

# Te agrego en un list comprehension y te hago una anotación
# en ves de usar 'USDT' in element['symbol'] usa element['symbol'][-4:] == 'USDT'
# monedas = [element['symbol'] for element in futures_exchange_info if element['symbol'][-4:] == 'USDT' and float(element['quoteVolume'])>200000000.00 and float(element['lastPrice'])<5]

ticker_dataframe = pd.DataFrame(monedas)
ticker_dataframe=ticker_dataframe[['symbol','lastPrice','quoteVolume']]
ticker_dataframe=ticker_dataframe.sort_values(by='quoteVolume',ascending=True)
ticker_dataframe=ticker_dataframe.reset_index(drop=True)
print(ticker_dataframe)
