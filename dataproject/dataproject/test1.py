#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader
from datetime import datetime
%matplotlib inline


#%%
start = datetime(2018,1,1)
end = datetime(2018,12,31)
ticker = 'AMZN'

#%%
def prices(name, start=start, end=end):
    '''returns a dataframe with stock-information for a given company'''
    return pandas_datareader.iex.daily.IEXDailyReader(name, start, end).read()

#%%
df = prices(ticker,start,end)


df.head()
#%%
df['close'].plot(legend=True, figsize=(10, 5), \
title='Amazon', \
label='Closing Price')

#%%
plt.figure(figsize=(10,5))
top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)
bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
top.plot(df.index, df['close']) #CMT.index gives the dates
bottom.bar(df.index, df['volume']) 

#%%
# set the labels
top.axes.get_xaxis().set_visible(False)
top.set_title('CapitalMall Trust')
top.set_ylabel('Adj Closing Price')
bottom.set_ylabel('Volume')