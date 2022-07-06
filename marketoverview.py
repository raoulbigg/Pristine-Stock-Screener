from EdgeWatch.edgewatch import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()

#Screening for edge
pairs = open('pairs.txt','r').readlines()
screener = Screener(tickers=pairs, timeframe="1h").start_stock_screener()