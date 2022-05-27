from EdgeWatch.edgewatch import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()

#Screening for edge
forex_pairs = open('forexpairs.txt','r').readlines()
screener = Screener(tickers=forex_pairs, timeframe="1h").start_forex_screener()