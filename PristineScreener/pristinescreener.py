import requests
from bs4 import BeautifulSoup
import sys
from PristineScreener.marketoverview import get_stocks_day_performance
from PristineScreener.ohlc.fetch_ohlc import StockData
from PristineScreener.ohlc.plot import createChart
from PristineScreener.pattern_elements.calculate_simplemas import *
from PristineScreener.pattern_elements.calc_pop import *
from PristineScreener.pattern_elements.calculate_priceaction import *
import datetime
import time
import os
import json



class MarketOverview(object):

    def todays_markets_overview(self):
        #Calls the get_stock_gainers and losers for the marketoverview
        #stocks_gainers = get_stocks_day_performance.get_stock_gainers()
        #stocks_losers = get_stocks_day_performance.get_stock_losers()
        market_today = datetime.today().strftime('%d-%m-%y')
        ##Print columns with the market overview
        #print('''\n\033[1;36;40m Market overview: \033[0m\n-------------\n''')
        #print("Stocks:")
        #print('{:16s}    {}\n'.format("Top gainers:", "Top losers:"))
        #print("\n".join("{:25s}    {}".format(x, y) for x, y in zip(stocks_gainers, stocks_losers)))
        #print('''---------------------------------\n''')
        return market_today


class Screener: 
    def __init__(self, tickers, timeframe):
        self.tickers = tickers
        self.timeframe = timeframe
        self.now = datetime.datetime.now()
        self.htmlLocation = "/var/www/html/flaskSite/static"
        
    def start_stock_screener(self):
        screen = False
        #Get info on if market is open tomorrow
        self.market_today = MarketOverview().todays_markets_overview()
        #Delete previous market scan .pngs
        if self.timeframe == "1d":
            for file in os.listdir(self.htmlLocation):
                if file.endswith('.png'):
                    os.remove(self.htmlLocation+"/"+file) 
            #Clear stocks500k file
            open("stocks500k.txt", "w")

        if self.timeframe == "1h":
            for file in os.listdir(self.htmlLocation+"/hourly"):
                if file.endswith('.png'):
                    os.remove(self.htmlLocation+"/hourly/"+file) 

        #Start screener
        screen = self.stockScreener()
        if screen:
            self.write_metadata(screen[0], screen[1])


    def stockScreener(self):
        #Fetch historical and live stock OHLC
        list_trades = []
        meta = []
        pops = []
        ohlc = StockData()
        print("\033[1;36;40m Fetching OHLC data and screening for edge on", self.timeframe + "\033[0m")
        for ticker in self.tickers:
            try:
                formatted_ticker = ticker.strip()
                data = ohlc.get_ohlc_data(formatted_ticker, self.timeframe)
                #Calc simple moving averages (8, 20 and 50)
                complete_data = calc_smas(data)
                #Calculate the picture of power
                pop = calc_picture_of_power(complete_data)
                if pop:
                    pops.append(pop.strip())
                    potential_trade = calc_bars_positions(complete_data, pop, self.timeframe)
                    if potential_trade:
                        print("\033[1;33;40m Retracement found: " + ticker.strip() + " " + pop.strip() + "\033[0m")
                        list_trades.append(ticker.strip())
                        meta.append(pop.strip())
                        createChart(complete_data, ticker, self.now, self.htmlLocation, self.timeframe)
            except Exception as e:
                #print(e)
                pass    

        return list_trades, meta, pops


    def write_metadata(self, meta, pops):
        # Data to be written
        dictionary = {
            "data": str(self.now),
            "timeframe": str(self.timeframe),
            "longs": str(meta.count("up")),
            "shorts": str(meta.count("down")),
            "pop_up":str(pops.count("up")),
            "pop_down":str(pops.count("down")),
            "market_today": self.market_today
        }
         
        with open((self.htmlLocation+"/meta{0}.json").format(self.timeframe), "w") as outfile:
            json.dump(dictionary, outfile)
