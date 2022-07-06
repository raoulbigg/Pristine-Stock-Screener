def calc_bars_positions(data, pop):
	current = data.iloc[0]
	barTwo = data.iloc[1]
	barThree = data.iloc[2]
	barFour = data.iloc[3]
	lastTenBars = [data.iloc[1],data.iloc[2],data.iloc[3],data.iloc[4], data.iloc[5],
					data.iloc[6],data.iloc[7],data.iloc[8],data.iloc[9],data.iloc[10]]

	if pop == "up:":
		countUP = 0
		for i in range(10):
			if i != 0:
				if current["Close"] > data.iloc[i]["Close"] and current["Close"] > data.iloc[i]["Open"]:
					countUP = countUP + 1
		if countUP == 9:
			if current["Close"] > current["Open"] and current["Close"] > barTwo["Close"] and barTwo["Close"] < barThree["Close"]:
				return "180bar:",current["Close"], "barTwo:", barTwo["Close"]


	if pop == "down":
		countDOWN = 0
		for i in range(10):
			if i != 0:
				if current["Close"] < data.iloc[i]["Close"] and current["Close"] < data.iloc[i]["Open"]:
					countDOWN = countDOWN + 1
		if countDOWN == 9:
			if current["Close"] < current["Open"] and current["Close"] < barTwo["Close"] and barTwo["Close"] > barThree["Close"]:
				return "180bar:",current["Close"], "barTwo:", barTwo["Close"], barTwo["Open"], "barThree:", barThree["Close"], "barFour:", barFour["Close"]