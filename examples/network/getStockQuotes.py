from googlefinance import getQuotes
import time

tickers = ['GSBD','BXMT','DIAX','BCX','DMO','BGX','BOE','ERC','RNP','RFI','ADX','EOD','EAD','FAX','CHMI']

#[{"Index": "NYSE", "LastTradeWithCurrency": "24.47", "LastTradeDateTime": "2017-05-04T15:57:45Z", "LastTradePrice": "24.47", "LastTradeTime": "3:57PM EDT", "LastTradeDateTimeLong": "May 4, 3:57PM EDT", "StockSymbol": "GSBD", "ID": "778646122952372"}]

listTicks = []


# get a list of a single ticker
# get the dictionary
# extract info

historicalData = {}
Iterations = 4

for i in range (0,4):
	time.sleep(3)
	for ticker in tickers:
		item = getQuotes(ticker)
		adict = item[0]	
		tckr = adict['StockSymbol']
		price = adict['LastTradePrice']
		yld = 0.0
		if adict.has_key('Yield'):
			yld =adict['Yield']

		entity = (float(price), float(yld))

		listOfTups = historicalData.get(tckr)
		if listOfTups is None:
			historicalData[tckr] = [entity]
		else:
			listOfTups.append(entity)
			historicalData[tckr] = listOfTups
		#print ("{0} {1} ".format(tckr, price))


# Alright the values need to be shown as a delta 

for k,v in historicalData:
	tckr = k
	min = 0
	max = 0 
	avg = 0

	prices = []
	for item in v:
		prices.append(v[1])
	min = min(prices)
	max = max(prices)
	avg = sum(prices)/len(prices)

	print('{0} : min {1} max{2} avg{3}'.format(tckr, min, max, avg))
	

#print (historicalData)



