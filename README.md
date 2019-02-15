# API-Graviex
using the Exchange Crypto Graviex API

# USE
from APIGraviex import APIGraviex
APIGraviex = APIGraviex(Access, Secret)

# Examples
print(APIGraviex.timestamp())
--
    1550236059

print(APIGraviex.market())  
--
    [{'name': 'GIO/BTC', 'id': 'giobtc'},
     {'name': 'GIO/DOGE', 'id': 'giodoge'},
     {'name': 'GIO/LTC', 'id': 'gioltc'},
     {'name': 'GIO/ETH', 'id': 'gioeth'},
     {'name': 'DOGE/BTC', 'id': 'dogebtc'},... ]

print(APIGraviex.tickers())  
--
   'umbbtc': {'volume': '8697.2565', 'api': True, 'quote_fixed': 9, 'volume2': '0.0036848326558', 'base_lot': None, 'base_fixed': 4,           'base_fee': 0.002, 'wstatus': 'on', 'at': 1550236487, 'high': '0.000000715', 'open': '0.000000310', 'quote_unit': 'btc', 'buy':           '0.000000444', 'low': '0.000000306', 'quote_min': '0.00000010', 'base_min': '0.00000010', 'base_unit': 'umb', 'quote_fee': 0.002,        'block_time': '2019-02-15 16:00:30', 'name': 'UMB/BTC', 'sell': '0.000000689', 'quote_lot': None, 'blocks': 58053, 'last':                '0.000000555'}}

print(APIGraviex.ticker('esbcbtc')) 
--
    {'quote_fee': 0.002, 'volume2': '0.472260441616', 'api': True, 'quote_lot': None, 'last': '0.000004537', 'block_time': '2019-02-15 16:17:36', 'base_lot': None, 'blocks': 145600, 'volume': '103540.7109', 'quote_fixed': 9, 'at': 1550236726, 'quote_unit': 'btc', 'low': '0.00000425', 'wstatus': 'on', 'base_fixed': 4, 'buy': '0.000004401', 'base_unit': 'esbc', 'name': 'ESBC/BTC', 'open': '0.000004370', 'base_min': '0.00000010', 'high': '0.000004869', 'sell': '0.000004749', 'quote_min': '0.00000010', 'base_fee': 0.002}

print(APIGraviex.me())  
--
    {'name': None, 'sn': 'PEXYXYXYXYXO', 'accounts_filtered': [{'currency': 'gio', 'name': 'GravioCoin', 'locked': '0.0', 'is_coin':          True, 'balance': '0.0', 'status': 'warning', 'is_purged': False}, {'currency': 'btc', 'name': 'Bitcoin', 'locked': '0.001721694',           'is_coin': True, 'balance': '0.000000000425076', 'status': 'ok', 'is_purged': False},  ...

print(APIGraviex.get_order_market('xmxbtc'))  
--
        [{'state': 'wait', 'ord_type': 'limit', 'id': 20257161, 'price': '0.000003', 'trades_count': 0, 'created_at': '2019-02-             15T12:53:46Z', 'market': 'satcbtc', 'volume': '573.898', 'at': 1550235226, 'side': 'buy', 'remaining_volume': '573.898',                'executed_volume': '0.0', 'avg_price': '0.0'}]

for all order print(APIGraviex.get_order_market('all'))
--

Place order 'buy' or 'sell' : print (APIGraviex.put_orders('satcbtc', 'buy', '7851.5809' , '0.000003300'))
--

Clear orders : print(APIGraviex.clear_orders())
--
