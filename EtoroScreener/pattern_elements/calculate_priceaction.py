def calc_bars_positions(data, pop, timeframe):

	if timeframe == "1d":	
		current = data.iloc[0]
		barTwo = data.iloc[1]
		barThree = data.iloc[2]
		barFour = data.iloc[3]


	if pop == "up":
		if current["Close"] > current["Open"] and current["Close"] > barTwo["Close"]:
			return "180bar:",current["Close"], "barTwo:", barTwo["Close"]



	if pop == "down":
		if current["Close"] < current["Open"] and current["Close"] < barTwo["Close"]:
			return "180bar:",current["Close"], "barTwo:", barTwo["Close"]