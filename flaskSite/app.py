from flask import Flask, render_template, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    images = []
    for file in os.listdir('static'):
        if file.endswith('.png'):
            images.append(file)
    meta = open("static/meta1d.json")
    meta_json = json.load(meta)
    print(meta_json)
    return render_template('index.html', images=images, meta=meta_json, mode="screen", img_src="static")

@app.route('/hourly')
def hourly():
    images = []
    for file in os.listdir('static/hourly'):
        if file.endswith('.png'):
            images.append(file)
    meta = open("static/meta1h.json")
    meta_json = json.load(meta)
    print(meta_json)
    return render_template('index.html', images=images, meta=meta_json, mode="screen", img_src="static/hourly")

@app.route('/watchlist', methods=['POST'])
def watchlist():
    images = []


    x = request.form['tickers'].replace(' ', '')
    tickers_list = list(x.split(","))
    for ticker in tickers_list:
        images.append(ticker+".png")

    return render_template('index.html', images=images, mode="watchlist")


if __name__ == '__main__':
    app.run(host="0.0.0.0")