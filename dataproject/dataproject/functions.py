#%% 
import time
import pandas_datareader
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from pytrends.request import TrendReq  #imports pytrends for loading google trends data
pytrends = TrendReq(hl='en-US', tz=360)
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib
import pylab
from statsmodels.formula.api import ols
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

    

def deletenan(firm):
    firm_nonan = firm.dropna()
    return firm_nonan
    
def scatterplot(firm):
    '''
    Arguments:
        firmname
    Returns:
        A scatterplot of the firms day-to-day closing stockprices
        against the google trends data associated with the firm'''
    firm_nonan = firm.dropna()
    return firm_nonan.plot.scatter(x = "searches", y = "close")


def OLS(firm):
    firm_nonan = firm.dropna()
    firm_OLS = ols("close ~ searches", data = firm_nonan).fit()
    return firm_OLS.summary()


def scatterols(firm):
    '''
    Arguments:
        firmname
    Returns:
        Scatterplot but this time with an added simple OLS regression'''
    fig, ax = plt.subplots()
    firm_nonan = firm.dropna()
    ax.plot(firm_nonan["searches"], firm_nonan["close"], "o", label = "Data")
    ax.set_xlabel("searches")
    ax.set_ylabel("close")
    firm_OLS = ols("close ~ searches", data = firm_nonan).fit()
    ax.plot(firm_nonan["searches"],firm_OLS.fittedvalues, "r", label = "OLS")
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

def bondfig(index, bond):
    '''
    Arguments: 
        Stock index name and bond name
    Return:
        A plot plotting the stock index price and bond price 
        plotted against weeks (in this case 1 year (52 weeks))'''
    fig, ax1 = plt.subplots()
    plt.figure()

    ax1.plot(index["Open"])
    ax1.set_xlabel("Week")
    ax1.set_ylabel("SPX", color = "b")
    ax1.tick_params("y", colors = "b")


    ax2 = ax1.twinx()
    ax2.plot(bond["Open"], "r")  #Plotting closing price as red.
    ax2.set_ylabel("Bond", color = "r")
    ax2.tick_params("y", colors = "r")

    fig.autofmt_xdate()
    plt.show()

    fig.autofmt_xdate()
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

def trendsintervalTSLA(start_date):
    '''
        Arguments:
            Start_time(datetime)    :   insert datetime date

        Returns:
            Interest_over_time_df(dataframe)    :   Dateframe for google searches on TSLA for the 250 days
    '''    
    maxstep = 269
    overlap = 40
    kw_list = ['TSLA']
    step    = maxstep - overlap + 1
    start_date = start_date.date()
    # Login to Google.
    pytrend = TrendReq()
    # Run the first time (if we want to start from today, otherwise we need to ask for an end_date as well
    today = datetime.today().date()
    old_date = today
    # Go back in time
    new_date = today - timedelta(days=step)
    # Create new timeframe for which we download data
    timeframe = new_date.strftime('%Y-%m-%d')+' '+old_date.strftime('%Y-%m-%d')
    pytrend.build_payload(kw_list=kw_list, timeframe = timeframe)
    interest_over_time_df = pytrend.interest_over_time()
    ## RUN ITERATIONS

    while new_date>start_date:
        
        ### Save the new date from the previous iteration.
        # Overlap == 1 would mean that we start where we
        # stopped on the iteration before, which gives us
        # indeed overlap == 1.
        old_date = new_date + timedelta(days=overlap-1)
        
        ### Update the new date to take a step into the past
        # Since the timeframe that we can apply for daily data
        # is limited, we use step = maxstep - overlap instead of
        # maxstep.
        new_date = new_date - timedelta(days=step)
        # If we went past our start_date, use it instead
        if new_date < start_date:
            new_date = start_date
            
        # New timeframe
        timeframe = new_date.strftime('%Y-%m-%d')+' '+old_date.strftime('%Y-%m-%d')
        print(timeframe)

        # Download data
        pytrend.build_payload(kw_list=kw_list, timeframe = timeframe)
        temp_df = pytrend.interest_over_time()
        if (temp_df.empty):
            raise ValueError('Google sent back an empty dataframe. Possibly there were no searches at all during the this period! Set start_date to a later date.')
        # Renormalize the dataset and drop last line
        for kw in kw_list:
            beg = new_date
            end = old_date - timedelta(days=1)
            
            # Since we might encounter zeros, we loop over the
            # overlap until we find a non-zero element
            for t in range(1,overlap+1):
                #print('t = ',t)
                #print(temp_df[kw].iloc[-t])
                if temp_df[kw].iloc[-t] != 0:
                    scaling = interest_over_time_df[kw].iloc[t-1]/temp_df[kw].iloc[-t]
                    #print('Found non-zero overlap!')
                    break
                elif t == overlap:
                    print('Did not find non-zero overlap, set scaling to zero! Increase Overlap!')
                    scaling = 0
            # Apply scaling
            temp_df.loc[beg:end,kw]=temp_df.loc[beg:end,kw]*scaling
        interest_over_time_df = pd.concat([temp_df[:-overlap],interest_over_time_df])
    return interest_over_time_df.drop(columns='isPartial')