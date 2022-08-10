from EdgeWatch.edgewatch import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()

#Screening for edge
#pairs = open('15m_pairs.txt','r').readlines()
pairs = open('pairs.txt','r').readlines()

#screener = Screener(tickers=pairs, timeframe="15m").start_stock_screener()
screener = Screener(tickers=pairs, timeframe="1d").start_stock_screener()
