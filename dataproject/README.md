# Dataproject

Our project is titled "Does google searches show market movements?", and is about showing how stocks and google searches are related. the project displays a stock Tesla (TSLA) with the correspondig google searches - this is not an econometrical excersize by any means - but more so to showcase the use of python to illustrate how data can be compared, and made interactive.  
We also have a few extra graphs and figures, such as the SPX index against 10-year US bond prices, even though google searches and stock prices on one hand seem far from bond prices, we can work with them very similarily in python.
## Project
The movements can be seen from running [dataproject.ipynb](https://github.com/NumEconCopenhagen/projects-2019-mk/blob/master/dataproject/dataproject/Dataproject.ipynb)
### Data
The project loads two csv files:

1. 10 year bond Weekly.csv downloaded from [yahoo finance - 10 year Treasury](https://finance.yahoo.com/quote/%5ETNX/history?period1=1514761200&period2=1546210800&interval=1wk&filter=history&frequency=1wk)
2. SPX-weekly-2018.csv downloaded from [yahoo finance - S&P 500](https://finance.yahoo.com/quote/%5EGSPC/history?period1=1514761200&period2=1546210800&interval=1wk&filter=history&frequency=1wk)

## Dependencies
Apart from a standard Anaconda Python 3 installation the project requires the following installations:
```
pip install pytrends
pip install plotly
pip install cufflinks
pip install fix_yahoo_finance
```


