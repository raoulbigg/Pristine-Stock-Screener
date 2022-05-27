import datetime                 # Date acquiring
import pytz                     # Time zone management
import pandas as pd 
import MetaTrader5       as mt5 # Importing OHLC data
import matplotlib.pyplot as plt # Plotting charts
import numpy             as np  # Mostly for array manipulation
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class ForexData(object):

    def __init__(self, ticker, interval):
        if interval == "5m":
            self.timeframe = mt5.TIMEFRAME_M5
        if interval == "15m":
            self.timeframe = mt5.TIMEFRAME_M15
        elif interval == "30m":
            self.timeframe = mt5.TIMEFRAME_M30
        elif interval == "1h":
            self.timeframe = mt5.TIMEFRAME_H1
        self.ticker = ticker

    #Receive historical stock data for ticker
    def get_live_data_mt5(self):

        #now datetime, +2hours because of exchange timezone
        now = datetime.datetime.now(pytz.utc) + datetime.timedelta(hours=2)

        #initialize MT5
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()

        #calculate from date
        utc_from = now - datetime.timedelta(days=7)

        #get bars + live data
        rates = None
        rates = mt5.copy_rates_range(self.ticker, self.timeframe, utc_from, now)
        if rates == None:
            rates = mt5.copy_rates_range(self.ticker, self.timeframe, utc_from, now)
        rates_frame = pd.DataFrame(rates)
        # convert time in seconds into the datetime format
        try:
            rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
            return pd.DataFrame(rates_frame)
        except Exception as e:
            return pd.DataFrame()
        #print(rates_frame)
        #rates_frame.to_csv(ticker+".csv")