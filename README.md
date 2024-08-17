# Pristine Stock Screener

###### stock screener that:

- Gets all US stocks (NYSE and NASDAQ).
- Receives **live** and **past** OHLC data for stocks using Yahoo yfinance lib.
- Calculates moving averages(20ma & 50ma).
- Calculates if prices if above a rising 20ma & 50ma. 
- Plots candlestick graphs using plotly.
- Places the graphs in a Flask application.

Screenshots of flask site after run of screener.py:
![alt tag](https://github.com/raoulbigg/Pristine-Stock-Screener/blob/master/flask-screenshot.png)

Scrollable
![alt tag](https://github.com/raoulbigg/Pristine-Stock-Screener/blob/master/flask-screenshot1.png)


# How to run:
```
python3 screener.py
cd flaskSite/; flask run
```


