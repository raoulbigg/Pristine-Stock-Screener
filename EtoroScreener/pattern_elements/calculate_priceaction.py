def calc_bars_positions(data, pop, timeframe):

	current = data.iloc[0]
	barTwo = data.iloc[1]
	barThree = data.iloc[2]
	barFour = data.iloc[3]



	if pop == "up":
		#Check if price is up
		if (current["Close"] > current["Open"]):
			#Looks at first open above engulfing bar. And look if a void is present.
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] > current["Close"]:
						if data.iloc[i+1]["Close"] < data.iloc[i+1]["Open"]:
							#calculate 40% of bar 2
							penetrationThreshold = (data.iloc[i+1]["High"] - data.iloc[i+1]["Low"]) * 0.4
							#if the high of bar 1 penetrates 40% or less of bar 2 return True
							if data.iloc[i]["High"] <= data.iloc[i+1]["Low"] + penetrationThreshold:
								return True
						else:
							break




	if pop == "down":
		#Check if price is down
		if (current["Close"] < current["Open"] ):
			#Looks at first open below engulfing bar. And look if a void is present.
			for i in range(30):
				if i != 0:
					if data.iloc[i]["Open"] < current["Close"]:
						if data.iloc[i+1]["Close"] > data.iloc[i+1]["Open"]:
							#calculate 40% of bar 2
							penetrationThreshold = (data.iloc[i+1]["High"] - data.iloc[i+1]["Low"]) * 0.4
							#if the low of bar 1 penetrates 40% or less of bar 2 return True
							if data.iloc[i]["Low"] >= data.iloc[i+1]["High"] - penetrationThreshold:
								return True
						else:
							break
