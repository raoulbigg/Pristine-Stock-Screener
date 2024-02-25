from PristineScreener.pristinescreener import *
from PristineScreener.marketoverview.symbols import *
import datetime
import time


#Get all US markets for 1d scan
USsymbols = Symbols().USsymbols()

#Get 500k+ US markets for 1h scan
USstocks500k = Symbols().stocks500k()

while 1 > 0:
	now = datetime.datetime.now()

	#Start 1d screener
	if (now.now().hour == 21 and now.now().minute == 59):
		screener = Screener(tickers=USsymbols, timeframe="1d").start_stock_screener()

	#Start 1h screener
	if (now.now().hour == 16 and now.now().minute == 1 or
		now.now().hour == 17 and now.now().minute == 1 or
		now.now().hour == 18 and now.now().minute == 1):
		screener = Screener(tickers=USstocks500k, timeframe="1h").start_stock_screener()	
	time.sleep(60)
#screener takes ~30min to finish
