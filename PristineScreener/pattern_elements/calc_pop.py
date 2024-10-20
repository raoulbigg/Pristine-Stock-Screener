def calc_picture_of_power(data):
	#Current bar (bar 0)
	close = data.iloc[0]["Close"]
	high = data.iloc[0]["High"]
	low = data.iloc[0]["Low"]
	very_short_sma = data.iloc[0]["SMA_10"]
	short_sma = data.iloc[0]["SMA_20"]
	medium_sma = data.iloc[0]["SMA_40"]

	#Bar 2
	close2 = data.iloc[2]["Close"]
	high2 = data.iloc[2]["High"]
	low2 = data.iloc[2]["Low"]
	very_short_sma2 = data.iloc[2]["SMA_10"]
	short_sma2 = data.iloc[2]["SMA_20"]
	medium_sma2 = data.iloc[2]["SMA_40"]

	#calc +POP
	if close > short_sma and very_short_sma >= short_sma and short_sma >= medium_sma:
		if short_sma > short_sma2 and very_short_sma > very_short_sma2 and medium_sma > medium_sma2:
			return "up"

	#calc -POP
	if close < short_sma and very_short_sma < short_sma and short_sma <= medium_sma:
		if short_sma < short_sma2 and very_short_sma < very_short_sma2 and medium_sma < medium_sma2:
			return "down"

	return
