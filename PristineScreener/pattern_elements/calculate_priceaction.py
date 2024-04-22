def calc_bars_positions(data, pop, timeframe):

	current = data.iloc[0]
	barOne = data.iloc[1]
	barTwo = data.iloc[2]
	barThree = data.iloc[3]


	if pop == "up":
		#If 3 consecutive Lower Lows and Lower Highs
		if barOne["Low"] < barTwo["Low"] and barTwo["Low"] < barThree["Low"] and \
		barOne["High"] < barTwo["High"] and barTwo["High"] < barThree["High"] or \
		current["Low"] < barOne["Low"] and barOne["Low"] < barTwo["Low"] and \
		current["High"] < barOne["High"] and barOne["High"] < barTwo["High"]:
			return True

		#If 3 consecutive red bars
		elif barOne["Close"] < barOne["Open"] and barTwo["Close"] < barTwo["Open"] and barThree["Close"] < barThree["Open"]:
			return True


	if pop == "down":
		#If 3 consecutive Higher Lows and Higher Highs
		if barOne["Low"] > barTwo["Low"] and barTwo["Low"] > barThree["Low"] and \
		barOne["High"] > barTwo["High"] and barTwo["High"] > barThree["High"] or \
		current["Low"] > barOne["Low"] and barOne["Low"] > barTwo["Low"] and \
		current["High"] > barOne["High"] and barOne["High"] > barTwo["High"]:
			return True

		#If 3 consecutive red bars
		elif barOne["Close"] > barOne["Open"] and barTwo["Close"] > barTwo["Open"] and barThree["Close"] > barThree["Open"]:
			return True


#TO-DO: calculate 3 consecutive lower lows and lower highs
