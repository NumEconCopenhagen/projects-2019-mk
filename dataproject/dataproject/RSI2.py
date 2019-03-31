## pip install plotly       <-- install inorder to show the plot type
## pip install talib        <-- install to do RSI calculations
## pip install cufflinks    <-- Install to make offline interactive plots
#%%
import plotly.plotly as py
import plotly.graph_objs as go
import talib 
import cufflinks as cf
import pandas as pd
from datetime import datetime
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
## Making Offline interactive charts
init_notebook_mode(connected = False)
cf.go_offline()


import functions.prices

start = datetime(2019,1,1)
end = datetime(2019,3,31)
ticker = 'NVO'
