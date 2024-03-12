def calc_picture_of_power(data):
	#Current bar (bar 0)
	close = data.iloc[0]["Close"]
	high = data.iloc[0]["High"]
	low = data.iloc[0]["Low"]
	very_short_sma = data.iloc[0]["SMA_13"]
	short_sma = data.iloc[0]["SMA_20"]
	medium_sma = data.iloc[0]["SMA_50"]

	#Bar 2
	close2 = data.iloc[2]["Close"]
	high2 = data.iloc[2]["High"]
	low2 = data.iloc[2]["Low"]
	short_sma2 = data.iloc[2]["SMA_20"]
	medium_sma2 = data.iloc[2]["SMA_50"]
	

	#calc +POP
	if close > short_sma and close > medium_sma:
		if short_sma > short_sma2 and medium_sma > medium_sma2:
			return "up"

	#calc -POP
	if close < short_sma and close < medium_sma:
		if short_sma < short_sma2 and medium_sma < medium_sma2:
			return "down"

	return
