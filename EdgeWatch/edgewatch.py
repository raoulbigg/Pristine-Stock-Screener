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
import json

class MarketOverview(object):

	def todays_markets_overview(self):
		#Calls the get_stock_gainers and losers for the marketoverview
		stocks_gainers = get_stocks_day_performance.get_stock_gainers()
		stocks_losers = get_stocks_day_performance.get_stock_losers()
		#Print columns with the market overview
		print('''\n\033[1;36;40m Market overview: \033[0m\n-------------\n''')
		print("Stocks:")
		print('{:16s}    {}\n'.format("Top gainers:", "Top losers:"))
		print("\n".join("{:25s}    {}".format(x, y) for x, y in zip(stocks_gainers, stocks_losers)))
		print('''---------------------------------\n''')



class Screener(object):
	def __init__(self, tickers, daily_tickers, timeframe):

		self.tickers = tickers
		self.daily_tickers = daily_tickers
		self.timeframe = timeframe

	def start_stock_screener(self):
		trade_hours = [16, 17, 18]
		trade_hours2 = [20]
		while 1 > 0:
			now = datetime.datetime.now()
			screen = False
			if self.timeframe == "1d":
				screen = self.stockScreener()
			if self.timeframe == "1h":
				if now.now().hour in trade_hours and now.now().minute == 12:
					screen = self.stockScreener()
				elif now.now().hour == 21 and now.now().minute == 10:
					self.timeframe = "1d"
					screen = self.stockScreener()
			if self.timeframe == "15m":
				if now.now().hour in trade_hours2 and now.now().minute % 15 == 0:
					screen = self.stockScreener()

			if screen:
				jsonD = json.dumps({self.timeframe: {"tickers": screen, "end_time": str(now)}})
				jsonFile = open("potential_trades.json", "w")
				jsonFile.write(jsonD)
				jsonFile.close()
				print('----------')
				if self.timeframe == "1d":
					sys.exit()
				time.sleep(50)
		time.sleep(3)


	def stockScreener(self):
		#Fetch historical and live stock OHLC
		list_trades = []
		ohlc = StockData()
		print("\033[1;36;40m Fetching OHLC data and screening for edge on", self.timeframe + "\033[0m")
		if self.timeframe == "1d":
			tickers = self.daily_tickers
		elif self.timeframe == "1h":
			tickers = self.tickers
		for ticker in tickers:
			try:
				formatted_ticker = ticker.split(":")[1].strip()
				data = ohlc.get_ohlc_data(formatted_ticker, self.timeframe)
				#Calc simple moving averages (20, 50 and 200)
				complete_data = calc_smas(data)
				#Calculate the picture of power
				pop = calc_picture_of_power(complete_data)
				if pop:
					potential_trade = calc_bars_positions(complete_data, pop, self.timeframe)
					if potential_trade:
						print("\033[1;33;40m Potential trade found: " + ticker.strip() + " " + pop.strip() + "\033[0m")
						list_trades.append(ticker.strip())
			except (AttributeError, IndexError, UnboundLocalError) as e:
				pass
		return list_trades
