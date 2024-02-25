import datetime                 # Date acquiring
import pytz                     # Time zone management
import pandas as pd 
import matplotlib.pyplot as plt # Plotting charts
import numpy             as np  # Mostly for array manipulation
import warnings
import yfinance as yf
warnings.simplefilter(action='ignore', category=FutureWarning)

class StockData(object):


    #Receive historical stock data for ticker
    def get_ohlc_data(self, ticker, interval):
        data = []
        
        #If 1 day screen
        if interval == "1d":
            data = yf.Ticker(ticker.strip()).history(interval='1d', period='90d')
            #If yesterdays volume is less then 100k: pass
            if data[::-1].iloc[1]["Volume"] > 100000:
                #Append ticker to file for 1h screens
                if data[::-1].iloc[1]["Volume"] > 500000:
                    with open("stocks500k.txt", "a") as f:
                        f.write(ticker+"\n")
                try:
                    return data
                except Exception as e:
                    pass

        #If 1h screen
        if interval == "1h":
            data = yf.Ticker(ticker.strip()).history(interval='1h', period='20d')
            try:
                return data
            except Exception as e:
                pass

