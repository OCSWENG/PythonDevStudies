import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# down load from Quandl

# should take a 8 year sample

aapl = pd.read_csv('AAPL_CLOSE',index_col='Date',parse_dates=True)
cisco = pd.read_csv('CISCO_CLOSE',index_col='Date',parse_dates=True)
ibm = pd.read_csv('IBM_CLOSE',index_col='Date',parse_dates=True)
amzn = pd.read_csv('AMZN_CLOSE',index_col='Date',parse_dates=True)

# create a data frame containing the set of equities or ETFs that would suit an investment strategy
 
stocks = pd.concat([aapl,cisco,ibm,amzn],axis=1)
stocks.columns = ['aapl','cisco','ibm','amzn']


# Dail change average
mean_daily_ret = stocks.pct_change(1).mean()


stock_normed = stocks/stocks.iloc[0]
stock_normed.plot()

stock_daily_ret = stocks.pct_change(1)

#detrending/normalizing the time series
log_ret = np.log(stocks/stocks.shift(1))

log_ret.hist(bins=100,figsize=(12,6));
plt.tight_layout()


log_ret.describe().transpose()

log_ret.mean() * 252

# Compute pairwise covariance of columns
log_ret.cov()

log_ret.cov()*252 # multiply by days


# MCS PART I

num_ports = 15000

all_weights = np.zeros((num_ports,len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

def mcs ():
	for ind in range(num_ports):

    		# Create Random Weights
    		weights = np.array(np.random.random(4))

    		# Rebalance Weights
    		weights = weights / np.sum(weights)
    
   		# Save Weights
    		all_weights[ind,:] = weights

    		# Expected Return
    		ret_arr[ind] = np.sum((log_ret.mean() * weights) *252)

    		# Expected Variance
    		vol_arr[ind] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))

    		# Sharpe Ratio
    		sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]


def get_ret_vol_sr(weights):
	"""
	Takes in weights, returns array or return,volatility, sharpe ratio
	"""
	weights = np.array(weights)
	ret = np.sum(log_ret.mean() * weights) * 252
	vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
	sr = ret/vol
	return np.array([ret,vol,sr])

def neg_sharpe(weights):
	return  get_ret_vol_sr(weights)[2] * -1

# Contraints
def check_sum(weights):
	'''
	Returns 0 if sum of weights is 1.0
	'''
	return np.sum(weights) - 1

def minimize_volatility(weights):
	return  get_ret_vol_sr(weights)[1] 

sharpe_arr.max()
argMax = sharpe_arr.argmax()
for column,weight in zip(stocks.columns,all_weights[argMax,:]):
	print(column + " : " + weight)

max_sr_ret = ret_arr[argMax]
max_sr_vol = vol_arr[argMax]

plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

# Add red dot for max SR
plt.scatter(max_sr_vol,max_sr_ret,c='red',s=50,edgecolors='black')


# part II

# By convention of minimize function it should be a function that returns zero for conditions
cons = ({'type':'eq','fun': check_sum})

# 0-1 bounds for each weight
bounds = ((0, 1), (0, 1), (0, 1), (0, 1))

# Initial Guess (equal distribution)
init_guess = [0.25,0.25,0.25,0.25]

# Sequential Least SQuares Programming (SLSQP).
opt_results = minimize(neg_sharpe,init_guess,method='SLSQP',bounds=bounds,constraints=cons)

results = get_ret_vol_sr(opt_results.x)

for column,weight in zip(stocks.columns,opt_results.x):
	print(column + " : " + weight)

# Our returns go from 0 to somewhere along 0.3
# Create a linspace number of points to calculate x on
frontier_y = np.linspace(0,0.3,100) # Change 100 to a lower number for slower computers!

frontier_volatility = []

for possible_return in frontier_y:
    # function for return
    cons = ({'type':'eq','fun': check_sum},
            {'type':'eq','fun': lambda w: get_ret_vol_sr(w)[0] - possible_return})
    
    result = minimize(minimize_volatility,init_guess,method='SLSQP',bounds=bounds,constraints=cons)
    frontier_volatility.append(result['fun'])

plt.figure(figsize=(12,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')

# Add frontier line
plt.plot(frontier_volatility,frontier_y,'g--',linewidth=3)

