import requests
import json
class Instrument(object):
    def __init__(self, next, results, previous):
        self.next = next
        self.results = json.loads(results.text)
        self.previous = previous

class results():
    def __init__(self,min_tick_size,splits,margin_initial_ratio,url,quote,symbol,
        bloomberg_unique,list_date,fundamentals,state,country,day_trade_ratio,tradeable,
        maintenance_ratio,id,market,name):
        self.min_tick_size = min_tick_size
        self.splits = splits
        self.margin_initial_ratio = margin_initial_ratio
        self.url = url
        self.quote = quote
        self.symbol = symbol
        self.bloomberg_unique = bloomberg_unique
        self.list_date = list_date
        self.fundamentals = fundamentals
        self.state = state
        self.country = country
        self.day_trade_ratio = day_trade_ratio
        self.tradeable = tradeable
        self.maintenance_ratio = maintenance_ratio
        self.id = id
        self.market = market
        self.name = name

def getInstrument(symbol):
    url = 'https://api.robinhood.com/instruments/?symbol=' + symbol
    content = requests.get(url)
    return json.loads(content.text)
