def calc_bars_positions(data, pop, timeframe):

	current = data.iloc[0]
	barOne = data.iloc[1]
	barTwo = data.iloc[2]
	barThree = data.iloc[3]


	if pop == "up":
		#Calc retracement
		if barOne["Close"] < barOne["Open"] and barTwo["Close"] < barTwo["Open"] and barThree["Close"] < barThree["Open"]:
			return True


	if pop == "down":
		#Calc retracement
		if barOne["Close"] > barOne["Open"] and barTwo["Close"] > barTwo["Open"] and barThree["Close"] > barThree["Open"]:
			return True

