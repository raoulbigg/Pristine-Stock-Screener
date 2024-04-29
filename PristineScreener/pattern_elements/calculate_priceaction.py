def calc_bars_positions(data, pop, timeframe):

	current = data.iloc[0]
	barOne = data.iloc[1]
	barTwo = data.iloc[2]
	barThree = data.iloc[3]


	if pop == "up":
		'''Calcs bar one low or close beneath bar two low or close and
		   bar two low or close beneath bar three low or close
		'''

		if barOne["Low"] < barTwo["Low"] or barOne["Close"] < barTwo["Close"]:
			if barTwo["Low"] < barThree["Low"] or barTwo["Close"] < barThree["Close"]:
				return True

		elif current["Low"] < barOne["Low"]:
			if barOne["Low"] < barTwo["Low"] or barOne["Close"] < barTwo["Close"]:
				return True




	if pop == "down":
		'''Calcs bar one high or close above bar two high or close and
		   bar two high or close above bar three high or close
		'''
		if barOne["High"] > barTwo["High"] or barOne["Close"] > barTwo["Close"]:
			if barTwo["High"] > barThree["High"] or barTwo["Close"] > barThree["Close"]:
				return True

		elif current["High"] < barOne["High"]:
			if barOne["High"] > barTwo["High"] or barOne["Close"] > barTwo["Close"]:
				return True
