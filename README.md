# Etoro-Screener

###### stock/forex/commodity/crypto screener that:

- Gets all US stocks from **Etoro** (NYSE and NASDAQ)
- Receives **live** and **past** OHLC data for Etoro stocks using Yahoo yfinance lib.
- Calculates moving averages, bars position and moving average distance for each stock. 
- Generates a potential_trades.txt with symbols if below criteria are met (Can be imported in TradingView)

The filters that the screener scans for are: 

##### (STRONG TREND) Law of Picture Of Power (POP):
	Criteria: 
	 +POP = rising 20sma > rising 40sma
	 -POP = declining 20sma < declining 40sma


##### Price action:
	Criteria: 
	 Looks if current bar is an engulfing bar
	 Looks if current bar closes in a VOID 
	 	(VOID = momentum move to the left == few to none reference points to supply or demand. Means that there is room for price to go)



# How to run:
```
python3 screener.py
```
