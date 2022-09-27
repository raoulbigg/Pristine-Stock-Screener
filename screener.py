from EdgeWatch.edgewatch import *
from EdgeWatch.marketoverview.symbols import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()

#Get all US markets on Etoro.com
ETORO = Symbols().etoroSymbols()
pairs = Symbols().etoroUS(ETORO)

#Start screener on All mode (calculates POP and priceaction)
screener = Screener(tickers=pairs, timeframe="1d", mode="All").start_stock_screener()
