#Calculate the 20 and 50 simple moving average (needed for the LAW Picture of Power AND the LAW of the 20ma)
def calc_smas(data):
	short_sma= 8
	medium_sma = 20
	long_sma = 50
	SMAs=[short_sma, medium_sma, long_sma]

	#Calculate 20ma and 50ma based on the closing price
	for i in SMAs:
		data["SMA_"+str(i)]= data.iloc[:,4].rolling(window=i).mean()
		
	#Return data in reverse (chronological sequence)
	return data.iloc[::-1]