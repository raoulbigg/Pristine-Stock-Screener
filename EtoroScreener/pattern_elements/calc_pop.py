def calc_picture_of_power(data):
	#Current bar
	close = data.iloc[0]["Close"]
	high = data.iloc[0]["High"]
	low = data.iloc[0]["Low"]
	sma = data.iloc[0]["SMA_8"]
	sma_very_short = data.iloc[0]["SMA_5"]
	short_sma = data.iloc[0]["SMA_20"]
	medium_sma = data.iloc[0]["SMA_40"]

	#Brevious bar
	close1 = data.iloc[1]["Close"]
	high1 = data.iloc[1]["High"]
	low1 = data.iloc[1]["Low"]
	sma1 = data.iloc[1]["SMA_8"]
	sma_very_short1 = data.iloc[1]["SMA_5"]
	short_sma1 = data.iloc[1]["SMA_20"]
	medium_sma1 = data.iloc[1]["SMA_40"]
	

	#calc +POP (if 20ma > r40ma)
	if short_sma > medium_sma and close > medium_sma and medium_sma > medium_sma1:
		return "up"
	#calc -POP (if 20ma < d40ma)
	if short_sma < medium_sma and close < medium_sma and medium_sma < medium_sma1:
		return "down"

	return
