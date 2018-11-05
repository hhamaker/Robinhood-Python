import AlphaVantagePositions
#set the symbol
symbol = 'GLOW'
#set the time series
#TIME_SERIES_INTRADAY, TIME_SERIES_DAILY, TIME_SERIES_DAILY_ADJUSTED, TIME_SERIES_WEEKLY
#TIME_SERIES_WEEKLY_ADJUSTED, TIME_SERIES_MONTHLY, TIME_SERIES_MONTHLY_ADJUSTED
time = 'TIME_SERIES_INTRADAY'
#set the interval
#1min, 5min, 15min, 30min, 60min
interval = '5min'

#make the call
stock = AlphaVantagePositions.getPositions(symbol, time, interval)

print(AlphaVantagePositions.printTimeSeries(stock))

