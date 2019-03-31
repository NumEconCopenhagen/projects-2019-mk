import pandas_datareader
from datetime import datetime
from pytrends.request import TrendReq  #imports pytrends for loading google trends data
pytrends = TrendReq(hl='en-US', tz=360)




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
            frequenicy for the inquired seachword 
    '''
    pytrends.build_payload(kw_list, cat=0, timeframe='2018-01-01 2018-12-31', geo='', gprop='')
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