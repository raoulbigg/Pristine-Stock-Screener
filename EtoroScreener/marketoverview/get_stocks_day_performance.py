import requests
from bs4 import BeautifulSoup

def get_stock_gainers():
    top_winners = []
    url = "https://finance.yahoo.com/gainers"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="lxml")
    percentages = soup.find_all('fin-streamer', {'data-field':'regularMarketChangePercent'})
    for percent in percentages:
        if "=" not in percent["data-symbol"]:
            top_winners.append(percent["data-symbol"] +' \033[92m'+ percent.get_text()+'\033[0m')
    return top_winners

def get_stock_losers():
    top_losers = []
    url = "https://finance.yahoo.com/losers"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="lxml")
    percentages = soup.find_all('fin-streamer', {'data-field':'regularMarketChangePercent'})
    for percent in percentages:
        if "=" not in percent["data-symbol"]:
            top_losers.append(percent["data-symbol"] +' \033[91m'+ percent.get_text()+'\033[0m')
    return top_losers
