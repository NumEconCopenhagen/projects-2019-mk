## pip install plotly       <-- install inorder to show the plot type
## pip install talib        <-- install to do RSI calculations
## pip install cufflinks    <-- Install to make offline interactive plots
#%%
import pandas_datareader
import plotly.plotly as py
import plotly.graph_objs as go
import talib 
import cufflinks as cf
import pandas as pd
from datetime import datetime
from pytrends.request import TrendReq  #imports pytrends for loading google trends data
pytrends = TrendReq(hl='en-US', tz=360)
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
## Making Offline interactive charts
init_notebook_mode(connected = False)
cf.go_offline()


#%%
#%%
def combine_data_frames(df1, df2):

        return df1.join(df2, how='outer')


#%%
start = datetime(2018,1,1)
end = datetime(2018,12,31)
ticker = 'NVDA'



ticker_search = searches(ticker)


ticker_search.head()


df = prices(ticker, start,end)
df.reset_index(inplace=True)


#%%
close = df['close'].values
#%%
rsi = talib.RSI(close, timeperiod = 14)


df["RSI"]= rsi
df["Overbought"] = 70
df["Oversold"] = 30
#%%
df.head(n=20)

combine_data_frames(df,ticker_search)




#%%
trace1 = go.Scatter(
    y=df['RSI'],
    x=df['date'],    
    name = "RSI",
    line = dict(color = '#7F7F7F'),
    )

#%%
trace2 = go.Scatter(
    y=df['Overbought'],
    x=df['date'],   
    name = "Overbought",
    line = dict(color = '#63c442'),
    hoverinfo='none'
    )
#%%
trace3 = go.Scatter(
    y=df['Oversold'],
    x=df['date'],   
    name = "Oversold",
    line = dict(color = '#705d65'),
    hoverinfo='none'
    )
#%%
trace4 = go.Scatter(
    y=df['close'],
    x=df['date'],   
    name = "Price",
    line = dict(color = '#2ed362'),
    )


#%%
data = [trace1,trace2,trace3,trace4]
#%%
layout = dict(
    title='Nvidia with RSI',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=12,
                     label = '1 year',
                     stepmode='backward'),
                dict(step='all')

            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)
#%%
fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Nvidia1")
