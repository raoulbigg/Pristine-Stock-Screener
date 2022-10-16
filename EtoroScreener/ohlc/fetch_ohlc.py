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
        if interval == "1d":
            data = yf.Ticker(ticker.strip()).history(interval='1d', period='90d')
        if interval == "2h":
            data = yf.Ticker(ticker.strip()).history(interval='90m', period='40d')
        try:
            return data
        except Exception as e:
            pass
        #print(rates_frame)
        #rates_frame.to_csv(ticker+".csv")
