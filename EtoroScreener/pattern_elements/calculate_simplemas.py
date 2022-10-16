#Calculate the 20 and 50 simple moving average (needed for the LAW Picture of Power AND the LAW of the 20ma)
def calc_smas(data):
	sma_very_short = 5
	sma = 8
	short_sma = 20
	medium_sma = 40
	SMAs=[sma_very_short, sma, short_sma, medium_sma]

	#Calculate 20ma and 50ma based on the closing price
	try:
		for i in SMAs:
			data["SMA_"+str(i)]= data['Close'].rolling(window=i).mean()
	except TypeError as e:
		pass
	#Return data in reverse (chronological sequence)
	return data.iloc[::-1]
