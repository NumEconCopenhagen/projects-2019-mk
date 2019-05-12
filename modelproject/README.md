# Modelproject

## Requirement
In order for you to get the same results as us, you need to download the following package though anaconda prompt or alike.
Needed package:
```
pip install fix_yahoo_finance
```

## The CAPM mode
Our modelproject creates the CAPM (capital asset pricing model) for a selected numbers of assets. The essence of the CAPM is captured in our last figure (both the interactive and the non-interactive), which showcases the relationsship between different portfolios, and how the return on the riskfree asset comes in to play, when finding the tangent portfolio.

### Overview of the code 
The first part of our project creates an overview over the assets and creates variables for later use.

The monte carlo simulation simulates a large amount of different combinations of asset in a porfolio.
(which essentially just means that we chose different weights of stock x,z,y when creating our "basket" of assets, aka the portfolio).
 
We add the risk adjusted return of invest, denoted as the sharpe ratio, which takes into consideration, that we cannot compare all the portfolios from a standpoint of "is one dominated by another" (Portfolio a is dominated by portfolio b, when the expected return of a<b and the risk (volatility) of a>=b. a is also dominated if exptected return a=b and the volatility of a>b). The sharpe ratio makes it possible for us to compare all non-dominated portfolio.
 
We add the capital marked line, which shows how a riskfree assets plays into our decision making.

