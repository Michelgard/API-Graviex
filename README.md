# API-Graviex
using the Exchange Crypto Graviex API

# USE
from APIGraviex import APIGraviex
APIGraviex = APIGraviex(Access, Secret)

# Example
print(APIGraviex.timestamp())
    1550236059

print(APIGraviex.market())
    [{'name': 'GIO/BTC', 'id': 'giobtc'},
     {'name': 'GIO/DOGE', 'id': 'giodoge'},
     {'name': 'GIO/LTC', 'id': 'gioltc'},
     {'name': 'GIO/ETH', 'id': 'gioeth'},
     {'name': 'DOGE/BTC', 'id': 'dogebtc'},... ]


print(APIGraviex.tickers())
print(APIGraviex.ticker('esbcbtc'))
print(APIGraviex.me())
