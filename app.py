from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/15m')
def quart():
    jsonFile = open("potential_trades.json")
    data = json.load(jsonFile)
    return render_template('index.html', tickers=data["15m"], timeframe="15m", interval="15")

@app.route('/hourly')
def hourly():
    jsonFile = open("potential_trades.json")
    data = json.load(jsonFile)
    return render_template('index.html', tickers=data["1h"], timeframe="hourly", interval="60")

@app.route('/daily')
def daily():
    jsonFile = open("potential_trades.json")
    data = json.load(jsonFile)
    return render_template('index.html', tickers=data["1d"], timeframe="daily", interval="D")
