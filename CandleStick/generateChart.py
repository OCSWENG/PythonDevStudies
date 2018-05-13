
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime as datetime
import quandl

    

def plot(EqTicker='SPY', start=datetime.datetime(2016, 5, 11), end=datetime.datetime(2018, 5, 11), api_key='somekeyregistered from quandl' ): 
    #start = datetime.datetime(2016, 5, 11)
    #end = datetime.datetime(2018, 5, 11)

    #If the start and end dates are outside yearly use dot plot
    #EqTicker = 'SPY'

    equity = web.DataReader(EqTicker, 'morningstar', start, end)

    # This won't work the api_key needs to be registered.
    quandl.ApiConfig.api_key = api_key
    interestRates =quandl.get("USTREASURY/YIELD")

    # candle stick chart

    # price versus each interest rate
    interestRateTimeFrame =['1 MO','3 MO', '6 MO', '1 YR', '2 YR', '3 YR', '5 YR', '7 YR', '10 YR', '20 YR', '30 YR']
    
    # clean up the data
    equitClose = equity.xs('Close',axis=1).reset_index(level=0,drop=True)
    #interestRates['Close']=equitClose

    interestRates.dropna()
    dat = interestRates.loc[start:end]
    plt.rc('font', size=20)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(25,15))

    interestRatesPlot = ax1.plot(dat.index.values, dat)
    ax1.set_title(' Interest Rates')
    ax1.legend(dat, interestRateTimeFrame)

    lbl =  EqTicker + '_Close_Price'
    equitPlot = ax2.plot(equitClose.index.values, equitClose,label =lbl)
    f.autofmt_xdate()
    ax2.legend()
    

    f.savefig('./images/'+ lbl+ '_versusInterest_Rates.png')


    
# things to do:
'''
    Render an html page with png
    User Input in the form of a POST, returning an html page

'''
