# Edge-Watch

###### Personal stock/forex/commodity/crypto screener that:


- Receives **live** and **past** OHLC data for stocks using Yahoo yfinance lib.
- calculates moving averages, bars position and moving average distance for each stock. 
- Generates a watchlist.txt file to import in TradingView

The filters that the screener scans for are: 

##### Law of 20ma:
	Description:			
	 The price can't stay long far from the 20ma (Only go long/ short at or near the 20ma).
	 Price can't be far from 20ma

##### Law of Picture Of Power (POP):
	Description: 
	 +POP = 20MA > 50MA AND rising 20ma
	 -POP = 20MA < 50MA AND declining 20ma

##### Price action:
	Description: 
	 Looks if current bar is an engulfing bar
	 Look if current bar > 20ma
	 Look if current bar's close is higher than closes of last 8 bars

