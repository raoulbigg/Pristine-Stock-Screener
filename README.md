# Pristine Stock Screener

###### stock screener that:

- Gets all US stocks (NYSE and NASDAQ)
- Receives **live** and **past** OHLC data for stocks using Yahoo yfinance lib.
- Calculates moving averages(20ma & 50ma) and bars position.
- Calculates if a retracement is present (LL's or 2-3 consecutive red bars)
- Calculates if prices if above a rising 20ma & 50ma. 
- Plots candlestick graphs using plotly
- Places the graphs in a Flask application

Screenshots of flask site after run of screener.py:
![alt tag](https://github.com/raoulbigg/Pristine-Stock-Screener/blob/master/flask-screenshot.png)

Scrollable
![alt tag](https://github.com/raoulbigg/Pristine-Stock-Screener/blob/master/flask-screenshot1.png)

The filters that the screener scans for are: 

##### (STRONG TREND) Law of Picture Of Power (POP):
	Criteria: 
	 +POP = close > rising 20sma and close >  rising 50sma
	 -POP = close < declining 20sma and close < declining 50sma


##### Price action:
	Criteria: 
	 Calculates if a retracement is present by using the bars OHLC


# How to run:
```
python3 screener.py
cd flaskSite/; flask run
```


