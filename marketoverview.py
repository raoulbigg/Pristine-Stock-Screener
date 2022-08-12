from EdgeWatch.edgewatch import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()

#Screening for edge
#pairs = open('15m_pairs.txt','r').readlines()
hourly_pairs = open('hourly_pairs.txt','r').readlines()
daily_pairs = open('pairs.txt','r').readlines()

#screener = Screener(tickers=pairs, timeframe="15m").start_stock_screener()
screener = Screener(tickers=hourly_pairs, daily_tickers=daily_pairs, timeframe="1h").start_stock_screener()
