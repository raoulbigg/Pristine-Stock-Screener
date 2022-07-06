def calc_picture_of_power(data):
	close = data.iloc[0]["Close"]
	short_sma = data.iloc[0]["SMA_20"]
	medium_sma = data.iloc[0]["SMA_50"]
	long_sma = data.iloc[0]["SMA_200"]

	close1 = data.iloc[1]["Close"]
	short_sma1 = data.iloc[1]["SMA_20"]
	medium_sma1 = data.iloc[1]["SMA_50"]
	long_sma1 = data.iloc[1]["SMA_200"]
	

	#calc +POP
	if short_sma > long_sma and medium_sma > long_sma and close > short_sma:
		if medium_sma > medium_sma1 and close / medium_sma <= 1.4:
			return "up"
	#calc -POP
	elif short_sma < long_sma and medium_sma < long_sma and close < short_sma:
		if medium_sma < medium_sma1 and medium_sma / close <= 1.4:
			return "down"
	return
