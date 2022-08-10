def calc_bars_positions(data, pop, timeframe):

	if timeframe == "1d":	
		current = data.iloc[0]
		barTwo = data.iloc[1]
		barThree = data.iloc[2]
		barFour = data.iloc[3]	

	if timeframe == "1h":	
		current = data.iloc[1]
		barTwo = data.iloc[2]
		barThree = data.iloc[3]
		barFour = data.iloc[4]	


	if pop == "up":
		countUP = 0
		for i in range(10):
			if i != 0:
				if current["Close"] > data.iloc[i]["Close"] and current["Close"] > data.iloc[i]["Open"]:
					countUP = countUP + 1
		if countUP >= 8:
			if current["Close"] > current["Open"] and current["Close"] > barTwo["Close"] and barTwo["Close"] < barThree["Close"] and barTwo["Close"] < barThree["Open"]:
				return "180bar:",current["Close"], "barTwo:", barTwo["Close"]


	if pop == "down":
		countDOWN = 0
		for i in range(10):
			if i != 0:
				if current["Close"] < data.iloc[i]["Close"] and current["Close"] < data.iloc[i]["Open"]:
					countDOWN = countDOWN + 1
		if countDOWN >= 8:
			if current["Close"] < current["Open"] and current["Close"] < barTwo["Close"] and barTwo["Close"] > barThree["Close"] and barTwo["Close"] > barThree["Open"]:
				return "180bar:",current["Close"], "barTwo:", barTwo["Close"], barTwo["Open"], "barThree:", barThree["Close"], "barFour:", barFour["Close"]