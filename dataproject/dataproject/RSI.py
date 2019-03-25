## pip install plotly  <-- install inorder to show the plot type
#%%
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime
import pandas as pd
import pandas_datareader.data as web

#%%
Stock = pd.read_csv('TSLA', parse_dates=True, index_col=0)


Stock.reset_index(inplace=True)
Stock.set_index("date", inplace=True)
#%%½
Stock.columns = [col.replace('TSLA', '') for col in Stock.columns]
#%%
trace = go.Scatter(x=list(Stock.date),
                   y=list(Stock.high))
#%%
Stock.head(n=20)

#%%
data = [trace]
layout = dict(
    title='Time series with range slider and selectors',
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
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
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
py.iplot(fig)