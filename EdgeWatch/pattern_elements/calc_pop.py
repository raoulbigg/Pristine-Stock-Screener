def calc_picture_of_power(data):
	close = data.iloc[0]["Adj Close"]
	medium_sma = data.iloc[0]["SMA_20"]
	long_sma = data.iloc[0]["SMA_50"]

	close1 = data.iloc[1]["Adj Close"]
	medium_sma1 = data.iloc[1]["SMA_20"]
	long_sma1 = data.iloc[1]["SMA_50"]

	#calc +POP
	if medium_sma > long_sma and close > medium_sma:
		if medium_sma > medium_sma1 and close / medium_sma <= 1.4:
			return "up"
	#calc -POP
	elif medium_sma < long_sma and close < medium_sma:
		if medium_sma < medium_sma1 and medium_sma / close <= 1.4:
			return "down"
	return
