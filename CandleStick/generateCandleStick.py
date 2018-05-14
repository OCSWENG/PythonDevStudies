
import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator,DayLocator, MONDAY

import datetime as dt
from datetime import timedelta

import pandas as pd
import pandas_datareader.data as web
import numpy as np

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12


def graph_data(stock,start, end):

    
    # Date  Close   High    Low   Open    Volume
    equity = web.DataReader(stock, 'morningstar', start, end)
    dictionary = equity.to_dict()

    equitClose = equity.xs('Close',axis=1).reset_index(level=0,drop=True)
    equitHigh = equity.xs('High',axis=1).reset_index(level=0,drop=True)
    equitLow = equity.xs('Low',axis=1).reset_index(level=0,drop=True)
    equitOpen = equity.xs('Open',axis=1).reset_index(level=0,drop=True)
    equitVolume = equity.xs('Volume',axis=1).reset_index(level=0,drop=True)

    dateTimeSeries = []
    for item in dictionary.values():
        for item2 in item.keys():
            ticker, time = item2
            dateTimeSeries.append(mdates.date2num(time.to_pydatetime()))

    DOCHLV = zip(dateTimeSeries, equity.Open, equity.Close, equity.High, equity.Low, equity.Volume)
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
   
    candlestick_ohlc(ax1, DOCHLV, width=0.4)

    ax1.xaxis.set_major_locator(mondays)
    ax1.xaxis.set_minor_locator(alldays)
    ax1.xaxis.set_major_formatter(weekFormatter)
    ax1.xaxis_date()
    ax1.autoscale_view()
    ax1.grid(True)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.ylabel('Price')
    plt.xlabel('Time')
    plt.title(stock)
    plt.show()


# code to check if the input is correct
codes = {'daily': 1,'weekly':2,'monthly':3,'quarterly':4,'yearly':5}
currentDate = dt.datetime.now()

def getTimeFrame (code, startDate):
    end = None
    timeframe = codes[code]
    if (timeframe == 1):
        # daily
        end = startDate + dt.timedelta(days=1)
        
    elif (timeframe == 2):
        # weekly
        end  = generateEndDateWeekly(startDate)
        
    elif (timeframe == 3):
        # monthly
        end = generateEndDateMonthly(startDate)
        
    elif (timeframe == 4):
        # quarterly
        end = generateEndDateQuarterly(startDate)
    elif (timeframe == 5):
        # yearly
        end = generateEndDateYearly(startDate)
    else:
        raise Exception ('The code was incorrect')
    return end


def generateEndDateWeekly (startDate):
    weeklyDelta =  startDate + dt.timedelta(days=7)
    return weeklyDelta

def generateEndDateMonthly (startDate):
    monthlyDelta =  startDate + dt.timedelta(days=(365/12))
    return monthlyDelta

def generateEndDateQuarterly (startDate):
    quarterlyDelta =  startDate + dt.timedelta(days=(365/4))
    return quarterlyDelta

def generateEndDateYearly (startDate):
    yearlyDelta =  startDate + dt.timedelta(days=365)
    return yearlyDelta
         
#    if (givenDate <= yearDelta):
 #   else:
  #      raise Exception("Start Date %s is beyond  a year %s".format(givenDate.strftime('%Y-%m-%d'), currentDate.strftime('%Y-%m-%d'))) 
       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='OHLC Display:')
    parser.add_argument('--ticker', action="store", required=True, dest="ticker")
    parser.add_argument('--period', action="store", choices=['D','d','W','w','M','m','Q','q','Y','y'], required=True, dest="period")
    parser.add_argument('--start', action="store", required=True, type=lambda d: dt.datetime.strptime(d, '%Y-%m-%d'),dest="start")
    args = parser.parse_args()
    ticker = args.ticker
    period = args.period
    startDate = args.start

    endDate = None
    if (period =='D' or period=='d'):
        endDate = getTimeFrame('daily', startDate)
    if (period =='W' or period=='w'):
        endDate = getTimeFrame('weekly',startDate)
    if (period =='M' or period=='m'):
        endDate = getTimeFrame('monthly',startDate)
    if (period =='Y' or period=='y'):
        endDate = getTimeFrame('yearly',startDate)
    if (period =='Q' or period=='q'):
        endDate = getTimeFrame('quarterly',startDate)

    graph_data(ticker,startDate, endDate)

