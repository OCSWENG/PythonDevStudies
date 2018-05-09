# Jan 1 2012 to Jan 1 2017 Equity Studies


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pandas_datareader
import datetime

import pandas_datareader.data as web

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2016, 12, 1)


tesla = web.DataReader("TSLA", 'iex', start, end)
ford = web.DataReader("F", 'iex', start, end)
gm = web.DataReader("GM",'iex',start,end)


tesla.to_csv('Tesla_Equity.csv')
ford.to_csv('Ford_Equity.csv')
gm.to_csv('GM_Equity.csv')

show = input("Enter y/n to show open price %")
if (show == 'y' or show =='Y'):
    tesla['open'].plot(label='Tesla Motors',figsize=(18,9),title='Open Price')
    gm['open'].plot(label='GM')
    ford['open'].plot(label='Ford')
    plt.legend()
    plt.show()


show = input("Enter y/n to show volume %")
if (show == 'y' or show =='Y'):
    tesla['volume'].plot(label='Tesla Motors',figsize=(18,9),title='Volume')
    gm['volume'].plot(label='gm')
    ford['volume'].plot(label='ford')
    plt.legend()
    plt.show()
    dateOfVolumeSpike = ford['volume'].idxmax()
    print("Ford volumen spike date: " , dateOfVolumeSpike)
    # search the web for urls related to ford financial , ford news on that dateOfVolumeSpike


tesla['total traded'] = tesla['open']*tesla['volume']
ford['total traded'] = ford['open']*ford['volume']
gm['total traded'] = gm['open']*gm['volume']


show = input("Enter y/n to show amount traded in $ %")
if (show == 'y' or show =='Y'):
    tesla['total traded'].plot(label='Tesla',figsize=(16,9))
    gm['total traded'].plot(label='GM')
    ford['total traded'].plot(label='Ford')
    plt.legend()
    plt.ylabel('total traded')
    plt.show()


    largeMoneyExchanged = tesla['total traded'].idxmax()

    # search the web for urls related to tesla financial , tesla news on that large money exchange

    print("Large amt of money exchanged: ", largeMoneyExchanged)


gm['MA50'] = gm['open'].rolling(50).mean()
gm['MA200'] = gm['open'].rolling(200).mean()

show = input("Enter y/n to show moving averages for gm & ford %")
if (show == 'y' or show =='Y'):
    gm[['open','MA50','MA200']].plot(label='GM',figsize=(16,8))
    plt.legend()
    plt.show()


# observe the relationship of F , GM and TSLA
from pandas.plotting import scatter_matrix

car_index = pd.concat([tesla['open'],gm['open'],ford['open']],axis=1)
car_index.columns = ['tesla open','gm open','ford open']

show = input("Enter y/n to show the correlations with scatter plot %")
if (show == 'y' or show =='Y'):
    scatter_matrix(car_index,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50});
    plt.show()

# daily percent change Rt = Pt/Pt-1  -1
# tesla['returns'] = (tesla['close'] / tesla['close'].shift(1) ) - 1

# or simply
ford['returns'] = ford['close'].pct_change(1)
gm['returns'] = gm['close'].pct_change(1)
tesla['returns'] = tesla['close'].pct_change(1)


#Which stock is the most "volatile"? 
# Determined by the variance in the daily returns

show = input("Enter y/n to show the histogram of ford %")
if (show == 'y' or show =='Y'):
    ford['returns'].hist(bins=50)
    plt.show()

show = input("Enter y/n to show the histogram of gm %")
if (show == 'y' or show =='Y'):
    gm['returns'].hist(bins=50)
    plt.show()

show = input("Enter y/n to show the histogram of tesla %")
if (show == 'y' or show =='Y'):
    tesla['returns'].hist(bins=50)
    plt.show()


show = input("Enter y/n to show the histogram of all three %")
if (show == 'y' or show =='Y'):
    tesla['returns'].hist(bins=100,label='tesla',figsize=(10,8),alpha=0.5)
    gm['returns'].hist(bins=100,label='gm',alpha=0.5)
    ford['returns'].hist(bins=100,label='ford',alpha=0.5)
    plt.legend()
    plt.show()


# Which equity has the widest plot

show = input("Enter y/n to show the density of all three %")
if (show == 'y' or show =='Y'):
    tesla['returns'].plot(kind='kde',label='tesla',figsize=(12,6))
    gm['returns'].plot(kind='kde',label='gm')
    ford['returns'].plot(kind='kde',label='ford')
    plt.legend()
    plt.show()


box_df = pd.concat([tesla['returns'],gm['returns'],ford['returns']],axis=1)
box_df.columns = ['Tesla Returns',' GM Returns','Ford Returns']

show = input("Enter y/n to show the box plot of all three %")
if (show == 'y' or show =='Y'):

    box_df.plot(kind='box',figsize=(8,11),colormap='jet')
    plt.show()


# scatter matrix plot to see the correlation between each of the equity daily returns
show = input("Enter y/n to show the scatter matrix of all three %")
if (show == 'y' or show =='Y'):
    scatter_matrix(box_df,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50});
    plt.show()

show = input("Enter y/n to show the scatter matrix of gm and ford %")
if (show == 'y' or show =='Y'):
    box_df.plot(kind='scatter',x=' GM Returns',y='Ford Returns',alpha=0.4,figsize=(10,8))
    plt.show()

# find out by price alone where it was better to place capital
#cumulative daily return is:
# ii=(1+rt)∗it−1

tesla['cumulative return'] = (1 + tesla['returns']).cumprod()
ford['cumulative return'] = (1 + ford['returns']).cumprod()
gm['cumulative return'] = (1 + gm['returns']).cumprod()

show = input("Enter y/n to show the cumulative return of all three %")
if (show == 'y' or show =='Y'):
    tesla['cumulative return'].plot(label='Tesla',figsize=(16,8),title='cumulative return')
    ford['cumulative return'].plot(label='Ford')
    gm['cumulative return'].plot(label='GM')
    plt.legend()
    plt.show()
