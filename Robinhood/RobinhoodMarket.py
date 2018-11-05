import requests
import json
import time
import datetime

def getMarkets():
    url = 'https://api.robinhood.com/markets/'
    content = requests.get(url)
    return json.loads(content.text)

def getMarketHours(mic):
    url = 'https://api.robinhood.com/markets/' + mic + '/hours/' + time.strftime("%Y-%m-%d")
    content = requests.get(url)
    return json.loads(content.text)

def isMarketOpen(mic):
    #get the hours
    url = 'https://api.robinhood.com/markets/' + mic + '/hours/' + time.strftime("%Y-%m-%d")
    content = requests.get(url)
    market = json.loads(content.text)
    #set the variables needed
    isOpen = False
    openTime = convertTime(market["extended_opens_at"])
    print(str(openTime))
    closeTime = convertTime(market["extended_closes_at"])
    print(str(closeTime))
    now = time.time()
    print(str(now))
    #check to see if now is between the extended hours
    if openTime != None and closeTime != None:
        if (now >= openTime and now < closeTime):
            isOpen = True
    return isOpen

def isMarketOpen2(market):
    #set the variables needed
    isOpen = False
    openTime = convertTime(market["extended_opens_at"])
    print(str(openTime))
    closeTime = convertTime(market["extended_closes_at"])
    print(str(closeTime))
    now = time.time()
    print(str(now))
    #check to see if now is between the extended hours
    if openTime != None and closeTime != None:
        if (now >= openTime and now < closeTime):
            isOpen = True
    return isOpen

def convertTime(timeToConvert):
    #replace the T's :'s and Z's
    if type(timeToConvert) is str:
        timeToConvert = timeToConvert.replace("T", "-")
        timeToConvert = timeToConvert.replace(":", "-")
        timeToConvert = timeToConvert.replace("Z", "")
        stringArray = timeToConvert.split("-")
        timestamp = datetime.datetime(int(stringArray[0]), int(stringArray[1]), int(stringArray[2]), 
            int(stringArray[3]), int(stringArray[4])).timestamp()
    else:
        return None
    return timestamp

class MarketResponse:
    def __init__(self, website, city, name, url, country, todays_hours, operating_mic,
        acronym, timezone, mic):
        self.website = website
        self.city = city
        self.name = name
        self.url = url
        self.country = country
        self.todays_hours = todays_hours
        self.operating_mic = operating_mic
        self.acronym = acronym
        self.timezone = timezone
        self.mic = mic

class MarketHoursResponse:
    def __init__(self, closes_at, extended_opens_at, next_open_hours, previous_open_hours,
        is_open, extended_closes_at, date, opens_at):
        self.closes_at = closes_at
        self.extended_opens_at = extended_opens_at
        self.next_open_hours = next_open_hours
        self.previous_open_hours = previous_open_hours
        self.is_open = is_open
        self.extended_closes_at = extended_closes_at
        self.date = date
        self.opens_at = opens_at        