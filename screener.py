from EdgeWatch.edgewatch import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()


pairs = open('pairs.txt','r').readlines()
screener = Screener(tickers=pairs, timeframe="1d").start_stock_screener()
