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
    def __init__(self, tickers,timeframe, mode):

        self.tickers = tickers
        self.timeframe = timeframe
        self.mode = mode

    def start_stock_screener(self):
        while 1 > 0:
            now = datetime.datetime.now()
            screen = False
            #if now.now().hour == 21 and now.now().minute == 10:
            screen = self.stockScreener()
            #Write to watchlist for TradingView
            if screen:
                with open("/var/www/html/potential_trades.txt", mode="w") as file:
                    file.write(", ".join(screen))
                print('----------')
                if self.timeframe == "1d":
                    sys.exit()
            time.sleep(3)


    def stockScreener(self):
        #Fetch historical and live stock OHLC
        list_trades = []
        ohlc = StockData()
        print("\033[1;36;40m Fetching OHLC data and screening for edge on", self.timeframe + "\033[0m")
        for ticker in self.tickers:
            try:
                formatted_ticker = ticker.split(":")[1].strip()
                data = ohlc.get_ohlc_data(formatted_ticker, self.timeframe)
                #Calc simple moving averages (8, 20 and 50)
                complete_data = calc_smas(data)
                #Calculate the picture of power
                pop = calc_picture_of_power(complete_data)
                if pop:
                    #If mode is all then look for PA
                    if self.mode == "All":
                        potential_trade = calc_bars_positions(complete_data, pop, self.timeframe)
                        if potential_trade:
                            print("\033[1;33;40m Potential trade found: " + ticker.strip() + " " + pop.strip() + "\033[0m")
                            list_trades.append(ticker.strip())
                    #If mode is MA then only calc POP
                    elif self.mode == "movingAverages":
                        print("\033[1;33;40m POP found: " + ticker.strip() + " " + pop.strip() + "\033[0m")
                        list_trades.append(ticker.strip())                        
            except (AttributeError, IndexError, UnboundLocalError) as e:
                pass
        return list_trades
