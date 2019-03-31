#%%
import pandas_datareader
import pandas as pd
import numpy as np
from datetime import datetime
from pytrends.request import TrendReq  #imports pytrends for loading google trends data
pytrends = TrendReq(hl='en-US', tz=360)
import matplotlib.pyplot as plt
#%matplotlib inline

start = datetime(2018,1,2)
end = datetime(2018,3,31)

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
        pytrends.build_payload(kw_list, cat=0, timeframe='2019-1-2 2019-3-31', geo='', gprop='')
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

#%%
def RSI(series, period):
    '''
        Arguments:
            series(float)   : the column index of close values
            period(float)   : Average gain of last 14 trading days 
                            / Average loss of last 14 trading days which means 
                            the value should be set to 14

        Returns:
            RSI(float)      : indicator if an stock is oversold or bought 
    '''
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
    u = u.drop(u.index[:(period-1)])
    d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
    d = d.drop(d.index[:(period-1)])
    rs = pd.stats.moments.ewma(u, com=period-1, adjust=False) / \
    pd.stats.moments.ewma(d, com=period-1, adjust=False)
    return 100 - 100 / (1 + rs)




    