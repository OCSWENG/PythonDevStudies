import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


bankDF = pd.read_csv('./banklist.csv')

# show the head of the dataFrame
bankDF.head()

columnNames = bankDF.columns

# find the number of states represented in this dataset

stateRepresentation = bankDF['ST'].nunique()

listOfStateRepresentation = bankDF['ST'].unique()

topFiveStates = bankDF.groupby('ST').count().sort_values('Bank Name', ascending=False).iloc[:5]['Bank Name']

topFiveAcquiring = bankDF['Acquiring Institution'].value_counts().iloc[:5]


banksAcqByBankOfTexas = bankDF[bankDF['Acquring Institution']=='State Bank of Texas']

# get all the banks of CA
#	Groupby City
#		count
#			present in decending Bank Name

bankDF[bankDF['ST']=='CA'].groupby('City').count().sort_values('Bank Name', ascending=False).head(1)


# what is the total number of banks that don't have a title Bank in their name
sum(bankDF['Bank Name'].apply(lambda x: 'Bank' not in x))


sum(bankDF['Bank Name'].apply(lambda x: x[0].upper() =='S'))


sum(bankDF['CERT'] > 20000)

sum(bankDF['Bank Name'].apply(lambda name: len(name.split())==2))

# pick the last two digits off of the date
sum(bankDF['Closing Date'].apply(lambda date: date[-2:]) == '08')
sum(pd.to_datetime(bankDF['Closing Date']).apply(lambda date: date.year >= 2008))




# Time Series

from dateTime import datetime
year_1=2006
month_1=7
day_1=25
hour_1=14
minute_1=25
second_1=15

date_1 =datetime(year_1,month_1,day_1)
datetime_1=datetime(year_1,month_1,day_1,hour_1,minute_1,second_1)



#DateTime Indexing
datetimeList= [datetime(2006,8,5), datetime(2008,8,5)]
dt_indx = pd.DatetimeIndex(datetimeList)

data = np.random.randn(2,2)

col = ['1','2']

df = pd.DataFrame(data,dt_indx, cols)
# what most finance data looks like

df.index.argmax()
df.index.max()
df.index.min()


#Time Resampling
# business quarters, years

df = pd.read_csv('walmart_stock.csv', index_col='Date', parse_dates=True)

#df.set_index('Date', inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].apply(pd.to_datetime)

# A = year end frequency
# Q = quarterly end freq

df.resample(rule='A').mean()

df.resample(rule='A').max()

def f_day (entry):
    return entry[0]

df.resample(rule='A').apply(f_day)


df['Close'].resample(rule='A').mean().plot(kind='bar')

# Time Shifts
# data is a fifo shift tail looses and head looses
df.shift(periods=1)

df.tshift(freq='M').head()


# Rolling & Expanding
# moving averages
# shift 7 points and mean it
df.rolling(7).mean().head(25)

# bollinger band
# significant movement

# 3 columns
df['Close 20 DMA'] = df['Close'].rolling(20).mean()

df['Close 20 D STD'] = df['Close'].rolling(20).std()

# upper band : 20ma + 2*std(20)
df['Upper'] = df['Close 20 DMA'] + 2*(df['Close 20 D STD'])
df['Lower'] = df['Close 20 DMA'] - 2*(df['Close 20 D STD'])

df[['Close', 'Close 20 DMA','Upper','Lower']].tail(365).plot(figsize(25,5))

# EWMA

airline = pd.read_csv('airline.csv', index_col='Month')
# clean up
airline.dropna(inplace=True)
airline.index=pd.to_datetime(airline.index)

# SMA
airline['6 MSMA'] = airline['Thousands of Passengers'].rolling(window=6)

airline['12 MSMA'] = airline['Thousands of Passengers'].rolling(window=12)
airline.plot(figsize(25,5))

# EWMA
# recent points have more weight

airline['EWMA_12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline[['Thousands of Passengers', 'EWMA_12]].plot(figsize(14,7))

# Alpha = ['span','center of mass','halfLife']
# span is a period 
# center of mass is inverse of span
# halfLife is a period of time

# ETS
# Error , Trend, Seasonality
airline = pd.read_csv('airline.csv', index_col='Month')
# clean up
airline.dropna(inplace=True)
airline.index=pd.to_datetime(airline.index)

# linear trend or exponential trend?
from statsmodel.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')

result.seasonal.plot()
result.trend.plot()

# result = seasonal_decompose(airline['Thousands of Passengers'], model='additive')

result.plot() # to see observed , trend, seasonal, residual

# portfolio study
# Daily return
# cumulative return
# average daily return
# std daily return
# sharpe ratio risk adjusted return
# 	mean daily return with std

#	S = (Rp - Rf)/sigP

# in 2018 Rf is about 1.5%
# usually a yearly return
# daily = k = sqrt(252)
# weekly = k = sqrt(52)
# montly = k = sqrt(12)

# sqrt(252) * SharpeRatio


import quandl

start = pd.to_datetime('2012')
end = pd.to_datetime('2017')

aapl = quandl.get('WIKI/AAPL.11',start_date=start, end_date=end)
cisco = quandl.get('WIKI/CSCO.11',start_date=start, end_date=end)
ibm = quandl.get('WIKI/IBM.11',start_date=start, end_date=end)
amzn= quandl.get('WIKI/AMZN.11',start_date=start, end_date=end)


appl.iloc[0]['Adj. Close']

for stock_df in (appl,cisco,ibm,amzn):
	stock_df['Normalize Return'] = stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']

print(aapl.head())


# 30% aaple
# 20% cisco
# 40% amazon
# 10% ibm

for stock_df, allo in zip((appl,cisco,ibm,amzn),[.3,.2,.4,.1]):
	stock_df['Allocation'] = stock_df['Normalized Return']*allo

print(aapl.head())
investment = 1000000

for stock_df in (appl,cisco,ibm,amzn):
	stock_df['Postion Values'] = stock_df['Allocation'] * investment

print(aapl.head())

allPosVals = [aapl['Position Values'], csco['Position Values'],ibm['Position Values'],amzn['Position Values']]
portfolioVal = pd.concat(allPossVals)

portfolioVal.colums = ['AAPL Pos','CSCO Pos','IBM Pos','AMZN Pos']

portfolioVal['Total Pos'] = portfolioVal.sum(axis=1)

portfolioVal['Total pos'].plot(figsize(14,7))
plt.title('Total Portfolio Value')

portfolioVal.drop('Total Pos', axis=1).plot(figsize(14,7))

portfolioVal['Daily Return'] = portfolioVal['Total Pos'].pct_change(1)

portfolioVal['Daily Return'].mean()

portfolioVal['Daily Return'].std()

portfolioVal['Daily Return'].plot(kind='hist', bins=75, figsize=(4,6))

portfolioVal['Daily Return'].plot(kind='kde',figsize=(4,6))

cumulativeReturn = (portfolioVal['Total Pos'][-1] / portfolioVal['Total Pos'][0] -1) * 100

sharpeRatio = portfolioVal['Daily Return'].mean()/portfolioVal['Daily Return'].std()

annualizeSharpeRatio = sharpeRatio * sqrt(252)
# (252**0.5) * SR

# the higher the better
# SR > 1, SR > 2, SR > 3


# random guess and check is monte carlo simulation
# calculate thousands of sharpe ratios for a set of equities.


# optimization algorithm














