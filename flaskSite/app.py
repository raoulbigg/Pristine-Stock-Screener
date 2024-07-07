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


if __name__ == '__main__':
    app.run(host="192.168.1.98")
