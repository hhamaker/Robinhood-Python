import RobinhoodGetQuote
import RobinhoodAuthentication
import RobinhoodAccount
import RobinhoodMarket
import RobinhoodPositions
import RobinhoodOrders
import RobinhoodInstruments

#testing section
#gets a quote for a passed in symbol
stock = RobinhoodGetQuote.getQuote("GLOW")
print(stock["symbol"])
print(stock["ask_price"])
print(stock["bid_price"])
print(stock["last_trade_price"])

#gets Login Token
token = RobinhoodAuthentication.getloginToken()
print(token)

#gets the markets in Robinhood
#markets = RobinhoodMarket.getMarkets()
#print(markets)

#gets MarketHours for the MIC passed in.
#marketHours = RobinhoodMarket.getMarketHours('XNYS')
#print(marketHours["opens_at"])
#print(marketHours["closes_at"])

#gets account information
#account = RobinhoodAccount.getAccountInfo(token)
#print(account["results"][0]["account_number"])
#print(account["results"])

#testing instrument call
#instrument = RobinhoodInstruments.getInstrument("ZNGA")
#print(instrument["results"][0]["url"])

#gets all the positions
#positions = RobinhoodPositions.getPositions(token)
#RobinhoodPositions.getCurrentStocks(token)

'''
symbol = "CHK"
type = "limit"
time_in_force = "gtc"
trigger = "immediate"
price = "0.35"
quantity = 1
side = "buy"
'''
#this is the long form makeOrder Method
#order = RobinhoodOrders.makeOrder(token, symbol, type, time_in_force, trigger, price, quantity, side)

quantity = 1
price = "0.50"
#smaller order Method
token  = RobinhoodAuthentication.getloginToken2()
order = RobinhoodOrders.makeLimitOrderNow(token, "ZNGA", quantity, price, "buy")
print(order["id"])

#checkOrder = RobinhoodOrders.checkOrder(token, '8c3e3199-5605-46fe-bd58-8f24ee6aa31f')
#print(checkOrder)

#cancelOrder = RobinhoodOrders.cancelOrder(token, '8c3e3199-5605-46fe-bd58-8f24ee6aa31f')
#print(cancelOrder)

#logs out
#RobinhoodAuthentication.logOut(token)
