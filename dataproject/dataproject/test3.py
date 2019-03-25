#%%
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#%%
##start = dt.datetime(2015, 1, 1)
##end = dt.datetime.now()
##df = web.DataReader("TSLA", 'google', start, end)

df = pd.read_csv('TSLA', parse_dates=True, index_col=0)


df.reset_index(inplace=True)
df.set_index("date", inplace=True)
#%%
df['high'].plot()
plt.show()
#%%
df['100ma'] = df['close'].rolling(window=100,min_periods=0).mean()
plt.show()
#%%
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1

#%%
ax1.plot(df.index, df['close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['volume'])

plt.show()