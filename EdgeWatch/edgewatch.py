import requests
from bs4 import BeautifulSoup
import sys
from EdgeWatch.marketoverview import get_stocks_day_performance
from EdgeWatch.ohlc.fetch_ohlc import StockData
from EdgeWatch.pattern_elements.calculate_simplemas import *
from EdgeWatch.pattern_elements.calc_pop import *
from EdgeWatch.pattern_elements.calculate_priceaction import *
import datetime
import time

class MarketOverview(object):

	def todays_markets_overview(self):
		#Calls the get_stock_gainers and losers for the marketoverview
		stocks_gainers = get_stocks_day_performance.get_stock_gainers()
		stocks_losers = get_stocks_day_performance.get_stock_losers()
		#Print columns with the market overview
		print('''\nMarket overview:\n-------------\n''')
		print("Stocks:")
		print('{:16s}    {}\n'.format("Top gainers:", "Top losers:"))
		print("\n".join("{:25s}    {}".format(x, y) for x, y in zip(stocks_gainers, stocks_losers)))
		print('''---------------------------------\n''')



class Screener(object):
	def __init__(self, tickers, timeframe):
		self.tickers = tickers
		self.timeframe = timeframe

	def start_stock_screener(self):
		now = datetime.datetime.now()
		trade_hours = [16, 17, 18]
		while 1 > 0:
			screen = False
			if self.timeframe == "1d":
				screen = self.stockScreener()
				sys.exit()
			if self.timeframe == "1h":
				if now.now().hour in trade_hours and now.now().minute == 15:
					screen = self.stockScreener()
			if screen:
				print('----------')
				time.sleep(50)
		time.sleep(3)


	def stockScreener(self):
		#Fetch historical and live forex OHLC
		ohlc = StockData()
		print("Fetching OHLC data and screening for edge on", self.timeframe)
		for ticker in self.tickers:
			try:
				data = ohlc.get_ohlc_data(ticker, self.timeframe)
				#Calc simple moving averages (8, 20 and 50)
				complete_data = calc_smas(data)
				#Calculate the picture of power
				pop = calc_picture_of_power(complete_data)
				if pop:
					potential_trade = calc_bars_positions(complete_data, pop)
					if potential_trade:
						print("\x1b[33;20m Potential trade found: " + ticker.strip() + " " + pop.strip() + "\033[0m")
			except (AttributeError, IndexError) as e:
				pass
		return 1