def calc_picture_of_power(data):
	close = data.iloc[0]["Close"]
	sma = data.iloc[0]["SMA_8"]
	short_sma = data.iloc[0]["SMA_20"]
	medium_sma = data.iloc[0]["SMA_40"]

	close1 = data.iloc[1]["Close"]
	sma1 = data.iloc[1]["SMA_8"]
	short_sma1 = data.iloc[1]["SMA_20"]
	medium_sma1 = data.iloc[1]["SMA_40"]
	

	#calc +POP (if 20ma > 40ma)
	if short_sma > medium_sma:
		return "up"
	#calc -POP (if 20ma < 40ma)
	if short_sma < medium_sma:
		return "down"

	return
