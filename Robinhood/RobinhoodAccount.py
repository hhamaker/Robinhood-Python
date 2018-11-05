import requests
import json

#makes a get call to robinhood quotes to get the stock info
def getAccountInfo(token):
    url = 'https://api.robinhood.com/accounts/'
    content = requests.get(url, headers = {"Authorization" : "Bearer " + token})
    return json.loads(content.text)

def getAccountURL(token):
    url = 'https://api.robinhood.com/accounts/'
    content = requests.get(url, headers = {"Authorization" : "Bearer " + token})
    account = json.loads(content["results"][0]["url"])
    accountURL = account["results"][0]["url"]
    return accountURL

class Account(object):
    def __init__(self, next, results, previous):
        self.next = next
        self.results = json.loads(results.text)
        self.previous = previous

class results(object):
    def __init__(self, deactivated, updated_at, margin_balances, cash_balances, withdrawal_halted,
    cash_available_for_withdrawal, type, sma, sweep_enabled, deposit_halted, buying_power,
    user, max_ach_early_access_amount, cash_held_for_orders, only_position_closing_trades,
    url, positions, created_at, cash, sma_held_for_orders, account_number, uncleared_deposits,
    unsettled_funds, nummus_enabled):
        self.deactivated = deactivated
        self.updated_at = updated_at
        self.margin_balances = json.loads(margin_balances.text)
        self.cash_balances = cash_balances
        self.withdrawal_halted = withdrawal_halted
        self.cash_available_for_withdrawal = cash_available_for_withdrawal
        self.type = type
        self.sma = sma
        self.sweep_enabled = sweep_enabled
        self.deposit_halted = deposit_halted
        self.buying_power = buying_power
        self.user = user
        self.max_ach_early_access_amount = max_ach_early_access_amount
        self.cash_held_for_orders = cash_held_for_orders
        self.only_position_closing_trades = only_position_closing_trades
        self.url = url
        self.positions = positions
        self.created_at = created_at
        self.cash = cash
        self.sma_held_for_orders = sma_held_for_orders
        self.account_number = account_number
        self.uncleared_deposits = uncleared_deposits
        self.unsettled_funds = unsettled_funds
        self.nummus_enabled = nummus_enabled

class margin_balances(object):
    def __init__(self, updated_at, gold_equity_requirement, outstanding_interest, cash_held_for_options_collateral,
        uncleared_nummus_deposits, overnight_ratio, day_trade_buying_power,
        cash_available_for_withdrawal, sma, cash_held_for_nummus_restrictions, marked_pattern_day_trader_date, 
        unallocated_margin_cash, start_of_day_dtbp, overnight_buying_power_held_for_orders, day_trade_ratio,
        cash_held_for_orders, unsettled_debit, created_at, cash_held_for_dividends, cash, start_of_day_overnight_buying_power,
        margin_limit, overnight_buying_power, uncleared_deposits, unsettled_funds, day_trade_buying_power_held_for_orders):
        self.updated_at = updated_at
        self.gold_equity_requirement = gold_equity_requirement
        self.outstanding_interest = outstanding_interest
        self.cash_held_for_options_collateral = cash_held_for_options_collateral
        self.uncleared_nummus_deposits = uncleared_nummus_deposits
        self.overnight_ratio = overnight_ratio
        self.day_trade_buying_power = day_trade_buying_power
        self.cash_available_for_withdrawal = cash_available_for_withdrawal
        self.sma = sma
        self.cash_held_for_nummus_restrictions = cash_held_for_nummus_restrictions
        self.marked_pattern_day_trader_date = marked_pattern_day_trader_date
        self.unallocated_margin_cash = unallocated_margin_cash
        self.start_of_day_dtbp = start_of_day_dtbp
        self.overnight_buying_power_held_for_orders = overnight_buying_power_held_for_orders
        self.day_trade_ratio = day_trade_ratio
        self.cash_held_for_orders = cash_held_for_orders
        self.unsettled_debit = unsettled_debit
        self.created_at = created_at
        self.cash_held_for_dividends = cash_held_for_dividends
        self.cash = cash
        self.start_of_day_overnight_buying_power = start_of_day_overnight_buying_power
        self.margin_limit = margin_limit
        self.overnight_buying_power = overnight_buying_power
        self.uncleared_deposits = uncleared_deposits
        self.unsettled_funds = unsettled_funds
        self.day_trade_buying_power_held_for_orders = day_trade_buying_power_held_for_orders


#makes a get call to robinhood quotes to get the stock info
def getUserInfo(token):
    url = 'https://api.robinhood.com/User/'
    content = requests.get(url, headers = {"Authorization":"Token " + token})
    return json.loads(content.text)

class User(object):
    def __init__(self, username, first_name, last_name, id_info, url, basic_info, email,
    investment_profile, id, international_info, employment, additional_info):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.id_info = id_info
        self.url = url
        self.basic_info = basic_info
        self.email = email
        self.investment_profile = investment_profile
        self.id = id
        self.international_info = international_info
        self.employment = employment
        self.additional_info = additional_info

