#Calculate the 20 and 50 simple moving average (needed for the LAW Picture of Power AND the LAW of the 20ma)
def calc_smas(data):
	short_sma = 20
	medium_sma = 40
	SMAs=[short_sma, medium_sma]

	#Calculate 20ma and 50ma based on the closing price
	try:
		for i in SMAs:
			data["SMA_"+str(i)]= data['Close'].rolling(window=i).mean()
	except TypeError as e:
		pass
	#Return data in reverse (chronological sequence)
	return data.iloc[::-1]
