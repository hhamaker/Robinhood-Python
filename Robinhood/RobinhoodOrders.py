import requests
import json
import RobinhoodPositions
import RobinhoodInstruments
import RobinhoodAccount

def makeOrder(token, account, symbol, type, time_in_force, trigger, price, 
    quantity, side):
    url = 'https://api.robinhood.com/orders/'
    #get the symbol from the instrument
    instrument = RobinhoodInstruments.getInstrument(symbol)
    instrumentURL = instrument["results"][0]["url"]

    #get the account from the token
    account = RobinhoodAccount.getAccountInfo(token)
    accountURL = account["results"][0]["url"]

    content = requests.post(url, headers = {"Authorization" : "Token " + token},
        data = {"account":accountURL, "instrument":instrumentURL, "symbol":symbol, "type":type,
        "time_in_force":time_in_force, "trigger":trigger, "price":price, 
        "quantity":quantity, "side":side})
    return json.loads(content.text)

#RobinhoodOrders.makeLimitOrderNow(token, "CHK", quantity, price, "BUY")
def makeLimitOrderNow(token, symbol, quantity, price, side):
    #set the url
    url = 'https://api.robinhood.com/orders/'
    #get the instrument from the symbol
    instrument = RobinhoodInstruments.getInstrument(symbol)
    instrumentURL = instrument["results"][0]["url"]
    #get the account from the token
    account = RobinhoodAccount.getAccountInfo(token)
    accountURL = account["results"][0]["url"]

    content = requests.post(url, headers = {"Authorization" : "Token " + token},
        data = {"account":accountURL, "instrument":instrumentURL, "symbol":symbol, "type":"limit",
        "time_in_force":"gtc", "trigger":"immediate", "price":price, 
        "quantity":quantity, "side":side})
    print(content.text)
    return json.loads(content.text)

def checkOrder(token, orderId):
    url = 'https://api.robinhood.com/orders/' + orderId
    content = requests.post(url, headers = {"Authorization" : "Token " + token})
    return json.loads(content.text)

def cancelOrder(token, orderId):
    url = 'https://api.robinhood.com/orders/' + orderId + '/cancel/'
    content = requests.post(url, headers = {"Authorization" : "Token " + token})
    return json.loads(content.text)

class order():
    def __init__(self, updated_at, executions, time_in_force, fees, cancel, id, 
        cumulative_quantity, stop_price, reject_reason, instrument, state, trigger, type,
        override_dtbp_checks, last_transaction_at, price, client_id, extended_hours, account,
        url, created_at, side, override_day_trade_checks, position, average_price, quantity):
        self.updated_at = updated_at
        self.executions = executions
        self.time_in_force = time_in_force
        self.fees = fees
        self.cancel = cancel
        self.id = id
        self.cumulative_quantity = cumulative_quantity
        self.stop_price = stop_price
        self.reject_reason = reject_reason
        self.instrument = instrument
        self.state = state
        self.trigger = trigger
        self.type = type
        self.override_dtbp_checks = override_dtbp_checks
        self.last_transaction_at = last_transaction_at
        self.price = price
        self.client_id = client_id
        self.extended_hours = extended_hours
        self.account = account
        self.url = url
        self.created_at = created_at
        self.side = side
        self.override_day_trade_checks = override_day_trade_checks
        self.position = position
        self.average_price = average_price
        self.quantity = quantity

class orderInfo():
    def __init__(self, updated_at, ref_id, time_in_force, fees, cancel, id, cumulative_quantity,
        stop_price, reject_reason, instrument, state, trigger, type, last_transaction_at, price,
        executions, extended_hours, account, url, created_at, side, position, average_price,
        quantity, override_day_trade_checks, override_dtbp_checks):
        self.updated_at = updated_at
        self.ref_id = ref_id
        self.time_in_force = time_in_force
        self.fees = fees
        self.cancel = cancel
        self.id = id
        self.cumulative_quantity = cumulative_quantity
        self.stop_price = stop_price
        self.reject_reason = reject_reason
        self.instrument = instrument
        self.state = state
        self.trigger = trigger
        self.type = type
        self.last_transaction_at = last_transaction_at
        self.price = price
        self.executions = executions
        self.extended_hours = extended_hours
        self.account = account
        self.url = url
        self.side = side
        self.position = position
        self.average_price = average_price
        self.quantity = quantity
        self.override_day_trade_checks = override_day_trade_checks
        self.override_dtbp_checks = override_dtbp_checks        