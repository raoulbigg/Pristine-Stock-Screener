# Edge-Watch

###### Personal stock/forex/commodity/crypto screener that:


- Receives **live** and **past** OHLC data for middle to high volume (500k+) stocks using Yahoo yfinance lib.
- calculates moving averages, bars position and moving average distance for each stock. 
- Fires an alert using [Notify.run](notify.run) when price action matches trade criteria.

The filters that the screener scans for are: 

##### Law of 20ma:
	Description:			
	 The price can't stay long far from the 20ma (Only go long/ short at or near the 20ma).
	 Price can't be far from 20ma


##### Law of the contraction/expansion:
	Description: 
	 Only enter at the beginning of a marathon (the start of an expansion phase after a contraction phase).
	 price needs to breakout/breakdown/retest to initialise a new move


##### Law of Picture Of Power (POP):
	Description: 
	 +POP = 8MA > 20MA > 50MA
	 -POP = 8MA < 20MA < 50MA

##### Price action:
	Description: 
	 Looks if current bar is breaking out/ retesting and is an engulfing bar

