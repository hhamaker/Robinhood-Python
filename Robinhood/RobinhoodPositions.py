import requests
import json

#gets current stocks that the account owner has
def getCurrentStocks(token):
    url = 'https://api.robinhood.com/positions/'
    content = requests.get(url, headers = {"Authorization" : "Token " + token})
    positions = json.loads(content.text)
    for result in positions["results"]:
        #determines if you currently have stocks
        if(result["quantity"] != "0.0000"):    
            print(getStockInfo(result["instrument"])["symbol"] + " " + result["quantity"] + " " + result["pending_average_buy_price"])


#makes a get call to robinhood quotes to get the stock info
def getPositions(token):
    url = 'https://api.robinhood.com/positions/'
    content = requests.get(url, headers = {"Authorization" : "Token " + token})
    return json.loads(content.text)

class Positions(object):
    def __init__(self, next, results, previous):
        self.next = next
        self.results = json.loads(results.text)
        self.previous = previous

class results(object):
    def __init__(self, shares_held_for_stock_grants, account, pending_average_buy_price, 
        shares_held_for_options_events, intraday_average_buy_price, url, shares_held_for_options_collateral, 
        created_at, updated_at, shares_held_for_buys, average_buy_price, instrument, intraday_quantity, 
        shares_held_for_sells, shares_pending_from_options_events, quantity):
        self.shares_held_for_stock_grants = shares_held_for_stock_grants
        self.account = account
        self.pending_average_buy_price = pending_average_buy_price
        self.shares_held_for_options_events = shares_held_for_options_events
        self.intraday_average_buy_price = intraday_average_buy_price
        self.url = url
        self.shares_held_for_options_collateral = shares_held_for_options_collateral
        self.created_at = created_at
        self.updated_at = updated_at
        self.shares_held_for_buys = shares_held_for_buys
        self.average_buy_price = average_buy_price
        self.instrument = instrument
        self.intraday_quantity = intraday_quantity
        self.shares_held_for_sells = shares_held_for_sells
        self.shares_pending_from_options_events = shares_pending_from_options_events
        self.quantity = quantity

def getStockInfo(instrumentURL):
    content = requests.get(instrumentURL)
    return json.loads(content.text)

class stock(object):
    def __init__(self, tradable_chain_id, min_tick_size, type, splits, margin_initial_ratio, 
        url, quote, tradability, bloomberg_unique, list_date, name, symbol, fundamentals, 
        state, country, day_trade_ratio, tradeable, maintenance_ratio, id, market, simple_name):
        self.tradable_chain_id = tradable_chain_id
        self.min_tick_size = min_tick_size
        self.type = type
        self.splits = splits
        self.margin_initial_ratio = margin_initial_ratio
        self.url = url
        self.quote = quote
        self.tradability = tradability
        self.bloomberg_unique = bloomberg_unique
        self.list_date = list_date
        self.name = name
        self.symbol = symbol
        self.fundamentals = fundamentals
        self.state = state
        self.country = country
        self.day_trade_ratio = day_trade_ratio
        self.tradeable = tradeable
        self.maintenance_ratio = maintenance_ratio
        self.id = id
        self.market = market
        self.simple_name = simple_name

def getSymbolFromInstrument(instrumentURL):
    content = requests.get(instrumentURL)
    return json.loads(content["symbol"])
