# Modelproject

# The CAPM mode
Out modelproject creates a CAPM (capital asset pricing model) in which we use different firms stock returns. The essence of the CAPM is captured in our last figure (both the interactive and the non-interactive), which showcases the relationsship between different portfoilios, and how the return on the riskfree asset comes in to play, when deciding what portfolio to chose.

# Overview of the code 
The first part of our project creates an overview over the stocks and creates some variables for later use.

The monte carlo simulation is really the bread and butter of the project, it simulates a large amount of different asset porfolios 
(which essentially just means that we chose different weights of stock x,z,y when creating our "basket" of assets, aka the portfolio).
 
We add something called the sharpe ratio, which takes into consideration, that we cannot compare all the portfolios from a standpoint of "is one dominated by another" (Portfolio a is dominated by portfolio b, when the expected return of a<b and the risk (volatility) of a>=b. a is also dominated if exptected return a=b and the volatility of a>b). The sharpe ratio makes it possible for us to compare all non-dominated portfolio.
 
We add the capital marked line, which shows how a riskfree assets plays into our decision making.
