def calc_bars_positions(data):
	current = data.iloc[0]
	barTwo = data.iloc[1]
	barThree = data.iloc[2]
	lastTenBars = [data.iloc[1],data.iloc[2],data.iloc[3],data.iloc[4], data.iloc[5],
					data.iloc[6],data.iloc[7],data.iloc[8],data.iloc[9],data.iloc[10]]
	void = False

	for bar in lastTenBars:
		if current["Adj Close"] > bar["Close"]:
			void = True
	if void and current["Adj Close"] > barTwo["Close"] and barTwo["Open"] and barTwo["Close"] < barThree["Close"]:
		return "180bar:",current["Adj Close"], "barTwo:", barTwo["Close"]

	for bar in lastTenBars:
		if current["Adj Close"] < bar["Close"]:
			void = True
	if void and current["Adj Close"] < barTwo["Close"] and barTwo["Open"] and barTwo["Close"] > barThree["Close"]:
		return "180bar:",current["Adj Close"], "barTwo:", barTwo["Close"]