from EdgeWatch.edgewatch import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()


daily_pairs = open('pairs.txt','r').readlines()
screener = Screener(daily_tickers=daily_pairs, timeframe="1d").start_stock_screener()
