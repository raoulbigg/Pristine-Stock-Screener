def calc_bars_positions(data, pop, timeframe):

	current = data.iloc[0]
	barTwo = data.iloc[1]
	barThree = data.iloc[2]
	barFour = data.iloc[3]


	if pop == "up":
		#Check if bullish engulfing
		if current["Close"] > current["Open"]:
			#Looks at first open above engulfing bar. And look if a void is present.
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] > current["Close"]:
						if data.iloc[i+1]["Close"] < data.iloc[i+1]["Open"]:
							#Calculate 40% of bar 3
							maxPenetration = data.iloc[i+1]["High"] - data.iloc[i+1]["Low"] * 0,4
							#if bar2 high does not penetrate bar3 more than 40%
							if data.iloc[i+1]["Low"] - data.iloc[i]["High"] < maxPenetration:
								return True
						else:
							break

			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] > current["Close"]:
						if data.iloc[i-1]["Close"] < data.iloc[i-1]["Open"]:
							maxPenetration = data.iloc[i]["High"] - data.iloc[i]["Low"] * 0,4
							if data.iloc[i]["Low"] - data.iloc[i-1]["High"] < maxPenetration:
								return True							
						else:
							break



	if pop == "down":
		#Check if bearish engulfing
		if current["Close"] < current["Open"]:
			#Looks at first open below engulfing bar. And look if a void is present.
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i+1]["Close"] > data.iloc[i+1]["Open"]:
							#Calculate 40% of bar 3
							maxPenetration = data.iloc[i+1]["High"] - data.iloc[i+1]["Low"] * 0,4
							#if bar2 low does not penetrate bar3 more than 40%
							if data.iloc[i+1]["High"] - data.iloc[i]["Low"] < maxPenetration:
								return True
						else:
							break
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i-1]["Close"] > data.iloc[i-1]["Open"]:
							maxPenetration = data.iloc[i]["High"] - data.iloc[i]["Low"] * 0,4
							if data.iloc[i]["High"] - data.iloc[i-1]["Low"] < maxPenetration:
								return True
						else:
							break
	
