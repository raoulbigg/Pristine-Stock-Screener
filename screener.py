from EtoroScreener.etoroscreener import *
from EtoroScreener.marketoverview.symbols import *

#Stock market overview
Marketoverview = MarketOverview().todays_markets_overview()

#Get all US markets on Etoro.com
symbols = Symbols()
ETOROsymbols = symbols.etoroSymbols()
USpairs = symbols.etoroUS(ETOROsymbols)

#Start screener
screener = Screener(tickers=USpairs, timeframe="1d").start_stock_screener()

#screener takes ~14min to finish