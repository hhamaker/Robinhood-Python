import requests
import json
import AlphaVantageCredentials

def getPositions(symbol, time, interval):
    apiKey = AlphaVantageCredentials.getApiKey()
    endpoint = 'https://www.alphavantage.co/query?'
    url = endpoint + 'function=' + time + '&symbol=' + symbol + '&interval=' + interval + '&apikey=' + apiKey
    content = requests.get(url)
    returnString = parseCrappyJSON(content.text)
    return json.loads(returnString)

def parseCrappyJSON(jsonString):
    jsonString = jsonString.replace("1. ", "")
    jsonString = jsonString.replace("2. ", "")
    jsonString = jsonString.replace("3. ", "")
    jsonString = jsonString.replace("4. ", "")
    jsonString = jsonString.replace("5. ", "")
    jsonString = jsonString.replace("6. ", "")
    jsonString = jsonString.replace(" (1min)", "")
    jsonString = jsonString.replace(" (5min)", "")
    jsonString = jsonString.replace(" (15min)", "")
    jsonString = jsonString.replace(" (30min)", "")
    jsonString = jsonString.replace(" (60min)", "")
    jsonString = jsonString.replace(" ", "_")
    jsonString = jsonString.replace("____", "   ")
    jsonString = jsonString.replace(":_", ": ")
    return jsonString

def printTimeSeries(jsonString):
    keys = jsonString["Time_Series"].keys()

    for key in keys:
        values = json.loads(key)
        for value in values:
            print("open = " + value)
    

class AlphaVantageCall(object):
    def __init__(self, Meta_Data, Time_Series):
        self.Meta_Data = json.loads(Meta_Data.text)
        self.Time_Series = json.loads(Time_Series.text)

class Meta_Data(object):
    def __init__(self, Information, Symbol, Last_Refreshed, Interval, Output_Size, Time_Zone):
        self.Information = Information
        self.Symbol = Symbol
        self.Last_Refreshed = Last_Refreshed
        self.Interval = Interval
        self.Output_Size = Output_Size
        self.Time_Zone = Time_Zone

class Time(object):
    def __init__(self,open, high, low, close, volume):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

class Time_Series(object):
    def __init__(self, Time):
        self.Time = json.loads(Time.text)
