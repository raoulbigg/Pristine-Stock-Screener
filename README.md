# Etoro-Screener

###### stock/forex/commodity/crypto screener that:

- Gets all US stocks from **Etoro** (NYSE and NASDAQ)
- Receives **live** and **past** OHLC data for Etoro stocks using Yahoo yfinance lib.
- Calculates moving averages, bars position and moving average distance for each stock. 
- Generates a potential_trades.txt with symbols if below criteria are met (Can be imported in TradingView)

The filters that the screener scans for are: 

##### (STRONG TREND) Law of Picture Of Power (POP):
	Description: 
	 +POP = 8MA > 20MA and 20MA > 40MA AND rising 20ma
	 -POP = 8MA < 20MA and 20MA < 40MA AND declining 20ma


##### (POTENTIAL BREAKOUT) Price action:
	Description: 
	 Looks if current bar is an engulfing bar
	 Look if current bar > 20ma
	 Look if current bar's close is higher than closes of last 5 bars


##### (OVERSOLD/ OVERBOUGHT) Law of 20ma:
	Description:			
	 The price can't stay long far from the 20ma (Only go long/ short at or near the 20ma).
	 Price can't be far from 20ma



# How to run:
```
python3 screener.py
```
