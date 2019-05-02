#%%
# import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pandas_datareader as web
import scipy.stats as scs
import statsmodels.api as sm
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf


#%%
def yprices(name, start, end):
    '''    
        Arguments: 
            name(string)    : input the ticker for the desired stock
            start(datetime) : Setting a starting date
            end(datetime)   : Setting a ending date 
         Returns:
            The function returns a Pandas DataFrame webscraped from yahoo finance containing the Date, High, Low, Close, Adj Close and Volume for the inquired stock 
            More information can be found at https://github.com/ranaroussi/fix-yahoo-finance
    '''
    yf.pdr_override() # Command to override the pandas search function
    return pdr.get_data_yahoo(name, start, end)

#%%
def print_statistics(array):
    ''' Prints selected statistics.
    Parameters
    ==========
    array: ndarray
    object to generate statistics on
    '''
    sta = scs.describe(array)
    print('%14s %15s' % ('statistic', 'value'))
    print(30 * '-')
    print('%14s %15.5f' % ('size', sta[0]))
    print('%14s %15.5f' % ('min', sta[1][0]))
    print('%14s %15.5f' % ('max', sta[1][1]))
    print('%14s %15.5f' % ('mean', sta[2]))
    print('%14s %15.5f' % ('std', np.sqrt(sta[3])))
    print('%14s %15.5f' % ('skew', sta[4]))
    print('%14s %15.5f' % ('kurtosis', sta[5]))


#%%
def normality_tests(arr):
    ''' Tests for normality distribution of given data set.
    Parameters
    ==========
    array: ndarray
    object to generate statistics on
    '''
    print('Skew of data set %14.3f' % scs.skew(arr))
    print('Skew test p-value %14.3f' % scs.skewtest(arr)[1])
    print('Kurt of data set %14.3f' % scs.kurtosis(arr))
    print('Kurt test p-value %14.3f' % scs.kurtosistest(arr)[1])
    print('Norm test p-value %14.3f' % scs.normaltest(arr)[1])


#%%
def statistics(weights):
     weights = np.array(weights)
     pret = np.sum(rets.mean() * weights) * 252
     pvol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
     return np.array([pret, pvol, pret / pvol])
     #this is a callable function that repeats work above

#%%
def min_func_sharpe(weights):
     return -statistics(weights)[2]
    #I think this is calling the eariler function - without the [2], the minimization crashes

#%%
def min_func_variance(weights):
     return statistics(weights)[1] ** 2

#%%
def min_func_port(weights):
     return statistics(weights)[1]

#%%
def equations(p, rf=0.01):
 eq1 = rf - p[0]
 eq2 = rf + p[1] * p[2] - f(p[2])
 eq3 = p[1] - df(p[2])
 return eq1, eq2, eq3
