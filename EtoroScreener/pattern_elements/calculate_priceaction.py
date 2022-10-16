def calc_bars_positions(data, pop, timeframe):

	current = data.iloc[0]
	barTwo = data.iloc[1]
	barThree = data.iloc[2]
	barFour = data.iloc[3]


	if pop == "up":
		#CHeck if bullish engulfing
		if current["Close"] > current["Open"] and current["Close"] > barTwo["Close"]:
			#Looks at first open above engulfing bar. And look if a void is present.
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] > current["Close"]:
						if data.iloc[i+1]["Close"] < data.iloc[i+1]["Open"]:
							if data.iloc[i+2]["Close"] < data.iloc[i+2]["Open"]:
								return "180bar:",current["Close"], "barTwo:", barTwo["Close"]
						else:
							break
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] > current["Close"]:
						if data.iloc[i-1]["Close"] < data.iloc[i-1]["Open"]:
							if data.iloc[i-2]["Close"] < data.iloc[i-2]["Open"]:
								return "180bar:",current["Close"], "barTwo:", barTwo["Close"]
						else:
							break
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i-1]["Close"] < data.iloc[i-1]["Open"]:
							if data.iloc[i+1]["Close"] < data.iloc[i+1]["Open"]:
								return "180bar:",current["Close"], "barTwo:", barTwo["Close"]
						else:
							break


	if pop == "down":
		#Check if bearish engulfing
		if current["Close"] < current["Open"] and current["Close"] < barTwo["Close"]:
			#Looks at first open below engulfing bar. And look if a void is present.
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i+1]["Close"] > data.iloc[i+1]["Open"]:
							if data.iloc[i+2]["Close"] > data.iloc[i+2]["Open"]:
								return "180bar:",current["Close"], "barTwo:", barTwo["Close"]
						else:
							break
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i-1]["Close"] > data.iloc[i-1]["Open"]:
							if data.iloc[i-2]["Close"] > data.iloc[i-2]["Open"]:
								return "180bar:",current["Close"], "barTwo:", barTwo["Close"]
						else:
							break
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i-1]["Close"] > data.iloc[i-1]["Open"]:
							if data.iloc[i+1]["Close"] > data.iloc[i+1]["Open"]:
								return "180bar:",current["Close"], "barTwo:", barTwo["Close"]
						else:
							break

	