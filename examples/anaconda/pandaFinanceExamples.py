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


