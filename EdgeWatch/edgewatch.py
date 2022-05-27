import requests
from bs4 import BeautifulSoup
from EdgeWatch.marketoverview import get_stocks_day_performance
from EdgeWatch.forex_data.fetch_forex_data import ForexData
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

	def start_forex_screener(self):
		now = datetime.datetime.now()
		while 1 > 0:
			screen = False
			if self.timeframe == "30m":
				if now.now().minute == 25 or now.now().minute == 55:
					screen = self.forexScreener()
			if self.timeframe == "15m":
				if now.now().minute == 13 or now.now().minute == 28 or now.now().minute == 43 or now.now().minute == 58:
					screen = self.forexScreener()	
			if self.timeframe == "1h":
				if now.now().minute == 2:
					screen = self.forexScreener()
			if screen:
				print('----------')
				time.sleep(60)

		time.sleep(3)


	def forexScreener(self):
		#Fetch historical and live forex OHLC
		fx = ForexData()
		print("Fetching OHLC data and screening for edge on ", self.timeframe)
		for ticker in self.tickers:
			data = fx.get_forex_data(ticker, self.timeframe)
			#Calc simple moving averages (8, 20 and 50)
			complete_data = calc_smas(data)
			#Calculate the picture of power
			pop = calc_picture_of_power(complete_data)
			if pop:
				potential_trade = calc_bars_positions(complete_data)
				if potential_trade:
					print("Potential trade found: ", ticker, potential_trade)
		return 1