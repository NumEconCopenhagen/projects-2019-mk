#%% 
import time
import pandas_datareader
import pandas as pd
import numpy as np
from datetime import datetime
from pytrends.request import TrendReq  #imports pytrends for loading google trends data
pytrends = TrendReq(hl='en-US', tz=360)
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib
import pylab
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
start = datetime(2018,1,2)
end = datetime(2018,3,31)

#%%

def yprices(name, start, end):
    '''    
        Arguments: 

            name(string)    : input the ticker for the desired stock
            start(datetime) : Setting a starting date
            end(datetime)   : Setting a ending date 

         Returns:
            The function returns a Pandas DataFrame webscraped from yahoo finance containing the Date, High, Low, Close, Adj close and Volume for the inquired stock 
            More information can be found at https://github.com/ranaroussi/fix-yahoo-finance
    '''
    yf.pdr_override()
    return pdr.get_data_yahoo(name, start, end)




#%%
def prices(name, start=start, end=end):
    '''    
        Arguments: 

            name(string)    : input the ticker for the desired stock, the ticker list can be found at https://iextrading.com/apps/stocks/
            start(datetime) : Setting a starting date
            end(datetime)   : Setting a ending date 

         Returns:
            The function returns a Pandas DataFrame containing the Date, High, Low, Close and Volume for the inquired stock 
    '''
    return pandas_datareader.iex.daily.IEXDailyReader(name, start, end).read()
#%%

def searches(*kw_list):
        '''    
        Arguments: 

            kw_list(string): insert the searchword 
            
        Returns:
            The function returns a Pandas DataFrame containing the search
            frequency for the inquired seachword 
        '''
        pytrends.build_payload(kw_list, cat=0, timeframe='2018-01-01 2018-03-31', geo='', gprop='')
        searches = pytrends.interest_over_time()
        return searches.drop(columns = "isPartial")


#%%
def combine_data_frames(df1, df2):
        '''    
        Arguments: 
            df1(DataFrame): 1st Pandas DataFrame
            df2(DataFrame): 2nd Pandas DataFrame 
        Returns:
            A joined dataframe contraining both dataframes, where the 
            2nd DataFrame is added on the right.
        '''
        return df1.join(df2, how='outer')

def scatterplot(firm):
    '''
    Arguments:
        firmname
    Returns:
        A scatterplot of the firms day-to-day closing stockprices
        against the google trends data associated with the firm'''
    IBM_nonan = IBM.dropna()
    return IBM_nonan.plot.scatter(x = "searches", y = "close")

def scatterols(firm):
    '''
    Arguments:
        firmname
    Returns:
        Scatterplot but this time with an added simple OLS regression'''
    fig, ax = plt.subplots()
    ax.plot(IBM_nonan["searches"], IBM_nonan["close"], "o", label = "Data")
    ax.set_xlabel("searches")
    ax.set_ylabel("close")
    ax.plot(IBM_nonan["searches"],IBM_OLS.fittedvalues, "r", label = "OLS")
    ax.legend()
    return plt.show()

def fig(firm):
    '''
    Arguments:
        firmname
    Returns:
        A plot containing the firms day-to-day closing stockprice
        and the google trends data associated with the firm, but controrary 
        to the "scatterplot" function, they are both plotted against time'''    
    fig, ax1 = plt.subplots()
    plt.figure()
    ax1.plot(firm["searches"])
    ax1.set_xlabel("Date")
    ax1.set_ylabel("searches", color = "b")
    ax1.tick_params("y", colors = "b")

    ax2 = ax1.twinx()
    ax2.plot(firm["close"], "r")  #Plotting closing price as red.
    ax2.set_ylabel("price", color = "r")
    ax2.tick_params("y", colors = "r")

    fig.autofmt_xdate()

    fig.legend(("searches", "closing price"))
    return plt.show()





def RSI(prices, n=14):
    '''
        Arguments:
            prices(float)   : the column index of close values
            period(float)   : Average gain of last 14 trading days 
                            / Average loss of last 14 trading days which means 
                            the value should be set to 14

        Returns:
            RSI(float)      : indicator if an stock is oversold or bought 
    '''    
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi
    